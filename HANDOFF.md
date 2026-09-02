# RELS 398 — Session Handoff

**Date:** 2026-09-02
**Repo:** `~/projects/RELS/398` (remote `https://github.com/kmpenner/RELS398.git`)
**HEAD at handoff:** `10b030a` (1 commit ahead of origin — push pending)
**Read first:** `~/projects/RELS/shared/LESSON_PIPELINE.md` — the single end-to-end
procedure. This document records where 398 sits inside it; it does not replace it.
Supersedes the 2026-08-27 handoff entirely.

---

## 1. Where the work stands

Live board: `python3 scripts/status.py`.

| Stage | Progress | Notes |
|---|---|---|
| Content markdown | **36 / 36** | Lint 36/36, 0 issues |
| Question banks | **36 / 36** | All rebuilt Sept 1 |
| PDF notes | 36 / 36 | 1.2's rebuilt Sept 1 (217 KB) |
| Slide images | **7 / 36** (1.1, 1.2, 2.1, 2.2, 2.3, 3.1, 3.2) | 1.2's set regenerated Sept 1 from the NEW content |
| Interactive XML / HTML | 7 / 36 built | 1.2 recompiled Sept 1 after the image refresh |
| Moodle deployment | Modules 0–3 live; 4–13 empty | See §3 |

**Lesson 1.2 was rewritten Sept 1** (user directive): the old Unicode/polytonic-Greek
lesson was replaced with **"Data That Lasts: FAIR Principles and the Scholarly
Edition Workflow"** — FAIR principles (Wilkinson et al. 2016), FAIR-before-the-Internet,
the 8-stage edition workflow (from Ken's DHSI-East 2022 keynote, in `raw/`),
Oxygen/VS Code/accounts, passage selection, and the Sep 4 README deliverable.
Everything downstream (bank, images, XML, HTML, PDF, brief/detailed audio,
infographic) was regenerated from the new content.

## 2. Traps that already cost time — do not repeat

- **Stale NotebookLM sources.** The course notebook (`.gemini_notebook`) is shared
  across the whole course. When a lesson's markdown changes, the OLD upload is
  still there; `generate_lesson_images.py --replace-source` deliberately reuses
  the uploaded copy, so decks/audio get built from superseded text and look
  perfectly fine. **Before regenerating media for rewritten content: delete the
  lesson's `Lesson_X_partN.md` sources in the notebook UI first** (scratch/
  `delete_stale_sources.py` does this via the kebab menu). Deck/audio titles are
  the tell — e.g. "The Digital Scholarly Edition" (new) vs "Greek Unicode
  Standards" (stale).
- **Question-bank duplicates.** Moodle dedupes by full question name within a
  category, so re-importing a bank onto a populated category silently doubles
  every question (Lesson 1.2 had reached 360 slots). Fixed permanently Sept 1:
  `populate_moodle_topic.py` now **purges each target category to empty before
  importing**, matching categories by FULL PATH from the bank XML's own
  `<category>` tag (`get_category_paths()`). Do not bypass this.
- **`create_resource` cannot recover cmids** on this Moodle (4.5/Workplace):
  after "Save", the redirect does not expose the new cmid, so
  `add_completion_restriction` inside the populator warns-and-skips. After any
  fresh deploy, set notes restrictions via `scratch/fix_restrictions_and_card.py`
  (looks up cmids from the course page, idempotent).
- **Quiz completion lives in the bulk editor** (course/bulkcompletion.php), not
  the modedit form. Moodle 4.5 rejects the save with "You must select at least
  one condition" unless "Add requirements" (radio 2) is combined with at least
  one requirement checkbox (here: "Receive a grade"). The populator now does this
  via `set_quiz_completion_require_grade()`.
- **Banner labels embed the image in intro HTML** — there is no file-manager
  field to swap. Changing a banner = delete the label, `create_image_label` a new
  one. `swap_banner.py` is the worked example.
- **Moodle AJAX `core_course_edit_module` move** rejects every parameter shape
  tried (id/targetcmid, parseInt, targetsectionid). Reordering is manual drag:
  Edit mode → ⋮ → Move.

## 3. Moodle state (course 51185)

- Course **hidden from students** (`visible=0`); 7 participants, no students yet.
- Section 0 (General), Modules 1–3 fully populated; Modules 4–13 are empty
  section shells (consider hiding until populated).
- **Notes restrictions live** for 1.1, 1.2, 3.1, 3.2, 3.3 (Notes unlock only when
  the lesson's Interactive Quiz is complete). Module 2's notes keep their own
  pre-existing restrictions. Quiz completion: all Module 1 + Module 3 quizzes =
  "Add requirements → Receive a grade".
- **Banner Sept 2 (Ken/Antigravity):** `10b030a` replaced the interim 4-slide
  strip with a custom editorial banner (148 KB jpg + artwork source). The label
  in Section 1 may need a manual redeploy to serve it — the label embeds the
  image; if the deployed bytes (pluginfile 1823258) are not the new file, swap
  via `swap_banner.py` pattern (delete label → recreate).
- **Course dashboard image** (16:9 `moodle_course_image.jpg`) uploaded Sept 1.
- **Scoped deploys work:** the populator purges only the categories named in the
  target topic's own bank XMLs and clears only that section — Module 2/3 were
  untouched by the Module 1 redeploy, verified.

## 4. Infrastructure notes

- **Z-AI vision billing:** `ZAI_API_KEY` is a **GLM Coding Plan key**, not
  General API. General API (`api.z.ai/api/paas/v4`) → "insufficient balance"
  (empty pay-as-you-go pool). Coding Plan endpoint
  (`api.z.ai/api/coding/paas/v4`) works but quota resets **weekly — next reset
  Sept 3, 02:01**. Do not top up General API by accident; decide deliberately.
- **fal.ai image generation:** account locked, TOP_UP required at
  fal.ai/dashboard/billing. `FAL_KEY` itself is valid.
- **Automation Chrome:** power loss kills it; restart with
  `bash scratch/start_scholar_chrome.sh` (profile `~/.gemini/scholar_profile`,
  port 9222). Moodle session may need re-login in that profile.
- **Image-generation quota:** one lesson (~30 slides) per daily Gemini window;
  exit code 3 = quota gone, stop and retry next day.

## 5. Next steps

1. **Push** the pending commit (`10b030a`).
2. **Banner position**: new banner label may sit at the end of Section 1 —
   drag to top (Edit mode → ⋮ → Move).
3. **Module 3 audio**: 3.1/3.2 have brief+detailed; 3.3 has neither (no source
   media generated) — plus no Module 3 summary PDF. Low priority.
4. **Phase D images for Modules 4–13** — batch as Gemini quota allows
   (`scripts/batch_lesson_images.py`), then compile per lesson.
5. **Phase F module assembly** for Modules 4–13 (banner, objectives, readings,
   watch list, workshop, weekly quiz), then Moodle deploys.
6. **Moodle-side course wrapper** (weekly quizzes schedule, syllabus block,
   exams) — still unscheduled; user decision.
7. Before making the course visible: review as a student, decide the fate of
   empty sections 4–13, set course image/banner final.

## 6. Working agreements (unchanged)

- Lint before every commit; check exit code directly.
- Commit per topic; substantive messages; lint status noted.
- Never `--no-images` in a batch loop; never fork shared scripts into `398/scripts/`.
- `/sit` read-only on remotes; `/stand` is the only push.
- `private/` holds student PII; gitignored; nothing moves out of it.
- Question banks: one question per section in page order, diagnostic feedback on
  every distractor, `note=` restates that section's takeaway.