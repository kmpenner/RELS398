# Lesson 2.2 — Deterministic Schema Validation, Linked Data, and Canonical Citation

*RELS 398 / ENGL 398 · Topic 2: Cataloguing · Meeting #4 (Wed Sep 9)*

***Step 2 of the three-step cycle: deterministic.** Today you take yesterday's hand-written header into Oxygen XML Editor, validate it against the TEI RELAX NG schema and Schematron rules, link your entities with RDF triples to LOD authority files, and assign Canonical Text Services (CTS) URNs. The validation engine is an uncompromising structural gatekeeper.*

---

## **01 Content**

**What "Deterministic" Means in Structural Philology**

The second step of our comparative cycle transitions from manual authorship to deterministic computation. In computational philology, a process is *deterministic* when identical inputs subjected to explicit, rule-governed algorithms produce identical, mathematically verifiable outputs every single time. Unlike probabilistic models, neural networks, or human interpretive intuition, deterministic systems operate without statistical approximation, ambiguity, or generative variance.

In the context of manuscript cataloguing and text encoding, deterministic methods govern document validation, semantic graph generation, and canonical citation resolving. When you feed your hand-written TEI XML document into a validation engine, the software does not "interpret" your prose or offer an intuitive impression of your encoding; it evaluates every element, attribute, and character against a formal mathematical grammar (Cummings, 2018; TEI Consortium, 2025).

The distinction between syntactic well-formedness and schema validity is the foundation of this discipline. A document that is well-formed merely satisfies the basic syntax of XML—tags close properly and attributes are quoted. A document that is *valid*, however, proves that its structural hierarchy, element sequencing, data types, and internal cross-references conform completely to a domain-specific model defined by an editorial community (Cummings, 2018; TEI Consortium, 2025). Schema validation is the non-negotiable structural gatekeeper of digital scholarship.

Furthermore, deterministic validation creates the epistemological foundation for downstream data processing. If a digital edition guarantees that every date is an ISO 8601 string and every manuscript shelfmark resides inside `//tei:msDesc/tei:msIdentifier/tei:idno`, external software can ingest millions of records without human intervention. Determinism replaces ad-hoc data cleaning with certified structural compliance.

**Takeaway:** Deterministic validation evaluates XML documents against explicit, rule-governed schemas, transforming subjective text entry into mathematically verifiable and interoperable research data.

---

## **02 Content**

**The Grammar of XML: Understanding RELAX NG (RNG)**

To enforce structural consistency across digital editions, the digital humanities community relies heavily on schema definition languages. Historically, XML utilized Document Type Definitions (DTDs) and W3C XML Schema (XSD). However, modern digital philology and the Text Encoding Initiative have standardized on RELAX NG (REgular LAnguage for XML Next Generation), typically expressed in its XML syntax (RNG) or compact syntax (RNC) (Cummings, 2018; TEI Consortium, 2025).

RELAX NG is based on the mathematical theory of formal grammars and tree automata. Unlike DTDs, which have limited datatype support and complex syntactic quirks, RELAX NG treats XML documents as structured pattern trees. It allows editors to define exact parent-child relationships, element choices, interleave patterns (allowing elements to occur in any order), and rich datatypes (such as ISO 8601 dates or numerical ranges) using standard W3C datatypes (TEI Consortium, 2025).

| Schema Technology | Theoretical Basis | Strengths in Manuscript Encoding | Primary Limitations |
| --- | --- | --- | --- |
| Document Type Definition (DTD) | Context-free grammar | Legacy standard, lightweight parsing | No namespace support, weak datatyping |
| W3C XML Schema (XSD) | Object-oriented grammar | Strong datatyping, widespread commercial adoption | Verbose syntax, rigid deterministic constraints |
| RELAX NG (RNG) | Tree automata & regular expressions | Clean syntax, full namespace support, flexible patterns | Requires supplementary rules for cross-element logic |
| ISO Schematron | Rule-based XPath assertions | Business logic, internal cross-reference auditing | Does not define basic structural grammar on its own |

By expressing TEI constraints in RELAX NG, a project can guarantee that every digital manuscript record shares an identical structural grammar regardless of which scholar authored the file. RELAX NG patterns can declare optional elements, mutually exclusive choices, and recursive structures without ambiguous parser states.

**Takeaway:** RELAX NG provides the mathematical tree grammar that defines permissible element hierarchies, sequences, and datatypes across TEI digital editions.

---

## **03 Content**

**Validating the Hand-Written Header in Oxygen XML Editor**

Today's practical work takes place inside the Oxygen XML Editor, the standard interactive development environment for digital textual scholarship. Oxygen integrates parser engines (such as Xerces and Jing) that execute real-time, background validation as you inspect and modify your XML files (Cummings, 2018).

To connect your XML document to a validation schema, you insert an `xml-model` processing instruction at the very top of your file, immediately following the XML declaration:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="https://raw.githubusercontent.com/msdesc/consolidated-tei-schema/master/msdesc.rng" 
            type="application/xml" 
            schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="https://raw.githubusercontent.com/msdesc/consolidated-tei-schema/master/msdesc.sch" 
            type="application/xml" 
            schematypens="http://purl.oclc.org/dsdl/schematron"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <!-- Document content -->
</TEI>
```

When you open yesterday's hand-written header in Oxygen with these processing instructions active, the editor will immediately audit your text. If your file contains syntax defects or schema violations, Oxygen displays red squiggly underlines and populates the lower validation panel with explicit compiler error logs.

Learning to read compiler error messages is an essential editorial skill. An error stating `element "mscontents" not allowed here; expected the element "msContents"` alerts you to a fatal case-sensitivity error. An error stating `attribute "material" not allowed at this point; missing required child "support"` indicates that your element nesting violates the RELAX NG content model (TEI Consortium, 2025).

As you resolve each error in Oxygen, the editor dynamically re-evaluates the tree, turning red warning indicators green only when every single syntactic and grammatical rule has been completely satisfied.

**Takeaway:** Oxygen XML Editor links XML documents to RELAX NG and Schematron schemas via `<?xml-model?>` instructions, providing instant compiler feedback on structural defects.

---

## **04 Content**

**Structural Rules and Element Hierarchy in RNG**

The primary function of a RELAX NG schema is enforcing hierarchical containment rules. In humanistic prose, a writer can place ideas in any sequence; in structured text encoding, elements must strictly obey parent-child and sibling rules defined by the schema (Cummings, 2018).

Consider the codicological hierarchy of `<msDesc>`. The TEI RELAX NG schema dictates that `<msDesc>` can only contain a specific sequence of major components: `<msIdentifier>`, followed optionally by `<head>`, `<msContents>`, `<physDesc>`, `<history>`, `<additional>`, and `<msPart>`. If an encoder accidentally inserts `<history>` before `<msContents>`, or places `<supportDesc>` directly inside `<msDesc>` without wrapping it in `<physDesc>`, the RELAX NG parser rejects the document instantly (TEI Consortium, 2025).

```xml
<!-- INVALID: Illegal sibling order and missing container -->
<msDesc xml:id="ms1">
  <msIdentifier><!-- ... --></msIdentifier>
  <history><!-- history placed prematurely before msContents --></history>
  <supportDesc material="parchment"><!-- supportDesc missing parent physDesc --></supportDesc>
