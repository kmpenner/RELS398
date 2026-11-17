# Lesson 11.2 — Automated Sentence Alignment and Rule-Based Tools

*RELS 398 / ENGL 398 · Topic 11: Alignment · Meeting #29 (Wed Nov 18)*

***Step 2 of the three-step cycle: deterministic.** Today you test automated length-based sentence alignment algorithms (Gale-Church) and interactive tools, auditing their precision and recall against your Tuesday manual ground truth.*

---

## **01 Content**

**The Need for Automated Sentence Alignment**

Yesterday you aligned historical sentences completely by hand. You matched ten sentence pairs and inspected every word. Doing ten sentences by hand is pleasant and educational. 

However, historical documents are often much longer. A legal code can contain hundreds of pages. A diplomatic registry can span thousands of clauses. Aligning ten thousand sentences by hand would take months of tedious labor.

This is where computational algorithms help. Computers can compare sentence lengths and vocabulary in seconds. They can propose alignments across vast digital corpora.

Today we explore Step 2 of the three-step cycle: **deterministic tools**. We will examine how automated algorithms align bilingual sentences, and we will measure their accuracy against your Tuesday manual ground truth.

**Takeaway:** Automated sentence alignment algorithms scale up translation linking across thousands of sentences, freeing human scholars from repetitive manual labor.

---

## **02 Content**

**What Does "Deterministic" Mean in Text Alignment?**

In computer science, a **deterministic algorithm** follows fixed, transparent mathematical rules. It does not guess. It does not use neural networks or artificial intelligence.

Key qualities of deterministic tools:

* Given the exact same two text files, the algorithm always produces the exact same alignment.
* Every decision can be traced back to an explicit mathematical calculation.
* The rules are predictable, repeatable, and transparent.

Deterministic tools are the bedrock of scholarly computing. Because they operate on clear rules, you can understand exactly why an algorithm made a correct link or why it made a mistake.

**Takeaway:** Deterministic tools follow fixed mathematical rules, producing predictable, transparent, and reproducible alignment results.

---

## **03 Content**

**The Core Intuition: Length-Based Alignment**

How can a computer match sentences in two different languages without understanding what the words mean?

In 1993, researchers William Gale and Kenneth Church discovered a fascinating linguistic truth. When humans translate text, sentence length remains remarkably consistent:

* A short source sentence almost always produces a short translated sentence.
* A long source paragraph almost always produces a long translated paragraph.
* Translators rarely turn a five-word clause into a fifty-word speech.

This insight forms the basis of **length-based sentence alignment** (the Gale-Church algorithm). Instead of reading the words, the computer simply counts characters. It pairs sentences whose character lengths match expected linguistic ratios.

**Takeaway:** Length-based alignment relies on the fact that translated sentences naturally correlate in length with their original source sentences.

---

## **04 Content**

**Character Counts vs. Word Counts**

Why did Gale and Church count individual characters rather than whole words?

Languages differ significantly in how they build words:

* Some languages use many short helper words (prepositions, articles, auxiliary verbs).
* Other languages combine concepts into long, inflected compound words.
* English might use three words (*in the house*) where Latin uses one (*domi*).

However, total character length (the number of letters) remains surprisingly stable across European translations. On average, a French sentence has about 1.15 characters for every 1.0 character in its English translation.

By comparing character counts rather than word counts, length-based algorithms avoid errors caused by differing word-formation habits.

**Takeaway:** Counting characters rather than words provides a more stable baseline for comparing sentence lengths across different languages.

---

## **05 Content**

**Sentence Boundary Detection**

Before an algorithm can count characters in a sentence, it must know where each sentence starts and ends. This task is called **sentence boundary detection** or **sentence tokenization**.

To a computer, a text file is just a long ribbon of letters. The computer must search for sentence endings:

* Periods (`.`), question marks (`?`), and exclamation points (`!`).
* Whitespace following the punctuation mark.
* A capital letter starting the next word.

