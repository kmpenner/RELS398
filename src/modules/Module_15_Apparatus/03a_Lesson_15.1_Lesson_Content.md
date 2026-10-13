# Lesson 15.1 — Constructing Positive and Negative Apparatus by Hand

*RELS 398 / ENGL 398 · Topic 15: Apparatus*

***Step 1 of the three-step cycle: manual.** Today you construct positive and
negative critical apparatus entries by hand in TEI XML, navigating the structural
tension between traditional print typography and machine-actionable markup.*

---

## **01 Content**

**The Function of the Apparatus Criticus**

The critical apparatus—the *apparatus criticus*—is the foundational mechanism of
textual scholarship. For centuries, printed editions of ancient, medieval, and early
modern texts have relegated variant readings to compressed footnotes at the bottom
of the page, recording where individual manuscripts deviate from a chosen base text
or an editorially reconstructed archetype. In digital scholarly editing, the
apparatus undergoes a profound ontological shift: it ceases to be a static
typographical footnote and becomes a dynamic, machine-actionable graph of textual
transmission.

The apparatus does not exist simply to compile an exhaustive catalogue of scribal
idiosyncrasies for its own sake. Rather, every entry in an apparatus constitutes a
structured historical claim about how a text moved through time, space, and human
hands. When an editor records that three ninth-century manuscripts share a unique
syntactic substitution against all earlier witnesses, that entry is not merely
descriptive; it provides the primary evidence required to deduce genealogical
descent, identify regional scribal networks, isolate dialectal shifts, and
reconstruct lost ancestral exemplars.

In traditional print philology—exemplified by monumental nineteenth-century editions
such as those of Karl Lachmann, Konstantin von Tischendorf, or B.F. Westcott and
F.J.A. Hort—this evidence was severely constrained by the physical economics of paper,
typesetting costs, and page geometry. Editors were forced to compress complex
manuscript evidence into cryptic abbreviations, ellipses, and Latin shorthand. The
digital critical edition dissolves these physical boundaries, allowing scholars to
record comprehensive textual variance with unprecedented granular precision
(Burnard, 2014).

Understanding this computational transformation begins by performing the editorial
labour manually. Today you will construct apparatus entries by hand, encoding
witness variance in Text Encoding Initiative (TEI) XML. By doing so, you will make
explicit every implicit decision that traditional print formats concealed beneath
typographical conventions, establishing the baseline ground truth for our entire
three-step apparatus pipeline.

**Vocabulary.** *Apparatus criticus* — a structured record of variant readings and
editorial decisions across witnesses. *Base text* — the primary witness or
reconstructed reading against which variants are collated. *Variation unit* — the
specific span of text where witnesses diverge.

**Takeaway:** The critical apparatus is not an ornamental footnote
but a structured data model recording evidence of historical transmission.

---

## **02 Content**

**Positive vs. Negative Apparatus in Print Tradition**

Before writing a single line of XML, an editor must confront a fundamental
dichotomy inherited from classical print philology: the distinction between a
positive and a negative apparatus. This distinction governs how witness support is
explicitly documented or tacitly implied across the edition.

In a **positive apparatus**, the editor explicitly lists the witnesses that support
the reading accepted in the main text (the lemma), alongside the witnesses that
support each competing variant reading. For example, if witness A and witness B read
"λόγος" while witness C reads "νόμος", a positive entry explicitly records:
`λόγος] A B ; νόμος C`. Both the lemma's attestation and the variant's attestation
are positively affirmed on the page, leaving no ambiguity regarding which manuscripts
were inspected, which scribal hands were verified, and what each witness actually
contains.

In a **negative apparatus**, the editor records *only* the witnesses that diverge
from the lemma, leaving the witnesses that support the lemma entirely implicit.
Using the same example, a negative entry records merely: `νόμος C`. The reader is
expected to deduce that because only witness C is listed for the variant, all other
extant witnesses in the edition's declared scope (witnesses A and B) necessarily
attest the lemma "λόγος".

| Apparatus Type | Lemma Attestation | Variant Attestation | Space Efficiency | Ambiguity Level |
| --- | --- | --- | --- | --- |
| Positive | Explicitly lists all witnesses | Explicitly lists all witnesses | Low (verbose) | Low (unambiguous) |
| Negative | Implicit (omits witnesses) | Explicitly lists all witnesses | High (compressed) | High (silent on lacunae) |

The negative apparatus was an ingenious typographical compromise developed to save
expensive page real estate in massive print undertakings such as the *Nestle-Aland*
Novum Testamentum Graece or the *Oxford Classical Texts*. In a print volume of seven
hundred pages, adopting a negative apparatus could reduce the overall page count by
thirty percent, making monumental editions economically viable for publishers.
However, this compression introduces severe epistemological vulnerabilities that
become fatal when transferred unthinkingly into digital computational systems.

**Takeaway:** A positive apparatus explicitly attests every
witness for both lemma and variants, whereas a negative apparatus records only
deviating witnesses to economize space.

---

## **03 Content**

**The Epistemological Danger of the Negative Apparatus**

The primary danger of the negative apparatus lies in its reliance on silence. In a
negative apparatus, silence is interpreted as assent: if a manuscript is not cited
against the lemma, the reader must assume it contains the lemma. In computational
philology, however, silence is inherently ambiguous and corrupts quantitative
models.

Consider what an unmentioned witness might actually represent in physical reality. A
manuscript omitted from a negative apparatus entry might indeed attest the lemma
perfectly. But it might equally be physically damaged at that exact line (a lacuna),
missing several quires, unreadable due to faded ink, written in a different dialect
that omits the entire clause, or simply overlooked by a fatigued human collator. A
negative apparatus cannot distinguish between active scribal agreement and the
physical absence of evidence.

When negative apparatus data is ingested by computational algorithms—such as
stemma-generation software, cladistic analysis pipelines, or phylogenetic tools—this
silence creates systematic statistical bias. An algorithm reading an unrecorded
witness will register a false positive for the lemma, artificially inflating the
statistical agreement between damaged manuscripts and the base text (Robinson &
Driscoll, 2016).

```text
Negative entry:      "νόμος C"
Reader assumes:      Witness A = λόγος, Witness B = λόγος
Physical reality:    Witness A = λόγος, Witness B = [parchment torn / lacunose]
Algorithmic error:   Witness B falsely scored as agreeing with Witness A
```

In an edition collating one hundred manuscripts where forty are fragmentary papyri, a
negative apparatus would imply that fragmentary papyri agree with the lemma across
thousands of verses where the papyrus leaves do not physically exist.

For digital scholarly editions, positive encoding is therefore the default best
practice. In TEI XML, every witness evaluated at a variation unit must be
explicitly declared, ensuring that missing text, lacunae, and authentic scribal
readings are transparently differentiated in the underlying dataset.

**Takeaway:** Silent agreement in a negative apparatus conflates
witness presence with physical absence, introducing fatal errors into automated
stemmatic analysis.

---

## **04 Content**

**The TEI P5 Critical Apparatus Module (`textcrit`)**