</msDesc>

<!-- VALID: Proper hierarchical nesting and sequential order -->
<msDesc xml:id="ms1">
  <msIdentifier><!-- ... --></msIdentifier>
  <msContents><!-- ... --></msContents>
  <physDesc>
    <objectDesc form="codex">
      <supportDesc material="parchment"><!-- ... --></supportDesc>
    </objectDesc>
  </physDesc>
  <history><!-- ... --></history>
</msDesc>
```

These containment rules prevent the degradation of archival data. Because every valid TEI document adheres to the same structural tree, downstream rendering scripts (XSLT transformations) and search engines can navigate directly to `//tei:physDesc/tei:objectDesc/tei:supportDesc` without writing specialized code for each contributor.

Furthermore, hierarchical containment formalizes ontological relationships: a `<supportDesc>` is not an independent physical object, but a physical property of the `<objectDesc>`, which in turn is a component of the manuscript's physical description.

**Takeaway:** RELAX NG strictly enforces element containment and sequencing, ensuring that complex manuscript metadata is predictable and machine-traversable.

---

## **05 Content**

**Data Typing, Enumerations, and Attribute Constraints**

Beyond governing element placement, RELAX NG enforces rigorous constraints on attribute values and textual content. In unconstrained XML, an attribute can contain any arbitrary string of text. A schema, however, restricts attributes to specific datatypes or closed lists of authorized terms (enumerations) (TEI Consortium, 2025).

Data typing is particularly vital for temporal and quantitative data. When recording dates in `<origDate>` or `<date>`, the TEI schema validates that `@when`, `@notBefore`, and `@notAfter` match the W3C XML Schema datatype `xsd:date` or `xsd:gYear` (ISO 8601 format: `YYYY-MM-DD` or `YYYY`). If a student writes `@when="Sixth Century"` or `@notBefore="ca. 550"`, the validator raises an invalid datatype error. Descriptive nuances belong in the element's text content; the attribute must remain a machine-computable integer or date string.

```xml
<!-- INVALID: Raw prose inside machine-readable attribute -->
<origDate when="Late Sixth Century" cert="maybe">Written ca. 575 CE</origDate>

<!-- VALID: Standard ISO 8601 date range with enumerated certainty -->
<origDate notBefore="0550" notAfter="0599" cert="medium">Late 6th century CE (ca. 550–599 CE)</origDate>
```

Furthermore, schemas enforce *enumerations*—controlled vocabularies for attributes like `@type`, `@role`, and `@status`. In `<objectDesc form="codex">`, the schema restricts `@form` to values such as `codex`, `leaf`, `scroll`, or `fragment`, preventing typographical errors like `book` or `manuscript-volume` from polluting digital databases.

By enforcing these constraints, deterministic validation guarantees that downstream statistical scripts can calculate median manuscript dates, sort volumes by dimension, or filter by support material without encountering unparseable formatting errors.

**Takeaway:** Schemas enforce ISO datatypes and controlled attribute enumerations, ensuring that chronological, numerical, and categorical values remain machine-computable.

---

## **06 Content**

**Beyond Grammar: The Necessity of Schematron Business Logic**

While RELAX NG provides an exceptional framework for defining grammatical structures and datatypes, it has a fundamental limitation: it operates locally within the context of parent-child relationships. RELAX NG cannot easily enforce rules that depend on relationships across disparate branches of the document tree.

For example, RELAX NG cannot verify whether an ID referenced in an attribute (such as `<name ref="#JD">` or `<add hand="#h2">`) actually exists as an `@xml:id` elsewhere in the file. Nor can it verify that *if* a manuscript is declared to have three hands (`<handDesc hands="3">`), there must be exactly three distinct `<handNote>` elements inside the container.

To enforce these complex editorial constraints, digital philologists deploy ISO Schematron (Cummings, 2018). Schematron is a rule-based validation language that uses XPath (XML Path Language) expressions to evaluate arbitrary assertions across the entire document tree. While RELAX NG asks "Is this element grammatically allowed here?", Schematron asks "Does this document satisfy our project's scholarly business logic?"

| Validation Need | Handled by RELAX NG | Handled by Schematron | Implementation Approach |
| --- | --- | --- | --- |
| Element hierarchy & nesting | Yes | Possible, but verbose | RNG tree grammar containment |
| ISO date formatting | Yes | Possible, but verbose | W3C XML Schema datatypes |
| Closed vocabulary enumerations | Yes | Yes | RNG `<choice>` / Schematron regex |
| Internal cross-reference existence | No | Yes | Schematron XPath `@target = //@xml:id` |
| Conditional requirements | No | Yes | Schematron `test="if-then" XPath rules` |
| Quantitative parity verification | No | Yes | Schematron `test="count(handNote) = @hands"` |

Schematron acts as the project's automated editorial supervisor, catching logical and referential errors that tree grammars overlook entirely.

**Takeaway:** ISO Schematron complements RELAX NG by executing XPath-driven business logic and cross-element assertions that grammar-based schemas cannot evaluate.

---

## **07 Content**

**Writing Schematron Rules for Internal Cross-References**

In manuscript studies, a digital edition is an interconnected network of cross-references. Scribes identified in `<respStmt>` are referenced in `<change>` logs; scribal hands defined in `<handDesc>` are referenced in transcription lines; and cited witnesses are referenced in the critical apparatus.

A Schematron schema consists of `<pattern>` containers holding `<rule>` elements with `@context` attributes. Inside each rule, one or more `<assert>` or `<report>` statements test boolean XPath expressions:

```xml
<schema xmlns="http://purl.oclc.org/dsdl/schematron">
  <ns prefix="tei" uri="http://www.tei-c.org/ns/1.0"/>
  
  <!-- Pattern 1: Verify hand references in text match defined handNotes -->
  <pattern id="handRefCheck">
    <rule context="tei:add[@hand]">
      <assert test="substring(@hand, 2) = //tei:handNote/@xml:id">
        The hand reference <value-of select="@hand"/> does not correspond to any defined tei:handNote @xml:id in this document.
      </assert>
    </rule>
  </pattern>

  <!-- Pattern 2: Enforce mandatory locus coordinates inside msItem -->
  <pattern id="locusCheck">
    <rule context="tei:msItem">
      <assert test="tei:locus[@from and @to]">
        Every tei:msItem must contain a tei:locus element with both @from and @to attributes.
      </assert>
    </rule>
  </pattern>
</schema>
```

When Oxygen executes this Schematron schema alongside RELAX NG, it checks every `<add>` tag in real time. If an encoder types `<add hand="#h4">` when only hands `#h1`, `#h2`, and `#h3` are defined in the header, Oxygen flags a custom, human-readable Schematron error, preventing broken pointers from reaching publication.

Writing project-specific Schematron rules allows editorial teams to automate quality assurance, freeing human editors from manually checking thousands of internal cross-references.

**Takeaway:** Schematron uses XPath assertions to audit internal cross-references and enforce mandatory editorial rules across the entire TEI document.

