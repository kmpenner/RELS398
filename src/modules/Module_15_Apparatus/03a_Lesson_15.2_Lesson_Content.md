# Lesson 15.2 — Automated Apparatus Generation with CollateX and Validation

*RELS 398 / ENGL 398 · Topic 15: Apparatus · Meeting #21 (Wed Oct 28)*

***Step 2 of the three-step cycle: deterministic.** Today you transform CollateX
alignment tables and variant graphs into TEI Critical Apparatus XML, validate the
generated markup, and measure algorithmic output against Tuesday's hand-crafted
ground truth.*

---

## **01 Content**

**From Alignment Graph to Critical Apparatus**

Yesterday you constructed critical apparatus entries by hand, experiencing the
intellectual rigor required to delimit variation units, select lemmas, classify
variants, and maintain referential integrity across witness sigla. Today you shift
from manual craftsmanship to deterministic automation.

In Week 7, you learned how automated collation engines like CollateX align multiple
textual witnesses into mathematical data structures called **variant graphs**.
A variant graph represents the converging and diverging paths of textual
transmission as a directed acyclic graph (DAG). In this mathematical graph, vertices
represent aligned words or tokens, while directed edges represent the sequence of
reading within each individual witness. However, an in-memory graph structure is not
yet an apparatus. To become usable within digital editions, publishing pipelines, and
archival repositories, the abstract nodes and edges of the graph must be serialized
into standardized, machine-actionable TEI XML (Haentjens Dekker & Middell, 2011).

This translation represents Phase 5 of the Gothenburg Model of automated collation:
the **Export phase**. In this phase, the algorithmic alignment produced during
pairwise or progressive graph matching is converted into structured `<app>`, `<lem>`,
and `<rdg>` elements.

```text
Gothenburg Model Pipeline:
[1. Tokenization] -> [2. Normalization] -> [3. Alignment] -> [4. Analysis] -> [5. Export (TEI XML)]
```

The conversion from a non-linear graph to linear XML markup is computationally
non-trivial. Where the variant graph branches into parallel paths, the exporter must
determine the precise boundaries of the variation unit, reconcile competing witness
paths, and output valid, well-formed TEI XML.

Today you will configure CollateX to export TEI apparatus XML, write custom
transformation scripts to convert CollateX JSON into advanced apparatus structures,
and subject the resulting XML to rigorous schema and Schematron validation.

**Vocabulary.** *Variant graph* — a directed acyclic graph representing textual
divergences and convergences across witnesses. *Export phase* — Phase 5 of the
Gothenburg Model, converting internal alignment graphs into interchange formats.
*Serialization* — translating in-memory data structures into a standardized file
format like XML.

**Takeaway:** Automated apparatus generation is the serialization
of an algorithmic variant graph into standardized TEI XML.

---

## **02 Content**

**The Gothenburg Model: Export Phase Architecture**

To understand how automated tools generate critical apparatuses, one must examine
the modular architecture defined by the **Gothenburg Model** (Haentjens Dekker &
Middell, 2011).

Developed in 2009 by an international consortium of digital humanists, the
Gothenburg Model divides automated collation into five distinct, decoupled phases.
This separation of concerns ensures that tokenization rules or normalization
filters can be modified without altering the underlying alignment algorithm or the
export serialization engine (Haentjens Dekker et al., 2015).

| Phase Number | Phase Name | Computational Function | Input / Output |
| --- | --- | --- | --- |
| Phase 1 | Tokenization | Segments raw text strings into discrete tokens | Text -> Token stream |
| Phase 2 | Normalization | Neutralizes non-significant orthographic variation | Token -> Normalized token |
| Phase 3 | Alignment | Calculates optimal string and graph correspondences | Normalized tokens -> Variant graph |
| Phase 4 | Analysis | Detects transpositions, omissions, and sub-graphs | Variant graph -> Analyzed graph |
| Phase 5 | Export | Serializes the graph into TEI XML, JSON, or tables | Analyzed graph -> TEI `<app>` markup |

In Phase 5, the exporter traverses the vertices (nodes) of the aligned variant
graph in topological order. Where all witnesses share a single path through a node,
the exporter outputs invariant text. Where the graph splits into parallel branches,
the exporter wraps the divergent paths within a TEI `<app>` container (Haentjens
Dekker & Middell, 2011).

Understanding this pipeline is crucial for debugging: if an error appears in your
final TEI apparatus, it is rarely an XML serialization bug. It is almost always a
failure that occurred upstream in Phase 1 (tokenization) or Phase 2 (normalization).
If a comma was attached to a word in Phase 1, CollateX will treat that word as a
distinct variant in Phase 3 and export a flawed apparatus in Phase 5.

**Takeaway:** The Gothenburg Model isolates apparatus export as
Phase 5, meaning exported XML fidelity depends entirely on upstream tokenization and
normalization.

---

## **03 Content**

**CollateX Output Formats and TEI Parallel Segmentation**

CollateX is the premier open-source engine for computerized collation, designed by
Ronald Haentjens Dekker and Gregor Middell. While CollateX supports diverse output
formats—including plain text alignment tables, HTML visualization matrices, GraphML,
and JSON—its primary interchange format for digital scholarly editing is TEI XML
(Haentjens Dekker & Middell, 2011).

CollateX natively implements the **Parallel Segmentation** linking method declared in
TEI P5 Chapter 13 (TEI Consortium, 2026). When CollateX generates TEI XML, it embeds
`<app>` elements directly inline within the token stream.

The engine offers specific export flags:

- `-f tei`: Standard TEI export producing inline `<app>`, `<lem>`, and `<rdg>`
  structures.

- `-f tei_ps`: Parallel segmentation export with explicit XML namespace declarations
  (`xmlns="http://www.tei-c.org/ns/1.0"`).

- `-f json`: Raw alignment graph data, enabling custom downstream XML generation.

```xml
<!-- Native CollateX TEI Parallel Segmentation Output -->
<app>
  <rdg wit="#WitnessA">λόγος</rdg>
  <rdg wit="#WitnessB">λόγος</rdg>
  <rdg wit="#WitnessC">νόμος</rdg>
</app>
```

Notice that by default, CollateX generates an un-lemmatized apparatus: every witness
reading is enclosed in an `<rdg>` element. It does not automatically elevate any
single reading to a `<lem>` unless the user explicitly designates a base witness
during execution (Haentjens Dekker et al., 2015). This design reflects a deliberate
theoretical stance: automated tools should record multi-witness alignment neutrally,
leaving the assignment of editorial privilege to the human scholar.

