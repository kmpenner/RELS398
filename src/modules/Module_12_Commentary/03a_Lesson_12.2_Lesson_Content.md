# Lesson 12.2 — Deterministic Intertextual Discovery and Linked Web Annotation

*RELS 398 / ENGL 398 · Topic 12: Commentary · Meeting #32 (Wed Nov 25)*

***Step 2 of the three-step cycle: rule-based.** Today we explore automated, rule-based methods for discovering text reuse and connecting annotations to the web. We examine how algorithms find shared phrases across legal treaties, revolutionary decrees. Letters. Then, we study the W3C Web Annotation Data Model to see how notes are shared across the open web. We audit these automated tools against Tuesday's hand-crafted ground truth.*

---

## **01 Content**

**The Algorithmic Search for Text Reuse**

Yesterday you wrote commentary notes by hand. You researched historical dictionaries and tracked down legal citations. That manual work is rewarding. However, it is slow. A scholar can only read one sentence at a time. No human editor can memorize thousands of archival pages to spot every hidden cross-reference.

rule-based algorithms solve this scale problem. A rule-based tool runs fixed mathematical and word rules. When given the same input, it always produces the same output. It does not guess or hallucinate like an artificial intelligence model.

In text analysis, rule-based algorithms look for text reuse. They scan large collections of documents to find repeated phrases, shared legal formulas, and literary echoes.

Consider our three course documents:
<ul>
  <li><strong>Andromeda (1752 Treaty):</strong> Did the British authorities copy specific clauses from the earlier 1725 Dummer's Treaty? An algorithm can compare both texts in seconds.</li>
  <li><strong>Ace (1791 French Decree):</strong> Does the decree reuse standard formulas from the 1789 Declaration of the Rights of Man? An algorithm highlights every matching phrase.</li>
  <li><strong>Olyvia (1967 Maud Lewis Letter):</strong> Did Maud Lewis use standard phrases when selling her art to collectors? A comparison across her surviving letters reveals her recurring formulas.</li>
</ul>

**Vocabulary.** *rule-based Algorithm* — a digital process with predictable, rule-based behavior that always yields identical results for a given input. *Text Reuse* — the repetition of identical or modified text across different documents.

**Takeaway:** rule-based text reuse algorithms scan vast document collections using fixed rules to discover shared phrases and citations beyond human memory.

---

## **02 Content**

**The Mechanics of Text Reuse: word vs. sentence**

When writers borrow from earlier texts, they reuse language in different ways. Some writers copy word-for-word. Others modify phrases to fit new contexts.

Text reuse falls into two main forms:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9. Border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px. Text-align: left;">Reuse Type</th>
      <th style="padding: 8px. Text-align: left;">Definition</th>
      <th style="padding: 8px. Text-align: left;">Detection Difficulty</th>
      <th style="padding: 8px. Text-align: left;">Cohort Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Verbatim Reuse</strong></td>
      <td style="padding: 8px;">Exact, word-for-word repetition of a phrase</td>
      <td style="padding: 8px;">Easy (simple string matching in VS Code)</td>
      <td style="padding: 8px;"><em>"saving to the said Tribe the free liberty of Hunting"</em> in 1725 and 1752 treaties.</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Modified Reuse</strong></td>
      <td style="padding: 8px;">Shared vocabulary with altered word order or grammar</td>
      <td style="padding: 8px;">Moderate (requires lemmatization and proximity rules)</td>
      <td style="padding: 8px;">French decree modifying a 1790 finance law: changing past tense verbs to modern legal mandates.</td>
    </tr>
  </tbody>
</table>

Simple string search in VS Code (`Cmd+F`) finds verbatim loans easily. But when authors change a word or reorder a clause, simple search fails. Advanced tools use statistical proximity and n-grams to detect these subtle connections.

**Vocabulary.** *Verbatim Reuse* — copying text character-for-character without modification. *Modified Reuse* — adapting an earlier text through summary, grammatical changes, or word omissions.

**Takeaway:** Text reuse ranges from verbatim copying to modified summary, requiring different algorithmic detection strategies.

---

## **03 Content**

**The Tesserae Framework: Principles of text-linking Discovery**

One of the most famous digital humanities tools for finding text reuse is the *Tesserae Project*, developed at the University at Buffalo. Originally designed for classical Latin and Greek poetry, its core principles apply to historical documents in any language.

Tesserae operates on a simple principle: **pairing of shared meaningful words**.
<ol>
  <li>The algorithm breaks texts into small segments (usually sentences or poetic lines).</li>
  <li>It ignores common filler words like "the", "and", and "in".</li>
  <li>It searches for pairs of sentences that share two or more rare vocabulary words.</li>
  <li>It scores each match based on how close the words appear to each other and how rare those words are in the wider language.</li>
</ol>

If two sentences share two common words like "king" and "day", the score is low. But if two sentences share rare terms like "assignats" and "counterfeiting", the algorithm flags a strong text-linking link.

**Vocabulary.** *Tesserae* — an open-source digital tool that finds text-linking parallels using word pairing scoring. *pairing* — the appearance of two or more specific words within the same sentence or window of text.

**Takeaway:** The Tesserae framework discovers text reuse by scoring the pairing of shared words based on rarity and physical proximity.

---

## **04 Content**

**Preprocessing: Stoplists and Normalization**