---

## **08 Content**

**Customizing the TEI: The ODD (One Document Does-It-All) Architecture**

The official TEI P5 Guidelines define over 500 distinct elements and hundreds of attributes (TEI Consortium, 2025). No single digital project ever uses all 500 elements. A manuscript cataloguing project requires deep physical description tags (`<collation>`, `<bindingDesc>`) but has no use for linguistic treebank elements or modern verse stanza tags.

To manage this complexity, the TEI community created the ODD (One Document Does-it-all) meta-schema architecture (Cummings, 2018). An ODD file is itself a TEI XML document that defines a customized subset of the TEI. In an ODD file, an editorial project declares:

- Which TEI modules are included (e.g., `msdescription`, `header`, `core`, `textstructure`).
- Which specific elements from those modules are retained or deleted.
- Which attributes are mandatory, optional, or prohibited on each element.
- Custom Schematron business rules tailored to the project's specific manuscript corpus.
- Human-readable prose explaining the project's editorial philosophy and cataloguing manual.

From this single ODD source of truth, automated compilers (such as the TEI `roma` or `oxgarage` tools) simultaneously generate the machine-actionable RELAX NG schema (`.rng`), the Schematron file (`.sch`), and the formatted HTML documentation and user manuals for project encoders (Cummings, 2018).

This unified compilation guarantees that documentation and validation schemas never drift out of sync: any change to the ODD file automatically updates both the validation rules and the project's published encoding guidelines.

**Takeaway:** The TEI ODD architecture generates project-specific RELAX NG schemas, Schematron rules, and human-readable documentation from a single XML source of truth.

---

## **09 Content**

**Case Study: The Bodleian `msdesc.odd` Consolidated Schema**

To understand how ODD customization works in major institutional archives, consider the Bodleian Library at the University of Oxford. The Bodleian preserves tens of thousands of medieval, early modern, Hebrew, Arabic, and Georgian manuscripts. Managing cataloguing data across disparate language departments required a single, uncompromising structural framework (Cummings, 2018).

The Bodleian developed a consolidated ODD schema named `msdesc.odd`, maintained publicly on GitHub (Cummings, 2018). This ODD customization includes the TEI `msdescription` module while stripping out hundreds of non-manuscript elements. Crucially, it introduces strict Schematron rules to enforce Oxford cataloguing standards:

```xml
<!-- Excerpt of Bodleian msdesc.odd Schematron constraint -->
<constraint>
  <sch:rule context="tei:msDesc">
    <sch:assert test="tei:msIdentifier/tei:idno">
      A manuscript description must have an institutional shelfmark in tei:idno.
    </sch:assert>
    <sch:assert test="tei:physDesc/tei:objectDesc/tei:supportDesc/@material">
      The support material attribute is mandatory on tei:supportDesc.
    </sch:assert>
  </sch:rule>
</constraint>
```

By publishing this schema in a version-controlled GitHub repository, the Bodleian allows cataloguers, postdocs, and external collaborators to validate their XML records locally in Oxygen before submitting pull requests. The automated continuous integration pipeline tests every submitted file against `msdesc.odd`, guaranteeing zero cataloguing drift across decades of archival work.

This institutional workflow demonstrates how customized schemas bridge the gap between individual scholarly cataloguers and massive institutional repositories.

**Takeaway:** Institutional repositories like the Bodleian Library use customized ODD schemas to enforce mandatory cataloguing constraints across diverse historical collections.

---

## **10 Content**

**Case Study: Bibliotheca Laureshamensis and the ENRICH Schema**

A premier exemplar of schema-driven digital reunification is the *Bibliotheca Laureshamensis – digital* project (Büttner & Kautz, 2013). During the early Middle Ages, the Benedictine Abbey of Lorsch was one of the greatest intellectual and manuscript production centers of the Carolingian Empire. However, across centuries of war, Reformation secularization, and library sales, its magnificent collection was completely dispersed. Today, the 331 surviving Lorsch manuscripts and fragments reside in 73 independent libraries across 13 nations (Büttner & Kautz, 2013).

To digitally reconstruct this lost Carolingian library, the project deployed the TEI ENRICH schema—a specialized, highly constrained profile of the TEI manuscript description guidelines designed specifically for medieval European codices (Büttner & Kautz, 2013).

Contributing archivists from Rome, London, Paris, Vienna, and Heidelberg generated ENRICH-conformant XML descriptions for their respective holdings. When XML files were uploaded to the central project repository, an automated Subversion/Git hook immediately validated every record against the ENRICH RELAX NG schema (Büttner & Kautz, 2013). Documents containing illegal tags, missing foliation records, or broken provenance structures were automatically rejected at the server gate.

The success of the Bibliotheca Laureshamensis demonstrated that a shared, deterministic schema can transcend international borders, language barriers, and institutional silos to digitally resurrect a destroyed historical library (Büttner & Kautz, 2013).

**Takeaway:** The Bibliotheca Laureshamensis virtually reunited 331 dispersed Carolingian manuscripts across 73 institutions by using the TEI ENRICH schema as an automated validation gate.

---

## **11 Content**

**The Limits of Document Isolation: Why XML Needs Linked Open Data**

While a valid TEI document achieves internal structural perfection, it remains an isolated digital island if it cannot communicate with the wider world. An XML file saved on a local hard drive or hosted on an institutional web server is an isolated data silo (Koho et al., 2021).

Consider how a traditional TEI document records entities:

```xml
<origin>
  <origPlace>Alexandria</origPlace>
  <origDate>575</origDate>
  <persName>Cyril of Alexandria</persName>
</origin>
```

To a computer, the string `"Alexandria"` is merely ten Unicode characters. The machine does not know whether `"Alexandria"` refers to Alexandria in Egypt, Alexandria in Virginia, or Alexandria in Scotland. It cannot automatically cross-reference this record with archaeological databases, geographic coordinate systems, or historical gazetteers. If another cataloguer encodes `"Alexandrie"` in French or `"al-Iskandariyya"` in Arabic, a database treats these as three entirely unrelated entities (Koho et al., 2021).

To transform static XML documents into active participants in global scholarly networks, digital humanists integrate the principles of Linked Open Data (LOD) and the Resource Description Framework (RDF) (Koho et al., 2021; Koho et al., 2023). Linking local textual assertions to global authority URIs ensures that our digital editions become searchable nodes within the wider Semantic Web.

**Takeaway:** Unlinked XML documents remain isolated textual silos; Linked Open Data connects local strings to global semantic authorities, enabling automated cross-institutional computation.

---

## **12 Content**

**The Resource Description Framework (RDF) and Semantic Triples**

The Resource Description Framework (RDF) is the core standard of the Semantic Web, maintained by the World Wide Web Consortium (W3C). While XML models data as a hierarchical *tree* of nested nodes, RDF models all knowledge as a directed, labeled *graph* composed of semantic triples (Koho et al., 2021; Koho et al., 2023).

An RDF triple consists of three components:

1. **Subject:** The entity being described, identified by a unique, persistent Uniform Resource Identifier (URI).
2. **Predicate:** The property, relationship, or attribute linking the subject to the object, also identified by a URI defined in a formal ontology.
3. **Object:** The value or related entity, which can be another URI (creating a graph link) or a literal string/number.

