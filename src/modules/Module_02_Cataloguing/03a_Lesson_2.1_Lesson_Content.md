# Lesson 2.1 — Codicological Description and Hand-Authoring the TEI Header

*RELS 398 / ENGL 398 · Topic 2: Cataloguing · Meeting #3 (Tue Sep 8)*

*Step 1 of the three-step cycle: manual ground truth. Today you hand-write a complete TEI Header and manuscript description (<msDesc>) for your chosen full-page witness in VS Code without automated schema autocomplete or AI. What you type with your own fingers becomes the authoritative baseline against which Wednesday's deterministic schema validation and Friday's AI metadata extraction will be tested and scored.*

---

## **01 Content**

**The Detective Problem: Why Ancient Books Don't Have Barcodes**

Pick up any paperback on your desk, flip to the back cover, and you will find a neat barcode accompanied by an ISBN. Flip inside to the copyright page, and you will see a publisher, a city, a publication year, Library of Congress catalog numbers, and a copyright notice. Everything about a modern mass-produced book is designed to be instantly indexed by automated global systems. If ten thousand students buy the same edition of a novel, every single copy has the identical page numbers, the identical typos, and the identical font.

Now look at the high-resolution image of the manuscript page you chose on Friday. 

There is no barcode. There is no title page. There is no copyright declaration, no page number, and often not even an author's name attached to the text. Surviving ancient and medieval manuscripts are one-of-a-kind physical survivors. Each codex was crafted by hand from animal skin or papyrus reeds, copied by a flesh-and-blood human being whose handwriting changed when they were tired, and rebound, trimmed, or damaged across centuries of war, fire, and library migrations. If a modern cataloguer simply slaps a single author and title on a manuscript, they erase 90% of what that physical object actually is. To study a historical document computationally, we first have to solve a detective problem: how do we describe a unique material artifact so that both human scholars and computer programs can find, understand, and trust it?

**Vocabulary.** *Codex* — a historical book made of folded sheets bound together at the spine (replacing the ancient scroll). *Bibliographic metadata* — structured information identifying what a text is, who created it, and where it lives.

**Takeaway:** Modern books are mass-produced and standardized, but historical manuscripts are unique material artifacts that require structured codicological descriptions instead of simple title-author tags.

---

## **02 Content**

**Cracking the Code: The Mystery of Library Shelfmarks**

When scholars refer to manuscripts, they speak in what sounds like secret code: *Vat. gr. 2121*, *Cotton Nero A.x*, *P.Oxy. 840*, or *Sinai gr. 1186*. To a newcomer, these strings of letters and numbers look like cryptic passwords. In reality, they are historical street addresses known as *shelfmarks* (or call numbers).

A shelfmark tells the story of where a physical book was shelved. In the Vatican Library (Biblioteca Apostolica Vaticana), *Vat. gr. 2121* means: the Vatican collection (*Vat.*), Greek language manuscript (*gr.*), item number 2121. In the British Library, the famous Cotton collection was originally organized in a room where bookcases were topped with busts of Roman emperors; *Cotton Nero A.x* (which preserves the unique copy of *Sir Gawain and the Green Knight*) was literally kept in the bookcase under Emperor Nero's bust, on top shelf A, tenth book from the left.

While shelfmarks are evocative pieces of library history, they pose a serious computational headache. What happens if a library moves a book, renumbers a collection, or changes its cataloguing dialect? How does an automated search engine in Antigonish know that "Vatican Greek 2121", "Vat. gr. 2121", and "BAV Vat.gr.2121" refer to the exact same physical volume in Rome? The answer is standardization. In digital editions, we record the traditional human shelfmark alongside persistent global identifiers (like CTS URNs and Trismegistos IDs) so that our references never break.

**Vocabulary.** *Shelfmark* — the unique identifier or call number assigned to a specific physical manuscript volume by its holding library. *Persistent identifier (PID)* — a permanent, machine-actionable web address that uniquely identifies a cultural object.

**Takeaway:** Shelfmarks are physical library call numbers with deep historical roots; digital editions anchor them with permanent web identifiers to prevent broken citations.

---

## **03 Content**

**What is a TEI Header? The Digital Passport of Your Page**

Think of a standard digital document — an HTML web page or a plain text file. At its simplest, it is just words on a screen. If you send that file to someone else, they have no built-in way of knowing who transcribed it, what library holds the original manuscript, what software was used, or whether they have permission to quote it in their own research.

Enter the **TEI Header**.

The Text Encoding Initiative (TEI) established a universal rule for scholarly electronic texts: every single digital edition must begin with a structured metadata envelope called the `<teiHeader>`. Think of the TEI Header as the official passport, birth certificate, and provenance dossier of your digital text. Before any of your manuscript transcription begins, the header formally documents:

1. What digital file this is and who edited it.
2. What license governs its reuse (putting FAIR principles into code).
3. The complete physical description of the manuscript witness resting in the library vault.
4. A dated changelog recording every single edit made to the file over time.

Because the header uses standardized XML tags recognized across the globe, any search engine, library repository, or computational pipeline can read your header and immediately understand what your edition represents.

**Vocabulary.** *TEI Header (`<teiHeader>`)* — the mandatory opening structural element in every TEI XML file that contains all bibliographic, codicological, and editorial metadata. *Machine-actionable* — structured so that computer algorithms can parse, query, and process the data without human intervention.

**Takeaway:** The TEI Header is the digital passport of your edition, packaging its authorship, open license, and physical manuscript details into a universally understood XML envelope.

---

## **04 Content**