To model textual variation without the compromises of print typography, the Text
Encoding Initiative provides a dedicated module: the `textcrit` (Critical
Apparatus) module, defined in Chapter 13 of the TEI P5 Guidelines (TEI Consortium,
2026).

The `textcrit` module establishes an expressive, standardized XML vocabulary
specifically designed to encode the complex multi-witness relationships that occur
across manuscript traditions. Rather than treating variants as typographical notes,
`textcrit` models variation as an intrinsic structural dimension of the text itself
(Burnard, 2014).

The module provides elements for declaring variation boundaries, grouping related
readings into genealogical sub-branches, linking readings to precise witness
identifiers, recording detailed codicological notes, and handling physical damage
such as parchment loss. By standardizing these concepts into an interoperable XML
schema, TEI ensures that critical editions are machine-actionable, archivable, and
independent of proprietary software platforms.

```xml
<app>
  <lem wit="#CodexA #CodexB">λόγος</lem>
  <rdg wit="#CodexC">νόμος</rdg>
</app>
```

When you activate the `textcrit` module in a TEI customization (using the TEI Roma
or ODD architecture), you gain access to elements that transform collation data into
richly structured digital knowledge. The schema validates the relationship between
lemmas and variant readings, enforces the presence of witness attestation
pointers, and enables downstream publishing tools to render interactive multi-witness
editions.

Over the following sections, you will learn to apply each core element of this
module by hand, building a comprehensive TEI critical apparatus file from scratch.

**Takeaway:** The TEI P5 `textcrit` module provides a standardized
XML vocabulary that converts textual variation from static print footnotes into
machine-actionable data.

---

## **05 Content**

**Core Elements: `<app>`, `<lem>`, and `<rdg>`**

The atomic unit of variation in the TEI `textcrit` module is the `<app>` (apparatus
entry) element. Every variation unit across your collated witnesses is encapsulated
within an individual `<app>` block (TEI Consortium, 2026).

Inside an `<app>` container, the text is divided into distinct reading elements:

- `<lem>` (**lemma**): Encodes the reading accepted by the editor in the established
  text, or the reading found in the designated base witness.

- `<rdg>` (**reading**): Encodes a variant reading attested by one or more
  diverging witnesses.

An apparatus entry must contain at least one `<rdg>`, and typically contains one
`<lem>` followed by one or more `<rdg>` elements. If an editor chooses not to
privilege any single reading as the lemma (as in a purely diplomatic multi-text
edition), an `<app>` may simply contain multiple competing `<rdg>` elements without
a `<lem>` (TEI Consortium, 2026).

| Critical Element | Syntactic Role | Occurrence in `<app>` | Primary Attributes |
| --- | --- | --- | --- |
| `<app>` | Container for a single variation unit | Parent wrapper | `@type`, `@from`, `@to`, `@loc` |
| `<lem>` | Preferred or base reading (lemma) | Zero or one | `@wit`, `@source`, `@resp` |
| `<rdg>` | Variant reading attested by witnesses | One or more | `@wit`, `@type`, `@cause`, `@hand` |

Notice that the text content inside `<lem>` and `<rdg>` contains the actual
graphemes or tokens found in the manuscripts, while the metadata explaining *who*
attests that reading is stored in attributes. This separation of content from
metadata is fundamental to XML architecture.

Furthermore, `<app>` tags can be nested when complex sub-variations occur within a
broader textual divergence, allowing editors to capture micro-variants without
losing the macro-level variation structure.

**Takeaway:** An `<app>` container encloses the variation unit,
using `<lem>` for the preferred reading and `<rdg>` for variant alternatives.

---

## **06 Content**

**Witness Sigla and the `@wit` Attribute**

In classical philology, individual manuscripts are designated by concise labels
called **sigla** (singular: *siglum*), such as א (Codex Sinaiticus), B
(Codex Vaticanus), or W (Codex Washingtonianus). In TEI XML, witness attestation is
managed through the `@wit` attribute on `<lem>` and `<rdg>` elements (TEI
Consortium, 2026).

The value of a `@wit` attribute is a whitespace-separated list of private Uniform
Resource Identifiers (URIs), each prefixed by a hash symbol (`#`). Each token in
the `@wit` string functions as an ID reference (IDREF) pointing to a unique
`@xml:id` defined in the document's witness catalogue (Burnard, 2014).

```xml
<app>
  <lem wit="#VatGr1209 #SinaitGr">ἐν ἀρχῇ ἦν ὁ λόγος</lem>
  <rdg wit="#AlexGr">ἐν ἀρχῇ ἦν ὁ νόμος</rdg>
  <rdg wit="#EphrGr #BezaeGr">ἦν ὁ λόγος ἐν ἀρχῇ</rdg>
</app>
```

In the example above, the lemma is attested jointly by `#VatGr1209` and `#SinaitGr`.
The first variant is attested by `#AlexGr`, while the second variant (a
transposition) is attested by `#EphrGr` and `#BezaeGr`.

Because XML parsers treat whitespace as an attribute delimiter in IDREFS data types,
multiple witnesses are simply separated by single spaces. If an editor forgets the
leading `#` prefix (writing `wit="VatGr1209"` instead of `wit="#VatGr1209"`), schema
validators will flag the attribute as a malformed URI reference.

Using explicit URI pointers guarantees that sigla are globally unique and immune to
typographic ambiguities (such as confusing Latin letter B with Greek Beta).

**Takeaway:** The `@wit` attribute uses space-separated `#sigla`
pointers to link readings directly to authoritative manuscript identifiers declared
in the TEI Header.

---

## **07 Content**

**Documenting the Witnesses: `<listWit>` and `<witness>`**

Every siglum cited in a `@wit` attribute must be formally declared and described
within the document metadata. If an apparatus contains `@wit="#VatGr1209"`, the XML
file must contain a matching element `<witness xml:id="VatGr1209">` (TEI Consortium,
2026).

Witness declarations are structured inside a `<listWit>` (witness list) element,
which is typically placed in the `<sourceDesc>` of the `<teiHeader>`, or within the
`<front>` matter of the critical edition. Each manuscript receives a `<witness>`
element containing its full shelfmark, repository name, dating, and physical
description (Burnard, 2014).

```xml
<teiHeader>
  <fileDesc>
    <sourceDesc>
      <listWit>
        <witness xml:id="VatGr1209">
          <msDesc>
            <msIdentifier>
              <settlement>Vatican City</settlement>
              <repository>Biblioteca Apostolica Vaticana</repository>
              <idno>Vat. gr. 1209</idno>
            </msIdentifier>
            <head>Codex Vaticanus, 4th century CE</head>
          </msDesc>
        </witness>
        <witness xml:id="SinaitGr">
          <msDesc>
            <msIdentifier>
              <settlement>London</settlement>
              <repository>British Library</repository>
              <idno>Add. MS 43725</idno>
            </msIdentifier>
            <head>Codex Sinaiticus, 4th century CE</head>
          </msDesc>
        </witness>
      </listWit>
    </sourceDesc>
  </fileDesc>
</teiHeader>
```