```
Subject (URI)                               Predicate (URI)                   Object (URI / Literal)
---------------------------------------------------------------------------------------------------------
<http://ldf.fi/schema/mmm/Vat_gr_2125>      crm:P108_was_produced_by          <http://ldf.fi/schema/mmm/Event_E01>
<http://ldf.fi/schema/mmm/Event_E01>        crm:P4_has_time-span              <http://vocab.getty.edu/aat/300404495>
<http://ldf.fi/schema/mmm/Event_E01>        crm:P7_took_place_at              <https://pleiades.stoa.org/places/727070>
```

In this graph architecture, knowledge is not confined to a single document. Triples from thousands of independent libraries can be aggregated into a single centralized knowledge graph and queried simultaneously using SPARQL (the standard query language for RDF) (Koho et al., 2023).

Graph-based data structures allow scholars to uncover non-linear historical connections—such as identifying all manuscripts illuminated by the same workshop that subsequently passed through the hands of the same Renaissance collector.

**Takeaway:** RDF models information as Subject-Predicate-Object triples, weaving disparate manuscript descriptions into a globally queryable semantic knowledge graph.

---

## **13 Content**

**From Strings to Things: Authority Control in TEI Markup**

The transition from textual strings to semantic graph nodes is encapsulated in the digital humanities slogan: **"Move from strings to things."** In a digital edition, we do not merely type the name of a person or place; we attach a persistent URI that identifies the actual historical entity (Koho et al., 2021).

The TEI provides standardized attributes—most notably `@ref` and `@corresp`—on names, places, dates, and materials to embed RDF URIs directly inside XML markup:

```xml
<p>Written on 
  <material ref="http://vocab.getty.edu/aat/300014224">parchment</material> 
  in 
  <placeName ref="https://pleiades.stoa.org/places/727070">Alexandria</placeName> 
  under the patronage of 
  <persName ref="https://viaf.org/viaf/88890041">René Marchal</persName>.
</p>
```

When a search indexer or RDF extraction pipeline processes this XML snippet, it does not rely on text matching. It resolves the URI `http://vocab.getty.edu/aat/300014224` to the Getty Art & Architecture Thesaurus concept for "parchment," the Pleiades URI `727070` to ancient Alexandria (with exact latitude/longitude coordinates), and the VIAF URI `88890041` to the specific historical person of Abbot René Marchal (Koho et al., 2021).

By disambiguating entities via URIs, digital editions ensure that spelling variations, dialectal shifts, and language differences no longer obstruct computational discovery.

**Takeaway:** Embedding persistent URIs in TEI `@ref` attributes transitions editions from ambiguous text strings to unambiguous, machine-resolvable entities.

---

## **14 Content**

**Global Authority Registers: VIAF, Getty TGN, Getty AAT, and Wikidata**

To make linked data effective, scholars do not invent arbitrary URIs; they link to established, globally maintained authority registers (Koho et al., 2021; Koho et al., 2023).

The primary authority registers in digital manuscript studies include:

- **Virtual International Authority File (VIAF):** Combines authority files from over 40 national libraries worldwide, establishing authoritative identifiers for historical authors, scribes, and collectors (e.g., `viaf.org/viaf/34454471` for Origen of Alexandria).
- **Getty Thesaurus of Geographic Names (TGN):** Provides hierarchical, georeferenced identifiers for historical and modern settlements, regions, and nations.
- **Getty Art & Architecture Thesaurus (AAT):** Provides standardized terminology for physical supports (`parchment`, `papyrus`), scripts (`uncial`, `Caroline minuscule`), and binding styles.
- **Pleiades Gazetteer of the Ancient World:** Provides historical coordinates, names, and temporal spans for ancient Mediterranean and Near Eastern locations.
- **Wikidata:** The world's largest open, multilingual knowledge base, providing Q-identifiers for historical figures, texts, institutions, and concepts (e.g., `Q112260` for Codex Marchalianus) (Koho et al., 2023).

| Authority Register | Primary Domain | Example Identifier | Resolved Entity |
| --- | --- | --- | --- |
| VIAF | Persons & Organizations | `viaf.org/viaf/88890041` | René Marchal (Abbot of Saint-Nom) |
| Getty TGN | Geographic Places | `vocab.getty.edu/tgn/7001303` | Rome (Italy) |
| Getty AAT | Materials & Techniques | `vocab.getty.edu/aat/300014224` | Parchment (material) |
| Pleiades | Ancient Mediterranean Geography | `pleiades.stoa.org/places/727070` | Alexandria (Egypt) |
| Wikidata | General Cultural Entities | `wikidata.org/entity/Q112260` | Codex Marchalianus (Q) |

Using these established authority registers ensures that our digital metadata is immediately compatible with international museum and library data infrastructures.

**Takeaway:** Linking to centralized authority registers like VIAF, Getty TGN/AAT, Pleiades, and Wikidata ensures that entities are globally disambiguated and machine-linked.

---

## **15 Content**

**Mapping Manuscript Migrations (MMM): Harmonizing Heterogeneous Data**

The transformative power of Linked Open Data is best demonstrated by the *Mapping Manuscript Migrations* (MMM) project (Koho et al., 2021; Koho et al., 2023). MMM brought together three massive, historically heterogeneous manuscript databases:

1. **Schoenberg Database of Manuscripts (SDBM):** Developed at the University of Pennsylvania, recording over 250,000 historical "observations" of manuscripts appearing in auction and sales catalogues across centuries.
2. **Bibale:** Developed by the IRHT in Paris, tracking the provenance and ownership histories of medieval collections.
3. **Medieval Manuscripts in Oxford Libraries:** Deeply structured TEI-XML descriptions of individual physical codices in Oxford collections (Koho et al., 2021).

These three sources had fundamentally incompatible data structures: SDBM modeled transaction events; Bibale modeled institutional collections; and Oxford modeled physical books.

Using an event-centric CIDOC-CRM and FRBRoo ontology, MMM harmonized all three datasets into a unified RDF knowledge graph containing over 20 million triples (Koho et al., 2021; Le Bœuf, 2012). Researchers can now write SPARQL queries that trace how a single manuscript moved from a 12th-century French abbey, through 18th-century private auctions in London, into a 20th-century American university library (Koho et al., 2021).

The MMM project proves that semantic web ontologies can bridge the gap between disparate archival traditions without erasing the unique local histories of individual collections.

**Takeaway:** Mapping Manuscript Migrations harmonized 20 million triples across SDBM, Bibale, and Oxford TEI files, proving that event-centric RDF models can unify heterogeneous institutional databases.

---

## **16 Content**

**Wikibase as a Knowledge Graph Platform for Codicology**

In recent years, the digital humanities community has embraced Wikibase—the open-source software engine that powers Wikidata—as a collaborative platform for hosting manuscript knowledge graphs (Koho et al., 2023).

Wikibase structures all data as *Items* (designated by `Q` numbers) and *Properties* (designated by `P` numbers). An Item represents an entity (e.g., `Q42: Codex Marchalianus`), while Properties represent predicates (e.g., `P14: held in repository`, `P22: material support`, `P35: date of origin`).

