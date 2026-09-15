# Lesson 10.2 — Collaborative Peer Review, Schema Validation Sweeps, and CI/CD

*RELS 398 / ENGL 398 · Topic 10: Consolidation · Meeting #27 (Fri Nov 13)*

*Consolidation week — the second of two meetings. Today you conduct a systematic
validation sweep across every TEI layer produced to date, configure automated
continuous integration workflows with GitHub Actions, and execute structured
human peer reviews using rubrics. **The Linguistic Markup Assignment is due today.***

---

## **01 Content**

**The Quality Assurance Gate in Textual Scholarship**

In classical and medieval philology, the integrity of a critical edition has
always depended upon rigorous quality assurance. In the print era, this assurance
was maintained through multiple rounds of proofs: publishers, editors, and
external readers combed through dense typesetting to detect transposed letters,
faulty punctuation, misattributed variant sigla, and erroneous manuscript shelfmarks
(Huskey, 2024). In digital scholarly editing, where texts are encoded in complex
hierarchical XML containing thousands of tags, attributes, and cross-references,
the need for quality control is amplified by an order of magnitude. A single
unclosed bracket, mismatched attribute value, or broken witness pointer can crash
rendering engines, corrupt search indexes, and invalidate downstream computational
analyses (TEI Consortium, 2026).

To guarantee scholarly reliability without overwhelming human editors, modern
digital humanities projects establish a **dual-gate quality assurance
architecture** (Huskey, 2024; Witt, 2018). This architecture separates quality
control into two complementary, non-overlapping domains: automated machine
validation and structured human peer review. Automated validation serves as the
first gate, checking syntactic well-formedness, structural grammar conformance,
and formal business logic before any human being reads the text. Structured peer
review serves as the second gate, evaluating philological fidelity, paleographical
judgment, lexical accuracy, and interpretive nuance.

Today's meeting executes this comprehensive quality assurance sweep across your
consolidated edition. You will audit the nine methodological layers constructed
across the term, configure automated GitHub Actions Continuous Integration (CI)
pipelines to enforce XML and Schematron schemas on every commit, and engage in an
in-class peer-review exchange to evaluate your classmates' work against a formal
six-domain rubric (Faghihi et al., 2022).

**Takeaway:** A robust digital edition relies on a dual-gate
quality assurance architecture combining automated schema validation with
structured human peer review.

---

## **02 Content**

**The Fragility of Local Desktop Validation**

When editors begin working with XML, they typically rely on interactive validation
features embedded within desktop Integrated Development Environments (IDEs), such
as Oxygen XML Editor or XML extensions in VS Code. In these desktop environments,
the editor validates files on demand, watching for red squiggly underlines or
clicking a "Validate" button to check the document against a local schema
(Kalvesmaki, 2024). While local interactive feedback is essential during initial
authoring, relying solely on local validation in a collaborative project is
inherently fragile.

Local validation environments suffer from severe configuration drift. One student
may have configured Oxygen to validate against a cached copy of the TEI All schema,
another may be validating against a customized local RELAX NG file, and a third may
have disabled schema validation entirely due to a misconfigured XML catalog path
(Faghihi et al., 2022). Furthermore, local validation depends entirely on human
memory: an editor working under deadline pressure may alter several lines of
morphological markup, forget to trigger a local validation check, and commit
malformed XML directly to the repository (Dunning, 2020).

| Validation Environment | Execution Trigger | Vulnerabilities in Collaborative Projects |
|---|---|---|
| **Local Desktop IDE** | Manual user action | Subject to configuration drift, stale schemas, and forgotten validation steps. |
| **Local Pre-Commit Hook** | Git commit command | Can be bypassed with `git commit --no-verify`; requires local software dependencies. |
| **Continuous Integration** | Automated push / PR event | Centralized, deterministic, unbypassable, and executed in clean virtual containers. |

To establish a bulletproof quality gate, collaborative projects must move
validation from the editor's private desktop to a centralized, headless Continuous
Integration environment (Dunning, 2020; Krautter et al., 2021). Centralized
validation runs automatically on independent cloud runners, using identical
dependencies and canonical schemas to evaluate every submitted commit under uniform
conditions.

**Takeaway:** Local desktop validation is necessary for
interactive authoring but insufficient for collaborative integrity, necessitating
centralized automated validation gates.

---

## **03 Content**

**The Multi-Tiered Validation Hierarchy**

Validating a rich TEI XML scholarly edition is not a monolithic, single-step
operation. Ensuring that a manuscript encoding is robust requires evaluating the
document across three distinct, progressively stricter tiers of constraint
(Kalvesmaki, 2024; TEI Consortium, 2026).

| Validation Tier | Standard / Specification | Scope and Focus |
|---|---|---|
| **Tier 3: Semantic Rules** | ISO Schematron (ISO/IEC 19757-3) | Contextual rules, attribute co-occurrence, ID/IDREF integrity |
| **Tier 2: Structural Grammar** | RELAX NG Grammar (ISO/IEC 19757-2) | Element nesting, document hierarchy, required child elements |
| **Tier 1: Syntax Baseline** | XML Well-Formedness (W3C Recommendation) | Syntax, balanced tags, quote characters, entity escaping |

The foundational tier is **XML Well-Formedness**. Governed by the W3C XML
specification, well-formedness checks that the document obeys the universal
syntax rules of XML: all elements open and close cleanly, tags nest without
overlapping, attributes are enclosed in quotation marks, and special characters
are properly escaped (TEI Consortium, 2026). If a document fails Tier 1, it is not
valid XML and cannot be processed by any downstream parser.

The second tier is **Structural Grammar**, enforced via **RELAX NG (ISO/IEC
19757-2)**. Grammar validation checks that the document obeys the structural
vocabulary of the Text Encoding Initiative. It dictates the geometric shape of the
document tree: ensuring that `<teiHeader>` contains `<fileDesc>`, that `<text>`
contains `<body>`, and that `<listWit>` contains only `<witness>` elements
(TEI Consortium, 2026).

The third tier is **Semantic Business Logic**, enforced via **ISO Schematron
(ISO/IEC 19757-3)**. Schematron evaluates contextual rules and cross-document
constraints that grammar-based schemas cannot express: verifying that every
witness siglum in an apparatus points to a defined `@xml:id`, that translation
elements specify correct language codes, and that morphological tokens contain both
lemmas and parts of speech (Kalvesmaki, 2024; Bauman, 2015).

**Takeaway:** Comprehensive XML quality control operates across
three distinct tiers: syntactic well-formedness, grammatical structure, and
rule-based semantic constraints.

---

## **04 Content**

**Tier 1 Validation: XML Well-Formedness and Parser Mechanics**

Every XML document is fundamentally a serialization of an abstract tree data
structure. For a computer to parse a text file into an in-memory Document Object
Model (DOM) tree, the file must adhere strictly to the syntactic grammar of XML.
Unlike HTML web browsers, which employ lenient error-correction algorithms to render
broken HTML tags gracefully, XML parsers operate under a strict **fatal error
policy**: the instant a parser encounters a syntax violation, it must halt
execution immediately and refuse to process the document (TEI Consortium, 2026).

A well-formed TEI XML document must satisfy five universal syntactic rules:

1. **Single Root Element:** Exactly one root element (typically `<TEI>`) must
   enclose all other elements in the document.

2. **Strict Element Nesting:** Elements must nest cleanly without overlapping. An
   inner element must be closed before its parent element closes (e.g. `<b><i>text</i></b>`,
   never `<b><i>text</b></i>`).

3. **Explicit Element Closure:** Every opening tag must have a corresponding closing
   tag, and all empty milestone elements must use self-closing syntax (e.g. `<pb/>`,
   `<lb/>`, `<cb/>`).

