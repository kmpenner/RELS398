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
- **[2026-09-03] Text & XML Editing Standard:** Visual Studio Code (VS Code) with XML tooling is the sole official editing environment across all course modules, completely replacing Oxygen XML Editor.
- **[2026-09-03] Full-Page Witness Standard:** Primary textual witnesses chosen by students must be an entire full page (one complete folio recto or verso, or complete epigraphic surface) of the artifact to ensure full codicological evidence.

---

## 3. Active Constraints & Inviolable Policies

- 🔒 **Lint Gate:** `python3 scripts/lint_lesson_content.py --course-dir .` must pass with **0 issues** before every commit.
- 🔒 **Shared Tooling:** Scripts under `scripts/` must be `runpy` shims pointing to `shared/scripts/`. Never fork shared scripts into the course repo.
- 🔒 **Privacy Boundary:** `private/` holds student PII; gitignored; never staged or pushed to GitHub.
- 🔒 **Session Boundaries:** `/sit` is read-only on remotes; `/stand` is the sole push to GitHub and sync to Google Drive.

---

## 4. Open Questions & Unresolved Issues

- ⚠️ **[OPEN - CONTENT CORRECTION NEEDED]:** `src/modules/Module_02_Cataloguing/03a_Lesson_2.2_Lesson_Content.md` tells students to use "Red Hat XML **or** Scholarly XML" for the `xml-model` step as if the two are interchangeable. They are not: Red Hat XML validates DTD and XSD, while RELAX NG (`msdesc.rng`) requires **Scholarly XML**. As written, a student with only Red Hat XML installed reaches "0 errors" because nothing is being checked — a silent failure at the Lesson 2.2 stage gate. Correct the lesson content and recompile the 2.2 question bank/notes before the validation lab runs.
- ⚠️ **[OPEN - AWAITING 5-HOUR QUOTA RESET]:** Slide deck generation for Lesson 3.3 (artifact count reached 66; prompt submitted cleanly after fixing picker toggle, but generation timed out waiting for new artifact). Resume when quota window refreshes (~16:53 local time).
- ⚠️ **[OPEN - NEXT ACTION]:** Resume image generation for Lesson 3.3 and proceed to companion media (brief, detailed, infographic) once quota refreshes, completing Module 03.

---

## 5. Active Milestone & Next Target

- **Current Phase:** Phase D/E Slide Illustrations & Companion Media for remaining lessons (starting with Lesson 3.3 upon quota refresh), following full completion of Phase F packages across all 13 modules.
- **Verification Gate:** `python3 scripts/lint_lesson_content.py --course-dir .` (36/36 clean, 0 issues) & `python3 scripts/status.py`.
- **Immediate Next Steps:**
  1. Re-run `generate_lesson_images.py --topic 3 --lesson 3.3` once Gemini Notebook quota refreshes.
  2. Generate companion media for Lesson 3.3 (`brief.m4a`, `detailed.m4a`, `infographic.jpg`).
  3. Compile interactive XML (`03_Interactive_Lesson_3.3.xml`) and HTML player for Lesson 3.3.
  4. Ensure Tuesday Meeting #3 readiness (Lesson 2.1 Teaching Plan and `witness_template.xml`).

---

## 6. Recent Workstream Ledger

- **[2026-09-09]**: Meeting #4 ran as a **rescheduled Lesson 2.1 lab, not Lesson 2.2**. Tuesday's Meeting #3 reached only bash basics, launching VS Code, and opening the project folder, leaving the entire TEI-header authoring block outstanding; the course is now one meeting behind plan.
  - Authored `src/modules/Module_02_Cataloguing/Lesson_2.1_Teaching_Plan_Compressed_2026-09-09.html` for the Wed 10:30–11:20 slot: 6 min tooling setup (extension install running under the Detective Problem framing), 10 min projector demo of the four core containers, **23 min protected hands-on authoring**, 7 min Git stage gate, 4 min schedule reset. The Witness Showcase is folded into the setup window rather than run as its own phase; the authoring block is explicitly protected, since Step 1's ground-truth claim collapses if keyboard time is cut.
  - Added a triage card (Minimum Viable Header = `fileDesc` + `msIdentifier` with repository and `idno`; defer `physDesc` detail first, `<availability>` second, **never** the commit) and an 11:00 hard time check, so every student commits something at the stage gate.
  - **Settled the extension policy:** install **Red Hat XML only** for Lesson 2.1 (well-formedness and tag symmetry without schema-driven autocomplete), hold **Scholarly XML** back to the Lesson 2.2 validation step, and disable Antigravity per-workspace for 2.1 — re-enabled for the Lesson 2.3 AI-extraction lab.
  - **Downstream:** Lesson 2.2 (deterministic validation) shifts to Friday and Lesson 2.3 (AI extraction) slides into the following week. Friday's plan has not yet been redrafted, and the 2.2/2.3 combination question is unresolved.

- **[2026-09-04]**: Completed Phase F assembly packages for **all remaining modules (Modules 05 through 13)**:
  - Authored and generated branded 1200×300 banners (`01_Banner.png`), Learning Objectives HTML, Reading Lists, Curated Watch Lists, Workshop suites (descriptions, submission guides, 10-point rubrics), and 10-question Weekly Knowledge Check Quizzes with rich diagnostic feedback (`scripts/banks/quiz_05.py` through `quiz_13.py` -> `09_Quiz.xml`).
  - All 13 course modules now possess 100% complete, fully validated Phase F assembly packages in both `src/modules/` and `dist/moodle/`.
