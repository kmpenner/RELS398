# Lesson 11.1 — Aligning Translation Sentences and Authoring Interlinear Glosses by Hand

*RELS 398 / ENGL 398 · Topic 11: Alignment · Meeting #28 (Tue Nov 17)*

***Step 1 of the three-step cycle: manual.** Today you align translation sentences and author four-line interlinear glosses by hand using the Leipzig Glossing Rules and TEI §16.1 standoff markup. That human gold standard is the reference for Wednesday's deterministic alignment tools and Friday's AI gloss generation.*

---

## **01 Content**

**Why Align Texts in a Digital Edition?**

In a printed book, translations usually sit on a facing page. Readers must look back and forth across the gutter. You must guess which English phrase matches each historical word. If the translator reorders sentences, the connection becomes confusing. Printed pages cannot show exact word links.

Digital editions solve this problem through **translation alignment**. Alignment creates explicit, clickable links between a source text and its translation. Instead of guessing, readers can click any historical sentence to see its modern translation. 

Alignment also holds editors accountable. Translators sometimes skip difficult phrases or smooth over strange grammar. When you link every sentence directly, all editorial decisions become visible. Nothing is hidden from the reader.

Today you begin the three-step comparative cycle for text alignment. Before you can align two texts, you must first produce a working **target text** (either an interlingual translation or an intralingual modern rendering). Then you will align sentences and words completely by hand. Your manual work will create the gold standard for testing automated tools tomorrow.

**Takeaway:** Digital alignment replaces guesswork with explicit links, connecting historical sentences directly to their modern translations.

---

## **02 Content**

**What is a Parallel Bitext? Interlingual vs. Intralingual Pairs**

In computational humanities, two connected versions of a text are called a **bitext**. A bitext is not simply two files stored in the same folder. It is a single data structure that links two text streams together.

Every bitext contains two distinct parts:

* **The Source Text:** The historical document in its original language and spelling (such as 18th-century French, colonial legal English, or vernacular handwriting).
* **The Target Text:** The parallel translation or modern reading version you author for contemporary readers.

Depending on your historical document, your bitext takes one of two forms:

* **Interlingual Bitext (Across Languages):** Translating a source document from one language into another—such as rendering Ace's 1791 French Revolutionary decree into modern English, or Olyvia's English letter into parallel Canadian French.
* **Intralingual Bitext (Across Registers or Eras):** Rendering a historical or dialectal English text into plain, modernized English—such as translating Andromeda's 1752 legal treaty clauses or Olyvia's 1967 Maritime vernacular handwriting into contemporary prose.

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Edition Type</th>
      <th style="width: 40%;">How Texts Are Stored</th>
      <th style="width: 35%;">Reader Experience</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Monolingual</strong></td>
      <td>One text file in one language.</td>
      <td>Readers see only original words.</td>
    </tr>
    <tr>
      <td><strong>Facing-Page Print</strong></td>
      <td>Two static pages side by side.</td>
      <td>Readers visually hunt for matches.</td>
    </tr>
    <tr>
      <td><strong>Digital Bitext</strong></td>
      <td>Two text streams linked by explicit IDs.</td>
      <td>Readers click to inspect linked pairs.</td>
    </tr>
  </tbody>
</table>

When you build a bitext—whether interlingual or intralingual—you map historical meaning across linguistic or historical distance.

**Takeaway:** A parallel bitext links a historical source text to an authored target text, whether interlingual (across languages) or intralingual (across historical registers).

---

## **03 Content**

**Step 0: Producing Your Target Text & Split-Editor Setup**

You cannot align a translation that does not exist yet. Before writing any alignment links, you must first produce your working target file (`target_translation.xml`) for a 10-sentence passage of your primary witness.

To draft a clean target text for alignment:

1. **Read sentence by sentence:** Work through your 10 chosen source sentences (`s1` through `s10`) in order, preserving their rhetorical flow.
2. **Draft an accountable rendering:** For non-English sources (Ace's French decree), draft a faithful modern English translation. For historical or vernacular English sources (Andromeda's 1752 Treaty or Olyvia's 1967 letter), draft a plain-language modern rendering (or a parallel French translation).
3. **Save in a separate TEI file:** Store your target sentences inside `target_translation.xml`—never paste translations inside your source manuscript XML.

Once `target_translation.xml` exists, Visual Studio Code lets you view both files side by side without switching tabs:

1. Open your source file (for example, `source_transcription.xml`).
2. Select **View > Editor Layout > Two Columns** (or press `Cmd+\` on macOS / `Ctrl+\` on Windows).
3. Drag `target_translation.xml` into the right pane.

This visual arrangement prevents mental fatigue and lets you verify sentence boundaries before encoding links.

**Takeaway:** Alignment begins by drafting a separate target text file (`target_translation.xml`), then opening source and target side by side in VS Code's two-column split editor.

---

## **04 Content**

**Sentences as Meaningful Units**

Before linking words, you must link larger grammatical units. The most natural unit of human thought is the **sentence**.

In historical manuscripts, sentences are not always easy to spot. Scribes often used erratic punctuation. An 18th-century French decree might run for fifteen lines before reaching a period. A personal letter might use dashes instead of periods.

When aligning historical texts, treat a sentence as a complete grammatical thought:

* It expresses a coherent action or statement.
* It usually contains a subject and a verb.
* It corresponds to a distinct sentence in a modern translation.

In your TEI XML file, you mark sentences using the standard `<s>` tag. Wrapping sentences in `<s>` tags creates clear targets for digital alignment.

**Takeaway:** Sentences marked with `<s>` tags provide the fundamental grammatical building blocks for sentence-level alignment.

---

## **05 Content**

**Assigning Unique Identifiers (`xml:id`)**

To link two sentences, the computer needs a way to address them. You give each sentence a unique name using the `xml:id` attribute.

Think of an `xml:id` as a street address:

* Every address in a town must be unique.
* No two sentences in your file may share the same `xml:id`.
* The ID should be short and predictable.

For our course, we use a simple naming convention:

* Source sentences use the prefix `s`: `xml:id="s1"`, `xml:id="s2"`, `xml:id="s3"`.
* Translation sentences use the prefix `t`: `xml:id="t1"`, `xml:id="t2"`, `xml:id="t3"`.

```xml
<!-- In the French source file -->
<s xml:id="s1">La Nation fait les assignats.</s>

<!-- In the English translation file -->
<s xml:id="t1">The Nation creates the paper currency.</s>
```

These IDs allow you to create clean, unambiguous links.

**Takeaway:** Every sentence receives a unique `xml:id` attribute so that external link elements can point to it without ambiguity.

---

## **06 Content**

**One-to-One Correspondences (1:1)**

The most straightforward alignment is a **one-to-one (1:1)** match. In a 1:1 match, exactly one source sentence translates into exactly one target sentence.

Consider this pair from an 18th-century proclamation:

* Source `s1`: *The Governor signed the treaty in council.*
* Target `t1`: *Le gouverneur a signé le traité en conseil.*

Both sentences start at the same point and finish at the same point. Their grammatical boundaries match. In modern translations of straightforward prose, 1:1 matches make up about eighty percent of all alignments.

When you find a 1:1 match, your editorial job is simple. You pair sentence `s1` directly with translation `t1`.

**Takeaway:** A one-to-one alignment occurs when a single source sentence maps directly onto a single translated sentence.

---

## **07 Content**

**One-to-Many Alignments (1:N)**

Historical writers loved long, complex sentences. An 18th-century legal decree often piles clause upon clause with semicolons. Modern English style prefers shorter, clearer sentences.

When a translator breaks one long historical sentence into two modern sentences, you have a **one-to-many (1:N)** alignment:

* Source `s4`: One long French legal clause of sixty words.
* Target `t4`: The first modern English sentence explaining the decree.
* Target `t5`: The second modern English sentence detailing the penalty.

You cannot force the translator's work back into a single sentence. Instead, your digital alignment must acknowledge reality. You link the single source sentence `s4` to both translation sentences: `t4` and `t5`.

**Takeaway:** A one-to-many alignment connects a single complex source sentence to multiple shorter modern translated sentences.

---

## **08 Content**

**Many-to-One Alignments (N:1)**

The opposite pattern also happens. Sometimes an original author writes several brief, telegraphic sentences. The translator combines them into a single flowing English sentence.

This pattern is a **many-to-one (N:1)** alignment:

* Source `s8`: *It rained.*
* Source `s9`: *The roads were bad.*
* Target `t8`: *Because it rained, the roads were muddy and impassable.*

In this example, the translator merged two historical sentences into one. 

When you link them, your alignment points from multiple source IDs to one target ID: `s8` and `s9` link to `t8`. Recognizing these shifts teaches you how translators interpret historical style.

**Takeaway:** A many-to-one alignment links multiple concise source sentences to a single combined translation sentence.

---

## **09 Content**

**Omissions and Additions (1:0 and 0:1)**

Sometimes a historical sentence has no translation at all. Other times, a modern translator adds an explanatory sentence not found in the original document.

These situations create special alignment patterns:

* **Omission (1:0):** A source sentence was omitted from the translation. You mark its target as `#none` or leave it unlinked.
* **Addition (0:1):** A modern translator added an introductory sentence to give context. It has no source counterpart.

<table>
  <thead>
    <tr>
      <th style="width: 20%;">Type</th>
      <th style="width: 30%;">Source Count</th>
      <th style="width: 30%;">Target Count</th>
      <th style="width: 20%;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1:1</strong></td>
      <td>One sentence</td>
      <td>One sentence</td>
      <td>Standard sentence</td>
    </tr>
    <tr>
      <td><strong>1:N</strong></td>
      <td>One sentence</td>
      <td>Two or more sentences</td>
      <td>Split legal clause</td>
    </tr>
    <tr>
      <td><strong>N:1</strong></td>
      <td>Two or more sentences</td>
      <td>One sentence</td>
      <td>Combined notes</td>
    </tr>
    <tr>
      <td><strong>1:0</strong></td>
      <td>One sentence</td>
      <td>Zero sentences</td>
      <td>Omitted formula</td>
    </tr>
  </tbody>
</table>

Recording omissions and additions ensures your digital edition remains honest about textual discrepancies.

**Takeaway:** Textual asymmetries include omissions (1:0) and additions (0:1), where sentences exist in only one language.

---

## **10 Content**

**Inline Markup vs. Standoff Markup**

How should we store these alignment links in XML? There are two different approaches: **inline markup** and **standoff markup**.

In inline markup, you place the translation directly inside the original text. You might put an `<add>` or `<note>` tag right next to every historical word. 

Inline markup causes serious problems:

* It clutters the historical text with modern words.
* It ruins the facsimile layout and line breaks.
* It makes validating the primary document difficult.

For translation alignment, the Text Encoding Initiative (TEI) strongly recommends **standoff markup**. In standoff markup, the source text and the translation live in clean, separate blocks. The links sit in a third location, pointing to both files.

**Takeaway:** Standoff markup stores alignment links separately from text content, keeping both original and translation files clean and valid.

---

## **11 Content**

**The TEI Standoff Philosophy**

Standoff markup treats your edition like a small library:

1. Book 1 is your transcribed manuscript witness.
2. Book 2 is your modern English translation.
3. The catalog index is your standoff link group.

Neither book is scribbled in or damaged by the catalog index. If you decide to add a second translation later (such as modern French or Mi'kmaw), you do not touch the original manuscript XML. You simply add another set of links.

This separation of concerns makes your digital edition durable. It follows the best practices of modern software design. It protects your hard work from accidental corruption.

**Takeaway:** The TEI standoff architecture separates text content from analytical links, allowing multiple translations without altering the base text.

---

## **12 Content**

**Introducing `<linkGrp>` and `<link>`**

The official TEI element for grouping alignment connections is `<linkGrp>` (link group). Inside `<linkGrp>`, each individual connection is represented by a `<link>` element.

The `<link>` element uses a single attribute named `@target`. The `@target` attribute holds the IDs of the two connected items, separated by a space:

```xml
<linkGrp type="translation-alignment">
  <link target="#s1 #t1"/>
  <link target="#s2 #t2"/>
  <link target="#s3 #t3"/>
</linkGrp>
```

Notice the number sign (`#`) before each ID. The number sign tells the XML processor: "Look for an element with this `xml:id` within this project."

If one source sentence matches two translation sentences, you list all three IDs in the target:

```xml
<link target="#s4 #t4 #t5"/>
```

**Takeaway:** The `<link>` element pairs sentence IDs using the `@target` attribute, prefixing each ID with a number sign (`#`).

---

## **13 Content**

**Placing the `<linkGrp>` in the TEI Document**

Where does `<linkGrp>` go inside your XML file? 

In TEI P5, you have two approved locations:

1. **Inside `<standOff>`:** Modern TEI includes a dedicated `<standOff>` element placed right after `<teiHeader>` or after `</text>`.
2. **Inside `<back>`:** You can place a `<div type="alignments">` inside the document's `<back>` matter.

Here is a typical document structure using `<standOff>`:

```xml
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
    <!-- Cataloguing metadata -->
  </teiHeader>
  <text>
    <!-- Primary transcription -->
  </text>
  <standOff>
    <linkGrp type="translation-alignment">
      <link target="#s1 #t1"/>
      <link target="#s2 #t2"/>
    </linkGrp>
  </standOff>
</TEI>
```

Keeping `<linkGrp>` inside `<standOff>` makes it easy for automated tools to locate your links.

**Takeaway:** Place your `<linkGrp>` elements inside a `<standOff>` element at the end of your TEI document for clean organization.

---

## **14 Content**

**Validating Standoff Links in VS Code**

When authoring standoff links by hand, it is easy to make a small typing error. If you mistype an ID, the link breaks.

Here is how to check your links in VS Code:

1. Check that every ID in `@target` starts with `#`. Typing `target="s1 t1"` without `#` is an invalid pointer.
2. Verify that the target sentence actually exists. If you write `#s5`, open your source pane and make sure `<s xml:id="s5">` is present.
3. Watch for red squiggly lines. If your XML schema checks ID references, VS Code will flag broken links immediately.
4. Check for duplicate IDs. Every `xml:id` must be completely unique across the file.

Taking five minutes to check these four rules will save hours of debugging later.

**Takeaway:** Valid standoff links always include the `#` prefix and point directly to existing, unique `xml:id` attributes.

---

## **15 Content**

**Moving from Sentences to Words: Why We Need Finer Detail**

Sentence alignment is helpful for general readers. But scholarly editions require deeper analysis.

Scholars often ask detailed linguistic questions:

* Exactly which historical French word translates as "deputy"?
* How did the 1752 treaty express colonial sovereignty in legal terminology?
* What grammatical form was Maud Lewis using when she wrote colloquial phrases?

To answer these questions, we must look below the sentence level. We must examine individual words and word parts. In linguistics, this fine-grained analysis is called **interlinear glossing**.

**Takeaway:** While sentence alignment links general ideas, interlinear glossing exposes the exact grammatical mechanics of individual words.

---

## **16 Content**

**What is an Interlinear Gloss?**

An **interlinear gloss** is a line of explanation written directly between the lines of a text. 

The practice has ancient roots:

* Medieval scribes wrote Latin glosses over Celtic and Old English texts.
* Monks added Greek words between Hebrew scriptural lines.
* 19th-century travelers wrote phonetic translations above Indigenous words.

In modern scholarship, interlinear glosses are not casual notes. They follow a rigorous international standard called the **Leipzig Glossing Rules**. The Leipzig rules turn informal marginal notes into a standardized grammatical language.

**Takeaway:** Interlinear glossing places grammatical and lexical explanations directly between text lines following standardized linguistic rules.

---

## **17 Content**

**The Leipzig Glossing Rules: An Overview**

The **Leipzig Glossing Rules** were developed by the Max Planck Institute for Evolutionary Anthropology and the University of Leipzig. They establish four rules of syntax and layout for multilingual texts.

The goal of the Leipzig rules is transparency:

* Anyone in the world should be able to understand the grammatical structure of your text, even if they do not speak the language.
* Every grammatical label must come from a shared list of standard abbreviations.
* Punctuation marks inside glosses have precise mathematical meanings.

Learning these rules allows you to present historical documents with professional scientific clarity.

**Takeaway:** The Leipzig Glossing Rules provide an international standard for formatting multilingual texts so their grammar is clear to any scholar.

---

## **18 Content**

**The Four-Tier Architecture of Leipzig Glossing**

A complete Leipzig gloss uses four vertical lines, stacked directly on top of each other:

1. **Line 1 (Source Text):** The exact historical words from your manuscript witness.
2. **Line 2 (Morpheme Breakdown):** The words divided into their grammatical stems and endings.
3. **Line 3 (Grammar Gloss):** Standardized labels identifying what each ending does grammatically.
4. **Line 4 (Free Translation):** A natural English sentence enclosed in quotation marks.

```text
Line 1: Les     citoyens parlèrent.
Line 2: le-s    citoyen-s parlé-rent
Line 3: DEF-PL  citizen-PL speak-3PL.PST
Line 4: "The citizens spoke."
```

Each vertical column aligns word-for-word. A reader can look straight down to see how each historical ending works.

**Takeaway:** The four-line Leipzig layout moves systematically from raw historical spelling to grammatical breakdown, linguistic labels, and modern translation.

---

## **19 Content**

**Tier 1: The Historical Surface Text**

Line 1 displays the **surface text**. The surface text is what your eyes see on the physical page.

When authoring Line 1:

* Preserve the historical spelling exactly as found in your document.
* Retain original accents, archaic letters, and contractions.
* Do not modernize spellings or expand abbreviations here.
* Separate each word with a space so it aligns with the lines below.

For Ace's French decree, Line 1 preserves 18th-century spellings like *assignats*. For Olyvia's letters, Line 1 preserves Maud Lewis's original handwriting and punctuation.

**Takeaway:** Line 1 preserves the raw historical spelling of the witness without modernization or silent alterations.

---

## **20 Content**

**Tier 2: Word and Morpheme Segmentation**

A **morpheme** is the smallest meaningful unit in a language. For example, the English word *cats* has two morphemes: the base noun *cat* and the plural ending *-s*.

In Line 2 of your gloss, you divide words into their constituent morphemes:

* Use a hyphen (`-`) to separate prefixes, stems, and suffixes.
* If a word cannot be broken into smaller pieces, leave it without hyphens.
* Align each segmented word directly beneath its Line 1 counterpart.

In French:

* Line 1: *décrets*
* Line 2: *décret-s* (stem + plural suffix)

Segmenting morphemes makes the building blocks of historical vocabulary visible to students and readers.

**Takeaway:** Line 2 breaks complex words into stems and grammatical endings using hyphens to mark boundaries.

---

## **21 Content**

**Tier 3: Grammatical Abbreviations**

Line 3 is where you provide grammatical definitions. The Leipzig standard uses a shared vocabulary of capital abbreviations.

Here are the most common labels you will use:

* `DEF`: Definite article (*the*)
* `INDF`: Indefinite article (*a*, *an*)
* `SG`: Singular
* `PL`: Plural
* `PST`: Past tense
* `PRS`: Present tense
* `1`, `2`, `3`: First, second, or third person
* `NEG`: Negative particle (*not*)

Whenever you gloss a lexical stem, use regular lowercase English (*citizen*, *speak*, *letter*). Whenever you gloss a grammatical function, use standard uppercase labels (`PL`, `PST`).

**Takeaway:** Line 3 combines lowercase English meanings for word stems with standard uppercase abbreviations for grammatical endings.

---

## **22 Content**

**The Hyphen vs. The Period: Rule 2 Explained**

The most famous rule in the Leipzig system is Rule 2. It governs punctuation in Line 3:

* **Use a Hyphen (`-`)** when there is a visible boundary in Line 2. A hyphen connects separate parts:
  * Line 2: *book-s*
  * Line 3: *book-PL* (one hyphen above, one hyphen below).

* **Use a Period (`.`)** when a single indivisible piece expresses multiple grammatical meanings at once:
  * In the French word *parla* ("he spoke"), the single letter *-a* expresses third person, singular, and past tense all together.
  * Line 2: *parl-a*
  * Line 3: *speak-3SG.PST*

The period signals that *3*, *SG*, and *PST* cannot be separated into distinct physical letters.

**Takeaway:** Hyphens mark physical boundaries between distinct morphemes; periods join multiple grammatical concepts packed into a single ending.

---

## **23 Content**

**Tier 4: The Free Idiomatic Translation**

Line 4 provides the **free translation**. 

While Lines 2 and 3 provide a literal, word-by-word breakdown, Line 4 gives the complete sentence in natural, idiomatic English. It shows how a fluent speaker would express the thought today.

Guidelines for Line 4:

* Always enclose the translation in double quotation marks.
* Use standard modern English punctuation and capitalization.
* Do not force awkward word order just to match the historical language.
* Ensure the translation captures the full legal or personal meaning of the passage.

Line 4 provides the context that makes the linguistic analysis above it meaningful.

**Takeaway:** Line 4 delivers a fluent, idiomatic English translation enclosed in quotation marks, conveying the complete meaning of the passage.

---

## **24 Content**

**Case Study 1: French Revolutionary Decree (Ace's Document)**

Let us examine how to gloss an excerpt from Ace's 1791 French decree (*Loi relative à la fabrication des assignats*).

Here is an official legal sentence:
*Line 1:* *L' Assemblée Nationale décrète la fabrication.*

Now we author the four Leipzig tiers:

* **Line 1 (Surface):** `L' Assemblée National-e décrète la fabrication.`
* **Line 2 (Segmentation):** `l' assemblée national-e décrèt-e la fabrication`
* **Line 3 (Gloss):** `DEF.SG assembly national-F.SG decree-3SG.PRS DEF.F.SG manufacture`
* **Line 4 (Translation):** `"The National Assembly decrees the manufacture."`

Notice how `l'` is glossed as `DEF.SG` with a period, because the single letter indicates both a definite article and singular number.

**Takeaway:** Applying Leipzig rules to 18th-century French clarifies how gender, number, and verb conjugations function in legal proclamations.

---

## **25 Content**

**Case Study 2: Peace and Friendship Treaty of 1752 (Andromeda's Document)**

Andromeda's document is the 1752 Peace and Friendship Treaty concluded in Halifax. It features formal colonial treaty language.

Consider this opening clause:
*Line 1:* *It is agreed that the Treaty of 1726 shall be renewed.*

In colonial documents, formal modal verbs like *shall* carry legal force. When glossing historical English into a parallel modern version:

* **Line 1:** `It is agreed that the Treaty of 1726 shall be renewed.`
* **Line 2:** `it is agree-d that the treaty of 1726 shall be renew-ed`
* **Line 3:** `3SG.EXPL be.3SG.PRS agree-PST.PTCP COMP DEF treaty of 1726 OBLIG be renew-PST.PTCP`
* **Line 4:** `"It is agreed that the 1726 Treaty must be renewed."`

Glossing legal terms reveals how power, obligation, and agreement were encoded in colonial treaties.

**Takeaway:** Glossing historical legal English highlights the precise function of modal verbs and passive agreements in colonial treaties.

---

## **26 Content**

**Case Study 3: Folk Art Correspondence (Olyvia's Document)**

Olyvia's document is an intimate 1967 personal letter written by Nova Scotia folk artist Maud Lewis to Leonard Kinnear.

Maud Lewis wrote in an informal, vernacular style:
*Line 1:* *I got your letter and was glad to hear from you.*

Because Maud's text is already in modern English, why do we gloss it? 

1. **Vernacular Grammar:** Dialectal phrases and regional idioms can be glossed to explain their historical and cultural nuance.
2. **Translation Alignment:** Her letters can be aligned with a parallel French translation for bilingual Canadian research.
3. **Normalized Reading Text:** An informal handwritten sentence can be aligned directly with an editorial regularized version.

Alignment is not just for ancient languages. It clarifies relationships between informal handwriting and formal published editions.

**Takeaway:** Interlinear glossing and alignment help scholars document vernacular dialect, informal handwriting, and parallel French translations.

---

## **27 Content**

**Encoding Leipzig Glosses in TEI XML**

How do we represent a four-line Leipzig gloss inside TEI XML? The TEI provides specialized linguistic elements:

* `<w>`: Represents a single word.
* `<m>`: Represents an individual morpheme inside a word.
* `<gloss>`: Contains the grammatical or lexical definition.

Here is how a single glossed word looks in clean TEI:

```xml
<w xml:id="w1">
  <m type="root">parl</m>
  <m type="suffix">-er</m>
  <gloss>speak-INF</gloss>
</w>
```

When you want to display the full four lines on a web page, you can group them inside an `<interlinear>` or `<table>` structure. This ensures the columns line up perfectly on screen.

**Takeaway:** TEI encodes interlinear glosses using `<w>` for words, `<m>` for morphemes, and `<gloss>` for linguistic definitions.

---

## **28 Content**

**Common Novice Pitfalls in Manual Alignment**

When students first align texts by hand, four common mistakes occur:

1. **The Missing Hash Mark:** Writing `target="s1 t1"` instead of `target="#s1 #t1"`. Without `#`, your software thinks you are linking to an external website.
2. **Unbalanced Columns:** Putting three words in Line 1, but four glosses in Line 3. Every word above must have exactly one corresponding gloss column below.
3. **Confusing Hyphens and Periods:** Using hyphens when no physical letter boundary exists in the text.
4. **Accidentally Deleting Original Spacing:** Removing spaces between words, causing gloss columns to collapse together.

Checking for these simple issues ensures your manual work is flawless.

**Takeaway:** Common alignment mistakes include missing `#` hash prefixes, mismatched column counts, and improper use of hyphens versus periods.

---

## **29 Content**

**Creating Your Tuesday Ground Truth Files**

Today in class, you will create three clean files in your personal project folder:

1. `target_translation.xml`: Your authored 10-sentence parallel target text (English translation for French sources, or modernized/plain-language rendering for historical or vernacular English sources).
2. `alignment_manual.xml`: A TEI file containing your 10-sentence passage and a standoff `<linkGrp>` linking source sentences to your target sentences.
3. `gloss_manual.xml`: A clean file containing your four-line Leipzig interlinear gloss for three selected sentences.

Take your time. Read each sentence carefully. Adjudicate every word division against your historical document.

This file is your **ground truth**. It represents human scholarly judgment. You will keep this file safe to test automated tools later this week.

**Takeaway:** Your Tuesday manual files establish the verified human ground truth against which all algorithmic and AI tools will be measured.

---

## **30 Content**

**Looking Ahead: Why Today's Manual Work Matters**

Congratulations on completing your first manual alignment and linguistic gloss!

Here is why your manual effort is so valuable:

* **Wednesday's Lesson (Deterministic Tools):** Tomorrow we will introduce automated sentence alignment software (the Gale-Church algorithm). You will test whether a computer script can match the sentences you aligned by hand.
* **Friday's Lesson (AI Assistance):** On Friday, you will ask an AI model in VS Code to generate alignments and Leipzig glosses. You will evaluate where the AI succeeded and where it stumbled.

Without today's manual baseline, you would have no way to evaluate automated tools. Scholarly digital editions always begin with human expertise.

**Takeaway:** Today's manual alignment provides the essential benchmark required to test and audit automated and AI-assisted tools for the rest of the week.
