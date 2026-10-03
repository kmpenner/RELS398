# Lesson 6.1 — Manual Normalization, Abbreviations, and Editorial Policy

*RELS 398 / ENGL 398 · Topic 6: Normalization · Meeting #14 (Tue Oct 6)*

***Step 1 of the three-step cycle: manual.** Today you establish your editorial regularization policy by hand, recording every spelling standardization and abbreviation expansion. Those recorded decisions become the rules Wednesday's regular expressions implement and Friday's AI pass is measured against.*

---

## **01 Content**

**The Problem Normalization Solves and Creates**

In Week 4, you produced an initial diplomatic transcription of your historical witness, and in Week 5, you reconciled it with an AI pass to establish a reliable consensus text in `transcription_reconciled.xml`. That diplomatic transcription records exactly what appears on the physical page: line breaks, capital letters, historical spellings, and scribal shorthand. That fidelity is the indispensable foundation of textual scholarship, but it immediately creates a practical dilemma for modern digital readers and researchers.

Historical writers rarely adhered to rigid orthographic standards. The same writer might spell a single word three different ways across two folios. In an 18th-century colonial treaty, you will find common nouns capitalized arbitrarily and words ending in archaic suffixes like *publick* alongside *public*. In 19th-century manuscript poetry, idiosyncratic capitalization and punctuation convey private emphasis. In 20th-century personal letters, vernacular phonetic spellings like *untill* or *allways* record spoken cadence.

When a digital text preserves only raw diplomatic spellings, computational search and discovery tools break down. A search query for *public* will fail to retrieve *publick*. A morphological analyzer or dictionary lookup cannot recognize unstandardized forms. Dialectal variations and historical shorthand render the document partially invisible to natural language processing engines, digital concordances, and full-text indexing (Burnard, 2014).

The traditional solution in print editing was simply to modernize the spelling silently. However, standardizing text on the page destroys the very historical evidence we set out to preserve. A scribe's variant spellings document phonological change, regional dialect, educational background, and scribal culture (Clemens & Graham, 2007). 

**Vocabulary.** *Normalization* — Mapping variant historical orthographic forms to modern standard lexical headwords. *Regularization* — The TEI term for standardizing spelling without altering underlying wording. *Diplomatic transcription* — A faithful representation of the text exactly as written on the physical witness.

**Takeaway:** Standardizing spelling makes historical documents digitally searchable, but silent modernization destroys crucial linguistic, dialectal, and scribal evidence.

---

## **02 Content**

**The Scholarly Dilemma: Preservation vs. Accessibility**

The digital editor stands between two competing demands: scholarly preservation and communicative accessibility. If you prioritize only preservation, your edition remains an accurate museum artifact of ink on parchment, but modern students and algorithmic search tools will struggle to read or query it. If you prioritize only accessibility by modernizing every word, you produce a smooth reading text while erasing the material and cultural specificity of the original author.

Textual theorists describe this tension as the conflict between the document as a physical artifact and the work as an abstract linguistic text (Driscoll, 2006). A diplomatic transcription privileges the physical event of inscription: the specific strokes of ink made by a colonial secretary in Halifax in 1752, Emily Dickinson in Amherst in 1862, or Maud Lewis in Digby in 1945. A normalized edition privileges the modern reader's ability to comprehend the message and link it to broader vocabularies.

In print scholarship, an editor was forced to choose one layer as primary and relegate the other to the footnotes or back matter. A "diplomatic edition" printed the historical spellings, forcing readers to consult a glossary for archaic abbreviations. A "critical edition" printed normalized spellings, crowding the bottom of the page with variant apparatus entries.

Digital text encoding eliminates the need for this painful compromise. Rather than forcing one layer to destroy or subordinate the other, the digital medium allows both layers to exist simultaneously within a single data structure (Pierazzo, 2015). The reader or downstream application can toggle between a strict diplomatic view and a standardized reading view on demand.

**Vocabulary.** *Document layer* — The textual record emphasizing physical and orthographic fidelity to the manuscript. *Reading layer* — The textual record regularized to modern orthographic standards for ease of comprehension and computational indexing.

**Takeaway:** Digital text encoding resolves the conflict between preservation and accessibility by maintaining diplomatic and normalized layers in parallel within a single document.

---

## **03 Content**

**The TEI Resolution: Parallel Layers with `<choice>`**

The Text Encoding Initiative (TEI) solves the preservation dilemma through parallel markup. Instead of altering the raw transcription or appending separate footnotes, the TEI provides the `<choice>` element (TEI Consortium, 2024).

The `<choice>` element functions as an editorial container. It signals to any processing software or human reader that two or more alternative encodings of the same textual unit are available. Within a `<choice>` block, the editor provides both the exact diplomatic reading found on the physical surface and the editorial regularization supplied for modern consumption.

When a digital publishing interface like TEI Publisher or an interactive HTML viewer renders a document containing `<choice>`, it can display either reading based on user preference. A researcher studying historical dialect can inspect the diplomatic layer with a single click, while a classroom student reading the text for historical content can toggle the normalized layer. Furthermore, web search crawlers and concordance builders can index both representations simultaneously.

The power of `<choice>` lies in its explicitness. It makes the editor's intervention visible, transparent, and reversible. An editor does not overwrite history; they annotate it. Every time you normalize an archaic form, you preserve the scribe's original handwriting directly alongside your modern interpretation.

**Vocabulary.** *`<choice>`* — A TEI element that groups alternative encodings of the same textual point, such as original spellings and normalized forms. *Parallel markup* — Encoding multiple interpretive layers simultaneously within the same document hierarchy.

**Takeaway:** The TEI `<choice>` element acts as a transparent container that holds original witness readings and modern editorial regularizations side by side.

---

## **04 Content**

**Orthographic Regularization: `<orig>` and `<reg>`**

When your goal is to regularize historical spelling without alleging that the historical writer made an error, the TEI `<choice>` element pairs two specific child elements: `<orig>` (original) and `<reg>` (regularization).

The `<orig>` element contains the raw, unstandardized characters exactly as transcribed from the witness. The `<reg>` element contains the standardized modern spelling established by the editor. The basic syntax is structured as follows:

```xml
<choice>
  <orig>publick</orig>
  <reg>public</reg>
</choice>
```

In this structure, `<orig>` represents the historical linguistic reality: the word *publick* as printed or written in an 18th-century document. The `<reg>` element provides the modern lexicographical standard: *public*. A search algorithm indexing the `<reg>` tag can connect this occurrence to every other instance of the word in a modern corpus, while an epigrapher or historical linguist can query the `<orig>` tag to chart the decline of terminal *k* in 18th-century English adjectives.

Notice that `<choice>` wraps only the specific lexical unit being regularized, not the entire sentence or line. Maintaining tight, word-level granularity ensures that surrounding whitespace, punctuation, and structural tags like `<lb/>` remain unaffected.

**Vocabulary.** *`<orig>`* — TEI element containing the original, un-regularized spelling found in the historical witness. *`<reg>`* — TEI element containing a regularized modern spelling supplied by the editor.