Furthermore, `<listWit>` elements can be nested to model entire manuscript families
or geographical groupings (such as Byzantine minuscules or Western witnesses).
Attaching an `@xml:id` to a nested `<listWit xml:id="ByzFamily">` allows an editor to
cite the entire group with `@wit="#ByzFamily"` in the apparatus, significantly
reducing markup verbosity while maintaining full traceability to individual codices.

This strict linkage guarantees referential integrity. An automated validator can
scan the entire apparatus, cross-reference every `@wit` token against the
`<listWit>`, and instantly alert the editor if an unregistered siglum or typographical
typo (such as `#VatGr1290` instead of `#VatGr1209`) appears in the text.

**Takeaway:** The `<listWit>` element in the TEI Header defines
authoritative `@xml:id` identifiers, nested families, and metadata for every
manuscript cited in the edition.

---

## **08 Content**

**Nested and Hierarchical Variants: `<rdgGrp>`**

Textual variation is rarely a flat list of isolated alternatives. In complex
manuscript traditions, variants frequently exhibit genealogical clustering, where
several manuscripts share a primary lexical substitution but diverge among
themselves in minor spelling or morphology (TEI Consortium, 2026).

To represent this hierarchical structure without flattening the evidence, TEI
provides the `<rdgGrp>` (reading group) element. An `<rdgGrp>` acts as an
intermediate container inside `<app>`, grouping related `<rdg>` elements under a
shared classification or stemmatic branch.

```xml
<app>
  <lem wit="#CodexA">ἔλαβεν</lem>
  <rdgGrp type="lexical-substitution">
    <rdg wit="#CodexB">ἐδέξατο</rdg>
    <rdgGrp type="orthographic-subvariant">
      <rdg wit="#CodexC">ἐδέξατο</rdg>
      <rdg wit="#CodexD">ἐδέξατοο</rdg>
      <rdg wit="#CodexE">ἐδέξατω</rdg>
    </rdgGrp>
  </rdgGrp>
</app>
```

In this example, the editor records that while `#CodexA` attests the lemma "ἔλαβεν",
witnesses B, C, D, and E share the lexical variant "ἐδέξατο". Furthermore, within
that variant branch, manuscripts D and E exhibit minor itacistic and dittographic
spelling corruptions ("ἐδέξατοο" and "ἐδέξατω").

Grouping readings via `<rdgGrp>` preserves the semantic hierarchy of the tradition.
An automated query can easily extract major lexical divergences across manuscript
families while filtering out superficial orthographic noise (Camps, Ing, & Spadini,
2019).

Without `<rdgGrp>`, an algorithm analyzing this site would treat all four variant
spellings as independent, unrelated divergences, distorting the genealogical stemma.

**Takeaway:** The `<rdgGrp>` element structures complex variations
hierarchically, grouping minor orthographic sub-variants beneath major lexical or
stemmatic divergences.

---

## **09 Content**

**Codicological and Paleographical Context: `<witDetail>`**

A manuscript reading is not merely a string of abstract characters; it is a physical
mark on an ancient physical surface. Scribes wrote in margins, erased mistakes,
corrected previous copyists, and damaged quires. When an editor needs to provide
specific codicological or paleographical notes about a reading, the `<witDetail>`
element is used (TEI Consortium, 2026).

The `<witDetail>` element is placed inside `<app>` alongside the reading it
annotates. It uses the `@wit` attribute to target the specific manuscript, and the
`@target` attribute to point to the `@xml:id` of the corresponding `<rdg>` or `<lem>`.

```xml
<app>
  <lem xml:id="lem_l1_4" wit="#VenetusA">τε καὶ αὐτοί</lem>
  <rdg xml:id="rdg_l1_4" wit="#Townley">τε καὶ ἄλλοι</rdg>
  <witDetail wit="#VenetusA" target="#lem_l1_4" type="correction">
    Written over an erasure by the first hand; the scraped area extends across 
    three character spaces into the right margin.
  </witDetail>
</app>
```

In traditional print editions, such notes were either omitted due to space
constraints or reduced to cryptic Latin sigla like *in ras.* (*in rasura*, over an
erasure) or *m. rec.* (*manu recentiori*, by a later hand).

By encoding this physical data explicitly in `<witDetail>`, digital editions allow
researchers to search, filter, and analyze scribal correction habits across an
entire codex, providing vital data for paleographical, codicological, and material
studies.

Furthermore, `<witDetail>` can link directly to high-resolution IIIF image
coordinates, allowing users to click a footnote and zoom into the exact scraped
parchment fibers on screen.

**Takeaway:** The `<witDetail>` element captures essential
paleographical and codicological context—such as erasures, corrections, and
marginal additions—tied directly to specific witness readings.

---

## **10 Content**

**Handling Physical Damage: `<lacunaStart>` and `<lacunaEnd>`**

One of the most frequent sources of error in textual scholarship is confusing an
intentional scribal omission with physical manuscript destruction. If a folio is
torn away or an ink blot obliterates a line, the manuscript does not "omit" the text
in a genealogical sense; the witness is simply non-extant at that point (TEI
Consortium, 2026).

To handle physical loss with rigorous precision, TEI provides empty milestone
elements: `<lacunaStart/>` and `<lacunaEnd/>`. These elements mark the exact
boundaries of physical damage for a specific witness using the `@wit` attribute.

```xml
<p>
  Ἐν ἀρχῇ ἦν ὁ λόγος, καὶ ὁ λόγος ἦν 
  <app>
    <lem wit="#CodexA #CodexB">πρὸς τὸν θεόν</lem>
    <rdg wit="#CodexC">παρὰ τῷ θεῷ</rdg>
    <rdg wit="#CodexD">
      <lacunaStart wit="#CodexD"/>
    </rdg>
  </app>
  , καὶ θεὸς ἦν ὁ λόγος. 
  <lacunaEnd wit="#CodexD"/>
</p>
```

When an automated collation engine or stemma-generating tool encounters a
`<lacunaStart/>`, it registers that `#CodexD` is inactive across that span. The
algorithm will not penalize `#CodexD` as an "omission" nor score it as agreeing with
the lemma (Mink, 2004).

When the damaged folio resumes, `<lacunaEnd wit="#CodexD"/>` signals that the
witness is once again available for collation. Explicit lacuna tagging is essential
for calculating accurate witness agreement percentages, establishing genealogical
coherence, and avoiding phantom stemmatic branches.

In large-scale traditions with hundreds of fragmentary papyri, milestone lacuna
tracking is the only mechanism that prevents mathematical models from collapsing into
statistical chaos.

**Takeaway:** Milestone elements `<lacunaStart/>` and
`<lacunaEnd/>` explicitly define spans of physical destruction, preventing algorithms
from misclassifying physical loss as intentional omission.

---

## **11 Content**

**The OHCO Problem in Textual Criticism**