**Why We Type XML by Hand (Tuesday's Ground Truth)**

In this morning's lab, you will open Visual Studio Code and type out an entire TEI Header character by character, angle bracket by angle bracket. There will be no autocomplete filling in tags for you, no red squiggles correcting your typos, and no AI prompt writing the code on your behalf. 

Why do we force you to type raw markup by hand?

When software autocompletes your tags or an AI generates markup for you, it hides the machine logic. You see a finished product without understanding the tree structure underneath. Even worse: AI language models are notorious for inventing plausible-sounding but completely illegal XML tags or hallucinating manuscript shelfmarks. If you don't know the syntax in your own fingers, you will never spot the AI's subtle hallucinations.

In this course, Tuesday is always **Step 1: Manual Ground Truth**. Hand-authoring forces you to make every structural decision deliberately. You have to decide whether that note in your manuscript margin is an owner's scribbled signature, a corrected spelling, or a liturgical instruction. What you produce today by hand will serve as your gold standard — the human baseline against which tomorrow's automated schema validator and Friday's AI model will be scored.

**Vocabulary.** *Ground truth* — empirical, human-verified baseline data against which automated scripts and machine learning models are evaluated. *Syntax* — the formal grammar rules that govern how a computer language or markup system must be written.

**Takeaway:** Hand-typing your first TEI Header builds the mental model and muscle memory required to catch AI hallucinations and automated parser errors.

---

## **05 Content**

**The XML Tree: Trunks, Branches, and Leaves**

XML (Extensible Markup Language) is often described in intimidating language, but its core architecture is as simple and organic as a tree. 

An XML document is a hierarchy of boxes inside boxes. Everything starts at the root (the trunk). From that root sprout major sections (branches), which divide into subsections (twigs), which finally hold the actual text (leaves). 

Every piece of information in XML is enclosed in **elements**. An element begins with an opening tag (`<tag>`) and ends with a matching closing tag (`</tag>`). The slash `/` is critical — it tells the parser that this box is now closed.

```xml
<manuscript>
    <support>parchment</support>
    <date>11th century</date>
</manuscript>
```

Here, `<manuscript>` is the parent branch. `<support>` and `<date>` are child elements living inside it. If you close an outer tag before closing an inner tag (like `<manuscript><date>11th century</manuscript></date>`), the tree breaks. XML parsers do not forgive structural overlap. It is clean, strict, and nested.

**Vocabulary.** *Element* — an XML building block composed of an opening tag, content, and a closing tag. *Nesting* — placing one element entirely inside another element without overlapping boundaries. *Root element* — the single outermost element that encloses the entire XML document.

**Takeaway:** XML is a strictly nested tree hierarchy where every opened element must be properly closed within its parent container.

---

## **06 Content**

**Elements, Attributes, and Case Sensitivity**

Inside our XML tree, elements do the heavy lifting of defining *structure*, but **attributes** provide *metadata* about those elements.

An attribute lives inside the opening tag of an element, written as a name followed by an equals sign and a value in quotes: `name="value"`. For example:

```xml
<title level="m" xml:lang="grc">Codex Marchalianus</title>
```

Here, `<title>` is the element. `level="m"` is an attribute specifying that this is a monograph/manuscript title, and `xml:lang="grc"` specifies that the title is in Ancient Greek.

Three ironclad rules to burn into your memory today:

1. **Attribute values MUST always be inside quotes**: `extent="full-page"` is valid; `extent=full-page` crashes the parser immediately.
2. **XML is case-sensitive**: `<teiHeader>` is not the same as `<teiheader>` or `<TEIHEADER>`. In the TEI standard, element names use specific camelCase conventions.
3. **Reserved characters must be escaped**: You cannot casually type `<` or `&` inside your text, because XML thinks they are code. An ampersand must be written as `&amp;`, and a less-than sign as `&lt;`.

**Vocabulary.** *Attribute* — a name-value property placed inside an element's start tag that adds metadata or identifiers to that element. *Case-sensitive* — treating uppercase and lowercase letters as entirely distinct characters.

**Takeaway:** Elements define structure; attributes add metadata inside start tags; quotes around attribute values and exact casing are non-negotiable.

---

## **07 Content**

**The Document Envelope: `<TEI>` and `<teiHeader>`**

Every TEI file you create this term will have the exact same top-level architecture. At the root of the file sits the `<TEI>` element. Inside `<TEI>`, there are exactly two main children:

```xml
<TEI xmlns="http://www.tei-c.org/ns/1.0">
    <teiHeader>
        <!-- All metadata about the file and the manuscript goes here -->
    </teiHeader>
    <text>
        <body>
            <!-- The actual manuscript transcription goes here in Week 4 -->
        </body>
    </text>
</TEI>
```

The attribute `xmlns="http://www.tei-c.org/ns/1.0"` is the XML Namespace declaration. It tells any computer in the world: *"The tags inside this file follow the official Text Encoding Initiative Guidelines version 5."*

Notice the clean division of labor. The `<teiHeader>` handles the *scholarship about the object* (metadata). The `<text>` element handles the *transcription of the object* (data). Today we focus entirely on the `<teiHeader>` — laying the architectural foundation before we transcribe a single Greek letter.

**Vocabulary.** *XML Namespace (`xmlns`)* — a unique URI declaring which vocabulary and schema standard governs the tags in an XML document. *Separation of concerns* — keeping descriptive metadata cleanly separated from transcription data.

**Takeaway:** Every TEI document wraps its metadata inside `<teiHeader>` and its transcription inside `<text>`, unified under the root `<TEI>` envelope.

---

## **08 Content**

**The Four Pillars of the Header**

When you open the `<teiHeader>`, you encounter four core functional zones. Think of them as the four pillars holding up your edition:

```xml
<teiHeader>
    <fileDesc>       <!-- 1. The File Description (Mandatory) -->
    <encodingDesc>   <!-- 2. The Encoding Principles (How you tagged it) -->
    <profileDesc>    <!-- 3. The Non-Bibliographic Profile (Language, hand) -->
    <revisionDesc>   <!-- 4. The Revision History (Who changed what, when) -->
</teiHeader>
```

1. **`<fileDesc>` (File Description)**: The absolute heart of the header. It describes your digital edition as an electronic file, and it houses the codicological description of the ancient manuscript itself. You cannot have a valid TEI file without it.
2. **`<encodingDesc>` (Encoding Description)**: Documents your editorial methods — for example, whether you normalized ancient spelling or transcribed abbreviations as symbols.
3. **`<profileDesc>` (Profile Description)**: Records contextual details like languages used (e.g. Ancient Greek, Latin) and hand definitions.
4. **`<revisionDesc>` (Revision Description)**: A structured historical changelog recording every major milestone in your project.

Today, 80% of our practical work will take place inside `<fileDesc>`.

**Vocabulary.** *`<fileDesc>`* — the mandatory TEI header element that contains full bibliographic and codicological descriptions of both the digital file and the source artifact. *`<revisionDesc>`* — the log of editorial changes and version history.

**Takeaway:** The TEI Header divides metadata into four clear zones: file description, encoding methods, language profile, and revision history.

---

## **09 Content**

**Giving Yourself Credit: `<fileDesc>` and `<titleStmt>`**

Inside `<fileDesc>`, our first major task is to establish who created this electronic edition. This is handled by `<titleStmt>` (Title Statement).

When you build a digital edition in this course, you are not just doing classroom homework; you are creating an open, citable scholarly artifact. You are the digital editor. Here is how that looks in TEI XML:

```xml
<titleStmt>
    <title>Digital Scholarly Edition of Vat. gr. 2121, Folio 213r</title>
    <author>Anonymous Scribe</author>
    <editor>
        <forename>Jane</forename>
        <surname>Doe</surname>
    </editor>
    <respStmt>
        <resp>Transcription and TEI encoding</resp>
        <name>Jane Doe</name>
    </respStmt>
    <sponsor>St. Francis Xavier University</sponsor>
    <funder>Department of Religious Studies / Digital Humanities Lab</funder>
</titleStmt>
```

Notice how specific this is. We distinguish between the original `<author>` of the ancient text and the modern `<editor>` who produced the digital edition. The `<respStmt>` (Responsibility Statement) explicitly states who did what. In collaborative digital projects with dozens of researchers, this transparency ensures that student researchers receive clear, permanent attribution for their markup.

**Vocabulary.** *`<titleStmt>`* — the element within `<fileDesc>` that groups information about the title of a work and those responsible for its intellectual content. *`<respStmt>`* — statement of responsibility indicating specific scholarly contributions.

**Takeaway:** `<titleStmt>` establishes your academic authorship and intellectual responsibility as the digital editor of the witness.

---

## **10 Content**

**Putting FAIR into Practice: `<publicationStmt>`**

Last week you learned the FAIR principles: research data must be *Findable, Accessible, Interoperable, and Reusable*. 

Where does "Reusable" actually get declared in code? Right inside `<publicationStmt>`.

If you publish a digital text online without an explicit license, standard copyright laws apply by default — meaning nobody else has the legal right to reuse your XML, train an HTR model on your transcriptions, or include your work in a broader corpus. In open digital humanities, we reject proprietary paywalls. We license our editions under Creative Commons open licenses:

```xml
<publicationStmt>
    <publisher>St. Francis Xavier University Digital Humanities Hub</publisher>
    <pubPlace>Antigonish, Nova Scotia</pubPlace>
    <date when="2026">2026</date>
    <availability status="free">
        <licence target="https://creativecommons.org/licenses/by/4.0/">
            Distributed under an open Creative Commons Attribution 4.0 International (CC BY 4.0) License.
        </licence>
    </availability>
</publicationStmt>
```

By adding this block to your header, you give scholars everywhere legal permission to read, analyze, and build upon your edition, provided they give you credit. That is FAIR scholarship in action.

**Vocabulary.** *`<publicationStmt>`* — the element that details the publication, distribution, and licensing conditions of the digital file. *Creative Commons (CC BY)* — a standard open-access license permitting free sharing and adaptation with attribution.

**Takeaway:** `<publicationStmt>` secures the reusability of your scholarship by explicitly declaring open-access distribution and licensing terms.

---

## **11 Content**

**The Codicological Heart: `<sourceDesc>`**

Now we reach the pivot point of the entire header: `<sourceDesc>` (Source Description).

Up to this point, `<fileDesc>` has been describing the *digital file* — you sitting at your laptop in Mulroney Hall in 2026. But a digital edition is an edition *of* something. What physical object did your text come from?

If your edition were based on a modern printed book, `<sourceDesc>` would contain a standard `<bibl>` tag with publisher, ISBN, and page numbers. But because your project is built upon a unique, handwritten ancient artifact, TEI gives us a specialized, powerhouse element: **`<msDesc>` (Manuscript Description)**.

```xml
<sourceDesc>
    <msDesc>
        <!-- The complete physical and historical biography of your codex -->
    </msDesc>
</sourceDesc>
```

Inside `<msDesc>`, we document the entire physical and historical reality of the manuscript: its library shelfmark, its physical material, its scribal hand, its dimensions, its ruling, and its historical journey.

**Vocabulary.** *`<sourceDesc>`* — records details of the source material from which an electronic text was derived. *`<msDesc>`* — the TEI manuscript description module used to catalogue unique codices, scrolls, and inscriptions.

**Takeaway:** `<sourceDesc>` houses the `<msDesc>` module, shifting our focus from the digital file to the physical reality of the surviving manuscript.

---

## **12 Content**

**Anchoring the Object: `<msIdentifier>`**

How do you guarantee that anyone in the world can identify the exact physical book your edition is based on? You anchor it with a standardized `<msIdentifier>` block.

The `<msIdentifier>` represents the administrative coordinates of the artifact. It moves logically from the broadest geographic location down to the specific shelfmark:

```xml
<msIdentifier>
    <settlement>Vatican City</settlement>
    <repository>Biblioteca Apostolica Vaticana</repository>
    <collection>Vaticani graeci</collection>
    <idno type="shelfmark">Vat. gr. 2121</idno>
    <altIdentifier type="trismegistos">
        <idno>62345</idno>
    </altIdentifier>
</msIdentifier>
```

- `<settlement>`: The city where the library is located.
- `<repository>`: The official institution or library holding the manuscript.
- `<collection>`: The specific collection within that library.
- `<idno>`: The official identification number or shelfmark.

Notice the `<altIdentifier>` tag: here we link our physical shelfmark to a global database number (like Trismegistos or Pinakes). This guarantees that even if the library renames a collection, our edition remains permanently linked to global manuscript authority files.

**Vocabulary.** *`<msIdentifier>`* — groups the identifying information (city, repository, collection, shelfmark) that uniquely designates a manuscript. *Authority file* — an international registry of standardized names and identifiers for cultural artifacts.

**Takeaway:** `<msIdentifier>` establishes unambiguous physical coordinates for your manuscript, pairing library shelfmarks with global authority IDs.

---

## **13 Content**

**What's on the Page? `<msContents>` and `<msItem>`**

Once we have established *which* manuscript we have, we must record *what text* it contains. This is governed by `<msContents>` and its child element `<msItem>`.

A single medieval codex might contain fifty different texts: three homilies, a commentary on the Psalms, a liturgical calendar, and a copy of the Book of Genesis. In your project, you are focusing on your **full-page witness**. Inside `<msItem>`, you document the boundaries and authorial identity of that specific text:

```xml
<msContents>
    <msItem n="1">
        <locus from="213r" to="213r">f. 213r</locus>
        <author key="LXX">Septuagint</author>
        <title xml:lang="grc">Γένεσις</title>
        <title xml:lang="en">Book of Genesis</title>
        <textLang mainLang="grc">Ancient Greek</textLang>
        <rubric>ΑΡΧΗ ΤΗΣ ΓΕΝΕΣΕΩΣ</rubric>
    </msItem>
</msContents>
```

Look at the `<locus>` element. The word *locus* is Latin for "place" — it tells the reader exactly which folio or page your witness spans. The `<rubric>` tag records any special text written in red ink, such as a traditional heading.

**Vocabulary.** *`<msContents>`* — describes the intellectual contents of a manuscript or manuscript part. *`<locus>`* — defines the precise page, folio, or line coordinates where a text appears within a volume. *Rubric* — text written in red ink to signal a title, section start, or liturgical instruction.

**Takeaway:** `<msContents>` maps the intellectual works preserved on your manuscript page, anchoring their titles, languages, and folio coordinates.

---

## **14 Content**

**Materiality and Support: Animal Skin vs. River Reeds**

Now we open `<physDesc>` (Physical Description). This is where digital humanities becomes deeply tactile. We are not describing abstract bits and bytes; we are describing a physical object that survived centuries of history.

The foundation of any manuscript is its **support material** — what is it written on?

```xml
<physDesc>
    <objectDesc form="codex">
        <supportDesc material="parchment">
            <support>
                <p>Prepared calfskin vellum of medium thickness, scraped smooth on the flesh side with visible follicle pores on the hair side.</p>
            </support>
        </supportDesc>
    </objectDesc>
</physDesc>
```

Historical manuscripts generally fall into three great material categories:

1. **Papyrus** (`material="papyrus"`): Ancient paper made from the sliced pith of Nile river reeds. Common in ancient Egypt and the Greco-Roman world; fibrous, brittle, and preserved primarily in arid climates.
2. **Parchment / Vellum** (`material="parchment"`): Specially prepared animal skin (calf, sheep, or goat) scraped thin, stretched on frames, and treated with lime. Extremely durable, flexible, and capable of being erased and written over.
3. **Paper** (`material="paper"`): Rag paper made from linen fibers, introduced to Europe from the Islamic world in the high Middle Ages.

When you look at high-resolution images of parchment, you can often tell the difference between the yellow-tinted "hair side" (which has tiny follicle dots) and the pale, smooth "flesh side"!

**Vocabulary.** *Support* — the physical material (parchment, papyrus, paper) that carries the written text. *Hair side / Flesh side* — the two distinct surfaces of animal skin parchment, differing in color, texture, and pore patterns.

**Takeaway:** `<supportDesc>` captures the tactile medium of your witness, distinguishing between fragile Egyptian papyrus, durable parchment vellum, and late medieval rag paper.

---

## **15 Content**

**Leaves, Folios, and Pages: The Geometry of a Codex**

When you read a modern book, you turn "pages" — page 1, page 2, page 3. But ancient and medieval scribes did not number individual pages; they numbered **leaves** (in Latin, *folia*).

A **folio** is a single sheet of parchment or paper bound into a book. Each folio has two sides:

- **Recto (r)**: The front side of the leaf, facing you on the right when the book is open.
- **Verso (v)**: The back side of the leaf, revealed when you turn the page over (facing you on the left).

Therefore, a manuscript with 100 leaves does not have page numbers 1 to 200. It has:
*Folio 1r, Folio 1v, Folio 2r, Folio 2v, Folio 3r ...*

In your course project, your primary witness is a **full-page textual artifact**. That means your witness is identified as either a complete *recto* or a complete *verso* (e.g. `f. 213r` or `f. 45v`). In your TEI Header, you record this extent:

```xml
<extent>
    <measure unit="leaf" quantity="1">1 folio (recto)</measure>
    <dimensions unit="mm" type="leaf">
        <height>285</height>
        <width>210</width>
    </dimensions>
</extent>
```

**Vocabulary.** *Folio (f.)* — an individual leaf of a codex. *Recto (r)* — the front side of a folio. *Verso (v)* — the back side of a folio. *Extent* — the physical size and quantity of leaves comprising a manuscript or document section.

**Takeaway:** Manuscripts are counted by folios rather than pages, where each physical leaf consists of a front face (recto) and a back face (verso).

---

## **16 Content**

**How Codices Were Assembled: Quires and Gatherings**

Before a scribe could write a single word, someone had to build the physical book. 

Medieval books were not made by binding individual loose sheets. Scribes took large pieces of animal skin, folded them in half (forming a *bifolio* or two-leaf booklet), and nested several bifolia together inside one another like a stack of greeting cards. This folded booklet is called a **quire** or a **gathering**.

The most popular gathering was the **quaternion** — four bifolia nested together to produce eight leaves (16 pages). 

Scribes cared deeply about aesthetics. To ensure that open openings looked harmonious, they followed **Gregory's Rule** (the law of facing sides): hair side always faced hair side, and flesh side always faced flesh side. When you open a well-made Greek or Latin codex, both facing pages share the exact same pale ivory hue!

In TEI XML, quire structure is encoded inside `<collation>`:

```xml
<collation>
    <p>Composed primarily of regular quaternions (gatherings of 8 leaves). Quire signatures marked in Greek numerals in the lower inner margin.</p>
</collation>
```

**Vocabulary.** *Quire / Gathering* — a group of folded leaves nested together and sewn through the crease to form a section of a codex. *Bifolio* — a single sheet folded in half to create two leaves (four pages). *Gregory's Rule* — the scribal practice of matching parchment openings so that hair side faces hair side and flesh side faces flesh side.

**Takeaway:** Codices are constructed from nested folded gatherings called quires, arranged with deliberate aesthetic symmetry according to Gregory's Rule.

---

## **17 Content**

**Ruling the Page: The Invisible Geometry of Scribes**

If you have ever tried to write on a completely blank sheet of unlined paper, you know that handwriting naturally drifts upward or downward. Medieval scribes could not afford crooked lines on expensive parchment. Before writing, they laid down a precise geometric grid.

Scribes used a sharp awl to prick tiny puncture holes along the outer margins of the parchment (a process called *pricking*). Then, using a straightedge, they scored lines across the leaf to guide their pens (called *ruling*).

Ruling was executed in two primary ways:

1. **Dry point**: Pressing a hard, blunt stylus into the parchment, creating an embossed furrow on one side and a raised ridge on the other.
2. **Lead point / Hard point**: Drawing faint grey lines using a lead pencil-like stylus.

When you inspect your full-page witness under high-resolution zoom, look closely between the lines of text. Can you see the faint horizontal ruling lines? Can you see the vertical *bounding lines* that keep the left and right margins razor-sharp?

**Vocabulary.** *Pricking* — tiny puncture marks made in the margins of parchment leaves to guide the ruling process. *Ruling* — the scored or drawn horizontal lines and vertical bounding margins that organize the text on a manuscript page.

**Takeaway:** Scribes used pricking and ruling to construct an architectural grid on blank parchment before writing a single word.

---

## **18 Content**

**Layout Architecture: Columns, Margins, and `<layoutDesc>`**

Manuscript pages are not all organized the same way. The spatial arrangement of text across a page is called its **layout**.

In the `<layoutDesc>` section of the TEI Header, we encode:

- How many columns of text are on the page (`columns="1"`, `columns="2"`, etc.).
- How many written lines are in each column (`writtenLines="25"`).
- Whether there are wide outer margins reserved for commentary or student notes.

```xml
<layoutDesc>
    <layout columns="1" writtenLines="28">
        <p>Single column of 28 lines, written in brown carbon ink below the top ruled line. Wide outer margins measuring approximately 45mm, containing occasional contemporary glosses.</p>
    </layout>
</layoutDesc>
```

Early uncial manuscripts of the Bible (like *Codex Sinaiticus*) were famous for having four narrow columns per page, resembling open scroll columns! By the eleventh century, many Byzantine minuscules adopted elegant single-column or double-column formats.

**Vocabulary.** *`<layoutDesc>`* — groups information regarding the physical arrangement of text on the page, including columns, lines, and margins. *Bounding lines* — vertical ruled lines that demarcate the margins and keep text justified.

**Takeaway:** `<layoutDesc>` records the spatial arrangement of the page, specifying column counts, written line counts, and margin dimensions.

---

## **19 Content**

**The Human Touch: Scribes, Hands, and `<handDesc>`**

A manuscript page is an intimate human record. When you look at the ink strokes, you are seeing the personal motor habits of an individual scribe who lived centuries ago.

In paleography (the study of ancient handwriting), we use the word **hand** to describe the handwriting of a specific scribe. A single codex might be copied by three different scribes, or a primary scribe might write the main biblical text while a later corrector writes corrections above the line.

Inside `<handDesc>`, we formally document every distinct hand visible on your full-page witness:

```xml
<handDesc hands="1">
    <handNote xml:id="h1" scope="sole" script="Byzantine_minuscule">
        <p>Primary hand: neat 11th-century Byzantine minuscule script written in dark brown carbon ink, with consistent letter heights and standard ligature sets.</p>
    </handNote>
</handDesc>
```

By assigning an `xml:id="h1"` to this hand, we create a computational hook! In Week 4, when you transcribe individual words or marginal corrections, you can tag them with `hand="#h1"`. Automated scripts can then instantly count how many words were written by the primary scribe versus later correctors!

**Vocabulary.** *Paleography* — the scholarly study of historical handwriting, scripts, and decipherment. *Hand (`<handNote>`)* — the distinct handwriting style of an individual scribe or annotator. *Ligature* — two or more letters connected together into a single fluid stroke.

**Takeaway:** `<handDesc>` defines the individual scribal hands on a page and assigns them unique XML IDs that link directly to transcription tags.

---

## **20 Content**

**Rubrication and Visual Hierarchy: `<decoDesc>`**

Look at your manuscript image. Is every word written in plain black ink, or do certain headings, initial letters, or chapter markers leap off the page in bright red, gold, or blue?

This decorative and functional hierarchy is called **rubrication** (from the Latin *ruber*, meaning "red"). 

In ancient and medieval book production, the main scribe copied the bulk of the text in dark carbon or gall ink, leaving blank spaces wherever an initial capital or chapter title belonged. Later, a specialist (the rubricator or illuminator) went through the book with red vermilion or minium ink to paint the headings, liturgical markers, and decorative initials.

In the TEI Header, decoration is captured under `<decoDesc>`:

```xml
<decoDesc>
    <decoNote type="initial">
        <p>One prominent 3-line initial capital in red ink at the start of Genesis 1:1, decorated with modest foliate penwork.</p>
    </decoNote>
</decoDesc>
```

Rubrics were not just pretty pictures; they were the user interface of the medieval codex! They allowed a reader to scan a dense parchment leaf and instantly find the beginning of a liturgical reading or chapter.

**Vocabulary.** *Rubrication* — the practice of writing titles, headings, and initial letters in red ink to establish visual hierarchy. *`<decoDesc>`* — describes the decorative elements of a manuscript, including miniatures, decorated initials, and marginal drawings.

**Takeaway:** Rubrication and decorative initials served as the visual user interface of historical manuscripts, recorded in TEI under `<decoDesc>`.

---

## **21 Content**

**The Scars of Time: Physical Condition and Damage**

A manuscript that has survived for eight hundred or two thousand years has lived a dangerous life. It has survived damp monastic scriptoria, hungry mice, insect larvae, soot from oil lamps, careless bookbinders, and wartime looting.

When you catalogue a manuscript, you must record its physical condition under `<condition>` inside `<supportDesc>`:

```xml
<condition>
    <p>Parchment leaf is in good structural condition. Moderate ink flaking along lines 12–14 due to moisture exposure. Upper outer margin trimmed during 17th-century rebinding, slightly clipping a marginal note.</p>
</condition>
```

Common types of physical damage to look for on your full-page witness:

- **Flaking**: Ink separating and falling off brittle parchment surfaces.
- **Foxing & Staining**: Brown spots caused by fungal mold or oxidation.
- **Cropping**: When 16th- or 17th-century bookbinders rebound ancient books, they often used large guillotines to slice the page edges, accidentally cutting off ancient marginal annotations!
- **Wormholes**: Circular tunnels eaten through parchment sheets by wood-boring beetle larvae.

Documenting damage is essential for text editing: if a letter is missing in your transcription, your condition report explains whether it was omitted by the scribe or eaten by an insect.

**Vocabulary.** *`<condition>`* — describes the physical state of preservation of a manuscript leaf, including damage, wear, and repairs. *Cropping* — the trimming of page margins during rebinding that often damages marginal notes.

**Takeaway:** `<condition>` records physical wear, moisture damage, and binder cropping, providing the physical explanation for lost or illegible text.

---

## **22 Content**

**The Book's Biography: `<history>` and `<origin>`**

Every manuscript has a life story. It was commissioned by someone, copied in a specific place at a specific time, bought, sold, bequeathed, inherited, stolen, and eventually catalogued in a modern research library.

This historical journey is documented in the `<history>` container of the TEI Header.

Within `<history>`, our first question is: *Where and when was this manuscript born?* This is recorded in `<origin>`:

```xml
<history>
    <origin>
        <origDate notBefore="1000" notAfter="1099">11th century</origDate>
        <origPlace ref="https://pleiades.stoa.org/places/520998">Constantinople</origPlace>
    </origin>
</history>
```

Look at the attributes in `<origDate>`: `notBefore="1000"` and `notAfter="1099"`. This is how digital humanists handle historical uncertainty! You may not know the exact Tuesday in the year 1042 when the scribe put down their pen, but paleographical evidence tells you the script belongs to the eleventh century. The `notBefore` and `notAfter` attributes translate fuzzy human dates into machine-queryable ISO numbers.

**Vocabulary.** *`<history>`* — groups elements concerning the complete historical development of a manuscript. *`<origin>`* — records the date and place of production of a manuscript. *Machine-queryable dating* — using standardized attributes (`notBefore`, `notAfter`, `when`) to enable computer chronological filtering.

**Takeaway:** `<origin>` records when and where a manuscript was created, converting historical date ranges into machine-queryable attributes.

---

## **23 Content**

**The Custodial Chain: `<provenance>` and Acquisition**

After a manuscript leaves the scribe's desk, who owned it?

The documented chain of custody of a cultural artifact is called its **provenance** (from the French *provenir*, "to come from"). A manuscript might have spent four centuries in a monastery on Mount Athos, was purchased by a Venetian ambassador in 1580, bequeathed to a French cardinal in 1650, and finally seized during the French Revolution to enter the Bibliothèque nationale de France in Paris.

In the TEI Header, each step in this historical journey is recorded in a `<provenance>` element:

```xml
<provenance notBefore="1500" notAfter="1550">
    <p>Belonged to the Monastery of Saint John the Theologian on Patmos, as indicated by a 16th-century Greek ex-libris inscription on folio 1v.</p>
</provenance>
<provenance notBefore="1600" notAfter="1650">
    <p>Acquired in Rome by Cardinal Lelio Biscia (1575–1638); arms stamped in gold on the leather binding.</p>
</provenance>
<acquisition when="1640">
    <p>Entered the Vatican Library following Cardinal Biscia's bequest in 1640.</p>
</acquisition>
```

Provenances often leave physical evidence on the page: scribbled ex-libris notes ("This book belongs to Brother Peter"), library stamps, coat-of-arms bookplates, and auction numbers.

**Vocabulary.** *Provenance* — the chronological history of ownership, custody, and location of a historical artifact. *Ex-libris* — a Latin phrase ("from the books of") denoting an ownership inscription or bookplate. *`<acquisition>`* — details how a repository officially acquired the manuscript.

**Takeaway:** `<provenance>` traces the custodial chain of custody from medieval monastic collections into modern research libraries.

---

## **24 Content**

**Connecting to Linked Open Data: CTS URNs and Trismegistos**

One of the great promises of digital humanities is **Linked Open Data** — the idea that cultural heritage records across the globe should connect to one another like links on the web.

If your TEI file simply says "Constantinople", a computer has to guess whether you mean the ancient Byzantine capital, a village in Ohio, or a book publisher. But if you connect your place name to a Linked Data URI (like Pleiades: `https://pleiades.stoa.org/places/520998`), the computer knows with mathematical certainty exactly which geographic coordinates on Earth you are referring to.

For ancient texts, the gold standard for linked identification is the **Canonical Text Service (CTS) URN**:

```xml
urn:cts:greekLit:tlg0527.tlg001.opp-grc1:1.1-1.14
```

This compact string breaks down like a universal postal code:

- `urn:cts:greekLit`: The ancient Greek literary text collection.
- `tlg0527`: The author identifier (Septuagint).
- `tlg001`: The work identifier (Genesis).
- `opp-grc1`: The specific edition or witness expression.
- `1.1-1.14`: The precise passage citation (Chapter 1, verses 1–14).

By embedding CTS URNs and Trismegistos IDs in your TEI Header, your edition becomes an active node in a worldwide computational network of classical and historical scholarship.

**Vocabulary.** *Linked Open Data (LOD)* — structured data published on the web so that it can be automatically interlinked across independent repositories. *Canonical Text Service (CTS) URN* — a uniform resource name that identifies a specific ancient text passage independently of any single printed book.

**Takeaway:** Linking names and texts to global URIs (like Pleiades and CTS URNs) transforms your isolated file into an interoperable node in the global web of scholarship.

---

## **25 Content**

**The Full `<msDesc>` Architecture: The Master Blueprint**

Now let us step back and look at the complete architectural blueprint of `<msDesc>`. When all the pieces fit together, here is how the manuscript description is organized inside your `<teiHeader>`:

```xml
<sourceDesc>
    <msDesc>
        <msIdentifier>
            <!-- 1. Where is it? (Settlement, Library, Shelfmark) -->
        </msIdentifier>
        <msContents>
            <!-- 2. What text is on this page? (Locus, Title, Author) -->
        </msContents>
        <physDesc>
            <!-- 3. What does it physically feel and look like? -->
            <objectDesc form="codex">
                <supportDesc material="parchment">
                    <extent> <!-- Leaves, Dimensions --> </extent>
                    <condition> <!-- Wear, Tears, Damage --> </condition>
                </supportDesc>
                <layoutDesc>
                    <!-- Columns, Lines, Margins -->
                </layoutDesc>
            </objectDesc>
            <handDesc>
                <!-- Scribes, Handwriting, Inks -->
            </handDesc>
            <decoDesc>
                <!-- Initials, Rubrication, Art -->
            </decoDesc>
        </physDesc>
        <history>
            <!-- 4. How did it get here? (Origin, Provenance, Acquisition) -->
        </history>
    </msDesc>
</sourceDesc>
```

Notice the beautiful internal logic. It moves from **identity** (`<msIdentifier>`), to **textual contents** (`<msContents>`), to **material physics** (`<physDesc>`), to **historical journey** (`<history>`). Every single physical observation you make about your manuscript page has a designated, unambiguous home.

**Vocabulary.** *Schema architecture* — the structural design and relationship of elements within a formal data model. *Coherence* — the logical organization of data from identification to physical description to historical lifecycle.

**Takeaway:** The `<msDesc>` module follows an intuitive four-part journey: administrative identity, textual contents, physical description, and historical provenance.

---

## **26 Content**

**Annotated Template for Your Primary Witness Header**

To help you hand-author your header today, here is the clean, annotated starter template for your primary witness. You will adapt this template in VS Code, replacing the placeholder values with the real facts from your chosen full-page artifact:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
    <teiHeader>
        <fileDesc>
            <titleStmt>
                <title>Digital Edition of [Shelfmark], Folio [Folio]</title>
                <editor>
                    <forename>[Your First Name]</forename>
                    <surname>[Your Last Name]</surname>
                </editor>
                <sponsor>St. Francis Xavier University</sponsor>
            </titleStmt>
            <publicationStmt>
                <publisher>StFX Digital Humanities</publisher>
                <date when="2026">2026</date>
                <availability status="free">
                    <licence target="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</licence>
                </availability>
            </publicationStmt>
            <sourceDesc>
                <msDesc>
                    <msIdentifier>
                        <settlement>[City]</settlement>
                        <repository>[Library]</repository>
                        <idno type="shelfmark">[Shelfmark]</idno>
                    </msIdentifier>
                    <msContents>
                        <msItem>
                            <locus>[e.g. f. 213r]</locus>
                            <title>[Work Title]</title>
                            <textLang mainLang="grc">Greek</textLang>
                        </msItem>
                    </msContents>
                    <physDesc>
                        <objectDesc form="codex">
                            <supportDesc material="parchment">
                                <extent>1 full folio page</extent>
                            </supportDesc>
                            <layoutDesc>
                                <layout columns="1" writtenLines="28"/>
                            </layoutDesc>
                        </objectDesc>
                        <handDesc>
                            <handNote xml:id="h1" script="minuscule"/>
                        </handDesc>
                    </physDesc>
                    <history>
                        <origin>
                            <origDate>[e.g. 11th century]</origDate>
                        </origin>
                    </history>
                </msDesc>
            </sourceDesc>
        </fileDesc>
    </teiHeader>
    <text>
        <body>
            <p><!-- Transcription will begin here in Week 4 --></p>
        </body>
    </text>
</TEI>
```

**Vocabulary.** *Starter template* — a validated skeletal code structure provided to guide student implementation. *Placeholder* — bracketed text indicating values that must be customized with empirical data.

**Takeaway:** This standardized starter template provides the skeletal envelope into which you will hand-type your primary witness details.

---

## **27 Content**

**The Top Five Traps for New XML Authors**

When writing XML by hand, humans make predictable errors. Because XML is a strict computational language, even a tiny typographic slip will break your document. Keep a sharp eye out for these top five beginner traps:

1. **The Missing Slash in the Closing Tag**: Writing `<title>Book of Genesis<title>` instead of `<title>Book of Genesis</title>`. Without that forward slash `/`, the parser thinks you opened a second title inside the first one!
2. **Mismatched Capitalization**: Typing `<teiheader>` to close an opened `<teiHeader>`. Remember: XML is strictly case-sensitive.
3. **Unquoted Attributes**: Writing `<layout columns=1>` instead of `<layout columns="1">`. Every attribute value in XML must be surrounded by quotation marks.
4. **Self-Closing Slashes in Void Elements**: Elements that have no text content inside them must be self-closed with a trailing slash: `<layout columns="1" writtenLines="25"/>`. If you omit the trailing slash (`<layout columns="1">`), the parser waits endlessly for a closing `</layout>` tag.
5. **Raw Ampersands**: Writing `Smith & Jones` instead of `Smith &amp; Jones`. If you need an ampersand, always write `&amp;`.

Tomorrow morning in Lesson 2.2, we will enable automated schema validation in VS Code to see how many of these traps caught you!

**Vocabulary.** *Self-closing tag* — an element without child text that closes itself with a trailing slash, such as `<lb/>` or `<milestone/>`. *Malformed XML* — markup that violates basic XML syntax rules, preventing parsers from building a valid tree.

**Takeaway:** Avoid the five classic traps: missing closing slashes, mismatched case, unquoted attributes, unclosed void tags, and unescaped ampersands.

---

## **28 Content**

**Hands-On in VS Code: Hand-Typing Your Witness Header**

Now open Visual Studio Code on your machine. Create a new file in your local course repository called:

`03a_Lesson_2.1_Primary_Witness_Header.xml`

Set up your workspace with your manuscript image on one side of your screen and VS Code on the other side. 

As you type out your `<teiHeader>`, inspect your full-page witness image carefully:

- Look at the top margin: is there an ancient folio number written in ink or pencil? Record it in `<locus>`.
- Count the lines of text in the column. Exactly how many lines are written on this leaf? Record it in `<layout writtenLines="nn">`.
- Look at the ink color. Is it jet black carbon ink, faded brown oak gall ink, or red rubrication? Record it in `<handNote>`.
- Look at the script style. Are the letters large, separated capital letters (uncials / majuscules), or small, connected letters with fluid strokes (minuscules)? Record it in `script=""`.

Do not rush. Type every bracket with deliberation. Remember: this file is your **ground truth**. If you skip details now, you will have nothing authoritative against which to evaluate automated tools later this week.

**Vocabulary.** *Split-screen inspection* — arranging a high-resolution image viewer alongside a text editor to perform direct visual encoding. *Ground truth authoring* — manual transcription and metadata recording performed with meticulous human verification.

**Takeaway:** In VS Code, hand-type your witness header while inspecting your high-resolution image side-by-side, recording empirical line counts, folio numbers, and ink details.

---

## **29 Content**

**Committing Your Ground Truth to Git**

Once you have finished hand-typing your header and saved your file, it is time to record your achievement in Git.

Open the integrated terminal in VS Code (`Ctrl+\`` or `Terminal -> New Terminal`) and check your status:

```bash
git status
```

You will see your new file `03a_Lesson_2.1_Primary_Witness_Header.xml` listed under untracked files. Stage it and make your commit:

```bash
git add 03a_Lesson_2.1_Primary_Witness_Header.xml
git commit -m "Topic 02 (Cataloguing): Hand-author manual TEI header ground truth for [Your Shelfmark]"
git push origin main
```

Write a commit message that means something! As Stephen Huskey noted in your readings, Git commit messages are your **scholarly research journal**. When you look back at your repository in December, this commit will mark the exact moment your digital edition project was formally catalogued and born.

Do not attempt to validate the file with software today. Leave it exactly as your human hands created it.

**Vocabulary.** *Git staging (`git add`)* — selecting modified files to be included in the next version checkpoint. *Atomic commit* — a Git commit that captures a single coherent, complete step in a project's lifecycle with a clear explanatory message.

**Takeaway:** Stage and commit your hand-authored XML header to Git with a descriptive message, creating the permanent timestamped baseline of your project.

---

## **30 Content**

**Synthesis: The Header as a Scholarly Argument**

Congratulations: you have just built the architectural foundation of a digital scholarly edition.

It is easy for beginners to assume that "the real work" of an edition is transcribing the text, and that the metadata header is just bureaucratic paperwork. But throughout history, the most consequential scholarly debates have hinged on metadata. Who wrote this manuscript? Where was it produced? Which century does the handwriting belong to? Is this marginal note an authorial correction or a later reader's opinion? 

