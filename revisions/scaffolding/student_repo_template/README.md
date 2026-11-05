# RELS 398 / ENGL 398 — Digital Edition Repository

**Student Name:** [Your Name]  
**Primary Witness Title:** [Title of Your Historical Document]  
**Repository URI:** `https://github.com/[Organization]/[Your-Repo-Name]`

---

## Repository Purpose & Architecture

This repository holds your working files, ground-truth tables, automated diffs, and validated TEI XML deliverables for **RELS 398.10 / ENGL 398.10: Digital Methods for Historical Documents**.

Every week follows the **Three-Step Comparative Cycle**:
1. **Tuesday (Step 1 - Manual Ground Truth):** Manual analysis and transcription using authoritative dictionaries and primary archival facsimiles.
2. **Wednesday (Step 2 - Deterministic Rule Script):** Algorithmic processing using standard NLP / regex / Python tools (e.g., TreeTagger, SpaCy, IIIF tools).
3. **Friday (Step 3 - AI Model & Synthesized Merge):** Controlled LLM evaluation under strict negative prompts, followed by a three-way diff audit and final merged TEI deliverable.

---

## Directory Structure

```text
├── .github/workflows/
│   └── tei_validate.yml      # Automated GitHub Actions validation on every push
├── schemas/
│   ├── edition.odd            # Progressive TEI ODD customization (updated weekly from Week 5)
│   └── msdesc.rng             # Compiled RELAX NG schema for TEI P5 validation
├── docs/
│   └── WORKFLOW_GUIDE.md      # Step-by-step git, validation, ODD, and submission guide
├── LEDGER.md                  # Your personal editorial policy and settled decisions
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
    ├── Module_12_Commentary/     # Week 12: Historical & Philological Commentary (<standOff>/<note>)
    └── Module_13_Publication/    # Week 13: Print-Ready Codex (Typst/PDF), ODD Docs, & Zenodo Release
```

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
