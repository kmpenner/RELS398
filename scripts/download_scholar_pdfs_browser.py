#!/usr/bin/env python3
"""RELS 398: Publisher-Aware Browser Fallback PDF Downloader via Chrome CDP

Downloads missing research papers via the authenticated Chrome browser session,
utilizing StFX Library Proxy (EZproxy) host-rewriting and publisher-specific
direct PDF resolution rules.
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote, urlsplit, urlunsplit
import requests
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

CDP_URL = "http://127.0.0.1:9222"
LIBRARY_PROXY_HOST = "libproxy.stfx.ca"
DOI_RE = re.compile(r'10\.\d{4,9}/[^\s&?#"\']+')


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
            doi = m.group(0).rstrip(".,)")
            if doi.endswith("/html") or doi.endswith("/pdf"):
                doi = doi.rsplit("/", 1)[0]
            return doi
    return None


def proxied(url: str, use_proxy: bool) -> str:
    if not use_proxy or not url:
        return url
    parts = urlsplit(url)
    host = parts.hostname or ""
    if not host or host.endswith(LIBRARY_PROXY_HOST) or "google.com" in host:
        return url
    rewritten = host.replace("-", "--").replace(".", "-") + "." + LIBRARY_PROXY_HOST
    if parts.port:
        rewritten = f"{rewritten}:{parts.port}"
    return urlunsplit((parts.scheme or "https", rewritten, parts.path, parts.query, parts.fragment))


def build_candidate_urls(r: dict, use_proxy: bool) -> list[str]:
    urls = []
    title_link = r.get("title_link") or ""
    pdf_link = r.get("pdf_link") or ""
    doi = extract_doi(pdf_link, title_link)

    # 1. Direct PDF link from metadata
    if pdf_link:
        urls.append(proxied(pdf_link, use_proxy))

    # 2. Publisher-specific direct PDF constructs via DOI
    if doi:
        if "springer.com" in title_link or "10.1007" in doi or "10.1140" in doi:
            urls.append(proxied(f"https://link.springer.com/content/pdf/{doi}.pdf", use_proxy))
        elif "wiley.com" in title_link or "10.1111" in doi:
            urls.append(proxied(f"https://onlinelibrary.wiley.com/doi/pdfdirect/{doi}", use_proxy))
        elif "tandfonline.com" in title_link or "10.1080" in doi or "10.4324" in doi:
            urls.append(proxied(f"https://www.tandfonline.com/doi/pdf/{doi}?download=true", use_proxy))
        elif "acm.org" in title_link or "10.1145" in doi:
            urls.append(proxied(f"https://dl.acm.org/doi/pdf/{doi}", use_proxy))
        elif "degruyter" in title_link or "10.1515" in doi:
            urls.append(proxied(f"https://www.degruyterbrill.com/document/doi/{doi}/pdf", use_proxy))
        elif "mdpi.com" in title_link or "10.3390" in doi:
            # MDPI direct PDF is typically /pdf on end of article link
            clean_link = title_link.rstrip("/")
            urls.append(f"{clean_link}/pdf")

    # 3. Landing page
    if title_link and "books.google.com" not in title_link:
        urls.append(proxied(title_link, use_proxy))

    return list(dict.fromkeys(urls))  # deduplicate preserving order


def try_download_one(page, url: str, dest: Path, timeout_ms: int = 25000) -> tuple[bool, str]:
    if not url:
        return False, "empty_url"

    resp = None
    # Pattern A: navigation triggers file download event
    try:
        with page.expect_download(timeout=8000) as dl_info:
            resp = page.goto(url, timeout=timeout_ms, wait_until="commit")
        download = dl_info.value
        download.save_as(str(dest))
        if dest.exists() and dest.stat().st_size > 1000:
            with open(dest, "rb") as f:
                if f.read(5).startswith(b"%PDF-"):
                    return True, "download_event_ok"
            dest.unlink(missing_ok=True)
            return False, "download_event_not_pdf"
    except PlaywrightTimeoutError:
        pass
    except Exception:
        pass

    # Pattern B: page settles on PDF content or PDF embed
    try:
        page.wait_for_timeout(3000)
        final_url = page.url
        content_type = ""
        try:
            content_type = (resp.headers or {}).get("content-type", "").lower() if resp else ""
        except Exception:
            pass

        looks_pdf = "pdf" in content_type or final_url.lower().split("?")[0].endswith(".pdf")
        if looks_pdf:
            api_resp = page.context.request.get(final_url, timeout=timeout_ms)
            body = api_resp.body()
            if body.startswith(b"%PDF-") and len(body) > 1000:
                dest.write_bytes(body)
                return True, f"direct_pdf_ok ({len(body)//1024} KB)"

        # Check for PDF embed/iframe/object
        pdf_embed = page.locator("embed[type='application/pdf'], iframe[src*='.pdf'], a[href*='.pdf'], a:has-text('Download PDF'), a:has-text('View PDF')").first
        if pdf_embed.count() > 0:
            pdf_href = pdf_embed.get_attribute("src") or pdf_embed.get_attribute("href")
            if pdf_href and (".pdf" in pdf_href or "download" in pdf_href):
                full_href = page.evaluate(f"new URL('{pdf_href}', window.location.href).href")
                try:
                    with page.expect_download(timeout=6000) as dl_info2:
                        page.goto(full_href, timeout=timeout_ms, wait_until="commit")
                    dl = dl_info2.value
                    dl.save_as(str(dest))
                    if dest.exists() and dest.stat().st_size > 1000:
                        return True, "embed_download_ok"
                except Exception:
                    api_resp2 = page.context.request.get(full_href, timeout=timeout_ms)
                    body2 = api_resp2.body()
                    if body2.startswith(b"%PDF-") and len(body2) > 1000:
                        dest.write_bytes(body2)
                        return True, "embed_fetched_ok"

    except Exception as ex:
        return False, f"browser_error: {ex}"

    return False, "no_pdf_resolved"


def process_topic_browser(json_file: Path, readings_dir: Path, page, use_proxy: bool):
    data = json.loads(json_file.read_text(encoding="utf-8"))
    qid = data["id"]
    topic_folder_name = data.get("topic") or f"Topic_{qid}"
    dest_dir = readings_dir / topic_folder_name
    dest_dir.mkdir(parents=True, exist_ok=True)

    manifest_file = dest_dir / "manifest.json"
    manifest = json.loads(manifest_file.read_text(encoding="utf-8")) if manifest_file.exists() else []
    manifest_by_idx = {m["index"]: m for m in manifest}

    results = data.get("results", [])
    print(f"\n=======================================================")
    print(f"Topic {qid}: {data['title']} (Browser + EZproxy Pass)")
    print(f"Target: {dest_dir}")
    print(f"=======================================================")

    for idx, r in enumerate(results, 1):
        title = r["title"]
        safe_title = sanitize_filename(title)
        filename = f"{idx:02d}_{safe_title}.pdf"
        dest_path = dest_dir / filename

        # Check if already present and valid
        if dest_path.exists() and dest_path.stat().st_size > 1000:
            continue

        existing_entry = manifest_by_idx.get(idx, {})
        if existing_entry.get("status") in ("cached", "downloaded"):
            continue

        print(f"\n[{idx}/{len(results)}] Resolving: {title[:75]}...")

        candidate_urls = build_candidate_urls(r, use_proxy)
        downloaded = False
        for target_url in candidate_urls:
            print(f"      Trying: {target_url[:80]}...")
            ok, reason = try_download_one(page, target_url, dest_path)
            if ok:
                size_kb = dest_path.stat().st_size // 1024
                print(f"      ✓ Acquired via Browser! ({size_kb} KB)")
                manifest_by_idx[idx] = {
                    "index": idx,
                    "title": title,
                    "status": "browser_downloaded",
                    "file": filename,
                    "source_url": target_url
                }
                downloaded = True
                break
            else:
                print(f"      ✗ {reason}")

        if not downloaded:
            print(f"      ⚠️ Could not resolve PDF in browser.")

        time.sleep(1.5)

    updated_manifest = [manifest_by_idx.get(i, {"index": i, "title": results[i-1]["title"], "status": "failed"}) for i in range(1, len(results) + 1)]
    manifest_file.write_text(json.dumps(updated_manifest, indent=2), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scholar-dir", default="raw/scholar_labs_results")
    ap.add_argument("--readings-dir", default="raw/readings")
    ap.add_argument("--topics", help="Comma-separated topic IDs to retry, e.g. '01,02,03'")
    ap.add_argument("--use-library-proxy", action="store_true", default=True)
    ap.add_argument("--cdp", default=CDP_URL)
    args = ap.parse_args()

    course_root = Path(__file__).resolve().parent.parent
    scholar_dir = course_root / args.scholar_dir
    readings_dir = course_root / args.readings_dir

    json_files = sorted(scholar_dir.glob("q[0-9]*.json"))
    if args.topics:
        selected_ids = {t.strip().zfill(2) for t in args.topics.split(",")}
        json_files = [f for f in json_files if f.stem.replace("q", "").zfill(2) in selected_ids]

    print(f"Connecting to Chrome over CDP at {args.cdp}...")
    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp(args.cdp)
        except Exception as e:
            sys.exit(f"Could not connect to CDP: {e}")

        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.new_page()

        for jf in json_files:
            process_topic_browser(jf, readings_dir, page, args.use_library_proxy)

        page.close()

    print("\nBrowser fallback download sweep complete.")


if __name__ == "__main__":
    main()
