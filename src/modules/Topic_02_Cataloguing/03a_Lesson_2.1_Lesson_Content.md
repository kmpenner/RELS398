# Lesson 2.1 — Codicological Description and Hand-Authoring the TEI Header

*RELS 398 / ENGL 398 · Topic 2: Cataloguing · Meeting #3 (Tue Sep 8)*

***Step 1 of the three-step cycle: manual.** Today you hand-write a complete TEI Header and codicological manuscript description (<msDesc>) for your chosen witness in a plain text editor without schema validation or autocomplete. What you produce is the ground-truth metadata baseline against which Wednesday's deterministic schema validation and Friday's AI extraction will be measured.*

---

## **01 Content**

**From Discursive Catalogues to Formal Metadata Systems**

The historical study of manuscripts has long been mediated through localized, print-based descriptive catalogues. For centuries, monastic librarians, university archivists, and classical philologists recorded their observations of handwritten codices in extensive discursive essays. A traditional nineteenth-century catalogue entry—such as those composed by Bernard de Montfaucon, Angelo Maria Bandini, or Konstantin von Tischendorf—might describe a manuscript's binding in poetic Latin, note the presence of marginal glosses in an unpunctuated paragraph, and summarize the contents of several theological treatises in a single flowing narrative (Le Bœuf, 2012). While these narrative catalogues represent monuments of humanistic erudition and paleographical insight, they were designed exclusively for human close reading. They treat metadata not as structured, queryable data points, but as literary exposition.

In the computational era, this discursive legacy presents insurmountable barriers to scholarship. An unstructured print catalogue cannot be indexed by a relational database, queried via an application programming interface (API), or integrated into an automated text-processing pipeline. If one catalogue describes a manuscript's support as "parchment," another as "membranaceus," and a third as "vellum with heavy follicle patterns," a search engine cannot determine whether these repositories hold the same material medium. Knowledge remains locked in institutional silos, isolated by idiosyncratic cataloguing dialects, varied regional descriptive conventions, and unstandardized abbreviations (Le Bœuf, 2012).

The transition to digital manuscript studies requires replacing discursive narrative with formal, machine-actionable data architectures. This transition does not diminish the qualitative richness of codicological description; rather, it formalizes that description within unambiguous structural envelopes. By translating physical observations—ruling patterns, quire structures, scribal hands, and provenance histories—into standardized, machine-readable hierarchies, digital editors ensure that their codicological claims can be computed, compared, aggregated, and preserved across decentralized global networks.

Furthermore, this formalization changes how scholars interact with the historical record. When metadata is structured into discrete, typed fields, researchers can execute complex computational queries across thousands of manuscripts simultaneously. A scholar can instantly aggregate all sixth-century Greek witnesses produced in Egypt that feature hexaplaric signs and single-column layouts. What previously required months of manual archival collation becomes an instantaneous computational operation, provided the underlying metadata adheres to a rigorous, shared data model.

**Takeaway:** Discursive print catalogues isolate codicological knowledge in human-readable silos; digital philology requires formal, machine-actionable schemas to enable computational analysis and cross-institutional discovery.

---

## **02 Content**

**The Epistemology of Manuscript Modeling: FRBRoo and LRMoo**

To build a rigorous digital description of a manuscript, an editor must first clarify what kind of ontological entity a handwritten codex actually is. In the world of modern library cataloguing, standard metadata models like Dublin Core and MARC were designed around mass-produced printed books. Printed books are defined by shared, reproducible editions: ten thousand copies of a modern paperback share the same publisher, pagination, font, layout, and textual content. In bibliographic ontology, this conceptual layer is formalized by the Functional Requirements for Bibliographic Records (FRBR) through the WEMI hierarchy: Work, Expression, Manifestation, and Item (Le Bœuf, 2012).