Before an algorithm can compare historical texts, you must prepare the data. If you feed raw transcriptions into an algorithm, punctuation marks, capital letters, and common words distort the results.

Text preprocessing involves three essential steps:
<ol>
  <li><strong>Punctuation Removal:</strong> Periods, commas, and hyphens are stripped so words match cleanly.</li>
  <li><strong>Case Folding:</strong> Converting all letters to lowercase so that "Treaty" matches "treaty".</li>
  <li><strong>Applying a Stoplist:</strong> Filtering out the most common grammatical words in the language.</li>
</ol>

A *stoplist* is a list of high-frequency words that carry little distinct meaning. In English, a stoplist contains words such as *the, of, and, to, in, that, is, was*. In French, it contains *le, la, les, de, et, en, du, pour*.

If you omit the stoplist, almost every sentence matches every other sentence because they all contain "the" and "and". Removing stopwords allows the algorithm to focus exclusively on meaningful nouns, verbs, and adjectives.

**Vocabulary.** *Stoplist* — a curated list of high-frequency words excluded from digital search to prevent noise. *Case Folding* — normalizing all text to lowercase to ensure uniform matching.

**Takeaway:** Preprocessing historical text through case folding, punctuation removal, and stoplists is essential for finding meaningful text reuse.

---

## **05 Content**

**Word Rarity and TF-IDF Weighting**

How does an algorithm know which words are truly important? In human reading, your brain naturally focuses on specialized words. Computers achieve this using a statistical formula called **TF-IDF** (Term Frequency–Inverse Document Frequency).

TF-IDF evaluates words based on two balances:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9. Border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px. Text-align: left;">Component</th>
      <th style="padding: 8px. Text-align: left;">Formula Meaning</th>
      <th style="padding: 8px. Text-align: left;">Effect on Word Score</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Term Frequency (TF)</strong></td>
      <td style="padding: 8px;">How often a word appears in a specific sentence</td>
      <td style="padding: 8px;">Words appearing multiple times score higher within that passage.</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Inverse Document Frequency (IDF)</strong></td>
      <td style="padding: 8px;">How rare the word is across the whole corpus</td>
      <td style="padding: 8px;">Words that appear everywhere receive near-zero weight. Rare words receive high scores.</td>
    </tr>
  </tbody>
</table>

For example, in Andromeda's treaty, the word "governor" appears on almost every page, so its IDF score is low. But the word "Truckhouse" appears in only two articles. Its high IDF score signals to the algorithm that this sentence contains a unique legal provision.

**Vocabulary.** *TF-IDF* — a statistical weight measuring how important a word is to a specific document within a collection. *Inverse Document Frequency* — a calculation that boosts rare terms and discounts ubiquitous words.

**Takeaway:** TF-IDF weighting mathematically models scholarly intuition by prioritizing rare, distinctive terms over ubiquitous vocabulary.

---

## **06 Content**

**Distance Scoring: Word Proximity**

Vocabulary rarity alone is not enough to confirm text reuse. Two rare words might appear in the same document simply by accident. To confirm an intentional borrow or legal formula, algorithms measure physical word distance.

Consider two sentences:
<ul>
  <li><strong>Sentence A:</strong> <em>"The Chief agreed to establish a Truckhouse on the Shubenacadie River."</em> (The words "Truckhouse" and "Shubenacadie" are separated by only 3 words).</li>
  <li><strong>Sentence B:</strong> <em>"A Truckhouse was opened in January. At the same time, five months later troops surveyed the distant Shubenacadie."</em> (The words are separated by 14 words).</li>
</ul>

Sentence A shows high phrase density. The words appear tightly grouped, suggesting a formulaic legal clause. Sentence B shows low phrase density.

rule-based tools like Tesserae calculate a distance score: words that appear close together receive a bonus. At the same time, words spread across long paragraphs are penalized.

**Vocabulary.** *Phrase Density* — the closeness of matching words within a text span. *Proximity Penalty* — reducing a match score when shared words are separated by many intervening terms.

**Takeaway:** Measuring word proximity ensures that algorithms prioritize compact, formulaic phrases over accidental, distant word pairings.

---

## **07 Content**

**Precision vs. Recall in Algorithmic Discovery**

When configuring any automated search tool, editors face a fundamental trade-off: **Precision vs. Recall**.

These two concepts measure search quality:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9. Border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px. Text-align: left;">Metric</th>
      <th style="padding: 8px. Text-align: left;">Definition</th>
      <th style="padding: 8px. Text-align: left;">High Setting Outcome</th>
      <th style="padding: 8px. Text-align: left;">Risk of Extreme Setting</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Precision</strong></td>
      <td style="padding: 8px;">What percentage of discovered matches are genuine historical connections?</td>
      <td style="padding: 8px;">Almost every result is a true parallel.</td>
      <td style="padding: 8px;">You miss many subtle, modified echoes (False Negatives).</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Recall</strong></td>
      <td style="padding: 8px;">What percentage of all true historical connections did the tool find?</td>
      <td style="padding: 8px;">The tool captures nearly every parallel in the archive.</td>
      <td style="padding: 8px;">The editor must sort through hundreds of irrelevant false alarms (False Positives).</td>
    </tr>
  </tbody>
</table>

In digital editing, we usually aim for balanced settings: strict enough to filter out pure noise. However, broad enough to surface unexpected connections.

