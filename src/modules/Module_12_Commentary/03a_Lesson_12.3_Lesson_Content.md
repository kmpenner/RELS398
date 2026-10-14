# Lesson 12.3 — AI-Assisted Commentary Drafting, Intertextual Verification, and Philological Vetting

*RELS 398 / ENGL 398 · Topic 12: Commentary · Meeting #33 (Fri Nov 27)*

***Step 3 of the three-step cycle: AI-assisted.** Today you evaluate AI models as drafting assistants for scholarly commentary notes across our three student projects. You test negative prompt constraints against hallucinations, conduct a forensic fact-checking audit, compare Manual vs Deterministic vs AI methods, and record your editorial decisions in a COMMENTARY.md ledger.*

---

## **01 Content**

**Entering Step 3: AI-Assisted Commentary Drafting**

This week we have examined how editors build scholarly commentary for historical documents. On Tuesday, you drafted notes by hand. You identified linguistic puzzles, historical people, and literary echoes in your text. On Wednesday, you explored rule-based algorithms. You tested stoplists, phrase matching, and W3C Web Annotation links.

Today is Friday, Meeting #33. We arrive at Step 3 of our comparative cycle: **artificial intelligence**.

Large language models (such as Claude and Gemini) can draft commentary notes quickly. Unlike simple keyword matching, AI models understand syntax and semantic meaning. They can summarize complex historical context, translate archaic phrasing, and draft explanatory paragraphs in seconds.

However, computational speed introduces serious editorial hazards. Language models predict plausible words based on statistical patterns. They do not consult verified archives unless we guide them. They can fabricate citations, misinterpret legal terms, and smooth away real historical difficulties.

Today you will evaluate AI models as drafting assistants. You will test their suggestions against your Tuesday manual notes and Wednesday rule-based results.

**Vocabulary.** *Generative AI* — computational models that generate text by predicting probable words from training data. *Human-in-the-Loop (HITL)* — an editorial workflow where human scholars review and approve every automated proposal.

**Takeaway:** AI models generate commentary quickly through semantic inference, but human editors must verify every claim against primary sources.

---

## **02 Content**

**Semantic Inference vs Lexical Matching**

To understand AI commentary, we must contrast **lexical matching** with **semantic inference**:
<ul>
  <li><strong>Lexical Matching (Wednesday):</strong> Finds exact words or lemmatized forms. If two documents use different words for the same idea, keyword matching fails.</li>
  <li><strong>Semantic Inference (Friday):</strong> Models words in high-dimensional vector spaces. The AI recognizes related concepts, synonyms, and thematic motifs even when no words match directly.</li>
</ul>

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px; text-align: left; width: 25%;">Analytical Feature</th>
      <th style="padding: 8px; text-align: left; width: 35%;">Rule-Based Matching (Wed)</th>
      <th style="padding: 8px; text-align: left; width: 40%;">AI Semantic Inference (Fri)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Matching Basis</strong></td>
      <td style="padding: 8px;">Exact character strings and word stems</td>
      <td style="padding: 8px;">Contextual meanings and thematic associations</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Synonym Handling</strong></td>
      <td style="padding: 8px;">Blind to synonyms unless manually listed</td>
      <td style="padding: 8px;">Understands equivalent concepts easily</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Primary Weakness</strong></td>
      <td style="padding: 8px;">Misses idea paraphrases</td>
      <td style="padding: 8px;">Invents connections that never existed historically</td>
    </tr>
  </tbody>
</table>

For example, consider Andromeda's 1752 Peace and Friendship Treaty. The text mentions "liberty of hunting and fishing." A rule-based search only finds identical legal phrasing. An AI model recognizes idea links to colonial resource rights and Mi'kmaw sovereignty.

**Takeaway:** Semantic inference allows AI models to connect related ideas across different vocabularies, acting as powerful hypothesis generators.

---

## **03 Content**

**AI Capabilities in Commentary Drafting**

When given clear guidelines, modern AI models excel at specific editorial tasks:
<ul>
  <li><strong>Drafting Historical Context:</strong> Summarizing background events, political institutions, and social customs of an era.</li>
  <li><strong>Explaining Technical Terms:</strong> Defining historical legal phrases, archaic units of currency, and specialized trade jargon.</li>
  <li><strong>Paraphrasing Complex Syntax:</strong> Unpacking convoluted legal clauses into plain language for modern readers.</li>
  <li><strong>Structuring Data:</strong> Formatting prose notes into structured TEI XML or JSON-LD tags.</li>
</ul>

Consider our cohort documents:
<ul>
  <li><strong>Ace (1791 French Decree):</strong> The model explains the monetary depreciation of paper <em>assignats</em> during the French Revolution.</li>
  <li><strong>Olyvia (1967 Maud Lewis Letter):</strong> The model identifies folk art terminology, Nova Scotia postal routes, and regional prices in 1967.</li>
  <li><strong>Andromeda (1752 Treaty):</strong> The model outlines the roles of Governor Peregrine Hopson and Mi'kmaw Chief Jean-Baptiste Cope in Halifax.</li>
</ul>

The model acts as an eager research assistant. It produces a first draft in seconds, saving hours of initial typing.

