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
3. **URIs and URLs**: In `ref="..."` or `target="..."`, the schema checks that the value is a properly formatted web address or CTS URN.

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
<!-- Before: Dumb strings in a silo -->
<settlement>Vatican City</settlement>
<repository>Biblioteca Apostolica Vaticana</repository>
<origPlace>Constantinople</origPlace>

<!-- After: Linked Open Data connected to global entities -->
<settlement ref="https://www.wikidata.org/wiki/Q237">Vatican City</settlement>
<repository ref="http://viaf.org/viaf/141312782">Biblioteca Apostolica Vaticana</repository>
<origPlace ref="https://pleiades.stoa.org/places/520998">Constantinople</origPlace>
```

Look at the difference. The human reader still sees the familiar English words "Vatican City" and "Constantinople". But underneath, the computer follows the `ref` attribute directly to Wikidata and Pleiades! Automated scripts can now crawl your edition, pull geographic coordinates, and automatically plot your manuscript on an interactive historical map!

**Vocabulary.** *Authority control* — the practice of linking variant names and terms to a single standardized identifier in an established cultural register. *`ref` attribute* — the TEI attribute used to point directly to a canonical URI or authority record.

**Takeaway:** By adding `ref` attributes to names and places, your TEI Header links human-readable text to permanent machine-readable authority records.

---

## **14 Content**

**The Global Authority Registers: VIAF, Pleiades, and Wikidata**

Where do you find these magical URIs for your manuscript entities? You look them up in recognized global authority registers:

1. **VIAF (Virtual International Authority File)** (`viaf.org`): The gold standard for historical people and cultural institutions. It combines authority files from the Library of Congress, the British Library, the Bibliothèque nationale de France, and the Vatican Library into a single universal ID.
2. **Pleiades Gazetteer** (`pleiades.stoa.org`): The premier authority for ancient and medieval geography. It provides permanent URIs, historical name variants, and precise GPS coordinates for ancient cities, provinces, and monasteries.
3. **Getty Vocabularies** (`getty.edu/research/tools/vocabularies/`):
   - **TGN (Thesaurus of Geographic Names)**: Global geographic authority.
   - **AAT (Art & Architecture Thesaurus)**: Standard terms for materials, scripts, and bookbinding techniques (e.g. "vellum", "minuscule", "rubrication").
4. **Wikidata** (`wikidata.org`): The open, multilingual knowledge graph that connects millions of historical entities, institutions, and texts.

In your lab work today, you will look up the VIAF record for your holding library and the Pleiades ID for your manuscript's place of origin.

**Vocabulary.** *VIAF* — Virtual International Authority File, linking personal and institutional identities across national libraries. *Pleiades* — open digital gazetteer of the premodern Greek and Roman world. *Getty AAT* — structured thesaurus of terms for cultural heritage materials and techniques.

**Takeaway:** Digital editors link their entities to trusted global registers like VIAF for people and institutions, Pleiades for ancient places, and Getty AAT for materials.

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

**The CITE Architecture and the OHCO2 Text Model**

To solve the crisis of broken links, classical philologists developed the **CITE Architecture** (Collections, Indices, Text, and Extensions) and the **OHCO2 Text Model**.

The OHCO2 model asserts a profound humanistic principle:
**An ancient text is an Ordered Hierarchy of Content Objects.**

What does that mean in plain English?

It means that an ancient text is not defined by the physical paper or modern web server it happens to be viewed on. When you read the Gospel of Mark or Homer's *Odyssey*, the text has a stable, logical structure that has existed for centuries:

- A text consists of Books.
- Books consist of Chapters.
- Chapters consist of Verses or Lines.

This logical hierarchy exists independently of whether the text is written on 4th-century Egyptian papyrus, printed in a 19th-century German book, or displayed on an iPhone screen. If our citation system points to the *logical structure* of the text rather than a *server file path*, the citation will never rot!

**Vocabulary.** *CITE Architecture* — a digital framework designed for persistent, machine-actionable scholarly citations in classical philology. *OHCO2* — Ordered Hierarchy of Content Objects, a theoretical model treating texts as stable structural hierarchies of books, chapters, and lines.

**Takeaway:** The OHCO2 text model treats literature as an ordered hierarchy of logical units (books, chapters, lines) rather than physical pages or server file paths.

---

## **19 Content**

**GPS Coordinates for Texts: The Anatomy of a CTS URN**

The primary tool of the CITE Architecture is the **Canonical Text Services (CTS) URN (Uniform Resource Name)**.

Think of a CTS URN as **permanent GPS coordinates for ancient texts**. Just as a latitude/longitude coordinate points to an exact physical spot on Earth regardless of whether you look at Google Maps, Apple Maps, or a paper atlas, a CTS URN points to an exact text passage regardless of what website displays it.

Here is what a complete CTS URN looks like:

```text
urn:cts:greekLit:tlg0527.tlg001.opp-grc1:1.1-1.14
```

Let us dissect this string piece by piece. It consists of five colon-separated zones:

1. `urn:cts`: Declares that this is a Canonical Text Service identifier.
2. `greekLit`: The text group or cultural corpus (Ancient Greek literature).
3. `tlg0527`: The author identifier in the Thesaurus Linguae Graecae registry (Septuagint).
4. `tlg001.opp-grc1`: The work and specific edition/witness expression (Book of Genesis, Greek text edition 1).
5. `1.1-1.14`: The precise passage citation (Chapter 1, verses 1 through 14).

Notice that there is no `http://`, no `.html`, and no website server name. This identifier will remain mathematically true and valid in the year 2526, long after today's web hosting companies have turned to dust.

