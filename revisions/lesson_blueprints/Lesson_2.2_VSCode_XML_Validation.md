# Blueprint: Lesson 2.2 — VS Code, RELAX NG Schemas, & CI Validation
## Course: RELS 398 / ENGL 398 · Meeting #4

> **Source Specification:** [`SESSION_CONTENT_SPEC.md`](file:///home/kmpenner/projects/RELS/398/SESSION_CONTENT_SPEC.md) §2.2  
> **Key Reform:** Arriving at the professional code editor (VS Code) only *after* understanding shell mechanics and Git remotes. Integrates local XML schema validation with automated GitHub Actions CI feedback.

---

### Core Learning Objectives
1. Configure Visual Studio Code with the Red Hat XML extension and TEI validator.
2. Differentiate between XML **well-formedness** (syntax rules) and XML **validity** (conformance to a schema grammar).
3. Validate TEI documents against Document Type Definitions (DTDs) and RELAX NG schemas (`msdesc.rng`).
4. Read and interpret schema validation errors in VS Code and in GitHub Actions CI logs.

---

### 50-Minute Classroom Progression

#### 1. Transitioning to VS Code (10 mins)
* Launching VS Code from the terminal: `code .`
* Installing core extensions:
  * **Red Hat XML** (`redhat.vscode-xml`): Real-time syntax highlighting, tag auto-closing, and schema binding.
  * **Scholarly XML** / TEI Validator: TEI-aware autocompletion and element documentation.

#### 2. Schemas & RELAX NG (`msdesc.rng`) (15 mins)
* What a schema does: defines allowed element names, valid child order, required attributes, and datatypes.
* Binding `header.xml` to `schemas/msdesc.rng` via XML processing instruction:
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <?xml-model href="schemas/msdesc.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
  <TEI xmlns="http://www.tei-c.org/ns/1.0">
  ...
  ```
* **Crucial Lesson Concept:** What the schema enforces vs. what it suggests. (Empirically demonstrated: `@material` in `msdesc.rng` suggests values like `perg` or `chart` but does not enforce them, whereas element sequence and attribute spelling are strictly enforced).

#### 3. Inducing and Resolving Schema Errors (15 mins)
* Deliberately breaking the schema in class:
  1. Add an invalid attribute: `<title level="nonsense">`. (VS Code underlines in red: *Attribute "level" not allowed here*).
  2. Put `<publicationStmt>` before `<titleStmt>`. (VS Code flags: *Element publicationStmt not allowed at this position*).
  3. Violate NCName rules: `xml:id="Front page"`. (VS Code flags: *Invalid NCName syntax; spaces forbidden*).
* Local terminal validation:
  ```bash
  xmllint --noout --relaxng schemas/msdesc.rng header.xml
  ```

#### 4. Pushing to GitHub & Observing CI Green Badge (10 mins)
* Commit the schema-bound header:
  ```bash
  git add header.xml
  git commit -m "style: bind header.xml to msdesc.rng schema and resolve validation errors"
  git push origin main
  ```
* Students open their repository's **Actions** tab on GitHub:
  * Watch `.github/workflows/tei_validate.yml` run `xmllint`.
  * Confirm the green checkmark appears on their commit.

#### 5. Exit Ticket / Milestone
* Repository on GitHub passes the automated CI validation gate with 0 schema errors.
