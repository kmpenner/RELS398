# Lesson 2.2 — Deterministic Schema Validation, Linked Data, and Canonical Citation

*RELS 398 / ENGL 398 · Topic 2: Cataloguing · Meeting #4 (Wed Sep 9)*

*Step 2 of the three-step cycle: deterministic computation. Yesterday you hand-wrote a complete TEI Header in VS Code without software help. Today you introduce that draft to the machine: you configure real-time schema validation in VS Code, slay the red squiggly lines, link your manuscript entities to global authority files using RDF triples, and assign Canonical Text Services (CTS) URNs. The validator is an uncompromising structural gatekeeper, turning human typing into verified, interoperable data.*

---

## **01 Content**

**The Rule of the Machine: What "Deterministic" Really Means**

Yesterday, you sat at your keyboard and made human, interpretive decisions. You looked at a high-resolution photograph of ancient parchment and decided how to describe ink colors, margin widths, and scribal handwriting in TEI XML. That was humanistic intuition at work.

Today, we meet the machine.

In digital scholarship, we call today's stage **deterministic**. A process is deterministic when identical inputs run through rule-governed algorithms produce the exact same, mathematically verifiable result every single time. There is no guessing, no mood, no statistical approximation, and no creative license. If you feed the number 2 + 2 into a calculator, it does not respond with "around 4ish" or write a poetic reflection on the nature of even numbers; it returns 4. Every time. Guaranteed.

When you validate your hand-written TEI XML document today, the software will not "interpret" your thoughts or grade you on effort. It will evaluate every single bracket, element name, attribute value, and closing slash against a strict mathematical rulebook called a **schema**. If your markup obeys the rulebook to the letter, the validator gives you a clean bill of health. If you missed a single quote mark, misspelled an element name, or put a date inside the wrong container, the validator will stop you cold. That uncompromising strictness is not your enemy; it is the quality assurance that makes digital editions durable for centuries.

**Vocabulary.** *Deterministic* — a computational process governed by explicit rules where identical inputs produce identical, mathematically verifiable outputs with zero variance. *Schema validation* — the algorithmic verification of an XML document against a formal structural rulebook.

**Takeaway:** Deterministic tools evaluate XML against unbending mathematical rules, ensuring that subjective human markup conforms to a rigorous, certified data standard.

---

## **02 Content**

**The Rulebook: How Schemas (RELAX NG) Police Your Markup**

In Lesson 1.1, you learned the difference between well-formed XML and valid XML. 

Anyone can write *well-formed* XML: as long as your tags nest properly and attribute values are wrapped in quotes, the syntax is technically correct. You could invent a tag called `<cheeseburger price="5">` or `<alienSpaceship>`, and basic XML wouldn't complain. 

But a scholarly community cannot function on made-up tags. If one scholar invents `<parchment>`, another writes `<animalSkin>`, and a third writes `<vellum>`, no search engine on Earth can connect their research. To collaborate globally, we need a shared rulebook that defines:

1. Exactly which tags are legally permitted.
2. Exactly where each tag is allowed to appear (parent-child relationships).
3. How many times an element can be repeated.
4. What format attribute values must follow (e.g., must dates look like `YYYY-MM-DD`?).

In modern digital philology, the premier schema language is **RELAX NG** (REgular LAnguage for XML Next Generation). RELAX NG treats your document as a tree structure, using regular expressions to define valid branching patterns. It is lightweight, flexible, and fully supports the massive international standard maintained by the Text Encoding Initiative (TEI).

**Vocabulary.** *Schema* — a formal machine-readable document specifying the structural rules, legal elements, and allowable attributes of an XML language. *RELAX NG (RNG)* — the schema standard used by the TEI to define document structure and grammar.

**Takeaway:** Basic XML syntax prevents computer crashes, but schemas (like RELAX NG) enforce the shared scholarly vocabulary that makes digital editions interoperable.

---

## **03 Content**

**Validating Your Hand-Written Header in VS Code**

Forget expensive, proprietary software. Today, you will perform industrial-grade XML schema validation directly inside **Visual Studio Code**.

To connect your XML file to an official online schema, you add a special processing instruction called `xml-model` at the very top of your document, immediately beneath the `<?xml version="1.0"?>` declaration:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="https://raw.githubusercontent.com/msdesc/consolidated-tei-schema/master/msdesc.rng" 
            type="application/xml" 
            schematypens="http://relaxng.org/ns/structure/1.0"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
