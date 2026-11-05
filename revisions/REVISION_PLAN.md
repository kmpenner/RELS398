# Master Revision Plan: Next Offering of RELS 398 / ENGL 398
## Digital Methods for Historical Documents

> **Status:** Strategic Roadmap & Implementation Scaffolding for Future Iterations  
> **Authority:** Preserves Fall 2026 settled decisions while establishing the blueprint for the next course offering.  
> **Governing References:** [`SESSION_CONTENT_SPEC.md`](file:///home/kmpenner/projects/RELS/398/SESSION_CONTENT_SPEC.md), [`LEDGER.md`](file:///home/kmpenner/projects/RELS/398/LEDGER.md).

---

## 1. Executive Summary & Core Motivations

The Fall 2026 maiden voyage of RELS 398 / ENGL 398 established a complete 13-module, 36-lesson curriculum grounded in a 3-student cohort working with distinct primary witnesses (1752 Peace and Friendship Treaty, 1791 French Revolutionary Decree, 1967 Maud Lewis correspondence).

While the pedagogical core—the **Three-Step Comparative Cycle** (Tuesday manual ground truth $\rightarrow$ Wednesday deterministic rule script $\rightarrow$ Friday AI-assisted model $\rightarrow$ synthesized merge)—proved exceptionally effective, the administrative and technical delivery encountered two major friction points:

1. **Submission Chaos on Moodle:**
   Relying on Moodle assignment dropboxes resulted in students uploading unversioned, loose files (`my txt.txt`, `Witness.xml`, loose `.docx` reflection essays) often weeks late. Because Moodle accepts arbitrary byte streams without validation, students frequently submitted non-validating XML (e.g., NCName syntax violations, malformed tags) that failed silently until instructor grading.
2. **Inverted Tool Ladder:**
   The original Week 1–2 sequence front-loaded VS Code and generative AI extensions into Lesson 1.1 before students understood command-line mechanics, plain text encoding, or raw markup syntax.

---

## 2. Core Reform 1: The Shell $\rightarrow$ Editor $\rightarrow$ AI Tool Ladder

The curriculum will strictly implement the deliberate pedagogical progression specified in [`SESSION_CONTENT_SPEC.md`](file:///home/kmpenner/projects/RELS/398/SESSION_CONTENT_SPEC.md):

```
       [ Stage 3: AI Extensions ]
       Lesson 2.3: Antigravity / Copilot / Claude
                 ▲
                 │
       [ Stage 2: Code Editor & Schema CI ]
       Lesson 2.2: VS Code + Red Hat XML + RELAX NG + GitHub Actions CI
                 ▲
                 │
       [ Stage 1: Terminal, Shell, Git, & GitHub ]
       Lesson 1.2: Bash + Plain Text + Local Git + Remote GitHub Push & PRs
       Lesson 2.1: TEI Header via `echo >` / `>>` committed & pushed to GitHub
```

### Revised Schedule for Weeks 1 & 2 (Relocating Module 10's GitHub Material to Week 1–2)

In Fall 2026, distributed Git, GitHub remotes, pull requests, and CI/CD were deferred until **Module 10 (Week 10)**. Moving GitHub onboarding to **Week 1 (Lesson 1.2) and Week 2 (Lessons 2.1–2.2)** ensures that **every single assignment starting with Module 2 is submitted on GitHub**, while freeing Week 10 in the 13-week schedule for **Multi-Witness Collation** across the 1760–1761 Halifax Treaty exemplars.

| Lesson | Focus | Core Tools & Concepts | Student Deliverable |
| :--- | :--- | :--- | :--- |
| **1.1** | **The Scholarly Edition Pipeline** | 10 tasks across 3 modes (Manual, Deterministic, AI), anchored in the 1760–1761 Halifax Treaties. | Selection of primary witness / district exemplar. |
| **1.2** | **FAIR Data, Shell, Git, & GitHub** | Bash navigation, plain text, Markdown, `git init`/`add`/`commit`, **GitHub authentication (`gh`), remote push, and Pull Request workflow** (relocated from old Lesson 10.1). | Live GitHub repository with pushed `README.md` and document metadata. |
| **2.1** | **TEI Header in Shell & GitHub Push** | Writing a valid `<teiHeader>` in bash using `echo >` and `echo >>`. Pushing branch and opening first PR on GitHub. | Pushed commit/PR on GitHub containing `header.xml`. |
| **2.2** | **VS Code, RELAX NG, & GitHub Actions CI** | VS Code installation, Red Hat XML extension, `msdesc.rng`, and **automated GitHub Actions CI validation gates** (relocated from old Lesson 10.2). | Schema-validated XML in VS Code; GitHub Actions CI badge turns green. |
| **2.3** | **AI Assistance in TEI Authoring** | Prompt engineering for TEI header completion under strict negative constraints; three-way diff and merge on GitHub. | First formal assignment submitted via GitHub Pull Request / Release tag (`v-module-02`). |

### Re-sequenced 13-Module Semester Map (Option A: Early Web Publication + Progressive ODD & Rendering)

By placing **Web Publication I at Week 5** (immediately after Week 4 Diplomatic Transcription) and introducing **progressive TEI ODD (One Document Does it all) development**, every subsequent week (Weeks 6–12) follows a unified three-part cumulative pattern in the student's GitHub repository:
1. **New TEI Markup** added to the edition XML.
2. **ODD Schema Customization** (`edition.odd` $\rightarrow$ compiled `.rng`) enabling the new module/elements and enforcing project-specific closed value lists (e.g., constraining `@pos` to the 17 UPOS tags in Week 8, or `@wit` to declared treaty witnesses in Week 7) validated by GitHub Actions CI.
3. **Live Web Rendering Update** (CSS/XSLT/Processing Model) immediately exposing the new editorial layer on the student's live **GitHub Pages** site.

| Week | Module | Focus | Cumulative Markup + ODD + Live Web View |
| :--- | :--- | :--- | :--- |
| **W1** | **Module 01** | **Orientation, Shell, Git, & GitHub** | Pipeline overview (1.1); FAIR, Bash, Git, & **remote GitHub push** (1.2, absorbs old 10.1). |
| **W2** | **Module 02** | **1. Cataloguing & Schema CI** | `<teiHeader>` via shell `echo >>` (2.1); VS Code, base ODD/`msdesc.rng`, & **GitHub Actions CI** (2.2, absorbs old 10.2); AI `<msDesc>` & 3-way merge (2.3). |
| **W3** | **Module 03** | **2. Archival Imaging & IIIF** | Physical photography/scanning (3.1); ImageMagick/GIMP & IIIF manifests (3.2); AI image enhancement & macro-layout (3.3). |
| **W4** | **Module 04** | **3. Diplomatic Transcription & Reconciliation** | Manual paleography (`witness.xml`, 4.1); deterministic HTR/OCR (4.2); Vision LLM + **3-way reconciliation** (`transcription_reconciled.xml`, 4.3 — combines old M4 & M5). |
| **W5** | **Module 05** | **4. Web Publication I & ODD Foundations** | Publish the diplomatic transcription + IIIF image to **GitHub Pages** (HTML/CSS/XSLT); initialize `edition.odd` documenting diplomatic elements (`<pb/>`, `<lb/>`, `<hi>`, `<unclear>`, `<gap/>`). |
| **W6** | **Module 06** | **5. Normalization & Regularization** | *Markup*: `<choice>`, `<orig>`/`<reg>`, `<abbr>`/`<expan>`. *ODD*: enable choice elements & `@resp` constraints. *Web*: add live **Diplomatic vs. Reading View toggle**. |
| **W7** | **Module 07** | **6. Multi-Witness Collation** | *Markup*: `<app>`, `<lem>`, `<rdg wit="...">` across the 1760–1761 Halifax Treaty exemplars. *ODD*: add `textcrit` module & closed `@wit` list. *Web*: interactive apparatus variant popovers. |
| **W8** | **Module 08** | **7. Lemmatization & Morphology** | *Markup*: `<w @lemma @pos @msd>`, `<pc>`, `<s>` on the collated text. *ODD*: add `analysis` module & closed `<valList>` of the **17 UPOS tags**. *Web*: word-level morphology inspector on hover. |
| **W9** | **Module 09** | **8. Named-Entity Markup** | *Markup*: `<persName>`, `<placeName>`, `<orgName>` with `@ref`. *ODD*: add `namesdates` module & `@type`/`@ref` rules. *Web*: highlighted entities with prosopography/gazetteer cards. |
| **W10** | **Module 10** | **9. Translation & Interlinear Glossing** | *Markup*: parallel translation division & Leipzig interlinear glosses. *ODD*: `@xml:lang` and division constraints. *Web*: facing-column translation pane. |
| **W11** | **Module 11** | **10. Dual Alignment (Text $\leftrightarrow$ Image & Text $\leftrightarrow$ Translation)** | *Markup*: `@facs` linking text/totems to IIIF `<zone>` coordinates + `<linkGrp>`/`<link>` aligning source `<s>`/`<w>` to translation. *ODD*: `linking` module rules. *Web*: synchronized image-zone & bitext highlighting. |
| **W12** | **Module 12** | **11. Digital Scholarly Commentary** | *Markup*: `<standOff>`, `<note target="#..." type="...">`. *ODD*: closed `<valList>` for `<note/@type>` (`philological`, `historical`, `legal`). *Web*: interactive commentary notes panel. |
| **W13** | **Module 13** | **12. Publication II (Print Codex, ODD Docs, & Archive)** | Compile final `edition.odd` into human-readable project documentation + custom `.rng`; typeset print critical edition codex (Typst/PDF); publish GitHub Release & Zenodo archival DOI. |

---

## 3. Core Reform 2: GitHub-Native Submission Architecture

In the next offering, **Moodle file upload dropboxes are completely replaced by GitHub repositories**.

### The Student Repository Architecture
Each student receives a dedicated repository (via **GitHub Classroom** or an organization repository, e.g., `RELS398-2027/student-witness`):
* The repository is initialized with:
  * Course schema: `msdesc.rng`.
  * Automated validation workflow: `.github/workflows/tei_validate.yml`.
  * Directory layout for weekly modules (`cataloguing/`, `transcription/`, `normalization/`, etc.).
  * Root `LEDGER.md` for student policy decisions.

### Three-Step Comparative Submissions via Commits / Pull Requests
Instead of uploading disconnected files to Moodle, students record each step of the weekly comparative cycle as a distinct commit or branch:
1. **Tuesday (Step 1 - Manual):** Commit manual ground truth table and initial XML (`git commit -m "step-1: manual ground truth"`).
2. **Wednesday (Step 2 - Deterministic):** Commit rule-based NLP output and error log (`git commit -m "step-2: deterministic nlp parse"`).
3. **Friday (Step 3 - AI & Merge):** Commit prompt record, diff audit (`LINGUISTIC_AUDIT.md`), and final merged TEI deliverable (`git commit -m "step-3: ai audit and merged tei"`).

The final weekly submission is made by **creating a Pull Request or tagging a release** (e.g., `v-module-08`). The instructor grades the exact commit hash, viewing visual line-by-line diffs directly in the GitHub web interface.

---

## 4. Core Reform 3: Automated CI/CD Validation Gates

Every student repository includes a GitHub Actions workflow (`.github/workflows/tei_validate.yml`) running on push and PR:

```yaml
name: TEI XML Validation Gate
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install libxml2
        run: sudo apt-get update && sudo apt-get install -y libxml2-utils
      - name: Validate TEI XML against RELAX NG
        run: |
          xmllint --noout --relaxng schemas/msdesc.rng submissions/**/*.xml
```

### Benefits for Students & Instructor
* **Immediate Feedback:** If a student types `xml:id="Front page"` (invalid NCName) or misses a closing tag, GitHub Actions fails immediately with a red indicator and exact line number.
* **Pre-Flight Confidence:** Students resolve syntax errors before the instructor ever looks at the submission.
* **Rubric Automation:** Eliminates lost grading time diagnosing trivial syntax slips; instructor grading focuses entirely on philological accuracy, authority control, and analytical reflection.

---

## 5. Core Reform 4: Student Anonymization & Canonical Demo Witnesses

### 1. Complete Cohort Anonymization
In the Fall 2026 offering, student names (Ace, Olyvia, Andromeda, and previously Jay) were deeply integrated into slides, teaching plans, and lesson prose. For the next iteration:
* **Purge Real Student Names:** Remove all student personal names from lecture slides, teaching plans, public lesson prose, and repository scaffolding.
* **Abstract Project Personas / Tracks:** Replace specific student references with durable, genre-based tracks:
  * **Track 1 (Diplomatic / Legal):** Early Modern Legal Proclamation or Treaty (e.g., 18th-century colonial treaty).
  * **Track 2 (Administrative / Continental):** Continental European Administrative Decree (e.g., 18th-century French National Assembly decree).
  * **Track 3 (Epistolary / Vernacular):** Modern Vernacular Correspondence (e.g., 20th-century personal letters).
* **Privacy Compliance:** Protects student intellectual property and privacy while allowing the course materials to be shared, open-sourced, or archived publicly without FERPA/privacy violations.

### 2. Canonical Anchor Witness for Classroom Demos: The 1760–1761 Halifax Treaties
A major friction in Fall 2026 was that lecture demonstrations constantly toggled between three disparate, highly eccentric documents (an 18th-century French decree with clitics and imperfect verb forms, a 1752 colonial treaty with archaic legal formulas, and a 1967 folk letter with colloquial Maritime dialect).

For the next offering, the **1760–1761 Halifax Peace and Friendship Treaties ("Burial of the Hatchet" treaties)** will serve as the universal classroom demonstration corpus:
* **Archival Witnesses:** Surviving parchment exemplars in Nova Scotia Archives (`RG 1 vol. 430`) and the UK National Archives (`CO 217`), negotiated between Governor Charles Lawrence / Jonathan Belcher and Mi'kmaw and Wolastoqey district chiefs (e.g., Paul Laurent of LaHave, Claude Rene of Shubenacadie/Chibenaccadie, Battiste Jerome of Richibucto, Michel Augustine of Richibucto, Francis Joseph of Miramichi).
* **Pedagogical & Curriculum Advantages:**
  * **Multi-Witness Collation & Apparatus (Modules 14/15 or Collation Week):** Because distinct Mi'kmaw districts signed separate parchment copies sharing the same core boilerplate (including the famous "Truckhouse" clause at the center of *R. v. Marshall* [1999]) with scribal variants, differing dates, district names, and signatories, the 1760–1761 treaties provide authentic multi-witness collation and parallel alignment material.
  * **Pictographic Signatures & IIIF Zones (Module 3):** Each chief signed with their personal clan totem/mark (bird, fish, bow, animal) alongside British signatures and wax seals, providing an exceptional demonstration for TEI `<figure>`, `<graphic>`, `<signed>`, and IIIF SVG bounding zones (`<zone>`).
  * **18th-Century Paleography & Regularization (Modules 4–6):** Manageable length (~600 words), clear 1760s legal script, standard suspensions/abbreviations (`&c.`, superscript contractions), and transparent archaic orthography for `<choice><orig><reg>`.
  * **Linguistic & Named-Entity Markup (Modules 8–9):** Rich modal auxiliaries, legal formulas, and high-recognition historical persons, Mi'kmaw districts, and colonial institutions.
  * **Independence in the Lab:** In-class demos use the 1760–1761 treaties (or compare two district exemplars like LaHave vs. Shubenacadie); students then apply the exact same methods to their own independent project witness during the workshop phase.

---

## 6. Directory Inventory of Revision Scaffolding

This directory contains ready-to-deploy scaffolding for the future course launch:

* [`revisions/scaffolding/.github/workflows/tei_validate.yml`](file:///home/kmpenner/projects/RELS/398/revisions/scaffolding/.github/workflows/tei_validate.yml): Turnkey CI workflow for student repositories.
* [`revisions/scaffolding/student_repo_template/`](file:///home/kmpenner/projects/RELS/398/revisions/scaffolding/student_repo_template/): Turnkey student starter repository template.
* [`revisions/lesson_blueprints/`](file:///home/kmpenner/projects/RELS/398/revisions/lesson_blueprints/): Detailed lesson plans for Lessons 1.1, 1.2, 2.1, 2.2, and 2.3.