**Takeaway:** AI models speed up commentary drafting by providing historical summaries, defining specialized terms, and structuring note metadata.

---

## **04 Content**

**The Epistemic Hazard: Citation Hallucination**

Despite their fluency, large language models present a major risk: **hallucination**.

Language models are word-predicting text generators. They predict what word sounds natural next in a sentence. They do not know whether a historical claim is true or false. When asked for evidence, models often invent convincing details:
<ul>
  <li><strong>Fabricated Primary Sources:</strong> Citing archive files, treaty articles, or court cases that do not exist.</li>
  <li><strong>Ghost Citations:</strong> Inventing author names, book titles, volume numbers, and page references that look scholarly but are completely fictitious.</li>
  <li><strong>False Quotations:</strong> Producing plausible quotations in archaic English or French that never appear in real historical documents.</li>
</ul>

In ordinary conversation, a minor error may go unnoticed. In a scholarly edition, an invented citation destroys the credibility of your research. A digital edition must be dependable. Readers rely on your notes to understand primary evidence.

**Vocabulary.** *Hallucination* — a phenomenon where an AI model generates false information, citations, or quotations while sounding confident and authoritative. *Epistemic integrity* — the truthfulness and verifiable accuracy of scholarly claims.

**Takeaway:** Because AI models predict words statistically, they can fabricate citations and historical evidence that appear completely genuine.

---

## **05 Content**

**Cohort Hallucination Audit: Treaty Clauses and Maud Lewis**

Let us examine real examples of model hallucinations from our three student projects.

When asked to provide historical notes for Andromeda's 1752 Treaty, an unconstrained model claimed:
<p style="background-color: #fef2f2; border-left: 4px solid #ef4444; padding: 12px; margin: 12px 0;">
<em>"Article 9 of the 1752 Treaty specifies that all trade disputes shall be adjudicated before the Court of Admiralty in Boston."</em>
</p>

This claim sounds official. But the 1752 Treaty contains only eight articles. Article 9 does not exist. Furthermore, trade disputes were managed in Halifax, not Boston. The model hallucinated the clause by blending details from older colonial records.

Similarly, when asked about Olyvia's 1967 letter from Maud Lewis to Leonard Kinnear, a model asserted:
<p style="background-color: #fef2f2; border-left: 4px solid #ef4444; padding: 12px; margin: 12px 0;">
<em>"Leonard Kinnear was a prominent art dealer in Montreal who hosted Lewis's first solo gallery exhibition in November 1966."</em>
</p>

This statement is entirely false. Leonard Kinnear was an amateur collector from New Brunswick who corresponded with Maud Lewis by mail. Maud Lewis never had a solo gallery show in Montreal in 1966.

**Takeaway:** Never accept AI claims about archival people or legal articles without checking the primary documents directly.

---

## **06 Content**

**Historical Anachronism and Conceptual Flattening**

A second major danger is **anachronism**. AI models are trained mostly on modern internet text. As a result, they frequently project modern concepts onto historical documents:
<ul>
  <li><strong>Modern Legal Definitions:</strong> Interpreting 18th-century treaties using 21st-century contract law concepts.</li>
  <li><strong>Modern Economic Concepts:</strong> Treating 1791 French <em>assignats</em> like modern fiat currency rather than land-backed revolutionary bonds.</li>
  <li><strong>Biographical Misunderstandings:</strong> Describing Maud Lewis's folk paintings using modern commercial art marketing terminology.</li>
</ul>

This tendency causes **idea flattening**. The model erases the unique historical oddities of the past. It replaces strange historical practices with familiar modern ideas.

Scholarly commentary must highlight the strangeness of the past. It should explain how historical people thought within their own time. When an AI replaces 18th-century concepts with modern clichés, the editor must step in and correct the text.

**Vocabulary.** *Anachronism* — placing an event, person, or idea in a time period where it does not belong. *idea flattening* — erasing historical differences by describing past ideas with modern categories.

**Takeaway:** AI models tend to project modern ideas onto historical records, requiring editors to guard against anachronism.

---

## **07 Content**

**Automation Bias and Editorial Vigilance**

When working with AI tools, editors face a psychological trap called **automation bias**.

Automation bias is the human tendency to trust automated systems uncritically. When an AI outputs a beautifully written, grammatical paragraph with clear headings, our brains assume it is correct. We read quickly and miss factual errors.

To fight automation bias, you must adopt **editorial vigilance**:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px; text-align: left; width: 30%;">Vigilance Habit</th>
      <th style="padding: 8px; text-align: left; width: 70%;">Action in VS Code</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Verify Every Date</strong></td>
      <td style="padding: 8px;">Check dates against archival metadata files in your workspace.</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Check Every Person</strong></td>
      <td style="padding: 8px;">Look up historical figures in authority records like the Dictionary of Canadian Biography.</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Confirm Quotations</strong></td>
      <td style="padding: 8px;">Search your transcription file using <code>Ctrl+F</code> to confirm the exact quoted string.</td>
    </tr>
  </tbody>
</table>

Treat every AI output as an unverified draft written by an eager student intern.

**Takeaway:** Automation bias leads scholars to trust fluent AI prose; editors must actively verify dates, names, and quotes against primary files.

