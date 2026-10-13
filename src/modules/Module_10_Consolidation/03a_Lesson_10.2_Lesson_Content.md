# Lesson 10.2 — Automated Schema Validation, CI/CD Gates, and Peer Review

*RELS 398 / ENGL 398 · Topic 10: Consolidation · Meeting #27 (Fri Nov 13)*

*Consolidation meeting — today you establish automated quality assurance for your
digital edition. You will build a multi-tiered validation pipeline using Relax NG,
Schematron, and GitHub Actions CI/CD, enforce branch protection gates, and conduct an
in-class peer review exchange across our seminar editions.*

---

## **01 Content**

**The Quality Assurance Gate in Textual Scholarship**

A digital edition requires high editorial standards. If an edition has broken tags, scholars cannot trust it. If metadata or links are missing, citation fails. Quality assurance is the careful process of checking files. It verifies that files meet technical and scholarly standards.

In digital editing, quality assurance relies on two complementary gates:

<table class="table table-bordered my-3">
<thead>
<tr>
<th>Quality Assurance Gate</th>
<th>Primary Instrument</th>
<th>What It Verifies</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Automated Validation Gate</strong></td>
<td>Software parsers (`xmllint`, Relax NG, Schematron, GitHub Actions)</td>
<td>Well-formedness, tag syntax, schema grammar, and attribute co-occurrence rules.</td>
</tr>
<tr>
<td><strong>Human Peer Review Gate</strong></td>
<td>Scholarly peers and editorial boards</td>
<td>Transcription fidelity, paleographical readings, historical accuracy, and interpretive insight.</td>
</tr>
</tbody>
</table>

Computers check rules fast. They scan thousands of lines in seconds. Humans provide historical judgment. Combining automated checks with human review gives your edition stability. It also ensures scholarly quality.

**Vocabulary.** *Quality Assurance (QA)* — The careful testing and verification of files against defined technical standards. *Dual-Gate Design* — Pairing automated software checks with human peer review to evaluate digital editions.

**Takeaway:** A dependable digital scholarly edition requires both automated software validation and human peer review.

---

## **02 Content**

**The Fragility of Local Desktop Validation**

During class, you validated XML in VS Code. You looked for red squiggly lines. Local validation helps during drafting. But relying only on your laptop is risky.

Local settings drift over time. One student might use an old schema. Another might ignore red squiggly lines. A third might forget to run checks before committing.

This creates a common trap: "It works on my machine!" When Ace clones Olyvia's repository, he may discover errors. Her local editor hid those mistakes. Automated workflows ensure consistency. Every file is tested against identical standards on an independent cloud server.

**Vocabulary.** *Local Settings Drift* — When individual desktop software settings, schemas, or extensions become outdated or inconsistent across a team. *Centralized Validation* — Running standardized automated tests on a shared remote server rather than individual laptops.

**Takeaway:** Local laptop validation is convenient for drafting, but centralized automated checks guarantee consistency across a project.

---

## **03 Content**

**The Multi-Tiered Validation Hierarchy**

Validation is not a single test. In digital editing, quality control operates across three levels. Each tier increases in strictness:

<table class="table table-bordered my-3">
<thead>
<tr>
<th>Validation Tier</th>
<th>Standard Technology</th>
<th>Core Question Answered</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tier 1: Syntax</strong></td>
<td>XML Well-Formedness (`xmllint`)</td>
<td>Is the document syntactically legal XML with closed, nested tags?</td>
</tr>
<tr>
<td><strong>Tier 2: Grammar</strong></td>
<td>RELAX NG Schema (`msdesc.rng`, `tei_all.rng`)</td>
<td>Do elements and attributes follow TEI structure rules and data types?</td>
</tr>
<tr>
<td><strong>Tier 3: Semantics</strong></td>
<td>ISO Schematron (`.sch`)</td>
<td>Do attributes follow project rules, cross-references, and conditional rules?</td>
</tr>
</tbody>
</table>

Each tier builds on the last level. A file must pass Tier 1 first. Then a schema checks Tier 2. Next, Schematron tests Tier 3 rules.

**Vocabulary.** *Validation Hierarchy* — A three-tiered system of testing XML files for syntax, structure rules, and semantic rules. *Project Rules* — Project-specific editorial rules that go beyond generic schema constraints.

**Takeaway:** Digital editions validate across three tiers: clean syntax, grammatical schemas, and semantic rules.

---

## **04 Content**

**Tier 1 Validation: XML Well-Formedness and Parser Mechanics**

Tier 1 validation checks **well-formedness**. Well-formedness is the basic syntax foundation set by the W3C.