In modern clean prose, sentence boundary detection is fairly easy. In historical documents, however, punctuation is full of traps.

**Takeaway:** Sentence boundary detection splits raw text into discrete sentence units by identifying terminal punctuation and whitespace.

---

## **06 Content**

**Historical Punctuation Traps**

Historical manuscripts frequently confuse automated sentence splitters.

Common historical stumbling blocks include:

* **Abbreviations:** Periods after titles and shortened words (*Mr.*, *Capt.*, *art.*, *décr.*) look like sentence endings.
* **Archaic Punctuation:** Colon dashes (`:-`), virgules (`/`), and raised dots that modern software does not recognize.
* **Run-On Legal Syntax:** 18th-century French decrees and English treaties often run for thirty lines without a single period.
* **Informal Writing:** Maud Lewis letters often omit periods entirely or use dashes to separate thoughts.

If the sentence splitter breaks a sentence at the wrong spot, every downstream alignment will fail.

**Takeaway:** Historical abbreviations, non-standard punctuation, and run-on legal clauses can trick automated sentence splitters.

---

## **07 Content**

**Visualizing the Alignment Matrix**

To understand how an alignment algorithm works, visualize a two-dimensional grid or **alignment matrix**.

Imagine a grid:

* Source sentences are listed along the vertical axis (from top to bottom).
* Translation sentences are listed along the horizontal axis (from left to right).

Each cell in the grid represents a possible pairing between source sentence `s` and target sentence `t`.

If two texts run in the exact same chronological order, the correct alignment forms a diagonal line from the top-left corner down to the bottom-right corner. The algorithm's job is to find the most probable diagonal path across the grid.

**Takeaway:** An alignment matrix plots source sentences against target sentences, where correct correspondences form a diagonal path across the grid.

---

## **08 Content**

**The Cost Function: Scoring Sentence Pairs**

How does the computer decide which path across the grid to take? It uses a **cost function**.

A cost function assigns a mathematical penalty score to every potential cell:

* If the length of source `s1` matches the expected length of target `t1`, the penalty score is near zero (an excellent match).
* If `s1` is twenty characters long and `t1` is three hundred characters long, the penalty score is very high (an improbable match).

The algorithm calculates the penalty scores for all possible combinations. It selects the overall path through the grid that has the lowest total penalty.

**Takeaway:** A cost function assigns penalty scores based on length differences, allowing the algorithm to find the path of least resistance.

---

## **09 Content**

**Allowing for Structural Shifts**

A naive algorithm would only look for simple one-to-one matches down the main diagonal. But real translations contain structural shifts.

The Gale-Church algorithm considers six possible move types at every step:

* **1:1:** One source sentence maps to one target sentence.
* **1:2:** One source sentence splits into two target sentences.
* **2:1:** Two source sentences merge into one target sentence.
* **1:0:** A source sentence was omitted in translation.
* **0:1:** A target sentence was added with no source equivalent.
* **2:2:** Two source sentences correspond to two target sentences as a combined block.

The algorithm tests each move type, searching for the lowest penalty score across the whole document.

**Takeaway:** Robust alignment algorithms evaluate multiple move types (including splits and merges) to accommodate translational variations.

---

## **10 Content**

**The "Domino Effect" in Alignment Slippage**

What happens when an automated algorithm makes a single mistake?

Because the algorithm reads sequentially from beginning to end, a single error can trigger a **domino effect**:

* Suppose the algorithm accidentally aligns source sentence `s4` with translation `t5`.
* Every subsequent sentence is now off by one.
* Sentence `s5` will be incorrectly paired with `t6`, and `s6` will be paired with `t7`.

This cascading failure continues until the algorithm hits a major structural break or a massive length difference that forces it back on track.

Recognizing the domino effect is crucial when auditing automated results.

**Takeaway:** A single misalignment can cause a cascading domino effect where all subsequent sentences become shifted by one position.

---