**Takeaway:** Pair `<orig>` and `<reg>` within a `<choice>` element to record historical orthography alongside modern standard spelling at word-level granularity.

---

## **05 Content**

**Editorial Responsibility and the `@resp` Attribute**

In academic digital editing, no editorial alteration should occur anonymously. Whenever an editor normalizes a word, expands an abbreviation, or amends a reading, the markup must explicitly record who authorized that interpretation. In the TEI Guidelines, this accountability is enforced through the `@resp` (responsibility) attribute (TEI Consortium, 2024).

The `@resp` attribute points to an identifier defined in the TEI Header—specifically within the `<titleStmt>` where editors, transcribers, and project contributors are catalogued. If your project header defines your role with `xml:id="KP"`, your regularization markup should explicitly reference your authority:

```xml
<choice>
  <orig>compleat</orig>
  <reg resp="#KP">complete</reg>
</choice>
```

Why is the `@resp` attribute attached to `<reg>` rather than `<orig>`? The original characters inside `<orig>` belong to the historical document and its primary author or scribe. You did not create *compleat*; the scribe wrote it. Conversely, the modern spelling *complete* is an interpretive editorial decision supplied by you.

Recording responsibility ensures that if a future scholar disagrees with your normalization—arguing, for instance, that an archaic word should have been regularized to a different lemma—they can trace the decision back to the specific editor and rationale recorded in the edition.

**Vocabulary.** *`@resp`* — A TEI attribute indicating the agent (editor, institution, or algorithm) responsible for an editorial intervention. *Editorial accountability* — The practice of explicitly attributing every interpretive layer of an edition to an identifiable scholar or project.

**Takeaway:** Always attach the `@resp` attribute to your regularized `<reg>` element to document who made the editorial intervention.

---

## **06 Content**

**Abbreviations in Historical Documents**

Historical documents are dense with abbreviations. Whether examining a medieval parchment charter, an 18th-century colonial treaty, a personal letter, or a revolutionary proclamation, writers consistently shortened words to save time, space, and materials.

Before the widespread availability of cheap industrial wood-pulp paper in the mid-19th century, writing surfaces were expensive commodities. In medieval and early modern scriptoria, parchment made from animal hide was labor-intensive and costly; scribes compressed text using elaborate systems of scribal shorthand to maximize the words per leaf (Clemens & Graham, 2007). Even after paper became common, bureaucratic clerks facing mountains of repetitive legal documents developed rapid abbreviation conventions for titles, dates, formulas, and legal terminology.

In informal writing, such as the personal correspondence of folk artist Maud Lewis, abbreviations reflect the natural tempo of vernacular communication. Writers omit apostrophes in common contractions (*cant*, *wont*) or truncate common words (*Nov.* for *November*). 

Leaving abbreviations unexpanded in a digital edition preserves the look of the document, but it creates severe barriers for readers unfamiliar with historical paleography and causes text-mining tools to miss critical named entities and titles. A complete digital edition must therefore account for abbreviations systematically.

**Vocabulary.** *Scribal abbreviation* — A conventional graphic compression of a word or phrase practiced by scribes and clerks to conserve space or speed writing. *Tironian notes* — An ancient Roman system of shorthand whose conventions influenced medieval and early modern European scribal abbreviations.

**Takeaway:** Historical abbreviations were practical tools for conserving expensive writing surfaces and speeding manual transcription, but they require digital expansion for modern accessibility.

---

## **07 Content**

**Encoding Abbreviations: `<abbr>` and `<expan>`**

Just as the TEI provides `<orig>` and `<reg>` for orthographic variation, it provides a dedicated pair of elements within `<choice>` for abbreviations: `<abbr>` (abbreviation) and `<expan>` (expansion) (TEI Consortium, 2024).

The `<abbr>` element captures the abbreviated form exactly as written on the manuscript page, including any raised superscript letters, periods, or truncation slashes. The `<expan>` element provides the fully expanded word supplied by the editor:

```xml
<choice>
  <abbr>Gov<hi rend="superscript">r</hi></abbr>
  <expan resp="#editor">Governor</expan>
</choice>
```

In this example from an 18th-century official proclamation, the clerk wrote *Gov* with a superscript *r*. A reading environment can render the raw abbreviation to show students how 18th-century titles were formatted, or it can swap in the expanded word *Governor* so a search for the office succeeds across all colonial records.

As with regularization, the expansion carries the `@resp` attribute because supplying the missing letters is an act of editorial interpretation. If a clerk writes *Hon.*, deciding whether to expand it as *Honorable*, *Honourable*, or *Honorary* requires scholarly judgment based on the document's date, location, and institutional context.

**Vocabulary.** *`<abbr>`* — TEI element containing an abbreviation of any kind. *`<expan>`* — TEI element containing the expansion of an abbreviation supplied by an editor.

**Takeaway:** Use `<choice><abbr>...</abbr><expan resp="#editor">...</expan></choice>` to encode historical abbreviations and their full editorial expansions in parallel.

---

## **08 Content**

**Suspensions, Contractions, and Brevigraphs**

To transcribe and expand abbreviations accurately, an editor must recognize the three primary morphological mechanisms used in historical writing: suspensions, contractions, and brevigraphs (Clemens & Graham, 2007).

A **suspension** occurs when the beginning of a word is written and the end is omitted, typically indicated by a terminal dot, colon, or horizontal stroke. For example, writing *Feb.* for *February* or *art.* for *article* in a French legal decree is a suspension. The reader is expected to supply the missing grammatical ending from the context.

A **contraction** occurs when the first and last letters of a word are retained while internal letters are dropped. In early modern English and colonial legal documents, contractions frequently place the terminal letters in superscript: *w<hi rend="superscript">ch</hi>* for *which*, *y<hi rend="superscript">e</hi>* for *the*, or *M<hi rend="superscript">r</hi>* for *Mister*.

A **brevigraph** is a specialized symbol or ligature that stands for an entire common syllable or word. The ampersand (*&*) is the most familiar surviving brevigraph, representing Latin *et* and English *and*. Another common brevigraph is *&c.* for *etcetera*. In TEI encoding, all three types are captured inside `<abbr>` and expanded inside `<expan>`.

**Vocabulary.** *Suspension* — An abbreviation where the end of the word is dropped. *Contraction* — An abbreviation where middle letters are omitted, often leaving the final letters in superscript. *Brevigraph* — A distinct symbol or monogram representing a complete word or syllable.

**Takeaway:** Historical abbreviations fall into three main types—suspensions, contractions, and brevigraphs—all of which are encoded using TEI `<abbr>` and `<expan>`.

---

## **09 Content**

**Regularization vs. Correction: `<reg>` vs. `<corr>`**

One of the most frequent errors made by novice text encoders is confusing **regularization** with **correction**. The TEI maintains a strict, fundamental distinction between these two editorial actions, and mixing them up distorts the linguistic truth of your witness (TEI Consortium, 2024).