- **[2026-09-04]**: Completely eliminated all legacy Oxygen XML references across the entire course repository:
  - Re-anchored instructions and validation workflows in Lessons 1.2, 9.3, 10.1, 10.2, 11.1, 13.1, 13.2, 13.3, and Question XMLs to Visual Studio Code (with XML extensions) and deterministic command-line validation (`xmllint`, `jing`).
- **[2026-09-04]**: Prepared Tuesday Sep 8 lab assets:
  - Authored and validated [src/modules/Module_02_Cataloguing/witness_template.xml](file:///home/kmpenner/projects/RELS/398/src/modules/Module_02_Cataloguing/witness_template.xml) as the starter ground-truth TEI Header skeleton for students to reference or copy during Tuesday's lab.
  - Synchronized compiled `03b_Lesson_2.3_Questions.xml` to `dist/moodle/Module_02_Cataloguing/`.
- **[2026-09-04]**: Completed Phase F assembly package for Module 04 (Diplomatic Transcription & HTR): generated 1200x300 banner (`01_Banner.png`), Learning Objectives, Reading List, Watch List, Workshop suite, and 10-question Weekly Knowledge Check Quiz (`scripts/banks/quiz_04.py` / `09_Quiz.xml`).
- **[2026-09-04]**: Fully refreshed and synchronized Section 2 (Module 02: Cataloguing) on live Moodle with our newly rewritten novice-accessible Lesson 2.1 and 2.2 content, fresh question banks, Notes PDFs, and sequential completion gates. Verified Section 1 student attempts intact (`cmid=1427950`, Attempts: 3).
- **[2026-09-04]**: Upstream fixes in `shared/scripts/notebook_ui.py`: repaired source picker view mode toggle to only switch when flat list options are absent, and added support for dismissing Google interstitial announcement modals with "Close dialog" buttons.
- **[2026-09-04]**: Formalized In-Class Teaching Plans (Phase E5) in `shared/LESSON_PIPELINE.md`. Authored and compiled `Lesson_2.1_Teaching_Plan_2026-09-08.html` for Meeting #3 (Tuesday Sep 8), preserving teaching plans strictly in `src/modules/` and excluding them from `dist/`.

- **[2026-09-03]**: Standardized on Visual Studio Code (VS Code) as the sole official text and XML editor across the course, removing all references to Oxygen XML Editor across Syllabus, Schedule, Lesson 1.2, Lesson 2.1, Lesson 2.2, question banks, and teaching plans.
- **[2026-09-03]**: Enforced the full-page textual witness requirement (complete folio recto/verso or epigraphic surface) across Syllabus, Schedule, Lesson 1.2, and Lesson 2.1.
- **[2026-09-03]**: Overhauled Lesson 2.1 (*Codicological Description and Hand-Authoring the TEI Header*) into an engaging, accessible format (Crash-Course style clarity); replaced graduate library ontology (FRBRoo/LRMoo/WEMI) with tactile manuscript codicology (shelfmarks, parchment/papyrus, folios, quires, ruling, hands). Recompiled 2.1 question bank, Notes PDF, HTML player, and interactive XML.
- **[2026-09-03]**: Overhauled Lesson 2.2 (*Deterministic Schema Validation, Linked Data, and Canonical Citation*) into an engaging, accessible format; reframed validation around VS Code with XML extensions (replacing Oxygen); demystified Linked Open Data (RDF triples, VIAF, Pleiades) and Canonical Text Services (CTS URNs). Recompiled 2.2 question bank, Notes PDF, HTML player, and interactive XML. All 36 course lessons pass lint with 0 issues.
- **[2026-08-31]**: Re-authored beginner-friendly Lesson 1.1 (Plain text, VS Code, Git, XML/TEI, Python, Claude AI pair-programming). Generated 30 fresh slide illustrations, Brief Audio (1:54), Deep Dive Audio (41:52), Infographic sheet, interactive XML, standalone HTML player with embedded base64 illustrations, and printable notes PDF.
- **[2026-08-31]**: Added automated activity deletion and section clearing to `moodle_automation.py` and `populate_moodle_topic.py`. Purged all duplicate activities from Moodle Section 1 and Section 2, cleanly redeploying both modules (51 live activities tracked in `moodle_manifest.json`).
- **[2026-08-29]**: Assembled Section 0 (General Orientation) and Module 03 (IIIF Imaging) full packages. Completed Lesson 3.2 illustrations (30 images), interactive XML, HTML player, and companion media (`b82521d`, `736dbb0`).
- **[2026-08-28]**: Completed Lesson 2.1 illustrations, interactive XML, HTML player, and companion media. Built Module 02 assembly package.
- **[2026-08-28]**: Populated Module 01 in Moodle course 51185 Section 1. Generated companion media across Lessons 1.1, 1.2, 2.2, 2.3, 3.1.
- **[2026-08-27]**: Rebuilt all 36 question XML banks and 36 offline PDF notes following takeaway marker canonicalization.
