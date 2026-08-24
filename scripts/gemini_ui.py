#!/usr/bin/env python3
"""Shared Gemini web-UI driving: pick the model, enable Deep Research.

This lived as an identical copy inside both run_gemini_deep_research.py and
batch_gemini_deep_research.py; it is factored out here so a Gemini UI change
only has to be fixed once.
"""
import re
import time

TARGET_MODEL = "3.1 Pro"   # must match the label Gemini's model picker shows


class UsageLimitError(RuntimeError):
    """The account cannot use the target model right now (quota exhausted).

    Separate from ModelSelectionError because it is not a selector problem and
    retrying other lessons is pointless -- a batch should stop immediately
    rather than fail once per lesson."""


class ModelSelectionError(RuntimeError):
    """Raised when we can't positively confirm the target model + Deep Research
    are active, so a run never silently proceeds on a lightweight fallback
    model and saves a report with no indication anything was wrong."""


# The toolbar button that opens the model picker. Its aria-label currently reads
# "Open mode picker, currently Pro".
_MODEL_BTN_SEL = (
    'button[aria-label*="mode picker" i], '
    'button[aria-label*="model" i], '
    '[data-test-id="bard-mode-menu-button"], '
    'button:has-text("Flash"), button:has-text("Pro")'
)

_MENU_ITEM_SEL = '[role="menuitemradio"], [role="menuitem"], [role="option"]'


def _open_model_menu(page, timeout: int):
    btn = page.locator(_MODEL_BTN_SEL).first
    btn.wait_for(state="visible", timeout=timeout)
    btn.click()
    page.wait_for_timeout(700)
    return btn


def _find_model_item(page, target_model: str):
    item = page.get_by_role("menuitemradio", name=re.compile(re.escape(target_model), re.I))
    if item.count() == 0:
        item = page.locator(f'{_MENU_ITEM_SEL}').filter(has_text=re.compile(re.escape(target_model), re.I))
    return item


def _item_is_selected(item) -> bool:
    """Is this menu entry the active model?

    Gemini marks the active entry with a `selected` CSS class, NOT with
    aria-checked (which stays null on every entry). The toolbar button is also
    useless for verification: with "3.1 Pro" active it just reads "Pro", so
    asserting the button contains the full target string always fails.
    """
    if (item.get_attribute("aria-checked") or "").lower() == "true":
        return True
    cls = item.get_attribute("class") or ""
    if re.search(r"\bselected\b", cls):
        return True
    # Fall back to a selected descendant (the checkmark element carries it too).
    try:
        return item.locator('.selected, [aria-checked="true"]').count() > 0
    except Exception:
        return False


# Once Deep Research is on, Gemini shows a "Deep research" chip in the composer
# toolbar. That chip is the only durable signal: clicking the menu toggle closes
# the menu and detaches the element, so re-reading its aria-checked always fails.
_TOOLBAR_SEL = '[class*="toolbox-drawer"] button, input-container button'


def deep_research_active(page) -> bool:
    """Chip check. NOTE: the composer toolbar collapses its chips on a narrow
    viewport, so a False here is not proof the mode is off -- always confirm
    with _read_dr_toggle(), which reads the menu itself."""
    try:
        chip = page.locator(_TOOLBAR_SEL).filter(has_text=re.compile("deep research", re.I))
        return chip.count() > 0
    except Exception:
        return False


def _open_tools_menu(page):
    tools_btn = page.locator('button[aria-label="Upload & tools"]').first
    if tools_btn.count() == 0:
        tools_btn = page.locator('button[aria-label*="tools" i]').first
    tools_btn.click(timeout=8000)
    page.wait_for_timeout(1200)


def _read_dr_toggle(page):
    """Open the tools menu and return (is_on, toggle_locator). Leaves the menu
    open so the caller can click the toggle. Reading aria-checked off the menu
    entry is viewport-independent, unlike the composer chip."""
    _open_tools_menu(page)
    pane = page.locator(".cdk-overlay-pane").last
    item = pane.get_by_role("menuitemcheckbox", name=re.compile("deep research", re.I))
    if item.count() == 0:
        item = page.locator('[role="menuitemcheckbox"]:has-text("Deep research")')
    item.first.wait_for(state="visible", timeout=6000)
    state = (item.first.get_attribute("aria-checked", timeout=4000) or "").lower() == "true"
    return state, item.first


