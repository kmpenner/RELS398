# NEXT — 398

**Updated 2026-09-16 (morning) by Claude.**

## State after the 2026-09-16 morning run

1. **Today's class is ready.** `Lesson_3.2_Teaching_Plan_2026-09-16.html` (Meeting
   #7, 10:30, MULH 3032) carries the 3.1 facsimile carry-over Tuesday missed, and
   now hands off Workshop 3 explicitly: students leave having *chosen* three zones,
   with two concrete homework tasks (does my repository serve IIIF? start
   `IMAGE_PROVENANCE.md`) and the rights question quoted verbatim. Commit `4ed08aa`.
2. **Module 4 content is done; images are the only thing outstanding.** Lessons
   4.1-4.3 rewritten for novices and lint-clean, 90 bank questions re-authored,
   notes PDFs rebuilt (17/18/19 pp), interactive XML and HTML players built
   **`--no-images` on purpose** (`4235296`).
3. **THE OPEN ITEM — Module 4 slide images.** All three lessons still hold the
   **old 15 images from 12 Sep, which illustrate pre-rewrite text and burn the
   removed jargon into the artwork** ("Overlapping Realities / Empty Milestones",
   "CRNN / CTC"). Fresh sources ARE uploaded and their digests match the current
   text, so nothing needs re-uploading. The decks were deferred by the Slides
   quota ("Scheduled for after 2pm") and the run was stopped at 08:20.
   - One-shot **system crontab** entry fires `scratch/recover_module4_decks.sh`
     at **14:08 today**; it removes its own crontab line so it cannot repeat, and
     logs to `scratch/recover_module4_<stamp>.log`. It needs CDP Chrome on 9222,
     signed in, and aborts cleanly saying so if that is missing.
   - It deliberately **does not rebuild or commit**: verifying the new slides no
     longer carry the old jargon is a visual check no script can make.
   - If it was missed: `python3 scripts/recover_decks.py --course-dir .` (report),
     then `--write`, then `generate_lesson_images.py --topic 4 --lesson <id>` for
     any lesson under 30 images.
4. **After the images land:** rebuild interactive XML and players **without**
   `--no-images` (replacing `4235296`), confirm 30 embedded images per player
   instead of 0, then commit. Then deploy Module 4 to Moodle Section 4.
5. **Tooling fixed today (shared):** `--replace-source` now actually replaces a
   changed source instead of reusing the stale one (`893697d`) - it previously
   meant the opposite of its name and would have built decks from superseded
   prose. Queue deferrals are now detected (`30cb34a`) instead of hanging a
   30-minute wait per lesson.
6. **26 question banks unblocked** (`cd57d63`): `TOPIC` corrected from the deleted
   `Topic_NN_*` tree to live `Module_NN_*` dirs, so Modules 5-13 can build again.
   The Syncthing conflict copies under `scripts/banks/` are now redundant.
7. **Drive mirror current** as of 08:18 (27m, 67 files, `EXIT=0`).

### Known stale / open judgement calls
- **Module 3 companion media** (audio, infographic, 13 Sep) narrates pre-rewrite
  text. Nothing is broken by it; nothing references it.
- **Module 4 length**: 4.2 and 4.3 grew slightly in the rewrite. Cutting to the
  2.5 h target needs an editorial decision (suggested: 4.2 s10, 4.3 s04-05).
- **Five uncited references in 4.3** (Clerice, Colavizza, Puigcerver, Romein,
  Strobel) - pre-existing, possibly deliberate further reading. The linter only
  checks body->references, so it never fires.
- **222 repo**: 171 untracked files, 626 MB, one 127 MB PDF over GitHub's limit;
  needs a `.gitignore` modelled on 398's.
- One stray `src/modules/Module_03_IIIF_Imaging/04_Lesson_3.1_Notes.pdf`; notes
  PDFs are otherwise dist-only.

## State after the 2026-09-13 morning run

1. **Week 3 Companion Media DONE (3.1, 3.2, 3.3):** Full media suite generated
   against the freshly aligned sources:
   - **3.1:** Brief audio (1:28), Deep Dive audio (64:56), Infographic (244 KB).
   - **3.2:** Brief audio (1:41), Deep Dive audio (51:43), Infographic (244 KB).
   - **3.3:** Brief audio (1:38), Deep Dive audio (58:27), Infographic (245 KB).
2. **Notebook sources synchronized:** Refreshed all source halves for Lessons 3.1,
   3.2, and 3.3 in the course Notebook (`baa262c1-2987-4e7b-a213-9cf8dc43460b`)
   with current rewritten text, and updated `.sources.json` SHA256 digests.
3. **Slides Quota Status:** Attempted slide deck generation for Lesson 3.3; verified
   the NotebookLM daily Slides quota is still exhausted (artifact count remained at
   80). Next slide run will resume when Slides quota resets.
4. **Tooling Hardened:** `shared/scripts/notebook_ui.py` patched to enforce desktop
   1920x1080 viewport and Studio tab selection (preventing responsive occlusion of
   dialog tiles), and added scroll-into-view before tile interactions.