4. **Quoted Attribute Values:** All attribute values must be enclosed in single or
   double quotation marks (e.g. `n="14v"`, never `n=14v`).

5. **Character Entity Escaping:** Literal ampersands (`&`), less-than signs (`<`),
   and greater-than signs (`>`) occurring within text must be escaped as `&amp;`,
   `&lt;`, and `&gt;`.

```bash
# Test well-formedness from the command line using libxml2 xmllint
xmllint --noout src/modules/Topic_04_Transcription/ms_a_folio_14v.xml

# If clean, xmllint exits with returncode 0 and prints nothing.
# If malformed, it reports the exact line, column, and syntax error:
# ms_a_folio_14v.xml:42: parser error : Opening and ending tag mismatch: orig line 40 and choice
```

**Takeaway:** Well-formedness is the non-negotiable syntactic
baseline of all XML, ensuring that documents can be parsed into unambiguous
hierarchical trees.

---

## **05 Content**

**Tier 2 Validation: Grammar-Based Schemas with RELAX NG**

Once a document is confirmed to be well-formed, it must be validated against a
structural schema to verify that its element vocabulary and parent-child
hierarchies conform to project standards. Historically, SGML and early XML projects
relied on Document Type Definitions (DTDs) or W3C XML Schema (XSD). However, the
international digital humanities community has universally standardized on **RELAX
NG (Regular Language for XML Next Generation)** (TEI Consortium, 2026).

RELAX NG, standardized as ISO/IEC 19757-2, is a pattern-based schema language that
excels at defining complex mixed-content models, ordered sequences, and open
choice structures. Unlike W3C XML Schema, which imposes rigid object-oriented typing
constraints ill-suited to literary and historical documents, RELAX NG models the
fluid, non-deterministic structures typical of humanistic texts (TEI Consortium,
2026).

In our TEI workflows, RELAX NG schemas are generated directly from ODD (One
Document Does it all) customization files, yielding compact `.rng` (XML syntax) or
`.rnc` (compact syntax) files. We execute RELAX NG validation using **Jing**, the
industry-standard Java-based RELAX NG validator originally authored by James Clark
(Dunning, 2020).

```bash
# Validate a TEI document against the project RELAX NG schema using Jing
java -jar /usr/local/bin/jing.jar schemas/project_tei_schema.rng   src/modules/Topic_04_Transcription/ms_a_folio_14v.xml

# Sample Jing error report:
# ms_a_folio_14v.xml:18: error: element "body" not allowed here;
# expected element "teiHeader"
```

Jing traverses the document tree and verifies that every element occurs only where
permitted by the grammar, catching missing metadata containers, illegal child tags,
and invalid attribute enumerations (Dunning, 2020).

**Takeaway:** RELAX NG enforces the geometric and structural
grammar of TEI documents, verifying that elements nest according to established
schema definitions.

---

## **06 Content**

**The Limits of Grammar: The OHCO Model and Business Logic**

While RELAX NG is exceptionally powerful for validating structural shapes, it
possesses fundamental theoretical limitations. These limitations stem directly from
the **Ordered Hierarchy of Content Objects (OHCO)** data model upon which XML
grammars are built (Renear et al., 1996). Under the OHCO thesis, an XML schema
treats a document strictly as a context-free hierarchical tree: it can evaluate
whether Element B is a valid child of Element A, but it cannot evaluate dynamic,
context-dependent relationships across distant branches of the tree (Renear et al.,
1996; McGann, 2014).

Consider three common philological rules in digital scholarly editing that
grammar-based schemas cannot express:

1. **Attribute Co-Occurrence Constraints:** If a `<title>` element has an attribute
   `@type="translation"`, its `@xml:lang` attribute must not match the language of
   the source text. RELAX NG can declare that both attributes are allowed, but it
   cannot make the value of one attribute conditionally dependent upon the value
   of another (Kalvesmaki, 2024).

2. **Relational Pointer Integrity:** If an apparatus reading contains `<rdg
   wit="#CodexVat">`, the identifier `#CodexVat` must correspond to an actual
   `<witness xml:id="CodexVat">` declared within the `<teiHeader>` (Bauman, 2015).
   RELAX NG can check that `@wit` contains an IDREF or URI, but it cannot cross-check
   whether that specific ID exists elsewhere in the corpus.

3. **Mutual Exclusivity in Normalization:** A `<choice>` container may hold either
   an `<orig>`/`<reg>` pair (historical regularization) or a `<sic>`/`<corr>` pair
   (scribal error correction), but must never mix `<orig>` with `<corr>`. RELAX NG
   struggles to enforce these nuanced combinatorial restrictions cleanly (TEI
   Consortium, 2026).

To enforce these vital philological "business rules," digital editions must layer
rule-based validation on top of structural grammar (Kalvesmaki, 2024).

**Takeaway:** Grammar-based schemas define structural shapes but
cannot enforce conditional co-occurrence rules or cross-referential integrity
across document trees.

---

## **07 Content**

**Tier 3 Validation: ISO Schematron (ISO/IEC 19757-3)**

To overcome the structural blindness of grammar-based schemas, the International
Organization for Standardization developed **Schematron**, formalized as ISO/IEC
19757-3 (Kalvesmaki, 2024). Unlike DTDs, XSD, or RELAX NG, which operate by matching
patterns against an entire document grammar, Schematron is a **rule-based
validation language** that evaluates specific conditions at specific locations
within an XML tree.

Schematron relies entirely on the **XML Path Language (XPath)** to navigate the
document structure and evaluate boolean expressions (Kalvesmaki, 2024). Instead of
defining what the entire document must look like, a Schematron schema consists of a
collection of assertions: "Whenever you encounter a node matching Context X,
Condition Y must evaluate to True; if it does not, output Error Message Z."

| Schematron Element | Semantic Role | Functional Description |
|---|---|---|
| `<sch:schema>` | Root Container | Declares namespaces, query bindings (XPath 2.0/3.0), and title. |
| `<sch:pattern>` | Rule Group | Groups related validation rules into logical domain modules. |
| `<sch:rule context="...">` | Target Selector | Uses an XPath match expression to bind the rule to specific XML nodes. |
| `<sch:assert test="...">` | Error Assertion | Evaluates an XPath boolean test. If **false**, triggers a validation failure. |
| `<sch:report test="...">` | Warning Reporter | Evaluates an XPath boolean test. If **true**, emits an informative notice. |

A defining strength of Schematron is its human-centered design. When a RELAX NG
parser fails, it emits cryptic technical output (e.g. `element "app" not allowed
here`). When Schematron fails, it outputs custom, plain-language diagnostic messages
written directly by the project editors, explaining *why* the encoding violates
philological standards and *how* to correct it (Kalvesmaki, 2024).

**Takeaway:** ISO Schematron uses XPath queries to validate
complex business rules and conditional constraints that lie beyond the reach of
grammar-based schemas.

---

## **08 Content**

**Authoring Schematron Rules for Scholarly Editions**

Writing effective Schematron rules requires mastering the interplay between the
`<sch:rule context="...">` selector and the `<sch:assert test="...">` condition.
The `context` attribute establishes the focal node in the XML tree, while the
`test` attribute contains an XPath expression evaluated from the perspective of
that focal node (Kalvesmaki, 2024).

Let us examine a concrete philological rule: in our critical apparatus (Topic 8),
every apparatus entry (`<app>`) must contain at least one reading (`<rdg>`) or
lemma (`<lem>`), and every `<rdg>` element must explicitly specify which manuscript
witness attests that reading via the `@wit` attribute (TEI Consortium, 2026).

