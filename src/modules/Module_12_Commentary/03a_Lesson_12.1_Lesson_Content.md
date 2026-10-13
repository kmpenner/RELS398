# Lesson 12.1 — Drafting Scholarly Commentary Notes by Hand: Categories, Anchors, and TEI Encoding

*RELS 398 / ENGL 398 · Topic 12: Commentary · Meeting #31 (Tue Nov 24)*

***Step 1 of the three-step cycle: manual.** Today you draft scholarly commentary notes by hand across philological, historical, and intertextual categories, establishing anchors and encoding them via TEI §17 standoff mechanisms (`<interpGrp>`, `<note>`, `<ptr>`). That manual corpus becomes the reference against which Wednesday's deterministic intertextual discovery and Friday's AI commentary drafting are measured.*

---

## **01 Content**

**The Epistemology of Scholarly Commentary**

The scholarly commentary is one of the oldest intellectual technologies in the Western and Near Eastern philological traditions. When an editor adds an explanatory note to a historical text, they are not merely decorating the base transcription with extraneous observations; they are actively constructing an interpretive bridge across historical, linguistic, and cultural distance. Far from being a passive paratext or an auxiliary appendage, commentary constitutes a primary genre of critical thought through which communities negotiate textual authority, preserve linguistic heritage, and mediate meaning for contemporary readers (Tafdrup et al., 2026).

The practice of systematic textual annotation originated in the Hellenistic Mediterranean, where the Alexandrian grammarians—most notably Zenodotus of Ephesus, Aristophanes of Byzantium, and Aristarchus of Samothrace—developed specialized critical signs (such as the *obelos*, the *asteriskos*, and the *diplê*) to flag suspected scribal interpolations, metrical anomalies, and mythological parallels in Homeric epic (Blackwell & Smith, 2014). In the medieval manuscript tradition, this impulse materialized in the physical layout of the page: manuscripts such as the famous Venetus A of Homer's *Iliad* enveloped the central poetic text within dense, multi-layered margins containing ancient *scholia* compiled over centuries. The medieval page functioned as an asynchronous, distributed workspace where generations of scholars entered into dialogue with the base text and with one another.

In the print era, the physical constraints of the codex flattened this dynamic dialogue into rigid typographic conventions: the critical apparatus at the bottom of the page, the endnote section at the back of the volume, and the separate multi-volume commentary. While print stabilized citation practices, it isolated annotations within proprietary volumes, preventing dynamic cross-referencing and obscuring the interconnected nature of textual knowledge (Schmidt, 2010).

The digital medium restores and vastly expands the relational architecture of historical commentary. In a digital scholarly edition, commentary ceases to be a static footnote trapped at the bottom of a printed page; it becomes an active, queryable node within an extensible knowledge graph. By linking textual spans to external authority files, digital gazetteers, and intertextual databases, digital commentary transforms the reading experience from linear consumption into an exploratory traversal of cultural history.

**Vocabulary.** *Paratext* — material surrounding the main text (notes, prefaces, apparatus) that frames its reception. *Scholia* — ancient or medieval marginal and interlinear notes explaining grammar, history, or rhetoric. *Epistemology* — the philosophical investigation of what constitutes knowledge and how interpretive claims are justified.

**Takeaway:** Scholarly commentary is an active epistemological practice that transforms historical texts from isolated documents into connected networks of cultural interpretation.

---

## **02 Content**

**Commentary as Layered Hermeneutics**

To design an effective digital commentary, an editor must distinguish commentary from the other critical layers of a scholarly edition: the diplomatic transcription, the critical apparatus, and the translation. While these layers frequently inform one another, they perform fundamentally distinct methodological operations and make different epistemic claims upon the text.

The diplomatic transcription records the physical characters and layout inscribed upon the historical carrier (Lesson 4.1). The critical apparatus records textual variance across surviving witnesses to document transmission history and justify emendations (Lessons 7.1 and 8.1). The translation renders the semantic content of the source text into a modern target language while preserving rhetorical and syntactical nuances (Lesson 11.1). Commentary, by contrast, provides the meta-critical explanation: it unpacks why a specific variant reading matters, why a grammatical construction is anomalous, who a named historical figure was, or what literary tradition an allusion engages.

| Editorial Layer | Primary Object of Analysis | Epistemic Goal | Core Question Answered |
| --- | --- | --- | --- |
| Diplomatic Transcription | Physical manuscript witness | Paleographical fidelity | *What strokes are on the page?* |
| Critical Apparatus | Collated variants across witnesses | Textual genealogy and emendation | *What did different scribes transmit?* |
| Critical Translation | Semantic and pragmatic structure | Linguistic accessibility | *How does this mean in another language?* |
| Scholarly Commentary | Cultural, historical, and linguistic context | Hermeneutic explanation | *What does this passage signify and evoke?* |

Commentary is inherently multi-vocal and layered. A single line of ancient Greek or Latin poetry may simultaneously require an explanation of an irregular Doric dialect form, a historical note on a Hellenistic battle, an intertextual reference to Hesiod's *Theogony*, and an overarching analysis of poetic meter. When an editor combines these disparate observations into a single undifferentiated footnote, the underlying data becomes opaque to computational analysis (Schmidt, 2010).

Digital scholarship addresses this complexity through layered hermeneutics. By decomposing commentary into explicit, semantically typed categories, the digital editor allows readers and analytical algorithms to filter, aggregate, and query specific interpretive threads across an entire corpus without wading through irrelevant prose.

**Vocabulary.** *Hermeneutics* — the theory and methodology of interpretation, particularly of historical and literary texts. *Multi-vocality* — the presence of multiple interpretive voices or analytical perspectives within an edition. *Typological decomposition* — separating complex qualitative commentary into distinct, standardized categories.

**Takeaway:** Commentary provides the interpretive rationale behind textual phenomena, requiring structured categorization to remain computationally tractable and pedagogically effective.

---

## **03 Content**

**The Four Core Categories of Scholarly Notes**

A robust digital commentary requires a disciplined taxonomy. Without explicit categorization, commentary degrades into an idiosyncratic collection of notes that cannot be searched, compared across editions, or converted into linked open data. Based on established traditions in classical and medieval philology and modern digital edition best practices, we formalize four core categories of scholarly commentary.

These four categories span the micro-linguistic to the macro-historical levels of textual analysis:

| Commentary Category | Core Domain | Primary Focus of Scholarly Notes | Typical Reference Types |
| --- | --- | --- | --- |
| Philological / Morphosyntactic | Linguistic mechanics | Irregular morphology, rare vocabulary, syntax, dialectal forms | Lexica, grammars, paleographical treatises |
| Historical / Geographic / Prosopographical | Real-world context | Historical persons, places, events, political institutions, realia | Gazetteers, authority files, historical encyclopedias |
| Intertextual / Citational | Textual relations | Direct citations, verbal echoes, allusions, structural parallels | Authoritative editions, parallel corpus databases |
| Structural / Rhetorical / Thematic | Macro-level form | Narrative voice, rhetorical figures, discourse shifts, themes | Rhetorical manuals, literary and theological commentaries |

When drafting notes by hand, the editor must assign every observation to one of these primary categories. This disciplined classification prevents analytical drift and lays the groundwork for standard encoding in TEI XML and the W3C Web Annotation Data Model.

By maintaining strict boundaries between these four types, a digital project can render distinct views for different audiences—such as hiding advanced philological debates for introductory language students or isolating historical place names for spatial GIS mapping (Francese, 2014; Simon et al., 2017).

**Vocabulary.** *Prosopography* — the historical study of persons, their genealogies, and their social connections. *Realia* — physical objects, customs, and material culture specific to a historical era. *Taxonomy* — a formal system of classification for ordering complex phenomena.

**Takeaway:** Digital commentary must be structured around four rigorous categories: philological, historical, intertextual, and structural-thematic.

---

## **04 Content**

**Category 1: Philological and Morphosyntactic Notes**

Philological notes are the bedrock of classical and historical commentary. Their primary objective is to resolve linguistic friction—to guide the reader through anomalous grammar, dialectal variations, rare lexical items, and archaic syntactic constructions that hinder comprehension or introduce interpretive ambiguity.

In historical Greek and Latin texts, philological notes frequently address dialectal shifts (such as Aeolic or Ionic forms in epic verse), Hellenistic koiné developments (such as the loss of the optative mood or confusion of prepositions), and irregular morphological paradigms. For example, when encountering a rare hapax legomenon or an archaic genitive singular in Homeric Greek (such as -οιο instead of -ου), the philological note provides the normalized lemma, identifies the morphological parsing, cites relevant grammar references, and explains the semantic nuances in context (Francese, 2014).

Furthermore, philological commentary directly intersects with textual criticism (Topic 15). Where the editor has accepted an emendation or preferred a difficult reading (*lectio difficilior*) in the critical apparatus, the philological note provides the extensive rationale:

