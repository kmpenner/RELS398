# Lesson 8.3 — AI-Assisted Linguistic Markup, Comparative Audit, and Assignment 8 Synthesis

*RELS 398 / ENGL 398 · Topic 8: Lemmatization · Meeting #22 (Fri Oct 30)*

***Step 3 of the three-step cycle: AI-assisted model.** Today you prompt AI models in VS Code Antigravity to analyze historical grammar, execute a three-way comparative audit (Manual vs NLP vs AI). Synthesize your final tei linguistic markup portfolio.*

---

## **01 Content**

**The Third Tier: Prompting Neural Models for Grammar**

Welcome to the final stage of Week Eight. On Tuesday, you parsed and lemmatized twenty words by hand using scholarly dictionaries. That manual work gave you an authoritative ground truth. On Wednesday, you ran deterministic NLP pipelines like TreeTagger and SpaCy. You saw their speed, but you also saw them stumble on Out-of-Vocabulary historical spellings.

Today, we take Step 3 of our three-step cycle: AI models. In VS Code Antigravity, we can prompt AI models to analyze historical grammar.

Unlike deterministic taggers that follow rigid suffix rules, modern language models were trained on billions of words from historical book. Archives. They possess remarkable intuition for archaic vocabulary. However, they bring serious risks, including invented lemmas and unrequested modernizations. Today, you will test an AI model on your text, execute a three-way comparativ. Finalize your linguistic markup assignment.

**Vocabulary.** *Language Model (LLM)*. An AI model trained on vast text datasets that predicts and generates natural language. *Three-Way Comparative Audit* — Comparing annotations across three tiers: manual human craft, deterministic NLP scrip. Generative ai models.

**Takeaway:** Large language models bring powerful intuition to historical language, but their outputs must be audited against manual ground truth.

---

## **02 Content**

**How Large Language Models Understand Historical Prose**

How can an AI model read eighteenth-century French or archaic legal Eng. A rule-based tool failed? The secret lies in pre-training data.

Deterministic taggers like TreeTagger rely on relatively small, modern dictionaries. If a word like *décrétoit* is missing from its dictionary, the tool fails. By contrast, AI models have ingested millions of digitized historical books, including eighteenth-century F. Colonial treaties.

During training, the model learned statistical associations across centuries of language change. It knows that eighteenth-century French authors wrote *-oit* where modern writers use *-ait*. It knows that *shew'd* means *showed*. This broad historical exposure gives neural models a significant advantage over simple lookup. Reading archival prose.

**Vocabulary.** *Pre-Training Data* — The massive collection of digital book. Historical documents used to train a neural language model. *Context Window* — The amount of surrounding text a model considers when analyzing words.

**Takeaway:** Language models succeed on historical prose because their training data includes centuries of digitized historical literature.

---

## **03 Content**

**Structured Prompt Engineering for Linguistic Markup**

While an AI model understands historical vocabulary, it will not output TEI XML automatically unless you instruct it with care. In computational editing, we use **structured prompt engineering**.

A structured prompt gives the model three essential things:
<ol>
  <li><strong>Role Definition:</strong> Instruct the model to act as an expert computational philologist and TEI encoder.</li>
  <li><strong>Task Specification:</strong> Instruct the model to tokenize the passage, look up canonical lemmas, and assign Universal Dependencies tags.</li>
  <li><strong>Output Format:</strong> Explicitly demand valid TEI P5 XML wrapped in <code>&lt;s&gt;</code>, <code>&lt;w&gt;</code>, and <code>&lt;pc&gt;</code> elements.</li>
</ol>

Without strict prompt formatting, models tend to produce conversational essays or unformatted markdown tables. A structured prompt forces the model to return clean, machine-readable XML.

**Vocabulary.** *System Prompt* — High-level instructions provided to an AI model that define its p. Required output format. *Structured Output* — Machine-readable output (such as valid XML or JSON) constrained by strict formatting rules.

**Takeaway:** Structured prompts define the model's expert role, specify its linguistic task, and enforce strict TEI XML output formatting.

---

## **04 Content**