```xml
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron"
            xmlns:tei="http://www.tei-c.org/ns/1.0"
            queryBinding="xslt2">
  <sch:ns prefix="tei" uri="http://www.tei-c.org/ns/1.0"/>

  <sch:pattern id="apparatus_rules">
    <sch:rule context="tei:app">
      <sch:assert test="tei:rdg or tei:lem" role="error">
        [APP-01] An &lt;app&gt; element must contain at least one &lt;lem&gt; or &lt;rdg&gt; child element.
      </sch:assert>
    </sch:rule>

    <sch:rule context="tei:rdg">
      <sch:assert test="@wit and normalize-space(@wit) != ''" role="error">
        [APP-02] Every &lt;rdg&gt; element must possess a non-empty @wit attribute specifying its manuscript witnesses.
      </sch:assert>
    </sch:rule>
  </sch:pattern>
</sch:schema>
```

Notice the structure of the assertions: the context targets `tei:rdg`, and the test
evaluates `@wit and normalize-space(@wit) != ''`. If an encoder writes
`<rdg>λόγος</rdg>` without a `@wit` attribute, Schematron instantly flags the
exact element and prints our custom diagnostic message: `[APP-02] Every <rdg>
element must possess a non-empty @wit attribute...` (Kalvesmaki, 2024).

**Takeaway:** Schematron rules combine XPath context matching with
explicit boolean tests to generate tailored, actionable diagnostic feedback for
editors.

---

## **09 Content**

**Enforcing Cross-Reference and Identifier Integrity**

One of the most dangerous defects in a digital scholarly edition is the **dangling
pointer**: an attribute pointing to an identifier (`@target="#note-1"`,
`@wit="#CodexB"`, `@corresp="#canvas-14v"`) that does not actually exist in the
repository (Bauman, 2015). In print, a missing footnote or broken cross-reference
is an annoying typographical flaw; in a digital edition, it breaks hyperlinks,
corrupts graph indexes, and causes automated collation pipelines to fail.

Schematron excels at validating cross-referential integrity across the entire
document tree. Using XPath functions like `id()`, `doc()`, and sequence comparison
operators, Schematron can cross-check references dynamically against declared
entities (Bauman, 2015; Kalvesmaki, 2024).

```xml
<sch:pattern id="pointer_integrity">
  <sch:rule context="tei:rdg[@wit]">
    <!-- Split multi-valued witness pointers (e.g. "@wit='#CodexA #CodexB'") -->
    <sch:assert test="every $w in tokenize(@wit, '\s+') satisfies
                      substring($w, 2) = //tei:witness/@xml:id"
                role="error">
      [REF-01] Witness reference '<sch:value-of select="@wit"/>' contains an undeclared siglum.
      Every siglum must match an @xml:id defined in the &lt;listWit&gt; header.
    </sch:assert>
  </sch:rule>

  <sch:rule context="tei:ref[@target]">
    <sch:assert test="starts-with(@target, 'http') or
                      starts-with(@target, 'urn:') or
                      substring-after(@target, '#') = //@xml:id"
                role="error">
      [REF-02] Local reference target '<sch:value-of select="@target"/>' does not resolve
      to any declared @xml:id in this document.
    </sch:assert>
  </sch:rule>
</sch:pattern>
```

In the rule above, XPath 2.0's `every $w in tokenize(...) satisfies ...` expression
splits compound witness sigla (such as `@wit="#CodexA #CodexB"`) and asserts that
every individual siglum matches an `@xml:id` declared within `<listWit>`. If an
encoder mistypes `#CodexC` as `#CodexX`, Schematron intercepts the mistake
instantly (Bauman, 2015).

**Takeaway:** Schematron XPath assertions guarantee relational
integrity by verifying that every internal pointer and witness siglum resolves to a
valid declared identifier.

---

## **10 Content**

**Validating Linguistic and Attribute Co-Occurrences**

In Week 9, you encoded morphological and lexical metadata for every Greek word in
your passage using the TEI `<w>` element. A valid linguistic layer requires strict
co-occurrence rules: each word token must carry a dictionary headword (`@lemma`), a
grammatical part-of-speech category, and a morphological feature string (TEI
Consortium, 2026). If an encoder provides a lemma but omits the part of speech, or
if they supply a Greek verb lemma for a word tagged as a preposition, the
linguistic index becomes corrupt.

Similarly, in Topic 6, you encoded orthographic normalization using the `<choice>`
element. Project editorial guidelines dictate strict container rules:

1. **Regularization Choice:** Must contain exactly one `<orig>` (diplomatic manuscript
   reading) and exactly one `<reg>` (normalized critical reading).

2. **Correction Choice:** Must contain exactly one `<sic>` (manifest scribal error)
   and exactly one `<corr>` (editorial emendation).

3. **No Hybrid Containers:** A `<choice>` must never mix `<orig>` with `<corr>` or
   `<sic>` with `<reg>`.

```xml
<sch:pattern id="linguistic_and_choice_rules">
  <!-- Enforce complete linguistic tagging on word tokens -->
  <sch:rule context="tei:w">
    <sch:assert test="@lemma and @ana" role="error">
      [LEMMA-01] Token &lt;w&gt; ('<sch:value-of select="."/>') must possess both @lemma and @ana attributes.
    </sch:assert>
  </sch:rule>

  <!-- Enforce valid pairing inside <choice> elements -->
  <sch:rule context="tei:choice">
    <sch:assert test="(tei:orig and tei:reg and not(tei:sic or tei:corr)) or
                      (tei:sic and tei:corr and not(tei:orig or tei:reg))"
                role="error">
      [NORM-01] Invalid &lt;choice&gt; container. A &lt;choice&gt; must strictly pair (&lt;orig&gt; + &lt;reg&gt;)
      for regularization or (&lt;sic&gt; + &lt;corr&gt;) for correction.
    </sch:assert>
  </sch:rule>
</sch:pattern>
```

By articulating these rules in Schematron, we guarantee that all student
contributions adhere to identical editorial conventions across the entire course
corpus (Kalvesmaki, 2024).

**Takeaway:** Rule-based validation prevents invalid editorial
combinations, ensuring that normalization pairs and morphological tags conform
strictly to project policy.

---

## **11 Content**

**Compiling and Executing Schematron via XSLT Engines**

Understanding how Schematron executes under the hood demystifies the continuous
integration build process. Schematron does not require a bespoke binary compiler;
instead, it is executed as a multi-stage **XSLT transformation pipeline** using an
XSLT 2.0/3.0 engine such as **Saxon** (Kalvesmaki, 2024).

The reference implementation of ISO Schematron operates via a four-stage pipeline
known as the **Schematron Skeleton Processor**:

1. **Inclusion Stage (`iso_dsdl_include.xsl`):** Resolves external schema inclusions
   (`<sch:include>`) and merges them into a single schema tree.

2. **Abstract Expansion Stage (`iso_abstract_expand.xsl`):** Expands abstract patterns
   and parameters into concrete XPath rules.

3. **Compilation Stage (`iso_svrl_for_xslt2.xsl`):** Transforms the Schematron `.sch`
   file into an executable XSLT stylesheet (typically named `validator.xsl`).

4. **Validation Execution:** The compiled `validator.xsl` stylesheet is executed
   against the target TEI XML document using Saxon, producing a **Schematron
   Validation Report Language (SVRL)** XML document (Kalvesmaki, 2024).