def ensure_model_and_deep_research(page, target_model: str = TARGET_MODEL,
                                   timeout: int = 15000) -> str:
    """Select `target_model` and enable Deep Research, verifying each step by
    reading the UI back. Returns the resolved model label."""
    # Gemini's composer collapses its tool chips on a narrow viewport, which
    # both hides state we verify against and changes the menu layout.
    try:
        page.set_viewport_size({"width": 1400, "height": 1000})
    except Exception:
        pass
    # 1-2. Open the picker and click the target entry.
    _open_model_menu(page, timeout)
    option = _find_model_item(page, target_model)
    if option.count() == 0:
        visible_items = page.locator(_MENU_ITEM_SEL).all_inner_texts()
        page.keyboard.press("Escape")
        raise ModelSelectionError(
            f"Could not find model option '{target_model}' in the picker. "
            f"Visible menu items were: {visible_items!r}"
        )
    full_text = (option.first.inner_text() or "").strip()
    label = full_text.split("\n")[0]

    # A model the account can't currently use is rendered disabled, with the
    # reset time in its own label ("3.1 Pro / Limit resets Aug 21, 1:58 AM").
    # Clicking it just burns the 30s Playwright timeout and surfaces a generic
    # "Locator.click: Timeout ... element is not enabled", which looks like a
    # selector bug rather than an exhausted quota -- so say what it really is.
    if (option.first.get_attribute("aria-disabled") or "").lower() == "true":
        detail = " ".join(full_text.split("\n")[1:]).strip()
        page.keyboard.press("Escape")
        raise UsageLimitError(
            f"Model '{target_model}' is disabled in the picker -- the account's "
            f"usage limit is reached. {detail or 'No reset time shown.'} "
            "Re-run after the limit resets."
        )

    option.first.click()
    page.wait_for_timeout(1000)

    # 3. Verify by re-opening the picker and checking which entry is marked
    #    selected -- don't trust the click, and don't read the toolbar button,
    #    which shows only the short name ("Pro").
    _open_model_menu(page, timeout)
    option = _find_model_item(page, target_model)
    ok = option.count() > 0 and _item_is_selected(option.first)
    if not ok:
        states = []
        items = page.locator(_MENU_ITEM_SEL)
        for i in range(items.count()):
            it = items.nth(i)
            states.append(((it.inner_text() or "").split("\n")[0], it.get_attribute("class")))
        page.keyboard.press("Escape")
        raise ModelSelectionError(
            f"Model picker did not switch to '{target_model}'. Menu entries and "
            f"their classes were: {states!r}"
        )
    page.keyboard.press("Escape")
    page.wait_for_timeout(400)

    # 4. Explicitly enable Deep Research (don't assume it's already on).
    if deep_research_active(page):
        return label or target_model

    try:
        is_on, toggle = _read_dr_toggle(page)
    except Exception as ex:
        page.keyboard.press("Escape")
        raise ModelSelectionError(f"Could not read the 'Deep research' toggle: {ex}")

    if is_on:
        page.keyboard.press("Escape")
        return label or target_model

    # Clicking closes the menu and detaches the element, so re-open it to verify
    # rather than re-reading the clicked locator.
    toggle.click(timeout=6000)
    page.wait_for_timeout(1500)
    if deep_research_active(page):
        return label or target_model
    try:
        is_on, _ = _read_dr_toggle(page)
    except Exception as ex:
        page.keyboard.press("Escape")
        raise ModelSelectionError(f"Could not confirm the 'Deep research' toggle: {ex}")
    page.keyboard.press("Escape")
    if not is_on:
        raise ModelSelectionError(
            "Clicked the 'Deep research' toggle but the menu still reports it off."
        )
    return label or target_model


# ---------------------------------------------------------------------------
# Deep Research run control
# ---------------------------------------------------------------------------

# Gemini answers a Deep Research prompt with a *plan* first ("Here's the plan
# I've put together... Edit plan | Start research") and only researches after
# you confirm. The original pipeline submitted the prompt and then waited for
# the streaming indicator to stop, which happens as soon as the plan finishes
# rendering -- so it saved the plan as the report and never ran the research.

_START_RESEARCH_RE = re.compile(r"start research", re.I)


def _start_research_button(page):
    btn = page.get_by_role("button", name=_START_RESEARCH_RE)
    if btn.count() == 0:
        btn = page.locator('button:has-text("Start research")')
    return btn


def start_deep_research(page, timeout_s: int = 120, verbose: bool = True) -> bool:
    """Wait for the research plan and click 'Start research'. Returns True if
    clicked, False if no such button ever appeared (some runs start on their
    own; the caller can proceed either way)."""
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        btn = _start_research_button(page)
        try:
            if btn.count() and btn.first.is_visible(timeout=1500):
                btn.first.click(timeout=6000)
                if verbose:
                    print("   ✓ Research plan confirmed ('Start research' clicked).")
                page.wait_for_timeout(3000)
                return True
        except Exception:
            pass
        time.sleep(3)
    if verbose:
        print("   ⚠️ No 'Start research' button appeared; assuming research auto-started.")
    return False