**Vocabulary.** *Precision* — the proportion of retrieved results that are relevant. *Recall* — the proportion of all relevant items that were successfully retrieved.

**Takeaway:** Editorial tool configuration balances precision against recall, trading off between missing subtle parallels and filtering out false alarms.

---

## **08 Content**

**What rule-based Algorithms Catch**

rule-based text reuse tools are remarkably powerful within their specific domain. They excel at finding patterns that human eyes overlook during long reading sessions.

rule-based algorithms reliably catch:
<ul>
  <li><strong>Verbatim legal Formulas:</strong> In Ace's French decrees, phrases like <em>"l'Assemblée Nationale a décrété et décrète"</em> appear across hundreds of parliamentary laws. An algorithm tags every occurrence instantly.</li>
  <li><strong>uniform Treaty Clauses:</strong> In Andromeda's 1752 treaty, formal promises of peace match earlier 1725 articles word-for-word across separate archival volumes.</li>
  <li><strong>Commercial Boilerplate:</strong> In Olyvia's Maud Lewis letters, recurring sales phrases (such as asking for payment by money order or listing price per painting) are surfaced across different correspondents.</li>
  <li><strong>Direct Quotations:</strong> Unattributed citations from earlier official notices or scripture are highlighted with mathematical certainty.</li>
</ul>

**Vocabulary.** *Boilerplate* — uniform, formulaic text reused in legal or administrative documents with little modification. *Verbatim Match* — an exact character-level match between two passages.

**Takeaway:** rule-based tools excel at surfacing verbatim legal formulas, commercial boilerplate, and direct legal cross-references.

---

## **09 Content**

**What rule-based Algorithms Miss**

While rule-based algorithms are fast and reliable, they have serious blind spots. Because they operate on literal vocabulary matching, they fail whenever meaning is conveyed through non-literal language.

rule-based algorithms fail to detect:
<ul>
  <li><strong>Synonym Substitution:</strong> If a later French decree replaces <em>"fabrication"</em> with <em>"création"</em>, a word-matching tool sees zero connection.</li>
  <li><strong>Conceptual Parallels:</strong> If an author alludes to an idea without using the author's exact words, the algorithm is completely blind to the connection.</li>
  <li><strong>Ironic Reversals:</strong> If a writer mocks an earlier political decree by negating its phrasing, string tools miss the rhetorical nuance.</li>
  <li><strong>Spelling Variations:</strong> In historical manuscripts, if Maud Lewis spells "February" as "Febuary", an un-normalized string search misses the match.</li>
</ul>

This is why automated tools cannot work alone. They require a human editor to review candidates, understand synonyms, and evaluate historical intent.

**Vocabulary.** *Synonymic Substitution* — replacing a word with an equivalent term having the same meaning. *False Negative* — a genuine historical parallel that an automated tool failed to discover.

**Takeaway:** rule-based tools are blind to synonyms, conceptual allusions, and spelling variations, requiring human oversight to catch missed connections.

---

## **10 Content**

**Auditing Algorithmic Output Against Tuesday's Ground Truth**

In the three-step cycle, Tuesday's manual notes serve as your **gold standard ground truth**. Today, you test whether an automated search algorithm can discover the same notes you wrote by hand.

When auditing algorithmic output:
<ol>
  <li><strong>Run the Search:</strong> Execute your automated search across your project corpus.</li>
  <li><strong>Compare Matches:</strong> Did the algorithm find the text-linking references you identified on Tuesday?
    <ul>
      <li>If yes, the algorithm validated your manual discovery and saved time.</li>
      <li>If it found references you missed, the algorithm expanded your research.</li>
      <li>If it missed references you found, analyze why (e.g., did synonym substitution hide the parallel?).</li>
    </ul>
  </li>
  <li><strong>Log False Alarms:</strong> Note how many coincidental word pairs the tool reported that have no historical relationship.</li>
</ol>

This comparative audit reveals the true capabilities and limits of automated tools.

**Vocabulary.** *Audit* — a systematic evaluation of digital output against an established, verified benchmark. *Gold Standard* — human-verified data used to evaluate automated accuracy.

**Takeaway:** Auditing algorithmic results against manual ground truth reveals tool strengths, uncovers missed parallels, and identifies false positives.

---

## **11 Content**

**Beyond the Local File: The Need for Web Annotation**

In Lesson 12.1, you stored notes inside the TEI `<standOff>` block of your local XML file. That local structure is ideal for publishing a self-contained edition. But what happens when you want to share annotations across the open internet?

Historical scholarship increasingly happens across distributed web platforms:
<ul>
  <li>A researcher at the Nova Scotia Archives wants to annotate a digitized scan of the 1752 Treaty on their website.</li>
  <li>A student at StFX wants to link their commentary note to that remote archive scan without asking the archivist for write access to their server.</li>
  <li>An art historian wants to attach an explanatory note directly to a Maud Lewis painting hosted on the Art Gallery of Nova Scotia website.</li>
</ul>

You cannot edit the XML files of remote museum servers. To allow anyone to annotate any web document without modifying the underlying server files, the World Wide Web Consortium (W3C) created the **Web Annotation Data Model**.

**Vocabulary.** *Distributed Annotation* — attaching comments to remote web resources without modifying the host server's source files. *W3C* — the World Wide Web Consortium, the international standards organization for the web.