```

When you open this file in VS Code with the right XML extension installed, the following happens automatically:

> **Install Scholarly XML, not just Red Hat XML.** These two extensions are *not* interchangeable for this step. Red Hat XML validates **DTD and XSD** schemas. TEI's `msdesc.rng` is a **RELAX NG** schema, and only **Scholarly XML** (publisher: Raff Viglianti) checks RELAX NG. If you have only Red Hat XML installed, you will see **zero errors** — not because your file is correct, but because nothing is inspecting it. A clean Problems panel from the wrong extension is a false negative, and it is the single most common way students are misled in this module.

1. VS Code reads the `xml-model` line and automatically downloads the official RELAX NG schema in the background.
2. The language server audits your document in real time as you type.
3. If an element is illegal, misspelled, or out of order, a red squiggly line appears instantly beneath the offending code.
4. The **Problems panel** at the bottom of your VS Code window (`Ctrl+Shift+M` or `Cmd+Shift+M`) gives you a line-by-line list of every defect.

You do not need to click "Compile" or upload your file to an external server. The machine gives you continuous, instant feedback.

**Vocabulary.** *`xml-model`* — an XML processing instruction that links a document directly to its validation schema and schema language. *Language server* — background software inside an editor that analyzes code in real time and reports diagnostics.

**Takeaway:** By adding an `xml-model` processing instruction in VS Code, the editor downloads the schema and validates your markup in real time with line-by-line diagnostics.

---

## **04 Content**

**Structural Rules and Element Hierarchy in RNG**

How does a RELAX NG schema actually make decisions about your text? It evaluates your document as an ordered hierarchy of containers.

Inside a schema, elements are defined with specific rules regarding their children:

- **Sequence (`<rng:group>`)**: Elements must appear in an exact chronological order. For example, inside `<fileDesc>`, TEI demands that `<titleStmt>` must come *before* `<publicationStmt>`, and `<publicationStmt>` must come *before* `<sourceDesc>`. If you flip the order, the schema flags an error!
- **Choice (`<rng:choice>`)**: You must provide one option from a set of alternatives (e.g. choose between `<p>` for prose description or `<msItem>` for structured listing).
- **Cardinality (`<rng:zeroOrMore>`, `<rng:oneOrMore>`, `<rng:optional>`)**: Governs how many times an element can appear. You can have multiple `<editor>` elements, but only one `<msIdentifier>` per manuscript description.

When you see a validation error that says *"Element 'sourceDesc' is not allowed here"*, the validator is rarely saying that `<sourceDesc>` doesn't exist. It is usually telling you that you put it in the wrong order or nested it inside the wrong parent box!

**Vocabulary.** *Sequence* — a schema constraint requiring child elements to appear in a strict, predefined order. *Cardinality* — rules defining the minimum and maximum number of times an element may legally appear within a parent container.

**Takeaway:** Schema validators check not only whether tags exist, but whether they appear in the correct sequence and within the correct parent container.

---

## **05 Content**

**Data Typing, Enumerations, and Attribute Constraints**

A schema does not just check tag names; it polices what goes *inside* those tags and attributes.

In computer science, unformatted text is called a "string". If a computer asks for a date and you type "sometime during the reign of Charlemagne, probably a chilly autumn", a human understands, but a database cannot calculate how many years passed between that event and the Norman Conquest.

Schemas enforce **datatypes**:

1. **ISO 8601 Dates**: In attributes like `when="1050"`, `notBefore="1000"`, or `notAfter="1099"`, the schema demands standard numerical formats (`YYYY` or `YYYY-MM-DD`). If you write `when="about 1050"`, validation fails.
2. **Enumerated Lists**: For certain attributes, the schema restricts you to a closed list of legal keywords. In `<supportDesc material="...">`, you must choose from authorized values like `"parchment"`, `"papyrus"`, or `"paper"`. If you type `material="animal_skin"`, the validator flags it because it violates the enumeration.
3. **URIs and URLs**: In `ref="..."` or `target="..."`, the schema checks that the value is a properly formatted web address or persistent identifier.

By enforcing strict datatypes, the schema ensures that your edition can be filtered, sorted, and calculated by automated algorithms worldwide.

**Vocabulary.** *Datatype* — a classification identifying the type of data a value can hold (e.g., integer, boolean, ISO date string). *Enumeration* — a closed, restricted set of allowable values for a specific attribute.

**Takeaway:** Schemas enforce datatypes and closed vocabulary enumerations, preventing fuzzy text from breaking automated database calculations.

---

## **06 Content**

**Beyond Grammar: The Necessity of Schematron Business Logic**

Here is a surprising truth about RELAX NG schemas: they have blind spots.

A RELAX NG schema is like an English spelling and grammar checker. It knows that *"The dog chased the cat"* is grammatically correct. But if you write *"The two-year-old child drove a commercial Boeing 747 across the Atlantic"*, the grammar checker sees no problem—subject, verb, object are all in order. It has no idea that the sentence makes no logical sense in the real world.

The same problem happens in XML. 

Suppose in your TEI Header you write:
```xml
<handDesc hands="1">
    <handNote xml:id="h1">...</handNote>
    <handNote xml:id="h2">...</handNote>
</handDesc>
```
To RELAX NG, this is valid XML. It has a `<handDesc>` containing `<handNote>` elements. But logically, you have contradicted yourself! You explicitly declared `hands="1"`, yet you immediately listed two distinct scribal hands (`h1` and `h2`)!

To catch these logical contradictions, digital editors use a complementary technology called **Schematron**. Schematron uses XPath expressions to write "business rules" that check real-world relationships across your document.

**Vocabulary.** *Schematron* — a rule-based validation language that asserts business logic, cross-element constraints, and semantic consistency in XML documents. *XPath* — a syntax used to navigate through elements and attributes in an XML document.

**Takeaway:** Grammatical schemas (RELAX NG) check tag structure, while rule-based validators (Schematron) catch real-world logical contradictions and broken cross-references.

---

## **07 Content**

**Writing Schematron Rules for Cross-References**

In your course project, one of the most powerful uses of Schematron is verifying internal cross-references.

In Lesson 2.1, you learned to give each scribal hand a unique identifier: `<handNote xml:id="h1">`. Later, in Week 4, when you transcribe text, you will link each line to that scribe using an attribute: `<line hand="#h1">`.

What happens if you accidentally type `<line hand="#h99">`?

Without Schematron, your XML might pass schema validation, but downstream software will crash because hand `#h99` does not exist! A Schematron rule prevents this by writing a simple assertion:

```xml
<pattern>
    <rule context="tei:line[@hand]">
        <assert test="substring-after(@hand, '#') = //tei:handNote/@xml:id">
            The hand reference <value-of select="@hand"/> must point to an existing handNote xml:id in the header!
        </assert>
    </rule>
</pattern>
```

If a reference breaks, Schematron prints a clear, human-readable error message in your editor: *"The hand reference #h99 must point to an existing handNote xml:id in the header!"* That is the power of automated structural auditing.

**Vocabulary.** *Cross-reference validation* — verifying that internal pointers (like `#h1`) match real identifier targets (`xml:id="h1"`) declared elsewhere in the document. *Assertion (`<assert>`)* — a Schematron test condition that triggers an error message if evaluated as false.

**Takeaway:** Schematron audits internal pointers across your document, guaranteeing that every hand, scribe, and image reference points to an existing target.

---

## **08 Content**

**Customizing the TEI: The ODD (One Document Does-It-All) Philosophy**

The complete Text Encoding Initiative Guidelines contain over 500 different elements and thousands of attributes. It covers everything from ancient Greek papyri to 19th-century poetry to speech corpora.

If you tried to validate your student manuscript against the *entire* TEI at once, it would be overwhelming. You could legally put stage directions from a Shakespeare play inside your biblical manuscript description!

