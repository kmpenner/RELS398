#!/usr/bin/env python3
"""RELS 398: Single Topic Gemini Deep Research Runner

Usage:
    ./scripts/run_gemini_deep_research.py --topic 1
    ./scripts/run_gemini_deep_research.py --topic 8
"""
import argparse
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deep_research import connect, run_topic, CDP_URL
from topic_map import ROOT


def main():
    ap = argparse.ArgumentParser(description="Run Gemini Deep Research for a single topic in RELS 398.")
    ap.add_argument("--topic", type=int, required=True, help="Topic number (1-13)")
    ap.add_argument("--prompts", default=str(ROOT / "src/RESEARCH_PROMPTS.md"), help="Path to RESEARCH_PROMPTS.md")
    ap.add_argument("--cdp", default=CDP_URL, help="Chrome CDP URL")
    ap.add_argument("--timeout", type=int, default=2400, help="Per-topic timeout in seconds")
    ap.add_argument("--allow-unattached", action="store_true", help="Run even if no PDFs downloaded")
    args = ap.parse_args()

    with sync_playwright() as p:
        page = connect(p, args.cdp)
        page.set_viewport_size({"width": 1400, "height": 1000})
        try:
            ok = run_topic(
                page, args.topic,
                prompts_file=Path(args.prompts),
                timeout=args.timeout,
                allow_unattached=args.allow_unattached
            )
            sys.exit(0 if ok else 1)
        finally:
            page.close()


if __name__ == "__main__":
    main()
