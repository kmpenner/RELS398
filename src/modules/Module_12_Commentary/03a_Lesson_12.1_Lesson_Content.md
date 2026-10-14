# Lesson 12.1 — Drafting Scholarly Commentary Notes by Hand: Categories, Anchors, and TEI Encoding

*RELS 398 / ENGL 398 · Topic 12: Commentary · Meeting #31 (Tue Nov 24)*

***Step 1 of the three-step cycle: manual.** Today you draft scholarly commentary notes by hand across language, historical, and intertextual categories. You establish stable anchors in your document and encode notes using TEI standoff mechanisms (`<standOff>`, `<interpGrp>`, `<note>`, and `@target`). That manual reference corpus becomes the baseline against which Wednesday's deterministic cross-referencing and Friday's AI commentary drafting are evaluated.*

---

## **01 Content**

**The Purpose of Scholarly Commentary**

When you transcribe an archive document, you record the characters written on the page. But historical documents do not speak for themselves. Words change meaning across centuries. Historical names refer to people whom modern readers do not recognize. Legal terms reflect political systems that no longer exist. 

Scholarly commentary bridges this gap. An explanatory note is not merely decorative trivia. It is an intentional interpretative bridge across time, language. Culture. When you add a commentary note, you help your reader understand why a passage matters and what it meant to its original audience.

In our course, you have already transcribed your document (Module 4), normalized unusual spellings (Module 6), tagged linguistic roots (Module 8), marked historical entities (Module 9). Aligned translations (Module 11). Commentary is the editorial layer that ties these threads together into a rich research edition.

Consider our cohort documents:
<ul>
  <li><strong>Ace (1791 French Decree):</strong> Explains the financial crisis of the French Revolution, the value of paper <em>assignats</em>, and the King's declining standard.</li>
  <li><strong>Olyvia (1967 Maud Lewis Letter):</strong> explains Maud's severe rheumatoid arthritis, her cottage near Digby, her pricing of paintings, and her correspondent Leonard Kinnear.</li>
  <li><strong>Andromeda (1752 Peace Treaty):</strong> Details the diplomatic negotiations between Mi'kmaq Chief Jean-Baptiste Cope and Nova Scotia Governor Peregrine Hopson at Halifax.</li>
</ul>

**Vocabulary.** *Commentary* — scholarly notes that explain historical context, difficult vocabulary, or literary references in a primary text. *Paratext* — editorial material surrounding a base text, including introductions, footnotes, and appendices.

**Takeaway:** Scholarly commentary is an active editorial practice that provides the historical, linguistic, and cultural context readers need to understand primary documents.

---

## **02 Content**

**The Editorial Layers of a Digital Edition**

A scholarly edition is built out of distinct, complementary layers. Beginners often mix these layers together into one long, confusing paragraph. Keeping each layer separate is essential for clear scholarship and clean digital markup.

The primary layers include:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
<tr style="background-color: #f1f5f9. Border-bottom: 2px solid #cbd5e1. ">
<th style="padding: 8px. Text-align: left. ">Editorial Layer</th>
<th style="padding: 8px. Text-align: left. ">Primary Focus</th>
<th style="padding: 8px. Text-align: left. ">Core Question Answered</th>
<th style="padding: 8px. Text-align: left. ">Example from Cohort</th>
    </tr>
  </thead>
  <tbody>
<tr style="border-bottom: 1px solid #e2e8f0. ">
<td style="padding: 8px. "><strong>Diplomatic Transcription</strong></td>
<td style="padding: 8px. ">Physical ink on paper</td>
<td style="padding: 8px. "><em>What exact characters are on the page?</em></td>
<td style="padding: 8px. ">Recording Maud Lewis's spelling "Febuary" and line breaks.</td>
    </tr>
<tr style="border-bottom: 1px solid #e2e8f0. ">
<td style="padding: 8px. "><strong>Normalization</strong></td>
<td style="padding: 8px. ">Standardized orthography</td>
<td style="padding: 8px. "><em>How does this map to modern spelling?</em></td>
<td style="padding: 8px. ">Wrapping 1791 French "assignats" with <code>&lt. Choice&gt. </code> tags.</td>
    </tr>
<tr style="border-bottom: 1px solid #e2e8f0. ">
<td style="padding: 8px. "><strong>Translation Alignment</strong></td>
<td style="padding: 8px. ">Bilingual equivalence</td>
<td style="padding: 8px. "><em>What does this mean in another language?</em></td>
<td style="padding: 8px. ">Aligning French decree sentences with modern English translations.</td>
    </tr>
    <tr>
<td style="padding: 8px. "><strong>Scholarly Commentary</strong></td>
<td style="padding: 8px. ">Historical and cultural meaning</td>
<td style="padding: 8px. "><em>Why does this matter, and what does it signify?</em></td>
<td style="padding: 8px. ">Explaining who Governor Hopson was and the Truckhouse trade system in 1752.</td>
    </tr>
  </tbody>
</table>

By maintaining clear boundaries between text record, translation. Commentary, your digital edition allows readers to toggle views easily between raw witness text and critical annotations.

**Vocabulary.** *Diplomatic Layer* — the exact record of physical textual features without editorial correction. *interpretive Layer* — the interpretive commentary that unpacks meaning and historical meaning.

**Takeaway:** Commentary provides the interpretive rationale behind textual features, remaining distinct from physical text record and linguistic normalization.

---

## **03 Content**

**The Three Core Categories of Commentary Notes**

To organize your commentary in Visual Studio Code, you must classify each note into a recognized category. Without standard categories, commentary quickly becomes cluttered and impossible to index.

Scholars organize commentary notes into three core categories:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
<tr style="background-color: #f1f5f9. Border-bottom: 2px solid #cbd5e1. ">
<th style="padding: 8px. Text-align: left. ">Category</th>
<th style="padding: 8px. Text-align: left. ">Scope</th>
<th style="padding: 8px. Text-align: left. ">Primary Questions Addressed</th>
    </tr>
  </thead>
  <tbody>
<tr style="border-bottom: 1px solid #e2e8f0. ">
<td style="padding: 8px. "><strong>1. language & Lexical</strong></td>
<td style="padding: 8px. ">Words, idioms, and grammar</td>
<td style="padding: 8px. ">What does this rare term mean? Why is this grammatical form unusual?</td>
    </tr>
<tr style="border-bottom: 1px solid #e2e8f0. ">
<td style="padding: 8px. "><strong>2. Historical & Contextual</strong></td>
<td style="padding: 8px. ">People, places, laws, and dates</td>
<td style="padding: 8px. ">Who was this person? Where was this place? What historical event caused this?</td>
    </tr>
    <tr>