```bash
# Step 1-3: Compile Schematron schema into an XSLT validator stylesheet
java -jar /usr/local/bin/saxon.jar -s:schemas/project_rules.sch   -xsl:iso-schematron/iso_svrl_for_xslt2.xsl -o:build/validator.xsl

# Step 4: Execute compiled validator against target TEI file to produce SVRL report
java -jar /usr/local/bin/saxon.jar -s:src/modules/Topic_04_Transcription/ms_a_folio_14v.xml   -xsl:build/validator.xsl -o:build/validation_report.svrl
```

The resulting SVRL file contains structured `<svrl:failed-assert>` elements
recording the exact XPath location, line number, role (`error`/`warning`), and text
of every failed assertion, making it easily parseable by automated CI tools
(Kalvesmaki, 2024; Dunning, 2020).

**Takeaway:** Schematron operates by compiling XPath rules into
XSLT stylesheets via Saxon, generating machine-readable SVRL reports of all
constraint violations.

---

## **12 Content**

**Introduction to Continuous Integration (CI/CD) for Digital Humanities**

In professional software development, **Continuous Integration (CI)** is a practice
where developers regularly merge code changes into a shared repository, after which
automated builds and test suites are executed automatically (Himmelstein et al.,
2019). In digital humanities, CI shifts quality control from a stressful,
post-production cleanup phase to a continuous, automatic background process (Weigl
et al., 2024).

Without Continuous Integration, quality control in digital editing is inherently
delayed. An encoder might spend four weeks transcribing a codex, only to discover at
the end of the semester that their XML files violate core schema rules, use invalid
Greek character entities, or contain hundreds of broken witness pointers. Repairing
these errors retroactively requires immense labor and often involves re-transcribing
damaged sections (Faghihi et al., 2022).

| Stage | Traditional Manual Workflow | Continuous Integration Workflow |
|---|---|---|
| **Trigger** | Periodic manual check by instructor | Automatic on every `git push` and Pull Request |
| **Execution** | Local desktop; dependent on editor setup | Clean cloud container (`ubuntu-latest`) |
| **Scope** | Often checks only active file | Exhaustively checks every XML file in the repository |
| **Feedback Time** | Days or weeks after submission | Under 60 seconds from push |
| **Merge Safety** | Vulnerable to human oversight | Mathematically blocked until 100% clean |

Continuous Integration embodies the principle of "shifting left": detecting defects
at the earliest possible moment in the editorial lifecycle. When a student pushes a
commit to GitHub, CI runners immediately spin up a clean virtual container, execute
syntax parsers, Jing RELAX NG validators, and Saxon Schematron suites, and report
the results within seconds (Dunning, 2020; Krautter et al., 2021).

**Takeaway:** Continuous Integration automates quality control,
running reproducible validation suites on every commit to prevent malformed data
from entering canonical repositories.

---

## **13 Content**

**Anatomy of a GitHub Actions Workflow**

On GitHub, Continuous Integration is configured through **GitHub Actions**. A
GitHub Actions workflow is a declarative automation pipeline defined inside a YAML
file located within the `.github/workflows/` directory of your repository (Dunning,
2020).

A GitHub Actions workflow consists of five fundamental building blocks:

1. **Workflow Name:** The human-readable title displayed in the GitHub Actions UI
   (e.g., `name: TEI XML Quality Gate`).

2. **Events (`on:`):** The repository triggers that cause the workflow to run. In
   digital editing, workflows typically trigger on `push` and `pull_request` events
   targeting the `main` branch.

3. **Jobs (`jobs:`):** A collection of sequential steps executed on a specific
   runner. Workflows can run multiple jobs concurrently (e.g. `validate-schema`,
   `lint-prose`, `compile-pdf`).

4. **Runner (`runs-on:`):** The operating system environment provisioned for the
   job. Most DH workflows use `runs-on: ubuntu-latest`.

5. **Steps (`steps:`):** The individual tasks executed within the job, which can
   include checking out code (`actions/checkout`), installing software dependencies
   (`actions/setup-java`), or executing shell commands (`run: jing ...`).

```yaml
# .github/workflows/validate-tei.yml
name: TEI XML Quality Gate

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  validate:
    name: Validate TEI Layers
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository code
        uses: actions/checkout@v4

      - name: Set up Java JDK 17
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'
```

**Takeaway:** GitHub Actions workflows define automated
event-driven pipelines that execute validation tasks inside isolated, ephemeral
virtual machines.

---

## **14 Content**

**Writing a Complete TEI Validation Workflow**

Let us now assemble a complete, production-grade GitHub Actions validation workflow
for our RELS 398 digital edition repository. This workflow executes a full sweep:
it installs Jing and Saxon, verifies XML well-formedness with `xmllint`, validates
structural grammar against our project RELAX NG schema, and evaluates business rules
against our ISO Schematron schema (Dunning, 2020; Krautter et al., 2021).

```yaml
name: TEI Validation Sweep

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  tei-validation:
    name: Multi-Tiered TEI Validation
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Install System Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y libxml2-utils default-jre wget

      - name: Download Jing and Saxon Processors
        run: |
          mkdir -p bin
          wget -q -O bin/jing.jar https://repo1.maven.org/maven2/org/relaxng/jing/20181222/jing-20181222.jar
          wget -q -O bin/saxon.jar https://repo1.maven.org/maven2/net/sf/saxon/Saxon-HE/12.4/Saxon-HE-12.4.jar

      - name: Tier 1: Check XML Well-Formedness
        run: |
          echo "Checking XML syntax with xmllint..."
          find data/ src/ -name "*.xml" -print0 | xargs -0 -n 1 xmllint --noout

      - name: Tier 2: Validate Structural RELAX NG Schema
        run: |
          echo "Validating structure with Jing..."
          find data/ src/ -name "*.xml" -print0 | xargs -0 -n 1 java -jar bin/jing.jar schemas/project_schema.rng

      - name: Tier 3: Validate ISO Schematron Business Rules
        run: |
          echo "Validating business rules with Saxon Schematron..."
          # Execute Schematron pipeline across all repository TEI XML files
          python3 scripts/validate_schematron.py --schema schemas/project_rules.sch
```

When committed to `.github/workflows/validate-tei.yml`, this workflow guarantees
that every single push and pull request is rigorously tested across all three tiers
before it can be merged (Dunning, 2020).

**Takeaway:** A standard TEI validation workflow automates Java
runtime provisioning, schema downloading, and multi-tiered validation across all
repository XML files.

---

## **15 Content**

**Integrating Community Validation Actions**

While writing custom shell commands in YAML provides full control, the digital
humanities community has developed specialized, pre-packaged GitHub Actions that
streamline TEI validation. Utilizing community actions reduces workflow boilerplate
and ensures adherence to DH software best practices (Dunning, 2020; Krautter et
al., 2021).

Two outstanding community actions are widely adopted in digital editing:

1. **`adunning/xml-model-validator`:** Created by Andrew Dunning (Oxford), this
   action automatically scans all XML files in a repository, parses their
   `<?xml-model?>` processing instructions, downloads the associated schemas, and
   validates each file using Jing and Saxon (Dunning, 2020).

2. **`dracor-org/dracor-validate-action`:** Developed for the Drama Corpora Project
   (DraCor), this action provides ultra-fast validation of TEI corpora against
   standard TEI All schemas and custom ODDs (Krautter et al., 2021).

```yaml
# Simplified workflow using adunning/xml-model-validator
name: Automated XML Model Validation

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate XML against declared xml-model schemas
        uses: adunning/xml-model-validator@v2
        with:
          files: 'data/**/*.xml src/**/*.xml'
```

By leveraging `xml-model-validator`, editors avoid hardcoding schema paths inside
the GitHub YAML file: the workflow dynamically discovers which schema governs each
individual XML file directly from its internal processing instructions (Dunning,
2020).