**Takeaway:** Web annotation standards allow scholars to attach commentary to remote archival images and texts across the internet without altering host servers.

---

## **12 Content**

**The W3C Web Annotation Data Model**

Published as an official W3C Recommendation in 2017, the *Web Annotation Data Model* formalizes how digital notes are structured on the web.

The model is built on a clean three-part structure:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9. Border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px. Text-align: left;">Component</th>
      <th style="padding: 8px. Text-align: left;">Role in Model</th>
      <th style="padding: 8px. Text-align: left;">Plain English Meaning</th>
      <th style="padding: 8px. Text-align: left;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Annotation</strong></td>
      <td style="padding: 8px;">The overarching container</td>
      <td style="padding: 8px;">The note object itself, with metadata (author, date, motivation).</td>
      <td style="padding: 8px;">Created by Ace on Nov 25, 2026.</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Target</strong></td>
      <td style="padding: 8px;">What is being annotated</td>
      <td style="padding: 8px;">The destination web page, image region, or text sentence.</td>
      <td style="padding: 8px;">A specific line in the 1791 French decree scan.</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Body</strong></td>
      <td style="padding: 8px;">What the note says</td>
      <td style="padding: 8px;">The explanatory comment, transcription, or classification.</td>
      <td style="padding: 8px;">"Assignats were paper currency issued in 1789."</td>
    </tr>
  </tbody>
</table>

By standardizing notes into Annotation, Target, and Body, annotations become shareable across any software platform on the web.

**Vocabulary.** *Annotation Body* — the content or comment being attached to a target. *Annotation Target* — the specific resource, web page, or image region being annotated.

**Takeaway:** The W3C Web Annotation Data Model structures commentary into three universal components: the Annotation, the Target, and the Body.

---

## **13 Content**

**JSON-LD: The Language of Web Annotations**

While TEI uses XML, modern web architecture predominantly uses JSON (JavaScript Object Notation). To represent semantic linked data, web annotations use **JSON-LD** (JSON for Linked Data).

JSON-LD allows plain JSON objects to act as linked data by including a `@context` declaration:
```json
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "id": "http://example.org/annotations/anno1",
  "type": "Annotation",
  "motivation": "commenting",
  "body": {
    "type": "TextualBody",
    "value": "Peregrine Hopson served as Governor of Nova Scotia from 1752 to 1753.",
    "format": "text/plain"
  },
  "target": "https://archives.novascotia.ca/treaty1752#clause3"
}
```

Notice how intuitive this is:
<ul>
  <li><code>@context</code> tells web software that this file follows official W3C rules.</li>
  <li><code>motivation</code> states why the note was made (e.g., commenting).</li>
  <li><code>body</code> contains the student's historical note.</li>
  <li><code>target</code> points to the live URL of the treaty in the Nova Scotia Archives.</li>
</ul>

**Vocabulary.** *JSON-LD* — a lightweight data format that encodes Linked Open Data within standard JSON syntax. *`@context`* — a JSON-LD property linking property names to uniform web ontologies.

**Takeaway:** JSON-LD serializes W3C Web Annotations into a web-native, machine-readable format that connects commentary to live URLs.

---

## **14 Content**

**The W3C Motivation Taxonomy**

Why did an editor create a note? In human writing, you understand an author's goal from tone and context. Computers need explicit signals.

The W3C standard provides a controlled vocabulary of **motivations**:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9. Border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px. Text-align: left;">W3C Motivation</th>
      <th style="padding: 8px. Text-align: left;">Scholarly Purpose</th>
      <th style="padding: 8px. Text-align: left;">Cohort Use Case</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><code>commenting</code></td>
      <td style="padding: 8px;">Explaining meaning, history, or context</td>
      <td style="padding: 8px;">Explaining who Governor Hopson was.</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><code>identifying</code></td>
      <td style="padding: 8px;">Attaching an authority record to a person or place</td>
      <td style="padding: 8px;">Linking "Marshalltown" to its GeoNames entry.</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><code>linking</code></td>
      <td style="padding: 8px;">Connecting one text directly to another</td>
      <td style="padding: 8px;">Linking the 1752 treaty to the 1725 treaty text.</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><code>transcribing</code></td>
      <td style="padding: 8px;">Providing a reading of physical handwriting on an image</td>
      <td style="padding: 8px;">Transcribing Maud Lewis's handwritten letter on a photograph.</td>
    </tr>
  </tbody>
</table>

Declaring your motivation allows web software to display notes appropriately—for example, showing `identifying` tags as clickable badges and `commenting` notes as sidebars.

**Vocabulary.** *Motivation* — the declared scholarly purpose or reason why an annotation was created. *Taxonomy* — a structured classification system.

**Takeaway:** Specifying a W3C motivation (`commenting`, `identifying`, `linking`) clarifies the scholarly purpose of each digital note for web software.

---

## **15 Content**

**The Anchoring Problem on the Dynamic Web**

On the public web, anchoring annotations is much harder than inside your local XML file. Websites change constantly. Website redesigns modify HTML layout. Text is updated, and image coordinates shift.

If your annotation simply says: <em>"Attach this note to character 450 on page X"</em>, any minor update to the web page will break your anchor. The note either appears in the wrong spot or disappears completely.

