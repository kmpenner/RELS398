#!/usr/bin/env python3
"""RELS 398: Scholar Literature PDF Downloader

Acquires peer-reviewed PDFs discovered in raw/scholar_labs_results/q*.json
and saves them into raw/readings/Topic_NN_<TopicName>/ for Phase B synthesis.
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin
import requests

UNPAYWALL_EMAIL = "rels-pipeline@stfx-noreply.invalid"
DOI_RE = re.compile(r'10\.\d{4,9}/[^\s&?#"\']+')

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml,application/pdf;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def sanitize_filename(name: str, max_len: int = 80) -> str:
    s = re.sub(r'[\\/*?:"<>|]', "", name)
    s = re.sub(r"\s+", "_", s).strip("_")
    return s[:max_len]


def extract_doi(*urls: str) -> str | None:
    for url in urls:
        if not url:
            continue
        m = DOI_RE.search(url)
        if m:
            return m.group(0).rstrip(".,)")
    return None


def find_doi_crossref(title: str, session: requests.Session) -> str | None:
    try:
        resp = session.get(
            "https://api.crossref.org/works",
            params={"query.bibliographic": title, "rows": 1},
            headers={"User-Agent": f"RELS398Pipeline/1.0 (mailto:{UNPAYWALL_EMAIL})"},
            timeout=10,
        )
        if resp.status_code == 200:
            items = resp.json().get("message", {}).get("items", [])
            if items:
                return items[0].get("DOI")
    except Exception:
        pass
    return None


def unpaywall_candidates(doi: str, session: requests.Session) -> list[str]:
    try:
        resp = session.get(
            f"https://api.unpaywall.org/v2/{doi}",
            params={"email": UNPAYWALL_EMAIL},
            timeout=15,
        )
        if resp.status_code != 200:
            return []
        data = resp.json()
    except Exception:
        return []

    if not data.get("is_oa"):
        return []

    urls = []
    locations = [data.get("best_oa_location")] + (data.get("oa_locations") or [])
    for loc in locations:
        if not loc:
            continue
        pdf_url = loc.get("url_for_pdf")
        if pdf_url and pdf_url not in urls:
            urls.append(pdf_url)
    return urls


def scrape_landing_page_for_pdf_link(landing_url: str, session: requests.Session) -> str | None:
    try:
        resp = session.get(landing_url, headers=HEADERS, timeout=15)
        if resp.status_code != 200 or "html" not in resp.headers.get("content-type", "").lower():
            return None
        html = resp.text
    except Exception:
        return None

    m = re.search(r'href=["\']([^"\']*viewcontent\.cgi\?[^"\']*)["\']', html, re.I)
    if not m:
        m = re.search(r'href=["\']([^"\']+\.pdf(?:\?[^"\']*)?)["\']', html, re.I)
    if not m:
        return None
    href = m.group(1).replace("&amp;", "&")
    return urljoin(landing_url, href)


def download_pdf(url: str, dest_path: Path, session: requests.Session) -> tuple[bool, str]:
    try:
        resp = session.get(url, headers=HEADERS, timeout=25, allow_redirects=True, stream=True)
        resp.raw.decode_content = True
    except Exception as ex:
        return False, str(ex)

    if resp.status_code != 200:
        return False, f"HTTP {resp.status_code}"

    content_type = resp.headers.get("content-type", "").lower()
    try:
        first_chunk = resp.raw.read(1024)
    except Exception as ex:
        return False, f"read error: {ex}"

    if b"%PDF-" not in first_chunk and "pdf" not in content_type:
        snippet = first_chunk[:200].decode("utf-8", errors="replace").replace("\n", " ")
        return False, f"not a PDF (content-type={content_type}; body_starts='{snippet}')"

    try:
        with open(dest_path, "wb") as f:
            f.write(first_chunk)
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
    except Exception as ex:
        dest_path.unlink(missing_ok=True)
        return False, f"write error: {ex}"

    if dest_path.stat().st_size <= 1000:
        dest_path.unlink(missing_ok=True)
        return False, "file too small (<= 1000 bytes)"

    return True, "ok"


def process_topic(json_file: Path, readings_dir: Path, session: requests.Session):
    data = json.loads(json_file.read_text(encoding="utf-8"))
    qid = data["id"]
    topic_folder_name = data.get("topic") or f"Topic_{qid}"
    dest_dir = readings_dir / topic_folder_name
    dest_dir.mkdir(parents=True, exist_ok=True)

    results = data.get("results", [])
    print(f"\n=======================================================")
    print(f"Topic {qid}: {data['title']}")
    print(f"Target: {dest_dir}")
    print(f"Discovered items: {len(results)}")
    print(f"=======================================================")

    manifest = []
    success_count = 0

    for idx, r in enumerate(results, 1):
        title = r["title"]
        safe_title = sanitize_filename(title)
        filename = f"{idx:02d}_{safe_title}.pdf"
        dest_path = dest_dir / filename

        print(f"\n[{idx}/{len(results)}] {title[:80]}...")

        # 1. Existing PDF check
        if dest_path.exists() and dest_path.stat().st_size > 1000:
            print(f"      ✓ Already downloaded ({dest_path.stat().st_size // 1024} KB)")
            manifest.append({"index": idx, "title": title, "status": "cached", "file": filename})
            success_count += 1
            continue

        # 2. Collect candidate URLs
        candidate_urls = []
        if r.get("pdf_link"):
            candidate_urls.append(r["pdf_link"])

        # DOI from URL or Crossref
        doi = extract_doi(r.get("title_link"), r.get("pdf_link"))
        if not doi and not candidate_urls:
            doi = find_doi_crossref(title, session)

        if doi:
            oa_urls = unpaywall_candidates(doi, session)
            candidate_urls.extend(oa_urls)

        if r.get("title_link") and not candidate_urls:
            scraped_url = scrape_landing_page_for_pdf_link(r["title_link"], session)
            if scraped_url:
                candidate_urls.append(scraped_url)

        # 3. Attempt downloads
        downloaded = False
        last_reason = "no OA candidate URLs found"

        for cand in candidate_urls:
            print(f"      Trying: {cand[:80]}...")
            ok, reason = download_pdf(cand, dest_path, session)
            if ok:
                size_kb = dest_path.stat().st_size // 1024
                print(f"      ✓ Success! Saved ({size_kb} KB)")
                manifest.append({"index": idx, "title": title, "status": "downloaded", "file": filename, "source_url": cand, "doi": doi})
                downloaded = True
                success_count += 1
                break
            else:
                last_reason = reason
                print(f"      ✗ Failed: {reason}")

        if not downloaded:
            print(f"      ⚠️ Could not acquire OA PDF ({last_reason})")
            manifest.append({"index": idx, "title": title, "status": "failed", "reason": last_reason, "doi": doi, "title_link": r.get("title_link")})

        time.sleep(1.0)

    (dest_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"\nTopic {qid} complete: {success_count}/{len(results)} PDFs available in {dest_dir.name}/")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scholar-dir", default="raw/scholar_labs_results")
    ap.add_argument("--readings-dir", default="raw/readings")
    ap.add_argument("--topics", help="Comma-separated topic IDs to download, e.g. '01,02'")
    args = ap.parse_args()

    course_root = Path(__file__).resolve().parent.parent
    scholar_dir = course_root / args.scholar_dir
    readings_dir = course_root / args.readings_dir
    readings_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()

    json_files = sorted(scholar_dir.glob("q[0-9]*.json"))
    if args.topics:
        selected_ids = {t.strip().zfill(2) for t in args.topics.split(",")}
        json_files = [f for f in json_files if f.stem.replace("q", "").zfill(2) in selected_ids]

    if not json_files:
        print("No scholar results JSON files found matching criteria.")
        return

    for jf in json_files:
        process_topic(jf, readings_dir, session)


if __name__ == "__main__":
    main()