To prevent this chaos, the TEI invented a design philosophy called **ODD (One Document Does-it-all)**.

An ODD file is a single master document written in TEI XML that defines a project's customized editorial profile. In an ODD file, a research team:

1. Selects only the specific TEI modules they need (e.g., `msdescription`, `textstructure`, `transcr`).
2. Deletes elements they will never use.
3. Modifies allowable attribute values to fit their corpus.
4. Writes documentation explaining *why* they chose those rules.

From this single ODD file, automated compilers generate both human-readable HTML documentation and the machine-readable RELAX NG schema (`.rng`) that polices your files!

**Vocabulary.** *ODD (One Document Does-it-all)* — the TEI format combining human-readable documentation, editorial guidelines, and machine-actionable schema specifications in a single XML source. *Subsetting* — creating a tailored profile of the TEI by including only relevant elements for a specific project.

**Takeaway:** The TEI is customized for specific projects through ODD files, which generate both human documentation and strict RELAX NG schemas from a single source.

---

## **09 Content**

**Case Study: The Bodleian `msdesc.odd` Consolidated Schema**

To see how world-class institutions use this workflow, look at the **Bodleian Libraries at the University of Oxford**.

The Bodleian holds tens of thousands of medieval and Renaissance manuscripts in dozens of languages (Greek, Latin, Arabic, Hebrew, Armenian). To catalogue these treasures consistently across hundreds of scholars, the Bodleian developed `msdesc.odd` — a consolidated manuscript description schema.

Instead of allowing cataloguers to invent whatever markup they pleased, the Bodleian schema strictly enforces:

- Standardized settlement and repository naming conventions.
- Mandatory `<supportDesc>` declarations with controlled vocabulary for parchment and paper.
- Standardized foliation formats (`f. 1r`, `f. 1v`).
- Automated linking to the Bodleian's internal digital library authority records.

The schema we link to in this course (`msdesc.rng`) is directly derived from these international consortium best practices. When your file validates against it, your work meets the exact same technical standard used by Oxford University.

**Vocabulary.** *Consolidated schema* — an institutional TEI customization that unifies cataloguing rules across large, heterogeneous archival collections. *Standardization* — adopting uniform encoding conventions across diverse manuscript traditions.

**Takeaway:** Major archives like Oxford's Bodleian Library rely on customized TEI schemas to ensure consistent cataloguing across thousands of historical manuscripts.

---

## **10 Content**

**Case Study: Bibliotheca Laureshamensis and the ENRICH Schema**

Another landmark case study in digital codicology is the **Bibliotheca Laureshamensis** (the virtual reconstruction of the medieval monastic library of Lorsch, Germany).

During the Reformation and the Thirty Years' War, the magnificent 8th-century library of Lorsch was dispersed across the globe. Today, its surviving codices are scattered across 73 libraries in 12 countries, including Heidelberg, Rome, London, and Vienna.

How do you digitally reunite a library that has been physically shattered for four centuries?

By using the **ENRICH (European Network for Research on Information and Cultural Heritage) TEI schema**. Participating libraries in Germany, the Vatican, and the UK each catalogued their physical holdings according to the shared ENRICH schema. Because the metadata was strictly valid and interoperable, a unified search portal was able to ingest XML records from 73 independent institutions and virtually assemble the entire monastic library on a single screen. That is the triumph of deterministic standards over local isolation.

**Vocabulary.** *Virtual reunification* — digitally aggregating separated leaves, quires, or entire manuscripts preserved in different global archives into a single unified scholarly resource. *Interoperability* — the ability of diverse computer systems to exchange and use data without custom conversion.

**Takeaway:** The virtual reconstruction of Lorsch Abbey demonstrates how shared XML schemas allow globally scattered manuscript collections to be digitally reunited.

---

## **11 Content**

**Breaking Out of the Silo: Why XML Needs Linked Open Data**

Validating your XML file in VS Code is a major milestone. Your file is structurally sound, grammatically clean, and internally consistent.

But it has one major limitation: **it is an isolated island**.

If your XML file says:
```xml
<origPlace>Constantinople</origPlace>
<author>John Chrysostom</author>
```
A computer knows that "Constantinople" is a place name and "John Chrysostom" is an author name. But to the computer, those words are just dumb sequences of text characters (strings). 

What if another scholar writes `<origPlace>Byzantium</origPlace>` or `<origPlace>Istanbul</origPlace>`? What if a French scholar writes `<author>Jean Chrysostome</author>`? To an automated search engine, those look like entirely different people and completely different cities!

To connect our scholarship to the rest of the world, we must move **from strings to things**. We must connect text names to permanent entities in global knowledge graphs. This is the world of **Linked Open Data (LOD)**.

**Vocabulary.** *Data silo* — an isolated repository of data that cannot easily interact with other computer systems. *Linked Open Data (LOD)* — structured data published on the web using open standards, explicitly linked to global knowledge bases.

**Takeaway:** Clean XML markup creates structured documents, but Linked Open Data connects the entities inside those documents to global knowledge networks.

---

## **12 Content**

**Speaking in Triples: The Resource Description Framework (RDF)**

How do computers express knowledge about the real world without getting confused by human language? They use **RDF (Resource Description Framework)**.

At its core, RDF is astonishingly simple. Every fact in the universe is expressed as a three-part sentence called a **triple**:

Subject -> Predicate -> Object

Think of it like basic English grammar:

- **Subject**: What are we talking about? (*This Manuscript Page*)
- **Predicate**: What is its relationship or property? (*was copied in*)
- **Object**: What is the target value? (*Constantinople*)

In RDF, however, we don't use fuzzy English words; we use permanent web addresses (URIs) for each of the three pieces:

- **Subject**: `https://digi.vatlib.it/view/MSS_Vat.gr.2121`
- **Predicate**: `http://purl.org/dc/terms/spatial`
- **Object**: `https://pleiades.stoa.org/places/520998`

When computers read this triple, there is zero ambiguity. A machine in Tokyo and a machine in Antigonish know with mathematical precision that this exact manuscript in Rome was created at the geographic coordinates of ancient Constantinople.