**Regularization** (`<orig>` and `<reg>`) applies to valid historical, regional, dialectal, or archaic forms. When an 18th-century writer spells *honour* as *honor*, or *public* as *publick*, or writes *étoit* instead of modern French *était*, the writer has not committed an error. They were writing acceptable, standard orthography for their time and culture. You regularize the form solely to assist modern digital retrieval.

**Correction** (`<sic>` and `<corr>`), by contrast, applies when the historical writer or printer made a genuine blunder—a slip of the pen, an accidental repetition (dittography), a missing letter that violates the language's own rules, or an obvious typographical error. If a scribe writes *the the* across a line break, or misspells a common word through clear mechanical inattention, the erroneous text is tagged with `<sic>` (Latin for "thus"), and the editorial correction is tagged with `<corr>`:

```xml
<choice>
  <sic>recieved</sic>
  <corr resp="#editor">received</corr>
</choice>
```

Never label an author's valid historical orthography as `<sic>`. Calling an 18th-century spelling "erroneous" reflects modern editorial arrogance; treat valid historical variation with `<orig>`/`<reg>`, and reserve `<sic>`/`<corr>` strictly for unambiguous mistakes.

**Vocabulary.** *`<sic>`* — TEI element indicating that text in a witness is reproduced verbatim despite being an error. *`<corr>`* — TEI element containing the editor's correction of an apparent error. *Scribal error* — A genuine blunder or slip of the pen, distinguished from acceptable historical spelling variation.

**Takeaway:** Use `<orig>`/`<reg>` for acceptable historical and dialectal spelling variants, and reserve `<sic>`/`<corr>` strictly for genuine scribal blunders.

---

## **10 Content**

**Case Study 1: 18th-Century Legal English (1752 Treaty)**

To understand how these principles operate in real projects, let us examine the first document in our course cohort: the **Peace and Friendship Treaty of 1752**, an official colonial legal instrument printed and inscribed in Nova Scotia (Archives RG 1 vol 430 no 2).

Official English documents of the mid-18th century exhibit distinct orthographic conventions that differ sharply from 21st-century practice:

<ol>
  <li><strong>Capitalization of Common Nouns:</strong> Eighteenth-century printing conventions capitalized almost all substantive nouns for visual emphasis (e.g., <em>Treaty</em>, <em>Governor</em>, <em>Articles</em>, <em>Tribe</em>, <em>Peace</em>). In a modern reading edition, an editor may choose to lowercase common nouns while retaining capitals for proper names.</li>
  <li><strong>Terminal Archaic Suffixes:</strong> Adjectives and nouns frequently retain older Germanic and French spellings, such as <em>publick</em>, <em>traffick</em>, and <em>compleat</em>.</li>
  <li><strong>The Long s:</strong> The typographical long <em>s</em> (<em>ſ</em>) appears throughout the printed text at the beginning and middle of words, while the short <em>s</em> appears only at the end.</li>
</ol>

When an editor normalizes the 1752 Treaty, they must decide whether the capitalization of nouns is syntactic (requiring regularization) or stylistic. If your editorial policy determines that common nouns should be regularized for sentence-level reading while preserving the original layout, you encode each instance deliberately:

```xml
<choice>
  <orig>Treaty</orig>
  <reg resp="#editor">treaty</reg>
</choice>
```

**Vocabulary.** *Long s (ſ)* — An archaic graphic variant of the lowercase letter *s* used initially and medially in handwriting and print until the early 19th century. *Substantive capitalization* — The 18th-century printing practice of capitalizing common nouns.

**Takeaway:** Eighteenth-century legal documents feature substantive noun capitalization, archaic terminal suffixes, and the long *s*, requiring clear editorial decisions about what to regularize.

---

## **11 Content**

**Archaic Contractions and Superscripts in Colonial Documents**

In addition to capitalization, the 1752 Treaty and contemporary colonial legal records rely heavily on traditional scribal contractions that confuse modern optical character recognition systems and novice readers.

The most famous example is the pseudo-archaic word *ye*, as in *ye Governor*. Novice readers frequently pronounce this word with a /j/ sound, imagining that early modern English speakers said "ye olde shop." In reality, the character written as *y* in *ye* is a scribal survivor of the Old and Middle English rune **thorn** (þ), which represented the /θ/ or /ð/ sound (*th*). When movable type was introduced to England from the Continent, German- and Dutch-cast fonts lacked a thorn sort, so English printers substituted the visually similar letter *y*. 

When a 1752 clerk wrote *y<hi rend="superscript">e</hi>*, they were simply writing *the*. When they wrote *y<hi rend="superscript">t</hi>*, they were writing *that*. In TEI, this is treated as an abbreviation contraction, not a spelling variant:

```xml
<choice>
  <abbr>y<hi rend="superscript">e</hi></abbr>
  <expan resp="#editor">the</expan>
</choice>
```