| Scholarly Component | Editorial Content for 1 Thess 2:7 Example |
| --- | --- |
| Target Passage | 1 Thess 2:7 (ἐγενήθημεν νήπιοι / ἤπιοι) |
| Apparatus Reading | νήπιοι א B C* vs ἤπιοι A C2 D Ψ |
| Morphosyntax | Adjective nominative masculine plural (νήπιος "infant" vs ἤπιος "gentle") |
| Philological Rationale | The reading νήπιοι represents the *lectio difficilior*. Although the metaphor shifts abruptly to a "nursing mother", the Alexandrian witnesses and scribal assimilation to ἐγενήθημεν favor the nasal. |

When authoring philological notes by hand, maintain a concise, standardized format: begin with the targeted lemma or phrase, declare the grammatical category or parsing, cite standard lexica or grammars (e.g., LSJ, BDAG, Smyth, or Kühner-Blass), and explain the precise interpretative consequence of the construction.

**Vocabulary.** *Hapax legomenon* — a word that occurs only once within a specified corpus or text. *Lectio difficilior* — the more difficult reading, often preferred in textual criticism because scribes tend to smooth difficult text. *Morphosyntax* — the interaction between morphological word-forms and syntactic sentence structures.

**Takeaway:** Philological notes explicate linguistic anomalies, grammatical parsing, and text-critical decisions to establish baseline semantic comprehension.

---

## **05 Content**

**Category 2: Historical, Prosopographical, and Geographic Notes**

Historical commentary grounds the literary work in its material and political environment. Ancient and medieval texts assume a vast store of cultural background knowledge that contemporary readers possessed naturally but modern readers lack. The historical note identifies historical persons (prosopography), physical locations (topography/geography), political offices, military events, and social customs.

However, a digital historical note should not merely summarize an encyclopedia article. Its function is to explain the specific relevance of the historical entity within the narrative or argumentative logic of the passage. For example, identifying the city of *Philippi* in a commentary on Acts requires noting not only that it was a city in eastern Macedonia, but specifically that it held the status of a Roman colony (*colonia Iulia Augusta Philippensis*) with the *ius Italicum*, which directly explains the legal privileges and civic pride depicted in the biblical narrative (Simon et al., 2017).

In modern digital workflows, historical notes must be formulated to interface with global Linked Open Data (LOD) authority files. When an editor annotates a historical figure or ancient settlement, the note should explicitly reference persistent, machine-readable identifiers:

| Entity Type | Entity Mentioned | Linked Open Data Authority | Persistent Identifier URI |
| --- | --- | --- | --- |
| Person | Julius Caesar | VIAF / Wikidata | `https://viaf.org/viaf/286265178` |
| Place | Philippi | Pleiades Ancient Places Gazetteer | `https://pleiades.stoa.org/places/501482` |
| Event | Battle of Actium | Wikidata | `https://www.wikidata.org/wiki/Q160181` |
| Group | Pharisees | Library of Congress (LCNAF) | `http://id.loc.gov/authorities/names/sh85100581` |

By anchoring manual historical notes to global gazetteers like Pleiades and authority registries like VIAF, the editor ensures that the commentary is not a closed silo, but a bridge to the broader semantic web (Simon et al., 2017).

**Vocabulary.** *Linked Open Data (LOD)* — structured data published on the web in standard formats that can be automatically interlinked across diverse repositories. *Gazetteer* — a geographic dictionary or directory used in conjunction with maps and historical texts. *Pleiades* — a community-built digital gazetteer of ancient places.

**Takeaway:** Historical notes identify persons, places, and realia, providing cultural context while anchoring entities to persistent linked open data identifiers.

---

## **06 Content**

**Category 3: Intertextual and Citational Notes**

Intertextual commentary documents the web of literary relations that connects a text to preceding and contemporary works. Authors in antiquity and the Middle Ages composed within rich traditions of imitation, citation, and allusion (*mimesis* and *aemulatio*), frequently embedding unacknowledged quotations, subtle verbal echoes, or structural parodies into their writing (Coffee et al., 2012).

Intertextual notes must distinguish between different degrees of textual connection:

| Intertextual Level | Definition and Criteria | Example Phenomenon |
| --- | --- | --- |
| Explicit Direct Citation | Author explicitly introduces an external text with a citation formula | "As it is written in the prophet Isaiah..." |
| Strict Verbal Borrowing | Verbatim or near-verbatim text reuse without an explicit formula | Quoting a classical poetic verse or liturgical formula |
| Literary Allusion / Echo | Non-verbatim borrowing sharing rare vocabulary and syntactic shape | Adapting Homeric epic phraseology in Hellenistic prose |
| Structural / Thematic Parallel | Shared narrative architecture or conceptual schema without shared words | Modeling a journey narrative upon the Homeric Nekyia |

In the DanteSources project, researchers established an explicit ontology (integrating CiTO, the Citation Typing Ontology) to categorize how Dante Alighieri engaged with his classical and medieval sources in the *Divine Comedy* and *Convivio* (Bartalesi et al., 2018). An intertextual note must not simply state "cf. Homer"; it must specify whether the author is explicitly quoting, implicitly parodying, directly translating, or conceptually refuting the cited source.

When drafting intertextual notes manually, record: (1) the exact source work and hierarchical passage, (2) the nature of the relationship (e.g., citation, allusion, polemical response), (3) the shared lexical or structural tokens, and (4) the literary significance of the borrowing. This structured manual record serves as the benchmark against which automated intertextual search engines (like Tesserae) are evaluated (Coffee et al., 2012).

**Vocabulary.** *Allusion* — an indirect or covert reference in literature to another work, person, or event. *CiTO (Citation Typing Ontology)* — a formal semantic ontology that characterizes the nature and purpose of citations between works. *Mimesis* — the classical literary practice of imitating and transforming authoritative model texts.

**Takeaway:** Intertextual notes categorize the precise nature of textual borrowing, distinguishing between explicit quotations, subtle echoes, and conceptual parallels.

---

## **07 Content**

**Category 4: Structural, Rhetorical, and Exegetical Notes**

The fourth category operates at the macro-level of literary form and theological or philosophical exegesis. Structural and rhetorical notes do not dissect individual words or identify external persons; instead, they analyze how the author constructs an argument, manages narrative pacing, deploys classical rhetorical figures, and articulates major conceptual themes.

In ancient rhetoric, authors structured speeches and treatises according to established formal divisions: the *exordium* (introduction), *narratio* (statement of facts), *propositio* (thesis), *probatio* (argumentation/proof), *refutatio* (rebuttal of objections), and *peroratio* (conclusion). A structural commentary note tracks these macro-level transitions, marking where the author pivots from narrative exposition to theological exhortation (e.g., moving from indicative theological statements to imperative ethical commands in Pauline epistles).

Rhetorical commentary similarly explicates figures of speech and thought:

| Rhetorical Dimension | Analytical Focus in Commentary | Scholarly Function |
| --- | --- | --- |
| Formal Discursive Unit | Identifying *exordium*, *probatio*, or *peroratio* | Maps overall argumentative architecture |
| Syntactic Figures | Documenting *chiasmus*, *parallelism*, *antithesis* | Explains stylistic rhythm and emphasis |
| Tropes and Schemes | Analyzing *metaphor*, *allegory*, *irony* | Unpacks figurative and symbolic meaning |
| Exegetical Synthesis | Tracing covenantal, ethical, or metaphysical themes | Connects local passage to author's broader theology |

Structural and exegetical notes provide the interpretive framework that gives coherence to the micro-level philological and historical notes. When encoded digitally, they allow scholars to analyze how rhetorical structures align with thematic developments across complex literary works (Klie et al., 2018).

**Vocabulary.** *Exegesis* — critical explanation or interpretation of a text, especially religious or philosophical literature. *Typology* — a method of biblical interpretation wherein people, events, or institutions in the Old Testament are viewed as prefigurations of the New Testament. *Antithesis* — a rhetorical figure wherein contrasting ideas are placed in sharp juxtaposition.

**Takeaway:** Structural and rhetorical notes explicate discourse architecture, argumentative transitions, and macro-level interpretive motifs.

---

## **08 Content**

**The Dilemma of the Anchor**

Once commentary notes are drafted, the digital editor faces a profound architectural challenge: how should these notes be attached to the text? In print, notes are bound to physical page coordinates or footnote superscript numbers. In digital editions, this connection is governed by the **anchor mechanism**—the computational method used to link an interpretive note to a specific span of source text.

Historically, early digital humanities systems attached notes using raw **character byte offsets** (e.g., "start at character 1,420 and end at character 1,455"). While computationally trivial to compute, byte offsets are catastrophically brittle. The moment an editor corrects a single typo upstream, normalizes a spelling, or inserts an omitted punctuation mark, every subsequent byte offset across the entire document shifts out of alignment, corrupting the commentary corpus (Sanderson et al., 2017).

Alternative approaches, such as relying purely on XML Document Object Model (DOM) paths or XPath queries (e.g., `/TEI/text/body/div[2]/p[4]/w[12]`), offer higher stability against character edits within sibling nodes. However, they break instantly if structural markup is refactored—such as when a paragraph is subdivided into lines, or when two chapters are merged (Schmidt, 2010).