An XML parser does not care about TEI rules. It ignores manuscripts. It only checks syntax. A document is well-formed if:

1. It contains exactly one root element enclosing all other tags.
2. Every start tag matches an end tag with identical spelling and case.
3. Elements nest cleanly without overlapping boundaries.
4. All attribute values are wrapped in matching quotation marks.

If a file breaks any of these rules, the parser stops. It reports a **fatal error**. Web browsers guess meaning when HTML is broken. XML parsers never guess. You test Tier 1 in your terminal using `xmllint`:

```bash
xmllint --noout witness.xml
```

**Vocabulary.** *Well-Formed XML* — XML text that strictly obeys basic syntax rules, allowing parsers to build a tree structure. *Fatal Error Policy* — The XML rule requiring software to stop parsing immediately when a syntax error is found.

**Takeaway:** Well-formedness is the non-negotiable syntactic baseline required before any schema validation can occur.

---

## **05 Content**

**Tier 2 Validation: Grammar-Based Schemas with RELAX NG**

Once your file is well-formed, Tier 2 evaluates its **validity**. A well-formed XML file can still contain invented tags like `<magic>` or `<cookie>`. Tier 2 checks your markup against a formal schema.

In the TEI community, the standard schema is **RELAX NG**. RELAX NG defines the allowed tags and grammar for an edition:

- It controls which elements may appear inside other elements.
- It specifies the required sequence of child elements.
- It defines which attributes are permitted on specific tags.
- It checks data types for attribute values, such as dates.

In this course, we test files against `msdesc.rng` or `tei_all.rng`. If Andromeda puts a `<p>` inside `<extent>`, RELAX NG catches it. The tool flags the mistake right away.

**Vocabulary.** *RELAX NG* — A powerful, modern schema language used by the TEI to specify element structures and attributes. *Schema Validity* — Conforming strictly to the structure rules and element rules of an official schema.

**Takeaway:** RELAX NG schemas enforce the structure rules, element ordering, and attribute types of your digital edition.

---

## **06 Content**

**The Limits of Grammar: What RELAX NG Cannot Catch**

RELAX NG checks structure rules well. But it has natural blind spots. RELAX NG cannot easily test conditional relationships across different parts of a file.

Consider these common editorial needs:

- If a `<persName>` has `type="deputy"`, it should require a `@ref` pointing to a person in the header.
- If a `<date>` tag contains text, its `@when` attribute should match the ISO format `YYYY-MM-DD`.
- If an editor tags a `<corr>` element, there must be a matching `<sic>` element inside a parent `<choice>`.
- Every local reference (such as `who="#editor"`) must resolve to a real `xml:id` defined in the file.

RELAX NG evaluates tags in isolation. It cannot evaluate complex conditional rules. To enforce these editorial guidelines, we need Tier 3 validation: Schematron.

**Vocabulary.** *Co-Occurrence Constraint* — A rule where the presence or value of one attribute depends on another attribute. *Context Rule* — An editorial condition that cannot be expressed purely through hierarchical tree grammar.

**Takeaway:** Grammar schemas cannot enforce cross-element conditional rules, creating the need for rule-based Schematron validation.

---

## **07 Content**

**Tier 3 Validation: ISO Schematron (ISO/IEC 19757-3)**

**Schematron** is a rule-based validation language. It is standardized under ISO/IEC 19757-3. RELAX NG describes an entire document tree from the top down. In contrast, Schematron makes targeted queries using XPath.

Schematron searches for specific patterns in text. When it finds a tag, it tests an assertion. If that test fails, Schematron prints a clear note. Project editors write these notes in plain English.

This makes Schematron friendly for scholars. Traditional parser warnings can be cryptic, like `element choice unexpected at this position`. Schematron prints plain language:

> "Error in French decree line 24: Every <orig> tag must be accompanied by a <reg> tag inside <choice>."

Schematron acts as an automated editorial supervisor. It checks project guidelines with high precision.

**Vocabulary.** *Schematron* — An ISO standard rule-based XML validation language based on XPath assertions. *XPath* — A query language used to select elements and evaluate expressions inside an XML document.

**Takeaway:** Schematron uses XPath to enforce project-specific editorial rules and emit plain-language error messages.

---

## **08 Content**

**Authoring Schematron Rules for Scholarly Editions**

Writing Schematron rules is straightforward. A Schematron file contains three main building blocks: patterns, rules, and assertions.

Here is a practical Schematron rule designed for our class editions:

```xml
<pattern id="check-dates">
  <rule context="tei:date[@when]">
    <assert test="matches(@when, '^\d{4}(-\d{2}(-\d{2})?)?$')">
      The @when attribute must follow ISO format: YYYY, YYYY-MM, or YYYY-MM-DD.
    </assert>
  </rule>
</pattern>
```

Let us look at how this works:

- `<rule context="...">`: Specifies the target elements. It selects every `<date>` tag that has a `@when` attribute.
- `<assert test="...">`: States the mandatory condition that must evaluate to true. Here, it checks that the date matches standard year, month, and day patterns.
- Error Message: The text inside `<assert>` is displayed to the student if the test fails.

When Olyvia types `when="Feb 13 1967"`, Schematron catches the informal date format. It tells her how to fix it.

**Vocabulary.** *Rule Context* — The XPath selector identifying which XML elements a Schematron rule applies to. *Schematron Assertion* — A condition that must be true; if false, its enclosed warning message is displayed.

**Takeaway:** Schematron patterns select target elements and test assertions, guiding editors with helpful error messages.

---

## **09 Content**

**Enforcing Cross-Reference and Identifier Integrity**

One of the best uses of Schematron is enforcing **identifier integrity**. In TEI XML, elements point to each other using internal links. Examples include `@ref="#cope"` or `@who="#editor"`.

Suppose Andromeda points to `#cope` in the treaty text. But she forgot to define `xml:id="cope"` in the `<teiHeader>`. The link is broken. RELAX NG cannot detect this missing link.

A simple Schematron rule checks every internal reference automatically:

```xml
<pattern id="check-internal-links">
  <rule context="tei:*[@ref[starts-with(., '#')]]">
    <assert test="//tei:*[@xml:id = substring-after(current()/@ref, '#')]">
      Broken reference: The target '<value-of select="@ref"/>' does not match any xml:id in this edition.
    </assert>
  </rule>
</pattern>
```

This automated check protects your edition. It verifies that all person, place, and organization references resolve to valid entities before you publish.

**Vocabulary.** *Identifier Integrity* — Guaranteeing that every local pointer or reference resolves to a valid, existing `xml:id`. *value-of* — A Schematron tag that inserts the value of an attribute directly into an error message.

**Takeaway:** Schematron rules verify that all internal links and person references resolve to defined identifiers in your edition.

---

## **10 Content**

**Validating Linguistic and Attribute Co-Occurrences**

In Module 8, you added linguistic tags to your witness. You marked words with `<w lemma="..." pos="...">`. Maintaining consistency across thousands of words requires automated testing.

Schematron easily enforces linguistic markup consistency:

<table class="table table-bordered my-3">
<thead>
<tr>
<th>Editorial Rule</th>
<th>Schematron Assertion</th>
<th>What It Prevents</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Lemma Completeness</strong></td>
<td><code>test="@lemma and string-length(@lemma) > 0"</code></td>
<td>Prevents tagging a word with `<w>` while forgetting its dictionary headword.</td>
</tr>
<tr>
<td><strong>Valid POS Tags</strong></td>
<td><code>test="@pos = ('NOUN', 'VERB', 'ADJ', 'PRON', 'DET', 'ADP')"</code></td>
<td>Catches typos like `pos="VERBB"` or non-standard part-of-speech codes.</td>
</tr>
<tr>
<td><strong>Regularization Pairs</strong></td>
<td><code>test="tei:orig and tei:reg"</code></td>
<td>Ensures `<choice>` elements include both historical original and regularized form.</td>
</tr>
</tbody>
</table>

When Ace encodes French decree verbs, these checks confirm every inflected form. Each word links to its canonical infinitive.

**Vocabulary.** *Linguistic Consistency* — Ensuring that all words share standardized grammatical categories and canonical lemmas. *Attribute Whitelist* — An explicit list of permitted values checked by a validation rule.

**Takeaway:** Schematron guards linguistic annotations by checking that words carry canonical lemmas and valid part-of-speech codes.

---

## **11 Content**

**Compiling and Executing Schematron via XSLT Engines**

You might wonder how a computer runs Schematron. Behind the scenes, Schematron relies on XSLT (Extensible Stylesheet Language Transformations).

A Schematron file (`.sch`) compiles into an XSLT stylesheet. It uses a standard three-stage pipeline. When that compiled XSLT runs against your TEI document, it outputs an SVRL report. SVRL stands for Schematron Validation Report Language.

In practice, you run Schematron in the terminal using **Jing**:

```bash
jing -c schema.rnc witness.xml
jing schema.sch witness.xml
```

Jing reads the Schematron file. It scans your TEI document. It prints line numbers for every rule violation. This terminal command lets us automate validation inside build scripts and CI pipelines.