**Takeaway:** Community-developed GitHub Actions streamline CI
setup by automatically discovering XML-model processing instructions and executing
standardized validation pipelines.

---

## **16 Content**

**Associating Documents and Schemas: `<?xml-model?>`**

To enable both desktop IDEs and automated CI runners to locate the correct schemas
automatically, XML documents must declare their schema associations using the W3C
**`<?xml-model?>` Processing Instruction** standard (TEI Consortium, 2026).

Historically, XML documents used `<!DOCTYPE>` declarations or `@xsi:schemaLocation`
attributes. However, the TEI Consortium standardized on `<?xml-model?>` because it
allows a single document to link multiple schemas of different types simultaneously
(TEI Consortium, 2026).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="../../schemas/project_schema.rng" 
            type="application/xml" 
            schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="../../schemas/project_rules.sch" 
            type="application/xml" 
            schematypens="http://purl.oclc.org/dsdl/schematron"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
    <fileDesc>
      <titleStmt>
        <title>Transcription of Folio 14v</title>
      </titleStmt>
      <!-- ... header metadata ... -->
    </fileDesc>
  </teiHeader>
  <text>
    <body>
      <p>...</p>
    </body>
  </text>
</TEI>
```

In the header above, two distinct processing instructions are declared:

- The first links `project_schema.rng` and specifies the RELAX NG namespace
  (`http://relaxng.org/ns/structure/1.0`).

- The second links `project_rules.sch` and specifies the ISO Schematron namespace
  (`http://purl.oclc.org/dsdl/schematron`).

When Oxygen, VS Code, or `xml-model-validator` opens this file, it immediately
recognizes both schemas and executes both validation passes concurrently (Dunning,
2020; TEI Consortium, 2026).

**Takeaway:** Standard `<?xml-model?>` processing instructions
declare the exact grammar and Schematron schemas governing a document, enabling
both IDEs and CI runners to validate automatically.

---

## **17 Content**

**Converting CI Failures to Inline GitHub Annotations**

When a Continuous Integration pipeline fails on GitHub, a major pedagogical hurdle
is diagnostic accessibility. If a student must open a raw terminal log, scroll
through 600 lines of Java stack traces and Maven download messages, and locate a
single cryptic error line, they quickly become overwhelmed and frustrated (Faghihi
et al., 2022).

To eliminate this barrier, advanced DH CI pipelines convert validation failures into
**inline GitHub Annotations** (Dunning, 2020). GitHub provides a special workflow
command syntax (`::error file=...,line=...,col=...::message`) that runners can emit
during execution:

```
::error file=data/transcriptions/folio_14v.xml,line=45,col=12::[NORM-01] Invalid <choice> container: <orig> cannot be paired with <corr>.
```

When GitHub Actions intercepts this workflow command, it renders a visual,
highlighted error box directly on the pull request diff, pinpointing the exact line
and column of the error in the contributor's browser window (Dunning, 2020).

```
File: data/transcriptions/folio_14v.xml
Line 45:   <choice><orig>καρδια</orig><corr>καρδίᾳ</corr></choice>
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[Error] [NORM-01] Invalid <choice> container: <orig> cannot be paired with <corr>.
        Use <orig> + <reg> for orthographic regularization.
```

By displaying actionable error messages directly beside the offending markup,
automated validation functions as an objective, non-judgmental automated tutor,
empowering students to debug and refine their encoding iteratively (Faghihi et al.,
2022).

**Takeaway:** Translating automated validation failures into
inline GitHub annotations provides contextual, non-judgmental feedback directly
alongside the offending markup.

---

## **18 Content**

**Protecting Branches with Automated CI Merge Gates**

The ultimate power of Continuous Integration in a collaborative project lies in
**Branch Protection Rules**. Without branch protection, automated CI is merely an
informative indicator: an editor could see a red failing test and choose to click
"Merge pull request" anyway, corrupting the production codebase (Himmelstein et al.,
2019).

GitHub allows repository administrators to configure strict protection policies on
the `main` branch:

1. **Require Status Checks to Pass Before Merging:** GitHub blocks the "Merge" button
   entirely until all designated CI validation jobs (e.g. `Multi-Tiered TEI
   Validation`) report green success codes.

2. **Require Pull Request Reviews:** Requires at least one approving review from a
   designated peer reviewer or course instructor before merging.

3. **Require Branches to be Up to Date:** Ensures that the contributor has merged
   the latest `upstream/main` commits into their feature branch prior to merging,
   preventing silent integration conflicts (Huskey, 2024).

| Pull Request Component | State / Verification | Description |
|---|---|---|
| **Target Commit** | `4a8f12c` | "Add diplomatic markup for Folio 15r" |
| **CI Status** | Passed | Well-Formedness, RELAX NG Grammar, ISO Schematron all green |
| **Peer Review** | Approved | Required review completed by assigned reviewer |
| **Merge Gate Status** | Unlocked | All branch protection checks satisfied; merge enabled |

By establishing automated merge gates, human error is mathematically designed out
of the system. The canonical `main` branch is guaranteed to remain valid,
schema-compliant, and continuously publishable at all times (Witt, 2018).

**Takeaway:** Branch protection rules enforce automated merge
gates, mathematically preventing malformed or unvalidated TEI data from polluting
the canonical edition.

---

## **19 Content**

**Automated Preview and Artifact Compilation in CI**

Continuous Integration workflows can extend far beyond validation: they can also
perform **Continuous Delivery (CD)** by automatically compiling and publishing
derivative edition formats on every commit (Weigl et al., 2024; Himmelstein et al.,
2019).

In textual scholarship, reviewers should not be forced to evaluate raw XML markup in
isolation; they need to inspect how the encoded text renders visually in a browser
or on a printed page (Rosselli Del Turco, 2016). We can configure GitHub Actions to
compile derivative outputs dynamically whenever a pull request is submitted:

| Derivative Target | Compilation Engine | Reviewer Utility |
|---|---|---|
| **Interactive HTML Web Edition** | CETEIcean / XSLT | Allows reviewers to test dynamic apparatus tooltips and facsimile zooming. |
| **Print-Ready PDF Notes** | Typst / Pandoc / XSL-FO | Compiles camera-ready PDF critical editions with footnotes and apparatus. |
| **Linguistic Concordance** | Python / CLTK | Extracts word frequency tables and morphological indexes for review. |

Using GitHub's `actions/upload-artifact` action, the CI pipeline can attach these
compiled HTML and PDF files directly to the pull request summary. A peer reviewer
can download and inspect the compiled PDF reading notes alongside the raw TEI XML
diff, evaluating both the underlying code and the rendered reading experience
simultaneously (Rosselli Del Turco, 2016; Weigl et al., 2024).

**Takeaway:** CI/CD pipelines can automatically generate static
HTML previews and PDF reading notes, allowing reviewers to evaluate visual
presentation alongside underlying code.

---

## **20 Content**

**The Boundary Between Automated Linting and Human Peer Review**

As our automated validation pipelines become increasingly sophisticated, it is
crucial to recognize the epistemological boundary between what machines can verify
and what requires humanistic critique (Huskey, 2024). A green checkmark from a CI
runner indicates that an XML file is syntactically valid and structurally compliant
with project schemas; it does *not* mean the edition is philologically correct.

| Evaluation Task | Automated CI Validation | Human Scholarly Peer Review |
|---|---|---|
| **Tag Syntax & Nesting** | Yes (100% automated) | Redundant (do not waste human time) |
| **RELAX NG Conformance** | Yes (100% automated) | Redundant (do not waste human time) |
| **Pointer & ID Resolution** | Yes (100% automated) | Redundant (do not waste human time) |
| **Paleographical Reading** | No (cannot evaluate ink traces) | Essential (evaluates facsimile zoom) |
| **Emendation Rationale** | No (cannot evaluate logic) | Essential (evaluates `<corr>` justification) |
| **Translation Fidelity** | No (cannot evaluate semantics) | Essential (evaluates English rendering) |