**Takeaway:** CollateX natively exports TEI XML using Parallel
Segmentation, producing un-lemmatized `<rdg>` elements unless a base text is
explicitly configured.

---

## **04 Content**

**Running CollateX to Generate TEI XML**

CollateX can be executed either as a standalone command-line tool (via Java JAR) or
programmatically via its Python library (`collatex`). In a reproducible digital
humanities workflow, the Python API provides maximum flexibility for integrating
collation into automated build pipelines.

To execute a three-witness collation and generate TEI XML directly in Python, we
instantiate a `Collation` object, append our witness transcriptions, and invoke the
`collate()` function with the output parameter set to `"tei"`:

```python
from collatex import Collation, collate

# 1. Instantiate the collation container
collation = Collation()

# 2. Add witness transcriptions
collation.add_plain_witness("WitA", "Ἐν ἀρχῇ ἦν ὁ λόγος")
collation.add_plain_witness("WitB", "Ἐν ἀρχῇ ἦν ὁ λόγος")
collation.add_plain_witness("WitC", "Ἐν ἀρχῇ ἦν ὁ νόμος")

# 3. Execute collation with TEI output serialization
tei_output = collate(collation, output="tei", layout="vertical")

# 4. Save the generated XML to disk
with open("apparatus_generated.xml", "w", encoding="utf-8") as f:
    f.write(tei_output)
```

When executed, CollateX tokenizes each witness by whitespace, aligns matching
tokens, identifies the divergence at token 5 ("λόγος" vs. "νόμος"), and outputs a
valid TEI XML fragment.

In larger production workflows, witnesses are rarely passed as plain strings.
Instead, structured JSON token streams containing pre-normalized values and
diplomatic surface forms are passed to ensure precise alignment control (Haentjens
Dekker et al., 2015). This structured approach allows editors to collate thousands of
lines while preserving underlying paleographical metadata.

**Takeaway:** The Python `collatex.collate()` API automates the
generation of TEI XML apparatuses directly from programmatic witness collections.

---

## **05 Content**

**Anatomy of Generated Parallel Segmentation XML**

Let us inspect the exact structure of the XML document generated by CollateX during
an automated collation run. Understanding this raw output reveals both the strengths
and the rough edges of algorithmic serialization.

When CollateX processes a sentence with multiple variant sites, it segments the text
into invariant text nodes interspersed with `<app>` containers:

```xml
<cx:apparatus xmlns:cx="http://interedition.eu/collatex/ns/1.0"
              xmlns="http://www.tei-c.org/ns/1.0">
  Ἐν ἀρχῇ ἦν 
  <app>
    <rdg wit="#WitA #WitB">ὁ λόγος</rdg>
    <rdg wit="#WitC">ὁ νόμος</rdg>
  </app>
  καὶ ὁ λόγος ἦν πρὸς τὸν θεόν.
</cx:apparatus>
```

Notice several important structural characteristics of this output:

1. **Witness Consolidation.** CollateX automatically merges identical readings into a
   single `<rdg>` element, combining witness sigla into a space-separated `@wit`
   attribute (`wit="#WitA #WitB"`).

2. **Invariant Inlining.** Text segments where all witnesses agree ("Ἐν ἀρχῇ ἦν ")
   are output as direct text children of the parent container, rather than being
   redundantly wrapped in `<app>` tags.

3. **Whitespace Attachment.** CollateX attaches leading or trailing whitespace
   directly to tokens. If tokenization is misconfigured, spaces may be swallowed or
   duplicated at apparatus boundaries.

While this output is structurally sound, it lacks critical editorial metadata: it
contains no `<lem>` element, no `@type` classifications, and no `<listWit>`
catalogue. These elements must be supplied through downstream post-processing scripts
or editorial refinement.

**Takeaway:** CollateX automatically consolidates identical
witnesses into shared `<rdg>` elements and inlines invariant text, but requires
post-processing to add editorial metadata.

---

## **06 Content**

**The Base Text Assignment in Automated Collation**

In classical textual criticism, the editor selects a base text to serve as the
editorial reference point. In automated collation, assigning a base text determines
which reading is serialized into the `<lem>` element and which readings become
`<rdg>` variants.

When using CollateX, the editor can designate a specific witness as the base text
using the `base_text` parameter. When a base text is specified, CollateX transforms
the output from a symmetrical reading list into an asymmetrical critical apparatus:

```python
# Designating Witness A as the authoritative base text
tei_output = collate(collation, output="tei", segmentation=True, base_text="WitA")
```

When serialized with a base text, CollateX extracts the token attested by `WitA`
and wraps it in `<lem wit="#WitA">`. All diverging tokens from other witnesses are
placed into subsequent `<rdg>` tags.

```xml
<app>
  <lem wit="#WitA #WitB">λόγος</lem>
  <rdg wit="#WitC">νόμος</rdg>
</app>
```

However, as discussed in Topic 14, designating a base text introduces genealogical
privilege. If `WitA` contains a corrupt or idiosyncratic scribal error, that error is
elevated to the `<lem>`, while authentic readings in other witnesses are marked as
deviations (Robinson & Driscoll, 2016). Editors must consciously decide whether
their edition requires a base-text apparatus or an un-lemmatized multi-witness graph.

**Takeaway:** Designating a base text in CollateX automatically
populates the `<lem>` element, but structurally privileges that witness's readings.

---

## **07 Content**

**The Problem of Orthographic Noise in Algorithmic Collation**

The greatest challenge facing deterministic collation tools is **orthographic
noise**. In historical manuscript traditions—particularly medieval vernaculars like
Old French, Middle High German, Middle English, and Early Modern Gaelic—spelling was
non-standardized and highly volatile (Camps, Ing, & Spadini, 2019).

Because CollateX relies on exact string equality (or simple Levenshtein edit-distance
matching), it treats every character-level difference as a substantive variation.
If three manuscripts spell the same word as "rois", "roys", and "reis", a naive
CollateX execution will fail to recognize that these are identical lexical items,
generating a noisy apparatus entry:

```xml
<!-- Un-normalized CollateX Output: Superficial Orthographic Noise -->
<app>
  <rdg wit="#MS_A">rois</rdg>
  <rdg wit="#MS_B">roys</rdg>
  <rdg wit="#MS_C">reis</rdg>
</app>
```

When an edition contains thousands of such entries, genuine stemmatic variants (such
as substituting "chevalier" for "seigneur") become buried beneath an avalanche of
meaningless phonetic spellings.