**Vocabulary.** *Jing* — An open-source command-line validator for RELAX NG and Schematron schemas written by James Clark. *SVRL* — Schematron Validation Report Language, the standard XML format used to report Schematron results.

**Takeaway:** Tools like Jing execute Schematron rules on the command line, enabling automated validation in scripts and CI pipelines.

---

## **12 Content**

**Introduction to Continuous Integration (CI/CD) for Digital Humanities**

Running `xmllint` and `jing` by hand in the terminal is a good habit. But people are forgetful. An editor working late at night might push a commit without running tests.

Modern software engineering solves this with **Continuous Integration (CI)**. Continuous Integration is the practice of automatically testing a project every time code is pushed to a shared repository.

In digital editing, CI acts as an automated gatekeeper. When Ace, Olyvia, or Andromeda pushes a commit, a cloud runner starts. It downloads the files. It runs `xmllint`. It checks Relax NG. It tests Schematron rules.

If all checks pass, the commit gets a green check (`✔`). If any check fails, it gets a red cross (`✖`). The author gets an alert right away.

**Vocabulary.** *Continuous Integration (CI)* — Automating tests and validation checks on a cloud server whenever repository commits are pushed. *CI Pipeline* — The sequence of automated steps executed by a CI server to verify project integrity.

**Takeaway:** Continuous Integration automatically tests every commit in the cloud, guaranteeing that broken files never go unnoticed.

---

## **13 Content**

**Anatomy of a GitHub Actions Workflow**

On GitHub, Continuous Integration is provided through **GitHub Actions**. A workflow is an automated procedure. It is defined in a YAML configuration file stored at `.github/workflows/validate.yml`.

A GitHub Actions workflow consists of four core concepts:

1. **Events (Triggers):** What starts the workflow? Common triggers are a `push` to `main` or opening a `pull_request`.
2. **Runners:** The virtual machine that executes your tests (such as `ubuntu-latest`, a clean Linux cloud server).
3. **Jobs:** A collection of steps executed on the runner.
4. **Steps:** Individual tasks, such as checking out code, installing software, or running terminal commands.

Workflows are saved as plain text files in your repository. Therefore, your testing rules are version-controlled alongside your text.

**Vocabulary.** *GitHub Actions* — GitHub's built-in platform for automating software workflows, testing, and continuous integration. *Workflow YAML* — A human-readable configuration file specifying triggers, environments, and test commands.

**Takeaway:** GitHub Actions workflows are version-controlled YAML files that define automated testing triggers and commands.

---

## **14 Content**

**Writing a Complete TEI Validation Workflow**

Let us examine a complete GitHub Actions workflow for a TEI digital edition.

Here is `.github/workflows/validate.yml`:

```yaml
name: TEI Edition Validation Gate

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository code
        uses: actions/checkout@v4

      - name: Install XML validation tools
        run: sudo apt-get update && sudo apt-get install -y libxml2-utils jing

      - name: Verify XML Well-Formedness
        run: xmllint --noout witness.xml

      - name: Validate TEI Relax NG Schema
        run: jing schemas/msdesc.rng witness.xml
```

Notice how clean this is. Every step matches commands you already ran locally. The cloud runner boots up, installs `xmllint` and `jing`, and runs your tests in under twenty seconds.

**Vocabulary.** *actions/checkout* — A standard GitHub action that downloads your repository code onto the cloud virtual machine. *ubuntu-latest* — The default Linux cloud environment provided by GitHub for running automated jobs.

**Takeaway:** A twenty-line YAML file configures GitHub Actions. It installs XML tools and tests your files on every push.

---

## **15 Content**

**Integrating Community Validation Actions**

Besides running raw terminal commands, you can use shared actions. The open-source digital humanities community shares many useful tools.

For instance, the TEI community shares actions that download official schemas automatically. You do not need to store large schema files in your repository. Instead, a workflow step fetches the canonical schema:

```yaml
      - name: Download Canonical TEI All Schema
        run: curl -s https://tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng -o tei_all.rng
```

Remote schema downloads ensure you test against official releases. This keeps your repo small. It also ensures international standards compliance.

**Vocabulary.** *Community Action* — A reusable workflow component published on the GitHub Actions Marketplace. *Canonical Schema URL* — The official, permanent web address where authoritative schema definitions are hosted.

**Takeaway:** Community actions and remote schema downloads keep repository sizes small while validating against official TEI releases.

---

## **16 Content**

**Associating Documents and Schemas: `<?xml-model?>`**

How does a computer know which schema belongs to an XML document? In TEI P5, we associate schemas using **processing notes**. We place them at the very top of the file, before `<TEI>`.