## **11 Content**

**Lexical Anchors: Preventing Cascading Errors**

How do scholars prevent cascading alignment errors? We use **lexical anchors** (also called landmark words or cognates).

Lexical anchors are words that are easy for computers to identify in both languages:

* **Proper Names:** *Louis*, *Halifax*, *Maud*, *Kinnear*, *Chebucto*.
* **Dates and Numbers:** *1752*, *1791*, *1967*, *Article 3*.
* **Cognates:** Words that look almost identical across languages (*constitution*, *assemblée*, *nation*).

When the algorithm sees *1752* in source sentence `s8` and in translation sentence `t8`, it locks them together. These anchor points act like pins along the diagonal path, stopping domino errors in their tracks.

**Takeaway:** Lexical anchors like dates, numbers, and proper names provide fixed landmark points that prevent cascading alignment errors.

---

## **12 Content**

**Running a Length-Based Aligner: hunalign in InterText**

You do not need to write Python to run sentence alignment. The standard length-based aligner, **hunalign**, combines the Gale-Church length statistics with an optional bilingual dictionary. If you give it no dictionary, it aligns by length alone, builds a dictionary from that first pass, and then aligns again.

The **InterText** desktop editor comes with hunalign built in. The workflow has five steps:

1. Import your source XML and your `target_translation.xml`, telling InterText that the alignable elements are your `<s>` sentences.
2. Run the aligner (**Edit > Auto aligner**, then choose hunalign).
3. Export the result as `alignment_deterministic.xml` before you change anything. This raw output is what you score.
4. Compare its sentence pairs with your `alignment_manual.xml` and calculate precision and recall.
5. Only then correct the pairs in InterText: **Enter** moves text down a row and **Backspace** moves it up.

Two other well-known tools do different jobs. **LF Aligner** is a front end for hunalign aimed at translators building translation memories. The **Alpheios Alignment Editor** and **Ugarit** are for *manual word-level* alignment: you click to pair words or phrases. They do not propose sentence pairs, so they are not deterministic sentence aligners. You will meet word-level work on Friday.

**Takeaway:** hunalign in InterText proposes sentence pairs automatically by length. Score its raw output before you correct it, or you end up grading your own corrections.

---

## **13 Content**

**Step-by-Step: Using an Alignment Web GUI**

Here is the standard workflow when using a web alignment tool:

1. **Prepare Your Text:** Copy your clean transcription text into your clipboard.
2. **Paste into Columns:** Open the tool in your web browser. Paste the historical source text on the left and your English translation on the right.
3. **Run Automatic Splitting:** Click the button to detect sentence boundaries. Verify that the sentence cuts look correct.
4. **Inspect Initial Links:** Review the algorithm's proposed sentence pairs.
5. **Drag to Correct:** If you spot a split (1:2) or merge (2:1), drag the sentence boxes together.
6. **Export TEI XML:** Click export to download your clean `<linkGrp>` markup.

This visual workflow avoids terminal friction while producing professional XML data.

**Takeaway:** Web alignment tools follow a simple paste, split, align, adjust, and export workflow that eliminates command-line frustration.

---

## **14 Content**

**Translating Tool Output into TEI Standoff Markup**

When you export data from an alignment tool, inspect the resulting XML.

A clean export produces a standard TEI `<linkGrp>`:

```xml
<linkGrp type="sentence-alignment">
  <link target="#s1 #t1"/>
  <link target="#s2 #t2"/>
  <link target="#s3 #t3 #t4"/>
</linkGrp>
```

Check the exported file against your document:

* Do the IDs in the `@target` attributes match the `xml:id` values in your transcription?
* Are the hash marks (`#`) present on every target?
* Is the `<linkGrp>` wrapped inside a `<standOff>` container?

Understanding the underlying XML ensures you can fix formatting errors easily.

**Takeaway:** Always inspect exported alignment XML to verify that target IDs, hash marks, and standOff containers conform to TEI standards.

