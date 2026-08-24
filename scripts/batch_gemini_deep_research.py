#!/usr/bin/env python3
"""RELS 398: Batch Gemini Deep Research Runner

Runs multiple topics in sequence, checking quota, attaching PDFs, and pausing
between runs.

Usage:
    ./scripts/batch_gemini_deep_research.py --topics 1,2,3
    ./scripts/batch_gemini_deep_research.py --start 1 --end 13
    ./scripts/batch_gemini_deep_research.py --topics 1 --force
"""
import argparse
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gemini_ui import UsageLimitError
from deep_research import connect, run_topic, CDP_URL
from topic_map import ROOT, report_path, TOPIC_MAP


def main():
    ap = argparse.ArgumentParser(description="Run Gemini Deep Research across multiple topics for RELS 398.")
    ap.add_argument("--topics", help="Comma-separated topic numbers, e.g. 1,2,3")
    ap.add_argument("--start", type=int, default=1, help="Start topic number (1-13)")
    ap.add_argument("--end", type=int, default=13, help="End topic number (1-13)")
    ap.add_argument("--force", action="store_true", help="Re-run even if report already exists")
    ap.add_argument("--prompts", default=str(ROOT / "src/RESEARCH_PROMPTS.md"))
    ap.add_argument("--cdp", default=CDP_URL)
    ap.add_argument("--timeout", type=int, default=2400)
    ap.add_argument("--allow-unattached", action="store_true")
    args = ap.parse_args()

    if args.topics:
        topics_to_run = [int(x.strip()) for x in args.topics.split(",")]
    else:
        topics_to_run = list(range(args.start, args.end + 1))

    print(f"RELS 398 Batch Deep Research plan: Topics {topics_to_run}")
    prompts_file = Path(args.prompts)

    with sync_playwright() as p:
        page = connect(p, args.cdp)
        page.set_viewport_size({"width": 1400, "height": 1000})

        for t in topics_to_run:
            dest = report_path(t)
            if dest.exists() and dest.stat().st_size > 3000 and not args.force:
                print(f"\n[Topic {t:02d}] Report already exists at {dest.name} ({dest.stat().st_size // 1024} KB). Skipping (use --force to overwrite).")
                continue

            try:
                ok = run_topic(
                    page, t,
                    prompts_file=prompts_file,
                    timeout=args.timeout,
                    allow_unattached=args.allow_unattached
                )
                if not ok:
                    print(f"[Topic {t:02d}] Run was not successful.")
            except UsageLimitError as ule:
                print(f"\n⛔ Quota/Usage limit reached: {ule}")
                print("Stopping batch run. Resume after the reset time.")
                break
            except Exception as ex:
                print(f"\n⚠️ Unexpected error on Topic {t:02d}: {ex}")

            time.sleep(5.0)

        page.close()

    print("\nBatch run finished.")


if __name__ == "__main__":
    main()