To make web annotations durable across website edits, the W3C standard invented **Selectors**. A selector is a smart mechanism that describes how to find the target passage even if the page layout shifts.

**Vocabulary.** *Dynamic Web* — web pages whose content or styling changes over time through database updates or redesigns. *Selector* — an algorithm or pattern that locates a target passage within a digital document.

**Takeaway:** Web annotations require resilient selectors to ensure notes stay attached to target text even when website layouts are updated.

---

## **16 Content**

**The `TextQuoteSelector`: Robust Text Anchoring**

The most resilient selector for web text is the **`TextQuoteSelector`**. Instead of counting characters or HTML divs, it uses the text itself, surrounded by its immediate context.

A `TextQuoteSelector` records three strings:
<ol>
  <li><strong>`exact`:</strong> The exact text being annotated.</li>
  <li><strong>`prefix`:</strong> The few words immediately preceding the target in the original page.</li>
  <li><strong>`suffix`:</strong> The few words immediately following the target in the original page.</li>
</ol>

Here is a JSON-LD example for Maud Lewis's letter:
```json
"selector": {
  "type": "TextQuoteSelector",
  "exact": "I have two small paintings done",
  "prefix": "Dear Mr. Kinnear, ",
  "suffix": ", one of oxen and one of cats."
}
```

Even if the web archivist changes the webpage font, wraps the letter in new HTML tags, or adds introductory paragraphs, the browser can search for the prefix, exact text, and suffix, reattaching the note perfectly!

**Vocabulary.** *`TextQuoteSelector`* — a resilient W3C selector that locates a target by matching the exact phrase and its immediate surrounding words. *Prefix / Suffix* — context strings used to disambiguate identical phrases on a page.

**Takeaway:** The `TextQuoteSelector` ensures annotations survive web redesigns by locking onto the target phrase and its surrounding context words.

---

## **17 Content**

**Positional and Image Selectors**

While text quotes are ideal for prose, historical documents also include digitized facsimile images, maps. Archival photographs. W3C defines specialized selectors for these media.

Key selector types include:
<ul>
  <li><strong>`TextPositionSelector`:</strong> Records starting and ending character numbers (e.g., characters 100 to 145). Fast to compute, but fragile on updated web pages.</li>
  <li><strong>`FragmentSelector`:</strong> Points to standard media fragments. For IIIF images, it defines a rectangular bounding box:
    <pre><code>"selector": {
  "type": "FragmentSelector",
  "conformsTo": "http://www.w3.org/TR/media-frags/",
  "value": "xywh=160,240,400,120"
}</code></pre>
  </li>
</ul>

With an image fragment selector, you can attach a note directly to King Louis XVI's signature at the bottom of Ace's French decree, or to Maud Lewis's painted signature on an archival photograph!

**Vocabulary.** *Media Fragment* — a W3C standard for addressing temporal or spatial regions of media files using URL coordinates (`xywh`). *Bounding Box* — the rectangular pixel boundaries enclosing an image feature.

**Takeaway:** Image fragment selectors allow scholars to attach commentary directly to specific visual regions on digitized manuscript scans and photographs.

---

## **18 Content**

**Selector Chains for Maximum Durability**

What happens if a website changes so drastically that a single selector fails? Professional web annotation platforms solve this by using **Selector Chains**.

In a selector chain, an annotation includes multiple selectors in a list:
<ol>
  <li>First, the browser tries a fast <code>FragmentSelector</code> or <code>TextPositionSelector</code>.</li>
  <li>If the position shifted due to page edits, the browser falls back to the resilient <code>TextQuoteSelector</code>.</li>
  <li>If the exact words were slightly modernized, an XPath selector attempts to locate the containing paragraph.</li>
</ol>

By combining fast positional lookups with robust text quote searches, selector chains ensure that historical notes survive for years on the evolving web.

**Vocabulary.** *Selector Chain* — an ordered list of fallback selectors that increases the likelihood of successfully resolving a digital annotation anchor. *Graceful Degradation* — software behavior where a system falls back to secondary methods if the primary method fails.

**Takeaway:** Combining positional lookups and text quote selectors into chains guarantees maximum durability for digital commentary on the web.

---

## **19 Content**

**Collaborative Web Annotation with Hypothes.is**

To see W3C web annotation in real-world practice, scholars use tools like **Hypothes.is**.

Hypothes.is is an open-source platform that brings an annotation layer to any website or PDF online:
<ul>
  <li>You install a browser extension or add a simple script to your web page.</li>
  <li>When you highlight text on any website (such as the Nova Scotia Archives or the British Library), a sidebar opens.</li>
  <li>You type your commentary note, add tags (like `#treaty` or `#assignats`), and click save.</li>
  <li>Behind the scenes, Hypothes.is automatically generates a full W3C JSON-LD annotation with a `TextQuoteSelector`!</li>
  <li>Your notes can be private for personal research, shared with a classroom group, or published publicly.</li>
</ul>

This means our three students could collaborate on annotating historical treaty scans across different universities in real time.

**Vocabulary.** *Hypothes.is* — an open-source digital platform that enables collaborative annotation across public web pages and online PDFs. *Annotation Layer* — a digital interface overlaying notes on top of web content without modifying the host site.

**Takeaway:** Platforms like Hypothes.is operationalize the W3C standard, allowing students and scholars to annotate live web pages and PDFs collaboratively.

---

## **20 Content**