While elements like `<app>`, `<lem>`, and `<rdg>` define the vocabulary of variation,
a profound architectural dilemma emerges when linking these variations to the
underlying text: the **OHCO problem** (Ordered Hierarchy of Content Objects).

Standard XML enforces a strict hierarchical tree structure. Every element must be
properly nested inside its parent, and elements cannot overlap across different
branches of the tree. In actual historical manuscripts, however, textual phenomena
frequently cross structural boundaries (Robinson & Driscoll, 2016).

Consider a variant reading that begins in the middle of one sentence and ends halfway
through the next, or a transposition where two entire paragraphs are inverted in
witness B compared to witness A. If an `<app>` tag begins inside one paragraph
`<div>` and attempts to close inside another, the XML becomes instantly malformed
and invalid.

```text
Invalid XML Overlap:
<s>This is the <app><lem>first sentence.</s>
<s>This is the second</lem><rdg>first and second combined</rdg></app> sentence.</s>
```

Similar overlapping traps occur when variants cross poetic verse lines (`<l>`), page
breaks (`<pb/>`), or editorial styling elements. To resolve this fundamental tension
between strict XML nesting and fluid manuscript variation, the TEI P5 Guidelines
specify three distinct architectural linking methods: **Parallel Segmentation**,
**Location-Referenced**, and **Double-Endpoint Attachment** (TEI Consortium, 2026).

**Takeaway:** The OHCO model of XML forbids overlapping tags,
requiring specialized TEI linking architectures to handle variants that cross
structural boundaries.

---

## **12 Content**

**Declaration of Linking Method: `<variantEncoding>`**

Because TEI supports three distinct structural paradigms for critical apparatuses,
every TEI document containing an apparatus must explicitly declare which linking
method it employs. This declaration is placed inside the `<teiHeader>` using the
`<variantEncoding>` element within `<encodingDesc>` (TEI Consortium, 2026).

The `<variantEncoding>` element requires two core attributes:

- `@method`: Specifies the linking mechanism. Allowed values are
  `parallel-segmentation`, `location-referenced`, or `double-endpoint-attachment`.

- `@location`: Specifies where the apparatus entries are stored relative to the
  text. Allowed values are `internal` (inline within the body text) or `external`
  (stored separately in `<back>` or an external file).

```xml
<teiHeader>
  <encodingDesc>
    <variantEncoding method="parallel-segmentation" location="internal"/>
  </encodingDesc>
</teiHeader>
```

This header declaration informs processing software, XSLT stylesheets, and automated
validators how to parse the apparatus. For example, a web viewer encountering
`parallel-segmentation` knows it can render the text by iterating directly through
inline elements, whereas encountering `double-endpoint-attachment` instructs the
software to build a pointer index between `<anchor>` tags and external apparatus
entries.

Without this explicit declaration, downstream transformation stylesheets cannot
reliably determine whether to parse the document as an inline token stream or an
external pointer network.

**Takeaway:** The `<variantEncoding>` element in the TEI Header
declares the project's chosen apparatus architecture (`method` and `location`) for
all downstream software tools.

---

## **13 Content**

**Method 1: Parallel Segmentation (`parallel-segmentation`)**

**Parallel Segmentation** is the most common and intuitive method for encoding a
critical apparatus in TEI XML. Under this method, the `<app>` element is embedded
directly inline within the text stream, exactly where the variation occurs (TEI
Consortium, 2026).

When using parallel segmentation with `location="internal"`, there is no separate
base text file. Instead, the apparatus elements *are* the text. The established
reading is wrapped in `<lem>`, the alternative readings are wrapped in `<rdg>`, and
the surrounding invariant text flows seamlessly around the `<app>` container.

```xml
<p>
  Ἐν ἀρχῇ ἦν ὁ 
  <app>
    <lem wit="#CodexA #CodexB">λόγος</lem>
    <rdg wit="#CodexC">νόμος</rdg>
  </app>
  , καὶ ὁ λόγος ἦν πρὸς τὸν θεόν.
</p>
```

The primary advantage of parallel segmentation is its computational simplicity. It
is exceptionally easy to transform with XSLT stylesheets: selecting all `<lem>`
elements instantly renders the base text, while selecting specific `@wit` values
allows software to reconstruct any individual witness on the fly. Furthermore,
automated collation tools like CollateX natively export in parallel segmentation
format (Haentjens Dekker et al., 2015).

However, parallel segmentation suffers from one severe limitation: it cannot handle
overlapping hierarchies. If a variant spans across a line break `<lb/>`, page break
`<pb/>`, or structural `<div>`, the inline markup breaks XML validity.

**Takeaway:** Parallel segmentation embeds `<app>` directly
inline, making it ideal for XSLT transformation and automated collation, but unable
to handle overlapping hierarchies.

---

## **14 Content**

**Drafting Parallel Segmentation by Hand**

To master parallel segmentation, let us walk through the manual encoding of a Greek
variation unit from the Epistle to the Galatians (Gal 1:1), comparing Codex
Sinaiticus (`#SinaitGr`), Codex Vaticanus (`#VatGr1209`), and Codex Bezae
(`#BezaeGr`).

Suppose the base text reads "Παῦλος ἀπόστολος οὐκ ἀπ᾽ ἀνθρώπων", but Codex Bezae
inserts the adjective "καινὸς" before "ἀπόστολος", while Codex Sinaiticus spells
"ἀπ᾽" as the unelided form "ἀπό".

Here is the step-by-step encoding process:

1. Identify the invariant anchor text before the variation: "Παῦλος ".

2. Open the `<app>` element for the first variation unit (the insertion in Bezae).

3. Encode the lemma (the absence of the word) and the variant reading:
   `<lem wit="#SinaitGr #VatGr1209"/><rdg wit="#BezaeGr">καινὸς</rdg>`.

4. Add the shared token: " ἀπόστολος οὐκ ".

5. Open the second `<app>` element for the orthographic elision:
   `<lem wit="#VatGr1209 #BezaeGr">ἀπ᾽</lem><rdg wit="#SinaitGr">ἀπό</rdg>`.

6. Close with the final invariant token: " ἀνθρώπων".

```xml
<p>
  Παῦλος 
  <app>
    <lem wit="#SinaitGr #VatGr1209"/>
    <rdg wit="#BezaeGr">καινὸς</rdg>
  </app>
  ἀπόστολος οὐκ 
  <app>
    <lem wit="#VatGr1209 #BezaeGr">ἀπ᾽</lem>
    <rdg wit="#SinaitGr">ἀπό</rdg>
  </app>
  ἀνθρώπων
</p>
```

Notice how an omission or insertion is modeled in parallel segmentation: an empty
`<lem/>` or `<rdg/>` explicitly marks the absence of text in that witness branch.
This explicit tagging maintains positive reporting across the entire verse.

**Takeaway:** In parallel segmentation, omissions and additions are
explicitly encoded using empty `<lem/>` or `<rdg/>` tags embedded directly within the
inline token stream.

---

## **15 Content**

**Method 2: Location-Referenced (`location-referenced`)**