Other ubiquitous colonial abbreviations include legal titles (*Esq<hi rend="superscript">r</hi>* for *Esquire*, *Gov<hi rend="superscript">r</hi>* for *Governor*) and commercial transaction terms (*rec'd* for *received*). By tagging these with `<abbr>` and `<expan>`, you preserve the graphic reality of 18th-century typography while delivering clear modern syntax to readers.

**Vocabulary.** *Thorn (þ)* — An ancient Germanic rune and Old/Middle English letter representing the *th* sound, often represented by the letter *y* in early modern printing. *Pseudo-archaisms* — Modern misinterpretations of historical graphic conventions, such as pronouncing *ye* as a *y* sound.

**Takeaway:** Early modern *ye* is a typographical substitution for the letter thorn, representing the word *the*, and should be encoded as an abbreviation with `<abbr>` and `<expan>`.

---

## **12 Content**

**Case Study 2: 19th-Century Poetic Idiosyncrasy (Emily Dickinson)**

Our second cohort project examines an autograph manuscript poem by **Emily Dickinson** (`MS Am 1118.3 [338]`, Amherst/Harvard). Dickinson's handwriting presents the exact opposite editorial challenge from an official printed treaty. Her manuscripts are intimate, private literary artifacts where orthography and layout are inseparable from poetic expression.

Dickinson's manuscripts display several famous idiosyncratic features:

<ul>
  <li><strong>Heavy Capitalization:</strong> She capitalizes common nouns and adjectives according to private psychological, symbolic, and rhythmic impulses (e.g., <em>Soul</em>, <em>Society</em>, <em>Door</em>, <em>Valves</em>, <em>Stone</em>).</li>
  <li><strong>The Dickinson Dash:</strong> In place of conventional commas, semicolons, and periods, Dickinson uses variable horizontal and slanted pen strokes of differing lengths (dashes), creating musical pauses and syntactic ambiguity.</li>
  <li><strong>Variant Spellings:</strong> She occasionally employs older, phonetic, or variant spellings, such as <em>opake</em> for <em>opaque</em>, or <em>etherial</em> for <em>ethereal</em>.</li>
</ul>

When editing Dickinson, an editor must confront the question: is an unusual spelling an error to be corrected, a historical spelling to be regularized, or an intentional poetic choice that must not be touched?

```xml
<choice>
  <orig>opake</orig>
  <reg resp="#editor">opaque</reg>
</choice>
```

While tagging *opake* with `<orig>` and `<reg>` allows modern readers to search for the poem using standard spelling, regularizing her capitalization or replacing her dashes with commas risks flattening her unique poetic voice.

**Vocabulary.** *Autograph manuscript* — A manuscript written in the author's own hand, rather than by a professional scribe or secretary. *Poetic orthography* — The deliberate or idiosyncratic use of spelling, capitalization, and punctuation for literary and rhythmic effect.

**Takeaway:** Emily Dickinson's autograph poetry uses capitalization, dashes, and variant spellings as expressive artistic devices, requiring extreme caution during normalization.

---

## **13 Content**

**When NOT to Normalize: The Poetic Boundary**

The power to normalize text in TEI brings with it the responsibility of restraint. Just because you *can* regularize a word does not mean you *should*. Nowhere is this principle more vital than in literary and poetic editing.

In modern publishing, editors have frequently inflicted severe damage on Dickinson's poetry by standardizing her work. Early post-mortem editors in the 1890s replaced her characteristic dashes with conventional commas and full stops, regularized her capitalized nouns to lowercase, and smoothed out her rhymes to fit Victorian hymnal meters. In doing so, they destroyed the jagged, hesitant, modernist rhythms that make her poetry revolutionary.

In your digital edition, you must define explicit boundaries between **orthographic regularization** and **editorial interference**. If Dickinson writes:

```text
The Soul selects her own Society —
Then — shuts the Door —
```

Regularizing *Society* to *society* or *Door* to *door* would eliminate her deliberate personification of abstract concepts. In a diplomatic edition of 19th-century poetry, capitalization that serves an artistic purpose should generally be preserved without a `<reg>` tag, unless your project explicitly creates a dual "reading text" for school children.

Before tagging any word with `<choice>`, ask yourself: does this spelling reflect mere mechanical variation, or does it carry semantic and aesthetic weight? If it carries aesthetic weight, leave it unaltered.

**Vocabulary.** *Over-editing* — The harmful editorial practice of regularizing authorial idiosyncrasies that were deliberately chosen for stylistic or artistic effect. *Personification capitalization* — Capitalizing common nouns to invest abstract concepts with human agency.

**Takeaway:** Editorial restraint is essential: never normalize capitalization, punctuation, or spelling that carries intentional poetic or stylistic meaning.

---

## **14 Content**

**Case Study 3: 20th-Century Vernacular Writing (Maud Lewis)**

Our third project centers on personal handwritten letters by celebrated Nova Scotia folk artist **Maud Lewis** (1903–1970). Lewis lived in rural Digby County with severe physical disabilities and limited formal education, painting vibrant folk scenes on cards and boards. Her personal correspondence provides invaluable historical and biographical documentation.

Her letters feature distinct vernacular and phonetic characteristics:

<ul>
  <li><strong>Phonetic Spellings:</strong> Doubling consonants or substituting letters based on sound, such as <em>allways</em> for <em>always</em>, <em>untill</em> for <em>until</em>, or <em>truely</em> for <em>truly</em>.</li>
  <li><strong>Unpunctuated Contractions:</strong> Omitting the apostrophe in common contractions, writing <em>dont</em>, <em>cant</em>, <em>wont</em>, and <em>didnt</em>.</li>
  <li><strong>Colloquial Syntax:</strong> Informal vernacular grammar reflecting Maritime oral speech patterns.</li>
</ul>

In Lewis's letters, an encoder faces words like *dont*:

```xml
<choice>
  <orig>dont</orig>
  <reg resp="#editor">don't</reg>
</choice>
```

Here, the editor supplies the missing apostrophe in `<reg>` so that natural language search engines identify the negative contraction, while `<orig>` preserves the unpunctuated form reflecting her rapid, informal hand.

**Vocabulary.** *Vernacular writing* — Informal, non-standardized written text produced outside formal academic, legal, or commercial institutions. *Phonetic spelling* — Spelling words according to their spoken pronunciation rather than dictionary conventions.

**Takeaway:** Personal letters by vernacular writers like Maud Lewis feature phonetic spellings and omitted apostrophes that can be regularized for readability while preserving their authenticity.

---

## **15 Content**

**Respecting the Vernacular Voice**

When editing vernacular texts, an editor must guard against the subtle hazard of **class and educational bias**. Throughout the history of scholarship, elite academic editors have often treated non-standard spelling in working-class, rural, or marginalized writers as "illiteracy" or "ignorance" requiring aggressive correction.

In digital textual scholarship, we reject this paternalistic framing. Non-standard spellings in personal correspondence are not badges of failure; they are linguistic records of regional speech, vernacular literacy, and personal identity. When Maud Lewis spells a word phonetically, she documents the phonetic reality of early-to-mid 20th-century rural Nova Scotian English.

When regularizing vernacular correspondence:

<ol>
  <li><strong>Never use `<sic>`/`<corr>` for vernacular spellings:</strong> Writing <em>allways</em> is an authentic phonetic variant, not a broken typographical blunder. Tag it with `<orig>` and `<reg>`, never `<sic>`.</li>
  <li><strong>Do not regularize colloquial grammar:</strong> If a writer uses a non-standard verb agreement (such as <em>we was</em>), do not "fix" the grammar to <em>we were</em>. That alters syntax and voice. Regularization governs spelling, not grammatical dialect.</li>
  <li><strong>State your rationale clearly:</strong> Explain in your project introduction that regularizations are provided solely for computational search and screen-reader accessibility, not to "clean up" the author's writing.</li>
</ol>

**Vocabulary.** *Linguistic paternalism* — The condescending editorial impulse to rewrite or correct non-standard vernacular voices to conform to prestige educational dialects. *Dialect preservation* — The editorial policy of maintaining authentic regional grammatical and phonetic features.

**Takeaway:** Treat vernacular writing with scholarly respect: use `<orig>`/`<reg>` to aid digital search, but never use `<sic>` or alter an author's authentic regional grammar.

---

## **16 Content**

**Case Study 4: 18th-Century Revolutionary French (1791 Decree)**

Our fourth cohort project investigates an official **French Revolutionary decree of 1791** from the National Assembly (*Comité des décrets*, Archives nationales, Paris). This document introduces students to historical variation in non-English European traditions.

Eighteenth-century French documents exhibit several systematic orthographic shifts that distinguish them from modern French:

<ul>
  <li><strong>The <em>oi</em> to <em>ai</em> Sound Shift:</strong> In the 18th century, the imperfect verb endings and nationality adjectives were still printed with the historical spelling <em>oi</em>, reflecting older medieval pronunciation, even though spoken French had shifted to /ɛ/. Thus, the 1791 decree writes <em>étoit</em> for modern <em>était</em>, <em>dérogeoit</em> for <em>dérogeait</em>, and <em>françois</em> for <em>français</em>. This spelling reform was proposed by Voltaire and officially codified by the Académie française in 1835.</li>
  <li><strong>Omission of Accents on Capital Letters:</strong> Eighteenth-century French printers routinely omitted acute, grave, and circumflex accents on capital letters due to physical font limitations (e.g., writing <em>DECRET</em> instead of <em>DÉCRET</em>).</li>
  <li><strong>Legal Formula Shorthand:</strong> Standard Latin and French legal abbreviations, such as <em>L.S.</em> (*Locus Sigilli* — place of the seal) and <em>art.</em> for <em>article</em>.</li>
</ul>

Encoding the Voltairean *oi*/*ai* shift in TEI is a classic application of regularization:

```xml
<choice>
  <orig>étoit</orig>
  <reg resp="#editor">était</reg>
</choice>
```

This ensures that modern French corpus tools immediately recognize the third-person singular imperfect verb form without losing the 1791 prerevolutionary orthography.

**Vocabulary.** *Voltairean orthography* — The historical French spelling using *oi* for sounds that later shifted to *ai* in the 1835 Académie reform. *Accented capitals* — The modern French typographical rule of placing accents on capital letters, widely omitted in 18th-century typography.

**Takeaway:** Eighteenth-century French documents systematically write *oi* where modern French writes *ai*, an orthographic shift that is cleanly normalized using `<orig>` and `<reg>`.

---

## **17 Content**

**Historical Precedents: Phonological Drift and Sound Mergers**

The spelling variations we see in 18th-century English, colonial treaties, Dickinson's poems, and Revolutionary French are not random occurrences. They are local manifestations of a universal linguistic law: **spoken language changes continuously, but written orthography tends to remain frozen** (Clemens & Graham, 2007).

A famous historical precedent taught in classical manuscript studies is **iotacism** (or itacism) in ancient and Byzantine Greek. Over several centuries, six distinct Greek vowels and diphthongs (*ι*, *η*, *υ*, *ει*, *οι*, *υι*) progressively merged in pronunciation until all six sounded identical to the vowel /i/ (like the *ee* in *beet*). Because scribes wrote what they heard, they began substituting these letters interchangeably. A scribe writing *τιμή* (honor) might write *τιμι*, or write *ἡμεῖς* (we) for *ὑμεῖς* (you), completely reversing the meaning of a sentence!

Similarly, in English, the **Great Vowel Shift** between 1400 and 1700 radically altered the pronunciation of long vowels, while printing presses froze late Middle English spelling into rigid type. That historical rupture is the reason English spelling today is notoriously irregular: words like *knight*, *meat*, and *meet* preserve historical sounds that vanished centuries ago.

Understanding that orthographic variation is driven by systematic sound changes gives you confidence as an editor. When you see a strange spelling on a manuscript page, you are looking at the living footprint of phonetic history.

**Vocabulary.** *Phonological drift* — The gradual, systematic change in the sound system of a language over time. *Sound merger* — A historical phonological process where two previously distinct sounds become identical in pronunciation.

**Takeaway:** Orthographic variation is the natural historical result of spoken pronunciation changing faster than conservative written spelling.

---

## **18 Content**

**Punctuation and Spacing Variations**

Orthographic variation extends beyond letters to punctuation marks, hyphens, and whitespace. Historical handwriting and early printing treat word division and line-end spacing very differently from modern word processors.

In 18th-century documents and vernacular letters, you will encounter:

<ol>
  <li><strong>Joined Words (Scriptio Continua remnants):</strong> Writers frequently join prepositions to their nouns or verbs (e.g., <em>inasmuch</em> written as <em>in as much</em>, or <em>today</em> written as <em>to day</em>).</li>
  <li><strong>Split Compound Words:</strong> Compound words that we write as a single unit are often hyphenated or divided by spaces (e.g., <em>every thing</em> for <em>everything</em>, <em>to morrow</em> for <em>tomorrow</em>).</li>
  <li><strong>Inconsistent Punctuation:</strong> The presence of virgules (slanted slash marks `/`) serving as general pause markers, colon marks used for abbreviations, or completely absent sentence punctuation.</li>
</ol>

When regularizing spacing, `<choice>` can wrap multi-token groups:

```xml
<choice>
  <orig>to morrow</orig>
  <reg resp="#editor">tomorrow</reg>
</choice>
```

However, editors must exercise caution with punctuation. Changing a historical author's punctuation can subtly alter the syntax and rhythm of a sentence. Unless missing punctuation makes a sentence completely unintelligible, preserve historical punctuation in your primary transcription and document any editorial additions explicitly.

**Vocabulary.** *Virgule* — A forward slash mark (`/`) used in medieval and early modern writing as a comma or caesura pause. *Word division* — The historical practice of spacing or joining words differently from modern dictionary standards.

**Takeaway:** Spacing variations and compound word divisions can be regularized within `<choice>`, but historical punctuation should be modified with great restraint.

---

## **19 Content**

**Nesting and Combining TEI Elements**

In complex historical documents, orthographic variation and abbreviations frequently collide in the very same word. What should an editor do when a historical clerk uses an abbreviation for a word that is *also* spelled archaically?

Consider an early legal document where the word *public* is abbreviated as *publ.*, but the full 18th-century spelling of the word was *publick*. Does the editor expand the abbreviation to modern *public* or historical *publick*? 

The TEI allows you to **nest** elements within `<choice>` or combine them to reflect multi-layered reality. There are two standard approaches:

```xml
<!-- Approach 1: Expand to the historical spelling first, then regularize -->
<choice>
  <orig>
    <choice>
      <abbr>publ.</abbr>
      <expan resp="#editor">publick</expan>
    </choice>
  </orig>
  <reg resp="#editor">public</reg>
</choice>
```

While nesting is syntactically valid in TEI XML, it can rapidly become verbose and difficult for humans to read. For most undergraduate editions, the TEI Guidelines recommend **combining both actions into a single direct pair**: expand the abbreviation directly into the modern standardized form in `<expan>`, and note your policy in the header:

```xml
<choice>
  <abbr>publ.</abbr>
  <expan resp="#editor">public</expan>
</choice>
```

Keeping markup clear and manageable is an essential skill in practical digital humanities. Choose the simplest valid structure that honestly represents the evidence.

**Vocabulary.** *Nested markup* — Placing one TEI `<choice>` element inside another to capture multiple layers of textual variation simultaneously. *Tag bloat* — Overly complex or nested XML that impairs human readability without adding proportionate scholarly value.

**Takeaway:** While TEI permits nesting `<abbr>` inside `<orig>`, practical editing favors the simplest clean markup that captures the necessary scholarly distinction.

---

## **20 Content**

**Milestones Inside Normalization Blocks**

A critical technical hazard occurs when a word that needs normalization happens to cross a **line break** or a **page break**.

In Week 4, you learned that physical line breaks must be recorded using the empty milestone tag `<lb/>`. Suppose that in the 1752 Treaty, the word *Governor* is written across the end of a line as *Gov-* on line 12 and *ernor* on line 13. Furthermore, suppose the word was written with an archaic spelling or abbreviation.

Where does the `<lb/>` element go? Should it go *inside* the `<choice>` block, or *outside* it?

```xml
<!-- CORRECT: The milestone sits inside the original reading -->
<choice>
  <orig>Gov-<lb n="13"/>ernor</orig>
  <reg resp="#editor">Governor</reg>
</choice>
```

In TEI encoding, physical milestone tags belong to the **diplomatic reality** of the document. The line break actually happened on the physical page between *Gov-* and *ernor*. The regularized form *Governor*, by contrast, is an abstract intellectual concept created by the modern editor—it does not have a physical line break. Therefore, the `<lb/>` tag resides inside the `<orig>` element.

If you placed the `<lb/>` outside `<choice>`, you would break the word in two separate XML chunks, making it impossible to search for the continuous word *Governor*. Keeping the milestone inside `<orig>` preserves both physical fidelity and lexical searchability.

**Vocabulary.** *Milestone tag* — An empty XML element (like `<lb/>` or `<pb/>`) that marks a physical boundary without enclosing text. *Hyphenated line-break* — A word divided across two typographic lines, requiring careful coordination with normalization markup.

**Takeaway:** Physical milestone tags like `<lb/>` belong inside the `<orig>` element because line breaks exist in the physical witness, not in the abstract regularized lemma.

---

## **21 Content**

**Formulating an Editorial Policy**

Before you type a single `<reg>` or `<expan>` tag into your document, you must pause and complete an essential intellectual task: **writing your Editorial Regularization Policy**.

A digital edition without an explicit policy is merely a collection of arbitrary personal whims. If you normalize *publick* to *public* on line 3, but leave *traffick* untouched on line 14 because you were tired, you have degraded the integrity of your dataset. A future scholar using your XML to study spelling evolution will reach false conclusions because your data reflects erratic human inattention rather than a coherent standard.

An Editorial Policy is an explicit set of rules defining:

<ol>
  <li><strong>Target Domain:</strong> Exactly which categories of variation you will regularize (e.g., terminal *k*, long *s*, *oi*/*ai* verbs, common-noun capitalization).</li>
  <li><strong>Exclusions:</strong> Exactly what you will leave untouched (e.g., authorial poetic capitalization, rhyme words, dialectal syntax).</li>
  <li><strong>Authority Standard:</strong> The external reference dictionary or standard you use as your target authority (e.g., modern *Merriam-Webster*, *Oxford English Dictionary*, or *Dictionnaire de l'Académie française*).</li>
</ol>

Your policy acts as your editorial contract. It governs every manual tag you apply today, every regular expression rule you write on Wednesday, and every prompt you feed to an AI model on Friday.

**Vocabulary.** *Editorial policy* — A formal, documented set of principles governing all editorial interventions and standardizations in an edition. *Target authority* — The standard reference dictionary or lexicon chosen as the normative baseline for regularization.

**Takeaway:** An explicit, written editorial policy is mandatory to ensure that all normalizations are consistent, defensible, and reproducible.

---

## **22 Content**

**The Principle of Consistency**

In textual scholarship, **consistency is more important than your specific choice of standard**. Whether an editor chooses to be conservative (normalizing very little) or liberal (modernizing thoroughly) is a defensible scholarly choice. What is completely indefensible is being inconsistent.

Consider the consequences of inconsistency in a digital corpus. If a corpus linguist runs a script across your edition to count occurrences of the lemma *treaty*, and half of your instances are tagged `<reg>treaty</reg>` while the other half are left untagged as diplomatic *Treaty*, the resulting statistical frequency will be wrong by 50%. Your inconsistency directly corrupts downstream quantitative research.

To maintain consistency:

<ul>
  <li><strong>Apply rules globally:</strong> If your policy dictates that 18th-century terminal *k* on adjectives is regularized, every single instance must receive the identical `<choice>` markup.</li>
  <li><strong>Treat identical abbreviations identically:</strong> If *y<hi rend="superscript">e</hi>* is expanded to *the* on line 2, it must be expanded to *the* on line 20, unless clear contextual evidence indicates a different meaning.</li>
  <li><strong>Log every exception:</strong> If you intentionally deviate from your standard rule in a specific line—for example, preserving a variant because it forms a poetic rhyme—you must document that specific exception in your project notes.</li>
</ul>

**Vocabulary.** *Internal consistency* — The rigorous application of the same editorial rules across every line and folio of an edition. *Corpus corruption* — The skewing of downstream statistical or lexical analyses caused by erratic or unstated editorial practices.

**Takeaway:** Consistency is the cardinal rule of digital editing: an editor must apply their stated regularization policy systematically to every occurrence in the text.

---

## **23 Content**

**Building the Editorial Rule Ledger**

To ensure absolute consistency, professional digital editors do not normalize text on the fly. Instead, they construct an **Editorial Rule Ledger**.

A Rule Ledger is a structured table that catalogues every rule in your policy before you begin encoding. It serves as your working blueprint during manual editing, your specifications sheet when writing regular expressions on Wednesday, and your grading rubric when auditing AI outputs on Friday.

For Workshop 6, your Rule Ledger will be recorded in a markdown file named `NORMALIZATION.md` in your repository. It contains five core columns:

<table style="width: 100%; border-collapse: collapse; margin-top: 1rem; margin-bottom: 1rem;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1; text-align: left;">
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Rule ID</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Pattern / Category</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Diplomatic Example</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Regularized Form</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Scholarly Rationale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>R-01</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Terminal <em>-ck</em> in adjectives</td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><em>publick</em></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><em>public</em></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Standard modern English lexicography; aligns with OED.</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>R-02</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Thorn contraction</td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><em>y<sup>e</sup></em></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><em>the</em></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Expand historical thorn substitution to modern definite article.</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>R-03</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Substantive noun capital</td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><em>Treaty</em></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><em>treaty</em></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Standardize 18th-century capital to lowercase for sentence parsing.</td>
    </tr>
  </tbody>
</table>

By maintaining this ledger, you transform subjective feelings into an auditable scientific protocol.

**Vocabulary.** *Rule Ledger* — A structured catalogue defining every active regularization rule, its input pattern, target replacement, and scholarly rationale. *Rule ID* — A unique alphanumeric identifier (e.g., `R-01`) assigned to an editorial rule for tracking and auditing.

**Takeaway:** Maintain an explicit Editorial Rule Ledger with unique rule IDs and clear rationales to track every transformation applied to your text.

---

## **24 Content**

**Categorizing Regularization Rules**

To keep your Rule Ledger organized and effective, divide your rules into four distinct **linguistic and typographical categories**:

<ol>
  <li><strong>Orthographic / Phonological Rules:</strong> Variations in spelling reflecting historical sound changes, dialect, or pre-reform orthography (e.g., <em>publick</em> &rarr; <em>public</em>, French <em>étoit</em> &rarr; <em>était</em>, Lewis's <em>allways</em> &rarr; <em>always</em>). These are encoded with `<orig>` and `<reg>`.</li>
  <li><strong>Abbreviation / Expansion Rules:</strong> Graphic compressions, suspensions, contractions, and brevigraphs (e.g., <em>y<sup>e</sup></em> &rarr; <em>the</em>, <em>Gov<sup>r</sup></em> &rarr; <em>Governor</em>, <em>&amp;</em> &rarr; <em>and</em>). These are encoded with `<abbr>` and `<expan>`.</li>
  <li><strong>Typographical / Graphemic Rules:</strong> Letterform substitutions that do not change spelling or meaning, such as replacing the long <em>s</em> (<em>ſ</em>) with short <em>s</em>. Many editors handle this as a global display transformation, or encode it as `<orig>ſ</orig><reg>s</reg>`.</li>
  <li><strong>Syntactic / Casing Rules:</strong> Regularizing substantive common-noun capitalization or joining split compound words (e.g., <em>to morrow</em> &rarr; <em>tomorrow</em>).</li>
</ol>

Categorizing your rules prevents category confusion. It ensures that when you write regular expressions on Wednesday, you know exactly which XML tags (`<reg>` vs. `<expan>`) your replacement patterns should generate.

**Vocabulary.** *Rule categorization* — Grouping editorial transformations by their linguistic mechanism (spelling, abbreviation, typography, or casing). *Graphemic variation* — Different physical shapes representing the same underlying letter (such as long *s* versus round *s*).

**Takeaway:** Categorize your rules into orthographic, abbreviation, typographical, and casing groups to ensure appropriate TEI tagging.

---

## **25 Content**

**Documenting the Policy in the TEI Header**

In a professional digital scholarly edition, your editorial policy is not just kept in an informal notebook; it is permanently encoded directly inside the document's **TEI Header** (TEI Consortium, 2024).

The TEI Header provides a dedicated structural element inside `<encodingDesc>` called `<editorialDecl>` (editorial declaration). Within `<editorialDecl>`, you place the `<normalization>` element to explain your policy in formal prose:

```xml
<teiHeader>
  <!-- ... fileDesc ... -->
  <encodingDesc>
    <editorialDecl>
      <normalization method="markup">
        <p>This edition regularizes historical 18th-century orthography and expands 
           abbreviations using parallel <gi>choice</gi> markup. Original spellings are 
           preserved in <gi>orig</gi> and regularized modern American English forms are 
           supplied in <gi>reg</gi> following Merriam-Webster's Collegiate Dictionary 
           (11th ed.). Abbreviations are expanded in <gi>expan</gi>. Common-noun 
           capitalization has been regularized to lowercase.</p>
      </normalization>
    </editorialDecl>
  </encodingDesc>
</teiHeader>
```

Notice the attribute `method="markup"`. This attribute explicitly informs any digital repository or harvesting bot that the normalization has been accomplished using parallel TEI tags (`<choice>`), rather than by silently overwriting the text (`method="silent"`). 

Documenting your policy in the header guarantees that your edition remains self-describing, transparent, and compliant with FAIR data principles decades after publication.

**Vocabulary.** *`<editorialDecl>`* — TEI Header element detailing the editorial practices, declarations, and policies applied to the text. *`<normalization>`* — TEI Header element specifying the degree and method of orthographic normalization applied. *`method="markup"`* — An attribute declaring that normalization is encoded non-destructively using TEI tags.

**Takeaway:** Record your editorial policy inside the `<editorialDecl>` and `<normalization>` elements of your TEI Header, declaring `method="markup"` for non-destructive transparency.

---

## **26 Content**

**Manual Normalization in VS Code**

Now that your policy is established and your Rule Ledger is built, you are ready to begin the manual work in Visual Studio Code.

Today's exercise focuses on a **20-line excerpt** selected from your consensus reconciled text in `transcription_reconciled.xml`. Working by hand is slow and deliberate, and that friction is precisely where learning happens. Hand-encoding forces you to examine every word with an editor's eye, noticing ambiguities that automated tools gloss over.

Follow this systematic manual workflow:

<ol>
  <li><strong>Open your reconciled transcription:</strong> In VS Code, open your `transcription_reconciled.xml` file. Ensure that the Red Hat XML and Scholarly XML extensions are active, displaying valid green checkmarks in the status bar.</li>
  <li><strong>Identify candidate words:</strong> Read your 20-line passage word by word against your Editorial Rule Ledger. When you encounter a candidate word—such as an archaic spelling like <em>publick</em> or an abbreviation like <em>w<sup>ch</sup></em>—confirm which rule ID applies.</li>
  <li><strong>Insert the `<choice>` block:</strong> Wrap the target word carefully. Cut the original word into `<orig>` or `<abbr>`, and type your regularized or expanded word into `<reg resp="#editor">` or `<expan resp="#editor">`.</li>
  <li><strong>Verify tag placement:</strong> Ensure that surrounding whitespace is outside the `<choice>` tags, and confirm that any existing milestone tags like `<lb/>` are not accidentally deleted or misplaced.</li>
</ol>

**Vocabulary.** *Hand-encoding* — The deliberate, manual insertion of XML tags around text, developing close-reading paleographical discipline. *Whitespace discipline* — Ensuring that spaces between words remain outside tagging structures to prevent collapsed words in downstream rendering.

**Takeaway:** Manual normalization in VS Code builds editorial discipline by requiring you to evaluate every word against your explicit policy ledger.

---

## **27 Content**

**Keyboard Shortcuts and Snippets for `<choice>`**

Typing `<choice><orig></orig><reg resp="#editor"></reg></choice>` by hand twenty times is tedious and prone to typing errors. Fortunately, VS Code provides powerful editing features that accelerate manual encoding without sacrificing human judgment.

You can dramatically speed up manual normalization using two techniques:

<ol>
  <li><strong>Wrap with Abbreviation / Emmet:</strong> Highlight the target word in your editor, open the Command Palette (<code>Cmd+Shift+P</code> on macOS or <code>Ctrl+Shift+P</code> on Windows), type <em>Emmet: Wrap with Abbreviation</em>, and type <code>choice>orig</code>. This instantly wraps your highlighted word inside <code>&lt;choice&gt;&lt;orig&gt;target&lt;/orig&gt;&lt;/choice&gt;</code>. Then simply place your cursor after <code>&lt;/orig&gt;</code> and type your <code>&lt;reg&gt;</code> tag.</li>
  <li><strong>Custom User Snippets:</strong> You can create a custom XML snippet in VS Code. Go to <em>Code &rarr; Settings &rarr; User Snippets</em>, select <code>xml.json</code>, and add a snippet named "TEI Choice Regularization":
  <pre><code>"TEI Choice Regularization": {
  "prefix": "treg",
  "body": [
    "&lt;choice&gt;",
    "  &lt;orig&gt;$TM_SELECTED_TEXT$1&lt;/orig&gt;",
    "  &lt;reg resp=\"#editor\"&gt;$2&lt;/reg&gt;",
    "&lt;/choice&gt;"
  ],
  "description": "Wrap selected text in TEI choice with orig and reg"
}</code></pre>
  With this snippet saved, you simply highlight any word, type your snippet prefix, and press <code>Tab</code>: the editor wraps your word in `<orig>` and jumps your cursor directly into `<reg>` ready to type the modern spelling!</li>
</ol>

**Vocabulary.** *User snippet* — A custom keyboard shortcut in an editor that expands a short prefix into a pre-formatted template of code or markup. *`$TM_SELECTED_TEXT`* — A snippet variable that captures whichever characters were highlighted in the editor when the shortcut was triggered.

**Takeaway:** Configure custom VS Code XML snippets to automate the repetitive typing of `<choice>` structures while keeping every editorial decision under manual human control.

---

## **28 Content**

**Validating Normalized TEI against the Schema**

Every time you edit XML, you must validate your file against the schema before moving forward. A single unclosed tag or mismatched element name breaks the entire document hierarchy.

In VS Code, the Scholarly XML and Red Hat XML extensions continuously validate your document against your project's RELAX NG schema (`msdesc.rng` or `tei_all.rng`). As you insert `<choice>` blocks, watch for real-time validation feedback:

<ul>
  <li><strong>Valid Child Combinations:</strong> The TEI schema strictly governs what elements may appear inside `<choice>`. Valid pairings include:
    <ul>
      <li>`<orig>` and `<reg>` (orthographic variation)</li>
      <li>`<abbr>` and `<expan>` (abbreviations)</li>
      <li>`<sic>` and `<corr>` (corrections)</li>
      <li>`<unclear>` paired with supplied readings</li>
    </ul>
    You cannot arbitrarily invent child elements or leave `<choice>` empty.</li>
  <li><strong>Red Squiggly Underlines:</strong> If you see a red squiggly line under `<choice>`, hover your cursor over it. The schema validator will tell you if you forgot a closing tag, misnamed an element (such as typing `<regular>` instead of `<reg>`), or placed elements in an invalid order.</li>
  <li><strong>Zero Errors in the Problems Panel:</strong> Open the Problems panel (<code>Cmd+Shift+M</code> or <code>Ctrl+Shift+M</code>). Before saving your work, verify that your document reports exactly <strong>0 errors</strong>.</li>
</ul>

**Vocabulary.** *Schema validation* — The automated process of verifying that an XML document conforms strictly to the structural and content rules of a formal schema. *Problems panel* — The VS Code interface listing all active syntax and validation errors across your open workspace.

**Takeaway:** Constantly monitor the VS Code Problems panel to ensure that every newly inserted `<choice>` block validates with zero schema errors.

---

## **29 Content**

**Preparing Your Manual Ground Truth for Wednesday**

Today's manual work is not just an isolated classroom exercise. The 20-line passage you hand-encode today serves a crucial methodological purpose: **it is your Ground Truth reference baseline for the rest of Week 6**.

Tomorrow, you will not be editing text by hand. Instead, you will build deterministic regular expression rules in VS Code to automate these same normalizations. On Friday, you will instruct an AI model to normalize the text using natural language prompts.

How will you know whether your regular expressions worked correctly? How will you know whether the AI hallucinated an expansion or over-normalized an archaic word?

You will know by **diffing** their outputs against today's manual ground truth. Because you spent today examining each word, consulting your policy ledger, and hand-encoding each `<choice>` block with verified scholarly judgment, today's file (`transcription_reconciled_manual.xml`) represents the gold standard of accuracy.

When you measure Wednesday's and Friday's automated passes, every point where they match your manual file will count as a confirmed true positive. Every point where an automated tool changes a word that your manual ground truth left alone will expose a potential false positive or hypercorrection.

**Vocabulary.** *Ground truth baseline* — An independently verified, hand-curated dataset used as the objective standard for testing and measuring the accuracy of automated models. *Gold standard* — The authoritative benchmark in a comparative experiment against which all other results are evaluated.

**Takeaway:** Your hand-encoded manual passage serves as the indispensable ground truth baseline against which Wednesday's regular expressions and Friday's AI outputs will be rigorously evaluated.

---

## **30 Content**

**Review and Workshop 6 Step 1 Checklist**

Today you laid the intellectual and structural foundations for the entire normalization module. You moved from the raw physical witness to a dual-layered digital edition that reconciles historical preservation with modern digital accessibility.

Before concluding today's work, review the **Workshop 6 Step 1 Checklist** to confirm that your repository is fully prepared:

<ol>
  <li><strong>20-Line Consensus Excerpt:</strong> Have you selected a clear 20-line passage from your consensus text in `transcription_reconciled.xml` and saved it as the foundation for your normalization workshop?</li>
  <li><strong>Editorial Policy Formulated:</strong> Have you written a clear paragraph defining your normalization scope, exclusions, and target authority dictionary?</li>
  <li><strong>Rule Ledger Catalogued:</strong> Have you created `NORMALIZATION.md` with an Editorial Rule Ledger containing at least 3 to 5 distinct rules with unique Rule IDs (`R-01`, `R-02`, etc.)?</li>
  <li><strong>Manual Markup Applied:</strong> Have you hand-encoded all target words in your excerpt using proper TEI `<choice>` markup with `<orig>`/`<reg resp="#editor">` and `<abbr>`/`<expan resp="#editor">`?</li>
  <li><strong>Fidelity Maintained:</strong> Have you verified that physical milestones (`<lb/>`) remain inside `<orig>` and that authorial poetic or dialectal choices have not been improperly erased?</li>
  <li><strong>Schema Validated:</strong> Does your XML file validate with <strong>0 errors</strong> in VS Code?</li>
</ol>

With Step 1 complete, you are ready for Wednesday, where you will translate these manual decisions into deterministic regular expressions.

**Vocabulary.** *Step 1 milestone* — The completion of the manual baseline transcription and policy ledger, locking the ground truth for comparative evaluation.

**Takeaway:** Completing Step 1 establishes a validated manual ground truth and an explicit rule ledger, preparing you to automate and audit normalization throughout the rest of the week.

---

## References

Burnard, L. (2014). *What is the Text Encoding Initiative? How to add intelligent markup to digital resources*. OpenEdition Press. https://doi.org/10.4000/books.oep.426

Clemens, R., & Graham, T. (2007). *Introduction to manuscript studies*. Cornell University Press.

Driscoll, M. J. (2006). Levels of transcription. In L. Burnard, K. O'Brien O'Keeffe, & J. Unsworth (Eds.), *Electronic textual editing* (pp. 254–261). Modern Language Association of America.

Pierazzo, E. (2015). *Digital scholarly editing: Theories, models and methods*. Ashgate Publishing.

TEI Consortium. (2024). *TEI P5: Guidelines for electronic text encoding and interchange* (version 4.8.0). TEI Consortium. https://tei-c.org/guidelines/p5/
