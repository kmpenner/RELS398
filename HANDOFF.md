# RELS 398 — Session Handoff

**Date:** 2026-08-27
**Repo:** `~/projects/RELS/398` (remote `https://github.com/kmpenner/RELS398.git`)
**HEAD at handoff:** `2fff957`
**Read first:** `~/projects/RELS/shared/LESSON_PIPELINE.md` — the single end-to-end
procedure. This document records where 398 sits inside it; it does not replace it.
The older `HANDOFF_lesson_pipeline.md` (Aug 25) is still accurate on authoring
conventions (§3–6 there); this file supersedes its progress tables and next-steps.

---

## 1. Where the work stands

Live board: `python3 scripts/status.py`. Snapshot as of this handoff:

| Stage | Progress | Notes |
|---|---|---|
| Content markdown | **36 / 36 written** | All topics authored, lint 36/36 clean |
| Question data modules | 36 / 36 in `scripts/banks/` | XML rebuild needed (see §3) |
| Question bank XML | 0 / 36 current | Stale — marker canonicalization touched all content |
| PDF notes | 0 / 36 current | Same staleness; rebuild after XML |
| Images | **4 / 36** (1.1, 2.2, 2.3, 3.1) | Blocked on Gemini daily quota |
| Interactive Moodle XML | 4 / 36 built and committed | Hard-gated on images (correctly) |

Style clause is locked in `.style` at the repo root (also copied into each
completed image dir as `.style`). Do not vary it between lessons.

Course notebook id lives in `.gemini_notebook`: `baa262c1-2987-4e7b-a213-9cf8dc43460b`.

---

## 2. What happened last session (2026-08-26)

1. Committed the four complete image sets + rebuilt Topic 9.2 PDF (`a7d3f4d`).
2. Compiled interactive lesson XML for 1.1, 2.2, 2.3, 3.1 and committed them with
   the staging dirs (`3ceb2bc`).
3. Canonicalized the takeaway marker from
   `**The takeaway for this page:** …` to `**Takeaway:** …` across all 36 content
   files, both handoff docs, and one compiled XML (`2fff957`). The linter's rule
   (`\*\*takeaway:\*\*`, case-insensitive) was already the shorter form; the prose
   is what changed.
4. Ran image generation for lesson 1.2: part 1 succeeded (15 slides in
   staging), part 2 hit Gemini's daily account limit. The script exited with code
   3 (`EXIT_ACCOUNT_LIMIT`) — the designed stop, not a crash.

## 3. Immediate next steps (unblocked now)

The takeaway-marker rewrite makes every question XML and PDF stale relative to
its content file. Rebuild them:

```bash
source ~/projects/RELS/.venv/bin/activate     # provides the markdown package
cd ~/projects/RELS/398
python3 scripts/question_bank.py --all
# then batch the PDFs — see HANDOFF_lesson_pipeline.md §4 for the exact
# per-lesson invocation (--topic INT, --lesson STRING)
python3 scripts/lint_lesson_content.py --course-dir .   # must stay 0 issues
```

Then commit per topic as usual.

## 4. The images queue (needs Gemini quota reset)

Order below follows the interrupted run; every deck's sources are already in the
notebook, so each resume passes `--replace-source` deliberately.

```bash
# 0. Start the automation Chrome (see §5) and verify:
curl -s http://127.0.0.1:9222/json/version   # expect a JSON blob

# 1. Finish lesson 1.2 (part 1 done — 15 slides in .staging_L1.2/part1/)
python3 scripts/generate_lesson_images.py --course-dir . --topic 1 --lesson 1.2 \
  --style "$(cat .style)" --replace-source

# 2. Then the other two interrupted lessons, same pattern:
#    --topic 2 --lesson 2.1   (part 1 source only)
#    --topic 3 --lesson 3.2   (both parts; part 1 has extracted slides already)

# 3. Remaining ~30 lessons have no staging at all: plain invocation,
#    no --replace-source, never --no-images.
```

After each success the natural follow-ups are
`compile_interactive_lesson.py --course-dir . --topic N --lesson N.M` (verified
working on all four finished lessons) and lint before committing.

**Watch for the account limit again.** Exit code 3 means the daily Slides quota
is gone; stop, do not retry the same batch later the same day. One lesson
(≈30 slides) may or may not fit depending on when the quota window resets.

## 5. Chrome CDP — resolved, use this recipe

Root cause found last session: Chrome ≥136 refuses `--remote-debugging-port` on
the *default* profile ("DevTools remote debugging requires a non-default data
directory"). Every earlier restart attempt against the normal desktop Chrome was
doomed regardless of flags.

The pipeline uses a dedicated signed-in automation profile:

```bash
bash scratch/start_scholar_chrome.sh    # launches ~/.gemini/scholar_profile on :9222
```

Symptoms to recognize if someone skips this step: port 9222 listens but every
`/json/*` endpoint returns 404. That state means the wrong Chrome owns the port.

If the *user's* desktop Chrome was killed in the crossfire, it does not come back
from a script — let Ken relaunch it from the desktop.

## 6. Working agreements (unchanged, restated briefly)

- Lint before every commit; check the exit code directly, don't pipe.
- Commit per topic; substantive messages; lint status noted.
- Never `--no-images` in a batch loop; never fork shared scripts into `398/scripts/`.
- `/sit` read-only on remotes; `/stand` is the only push.
- `private/` holds student PII; gitignored; nothing moves out of it.
- Question banks: one question per section in page order, diagnostic feedback on
  every distractor, `note=` restates that section's takeaway (now `**Takeaway:**`).

## 7. Suggested order from here

1. Rebuild question XMLs + PDFs (§3) — mechanical, unblocked, clears the △ board.
2. Resume images 1.2 → 2.1 → 3.2 after quota resets (§4), then interactive compiles.
3. Batch remaining lessons' images, a few per day as quota allows.
4. Interactive XML + any Moodle packaging as image sets land.