# A finished Deep Research report always ends with its source list, and its
# inline markers only appear once Gemini has attached citations. Both are
# absent while the report is still being composed, which makes them a far
# better "done" signal than text length alone.
_CITATION_PROBE = """() => {
  const roots = document.querySelectorAll(
    'deep-research-immersive-panel, extended-response-panel, message-content');
  let sources = 0, markers = 0;
  roots.forEach((r) => {
    sources += r.querySelectorAll('a[data-test-id="browse-web-item-link"], browse-item a[href]').length;
    markers += r.querySelectorAll('[data-turn-source-index], source-footnote, sources-carousel-inline').length;
  });
  return { sources, markers };
}"""


def citation_state(page) -> dict:
    try:
        return page.evaluate(_CITATION_PROBE) or {"sources": 0, "markers": 0}
    except Exception:
        return {"sources": 0, "markers": 0}


def _response_text(page, root_selectors) -> str:
    """Longest text across the candidate containers.

    Taking the first selector that merely *exists* is wrong: an empty
    extended-response-panel can be present while the real report lives in
    deep-research-immersive-panel, which would stall completion detection
    forever on an empty string."""
    best = ""
    for sel in root_selectors:
        loc = page.locator(sel)
        try:
            if not loc.count():
                continue
            text = (loc.last.inner_text() or "").strip()
            if len(text) > len(best):
                best = text
        except Exception:
            continue
    return best


def wait_for_research_complete(page, root_selectors, timeout_s: int = 1800,
                               min_chars: int = 3000, poll_s: int = 15,
                               verbose: bool = True) -> str:
    """Block until the Deep Research report is finished.

    Completion requires all of: no 'Start research' button pending, no stop /
    streaming indicator, at least `min_chars` of text, and the text length
    unchanged across two consecutive polls (the report streams in, so a single
    length check can catch it mid-write)."""
    start = time.time()
    last_len = -1
    stable = 0
    STABLE_POLLS = 4     # ~60s unchanged; Deep Research pauses mid-write, and
                         # 2 polls was short enough to mistake a pause for done
    while time.time() - start < timeout_s:
        # NOTE: do NOT look for / click "Start research" here. The plan message
        # stays in the transcript with its button still visible even after the
        # research has finished, so re-clicking it loops forever and the loop
        # never evaluates completion. The plan is confirmed once, up front, by
        # start_deep_research().
        streaming = False
        try:
            stop_btn = page.locator('button[aria-label*="Stop" i]')
            streaming = stop_btn.count() > 0 and stop_btn.first.is_visible(timeout=1000)
        except Exception:
            streaming = False

        text = _response_text(page, root_selectors)
        cites = citation_state(page)
        long_enough = len(text) >= min_chars
        cited = cites["sources"] > 0 and cites["markers"] > 0

        if not streaming and long_enough:
            if len(text) == last_len:
                stable += 1
            else:
                stable = 0
            # Require the citations to have landed too -- capturing a report
            # before Gemini attaches them yields 0 references from a run that
            # actually cited 30+ sources.
            if stable >= STABLE_POLLS and cited:
                if verbose:
                    print(f"   ✓ Research complete ({len(text)} chars, "
                          f"{cites['sources']} sources, {cites['markers']} markers, "
                          f"{int(time.time() - start)}s).")
                return text
        else:
            stable = 0
        last_len = len(text)
        if verbose:
            print(f"   Researching... ({int(time.time() - start)}s, {len(text)} chars, "
                  f"sources={cites['sources']}, stable={stable}"
                  f"{', streaming' if streaming else ''})")
        time.sleep(poll_s)

    if verbose:
        print(f"   ⚠️ Timed out after {timeout_s}s.")
    return _response_text(page, root_selectors)


# ---------------------------------------------------------------------------
# Output sanity
# ---------------------------------------------------------------------------

# Deep Research answers with a plan before it researches. If the plan is ever
# captured as the report (as happened before start_deep_research() existed),
# it is far better to fail loudly than to overwrite a real report with it.
_PLAN_MARKERS = ("start research", "research websites", "edit plan",
                 "here's the plan", "here is the plan")


def looks_like_research_plan(text: str) -> bool:
    low = (text or "").lower()
    hits = sum(1 for m in _PLAN_MARKERS if m in low)
    if hits >= 2:
        return True
    # A short response carrying any plan marker is a plan, not a report.
    return hits >= 1 and len(low) < 6000