5. **Next immediate step:** Deploy Week 3 companion media to Moodle Section 3 via
   `populate_moodle_topic.py` / `update_moodle_item.py`, and prepare Class #5
   for RELS 216.

## State after the 2026-09-12 morning run

1. **Recovered at zero quota cost:** 4.1, 4.2, 4.3 each have 15/30 images
   (part-1 halves). 4.1+4.3 from the overnight "after 5am" queue; 4.2's deck
   (which had lost its source label) regenerated fresh in the 9am run.
2. **Second quota wall, later in the day:** the 9am batch attempt queued the
   three part-2 decks as **"Scheduled for after 1pm"** (NotebookLM quota
   queue — the generations are paid for). One-shot cron job
   `rels-398-image-batch-1pm` (id `15890ccf6a1b`, fires 13:10 ADT, reports
   via Telegram) will: recover those decks, then resume the batch for
   remaining lessons. If it was missed, just re-run:
   `recover_decks.py --write`, then `batch_lesson_images.py --only <pending>
   --max-consecutive-failures 3` (exact command in NEXT 2026-09-11 entry).
3. `shared/scripts/recover_decks.py` hardened: per-artifact error isolation,
   already-on-disk duplicate skip, virtualized-list tail timeouts tolerated.
   Full 80-item sweep verified completing (items 47+ legitimately unreadable
   — list won't scroll that far; newest items are always at top).
4. **Settled 2026-09-12 (Ken):** Media set for 398 is the **full suite** (brief
   audio, detailed audio / Deep Dive, and infographic) across all lessons,
   including rebuilt lessons (unlike 113, which skips Deep Dive). Unblocks the
   Week 3 media regeneration pass.
5. Image scoreboard: 7 lessons complete (1.1–3.2), 3 half done (4.1–4.3),
   26 not started (5.1–13.2), 3.3 paused by design. Interactive XML remains
   hard-gated on images.

## State after the 2026-09-11 evening session

1. **Week 3 rewrite is DONE** (LEDGER "ACTIVE TARGET" entry is stale — remove
   at next /stand): 3.1 rebuilt in commit `18e2f9e`, 3.2+3.3 in `8d3afba`.
   Content, banks, interactive XML/HTML, PDFs, deploy scripts, lint 36/36.
2. **Images: 7/36 lessons have slide images** (1.1, 1.2, 2.1, 2.2, 2.3, 3.1,
   3.2). The 2026-09-11 evening batch (4.1–13.2) failed 3-in-a-row: the daily
   **Slides quota is exhausted**. NotebookLM did NOT reject the requests —
   decks for 4.1/4.2/4.3 part 1 are sitting in the notebook as
   **"Scheduled for after 5am"** (top three artifact-library-items).
3. **Recovery steps, in order (next morning):**
   a. `python3 scripts/recover_decks.py` (dry) — expect the three 4.x part-1
      decks mapped to lessons 4.1–4.3. Then `--write` to download + extract.
      NOTE: the sweep crashed once at artifact 43/76 with a Playwright
      scroll timeout (`artifact-library-item` nth(43), virtualized list) —
      harmless for the top-of-list items; re-run if it dies again.
      ALSO: ignore (or delete in the UI) the old `Lesson_3.3_part1` deck —
      it was generated from the PRE-rewrite text; recovering it would write
      stale images.
   b. Resume the image batch (it skips completed lessons):
      `~/projects/RELS/.venv/bin/python scripts/batch_lesson_images.py --only 4.1 4.2 4.3 5.1 5.2 5.3 6.1 6.2 6.3 7.1 7.2 7.3 8.1 8.2 8.3 9.1 9.2 9.3 10.1 10.2 11.1 11.2 11.3 12.1 12.2 12.3 13.1 13.2 --max-consecutive-failures 3`
      (background, tee to scratch/). ~51 deck halves remain; expect several
      daily quota windows.
   c. If a lesson fails with "no new deck appeared" again, check the notebook
      first: "Scheduled for after 5am" = quota queue, recoverable tomorrow.
4. **Companion media status:** 3.1/3.2 media (brief/detailed/infographic,
   Aug 28–29) is STALE — quotes pre-rewrite text; needs regeneration.
   3.3 has no media and no images yet (its slides are also blocked on quota,
   and its old part-1 deck should NOT be recovered). Media for 4.x+ follows
   its images. Pending decision (asked Ken, unanswered 2026-09-11): for
   regenerated lessons, full brief+detailed+infographic, or brief+
   infographic only? 398's existing set is full (unlike 113, which skips
   Deep Dive).
5. Chrome/CDP was healthy all evening (scholar profile on :9222).

## Older notes (2026-08-30, kept for reference)

- Question-bank XML / PDF notes rebuild pass was the then-plan; Module 02–03
  banks have since been rebuilt (see LEDGER settled decisions 2026-09-10).
- `python3 scripts/status.py` remains the coarse snapshot; HANDOFF.md dated
  2026-08-27.

## Email history

See `emails.md` in this folder.