Furthermore, orthographic instability frequently causes CollateX's alignment
algorithm to suffer from **alignment drift**, misaligning adjacent words and
creating artificially fragmented variation units across successive sentences
(Camps, Ing, & Spadini, 2019).

**Takeaway:** Un-normalized historical spelling creates severe
orthographic noise in CollateX, obscuring substantive variants and fragmenting
apparatus entries.

---

## **08 Content**

**The FALCON Solution: NLP Pre-Processing and Normalization**

To solve the problem of orthographic noise without sacrificing diplomatic accuracy,
the FALCON project (**F**or **A**lignment, **L**emmatization and **C**ollatio**N**),
developed by Jean-Baptiste Camps, Lucence Ing, and Elena Spadini, introduced a
breakthrough pre-processing architecture (Camps, Ing, & Spadini, 2019).

Rather than feeding raw transcription strings directly into CollateX, the FALCON
pipeline first processes each witness with advanced Natural Language Processing (NLP)
lemmatizers and morphological taggers (such as Pyrrha, Pie, or Freeling). Each token
in the manuscript is enriched with two distinct properties:

- `t` (**surface form**): The raw, diplomatic graphemic string found in the
  manuscript (e.g., "roys").

- `n` (**normalized lemma**): The standardized dictionary headword (e.g., "roi").

```json
{
  "witnesses": [
    {"id": "A", "tokens": [{"t": "li", "n": "le"}, {"t": "rois", "n": "roi"}]},
    {"id": "B", "tokens": [{"t": "li", "n": "le"}, {"t": "roys", "n": "roi"}]},
    {"id": "C", "tokens": [{"t": "li", "n": "le"}, {"t": "reis", "n": "roi"}]}
  ]
}
```

CollateX is then instructed to align the witnesses based strictly on the normalized
property (`"n"`). Because all three manuscripts share the normalized lemma `"roi"`,
CollateX aligns them perfectly on a single graph node, completely eliminating
alignment drift (Camps, Ing, & Spadini, 2019).

**Takeaway:** The FALCON workflow aligns witnesses on normalized
lemmas (`"n"`) while preserving diplomatic surface strings (`"t"`), eliminating
orthographic noise in automated collation.

---

## **09 Content**

**Re-Injecting Critical Variants into TEI XML**

Once CollateX has successfully aligned witnesses based on normalized lemmas, the
final step of the FALCON architecture is **variant re-injection**. In this step, the
original diplomatic surface forms are re-injected into the final TEI XML apparatus
(Camps, Ing, & Spadini, 2019).

During serialization, the exporter checks whether the aligned tokens differ in their
diplomatic surface forms (`"t"`). If all witnesses share both the same lemma and the
same surface form, the text is output as invariant prose. If witnesses share the same
lemma but differ in spelling, the exporter generates a grouped orthographic entry:

```xml
<!-- Re-injected TEI Apparatus from FALCON Pipeline -->
<app>
  <lem wit="#MS_A">rois</lem>
  <rdg wit="#MS_B" type="orthographic">roys</rdg>
  <rdg wit="#MS_C" type="orthographic">reis</rdg>
</app>
```

If the witnesses differ in their normalized lemma (for example, if `#MS_C` reads
"seigneur" instead of "roi"), the pipeline classifies the entry as a substantive
lexical variant:

```xml
<app>
  <lem wit="#MS_A #MS_B">rois</lem>
  <rdg wit="#MS_C" type="substantive">seigneur</rdg>
</app>
```

This automated re-injection achieves the ideal balance: algorithmic alignment is
robust and noise-free, while the resulting TEI apparatus preserves every authentic
paleographical detail of the original manuscripts (Camps, Ing, & Spadini, 2019).

**Takeaway:** Re-injection maps diplomatic surface forms back into
aligned graph nodes, automatically classifying variants into substantive and
orthographic categories.

---

## **10 Content**

**The Concept of Stratified Editing**

The success of multi-stage pipelines like FALCON highlights a major conceptual
evolution in digital philology: the paradigm of **stratified editing**, formulated by
Ariane Pinche (2025).

In traditional print editing, the establishment of the text was a destructive
pipeline. The editor transcribed the manuscripts, silently regularized spelling,
made conjectures, and published a single polished text, discarding the intermediate
transcription notes and normalization tables. In the age of AI and automated
textual recognition, Pinche argues that a digital edition must be conceived as a
series of distinct, reusable **strata** (layers) of scholarly knowledge (Pinche,
2025).

| Edition Stratum | Data Layer | Content and Encoding | Computational Utility |
| --- | --- | --- | --- |
| **Stratum 1** | Raw Recognition | Raw ATR / HTR outputs; uncorrected characters | Benchmark for machine learning models |
| **Stratum 2** | Diplomatic Transcription | Character-accurate transcription with `<orig>` markup | Material and paleographical analysis |
| **Stratum 3** | Normalized & Lemmatized | Standardized orthography and POS tags | Algorithmic collation and indexing |
| **Stratum 4** | Critical Apparatus | Structured TEI `<app>` with stemmatic variants | Genealogical and editorial scholarship |

Under the stratified editing framework, the TEI critical apparatus is not a
replacement for diplomatic transcription; it is the fourth stratum resting upon
transparently documented lower layers (Pinche, 2025).

When an automated script generates an apparatus, it must link back to these
underlying strata, ensuring that every editorial transformation remains fully
auditable and reproducible.

**Takeaway:** Stratified editing preserves raw ATR, diplomatic
transcription, normalized tokens, and critical apparatus markup as distinct,
reusable layers of scholarship.

---

## **11 Content**

**Managing Transpositions in Algorithmic Apparatuses**

One of the most notoriously difficult textual phenomena for automated collation
engines to handle is **transposition**—where words, phrases, or entire clauses appear
in different sequential orders across witnesses (Haentjens Dekker et al., 2015).

Consider a variation where Witness A reads "ὁ λόγος ἦν ἐν ἀρχῇ" (the word was in the
beginning) while Witness B reads "ἐν ἀρχῇ ἦν ὁ λόγος" (in the beginning was the
word). In a variant graph, CollateX detects this inversion as a pair of crossed
edges. However, serializing crossed graph edges into linear, inline TEI Parallel
Segmentation is mathematically impossible without breaking the token sequence.

When forced to export parallel segmentation for a transposition, CollateX typically
fragments the transposition into two separate, artificial variation units:

```xml
<!-- Fragmented Transposition in Parallel Segmentation -->
<app>
  <rdg wit="#WitA">ὁ λόγος</rdg>
  <rdg wit="#WitB"/>
</app>
 ἦν 
<app>
  <rdg wit="#WitA">ἐν ἀρχῇ</rdg>
  <rdg wit="#WitB">ἐν ἀρχῇ ὁ λόγος</rdg>
</app>
```

This fragmentation obscures the historical reality: the scribe did not delete "ὁ
λόγος" at the start and insert it at the end; the scribe simply transposed the two
phrases (Haentjens Dekker et al., 2015).

To properly represent transpositions, digital editions must either use TEI
Double-Endpoint Attachment (pointing to milestone anchors) or deploy the TEI
`<transpose>` and `<ptr>` elements defined in the `transcr` module.

**Takeaway:** Parallel segmentation cannot linearly serialize
crossed graph edges, fragmenting complex transpositions into artificial additions and
omissions.

---

## **12 Content**

**Transforming CollateX JSON into TEI XML via Python**

Because native CollateX TEI export is limited to basic parallel segmentation,
production digital edition workflows often export CollateX alignment data as JSON,
using custom Python scripts to generate sophisticated, enriched TEI markup.

A CollateX JSON export consists of an alignment table where each row corresponds to
an aligned column across all witnesses:

```json
{
  "table": [
    [["ὁ"], ["ὁ"], ["ὁ"]],
    [["λόγος"], ["λόγος"], ["νόμος"]],
    [["ἦν"], ["ἦν"], ["ἦν"]]
  ],
  "witnesses": ["WitA", "WitB", "WitC"]
}
```

Using Python's `lxml` library, we can iterate through this table, detect columns
containing variation, group identical readings, assign lemmas based on project rules,
and emit fully custom TEI XML:

```python
from lxml import etree

def json_to_tei_app(collatex_json):
    root = etree.Element("div", xmlns="http://www.tei-c.org/ns/1.0")
    witnesses = collatex_json["witnesses"]
    
    for column in collatex_json["table"]:
        # Check if all tokens in the column are identical
        tokens = [cell[0] if cell else "" for cell in column]
        if len(set(tokens)) == 1:
            # Invariant text
            root.text = (root.text or "") + tokens[0] + " "
        else:
            # Divergent tokens -> Create TEI <app>
            app = etree.SubElement(root, "app")
            # First witness as lemma
            lem = etree.SubElement(app, "lem", wit=f"#{witnesses[0]}")
            lem.text = tokens[0]
            # Remaining witnesses as variants
            for w_idx in range(1, len(witnesses)):
                if tokens[w_idx] != tokens[0]:
                    rdg = etree.SubElement(app, "rdg", wit=f"#{witnesses[w_idx]}")
                    rdg.text = tokens[w_idx]
    return etree.tostring(root, pretty_print=True, encoding="unicode")
```

Writing your own serializer gives you total control over attribute injection,
namespace management, and schema compliance.

**Takeaway:** Custom Python serialization of CollateX JSON data
enables editors to inject project-specific lemma rules, metadata attributes, and
advanced XML structures.

---

## **13 Content**

**Generating Location-Referenced and Double-Endpoint Apparatuses Algorithmically**

While Parallel Segmentation is the default export of automated collation, custom
Python post-processors can easily transform alignment data into **Location-Referenced**
or **Double-Endpoint Attachment** apparatuses.

To generate a Double-Endpoint Attachment apparatus algorithmically, the serialization
script performs two passes over the alignment table:

1. **Pass 1 (Base Text Construction):** The script builds the `<body>` text from the
   designated base witness, automatically inserting empty `<anchor xml:id="a1"/>`
   and `<anchor xml:id="a2"/>` elements before and after each contested word span.

2. **Pass 2 (External Apparatus Generation):** The script creates the `<back>`
   container, generating `<app from="#a1" to="#a2">` elements containing the lemma
   and variant `<rdg>` tags targeting those exact milestone IDs.

```xml
<!-- Algorithmically Generated Double-Endpoint TEI -->
<body>
  <p>Ἐν ἀρχῇ ἦν ὁ <anchor xml:id="anc_1"/>λόγος<anchor xml:id="anc_2"/>...</p>
</body>
<back>
  <div type="apparatus">
    <app from="#anc_1" to="#anc_2">
      <lem wit="#WitA #WitB">λόγος</lem>
      <rdg wit="#WitC">νόμος</rdg>
    </app>
  </div>
</back>
```

This automated two-pass architecture eliminates the massive manual labor of
inventing and maintaining hundreds of anchor identifiers, making Double-Endpoint
Attachment practical for large-scale corpora.

**Takeaway:** Algorithmic two-pass serialization enables automated
generation of Double-Endpoint Attachment markup without the tedious manual overhead
of hand-coding anchor IDs.

---

## **14 Content**

**Validation Layer 1: XML Well-Formedness and Schema Validation**

Once an automated script generates a TEI critical apparatus file, that file must
pass through multiple rigorous validation gates before it can be trusted or merged
into a repository. The first gate is **Schema Validation** (TEI Consortium, 2026).

Schema validation evaluates two distinct levels of XML correctness:

- **Well-Formedness:** Checks whether the file adheres to universal XML syntax rules
  (every open tag is closed, attributes are properly quoted, reserved characters like
  `&` and `<` are escaped as entities, and elements do not overlap).

- **Validity:** Checks whether the document conforms strictly to the structural and
  lexical rules defined in the official TEI P5 Relax NG schema (`tei_all.rng`).

```bash
# Validate generated apparatus against TEI P5 Relax NG Schema
jing https://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng      src/modules/Topic_08_Apparatus/apparatus_generated.xml
```

Schema validation immediately detects illegal tag nestings (such as placing a
`<div>` inside an `<app>`), missing mandatory attributes, or unauthorized element
names.

However, schema validation alone is insufficient for critical editions. A document
can be one hundred percent schema-valid while containing catastrophic philological
and referential errors.

**Takeaway:** Schema validation using Relax NG guarantees syntax
well-formedness and TEI structural compliance, serving as the first quality gate.

---

## **15 Content**

**Validation Layer 2: Schematron Rules for Critical Apparatus**

To enforce project-specific business logic that standard Relax NG schemas cannot
express, digital editors use **ISO Schematron**. Schematron allows scholars to define
rule-based assertions using XPath expressions, validating referential integrity and
editorial constraints (TEI Consortium, 2026).

For critical apparatus encoding, Schematron rules enforce four essential
philological constraints:

1. **Witness Integrity:** Every siglum token cited in a `@wit` attribute must match an
   existing `@xml:id` declared inside the `<listWit>` in the header.

2. **No Redundant Readings:** An `<app>` entry must not contain multiple identical
   `<rdg>` elements for the same witness.

3. **Anchor Pairing:** In double-endpoint attachment, every `@from` and `@to` URI
   must resolve to an existing `<anchor>` element in the body text.

4. **Empty Reading Documentation:** If an `<rdg>` is empty (representing an
   omission), it must carry `@type="omission"` or contain a `<lacunaStart/>`.

```xml
<!-- Schematron Rule: Verify that every @wit siglum exists in <listWit> -->
<sch:pattern xmlns:sch="http://purl.oclc.org/dsdl/schematron">
  <sch:rule context="tei:rdg | tei:lem">
    <sch:assert test="every $w in tokenize(@wit, s+) satisfies 
                      //tei:witness[@xml:id = substring-after($w, #)]">
      Error: Apparatus cites an undeclared witness siglum in <sch:value-of select="@wit"/>!
    </sch:assert>
  </sch:rule>
</sch:pattern>
```

Running Schematron validation via Python or `xmllint` guarantees that typos in
manuscript sigla are caught automatically during continuous integration.

**Takeaway:** Schematron rules enforce deep referential integrity,
guaranteeing that every cited witness siglum resolves to a valid entry in the TEI
witness catalogue.

---

## **16 Content**

**The TEI Critical Apparatus Toolbox**

Beyond command-line scripts, one of the most widely used specialist tools for
validating and manipulating TEI apparatus XML is the **TEI Critical Apparatus
Toolbox**, developed by medievalist Marjorie Burghart (EHESS / CIHAM).

The TEI Critical Apparatus Toolbox is an open-source, web-based and standalone suite
specifically engineered to process TEI P5 documents encoded with the `textcrit`
module. It provides an intuitive interface for scholars to audit apparatus
consistency, generate interactive visualizations, and prepare texts for collation.

The Toolbox operates directly on TEI XML files that utilize Parallel Segmentation.
It performs deep parsing of `<app>`, `<lem>`, `<rdg>`, `<rdgGrp>`, `<witDetail>`, and
`<listWit>` elements, executing complex consistency checks that would otherwise
require writing bespoke XSLT stylesheets.

```text
TEI Critical Apparatus Toolbox Core Modules:
1. Consistency Check: Audits witness presence, missing readings, and sigla coverage
2. Edition Display: Generates dynamic positive/negative apparatus web interfaces
3. Collation Preparation: Strips markup to generate clean token streams for CollateX
4. Parallel Text Viewer: Displays side-by-side diplomatic reconstructions of witnesses
```

For digital editors, the Toolbox serves as an indispensable bridge between raw XML
markup and publishable scholarly interfaces.

**Takeaway:** The TEI Critical Apparatus Toolbox provides an
integrated environment for auditing witness consistency, transforming apparatus
views, and publishing dynamic editions.

---

## **17 Content**

**Toolbox Function 1: Witness Consistency Checking**

The most powerful diagnostic feature of the TEI Critical Apparatus Toolbox is its
**Witness Consistency Checker**.

When editing a tradition with dozens of manuscripts, human editors frequently lose
track of witness coverage. If an editor collates ten manuscripts across a chapter,
every single `<app>` entry should account for all ten manuscripts—either as
attesting the lemma, attesting a variant reading, or marked as lacunose. If an `<app>`
entry only accounts for eight manuscripts, two witnesses have silently disappeared
from the dataset.

The Toolbox consistency checker parses the entire `<text>` stream against the
`<listWit>`, generating an interactive **Witness Availability Matrix**:

| Line Number | Variation Unit | Declared Scope | Missing Witnesses | Diagnostic Status |
| --- | --- | --- | --- | --- |
| Line 12 | `B04K1V1U2` | 10 manuscripts | None | Clean (10/10) |
| Line 14 | `B04K1V1U4` | 10 manuscripts | `#CodexBezae` | Warning: Witness omitted! |
| Line 18 | `B04K1V1U8` | 10 manuscripts | `#Minuscule892` | Warning: Witness omitted! |
| Line 22 | `B04K1V2U1` | 10 manuscripts | None (Lacuna active) | Clean (9/9 active + 1 lacuna) |

This diagnostic report instantly pinpoints omissions, enabling the editorial team to
re-examine the manuscript facsimiles and rectify the data before publication.

**Takeaway:** The Toolbox's consistency checker detects
unintentional witness omissions at variation units, preventing silent data loss.

---

## **18 Content**

**Toolbox Function 2: Transforming Parallel Segmentation to Alternate Views**

A fundamental advantage of encoding an apparatus in TEI Parallel Segmentation is
that the underlying XML contains all the data necessary to generate multiple distinct
typographical presentations dynamically.

Using the TEI Critical Apparatus Toolbox, a single TEI XML file can be transformed
on the fly into three completely different editorial views:

1. **Positive Apparatus View:** Renders the established base text with a full
   positive apparatus at the bottom of the screen, explicitly listing all supporting
   witnesses for every lemma and variant.

2. **Negative Apparatus View:** Renders a compressed print-style edition, listing
   only diverging witnesses in the critical notes.

3. **Individual Witness Reconstruction:** Reconstructs the complete diplomatic text
   of any single manuscript (e.g., displaying Codex Vaticanus exactly as it reads) by
   filtering the XML to extract only the tokens tagged with `@wit="#VatGr1209"`.

```text
Single TEI Source -> [XSLT / Toolbox Engine] -> (1) Interactive Web Edition with Pop-up Variants
                                            -> (2) Print-ready PDF with Footnote Apparatus
                                            -> (3) Diplomatic Full-text Witness Transcriptions
```

This flexibility proves that the digital apparatus is not a static document, but a
computational database from which infinite specialized presentations can be
generated (Burnard, 2014).

**Takeaway:** A single TEI Parallel Segmentation file can be
dynamically transformed into positive apparatuses, negative apparatuses, or
complete diplomatic witness reconstructions.

---

## **19 Content**

**Toolbox Function 3: Collation Preparation and Normalization Display**

In addition to auditing and publishing, the TEI Critical Apparatus Toolbox serves a
vital function at the front end of the editorial pipeline: **Collation Preparation**.

When preparing existing TEI transcriptions for automated collation with CollateX,
the text is often encumbered with inline interpretive markup—such as `<persName>`,
`<placeName>`, `<choice>`, `<abbr>`, and `<expan>`. Feeding this raw XML directly
into CollateX causes the collation engine to crash or misinterpret markup tags as
textual tokens.