**Providing the Universal Dependencies Schema in Prompts**

Never assume an AI model remembers the exact tags you want. Large models know dozens of different grammar tagsets, from older Penn Treebank tags to French national standards.

To guarantee consistent output, provide the exact **Universal Dependencies (UD)** tagset directly in your prompt. List the core UPOS tags: `NOUN`, `VERB`, `ADJ`, `ADV`, `PRON`, `DET`, `AUX`, `ADP`, `CCONJ`,. `punct`.

Instruct the model explicitly: *Use only official Universal Dependencies UPOS tags in the pos attribute*. When the model has the allowed tags in its prompt, it will not invent non-standard labels like `PREP` or `ARTICLE`. This keeps the AI output aligned with your Tuesday ground truth and Wednesday NLP benchmark.

**Takeaway:** Including the 17 Universal Dependencies UPOS tags in your prompt prevents the model from inventing non-standard grammatical labels.

---

## **05 Content**

**Enforcing Strict Negative Constraints**

In prompt engineering, what you forbid is just as important as what you request. These boundaries are called **negative constraints**.

Language models are trained to be helpful assistants. When they see historical spelling mistakes or scribal abbreviations, their default instinct is to "fix" the text for modern readers. In scholarly editing, this instinct corrupts historical evidence!

Include these four negative constraints in your prompt:
<ol>
  <li><strong>DO NOT alter surface text:</strong> Preserve the exact historical characters, spelling slips, and accents inside the <code>&lt;w&gt;</code> tags.</li>
  <li><strong>DO NOT invent lemmas:</strong> Use modern canonical dictionary headwords; do not invent archaic lemmas like <em>faisoir</em>.</li>
  <li><strong>DO NOT drop punctuation:</strong> Enclose every comma, period, and colon in a <code>&lt;pc&gt;</code> tag.</li>
  <li><strong>DO NOT wrap in markdown fences:</strong> Output raw XML without conversational introductions or explanations.</li>
</ol>

Negative constraints rein in the model's helpful impulses and enforce scholarly discipline.

**Vocabulary.** *Negative Constraint*. An explicit instruction in a prompt that forbids unwanted model behaviors, such as modernizing spelling or dropping punctuation.

**Takeaway:** Negative constraints prevent AI models from modernizing historical spellings, dropping punctuation, or adding conversational filler.

---

## **06 Content**

**Invented word Modes in Historical Lemmatization**

The greatest danger when using AI in scholarly editing is **invented word**. A inv. A model generates plausible-sounding output that is factually wrong or non-existent.

In linguistic markup, invented words take specific forms:
<ul>
  <li><strong>Invented Lemmas:</strong> The model invents a fake Latin or Old French root word that never existed in any dictionary.</li>
  <li><strong>Confabulated Meanings:</strong> The model invents an imaginary historical meaning to explain an unusual spelling.</li>
  <li><strong>Ghost Morphemes:</strong> The model breaks a simple word into non-existent prefixes and suffixes.</li>
</ul>

Because language models write with total grammatical confidence, invented words can easily fool unwary editors. Every lemma produced by an AI model must be checked against an authoritative dictionary (OED or TLFi).

**Vocabulary.** *Invented word* — Confidently generated model output that is factually false, ungrounded, or non-existent in reality. *Lexical Verification* — Checking model-generated words against an authoritative reference dictionary.

**Takeaway:** AI models can confidently invent non-existent lemmas; every AI-generated headword must be verified against an authoritative lexicon.

---

## **07 Content**

**The Modernizing error Hazard in Historical Linguistics**

A subtle form of invented word is **modernizing error**. Modernizing. A model treats a genuine historical feature as an error and silently "corrects" it.

In Andromeda's 1752 Treaty, the scribe wrote *acknowledg'd*. An AI model might silently change the surface text to *acknowledged* inside the `<w>` tag, erasing the historical apostrophe. In Maud Lewis's letters, an informal phrase like *them things* might be silently converted to *those things*.