| Anchor Mechanism | How It Identifies Text | Failure Mode | Resilience Rating |
| --- | --- | --- | --- |
| Byte Offset | Integer character position from file start | Breaks on any upstream edit | Very Low |
| Pure DOM/XPath | XML tree address of the containing element | Breaks when markup hierarchy changes | Moderate |
| Unique `xml:id` | Explicit identifier assigned to text element | Highly stable; requires pre-tagging every word | High |
| Canonical URN | Standardized hierarchical intellectual citation | Independent of files, markup, and domains | Exceptional |

To build durable digital editions that survive software updates, markup revisions, and web migration, editors must employ stable, technology-independent addressing mechanisms.

**Vocabulary.** *Anchor* — the precise mechanism or selector that binds an annotation to a specific target in a digital document. *Byte offset* — the position of a character expressed as a numerical distance in bytes from the start of a file. *Brittleness* — the vulnerability of an automated link to break when the underlying source document undergoes minor revisions.

**Takeaway:** Primitive character offsets break when text is edited; digital commentary requires resilient anchor mechanisms based on unique IDs and canonical citation schemes.

---

## **09 Content**

**Canonical Text Services (CTS) and CITE Architecture**

To resolve the fragility of digital text anchors, Christopher Blackwell and Neel Smith developed the **Canonical Text Services (CTS)** protocol and the **CITE Architecture** at Harvard University's Center for Hellenic Studies (Blackwell & Smith, 2014). The foundational insight of the CTS model is that digital humanities projects must cite *intellectual works*, not arbitrary digital files or temporary web URLs.

When a classical scholar cites "Homer, *Iliad* 1.1," that citation remains valid whether the reader is looking at a 10th-century Byzantine parchment, an 18th-century printed edition, or a modern TEI XML file on GitHub. The CTS protocol translates this timeless scholarly citation practice into a formal, machine-actionable syntax: the **CTS Uniform Resource Name (URN)** (Blackwell & Smith, 2014).

A CTS URN is a persistent, globally unique identifier structured into five distinct hierarchical components:

| CTS URN Component | Formal Segment | Purpose in Citation | Example Value |
| --- | --- | --- | --- |
| Protocol Scheme | `urn:cts:` | Declares the formal URI scheme and protocol | `urn:cts:` |
| Namespace | `greekLit:` | Domain authority or disciplinary corpus | `greekLit:` |
| Textgroup | `tlg0012:` | Author or traditional corpus grouping | `tlg0012` (Homer) |
| Work | `tlg001:` | Specific intellectual composition | `tlg001` (*Iliad*) |
| Version | `perseus-grc2:` | Specific digital edition or translation | `perseus-grc2` |
| Passage | `1.1-1.5` | Hierarchical canonical citation range | `1.1-1.5` (Book 1, lines 1–5) |

By utilizing CTS URNs within digital commentary, an editor binds notes to the abstract, canonical hierarchy of the work rather than to a transient HTML page.

**Vocabulary.** *CTS URN* — Canonical Text Services Uniform Resource Name; a standardized, syntax-governed identifier for citing textual passages. *CITE Architecture* — Collection, Index, Text, Extension; a computational framework for citing scholarly resources. *Textgroup* — the authorial or traditional grouping of related works within CTS.

**Takeaway:** CTS URNs provide technology-independent, persistent identifiers that link commentary to canonical intellectual works rather than fragile web files.

---

## **10 Content**

**Hierarchical Addressability with CTS URNs**

The true power of CTS URNs lies in their hierarchical addressability. Because the URN syntax models the internal structure of the literary work, a digital system can address the text at multiple granularities—from an entire multi-volume work down to a single word or character token (Blackwell & Smith, 2014).

Consider how a digital commentary can target different structural depths of the same historical text using CTS syntax:

| Citation Level | CTS URN Suffix | Target Scope | Primary Commentary Use Case |
| --- | --- | --- | --- |
| Corpus / Work | `tlg0012.tlg001:1-24` | Entire epic | Overarching thematic introductions and structural overviews |
| Section / Book | `tlg0012.tlg001:1` | Complete Book 1 | Narrative division notes and compositional outlines |
| Line / Verse | `tlg0012.tlg001:1.1` | Single verse line | Line-level context, historical realia, and poetic meter |
| Range | `tlg0012.tlg001:1.1-1.7` | Opening proem | Rhetorical units, extended speeches, and allegories |
| Token Sub-reference | `tlg0012.tlg001:1.1@μῆνιν[1]` | First token occurrence | Morphosyntactic parsing and lexical definitions |

This sub-reference syntax (`@token[index]`) allows an editor to anchor a philological note directly to a specific grammatical word without requiring the underlying XML document to insert intrusive markup tags around that word (Blackwell & Smith, 2014). If a sentence contains two instances of the particle καί, `@καί[2]` unambiguously targets the second occurrence.

Furthermore, CTS URNs support version-independent addressing. If an editor omits the version segment (`tlg0012.tlg001:1.1`), the commentary attaches to *any* edition or translation of Homer's *Iliad* that implements the CTS protocol, enabling cross-edition commentary sharing across institutions.

**Vocabulary.** *Sub-reference* — an extended syntax in CTS URNs (using `@`) that targets specific words or characters within a canonical passage. *Hierarchical granularity* — the ability of an addressing system to operate across multiple nested levels of a text. *Version independence* — the property of a citation that allows it to resolve across different editions of the same work.

**Takeaway:** CTS URN sub-references allow commentary to target entire chapters, verse ranges, or individual words with mathematical precision and cross-edition durability.

---

## **11 Content**

**The Overlapping Hierarchies Problem in XML**

When implementing digital commentary within standard markup languages like XML, textual scholars inevitably run into a fundamental technical barrier: the **overlapping hierarchies problem** (Schmidt, 2010).

Standard XML enforces the **Ordered Hierarchy of Content Objects (OHCO)** model. In this model, every document is treated as a strictly nested tree structure: elements must open and close cleanly within their parent containers (`<a><b></b></a>`). Overlapping tags (`<a><b></a></b>`) are strictly forbidden and cause XML parsers to fail instantly.

However, historical cultural heritage texts are not single trees; they are multi-dimensional fabrics containing multiple concurrent, non-coincident hierarchies:

| Concurrent Hierarchy | Structural Units Involved | Conflict Example with Standard XML |
| --- | --- | --- |
| Physical Carrier | Pages, columns, line breaks (`<pb/>`, `<cb/>`, `<lb/>`) | A sentence begins on Page 1 Col B and ends on Page 2 Col A |
| Literary / Metrical | Stanzas, poetic lines, stichs (`<lg>`, `<l>`) | A syntactic clause crosses from line 14 into line 15 |
| Syntactic / Linguistic | Sentences, clauses, phrases (`<s>`, `<cl>`, `<phr>`) | A quotation begins mid-clause and spans three poetic lines |
| Editorial Commentary | Philological and historical notes (`<note>`) | An interpretive note targets a phrase spanning across a line break |

As Desmond Schmidt has extensively argued, embedding interpretive commentary directly into the primary XML text stream forces the editor to choose one hierarchy as dominant while artificially fragmenting or corrupting all concurrent hierarchies (Schmidt, 2010). If an editor creates an inline `<note>` tag that begins in the middle of one metrical line and extends across a page break into the next sentence, standard XML cannot represent this without convoluted milestone elements (`<milestone/>`) or fragmented tags.

Embedding commentary directly into the base text stream creates severe maintenance liabilities: it clutters the transcription, obscures paleographical data, complicates collaborative editing, and risks breaking document validation whenever a note is edited (Schmidt, 2010).

**Vocabulary.** *OHCO model* — Ordered Hierarchy of Content Objects; the theoretical model underlying XML that treats documents as strictly nested trees. *Overlapping hierarchies* — a condition where two or more logical structural systems in a document cross boundaries without nesting. *Milestone tag* — an empty XML tag used to mark a boundary in a secondary hierarchy without enclosing content.

**Takeaway:** Embedded XML markup cannot natively handle overlapping physical, metrical, and interpretive structures, necessitating externalized annotation architectures.

---

## **12 Content**

**Introduction to TEI Stand-Off Markup**

To overcome the overlapping hierarchies problem and decouple interpretive commentary from primary manuscript transcriptions, the Text Encoding Initiative (TEI) introduced **stand-off markup** (TEI Consortium, 2026).

In stand-off markup, annotations, linguistic parsings, and commentary notes do not reside inline within the flow of the transcription. Instead, the primary text remains pristine, containing only the baseline transcription and stable structural tags. All editorial interpretations, historical notes, and intertextual cross-references are stored in a dedicated, external container element: the `<standOff>` element (TEI Consortium, 2026).

The `<standOff>` container is placed at the document level (as a child of `<TEI>`, following `<teiHeader>` and parallel to `<text>`), or in an entirely separate XML document:

```xml
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
    <!-- Catalogue and metadata -->
  </teiHeader>
  <text>
    <body>
      <div type="chapter" n="1">
        <p>
          <w xml:id="w1">Ἐν</w>
          <w xml:id="w2">ἀρχῇ</w>
          <w xml:id="w3">ἦν</w>
          <w xml:id="w4">ὁ</w>
          <w xml:id="w5">λόγος</w>
        </p>
      </div>
    </body>
  </text>
  <standOff>
    <!-- All commentary notes, interpretations, and LOD links live here -->
  </standOff>
</TEI>
```

This architectural separation provides transformative advantages for the digital editor:

- **Transcription Integrity:** The diplomatic or critical text remains clean, easily readable, and protected from accidental corruption during commentary revisions.
- **Infinite Interpretive Layers:** Multiple scholars can author competing or specialized commentary layers (e.g., a linguistic layer, a theological layer, a feminist critical layer) referencing the same base text without interference.
- **Overlapping Spans:** Commentary notes can target arbitrary spans of text that cross line, sentence, or page boundaries without causing XML validation errors (Schmidt, 2010).

**Vocabulary.** *Stand-off markup* — a markup technique where annotations and structural codes are stored outside the primary text stream and connected via pointers. `<standOff>` — the official TEI container element for contextual and interpretive data. *Separation of concerns* — a software architecture principle separating distinct domains of data to enhance maintainability.

**Takeaway:** TEI stand-off markup externalizes commentary into a dedicated container, preserving transcription integrity while supporting infinite overlapping interpretive layers.

---

## **13 Content**

**TEI §17 Simple Analytic Mechanisms**

Chapter 17 of the TEI P5 Guidelines, titled *Simple Analytic Mechanisms*, provides the formal toolkit for encoding scholarly commentary, thematic analyses, and interpretive groupings in stand-off architectures (TEI Consortium, 2026).

Rather than forcing commentary into generic, untyped paragraph tags, TEI §17 provides specialized semantic elements designed to express complex hermeneutic judgments:

| TEI Element | Full Formal Name | Core Function in Commentary | Key Attributes |
| --- | --- | --- | --- |
| `<interpGrp>` | Interpretation Group | Groups related interpretive notes by category, theme, or author | `@type`, `@subtype`, `@resp` |
| `<interp>` | Interpretation | Formal statement of an interpretive or conceptual analysis | `@xml:id`, `@type`, `@inst`, `@resp` |
| `<spanGrp>` | Span Group | Groups a collection of contiguous or non-contiguous text spans | `@type`, `@resp`, `@target` |
| `<span>` | Span | Associates an interpretive note with a specific span of characters/words | `@xml:id`, `@from`, `@to`, `@target` |
| `<ptr>` | Pointer | Empty pointing element establishing an unambiguous directional link | `@target`, `@type`, `@cRef` |
| `<link>` | Link | Bidirectional or multi-target association between multiple nodes | `@targets`, `@type`, `@resp` |

These elements function as an integrated relational network. An editor creates an `<interpGrp>` declaring a broad category of commentary (e.g., `type="philological"`), populates it with individual `<interp>` or `<note>` elements containing the explanatory prose, and connects those notes to targeted words in the `<text>` using `<ptr>` or `<span>` elements (TEI Consortium, 2026).

By adopting TEI §17 mechanisms, a digital scholarly edition transforms humanistic prose into a structured, machine-actionable database of critical arguments.

**Vocabulary.** *TEI P5* — the current fifth version of the Text Encoding Initiative Guidelines. *Analytic mechanism* — a formal markup structure designed to encode textual analysis and interpretation. *Relational network* — a system of data objects connected by explicit, typed references.

**Takeaway:** TEI §17 provides standardized analytic elements (`<interpGrp>`, `<interp>`, `<span>`, `<ptr>`) for formalizing humanistic commentary into structured, queryable data.

---

## **14 Content**

**Encoding Editorial Interpretations with `<interpGrp>` and `<interp>`**

The `<interpGrp>` (interpretation group) and `<interp>` (interpretation) elements allow editors to declare analytical categories and attach interpretive labels to text spans.

The `<interpGrp>` element acts as a thematic container, collecting interpretations that belong to a single domain of inquiry. For example, an editor can create separate groups for rhetorical figures, theological concepts, and prosopographical identifications. Individual `<interp>` elements inside the group define specific values within that domain (TEI Consortium, 2026):

```xml
<standOff>
  <!-- Rhetorical Analysis Group -->
  <interpGrp type="rhetoric" resp="#kmp">
    <interp xml:id="rhet-antithesis">Antithesis: contrasting parallel clauses</interp>
    <interp xml:id="rhet-chiasmus">Chiasmus: ABBA syntactic inversion</interp>
    <interp xml:id="rhet-metaphor">Metaphor: source-domain conceptual transfer</interp>
  </interpGrp>

  <!-- Thematic and Theological Group -->
  <interpGrp type="theology" resp="#kmp">
    <interp xml:id="theo-covenant">Covenant theology and divine promise</interp>
    <interp xml:id="theo-eschatology">Eschatological judgment and restoration</interp>
  </interpGrp>
</standOff>
```

Once defined, these interpretations can be linked to the base text in two ways:

- **In-text association:** Adding the `@ana` (analysis) or `@inst` (instance) attribute directly to a text element in the body: `<seg ana="#rhet-antithesis">...</seg>`.
- **Stand-off association:** Using a separate `<link>` element in the `<standOff>` container to pair the text span with the interpretation ID without modifying the transcription stream (Schmidt, 2010).

This structure ensures consistency across a multi-editor project. When multiple scholars annotate a corpus, they select from a controlled vocabulary of `<interp>` definitions, eliminating terminological divergence and enabling macro-level comparative queries.

**Vocabulary.** *Controlled vocabulary* — an authoritative, restricted list of terms used for indexing and categorizing data. `@ana` — TEI attribute used to associate any text element with an external interpretive definition (`<interp>`). `@resp` — TEI attribute designating the scholar responsible for an editorial assertion.

**Takeaway:** `<interpGrp>` and `<interp>` formalize controlled vocabularies of editorial interpretation, linking analytical concepts to text spans via standard attributes.

---

## **15 Content**

**Pointing and Linking: The `<ptr>` and `<link>` Elements**

Connecting stand-off commentary to the base transcription requires precise pointing syntax. In TEI XML, this is achieved primarily through the empty `<ptr>` (pointer) and `<link>` elements (TEI Consortium, 2026).

The `<ptr>` element creates a unidirectional link from the location where it is placed to one or more target resources declared in its `@target` attribute. The `@target` attribute uses Uniform Resource Identifiers (URIs). Within the same document, an internal link is expressed using a fragment identifier (`#id`):

```xml
<!-- In the standOff container -->
<note xml:id="note-01" type="philological" resp="#kmp">
  <ptr target="#w5 #w6"/>
  The phrase <mentioned>ὁ λόγος</mentioned> reflects Hellenistic Jewish
  adaptations of the Sapiential literature (cf. Prov 8:22), functioning here
  as the divine mediating principle.
</note>
```

When connecting multiple disjoint elements or establishing complex multi-party associations, the `<link>` element is preferred. The `<link>` element resides inside a `<linkGrp>` (link group) in the `<standOff>` section and lists all participating nodes in its `@targets` attribute:

```xml
<standOff>
  <linkGrp type="intertextual-alignment" resp="#kmp">
    <!-- Links text span w1-w5 to Septuagint Genesis 1:1 and to a commentary note -->
    <link targets="#seg-john1-1 #lxx-gen1-1 #note-intertext-gen"/>
  </linkGrp>
</standOff>
```

| Pointing Syntax | Example | Scope | Resolution Mechanism |
| --- | --- | --- | --- |
| Same-Document ID | `target="#w12"` | Within current XML file | Resolves to element with matching `xml:id` |
| Cross-Document File | `target="edition_b.xml#w12"` | Local repository file | Relative file path + XML ID |
| Canonical CTS URN | `target="urn:cts:greekLit:tlg0012.tlg001:1.1"` | Global corpus | Resolved via CTS resolver service |
| Web URL / LOD URI | `target="https://pleiades.stoa.org/places/501482"` | Global semantic web | Standard HTTP GET resolution |

By utilizing standard URI pointing mechanisms, TEI pointers seamlessly bridge local document structures with global linked open data architectures (Simon et al., 2017).

**Vocabulary.** *Fragment identifier* — the portion of a URI following a `#` symbol that specifies a distinct anchor within a document. *Unidirectional link* — a link that points in one direction from source to target. *Link group (`<linkGrp>`)* — a TEI container for organizing related `<link>` elements.

**Takeaway:** `<ptr>` and `<link>` elements use URI and fragment identifier syntax to create unambiguous connections between stand-off notes, text spans, and external resources.

---

## **16 Content**

**Discrete In-Text Spanning with `<seg>` and `<spanGrp>`**

While pointing to individual word IDs (`#w1`) is effective for single-word glosses, scholarly commentary frequently targets multi-word phrases, clauses, or complex syntactic units that do not correspond to existing structural tags like `<p>` or `<l>`. To mark these targets without corrupting document grammar, TEI provides the generic `<seg>` (segment) and stand-off `<span>` elements (TEI Consortium, 2026).