**Vocabulary.** *CTS URN* — Canonical Text Services Uniform Resource Name, a permanent, syntax-governed identifier for text passages that functions independently of web hosting infrastructure. *Canonical citation* — a standardized citation format traditionally used by scholars to cite a work by its internal structure (chapter, verse, line).

**Takeaway:** A CTS URN acts as permanent GPS coordinates for literature, citing text passages by their logical structure rather than temporary website URLs.

---

## **20 Content**

**Granular Passage Addressing in CTS URNs**

One of the greatest features of CTS URNs is their incredible flexibility in citation granularity. You can cite as broadly as an entire author's corpus, or as specifically as a single word on a manuscript page!

Look at how the citation zooms in:

| Granularity Level | CTS URN Syntax | What It Identifies |
| :--- | :--- | :--- |
| Corpus Level | `urn:cts:greekLit:tlg0527` | The entire Greek Septuagint corpus |
| Work Level | `urn:cts:greekLit:tlg0527.tlg001` | The Book of Genesis |
| Edition Level | `urn:cts:greekLit:tlg0527.tlg001.opp-grc1` | The specific digital Greek edition |
| Chapter Level | `urn:cts:greekLit:tlg0527.tlg001.opp-grc1:1` | Genesis Chapter 1 |
| Verse Range | `urn:cts:greekLit:tlg0527.tlg001.opp-grc1:1.1-1.14` | Genesis 1:1 through 1:14 (Your full-page witness!) |
| Single Verse | `urn:cts:greekLit:tlg0527.tlg001.opp-grc1:1.1` | Genesis Chapter 1, verse 1 |

Because the syntax is strictly standardized, any automated script can parse this string, calculate that verse `1.1` is contained inside chapter `1`, and fetch the exact XML fragment on demand.

**Vocabulary.** *Citation granularity* — the level of structural specificity (corpus, work, book, chapter, verse, word) targeted by a citation identifier. *Range expression* — citing an unbroken sequence of text units using a hyphen (`from-to`).

**Takeaway:** CTS URNs support scalable granularity, allowing scholars to reference an entire work, a chapter, or an exact verse range with identical mathematical syntax.

---

## **21 Content**

**Sub-Reference Syntax: Targeting the Individual Word**

What happens if you want to cite a single specific word in your manuscript that contains an unusual scribal spelling?

Ancient texts do not have word numbers. But the CTS standard includes a brilliant mechanism called **sub-reference syntax** using the `@` symbol:

```text
urn:cts:greekLit:tlg0527.tlg001.opp-grc1:1.1@ἀρχῇ
```

This URN targets the specific word **ἀρχῇ** ("beginning") inside Genesis 1:1!

What if a word appears multiple times in the same verse? (For example, the Greek conjunction **καί** might appear four times in a single line). You simply add an ordinal index in brackets:

```text
urn:cts:greekLit:tlg0527.tlg001.opp-grc1:1.1@καί[2]
```

This specifies the *second* occurrence of the word *καί* in verse 1! With sub-references, scholars can create digital footnotes, grammatical tags, and paleographical notes that point directly to an individual word on a parchment leaf with mathematical precision.

**Vocabulary.** *Sub-reference (`@`)* — CTS syntax used to identify a specific word or token within a cited passage by its textual string. *Ordinal indexing (`[n]`)* — specifying which instance of a repeated word is targeted within a passage.

**Takeaway:** Sub-reference syntax allows CTS URNs to pinpoint individual words within a verse, providing exact targets for textual variants and linguistic commentary.

---

## **22 Content**

**CITE URNs for Physical Objects: Folios, Images, and Papyri**

Texts are logical entities, but manuscripts are physical objects. What if you want to cite the physical leaf itself rather than the abstract literary work?

The CITE Architecture includes a companion standard called the **CITE Object URN**:

```text
urn:cite2:rels398:manuscripts.v1:vat_gr_2121_f213r
```

Notice the syntax:

- `urn:cite2`: Declares a CITE Object collection.
- `rels398`: The project namespace (our course repository!).
- `manuscripts.v1`: The collection name (manuscript leaves, version 1).
- `vat_gr_2121_f213r`: The unique object identifier (Vatican Greek 2121, folio 213 recto).

By pairing CTS URNs (for texts) with CITE Object URNs (for physical leaves), your digital edition creates a perfect semantic bridge between literature and codicology. You can formally assert: *"The text identified by `urn:cts:...:1.1-1.14` is inscribed on the physical artifact identified by `urn:cite2:...:vat_gr_2121_f213r`."*

**Vocabulary.** *CITE Object URN* — a persistent identifier used to cite physical artifacts, museum objects, and digital images independently of text hierarchies. *Semantic bridge* — linking physical artifact records directly to literary text passages.

**Takeaway:** While CTS URNs cite text passages, CITE Object URNs cite physical manuscript leaves and images, creating a permanent bridge between text and physical artifact.

---

## **23 Content**

**Embedding CTS URNs into the TEI Header**

How do you formally record the CTS URN of your witness inside your TEI Header?

You place it directly inside the `<msContents>` block that you authored yesterday, using the `n` or `corresp` attribute:

```xml
<msContents>
    <msItem n="1" corresp="urn:cts:greekLit:tlg0527.tlg001.opp-grc1:1.1-1.14">
        <locus from="213r" to="213r">f. 213r</locus>
        <title xml:lang="grc">Γένεσις</title>
        <title xml:lang="en">Book of Genesis</title>
        <textLang mainLang="grc">Ancient Greek</textLang>
    </msItem>
</msContents>
```

Look at what this accomplishes:

1. `<locus>` records the **physical coordinates** on the parchment (`f. 213r`).
2. `corresp="..."` records the **canonical literary coordinates** in the global CTS network (`Genesis 1:1-1.14`).

Any modern digital humanities tool can now ingest your header and immediately connect your physical transcription to every other edition, translation, and commentary of Genesis Chapter 1 across the globe.

**Vocabulary.** *`corresp` attribute* — a TEI attribute used to declare a correspondence or link between an element and an external resource or URN. *Dual citation* — anchoring both physical page location and canonical literary chapter/verse coordinates simultaneously.

**Takeaway:** Embedding CTS URNs into `<msItem corresp="...">` links the physical folio of your manuscript to the global literary citation network.

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

**Enriching with Linked Open Data: VIAF and Pleiades**

Once your file has zero grammatical errors, our next task is to enrich your header with Linked Open Data authority URIs.

Open your browser and look up two global identifiers for your witness:

1. **Holding Repository**: Go to `viaf.org` and search for your holding library (e.g. "Biblioteca Apostolica Vaticana" or "British Library"). Copy the canonical VIAF URL (e.g., `http://viaf.org/viaf/141312782`). Add it to `<repository>`:
   ```xml
   <repository ref="http://viaf.org/viaf/141312782">Biblioteca Apostolica Vaticana</repository>
   ```