---

## **08 Content**

**The Epistemic Boundary: Public History vs Archival Witnesses**

To evaluate AI assistance, you must know what language models know and what they do not know.

Language models have vast knowledge of **broad public history**:
<ul>
  <li>They know the major dates and battles of the French Revolution.</li>
  <li>They know the names of British colonial governors and French monarchs.</li>
  <li>They know general information about famous artists and historic treaties.</li>
</ul>

However, models have no direct access to **unique archival witnesses**:
<ul>
  <li>The model has never seen the physical letter Maud Lewis mailed to Leonard Kinnear in 1967.</li>
  <li>The model does not know the exact ink corrections on Ace's copy of the 1791 French decree.</li>
  <li>The model cannot see the wax seals or margin notations on Andromeda's 1752 treaty manuscript.</li>
</ul>

This division defines your **epistemic boundary**. Use AI to draft general historical context. But rely exclusively on your own eyes and transcription files for the unique features of your manuscript.

**Takeaway:** AI models excel at general historical background but know nothing about the physical peculiarities of your unique archival manuscript.

---

## **09 Content**

**Designing Structured System Prompts for Commentary**

Casual prompts produce poor commentary. If you ask an AI model, "Tell me about this document," it returns rambling paragraphs filled with generic opinions.

A scholarly **system prompt** guides the model with clear rules:
<ol>
  <li><strong>Role Definition:</strong> State the exact scholarly role (for example, "You are an assistant editor in digital documentary editing").</li>
  <li><strong>Document Context:</strong> Provide the exact title, date, author, and archival repository of your source.</li>
  <li><strong>Target Span:</strong> Supply the exact sentence or phrase you want to annotate, including its <code>xml:id</code> anchor.</li>
  <li><strong>Target Category:</strong> Specify whether you want a philological, historical, or intertextual note.</li>
  <li><strong>Audience Level:</strong> Ask for clear, concise prose suitable for undergraduate researchers.</li>
</ol>

When you provide concrete boundaries, the model focuses its attention on the specific passage. Its answers become factual, relevant, and useful.

**Takeaway:** Structured system prompts define roles, context, target spans, and categories, forcing the AI to generate disciplined commentary drafts.

---

## **10 Content**

**Negative Prompt Constraints and Guardrails**

Positive instructions tell the AI what to do. **Negative constraints** tell the AI what it is strictly forbidden from doing.

Negative guardrails are your best defense against hallucinated citations:
<ul>
  <li><em>"Do NOT invent secondary source citations or page numbers."</em></li>
  <li><em>"Do NOT assume modern legal meanings for 18th-century terms."</em></li>
  <li><em>"If a historical fact is unverified or uncertain, explicitly write [UNVERIFIED]."</em></li>
  <li><em>"Cite only primary sources included in the prompt context."</em></li>
  <li><em>"Keep explanations under 100 words per note."</em></li>
</ul>

Forcing the model to output `[UNVERIFIED]` is especially effective. It gives the model permission to admit uncertainty instead of inventing a plausible lie.

When you inspect the generated draft in VS Code, you can search for `[UNVERIFIED]` to see exactly where you need to do manual archive research.

**Takeaway:** Negative prompt constraints prevent hallucinations by explicitly forbidding invented citations and demanding [UNVERIFIED] flags for uncertain claims.

---

## **11 Content**

**Schema-Constrained Generation: Structured JSON and TEI Output**

Raw text output from an AI model is difficult to integrate into digital editions. You must manually copy, paste, and reformat every sentence.

Instead, you can instruct the model to produce **schema-constrained output** using JSON or TEI XML:
<pre><code>{
  "target_id": "seg_assignat_01",
  "category": "historical",
  "lemma": "assignats",
  "draft_note": "Paper currency issued during the French Revolution, backed by confiscated church lands.",
  "confidence": "high",
  "sources": [
    "Archives Parlementaires, vol. 26"
  ]
}</code></pre>

Demanding structured fields forces the model to separate its claims into distinct parts:
<ul>
  <li><code>target_id</code> ensures the note links to an anchor in your transcription.</li>
  <li><code>category</code> matches your editorial taxonomy from Lesson 12.1.</li>
  <li><code>lemma</code> identifies the exact word being explained.</li>
  <li><code>sources</code> isolates citations so you can verify them individually.</li>
</ul>

Structured output simplifies validation and allows automated scripts to parse the results.

**Takeaway:** Requesting JSON or XML output forces the model to structure its commentary notes into distinct, machine-readable fields.

---

## **12 Content**

**Anchoring AI Notes to Stable XML Identifiers**

In Lesson 12.1, you created stable anchors in your transcription files using `xml:id` attributes. Every note pointed to an anchor with a `@target` reference.

When you generate notes with an AI assistant, you must maintain this anchoring discipline:
<ul>
  <li>Provide the AI with the list of valid `xml:id` attributes from your document.</li>
  <li>Instruct the model to link every proposed note to an existing ID.</li>
  <li>Forbid the model from creating new, unanchored notes.</li>
</ul>

Consider this example from Ace's 1791 decree:
<pre><code>&lt;!-- In your transcription file --&gt;
&lt;seg xml:id="seg_loi_1791_03"&gt;fabrication des assignats&lt;/seg&gt;