A standard TEI document begins with `<?xml-model?>` declarations:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="schemas/msdesc.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="schemas/rules.sch" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
```

Notice that we include two separate `<?xml-model?>` lines:

- The first line links the Relax NG structural schema (`.rng`).
- The second line links the Schematron rule file (`.sch`).

When VS Code or automated validators open your document, they read these lines. They automatically apply both validation tiers.

**Vocabulary.** *Processing Note* — A special XML declaration (`<?...?>`) providing instructions to software processing the document. *xml-model* — The standard W3C processing instruction that associates an XML file with its schema.

**Takeaway:** The xml-model processing instruction links both Relax NG and Schematron schemas directly inside the XML document header.

---

## **17 Content**

**Converting CI Failures to Inline GitHub Annotations**

When a CI workflow fails on GitHub, finding the error is easy. You do not have to read thousands of lines of terminal logs.

GitHub Actions turns validation output into visual **annotations**. When `xmllint` or `jing` reports an error on line 64, GitHub flags that line. It shows a yellow warning or red error badge in the pull request diff.

Clicking on the badge opens the exact message:

> "Error: element persName missing required attribute ref at line 64, column 12."

This quick feedback loop helps authors fix mistakes fast. You see the line. You read the error. You fix it in VS Code and push an update.

**Vocabulary.** *GitHub Annotation* — A visual inline alert displayed on a pull request diff highlighting the line where a CI test failed. *Feedback Loop* — The rapid cycle of making changes, receiving automated test results, and correcting mistakes.

**Takeaway:** GitHub CI automatically displays validation errors as inline visual annotations on the exact lines that caused the failure.

---

## **18 Content**

**Protecting Branches with Automated CI Merge Gates**

Running automated tests is useful. But what prevents someone from merging broken code anyway? The answer is **Branch Protection Rules**.

GitHub lets repository owners set protection rules on the `main` branch:

<table class="table table-bordered my-3">
<thead>
<tr>
<th>Protection Setting</th>
<th>What It Enforces</th>
<th>Scholarly Benefit</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Require status checks to pass</strong></td>
<td>The green "Merge" button is disabled until the validation workflow passes with 0 errors.</td>
<td>Guarantees that broken XML or invalid schemas can never enter the official master text.</td>
</tr>
<tr>
<td><strong>Require pull request reviews</strong></td>
<td>At least one peer reviewer must formally approve the PR before merging.</td>
<td>Ensures all textual changes receive human scholarly review.</td>
</tr>
<tr>
<td><strong>Do not allow bypassing</strong></td>
<td>Applies the rules to repository administrators and instructors as well.</td>
<td>Enforces equal accountability and disciplined version-control habits across the team.</td>
</tr>
</tbody>
</table>

With branch protection on, your CI pipeline becomes a mandatory gate. Quality rules are enforced automatically by software.

**Vocabulary.** *Branch Protection Rule* — A safety rule on GitHub that blocks direct pushes and prevents merging until checks pass. *Merge Gate* — A mandatory validation test that must succeed before a pull request can be merged.

**Takeaway:** Branch protection rules disable the merge button until all automated validation tests pass with zero errors.

---

## **19 Content**

**Automated Preview and Artifact Compilation in CI**

Continuous Integration does more than catch mistakes. Modern digital projects use CI to **compile edition artifacts** automatically on every push.

In Module 7, you made stylesheets to turn TEI XML into HTML reading views. In this course, we also compile printable PDF notes. You can configure GitHub Actions to build these views automatically:

```yaml
      - name: Compile HTML Reading View
        run: python3 scripts/generate_reading_view.py witness.xml dist/index.html

      - name: Deploy Preview to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```

When a pull request merges into `main`, GitHub Actions rebuilds the reading view. It publishes the pages to GitHub Pages. Reviewers can read the live edition in any browser.

**Vocabulary.** *Artifact Compilation* — Automatically transforming raw TEI XML source files into user-friendly formats like HTML or PDF. *GitHub Pages* — A free hosting service provided by GitHub to serve static websites directly from a repository.

**Takeaway:** CI workflows can automatically transform raw TEI XML into web reading views and publish them live to GitHub Pages.

---

## **20 Content**

**The Boundary Between Automated Linting and Human Peer Review**

Automated CI pipelines are powerful, but they have natural limits. Software verifies whether XML is well-formed. It checks whether attributes follow a schema. It verifies whether links resolve.

However, software cannot determine whether your transcription is **true**:

- Software cannot tell whether a scribal stroke in Maud Lewis's letter is an *e* or an *o*.
- Software cannot know whether an omitted word in Ace's French decree was deliberate or accidental.
- Software cannot evaluate whether Andromeda chose the best treaty translation.

Automated linting handles the basic mechanics. This frees human reviewers to focus on paleographical judgment, historical context, and scholarly rigor.

**Vocabulary.** *Basic Mechanics* — The basic syntactic and grammatical correctness verified automatically by software. *Scholarly Insight* — The critical human evaluation of historical evidence, paleography, and context.

**Takeaway:** Software enforces mechanical validity, freeing human scholars to focus on paleographical judgment and historical interpretation.

---

## **21 Content**

**Designing a Structured TEI Peer-Review Rubric**

When reviewing a classmate's edition, helpful feedback requires a rubric. Without a rubric, reviews become vague comments like "looks good to me!"

A scholarly review rubric evaluates four distinct layers:

1. **Metadata and Codicology (`teiHeader`):** Are the repository, shelfmark, and license accurately recorded?
2. **Diplomatic Fidelity (`<facsimile>` & `<text>`):** Do line breaks (`<lb/>`) and characters match the high-resolution manuscript image?
3. **Editorial Normalization (`<choice>`):** Are regularized spellings and expanded abbreviations historically defensible?
4. **Entity Markup & Linking (`<persName>`, `<placeName>`):** Do entity tags resolve to verifiable authority records like VIAF or Wikidata?

This structured rubric guides your evaluation during our in-class peer review exchange.

**Vocabulary.** *Peer-Review Rubric* — A standardized set of criteria used to evaluate the scholarly and technical quality of an edition. *Editorial Layer* — A distinct level of annotation within a multi-tiered digital edition.

**Takeaway:** A structured four-layer rubric ensures that peer review evaluates metadata, diplomatic fidelity, normalization, and entity markup.

---

## **22 Content**

**Auditing the `teiHeader` and Provenance Layer**

The first stage of peer review evaluates the `<teiHeader>`. The header is the identity card of the edition. If the header is incomplete, future scholars cannot cite the document reliably.

When auditing a classmate's header, check these four items:

<table class="table table-bordered my-3">
<thead>
<tr>
<th>Header Component</th>
<th>What to Verify</th>
<th>Common Error to Flag</th>
</tr>
</thead>
<tbody>
<tr>
<td><code><titleStmt></code></td>
<td>Author, title, and responsible student editor defined with `@xml:id`.</td>
<td>Missing student editor name or placeholder "Title goes here" text.</td>
</tr>
<tr>
<td><code><publicationStmt></code></td>
<td>Clear open license (such as Creative Commons CC BY 4.0).</td>
<td>Undefined availability or restrictive copyright claims.</td>
</tr>
<tr>
<td><code><sourceDesc></code></td>
<td>Holding archive, shelfmark, physical support, and date.</td>
<td>Incomplete physical description or missing institution name.</td>
</tr>
<tr>
<td><code><revisionDesc></code></td>
<td>Chronological log of revisions recording commits and PRs.</td>
<td>Empty revision history with no record of past editorial changes.</td>
</tr>
</tbody>
</table>

A complete header guarantees your edition follows FAIR principles (Findable, Accessible, Interoperable, and Reusable).

**Vocabulary.** *sourceDesc* — The TEI Header element recording the physical holding institution, shelfmark, and provenance of the original witness. *FAIR Data Principles* — International guidelines ensuring digital scholarship is Findable, Accessible, Interoperable, and Reusable.

**Takeaway:** Auditing the teiHeader verifies that physical holding archives, licenses, and revision histories are thoroughly documented.

---

## **23 Content**

**Auditing Diplomatic Transcription and Physical Milestones**

The second stage of peer review audits the diplomatic transcription against visual evidence. Open your classmate's manuscript image side by side with their TEI XML in VS Code.

As a reviewer, read the text line by line:

- **Line Breaks (`<lb/>`):** Does every `<lb/>` tag match a physical line start on the page?
- **Character Accuracy:** Did the transcriber misread letterforms, such as confusing long *s* with *f* in French?
- **Damage and Ambiguity:** Are torn regions tagged with `<unclear>` or `<gap>`?
- **Zone Links:** Does the `@facs` attribute point to the correct coordinate zone on the image?

If you spot an alternative reading, do not fix it in secret. Open a comment on GitHub. Explain what handwriting strokes support your reading.

**Vocabulary.** *Diplomatic Audit* — A line-by-line verification comparing transcribed XML characters directly against high-resolution manuscript images. *Physical Milestone* — An empty XML tag (like `<pb/>` or `<lb/>`) marking a physical transition in the original witness.

**Takeaway:** Auditing diplomatic transcription requires comparing every character, line break, and unclear stroke against high-resolution facsimiles.

---

## **24 Content**

**Auditing Normalization, Rendering, and Stylesheets**

The third stage of peer review evaluates editorial regularizations and reading stylesheets developed in Modules 6 and 7.

Inspect how your classmate regularized historical language:

- **Symmetry of `<choice>`:** Does every `<choice>` contain a balanced pair (such as `<orig>` with `<reg>`, or `<abbr>` with `<expan>`)?
- **Historical Accuracy:** In Ace's 1791 decree, did he accurately normalize Voltairean *-oit* spelling endings (such as *décrétoit* to *décrétait*)? In Andromeda's treaty, are 18th-century abbreviations expanded accurately?
- **Stylesheet Legibility:** Open their HTML reading view in a browser. Does the CSS clearly distinguish between diplomatic and regularized views? Can readers toggle layers comfortably?

A strong edition respects both historical authenticity and modern readability. Reviewers ensure that normalization rules were applied consistently rather than haphazardly.

**Vocabulary.** *Regularization Audit* — Evaluating whether historical spelling changes and abbreviation expansions are applied consistently. *Reading View Toggle* — A stylesheet mechanism allowing readers to switch between diplomatic and modern reading modes.

**Takeaway:** Auditing normalization ensures that historical spelling choices are linguistically sound and render clearly in stylesheets.

---

## **25 Content**

**Auditing Linguistic Markup and Named Entities**

The fourth stage of peer review evaluates the grammatical and named-entity annotations added in Modules 8 and 9.

Review these semantic layers:

<table class="table table-bordered my-3">
<thead>
<tr>
<th>Annotation Layer</th>
<th>Inspection Checklist</th>
<th>Concrete Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Linguistic Markup (`<w>`)</strong></td>
<td>Verify that part-of-speech tags and dictionary lemmas are accurate.</td>
<td>Confirming *promis'd* has lemma *promise* and `pos="VERB"`.</td>
</tr>
<tr>
<td><strong>Named Entities</strong></td>
<td>Check that people, places, and organizations are correctly tagged.</td>
<td>Confirming `<persName>` wraps *Jean-Baptiste Cope* and `<placeName>` wraps *Chigabenakady*.</td>
</tr>
<tr>
<td><strong>Authority Links</strong></td>
<td>Click every `@ref` link to ensure it opens a real VIAF, GeoNames, or Wikidata page.</td>
<td>Verifying that VIAF ID `61536214` resolves to François-Claude-Amour de Bouillé.</td>
</tr>
</tbody>
</table>

Checking authority links is vital. A broken VIAF link hurts your connection to Linked Open Data.

**Vocabulary.** *Semantic Audit* — Verifying that grammatical tags, named entities, and authority record links represent true historical data. *Authority Link Resolution* — Confirming that external URIs (like VIAF or Wikidata) resolve to the correct real-world entity.

**Takeaway:** Auditing linguistic and entity markup confirms that lemmas are canonical and authority links resolve to verified records.

---

## **26 Content**

**Executing the In-Class Peer Review Exchange**

During today's in-class lab, our three cohort members execute a peer review exchange:

- **Ace** reviews **Olyvia's** Maud Lewis correspondence edition.
- **Olyvia** reviews **Andromeda's** 1752 Peace and Friendship Treaty edition.
- **Andromeda** reviews **Ace's** 1791 French Revolutionary decree edition.

Follow this four-step peer review protocol:

1. **Clone the Repository:** Clone your partner's repository from GitHub to your laptop.
2. **Run Automated CI Checks:** Run `xmllint` and `jing` in your terminal to verify their automated validation passes.
3. **Conduct the 4-Layer Audit:** Inspect their header, facsimiles, normalizations, and entities against the rubric.
4. **Open Constructive Issues:** Open at least two clear GitHub Issues or inline PR comments praising strong encoding and suggesting specific improvements.

Reviewing a classmate's edition sharpens your own editorial eye and strengthens the collective quality of our seminar's editions.

**Vocabulary.** *Peer Review Exchange* — A structured in-class partnership where students audit each other's digital editions. *Helpful Feedback* — Actionable, respectful criticism that identifies specific problems and provides clear solutions.

**Takeaway:** The in-class peer review exchange allows students to test each other's editions against automated checks and scholarly rubrics.

---

## **27 Content**

**Case Study: Digital Scholarly Publishing and Traveling Validation**

To see automated validation operating in major digital humanities publishing, examine the **Digital Latin Library (DLL)**, a joint initiative of the Society for Classical Studies and the Medieval Academy of America.

The DLL publishes born-digital Latin editions in its *Library of Digital Latin Texts* (LDLT). Instead of sending printed books to a press, scholars submit Git repos containing TEI XML.

The DLL uses a CI pipeline called the "Traveling Imprimatur." When an editor submits work, the CI server tests Relax NG and Schematron rules. If tests pass, the edition advances to human peer review. Once approved, the edition receives a digital certificate of scholarly quality.

**Vocabulary.** *Digital Latin Library (DLL)* — A major scholarly publishing platform that peer-reviews and publishes open-access digital Latin editions. *Traveling Imprimatur* — An automated cryptographic certificate confirming an edition passed all schema and editorial validation gates.

**Takeaway:** Major publishing platforms like the Digital Latin Library use automated CI pipelines as formal gateways to scholarly publication.

---

## **28 Content**

**Digital Longevity and the Endings Project Principles**

When building digital editions, scholars must consider digital longevity. Hundreds of early digital humanities projects from the 1990s and 2000s are now completely dead. They relied on complex databases and old plugins. These tools broke when grant funding ended.

To prevent digital decay, the University of Victoria established **The Endings Project**. The Endings Project defines five principles for long-term digital preservation:

1. **Static Files Only:** Rely on static HTML, CSS, and plain XML. Avoid server-side databases (like MySQL or PHP) that require ongoing maintenance.
2. **Standards Compliance:** Use open, international standards (like W3C XML and TEI P5) that any modern computer can parse.
3. **Self-Contained Data:** Keep all metadata, text, and stylesheets inside the repository rather than relying on external dynamic servers.
4. **Platform Independence:** Ensure the edition can run locally from a USB drive or static web host without special server software.
5. **No Dynamic Vulnerabilities:** Static files have no database security holes and can survive safely for decades.

Building your edition in clean TEI XML with CSS ensures your work stays readable twenty years from now.

**Vocabulary.** *The Endings Project* — A digital humanities research initiative defining technical standards for long-term preservation of digital editions. *Digital Longevity* — The capacity of digital resources to remain accessible, functional, and citeable over decades.

**Takeaway:** The Endings Project principles mandate static, open-standard files to ensure digital editions survive for decades without maintenance.

---

## **29 Content**

**Archiving, Persistent Identification, and FAIR Data**

GitHub is an outstanding platform for active collaboration and continuous integration. However, GitHub is a commercial company. It is not an archival repository. Long-term scholarly preservation requires depositing your edition in an academic data repository.

When your edition is finished, archive a release on **Zenodo**. Zenodo is an open research repository run by CERN:

- **Permanent Digital Object Identifier (DOI):** Zenodo mints a permanent, citable DOI (such as `10.5281/zenodo.1234567`) for your repository snapshot.
- **Automated GitHub Integration:** You can link GitHub directly to Zenodo so that every new GitHub Release is archived automatically.
- **FAIR Compliance:** Zenodo guarantees permanent bit-level preservation, indexing your metadata in international academic search engines.

Archiving your consolidated repo gives your scholarship a permanent home. It becomes citable in the global academic record.

**Vocabulary.** *Zenodo* — An open-access scholarly repository operated by CERN that provides permanent storage and DOIs for research data. *Digital Object Identifier (DOI)* — A persistent, unique alphanumeric string used to permanently identify and cite academic publications.

**Takeaway:** Archiving releases to Zenodo mints permanent DOIs. It guarantees long-term preservation.

---

## **30 Content**

**The Consolidated Milestone: Looking Ahead to Final Publication**

Congratulations! You have completed the mid-term consolidation milestone for RELS 398.

Look at how far your digital edition has advanced:

- You built a codicological `<teiHeader>` cataloguing your witness.
- You linked high-resolution `<facsimile>` images with coordinate zones.
- You created diplomatic and AI-reconciled transcriptions.
- You regularized historical orthography using `<choice>` tags.
- You designed responsive reading views with CSS.
- You enriched your text with grammatical lemmatization and named entities.
- Today, you united all these layers under automated CI validation and collaborative peer review.

Next week, in Module 11, we begin Phase 3: **Advanced Publication and Interactive Presentation**. You will turn your consolidated edition into web interfaces and interactive tools.

**Vocabulary.** *Consolidated Edition* — A unified digital scholarly edition integrating metadata, facsimile, transcription, regularization, and entity layers. *Project Milestone* — A major project stage where all underlying data layers are validated and prepared for publication.

**Takeaway:** Completing the consolidation milestone unites nine editorial layers under automated CI gates, preparing your edition for publication.

---