<td style="padding: 8px. "><strong>3. Intertextual & Citational</strong></td>
<td style="padding: 8px. ">Connections to other documents</td>
<td style="padding: 8px. ">What law, treaty, letter, or scripture does this passage quote or echo?</td>
    </tr>
  </tbody>
</table>

Each category serves a specific reading need. A reader studying historical currency in revolutionary France needs historical notes on assignats. A linguist studying Nova Scotia folk speech needs lexical notes on Maud Lewis's colloquialisms. A legal historian needs intertextual links to earlier colonial treaties.

**Vocabulary.** *Taxonomy* — a structured system of grouping. *Controlled Vocabulary* — a standardized set of pre-defined terms used for labeling data.

**Takeaway:** Grouping commentary into language, historical, and intertextual categories ensures consistent annotation and enables automated indexing.

---

## **04 Content**

**Category 1: language and Lexical Notes**

language notes examine language, vocabulary, and grammar. They explain archaic terms, obsolete meanings, legal jargon, and regional dialect phrases.

In historical documents, familiar words often carried different meanings in earlier centuries. For example:
<ul>
  <li>In Andromeda's 1752 Treaty, the phrase <em>"Truckhouse"</em> does not mean a garage or motor vehicle shop. In colonial Nova Scotia, a truckhouse was a government-run trading post where Mi'kmaq hunters exchanged furs for European goods at fixed rates. A language note clarifies this definition.</li>
  <li>In Ace's 1791 French decree, the word <em>"assignats"</em> originally referred to state bonds. However, Rapidly transformed into paper bank notes subject to runaway inflation. A lexical note explains this shift.</li>
  <li>In Olyvia's 1967 letter, Maud Lewis mentions she cannot paint quickly due to her hands being <em>"crooked."</em> A lexical and medical note clarifies that Maud suffered from juvenile rheumatoid arthritis that deformed her fingers.</li>
</ul>