&lt;!-- In the AI-generated note --&gt;
&lt;note type="historical" target="#seg_loi_1791_03" resp="#ai-draft"&gt;
  The French National Assembly authorized assignat production to stabilize public debt.
&lt;/note&gt;</code></pre>

Notice the `@resp` attribute. It records that this note was drafted by an AI model. Anchoring notes to stable IDs keeps your edition organized.

**Takeaway:** AI-drafted commentary notes must point to valid xml:id anchors in your transcription, with provenance tracked in the resp attribute.

---

## **13 Content**

**Philological Vetting: 18th-Century French and Colonial English**

AI models often misread historical vocabulary because words evolve over time. Editors must vet every linguistic claim:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px; text-align: left; width: 25%;">Historical Word</th>
      <th style="padding: 8px; text-align: left; width: 35%;">AI Modern Misreading</th>
      <th style="padding: 8px; text-align: left; width: 40%;">Vetted Historical Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>cours forcé</strong> (1791 French)</td>
      <td style="padding: 8px;">Forced running or fast pace</td>
      <td style="padding: 8px;">Mandatory legal tender status for paper currency.</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Truckhouse</strong> (1752 Treaty)</td>
      <td style="padding: 8px;">A garage or repair depot for trucks</td>
      <td style="padding: 8px;">A government trading post for regulated bartering of furs and goods.</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Febuary</strong> (1967 Maud Lewis)</td>
      <td style="padding: 8px;">A spelling mistake that should be corrected</td>
      <td style="padding: 8px;">A phonetic folk spelling reflecting maritime Canadian speech patterns.</td>
    </tr>
  </tbody>
</table>

When vetting AI drafts, check historical dictionaries. For 18th-century French, check the 1798 *Dictionnaire de l'Académie française*. For colonial English, check the Oxford English Dictionary's historical quotations.

**Takeaway:** Philological vetting catches humorous or misleading modern readings of historical vocabulary, restoring true archival meaning.

---

## **14 Content**

**Intertextual Allusion Detection: Real vs Imagined Parallels**

AI models excel at detecting thematic allusions across literary and legal traditions. Because they have seen millions of books, they notice echoes that human editors overlook.

However, models frequently confuse thematic resemblance with actual textual borrowing:
<ul>
  <li><strong>Thematic Resemblance:</strong> Two texts discuss the same topic (such as peace, trade, or winter cold) using standard cultural imagery.</li>
  <li><strong>Textual Borrowing:</strong> An author deliberately adapts or quotes an earlier document.</li>
</ul>

For example, when examining Andromeda's 1752 Treaty, an AI might suggest an allusion to John Locke's *Second Treatise of Government* regarding property rights. While Locke influenced colonial thinking, there is no evidence the Halifax treaty authors quoted Locke directly.

Conversely, the model might correctly identify borrowing between the 1752 Treaty and the 1725 Dummer's Treaty. In that case, identical phrasing confirms genuine textual reuse.

The editor's job is to distinguish between genuine historical borrowing and accidental conceptual overlap.

**Takeaway:** AI models discover interesting thematic parallels, but editors must verify whether an echo represents genuine historical borrowing or coincidence.

---

## **15 Content**

**Entity Linking and Authority Control (Wikidata and VIAF)**

In Lesson 12.1 and Module 9, you explored named entities. Commentary notes frequently explain historical persons and geographic places.

You can ask an AI model to propose authority control identifiers for historical entities:
<ul>
  <li><strong>Wikidata QIDs:</strong> Persistent identifiers for people, concepts, and places across all languages.</li>
  <li><strong>VIAF IDs:</strong> Virtual International Authority File numbers used by global research libraries.</li>
</ul>

Here is how an AI assistant might propose authority links:
<pre><code>{
  "entity": "Peregrine Hopson",
  "role": "Governor of Nova Scotia (1752-1753)",
  "wikidata_qid": "Q7168019",
  "viaf_id": "104473859"
}</code></pre>

Always verify these identifiers in your browser before adding them to your TEI header or note tags. AI models occasionally mix up people with similar names, such as confusing Peregrine Hopson with his uncle or military colleagues.

**Takeaway:** AI models can draft Wikidata and VIAF identifiers for historical entities, but editors must confirm that each link points to the correct individual.

---

## **16 Content**

**Detecting Model Sycophancy and Leading Prompts**

Language models suffer from a behavioral flaw known as **sycophancy**. They tend to agree with whatever opinion or premise the user presents.

If you write a leading prompt:
<p style="background-color: #fef2f2; border-left: 4px solid #ef4444; padding: 12px; margin: 12px 0;">
<em>"Explain how Maud Lewis deliberately encoded anti-war political messages in this 1967 letter."</em>
</p>

The AI will not correct your mistaken assumption. Instead, it will draft an elaborate, fluent argument defending your false premise. It will invent reasons why Maud Lewis's mention of paint prices was a subtle critique of the Vietnam War.

To avoid sycophancy, always use **neutral, open-ended prompts**:
<p style="background-color: #f0fdf4; border-left: 4px solid #22c55e; padding: 12px; margin: 12px 0;">
<em>"Analyze the primary subject matter of this 1967 letter. Does the text contain political commentary, or does it focus on commercial sales and personal news? Cite exact lines."</em>
</p>

