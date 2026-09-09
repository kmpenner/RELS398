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
  4. Correct `03a_Lesson_2.2_Lesson_Content.md` (Red Hat XML does not validate RELAX NG) and recompile the 2.2 bank/notes before Friday's Meeting #5.
  5. Fix `populate_moodle_topic.py` bank-import ordering: it imports question banks before replacing activities, so purging a category whose quiz still exists loops and aborts.
  6. Regenerate Lesson 2.3 companion media (brief/detailed audio, infographic) once quota allows — the 2026-08-28 versions narrate the pre-redesign text and are now two revisions behind.
  7. Remaining novice rewrites: 17 lessons from the 2026-08-26 bulk-authored cohort (Modules 08–13). Modules 03–07 were hand-authored and already read in range.

---

## 6. Recent Workstream Ledger

- **[2026-09-09]**: Redeployed **Lesson 2.3 to live Moodle** (course 51185, Section 2) with the redesigned content, and fixed two safety defects found on the way.
  - **`get_quiz_attempt_count` failed open** (`shared/scripts/moodle_automation.py`): it swallowed every exception and returned 0, and callers treat 0 as permission to delete. An unconnected driver reported "0 attempts" on four quizzes while every request was throwing. Now positively confirms a quiz view page rendered (`body id=page-mod-quiz-view`) and raises `AttemptCheckError` when the count cannot be established; `strict=False` keeps lenient behaviour for reporting only. Also closed two further fail-open paths: `delete_activities` fell back to an empty `cm_map` when `get_course_state()` failed, which made every `modname` empty and skipped the quiz guard for the whole batch, and `delete_activity` warned-and-continued when its pre-check threw. Committed to `shared` (758ae4c).
  - **The manifest was stale.** cmids 1422956–1423010 predated the 2026-09-04 Section 2 resync; the live section now runs 1428505–1428528. `dump_moodle_manifest.py` re-run and committed. Attempts then verified genuinely at **0** for Lessons 2.1, 2.2, 2.3 and the Weekly Quiz before anything was deleted.
  - **Purging a question category fails while its quiz still exists.** Moodle will not hard-delete questions in use, so `purge_question_categories_for_import` reported "deleted 60 question(s)" ten times over and aborted. Order must be: delete the quiz activity first, then purge and re-import, then create the replacement. `populate_moodle_topic.py` imports banks *before* replacing activities (line ~185), so a full topic run will hit this on any section whose quizzes already exist — worth fixing there.
  - **Deployed:** Notes PDF replaced (cmid 1428521 → 1430835); Interactive Quiz rebuilt from the re-imported bank (cmid 1428520 → 1430839), verified at 60 slots with content/question pairs correctly interleaved, 1 question per page, `immediatefeedback` behaviour, 19 review options enabled, sequential navigation, completion require-grade.
  - **Repaired a side effect:** deleting the old quiz left the Notes PDF's completion restriction pointing at a dead cmid (`{"type":"completion","cm":0}` with `error_selectcmid`). Re-pointed at 1430839 and verified.
  - **Still stale on Moodle:** Lesson 2.3 Brief/Detailed audio (cmid 1428519, 1428522) and the Infographic (1428518) all date from 2026-08-28 and narrate the pre-redesign lesson.

- **[2026-09-09]**: **Redesigned Lesson 2.3 from the module's learning objectives rather than revising the inherited section list**, on the instruction not to treat the previous structure as a constraint. Retitled *Auditing AI-Generated Manuscript Metadata*. All 30 section topics are new; readability holds at grade 8.7 (14.0 words per sentence, 4.9% four-syllable).
  - **Gap found and closed:** the workshop rubric awards 3 of 10 points for authority control using **Trismegistos, Pinakes, and Diktyon**, and no lesson in the course had ever taught them — 2.2 taught VIAF, Pleiades, and Getty AAT, which identify people and places, not texts, works, or Greek codices. Sections 06–10 now cover the three registers and how they attach to `msDesc` via `@ref`, `@corresp`, and `altIdentifier`. Section 09 deliberately withholds the example Diktyon number so students look it up: an unverified identifier is the exact failure the lesson trains against.
  - **Restructured around the graded verb.** The submission asks for *at least two subtle hallucinations* — errors that pass validation. Sections 18–22 are five worked subtle failures (fabricated provenance; false precision from hedged evidence; silent omission; an authority link resolving to a real but wrong record; a well-formed CTS URN pointing at the wrong text), each with what catches it and why the schema does not. Section 04 establishes the well-built-versus-true distinction the whole second half depends on; section 29 scaffolds the 300–500 word comparison directly against the three rubric clauses.
  - **Cut as serving no objective:** the five computer-vision sections (MEM, multilayer vision, ROI detection, multimodal knowledge graphs, vision failure modes), the two-model behavioural profiling, the CI/CD pipeline, and the economics table. The Eurocentric-bias argument was kept and relocated to section 23, reframed around training-data coverage of scholarly traditions, where it bears directly on the students' own auditing decisions.
  - **Corrects a false statement in the previous entry:** the 30 slide images are **not** style-neutral illustrations. They are titled slides with rendered text carrying the old headings and vocabulary ("ChatGPT-4 Profile", "Automated Evaluation Metrics — Precision | Recall | F1-Score", "CI/CD Production Pipeline"), so they were already stale after the first rewrite. All 30 regenerated via OpenRouter (`google/gemini-3.1-flash-image`) using the stored `.style` clause and the real thematic headings, at the course's 80 KB budget — no Gemini Notebook quota consumed. Generator script kept at `shared/skills/` for reuse; note that `.style` ends "no text, lettering, or labels", which the script strips because the heading is part of the image request.
  - **Rebuilt in pipeline order:** question bank re-authored (30 Q, names and takeaways verified equal to the lesson by script), bank XML, notes PDF, interactive XML (3.38 MB, 61 question elements), HTML player. `src/modules/` and `dist/moodle/` byte-identical. Lint clean, 36/36.