The `<seg>` element can be wrapped directly around arbitrary text sequences in the body:

```xml
<p>
  <seg xml:id="seg-cl1">Ἐν ἀρχῇ ἦν ὁ λόγος</seg>, 
  καὶ <seg xml:id="seg-cl2">ὁ λόγος ἦν πρὸς τὸν θεόν</seg>...
</p>
```

However, if wrapping a `<seg>` element disrupts an existing hierarchy (for instance, if the target span crosses from the end of one sentence into the beginning of another, or crosses a poetic line break), the stand-off `<span>` element within a `<spanGrp>` provides a completely non-invasive alternative (TEI Consortium, 2026):

```xml
<standOff>
  <spanGrp type="rhetorical-unit" resp="#kmp">
    <!-- Span defined by explicit start (@from) and end (@to) targets -->
    <span xml:id="span-proem" from="#w1" to="#w15">
      The opening syntactic period establishes the timeless ontological status
      of the subject prior to creation.
    </span>
  </spanGrp>
</standOff>
```

In this stand-off architecture:

- `@from` specifies the `xml:id` of the first token in the span.
- `@to` specifies the `xml:id` of the final token in the span.
- The base text remains completely unmodified, containing no inline boundary tags.

This approach resolves the overlapping hierarchies problem completely: any number of overlapping or nested `<span>` elements can target intersecting ranges across the text without conflicting with one another or breaking XML validation (Schmidt, 2010).

**Vocabulary.** `<seg>` — a TEI element used to segment arbitrary text spans in the body for analytic or linguistic purposes. `<span>` — a stand-off element defining a text range via start and end boundary attributes. *Non-invasive markup* — annotation techniques that record textual properties without altering the base transcription stream.

**Takeaway:** Stand-off `<span>` elements define multi-word commentary targets via `@from` and `@to` boundaries, enabling overlapping spans without inserting intrusive inline tags.

---

## **17 Content**

**Traditional Inline `<note>` vs Stand-Off Notes**

In TEI encoding, an editor must choose between two distinct methods for storing commentary notes: **inline notes** and **stand-off notes**. Both are fully conformant with the TEI P5 Guidelines, but they represent very different architectural philosophies.

An **inline note** embeds the `<note>` element directly within the prose stream at the exact point of occurrence:

```xml
<!-- INLINE ENCODING -->
<p>
  Ἐν ἀρχῇ ἦν ὁ λόγος
  <note type="philological" resp="#kmp">
    The term <mentioned>λόγος</mentioned> carries both Hellenistic philosophical
    and Jewish sapiential resonances.
  </note>
  καὶ ὁ λόγος ἦν πρὸς τὸν θεόν...
</p>
```

A **stand-off note** stores the `<note>` in the `<standOff>` section, connecting to the text via a pointer:

```xml
<!-- STAND-OFF ENCODING -->
<standOff>
  <note xml:id="n-logos-phil" type="philological" target="#w5" resp="#kmp">
    The term <mentioned>λόγος</mentioned> carries both Hellenistic philosophical
    and Jewish sapiential resonances.
  </note>
</standOff>
```

| Architectural Criterion | Inline `<note>` Model | Stand-Off `<note>` Model |
| --- | --- | --- |
| Visual Legibility of Base Text | Poor; prose is fragmented by long notes | Excellent; base text stream is clean |
| Overlapping Spans | Impossible without milestone hacks | Native; arbitrary spans supported |
| Multi-Editorial Collaboration | Fragile; merge conflicts in base file | Robust; notes can live in separate modular files |
| Processing Complexity | Low; notes are parsed in document order | Moderate; requires pointer resolution |
| Conversion to Linked Open Data (RDF) | Cumbersome | Direct mapping to W3C Web Annotation graphs |

For small, single-editor projects with brief glosses, inline notes offer simplicity. However, for large-scale scholarly editions, multi-institutional collaborations, and rich multi-layered commentaries, stand-off notes are universally preferred (Schmidt, 2010; Tafdrup et al., 2026).

**Vocabulary.** *Inline encoding* — placing markup and annotations directly inside the primary text stream. *Merge conflict* — a version control collision occurring when multiple contributors edit the same lines of a file concurrently. *Modularity* — the degree to which a system's components can be separated and recombined.

**Takeaway:** Stand-off notes are superior to inline notes for scholarly commentary because they preserve transcription clarity, prevent merge conflicts, and support multi-layered annotations.

---

## **18 Content**

**Typing Commentary Notes in TEI**

To ensure that commentary notes can be filtered, styled, and searched systematically, the TEI `<note>` element must be enriched with standardized metadata attributes. An untyped `<note>` tag represents a missed opportunity for computational analysis (TEI Consortium, 2026).

The five essential attributes for structuring scholarly notes in TEI are:

```xml
<note xml:id="n-actium-hist"
      type="historical"
      subtype="battle"
      resp="#kmp"
      cert="high"
      source="#cambridge-ancient-history">
  <ptr target="#w42"/>
  The naval engagement at Actium (31 BCE) consolidated Octavian's sole dominance
  over the Roman world, terminating the civil wars of the late Republic.
</note>
```

- `@xml:id` — A unique document-level identifier allowing the note to be targeted by pointers, cross-references, and external RDF graphs.
- `@type` — The primary category of commentary, conforming to our four-part taxonomy (`philological`, `historical`, `intertextual`, `structural`).
- `@subtype` — A granular domain-specific sub-classification (e.g., `morphology`, `syntax`, `lexicon`, `geography`, `prosopography`, `allusion`, `rhetoric`).
- `@resp` — An explicit reference to the editor or agent responsible for authoring the note (pointing to an `xml:id` in the `<teiHeader>` `<respStmt>`).
- `@cert` — The degree of editorial certainty regarding the interpretive assertion (`high`, `medium`, `low`, `unknown`).
- `@source` — A bibliographic pointer to the reference work, grammar, or primary edition supporting the assertion.

By consistently applying these attributes, the digital edition enables dynamic user interfaces where readers can toggle specific commentary layers—such as viewing only philological notes for language learning, or viewing only historical notes for contextual study (Francese, 2014).

**Vocabulary.** `@subtype` — a TEI attribute providing a secondary, finer classification within a primary `@type`. `@cert` — a TEI attribute declaring the degree of editorial certainty for an assertion. *Dynamic filtering* — the capability of a digital interface to show or hide content based on user-selected metadata criteria.

**Takeaway:** Enriching `<note>` elements with `@type`, `@subtype`, `@resp`, `@cert`, and `@source` enables multi-dimensional filtering and transparent scholarly accountability.

---

## **19 Content**

**Structuring Complex Note Bodies**

A scholarly commentary note is rarely a flat string of prose. It often contains internal structural complexity, including quoted historical texts, foreign language terms, bibliographic citations, and cross-references to other notes within the edition (TEI Consortium, 2026).

TEI provides rich inline elements to structure the internal body of a `<note>`:

```xml
<note xml:id="n-pauline-grace" type="philological" subtype="semantics" resp="#kmp">
  <ptr target="#w18"/>
  <p>
    The noun <mentioned xml:lang="grc">χάρις</mentioned> operates here within
    the semantic field of Hellenistic benefaction systems rather than abstract
    post-Reformation theological categories (see <bibl><author>Jouette Bassler</author>,
    <title>Divine Impartiality</title>, <biblScope unit="page">12–18</biblScope></bibl>).
  </p>
  <p>
    For the sociolinguistic background of asymmetric reciprocity in Greco-Roman
    patronage, compare <ref target="#n-patronage-hist">Note 14.2</ref> and the
    parallel usage in <cit><bibl>IG II² 1006.15</bibl><quote xml:lang="grc">εὐνοίας
    ἕνεκα καὶ χάριτος</quote></cit>.
  </p>
</note>
```

Key inline structuring elements include:

- `<mentioned>` — Marks linguistic forms, words, or letters cited as the object of discussion rather than used in narrative prose.
- `<quote>` and `<cit>` — Encapsulates quoted source material paired with its bibliographic citation (`<bibl>`).
- `<bibl>` and `<biblScope>` — Formats structured secondary literature references with author, title, volume, and page boundaries.
- `<ref>` — Creates active cross-references to other notes, chapters, or appendices in the digital edition.
- `<gloss>` — Supplies a concise translation or semantic gloss for a foreign-language term.

Structuring note bodies with these elements ensures that bibliographic citations can be extracted into automated reading lists, linguistic terms can be indexed in glossaries, and cross-reference links remain functional across web builds (Francese, 2014).

**Vocabulary.** `<mentioned>` — a TEI element used to mark words or phrases mentioned as linguistic objects rather than used in communication. `<cit>` — a TEI container element combining a quotation with a bibliographic reference. *Semantic field* — the organization of related words and concepts within a language.

**Takeaway:** Structuring note bodies with `<mentioned>`, `<cit>`, `<bibl>`, and `<ref>` allows digital publishing systems to automatically build bibliographies, indexes, and internal link networks.

---

## **20 Content**

**Connecting to External Authority Files**