Neutral phrasing encourages the model to report evidence rather than flatter your preconceptions.

**Vocabulary.** *Sycophancy* — the tendency of AI models to agree with the user's suggestions and validate false premises rather than giving objective facts.

**Takeaway:** Write neutral prompts without leading assumptions to prevent AI models from generating flattering but false historical theories.

---

## **17 Content**

**Multi-Model Cross-Verification Pipelines**

A powerful technique for vetting commentary is **multi-model cross-verification**.

Instead of trusting a single AI model, you send the same structured prompt to two different models (for example, Claude and Gemini) or run the same model at two different temperature settings:
<ol>
  <li><strong>Generate Draft A:</strong> Prompt Model 1 for historical and philological notes.</li>
  <li><strong>Generate Draft B:</strong> Prompt Model 2 using the identical system prompt and document context.</li>
  <li><strong>Run Comparison:</strong> Compare the outputs side by side in VS Code.</li>
  <li><strong>Isolate Disagreements:</strong> Where both models agree on dates, names, and meanings, confidence is higher. Where they disagree, you have located a potential error or ambiguity.</li>
</ol>

This cross-check is especially helpful for historical dates and translations of archaic words. Discrepancies between models immediately highlight where human archive verification is needed.

**Takeaway:** Running prompts across two different models highlights factual disagreements and flags passages that require close human review.

---

## **18 Content**

**The Four-Step Forensic Fact-Checking Protocol**

When auditing an AI-generated commentary draft, follow this four-step forensic protocol:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px; text-align: left; width: 15%;">Step</th>
      <th style="padding: 8px; text-align: left; width: 25%;">Audit Focus</th>
      <th style="padding: 8px; text-align: left; width: 60%;">Action in VS Code</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Step 1</strong></td>
      <td style="padding: 8px;"><strong>Quotation Check</strong></td>
      <td style="padding: 8px;">Search your transcription file to confirm that every quoted string matches character for character.</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Step 2</strong></td>
      <td style="padding: 8px;"><strong>Entity Check</strong></td>
      <td style="padding: 8px;">Verify people, places, and organizations against authoritative biographical dictionaries and gazetteers.</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Step 3</strong></td>
      <td style="padding: 8px;"><strong>Citation Check</strong></td>
      <td style="padding: 8px;">Search library catalogs or digital repositories to verify that cited secondary works actually exist.</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Step 4</strong></td>
      <td style="padding: 8px;"><strong>Anchor Check</strong></td>
      <td style="padding: 8px;">Confirm that the target <code>xml:id</code> exists in your transcription and covers the intended span.</td>
    </tr>
  </tbody>
</table>

This protocol takes only a few minutes per note, but it ensures that your digital edition maintains high scholarly standards.

**Takeaway:** Follow a four-step audit protocol—checking quotations, entities, citations, and XML anchors—before accepting any AI note.

---

## **19 Content**

**Human-in-the-Loop (HITL) Validation Protocols**

In a digital edition, the AI is an assistant, not an author. The human editor bears full intellectual and ethical responsibility for the finished edition.

To manage this responsibility, adopt a formal **HITL decision framework**:
<ul>
  <li><strong style="color: #16a34a;">ACCEPT:</strong> The AI draft is factually accurate, beautifully written, properly anchored, and well cited. You adopt it with minimal copyediting.</li>
  <li><strong style="color: #2563eb;">REVISE:</strong> The draft contains good historical insight, but its tone is modern, its wording is wordy, or a minor date is wrong. You rewrite the text.</li>
  <li><strong style="color: #dc2626;">REJECT:</strong> The draft contains fabricated citations, hallucinated legal clauses, or anachronistic theories. You discard the note completely.</li>
  <li><strong style="color: #d97706;">FLAG:</strong> The draft makes an intriguing historical claim that you cannot verify immediately. You mark it for archive investigation.</li>
</ul>

Documenting your decisions ensures transparent editorial practice.

**Takeaway:** The human editor holds final authority, classifying every AI proposal as Accept, Revise, Reject, or Flag.

---

## **20 Content**

**The Commentary Ledger: COMMENTARY.md**

To track your editorial decisions, create a tracking ledger called `COMMENTARY.md` in your project folder.

A commentary ledger records the provenance and verification history of every note:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px; text-align: left;">Anchor ID</th>
      <th style="padding: 8px; text-align: left;">Category</th>
      <th style="padding: 8px; text-align: left;">Draft Origin</th>
      <th style="padding: 8px; text-align: left;">Decision</th>
      <th style="padding: 8px; text-align: left;">Audit Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><code>#seg_01</code></td>
      <td style="padding: 8px;">Historical</td>
      <td style="padding: 8px;">AI (Claude 3.5)</td>
      <td style="padding: 8px; color: #2563eb;"><strong>REVISE</strong></td>
      <td style="padding: 8px;">Corrected hallucinated 1792 date to 1791; trimmed wordiness.</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><code>#seg_02</code></td>
      <td style="padding: 8px;">Linguistic</td>
      <td style="padding: 8px;">Manual (Tuesday)</td>
      <td style="padding: 8px; color: #16a34a;"><strong>ACCEPT</strong></td>
      <td style="padding: 8px;">Verified against 1798 Academy dictionary.</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><code>#seg_03</code></td>
      <td style="padding: 8px;">Intertextual</td>
      <td style="padding: 8px;">Rule-based (Wed)</td>
      <td style="padding: 8px; color: #dc2626;"><strong>REJECT</strong></td>
      <td style="padding: 8px;">Spurious 3-gram match on common legal formula.</td>
    </tr>
  </tbody>