**Vocabulary.** *RDF (Resource Description Framework)* — a standard data model for representing information about resources on the web as semantic graphs. *Semantic triple* — a foundational knowledge statement composed of a Subject, a Predicate, and an Object.

**Takeaway:** RDF models knowledge as unambiguous three-part statements (Subject to Predicate to Object), connecting web identifiers into global knowledge graphs.

---

## **13 Content**

**From Strings to Real Things: Authority Control in TEI**

How do we embed these global Linked Data identifiers directly into our hand-authored TEI Header?

We use **authority control attributes**, primarily `ref="..."` and `key="..."`.

Look at how we transform plain text into Linked Data:

```xml
<!-- Before: plain strings with no external reference -->
<settlement>Antigonish</settlement>
<repository>Nova Scotia Archives</repository>
<origPlace>Halifax</origPlace>

<!-- After: connected to authority records -->
<settlement ref="https://www.wikidata.org/wiki/Q3350">Antigonish</settlement>
<repository ref="http://viaf.org/viaf/...">Nova Scotia Archives</repository>
<origPlace ref="https://www.geonames.org/...">Halifax</origPlace>
```

Look at the difference. The human reader still sees the familiar words. But underneath, the computer follows the `ref` attribute straight to the authority record. Automated tools can then crawl your edition, pull the coordinates or the institutional identity, and connect your document to everything else described by the same registers.

**Vocabulary.** *Authority control* — the practice of linking variant names and terms to a single standardized identifier in an established cultural register. *`ref` attribute* — the TEI attribute used to point directly to a canonical URI or authority record.

**Takeaway:** By adding `ref` attributes to names and places, your TEI Header links human-readable text to permanent machine-readable authority records.

---

## **14 Content**

**The Authority Registers: A General Layer and a Tradition-Specific Layer**

Where do you find these URIs for your document's entities? You look them up in recognized authority registers — but there are two layers, and only the first is universal.

**The general layer applies to almost any historical document:**

1. **VIAF (Virtual International Authority File)** (`viaf.org`): The gold standard for historical people and corporate bodies. It combines authority files from the Library of Congress, the British Library, the Bibliothèque nationale de France, and many others into a single identifier for a person or institution.
2. **Wikidata** (`wikidata.org`): The open, multilingual knowledge graph. A `Q` number identifies a person, place, work, or institution, and it links out to every other register.
3. **Library of Congress authorities** (`id.loc.gov`): LCCN and name/title authorities. Strong for printed material and for American imprints in particular.
4. **Getty Vocabularies** (`getty.edu/research/tools/vocabularies/`):
   - **TGN (Thesaurus of Geographic Names)**: global geographic authority, for `<origPlace>` and `<settlement>`.
   - **AAT (Art & Architecture Thesaurus)**: standard terms for materials, scripts, and techniques — for example "parchment", "laid paper", "cursive".
5. **GeoNames** (`geonames.org`): a general gazetteer, useful for modern place names when TGN has no entry.

**The tradition-specific layer is where documents diverge.** A register built for one scholarly tradition will not describe a document from another, and choosing the wrong register is a methodological error rather than a harmless one:

| Your document | The registers that actually govern it |
| :--- | :--- |
| A **Greek literary manuscript** | **Trismegistos** (the text as a documented object), **Pinakes** (the work and the manuscripts carrying it), **Diktyon** (the physical Greek codex), and **Pleiades** for ancient places. |
| An **18th-century French royal act** | **Archives nationales** cotes; **Gallica / BnF ARK** identifiers of the form `ark:/12148/...`; **FranceArchives**. |
| A **Peace and Friendship Treaty document** | **Nova Scotia Archives** references (`RG 1 volume ... number ...`); **Library and Archives Canada**; the **National Archives (UK)**, Colonial Office papers `CO 217`. |
| A **19th-century American literary manuscript** | **Emily Dickinson Archive**; **Houghton Library** call numbers in the `MS Am 1118.x` series; **Amherst College** `AC` accession numbers. |

Neither Trismegistos nor Pleiades will help you with a French decree, a treaty, or a Dickinson poem. That does not mean those documents lack authority control; it means their authority lives in different registers, and **finding out which is part of the scholarly work**.

**In your lab work today**, identify the general-layer record for the person or institution attached to your document, then find at least one tradition-specific identifier and confirm it resolves to the right object.

**A warning about verification.** Some registers return a success response for identifiers that do not exist. A VIAF URL with an invented number still loads a page. **Do not validate an identifier by checking that the link opens** — open the record and read its content against an independent source. A live link is not evidence.

**Vocabulary.** *Authority control* — linking variant names and terms to a single standardized identifier in an established register. *VIAF* — Virtual International Authority File, linking personal and corporate identities across national libraries. *Gazetteer* — a geographical dictionary or register; TGN and GeoNames are gazetteers.

**Takeaway:** Authority control has a general layer (VIAF, Wikidata, LC, Getty) that works for almost anything, and a tradition-specific layer that does not transfer between traditions. Identify both, justify why each register governs your document, and verify by reading the record rather than by checking that the link loads.

---

## **15 Content**

**Mapping Manuscript Migrations (MMM): Harmonizing Global Data**

To see the staggering power of Linked Open Data in codicology, consider the **Mapping Manuscript Migrations (MMM)** project.

For centuries, scholars had no way to track how manuscripts moved across Europe between the Middle Ages and the twentieth century. Data was trapped in separate institutional databases: the Schoenberg Database of Manuscripts at Penn, the Bibale database in Paris, and the Medieval Manuscripts in Oxford Libraries portal.

The MMM project took over 500,000 manuscript records from these three independent institutions, converted their metadata into RDF triples, and linked them through shared authority IDs (VIAF, Wikidata, and TGN).

The result? 

An interactive computational platform (`mappingmanuscriptmigrations.org`) where researchers can track the entire lifetime journey of a manuscript. You can see how a codex copied in a German monastery in 1100 was sold to an Italian merchant in 1520, bought by an English duke in 1740, and purchased by an American university in 1950. That global visualization is only possible because independent cataloguers agreed on shared Linked Data identifiers.