A major goal of digital scholarship is to break out of institutional silos by connecting local textual observations to the global **Linked Open Data (LOD)** cloud (Simon et al., 2017). When an editor writes a historical or geographic note, they should not stop at prose description; they should link the entity to global authority files.

In TEI stand-off commentary, external authorities are integrated using the `ref` attribute or `<ref>` elements pointing to persistent Linked Open Data Uniform Resource Identifiers (URIs):

```xml
<standOff>
  <!-- Prosopographical Register linking local IDs to global LOD URIs -->
  <listPerson>
    <person xml:id="pers-cleopatra">
      <persName xml:lang="grc">Κλεοπάτρα</persName>
      <persName xml:lang="en">Cleopatra VII Philopator</persName>
      <idno type="URI">https://viaf.org/viaf/67256875</idno>
      <idno type="URI">https://www.wikidata.org/wiki/Q635</idno>
    </person>
  </listPerson>

  <!-- Geographic Register linking ancient toponyms to Pleiades -->
  <listPlace>
    <place xml:id="place-alexandria">
      <placeName xml:lang="grc">Ἀλεξάνδρεια</placeName>
      <placeName xml:lang="en">Alexandria, Egypt</placeName>
      <idno type="URI">https://pleiades.stoa.org/places/727070</idno>
      <location>
        <geo>31.2001 29.9187</geo>
      </location>
    </place>
  </listPlace>
</standOff>
```

| Entity Domain | Primary Authority Registry | Description & Strengths |
| --- | --- | --- |
| Historical Places | **Pleiades Gazetteer** | The definitive spatial registry for ancient Mediterranean geography; provides coordinates, historical names, and bibliographies. |
| Global Entities | **Wikidata** | Structured multilingual knowledge base; ideal for wide-ranging historical concepts, events, and objects. |
| Authors & Persons | **VIAF (Virtual International Authority File)** | Merges national library authority records into globally unique identifiers for historical and modern authors. |
| Classical Works | **Perseus / CTS Catalogues** | Standardized URN catalogues for classical Greek and Latin literature. |

By incorporating `<listPerson>` and `<listPlace>` registers into the `<standOff>` container, local notes can simply reference `#pers-cleopatra` or `#place-alexandria`. Downstream rendering engines can then automatically pull coordinates for interactive mapping, fetch external biographies, and connect the edition to other projects across the web (Simon et al., 2017).

**Vocabulary.** *Authority file* — a standardized record that establishes the recognized heading and unique identifier for an entity. *VIAF* — Virtual International Authority File; a collaborative service aggregating national library authority files. *Toponym* — the proper name of a geographical place.

**Takeaway:** Encoding Linked Open Data URIs in `<listPerson>` and `<listPlace>` registers connects local commentary notes to global mapping and prosopographical databases.

---

## **21 Content**

**Case Study: Dickinson College Commentaries (DCC)**

The **Dickinson College Commentaries (DCC)** project, directed by Christopher Francese, provides a premier real-world model for designing digital scholarly commentaries tailored for pedagogy and scholarship (Francese, 2014).

The DCC project addresses a fundamental pedagogical dilemma in classical studies: traditional printed commentaries are often burdened with arcane 19th-century text-critical debates that overwhelm intermediate readers, while simplified student editions omit crucial cultural and linguistic nuance. DCC resolves this by developing an innovative, multi-layered digital architecture:

| DCC Pedagogical Tier | Implementation Mechanism | Learning Outcome |
| --- | --- | --- |
| Tier 1: Core Vocabulary Scaffolding | Algorithmically isolates words outside top 1,000 core lemmas | Provides running glosses without manual glossing fatigue |
| Tier 2: Grammatical & Philological Notes | Direct links to digital Allen & Greenough / Smyth sections | Teaches syntax through active reference consultation |
| Tier 3: Linked Realia & Spatial Media | Embeds Pleiades-aligned historical maps and images | Visualizes ancient topography and material culture |

A cornerstone of the DCC methodology is its algorithmic vocabulary filtering (Francese, 2014). By cross-referencing Latin and Greek texts against frequency data from the *Thesaurus Linguae Graecae* (TLG) and the *Laboratoire d'Analyse Statistique des Langues Anciennes* (LASLA), DCC isolates the core vocabulary (lemmas accounting for 70–80% of running words in classical literature). The human editors then focus their manual commentary on non-core vocabulary and complex syntax, saving hundreds of hours of repetitive glossing.

Furthermore, DCC links every grammatical explanation directly to sections of standard digital reference grammars (such as Allen & Greenough for Latin or Smyth for Greek), transforming the commentary into an active learning environment (Francese, 2014).

**Vocabulary.** *Vocabulary scaffolding* — providing targeted lexical support based on empirical frequency metrics to assist reading comprehension. *LASLA* — Laboratoire d'Analyse Statistique des Langues Anciennes; a research institute providing lemmatized Latin linguistic corpora.

**Takeaway:** Dickinson College Commentaries demonstrates how algorithmic vocabulary filtering and linked grammatical references create powerful, multi-tiered digital commentary editions.

---

## **22 Content**

**Case Study: Scholarly Commentary in *Grundtvig's Works***

The Danish digital edition of *Grundtvig's Works* (*Grundtvigs Værker*, GV) represents one of the largest and most ambitious digital scholarly editing projects in modern European humanities (Tafdrup et al., 2026). N.F.S. Grundtvig (1783–1872) was a towering Danish theologian, poet, and philosopher whose massive written corpus spans over 1,000 published works and extensive manuscripts.

The primary editorial mission of the GV project is historical mediation. Grundtvig’s 19th-century Danish is heavily archaizing, steeped in Scandinavian mythology, and saturated with obscure biblical allusions. Over more than a decade, the editorial team manually produced an astonishing volume of scholarly commentary:

| Annotation Metric in GV Edition | Total Count Produced | Editorial Labor Requirement |
| --- | --- | --- |
| Explanatory Commentary Notes | 158,000+ notes | Deep manual historical, theological, and lexical research |
| Named Entity Annotations | 166,430+ entities | Disambiguating historical, mythological, and geographic entities |
| Biblical & Intertextual Citations | 10,980+ citations | Tracing unacknowledged Lutheran scriptural and hymn paraphrases |

As Tafdrup et al. (2026) document, every single note in the GV edition represents an intensive act of manual scholarship. Editors had to trace obscure biblical paraphrases where Grundtvig reworded Danish Lutheran liturgical texts without quotation marks, cross-reference 19th-century Scandinavian political debates, and formulate standardized explanations in TEI-compliant XML.

The GV case study underscores the irreplaceable value of human editorial expertise: manual note drafting captures subtle theological subversions, ironic parodies, and local historical resonances that no automated system can detect from scratch. However, the GV team also recognized that the sheer scale of the corpus created massive labor bottlenecks, prompting them to explore how deterministic algorithms and generative AI could assist in identifying prospective candidates for human verification (Tafdrup et al., 2026).

**Vocabulary.** *Historical mediation* — the editorial practice of explaining historical, theological, and linguistic distance for modern readers. *Archaism* — the deliberate use of outdated or ancient language forms and styles. *Liturgical paraphrase* — rewording liturgical or biblical texts into poetry or prose.

**Takeaway:** The *Grundtvig's Works* edition demonstrates the irreplaceable depth of manual scholarly commentary alongside the labor limits that motivate computational assistance.

---

## **23 Content**

**Hands-On Exercise: Establishing the Ground-Truth Passage**

Today’s manual exercise establishes the reference dataset for Topic 12. You will select a complex, multi-dimensional passage from your course witness corpus (or a shared classical/biblical test passage, such as 1 Thessalonians 2:1–12 or a section of the *Acts of the Apostles*), transcribe the base text, assign persistent token identifiers, and author a comprehensive set of commentary notes by hand.

Follow this systematic step-by-step workflow:

| Step | Operation | Technical Requirement | Output Artifact |
| --- | --- | --- | --- |
| 1 | Select Text Segment | Choose a 10–15 verse/line passage with rich historical and linguistic features | Base text transcription |
| 2 | Assign Token IDs | Tokenize the passage and wrap words in `<w xml:id="...">` elements | Machine-addressable base XML |
| 3 | Create Stand-Off Shell | Build the `<standOff>` container with empty `<interpGrp>` elements | Stand-off architecture |
| 4 | Draft Philological Notes | Author 3–4 notes on difficult morphology, syntax, and rare vocabulary | Philological note corpus |
| 5 | Draft Historical Notes | Author 3–4 notes on persons, places, and cultural realia with LOD URIs | Historical note corpus |
| 6 | Draft Intertextual Notes | Author 2–3 notes identifying allusions and citations with precise sources | Intertextual note corpus |
| 7 | Draft Structural Notes | Author 1–2 notes analyzing discourse structure and rhetorical figures | Structural note corpus |
| 8 | Validate & Link | Connect notes to text IDs via `<ptr>` and validate against TEI schemas | Clean, validated TEI file |