To ingest heterogeneous manuscript metadata into Wikibase, projects utilize reconciliation workflows in OpenRefine (Koho et al., 2023). Disparate text strings from library catalogues are matched algorithmically against existing Wikidata and VIAF entities, assigning high-confidence URI matches and flagging ambiguous names for human review. Once populated, a Wikibase instance provides a built-in SPARQL endpoint, visual graph exploration tools, and a REST API, democratizing access to complex Linked Open Data (Koho et al., 2023).

| Wikibase Subject Item | Predicate Property | Object Target / Value | Codicological Interpretation |
| --- | --- | --- | --- |
| `Q112260` (Codex Marchalianus) | `P14` (held in repository) | `Q213878` (Biblioteca Apostolica Vaticana) | Physical institutional custody |
| `Q112260` (Codex Marchalianus) | `P22` (material support) | `Q226697` (Parchment) | Codicological medium |
| `Q112260` (Codex Marchalianus) | `P35` (date of origin) | `"0550-0600"` (ISO 8601 Interval) | Chronological manufacturing span |
| `Q112260` (Codex Marchalianus) | `P48` (contains text) | `Q665274` (Book of Isaiah - Septuagint) | Intellectual work content |

**Takeaway:** Wikibase provides an accessible, graph-native platform for hosting manuscript data, combining OpenRefine entity reconciliation with SPARQL querying capabilities.

---

## **17 Content**

**Factoid Prosopography in Syriaca.org and the SPEAR Project**

A sophisticated application of TEI and Linked Data is *factoid prosopography*, exemplified by the Syriac Persons, Events, and Relations (SPEAR) project within the Syriaca.org ecosystem (Berti, 2016).

Traditional prosopography attempts to write a unified, synthesized biographical narrative about a historical figure. Factoid prosopography, conversely, encodes discrete "factoids"—isolated assertions made by specific primary source texts, without deciding in advance whether those assertions are historically true (Berti, 2016).

When a 7th-century Syriac chronicle asserts that "Bishop Severus traveled to Antioch in 512 CE," SPEAR uses a customized TEI ODD schema to encode this claim as an event. The encoder links the person (`Severus`), the location (`Antioch`), and the date (`512`) to Syriaca.org RDF authority URIs. Furthermore, the encoding embeds a Canonical Text Services (CTS) URN pointing directly to the specific line of the Syriac chronicle that makes the assertion (Berti, 2016).

This architecture creates a completely verifiable, machine-actionable chain of evidence: an abstract historical claim in a knowledge graph points to a URI, which is justified by a CTS URN, which resolves to an exact word in a primary manuscript witness (Berti, 2016). Factoid prosopography ensures that contradictory historical assertions can be modeled transparently without editorial bias.

**Takeaway:** The SPEAR project demonstrates factoid prosopography by linking TEI event tags to RDF authority files, with every historical assertion justified by an exact CTS URN.

---

## **18 Content**

**The Crisis of Brittle Citations: Why Web URLs Fail Scholarship**

In traditional print scholarship, classical and biblical philologists cite texts using canonical division systems: *Iliad* 1.1, *Romans* 3:23, or *Republic* 514a. These citations are permanent; they do not depend on which printing house manufactured the physical book you hold.

When humanities scholarship moved to the web in the 1990s, this citation stability was catastrophically undermined. Projects began citing web URLs (e.g., `http://example.org/texts/greek/iliad_book1.html`). Web URLs, however, are inherently brittle:

- **Link Rot:** Server domains expire, institutional paths change, and projects lose funding, rendering URLs dead within years (Smith, 2009; Blackwell & Smith, 2019).
- **Technology Dependence:** A URL points to a specific server implementation (e.g., a `.php` script or `.html` file) rather than the abstract intellectual text.
- **Granularity Collapse:** Standard URLs cannot address specific word tokens, apparatus variants, or physical manuscript bounding boxes without platform-dependent URL parameters (Blackwell & Smith, 2019).

To restore canonical citation stability to digital textual scholarship, Christopher Blackwell and Neel Smith developed the Canonical Text Services (CTS) protocol and the broader CITE Architecture (Blackwell & Smith, 2019; Smith, 2009).

**Takeaway:** Web URLs suffer from link rot and technology dependence; digital textual scholarship requires domain-independent, canonical citation protocols.

---

## **19 Content**

**The CITE Architecture and the OHCO2 Text Model**

The Canonical Text Services (CTS) standard is built upon a fundamental theoretical foundation known as the **OHCO2 model** (Ordered Hierarchy of Content Objects) (Blackwell & Smith, 2019; Smith, 2009).

The OHCO2 model asserts that a text is not a sequence of physical printed pages, nor a collection of digital pixel grids. A text is an abstract, hierarchical tree of citable intellectual nodes: Books contain Chapters, Chapters contain Sections, and Sections contain Lines or Words (Blackwell & Smith, 2019; Tiepmar & Heyer, 2014).

Within the CITE (Collections, Indices, Texts, Extensions) Architecture, citation identifiers are modeled as Uniform Resource Names (URNs). Unlike Uniform Resource Locators (URLs), which specify *where* a file is currently hosted, a URN specifies *what* an intellectual object is, independently of any server, network protocol, or physical medium (Blackwell & Smith, 2019).

```
Traditional URL (Brittle, Server-Bound):
https://library.vatican.va/digitized/vat_gr_2125/viewer.html?folio=62r&zoom=3

CITE Architecture URN (Persistent, Abstract, Canonical):
urn:cts:greekLit:tlg0527.tlg001.perseus-grc1:1.1
urn:cite2:hmt:va_images.v1:VA062RN_0062
```

By decoupling citation identity from web storage locations, the CITE architecture ensures that digital scholarly citations remain valid for centuries, outlasting transient servers and institutional re-organizations (Blackwell & Smith, 2019).

**Takeaway:** The CITE Architecture models texts as abstract citation trees (OHCO2), using persistent URNs to identify texts and artifacts independently of physical servers.

---

## **20 Content**

**Anatomy of the Canonical Text Services (CTS) URN**

A Canonical Text Services (CTS) URN is a strictly formalized, colon-delimited string that uniquely identifies any text, edition, translation, or passage across the entirety of world literature (Blackwell & Smith, 2019; Tiepmar & Heyer, 2014).

Every valid CTS URN conforms to a rigid hierarchical structure:

`urn:cts:NAMESPACE:WORK_IDENTIFIER:PASSAGE_COMPONENT`

The `WORK_IDENTIFIER` is divided into three to four period-delimited segments:

`TEXTGROUP.WORK.VERSION.EXEMPLAR`

```
urn:cts:greekLit:tlg0527.tlg001.perseus-grc1:1.1
^       ^        ^       ^      ^            ^
Scheme  Domain   Group   Work   Version      Passage
```