In Ace's 1791 decree, an 18th-century verb form like *décrétoit* might be silently changed to *décrétait*. When an editor asks for linguistic markup, they want tags attached to the historical ink, not a modern rewrite. Tracking modernizing errors is one of your main tasks during today's audit.

**Vocabulary.** *Modernizing error* — An autom. A model inappropriately modernizes or standardizes genuine historical language features.

**Takeaway:** Watch out for hypercorrection: AI models often try to smooth away historical spellings, contractions, and scribal quirks.

---

## **08 Content**

**Handling Out-of-Vocabulary Terms with Generative Context**

While AI models have risks, they also possess genuine strengths. Their greatest advantage over deterministic taggers is their ability to handle Out-of-Vocabulary historical words.

On Wednesday, you saw that TreeTagger failed on *décrétoit*. *shew'd* because those exact spellings were missing from its modern dictionary. A AI model does not suffer from this rigid limitation.

Because the AI model reads the entire sentence, it understands the syntax. It sees that *décrétoit* occupies the finite verb slot following the subject *l'Assemblée*. It recognizes the historical *-oit* suffix as an older imperfect ending. It correctly deduces that the base lemma is *décréter*. Where deterministic tools fail, generative models use context to solve historical puzzles.

**Takeaway:** Generative AI models use full sentence context to deduce correct lemmas for historical spellings that break deterministic taggers.

---

## **09 Content**

**Prompting for TEI XML vs JSON Output**

When designing an AI pipeline, you have two choices for output format: requesting raw TEI XML directly, or requesting structured JSON that you convert to XML with a script.

Requesting TEI XML directly is fast and convenient:
```xml
<w lemma="promise" pos="VERB">promis'd</w>
```
However, models sometimes make small XML syntax errors, such as forgetting a closing tag or omitting quotes around attributes.

Requesting structured JSON is often more robust:
```json
{"token": "promis'd", "lemma": "promise", "pos": "VERB"}
```
A short Python script can validate the JSON and convert it into valid TEI XML. For today's classroom exercise, prompting directly for clean TEI XML is completely f. Large projects often use the json-to-xml route.

**Takeaway:** Prompting for TEI XML directly is fast for short excerpts; prompting for JSON provides stricter programmatic validation for large texts.

---

## **10 Content**

**The Three-Way Comparative Audit: Manual vs NLP vs AI**

Now we bring all three stages of Week Eight together in our **Three-Way Comparative Audit**.

Open three files side by side in VS Code:
<ol>
  <li><code>ground_truth_manual.xml</code>: Tuesday's hand-verified philological baseline.</li>
  <li><code>nlp_baseline.xml</code>: Wednesday's deterministic SpaCy / TreeTagger output.</li>
  <li><code>ground_truth_ai.xml</code>: Today's AI-generated markup.</li>
</ol>

By comparing all three tiers across the exact same twenty-word passage, you can evaluate each technology objectively. Where did all three agree? Where did the deterministic tool fail while the AI succeeded? Where did the AI hallucinate while human scholarship stood firm?

**Takeaway:** The three-way audit compares manual, deterministic, and AI markup side by side, evaluating the strengths and weaknesses of each tier.

---

## **11 Content**

**Taxonomy of Discrepancies: Four Error Categories**

When you compare your three files, you will find differences. To analyze them rigorously, classify every discrepancy into one of four standard categories:

<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>Name</th>
      <th>Description and Cause</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Category A</strong></td>
      <td>Human Slip</td>
      <td>A human error in Tuesday's manual ground truth caused by fatigue or a typo.</td>
      <td>Human miskeyed lemma as <code>trety</code></td>
    </tr>
    <tr>
      <td><strong>Category B</strong></td>
      <td>Deterministic Rigid Miss</td>
      <td>The rule-based NLP tool failed due to an Out-of-Vocabulary historical spelling.</td>
      <td>SpaCy failed on <code>décrétoit</code> or <code>shew'd</code></td>
    </tr>
    <tr>
      <td><strong>Category C</strong></td>
      <td>AI Hallucination / Smoothing</td>
      <td>The AI model modernized spelling, invented a fake lemma, or dropped punctuation.</td>
      <td>AI altered <code>promis'd</code> to <code>promised</code></td>
    </tr>
    <tr>
      <td><strong>Category D</strong></td>
      <td>Genuine Crux / Ambiguity</td>
      <td>The text allows two equally valid grammatical readings; both tiers are defensible.</td>
      <td>Homograph <code>will</code> as noun vs auxiliary</td>
    </tr>
  </tbody>