An automated validator cannot look at a high-resolution IIIF image and determine
whether a faint letterform is an epsilon or a theta. It cannot judge whether an
editor's conjectural emendation is historically plausible, nor can it evaluate
whether an English translation captures the rhetorical subtlety of a Greek clause
(Huskey, 2024). Automation exists to handle the tedious mechanics of structural
verification, liberating human peer reviewers to concentrate their intellectual
energy on interpretive, historical, and philological scholarship (Witt, 2018).

**Takeaway:** Automated pipelines verify structural and syntactic
conformance, liberating human peer reviewers to concentrate on interpretive
nuance and philological rigor.

---

## **21 Content**

**Designing a Structured TEI Peer-Review Rubric**

To conduct rigorous, consistent human peer reviews within a collaborative project,
evaluators must follow a structured **peer-review rubric** (Faghihi et al., 2022).
Without an explicit rubric, peer reviews tend to degenerate into superficial
formatting critiques or vague expressions of praise.

A model TEI peer-review rubric bridges the technical and the philological across
six essential domains (Faghihi et al., 2022; Huskey, 2024):

| Evaluation Domain | Assessment Criteria | Action Required if Deficient |
|---|---|---|
| **1. Pipeline Validation** | Does the PR pass all automated CI checks (syntax, Jing, Saxon)? Are there failing annotations? | **Block Merge.** Contributor must resolve CI errors before proceeding. |
| **2. Structural Integrity** | Does OHCO nesting reflect the codex? Are `<pb/>` and `<lb/>` milestones placed accurately without breaking blocks? | **Request Changes.** Reviewer highlights improper milestone placement. |
| **3. Philological Accuracy** | Are scribal interventions correctly tagged? Are `<choice>`, `<orig>`, `<reg>`, `<sic>`, and `<corr>` justified by facsimile evidence? | **Request Changes.** Reviewer cites facsimile coordinates to dispute readings. |
| **4. Semantic Precision** | Are named entities (`<persName>`, `<placeName>`) identified? Do `@ref` attributes point to valid authority URIs? | **Request Changes.** Reviewer identifies missing semantic tags or broken URIs. |
| **5. Metadata Provenance** | Is `<teiHeader>` complete? Does `<revisionDesc>` log the contributor's name, date, and change rationale? | **Request Changes.** Contributor must supply missing attribution metadata. |
| **6. Minimal Computing** | Does markup separate data from presentation? Are hardcoded display styles avoided in favor of semantic tags? | **Request Changes.** Remove presentation markup in favor of CSS classes. |

**Takeaway:** A structured peer-review rubric provides an
objective framework for evaluating both technical encoding standards and humanistic
scholarship.

---

## **22 Content**

**Auditing the `teiHeader` and Provenance Layer**

The first substantive domain of our peer-review sweep is the **`<teiHeader>` and
provenance layer**, constructed during Topic 2 (Cataloguing) and refined across the
term (Driscoll, 2016). The `teiHeader` is the bibliographic soul of the edition: if
its metadata is incomplete or inaccurate, the edition cannot be cited, indexed, or
preserved by research libraries (TEI Consortium, 2026).

When auditing a peer's `teiHeader`, reviewers must evaluate four core sections:

1. **Manuscript Description (`<msDesc>`):** Verify that the `<msIdentifier>`
   accurately records the holding institution, repository, collection, and
   shelfmark (e.g. Biblioteca Apostolica Vaticana, Vat.gr.1209) (Driscoll, 2016).

2. **Physical Description (`<physDesc>`):** Confirm that the support material
   (parchment/paper), page dimensions, layout (columns, lines per page), and scribal
   hands (`<handDesc>`) are documented accurately.

3. **Editorial Declaration (`<editorialDecl>`):** Ensure that the project's
   normalization, correction, and lemmatization policies are explicitly declared in
   prose so that external scholars understand the editorial principles applied.

4. **Attribution and Revision History (`<revisionDesc>`):** Check that every student
   contributor is credited in `<titleStmt>/<respStmt>` with their ORCID identifier,
   and that all major milestones are logged as dated `<change>` elements (Daquino
   et al., 2023).

**Takeaway:** Auditing the `teiHeader` ensures that manuscript
physical descriptions, provenance history, and contributor attribution meet
international cataloguing standards.

---

## **23 Content**

**Auditing Diplomatic Transcription and Physical Milestones**

The second domain of our peer-review sweep evaluates the **diplomatic
transcription layer** (Topic 4) and its integration with high-resolution **IIIF
facsimiles** (Topic 3). The diplomatic layer must serve as an unvarnished,
faithful digital surrogate of the physical manuscript artifact (TEI Consortium,
2026).

Reviewers must open the peer's transcription XML file alongside the primary IIIF
manifest in an image viewer (such as Mirador or the Universal Viewer) and audit the
following points:

- **Milestone Correspondence:** Verify that every page break (`<pb n="..."/>`) and
  line break (`<lb n="..."/>`) corresponds exactly to the physical structure
  visible in the facsimile. Ensure line breaks occur at true scribal line endings,
  not arbitrary editor wrapping (TEI Consortium, 2026).

- **Paleographical Accuracy:** Zoom in to high-resolution facsimile regions to
  verify doubtful letterforms, ambiguous ligatures, and punctuation strokes.

- **Scribal Alterations:** Check that physical corrections on the page are
  accurately encoded using appropriate physical tags: `<add place="above">` for
  supralinear additions, `<del rend="strikethrough">` for cancelled text, and
  `<subst>` for inline substitutions.

- **Damage and Illegibility:** Ensure that damaged or abraded characters are marked
  with `<unclear>` and lacunae are measured with `<gap reason="lost" unit="char"
  quantity="..."/>`.

**Takeaway:** Auditing the diplomatic layer confirms that
physical milestones and scribal alterations faithfully represent the primary
manuscript evidence.

---

## **24 Content**

**Auditing Normalization, Collation, and Variant Apparatus**

The third domain of our audit evaluates the **normalization layer** (Topic 6), the
**collation results** (Topic 7), and the **critical apparatus** (Topic 8). In this
domain, reviewers evaluate how the editor mediated between the raw manuscript
witness and the critical text (TEI Consortium, 2026).

Reviewers must inspect the following editorial structures:

1. **Orthographic Normalization (`<choice>`):** Check that historical spelling
   variants (e.g. itacisms like ει for ι, moveable nu variations) are encoded using
   `<orig>` and `<reg>`, while genuine scribal errors are encoded using `<sic>` and
   `<corr>`. Verify that all normalized readings (`<reg>`) conform to standard
   lexicon orthography (LSJ / BDAG).

2. **Apparatus Structure (`<app>`):** Evaluate whether the apparatus criticus
   follows a clear positive model (`<lem>` + `<rdg>`) or negative model (`<rdg>`
   only). Confirm that the lemma matches the accepted reading of the critical text.

3. **Witness Attribution (`@wit`):** Cross-check that every variant reading lists
   its supporting manuscript witnesses using declared sigla (e.g. `@wit="#CodexA
   #CodexB"`), and that variant readings are corroborated by collation tables.

Reviewers should actively query subjective editorial decisions: if an editor
marked an unusual reading as a scribal error (`<sic>`) when it could represent a
legitimate dialectal variant (`<orig>`), the reviewer should raise this question in
an inline PR comment (Witt, 2018).

