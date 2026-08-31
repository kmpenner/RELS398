# Work Ledger: RELS 398 / ENGL 398 (Digital Methods for Historical Documents)

> **Governance Principle (Automated Work Ledger / TRACER Protocol):**
> Agents must read this file before acting. Do not reopen settled decisions without explicit user instruction. Do not unilaterally resolve open questions. Check changes against the verification gate before committing.

---

## 1. Source Hierarchy & Authority

1. **Top Authority / Pipeline Standard:** `shared/LESSON_PIPELINE.md`
2. **Repository Architecture & Organization:** `shared/COURSE_ORGANIZATION.md`, `shared/MOODLE_COURSE_PATTERN.md`
3. **Primary Course State & Config:** `course.json`, `moodle_manifest.json`, `scripts/topic_map.py`
4. **Authoritative Content & Data:** `src/modules/` (Lesson content markdown, prompt records), `scripts/banks/` (Question data modules)
5. **Artifact Output (Production):** `dist/` (Compiled XML, PDFs, HTML players, banners)
6. **Ephemeral / Scratch (Non-authoritative):** `scratch/`, staging directories (`.staging_*`)

---

## 2. Settled Decisions (Locked Baseline)

- **[2026-08-25] Three-Step Comparative Cycle:** Most weeks run Tue (manual baseline) → Wed (deterministic rule script) → Fri (AI-assisted model). Lessons 1.1–1.2, 3.1–3.3, 5.1–5.2, 10.1–10.2, 13.1–13.3 deviate by design per schedule.
- **[2026-08-26] Section & Length Model:** Exactly 30 sections per lesson (`## **01 Content**` … `## **30 Content**`), ~8,500–9,500 words per lesson, closing with `**Takeaway:** …`.
- **[2026-08-27] Fixed Build Order:** `content → question bank → PDF notes → images → interactive XML → HTML player → companion media`.
- **[2026-08-28] Module-Specific Visual Styles:** Each module maintains a dedicated, content-tailored visual style in its `Module_NN_*/.style` and lesson image folders (`03c_*_Images/.style`) reflecting its domain (manuscripts, paleography, IIIF, XML, NLP).
- **[2026-08-28] Standalone HTML Players:** Compiled via `generate_interactive_html_lesson.py` into both `src/modules/` and `dist/moodle/` for offline study.
- **[2026-08-28] Moodle Quiz Configuration:** Formative interactive quizzes and weekly knowledge check quizzes configure `behaviour=immediatefeedback`, `navmethod=sequential`, 1 question/page, and 19 review checkboxes.

---

## 3. Active Constraints & Inviolable Policies

- 🔒 **Lint Gate:** `python3 scripts/lint_lesson_content.py --course-dir .` must pass with **0 issues** before every commit.
- 🔒 **Shared Tooling:** Scripts under `scripts/` must be `runpy` shims pointing to `shared/scripts/`. Never fork shared scripts into the course repo.
- 🔒 **Privacy Boundary:** `private/` holds student PII; gitignored; never staged or pushed to GitHub.
- 🔒 **Session Boundaries:** `/sit` is read-only on remotes; `/stand` is the sole push to GitHub and sync to Google Drive.

---

## 4. Open Questions & Unresolved Issues

- ⚠️ **[OPEN - AWAITING QUOTA RESET]:** Gemini Slides daily quota ceiling for Lesson 3.3 slide deck generation (staged in `.staging_L3.3/`).
- ⚠️ **[OPEN - PENDING USER REVIEW]:** Moodle course 51185 Section 2 & Section 3 activity population following Moodle re-login.

---

## 5. Active Milestone & Next Target

- **Current Phase:** Phase D/E Slide Illustrations & Companion Media for remaining lessons (starting with Lesson 3.3), and Phase F Module Assembly for Modules 04–13.
- **Verification Gate:** `python3 scripts/lint_lesson_content.py --course-dir .` (36/36 clean, 0 issues) & `python3 scripts/status.py`.
- **Immediate Next Steps:**
  1. Resume slide deck generation for Lesson 3.3 once quota allows.
  2. Author Phase F packages (Banner, Objectives, Readings, Watch List, Workshop, Weekly Quiz) for Module 04 (Transcription).

---

## 6. Recent Workstream Ledger

- **[2026-08-29]**: Assembled Section 0 (General Orientation) and Module 03 (IIIF Imaging) full packages. Completed Lesson 3.2 illustrations (30 images), interactive XML, HTML player, and companion media (`b82521d`, `736dbb0`).
- **[2026-08-28]**: Completed Lesson 2.1 illustrations, interactive XML, HTML player, and companion media. Built Module 02 assembly package.
- **[2026-08-28]**: Populated Module 01 in Moodle course 51185 Section 1. Generated companion media across Lessons 1.1, 1.2, 2.2, 2.3, 3.1.
- **[2026-08-27]**: Rebuilt all 36 question XML banks and 36 offline PDF notes following takeaway marker canonicalization.