</table>

This taxonomy turns random errors into structured scholarly insights.

**Vocabulary.** *Error Taxonomy*. A formal classification system used to categoriz. Analyze the root causes of computational and human errors.

**Takeaway:** Classify every disagreement into Category A (human slip), B (NLP rigid miss), C (AI hallucination), or D (genuine crux).

---

## **12 Content**

**Evaluating Token-Level Accuracy Across All Three Tiers**

To complete your benchmark, calculate token-level accuracy for both automated tiers against your manual ground truth.

Create a summary comparison table in your notes:

<table>
  <thead>
    <tr>
      <th>Metric</th>
      <th>Deterministic NLP (SpaCy / TreeTagger)</th>
      <th>AI Model (Antigravity / Claude)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Total Tokens Evaluated</td>
      <td>20</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Matching UPOS Tags</td>
      <td>18 / 20 (90%)</td>
      <td>19 / 20 (95%)</td>
    </tr>
    <tr>
      <td>Matching Lemmas</td>
      <td>16 / 20 (80%)</td>
      <td>19 / 20 (95%)</td>
    </tr>
    <tr>
      <td>Overall Token Accuracy</td>
      <td>80%</td>
      <td>95%</td>
    </tr>
  </tbody>
</table>

In most historical documents, the AI model scores higher on lemm. Of its broader vocabulary. It may lose points on punctuation or surface-text alterations.

**Takeaway:** Calculate token-level POS and Lemma accuracy for both automated tiers to see which tool performed best on your document.

---

## **13 Content**

**Calculating AI Precision, Recall, and Invented word Rates**

In addition to accuracy, calculate the model's **invented word rate** and **modernizing error rate**.

Use these two simple metrics:
<ul>
  <li><strong>Hallucination Rate:</strong> (Number of Invented Lemmas / Total Tokens) * 100. In a sound scholarly prompt, this should be 0%.</li>
  <li><strong>Hypercorrection Rate:</strong> (Number of Altered Surface Words / Total Tokens) * 100. This measures how often the model modernized your historical characters.</li>
</ul>

If the model changed *promis'd* to *promised* once in twenty words, its modernizing error rate is 5%. Documenting these rates proves that you are evaluating AI with scientific rigor.

**Takeaway:** Quantify AI risks by calculating hallucination and hypercorrection rates alongside standard precision and recall scores.

---

## **14 Content**

**Testing AI on Andromeda's 1752 Treaty Excerpt**

Let us look at how an AI model performs on Andromeda's project: the 1752 P. Friendship treaty.

Clause: *All Treaties shall be renewed by the Governor*.

Here is the three-way comparison:
<ul>
  <li><strong>Manual Ground Truth:</strong> <em>All</em> (DET, all), <em>Treaties</em> (NOUN, treaty), <em>shall</em> (AUX, shall), <em>be</em> (AUX, be), <em>renewed</em> (VERB, renew).</li>
  <li><strong>Deterministic SpaCy:</strong> Matched all five tokens perfectly (100% accuracy).</li>
  <li><strong>AI Model:</strong> Matched all five tokens perfectly, and correctly identified that <em>renewed</em> is a passive participle.</li>
</ul>

On standard 18th-century legal formulas, both automated tools perform exceptionally well. Disagreements only emerge when archaic contractions like *promis'd* or legal compounds like *whereunto* appear.

**Takeaway:** On standard legal English formulas, both deterministic NLP and AI models achieve near-perfect agreement with human ground truth.

---

## **15 Content**

**Testing AI on Ace's 1791 French Decree Excerpt**

Now let us examine Ace's project: a 1791 French Revolutionary decree containing the archaic verb *décrétoit*.

Sentence: *L'Assemblée nationale décrétoit la loi*.

