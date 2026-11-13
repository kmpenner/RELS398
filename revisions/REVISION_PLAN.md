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

## 6. Core Reform 5: 100% Open Access Course Reading Spine

Two Open Access edited collections co-edited by Laura Estill (StFX) and Ray Siemens (UVic) provide a zero-cost, up-to-date methodological and case-study reading spine across the 13-week sequence:

1. **[*The Companion to Digital Humanities in Practice*](file:///home/kmpenner/projects/RELS/398/raw/readings/Crompton_et_al_2025_Companion_DH_in_Practice/Crompton_Estill_Lane_Siemens_2025_Companion_to_Digital_Humanities_in_Practice.pdf)**, ed. Constance Crompton, Laura Estill, Richard J. Lane, and Ray Siemens (London: Routledge, Nov. 2025; CC BY-NC-ND 4.0, DOI: `10.4324/9781003327677`). Provides technical and methodological walkthroughs (IIIF, HTR, TEI/Git, Wikidata Entity Linking, codicological metadata, situated data, and AI ethics).
2. **[*The Past, Present, and Future of Early Modern Digital Studies: Iter at 25*](file:///home/kmpenner/projects/RELS/398/raw/readings/NTMRS_11_2023/NTMRS-11-full-volume-January-2023.pdf)** (*New Technologies in Medieval and Renaissance Studies* 11), ed. Laura Estill and Ray Siemens (New York: Iter Press, 2023; CC BY-NC 4.0). Provides longitudinal edition case studies, social/network edition theory, and long-term sustainability post-mortems.

### Module-by-Module Open Access Reading Assignments

All extracted chapter slices have been rebuilt page-by-page via `pypdf.PdfWriter()` (pruning parent xref streams) and placed in both their volume folders and the corresponding `raw/readings/Module_*/` directories:

| Week | Module | Core Technical / Methodological Reading (*Companion* 2025) | Edition Case Study / Critical Framing (*NTMRS 11* 2023 / *Companion* 2025) |
| :--- | :--- | :--- | :--- |
| **W1** | **M01: Orientation, Shell, Git, & GitHub** | [Lavin, Ch. 8: "Why Digital Humanists Should Emphasize Situated Data over Capta"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_01_Orientation/Companion_2025_Ch08_Lavin_Situated_Data_Over_Capta.pdf) (pp. 121–136) | [Estill, Ch. 10: "Digital Humanities' Shakespeare Problem"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_01_Orientation/NTMRS11_2023_Ch10_Estill_DH_Shakespeare_Problem.pdf) (pp. 217–243); [Crompton et al., Ch. 1: "DH in Practice"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_01_Orientation/Companion_2025_Ch01_Crompton_et_al_DH_in_Practice_Intro.pdf) (pp. 3–18) |
| **W2** | **M02: Cataloguing (`<teiHeader>`) & Schema CI** | [Campagnolo, Ch. 9: "Digitizing the Container: Books as Objects in the Digital Medium"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_02_Cataloguing/Companion_2025_Ch09_Campagnolo_Digitizing_the_Container_Books_as_Objects.pdf) (pp. 139–158) | [James & Shami, Ch. 6: "GEMMS: Gateway to Early Modern Manuscript Sermons"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_02_Cataloguing/NTMRS11_2023_Ch06_James_Shami_GEMMS_Manuscript_Sermons_Metadata.pdf) (pp. 125–143); [Rockwell & Hegde, Ch. 16: "Thinking-Through the Ethics of AI"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_02_Cataloguing/Companion_2025_Ch16_Rockwell_Hegde_Ethics_of_AI.pdf) (pp. 281–298); [Shrout, Ch. 15: "Against Violent Quantification"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_02_Cataloguing/Companion_2025_Ch15_Shrout_Against_Violent_Quantification.pdf) (pp. 262–280) |
| **W3** | **M03: Archival Imaging & IIIF** | [Robson & O'Neill, Ch. 11: "IIIF for Digital Humanities"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_03_IIIF_Imaging/Companion_2025_Ch11_Robson_ONeill_IIIF_for_Digital_Humanities.pdf) (pp. 179–190: Image & Presentation APIs) | — |
| **W4** | **M04: Diplomatic Transcription & Reconciliation** | [Stokes & Kiessling, Ch. 6: "Sharing Data for Handwritten Text Recognition (HTR)"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_04_Transcription/Companion_2025_Ch06_Stokes_Kiessling_Sharing_Data_for_HTR.pdf) (pp. 95–104) | [Siemens et al., Ch. 5: "Building A Social Edition of the Devonshire Manuscript"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_04_Transcription/NTMRS11_2023_Ch05_Siemens_et_al_Social_Edition_Devonshire_Manuscript.pdf) (pp. 99–123) |
| **W5** | **M05: Web Publication I & ODD Foundations** | [Grallert, Ch. 5: "Editing Mundane Texts across the Digital Divide"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_07_Rendering/Companion_2025_Ch05_Grallert_Editing_Mundane_Texts_TEI_Git.pdf) (pp. 70–83: TEI P5, GitHub, static publishing) | [Meneses, Ch. 8: "Extending the Contribution of Online Digital Projects (DEx)"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_07_Rendering/NTMRS11_2023_Ch08_Meneses_Extending_Online_Digital_Projects_DEx.pdf) (pp. 171–188) |
| **W6** | **M06: Normalization & Regularization** | [Grallert, Ch. 5: "Editing Mundane Texts across the Digital Divide"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_06_Normalization/Companion_2025_Ch05_Grallert_Editing_Mundane_Texts_TEI_Git.pdf) (pp. 84–94: character normalization, transcription QC) | [Ullyot, Ch. 12: "The Way We Read Now: Criticism in the Age of EEBO"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_06_Normalization/NTMRS11_2023_Ch12_Ullyot_The_Way_We_Read_Now_EEBO.pdf) (pp. 259–273) |
| **W7** | **M07: Multi-Witness Collation** | Existing Module 14/15 collation & apparatus readings (`raw/readings/Module_14_Collation/`) | *Devonshire Manuscript* witness collation sections in [Siemens et al., Ch. 5](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_05_Reconciliation/NTMRS11_2023_Ch05_Siemens_et_al_Social_Edition_Devonshire_Manuscript.pdf) |
| **W8** | **M08: Lemmatization & Morphology** | Existing Module 08 lemmatization readings (`raw/readings/Module_08_Lemmatization/`) | [Ullyot, Ch. 12: "The Way We Read Now: Criticism in the Age of EEBO"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_08_Lemmatization/NTMRS11_2023_Ch12_Ullyot_The_Way_We_Read_Now_EEBO.pdf) (machine-augmented pattern search) |
| **W9** | **M09: Named-Entity Markup** | [Gutiérrez, Burghardt, & Niekler, Ch. 2: "From a 'Bag of Names' to a 'Name Index': Using Wikipedia and Wikidata"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_09_Named_Entities/Companion_2025_Ch02_Gutierrez_et_al_Bag_of_Names_to_Name_Index_Wikidata.pdf) (pp. 21–27) | [Dase, Ch. 7: "Towards a Model of the Network Edition"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_09_Named_Entities/NTMRS11_2023_Ch07_Dase_Towards_a_Model_of_the_Network_Edition.pdf) (pp. 145–169) |
| **W11** | **M11: Dual Alignment (Text $\leftrightarrow$ Image & Translation)** | [Robson & O'Neill, Ch. 11: "IIIF for Digital Humanities"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_11_Alignment/Companion_2025_Ch11_Robson_ONeill_IIIF_for_Digital_Humanities.pdf) (pp. 190–204: W3C Web Annotations, Mirador, & GitHub annotation tools) | — |
| **W12** | **M12: Digital Scholarly Commentary** | [Stoyanova, Eide, & Türkoglu, Ch. 10: "Modeling Cultural Heritage Materials for Discovery and Analysis"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_12_Commentary/Companion_2025_Ch10_Stoyanova_Eide_Turkoglu_Modeling_Cultural_Heritage.pdf) (pp. 159–178) | [Dase, Ch. 7: "Towards a Model of the Network Edition"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_12_Commentary/NTMRS11_2023_Ch07_Dase_Towards_a_Model_of_the_Network_Edition.pdf) (pp. 158–169) |
| **W13** | **M13: Publication II (Print Codex, ODD, & Archive)** | [Hendriksen, Ch. 11: "Data That Last: Reflections on Sustainability in DH Projects"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_13_Publication/NTMRS11_2023_Ch11_Hendriksen_Data_That_Last_Sustainability.pdf) (pp. 245–258) | [El Khatib, Ch. 3: "The Exigency of *Early Modern Digital Review*"](file:///home/kmpenner/projects/RELS/398/raw/readings/Module_13_Publication/NTMRS11_2023_Ch03_El_Khatib_Early_Modern_Digital_Review.pdf) (pp. 55–73) |

---

## 7. Directory Inventory of Revision Scaffolding

This directory contains ready-to-deploy scaffolding for the future course launch:

* [`revisions/scaffolding/.github/workflows/tei_validate.yml`](file:///home/kmpenner/projects/RELS/398/revisions/scaffolding/.github/workflows/tei_validate.yml): Turnkey CI workflow for student repositories.
* [`revisions/scaffolding/student_repo_template/`](file:///home/kmpenner/projects/RELS/398/revisions/scaffolding/student_repo_template/): Turnkey student starter repository template.
* [`revisions/lesson_blueprints/`](file:///home/kmpenner/projects/RELS/398/revisions/lesson_blueprints/): Detailed lesson plans for Lessons 1.1, 1.2, 2.1, 2.2, and 2.3.