**Semantic Tagging and Authority Linking with Recogito**

Another celebrated digital humanities platform built on W3C standards is **Recogito**, created by the Pelagios Network.

Recogito is specifically designed for historical documents, maps, and archival scans:
<ul>
  <li>It allows editors to upload historical texts or high-resolution images.</li>
  <li>When you highlight a place name like "Halifax" or "Digby", Recogito automatically queries global gazetteers (such as GeoNames and Pleiades).</li>
  <li>It displays a map showing the historical location and prompts you to confirm the match.</li>
  <li>Once confirmed, Recogito stores the annotation in W3C format, complete with authority URIs and latitude/longitude coordinates.</li>
</ul>

Recogito bridges the gap between text reading and geographic visualization, turning text mentions into interactive maps.

**Vocabulary.** *Recogito* — a digital humanities tool for collaborative semantic annotation of historical texts, maps. Images. *Geoparsing* — identifying place names in text and mapping them to geographic coordinates.

**Takeaway:** Recogito demonstrates how W3C web annotations connect textual mentions of places to interactive maps and global gazetteers.

---

## **21 Content**

**Linked Open Data and Knowledge Graphs**

When you connect commentary notes to global authority files (such as Wikidata, GeoNames, or VIAF), your digital edition joins a global **Knowledge Graph**.

In a traditional library catalog, documents sit on separate shelves. But in a Linked Open Data knowledge graph, data forms a web of relationships:
<ul>
  <li><em>Peregrine Hopson</em> (Wikidata Q7168341) <strong>[was governor of]</strong> <em>Nova Scotia</em> (Wikidata Q1952).</li>
  <li><em>The Treaty of 1752</em> <strong>[was signed by]</strong> <em>Jean-Baptiste Cope</em> (Wikidata Q6169974).</li>
  <li><em>Maud Lewis</em> (Wikidata Q432374) <strong>[lived in]</strong> <em>Digby County</em> (Wikidata Q257776).</li>
</ul>

When your edition exports its annotations in JSON-LD, external researchers can query these relationships computationally, discovering connections between colonial Canada, revolutionary Europe, and twentieth-century art history.

**Vocabulary.** *Knowledge Graph* — a structured network of interconnected concepts, entities. Relationships encoded in linked data standards. *RDF (Resource Description Framework)* — the foundational W3C data model for linked data.

**Takeaway:** Linking annotations to global authorities integrates local student editions into a worldwide knowledge graph of historical data.

---

## **22 Content**

**Querying Commentary Networks with SPARQL**

How do researchers query vast knowledge graphs? In relational databases, developers use SQL. In the world of Linked Open Data, scholars use **SPARQL** (SPARQL Protocol and RDF Query Language).

A SPARQL query searches for graph patterns across linked datasets. For example, a researcher can ask:
<pre><code>SELECT ?treaty ?governor ?date WHERE {
  ?treaty wdt:P31 wd:Q131569 .       # is a treaty
  ?treaty wdt:P1001 wd:Q1952 .       # jurisdiction: Nova Scotia
  ?treaty wdt:P580 ?date .           # signed date
  ?treaty wdt:P110 ?governor .       # signed by governor
}</code></pre>

In a single query taking less than one second, the database returns every colonial treaty signed in Nova Scotia, its signing date, and the governing British official!

By authoring standards-compliant commentary, our student editions prepare historical data for this advanced digital scholarship.

**Vocabulary.** *SPARQL* — the standard semantic query language used to retrieve and manipulate data stored in Resource Description Framework (RDF) format. *Graph Pattern* — a query template specifying conditions that data nodes and links must satisfy.

**Takeaway:** SPARQL enables scholars to execute complex relational queries across distributed linked data networks and digital commentaries.

---

## **23 Content**

**Comparing TEI Standoff XML vs. W3C JSON-LD**

As a digital editor, you now know two major annotation frameworks: TEI Standoff XML (Lesson 12.1) and W3C Web Annotation JSON-LD (Lesson 12.2). Which one should you use?

Both frameworks have distinct architectural strengths:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9. Border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px. Text-align: left;">Feature</th>
      <th style="padding: 8px. Text-align: left;">TEI Standoff XML</th>
      <th style="padding: 8px. Text-align: left;">W3C JSON-LD</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Primary Purpose</strong></td>
      <td style="padding: 8px;">Long-term archival preservation of texts</td>
      <td style="padding: 8px;">Dynamic, web-native sharing across sites</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>File Relationship</strong></td>
      <td style="padding: 8px;">Self-contained inside the edition document</td>
      <td style="padding: 8px;">External notes pointing to remote URLs</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Schema Validation</strong></td>
      <td style="padding: 8px;">Strict XML Schema / Relax NG validation</td>
      <td style="padding: 8px;">Flexible JSON Schema and RDF graphs</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Best Humanities Use</strong></td>
      <td style="padding: 8px;">Publishing complete critical scholarly editions</td>
      <td style="padding: 8px;">Annotating remote archives, images, and maps</td>
    </tr>
  </tbody>
</table>

In modern digital publishing, projects often maintain primary source editions in TEI XML, then export notes to JSON-LD for interactive web exploration.

**Vocabulary.** *Data data sharing* — the ability of different digital systems and software to exchange and interpret data seamlessly. *Serialization* — converting structured in-memory data objects into a text format (like XML or JSON) for storage or transmission.