Here is the three-way comparison:
<ul>
  <li><strong>Manual Ground Truth:</strong> <em>décrétoit</em> &rarr; lemma <code>décréter</code>, UPOS <code>VERB</code>, Features: Tense=Imp|VerbForm=Fin.</li>
  <li><strong>Deterministic SpaCy:</strong> <em>décrétoit</em> &rarr; lemma <code>décrétoit</code>, UPOS <code>NOUN</code> (Category B error: OOV suffix failure).</li>
  <li><strong>AI Model:</strong> <em>décrétoit</em> &rarr; lemma <code>décréter</code>, UPOS <code>VERB</code>, Features: Tense=Imp|VerbForm=Fin (Match!).</li>
</ul>

Look at that result! SpaCy failed because *-oit* was missing from its modern dictionary. The AI model recognized the 18th-century suffix. Mapped the verb to its proper infinitive *décréter*. This is a clear demonstration of AI's strength on historical morphology.

**Takeaway:** AI models successfully resolve 18th-century French verbal suffixes like *-oit* where deterministic dictionaries fail.

---

## **16 Content**

**Testing AI on Maud Lewis's Folk Correspondence Excerpt**

Next, we examine Olyvia's project: Maud Lewis's informal 1967 letter: *I received your letter today*.

Here is the three-way comparison:
<ul>
  <li><strong>Manual Ground Truth:</strong> <em>your</em> &rarr; lemma <code>you</code>, UPOS <code>PRON</code>, Feature: Poss=Yes (OED policy).</li>
  <li><strong>Deterministic SpaCy:</strong> <em>your</em> &rarr; lemma <code>your</code>, UPOS <code>PRON</code> (Lexicographical policy disagreement).</li>
  <li><strong>AI Model:</strong> <em>your</em> &rarr; lemma <code>you</code>, UPOS <code>PRON</code> (Followed prompt policy!).</li>
</ul>

Because our prompt explicitly instructed the AI model to map possessive pronouns to base personal pronouns, the AI followed our project policy. SpaCy could not be reconfigured without editing its internal lexicon. AI prompts offer superior flexibility when enforcing custom project guidelines.

**Takeaway:** AI models easily adopt custom project dictionary policies provided in prompts, outperforming rigid pre-compiled tagger libraries.

---

## **17 Content**

**Adjudicating Disagreements: The Editor as Arbiter**

After completing your three-way audit, you will have a table of disagreements. Now comes the core scholarly duty: **editorial adjudication**.

An algorithm cannot decide what belongs in your final edition. The human editor is the ultimate arbiter. Go through each discrepancy:
<ul>
  <li>If the machine made an error (Category B or C), reject the machine prediction and keep your manual ground truth.</li>
  <li>If the machine exposed a genuine human slip in your Tuesday table (Category A), gratefully correct your ground truth!</li>
  <li>If the disagreement is a genuine crux (Category D), select the reading best supported by historical evidence and document your reasons.</li>
</ul>

This review process transforms raw machine output into reliable, peer-reviewed scholarship.

**Vocabulary.** *Editorial Adjudication*. The scholarly decision-making p. A human editor resolves conflicting readings and approves the final text.

**Takeaway:** The human editor serves as the ultimate arbiter, adjudicating every machine disagreement before publishing the edition.

---

## **18 Content**

**Synthesizing the Final Linguistic XML: `transcription_linguistic.xml`**

With all disagreements adjudicated, you are ready to produce your official deliverable: `transcription_linguistic.xml`.

This file merges the verified readings into your complete project TEI document. Every word token in your 20-word excerpt is wrapped in a `<w>` tag with verified `@lemma`. `@pos` attributes. Punctuation is enclosed in `<pc>`. Sentences are enclosed in `<s>`.

Check that your file is well-formed XML:
<ul>
  <li>Every open tag has a matching closing tag.</li>
  <li>Attribute values are enclosed in quotes.</li>
  <li>The XML tree nests cleanly without overlapping boundaries.</li>
</ul>

This file represents the definitive linguistic layer of your digital edition.

