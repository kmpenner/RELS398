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