**Takeaway:** Auditing normalization and apparatus layers ensures
that editorial emendations and variant readings are transparently documented and
philologically justified.

---

## **25 Content**

**Auditing Linguistic Markup and Morphosyntax (Assignment 3)**

The fourth domain of today's audit focuses directly on the **Linguistic Markup
Assignment (Assignment 3)**, which is formally due today. In Week 9, you lemmatized
and morphologically tagged your assigned Greek passage. Today, peer reviewers will
audit these linguistic annotations before final submission (TEI Consortium, 2026).

Reviewers must systematically sample at least 15 word tokens (`<w>`) across the
peer's text and evaluate four linguistic dimensions:

| Linguistic Dimension | Audit Criteria | Common Encoding Errors to Flag |
|---|---|---|
| **Lemma Headword (`@lemma`)** | Accurate dictionary citation form in Unicode Greek (e.g. `lemma="λόγος"`, `lemma="εἰμί"`). | Inflected forms erroneously used as lemmas; missing breathing marks or accents. |
| **Part of Speech (`@ana`)** | Standard POS tag matching project ontology (e.g. `#noun`, `#verb`, `#adj`, `#prep`). | Conflating adjectives with substantives; misidentifying particles. |
| **Morphological Features** | Complete feature string: Person, Number, Tense, Voice, Mood, Case, Gender, Degree. | Missing case/gender on participles; incorrect aorist voice identification. |
| **Contractions & Enclitics** | Correct decomposition of crasis and enclitic accent shifts. | Attaching enclitic accents to dictionary lemmas. |

Reviewers cross-check questionable lemmas against authoritative lexicons (Liddell-Scott-Jones
via Logeion) and use inline GitHub review comments to suggest corrected
morphological feature strings (Faghihi et al., 2022).

**Takeaway:** Auditing the linguistic layer verifies that Greek
lemmas, morphological parsings, and grammatical attributes are philologically
accurate across all encoded tokens.

---

## **26 Content**

**Executing the In-Class Peer Review Exchange**

With our rubrics defined and our validation pipelines operational, we now initiate
today's **In-Class Peer Review Exchange**. In this exercise, each student pairs with
an assigned classmate to conduct a formal, reciprocal peer review of their
consolidated digital edition (Faghihi et al., 2022).

Follow this step-by-step protocol during the lab session:

1. **Locate Peer's Pull Request:** Navigate to the canonical class repository on
   GitHub and open the active Pull Request submitted by your assigned peer partner
   (e.g., `PR #16: Consolidate Edition Layers for Folio 14v`).

2. **Verify Automated CI Status:** Confirm that the pull request displays a green
   checkmark indicating that all automated GitHub Actions validation passes
   succeeded. If CI failed, alert your partner immediately.

3. **Inspect the Diff:** Open the "Files changed" tab. Review the TEI XML diff line
   by line against the six-domain rubric.

4. **Leave Granular Inline Comments:** Post at least **three substantive inline
   review comments** on specific lines of markup. At least one comment must query a
   paleographical or normalization decision, and at least one must verify a
   linguistic lemma tag. Use GitHub's `suggestion` block syntax to propose concrete
   markup fixes where appropriate.

5. **Submit Formal Review:** Click "Review changes," write a constructive summary
   evaluating the edition's overall strengths and areas for improvement, and select
   *Approve* or *Request Changes* (Faghihi et al., 2022).

```markdown
<!-- Example of a constructive peer review summary -->
### Peer Review Summary for Codex B Edition (Folio 14v)
**Reviewer:** `@peer_reviewer` · **Status:** `Request Changes`

- **Pipeline:** Automated CI is green (Jing RELAX NG and Saxon Schematron passed).
- **Physical Layer:** Page break and line breaks match IIIF canvas #14 perfectly.
- **Normalization:** Excellent use of `<choice>` for itacisms. Please see inline comment on line 42 regarding the classification of `<sic>` vs `<orig>`.
- **Linguistic Layer:** 18 tokens audited; 17 correct. Found one minor parsing error on line 58 (verb tagged as imperfect instead of aorist).
```

**Takeaway:** The peer review exchange provides real-world
experience in evaluating, annotating, and adjudicating scholarly markup within an
active collaborative repository.

---

## **27 Content**

**Case Study: The Digital Latin Library and the Traveling Imprimatur**

To see how distributed version control and collaborative peer review transform the
institutional landscape of textual scholarship, we examine the **Digital Latin
Library (DLL)** and its publication platform, the **Library of Digital Latin Texts
(LDLT)**, directed by Samuel J. Huskey (Huskey, 2024).

Historically, the authority of a critical edition was bound to the prestige of the
academic publishing house (e.g. Oxford Classical Texts, Teubner, Budé) that printed
it. These commercial presses held a monopoly on scholarly validation, locking
critical editions behind expensive paywalls and proprietary formats that prevented
computational analysis (Huskey, 2024).

| Publishing Model | Workflow Pipeline | Governance and Access |
|---|---|---|
| **Traditional Commercial Press** | Scholar $\rightarrow$ Commercial Press $\rightarrow$ Paywalled Print Volume | Editorial board enclosed within private publishing house; proprietary distribution |
| **LDLT Model (Traveling Imprimatur)** | Scholar (GitHub Fork) $\rightarrow$ Pull Request $\rightarrow$ Learned Society Peer Review $\rightarrow$ Open TEI XML Edition | Society editorial board reviews Git PR; open-access repository with traveling imprimatur |

Huskey revolutionized this paradigm by introducing the concept of the **"Traveling
Imprimatur"** (Huskey, 2024). The LDLT decouples peer review from the publication
platform. Scholars author critical editions in TEI XML and submit them via GitHub
pull requests. Independent editorial boards appointed by learned societies—such as
the Society for Classical Studies (SCS) and the Medieval Academy of America
(MAA)—conduct rigorous, blind peer review directly on the Git repository using
automated validation and humanistic critique. Once approved, the edition receives
the society's official imprimatur (seal of quality) and is published as an open-access,
version-controlled TEI repository that can be hosted on any platform or archived
permanently (Huskey, 2024).

**Takeaway:** The Digital Latin Library proves that
version-controlled peer review can award authoritative academic credentials that
travel independently of proprietary hosting platforms.

---

## **28 Content**

**Digital Longevity and the Endings Project Principles**

As you finalize your consolidated edition, you must confront the problem of
**digital longevity**. The digital humanities are littered with the corpses of
ambitious digital editions that decayed into uselessness within 5 to 10 years of
publication—a phenomenon known as "software rot" or "digital entropy" (Holmes &
Turska, 2023; Rosselli Del Turco, 2016). Projects built upon complex dynamic
databases (MySQL), server-side scripting languages (PHP, Ruby on Rails), and
proprietary content management systems fail the moment grant funding expires,
security vulnerabilities emerge, or university IT servers are decommissioned (Brett,
2023).

To guarantee that your scholarship survives for decades, our curriculum adheres to
the **Endings Project Principles**, established by Martin Holmes and colleagues at
the University of Victoria (Holmes & Turska, 2023).

| Endings Principle | Architectural Requirement | Application to Course Edition |
|---|---|---|
| **1. Data Independence** | Pure TEI XML open standards; no proprietary databases. | The entire edition exists as static, human-readable XML files in Git. |
| **2. Zero Server Dependency** | No dynamic server-side processing or backend scripts. | Publication relies on static HTML/CSS pre-rendered via client-side libraries. |
| **3. Graceful Degradation** | The edition must remain fully readable even if JavaScript fails. | Static XML and HTML can be read in any basic web browser or plain-text reader. |
| **4. Minimal Computing** | Lightweight static files hosted on distributed infrastructure. | Hosted for free on GitHub Pages, decentralized IPFS, or static institutional servers. |