**Takeaway:** Combine your adjudicated readings into `transcription_linguistic.xml`, verifying clean XML syntax and well-formed tags.

---

## **19 Content**

**Transparent Metadata Attribution with `@resp`**

In digital scholarly editions, transparency is paramount. R. Researchers must know who produced each annotation: a human scholar, a deterministic script, or an ai model.

TEI P5 provides the `@resp` (responsibility) attribute for this exact purpose. In your `teiHeader`, define your agents:
```xml
<respStmt>
  <resp>Manual annotation</resp>
  <name xml:id="editor">Ken Penner</name>
</respStmt>
<respStmt>
  <resp>Deterministic NLP pipeline</resp>
  <name xml:id="spacy">SpaCy 3.7 (en_core_web_sm)</name>
</respStmt>
<respStmt>
  <resp>AI-assisted parsing</resp>
  <name xml:id="claude">Claude 3.5 Sonnet / Antigravity</name>
</respStmt>
```

On your `<w>` elements, you can cite who verified the tag: `<w lemma="renew" pos="VERB" resp="#editor">`. Transparent attribution ensures full academic integrity.

**Vocabulary.** *`@resp`*. The tei attribute that indicates who is responsible for a specific editorial decision, correction, or markup layer.

**Takeaway:** Use the TEI `@resp` attribute and header statements to document whether annotations came from human editors, scripts, or AI models.

---

## **20 Content**

**Combining All Layers: The Complete TEI Architecture**

Take a moment to admire what your TEI document now contains. Over eight weeks, you have built a deeply layered digital monument:

<ol>
  <li><strong>Metadata Layer:</strong> The <code>teiHeader</code> catalogues author, date, archive, license, and project policies.</li>
  <li><strong>Image Layer:</strong> The <code>&lt;facsimile&gt;</code> container links high-resolution image manifests directly to text surfaces.</li>
  <li><strong>Diplomatic Layer:</strong> The transcribed text preserves original ink, scribal lineation (<code>&lt;lb/&gt;</code>), and historical characters.</li>
  <li><strong>Regularization Layer:</strong> The <code>&lt;choice&gt;</code> elements pair original spellings (<code>&lt;orig&gt;</code>) with modernized readings (<code>&lt;reg&gt;</code>).</li>
  <li><strong>Linguistic Layer:</strong> The <code>&lt;w&gt;</code> and <code>&lt;s&gt;</code> elements record dictionary lemmas, parts of speech, and syntactic features.</li>
</ol>

All five layers coexist in a single well-formed XML file. This is the true power of the Text Encoding Initiative.

**Takeaway:** Your final TEI file unifies metadata, images, diplomatic text, normalized readings, and linguistic grammar in a single standards-compliant document.

---

## **21 Content**

**Building Syntactic Dependency Trees with AI**

In addition to parts of speech, you can prompt modern AI models to generate complete Universal Dependencies syntax trees in CoNLL-U format.

In your prompt, instruct the model: *For each word, identify its governing head ID. Its deprel relation tag*. The model will output the full 10-column table, identifying the root v. Linking subjects, obj. Modifiers.

When evaluating AI syntax trees, check for **cycle errors**. In a valid dependency tree, no word can depend on itself. Arrows must never form closed loops. The tree must form a clean hierarchy descending from the central root verb.

**Vocabulary.** *Treebank* — A text corpus annotated with complete syntactic dependency or phrase-structure trees. *Cycle Error*. An invalid syntactic grap. Dependency links form an infinite closed loop rather than a rooted tree.

**Takeaway:** AI models can predict complete syntactic dependency trees, but editors must audit them to ensure clean hierarchies without cycle errors.

---

## **22 Content**

**Auditing AI Dependency Trees Against Ground Truth**

Auditing a syntax tree is straightforward when you follow the grammatical flow of the sentence.