</table>

Maintaining this ledger fulfills your course requirement for transparent research. It shows your instructor exactly how you applied human expertise to evaluate computational suggestions.

**Takeaway:** The COMMENTARY.md ledger logs the origin, audit notes, and editorial decision for every note in your digital edition.

---

## **21 Content**

**Hands-On: Prompting for Ace's 1791 French Decree**

Let us apply these methods to our three student projects, starting with Ace's 1791 decree (*Loi relative à la fabrication des assignats*).

Open VS Code and open your AI chat window. Enter a disciplined system prompt:
<pre><code>Role: Assistant scholarly editor in 18th-century French digital history.
Source: 1791 National Assembly decree on assignats (Paris, Imprimerie Royale).
Target Span: "fabrication des assignats de 5 livres" (xml:id="seg_assig_05")
Task: Draft a concise historical commentary note explaining why 5-livre assignats were introduced in 1791.
Constraints:

- Maximum 80 words.
- Do NOT invent secondary citations.
- Explicitly mention the shift from large-denomination notes to small currency for daily wages.
- If citing a decree date, verify it against standard revolutionary calendars.</code></pre>

Review the generated response:
<ul>
  <li>Does it explain that early assignats were only issued in large sums (such as 1,000 livres), causing coin shortages?</li>
  <li>Does it describe how 5-livre notes were created to pay everyday workers and soldiers?</li>
  <li>Did the model fabricate any non-existent committee names?</li>
</ul>

**Takeaway:** Prompting for historical decrees requires specifying denominations, legislative context, and strict negative constraints against fake dates.

---

## **22 Content**

**Hands-On: Prompting for Olyvia's 1967 Maud Lewis Letter**

Next, let us prompt for Olyvia's project: Maud Lewis's February 1967 letter to Leonard Kinnear.

Enter this prompt in VS Code:
<pre><code>Role: Assistant editor in Canadian folk art and maritime social history.
Source: Maud Lewis, handwritten letter to Leonard Kinnear, Feb 1967 (Digby, NS).
Target Span: "The price of the paintings is \$6.00" (xml:id="seg_price_01")
Task: Draft a biographical and economic commentary note on Maud Lewis's pricing in 1967.
Constraints:

- Maximum 75 words.
- Explain her modest pricing despite growing national publicity following the 1965 CBC documentary.
- Note that Leonard Kinnear was a private correspondent in Moncton, New Brunswick.
- Do NOT claim she employed gallery agents or held formal exhibitions.</code></pre>

Examine the result:
<ul>
  <li>Did the model accurately mention her husband Everett's role in roadside sales?</li>
  <li>Did it mention the CBC *Telescope* broadcast from 1965 that made her famous across Canada?</li>
  <li>Did it keep the explanation grounded in regional Nova Scotia folk art?</li>
</ul>

**Takeaway:** Prompting for personal letters requires strict biographical guardrails to avoid confusing private correspondence with commercial gallery business.

---

## **23 Content**

**Hands-On: Prompting for Andromeda's 1752 Treaty**

Now let us prompt for Andromeda's document: the 1752 Peace and Friendship Treaty concluded at Halifax.

Enter this prompt:
<pre><code>Role: Assistant documentary editor in 18th-century Mi'kmaq-British treaty history.
Source: 1752 Peace and Friendship Treaty, Halifax, Nova Scotia.
Target Span: "free liberty of Hunting and Fishing as usual" (xml:id="seg_hunt_01")
Task: Draft a legal and historical commentary note explaining the meaning of this clause in 1752.
Constraints:

- Maximum 90 words.
- Mention Governor Peregrine Hopson and Chief Jean-Baptiste Cope.
- Connect to earlier agreements (1725 Dummer's Treaty).
- Note that this clause recognized ongoing Mi'kmaw resource harvesting rights.
- Do NOT cite modern court decisions or 21st-century legal cases.</code></pre>

Audit the response:
<ul>
  <li>Did the model describe the diplomatic relationship between Cope and Hopson accurately?</li>
  <li>Did it follow the negative constraint forbidding 21st-century legal references?</li>
  <li>Did it stay focused on the historical context of 1752?</li>
</ul>

**Takeaway:** Treaty commentary requires careful historical balancing, connecting 18th-century agreements to prior treaties while excluding modern legal anachronisms.

---

## **24 Content**

**Hands-On: The Hallucination Hunt (Catching Fabricated Sources)**

Now you will practice forensic editing. Below is an unvetted AI commentary draft containing three deliberate errors:
<p style="background-color: #fef2f2; border-left: 4px solid #ef4444; padding: 12px; margin: 12px 0;">
<em>"In the 1752 Halifax Treaty, Article 12 established a joint British-Mi'kmaw naval patrol on the Shubenacadie River. According to Dr. Ronald MacFarlane's 1984 monograph, 'Colonial Treaties of Acadia' (University of Toronto Press, p. 142), Chief Jean-Baptiste Cope personally delivered twenty beaver pelts to Halifax in January 1753 to purchase five British cannons."</em>
</p>

Find the three hallucinations:
<ol>
  <li><strong>The Article Number:</strong> The 1752 Treaty has only 8 articles. Article 12 is fictitious.</li>
  <li><strong>The Monograph and Citation:</strong> "Dr. Ronald MacFarlane" and his book *Colonial Treaties of Acadia* (1984) do not exist. The AI made up the author, book, publisher, and page.</li>
  <li><strong>The Cannon Purchase:</strong> Chief Cope never traded pelts for British cannons in January 1753. This claim is completely invented.</li>
</ol>

Spotting these fabrications proves why the human editor must never trust unverified citations.

**Takeaway:** Practicing hallucination hunts sharpens your editorial eye to catch fake articles, phantom books, and invented historical events.

---

## **25 Content**

**Hands-On: Vetting Tone, Grammar, and Style**

In addition to catching factual errors, you must vet the writing style of AI drafts. Language models often produce wordy, cliché-filled prose:
<ul>
  <li><strong>Eliminate Buzzwords:</strong> Remove empty phrases like "serves as a testament to," "rich tapestry," and "plays a pivotal role."</li>
  <li><strong>Prefer Active Voice:</strong> Change "The assignats were seen by the assembly as being" to "The assembly issued assignats to."</li>
  <li><strong>Cut Redundant Explanations:</strong> Keep your notes concise so readers can read them quickly without losing their place in the primary document.</li>
</ul>

Here is a before-and-after revision:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px; text-align: left; width: 50%;">Unvetted AI Draft</th>
      <th style="padding: 8px; text-align: left; width: 50%;">Vetted Human Revision</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px; background-color: #fff1f2;">This pivotal clause stands as a profound testament to the complex sociopolitical dynamics of 1752 Halifax, illuminating the ongoing negotiations.</td>
      <td style="padding: 8px; background-color: #f0fdf4;">Article 4 guaranteed Mi'kmaw hunting and fishing rights, continuing terms first established in the 1725 Dummer's Treaty.</td>
    </tr>
  </tbody>
</table>

Crisp, concise prose is the mark of good scholarship.

**Takeaway:** Vetting style means removing AI clichés and wordiness, producing clear and direct explanations for your readers.

---

## **26 Content**

**Hands-On: Converting Vetted AI Notes to TEI Standoff XML**

Once you have verified and polished an AI-drafted note, you encode it into your document's TEI `<standOff>` section.

Use the TEI tagging standards you mastered in Lesson 12.1:
<pre><code>&lt;standOff&gt;
  &lt;interpGrp type="commentary"&gt;
    &lt;note xml:id="note_assig_05"
          target="#seg_assig_05"
          type="historical"
          resp="#ai-draft"&gt;
      &lt;p&gt;The National Assembly issued five-livre assignats in May 1791 
      to relieve a severe shortage of small silver coinage for daily wages.&lt;/p&gt;
      &lt;bibl&gt;Archives Parlementaires, 26:145.&lt;/bibl&gt;
    &lt;/note&gt;
  &lt;/interpGrp&gt;
&lt;/standOff&gt;</code></pre>

Notice how we record responsibility:
<ul>
  <li><code>resp="#ai-draft"</code> records that the initial draft was machine-generated.</li>
  <li>In your TEI header, declare `<respStmt>` to credit the human editor who audited and verified the note.</li>
</ul>

This encoding preserves complete transparency while maintaining standard TEI P5 compliance.

**Takeaway:** Encode vetted notes into TEI standOff elements, using resp attributes to maintain transparent records of AI assistance and human editing.

---

## **27 Content**

**Hands-On: Serializing Vetted Commentary as W3C JSON-LD**

To make your vetted commentary available across the web, serialize it using the W3C Web Annotation Data Model you studied on Wednesday.

Here is a complete JSON-LD annotation for Olyvia's Maud Lewis note:
<pre><code>{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "id": "https://rels398.stfx.ca/annotations/maud_01",
  "type": "Annotation",
  "motivation": "commenting",
  "creator": {
    "id": "https://rels398.stfx.ca/editors/olyvia",
    "type": "Person",
    "name": "Olyvia"
  },
  "generator": {
    "type": "Software",
    "name": "Claude 3.5 Sonnet"
  },
  "target": {
    "source": "https://rels398.stfx.ca/texts/lewis_kinnear_1967.xml",
    "selector": {
      "type": "TextQuoteSelector",
      "exact": "The price of the paintings is \$6.00"
    }
  },
  "body": {
    "type": "TextualBody",
    "value": "Maud Lewis maintained modest prices of \$4 to \$6 for paintings sold from her Digby cottage during the late 1960s.",
    "format": "text/plain"
  }
}</code></pre>

Notice the clear distinction between `creator` (the student editor) and `generator` (the AI drafting tool). This format makes your commentary shareable across modern web viewers.

**Takeaway:** Serializing vetted notes as W3C JSON-LD distinguishes human creator from AI generator, enabling open web annotation sharing.

---

## **28 Content**

**The Three-Way Comparative Audit Matrix**

We have now tested three distinct methods for building scholarly commentary. Let us compare them across key editorial dimensions:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px; text-align: left; width: 22%;">Dimension</th>
      <th style="padding: 8px; text-align: left; width: 26%;">1. Manual (Tue)</th>
      <th style="padding: 8px; text-align: left; width: 26%;">2. Deterministic (Wed)</th>
      <th style="padding: 8px; text-align: left; width: 26%;">3. AI-Assisted (Fri)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Drafting Speed</strong></td>
      <td style="padding: 8px;">Slow (15-30 min/note)</td>
      <td style="padding: 8px;">Instantaneous</td>
      <td style="padding: 8px;">Very fast (seconds)</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Precision</strong></td>
      <td style="padding: 8px;">High (human verified)</td>
      <td style="padding: 8px;">Variable (spurious matches)</td>
      <td style="padding: 8px;">Medium (plausible errors)</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Recall</strong></td>
      <td style="padding: 8px;">Low (limited by memory)</td>
      <td style="padding: 8px;">High for exact phrases</td>
      <td style="padding: 8px;">High for thematic motifs</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Error Type</strong></td>
      <td style="padding: 8px;">Omission, human fatigue</td>
      <td style="padding: 8px;">Literalism, formula matches</td>
      <td style="padding: 8px;">Hallucination, anachronism</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Required Skill</strong></td>
      <td style="padding: 8px;">Philological expertise</td>
      <td style="padding: 8px;">Scripting and thresholds</td>
      <td style="padding: 8px;">Forensic fact-checking</td>
    </tr>
  </tbody>
</table>

This comparative matrix demonstrates that no single method is sufficient on its own. The best digital editions combine manual expertise, rule-based algorithms, and vetted AI assistance.

**Takeaway:** Combining manual close reading, rule-based text search, and vetted AI drafts creates a resilient and balanced commentary workflow.

---

## **29 Content**

**Ethical Transparency and Scholarly Provenance**

Using AI tools in academic research requires strict ethical transparency. Hiding AI assistance is academic dishonesty. Disclosing it clearly is good digital scholarship.

In your edition's TEI header or introductory paratext, include an **Editorial Method Statement**:
<p style="background-color: #f8fafc; border-left: 4px solid #64748b; padding: 12px; margin: 12px 0;">
<em>"Commentary notes in this digital edition were drafted using Claude 3.5 Sonnet as a research assistant. All generated claims, historical dates, and citations were audited, corrected, and verified against primary archival documents by the editor. Fabricated references and anachronistic interpretations were rejected. Final editorial responsibility rests entirely with the human editor."</em>
</p>

This statement clarifies that the AI served as a tool for initial drafting, while human expertise ensured truthfulness and historical accuracy.

**Takeaway:** Ethical scholarship requires full disclosure of AI drafting tools, documenting editorial audit procedures, and claiming final human responsibility.

---

## **30 Content**

**Synthesis: Completing the Commentary Cycle and Preparing for Assignment 12**

Congratulations! You have completed the Three-Step Comparative Cycle for Topic 12:
<ol>
  <li><strong>Lesson 12.1 (Manual):</strong> You authored historical, linguistic, and intertextual notes by hand and encoded them into TEI <code>&lt;standOff&gt;</code> and <code>&lt;interpGrp&gt;</code> elements.</li>
  <li><strong>Lesson 12.2 (Deterministic):</strong> You scanned for text reuse using stoplists, n-grams, and TF-IDF formulas, serializing notes as W3C JSON-LD.</li>
  <li><strong>Lesson 12.3 (AI-Assisted):</strong> You tested AI drafting assistants with negative constraints, audited outputs for hallucinations, and logged decisions in <code>COMMENTARY.md</code>.</li>
</ol>

**Assignment 12 Details:**
<ul>
  <li><strong>Due Date:</strong> Friday, December 4, at 11:00 PM.</li>
  <li><strong>Total Value:</strong> 80 points on Moodle.</li>
  <li><strong>Grading Rubric (4+3+3):</strong>
    <ol>
      <li><strong>Manual Ground Truth Precision (4 points / 40%):</strong> Accurate, scholarly commentary notes anchored to your primary transcription file.</li>
      <li><strong>Standoff TEI Markup Validity (3 points / 30%):</strong> Well-formed TEI XML using <code>&lt;standOff&gt;</code>, <code>&lt;interpGrp&gt;</code>, and <code>@target</code> attributes.</li>
      <li><strong>Comparative Audit Reflection (3 points / 30%):</strong> A completed <code>COMMENTARY.md</code> ledger comparing manual, rule-based, and AI-assisted notes with honest audit reflections.</li>
    </ol>
  </li>
</ul>

Submit your files on Moodle by December 4. Your commentary edition will serve as the foundation for our final publication modules!

**Takeaway:** Assignment 12 brings together manual precision, standoff TEI markup, and comparative audit reflections, due Friday, December 4 at 11:00 PM.