When drafting a language note:
<ol>
  <li>Define the specific word or phrase concisely.</li>
  <li>Identify the historical language period or dialect.</li>
  <li>Cite an trusted dictionary or glossary (such as the Oxford English Dictionary or the Dictionnaire de l'Académie française).</li>
</ol>

**Vocabulary.** *word study* — the historical study of language, literature, and how texts transmit meaning over time. *Truckhouse* — an 18th-century government trading post in British North America.

**Takeaway:** language notes clarify obsolete vocabulary, historical legal terminology, and regional expressions to prevent modern misinterpretation.

---

## **05 Content**

**Category 2: Historical and Contextual Notes**

Historical notes supply the factual background readers need to understand the social world behind the text. They identify historical figures, geographical locations, political institutions, and material culture.

Historical notes answer questions such as:
<ul>
  <li><strong>People:</strong> Who was Peregrine Thomas Hopson? (He was the British Governor of Nova Scotia from 1752 to 1753, known for negotiating peaceful relations with local First Nations).</li>
  <li><strong>Places:</strong> Where is Marshalltown, Nova Scotia? (A small rural community in Digby County where Maud and Everett Lewis lived in a tiny one-room painted cottage).</li>
  <li><strong>Institutions:</strong> What was the <em>Assemblée Nationale</em> in 1791? (The revolutionary legislative parliament of France that stripped King Louis XVI of absolute power).</li>
  <li><strong>Material Culture:</strong> What was an <em>assignat de 5 livres</em> made of? (Handmade rag paper watermarked with royal seals and revolutionary slogans to discourage counterfeiting).</li>
</ul>

A strong historical note does not copy an entire encyclopedia article. Instead, it provides three to four concise sentences giving only the facts relevant to the document passage.

**Vocabulary.** *biography* — the study of the lives, careers, and social networks of historical individuals. *Realia* — real-world physical objects, customs, and institutions characteristic of a historical culture.

**Takeaway:** Historical notes identify people, places, dates, and institutions, giving readers the essential background context behind the text.

---

## **06 Content**

**Category 3: Intertextual and Citational Notes**

Historical documents are rarely created in isolation. They quote laws, echo previous treaties, cite personal correspondence. Allude to literature. Intertextual notes uncover and explain these connections.

Consider how our three student documents rely on external texts:
<ul>
  <li><strong>Andromeda's 1752 Treaty:</strong> Article 1 explicitly reaffirms the earlier Peace Treaty of 1725 signed at Boston. An intertextual note explains what the 1725 treaty set and links the reader to its text in the Nova Scotia Archives.</li>
  <li><strong>Ace's 1791 Decree:</strong> The decree cites earlier financial legislation passed on September 29, 1790. An intertextual note provides the date, legislative session. Volume number of the earlier law.</li>
  <li><strong>Olyvia's 1967 Letter:</strong> Maud Lewis writes in response to an order from Leonard Kinnear. An intertextual note links Maud's letter to Kinnear's original inquiry and points out the specific folk paintings delivered to him.</li>
</ul>

When writing intertextual notes, specify whether the connection is a direct quotation, a formal legal cross-reference, an allusion, or a thematic parallel.

**Vocabulary.** *textual linking* — the relational network connecting a text to other written or cultural works. *Citation* — a formal reference to a specific published source, archive document, or legal code.

**Takeaway:** Intertextual notes identify and explain citations, legal cross-references, and literary echoes that link a document to a wider network of texts.

---

## **07 Content**

**The Dilemma of Text Anchors**

Before you can attach a commentary note to a digital text, you must solve a technical problem: how do you connect the note to the exact word or sentence it explains?

In early digital humanities projects, editors tried using raw character offsets. For example, a database might record: <em>"Attach Note 1 to characters 142 through 158."</em> This approach proved disastrous. Whenever an editor fixed a spelling typo or added a missed word at the beginning of the file, every single character offset shifted, breaking all subsequent links.

Digital editions solve this problem by assigning permanent identifiers directly into the markup. Rather than counting characters, we give each structural unit a unique `xml:id` attribute:
```xml
<s xml:id="s12">The said Tribe shall have free liberty to hunt.</s>
```
A note can now securely point to `#s12`. Even if you insert ten new paragraphs earlier in the file, `#s12` remains stable, and the link never breaks.

**Vocabulary.** *Anchor* — a designated target point or passage in a digital document to which an annotation is attached. *Character Offset* — counting raw character positions from the start of a file, an fragile method for digital annotation.

**Takeaway:** Robust digital commentary relies on stable XML identifier anchors rather than fragile character offsets that break when text is revised.

---

## **08 Content**

**scope of Anchors: Words, Spans, and Sentences**

When annotating a document in VS Code, you must decide how broad or narrow your anchor should be. This choice is called anchor scope.

There are three common levels of scope:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
<tr style="background-color: #f1f5f9. Border-bottom: 2px solid #cbd5e1. ">
<th style="padding: 8px. Text-align: left. ">Anchor Level</th>
<th style="padding: 8px. Text-align: left. ">TEI Element</th>
<th style="padding: 8px. Text-align: left. ">Best Suited For</th>
<th style="padding: 8px. Text-align: left. ">Example</th>
    </tr>
  </thead>
  <tbody>
<tr style="border-bottom: 1px solid #e2e8f0. ">
<td style="padding: 8px. "><strong>Word Token</strong></td>
<td style="padding: 8px. "><code>&lt. W xml:id="w1"&gt. </code></td>
<td style="padding: 8px. ">Lexical glosses, archaic words</td>
<td style="padding: 8px. ">Explaining the single word <code>&lt. W xml:id="w4"&gt. Truckhouse&lt. /w&gt. </code></td>
    </tr>
<tr style="border-bottom: 1px solid #e2e8f0. ">
<td style="padding: 8px. "><strong>Arbitrary Phrase</strong></td>
<td style="padding: 8px. "><code>&lt. Seg xml:id="seg1"&gt. </code></td>
<td style="padding: 8px. ">Idioms, compound titles, historical events</td>
<td style="padding: 8px. "><code>&lt. Seg xml:id="seg2"&gt. Fabrication des assignats&lt. /seg&gt. </code></td>
    </tr>
    <tr>
<td style="padding: 8px. "><strong>Full Sentence / Clause</strong></td>
<td style="padding: 8px. "><code>&lt. S xml:id="s1"&gt. </code></td>
<td style="padding: 8px. ">Historical context, legal obligations</td>
<td style="padding: 8px. ">Explaining Article 4 of the 1752 Treaty on trade monopolies</td>
    </tr>
  </tbody>
</table>

For novice editors, anchoring notes to sentences (`<s>`) or distinct phrases (`<seg>`) is usually the cleanest approach. It avoids cluttering every single word with an identifier while giving readers precise references.

**Vocabulary.** *scope* — the scale or level of detail of an anchor (word, phrase, sentence, or paragraph). *Segmentation* — dividing running text into discrete syntactic units with `<seg>` or `<s>`.

**Takeaway:** Match your anchor scope to the purpose of the note: use word anchors for lexical glosses, and sentence or phrase anchors for historical commentary.

---

## **09 Content**

**The Problem of Overlapping Markup**

XML is a hierarchical data structure. Every opening tag must be closed within the same parent element. This rule makes XML tidy and predictable. However, It creates headaches when modeling historical documents.

In a physical manuscript or printed treaty, textual features frequently overlap:
<ul>
  <li>A sentence may start near the bottom of folio 1r and finish at the top of folio 1v.</li>
  <li>A commentary note might explain a three-word phrase that straddles two printed lines.</li>
  <li>A historical event note might cover the second half of sentence 3 and the first half of sentence 4.</li>
</ul>

If you try to nest an inline `<note>` across an element boundary, the XML parser throws a fatal error:
```xml
<!-- INVALID XML: OVERLAPPING TAGS -->
<s xml:id="s1">King George <note>rules Great Britain</s>
<s xml:id="s2">and Ireland</note> happily.</s>
```
The browser or validator will refuse to open the document. To solve this problem without breaking XML rules, modern digital editions use standoff markup.

**Vocabulary.** *Well-Formed XML* — XML that strictly obeys syntactic rules, including proper tag nesting and closing. *Overlapping Hierarchy* — when two conceptual structures (such as physical lines and grammatical sentences) cross paths without nesting neatly.

**Takeaway:** XML requires strict tree nesting, making it impossible to overlap inline tags across element boundaries.

---

## **10 Content**

**Introduction to TEI Standoff Markup**

Standoff markup separates your commentary notes from the base text record. Instead of embedding notes directly inside the running text, you store them in a dedicated `<standOff>` section at the end of your TEI document.

In standoff architecture:
<ol>
  <li>The base text remains clean, diplomatic, and unobstructed by long editorial paragraphs.</li>
  <li>Each note lives in the `<standOff>` container and includes a `@target` attribute pointing back to one or more text anchors.</li>
  <li>Multiple notes can target the same word without tangling code.</li>
  <li>A note can target multiple separated sentences without violating XML nesting rules.</li>
</ol>

Here is the basic structure of a TEI document with standoff markup:
```xml
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>...</teiHeader>
  <text>
    <body>
      <p>
        <s xml:id="tr_s1">Done at Halifax this 22nd day of November 1752.</s>
      </p>
    </body>
  </text>
  <standOff>
    <note target="#tr_s1" type="historical">
      Signed in the Council Chamber by Governor Peregrine Hopson.
    </note>
  </standOff>
</TEI>
```

**Vocabulary.** *Standoff Markup* — encoding annotations and editorial data in a separate container outside the primary text, linked via URI pointers. *Inline Markup* — placing tags directly around or inside the words of the running text.

**Takeaway:** Standoff markup places annotations in a separate `<standOff>` section, keeping base text clean and allowing complex, multi-point linking.

---

## **11 Content**

**TEI Chapter 17: Simple Analytic Mechanisms**

The TEI P5 Guidelines provide a dedicated module for scholarly interpretation: Chapter 17, titled *Simple Analytic Mechanisms*. This chapter defines standardized elements for attaching interpretations, thematic analyses, and structured commentary to texts.

The primary elements defined in Chapter 17 include:
<ul>
<li><code>&lt. Interp&gt. </code>: Defines a single interpretive category, theme, or topic (for example: "Colonial Trade Policy" or "Paper Currency Depreciation").</li>
<li><code>&lt. InterpGrp&gt. </code>: Groups related interpretations into a shared domain (such as historical themes or linguistic registers).</li>
<li><code>&lt. Span&gt. </code>: Associates an interpretive element with a specific span of text using <code>@from</code> and <code>@to</code> pointers.</li>
<li><code>&lt. SpanGrp&gt. </code>: A collection of related <code>&lt. Span&gt. </code> elements.</li>
</ul>

Using Chapter 17 elements turns your commentary from unstructured footnotes into searchable semantic data that computers can analyze and index.

**Vocabulary.** *Simple Analytic Mechanisms* — the TEI module (Chapter 17) providing elements for qualitative annotation, thematic tagging, and textual analysis. *Semantic Annotation* — tagging text with structured data that describes its meaning and context.

**Takeaway:** TEI Chapter 17 provides standardized elements (`<interpGrp>`, `<interp>`, and `<span>`) for encoding structured interpretive metadata.

---

## **12 Content**

**Encoding Controlled Interpretations with `<interpGrp>`**

When annotating historical texts, editors often want to tag recurring themes. For instance, in colonial treaties, passages repeatedly discuss trade, military defense, gift exchange, or territorial boundaries.

Rather than typing these themes freely into every note, you define a controlled vocabulary using `<interpGrp>` in your `<standOff>` block:
```xml
<standOff>
  <interpGrp type="treaty_themes">
    <interp xml:id="th_trade">Commercial Regulations and Truckhouses</interp>
    <interp xml:id="th_peace">Cessation of Hostilities</interp>
    <interp xml:id="th_provision">Annual Rations and Subsidy</interp>
    <interp xml:id="th_jurisdiction">Legal Trials and Prisoner Return</interp>
  </interpGrp>
</standOff>
```
Once these themes are declared, any note or sentence can reference them using the `@ana` (analysis) attribute:
```xml
<s xml:id="s4" ana="#th_trade">The said Tribe shall have free liberty to bring to Sale...</s>
```
A web browser or search tool can now instantly retrieve every sentence in the edition dealing with trade regulations.

**Vocabulary.** *Controlled Vocabulary* — an trusted, pre-defined list of authorized terms used for consistent tagging. *`@ana` Attribute* — a TEI attribute that points to an interpretive definition explaining the passage.

**Takeaway:** Defining themes in an `<interpGrp>` sets up a controlled vocabulary that makes commentary themes systematically searchable across an entire edition.

---

## **13 Content**

**Pointing and Linking: The Syntax of `@target`**

To connect a standoff note to its text anchor, TEI uses URI pointers in the `@target` attribute. Understanding this syntax is essential for avoiding broken links.

The key rules for `@target` pointers are:
<ol>
<li><strong>The Hash Prefix (`#`):</strong> When pointing to an element in the same XML file, you must begin the value with a hash symbol (`#`). The hash tells the system to look for an <code>xml:id</code> within the current document. Writing <code>target="s1"</code> is an error. Write <code>target="#s1"</code>.</li>
  <li><strong>Multiple Targets:</strong> A single note can explain multiple sentences or words. Separate each target ID with a space: <code>target="#s1 #s2"</code>.</li>
  <li><strong>Cross-Document Linking:</strong> To point to an element in another file, write the file path followed by the hash and ID: <code>target="witness_a.xml#s1"</code>.</li>
</ol>

Here is an example connecting one historical note to two related sentences:
```xml
<note target="#s1 #s2" type="historical">
  These opening clauses establish the formal diplomatic protocol between British colonial authorities and the Shubenacadie Mi'kmaq delegation.
</note>
```

**Vocabulary.** *Fragment Identifier* — the part of a URI beginning with `#` that specifies a unique element within a document. *URI (Uniform Resource Identifier)* — a standardized string that points out a digital resource.

**Takeaway:** The `@target` attribute links standoff notes to text anchors using the `#id` syntax, supporting multiple space-separated targets.

---

## **14 Content**

**standard Inline `<note>` vs. Standoff `<note>`**

Beginners frequently ask: when should I use a standard inline `<note>`. When should I use standoff `<note>`?

Both methods have legitimate roles in digital publishing:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
<tr style="background-color: #f1f5f9. Border-bottom: 2px solid #cbd5e1. ">
<th style="padding: 8px. Text-align: left. ">Feature</th>
<th style="padding: 8px. Text-align: left. ">Inline <code>&lt. Note&gt. </code></th>
<th style="padding: 8px. Text-align: left. ">Standoff <code>&lt. Note&gt. </code></th>
    </tr>
  </thead>
  <tbody>
<tr style="border-bottom: 1px solid #e2e8f0. ">
<td style="padding: 8px. "><strong>Location in File</strong></td>
<td style="padding: 8px. ">Directly inside <code>&lt. P&gt. </code> or <code>&lt. S&gt. </code> text</td>
<td style="padding: 8px. ">Inside <code>&lt. StandOff&gt. </code> at end of document</td>
    </tr>
<tr style="border-bottom: 1px solid #e2e8f0. ">
<td style="padding: 8px. "><strong>Best Use Case</strong></td>
<td style="padding: 8px. ">Simple author footnotes printed in source</td>
<td style="padding: 8px. ">Modern scholarly commentary and critical notes</td>
    </tr>
<tr style="border-bottom: 1px solid #e2e8f0. ">
<td style="padding: 8px. "><strong>Readability of Base Text</strong></td>
<td style="padding: 8px. ">Poor (cluttered by lengthy note text)</td>
<td style="padding: 8px. ">Excellent (base text remains clean)</td>
    </tr>
    <tr>
<td style="padding: 8px. "><strong>Multi-Point Linking</strong></td>
<td style="padding: 8px. ">Impossible (anchored only to its insertion spot)</td>
<td style="padding: 8px. ">Supported (can target multiple words or sentences)</td>
    </tr>
  </tbody>
</table>

For modern scholarly commentary in our course projects, standoff notes are preferred. They keep your text record clean and allow rich cross-referencing.

**Vocabulary.** *Inline Note* — an explanatory note inserted directly into the stream of the primary text. *Standoff Container* — a dedicated section of an XML file reserved for external annotations.

**Takeaway:** Use inline notes only for original author footnotes found in the source. Use standoff notes for modern scholarly commentary.

---

## **15 Content**

**Typing Commentary Notes with `@type` and `@subtype`**

In TEI XML, an untyped `<note>` is treated as generic text. To allow stylesheets and reading interfaces to filter notes intelligently, always specify the category using the `@type` and `@subtype` attributes.

Recommended values for scholarly commentary include:
<ul>
  <li><code>@type="language"</code>: Linguistic, grammatical, and lexical notes.
    <ul>
      <li><code>subtype="lexical"</code>: Explaining rare or archaic vocabulary.</li>
      <li><code>subtype="morphosyntax"</code>: Analyzing unusual grammar or word forms.</li>
    </ul>
  </li>
  <li><code>@type="historical"</code>: Historical context, realia, and biography.
    <ul>
      <li><code>subtype="biographical"</code>: naming historical persons.</li>
      <li><code>subtype="geographical"</code>: explaining locations and boundaries.</li>
      <li><code>subtype="institutional"</code>: Explaining laws, councils, or monetary systems.</li>
    </ul>
  </li>
  <li><code>@type="intertextual"</code>: References to external texts.
    <ul>
      <li><code>subtype="citation"</code>: Direct quotation or legal statute reference.</li>
      <li><code>subtype="allusion"</code>: Echo or thematic parallel.</li>
    </ul>
  </li>
</ul>

Here is a typed note for Ace's 1791 decree:
```xml
<note target="#s3" type="historical" subtype="institutional">
  The Comité des décrets was the parliamentary committee responsible for drafting the official text of laws passed by the National Assembly before royal sanction.
</note>
```

**Vocabulary.** *Attribute Value* — the specific setting assigned to an XML attribute in quotation marks. *Facet* — a distinct dimension or subcategory of metadata.

**Takeaway:** Classify every commentary note using `@type` and `@subtype` so digital editions can filter annotations by analytical domain.

---

## **16 Content**

**Structuring Rich Note Bodies**

A scholarly commentary note is not just a plain string of text. Inside a `<note>`, you frequently quote foreign words, cite books, or mention historical dates. TEI provides phrase-level elements to structure the interior of your note:

<ul>
<li><code>&lt. Mentioned&gt. </code>: Marks a word or phrase from the base text being discussed (e.g., <code>&lt. Mentioned&gt. Truckhouse&lt. /mentioned&gt. </code>).</li>
<li><code>&lt. Gloss&gt. </code>: Provides a concise modern definition or equivalent phrase.</li>
<li><code>&lt. Cit&gt. </code> and <code>&lt. Quote&gt. </code>: Embeds a quotation from a secondary source or historical dictionary.</li>
<li><code>&lt. Bibl&gt. </code>: Provides a book citation for the scholarly source supporting your note.</li>
<li><code>&lt. Ref target="https://..."&gt. </code>: Provides a clickable link to a digital archive or standard record.</li>
</ul>

Here is a fully structured note for Olyvia's Maud Lewis letter:
```xml
<note target="#w8" type="philological" subtype="lexical">
  <mentioned>crooked</mentioned>: Used here by Lewis to describe the physical deformity of her hands caused by rheumatoid arthritis. See <bibl>Lance Woolaver, <title>Maud Lewis: The Heart on the Door</title> (1995), p. 42</bibl>.
</note>
```

**Vocabulary.** *Phrase-Level Element* — an XML element designed to mark words or short phrases within a paragraph or note. *book Reference* — formal citation details attributing information to published scholarship.

**Takeaway:** Structure the interior of commentary notes using `<mentioned>`, `<gloss>`, and `<bibl>` to maintain academic rigor and book attribution.

---

## **17 Content**

**Attributing Editorial credit with `@resp`**

Scholarly commentary is an act of interpretation. Different scholars may hold conflicting views about a historical passage, or notes may be drafted by student editors and revised by instructors.

TEI tracks editorial authorship using the `@resp` (credit) attribute. The value of `@resp` is a pointer to an editor defined in the `teiHeader`:
<ol>
<li>In your <code>&lt. TeiHeader&gt. </code>, list all contributors inside <code>&lt. TitleStmt&gt. </code> with unique <code>xml:id</code> values:
<pre><code>&lt. Editor xml:id="al"&gt. Ace Long&lt. /editor&gt. 
&lt;editor xml:id="kp"&gt;Ken Penner&lt;/editor&gt;</code></pre>
  </li>
  <li>In your standoff notes, attribute each note to its author using <code>@resp</code>:
<pre><code>&lt. Note target="#s1" type="historical" resp="#al"&gt. 
  Drafted by Ace Long analyzing Revolutionary monetary policy.
&lt;/note&gt;</code></pre>
  </li>
</ol>

When artificial intelligence is used to generate draft commentary (as we will explore in Lesson 12.3), clarity requires tagging those notes with `resp="#gemini"` or `resp="#ai"` to distinguish machine suggestions from verified human scholarship.

**Vocabulary.** *Provenance* — the documented history of ownership, creation, and editorial credit for a text or annotation. *`@resp` Attribute* — an XML attribute naming the person or tool responsible for a specific markup decision.

**Takeaway:** Attribute every commentary note to its human author or AI assistant using `@resp` to maintain scholarly clarity and honesty.

---

## **18 Content**

**Connecting Commentary to External standard Files**

A major advantage of digital commentary over printed footnotes is linked open data. When you mention a historical person, place, or institution, you can connect your note directly to global standard files using the `@ref` attribute.

Standard international standard files include:
<ul>
  <li><strong>Wikidata:</strong> Persistent global identifiers for people, places. Events (e.g., <code>https://www.wikidata.org/wiki/Q131376</code> for King Louis XVI).</li>
  <li><strong>GeoNames:</strong> Global geographic database of historical and modern places (e.g., <code>https://www.geonames.org/6355375</code> for Digby, Nova Scotia).</li>
  <li><strong>BnF (Bibliothèque nationale de France):</strong> trusted identifiers for French historical figures and legal bodies.</li>
  <li><strong>Canadian Dictionary of Biography:</strong> trusted biographies for figures such as Governor Peregrine Hopson and Chief Jean-Baptiste Cope.</li>
</ul>

Here is an example linking a historical note to both Wikidata and the Canadian Biography:
```xml
<note target="#s2" type="historical" subtype="biographical">
  Governor <persName ref="https://www.wikidata.org/wiki/Q7168341">Peregrine Thomas Hopson</persName> assumed office in Halifax in August 1752.
</note>
```

**Vocabulary.** *Linked Open Data (LOD)* — structured data published on the web in standardized formats allowing computers to connect related concepts across repositories. *standard Record* — an set, unique record in a library catalog that clearly points out an entity.

**Takeaway:** Enrich commentary notes with standard URIs (`@ref`) to link your local edition to the global web of historical and geographical data.

---

## **19 Content**

**Step-by-Step: Preparing Your Document for Annotation in VS Code**

Before drafting notes, you must prepare your base TEI XML file in Visual Studio Code. Follow these practical steps:

<ol>
  <li><strong>Open Your File in VS Code:</strong> Launch VS Code and open your project file (e.g., <code>witness.xml</code>).</li>
  <li><strong>Verify XML Well-Formedness:</strong> Check the bottom status bar for Red Hat XML validation errors. Ensure the file has 0 errors before proceeding.</li>
  <li><strong>Review Existing Identifiers:</strong> Check whether your sentences or clauses already carry <code>xml:id</code> attributes from earlier modules. If they do not, add sequential identifiers:
<pre><code>&lt. P&gt. 
&lt. S xml:id="s1"&gt. First sentence of witness...&lt. /s&gt. 
&lt. S xml:id="s2"&gt. Second sentence of witness...&lt. /s&gt. 
&lt;/p&gt;</code></pre>
  </li>
  <li><strong>Split Your Editor:</strong> Press <code>Cmd+\</code> (macOS) or <code>Ctrl+\</code> (Windows) to open a two-column editor. Put your base text on the left and your new commentary file (<code>commentary.xml</code>) on the right.</li>
<li><strong>Add the Standoff Container:</strong> If you are working within a single TEI file, scroll to the bottom right before the closing <code>&lt. /TEI&gt. </code> tag and create the <code>&lt. StandOff&gt. </code> element:
<pre><code>&lt. StandOff&gt. 
&lt. !-- Commentary notes will go here --&gt. 
&lt;/standOff&gt;
&lt;/TEI&gt;</code></pre>
  </li>
</ol>

**Vocabulary.** *Split Editor* — viewing two files or two panes of the same file side-by-side in VS Code. *Anchor Preparation* — ensuring all target passages carry unique, well-formed `xml:id` values.

**Takeaway:** Prepare your document in VS Code by verifying XML well-formedness, setting sequential `xml:id` anchors, and setting up a two-column editor layout.

---

## **20 Content**

**Hands-On Walkthrough: Drafting language Notes**

Now let us practice drafting a language note. Select a sentence from your document that contains an archaic, dialectal, or specialized technical word.

Follow this workflow:
<ol>
<li><strong>Locate the Target Word:</strong> Identify the word in your base text. Wrap it in a <code>&lt. W&gt. </code> tag with an <code>xml:id</code>, or identify the containing sentence ID:
<pre><code>&lt. W xml:id="w_assignat"&gt. Assignats&lt. /w&gt. </code></pre>
  </li>
  <li><strong>Research the Word:</strong> Look up the historical usage in an trusted dictionary. Determine when the term entered common use and how its meaning shifted.</li>
<li><strong>Draft the Note in Standoff:</strong> Inside <code>&lt. StandOff&gt. </code>, add a typed note referencing the word anchor:
<pre><code>&lt. Note target="#w_assignat" type="language" subtype="lexical" resp="#al"&gt. 
&lt. Mentioned&gt. Assignats&lt. /mentioned&gt. : Originally paper bonds issued in 1789 secured against confiscated clergy lands (biens nationaux), assignats functioned as legal tender paper currency by 1791, experiencing massive runaway inflation.
&lt;/note&gt;</code></pre>
  </li>
  <li><strong>Verify the Pointer:</strong> In VS Code, search for <code>w_assignat</code> to confirm that the ID in the base text matches the note target exactly.</li>
</ol>

**Vocabulary.** *dictionary work* — the scholarly discipline and practice of compiling dictionaries and analyzing word histories. *runaway inflation* — rapid, out-of-control currency depreciation, as seen with French revolutionary assignats.

**Takeaway:** Author language notes by naming specialized terms, researching their historical definitions, and linking them to word or sentence anchors via `@target`.

---

## **21 Content**

**Hands-On Walkthrough: Drafting Historical Notes**

Next, draft a historical commentary note for an institution, person, or geographical landmark mentioned in your witness.

Let us draft a note for Andromeda's 1752 Treaty mentioning Chief Jean-Baptiste Cope:
<ol>
  <li><strong>Identify the Anchor in Base Text:</strong>
<pre><code>&lt. S xml:id="tr_s3"&gt. Between His Excellency Peregrine Thomas Hopson... and Major Jean Baptiste Cope, Chief Sachem of the Tribe of Mickmack Indians...&lt. /s&gt. </code></pre>
  </li>
  <li><strong>Gather Biographical Facts:</strong>
    <ul>
      <li>Jean-Baptiste Cope was a prominent Mi'kmaq leader of the Shubenacadie district.</li>
      <li>He negotiated the 1752 treaty to secure hunting, fishing. Trading rights while seeking to protect his community from military conflict.</li>
      <li>The treaty was signed in Halifax in November 1752.</li>
    </ul>
  </li>
  <li><strong>Compose the Standoff Note:</strong>
<pre><code>&lt. Note target="#tr_s3" type="historical" subtype="biographical" resp="#ag"&gt. 
Major &lt. PersName ref="https://www.biographi.ca/en/bio/cope_jean_baptiste_3E.html"&gt. Jean-Baptiste Cope&lt. /persName&gt. (died c. 1758–1760) was a prominent Mi'kmaq leader who led negotiations for the Treaty of 1752 at Halifax. The title "Major" was an honorary military designation recognized by both French and British standards.
&lt;/note&gt;</code></pre>
  </li>
</ol>

Notice how this note concisely provides the dates, historical role. Explanation of his title, without cluttering the main reading text.

**Vocabulary.** *Chief Sachem* — an Anglicized colonial term for a principal regional leader or political spokesperson among northeastern Indigenous nations. *Honorary Title* — a formal title conferred as an honor or diplomatic recognition.

**Takeaway:** Historical notes explain persons and institutions by synthesizing verified biographical facts and linking them to external biographical dictionaries.

---

## **22 Content**

**Hands-On Walkthrough: Drafting Intertextual Notes**

Now draft an intertextual note connecting your document to an earlier or contemporary text.

Let us examine Maud Lewis's 1967 letter from Olyvia's project. Maud mentions that she has paintings ready for Mr. Kinnear:
<ol>
  <li><strong>Identify the Textual Reference:</strong>
<pre><code>&lt. S xml:id="ml_s5"&gt. I have two small paintings done, one of oxen and one of cats.&lt. /s&gt. </code></pre>
  </li>
  <li><strong>Trace the Art Historical Intertext:</strong>
    <ul>
      <li>Maud Lewis repeatedly painted specific iconic compositions throughout her career: pairs of black and white cats in flowerbeds. Oxen teams decorated with floral yokes.</li>
      <li>Her letters frequently negotiate the sale of these standard subjects for small sums (often $4 to $6).</li>
    </ul>
  </li>
  <li><strong>Draft the Intertextual Note:</strong>
<pre><code>&lt. Note target="#ml_s5" type="intertextual" subtype="allusion" resp="#ol"&gt. 
  Maud Lewis's reference to "oxen" and "cats" points to her most celebrated serial folk art compositions. Similar compositions from 1965–1967 are preserved in the permanent collection of the Art Gallery of Nova Scotia (accession numbers 1984.001 and 1987.014).
&lt;/note&gt;</code></pre>
  </li>
</ol>

This note connects a casual personal letter to surviving physical art objects in public museum collections, greatly enhancing the scholarly value of the edition.

**Vocabulary.** *Intertextual Web* — the network of related documents, visual artworks, or cultural artifacts referenced by a historical text. *Accession Number* — a unique identifier assigned by a museum or library to an object in its permanent collection.

**Takeaway:** Intertextual notes connect primary documents to related legal statutes, personal correspondence, and preserved museum artifacts.

---

## **23 Content**

**Validating Pointers and Link Integrity in VS Code**

A broken link in a digital edition is just as bad as a 404 error on a website. If a note targets `#s99` but there is no element with `xml:id="s99"`, readers and software cannot display the annotation.

You can easily audit your link integrity in VS Code:
<ol>
  <li><strong>Use VS Code Find (`Cmd+F` / `Ctrl+F`):</strong> Copy the ID target (e.g., <code>tr_s3</code>). Press <code>Cmd+F</code> and paste the text. You must see at least two matches:
    <ul>
<li>The declaration in the text: <code>&lt. S xml:id="tr_s3"&gt. </code></li>
<li>The target in your note: <code>&lt. Note target="#tr_s3"&gt. </code></li>
    </ul>
    If you only see one match, you have an orphaned pointer.
  </li>
  <li><strong>Use Red Hat XML Extension:</strong> The XML extension flags duplicate `xml:id` values. Every `xml:id` across your file must be completely unique.</li>
  <li><strong>Verify the Hash Prefix:</strong> Run a quick regex search in VS Code for <code>target="[^#]</code>. This finds any `@target` attribute where you forgot to include the required `#` symbol!</li>
</ol>

**Vocabulary.** *Orphaned Pointer* — an annotation link pointing to an ID that does not exist in the document. *Link Integrity* — the state where every internal and external URI resolves to a valid, existing destination.

**Takeaway:** Validate link integrity in VS Code by verifying that every `@target` includes the `#` prefix and matches an existing `xml:id`.

---

## **24 Content**

**Case Study: The Dickinson College Commentaries Model**

To understand how professional digital humanities projects handle commentary, consider the *Dickinson College Commentaries* (DCC) directed by Christopher Francese.

DCC publishes digital editions of historical Latin and Greek texts designed specifically for intermediate students and researchers. Their commentary model follows several principles that match our course approach:
<ul>
  <li><strong>Clear Separation of Layers:</strong> The base reading text is displayed cleanly on the left. Meanwhile, vocabulary glosses and historical notes appear in collapsible sidebars on the right.</li>
  <li><strong>Controlled Vocabulary Tiers:</strong> Notes are strictly divided into vocabulary explanations, grammatical analyses, and historical/geographical context.</li>
  <li><strong>Linked Open Data Gazetteers:</strong> Every ancient toponym links to the <em>Pleiades</em> gazetteer of ancient places. This provides coordinates and map views.</li>
  <li><strong>Novice-Centered Explanations:</strong> Instead of assuming graduate-level language knowledge, DCC notes explain historical idioms in clear, accessible English.</li>
</ul>

By adopting this modular, user-focused architecture, our student editions achieve the same clarity and usability as major university digital projects.

**Vocabulary.** *Toponym* — the proper name of a place or geographical feature. *Gazetteer* — a geographical dictionary or directory providing coordinates and historical information about places.

**Takeaway:** The Dickinson College Commentaries model shows how clean visual separation, controlled categories, and linked gazetteers make historical texts accessible to students.

---

## **25 Content**

**Case Study: Scholarly Commentary in Legal and archive Editions**

While classical editions often emphasize literary style, archive and legal editions (such as the *Early Canadiana Online* project or the French *Archives Parlementaires*) require a distinct commentary strategy.

When annotating colonial proclamations or revolutionary statutes:
<ul>
  <li><strong>Focus on standard and Sanction:</strong> The commentary must explain who held the legal standard to issue the document. In Ace's 1791 decree, notes must explain why the King's seal appears alongside the signature of the President of the National Assembly.</li>
  <li><strong>Documenting Legal Precedents:</strong> In Andromeda's 1752 Treaty, the commentary must trace how each article reflects British colonial policies set in earlier treaties with First Nations across the Atlantic seaboard.</li>
  <li><strong>Social Impact vs. Official Rhetoric:</strong> Official legal decrees often claim that laws were universally welcomed. Scholarly notes provide the reality check, detailing public protests, financial panic, or indigenous sovereignty concerns omitted from the official record.</li>
</ul>

Editorial neutrality does not mean ignoring historical controversy. It means documenting multiple perspectives using verified archive evidence.

**Vocabulary.** *Statute* — a formal written enactment of a legislative standard that governs a city, state, or country. *Royal Sanction* — the formal approval of a bill by a monarch, necessary for legislation to take legal effect in constitutional monarchies.

**Takeaway:** archive and legal commentary studies legislative standard, historical precedents, and the social realities behind official administrative rhetoric.

---

## **26 Content**

**Designing Your Commentary Editorial Policy**

Before drafting a complete set of notes, professional editors establish an Editorial Policy. Without a written policy, you will inevitably write too many notes on some paragraphs and none on others.

Your commentary policy should answer four basic questions:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
<tr style="background-color: #f1f5f9. Border-bottom: 2px solid #cbd5e1. ">
<th style="padding: 8px. Text-align: left. ">Policy Question</th>
<th style="padding: 8px. Text-align: left. ">Decision Criteria</th>
<th style="padding: 8px. Text-align: left. ">Example Standard</th>
    </tr>
  </thead>
  <tbody>
<tr style="border-bottom: 1px solid #e2e8f0. ">
<td style="padding: 8px. "><strong>Who is your target reader?</strong></td>
<td style="padding: 8px. ">Determines assumed prior knowledge</td>
<td style="padding: 8px. ">Undergraduate humanities students who need explanations of 18th-century currency.</td>
    </tr>
<tr style="border-bottom: 1px solid #e2e8f0. ">
<td style="padding: 8px. "><strong>What triggers a lexical note?</strong></td>
<td style="padding: 8px. ">Threshold for obsolete vocabulary</td>
<td style="padding: 8px. ">Any word absent from a standard modern collegiate dictionary, or used in an obsolete sense.</td>
    </tr>
<tr style="border-bottom: 1px solid #e2e8f0. ">
<td style="padding: 8px. "><strong>What entities require naming?</strong></td>
<td style="padding: 8px. ">Selection rule for historical figures</td>
<td style="padding: 8px. ">Every named historical person and every geographical location mentioned in the text.</td>
    </tr>
    <tr>
<td style="padding: 8px. "><strong>What is the maximum note length?</strong></td>
<td style="padding: 8px. ">Prevents sprawling essays</td>
<td style="padding: 8px. ">Notes must be concise (between 30 and 75 words) with at least one external reference.</td>
    </tr>
  </tbody>
</table>

Documenting these guidelines in a short `COMMENTARY.md` file guarantees consistency across all your edition notes.

**Vocabulary.** *Editorial Policy* — a written statement governing the principles, scope, and formatting standards applied by an editor to a text. *Annotation Threshold* — the set criteria that determine whether a textual feature merits an explanatory note.

**Takeaway:** Establish a clear commentary editorial policy defining target audience, entity naming rules, and note length limits before writing.

---

## **27 Content**

**Hands-On Exercise: Building the Standoff TEI Shell**

Let us now build the complete standoff TEI XML shell in VS Code. Create a new file named `commentary_hand.xml` or open your existing project TEI file.

Assemble the following components:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
    <fileDesc>
      <titleStmt>
        <title>Scholarly Commentary on Primary Witness</title>
        <editor xml:id="ed1">Student Editor</editor>
      </titleStmt>
      <publicationStmt>
        <p>RELS 398 Digital Methods Course Project</p>
      </publicationStmt>
      <sourceDesc>
        <p>Authored commentary anchored to primary archival witness.</p>
      </sourceDesc>
    </fileDesc>
  </teiHeader>
  <text>
    <body>
      <div type="transcription">
        <!-- Your base text with xml:id anchors -->
      </div>
    </body>
  </text>
  <standOff>
    <interpGrp type="categories">
      <interp xml:id="cat_phil">Philological &amp; Lexical</interp>
      <interp xml:id="cat_hist">Historical &amp; Contextual</interp>
      <interp xml:id="cat_inter">Intertextual &amp; Citational</interp>
    </interpGrp>
    <div type="commentary">
      <!-- Your typed standoff notes go here -->
    </div>
  </standOff>
</TEI>
```

Verify that your file validates against the TEI schema in VS Code.

**Vocabulary.** *TEI Shell* — the foundational XML document structure containing `teiHeader`, `text`, and optional `standOff` containers. *Well-Formedness Check* — confirming that all opening tags match closing tags and syntax is valid.

**Takeaway:** The standoff TEI shell provides a robust structure combining the `teiHeader`, base text record `<body>`, and annotations in `<standOff>`.

---

## **28 Content**

**Authoring a Five-Note Reference Corpus**

For today's lab milestone, you will author five high-quality commentary notes by hand on a single excerpt of your document.

Your five notes must include:
<ol>
  <li><strong>Two language / Lexical Notes:</strong> Explaining an archaic term, unusual spelling, or technical legal phrase.</li>
  <li><strong>Two Historical / Contextual Notes:</strong> explaining a named person, place, or institution, complete with an external standard URI (Wikidata, GeoNames, or Dictionary of Canadian Biography).</li>
  <li><strong>One Intertextual Note:</strong> Explaining a cross-reference, legal precedent, letter, or museum collection object.</li>
</ol>

Here is a checklist for every note you write:
<ul>
  <li>Does the note carry a valid `@target` starting with `#`?</li>
  <li>Does it specify `@type` and `@subtype`?</li>
  <li>Does it identify the author using `@resp`?</li>
  <li>Does the text inside avoid fluff, providing concise, verified information?</li>
</ul>

This hand-authored five-note set is your manual reference corpus.

**Vocabulary.** *Reference Corpus* — a verified, hand-curated dataset used as the gold standard for measuring automated and AI tools. *Gold Standard* — ground-truth data created with maximum human accuracy.

**Takeaway:** Authoring five diverse commentary notes creates a reliable manual gold standard for evaluating deterministic search tools and AI models.

---

## **29 Content**

**Documenting Your Manual Notes in `COMMENTARY.md`**

In professional software development and digital editing, data files are accompanied by records. In your project workspace, create a markdown file named `COMMENTARY.md`.

In `COMMENTARY.md`, record:
<ol>
  <li><strong>Document Summary:</strong> Title, archive shelfmark, date, and selected passage.</li>
  <li><strong>Note Inventory Table:</strong> A table listing each note's ID, target anchor, category, and core topic.</li>
  <li><strong>Sources Consulted:</strong> A book list of dictionaries, historical books. archive registers used to verify your facts.</li>
  <li><strong>Editorial Reflection (150–250 words):</strong> Discuss the challenges of manual commentary. Which notes took the longest to research? Where did modern dictionaries fail to explain historical terms?</li>
</ol>

This markdown ledger tracks your editorial decisions and will be updated on Wednesday and Friday as you compare manual notes with algorithmic and AI-assisted annotation.

**Vocabulary.** *records Ledger* — a structured text record tracking editorial decisions, research sources, and audit findings over time. *book list* — a systematic list of books, articles, and archive documents cited in scholarly work.

**Takeaway:** Document your research process and note inventory in `COMMENTARY.md` to maintain a permanent record of your editorial sources and methodology.

---

## **30 Content**

**Synthesis: The Human-in-the-Loop Foundation**

Today you have explored the foundational craft of scholarly commentary. You learned why commentary is an essential interpretive layer of a digital edition, distinct from physical text record and linguistic normalization.

You mastered key technical skills in Visual Studio Code:
<ul>
  <li>Classifying notes into language, historical, and intertextual categories.</li>
  <li>setting stable, non-breaking `xml:id` anchors in running text.</li>
  <li>Encoding annotations in a clean TEI `<standOff>` container using Chapter 17 principles.</li>
  <li>Connecting notes to text anchors via `@target` with proper `#` URI syntax.</li>
  <li>Enriching commentary with Linked Open Data standard records and book citations.</li>
</ul>

As we move forward in Week 12, remember: no computer algorithm and no artificial intelligence model can replace human judgment. Tomorrow, we will test deterministic tools for finding intertextual cross-references. On Friday, we will test large language models for drafting notes. But whatever automated tools propose, you—the human scholar—remain the final standard.

**Vocabulary.** *Human-in-the-Loop* — a workflow model where automated and AI systems assist humans, but human experts make all final critical decisions. *Scholarly Judgment* — the informed, critical evaluation of historical evidence and textual meaning.

**Takeaway:** Manual commentary sets up the irreplaceable human gold standard against which all automated and AI-assisted annotation tools must be evaluated.