| Component | Example Segment | Semantic Meaning | Structural Function |
| --- | --- | --- | --- |
| Scheme & Protocol | `urn:cts:` | Declares the string as a CTS canonical identifier | Enforces CITE architecture compliance |
| Namespace | `greekLit` | Authoritative authority domain | Governs the collection namespace |
| Textgroup | `tlg0527` | Author or thematic corpus | Septuagint Old Greek Corpus |
| Work | `tlg001` | Specific intellectual work | Book of Isaiah |
| Version (Optional) | `vat-gr-2125` | Specific manuscript witness or edition | Codex Marchalianus text layer |
| Exemplar (Optional)| `diplomatic` | Distinct physical copy or editorial layer | Diplomatic transcription layer |
| Passage (Optional) | `1.1` | Hierarchical passage address | Chapter 1, Verse 1 |

**Takeaway:** A CTS URN decomposes text identification into a rigorous hierarchy: protocol, namespace, textgroup, work, version, exemplar, and passage.

---

## **21 Content**

**Granular Passage Addressing in CTS URNs**

The power of the CTS URN syntax lies in its ability to address texts at varying levels of abstraction and granular precision (Blackwell & Smith, 2019; Smith, 2009).

A scholar can cite an entire literary work, a specific chapter, a single line, or a passage range across chapters, simply by modifying the passage component:

- **Work-Level Citation:** `urn:cts:greekLit:tlg0527.tlg001` (Cites the abstract Book of Isaiah across all editions and translations).
- **Specific Witness Citation:** `urn:cts:greekLit:tlg0527.tlg001.vat-gr-2125` (Cites the specific manifestation of Isaiah preserved in Codex Marchalianus).
- **Single Node Citation:** `urn:cts:greekLit:tlg0527.tlg001.vat-gr-2125:1.2` (Cites Chapter 1, Verse 2 in Codex Marchalianus).
- **Passage Range Citation:** `urn:cts:greekLit:tlg0527.tlg001.vat-gr-2125:1.1-1.5` (Cites the continuous passage from Chapter 1 Verse 1 through Chapter 1 Verse 5).

Because the CTS citation hierarchy reflects the conceptual structure of the work rather than physical line breaks, a CTS-aware application can retrieve the exact corresponding Greek text, English translation, and Latin Vulgate parallel simultaneously for any valid URN (Tiepmar & Heyer, 2014).

This hierarchical addressing enables seamless navigation across comparative digital editions, allowing users to zoom out to whole books or zoom in to single verses dynamically.

**Takeaway:** CTS URNs support flexible granularity, enabling seamless citations from overarching works down to specific verses and continuous passage ranges.

---

## **22 Content**

**Sub-Reference Syntax and String Indexing**

Textual criticism requires even greater precision than verse-level citation. When recording a variant reading in a critical apparatus or commenting on a scribal correction, an editor must cite a specific word, character, or repeated term within a verse (Blackwell & Smith, 2019).

The CTS specification provides a standardized **sub-reference syntax** using the `@` symbol:

`PASSAGE@TOKEN[INDEX]`

Consider Isaiah 1:2: *«ἄκουε οὐρανὲ καὶ ἐνωτίζου γῆ ὅτι κύριος ἐλάλησεν...»*

- **Single Word Target:** `urn:cts:greekLit:tlg0527.tlg001.vat-gr-2125:1.2@οὐρανὲ` (Isolates the word *οὐρανὲ* in verse 2).
- **Disambiguating Repeated Words:** If the word *καὶ* occurs four times in verse 2, `@καὶ[2]` targets the second instance of *καὶ*.
- **Sub-Token Character Offsets:** `urn:cts:greekLit:tlg0527.tlg001.vat-gr-2125:1.2@ἐνωτίζου[1,1-4]` (Isolates the first four characters *ἐνωτ-* of the word *ἐνωτίζου*).
- **Sub-Reference Range:** `urn:cts:greekLit:tlg0527.tlg001.vat-gr-2125:1.2@οὐρανὲ-1.2@γῆ` (Cites the exact substring from *οὐρανὲ* through *γῆ*).

This sub-reference syntax allows digital critical apparatuses and factoid databases to target exact paleographical tokens without adding invasive XML markup to the base transcription (Blackwell & Smith, 2019; Berti, 2016).

**Takeaway:** CTS sub-reference syntax (`@token[index]`) enables mathematical citation of specific words, repeated tokens, and character substrings within a passage.

---

## **23 Content**

**CITE URNs for Non-Textual Artifacts: Folios, Images, and Papyri**

While CTS URNs address abstract textual hierarchies, digital editions also encompass physical artifacts: manuscript folios, papyrus fragments, physical inscriptions, and high-resolution digital images. The broader CITE Architecture provides the **CITE2 URN** protocol for non-textual cultural objects (Blackwell & Smith, 2019; Babeu, 2019).

A CITE2 URN identifies objects within structured collections:

`urn:cite2:NAMESPACE:COLLECTION.VERSION:OBJECT_ID`

```
Manuscript Folio Object:
urn:cite2:hmt:msA.v1:62r

High-Resolution IIIF Image:
urn:cite2:hmt:va_images.v1:VA062RN_0062

Image Region of Interest (Bounding Box Coordinates):
urn:cite2:hmt:va_images.v1:VA062RN_0062@0.15,0.22,0.60,0.18
```

By pairing CTS URNs (identifying the text) with CITE2 URNs (identifying the image and physical leaf), a digital scholarly edition establishes a complete, bi-directional alignment between the transcribed words, the physical parchment folio, and the digital facsimile pixels (Blackwell & Smith, 2019; Babeu, 2019).

This alignment allows users to click on any word in a digital critical edition and immediately highlight the exact pixels on the high-resolution manuscript image where the scribe wrote that word.

**Takeaway:** CITE2 URNs identify physical manuscript folios and high-resolution images, linking textual transcriptions directly to visual facsimiles.

---

## **24 Content**

**The Linked Fragment: Citing Lost Authors and Textual Reuses**

A profound challenge in classical philology is encoding *fragments*—lost historical texts that survive only as brief quotations, paraphrases, or allusions preserved within the surviving works of later authors (Berti, 2016).

