#!/usr/bin/env python3
"""RELS 398: Browser-based Fallback PDF Downloader via Chrome CDP

Downloads research papers that block headless requests (MDPI, Springer,
Digital Commons, PMC interstitials) using the authenticated Chrome browser session.
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote, urlsplit, urlunsplit
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

CDP_URL = "http://127.0.0.1:9222"
LIBRARY_PROXY_HOST = "libproxy.stfx.ca"


def sanitize_filename(name: str, max_len: int = 80) -> str:
    s = re.sub(r'[\\/*?:"<>|]', "", name)
    s = re.sub(r"\s+", "_", s).strip("_")
    return s[:max_len]


def proxied(url: str, use_proxy: bool) -> str:
    if not use_proxy or not url:
        return url
    parts = urlsplit(url)
    host = (parts.hostname or "")
    if not host or host.endswith(LIBRARY_PROXY_HOST):
        return url
    rewritten = host.replace("-", "--").replace(".", "-") + "." + LIBRARY_PROXY_HOST
    if parts.port:
        rewritten = f"{rewritten}:{parts.port}"
    return urlunsplit((parts.scheme or "https", rewritten, parts.path, parts.query, parts.fragment))


def try_download_one(page, url: str, dest: Path, timeout_ms: int = 25000) -> tuple[bool, str]:
    if not url:
        return False, "empty_url"

    # Pattern A: navigation triggers download event
    try:
        with page.expect_download(timeout=8000) as download_info:
            try:
                page.goto(url, timeout=timeout_ms, wait_until="domcontentloaded")
            except PlaywrightTimeoutError:
                pass
        download = download_info.value
        download.save_as(str(dest))
        if dest.exists() and dest.stat().st_size > 1000:
            with open(dest, "rb") as f:
                if f.read(5).startswith(b"%PDF-"):
                    return True, "download_event_ok"
            dest.unlink(missing_ok=True)
            return False, "download_event_not_pdf"
    except Exception:
        pass

    # Pattern B: page loads or navigates to PDF URL / PDF embed
    try:
        page.wait_for_timeout(3000)
        final_url = page.url
        
        # Check if browser navigated to a .pdf URL directly
        if final_url.lower().endswith(".pdf") or "pdf" in final_url.lower():
            resp = page.request.get(final_url, timeout=timeout_ms)
            if resp.status == 200:
                body = resp.body()
                if body.startswith(b"%PDF-") and len(body) > 1000:
                    dest.write_bytes(body)
                    return True, "direct_pdf_ok"

        # Check for iframe or embed pointing to PDF
        pdf_embed = page.locator("embed[type='application/pdf'], iframe[src*='.pdf'], a[href*='.pdf']").first
        if pdf_embed.count() > 0:
            pdf_href = pdf_embed.get_attribute("src") or pdf_embed.get_attribute("href")
            if pdf_href:
                resp = page.request.get(pdf_href, timeout=timeout_ms)
                if resp.status == 200:
                    body = resp.body()
                    if body.startswith(b"%PDF-") and len(body) > 1000:
                        dest.write_bytes(body)
                        return True, "embed_pdf_ok"

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
    print(f"Topic {qid}: {data['title']} (Browser Pass)")
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

        print(f"\n[{idx}/{len(results)}] Retrying: {title[:75]}...")

        candidate_urls = []
        if r.get("pdf_link"):
            candidate_urls.append(r["pdf_link"])
        if r.get("title_link"):
            candidate_urls.append(r["title_link"])

        downloaded = False
        for u in candidate_urls:
            target_url = proxied(u, use_proxy)
            print(f"      Navigating to: {target_url[:80]}...")
            ok, reason = try_download_one(page, target_url, dest_path)
            if ok:
                size_kb = dest_path.stat().st_size // 1024
                print(f"      ✓ Browser Acquired! ({size_kb} KB)")
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
            print(f"      ⚠️ Still unacquired via browser.")

        time.sleep(1.5)

    updated_manifest = [manifest_by_idx.get(i, {"index": i, "title": results[i-1]["title"], "status": "failed"}) for i in range(1, len(results) + 1)]
    manifest_file.write_text(json.dumps(updated_manifest, indent=2), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scholar-dir", default="raw/scholar_labs_results")
    ap.add_argument("--readings-dir", default="raw/readings")
    ap.add_argument("--topics", help="Comma-separated topic IDs to retry, e.g. '03,08,10'")
    ap.add_argument("--use-library-proxy", action="store_true")
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
