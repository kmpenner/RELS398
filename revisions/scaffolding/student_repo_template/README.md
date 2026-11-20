# RELS 398 / ENGL 398 — Digital Edition Repository

**Student Name:** [Your Name]  
**Primary Witness Title:** [Title of Your Historical Document]  
**Repository URI:** `https://github.com/[Organization]/[Your-Repo-Name]`  
**Published GitHub Pages URL:** `https://[Organization].github.io/[Your-Repo-Name]/`

---

## Repository Purpose & Architecture

This repository holds your working files, ground-truth tables, automated diffs, progressive TEI ODD customization, validated TEI XML deliverables, and live GitHub Pages web edition for **RELS 398.10 / ENGL 398.10: Digital Methods for Historical Documents**.

Every analytical week follows the **Three-Step Comparative Cycle**:
1. **Tuesday (Step 1 - Manual Ground Truth):** Manual analysis and transcription using authoritative dictionaries and primary archival facsimiles.
2. **Wednesday (Step 2 - Deterministic Rule Script):** Algorithmic processing using standard NLP / regex / Python tools (e.g., TreeTagger, SpaCy, IIIF tools).
3. **Friday (Step 3 - AI Model & Synthesized Merge):** Controlled LLM evaluation under strict negative prompts, followed by a three-way diff audit and final merged TEI deliverable.

---

## Directory Structure

```text
├── .github/workflows/
│   ├── tei_validate.yml         # Automated GitHub Actions XML validation on every push
│   └── pages.yml                # Automated deployment of site/ to GitHub Pages
├── schemas/
│   ├── edition.odd              # Progressive TEI ODD customization (updated weekly from Week 5)
│   └── msdesc.rng               # Compiled RELAX NG schema for TEI P5 validation
├── site/                        # Live GitHub Pages static web edition (CETEIcean + OpenSeadragon)
│   ├── index.html               # 3-pane viewer (Facsimile + Diplomatic/Regularized + Translation)
│   ├── edition.css              # Display + CSS Paged Media (@media print) styles
│   ├── viewer.js                # Zone highlighting, <choice> toggle, link sync, <standOff> popovers
│   └── data/
│       ├── edition.xml          # Canonical TEI P5 edition (starter 1760 Halifax Treaty excerpt)
│       └── treaty_1760_sample.svg
├── docs/
│   └── WORKFLOW_GUIDE.md        # Step-by-step git, validation, ODD, and submission guide
├── LEDGER.md                    # Your personal editorial policy and settled decisions
└── submissions/
    ├── Module_01_Orientation/    # Week 1: Witness Selection, FAIR, & Initial GitHub Commit
    ├── Module_02_Cataloguing/    # Week 2: TEI Header, Authority Control, & CI Validation
    ├── Module_03_IIIF_Imaging/   # Week 3: Archival Imaging & IIIF Manifests
    ├── Module_04_Transcription/  # Week 4: Diplomatic Transcription & 3-Way Reconciliation
    ├── Module_05_Web_Publication/# Week 5: Diplomatic Web Edition (GitHub Pages) & ODD Foundations
    ├── Module_06_Normalization/  # Week 6: Regularization (<choice>), ODD Rules, & Reading View Toggle
    ├── Module_07_Collation/      # Week 7: Multi-Witness Collation (<app>/<lem>/<rdg>), ODD @wit, & Web Apparatus
    ├── Module_08_Lemmatization/  # Week 8: Linguistic Markup (UPOS/FEATS), Closed ODD @pos, & Hover Inspector
    ├── Module_09_Named_Entities/ # Week 9: Named Entity Recognition, ODD @ref, & Prosopography Cards
    ├── Module_10_Translation/    # Week 10: Translation, Interlinear Glossing, & Facing-Column View
    ├── Module_11_Alignment/      # Week 11: Dual Alignment (Text-to-Image @facs & Text-to-Translation <linkGrp>)
    ├── Module_12_Publication_II/ # Week 12: Parallel Web Edition on GitHub Pages & Lightweight Commentary
    └── Module_13_Publication_III/# Week 13: Print Codex, ODD Documentation, Peer Review, & Zenodo Release
```

---

## Previewing Your Live Web Edition Locally

Serve the `site/` folder over local HTTP (do not open directly as `file://` if auto-loading `./data/edition.xml`, or use the **Files** button in the top bar):

```bash
python3 -m http.server 8799 --directory site
```

Then open `http://127.0.0.1:8799/` in your browser. Every push to `main` automatically deploys `site/` to GitHub Pages via `.github/workflows/pages.yml`.

---

## Submission & Grading Protocol

1. **Incremental Commits:** Commit your work at the end of every class meeting:
   * `git commit -m "Step 1 (manual): 20-word ground truth table"`
   * `git commit -m "Step 2 (deterministic): SpaCy parse results"`
   * `git commit -m "Step 3 (ai): three-way diff and merged xml"`
2. **Pre-Push Validation:** Validate your XML locally using `xmllint` before pushing:
   ```bash
   xmllint --noout --relaxng schemas/msdesc.rng submissions/Module_NN_*/transcription_*.xml
   ```
3. **GitHub Actions Green Badge:** Every push triggers automated validation in the **Actions** tab. If your push displays a red cross, click into the logs to see the exact line where your XML violates the schema, fix it, and push again.
4. **Final Weekly Submission:** Create a GitHub Release or Pull Request named `v-module-NN` by Friday at 11:00 PM.