The Toolbox allows editors to configure automated extraction filters:

- **Regularized Stream:** Automatically selects `<reg>` inside `<choice>`, strips
  all non-textual tags, and outputs a normalized plain-text token stream for CollateX
  alignment.

- **Diplomatic Stream:** Selects `<orig>` and `<abbr>`, outputting an exact surface
  transcription.

Furthermore, the Toolbox provides a side-by-side visualization showing how normalized
tokens align with their underlying diplomatic manuscript facsimiles, providing
complete transparency during editorial review (Camps, Ing, & Spadini, 2019).

**Takeaway:** The Toolbox prepares raw TEI transcriptions for
CollateX by extracting clean normalized or diplomatic token streams.

---

## **20 Content**

**Validating Lacunae and Physical Gaps**

In Lesson 15.1, you learned how `<lacunaStart/>` and `<lacunaEnd/>` milestones
explicitly mark spans of physical parchment loss. In automated workflows, validating
the placement and scope of these lacuna milestones is essential for mathematical
accuracy in downstream stemmatology (Mink, 2004).

When an automated script parses an apparatus, it must maintain a dynamic state
machine tracking which witnesses are currently "active" versus "lacunose".

```text
Lacuna State Machine Logic:
1. Encounter <witness xml:id="MS_A"/>       -> Set State(MS_A) = ACTIVE
2. Encounter <lacunaStart wit="#MS_A"/>     -> Set State(MS_A) = LACUNOSE
3. Variation unit with no mention of MS_A   -> If State(MS_A) == LACUNOSE: VALID (ignore)
                                            -> If State(MS_A) == ACTIVE: ERROR (unrecorded omission!)
4. Encounter <lacunaEnd wit="#MS_A"/>       -> Set State(MS_A) = ACTIVE
```

If a script fails to enforce this state machine, a damaged manuscript will be
falsely flagged as missing data at every variation unit across fifty pages.
Conversely, if an editor forgets to insert `<lacunaEnd/>`, the witness will remain
permanently muted for the remainder of the edition.

Automated validation scripts must parse all milestone pairs and confirm that every
`<lacunaStart>` has exactly one corresponding `<lacunaEnd>` with matching `@wit`
attributes.

**Takeaway:** Automated validation of lacuna state machines ensures
that physically damaged manuscripts are accurately excluded from statistical
collation metrics without false omission warnings.

---

## **21 Content**

**Automated Generation of `<rdgGrp>` Hierarchies**

In Lesson 15.1, you manually grouped related variants into `<rdgGrp>` hierarchies to
distinguish substantive lexical divergences from minor orthographic corruptions. In
an automated pipeline, this grouping can be performed algorithmically using
deterministic rule classifiers.

After CollateX produces an `<app>` entry with multiple `<rdg>` elements, a Python
post-processor evaluates the string distance and morphological lemmas of each
reading:

```python
# Rule-based Variant Hierarchy Classifier
def structure_reading_group(app_elem):
    # If readings share the same base lemma but differ in itacisms,
    # group them into an orthographic <rdgGrp>
    readings = app_elem.findall("tei:rdg", namespaces={"tei": "http://www.tei-c.org/ns/1.0"})
    # Algorithmic clustering logic based on Levenshtein edit-distance...
```

The classifier wraps itacistic variations (e.g., "ἐδέξατο", "ἐδέξατω") inside an
`<rdgGrp type="orthographic">`, while placing major lexical substitutions (e.g.,
"ἔλαβεν" vs. "ἐδέξατο") at the top level of the `<app>` container.

```xml
<app>
  <lem wit="#MS_A">ἔλαβεν</lem>
  <rdgGrp type="substantive">
    <rdg wit="#MS_B">ἐδέξατο</rdg>
    <rdgGrp type="orthographic">
      <rdg wit="#MS_C">ἐδέξατω</rdg>
    </rdgGrp>
  </rdgGrp>
</app>
```

This automated clustering eliminates hundreds of hours of manual markup while
ensuring absolute consistency in how variation hierarchies are modeled across
massive corpora (Camps, Ing, & Spadini, 2019).

**Takeaway:** Deterministic string-distance algorithms and
morphological rules can automatically organize flat CollateX output into hierarchical
`<rdgGrp>` structures.

---

## **22 Content**

**Benchmarking CollateX Output Against Tuesday's Manual Ground Truth**

Today's central laboratory exercise is to benchmark CollateX's automated TEI
output directly against the manual ground truth you established in Lesson 15.1.

To execute this benchmark, we compare the two files using three formal quantitative
metrics:

- **Variation Unit Boundary Recall:** Did CollateX identify the exact same start and
  end word boundaries for each `<app>` that you identified by hand?

- **Token Match Precision:** Did CollateX correctly separate invariant text from
  divergent tokens, or did it swallow adjacent invariant words into the apparatus?

- **Witness Sigla Accuracy:** Did the automated tool properly assign all witness
  sigla to their corresponding readings?

```text
Benchmarking Scorecard (Lesson 15.1 vs. Lesson 15.2):
- Total Variation Units:        14
- Exact Boundary Matches:       12 / 14 (85.7%)
- Boundary Discrepancies:        2 / 14 (Transposition split into 2 units)
- False Positive Variants:       0
- Sigla Resolution Accuracy:    100%
```

Analyzing the discrepancies reveals the precise mathematical behavior of CollateX:
where the algorithm failed to match human judgement, it was almost always due to
complex multi-word transpositions or un-normalized phonetic spellings (Haentjens
Dekker & Middell, 2011).

**Takeaway:** Benchmarking automated apparatuses against manual
ground truth quantifies algorithmic precision and pinpoints systematic collation
edge cases.

---

## **23 Content**

**Case Study: The Beckett Digital Manuscript Project (BDMP)**

To examine how automated collation and TEI apparatus encoding operate at scale in
modern textual scholarship, consider the **Beckett Digital Manuscript Project
(BDMP)**, directed by Dirk Van Hulle and Vincent Neyt (Haentjens Dekker et al.,
2015).

Samuel Beckett's creative process left a vast genetic archive of drafts, notebooks,
typescripts, and self-translations in English and French. The genetic edition aims
to trace the precise evolution of Beckett's works across dozens of authorial
versions.