The second architectural model is the **Location-Referenced** method. This method
most closely replicates the typographical structure of the traditional printed
critical edition (TEI Consortium, 2026).

In a location-referenced apparatus, the primary base text in the `<body>` contains
clean, uninterrupted prose with no inline `<app>` tags. All apparatus entries are
extracted into a separate container—typically in the `<back>` matter of the document
or in a standalone file—and linked back to the text using a `@loc` (location)
attribute.

```xml
<body>
  <p n="1">Ἐν ἀρχῇ ἦν ὁ λόγος, καὶ ὁ λόγος ἦν πρὸς τὸν θεόν.</p>
</body>
<back>
  <app loc="1">
    <lem wit="#CodexA #CodexB">λόγος</lem>
    <rdg wit="#CodexC">νόμος</rdg>
  </app>
</back>
```

The `@loc` attribute uses human-readable coordinates, such as line numbers, verse
numbers, or page references (`loc="line 14"` or `loc="Gal 1:1"`).

While this method preserves an immaculate base text free of markup clutter, it has
severe computational drawbacks. Because `@loc` coordinates are approximate and
informal, automated software cannot determine the exact word boundaries where the
variant attaches. It is nearly impossible for an algorithm to dynamically reconstruct
witness texts or calculate exact string alignments from a location-referenced
apparatus (Robinson & Driscoll, 2016).

**Takeaway:** Location-referenced apparatuses cleanly separate base
text from variants using `@loc` coordinates, but their informal linkage makes
automated computational processing exceedingly difficult.

---

## **16 Content**

**Drafting Location-Referenced Apparatus by Hand**

To construct a location-referenced apparatus by hand, the editor must establish a
rigorous canonical reference system (such as line numbers or chapter/verse markers)
before drafting the external entries.

Let us encode a two-line poetic passage where the base text resides in `<body>` and
the critical notes reside in `<back>`:

```xml
<text>
  <body>
    <lg>
      <l n="1">Sing in me, Muse, and through me tell the story</l>
      <l n="2">Of that man skilled in all ways of contending</l>
    </lg>
  </body>
  <back>
    <div type="apparatus">
      <app loc="1">
        <lem wit="#Ed1 #Ed2">tell the story</lem>
        <rdg wit="#MS_H">sing the tale</rdg>
        <rdg wit="#MS_L">tell the song</rdg>
      </app>
      <app loc="2">
        <lem wit="#Ed1 #MS_H">in all ways</lem>
        <rdg wit="#MS_L #Ed2">in many ways</rdg>
      </app>
    </div>
  </back>
</text>
```

Notice that in location-referenced encoding, the `<lem>` element is mandatory in
every `<app>` entry because the external note must explicitly quote the exact words
from the base text that are being contested. Without quoting the lemma, a reader
looking at `loc="1"` would have no way of knowing which phrase in line 1 was subject
to variation.

This requirement mirrors traditional print conventions (where the lemma is followed
by a square bracket `]`), making it comfortable for human readers but fragile if line
numbering shifts during subsequent editorial revisions.

**Takeaway:** Location-referenced apparatuses require explicit
lemmas to identify the target phrase within the referenced line or verse coordinate.

---

## **17 Content**

**Method 3: Double-Endpoint Attachment (`double-endpoint-attachment`)**

The third and computationally most sophisticated architectural model is the
**Double-Endpoint Attachment** method (TEI Consortium, 2026).

This method solves the OHCO overlapping hierarchy problem completely by separating
the apparatus from the base text while maintaining mathematically exact,
machine-actionable pointers. In the base text, the editor inserts empty milestone
elements called `<anchor/>`, each equipped with a unique `@xml:id`. The apparatus
entries are stored externally (in `<back>` or a separate XML file) and use `@from`
and `@to` attributes to target those exact anchor points.

```xml
<body>
  <p>
    Ἐν ἀρχῇ ἦν ὁ <anchor xml:id="a1"/>λόγος<anchor xml:id="a2"/>, 
    καὶ ὁ λόγος ἦν πρὸς τὸν θεόν.
  </p>
</body>
<back>
  <app from="#a1" to="#a2">
    <lem wit="#CodexA #CodexB">λόγος</lem>
    <rdg wit="#CodexC">νόμος</rdg>
  </app>
</back>
```

Because `<anchor/>` elements are empty milestones, they can be placed anywhere in
the document—across paragraph breaks, inside quotations, or across structural
boundaries—without violating XML nesting rules.

The apparatus entry cleanly spans the precise substring between `@from="#a1"` and
`@to="#a2"`. This architecture provides the ultimate balance: an unobstructed base
text combined with exact, algorithmic machine-actionability (Schmidt & Colomb, 2009).

**Takeaway:** Double-endpoint attachment uses external `<app>`
elements pointing to `<anchor/>` milestones via `@from` and `@to`, solving
overlapping hierarchies with exact computational precision.

---

## **18 Content**

**Drafting Double-Endpoint Attachment by Hand**

To appreciate the power and overhead of double-endpoint attachment, let us encode a
complex scenario where a variant reading crosses a line boundary within a poetic
stanza.

In this example, witness `#MS_B` transposes the closing words of line 1 and the
opening words of line 2:

```xml
<text>
  <body>
    <lg>
      <l n="1">The wandering prince sailed <anchor xml:id="p1"/>across the wine-dark</l>
      <l n="2">sea of ancient memory,<anchor xml:id="p2"/> seeking his home.</l>
    </lg>
  </body>
  <back>
    <div type="apparatus">
      <app from="#p1" to="#p2">
        <lem wit="#MS_A #Ed1">
          across the wine-dark<lb/>sea of ancient memory,
        </lem>
        <rdg wit="#MS_B">
          over ancient waves<lb/>and dark wine-seas,
        </rdg>
      </app>
    </div>
  </back>
</text>
```

If we attempted to encode this variant using parallel segmentation, the `<app>`
element would have to wrap around the closing `</l>` tag of line 1 and the opening
`<l>` tag of line 2, causing an immediate XML parsing error.

With double-endpoint attachment, `<anchor xml:id="p1"/>` sits inside line 1, and
`<anchor xml:id="p2"/>` sits inside line 2. The external `<app>` bridges the two
milestones effortlessly. The trade-off is substantial encoding overhead: the editor
must invent, maintain, and verify hundreds of unique anchor IDs across the edition.

**Takeaway:** Double-endpoint attachment easily spans structural
tags like line and stanza boundaries, but demands meticulous maintenance of anchor
identifiers.

---

## **19 Content**

**Comparing the Three TEI Linking Methods**

Choosing among the three TEI apparatus linking methods is one of the most critical
architectural decisions in any digital edition project. Once chosen and declared in
the `<variantEncoding>` header, altering the linking method across thousands of lines
requires substantial automated scripting or painful manual re-encoding.

The following comparative evaluation summarizes the trade-offs:

| Technical Criterion | Parallel Segmentation | Location-Referenced | Double-Endpoint Attachment |
| --- | --- | --- | --- |
| **Storage Location** | Inline inside `<body>` | External in `<back>` / file | External in `<back>` / file |
| **Linkage Mechanism** | Direct element wrapping | Approximate `@loc` string | Exact `@from` and `@to` URIs |
| **Overlapping Markup** | Fails completely | Bypasses (informal) | Fully supported via `<anchor>` |
| **XSLT Processing** | Extremely simple | Difficult (fuzzy target) | Moderate (pointer resolution) |
| **CollateX Native Export**| Supported natively | Not supported | Requires custom post-processor |
| **Base Text Legibility** | Cluttered by markup | Immaculate clean prose | Clean except for empty anchors |
| **Machine Actionability** | High | Low | Maximum |

For most straightforward digital editions with stable orthography and well-behaved
word boundaries, Parallel Segmentation remains the standard choice due to its direct
compatibility with automated collation pipelines (Haentjens Dekker & Middell, 2011).
However, for complex manuscript traditions featuring massive structural
transpositions, Double-Endpoint Attachment represents the computational gold
standard.

**Takeaway:** Choose Parallel Segmentation for automated collation
workflows, and Double-Endpoint Attachment when managing overlapping structural
hierarchies and complex transpositions.

---

## **20 Content**

**Editorial Judgement and Lemma Selection**

Encoding an apparatus is never a purely mechanical task; it is an act of deep
critical interpretation. The fundamental decision of what to place in the `<lem>`
element versus what to place in an `<rdg>` element reflects the editor's theoretical
commitments regarding the text.

In a **copy-text or base-text edition**, the editor designates one specific historical
manuscript as the base. The readings of that manuscript are systematically placed in
the `<lem>`, while all deviations in other witnesses are relegated to `<rdg>` tags.
The lemma represents historical attestation in a single document.

In an **eclectic or critical edition** (such as the traditional Lachmannian method),
the editor reconstructs an idealized archetype that may not correspond to any single
surviving physical witness. In this framework, the `<lem>` represents the reading
judged by the editor to be most original based on internal and external evidence
(e.g., *lectio difficilior potior*, the more difficult reading is preferable), while
`<rdg>` elements record corruptions, scribal harmonizations, and secondary variants
(Robinson & Driscoll, 2016).

```xml
<!-- Eclectic Reconstruction: Lemma is an editorial conjecture not found in A or B -->
<app>
  <lem resp="#KMPenner">ἀληθείᾳ</lem>
  <rdg wit="#CodexA">ἀγάπῃ</rdg>
  <rdg wit="#CodexB">πίστει</rdg>
</app>
```

When recording an editorial emendation or conjecture not attested by any surviving
manuscript, the `@resp` attribute on `<lem>` identifies the scholar responsible for
the conjecture, preserving full transparency.

**Takeaway:** The `<lem>` element embodies editorial judgement—whether
designating a historical copy-text reading or an eclectically reconstructed original.

---

## **21 Content**

**Typology of Readings: The `@type` and `@cause` Attributes**

A rigorous critical apparatus does not simply record *what* differs; it classifies
*how* and *why* the text varies. The TEI P5 `textcrit` module provides two key
attributes on `<rdg>` to capture this analytical taxonomy: `@type` and `@cause` (TEI
Consortium, 2026).

The `@type` attribute categorizes the linguistic nature of the variant reading:

- `substantive`: A major lexical or semantic change altering the meaning.

- `orthographic`: A minor spelling variation, itacism, or phonetic shift.

- `grammatical`: A morphological inflection, case change, or tense shift.

- `transposition`: A change in word order across witnesses.

- `omission`: The absence of text present in other witnesses.

- `addition`: The insertion of new material not found elsewhere.

```xml
<app>
  <lem wit="#CodexA">ἔγραψα ὑμῖν</lem>
  <rdg wit="#CodexB" type="transposition">ὑμῖν ἔγραψα</rdg>
  <rdg wit="#CodexC" type="substantive" cause="homoioteleuton">ἔγραψα</rdg>
  <rdg wit="#CodexD" type="orthographic" cause="itacism">ἔγραψα ὑμεῖν</rdg>
</app>
```

The `@cause` attribute documents the paleographical or psychological mechanism that
generated the error during scribal transmission. Common text-critical causes include
`homoioteleuton` (skipping text due to similar line endings), `dittography`
(unintentional duplication), and `itacism` (vowel confusion due to Byzantine Greek
phonology, such as confusing αι and ε, or ει, η, and ι).

Explicitly tagging `@type` and `@cause` transforms the apparatus into an empirical
dataset for studying scribal habits and dialectal evolution across centuries.

**Takeaway:** Use `@type` to classify the linguistic category of a
variant and `@cause` to record the paleographical mechanism behind the scribal
divergence.

---

## **22 Content**

**Scribal Hands and Layers: `@hand` and `<add>` / `<del>`**

Manuscripts are layered physical artifacts. Scribes made corrections while copying
(*prima manus*), contemporary rubricators made adjustments, and subsequent readers
centuries later erased words, added marginal glosses, or altered readings to match
different manuscript families (TEI Consortium, 2026).

To distinguish between the original copyist and later correctors within the
apparatus, TEI combines witness sigla with the `@hand` attribute. First, scribal
hands are declared within the `<witness>` metadata using `<handNote xml:id="..."/>`.
In the apparatus, the reading specifies both `@wit` and `@hand`.

```xml
<app>
  <lem wit="#SinaitGr" hand="#Sinait_orig">ἔχετε</lem>
  <rdg wit="#SinaitGr" hand="#Sinait_corr">ἔχομεν</rdg>
  <rdg wit="#VatGr1209">ἔχομεν</rdg>
</app>
```

In this example, the original scribe of Codex Sinaiticus (`#Sinait_orig`) wrote the
second-person plural "ἔχετε", but a later corrector (`#Sinait_corr`) altered the text
to the first-person plural "ἔχομεν", bringing the manuscript into agreement with
Codex Vaticanus.

Furthermore, editors can embed genetic transcription tags—such as `<add>`
(addition), `<del>` (deletion), and `<subst>` (substitution)—directly inside an
`<rdg>` element. This bridges the gap between text-critical comparison and diplomatic
paleography, creating a truly multi-layered digital edition.

**Takeaway:** The `@hand` attribute and embedded `<add>`/`<del>`
elements precisely record multi-layered scribal corrections across different
historical hands within a single witness.

---

## **23 Content**

**Case Study: St. Francis Xavier University Special Collections**

To ground these theoretical encoding models in physical archival practice, consider
the rare materials preserved in the Angus L. Macdonald Library at St. Francis Xavier
University in Antigonish, Nova Scotia.

The library's Special Collections houses significant Gaelic manuscript and archival
holdings—most notably the Ridge Manuscripts—alongside medieval European manuscript
leaves and early printed books. In regional Scottish Gaelic poetry collections, oral
performance and manuscript transmission coexisted for generations across Cape Breton
and mainland Nova Scotia.

When collating Nova Scotian Gaelic laments and bardic poetry, editors encounter
extreme graphemic instability, dialectal phonetic spelling, and fluid stanza orders
derived from distinct oral recitations. Attempting to encode these witnesses using a
rigid print-based negative apparatus completely obscures the performance variations
inherent to Gaelic oral culture.

