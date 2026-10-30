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
       [ Stage 2: Code Editor ]
       Lesson 2.2: VS Code + Red Hat XML + RELAX NG / Schematron
                 ▲
                 │
       [ Stage 1: Terminal & Shell ]
       Lesson 1.2: Bash + Plain Text + Local Git
       Lesson 2.1: TEI Header via `echo >` / `>>` + Remote GitHub
```

### Revised Schedule for Weeks 1 & 2

| Lesson | Focus | Core Tools & Concepts | Student Deliverable |
| :--- | :--- | :--- | :--- |
| **1.1** | **The Scholarly Edition Pipeline** | 10 tasks across 3 modes (Manual, Deterministic, AI). No front-loaded software tours. | Selection of primary witness folio / document. |
| **1.2** | **FAIR Data, Shell, & Local Git** | Bash terminal navigation, plain text, Markdown, `git init`, `git add`, `git commit`. | Local git repo with `README.md` and document metadata. |
| **2.1** | **TEI Header & GitHub Remote** | Writing a valid `<teiHeader>` in bash using `echo >` and `echo >>`. Authenticating GitHub via `gh`/SSH and pushing remote. | First pushed commit on GitHub repository containing `header.xml`. |
| **2.2** | **VS Code & Schema Validation** | VS Code installation, Red Hat XML extension, RELAX NG (`msdesc.rng`), schema validation errors. | Schema-validated XML in VS Code; GitHub Actions CI turn green. |
| **2.3** | **AI Assistance in TEI Authoring** | Prompt engineering for TEI header completion under strict negative constraints. | Three-way audit of manual vs. AI header elements. |

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

### 2. A Canonical "Anchor Witness" for Classroom Demos
A major friction in Fall 2026 was that lecture demonstrations constantly toggled between three disparate, highly eccentric documents (an 18th-century French decree with clitics and imperfect verb forms, a 1752 colonial treaty with archaic legal formulas, and a 1967 folk letter with colloquial Maritime dialect).

For the next offering:
* **One Typical Anchor Witness for In-Class Demos:** The instructor adopts a single, well-documented, canonical witness (e.g., a standard Early Modern English printed witness like Shakespeare First Folio / King James Bible, or a canonical Latin/English manuscript leaf) as the **universal lecture demonstration**.
* **Pedagogical Benefits:**
  * **Cleaner Pedagogy:** Core markup concepts (element nesting, clitic splitting, authority lookup, regularized spelling) are taught on a text with predictable, transparent orthography.
  * **Standard Benchmark:** All students see the exact same reference baseline modeled before they attempt to apply those principles to their own eccentric project documents.
  * **Independence in the Lab:** In-class demos use the anchor witness; students apply the methods to their independent document during the workshop phase.

---

## 6. Directory Inventory of Revision Scaffolding

This directory contains ready-to-deploy scaffolding for the future course launch:

* [`revisions/scaffolding/.github/workflows/tei_validate.yml`](file:///home/kmpenner/projects/RELS/398/revisions/scaffolding/.github/workflows/tei_validate.yml): Turnkey CI workflow for student repositories.
* [`revisions/scaffolding/student_repo_template/`](file:///home/kmpenner/projects/RELS/398/revisions/scaffolding/student_repo_template/): Turnkey student starter repository template.
* [`revisions/lesson_blueprints/`](file:///home/kmpenner/projects/RELS/398/revisions/lesson_blueprints/): Detailed lesson plans for Lessons 1.1, 1.2, 2.1, 2.2, and 2.3.