By separating your underlying scholarly data (TEI XML) from dynamic presentation
frameworks, and by utilizing lightweight, client-side rendering engines like
**CETEIcean** (which uses standard CSS to style TEI elements natively in the browser
without transformations), your edition achieves true digital permanence (Rosselli
Del Turco, 2016; Holmes & Turska, 2023).

**Takeaway:** Adhering to Endings Project principles ensures that
digital critical editions remain functional, secure, and citeable for decades
without ongoing server maintenance.

---

## **29 Content**

**Archiving, Persistent Identification, and FAIR Data Compliance**

The final phase of digital scholarly consolidation is ensuring that your edition
satisfies the **FAIR Data Principles**: ensuring that your research data is
**Findable**, **Accessible**, **Interoperable**, and **Reusable** (Daquino et al.,
2023).

While GitHub is an exceptional environment for active, collaborative development,
it is not a permanent scholarly preservation archive. A commercial company could
alter its pricing, delete inactive accounts, or modify its terms of service.
Therefore, mature digital editions archive formal release snapshots to permanent,
open-access academic data repositories such as **Zenodo** (operated by CERN)
(Daquino et al., 2023; Brett, 2023).

| Stage | Action / Event | Output / Persistence |
|---|---|---|
| **1. Development** | Active Git repository editing on feature branches | Dynamic version-controlled commits |
| **2. Release Tagging** | Create formal GitHub Release (e.g., `v1.0-consolidated`) | Trigger automated Zenodo webhook |
| **3. Archival Snapshot** | Zenodo captures immutable ZIP archive of repository | Redundant long-term preservation storage |
| **4. Persistent Identifier** | Zenodo mints registered Digital Object Identifier | Globally unique, citeable DOI (e.g., `10.5281/zenodo.123456`) |

GitHub provides native, automated integration with Zenodo. Whenever you tag a
formal release in your repository (e.g. `release-v1.0-consolidated`), Zenodo
automatically pulls an immutable snapshot archive, stores it across redundant
European server clusters, and mints a permanent **Digital Object Identifier (DOI)**
(Brett, 2023). Furthermore, by including a standardized **Citation File Format**
(`CITATION.cff`) in your repository root, you ensure that reference management
software (Zotero, Mendeley) and academic bibliographies can cite your digital
edition with perfect bibliographic precision (Daquino et al., 2023).

**Takeaway:** Archiving version-controlled releases to permanent
repositories like Zenodo assigns permanent DOIs, ensuring long-term citability and
FAIR data compliance.

---

## **30 Content**

**The Consolidated Milestone: Submitting Assignment 3 and Looking Ahead**

Today marks a major pedagogical milestone in RELS 398. Over the past ten weeks, you
have transformed raw, fragmented manuscript images into a fully consolidated,
schema-validated, multi-layered digital critical edition.

Before concluding today's lab session, execute the final submission steps for your
**Linguistic Markup Assignment (Assignment 3)**:

1. **Incorporate Peer Feedback:** Review the comments and suggested changes left on
   your pull request by your peer partner, commit any necessary corrections, and
   verify that automated CI remains green.

2. **Merge Pull Request:** Once approved, merge your feature branch into your local
   and remote `main` branch.

3. **Submit Assignment Commit Hash:** Submit the 40-character SHA hash of your
   merged commit to Moodle for formal grading.

Next week in **Topic 11 (Translation Alignment and Interlinear Glossing)**, we move
from monolingual textual criticism to bilingual comparative philology. In Meeting
#28 on Tuesday, you will begin aligning your Greek critical text with historical
Latin and English translations, exploring the international **Leipzig Glossing
Rules** and constructing linked interlinear data representations (TEI Consortium,
2026).

**Takeaway:** Week 10 consolidation validates and unifies all
accumulated edition layers, establishing the rigorous foundation needed for
bilingual translation alignment and commentary.

---

## References

Almas, B., & Beaulieu, M.-C. (2013). Developing a new integrated editing platform
for source documents in classics. In *Digital Humanities 2013 Conference
Abstracts*. University of Nebraska–Lincoln.

Bauman, S. (2015). Freedom to constrain: Advanced TEI customization with ODD.
*Women Writers Project*.

Brett, A. D. J. (2023). Preserving digital humanities projects through minimal
computing. *Adam DJ Brett*. https://www.adamdjbrett.com/blog/dh-part-5-preserving-digital-humanities-projects/

Daquino, M., Wigham, M., Daga, E., Giagnolini, L., & Tomasi, F. (2023). CLEF: A
Linked Open Data native system for crowdsourcing. *ACM Journal on Computing and
Cultural Heritage*, 16(3), 1–17. https://doi.org/10.1145/3594721

Driscoll, M. J. (2016). *TEI XML customisation for manuscript description*. The
FASNL Project. http://driscoll.dk/fasnl/FASNL_msDesc_v1_2016.html

Dunning, A. (2020). *xml-model-validator: GitHub Action for validating TEI XML
files*. https://github.com/adunning/xml-model-validator

Faghihi, Y., Holford, M., & Jones, H. (2022). Teaching the Text Encoding Initiative:
Context, Community and Collaboration. *Journal of Open Humanities Data*, 8(15),
1–14. https://doi.org/10.5334/johd.72

Himmelstein, D. S., Rubinetti, V., Slochower, D. R., Hu, D., Malladi, V. S., Greene,
C. S., & Gitter, A. (2019). Open collaborative writing with Manubot. *PLOS
Computational Biology*, 15(6), e1007128. https://doi.org/10.1371/journal.pcbi.1007128

Holmes, M., & Turska, M. (2023). Embracing Endings: Principles for digital
longevity and their importance for research software engineers. *DHTech Blog*.
https://dh-tech.adho.org/blog/2023/08/07/endings-principles/

Huskey, S. J. (2024). Decoupling quality control and publication: The Digital Latin
Library and the traveling imprimatur. In *Digital Scholarly Editing in Practice*.
Cambridge University Press.

Kalvesmaki, J. (2024). Schematron as XSLT interface, and advanced validation models.
In *Proceedings of Balisage: The Markup Conference 2024*. https://doi.org/10.4242/BalisageVol30.Kalvesmaki01

Krautter, B., Pagel, J., & Reiter, N. (2021). *dracor-validate-action: GitHub
Action for validating TEI files*. https://github.com/dracor-org/dracor-validate-action

McGann, J. (2014). *A New Republic of Letters: Memory and Scholarship in the Age of
Digital Reproduction*. Harvard University Press.

Renear, A., Mylonas, E., & Durand, D. (1996). Refining our notion of what text
really is: The problem of overlapping hierarchies. In *Research in Humanities
Computing* (Vol. 4). Oxford University Press.

Rosselli Del Turco, R. (2016). The quest for the "hundred year" digital scholarly
edition. In *Digital Editing and Publishing*. Digital Humanities Institute.

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/

Weigl, D. M., Janjuš, O., Rosmer, S., de Valk, R., & Lewis, D. (2024). Collaborative
workflows for encoding, validating, and publishing a multimodal digital edition. In
*Proceedings of the 11th International Conference on Digital Libraries for
Musicology* (DLfM '24), pp. 78–86. https://doi.org/10.1145/3748336.3748349

Witt, J. C. (2018). Re-conceiving the Christian scholastic corpus with the
Scholastic Commentaries and Texts Archive. In *Past and Future: Medieval Studies
Today*, pp. 103–128. Brepols.

Witt, J. C. (2019). Digital scholarly editions as interfaces. In *Digital Scholarly
Editions as Interfaces*, pp. 191–214. BoD.