The BDMP integrated CollateX directly into its core digital infrastructure. Because
modern authorial manuscripts feature massive cancellations, interlinear additions,
and recurring draft revisions, manual collation across thousands of pages was
impossible. The BDMP team developed a customized CollateX interface that ingests
richly encoded TEI transcriptions, aligns genetic draft sequences, and dynamically
renders variant graphs in the browser (Haentjens Dekker et al., 2015).

```text
BDMP Genetic Architecture:
[TEI Draft Transcriptions] -> [CollateX Engine] -> [Interactive Variant Graph Viewer]
                                                -> [Dynamic Genetic Apparatus]
```

The project demonstrated that automated collation is not merely for ancient or
medieval texts; in modern genetic criticism, it provides the only scalable means to
map the non-linear development of an author's thought across decades of revision
(Haentjens Dekker et al., 2015).

**Takeaway:** The Beckett Digital Manuscript Project proves that
CollateX-driven TEI apparatuses are vital for mapping complex genetic draft
revisions in modern literature.

---

## **24 Content**

**Case Study: The Scholastic Commentaries and Texts Archive (SCTA)**

While the BDMP applies automated apparatuses to modern genetic drafts, the
**Scholastic Commentaries and Texts Archive (SCTA)**, directed by Jeffrey C. Witt,
deploys TEI apparatus encoding across a distributed medieval corpus (Witt, 2018).

Medieval scholastic theologians wrote massive commentaries on Peter Lombard's
*Sentences*, creating a dense web of quotations, cross-references, and variant
manuscripts scattered across European libraries. Traditional editions treated each
commentary as an isolated silo.

The SCTA pioneers a Linked Open Data (LOD) architecture where TEI critical
apparatuses are converted into machine-readable RDF graphs. In the SCTA model, every
`<app>` entry, `<lem>`, and `<rdg>` is assigned a persistent URI. Using the
LombardPress publishing framework, raw TEI XML apparatus data is separated entirely
from the user interface (Witt, 2018).

```text
SCTA Linked Architecture:
[TEI Apparatus XML] -> [RDF Triples Graph] -> [SPARQL API] -> [LombardPress Viewer + IIIF Canvas]
```

Researchers can query the SCTA database to find every instance where a 14th-century
commentator quoted a specific variant reading of Augustine, linking the TEI text
directly to high-resolution manuscript images served via the International Image
Interoperability Framework (IIIF) (Witt, 2018).

**Takeaway:** The SCTA transforms TEI apparatus markup into Linked
Open Data, connecting variant readings to global SPARQL endpoints and IIIF image
canvases.

---

## **25 Content**

**Case Study: Coherence-Based Genealogical Method (CBGM) Data Pipelines**

In Lesson 15.1, you learned that the *Editio Critica Maior* (ECM) of the Greek New
Testament relies on the Coherence-Based Genealogical Method (CBGM). Today we examine
the **data pipeline** that feeds millions of apparatus entries into the CBGM
computational matrix (Mink, 2004).

At the Institut für neutestamentliche Textforschung (INTF), thousands of full-text
Greek transcriptions are collated using automated tools. The resulting collations are
validated using strict automated scripts that check for syntax compliance, sigla
resolution, and lacuna continuity.

The validated TEI XML apparatus is then converted into a genealogical matrix where
each variation unit is assigned a local stemma. The CBGM engine parses this matrix to
calculate **pre-genealogical coherence**—the percentage of agreement between every
pair of manuscripts across all variation units (Mink, 2004).

```text
INTF CBGM Pipeline:
[Full Transcriptions] -> [CollateX Collation] -> [TEI XML Apparatus Validation]
                      -> [Local Stemmata Assignment] -> [CBGM Coherence Matrix]
```

If a single automated apparatus entry contains a malformed siglum or an unrecorded
lacuna, the error ripples through thousands of statistical calculations. Strict
deterministic validation is the absolute prerequisite for mathematical stemmatology
(Mink, 2004).

**Takeaway:** The INTF data pipeline proves that rigorous
deterministic validation of TEI apparatus XML is essential for calculating accurate
genealogical coherence in the CBGM.

---

## **26 Content**

**Automating the Pipeline: From Transcriptions to Validated Apparatus**

To achieve full reproducibility in digital editing, all the tools explored today
should be integrated into an automated, single-command build pipeline.

Using a Bash script or a Python workflow manager (such as `doit` or `snakemake`), we
can chain together transcription extraction, CollateX collation, TEI serialization,
and Schematron validation into an uninterrupted pipeline:

```bash
#!/usr/bin/env bash
# End-to-End Automated Apparatus Pipeline
set -euo pipefail

echo "==> Step 1: Pre-processing and tokenizing TEI transcriptions..."
python3 scripts/tokenize_witnesses.py --input raw/transcriptions/ --output build/tokens.json

echo "==> Step 2: Running CollateX alignment with FALCON normalization..."
python3 scripts/run_collatex.py --tokens build/tokens.json --output build/alignment.json

echo "==> Step 3: Serializing alignment graph to TEI Parallel Segmentation..."
python3 scripts/serialize_tei.py --json build/alignment.json --output dist/apparatus.xml

echo "==> Step 4: Validating apparatus against TEI P5 RNG and Schematron..."
jing schemas/tei_all.rng dist/apparatus.xml
python3 scripts/validate_schematron.py --schema schemas/apparatus.sch --xml dist/apparatus.xml

echo "==> Pipeline complete: Validated apparatus generated at dist/apparatus.xml"
```

Running this pipeline guarantees that whenever a transcription typo is corrected in
an underlying manuscript file, the entire critical apparatus is re-collated,
re-serialized, and re-validated in seconds.

**Takeaway:** An automated build pipeline links tokenization,
CollateX alignment, TEI serialization, and validation into a fully reproducible
editorial workflow.

---

## **27 Content**

**Common Failure Modes in Deterministic Apparatus Generation**

While deterministic automation provides speed and mathematical exactness, it is
vulnerable to specific systematic failure modes. When diagnosing automated collation
pipelines, watch for the following four recurring errors:

1. **Alignment Drift:** When un-normalized spelling differences or long omissions
   cause the alignment algorithm to misalign adjacent words, creating cascaded false
   variants across subsequent lines (Camps, Ing, & Spadini, 2019).

2. **Markup Stripping Collateral Damage:** Stripping inline tags (such as
   `<persName>` or `<supplied>`) before collation, resulting in an apparatus that
   lacks essential semantic annotations present in the original transcriptions.

3. **Whitespace and Punctuation Splallowing:** Collapsing punctuation tokens into
   adjacent words during tokenization, causing "λόγος," to fail matching "λόγος".