**Takeaway:** TEI XML is ideal for archival textual editions, while W3C JSON-LD excels at web-native sharing and distributed annotation across remote servers.

---

## **24 Content**

**Hands-On Exercise: Searching for Text Reuse in VS Code**

Let us practice finding text reuse deterministically in Visual Studio Code.

Follow these practical steps:
<ol>
  <li><strong>Identify Candidate Phrases:</strong> Review your primary witness passage. Highlight a formulaic phrase (e.g., <em>"free liberty of hunting"</em> in Andromeda's treaty, or <em>"l'Assemblée Nationale"</em> in Ace's decree).</li>
  <li><strong>Use VS Code Multi-File Search:</strong> Press <code>Cmd+Shift+F</code> (macOS) or <code>Ctrl+Shift+F</code> (Windows) to open global search across your workspace.</li>
  <li><strong>Configure Search Boundaries:</strong>
    <ul>
      <li>In the <em>files to include</em> box, type <code>src/</code> or your historical corpus directory.</li>
      <li>Search for the exact phrase to detect verbatim loans.</li>
      <li>Use regex mode (click the <code>.*</code> icon) to search with flexible word gaps: <code>liberty\s+(?:\w+\s+){1,4}hunting</code>. This finds "liberty" and "hunting" separated by up to four words!</li>
    </ul>
  </li>
  <li><strong>Review Discovered Matches:</strong> Record matching filenames, line numbers, and surrounding context.</li>
</ol>

**Vocabulary.** *Multi-File Search* — querying an entire folder or project directory simultaneously in an editor. *Regular Expression Proximity* — using regex wildcards to match words within a specified distance.

**Takeaway:** Use VS Code multi-file and regex search to detect verbatim formulas and proximity matches across your project corpus.

---

## **25 Content**

**Hands-On Exercise: Converting a TEI Note to W3C JSON-LD**

Now let us convert one of the manual standoff notes you wrote on Tuesday into a W3C Web Annotation JSON-LD object.

Take your historical note identifying Governor Hopson or Chief Cope from Lesson 12.1:
<ol>
  <li>Create a new file named <code>annotation.json</code> in your project folder.</li>
  <li>Add the standard W3C <code>@context</code> and <code>type</code> headers.</li>
  <li>Set the <code>motivation</code> to <code>"commenting"</code>.</li>
  <li>Put your note text into the <code>body</code> object.</li>
  <li>In the <code>target</code> object, specify the source URL and build a <code>TextQuoteSelector</code> with <code>exact</code>, <code>prefix</code>, and <code>suffix</code> strings from your document.</li>
</ol>

Here is the completed conversion template:
```json
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "type": "Annotation",
  "motivation": "commenting",
  "body": {
    "type": "TextualBody",
    "value": "Major Jean-Baptiste Cope was principal Chief of the Shubenacadie Mi'kmaq who led treaty negotiations.",
    "format": "text/plain"
  },
  "target": {
    "source": "https://archives.novascotia.ca/treaties/1752/",
    "selector": {
      "type": "TextQuoteSelector",
      "exact": "Major Jean Baptiste Cope",
      "prefix": "between His Excellency Peregrine Thomas Hopson and ",
      "suffix": ", Chief Sachem of the Tribe"
    }
  }
}
```

**Vocabulary.** *Data Conversion* — translating data from one representation format into another while preserving semantic meaning. *TextualBody* — a W3C entity representing plain or HTML text content inside an annotation.

**Takeaway:** Converting TEI standoff notes into W3C JSON-LD makes your commentary accessible to web browsers and external digital archives.

---

## **26 Content**

**Designing a rule-based Commentary Index Table**

In your digital edition, readers need a way to browse notes by category without reading every page linearly. A rule-based commentary index provides this structured access.

An effective index table includes five core columns:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9. Border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px. Text-align: left;">Note ID</th>
      <th style="padding: 8px. Text-align: left;">Anchor Target</th>
      <th style="padding: 8px. Text-align: left;">Category &amp. Subtype</th>
      <th style="padding: 8px. Text-align: left;">Headword / Topic</th>
      <th style="padding: 8px. Text-align: left;">External Authority Link</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><code>note_01</code></td>
      <td style="padding: 8px;"><code>#s3</code></td>
      <td style="padding: 8px;">Historical / Biographical</td>
      <td style="padding: 8px;">Chief Jean-Baptiste Cope</td>
      <td style="padding: 8px;">Dictionary of Canadian Biography (biographi.ca)</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><code>note_02</code></td>
      <td style="padding: 8px;"><code>#w14</code></td>
      <td style="padding: 8px;">Philological / word</td>
      <td style="padding: 8px;">Truckhouse</td>
      <td style="padding: 8px;">Oxford English Dictionary</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><code>note_03</code></td>
      <td style="padding: 8px;"><code>#s5</code></td>
      <td style="padding: 8px;">text-linking / Legal</td>
      <td style="padding: 8px;">1725 Dummer's Treaty</td>
      <td style="padding: 8px;">Nova Scotia Archives RG 1</td>
    </tr>
  </tbody>
</table>

Publishing this index at the end of your edition allows students and researchers to navigate annotations directly by topic.

**Vocabulary.** *Commentary Index* — a structured tabular directory listing all annotations in an edition by identifier, category. Target. *Headword* — the primary term or title identifying a specific reference entry.

**Takeaway:** A commentary index table organizes all edition notes into a clear directory with categories, headwords, and authority links.

---

## **27 Content**

**Evaluating Candidate Matches: The Human Gatekeeper**

When running automated discovery tools, remember that an algorithmic match is only a **proposal**. It is not a proven fact.

Every automated candidate must pass three human evaluative gates:
<ol>
  <li><strong>Gate 1: Historical Plausibility:</strong> Was the earlier text physically accessible to the author? (Maud Lewis in 1967 Digby could not have borrowed phrasing from an unpublished private diary in Paris).</li>
  <li><strong>Gate 2: Idiomatic Coincidence:</strong> Is the match simply a standard everyday greeting or common speech idiom rather than an intentional literary allusion?</li>
  <li><strong>Gate 3: Editorial Significance:</strong> Does documenting this connection actually help the reader understand the text, or does it clutter the edition with useless trivia?</li>
</ol>

If a candidate match fails any of these gates, reject it. Your reputation as an editor depends on filtering out noise.

**Vocabulary.** *Candidate Match* — a potential text parallel surfaced by an algorithm that requires human verification. *Evaluative Gate* — a strict quality checkpoint a match must satisfy before being admitted to an edition.

**Takeaway:** Treat all algorithmic matches as proposals; apply strict historical plausibility and significance gates before accepting notes into your edition.

---

## **28 Content**

**Documenting rule-based Discoveries in `COMMENTARY.md`**

Open your `COMMENTARY.md` research ledger. Today you record your rule-based experiments and audit findings.

Add a new section titled `## Wednesday Audit: rule-based Discovery`:
<ol>
  <li><strong>Search Strategy:</strong> What keywords, regex proximity patterns, or multi-file searches did you execute?</li>
  <li><strong>Algorithm Results Table:</strong>
    <ul>
      <li>Matches Found: list every surfaced parallel with source location.</li>
      <li>Classification: label each as True Positive (genuine historical link) or False Positive (coincidental overlap).</li>
    </ul>
  </li>
  <li><strong>Ground Truth Comparison:</strong> Did the automated search catch the notes you wrote on Tuesday? What did it miss, and why?</li>
  <li><strong>W3C Export Verification:</strong> Confirm that your <code>annotation.json</code> file passes JSON-LD syntax validation.</li>
</ol>

Documenting these metrics proves that your edition rests on disciplined comparative research.

**Vocabulary.** *True Positive* — an automated match that represents a genuine, verified historical connection. *False Positive* — an automated match caused by accidental similarity that carries no real historical link.

**Takeaway:** Record search strategies, true/false positive counts, and ground truth comparisons in `COMMENTARY.md` to document your algorithmic audit.

---

## **29 Content**

**Preparing for Friday: The Shift to AI-Assisted Commentary**

Today you explored rule-based tools. You saw that algorithms excel at rigid, verbatim matching. However, struggle with synonyms, summaries, and cultural meaning.

This sets the stage for Friday's final step in the comparative cycle: **Artificial Intelligence**.

Large language models (like Gemini and Claude) operate completely differently from rule-based tools:
<ul>
  <li>They understand synonyms, context, and semantic meaning.</li>
  <li>They can draft fluent, informative explanations of complex historical events in seconds.</li>
  <li><strong>However:</strong> Unlike rule-based tools, language models can hallucinate plausible-sounding falsehoods, invent non-existent book citations, and misdate historical treaties.</li>
</ul>

On Friday, we will test whether AI models can draft accurate commentary notes for Ace, Olyvia. Andromeda's documents, and we will audit their suggestions against Tuesday's manual ground truth and today's rule-based findings.

**Vocabulary.** *Hallucination* — a phenomenon where a generative language model produces plausible-sounding but factually fabricated information. *Three-Way Cycle* — comparing manual human work, rule-based algorithms, and generative AI models.

**Takeaway:** rule-based tools provide predictable string matching, setting the stage for evaluating AI models that understand semantic context but risk factual hallucination.

---

## **30 Content**

**Synthesis: The Complementarity of Tools**

Today you expanded your digital editing toolkit from local XML files to automated search algorithms and international web standards.

You learned:
<ul>
  <li>How rule-based algorithms use stoplists, TF-IDF rarity, and word proximity to uncover text reuse.</li>
  <li>Why algorithms excel at finding verbatim legal boilerplate but miss conceptual summaries.</li>
  <li>How the W3C Web Annotation Data Model structures commentary into Annotation, Target, and Body.</li>
  <li>Why the <code>TextQuoteSelector</code> ensures notes survive website updates on the dynamic web.</li>
  <li>How Linked Open Data and knowledge graphs connect local archival notes to global scholarship.</li>
</ul>

Neither manual research nor automated algorithms can solve the challenges of digital editing alone. Manual work ensures intellectual depth. Rule-based tools provide archival scale. Web standards ensure global accessibility. When combined, they produce resilient, world-class scholarly editions.

**Vocabulary.** *Complementarity* — the way different tools and methods compensate for each other's weaknesses when combined effectively. *Scholarly Rigor* — adhering to strict evidential and methodological standards in research.

**Takeaway:** Combining manual human depth, rule-based archival scale, and W3C web standards produces durable, connected digital scholarly editions.