In traditional print editions (such as Felix Jacoby's *Fragmente der griechischen Historiker*), editors printed reconstructed fragments in isolation, severing them from their physical host contexts. In digital philology, Monica Berti demonstrates that CTS URNs and TEI XML allow scholars to represent the "linked fragment" with total contextual fidelity (Berti, 2016).

Using TEI `<cit>` markup paired with CTS URNs, an editor records both the citing host text and the cited lost author:

```xml
<cit>
  <quote>
    <!-- Text of the lost fragment as quoted by the host author -->
    <w ref="urn:cts:greekLit:tlg0016.tlg001:1.10">...</w>
  </quote>
  <bibl>
    <author ref="https://viaf.org/viaf/100189914">Hecataeus of Miletus</author>
    <title ref="urn:cts:greekLit:tlg0592.tlg001">Genealogiai</title>
    <citedRange>Frag. 15</citedRange>
  </bibl>
</cit>
```

This architecture ensures that a fragment is never ripped from its manuscript host; the CTS URN anchors the quote to its exact place in the surviving witness while simultaneously connecting it to the author's virtual collected works (Berti, 2016).

**Takeaway:** CTS URNs and TEI `<cit>` elements model fragmentary text reuses, preserving the physical host context while linking citations to lost works.

---

## **25 Content**

**CTS Implementations and Web Microservices**

A persistent URN is an abstract identifier; to be useful to human researchers, it must be resolved into actual digital data. This resolution is handled by Canonical Text Services web microservices (Tiepmar & Heyer, 2014).

A CTS service is an API that accepts standardized HTTP requests and returns structured XML or JSON responses. The CTS specification defines five mandatory request verbs (Tiepmar & Heyer, 2014):

1. `GetCapabilities`: Returns an inventory of all textgroups, works, editions, and translations available on the server.
2. `GetValidReff`: Returns a list of all valid passage URNs within a given text or range.
3. `GetPassage`: Returns the transcribed TEI XML text for a specific passage URN.
4. `GetPassagePlus`: Returns the passage text along with preceding and following passage citations for navigation.
5. `GetFirstUrn` / `GetPrevNextUrn`: Navigates linearly across the citation tree.

```
Example HTTP CTS API Request:
https://cts.perseids.org/api/cts?request=GetPassage&urn=urn:cts:greekLit:tlg0527.tlg001.perseus-grc1:1.1

Server Response:
<GetPassage>
  <request><urn>urn:cts:greekLit:tlg0527.tlg001.perseus-grc1:1.1</urn></request>
  <reply>
    <passage>
      <TEI xmlns="http://www.tei-c.org/ns/1.0">
        <div type="edition" n="urn:cts:greekLit:tlg0527.tlg001.perseus-grc1">
          <div type="textpart" subtype="chapter" n="1">
            <div type="textpart" subtype="verse" n="1">
              <p>ΟΡΑΣΙΣ ΗΝ ΕΙΔΕΝ ΗΣΑΙΑΣ ΥΙΟΣ ΑΜΩΣ...</p>
            </div>
          </div>
        </div>
      </TEI>
    </passage>
  </reply>
</GetPassage>
```

Because CTS services speak a standardized protocol, a client application can pull Greek texts from Leipzig, Latin texts from Harvard, and Syriac texts from Oxford into a single unified collation interface (Tiepmar & Heyer, 2014).

**Takeaway:** CTS web microservices expose standardized API endpoints (`GetPassage`, `GetValidReff`) that resolve abstract URNs into structured XML text fragments.

---

## **26 Content**

**Integrating CTS URNs into the `<teiHeader>` and Body**

To ensure that your digital edition is fully CTS-compliant, you must embed canonical identifiers directly into your TEI Header and structural text body.

In the `<teiHeader>`, the `<msItem>` and `<title>` elements declare the canonical work identifier via the `@ref` attribute. In the `<body>` of the document, each hierarchical division (`<div>`) declares its structural subtype and canonical citation number (`@n`):

```xml
<teiHeader>
  <fileDesc>
    <sourceDesc>
      <msDesc>
        <msContents>
          <msItem n="2">
            <title ref="urn:cts:greekLit:tlg0527.tlg001">Book of Isaiah</title>
          </msItem>
        </msContents>
      </msDesc>
    </sourceDesc>
  </fileDesc>
</teiHeader>

<text>
  <body xml:lang="grc" n="urn:cts:greekLit:tlg0527.tlg001.vat-gr-2125">
    <div type="textpart" subtype="book" n="1">
      <div type="textpart" subtype="chapter" n="1">
        <div type="textpart" subtype="verse" n="1">
          <p>ΟΡΑΣΙΣ ΗΝ ΕΙΔΕΝ ΗΣΑΙΑΣ ΥΙΟΣ ΑΜΩΣ...</p>
        </div>
        <div type="textpart" subtype="verse" n="2">
          <p>ΑΚΟΥΕ ΟΥΡΑΝΕ ΚΑΙ ΕΝΩΤΙΖΟΥ ΓΗ...</p>
        </div>
      </div>
    </div>
  </body>
</text>
```

By nesting `<div type="textpart" subtype="chapter" n="1">` and `<div type="textpart" subtype="verse" n="1">`, your XML tree mirrors the exact OHCO2 citation hierarchy, allowing automated CTS scrapers to harvest your text without manual configuration.

This alignment ensures that your edition can participate directly in distributed text service networks, automated alignment engines, and multi-witness collation pipelines.

**Takeaway:** Embedding CTS URNs in `<msItem>` and structural `<div type="textpart">` elements aligns the TEI XML tree with the canonical citation hierarchy.

---

## **27 Content**

**Hands-On: Validating and Enriching the Primary Witness Header**

Now we execute the core practical work of Meeting #4. You will take yesterday's hand-written XML file (`03a_Lesson_2.1_Primary_Witness_Header.xml`), open it in Oxygen XML Editor, and execute a complete deterministic validation and linked data audit.

Follow these systematic steps:

1. **Schema Association:** Verify that the `<?xml-model?>` processing instructions for the TEI consolidated RELAX NG schema and Schematron rules are active at the top of your file.
2. **Grammar Validation:** Run the Oxygen validator (`Validate Document` / `Ctrl+Shift+V` or `Cmd+Shift+V`). Inspect the error log:
   - Fix all invalid element nesting (e.g., ensure `<supportDesc>` is inside `<objectDesc>`).
   - Correct all non-standard date strings into ISO 8601 format (`YYYY-MM-DD` or `YYYY`).
   - Fix all capitalization and entity escape errors.
3. **Cross-Reference Auditing:** Run the Schematron audit:
   - Ensure all `@hand` pointers (e.g., `#h1`) correspond to valid `<handNote xml:id="h1">` declarations.
   - Verify that all `<msItem>` elements contain valid `<locus>` foliation coordinates.
4. **Linked Data Enrichment:**
   - Attach VIAF URIs to all historical authors, editors, and scribes (`<persName ref="...">`).
   - Attach Getty TGN or Pleiades URIs to your manuscript's place of origin and current settlement (`<placeName ref="...">`).
   - Attach Getty AAT URIs to physical support materials (`<material ref="...">`).
   - Assign the canonical CTS URN to your primary work in `<msItem>` and `<body>`.

Save your validated file as `src/modules/Topic_02_Cataloguing/03a_Lesson_2.2_Primary_Witness_Header_Validated.xml`.

**Takeaway:** The validation lab transforms raw manual markup into a certified, schema-valid, linked-data-enriched digital manuscript record.

---

## **28 Content**

**Extracting RDF Triples from TEI via XSLT and SPARQL**

Once a TEI Header is validated and enriched with URIs, it can be automatically converted into RDF semantic triples. This transformation is typically executed using XSLT (Extensible Stylesheet Language Transformations) stylesheets (Koho et al., 2021).

An XSLT script traverses the validated TEI XML tree, matches `<msDesc>`, `<origin>`, and `<persName>` elements, and outputs standard RDF/XML or Turtle syntax:

```xml
<!-- Conceptual XSLT Rule for Generating RDF Triples from TEI -->
<xsl:template match="tei:msDesc">
  <rdf:Description rdf:about="http://example.org/manuscript/{@xml:id}">
    <rdf:type rdf:resource="http://erlangen-crm.org/current/E22_Man-Made_Object"/>
    <crm:P1_is_identified_by>
      <xsl:value-of select="tei:msIdentifier/tei:idno"/>
    </crm:P1_is_identified_by>
    <crm:P46i_forms_part_of rdf:resource="{tei:msIdentifier/tei:repository/@ref}"/>
  </rdf:Description>
</xsl:template>
```

When this transformation is executed across thousands of TEI documents, the resulting RDF graphs are ingested into a triple store (such as GraphDB or Apache Jena) and queried via SPARQL:

```sparql
PREFIX crm: <http://erlangen-crm.org/current/>
PREFIX tei: <http://www.tei-c.org/ns/1.0/>

SELECT ?manuscript ?shelfmark ?place
WHERE {
  ?manuscript a crm:E22_Man-Made_Object ;
              crm:P1_is_identified_by ?shelfmark ;
              crm:P108i_was_produced_by ?production .
  ?production crm:P7_took_place_at ?place .
  FILTER (CONTAINS(STR(?place), "Alexandria"))
}
```

This query searches millions of records in seconds, demonstrating the immense analytical payoff of structured, linked metadata (Koho et al., 2021; Koho et al., 2023).

**Takeaway:** Validated TEI headers are transformed into RDF triples via XSLT, enabling lightning-fast SPARQL queries across decentralized international repositories.

---

## **29 Content**

**Auditing the Deterministic Pass: Clean Validation as the Stage Gate**

Before concluding today's deterministic session, you must verify that your enriched document passes all validation gates with **zero errors and zero warnings**.

In the RELS 398 curriculum, validation is not an optional checklist; it is an unforgiving stage gate. You cannot proceed to Friday's AI evaluation lab if your underlying ground-truth XML file contains broken trees or invalid datatypes.

Run the repository linter and schema checker from your terminal:

```bash
# Verify Git status
git status

# Stage your validated, linked TEI file
git add src/modules/Topic_02_Cataloguing/03a_Lesson_2.2_Primary_Witness_Header_Validated.xml

# Commit the deterministic milestone with an informative audit log
git commit -m "Topic 02: Validated primary witness header against RELAX NG, Schematron, and LOD authorities"
```

Document your validation results in your personal lab notes: record how many syntax errors Oxygen caught in your Tuesday draft, what types of errors they were (e.g., date formats, nesting, unclosed tags), and how you resolved them. This error log will form the quantitative baseline for Friday's comparative report.

**Takeaway:** A zero-error validation report is the mandatory stage gate that certifies your ground truth before comparative AI benchmarking.

---

## **30 Content**

**Synthesis: The Triple Infrastructure of Digital Philology**

Today's meeting has integrated the three indispensable pillars of modern digital textual scholarship:

1. **TEI XML & RELAX NG:** Provides the granular, hierarchical markup vocabulary and structural grammar to represent the complex materiality of handwritten codices (Cummings, 2018; TEI Consortium, 2025).
2. **RDF & Linked Open Data:** Connects local document strings to global semantic knowledge graphs, turning isolated files into interoperable nodes on the Semantic Web (Koho et al., 2021; Koho et al., 2023).
3. **CTS URNs & CITE Architecture:** Establishes permanent, machine-actionable, canonical citations that identify texts, passages, and manuscript folios independently of physical servers (Blackwell & Smith, 2019; Smith, 2009).

| Infrastructure Layer | Core Standard & Schema | Primary Function in Digital Scholarship | Scholarly Benefit |
| --- | --- | --- | --- |
| Codicological Markup | TEI XML / RELAX NG | Internal document grammar and manuscript description | Preserves material and paleographic nuances in machine-readable trees |
| Semantic Web Graph | RDF / Linked Open Data | Global entity reconciliation and cross-repository queries | Connects local text strings to international authority knowledge bases |
| Citation Ontology | CTS URN / CITE Architecture | Technology-independent, machine-actionable text addressing | Provides persistent, granular citations down to words and substrings |

```
Comparative Cycle Progress — Week 2 (Topic 02):
[X] Tue: Manual — Hand-written TEI Header and msDesc (Human Ground Truth)
[X] Wed: Deterministic — RELAX NG & Schematron validation in Oxygen, RDF LOD, CTS URNs
[ ] Fri: AI-Assisted — LLM metadata extraction scored against your manual baseline
```

On Friday, we complete the cycle with Step 3: AI-assisted metadata extraction. You will prompt Large Language Models and computer vision pipelines to catalogue your manuscript passage automatically, scoring their outputs directly against the validated ground truth you certified today.

**Takeaway:** TEI XML, RDF Linked Open Data, and CTS URNs form the three-part computational infrastructure that makes digital textual scholarship permanent, interoperable, and reproducible.

---

## References

Babeu, A. (2019). Digital catalogs of ancient Greek authors and works through papyrological data. In M. Berti (Ed.), *Digital Classical Philology: Ancient Greek and Latin in the Digital Revolution* (pp. 55–72). De Gruyter Saur. https://doi.org/10.1515/9783110599572

Berti, M. (2016). The linked fragment: TEI and the encoding of text reuses of lost authors. *Journal of the Text Encoding Initiative*, 8. https://doi.org/10.4000/jtei.1218

Blackwell, C., & Smith, N. (2019). The CITE Architecture: A conceptual and practical overview. In M. Berti (Ed.), *Digital Classical Philology: Ancient Greek and Latin in the Digital Revolution* (pp. 73–94). De Gruyter Saur.

Büttner, A., & Kautz, M. (2013). Bibliotheca Laureshamensis – digital: virtuelle Klosterbibliothek Lorsch. *Pergament und Stein (Lorscher Studien 2)*, 5–8.

Cummings, J. (2018). The Text Encoding Initiative and the study of literature. In R. Siemens & S. Schreibman (Eds.), *A Companion to Digital Literary Studies* (pp. 451–476). Blackwell.

Koho, M., Burrows, T., Hyvönen, E., Ikkala, E., Page, K., Ransom, L., ... & Wijsman, H. (2021). Harmonizing and publishing heterogeneous premodern manuscript metadata as Linked Open Data. *Journal of the Association for Information Science and Technology*, 73(2), 240–257. https://doi.org/10.1002/asi.24499

Koho, M., Coladangelo, L. P., Ransom, L., & Emery, D. (2023). Wikibase model for premodern manuscript metadata harmonization, linked data integration, and discovery. *ACM Journal on Computing and Cultural Heritage*, 16(3), Article 56. https://doi.org/10.1145/3594723

Le Bœuf, P. (2012). Modeling rare and unique documents: Using FRBRoo/CIDOC CRM. *Journal of Archival Organization*, 10(2), 96–106.

Smith, N. (2009). Citation in classical studies. *Digital Humanities Quarterly*, 3(1).

TEI Consortium. (2025). *TEI P5: Guidelines for Electronic Text Encoding and Interchange*. Version 4.8.0. https://tei-c.org/release/doc/tei-p5-doc/en/html/

Tiepmar, J., & Heyer, G. (2014). A new implementation for Canonical Text Services. In *Proceedings of the Workshop on Human-Computer Tractable Data for the Digital Humanities* (pp. 1–8).