4. **Sigla Mapping Mismatches:** Discrepancies between witness IDs in the collation
   JSON (e.g., `"id": "A"`) and the authoritative `@xml:id` in the `<listWit>`
   (e.g., `xml:id="CodexA"`), causing Schematron validation failures.

```text
Collation Failure:   MS_A = "word," (with comma) vs. MS_B = "word" (no comma)
Naive CollateX:      Flags as substantive variation!
Corrected Pipeline:  Punctuation stripped during Phase 2 (Normalization)
```

Anticipating these failure modes allows editors to refine upstream normalization
rules rather than attempting to fix exported XML by hand.

**Takeaway:** Upstream tokenization glitches and alignment drift
are the primary causes of malformed apparatus entries in automated collation.

---

## **28 Content**

**Debugging and Repairing Malformed Apparatus Entries**

When automated validation flags an error in a generated apparatus file, editors must
follow a systematic debugging protocol.

**Step 1: Isolate the Variation Unit.** Locate the exact line number and `@xml:id` of
the failing `<app>` entry from the Schematron error log.

**Step 2: Inspect Upstream Collation Data.** Check the corresponding column in the
intermediate CollateX JSON table. Did CollateX align the tokens incorrectly, or did
the serializer output invalid XML?

**Step 3: Refine Normalization or Tokenization Rules.** If the error was caused by
spelling instability or punctuation attachment, add a normalization rule to Phase 2
of your pipeline rather than manually editing the XML file.

**Step 4: Re-run the Automated Pipeline.** Execute the build script and verify that
the Schematron validation passes cleanly.

```text
Editorial Rule: Never manually edit generated XML!
Always fix the upstream rule in Python/JSON and re-run the build pipeline.
```

Adhering strictly to this debugging protocol maintains the core principle of
reproducible digital scholarship: the generated apparatus is a deterministic
artifact of the code and transcriptions, not an artisanal hand-edited document.

**Takeaway:** Always debug automated apparatus errors by correcting
upstream tokenization and normalization rules rather than hand-patching generated
XML.

---

## **29 Content**

**Preparing the Test Suite for Friday's AI Experiments**

Today you have achieved deterministic mastery: you have aligned witnesses with
CollateX, serialized alignment graphs into TEI XML, and validated the output against
strict schemas and Schematron rules.

On Friday, in Lesson 15.3, we will explore the third step of the comparative cycle:
**AI-assisted apparatus construction**. We will evaluate how Large Language Models
(LLMs) handle unstructured legacy printed apparatuses, test their ability to draft
semantic commentary, and confront the dangerous phenomenon of **hallucinated
witnesses and ghost variants**.

To prepare for Friday's experiments, you must assemble a standardized **Evaluation
Test Suite** consisting of three files:

- `ground_truth_manual.xml`: Your hand-crafted TEI apparatus from Tuesday (Lesson
  8.1).

- `deterministic_collatex.xml`: Your validated CollateX apparatus from today (Lesson
  8.2).

- `raw_collation_matrix.json`: The un-lemmatized CollateX alignment table.

On Friday, you will feed these datasets into state-of-the-art language models and
rigorously benchmark their generative output against your deterministic baseline.

**Takeaway:** Today's validated CollateX XML and alignment tables
form the deterministic baseline for Friday's AI evaluation experiments.

---

## **30 Content**

**Summary and the Deterministic Baseline**

Today's meeting has established the deterministic foundation of Topic 8. You have
explored Phase 5 of the Gothenburg Model, mastering the conversion of variant graphs
into TEI Parallel Segmentation XML.

You have investigated the breakthrough architectures that make automated collation
viable for historical texts: the FALCON workflow for NLP-driven lemmatization,
Ariane Pinche's paradigm of stratified editing, and the multi-layered validation
gates provided by Relax NG, ISO Schematron, and the TEI Critical Apparatus Toolbox.

Through real-world case studies—the Beckett Digital Manuscript Project, the
Scholastic Commentaries and Texts Archive, and the Editio Critica Maior—you have seen
how deterministic apparatus generation powers modern digital scholarship at global
scale.

```text
The Three-Step Apparatus Cycle:
- Tuesday:           Manual TEI apparatus construction (Ground Truth established)
- Wednesday (Today): Deterministic CollateX transformation and schema validation
- Friday:            AI-assisted apparatus parsing, hallucination hunting, and HITL
```

With your deterministic baseline securely established and validated, you are fully
equipped to test the capabilities and perils of artificial intelligence in Friday's
investigation.

**Takeaway:** Deterministic CollateX collation combined with
Schematron validation delivers high-speed, mathematically reproducible TEI
apparatuses, establishing the baseline for AI evaluation.

---

## References

Burnard, L. (2014). *What is the Text Encoding Initiative? How to add intelligent
markup to digital resources*. OpenEdition Press.
https://doi.org/10.4000/books.oep.426

Camps, J.-B., Ing, L., & Spadini, E. (2019). *Collating medieval vernacular texts:
Aligning witnesses, classifying variants*. Digital Humanities 2019 (DH2019),
Utrecht. https://hal.archives-ouvertes.fr/hal-02268348

Haentjens Dekker, R., & Middell, G. (2011). Computer-supported collation with
CollateX: Managing textual variance in an environment with varying requirements. In
*Supporting Digital Humanities*.

Haentjens Dekker, R., van Hulle, D., Middell, G., Neyt, V., & van Zundert, J.
(2015). Computer-supported collation of modern manuscripts: CollateX and the
Beckett Digital Manuscript Project. *Digital Scholarship in the Humanities, 30*(3),
452–470. https://doi.org/10.1093/llc/fqu007

Mink, G. (2004). Problems of a highly contaminated tradition: The New Testament.
Stemmata of variants as a source of a genealogy for text types or of single
manuscripts. In *Studies in Stemmatology II* (pp. 13–85). John Benjamins.

Pinche, A. (2025). Editing in the age of AI: stratified establishment of medieval
texts. *International Journal of Digital Humanities*.
https://doi.org/10.1007/s42803-025-00116-6

Robinson, P., & Driscoll, M. J. (Eds.). (2016). *Digital scholarly editing:
Theories and practices*. Open Book Publishers.
https://doi.org/10.11647/OBP.0095

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/

Witt, J. C. (2018). Digital scholarly editions as interfaces: The case of the
Scholastic Commentaries and Texts Archive. In *Digital Scholarly Editions as
Interfaces* (pp. 143–161). BoD–Books on Demand.