Ask these four structural questions:
<ol>
  <li><strong>Root Check:</strong> Did the model assign <code>root</code> to the main finite verb or participle?</li>
  <li><strong>Subject Check:</strong> Does the nominal subject (<code>nsubj</code>) point directly to the root verb?</li>
  <li><strong>Object Check:</strong> Does the direct object (<code>obj</code>) attach to its governing transitive verb?</li>
  <li><strong>Preposition Check:</strong> Do prepositions attach to their noun objects with relation <code>case</code>?</li>
</ol>

If the model attaches an adverbial clause to the wrong noun, correct the head ID. Auditing syntax trees sharpens your understanding of how historical authors constructed arguments.

**Takeaway:** Audit AI dependency trees by verifying root verbs, subject links, direct objects, and prepositional attachments.

---

## **23 Content**

**The Reflection Report: Analyzing Linguistic Bottlenecks**

For tonight's Assignment 8 submission, you will write a **300–500 word critical reflection** analyzing your findings.

Your reflection should not simply restate your tables. It should answer these scholarly questions:
<ul>
  <li>Which morphological categories caused the highest failure rate in the automated tools?</li>
  <li>Why did deterministic taggers stumble on historical spellings, while the AI model handled them?</li>
  <li>Did the AI model introduce any subtle hypercorrections or hallucinated lemmas?</li>
  <li>How did Module 6 spelling normalizations help bridge the gap between historical ink and modern algorithms?</li>
</ul>

A strong reflection connects technical error rates to broader philological and historical principles.

**Takeaway:** Your 300–500 word reflection should analyze why specific grammatical categories failed and discuss the trade-offs of automation.

---

## **24 Content**

**Documenting the Three-Way Audit in `LINGUISTIC_AUDIT.md`**

To keep your work organized, assemble y. Reflection inside `linguistic_audit.md` in your repository root.

Your audit report should contain four clear sections:
<ol>
  <li><strong>Master Comparison Table:</strong> A 20-row table comparing Token, Manual Parse, NLP Parse, and AI Parse.</li>
  <li><strong>Accuracy Scorecard:</strong> Numerical accuracy percentages, precision, recall, and hallucination rates.</li>
  <li><strong>Discrepancy Taxonomy:</strong> An analysis sorting disagreements into Categories A, B, C, and D.</li>
  <li><strong>Critical Reflection:</strong> Your 300–500 word discussion of algorithmic strengths and limitations.</li>
</ol>

This report serves as the primary scholarly text that K. Evaluate for your assignment grade.

**Takeaway:** Compile your master comparison table, scorecard, discrepancy taxonomy, and reflection in `LINGUISTIC_AUDIT.md`.

---

## **25 Content**

**Finalizing Assignment: Module 8 (Linguistic Markup)**

Tonight at 11:00 PM, **Assignment: Module 8 (Linguistic Markup)** is due on Moodle. Let us review the grading. You know exactly how your work will be evaluated:

<ul>
  <li><strong>Manual Ground Truth Precision (4 pts / 40%):</strong> Your 20-word manual parse accurately identifies canonical dictionary lemmas and inflectional features without grammatical errors.</li>
  <li><strong>TEI Linguistic Markup Validity (3 pts / 30%):</strong> Your XML cleanly wraps tokens in <code>&lt;w&gt;</code> and <code>&lt;pc&gt;</code> elements with valid <code>lemma=</code> and <code>pos=</code> attributes conforming to TEI P5.</li>
  <li><strong>Comparative Error Analysis (3 pts / 30%):</strong> Your reflection insightfully discusses why automated engines struggle with homographs, historical spellings, or rare irregular conjugations.</li>
</ul>

Total grade: 10 points (scaled to 80 points in the Moodle gradebook). Meeting these three standards ensures full marks.

**Takeaway:** Assignment 8 is graded on manual precision (4 pts), TEI XML validity (3 pts), and comparative error analysis (3 pts).

---

## **26 Content**

**Validating Your TEI File Against the Course Schema**

Before submitting your assignment, you must run the course schema validator on `transcription_linguistic.xml`.

In your VS Code terminal, run the validator:
```bash
python3 scripts/validate_tei.py src/modules/Module_08_Lemmatization/transcription_linguistic.xml
```