2. **Place of Origin**: Go to `pleiades.stoa.org` and search for the ancient city where your manuscript was produced (e.g., "Constantinople" or "Alexandria"). Copy the Pleiades URL (e.g., `https://pleiades.stoa.org/places/520998`). Add it to `<origPlace>`:
   ```xml
   <origPlace ref="https://pleiades.stoa.org/places/520998">Constantinople</origPlace>
   ```

Now, your edition is no longer an isolated file; it is an active node connected to international library and geographical authority networks.

**Vocabulary.** *Entity enrichment* — adding external authority identifiers (URIs) to plain text names in an electronic document. *Canonical record* — the authoritative master entry representing an entity in a shared database.

**Takeaway:** Enrich your repository with its VIAF identifier and your place of origin with its Pleiades URI to connect your edition to global authority networks.

---

## **27 Content**

**Adding Your Canonical Citation: Minting Your CTS URN**

Now add your witness's canonical citation.

Look at your chosen manuscript page. Identify the exact book, chapter, and verse range inscribed on the parchment (e.g., Genesis 1:1–14, or Iliad 1:1–25).

In your `03a_Lesson_2.2_Validated_Witness_Header.xml` file, update `<msContents>`:

1. Construct the CTS URN according to standard syntax:
   - Septuagint Greek: `urn:cts:greekLit:tlg0527.tlg001.opp-grc1:CHAPTER.VERSE_START-CHAPTER.VERSE_END`
   - New Testament Greek: `urn:cts:greekLit:tlg0031.tlg001.opp-grc1:...`
2. Insert this URN into the `corresp` attribute of `<msItem>`:
   ```xml
   <msContents>
       <msItem n="1" corresp="urn:cts:greekLit:tlg0527.tlg001.opp-grc1:1.1-1.14">
           <locus>f. 213r</locus>
           <title>Book of Genesis</title>
           <textLang mainLang="grc">Greek</textLang>
       </msItem>
   </msContents>
   ```

Save the file. Verify that VS Code accepts the attribute without schema warnings.

**Vocabulary.** *URN minting* — generating and assigning a standardized uniform resource name according to established syntactic domain rules. *Corpus coordinates* — identifying a text passage by its standard author and work registry numbers.

**Takeaway:** Construct the CTS URN for your full-page passage and attach it via `<msItem corresp="...">`, permanently indexing your witness in the global classical corpus.

---

## **28 Content**

**Extracting RDF Triples: Seeing Your Header as Linked Data**

To verify that your Linked Data markup actually works, how does a computer read it?

When semantic web tools (like Apache Jena or Python's `rdflib`) ingest your TEI Header, they automatically extract RDF triples from your tags and attributes. 

From the tags you just authored, the computer generates clean semantic statements:

```turtle
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix dct: <http://purl.org/dc/terms/> .

<https://digi.vatlib.it/view/MSS_Vat.gr.2121>
    dct:title "Vat. gr. 2121" ;
    crm:P53_has_former_or_current_location <http://viaf.org/viaf/141312782> ;
    crm:P7_took_place_at <https://pleiades.stoa.org/places/520998> ;
    dct:relation <urn:cts:greekLit:tlg0527.tlg001.opp-grc1:1.1-1.14> .
```

Look at how clear that is to a computer! 

- The manuscript volume has a title `"Vat. gr. 2121"`.
- It is located at the Vatican Library (`viaf...141312782`).
- It was created at Constantinople (`pleiades...520998`).
- It carries the text of Genesis 1:1–14 (`urn:cts...`).

Your plain text XML file has officially become a queryable knowledge graph.

**Vocabulary.** *Turtle (`.ttl`)* — a human-readable text syntax used to write and serialize RDF semantic graphs. *Triple extraction* — the algorithmic translation of structured XML elements and attributes into semantic Subject-Predicate-Object statements.

**Takeaway:** Automated parsers extract clean RDF triples from your TEI tags and `ref` attributes, transforming your XML file into a queryable semantic knowledge graph.

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
2. **Wednesday (Deterministic Validation)**: You introduced your draft to the machine. You ran it against the official TEI RELAX NG schema in VS Code, slayed the syntax errors, enriched your entities with VIAF and Pleiades URIs, and minted a permanent CTS URN.

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