Begin by creating your base XML document. Ensure that every word token receives a deterministic `xml:id` following a consistent naming scheme: `w-1`, `w-2`, `w-3`, or `w-12-1-1` (specifying Topic, Chapter, and Word index). These IDs will serve as the anchors for all subsequent manual, deterministic, and AI-assisted annotations.

**Vocabulary.** *Ground truth* — the verified, authoritative reference dataset against which automated and experimental models are tested. *Tokenization* — the process of segmenting a continuous text stream into discrete words and punctuation marks. *Deterministic identifier* — an ID generated by a predictable rule that remains consistent across processing runs.

**Takeaway:** Establishing a stable ground-truth passage with explicit token IDs is the foundational prerequisite for all digital commentary encoding.

---

## **24 Content**

**Hands-On Exercise: Drafting Philological Notes by Hand**

With your base text tokenized and assigned `xml:id` attributes, author your philological commentary notes. Focus on explaining linguistic features that require grammatical expertise and lexicon consultation.

When drafting each note by hand, structure your content into three explicit components:

1. **Target Identification:** The exact lemma, word form, and token ID (`#w-X`).
2. **Morphosyntactic Classification:** Parsing details (case, number, gender, tense, voice, mood) and syntactical category (e.g., *genitive of source*, *dative of disadvantage*, *historical present*).
3. **Hermeneutic Explanation:** Why this specific grammatical form matters for the meaning of the passage, citing authoritative lexica (LSJ, BDAG) or standard grammars.

| Philological Note Field | Editorial Analysis for 1 Thess 2:2 |
| --- | --- |
| Target Identifier | `#w14` (ἐπαρρησιασάμεθα) |
| Morphological Parsing | Verb, 1st person plural, aorist middle deponent indicative of παρρησιάζομαι |
| Reference Citations | BDAG 781b; Smyth §1890 |
| Semantic Nuance | In classical Athenian democracy, παρρησία denoted the citizen's civic right of free speech; in early Christian literature it denotes courageous proclamation in the face of civic opposition. |

Draft at least three distinct philological notes for your selected passage. Ensure that your notes address genuine linguistic complexities rather than trivial definitions.

**Vocabulary.** *Deponent verb* — a verb with passive or middle morphological forms but an active semantic meaning. *Parrhesia* — in ancient Greece, the practice and civic right of speaking candidly and boldly. *Semantic shift* — the evolution of word meanings over historical time.

**Takeaway:** Philological drafting requires precise morphological parsing, standard lexical citations, and contextual explanations of semantic nuance.

---

## **25 Content**

**Hands-On Exercise: Drafting Historical and Intertextual Notes by Hand**

Next, author the historical, prosopographical, and intertextual commentary notes for your test passage. These notes require consulting historical gazetteers, classical reference works, and biblical cross-reference tools.

For **historical notes**, identify every proper noun, political title, and cultural custom. Record:

- The historical identity of the entity.
- The precise relevance of this background to the argument of the text.
- The persistent Linked Open Data URI (Pleiades for places, VIAF/Wikidata for persons).

For **intertextual notes**, identify citations, allusions, and structural echoes. Record:

- The target passage and the source passage.
- The nature of the intertextual link (explicit quotation, verbal allusion, structural parallel).
- The exact shared lemmas or conceptual motifs.

| Annotation Layer | Target Tokens | Primary Source / Authority URI | Hermeneutic Rationale |
| --- | --- | --- | --- |
| Historical Note | `#w8` (Φιλίπποις) | `https://pleiades.stoa.org/places/501482` | Roman colony status; mistreatment of Roman citizens violated Lex Julia |
| Intertextual Note | `#w22-#w25` (τὸ εὐαγγέλιον τοῦ θεοῦ) | LXX Isaiah 52:7 / Priene Inscription | Echoes Isaianic herald while subverting the Roman imperial cult's *euangelia* |

Author at least three historical/LOD notes and two intertextual notes for your passage.

**Vocabulary.** *Lex Julia* — ancient Roman legislation safeguarding citizens against arbitrary physical abuse without trial. *Imperial cult* — the official religious veneration of Roman emperors as divine benefactors across the empire. *Priene Inscription* — famous 9 BCE Greek inscription from Asia Minor using *euangelia* for Caesar Augustus.

**Takeaway:** Historical notes anchor entities to LOD URIs, while intertextual notes articulate the literary and ideological dimensions of textual echoes.

---

## **26 Content**

**Hands-On Exercise: Constructing the Stand-Off TEI Header and Architecture**

Now, translate your manual drafting sheets into a fully compliant TEI XML document utilizing `<standOff>` architecture. Open your editor and construct the document skeleton.

In the `<teiHeader>`, declare the metadata for your commentary edition, including the `<respStmt>` defining your editorial identity (which will be referenced by `@resp` attributes in your notes):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
    <fileDesc>
      <titleStmt>
        <title>Scholarly Digital Commentary: 1 Thessalonians 2:1–8</title>
        <author>Ken M. Penner</author>
        <respStmt>
          <resp>Commentary author and encoder</resp>
          <name xml:id="kmp">Ken M. Penner</name>
        </respStmt>
      </titleStmt>
      <publicationStmt>
        <publisher>RELS 398 Digital Humanities Laboratory</publisher>
        <date>2026</date>
        <availability><licence target="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</licence></availability>
      </publicationStmt>
      <sourceDesc>
        <p>Transcribed from Codex Sinaiticus (London, BL Add. MS 43725).</p>
      </sourceDesc>
    </fileDesc>
  </teiHeader>
  
  <text>
    <body>
      <div type="chapter" n="2">
        <p>
          <w xml:id="w1">Αὐτοὶ</w> <w xml:id="w2">γὰρ</w> <w xml:id="w3">οἴδατε</w>,
          <w xml:id="w4">ἀδελφοί</w>, <w xml:id="w5">τὴν</w> <w xml:id="w6">εἴσοδον</w>
          <w xml:id="w7">ἡμῶν</w> <w xml:id="w8">τὴν</w> <w xml:id="w9">πρὸς</w>
          <w xml:id="w10">ὑμᾶς</w>...
        </p>
      </div>
    </body>
  </text>
  
  <standOff>
    <!-- We will populate interpretation groups and notes here -->
  </standOff>
</TEI>
```

Ensure that your schema declaration points to the official TEI P5 RelaxNG schema (`tei_all.rng`). This allows your XML editor to validate your stand-off elements in real time.

**Vocabulary.** `tei_all.rng` — the complete, unrestricted RelaxNG schema containing all TEI P5 modules and elements. `<publicationStmt>` — TEI header element detailing the publication and licensing of the electronic document. `<sourceDesc>` — TEI header element recording the physical manuscript or printed edition source.

**Takeaway:** Building the TEI document shell establishes formal editorial metadata, licensing, and schema validation for the stand-off commentary.

---

## **27 Content**

**Hands-On Exercise: Linking Pointers and Validating TEI Markup**

Now populate the `<standOff>` section with your drafted notes, utilizing structured `<interpGrp>`, `<listPlace>`, `<listPerson>`, and `<note>` elements with active pointer connections.

Follow this complete stand-off encoding pattern:

```xml
<standOff>
  <!-- 1. Controlled Interpretive Vocabulary -->
  <interpGrp type="commentary-taxonomy" resp="#kmp">
    <interp xml:id="cat-phil">Philological and morphosyntactic analysis</interp>
    <interp xml:id="cat-hist">Historical, geographic, and prosopographical realia</interp>
    <interp xml:id="cat-intertext">Intertextual citation, allusion, and text reuse</interp>
    <interp xml:id="cat-struct">Structural, rhetorical, and exegetical analysis</interp>
  </interpGrp>

  <!-- 2. Geographic Register with Pleiades URI -->
  <listPlace>
    <place xml:id="pl-philippi">
      <placeName xml:lang="grc">Φίλιπποι</placeName>
      <placeName xml:lang="en">Philippi</placeName>
      <idno type="URI">https://pleiades.stoa.org/places/501482</idno>
    </place>
  </listPlace>

  <!-- 3. Structured Commentary Notes -->
  <note xml:id="note-12-1" type="philological" subtype="grammar" resp="#kmp" target="#w14">
    <p>The verb <mentioned xml:lang="grc">ἐπαρρησιασάμεθα</mentioned> denotes bold public speech...</p>
  </note>

  <note xml:id="note-12-2" type="historical" subtype="topography" resp="#kmp" target="#w8">
    <p>Reference to mistreatment at <ref target="#pl-philippi">Philippi</ref> evokes civic Roman status...</p>
  </note>

  <note xml:id="note-12-3" type="intertextual" subtype="echo" resp="#kmp" target="#w22 #w23 #w24 #w25">
    <p>The formula <mentioned xml:lang="grc">τὸ εὐαγγέλιον τοῦ θεοῦ</mentioned> echoes LXX Isa 52:7...</p>
  </note>
