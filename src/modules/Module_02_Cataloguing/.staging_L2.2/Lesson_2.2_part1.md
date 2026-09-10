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
<origPlace>Halifax</origPlace>
<author>Thomas Hopson</author>
```
A computer knows that "Halifax" is a place name and "Thomas Hopson" is a person's name. But to the computer, those words are just dumb sequences of text characters (strings). 

What if another scholar writes `<origPlace>Kjipuktuk</origPlace>` or `<settlement>Halifax, N.S.</settlement>`? What if a French source writes `<author>Thomas Hopsonn</author>`? To an automated search engine, those look like entirely different people and completely different cities!

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
- **Object**: What is the target value? (*Halifax*)

In RDF, however, we don't use fuzzy English words; we use permanent web addresses (URIs) for each of the three pieces:

- **Subject**: `https://archives.novascotia.ca/mikmaq/archives/?ID=623`
- **Predicate**: `http://purl.org/dc/terms/spatial`
- **Object**: `https://pleiades.stoa.org/places/520998`

When computers read this triple, there is zero ambiguity. A machine in Tokyo and a machine in Antigonish both resolve that identifier to the same place, with no ambiguity about which Halifax is meant.

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