**Vocabulary.** *Data harmonization* — integrating disparate data formats from multiple archives into a unified, coherent semantic model. *Schoenberg Database of Manuscripts (SDBM)* — an international database tracking manuscript provenance, sales, and migrations.

**Takeaway:** The Mapping Manuscript Migrations project proves how linking local catalog records to shared RDF authorities unlocks global historical patterns of manuscript trade and provenance.

---

## **16 Content**

**Wikibase and Knowledge Graphs for Codicology**

In recent years, the digital humanities community has embraced **Wikibase** — the open-source software engine behind Wikidata — as a flexible platform for building domain-specific knowledge graphs.

Why Wikibase?

Traditional relational databases are rigid: they require fixed tables with predefined columns. If you discover an unexpected codicological detail (such as a 14th-century merchant's shopping list scribbled on a flyleaf), a traditional database has nowhere to put it. 

A knowledge graph, by contrast, is a living web of nodes and edges. You can connect any entity to any other entity using typed properties:

- *Manuscript X* -> `hasBinding` -> *16th-century pigskin*
- *Manuscript X* -> `containsAnnotationBy` -> *Erasmus of Rotterdam*
- *Erasmus of Rotterdam* -> `studiedAt` -> *University of Paris*

When your TEI Header includes Wikidata identifiers (`ref="https://www.wikidata.org/wiki/Q..."`), external knowledge graphs can ingest your edition and automatically connect your full-page witness to millions of related historical facts.

**Vocabulary.** *Knowledge graph* — a network of real-world entities and their semantic relationships, represented as interconnected nodes and edges. *Wikibase* — the open-source software used to create collaborative, machine-actionable knowledge graphs.

**Takeaway:** Knowledge graphs represent complex, interconnected manuscript histories as living networks of entities and relationships, easily enriched by TEI metadata.

---

## **17 Content**

**Link Rot and 404s: Why Regular Web Links Fail Ancient Documents**

Now let us tackle a second great danger in digital scholarship: **the crisis of broken citations**.

Suppose you are writing a research paper and you cite an online manuscript image like this:
`https://www.somelibrary.edu/special-collections/greek/mss/box4/image23.jpg`

What happens in three years when the library updates its web server? What happens when the library renames its website, reorganizes its digital collections, or goes through a rebranding campaign?

**404 Not Found. The link dies.**

This disease is known as **link rot**. In computational scholarship, relying on standard web URLs is fatal. If the citations in your digital edition break after five years, your scholarship is useless to the next generation of researchers.

Ancient texts have survived for thousands of years. Homer's *Iliad* has been read for nearly three millennia; the Greek Septuagint for over two thousand years. How can we build digital citations that last as long as the manuscripts themselves? We need citation systems that are independent of temporary web server addresses.

**Vocabulary.** *Link rot* — the phenomenon where web links become broken and point to missing resources (404 errors) as servers and website structures change over time. *Ephemerality* — the fragile, short-lived nature of standard web URLs.

**Takeaway:** Standard web URLs are fragile and prone to link rot; scholarly editions require persistent, location-independent citation architectures that outlive server reboots.

---

## **18 Content**

**Citing a Structure, Not a File**

To understand why canonical citation matters, separate two things that are easy to confuse: the **logical structure** of a text, and the **physical carrier** it happens to sit on.

Consider any document you might edit:

- A **treaty** has articles and clauses, and it exists in several exemplars — a printed proclamation, manuscript copies in council registers, a transcription sent to London. The *text* of the treaty is one thing; each *carrier* is another.
- A **French royal act** has a preamble, a dispositif, and a dating clause. It may survive as a sealed parchment original, as a registration in a court's register, and as a printed piece in a *recueil*. Three carriers, one act.
- A **Dickinson poem** has stanzas and lines. It may exist as a pencil draft on wrapping paper, a fair copy, and a transcription in a printed edition. The poem is not the paper.

The principle this illustrates — that a text has a structure independent of the object carrying it — is what makes durable citation possible. If your citation points at the *structure* (article 3 of the treaty, verse 4 of the poem) rather than at *this file on this server*, the citation survives the server being reorganised.

Different traditions formalise this differently. Classical philology built the **CITE Architecture** and the **OHCO2 model** ("Ordered Hierarchy of Content Objects") for Greek and Latin texts, and **CTS URNs** to address them. Modern archival practice uses persistent identifiers like **ARK**. Library cataloguing uses call numbers plus series structure. The implementations differ; the underlying insight is the same.

**Vocabulary.** *Logical structure* — the internal organisation of a text (articles, chapters, lines) as distinct from its physical carrier. *Carrier* — the physical object or file that transmits a text. *CITE Architecture* — a framework from classical philology for persistent, machine-actionable citation. *OHCO2* — Ordered Hierarchy of Content Objects; the model treating texts as stable structural hierarchies.

**Takeaway:** Distinguish the text's logical structure from the physical carrier that transmits it — that distinction is what lets a citation outlive the shelfmark, the server, and the file path.

---

## **19 Content**

**Canonical Citation: Giving Your Object a Stable Address**

A citation that depends on a shelfmark is fragile. Shelfmarks change: libraries reclassify, collections move, and a manuscript catalogued as one shelfmark today can be renumbered in the next revision. If your edition cites the shelfmark alone, your citation breaks the moment the holding library reorganises.

**Canonical citation** solves this by giving your object an identifier that survives such changes.

The general principle is the same in every tradition: an identifier is assigned by some authority, it is persistent, and it resolves to the object regardless of where the object currently sits.

**Vocabulary.** *Persistent identifier* — an identifier designed to keep resolving to the same object even when URLs, systems, or shelfmarks change. *Canonical citation* — citing an object by such an identifier rather than by a location-dependent label.

**Takeaway:** Cite your object by a persistent identifier as well as by its shelfmark, because shelfmarks change and scholarship has to outlast them.

---

## **20 Content**

**Three Citation Systems, Three Traditions**

The identifier that works for your document depends on its tradition. Here are the three in play this term.

**1. ARK — for the French decree (and a great deal else).**

An **ARK** (Archival Resource Key) is a persistent identifier designed for archival and cultural objects. It takes the form:

```text
ark:/12148/bpt6k9690620k
```

- `ark:` declares the scheme.
- `12148` is the **NAAN** — the Name Assigning Authority Number. BnF's is `12148`.
- `bpt6k9690620k` is the object name.

The point of ARK is that the **Name Mapping Authority** — the organisation currently serving the object — can change while the ARK name stays fixed. That is why it persists. Note the syntax: `ark:/` takes a **single** slash; the NAAN is separated from the name by a further slash.

**2. Library call numbers — for the Dickinson manuscript.**

Harvard's Houghton Library identifies Dickinson material by a call number in a fixed series:

```text
MS Am 1118.3 [338]
```

`MS Am` denotes an American manuscript; `1118.3` is the series (poems — fascicles and loose sheets, as distinct from `1118.2`, the Holland letters); `[338]` is the item. This is not a persistent identifier in the ARK sense — it is a shelfmark — but it is the citable reference the holding library requires, and it is stable in practice because Houghton maintains it.

**3. Archival reference numbers — for the treaty.**

The Nova Scotia Archives cites by record group, volume, and number:

```text
RG 1 volume 430 number 2
```

Oversize items get a separate form, `O/S number 511`. Note what this citation does *not* tell you: whether you are looking at an original, a copy, or a printed edition. Two documents in the same volume can differ in status entirely, so the reference number must be paired with a statement of what the object actually is.

**Vocabulary.** *ARK* — Archival Resource Key; a persistent identifier for archival objects. *NAAN* — Name Assigning Authority Number, the numeric prefix identifying which institution minted the ARK. *Record group* — an archival arrangement unit, here abbreviated `RG`.

**Takeaway:** ARK, library call number, and archival reference number are three different citation systems serving three different traditions — use the one your holding institution uses, and copy its syntax exactly rather than normalising it.

---

## **21 Content**

**Reading a Record, Not Just Finding It**

Finding an identifier is not the same as verifying one. A record has to be read.

Take the Gallica item you may be using this term. Its ARK is `ark:/12148/bpt6k9690620k`. Open the record and you find:

| Field | Value |
| :--- | :--- |
| Shelfmark | Bibliothèque nationale de France, département Droit, économie, politique, F-21718 |
| Date | 1771 |
| Format | 67 pièces en 1 vol. in-4° |
| Creator | Louis XV (1710-1774 ; roi de France) |

Every one of those fields is a fact you can put in a TEI header — and every one is a fact you can check. Does the date match what you expected? Is the creator the person you thought? Does "67 pièces en 1 vol." describe one document or sixty-seven bound together? That last question matters: a *recueil* is a collected volume, and cataloguing it as though it were a single act would be a mistake.

**The same discipline applies to every register.** A Dickinson call number tells you which series the item sits in, which tells you whether it is a poem or a letter. A treaty reference number tells you the volume but not the status. Reading the record is what converts an identifier into knowledge.

**Vocabulary.** *Recueil* — a collected volume; in French archival and library practice, a set of pieces bound together, each with its own date, which may be catalogued as one item or many.

**Takeaway:** An identifier is a pointer, not a fact. Open the record and read its fields, because the metadata inside is what goes into your header — and mismatches between the record and your expectations are findings, not obstacles.

---

## **22 Content**

**Dating: Where Records Mislead**

Dates in catalogue records are not neutral facts, and this is the single most productive place to catch a subtle error.

**Editorial attribution.** The Emily Dickinson Archive states plainly that Dickinson "very rarely dated her poems," and that the libraries and editions "often give approximate dates." A date in a Dickinson record is therefore an *editorial attribution*, not an authorial statement — frequently with the attributing scholar named in brackets. Recording it as a certain date in your header would overstate the evidence. TEI gives you the vocabulary to be honest about this, and Module 02's `<origin>` work is where you apply it.

**Calendar style.** France adopted the Gregorian calendar in December 1582, so no Julian day-shift applies to an 18th-century French document. Do not "correct" one. The trap that *does* apply is **year-start style**: before the *édit de Roussillon* (1564) took full effect in 1567, the year was reckoned from Easter or Christmas in various usages, so a document dated between 1 January and Easter is often **one year later** in modern reckoning.

**Printed vs manuscript date.** A printed proclamation carries a date of printing. That is not necessarily the date of the event it records, and it is certainly not the date of the agreement it publishes.

**Vocabulary.** *Editorial attribution* — a date supplied by a modern editor rather than stated by the document. *Year-start style* — the convention determining which day begins the year, which varied by place and period.

**Takeaway:** Ask of every date whether it is authorial, editorial, or a record of something else — and record the uncertainty rather than flattening it, because a confident wrong date is exactly the failure your workshop is about.

---

## **23 Content**

**Recording the Citation in Your Header**

How do you put all of this into your TEI header?

The `ref` attribute carries the identifier, on whichever element describes the thing being identified:

```xml
<msIdentifier>
    <settlement ref="https://www.wikidata.org/wiki/Q3350">Antigonish</settlement>
    <repository ref="http://viaf.org/viaf/...">Nova Scotia Archives</repository>
    <idno type="reference">RG 1 volume 430 number 2</idno>
    <idno type="ARK">ark:/12148/bpt6k9690620k</idno>
</msIdentifier>
```

Three things to notice:

1. **`<idno>` takes a `type` attribute.** Use it. A reference number, an ARK, and a call number are different kinds of identifier, and `type` is how you say which is which. A bare `<idno>` with no type tells a reader nothing about what they are looking at.
2. **`ref` goes on the element it identifies**, not on the header as a whole. A repository name gets a repository's authority URI; a settlement gets a place's.
3. **The human-readable text stays human-readable.** The reader sees "Nova Scotia Archives"; the machine follows the URI. That is the whole point of authority control.

For the status of the object — original, copy, transcript, or printed edition — use `<note>` inside or beside the identifier, because the reference number alone will not tell you:

```xml
<idno type="reference">RG 1 volume 430 number 2</idno>
<note type="status">Printed proclamation; no original signed copy is known to survive.</note>
```

**Vocabulary.** *`ref` attribute* — the TEI attribute pointing to a canonical URI or authority record. *`idno`* — the TEI element for a formal identifier, qualified by `type`.

**Takeaway:** Record each identifier in its own `<idno>` with a `type`, put authority URIs in `ref` on the element they identify, and state the object's status separately — because the identifier alone does not say what kind of thing you are holding.

---

## **24 Content**

**Hands-On in VS Code: Connecting to the Schema**

Now it is time for today's practical lab work. 

Open Visual Studio Code on your machine. Open your course repository, and locate the primary witness header file you hand-authored yesterday:

`03a_Lesson_2.1_Primary_Witness_Header.xml`

Make a copy of this file for today's milestone:

`03a_Lesson_2.2_Validated_Witness_Header.xml`

Now, insert the official schema instruction at the very top of the file, right after line 1:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="https://raw.githubusercontent.com/msdesc/consolidated-tei-schema/master/msdesc.rng" 
            type="application/xml" 
            schematypens="http://relaxng.org/ns/structure/1.0"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
```

Save the file (`Ctrl+S` or `Cmd+S`).

Watch your editor. Within two seconds, the background XML language server in VS Code will parse your hand-written markup against the official schema. If you made any syntax or structural mistakes yesterday, red squiggly lines will appear!

**Vocabulary.** *Schema linking* — declaring the online or local location of a schema within an XML file to enable real-time editor validation. *Diagnostics* — the automated error and warning messages generated by a language server.

**Takeaway:** Copy your hand-written header to `03a_Lesson_2.2_Validated_Witness_Header.xml`, add the `xml-model` processing instruction, and let VS Code audit your markup.

---

## **25 Content**

**Slaying the Red Squiggles: Reading Validator Error Messages**

When red squiggly lines light up your screen, do not panic! Every programmer and digital editor in the world spends their days debugging errors. The secret to debugging is learning how to read what the validator is trying to tell you.

Open the Problems panel in VS Code (`Ctrl+Shift+M` or `Cmd+Shift+M`). 

Here are the three most common error messages you will encounter today, and how to fix them:

1. **"Element 'xyz' is not allowed here"**: You put a tag in the wrong container or out of sequence. Check the order! Does `<publicationStmt>` come before `<sourceDesc>`? Did you accidentally put `<supportDesc>` outside of `<objectDesc>`?
2. **"The element type 'xyz' must be terminated by the matching end-tag"**: You forgot the closing slash `/` in your end tag, or you forgot to close a tag altogether.
3. **"Attribute 'material' has invalid value"**: You typed a value that violates the schema enumeration. For example, you typed `material="vellum"`, but the schema only permits `material="parchment"`. Change it to `"parchment"`!

Work through the Problems panel one line at a time. Click on an error in the panel, and VS Code will jump directly to the offending line in your code. Fix the issue, save the file, and watch the error count drop.

**Vocabulary.** *Debugging* — the process of identifying, analyzing, and removing errors from computer code or markup. *Problems panel* — the VS Code interface displaying active errors, warnings, and schema diagnostic messages.

**Takeaway:** Read schema error messages carefully to identify sequence mistakes, unclosed tags, or illegal attribute values, resolving them one by one.

---

## **26 Content**

**Enriching Your Header with Authority URIs**

Once your file validates with zero errors, the next task is to enrich your header with authority URIs.

Open your browser and look up two identifiers for your document:

1. **Holding repository.** Search `viaf.org` or `wikidata.org` for the institution that holds your document — the Nova Scotia Archives, the Houghton Library, the Bibliothèque nationale de France. Copy the canonical URI and put it on `<repository>`:
   ```xml
   <repository ref="http://viaf.org/viaf/...">Nova Scotia Archives</repository>
   ```
   If the institution has no authority record, say so in a `<note>` — a verified absence is a finding, and it is honest.

2. **Place of origin or place of issue.** Use the register that fits your document. **TGN** (`getty.edu`) or **GeoNames** work for most modern and early-modern places. **Pleiades** is the right tool only for ancient Greek and Roman geography — it will not help you with Halifax, Amherst, or Paris.
   ```xml
   <origPlace ref="https://www.geonames.org/...">Halifax</origPlace>
   ```

**Verify by reading the record, not by checking the link.** Open each URI and confirm that the name, dates, and description match the entity you intend. Some registers return a page even for identifiers that do not exist, so a link that loads proves nothing.

**Vocabulary.** *Entity enrichment* — adding external authority identifiers to plain-text names in a document. *Canonical record* — the authoritative master entry for an entity in a shared register.

**Takeaway:** Enrich your repository and place of issue with authority URIs from the register appropriate to your document's tradition, and verify each by reading the record's content rather than by confirming the link resolves.

---

## **27 Content**

**Adding Your Canonical Citation**

Now add your witness's identifiers to your header.

**Step 1 — identify what kind of identifier your holding institution uses.** This depends on your document:

- **A French act** → an ARK, e.g. `ark:/12148/bpt6k9690620k`, found in the Gallica record.
- **A Dickinson manuscript** → a Houghton call number, e.g. `MS Am 1118.3 [338]`, from the finding aid or the Emily Dickinson Archive.
- **A treaty document** → a Nova Scotia Archives reference, e.g. `RG 1 volume 430 number 2`.

**Step 2 — find the general-layer authority URI** for the holding institution or the person chiefly responsible. This is usually a VIAF or Wikidata URI, and it is frequently provided on the institution's own record page.

**Step 3 — write them into `<msIdentifier>`**, each in its own `<idno>` with a `type`, and add a `<note>` recording the object's status:

```xml
<msIdentifier>
    <settlement ref="https://www.wikidata.org/wiki/Q3350">Antigonish</settlement>
    <repository ref="http://viaf.org/viaf/...">Nova Scotia Archives</repository>
    <idno type="reference">RG 1 volume 430 number 2</idno>
    <note type="status">Printed proclamation; no original signed copy is known to survive.</note>
</msIdentifier>
```

Save the file and verify that VS Code accepts the attributes without schema warnings.

**One rule above all:** copy the identifier in the **exact syntax** you found it. Do not normalise `ark:/` to `ark://`, do not convert `RG 1 volume 430 number 2` into `RG1/430/2`, and do not add or remove brackets in a call number. An identifier is a name, and renaming it breaks it.

**Vocabulary.** *`idno`* — the TEI element for a formal identifier, qualified by a `type` attribute. *`ref`* — the attribute carrying a canonical URI for the element it sits on.

**Takeaway:** Put each identifier in its own typed `<idno>`, add the object's status as a `<note>`, and copy the syntax exactly as the issuing institution writes it.

---

## **28 Content**

**Seeing Your Header as Linked Data**

How does a computer read the markup you just wrote?

When semantic tools ingest your TEI header, they extract the identifiers and URIs you recorded and turn them into statements a machine can follow. Conceptually, your header becomes a set of assertions:

```text
<your document>  has holding institution  <Nova Scotia Archives>
<your document>  has reference number     "RG 1 volume 430 number 2"
<your document>  has status               "printed proclamation"
<Nova Scotia Archives>  is identified by  <its VIAF URI>
```

That is the payoff of authority control: your plain XML file has become a set of queryable claims about real-world entities, and each claim is traceable to a source.

**And here is where the lesson connects to your workshop.** Every one of those claims is checkable, which means every one can be *false*. A model can produce a well-formed header asserting a repository URI that resolves to a different institution, or a reference number that belongs to a different volume. The structure will validate. Only a human comparing the claim against the record catches it.

**Vocabulary.** *Triple* — a subject-predicate-object statement; the unit of Linked Data. *Triple extraction* — deriving such statements from structured markup.

**Takeaway:** Your header is a set of checkable claims about real entities — which is exactly why an AI-generated header can be confidently, structurally valid, and wrong.

---

## **29 Content**

**The Stage Gate: Achieving a Zero-Error Audit in Git**

Before you commit today's work, you must pass the **deterministic stage gate**.

Look at the bottom left of your VS Code window. The Problems counter must say:
**0 Errors, 0 Warnings.**

A single remaining syntax error or schema violation means your document cannot be ingested by downstream pipelines in Weeks 3 through 13. Deterministic validation is an all-or-nothing threshold.

Once your file passes with zero errors, stage and commit it to Git:

```bash
git add 03a_Lesson_2.2_Validated_Witness_Header.xml
git commit -m "Topic 02 (Cataloguing): Pass deterministic schema validation in VS Code with LOD & CTS enrichment [0 errors]"
git push origin main
```

Notice the commit message: `[0 errors]`. You are documenting that your work passed the automated audit. Your Git commit history is your permanent, tamper-proof lab notebook.

**Vocabulary.** *Stage gate* — a mandatory quality-assurance milestone that must be 100% satisfied before a project can advance to the next production phase. *Clean validation* — an XML document state containing zero errors and zero warnings against all active schemas.

**Takeaway:** Verify that VS Code reports 0 errors and 0 warnings, then commit your validated header to Git as your certified deterministic milestone.

---

## **30 Content**

**Synthesis: The Three-Step Cycle in Action**

Look back at what you have accomplished across the first two days of Module 02:

1. **Tuesday (Manual Ground Truth)**: You hand-wrote your manuscript description in raw XML. You made human decisions about ink, parchment, and scribal hands, discovering firsthand the tactile complexity of the artifact.
2. **Wednesday (Deterministic Validation)**: You introduced your draft to the machine. You ran it against the official TEI RELAX NG schema in VS Code, slayed the syntax errors, enriched your entities with authority URIs from the registers appropriate to your document, and recorded its persistent identifier.

You now possess an authoritative, certified baseline. 

Why was this two-step preparation so crucial?

Because on **Friday, in Lesson 2.3**, we unleash **Artificial Intelligence**. You will feed raw cataloguing prose and manuscript images into large language models (LLMs) and ask the AI to automatically extract metadata and generate TEI markup.

Because LLMs are probabilistic, they will hallucinate. They will invent non-existent shelfmarks, mix up folio numbers, and generate invalid XML tags that sound convincing. But on Friday, the AI will not be able to fool you. You will have your human ground truth from Tuesday and your deterministic schema validator from Wednesday. You will measure the AI's output against your baseline, calculate its precision and recall, and discover exactly where AI accelerates scholarship—and where it fails.

**Due today, Wednesday September 9.** Your fully validated `03a_Lesson_2.2_Validated_Witness_Header.xml` committed and pushed to GitHub with zero schema errors.

**Next class (Friday).** Step 3: Probabilistic AI-assisted metadata extraction, entity recognition, and scoring AI accuracy against human ground truth.

**Takeaway:** Manual ground truth plus deterministic validation creates the rigorous foundation needed to evaluate and control probabilistic AI on Friday.

---

## References

Blackwell, C. W., & Smith, N. (2019). The CITE Architecture: A framework for linked data in the humanities. *Digital Humanities Quarterly, 13*(1).

Bodleian Libraries. (2024). *Bodleian TEI manuscript description schema (msdesc.odd)*. University of Oxford. https://github.com/bodleian/consolidated-tei-schema

Cummings, J. (2018). The Text Encoding Initiative and the study of literature. In *A New Companion to Digital Humanities* (pp. 451–476). Wiley-Blackwell.

Griffitts, T. (2020). *Digital philology and the Text Encoding Initiative: Methods for ancient manuscript research*. De Gruyter.

Huskey, S. J. (2024). Committing to reproducibility and explainability: Using Git as a research journal. *International Journal of Digital Humanities, 6*, 9–21. https://doi.org/10.1007/s42803-023-00076-9

Hyvönen, E., et al. (2021). Mapping Manuscript Migrations: A knowledge graph and portal for medieval and Renaissance manuscripts. *Digital Humanities Quarterly, 15*(2).

Smith, N., & Blackwell, C. W. (2012). *The Canonical Text Services protocol*. Harvard University Center for Hellenic Studies.

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and interchange* (Version 4.12.0). https://tei-c.org/guidelines/p5/