```xml
<app>
  <lem wit="#RidgeMS">Bu tu marbhaiche na h-eala</lem>
  <rdg wit="#CapeBretonTrad" type="dialectal">Bu tu marbhaich' an eala</rdg>
  <rdg wit="#HighlandPrint" type="orthographic">Bu tu marbhaiche na h-ealaidh</rdg>
</app>
```

By employing TEI positive parallel segmentation and rich `<witDetail>` annotations,
undergraduate editors at StFX can preserve the exact orthographic integrity of Cape
Breton Gaelic scribes while documenting how transatlantic migration altered poetic
diction over two centuries.

**Takeaway:** Physical archival holdings—such as StFX's Gaelic
manuscripts—demonstrate that positive digital apparatus encoding is essential for
capturing dialectal and performance variance without editorial distortion.

---

## **24 Content**

**Case Study: The Homer Multitext (HMT) and Venetus A**

The limitations of traditional print critical apparatuses are nowhere more
dramatically demonstrated than in the transmission of Homer's *Iliad*. For over a
century, scholarly study of Homer relied on T.W. Allen's 1931 Oxford Classical Text,
which reconstructed an artificial composite archetype and compressed all manuscript
evidence into a dense, negative apparatus (Dué & Ebbott, 2010).

The Homer Multitext (HMT) project, directed by Casey Dué and Mary Ebbott at
Harvard's Center for Hellenic Studies, utterly rejected this Lachmannian archetype
model. Drawing on Milman Parry and Albert Lord's oral-formulaic theory, the HMT
argues that there was no single "original" written text of the *Iliad*; every
manuscript represents a distinct, frozen performance of an evolving epic tradition
(Dué & Ebbott, 2010).

The HMT focuses on the 10th-century Venetus A manuscript (Marcianus Graecus 454),
renowned for its extensive surrounding layers of ancient marginal commentary
(*scholia*). In Allen's 1931 apparatus, an entry at *Iliad* 1.4 noted that the words
"τε καὶ αὐτοί" were written over an erasure. However, Allen failed to record that the
physical erasure was three times larger than the replaced words, completely obscuring
a major scribal intervention that altered the interpretation of the adjacent
scholion.

```text
Traditional Print (Allen 1931):  "τε καὶ αὐτοί in ras." (compressed footnote)
HMT Multitext Model:             Full diplomatic transcription + high-resolution IIIF 
                                 image + CTS URN standoff annotation + scholia linkage
```

Instead of a traditional base text with apparatus footnotes, the HMT uses Canonical
Text Services (CTS) URNs and stand-off markup to treat every witness, scholion, and
image coordinate as an autonomous node in a linked data graph (Dué & Ebbott, 2010).

**Takeaway:** The Homer Multitext proves that print apparatuses
frequently suppress vital physical evidence, demonstrating the need for multi-text
digital architectures.

---

## **25 Content**

**Case Study: Editio Critica Maior (ECM) of the Greek New Testament**

While the Homer Multitext abandons the search for an initial text, the *Editio
Critica Maior* (ECM) of the Greek New Testament—produced by the Institut für
neutestamentliche Textforschung (INTF) in Münster—pursues the reconstruction of the
*Ausgangstext* (Initial Text) across a massive, highly contaminated tradition of over
5,500 Greek manuscripts (Mink, 2004).

Because New Testament scribes regularly harmonized parallel passages and copied from
multiple exemplars simultaneously (contamination), traditional family trees (stemmata
codicum) cannot be drawn. To resolve this, Gerd Mink developed the Coherence-Based
Genealogical Method (CBGM), an algorithmic framework that calculates the statistical
coherence between witnesses across thousands of variation units (Mink, 2004).

The entire computational engine of the CBGM is powered by exhaustive TEI XML
collations. Every single variation unit across hundreds of manuscripts is encoded as
a discrete `<app>` entry containing full positive attestation.

```xml
<app n="B04K1V1U2-4">
  <lem wit="#P66 #P75 #CodexVat">ἐν ἀρχῇ ἦν ὁ λόγος</lem>
  <rdg wit="#CodexBezae">ἦν ὁ λόγος ἐν ἀρχῇ</rdg>
  <rdg wit="#Minuscule892">ἐν ἀρχῇ ἦν λόγος</rdg>
</app>
```

In the ECM workflow, editors assign local genealogical priorities to each variant
(creating a "local stemma" for that `<app>`), which the CBGM software then aggregates
globally to establish pre-genealogical coherence across the entire corpus (Mink,
2004). Without exhaustively validated, machine-readable TEI apparatus data, this
mathematical reconstruction of textual history would be impossible.

**Takeaway:** The ECM demonstrates how exhaustive TEI apparatus
encoding provides the mathematical dataset required for modern phylogenetic methods
like the CBGM.

---

## **26 Content**

**Manual Encoding Exercises: The Three Passages**

To consolidate your practical mastery of manual apparatus construction, you will now
encode three distinct textual problems representing common editorial challenges.

**Exercise 1: Simple Lexical Substitution.** Collating three witnesses where Witness
A reads "ὁ ἥλιος ἔλαμψεν", Witness B reads "ὁ ἥλιος ἔφαεν", and Witness C reads "ὁ
ἀστὴρ ἔλαμψεν". Encode this using positive Parallel Segmentation, designating
Witness A as the lemma.

```xml
<p>
  ὁ 
  <app>
    <lem wit="#WitA #WitB">ἥλιος</lem>
    <rdg wit="#WitC" type="substantive">ἀστὴρ</rdg>
  </app>
  <app>
    <lem wit="#WitA #WitC">ἔλαμψεν</lem>
    <rdg wit="#WitB" type="substantive">ἔφαεν</rdg>
  </app>
</p>
```

**Exercise 2: Multi-Word Transposition with Addition.** Base text reads "in the city of
Rome". Witness B reads "in Rome the great city". Witness C reads "in the city of
Athens". Notice that the variation spans three words and involves both lexical
substitution and syntactic inversion.

```xml
<p>
  <app>
    <lem wit="#WitA">in the city of Rome</lem>
    <rdg wit="#WitB" type="transposition">in Rome the great city</rdg>
    <rdg wit="#WitC" type="substantive">in the city of Athens</rdg>
  </app>
</p>
```

**Exercise 3: Physical Lacuna.** Base text reads "They walked through the dark
forest until dawn." Witness B is physically torn after "through", losing the words
"the dark forest", and resumes at "until". Encode using `<lacunaStart/>` and
`<lacunaEnd/>`.

```xml
<p>
  They walked through 
  <app>
    <lem wit="#WitA">the dark forest</lem>
    <rdg wit="#WitB">
      <lacunaStart wit="#WitB"/>
    </rdg>
  </app>
  until dawn.
  <lacunaEnd wit="#WitB"/>
</p>
```