A TEI Header is not administrative bureaucracy; it is a **rigorous scholarly argument in structural form**. Every tag you chose today—every date range, every material support label, every line count—represents an empirical claim based on physical manuscript evidence.

Tomorrow morning, in **Lesson 2.2**, we will enter **Step 2 of our three-step cycle (Deterministic Software)**. We will turn on the XML validation engine in VS Code, link our file to the official TEI RELAX NG schema, and watch the compiler evaluate our manual draft. Every syntax error and schema warning that lights up your screen tomorrow will teach you exactly where human intuition diverges from computational precision.

**Due today, Tuesday September 8.** Your hand-authored `03a_Lesson_2.1_Primary_Witness_Header.xml` committed and pushed to your GitHub repository.

**Tomorrow (Wednesday).** Step 2: Deterministic schema validation in VS Code, fixing syntax defects, building RDF linked data triples, and minting CTS URNs.

**Takeaway:** A TEI Header is a structured scholarly argument about a physical artifact; your manual draft today is the empirical baseline for tomorrow's automated validation audit.

---

## References

Blackwell, C. W., & Smith, N. (2019). The CITE Architecture: A framework for linked data in the humanities. *Digital Humanities Quarterly, 13*(1).

Ceriani, A. M. (1890). *De codice Marchaliano vaticano graeco 2125*. Bibliotheca Apostolica Vaticana.

Clemens, R., & Graham, T. (2007). *Introduction to manuscript studies*. Cornell University Press.

Cummings, J. (2018). The Text Encoding Initiative and the study of literature. In *A New Companion to Digital Humanities* (pp. 451–476). Wiley-Blackwell.

Griffitts, T. (2020). *Digital philology and the Text Encoding Initiative: Methods for ancient manuscript research*. De Gruyter.

Huskey, S. J. (2024). Committing to reproducibility and explainability: Using Git as a research journal. *International Journal of Digital Humanities, 6*, 9–21. https://doi.org/10.1007/s42803-023-00076-9

Le Bœuf, P. (2012). Codicological metadata and the FRBR model. *Gazette du livre médiéval, 58*(1), 14–32.

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and interchange* (Version 4.12.0). https://tei-c.org/guidelines/p5/