- **[2026-09-09]**: Rewrote **Lesson 2.3** (*AI-Assisted Metadata Enrichment, Entity Extraction, and Validation Auditing*) into the novice-accessible register, and rebuilt every downstream deliverable. Readability moved from **Flesch–Kincaid grade 19.1 to 8.8** (23.3 → 14.3 words per sentence; 16.8% → 4.8% four-syllable words), bringing it below the 12.1/13.0 of the already-rewritten 2.1 and 2.2.
  - **Prior-knowledge constraint applied:** the rewrite assumes only what Lessons 1.1, 1.2, 2.1, and 2.2 actually taught. Transformer/token/embedding theory, the F1 formula, the CV model zoo (YOLOv11, Detectron2, BLIP-2, Mistral-7B), and CI/CD jargon are gone; precision and recall are now derived from the six-field scorecard students fill in by hand, and every remaining term is defined at first use. Callbacks to Wednesday's schema, Tuesday's `msDesc`, Lesson 1.1's Git and Python, and 2.2's RDF triples carry the load instead.
  - **Section topics preserved 1:1** across all 30 pages, so the existing 30 slide illustrations in `03c_Lesson_2.3_Images/` remain valid and were not regenerated (Gemini quota preserved).
  - **Question bank rewritten** (`scripts/banks/lesson_2_3.py`): all 30 stems, options, and feedback re-authored against the new sections; names and `note=` fields verified equal to the new headings and takeaways by script. Absurdist distractors ("3D holographic wireframes", "time-travel short story") replaced with plausible wrong answers targeting real misconceptions, so the checks actually test comprehension.
  - **Rebuilt in pipeline order** (content → bank → PDF notes → images → interactive XML → HTML player): `03b_Lesson_2.3_Questions.xml` (30 Q), `04_Lesson_2.3_Notes.pdf`, `03_Interactive_Lesson_2.3.xml` (3.21 MB, images embedded), `03_Interactive_Lesson_2.3.html`. `src/modules/` and `dist/moodle/` verified byte-identical. Lint clean, 36/36 lessons, 0 issues.
  - **Not regenerated:** companion media in `03d_Lesson_2.3_Media/` (`brief.m4a`, `detailed.m4a`, `infographic.jpg`, dated 2026-08-28) still narrate the pre-rewrite text. Nothing in the lesson or interactive XML references them, so no build is broken, but the audio is now out of step with the prose.
  - **Also open:** Moodle Section 2 still serves the old 2.3 lesson and bank; redeploy before Friday.

- **[2026-09-09]**: Resolved the schedule slip by **combining Lessons 2.2 and 2.3 into Friday's Meeting #5** rather than pushing 2.3 into the following week — the Module 02 Workshop Comparison Post is due Friday 11:00 PM and requires the AI-audit step, so 2.3 could not slip.
  - Authored `src/modules/Module_02_Cataloguing/Lesson_2.2_2.3_Combined_Teaching_Plan_2026-09-11.html`: 6 min Scholarly XML install and framing, 8 min projector demo linking `msdesc.rng`, **16 min Lab A (validate the human file to 0 errors)**, **12 min Lab B (generate an AI header, run it through the same gate, score it)**, 6 min pooling results at the board, 2 min commit.
  - **Combining principle:** the schema is the shared instrument, taught once and used twice — first on the student's header, then on the machine's. Everything that does not pass through the Problems panel was cut from class time: the VIAF/Pleiades/CTS enrichment block moves to the workshop (where Trismegistos/Pinakes authority reconciliation already lives), and 2.3's theory (semantic–structural trade-off, `macro.xml` authority architecture, NERD) stays on Moodle as the interactive lessons and quizzes.
  - Lab B assessment is a **6-field scorecard** (repository, `idno`, material, extent, hand count, date; each marked correct/wrong/invented/missing) plus the AI file's raw first-pass schema error count. Teaching point: a schema-valid but factually false shelfmark passes the gate — structure is checkable by machine, truth is not.
  - Completed `labs/witness.xml`, the header the class built together Wednesday: restored the TEI namespace, `teiHeader`, and real containment (`sourceDesc/msDesc/msIdentifier`, `physDesc/objectDesc/supportDesc`), and validated it clean against `msdesc.rng`. The one genuine error found on the way — `<extent>` rejecting a `<p>` that its sibling `<support>` accepts — is retained as Friday's live demo error in place of a contrived one.

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