The validator checks:
<ul>
  <li>Well-formed XML syntax: all tags closed and properly nested.</li>
  <li>Valid attribute names: <code>lemma</code> and <code>pos</code> on <code>&lt;w&gt;</code> elements.</li>
  <li>No illegal characters or broken entity references.</li>
</ul>

Fix any validation errors immediately. A valid TEI file is a mandatory requirement for full credit.

**Takeaway:** Always run the schema validator on your TEI file before submission to verify that XML syntax and attributes are well-formed.

---

## **27 Content**

**Packaging the Submission Portfolio for Moodle**

To complete your submission, make sure all four project deliverables are committed to your git repository:

<ol>
  <li><code>LEMMATIZATION_POLICIES.md</code>: Your project's dictionary and tokenization rules.</li>
  <li><code>tagger_pipeline.py</code>: Your Python script for automated NLP execution.</li>
  <li><code>transcription_linguistic.xml</code>: Your validated TEI XML fragment with <code>&lt;w&gt;</code> elements.</li>
  <li><code>LINGUISTIC_AUDIT.md</code>: Your three-way comparative audit table and 300–500 word reflection.</li>
</ol>

On Moodle, upload your `transcription_linguistic.xml`. Paste the text of your `linguistic_audit.md` into the online submission box before 11:00 pm tonight.

**Takeaway:** Submit your validated TEI XML file and reflection report to the Moodle assignment portal before 11:00 PM tonight.

---

## **28 Content**

**Looking Ahead: From Words to Named Entities in Module 9**

Congratulations on completing Module 8! You have mastered grammatical words, dictionary headwords, and syntactic trees.

Next week, in Module 9, we take the next logical step in digital textual editing: **Named Entity Recognition (NER)**.

Grammar tells us what a word *does* in a sentence (it is a noun, a verb, an adjective). Named entity markup tells us what a word *refers to* in the real world:
<ul>
  <li>People: <code>&lt;persName&gt;</code> (Peregrine Thomas Hopson, Maud Lewis, King Louis XVI).</li>
  <li>Places: <code>&lt;placeName&gt;</code> (Halifax, Nova Scotia, Paris).</li>
  <li>Organizations: <code>&lt;orgName&gt;</code> (National Assembly, Mi'kmaq Nation).</li>
</ul>

Your linguistic markup provides the grammatical foundation on which named entity recognition will build.

**Takeaway:** Module 9 will build on your linguistic markup by identifying and encoding named people, places, and historical organizations.

---

## **29 Content**

**The Digital Textual Scholar's Toolkit**

Step back and look at the method you have practiced this week. You did not rely exclusively on human close reading, nor did you blindly surrender your text to an automated algorithm.

You practiced a three-step critical method:
<ol>
  <li><strong>Establish Ground Truth:</strong> Close human philology and authoritative dictionaries set the gold standard.</li>
  <li><strong>Deploy Deterministic Tools:</strong> Fast rule-based and statistical scripts scale processing across corpora.</li>
  <li><strong>Evaluate with AI & Audit:</strong> Generative models resolve complex edge cases, while critical human review catches hallucinations.</li>
</ol>

This balanced workflow represents the cutting edge of digital humanities scholarship today.

**Takeaway:** True digital scholarship combines human philological ground truth, deterministic scripts, and generative AI under critical human oversight.

---

## **30 Content**

**Human Judgment in an Era of Linguistic AI**

As AI models grow more f. Capable, some people wonder if human textual scholarship will become obsolete.

Week Eight gives you the definitive answer to that question: **absolutely not.**

An AI model has no historical stake in truth. It will happily alter historical characters, smooth over scribal slip. Invent non-existent latin roots with absolute confidence. It cannot replace the scholar who spent months studying the ink, the pap. The archival context of an eighteenth-century document.

AI models are extraordinary power tools. But power tools require a skilled craftsperson. You are the craftsperson. Your historical knowledge, your philological judgment,. Your commitment to truth are what make digital editions trustworthy. Keep that critical human eye sharp, and enjoy your weekend!

**Takeaway:** AI provides extraordinary speed, but human scholars remain the essential guardians of historical truth and textual integrity.

---
