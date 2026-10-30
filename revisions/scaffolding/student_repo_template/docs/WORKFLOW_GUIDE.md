# Student Git & Validation Workflow Guide
## RELS 398 / ENGL 398: Digital Methods for Historical Documents

This guide outlines the standard terminal commands and editorial practices for managing your digital edition on GitHub.

---

### 1. Daily Session Start: Syncing Your Workspace

Before beginning work on your project:
```bash
# Verify your local branch is clean and up to date
git status
git pull origin main
```

---

### 2. The Three-Step Weekly Commit Cycle

Never write all three stages at once. The integrity of your grade depends on the **commit timestamp audit trail** proving that manual ground truth preceded automated tool testing.

#### Tuesday: Step 1 (Manual Ground Truth)
1. Complete your 20-word ground truth table in your module directory.
2. Draft your manual XML fragment (`witness.xml` or `transcription_manual.xml`).
3. Commit to git:
   ```bash
   git add submissions/Module_NN/
   git commit -m "Step 1: manual ground truth table and initial tei fragment"
   git push origin main
   ```

#### Wednesday: Step 2 (Deterministic NLP / Tool Run)
1. Execute your automated script (TreeTagger, SpaCy, or regex regularizer).
2. Save raw output and benchmark tables to `NLP_BENCHMARK.md`.
3. Commit to git:
   ```bash
   git add submissions/Module_NN/
   git commit -m "Step 2: deterministic parser output and token accuracy benchmark"
   git push origin main
   ```

#### Friday: Step 3 (AI Audit & Synthesized Merge)
1. Query the AI model under strict negative prompt constraints.
2. Conduct the 3-way side-by-side diff in `LINGUISTIC_AUDIT.md`.
3. Synthesize the final validated TEI XML (`transcription_linguistic.xml`).
4. Validate schema before committing:
   ```bash
   xmllint --noout --relaxng schemas/msdesc.rng submissions/Module_NN/*.xml
   ```
5. Commit and tag submission:
   ```bash
   git add submissions/Module_NN/
   git commit -m "Step 3: three-way diff audit and validated merged tei xml"
   git tag -a v-module-NN -m "Submission for Module NN"
   git push origin main --tags
   ```

---

### 3. Troubleshooting GitHub Actions Validation Failures

If your push triggers a **red failure mark** on GitHub:
1. Navigate to the **Actions** tab on your GitHub repository.
2. Click on the failed workflow run named `TEI XML Validation Gate`.
3. Click `Schema Validation (xmllint)` to view the terminal log.
4. Locate the line with `validates fails` or `error :`.
   * *Example:* `transcription.xml:42: element choice: Relax-NG validity error : Expecting element orig, got origg`
5. Open that exact line in VS Code, correct the typo, and push:
   ```bash
   git add .
   git commit -m "fix: resolve schema validation error on line 42"
   git push origin main
   ```
6. Confirm the Actions tab now displays a green checkmark.