**Takeaway:** Manual encoding of multi-word variants and lacunae
forces the editor to define precise variation unit boundaries and handle physical
damage explicitly.

---

## **27 Content**

**Common Syntax Pitfalls in Manual TEI XML**

Manual XML encoding is inherently prone to syntactic and structural errors. When
authoring apparatus markup by hand in a text editor, keep an active watch for the
following recurring pitfalls that cause schema validation failures:

1. **Unresolved Sigla References.** Writing `@wit="#CodexA"` when the matching
   `<witness xml:id="CodexA">` in the `<listWit>` is named `Codex_A` or `CodexA1`.
   XML ID/IDREF matching is strictly case-sensitive and must match character for
   character.

2. **Missing Hash Prefix in `@wit`.** Writing `wit="CodexA"` instead of
   `wit="#CodexA"`. In TEI P5, `@wit` takes a list of URI pointers; omitting the `#`
   transforms the siglum into an invalid relative URI.

3. **Unescaped XML Reserved Characters.** Using bare ampersands (`&`), angle
   brackets (`<`, `>`), or unescaped quotes inside prose or attributes. Always use
   standard entity references (`&amp;`, `&lt;`, `&gt;`).

4. **Orphaned Milestone Tags.** Inserting a `<lacunaStart wit="#CodexB"/>` without a
   corresponding `<lacunaEnd wit="#CodexB"/>` later in the document.

5. **Overlapping Tag Violations in Parallel Segmentation.** Attempting to place an
   inline `<app>` across structural elements like `</p><p>` or `</div><div>`.

```text
Common Error:        <rdg wit="CodexA">λόγος & σοφία</rdg>
Corrected XML:       <rdg wit="#CodexA">λόγος &amp; σοφία</rdg>
```

Running an XML syntax linter (such as `xmllint`) in your terminal immediately catches
these well-formedness errors before you submit files to schema validation.

**Takeaway:** Strict vigilance over IDREF pointers, URI `#`
prefixes, XML entity escaping, and milestone closure prevents fatal validation
failures in hand-crafted TEI.

---

## **28 Content**

**Building the Method Reference Document**

As you finalize your manual apparatus encoding, you must document your editorial
rules in a formal **Method Reference Document**. This document serves as the project's
internal editorial constitution, recording every decision made during manual
transcription and collation.

Your Method Reference Document must answer five fundamental architectural questions:

1. **Declared Linking Method:** Which `<variantEncoding>` method
   (`parallel-segmentation`, `location-referenced`, or `double-endpoint-attachment`)
   does the project enforce, and why?

2. **Witness Hierarchy:** Is there a designated copy-text whose readings populate
   `<lem>`, or is the edition eclectic / multi-text?

3. **Granularity of Variation:** Are minor itacisms, movable nu (*nu ephelkystikon*),
   and punctuation variants encoded, or are they regularized in `<orig>` / `<reg>`
   layers?

4. **Typology Taxonomy:** What controlled vocabulary is permitted in `@type`
   (`substantive`, `orthographic`, `transposition`, `omission`, `addition`)?

5. **Sigla Authority:** Where is the authoritative `<listWit>` maintained, and what
   is the exact naming convention for manuscript identifiers?

Documenting these constraints in markdown ensures complete consistency across your
editorial team and provides the baseline specification required to configure
automated tools.

**Takeaway:** A Method Reference Document formalizes project rules
for linking methods, lemma selection, variant classification, and witness sigla.

---

## **29 Content**

**Preparation for Wednesday's Deterministic Transformation**

Today you have experienced the slow, intellectually rigorous labour of constructing
critical apparatus entries by hand. You have determined variation boundaries,
assigned lemmas, classified variants with `@type`, and linked witnesses via `@wit`.

Tomorrow, in Lesson 15.2, you will transition to the second step of the comparative
cycle: **deterministic automation**. You will take the multi-witness collations
generated by CollateX during Week 7 and run deterministic transformation scripts to
convert alignment tables and variant graphs directly into TEI Critical Apparatus XML.

To prepare for Wednesday's session, ensure you have the following components ready in
your workspace:

- Your completed manual TEI XML apparatus file from today's exercises.

- Your verified CollateX alignment JSON export from Topic 7.

- A functional Python 3 environment with `collatex` and `lxml` installed.

- The TEI P5 All Relax NG schema (`tei_all.rng`) downloaded locally for schema
  validation.

Tomorrow you will measure exactly how much human labour CollateX automates, where
algorithmic conversion excels, and where machine alignment fails to replicate the
nuanced classification of the human editor.

**Takeaway:** Today's hand-crafted TEI apparatus serves as the
ground-truth benchmark against which tomorrow's automated CollateX export will be
measured.

---

## **30 Content**

**Summary and the Ground Truth Milestone**

Today's meeting has established the foundational ground truth for Topic 8. You have
explored the transition from print-based negative apparatuses to machine-actionable
TEI XML, mastering the core elements of the `textcrit` module: `<app>`, `<lem>`,
`<rdg>`, `<rdgGrp>`, `<witDetail>`, and milestone lacuna tags.

You have analyzed the profound trade-offs among the three TEI linking methods,
learning why Parallel Segmentation is ideal for inline automated workflows, while
Double-Endpoint Attachment overcomes the OHCO overlapping hierarchy problem in
complex manuscript traditions.

Most importantly, you have experienced why the critical apparatus is an act of
historical interpretation. Deciding what constitutes a lemma, grouping readings into
genealogical branches, and classifying errors with `@cause` requires philological
judgement that no software tool can supply autonomously.

```text
The Three-Step Apparatus Cycle:
- Tuesday (Today):    Manual TEI apparatus construction (Ground Truth established)
- Wednesday:          Deterministic CollateX transformation and schema validation
- Friday:             AI-assisted apparatus parsing, hallucination hunting, and HITL
```

Keep your hand-encoded XML file clean and well-documented. It is the gold standard
against which all subsequent computational methods in this module will be evaluated.

**Takeaway:** Manual TEI apparatus construction makes every
philological assumption explicit, establishing the baseline ground truth for the
entire apparatus pipeline.

---

## References

Burnard, L. (2014). *What is the Text Encoding Initiative? How to add intelligent
markup to digital resources*. OpenEdition Press.
https://doi.org/10.4000/books.oep.426

Camps, J.-B., Ing, L., & Spadini, E. (2019). *Collating medieval vernacular texts:
Aligning witnesses, classifying variants*. Digital Humanities 2019 (DH2019),
Utrecht. https://hal.archives-ouvertes.fr/hal-02268348

Dué, C., & Ebbott, M. (2010). *Mothers in arms: The role of women in the Hebrew
Bible and Homer*. (Homer Multitext Project architecture).

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

Robinson, P., & Driscoll, M. J. (Eds.). (2016). *Digital scholarly editing:
Theories and practices*. Open Book Publishers.
https://doi.org/10.11647/OBP.0095

Schmidt, D., & Colomb, R. (2009). A data structure for representing multi-version
texts online. *International Journal of Human-Computer Studies, 67*(6), 497–514.

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/
