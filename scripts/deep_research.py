#!/usr/bin/env python3
"""RELS 398: Gemini Deep Research Automation

Orchestrates Stage 2 deep research reports for RELS 398 via Chrome CDP:
- Connects to active, authenticated Chrome profile
- Selects 3.1 Pro / Advanced model & enables Deep Research mode
- Attaches downloaded literature PDFs from raw/readings/Topic_NN/
- Submits structured Stage 2 research prompt
- Approves the research plan ("Start research")
- Waits for synthesis to complete and stable text
- Extracts DOM content, parses inline citation markers, generates APA reference section
- Writes final report to src/research_reports/Topic_NN_<Name>_Deep_Research_Report.md
"""
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gemini_ui import (
    ModelSelectionError, UsageLimitError, ensure_model_and_deep_research,
    looks_like_research_plan, start_deep_research, wait_for_research_complete,
)
from topic_map import ROOT, extract_prompt_for_topic, lit_dir, report_path, TOPIC_MAP
from gemini_citations import (
    RESPONSE_ROOT_SELECTORS, extract_and_write, parse_readings_manifest,
)

CDP_URL = "http://127.0.0.1:9222"
MIN_REPORT_CHARS = 3000


def connect(playwright, cdp_url: str = CDP_URL):
    browser = playwright.chromium.connect_over_cdp(cdp_url)
    return browser.contexts[0].new_page()


def attach_pdfs(page, pdf_files) -> bool:
    """Attach PDFs via the Upload & tools menu."""
    upload_btn = page.locator('button[aria-label="Upload & tools"]').first
    if not upload_btn.count():
        print("       ⚠️ 'Upload & tools' button not found; sending prompt unattached.")
        return False
    upload_btn.click()
    page.wait_for_timeout(1000)
    with page.expect_file_chooser(timeout=10000) as fc:
        page.locator('button:has-text("Upload files"), [aria-label*="Upload files"]').first.click()
    fc.value.set_files([str(p.resolve()) for p in pdf_files])
    print(f"       -> Uploading {len(pdf_files)} PDF(s)...", flush=True)
    page.wait_for_timeout(8000)  # let attachment chips finish processing
    return True


def submit_prompt(page, prompt: str) -> None:
    box = page.locator('div[aria-label="Enter a prompt for Gemini"]').first
    if not box.count():
        box = page.locator("rich-textarea div, textarea").first
    box.click()
    box.fill(prompt)
    page.wait_for_timeout(800)
    send = page.locator('button[aria-label*="Send"], button[aria-label*="Submit"], button.send-button').first
    if send.count() and send.is_visible():
        send.click()
    else:
        page.keyboard.press("Enter")


def run_topic(page, topic_num: int, prompts_file: Path = None, timeout: int = 2400,
              allow_unattached: bool = False, hover_citations: bool = True,
              debug_dump: bool = True) -> bool:
    """Run one topic end to end."""
    out_file = report_path(topic_num)
    topic_dir = lit_dir(topic_num)
    topic_name = TOPIC_MAP.get(topic_num, f"Topic_{topic_num:02d}")
    out_file.parent.mkdir(parents=True, exist_ok=True)

    prompt = extract_prompt_for_topic(topic_num, prompts_file)
    if not prompt:
        print(f"       ⚠️ No Stage 2 prompt found for Topic {topic_num}.")
        return False

    pdf_files = sorted(topic_dir.glob("*.pdf"))
    print(f"\n[Topic {topic_num:02d}] {topic_name}: {len(pdf_files)} PDF(s) to attach.")
    if not pdf_files and not allow_unattached:
        print("       ⛔ 0 PDFs -- skipping rather than running unattached Deep Research.")
        return False

    page.goto("https://gemini.google.com/app", timeout=45000)
    page.wait_for_timeout(3000)

    resolved_model = ensure_model_and_deep_research(page)  # UsageLimitError propagates
    print(f"       ✓ {resolved_model} + Deep Research confirmed.")

    if pdf_files:
        try:
            attach_pdfs(page, pdf_files)
        except Exception as ex:
            print(f"       ⚠️ Attachment failed ({ex}); continuing unattached.")

    submit_prompt(page, prompt)
    print("       -> Prompt submitted. Waiting for research plan...")
    start_deep_research(page, timeout_s=180, verbose=False)

    print(f"       -> Deep Research running (timeout {timeout}s)...", flush=True)
    report_text = wait_for_research_complete(
        page, RESPONSE_ROOT_SELECTORS, timeout_s=timeout, verbose=False)

    if len(report_text) < MIN_REPORT_CHARS:
        print(f"       ⚠️ Only {len(report_text)} chars captured; leaving existing report untouched.")
        return False
    if looks_like_research_plan(report_text):
        print("       ⛔ Captured research PLAN instead of full report; leaving existing report untouched.")
        return False

    stats = extract_and_write(
        page, out_file,
        title=f"Topic {topic_num:02d} ({topic_name}): Academic Deep Research Report",
        meta={"Model": f"{resolved_model} (Deep Research)",
              "Attachments": f"{len(pdf_files)} PDF(s)"},
        readings=parse_readings_manifest(topic_dir / "manifest.json"),
        hover=hover_citations, debug_dump=debug_dump,
        fallback_text=report_text, verbose=False)
    print(f"       ✅ Successfully saved: {stats['chars']} chars, {stats['sources']} source(s) -> {out_file.name}")
    return True