</standOff>
```

Once encoded, validate the document. Check that:

1. Every `@target` URI correctly resolves to an existing `xml:id` in the document.
2. All `<note>` elements contain mandatory `@type` and `@resp` attributes.
3. XML syntax is well-formed with no unclosed tags or unescaped ampersands.

**Vocabulary.** *Well-formedness* — the structural syntax rule in XML requiring all tags to be properly closed, quoted, and nested. *Schema validity* — the property of an XML document conforming to a formal grammar ruleset (such as TEI RelaxNG). `@target` resolution — verifying that a pointer URI matches an actual existing target identifier.

**Takeaway:** Populating `<standOff>` with typed `<note>`, `<interpGrp>`, and `<listPlace>` elements creates a valid, fully linked TEI commentary file.

---

## **28 Content**

**Designing the Editorial Statement for Commentary**

A digital scholarly edition is incomplete without an explicit **Editorial Statement** explaining the principles, boundaries, and scope of its commentary. Just as an editor must publish their normalization policy (Topic 6) and collation principles (Topic 14), they must define their commentary rationale in the `<editorialDecl>` of the `<teiHeader>` (TEI Consortium, 2026).

The commentary editorial statement must address four fundamental questions:

1. **Target Audience and Pedagogical Level:** Is the commentary intended for introductory students (requiring extensive vocabulary scaffolding and basic historical glosses), advanced researchers (focusing on complex text-critical and intertextual debates), or a hybrid audience (Francese, 2014)?
2. **Annotation Thresholds:** What criteria trigger a note? Are all proper nouns annotated, or only those whose significance is not obvious? What degree of lexical rarity triggers a grammatical note?
3. **Citation Standards:** What edition standards and authority gazetteers are privileged? How are biblical, classical, and epigraphic sources cited?
4. **Attribution and Methodology:** Who authored the notes? How are collaborative interventions, peer reviews, and computational tools credited?

```xml
<encodingDesc>
  <editorialDecl>
    <interpretation>
      <p>Commentary notes are classified according to a four-tier taxonomy: philological,
      historical, intertextual, and structural. Philological notes are provided for all words
      falling outside the core 1,000 Hellenistic Greek vocabulary list. Historical place names
      are linked to the Pleiades Gazetteer. Intertextual notes distinguish between explicit
      citations (marked via CiTO properties) and verbal allusions. All notes are authored in
      stand-off XML and licensed under CC BY 4.0.</p>
    </interpretation>
  </editorialDecl>
</encodingDesc>
```

Documenting these policies ensures that your commentary remains transparent, reproducible, and methodologically coherent.

**Vocabulary.** `<editorialDecl>` — TEI header element providing details of editorial practices applied during text encoding. `<interpretation>` — TEI sub-element describing the scope of interpretive and analytic annotations. *Annotation threshold* — the explicit editorial criteria determining when a textual feature warrants an explanatory note.

**Takeaway:** The commentary editorial statement formalizes selection criteria, target audience levels, citation standards, and attribution protocols.

---

## **29 Content**

**Preparing the Manual Reference Corpus for Algorithmic Auditing**

The manual commentary notes you have authored and encoded today are not merely a standalone assignment. They constitute the **ground-truth reference corpus** for the entire three-step cycle of Topic 12.

Tomorrow (Lesson 12.2), we will deploy deterministic intertextual discovery algorithms—specifically the Tesserae project’s n-gram and TF-IDF scoring engine—to automatically search for text reuse across our corpus (Coffee et al., 2012). On Friday (Lesson 12.3), we will prompt Large Language Models (LLMs) to draft philological, historical, and intertextual commentary notes across the exact same passage (Tafdrup et al., 2026).

To prepare your manual data for systematic comparison, compile an audit summary table recording the baseline metrics of your manual pass:

| Annotation Category | Total Notes Authored | Unique Text Tokens Targeted | External LOD URIs Linked | Primary Reference Works Consulted |
| --- | --- | --- | --- | --- |
| Philological | 3 | 4 | 0 | BDAG, Smyth, BDF |
| Historical / Geographic | 3 | 3 | 3 (Pleiades, VIAF) | OCD, Pleiades, Brill Pauly |
| Intertextual / Citational | 2 | 6 | 0 | NA28 Cross-refs, Rahlfs LXX |
| Structural / Rhetorical | 1 | 15 | 0 | Lausberg, Bullinger |
| **Total / Baseline** | **9 notes** | **28 tokens** | **3 authorities** | — |

Save this summary. Tomorrow and Friday, you will evaluate how many of these manual discoveries the automated tools replicate, how many they miss (false negatives), and how many spurious leads they generate (false positives).

**Vocabulary.** *Ground-truth corpus* — the verified human reference dataset used to benchmark automated algorithms. *False negative* — an authentic feature that an automated algorithm fails to detect. *False positive* — a spurious candidate generated by an algorithm that does not represent a true match.

**Takeaway:** Compiling a structured audit summary of today's manual notes establishes the quantitative baseline for auditing automated and AI tools later this week.

---

## **30 Content**

**Synthesis: The Human-in-the-Loop Foundation of Digital Commentary**

The core thesis of today’s lesson is that digital scholarly commentary is not a collection of isolated footnotes, but a structured, multi-dimensional knowledge network.

We have established that:

1. **Epistemology:** Commentary transforms historical transcriptions from inert text streams into active, dialogical knowledge sites, continuing a scholarly lineage stretching from Alexandrian grammarians to modern linked data networks (Blackwell & Smith, 2014; Tafdrup et al., 2026).
2. **Typological Discipline:** Effective digital commentary must be decomposed into explicit, standardized categories—philological, historical, intertextual, and structural—to prevent analytical drift and enable computational queries.
3. **Architectural Separation:** The overlapping hierarchies of historical texts and interpretive layers cannot be handled cleanly by embedded inline tags. TEI stand-off markup (`<standOff>`, `<interpGrp>`, `<note>`, `<ptr>`) solves the overlap problem by decoupling annotations from base transcriptions (Schmidt, 2010).
4. **Canonical Addressing:** Stable, persistent addressing through CTS URNs and Linked Open Data URIs ensures that digital commentary survives file refactoring, schema migrations, and web link rot (Blackwell & Smith, 2014; Simon et al., 2017).

Manual commentary drafting requires immense erudition, hermeneutic reflection, and rigorous philological discipline. It represents the gold standard of scholarly depth. However, its labor-intensive nature creates severe scalability bottlenecks for large cultural heritage corpora (Tafdrup et al., 2026).

**For Wednesday:** Install and review the Tesserae intertextual discovery documentation; examine how deterministic frequency-weighted algorithms detect text reuse across classical corpora.

**Takeaway:** Manual commentary provides the irreplaceable ground truth of scholarly depth, structured through TEI stand-off markup to anchor subsequent computational discovery.

---

## References

Bartalesi, V., Meghini, C., & Metilli, D. (2018). *A web application for exploring primary sources: The DanteSources case study*. Italian National Research Council (ISTI-CNR). https://openportal.isti.cnr.it/data/2018/384308/2018_384308.preprint.pdf

Blackwell, C. W., & Smith, N. (2014). *The Canonical Text Services URN specification, version 2.0.rc.1*. Center for Hellenic Studies, Harvard University. https://cite-architecture.github.io/ctsurn_spec/

Coffee, N., Koenig, J.-P., Poornima, S., Forstall, C. W., Ossewaarde, R., & Jacobson, S. L. (2012). The Tesserae Project: Intertextual analysis of Latin poetry. *Literary and Linguistic Computing, 28*(2), 221–228. https://doi.org/10.1093/llc/fqs033

Francese, C. (2014). *About DCC: Overview and pedagogical principles*. Dickinson College Commentaries. https://dcc.dickinson.edu/about-dcc

Klie, J.-C., Bugert, M., Boullosa, B., Eckart de Castilho, R., & Gurevych, I. (2018). The INCEpTION platform: Machine-assisted and knowledge-oriented interactive annotation. In *Proceedings of the 27th International Conference on Computational Linguistics: System Demonstrations* (pp. 5–9). Association for Computational Linguistics. https://aclanthology.org/C18-2002/

Sanderson, R., Ciccarese, P., & Young, B. (Eds.). (2017). *Web Annotation Data Model* (W3C Recommendation 23 February 2017). World Wide Web Consortium. https://www.w3.org/TR/annotation-model/

Schmidt, D. (2010). The inadequacy of embedded markup for cultural heritage texts. *Literary and Linguistic Computing, 25*(3), 337–356. https://doi.org/10.1093/llc/fqq007

Simon, R., Barker, E., Desoto, P., & Isaksen, L. (2017). *Linked data annotation without the pointy brackets: Introducing Recogito 2*. Pelagios Network. https://www.researchgate.net/publication/316865029_Linked_Data_Annotation_Without_the_Pointy_Brackets_Introducing_Recogito_2

Tafdrup, J., Bjerring-Hansen, J., & Hansen, J. N. (2026). Convergences. AI, editorial practice, and the Danish Digital Scholarly Edition of Grundtvig’s Works. *International Journal of Digital Humanities, 8*, 191–211. https://doi.org/10.1007/s42803-026-00125-z

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and interchange* (Version 4.8.1). https://www.tei-c.org/release/doc/tei-p5-doc/en/html/