---

## **15 Content**

**Word-Level Alignment: Beyond the Sentence**

Once sentences are linked, can algorithms align individual words?

Sentence alignment is relatively easy because sentence order rarely changes. Word alignment is much harder because different languages use radically different word orders:

* In English, adjectives precede nouns (*the white cat*).
* In French, adjectives often follow nouns (*le chat blanc*).
* German puts verbs at the very end of subordinate clauses.

Automated word alignment tools must map complex word shuffles without getting confused by reordered syntax.

**Takeaway:** Word-level alignment is more challenging than sentence alignment because languages frequently invert or reorder words.

---

## **16 Content**

**Bilingual Dictionaries and Lookup Tables**

How do deterministic tools approach word alignment? They rely on **bilingual dictionaries** and lookup tables.

A deterministic word aligner checks each word against a dictionary:

* It looks up the French word *décret* and finds English *decree*.
* If both words appear in linked sentences `s1` and `t1`, it creates a word link.
* It checks inflected forms against a lemmatized vocabulary list.

When a word appears in the dictionary, alignment is fast and accurate. But when historical spelling diverges from modern dictionaries, the rule-based approach stalls.

**Takeaway:** Deterministic word aligners use bilingual dictionaries to match words across linked sentences, succeeding when vocabulary is standardized.

---

## **17 Content**

**The Out-of-Vocabulary (OOV) Bottleneck**

When historical words do not appear in modern dictionaries, we call them **out-of-vocabulary (OOV)** words.

Historical documents are filled with OOV words:

* Archaic legal terms (*assignats*, *billon*, *lettres patentes*).
* Regional place names (*Cobequid*, *Chebucto*, *Digby Gut*).
* Historical spelling variations (*agree-d*, *compleat*, *recompence*).

A rule-based dictionary cannot link a word it has never seen. When an algorithm encounters an OOV word, it leaves the word unaligned or guesses incorrectly.

Human editors must step in to bridge these lexical gaps.

**Takeaway:** Out-of-vocabulary words like archaic spellings and local place names cannot be resolved by standard bilingual dictionaries alone.

---

## **18 Content**

**Comparing Manual and Deterministic Results**

Now we come to the core pedagogical exercise of our three-step cycle: **the comparative audit**.

You have two sets of sentence alignments:

1. **Set A (Your Tuesday Baseline):** Hand-crafted in VS Code, representing verified human judgment.
2. **Set B (Wednesday's Algorithm):** Produced automatically by length-based alignment software.

Place both files side by side in VS Code using the two-column split editor. Compare them sentence by sentence. Where did the algorithm agree with your human choices? Where did it make a different choice?

**Takeaway:** Comparing automated algorithmic results against your manual baseline reveals the strengths and weaknesses of computational methods.

---

## **19 Content**

**Calculating Accuracy: Precision and Recall**

To evaluate the algorithm scientifically, we use two standard metrics: **Precision** and **Recall**.

Think of them in plain terms:

* **Precision:** Out of all the links the algorithm proposed, how many were actually correct?
* **Recall:** Out of all the true links that exist in the text, how many did the algorithm manage to find?

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Metric</th>
      <th style="width: 40%;">Plain English Definition</th>
      <th style="width: 35%;">Formula</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Precision</strong></td>
      <td>How reliable are the proposed links?</td>
      <td>Correct Links / Total Proposed Links</td>
    </tr>
    <tr>
      <td><strong>Recall</strong></td>
      <td>How complete is the alignment?</td>
      <td>Correct Links / Total True Links</td>
    </tr>
  </tbody>
</table>

Calculating these two percentages gives you an objective measurement of algorithmic quality.

**Takeaway:** Precision measures the accuracy of proposed links, while recall measures how many total true links were captured.

---

## **20 Content**

**Case Study: Auditing Ace's 1791 French Decree**

Let us see how a length-based algorithm performs on Ace's French Revolutionary decree.

The French decree contains formal administrative clauses:

* Sentence 1 announces the decree (*L'Assemblée Nationale décrète...*).
* Sentence 2 is an eighty-word sentence specifying metal currency denominations.

What happens during automated alignment?

* **Success:** Sentence 1 is short in French and short in English. The algorithm scores a clean 1:1 match with 100% precision.
* **Failure:** In Sentence 2, the English translator split the eighty-word sentence into two clear English sentences. The length algorithm attempted a 1:1 match and failed.

Human intervention was required to change the 1:1 link into a 1:2 link.

**Takeaway:** Length-based tools handle simple French clauses easily but struggle when translators split long administrative sentences.

---

## **21 Content**

**Case Study: Auditing Andromeda's 1752 Treaty**

Andromeda's document is the 1752 Peace and Friendship Treaty. It features numbered articles.

Numbered articles provide a huge advantage for alignment algorithms:

* Every article begins with an explicit label (*Article 1*, *Article 2*, *Article 3*).
* Numbers act as perfect lexical anchors.
* Even if sentence lengths vary, the Roman numerals keep the algorithm on track.

Because the treaty text has strong structural anchors, the automated alignment achieved nearly 95% precision. 

Structured legal texts with numbered divisions are the easiest genre for automated tools to align.

**Takeaway:** Numbered articles and Roman numerals act as structural anchors that dramatically boost alignment accuracy in legal treaties.

---

## **22 Content**

**Case Study: Auditing Olyvia's Maud Lewis Letter**

Olyvia's document is an informal handwritten letter by Maud Lewis.

Letters present distinct challenges for length-based algorithms:

* Maud's sentences are brief and conversational (*I got your letter. Was glad to hear.*).
* Punctuation is sporadic; thoughts flow together without periods.
* In a parallel French translation, colloquial Maritime expressions require longer French phrasing.

Because the sentence boundaries were ambiguous, the automated sentence splitter struggled. It merged two short thoughts into one block. 

This case demonstrates why personal letters require careful human boundary checking before running automated tools.

**Takeaway:** Informal letters with conversational syntax and sporadic punctuation require human boundary editing before algorithms can succeed.

---

## **23 Content**

**Evaluating Non-Isomorphic Alignments**

In linguistics, **isomorphism** means having the exact same shape or structure. When two languages share the same sentence structure, alignment is isomorphic.

**Non-isomorphic alignments** occur when two languages express the same meaning using completely different grammatical structures:

* A single French passive participle requires an English subordinate clause with three words.
* A legal idiom in the 1752 treaty requires a full sentence explanation in modern French.

Deterministic algorithms expect roughly equal ratios. When syntax becomes non-isomorphic, length formulas break down. Documenting these moments teaches us where languages diverge in expressive style.

**Takeaway:** Non-isomorphic structures occur when languages use radically different grammatical forms to express the same thought.

---

## **24 Content**

**Pre-Processing Your Texts for Better Alignment**

If you want automated tools to succeed, you should prepare your texts beforehand. This preparation is called **pre-processing**.

Simple pre-processing steps for novices:

1. **Clean Up Broken Words:** Remove hyphenated line-end splits from transcription files (*fa- / brication* becomes *fabrication*).
2. **Standardize Abbreviations:** Expand known abbreviations or protect trailing periods (*Mr.* becomes `Mr_`).
3. **Harmonize Paragraphs:** Ensure that both files have the same number of paragraph breaks before running sentence splitters.

Spending three minutes cleaning text before alignment saves an hour of manual corrections later.

**Takeaway:** Pre-processing text by cleaning line breaks, harmonizing paragraphs, and protecting abbreviations drastically improves alignment accuracy.

---

## **25 Content**

**Automated Standoff Generation in Python**

For students interested in how tools work behind the scenes, a simple Python script can generate `<linkGrp>` markup in seconds.

Here is the general structure of an alignment script:

1. It reads the source file and extracts all elements with `xml:id` attributes starting with `s`.
2. It reads the translation file and extracts all elements with IDs starting with `t`.
3. It compares character lengths and pairs matching IDs.
4. It writes a clean `<linkGrp>` block to an output file.

You do not need to write this script today. But knowing that the logic is straightforward demystifies digital tools.

**Takeaway:** Scripted alignment simply automates ID extraction, length comparison, and XML writing into a repeatable loop.

---

## **26 Content**

**Saving Your Wednesday Alignment File**

Today you will save your verified algorithmic output in your project repository.

File naming convention:

* File path: `alignment_deterministic.xml`.
* Location: Your project root folder alongside `alignment_manual.xml`.
* Content: Your 10-sentence passage with automated links that you have inspected, corrected, and verified.

In the file header, record any changes you had to make to the algorithm's initial proposal. Documenting your edits shows how human expertise refines computational output.

**Takeaway:** Save your inspected algorithmic output as alignment_deterministic.xml, documenting any corrections made to the computer's proposals.

---

## **27 Content**

**Documenting Discrepancies in ALIGNMENT.md**

A scholarly edition does not just publish data; it explains its editorial methodology.

In your project repository, open `ALIGNMENT.md` and record your findings:

* Total sentence pairs tested.
* Number of pairs the algorithm got right on the first try.
* Number of pairs that required human correction.
* Calculated Precision and Recall percentages.
* A brief paragraph explaining why the algorithm struggled on specific sentences.

This reflection document forms part of your semester portfolio.

**Takeaway:** Documenting alignment metrics and failure modes in ALIGNMENT.md provides scholarly transparency for your digital edition.

---

## **28 Content**

**Common Novice Pitfalls in Algorithmic Alignment**

When working with automated alignment tools, watch out for these four traps:

1. **Trusting the Algorithm Blindly:** Assuming that because a computer generated the links, they must be correct. Always verify by eye.
2. **Ignoring the Domino Effect:** Missing a single shifted link at sentence four, resulting in eight misaligned sentences below it.
3. **Mismatched IDs After Export:** Exporting generic IDs (`src_1`, `tgt_1`) from a web tool that do not match your project's `xml:id` convention.
4. **Deleting Punctuation in Pre-Processing:** Accidentally erasing periods needed for sentence splitting while cleaning up text.

Staying alert to these pitfalls ensures your data remains rigorous.

**Takeaway:** Avoid blind trust in algorithms, check for cascading shifts, and ensure exported IDs match your project's naming conventions.

---

## **29 Content**

**The Limits of Deterministic Tools**

Deterministic tools are fast, transparent, and reproducible. But they have clear limits:

* They do not understand semantics, context, or metaphor.
* They cannot recognize when a translator translated a phrase idiomatically rather than literally.
* They fail when historical spelling is inconsistent or unstandardized.

A length formula knows that two sentences are fifty characters long. It cannot tell you whether the sentences actually mean the same thing. Human judgment remains irreplaceable.

**Takeaway:** While deterministic tools excel at speed and mathematical transparency, they lack semantic understanding and cannot interpret figurative language.

---

## **30 Content**

**Looking Ahead: Step 3 (AI Assistance on Friday)**

Congratulations on completing Step 2 of the alignment cycle!

Here is how our comparative progression connects:

* **Tuesday (Manual):** You authored 10 sentence pairs and three Leipzig glosses by hand (human gold standard).
* **Wednesday (Deterministic):** You tested length-based algorithms, inspected alignment matrices, and calculated precision and recall.
* **Friday (AI-Assisted):** On Friday, you will use artificial intelligence (Claude and Gemini in VS Code) to propose sentence alignments and Leipzig glosses.

You will compare all three methods side by side. You will see exactly where statistical rules succeed and where neural AI models provide deeper linguistic insights.

**Takeaway:** Today's deterministic audit bridges manual human scholarship with Friday's AI-assisted alignment tools.