In the FRBR model, a *Work* is the abstract intellectual creation (such as Homer's *Iliad* or the biblical Book of Isaiah); an *Expression* is a specific intellectual realization in language and signs (such as the Greek Septuagint translation); a *Manifestation* is the physical embodiment of an expression in a published edition; and an *Item* is a single concrete exemplar owned by a library. For mass-produced print books, thousands of identical *Items* embody a single *Manifestation*.

Premodern manuscripts break this bibliographic assumption entirely. Every handwritten codex is a singular historical artifact produced through manual labor under unique material conditions. There is no mass-produced edition. To capture this reality, cultural heritage ontologists developed FRBRoo (an object-oriented harmonization with the CIDOC Conceptual Reference Model) and its successor LRMoo (Le Bœuf, 2012). In FRBRoo, a printed book is modeled as an instance of `F3 Manifestation Product Type`, representing a class of identical copies. A handwritten codex, by contrast, is modeled as an `F4 Manifestation Singleton`: an artifact where the physical manifestation and the concrete physical item are inextricably bound together as a singular, unrepeatable historical event (Le Bœuf, 2012).

| Ontological Level | Mass-Produced Print Concept | Manuscript Singleton Concept | Concrete Manuscript Example |
| --- | --- | --- | --- |
| Work | Abstract intellectual creation | Abstract intellectual creation | Book of Isaiah |
| Expression | Intellectual realization in language | Specific translation / redaction | Greek Septuagint Translation |
| Manifestation | `F3 Manifestation Product Type` (Print Run) | `F4 Manifestation Singleton` (Unique Codex) | Codex Marchalianus (Vat. gr. 2125) |
| Item | Single circulating copy on a shelf | Concrete physical artifact in archive | Vatican Library physical vault volume |

Because every manuscript is an `F4 Manifestation Singleton`, cataloguing a manuscript requires documenting not only the abstract texts it carries, but the physical biography of the unique physical container itself. The digital record must capture the unique parchment preparation, unique scribal hands, historical marginal glosses, quire repairs, and distinct provenance transfers that belong exclusively to that specific volume (Le Bœuf, 2012).

**Takeaway:** Modern print catalogues model mass-produced publication types, but premodern manuscripts are manifestation singletons whose unique physical embodiment cannot be separated from their textual witness.

---

## **03 Content**

**Why We Hand-Write XML Markup Before Running a Validator**

This morning begins the three-step comparative cycle for Topic 02. Before you open Oxygen XML Editor, before you load a RELAX NG schema, and before you run an automated parsing script, you will write a complete TEI Header and manuscript description by hand in a bare text editor. This exercise is not a historical reenactment or an exercise in arbitrary difficulty; it is an essential epistemological discipline.

Automated tools, schema-aware editors, and artificial intelligence models make structural decisions for you. When an interactive development environment (IDE) auto-closes your XML tags or provides a drop-down menu of permitted child elements, it conceals the underlying tree structure of the data model. When an AI model generates an XML block from a plain-text prompt, it predicts probable sequences of tokens without understanding the codicological realities those tokens represent. By writing every angle bracket, every element name, and every attribute value manually, you force yourself to make every architectural decision explicitly.

Hand-authoring slows down your analytical gaze and cultivates close codicological attention. As you inspect high-resolution digital facsimiles of your manuscript, you must decide whether an ink note in the upper margin is a chapter title (`<rubric>`), a liturgical instruction (`<head>`), an added variant (`<add>`), or an owner's acquisition mark (`<provenance>`). You must decide how to represent a missing quire or an ambiguous foliation sequence without relying on software defaults. The manual header you produce today will serve as your absolute *ground truth*—the gold standard against which tomorrow's deterministic schema validation and Friday's probabilistic AI extractions will be tested and scored.

Furthermore, hand-authoring establishes intellectual ownership over the digital edition. When you manually structure metadata, you experience firsthand the tensions between physical ambiguity and digital taxonomy. Scribes did not create manuscripts to fit into modern XML schemas; they wrote across margins, erased lines, added loose slips, and changed layouts mid-quire. Confronting these anomalies by hand ensures that you understand the editorial cost of computational modeling before you delegate tasks to automated algorithms.

**Takeaway:** Writing XML markup by hand forces conscious decision-making for every codicological feature, establishing the authoritative human ground truth required to evaluate automated tools.

---

## **04 Content**

**XML Fundamentals: The Syntax of Tree Structures**

The Text Encoding Initiative (TEI) is an application of XML (Extensible Markup Language). XML is not a programming language; it is a formal metalanguage for declaring structural hierarchies in plain text. Every XML document represents a mathematical tree consisting of nodes, branches, and leaves. Before encoding complex manuscript metadata, you must master the rigid rules of XML well-formedness.

A document is *well-formed* if and only if it satisfies the fundamental syntactic grammar of XML. If a document violates even a single well-formedness rule, XML parsers are required by specification to halt immediately and raise a fatal error. Unlike web browsers, which forgivingly guess the layout of broken HTML, XML processors practice zero tolerance for syntax defects. This uncompromising strictness is intentional: it ensures that data structures are unambiguous and machine-parsable across all computing environments.

The core rules of well-formed XML are absolute:

- **Single Root Element:** Every XML document must contain exactly one root element that encloses all other content. No tags may exist outside this primary container (except for processing instructions and XML declarations).
- **Matching Closing Tags:** Every opening tag (e.g., `<title>`) must have a corresponding, explicitly spelled closing tag (e.g., `</title>`), or be written as a self-closing element (e.g., `<pb/>` for page beginnings).
- **Strict Nesting:** Elements must nest cleanly inside one another without overlapping. The sequence `<a><b></a></b>` is illegal; it must be written `<a><b></b></a>`.
- **Case Sensitivity:** XML is strictly case-sensitive. The tag `<titleStmt>` is completely distinct from `<titlestmt>` or `<TitleStmt>`. An opening `<teiHeader>` cannot be closed with `</TeiHeader>`.
- **Quoted Attribute Values:** All attribute values must be enclosed in single or double quotation marks (e.g., `@type="parchment"`, never `@type=parchment`).

| XML Syntactic Rule | Invalid Example | Valid Well-Formed Equivalent | Structural Rationale |
| --- | --- | --- | --- |
| Root containment | `<header></header><text></text>` | `<TEI><header></header><text></text></TEI>` | XML trees must have a single root vertex |
| Tag closing | `<p>This is a paragraph.` | `<p>This is a paragraph.</p>` | Every opened branch must be explicitly terminated |
| Clean nesting | `<persName><orgName></persName></orgName>` | `<persName><orgName></orgName></persName>` | Hierarchy prohibits overlapping branch intersections |
| Case matching | `<msDesc></msdesc>` | `<msDesc></msDesc>` | XML parsers evaluate Unicode code points strictly |
| Attribute quotes | `<dim type=leaf>` | `<dim type="leaf">` | Attribute values must be delimited string literals |

Understanding these syntactic foundations is essential because even a trivial typo—such as a missing slash in a closing tag or an unquoted attribute—will cause downstream validation tools and rendering scripts to fail completely.

**Takeaway:** XML enforces strict syntactic well-formedness—single root, perfect nesting, exact case matching, and quoted attributes—with zero tolerance for parsing defects.

---

## **05 Content**

**Elements, Attributes, and the Hierarchy of Containment**

In XML, information is structured using two primary mechanisms: elements and attributes. Knowing when to store data as element text content versus attribute values is one of the foundational design skills in digital text encoding.

*Elements* represent semantic units and structural containers. They can hold plain text, child elements, or a mixture of both. Elements express hierarchy and sequence: an `<msContents>` element contains one or more `<msItem>` child elements, which in turn contain `<title>` and `<incipit>` elements. When information possesses its own internal structure, requires sequential ordering, or represents primary narrative content, it must be encoded as an element.

*Attributes* provide metadata about elements. They sit inside the opening tag and take the form of name-value pairs (e.g., `<supportDesc material="parchment">`). Attributes cannot contain child elements; they hold flat, unparsed text strings or controlled identifiers. Attributes are appropriate for categorizing an element (`@type="uncial"`), assigning machine-readable dates (`@when="0550"`), specifying measurement units (`@unit="mm"`), or linking to external authority registers (`@ref="https://viaf.org/viaf/88890041"`).

```xml
<!-- Example of element hierarchy combined with informative attributes -->
<supportDesc material="parchment">
  <support>
    <p>Fine calfskin vellum, carefully scraped and bleached, with minimal follicle visibility on flesh sides.</p>
  </support>
  <extent>
    <dimensions unit="mm" type="leaf">
      <height quantity="305"/>
      <width quantity="240"/>
    </dimensions>
    <dimensions unit="mm" type="written">
      <height quantity="220"/>
      <width quantity="155"/>
    </dimensions>
  </extent>
</supportDesc>
```

Finally, XML reserves five characters that cannot be written directly in text content because they conflict with syntax delimiters. You must escape these using predefined character entity references: `&lt;` for `<` (less than), `&gt;` for `>` (greater than), `&amp;` for `&` (ampersand), `&apos;` for `'` (apostrophe), and `&quot;` for `"` (quotation mark). Writing a bare ampersand (such as `Clemens & Graham`) causes an immediate fatal parser crash.

**Takeaway:** Elements define hierarchical containers and primary content, while attributes supply qualifying metadata, categorical types, machine-readable values, and external links.

---

## **06 Content**

**The Anatomy of the TEI Document Envelope**

The Text Encoding Initiative (TEI) Guidelines establish a standardized XML vocabulary for representing textual and codicological materials (TEI Consortium, 2025). Every standard TEI document begins with a root `<TEI>` element containing two mandatory top-level branches: the `<teiHeader>` and the `<text>` (or `<facsimile>`).

The `<teiHeader>` serves as the digital metadata envelope. It contains all the bibliographic, codicological, administrative, and structural documentation required to understand the digital file and the physical source from which it was made (TEI Consortium, 2025). The `<text>` element contains the actual transcription of the manuscript's textual content, structured into front matter (`<front>`), body text (`<body>`), and back matter (`<back>`).

| Structural Branch | XML Container | Primary Function in Edition | Codicological Scope |
| --- | --- | --- | --- |
| Root | `<TEI>` | Root envelope enclosing metadata and primary text | Entire digital file and document ecosystem |
| Metadata Header | `<teiHeader>` | Metadata envelope for bibliographic and codicological data | Archival, codicological, and project documentation |
| File Description | `<fileDesc>` | Bibliographic description of digital file and physical source | Mandatory core metadata container |
| Encoding Description | `<encodingDesc>` | Editorial principles, normalization rules, and markup taxonomy | Technical relationship between source and digital edition |
| Profile Description | `<profileDesc>` | Non-bibliographic classifications, languages, and contexts | Subject headings, languages, text creation contexts |
| Revision Description | `<revisionDesc>` | Change log recording modifications made to digital file | Editorial audit trail and commit history |
| Text Carrier | `<text>` | Transcribed primary source divided into front, body, and back | Primary diplomatic or critical transcription |

The strict separation between `<teiHeader>` and `<text>` is fundamental to digital editing. A transcription without a header is an anonymous orphan; a header without a transcription is a rich codicological catalogue record. Today's lesson focuses entirely on authoring the `<teiHeader>` and its manuscript description module, establishing the metadata scaffolding that will support all subsequent transcription and collation work in future weeks.

**Takeaway:** A TEI document cleanly separates descriptive metadata in the `<teiHeader>` from transcribed primary text in `<text>`, ensuring the digital edition remains fully documented and auditable.

---

## **07 Content**

**The Digital Edition as Artifact: `<fileDesc>` and `<titleStmt>`**

The first mandatory child of `<teiHeader>` is `<fileDesc>` (file description). The `<fileDesc>` contains the full bibliographic description of the digital file itself, ensuring that the electronic edition can be cited as an independent intellectual publication (TEI Consortium, 2025).

Within `<fileDesc>`, the first required element is `<titleStmt>` (title statement). The `<titleStmt>` records the title of the digital edition, the authors or principal investigators responsible for its creation, and any supporting sponsors or editors. It is crucial to understand that the title encoded in `<titleStmt>` is the title of *your digital project*, not the ancient title of the manuscript.

```xml
<fileDesc>
  <titleStmt>
    <title>Digital Scholarly Edition of Codex Marchalianus (Vat. gr. 2125): A Diplomatic Encoding of the Book of Isaiah</title>
    <author>Anonymous 6th-Century Scribes</author>
    <editor role="principal-investigator">Prof. K. M. Penner</editor>
    <editor role="encoder">Jane Doe</editor>
    <sponsor>St. Francis Xavier University Digital Humanities Initiative</sponsor>
    <funder>Social Sciences and Humanities Research Council of Canada</funder>
  </titleStmt>
  <!-- ... publicationStmt and sourceDesc follow ... -->
</fileDesc>
```

When formulating a digital title, clarity and precision are essential. The title should explicitly name the primary witness, its institutional shelfmark, the specific biblical or literary text encoded, and the editorial approach (e.g., diplomatic transcription, critical edition, or codicological sample).

Furthermore, documenting project sponsors and funding agencies in `<sponsor>` and `<funder>` ensures that grant requirements and institutional support are formally encoded within the digital file's permanent metadata header.

**Takeaway:** The `<fileDesc>` and `<titleStmt>` document the digital edition as an independent intellectual publication, distinguishing the digital editors from the ancient scribes.

---

## **08 Content**

**Encoding Intellectual Responsibility and Contributions**

Scholarly editions are collaborative endeavors involving transcribers, encoders, research assistants, and institutional investigators. The TEI provides the `<respStmt>` (responsibility statement) element to record granular intellectual credit within the `<titleStmt>`.

A `<respStmt>` pairs a specific statement of responsibility (`<resp>`) with the individual or group who performed it (`<name>` or `<persName>`). In digital philology, transparency regarding who transcribed a folio, who encoded the XML tags, and who audited the collations is essential for scholarly accountability.

```xml
<titleStmt>
  <title>Diplomatic Edition and Codicological Metadata for Codex Marchalianus</title>
  <respStmt>
    <resp>Transcription of Greek diplomatic text</resp>
    <name xml:id="KP">Ken M. Penner</name>
  </respStmt>
  <respStmt>
    <resp>TEI Header manuscript description and collation markup</resp>
    <name xml:id="JD">Jane Doe</name>
  </respStmt>
  <respStmt>
    <resp>Palaeographic audit of hexaplaric marginalia</resp>
    <name xml:id="AS">Alex Smith</name>
  </respStmt>
  <respStmt>
    <resp>Digitization and IIIF manifest curation</resp>
    <orgName xml:id="STFX_DH">St. FX Digital Humanities Laboratory</orgName>
  </respStmt>
</titleStmt>
```

Notice the inclusion of `@xml:id` attributes on each `<name>` element. These unique identifiers allow later elements in the document—such as `<revisionDesc>` change logs or apparatus readings—to point back to specific contributors without repeating their full names.

By formally defining contributor IDs at the top of the header, the digital edition creates a closed, auditable namespace for all editorial assertions made throughout the lifetime of the project.

**Takeaway:** Granular intellectual credit and editorial accountability are established using `<respStmt>`, linking specific scholarly tasks to identified contributors via `@xml:id`.

---

## **09 Content**

**Digital Distribution and Licensing: `<publicationStmt>`**

The second mandatory child of `<fileDesc>` is `<publicationStmt>` (publication statement). This element details the publication, distribution, and licensing conditions under which the digital text is made available to the public (TEI Consortium, 2025).

A properly constructed `<publicationStmt>` must declare the publisher or distributing institution, the geographic settlement, the publication date, and the formal intellectual property license. In modern open-access digital scholarship, editions are frequently published under Creative Commons licenses (such as CC BY 4.0 or CC BY-SA 4.0).

```xml
<publicationStmt>
  <publisher>Department of Religious Studies, St. Francis Xavier University</publisher>
  <pubPlace>Antigonish, Nova Scotia, Canada</pubPlace>
  <date when="2026-09-08">September 8, 2026</date>
  <availability status="restricted">
    <licence target="https://creativecommons.org/licenses/by/4.0/">
      Distributed under an open-access Creative Commons Attribution 4.0 International License (CC BY 4.0).
    </licence>
  </availability>
  <idno type="URI">https://hdl.handle.net/123456789/398-vat-gr-2125</idno>
  <idno type="DOI">10.5281/zenodo.1234567</idno>
</publicationStmt>
```

The `@when` attribute on the `<date>` element enforces standard ISO 8601 formatting (`YYYY-MM-DD`). This ensures that search indexers and bibliographic harvesters can parse publication dates deterministically regardless of human reading habits.

Including persistent digital identifiers—such as Digital Object Identifiers (DOIs) or Handle URIs—within `<idno>` ensures that your digital edition can be permanently cited and indexed in international academic repositories.

**Takeaway:** The `<publicationStmt>` establishes the legal and institutional availability of the digital edition, recording open-access licenses, distributors, and ISO-standard dates.

---

## **10 Content**

**The Source of Record: `<sourceDesc>` as the Codicological Anchor**

The third mandatory child of `<fileDesc>` is `<sourceDesc>` (source description). In a digital edition of a modern printed novel, `<sourceDesc>` might contain a simple bibliographic citation of the 1922 first edition (`<bibl>`). In digital manuscript studies, however, `<sourceDesc>` is the codicological anchor of the entire enterprise.

When an edition is derived directly from a handwritten artifact, `<sourceDesc>` must contain the specialized `<msDesc>` (manuscript description) module (TEI Consortium, 2025). The `<msDesc>` element replaces vague prose citations with a comprehensive, nested taxonomy designed to capture the material, intellectual, and chronological reality of the physical witness.

| `<msDesc>` Sub-Module | TEI Element | Codicological Scope | Primary Child Elements |
| --- | --- | --- | --- |
| Identification | `<msIdentifier>` | Physical holding repository, settlement, and shelfmark | `<country>`, `<settlement>`, `<repository>`, `<idno>` |
| Intellectual Contents | `<msContents>` | List of works, incipits, explicits, and paratexts | `<msItem>`, `<title>`, `<author>`, `<incipit>` |
| Physical Description | `<physDesc>` | Support material, foliation, collation, layout, script, binding | `<objectDesc>`, `<handDesc>`, `<decoDesc>`, `<bindingDesc>` |
| Historical Lifecycle | `<history>` | Origin date/place, chronological provenance transfers, acquisition | `<origin>`, `<provenance>`, `<acquisition>` |
| Supplementary Records | `<additional>` | Microfilms, digital surrogates, finding aids, and bibliography | `<adminInfo>`, `<surrogates>`, `<listBibl>` |

By placing `<msDesc>` inside `<sourceDesc>`, you declare that the digital text following in `<body>` is a direct surrogate and representation of this specific physical object. The metadata encoded in `<msDesc>` provides the physical context that justifies every transcription and apparatus decision made in the body text.

**Takeaway:** In manuscript-based editions, `<sourceDesc>` houses the `<msDesc>` module, anchoring the digital transcription to a specific historical codex.

---

## **11 Content**

**Anchoring the Physical Object: The `<msIdentifier>` Architecture**

Every manuscript description must begin with an `<msIdentifier>` element. The function of `<msIdentifier>` is to provide unambiguous geographic, institutional, and archival coordinates for the physical object (TEI Consortium, 2025).

A handwritten codex exists in a real-world repository. To ensure that scholars worldwide can locate and inspect the physical artifact, `<msIdentifier>` enforces a strict hierarchical address:

- `<country>`: The nation-state where the repository is currently located.
- `<settlement>`: The city, town, or locality of the holding library.
- `<institution>`: The overarching parent organization (e.g., a university, national library, or ecclesiastical body).
- `<repository>`: The specific library, archive, or department holding the item.
- `<collection>`: The named manuscript collection or archival series (optional but common).
- `<idno>`: The shelfmark, catalogue number, or call number uniquely identifying the volume within that repository.
- `<altIdentifier>`: Secondary historical shelfmarks, former collection numbers, or standard cataloguing sigla (such as Gregory-Aland numbers or Rahlfs numbers for biblical manuscripts).

```xml
<msIdentifier>
  <country>Vatican City</country>
  <settlement>Vatican City</settlement>
  <institution>Holy See</institution>
  <repository>Biblioteca Apostolica Vaticana</repository>
  <collection>Vaticani graeci</collection>
  <idno>Vat. gr. 2125</idno>
  <altIdentifier type="Rahlfs">
    <idno>Q</idno>
  </altIdentifier>
  <altIdentifier type="Diktyon">
    <idno>68437</idno>
  </altIdentifier>
  <altIdentifier type="Pinakes">
    <idno>68437</idno>
  </altIdentifier>
</msIdentifier>
```

By recording standard scholarly sigla—such as Rahlfs number Q or Pinakes identifier 68437—inside `<altIdentifier>`, you ensure that external research databases can automatically link your digital edition to existing international authority indices.

**Takeaway:** The `<msIdentifier>` provides the definitive archival address of the physical object, combining country, settlement, repository, shelfmark, and standard scholarly sigla.

---

## **12 Content**

**Case Study: Locating and Identifying Codex Marchalianus (Vat. gr. 2125)**

To ground this markup in a concrete historical exemplar, we examine Codex Marchalianus, preserved in the Vatican Library under the shelfmark *Vat. gr. 2125*. Designated by Alfred Rahlfs as manuscript **Q**, Codex Marchalianus is one of the most celebrated surviving Greek witnesses to the Old Testament prophetic books (Ceriani, 1890).

Written in Egypt during the sixth century CE, Codex Marchalianus is a parchment codex containing the Twelve Minor Prophets, Isaiah, Jeremiah (with Baruch, Lamentations, and the Epistle), Ezekiel, and Daniel (with Susanna and Bel and the Dragon). What makes the manuscript extraordinary is not merely its early date, but its complex layering: written in an elegant Byzantine uncial (majuscule) hand, its wide margins were subsequently packed with thousands of hexaplaric notes, variant readings from Aquila, Symmachus, and Theodotion, and patristic scholia by sixth- and seventh-century correctors (Ceriani, 1890).

When Antonio Maria Ceriani published his landmark photographic facsimile and codicological commentary in 1890, he provided the scholarly world with an exhaustive description of its quires, hands, and history (Ceriani, 1890). In our course exercises, we translate Ceriani's discursive nineteenth-century Latin introduction into structured, machine-actionable TEI XML.

```
Codex Marchalianus Codicological Overview:
- Repository: Biblioteca Apostolica Vaticana (Vatican City)
- Shelfmark: Vat. gr. 2125 (Siglum Q / Rahlfs 2125)
- Date: 6th century CE (origin in Byzantine Egypt)
- Support: Fine calfskin parchment, 416 surviving leaves (foliated 1-416)
- Dimensions: ~305 mm x 240 mm (single column, 29 lines per page)
- Ruling: Hard dry point on flesh side (Leroy-Sautel pattern 00D1)
- Script: Formal Egyptian/Byzantine uncial (majuscule) in dark brown iron-gall ink
- Correctors: Extensive 6th/7th-century marginal hands supplying Hexaplaric variants
```

Translating Ceriani's observations into TEI requires mapping nineteenth-century Latin codicology into rigid XML trees, identifying where Ceriani's prose can be broken down into structured attributes and child elements (Ceriani, 1890).

**Takeaway:** Codex Marchalianus (Vat. gr. 2125) exemplifies a multi-layered sixth-century prophetic witness whose complex physical and marginal features demand rigorous TEI codicological description.

---

## **13 Content**

**Mapping the Intellectual Contents: `<msContents>` and `<msItem>`**

Following the identification of the physical manuscript, the next major branch of `<msDesc>` is `<msContents>`. The `<msContents>` element records the intellectual texts contained within the volume (TEI Consortium, 2025).

A codex is rarely a single continuous text; it is frequently an anthology, a compilation of multiple biblical books, or a collection of disparate patristic treatises. Inside `<msContents>`, each distinct intellectual work is encapsulated within an `<msItem>` element. If a manuscript contains five books of the prophets, the `<msContents>` container will hold five distinct `<msItem>` children, ordered sequentially as they appear in the physical book.

```xml
<msContents>
  <summary>Greek Old Testament Prophets (Twelve Minor Prophets, Isaiah, Jeremiah, Ezekiel, Daniel) with Hexaplaric marginal notes.</summary>
  <textLang mainLang="grc">Ancient Greek (Biblical / Septuagint)</textLang>
  
  <msItem n="1">
    <locus from="1r" to="58v">ff. 1r-58v</locus>
    <title>Dodekapropheton (Twelve Minor Prophets)</title>
    <textLang mainLang="grc"/>
  </msItem>
  
  <msItem n="2">
    <locus from="59r" to="142v">ff. 59r-142v</locus>
    <title>Book of Isaiah</title>
    <textLang mainLang="grc"/>
  </msItem>
  
  <msItem n="3">
    <locus from="143r" to="248v">ff. 143r-248v</locus>
    <title>Jeremiah, Baruch, Lamentations, Epistle of Jeremiah</title>
    <textLang mainLang="grc"/>
  </msItem>
</msContents>
```

The `<locus>` element explicitly binds each intellectual item to its physical coordinates in the book, recording the starting and ending folios (`from="59r" to="142v"`).

When a manuscript contains paratextual additions—such as scribal poems, tables of contents, or Eusebian canon lists—these are also encoded as discrete `<msItem>` or `<msItemStruct>` nodes, preserving the exact internal architecture of the codex.

**Takeaway:** The `<msContents>` element structures the intellectual works in a codex into discrete `<msItem>` nodes, mapping each work to its physical folio range via `<locus>`.

---

## **14 Content**

**Titles, Attributions, and Textual Boundaries**

Within each `<msItem>`, a digital editor must document the internal textual boundaries and scribal framing formulas that define the work. Historical manuscripts do not have modern title pages; scribes marked the beginning and ending of texts with specialized formulas.

To encode these features, TEI provides several dedicated child elements inside `<msItem>`:

- `<author>`: The historical or traditional author attributed to the work.
- `<title>`: The standardized or editorial title of the text.
- `<rubric>`: The heading, title, or liturgical formula written by the scribe at the start of a section (often written in red ink or distinctive script).
- `<incipit>`: The opening words of the actual text itself. Scribes and cataloguers use the incipit to identify texts when titles are missing or damaged.
- `<explicit>`: The closing words of the primary text.
- `<finalRubric>` or `<colophon>`: The concluding scribal blessing, signature, or book-closing announcement.

```xml
<msItem n="2">
  <locus from="59r" to="142v">ff. 59r-142v</locus>
  <author>Isaiah the Prophet</author>
  <title>Book of Isaiah</title>
  <rubric xml:lang="grc">ΟΡΑΣΙΣ ΗΝ ΕΙΔΕΝ ΗΣΑΙΑΣ ΥΙΟΣ ΑΜΩΣ</rubric>
  <incipit xml:lang="grc">Ακουε ουρανε και ενωτιζου γη οτι κυριος ελαλησεν...</incipit>
  <explicit xml:lang="grc">...και εσονται εις ορασιν παση σαρκι.</explicit>
  <finalRubric xml:lang="grc">ΕΤΕΛΕΣΘΗ ΗΣΑΙΑΣ Ο ΠΡΟΦΗΤΗΣ</finalRubric>
</msItem>
```

By recording both the standardized title and the exact scribal `<rubric>` and `<incipit>`, you preserve both machine-searchable standardization and diplomatic fidelity to the physical witness.

In many premodern manuscripts, titles are damaged or absent. In such cases, the `<incipit>` is the primary diagnostic feature used by cataloguing databases to automatically identify the text against canonical registers.

**Takeaway:** Dedicated elements like `<rubric>`, `<incipit>`, and `<explicit>` record the exact scribal framing formulas that mark textual boundaries in the codex.

---

## **15 Content**

**The Physical Description Envelope: `<physDesc>` and Materiality**

The third major branch of `<msDesc>` is `<physDesc>` (physical description). While `<msContents>` documents the intellectual layer, `<physDesc>` captures the physical, material embodiment of the artifact (TEI Consortium, 2025).

The `<physDesc>` element is a structured container holding several specialized sub-modules:

| Physical Property | TEI Sub-Element | Codicological Focus |
| --- | --- | --- |
| Object Architecture | `<objectDesc>` | Support medium, dimensions, foliation, quires, and layout |
| Paleography & Script | `<handDesc>` | Scribal hands, scripts, ink colors, and hand shifts |
| Non-Latin/Greek Scripts | `<scriptDesc>` | Character systems in multilingual or non-Western codices |
| Typography (Incunabula) | `<typeDesc>` | Early printed typefaces and font classifications |
| Musical Notation | `<musicNotation>` | Neumes, staves, and liturgical musical notation |
| Illumination & Art | `<decoDesc>` | Miniatures, decorated initials, and marginal signs |
| Secondary Inscriptions | `<additions>` | Marginal glosses, probationes pennae, and ownership notes |
| Bookbinding | `<bindingDesc>` | Binding structure, boards, leather, clasps, and repairs |
| Seals | `<sealDesc>` | Attached wax, lead, or applied institutional seals |

In hand-authoring `<physDesc>`, you must resist the temptation to write unstructured prose summaries. Every physical property must be placed in its appropriate TEI container to ensure computational discoverability.

By organizing physical data into these distinct containers, digital editions allow scholars to run targeted statistical analyses across manuscript corpora—such as analyzing the correlation between parchment thickness, ruling patterns, and scribal hands.

**Takeaway:** The `<physDesc>` module formalizes the material properties of the manuscript into dedicated sub-elements for support, layout, script, decoration, and binding.

---

## **16 Content**

**Support and Dimensions: `<objectDesc>` and `<supportDesc>`**

Inside `<physDesc>`, the core physical structure of the book is captured within `<objectDesc>`. The `<objectDesc>` element contains two primary sub-elements: `<supportDesc>` (the material carrier and leaf structure) and `<layoutDesc>` (the mise-en-page or page layout).

The `<supportDesc>` element requires an explicit `@material` attribute declaring the medium (e.g., `parchment`, `paper`, `papyrus`, or `mixed`). Inside `<supportDesc>`, the editor provides a prose description in `<support>`, followed by numerical measurements in `<extent>`.

```xml
<objectDesc form="codex">
  <supportDesc material="parchment">
    <support>
      <p>High-quality calfskin parchment, medium thickness, supple and well-scraped. Follicle patterns visible on flesh sides; hair sides show light yellow tone.</p>
    </support>
    <extent>
      <measure unit="leaf" quantity="416">416 folios</measure>
      <dimensions unit="mm" type="leaf">
        <height quantity="305">305 mm</height>
        <width quantity="240">240 mm</width>
      </dimensions>
      <dimensions unit="mm" type="written">
        <height quantity="220">220 mm</height>
        <width quantity="155">155 mm</width>
      </dimensions>
    </extent>
  </supportDesc>
</objectDesc>
```

Notice that measurements are encoded twice: as machine-readable numbers inside `@quantity` attributes, and as human-readable strings inside element content. This dual-encoding pattern ensures that computational algorithms can calculate aspect ratios or search by dimension thresholds without parsing raw text strings.

Recording both total leaf dimensions and written area dimensions allows scholars to calculate the ratio of margin to text, providing critical evidence regarding the prestige and economic expenditure of the manuscript's production.

**Takeaway:** The `<supportDesc>` captures the physical medium and leaf dimensions, using `@quantity` and `@unit` attributes to provide machine-actionable measurements.

---

## **17 Content**

**Foliation, Pagination, and Extent**

Manuscripts often exhibit complex foliation histories. A codex may contain medieval Roman numerals in ink, eighteenth-century Arabic numerals in iron-gall ink, and modern stamped or penciled foliation applied by nineteenth-century library conservators.

The TEI allows editors to record these distinct numbering systems using the `<foliation>` element inside `<supportDesc>`. If folios were lost, inserted out of order, or misnumbered, these anomalies must be explicitly documented.

```xml
<supportDesc material="parchment">
  <extent>
    <measure unit="leaf" quantity="416">416 folios</measure>
  </extent>
  <foliation n="1" type="modern">
    Modern pencil foliation in upper right recto corner, numbered 1-416, applied during Vatican Library conservation in 1888.
  </foliation>
  <foliation n="2" type="early-modern">
    Traces of an earlier 16th-century ink foliation in lower margin, partly trimmed away by rebinding.
  </foliation>
  <condition>
    <p>Complete except for lost preliminary leaves; leaves 12 and 13 show minor insect damage in outer margins, text unaffected.</p>
  </condition>
</supportDesc>
```

Documenting the foliation system is essential for citation integrity: if a nineteenth-century collator cites folio 62v based on an old ink numbering, while your digital edition cites folio 64v based on modern pencil numbering, the discrepancy must be resolved in `<foliation>`.

Furthermore, recording physical damage and insect erosion in `<condition>` establishes the material justification for lacunae and illegible readings in downstream diplomatic transcriptions.

**Takeaway:** The `<foliation>` element documents the history and location of leaf-numbering systems, resolving discrepancies between historical and modern citations.

---

## **18 Content**

**Codicological Collation Formulas: `<collation>`**

In manuscript studies, *collation* refers to the physical assembly of quires (gatherings of bifolia) that form the codex. Documenting collation reveals how the manuscript was manufactured, whether quires were lost, and where later leaves were inserted.

Within `<supportDesc>`, the `<collation>` element records the quire structure. Codicologists represent quires using standardized algebraic notation, such as the formula popularized by Neil Ker: quire numbers in Roman or Arabic numerals, followed by superscripts indicating the number of leaves in the quire (e.g., $1	ext{–}52^8$ denoting 52 regular quaterniones).

```xml
<collation>
  <p>The manuscript consists of 52 regular quaterniones (quires of 8 leaves / 4 bifolia), numbered continuously with Greek quire signatures in the upper inner margin.</p>
  <formula>1-52<hi rend="superscript">8</hi> (total 416 leaves)</formula>
  <signatures>Original Greek quire signatures (αʹ through νβʹ) written by the primary scribe on the first recto and last verso of each gathering.</signatures>
  <catchwords>No catchwords present (consistent with 6th-century Egyptian uncial practices).</catchwords>
</collation>
```

When hand-authoring `<collation>`, digital editors must carefully inspect quire signatures and hair/flesh orientation (Gregory's Rule) on digital facsimiles to verify whether quires are intact or anomalous. Gregory's Rule observes that Greek scribes arranged quires so that flesh sides faced flesh sides and hair sides faced hair sides across every opening.

Deviations from Gregory's Rule or breaks in quire signature numeration indicate missing leaves, inserted bifolia, or structural disruptions that must be documented in the `<collation>` formula.

**Takeaway:** The `<collation>` element formalizes the physical structure of quires, leaf counts, and quire signatures, exposing the mechanical construction of the codex.

---

## **19 Content**

**Layout Description and Page Architecture: `<layoutDesc>`**

The second major child of `<objectDesc>` is `<layoutDesc>` (layout description). This element describes the mise-en-page: how the physical surface of each page was prepared, ruled, and filled with script.

Within `<layoutDesc>`, one or more `<layout>` elements record the number of columns, lines per column, ruling methods, and bounding box dimensions. Attributes such as `@columns`, `@writtenLines`, and `@ruledLines` provide machine-readable layout parameters.

```xml
<layoutDesc>
  <layout columns="1" writtenLines="29" ruledLines="29">
    <p>Written in a single broad column of 29 lines per page. Bounding lines and text lines scored with a hard dry point on the flesh side (Leroy-Sautel ruling pattern 00D1).</p>
    <dimensions unit="mm" type="column">
      <height quantity="220"/>
      <width quantity="155"/>
    </dimensions>
    <note>Exceptionally wide outer margins (approx. 65 mm) deliberately planned to accommodate hexaplaric notes and patristic scholia.</note>
  </layout>
</layoutDesc>
```

Recording page architecture is critical for downstream transcription and image alignment: automated handwriting recognition (HTR) and layout analysis tools (such as Transkribus in Week 4) depend directly on baseline and column models defined in `<layoutDesc>`.

Codicologists classify ruling patterns using standard classification systems, such as the Leroy-Sautel system for Greek manuscripts. Recording the ruling code (`00D1`) in `<layout>` allows computational comparison of scriptorium ruling traditions across late antiquity.

**Takeaway:** The `<layoutDesc>` and `<layout>` elements capture the mise-en-page, specifying column counts, written lines, ruling techniques, and margin widths.

---

## **20 Content**

**Paleographic Analysis: The `<handDesc>` and `<handNote>` Elements**

Following `<objectDesc>`, the next critical component of `<physDesc>` is `<handDesc>` (hand description). A manuscript may be written by a single scribe or by multiple collaborating scribes across centuries.

Within `<handDesc>`, each distinct scribal hand is assigned a `<handNote>` element with a unique `@xml:id`. The `<handNote>` describes the script family, ink color, letterform ductus, and chronological period of that hand.

```xml
<handDesc hands="3">
  <summary>Written primarily in a formal 6th-century Byzantine uncial hand, with extensive 6th- and 7th-century marginal hands.</summary>
  
  <handNote xml:id="h1" scope="major" script="uncial" medium="brown-ink">
    <p><label>Hand 1 (Primary Scribe):</label> Formal Egyptian/Byzantine uncial (majuscule), upright, round, with slight serifs on vertical strokes of tau and gamma. Brown iron-gall ink. Responsible for the primary biblical text.</p>
  </handNote>
  
  <handNote xml:id="h2" scope="minor" script="cursive-uncial" medium="black-ink">
    <p><label>Hand 2 (Hexaplaric Corrector):</label> Rapid semi-uncial hand writing in dark blackish-green ink in outer margins. Responsible for supplying variant readings from Aquila, Symmachus, and Theodotion.</p>
  </handNote>
  
  <handNote xml:id="h3" scope="minor" script="byzantine-minuscule" medium="faded-ink">
    <p><label>Hand 3 (Late Scholiast):</label> Early minuscule hand (9th/10th century) adding occasional theological glosses in lower margins.</p>
  </handNote>
</handDesc>
```

Assigning `@xml:id="h1"`, `@xml:id="h2"`, etc., enables you to tag every word, line, or marginal addition in your transcription with a `@hand` attribute (e.g., `<add hand="#h2">`), explicitly linking text fragments to specific scribes.

In ancient manuscripts, scribes also used distinctive abbreviations known as *nomina sacra* (e.g., ΘΣ for Θεός, ΚΣ for Κύριος) written with a supralinear stroke. Documenting how each hand treats nomina sacra provides vital paleographical diagnostic data.

**Takeaway:** The `<handDesc>` and `<handNote>` elements document distinct scribal hands, establishing unique `@xml:id` handles for granular paleographic attribution in transcriptions.

---

## **21 Content**

**Decorations, Miniatures, and Marginal Signs: `<decoDesc>`**

Manuscripts frequently contain non-textual graphic elements, ranging from full-page illuminations to subtle philological punctuation signs. These features are documented in `<decoDesc>` (decoration description).

Inside `<decoDesc>`, each distinct decorative element or system of signs is encoded inside a `<decoNote>` element. In biblical manuscripts like Codex Marchalianus, critical signs—such as Aristarchian asterisks and obels—are vital philological data (Ceriani, 1890).

```xml
<decoDesc>
  <decoNote type="initials">
    <p>Enlarged uncial initials at the beginning of each biblical book (approx. 25-30 mm high), decorated with simple red and green geometric penwork.</p>
  </decoNote>
  <decoNote type="philological-signs">
    <p>Extensive use of Origenian hexaplaric signs in left margins: asterisks (※) marking words present in Hebrew but missing in the Old Greek, and obels (÷) marking words present in the Old Greek but absent in Hebrew.</p>
  </decoNote>
  <decoNote type="miniatures" subtype="frontispiece">
    <p>No figurative miniatures; decorative knotted headpieces at the opening of Isaiah (fol. 59r) and Jeremiah (fol. 143r).</p>
  </decoNote>
</decoDesc>
```

Documenting these signs in the header provides the cataloguing framework required when you later transcribe marginal signs in Topic 04 and Topic 08.

Origen's Hexapla placed six parallel columns side-by-side to compare the Hebrew text with Greek translations. In copies of the Septuagint derived from the Hexapla, scribes transferred Origen's critical signs into the margins, making them indispensable evidence for textual criticism (Ceriani, 1890).

**Takeaway:** The `<decoDesc>` module catalogues artistic illuminations, decorated initials, and critical philological signs like asterisks and obels.

---

## **22 Content**

**The Binding and Structural Protection: `<bindingDesc>`**

A codex is protected by its binding. However, very few premodern manuscripts retain their original bindings; most surviving codices have been rebound multiple times across their historical lifecycle.

Within `<physDesc>`, the `<bindingDesc>` element records the physical construction, boards, covering materials, clasps, and conservation history of the binding.

```xml
<bindingDesc>
  <binding contemporary="false">
    <p>Vatican Library conservation binding executed in 1968. Dark brown morocco leather over modern wooden boards, gold-stamped on spine with the arms of Pope Paul VI and the shelfmark <quote>Vat. Gr. 2125</quote>.</p>
    <condition>
      <p>Excellent modern structural condition; spine tight, sewing on five modern raised cords with acid-free Japanese paper guards.</p>
    </condition>
    <decoNote>Blind-tooled fillets on front and back boards.</decoNote>
  </binding>
</bindingDesc>
```

The attribute `@contemporary="false"` explicitly states that the binding is not contemporary with the sixth-century manufacturing of the parchment leaves. This distinction prevents researchers from mistaking modern binding structures for late antique craft.

When older binding fragments—such as medieval pastedowns or fragments of lost manuscripts used as spine lining—are preserved during rebinding, their presence is documented inside `<binding>` child elements.

**Takeaway:** The `<bindingDesc>` documents the bookbinding materials, sewing structure, and conservation history, explicitly distinguishing contemporary bindings from modern rebinding.

---

## **23 Content**

**The Chronological Lifecycle: The `<history>` Element**

The fourth major branch of `<msDesc>` is `<history>`. The `<history>` element formalizes the chronological lifecycle and historical movement of the artifact across time and space (TEI Consortium, 2025).

A manuscript is not a static museum object; it is an itinerant survivor. It was manufactured at a specific date in a specific scriptorium (`<origin>`), possessed by a succession of monastic communities, private collectors, or royal libraries (`<provenance>`), and ultimately accessioned into its current repository (`<acquisition>`).

| Historical Stage | TEI Child Element | Codicological and Custodial Scope |
| --- | --- | --- |
| Manufacturing Moment | `<origin>` | Scribal production date, scriptorium place, and scribe |
| First Custodial Phase | `<provenance>` (1) | Early monastic preservation and medieval library holdings |
| Second Custodial Phase | `<provenance>` (2) | Renaissance humanistic collectors and private ownership |
| Institutional Accession | `<acquisition>` | Formal transfer and entry into current institutional repository |

By structuring history into distinct chronological events, TEI aligns directly with event-centric Linked Open Data ontologies like CIDOC-CRM (Le Bœuf, 2012; Koho et al., 2021). Each historical transfer represents a discrete event with its own temporal bounds, geographic locations, and historical agents.

**Takeaway:** The `<history>` element traces the temporal lifecycle of the codex, dividing its history into origin, sequential provenance transfers, and modern institutional acquisition.

---

## **24 Content**

**Dating and Localizing the Manuscript: `<origin>`**

The `<origin>` element records the circumstances of the manuscript's creation. It captures *when* the manuscript was written (`<origDate>`) and *where* it was written (`<origPlace>`).

Dating premodern manuscripts is inherently uncertain. When a colophon is missing, palaeographers estimate date ranges based on script style, orthography, and material support. The TEI provides machine-readable date attributes to capture this scholarly uncertainty:

- `@when`: A single exact date (e.g., `@when="1245-04-12"`).
- `@notBefore` and `@notAfter`: A bounding date range (e.g., `@notBefore="0550"` and `@notAfter="0599"` for the sixth century).
- `@from` and `@to`: A known period of continuous production.
- `@cert`: Editorial certainty (`high`, `medium`, `low`).

```xml
<history>
  <origin>
    <origDate notBefore="0550" notAfter="0599" cert="medium" evidence="palaeographic">
      Late 6th century CE (ca. 550–600 CE)
    </origDate>
    <origPlace ref="https://pleiades.stoa.org/places/727070">
      Egypt (likely Alexandria or the Nitrian Desert)
    </origPlace>
    <p>Produced in an established Byzantine-Egyptian scriptorium, as evidenced by distinctive Coptic-influenced uncial letterforms and Egyptian orthographic patterns (Ceriani, 1890).</p>
  </origin>
</history>
```

By encoding `@evidence="palaeographic"`, the editor explicitly documents the scholarly basis for the assigned date, distinguishing stylistic dating from explicit colophon dates.

**Takeaway:** The `<origin>` element uses ISO 8601 attributes like `@notBefore` and `@notAfter` to represent historical dating ranges and palaeographical uncertainty.

---

## **25 Content**

**Custodial Chain and Migration: The `<provenance>` Sequence**

Between its creation and its arrival in a modern research library, a manuscript often migrated across continents through sales, bequests, confiscations, and gifts. Each discrete historical transfer of custody is encoded in an independent `<provenance>` element (Koho et al., 2021).

Recording provenance as a sequence of distinct events allows computational knowledge graphs to map the migration of cultural heritage across centuries (Koho et al., 2021).

```xml
<history>
  <origin><!-- ... --></origin>
  
  <provenance notBefore="0800" notAfter="0900">
    <p>Preserved in the Library of the Monastery of Saint Macarius the Great in the Nitrian Desert (Wadi El Natrun, Egypt) during the 9th century.</p>
  </provenance>
  
  <provenance notBefore="1500" notAfter="1550">
    <p>Acquired by the humanist scholar and collector René Marchal, Abbot of Saint-Nom in Paris, from whose collection the manuscript derives its traditional name <name type="ms-nickname">Codex Marchalianus</name>.</p>
  </provenance>
  
  <provenance when="1738">
    <p>Passed into the collection of Cardinal François de Mailly, Archbishop of Reims, who subsequently gifted the volume to Pope Clement XII for the Vatican Library in 1738.</p>
  </provenance>
</history>
```

When a manuscript contains former library shelfmarks or bookplates, these physical traces are encoded within their respective `<provenance>` elements, establishing a verifiable physical audit trail for each custodial transfer (Koho et al., 2021).

**Takeaway:** The custodial chain is modeled as a chronological sequence of `<provenance>` elements, enabling computational tracking of manuscript migrations across time and geography.

---

## **26 Content**

**Administrative and Acquisition Metadata: `<acquisition>` and `<additional>`**

The final elements of the manuscript description record institutional acquisition and supplementary administrative metadata.

The `<acquisition>` element sits inside `<history>` and details the specific date, method, and transaction by which the manuscript entered its current repository. Following `<history>`, the optional `<additional>` element records administrative surrogates (microfilms, digitizations), secondary literature (`<listBibl>`), and cross-references to external catalogues.

```xml
<history>
  <!-- origin and provenance -->
  <acquisition when="1738-06-15">
    <p>Accessioned into the Biblioteca Apostolica Vaticana on June 15, 1738, under the reign of Pope Clement XII, entered into the Latin-Greek inventory as <quote>Vat. gr. 2125</quote>.</p>
  </acquisition>
</history>

<additional>
  <adminInfo>
    <recordHist>
      <source>
        <p>Codicological metadata transcribed from Ceriani (1890) and updated against the online Vatican Library DVL catalogue records.</p>
      </source>
    </recordHist>
  </adminInfo>
  <listBibl>
    <bibl>Ceriani, A. M. (1890). <title>De Codice Marchaliano seu Vaticano Graeco 2125: Prophetarum Bibliothecae Vaticanae commentatio</title>. Romae.</bibl>
  </listBibl>
</additional>
```

Recording secondary literature in `<listBibl>` ensures that future editors can trace the scholarly genealogy of every codicological claim made in the digital header.

**Takeaway:** The `<acquisition>` and `<additional>` elements document the institutional accession history, cataloguing sources, and related secondary bibliography for the manuscript.

---

## **27 Content**

**Common Syntax Traps in Hand-Authoring TEI Headers**

When writing XML by hand without the safety net of an interactive compiler, beginners frequently fall into predictable syntax traps. Understanding these common defects will help you audit your draft before tomorrow's validation lab.

| Syntax Defect | Error Description | Prevention and Solution |
| --- | --- | --- |
| Unescaped ampersand | Writing `&` directly in text content (e.g., `Clemens & Graham`) | Always write `&amp;` in XML text nodes. |
| Tag case mismatch | Mismatched capitalization (e.g., `<msDesc>` closed with `</msdesc>`) | Enforce exact case consistency across opening and closing tags. |
| Missing attribute quotes | Omitting quotes around attribute values (e.g., `<measure quantity=416>`) | Always surround attribute values with double quotes (`quantity="416"`). |
| Illegal element nesting | Placing `<msContents>` outside `<msDesc>` or `<titleStmt>` outside `<fileDesc>` | Review the strict TEI hierarchy before closing parent elements. |
| Incomplete self-closure | Writing `<pb>` or `<lb>` without a trailing slash | Use explicit self-closing syntax: `<pb/>`, `<lb/>`, `<dimensions/>`. |

Taking time to manually trace your element openings and closures line-by-line prevents cascade parsing errors where a single missing bracket invalidates hundreds of subsequent lines.

Furthermore, pay close attention to XML attribute naming conventions: attributes like `@xml:id` and `@xml:lang` belong to the reserved XML namespace and require the `xml:` prefix, whereas standard TEI attributes like `@type`, `@n`, and `@ref` must never carry a prefix.

**Takeaway:** Hand-written XML requires rigorous manual checking for unescaped characters, case mismatches, missing quotes, and improper tag containment.

---

## **28 Content**

**Building the Ground Truth: The Student's Primary Witness Header**

Now you synthesize all twenty-seven preceding sections into a complete, working XML document. Today's lab deliverable is to hand-author the full `<teiHeader>` for the primary manuscript witness you selected in Week 1.

Open a basic plain-text editor (such as VS Code with XML extensions disabled, nano, or TextEdit in plain-text mode). Do not use Oxygen XML Editor today; do not use automated schema autocomplete.

Your file must contain the following complete structure:

1. The XML declaration: `<?xml version="1.0" encoding="UTF-8"?>`
2. The root `<TEI>` element declaring the TEI namespace: `<TEI xmlns="http://www.tei-c.org/ns/1.0">`
3. A complete `<teiHeader>` containing:
   - `<fileDesc>` with `<titleStmt>`, `<publicationStmt>`, and `<sourceDesc>`
   - An `<msDesc>` inside `<sourceDesc>` with `<msIdentifier>`, `<msContents>`, `<physDesc>`, and `<history>`
4. A stub `<text>` element containing a placeholder division for next week's transcription:
   ```xml
   <text>
     <body>
       <div type="transcription">
         <p><!-- Diplomatic transcription will be authored here in Topic 04 --></p>
       </div>
     </body>
   </text>
   ```

Save your file in your personal Git repository under the path `src/modules/Topic_02_Cataloguing/03a_Lesson_2.1_Primary_Witness_Header.xml`.

Ensure that your header contains real codicological data derived from your inspection of your manuscript's digital facsimiles and published catalogue records, rather than placeholder lorem ipsum text.

**Takeaway:** Hand-authoring your selected manuscript's complete `<teiHeader>` creates the foundational XML ground truth for the remainder of the semester.

---

## **29 Content**

**Preparing for Wednesday's Audit: Deliverables and Configuration**

Before you conclude today's session, you must commit your hand-authored XML file to Git version control. Today's commit represents your unassisted, manual editorial work.

Follow the version control discipline established in Topic 01 (Huskey, 2024). Review your file status, verify that your changes are staged cleanly, and compose an atomic commit message describing your codicological decisions.

```bash
# Verify the status of your newly created header
git status

# Stage your hand-written TEI header
git add src/modules/Topic_02_Cataloguing/03a_Lesson_2.1_Primary_Witness_Header.xml

# Create an atomic commit documenting your manual baseline
git commit -m "Topic 02: Hand-authored initial teiHeader and msDesc for primary witness"
```

Do not edit this file further today. Tomorrow morning, in Lesson 2.2, you will open this exact file in Oxygen XML Editor and subject it to deterministic RELAX NG and Schematron schema validation. Every error that Oxygen flags tomorrow will be a direct measurement of the gap between human intuition and formal computational schemas.

Freezing your manual ground truth in Git ensures that your comparative experiment remains mathematically valid and auditable throughout the course.

**Takeaway:** Committing your hand-written XML file to Git freezes your manual ground truth, establishing the baseline for tomorrow's deterministic schema audit.

---

## **30 Content**

**Synthesis: The Header as an Argument in Structural Form**

A TEI Header is not administrative overhead; it is a scholarly argument in structural form. When you decide how to represent a manuscript's quire structure, how to date its scribal hands, and how to identify its historical owners, you are performing original textual scholarship (Le Bœuf, 2012; TEI Consortium, 2025).

The manual step of this week's comparative cycle has forced you to slow down and confront the material complexity of your historical witness. By translating physical parchment, ruling patterns, and ink traces into rigid XML elements, you have experienced the profound epistemological shift from discursive cataloguing to formal data modeling.

```
Comparative Cycle Progress — Week 2 (Topic 02):
[X] Tue: Manual — Hand-written TEI Header and msDesc (Human Ground Truth)
[ ] Wed: Deterministic — RELAX NG & Schematron validation in Oxygen, RDF LOD, CTS URNs
[ ] Fri: AI-Assisted — LLM metadata extraction scored against your manual baseline
```

Tomorrow, we move to Step 2: deterministic validation. You will see how formal schemas act as unyielding gatekeepers, ensuring that your humanistic interpretations conform perfectly to global computational standards.

As you step away from your editor today, reflect on the decisions you made. Every tag you chose represents a theoretical claim about how a physical historical object should be represented in a digital medium.

**Takeaway:** A TEI Header is an explicit scholarly argument that translates physical manuscript materiality into a formal, auditable digital data architecture.

---

## References

Ceriani, A. M. (1890). *De Codice Marchaliano seu Vaticano Graeco 2125: Prophetarum Bibliothecae Vaticanae commentatio*. Romae.

Huskey, S. J. (2024). Editorial workflows in the digital age: Git and version control for textual scholarship. *Digital Humanities Quarterly*, 18(2).

Koho, M., Burrows, T., Hyvönen, E., Ikkala, E., Page, K., Ransom, L., ... & Wijsman, H. (2021). Harmonizing and publishing heterogeneous premodern manuscript metadata as Linked Open Data. *Journal of the Association for Information Science and Technology*, 73(2), 240–257. https://doi.org/10.1002/asi.24499

Le Bœuf, P. (2012). Modeling rare and unique documents: Using FRBRoo/CIDOC CRM. *Journal of Archival Organization*, 10(2), 96–106.

TEI Consortium. (2025). *TEI P5: Guidelines for Electronic Text Encoding and Interchange*. Version 4.8.0. https://tei-c.org/release/doc/tei-p5-doc/en/html/
