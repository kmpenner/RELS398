# Lesson 9.3 — AI-Assisted Entity Tagging, Entity Linking, and Comparative Audit

*RELS 398 / ENGL 398 · Topic 9: Named Entities · Meeting #25 (Fri Nov 6)*

***Step 3 of the three-step cycle: AI-assisted synthesis.** Today you prompt AI models in VS Code to tag and link historical entities, execute a three-way comparative audit, and finalize Assignment 9.*

---

## **01 Content**

**The AI Revolution in Philology: Flexible Models for Historical Prose**

Over the past two meetings, you explored two different ways to find historical entities. On Tuesday, you established human ground truth through close reading and authority research. On Wednesday, you ran deterministic natural language processing pipelines using SpaCy and gazetteer lists. You saw that while automated models process archives in seconds, rigid statistical rules struggle with archaic spelling and complex syntax.

Today, we complete our three-step comparative cycle by introducing generative artificial intelligence. Large language models (LLMs) operate fundamentally differently from traditional statistical sequence taggers. Instead of analyzing text through isolated token windows, generative models process rich, multi-sentence semantic context.

Generative AI understands historical rhetorical patterns and informal prose with remarkable flexibility. But it brings severe hazards: non-deterministic output, prompt drift, and fabricated facts. Today, you will command an AI model in VS Code, audit its predictions against human ground truth, and synthesize your final portfolio for Assignment 9.

**Vocabulary.** *Generative AI* — Large language models that generate structured text, code, or annotations based on contextual prompts. *Context Window* — The span of text that a language model can process and analyze simultaneously.

**Takeaway:** Generative AI brings contextual flexibility to historical prose but requires rigorous human auditing to prevent hallucinations.

---

## **02 Content**

**Why LLMs Excel at Historical Names: Semantic and Syntactic Depth**

Traditional sequence taggers like SpaCy evaluate each word primarily through local grammatical transitions. If an unfamiliar word appears, the statistical chain fractures.

Large language models are trained on billions of parameters across historical books, encyclopedias, and diverse web corpora. They understand that an eighteenth-century phrase like *in the twenty-sixth year of His Majesty's reign* functions as a calendar expression, even though it contains no numbers.

Furthermore, LLMs handle informal language with ease. When Maud Lewis refers casually to *Everett*, an AI model recognizes from the surrounding letter that Everett is her husband. It connects the casual mention to his full identity without needing an explicit honorific title like *Mr.* or *Governor*.

**Vocabulary.** *Semantic Depth* — An algorithm's ability to understand overarching meaning rather than superficial word patterns. *Implicit Entity* — A person or place referred to indirectly through kinship words, pronouns, or titles.

**Takeaway:** Large language models interpret complex historical syntax and informal names by analyzing broad semantic meaning.

---

## **03 Content**

**The Hallucination Hazard: Inventing Plausible Fiction**

The greatest strength of generative AI is also its greatest danger: its fluency. Language models are probabilistic token predictors, not factual databases.

When an AI model does not know an authority identifier, it does not stop and admit defeat. Instead, it predicts what a plausible identifier ought to look like. If you ask an unconstrained model to find the Wikidata Q-identifier for a minor French clerk or a local colonial settler, it will effortlessly invent a fake number like `Q9847125`.

To the untrained eye, the generated XML looks flawless: tags match, attributes are present, and the format validates. But the identifier points to an unrelated modern topic, or to a web page that does not exist. Digital humanists must never accept AI output without verifying external links.

**Vocabulary.** *Model Hallucination* — When an AI model generates plausible-sounding but completely fabricated facts or identifiers. *Fluent Falsehood* — Text that appears grammatically correct and convincing but is factually untrue.

**Takeaway:** Language models invent plausible-sounding authority identifiers when unconstrained; editors must verify all external links.

---

## **04 Content**

**Prompt Engineering: Zero-Shot vs. Few-Shot Annotation**

The quality of AI-generated markup depends entirely on prompt engineering. How you instruct the model determines whether you receive scholarly markup or useless fiction.

In **zero-shot prompting**, you give the model an instruction with no examples: *Tag the named entities in this eighteenth-century text*. The model guesses at your conventions, invents custom XML tags, and modernizes spelling without your permission.

In **few-shot prompting**, you provide explicit persona instructions, strict rules, and two or three concrete input-output examples. By showing the model exactly how you want tags, IDs, and attributes formatted, you lock its output into valid TEI XML.

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 0.5rem; text-align: left;">Prompting Strategy</th>
      <th style="padding: 0.5rem; text-align: left;">Input Structure</th>
      <th style="padding: 0.5rem; text-align: left;">Typical Failure Modes</th>
      <th style="padding: 0.5rem; text-align: left;">Scholarly Suitability</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Zero-Shot</td>
      <td style="padding: 0.5rem;">Bare instruction without examples</td>
      <td style="padding: 0.5rem;">Custom tags, modernizes spelling, invents URIs</td>
      <td style="padding: 0.5rem;">Unsuitable for academic editions</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem;">Few-Shot</td>
      <td style="padding: 0.5rem;">Persona + strict rules + 2-3 exemplars</td>
      <td style="padding: 0.5rem;">Minor boundary slips, prompt drift on long texts</td>
      <td style="padding: 0.5rem;">Standard for digital scholarship</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Zero-Shot Prompting* — Giving an AI model a task without providing demonstration examples. *Few-Shot Prompting* — Providing an AI model with several concrete input-output examples to guide its behavior.

**Takeaway:** Few-shot prompting with concrete examples forces language models to follow strict TEI schema guidelines.

---

## **05 Content**

**Injecting Editorial Policies: Positive and Negative Constraints**

To achieve reliable results, your system prompt must incorporate the rules from your `ENTITY_POLICIES.md` file.

Scholarly prompts require two types of constraints:

1. **Positive Constraints:** Explicit rules stating what the model must do (e.g., *Use TEI persName, placeName, orgName, and date tags; normalize dates using the when attribute in YYYY-MM-DD format*).

2. **Negative Constraints:** Explicit prohibitions stating what the model must never do (e.g., *Do NOT alter historical spelling inside tags; do NOT invent authority identifiers; do NOT include conversational preamble*).

Negative constraints are essential. They prevent the model from modernizing eighteenth-century spellings like *shew'd* or adding polite commentary before the XML.

**Vocabulary.** *Positive Constraint* — An instruction that directs an algorithm on what actions or formats it must produce. *Negative Constraint* — A rule forbidding an algorithm from performing specific actions, such as altering text.

**Takeaway:** Combining positive guidelines with negative constraints keeps AI models focused on strict schema conformity.

---

## **06 Content**

**Automating AI Prompts in VS Code: ai_entity_parser.py**

In today's lab, you will not copy and paste text into a public web chat. Instead, you will execute a Python script in VS Code called `ai_entity_parser.py`.

The script reads your manuscript excerpt, packages it with your system prompt and few-shot examples, and sends it to the language model API. It captures the generated XML, validates its structure, and saves it to `ground_truth_entities_ai.xml`.

Automating the interaction through code gives you an exact, reproducible record of your parameters, temperature settings, and model versions. Every step in your editorial workflow is documented in your repository.

**Vocabulary.** *API Script* — A programmatic script that communicates with a remote server or model automatically. *Reproducibility* — The scientific principle that an experiment can be run by others and produce the same results.

**Takeaway:** Automating AI queries through Python scripts creates an exact, reproducible audit trail in your project repository.

---

## **07 Content**

**The TEI XML Schema Quality Gate**

Before you compare AI predictions against your human baseline, the generated XML must pass two strict quality gates.

The first gate is **well-formedness and validation**. Every opening tag must have a matching closing tag. Attribute names must be spelled correctly (`ref=`, not `link=`). Date formats must conform to ISO 8601.

The second gate is **textual integrity**. The AI must not alter a single character of your manuscript witness. If the model modernized *décrétoit* to *décrétait* or expanded abbreviations without using `<choice>`, the file fails the quality gate immediately.

Open the Problems panel in VS Code (`Ctrl+Shift+M`) to confirm that `ground_truth_entities_ai.xml` validates to zero errors.

**Vocabulary.** *Quality Gate* — A mandatory validation test that a file must pass before being accepted into a pipeline. *Textual Integrity* — Preserving the exact characters of the primary manuscript without unauthorized alterations.

**Takeaway:** AI-generated XML must pass schema validation and preserve original spelling before being audited.

---

## **08 Content**

**The Token Alignment Gate: Matching Entity Spans**

Before calculating accuracy scores, you must verify **token alignment** between your manual and AI files.

An automated script cannot calculate precision if the two files disagree on word boundaries. For example, if your manual file tagged `Major Jean Baptiste Cope` as twenty characters and the AI split the title into separate elements, the comparison script must align those spans.

Ensure that both files contain the exact same continuous passage. In `ai_entity_parser.py`, you can run an automated alignment checker that verifies word counts before running the comparative evaluation.

**Vocabulary.** *Span Alignment* — Matching start and end word positions between two different annotation files. *Alignment Gate* — A verification step ensuring that text spans match before mathematical scoring begins.

**Takeaway:** Verifying span alignment between manual and AI files ensures that mathematical scoring is fair and accurate.

---

## **09 Content**

**The Three-Way Comparative Diff in VS Code**

Now comes the heart of our module: the **Three-Way Comparative Audit**. You will compare all three passes side by side in Visual Studio Code:

1. **Manual Ground Truth (`ground_truth_entities_manual.xml`):** The human baseline (Tuesday).

2. **Deterministic NLP (`ner_baseline.xml`):** The SpaCy sequence model (Wednesday).

3. **AI-Assisted Model (`ground_truth_entities_ai.xml`):** The LLM prompt output (Friday).

Open VS Code split editors to view the files simultaneously, or run split diffs:
```bash
code --diff ground_truth_entities_manual.xml ground_truth_entities_ai.xml
```

You can now observe exactly where the deterministic tool stumbled, where the AI succeeded, and where both failed.

**Vocabulary.** *Three-Way Audit* — A comparative study evaluating manual, deterministic, and AI methods on the same passage. *Split Editor* — A screen layout displaying multiple files side by side in an editor.

**Takeaway:** The three-way audit compares manual, deterministic, and AI annotations side by side to reveal their relative strengths.

---

## **10 Content**

**Scoring the AI Pass: Precision, Recall, and F1-Score**

Just as you measured SpaCy's accuracy on Wednesday, you will now calculate mathematical scores for the AI model.

Count your True Positives, False Positives, and False Negatives:

* **Precision:** How many of the AI's entity tags matched your manual ground truth?

* **Recall:** Did the AI discover all twenty entities that you identified by hand?

* **F1-Score:** What is the balanced harmonic score of the AI model?

Compare these numbers directly against Wednesday's SpaCy scores. In most historical documents, generative AI achieves higher Recall than SpaCy because it recognizes unusual syntax, but it may have lower Precision due to over-tagging common nouns.

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 0.5rem; text-align: left;">Method</th>
      <th style="padding: 0.5rem; text-align: left;">Precision (%)</th>
      <th style="padding: 0.5rem; text-align: left;">Recall (%)</th>
      <th style="padding: 0.5rem; text-align: left;">F1-Score (%)</th>
      <th style="padding: 0.5rem; text-align: left;">Primary Failure Mode</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Manual Baseline (9.1)</td>
      <td style="padding: 0.5rem;">100.0%</td>
      <td style="padding: 0.5rem;">100.0%</td>
      <td style="padding: 0.5rem;">100.0%</td>
      <td style="padding: 0.5rem;">Slow, labor-intensive craft</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Deterministic NLP (9.2)</td>
      <td style="padding: 0.5rem;">78.5%</td>
      <td style="padding: 0.5rem;">65.0%</td>
      <td style="padding: 0.5rem;">71.1%</td>
      <td style="padding: 0.5rem;">OOV spelling, toponym blindness</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem;">Generative AI (9.3)</td>
      <td style="padding: 0.5rem;">88.2%</td>
      <td style="padding: 0.5rem;">90.0%</td>
      <td style="padding: 0.5rem;">89.1%</td>
      <td style="padding: 0.5rem;">Over-tagging, invented URIs</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Comparative Metrics* — Using identical mathematical formulas to benchmark two different technologies against a single human baseline. *Over-Tagging* — Tagging ordinary capitalized nouns as entities when they are merely general concepts.

**Takeaway:** Computing comparative scores reveals that AI models often achieve higher recall than rule-based taggers but require auditing for precision.

---

## **11 Content**

**Building the Three-Way Discrepancy Matrix**

In your capstone report, `ENTITY_AUDIT.md`, you will compile a comprehensive comparative matrix across all twenty mentions.

The table features five columns:

1. **Mention:** The raw text string in the manuscript.

2. **Manual Ground Truth (9.1):** Your verified human tag and authority link.

3. **Deterministic NLP (9.2):** What SpaCy predicted.

4. **Generative AI (9.3):** What the LLM predicted.

5. **Scholarly Analysis:** Which method succeeded and why.

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 0.5rem; text-align: left;">Mention</th>
      <th style="padding: 0.5rem; text-align: left;">Manual Truth (9.1)</th>
      <th style="padding: 0.5rem; text-align: left;">NLP (9.2)</th>
      <th style="padding: 0.5rem; text-align: left;">AI (9.3)</th>
      <th style="padding: 0.5rem; text-align: left;">Analysis</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Major Cope</td>
      <td style="padding: 0.5rem;"><code>persName (dcb:cope)</code></td>
      <td style="padding: 0.5rem;"><code>Cope (PER)</code></td>
      <td style="padding: 0.5rem;"><code>persName (dcb:cope)</code></td>
      <td style="padding: 0.5rem;">AI included title and linked DCB correctly</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Chigabenakady</td>
      <td style="padding: 0.5rem;"><code>placeName (geonames)</code></td>
      <td style="padding: 0.5rem;">[Missed]</td>
      <td style="padding: 0.5rem;"><code>placeName</code></td>
      <td style="padding: 0.5rem;">AI recognized place; prompt prevented fake ID</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem;">Assemblée</td>
      <td style="padding: 0.5rem;"><code>orgName (wikidata)</code></td>
      <td style="padding: 0.5rem;"><code>LOC</code></td>
      <td style="padding: 0.5rem;"><code>orgName</code></td>
      <td style="padding: 0.5rem;">AI resolved organization type cleanly</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Discrepancy Matrix* — A multi-column table displaying side-by-side annotations across three distinct workflows. *Scholarly Analysis* — Evaluating the theoretical and practical reasons behind divergent machine readings.

**Takeaway:** The three-way discrepancy matrix provides a clear, side-by-side comparison of human, statistical, and AI annotations.

---

## **12 Content**

**Cohort Synthesis A: Ace and French Revolutionary Entities**

Let us look at how the three methods performed on Ace's 1791 French Revolutionary decree.

On Wednesday, SpaCy's French sequence model struggled with elided articles and legislative committees. It tagged `l'Assemblée nationale` as a location and completely overlooked minor signers like `Dejoly`.

The generative AI model performed significantly better. Informed by prompt context about 1791 constitutional France, the AI recognized that the National Assembly was a legislative body (`orgName`). It separated the elided article `l'` from the entity span. However, the AI attempted to invent a French national archive identifier for `Dejoly` that did not exist. Ace's manual ground truth was essential to catch the hallucination.

**Vocabulary.** *Contextual Recovery* — When an AI model uses broad historical understanding to identify an entity that rigid taggers missed. *Fabricated Identifier* — A fake archive number invented by an AI model to satisfy a prompt request.

**Takeaway:** In French revolutionary texts, AI models resolve complex institutional bodies but tend to invent fake archive identifiers.

---

## **13 Content**

**Cohort Synthesis B: Olyvia and Maud Lewis's Folk Correspondence**

In Olyvia's Maud Lewis letter, the three-way comparison highlights the difference between rigid models and contextual models on informal writing.

SpaCy struggled with casual first names and rural place names. It tagged *Everett* with low confidence and missed *Marshalltown* entirely because the hamlet was absent from modern training corpora.

The generative AI model easily identified *Everett* as a person and *Marshalltown* as a place. Because LLMs have ingested regional Canadian culture and art history, the model recognized Maud Lewis's rural home. However, the AI tended to over-tag common objects, attempting to tag *paintings* or *cards* as corporate works. Olyvia's manual policy restrained the model's over-enthusiasm.

**Vocabulary.** *Cultural Ingestion* — An AI model's ability to recall regional artistic or cultural facts from its training data. *Over-Generalization* — Tagging ordinary everyday items as formal cultural titles.

**Takeaway:** In informal correspondence, AI models recognize rural places and first names but tend to over-tag common descriptive words.

---

## **14 Content**

**Cohort Synthesis C: Andromeda and the 1752 Treaty**

In Andromeda's 1752 Treaty, the three-way comparison demonstrates the high stakes of diplomatic and Indigenous sovereignty.

SpaCy suffered from toponym blindness, completely skipping the Indigenous district of *Chigabenakady*. It truncated *Major Jean Baptiste Cope* into a bare surname and confused sovereign councils with physical buildings.

The generative AI model succeeded in capturing full composite titles: `Major Jean Baptiste Cope, Chief Sachem`. Guided by prompt rules, it recognized *Chigabenakady* as a geographic place. However, when asked to link the place, the AI attempted to attach a modern colonial municipality in Ontario with a similar name. Andromeda's manual ground truth rescued the historical Mi'kmaw territory from automated geographic displacement.

**Vocabulary.** *Geographic Displacement* — When an automated tool attaches a historical place to a modern municipality in the wrong province. *Composite Title* — An entity mention that combines multiple honorary, military, and sovereign titles.

**Takeaway:** In colonial treaties, AI models capture complex composite titles but require human oversight to prevent geographic displacement.

---

## **15 Content**

**The Four Discrepancy Classes in ENTITY_AUDIT.md**

In your audit report, classify every point of disagreement into our four-part course taxonomy:


1. **Boundary Mismatches:** Differences in where an entity span starts or ends (e.g., dropping or keeping official titles).

2. **Category Disagreements:** Classifying an entity as a place (`placeName`) versus an organization (`orgName`).

3. **Authority Linking Errors:** Attaching an incorrect Wikidata QID, or inventing a fake URI where no record exists.

4. **Historical Orthography Failures:** OOV spelling slips or archaic punctuation that caused a model to miss an entity.

Discuss at least three specific case studies in detail in your report, explaining what each error reveals about digital tools.

**Vocabulary.** *Boundary Mismatch* — When two annotation passes identify the same entity but disagree on its starting or ending words. *Category Disagreement* — When annotators agree on a name span but disagree on its semantic entity class.

**Takeaway:** Classifying errors into boundary, category, linking, and spelling failures provides a structured framework for critical reflection.

---

## **16 Content**

**Auditing Entity Links: Detecting Invented Q-Identifiers**

Auditing authority links requires active verification, not passive reading. You must test every URI generated by the model.

Open each link in your web browser. If the AI generated `ref="wikidata:Q7732"`, verify that the link opens the Wikidata page for King Louis XVI. If the link returns an HTTP 404 error, or opens an article about a Swedish municipality, the model hallucinated.

When you discover an invented identifier, document it prominently in your audit report. Explain why the model invented the link and how your manual ground truth protected your edition from data corruption.

**Vocabulary.** *Link Verification* — Testing an automated hyperlink in a web browser to ensure it points to the correct historical entity. *HTTP 404* — The standard web error code indicating that a requested page or identifier does not exist.

**Takeaway:** Editors must click and verify every automated authority link in a browser to catch hallucinated identifiers.

---

## **17 Content**

**The Fallacy of Pure Automation**

Our three-step comparative cycle leads to a vital scholarly conclusion: the fallacy of pure automation.

Software companies often market automated language models as total replacements for human editorial labor. They claim that an algorithm can parse, tag, and publish historical archives in minutes without human supervision.

Our experiments prove that pure automation produces silent, corrupting errors across historical collections. An un-audited algorithm quietly drops Indigenous place names, mislinks historical leaders to modern celebrities, and fabricates authority records. Speed without human verification produces digital noise, not scholarship.

**Vocabulary.** *Pure Automation* — Relying entirely on software pipelines without human editorial verification. *Silent Error* — An automated mistake that passes computer checks without throwing an error, escaping notice.

**Takeaway:** Relying entirely on automated tools produces silent errors that corrupt historical truth across archival collections.

---

## **18 Content**

**The Human-in-the-Loop Scholarly Model**

If pure automation fails, what is the proper role of computational tools in digital editing? The answer is the **Human-in-the-Loop** model.

In a human-in-the-loop workflow, computational tools and generative models act as rapid first-pass draft assistants. They scan thousands of words, extract initial candidate spans, and suggest possible authority links in seconds.

The human philologist remains in control. The human scholar establishes ground truth, writes editorial rules, audits machine predictions, resolves edge cases, and verifies historical truth. This model combines computational speed with gold-standard scholarly rigor.

**Vocabulary.** *Human-in-the-Loop* — A workflow where automated systems generate draft annotations that are audited and verified by human experts. *First-Pass Assistant* — Using an algorithm to produce an initial draft that human editors refine.

**Takeaway:** The human-in-the-loop model combines computer processing speed with human philological rigor and historical judgment.

---

## **19 Content**

**Assignment 9 Overview: The Named-Entity Markup Portfolio**

Today's lab provides the materials for **Assignment: Module 9 (Named-Entity Markup)**, due tonight, Friday, November 6, by 11:00 PM.

Your assignment brings together the work of all three meetings into a unified digital portfolio in your git repository.

Your portfolio must contain:

1. `ENTITY_POLICIES.md`: Your declared authority registries, granularity policy, and date rules.

2. `ground_truth_entities_manual.xml`: Your 20-entity human gold standard (Tuesday).

3. `ner_baseline.xml` and `NER_BENCHMARK.md`: Your deterministic SpaCy baseline and scores (Wednesday).

4. `ground_truth_entities_ai.xml`: Your AI-assisted TEI markup (Friday).

5. `ENTITY_AUDIT.md`: Your capstone three-way comparative audit report.

**Vocabulary.** *Entity Portfolio* — The complete set of policy files, XML transcripts, and audit reports that document your entity markup. *Capstone Report* — The final synthesis report that evaluates all experimental findings across a module.

**Takeaway:** Assignment 9 bundles your policy rules, manual XML, SpaCy baseline, AI markup, and three-way audit into a final portfolio.

---

## **20 Content**

**The 4 + 3 + 3 Grading Rubric (80 Moodle Points)**

Assignment 9 is evaluated on our standard course rubric: 4 + 3 + 3 raw points, scaled to 80 points in the Moodle gradebook.

The three dimensions evaluate your scholarship across the three-step cycle:

* **Dimension 1: Manual Ground Truth Precision (4 pts / 32 moodle pts):** Accurate identification of twenty entities, correct category typing, valid date normalization, and rigorous authority linking (including verified absences).

* **Dimension 2: TEI Entity Markup Validity (3 pts / 24 moodle pts):** Well-formed XML, schema conformity, correct attribute usage (`ref=`, `when=`), unique IDs, and span alignment across all files.

* **Dimension 3: Comparative Error Analysis (3 pts / 24 moodle pts):** Mathematical accuracy scoring (Precision, Recall, F1), complete discrepancy matrix, and insightful 300–500 word methodological reflection.

**Vocabulary.** *Rubric Dimension* — A specific grading criterion evaluating a core academic skill or technical deliverable. *Scale Weight* — Converting raw rubric points into course gradebook values.

**Takeaway:** Assignment 9 is evaluated on manual precision (4 pts), XML validity (3 pts), and comparative error analysis (3 pts).

---

## **21 Content**

**Rubric Dimension 1: Manual Precision and Policy Rigor**

To earn full marks on Dimension 1, your manual ground truth must reflect exemplary philological craft.

Every entity mention in your twenty-item table must be verified against historical evidence. Personal names must be checked against biographical dictionaries. Place names must be verified in gazetteers. Dates must be correctly calculated into ISO 8601 timestamps.

Your `ENTITY_POLICIES.md` must clearly define your rules for compound names and regional registries. If an entity lacks a public record, you must document the search evidence to claim a verified absence. Fabricated links or unverified guesses lose marks on this dimension.

**Vocabulary.** *Policy Rigor* — Strictly adhering to declared editorial rules across an entire document. *Search Evidence* — Documenting the databases and catalogues queried during authority research.

**Takeaway:** Dimension 1 awards full marks for verified authority links, accurate date calculations, and documented absence policies.

---

## **22 Content**

**Rubric Dimension 2: TEI XML Validity and Token Alignment**

Dimension 2 evaluates your technical XML craft and schema compliance.

Your XML files (`ground_truth_entities_manual.xml` and `ground_truth_entities_ai.xml`) must validate to zero errors against the course schema in VS Code. All tags must close properly, and element names must match TEI P5 Chapter 13.

Crucially, your entity tags must respect token boundaries. Leading articles should remain outside the tags unless part of a proper title. Punctuation must not be accidentally swallowed inside place or person tags. Clean, valid XML earns full marks on this dimension.

**Vocabulary.** *Schema Compliance* — An XML document that satisfies all syntax and structural constraints of its schema. *Punctuation Hygiene* — Keeping commas, periods, and quotation marks outside entity tags.

**Takeaway:** Dimension 2 awards full marks for schema-valid XML, clean token boundaries, and proper attribute syntax.

---

## **23 Content**

**Rubric Dimension 3: Comparative Analysis and Critical Synthesis**

Dimension 3 evaluates your critical reflection and computational understanding.

Your capstone report, `ENTITY_AUDIT.md`, must present mathematically accurate Precision, Recall, and F1 scores for both SpaCy and the AI model. Your discrepancy matrix must categorize every disagreement cleanly.

The core of Dimension 3 is your 300–500 word reflection. You must explain *why* the tools behaved differently. Discuss what your findings reveal about the limits of automation and the necessity of human ground truth in digital textual scholarship.

**Vocabulary.** *Critical Synthesis* — Combining experimental data, technical observations, and historical context into an insightful essay. *Methodological Reflection* — Analyzing how digital tools shape our understanding of historical evidence.

**Takeaway:** Dimension 3 awards full marks for mathematically sound scoring, clear error diagnosis, and insightful reflection.

---

## **24 Content**

**Common Pitfalls to Avoid in Assignment 9**

Review your portfolio against these four common student traps before submitting:


1. **Submitting Broken XML:** Always run schema validation in VS Code before committing. An unclosed tag or invalid attribute breaks the entire file.

2. **Missing Authority Links:** Every entity tag must carry an authoritative `@ref` attribute or point to a local header record.

3. **Empty Error Diagnoses:** In your discrepancy table, do not simply write "machine was wrong." Explain *why* it failed (e.g., OOV spelling, title truncation, type confusion).

4. **Vague Reflection:** Avoid generic statements like "AI is very smart but makes mistakes." Ground your essay in specific words from your project witness.

**Vocabulary.** *Submission Audit* — A final systematic review of all project files against rubric requirements before submission. *Vague Critique* — Unsubstantiated opinions that lack specific textual or empirical evidence.

**Takeaway:** Avoid common pitfalls by validating XML, checking authority links, and writing specific error diagnoses.

---

## **25 Content**

**Authoring the Methodological Reflection in ENTITY_AUDIT.md**

Your reflection in `ENTITY_AUDIT.md` should read like a published scholarly note in digital humanities.

Structure your essay in three short, focused paragraphs:

1. **The Machine's Blind Spots:** Discuss where automated models stumbled on your specific document (e.g., archaic French imperfect verbs, Maritime nicknames, or Indigenous toponyms).

2. **The Power and Peril of AI:** Contrast SpaCy's rigid sequence modeling with the LLM's fluent contextual understanding, highlighting any subtle hallucinations you caught.

3. **The Role of the Digital Editor:** Conclude with a strong argument defending the irreplaceable role of human scholarship in the era of artificial intelligence.

**Vocabulary.** *Scholarly Note* — A concise, formal academic essay discussing a specific methodological or historical problem. *Editorial Defense* — An evidence-based argument articulating the value of human historical scholarship.

**Takeaway:** A well-structured three-paragraph reflection articulates the methodological lessons of your three-way entity audit.

---

## **26 Content**

**Packaging Your Repository for Submission**

Before submitting your assignment on Moodle, verify that your project repository is completely organized and clean.

Ensure that all five core files reside in their proper locations on the `main` branch. Open your terminal in VS Code and verify git status:
```bash
git status
```

Your working tree should report: `nothing to commit, working tree clean`. If any uncommitted changes appear, stage and commit them with a descriptive commit message. A tidy repository ensures that instructors can inspect your code and XML without friction.

**Vocabulary.** *Repository Hygiene* — Maintaining clean, organized project folders without stray temporary files or uncommitted changes. *Descriptive Commit* — A git commit message that explains exactly what changes were made and why.

**Takeaway:** Verifying that your git repository is clean and properly organized ensures a smooth submission process on Moodle.

---

## **27 Content**

**Submitting on Moodle: The Assignment Form**

Assignment 9 is submitted through the official Moodle assignment activity: **Assignment: Module 9 (Named-Entity Markup)**.

The assignment activity accepts two submission methods:

1. **Repository Link:** A direct web link to your public or private GitHub repository branch.

2. **ZIP Bundle:** A compressed archive containing your five project files (`ENTITY_POLICIES.md`, manual XML, baseline XML, AI XML, and `ENTITY_AUDIT.md`).

Review your submission in the Moodle preview before clicking final submit. The assignment deadline is tonight, Friday, November 6, at 11:00 PM.

**Vocabulary.** *Online Submission* — Submitting digital project links or compressed archives directly through a learning management system. *Submission Due Date* — The formal deadline by which student work must be recorded in the system.

**Takeaway:** Submit your repository link or ZIP bundle through Moodle Assignment 9 before tonight's 11:00 PM deadline.

---

## **28 Content**

**The Bigger Picture: From Words to Historical Networks**

Take a moment to appreciate how far your digital edition has developed.

In Week 4, your text was a raw diplomatic transcription. In Week 6, you normalized its spelling. In Week 8, you gave each word a part of speech and dictionary lemma. Today, in Week 9, you connected your text to the global web of historical people, places, and organizations.

Your edition is no longer an isolated document sitting on a hard drive. It is an interconnected node in global historical scholarship. Researchers studying Revolutionary Paris, Maritime folk art, or eighteenth-century Mi'kmaw diplomacy can find your document and link their data to yours.

**Vocabulary.** *Interconnected Node* — A digital edition whose authority links connect it directly into global semantic networks. *Scholarly Network* — The worldwide web of linked open data connecting archives, libraries, and museums.

**Takeaway:** Entity markup transforms an isolated transcription into an interconnected node within global scholarly networks.

---

## **29 Content**

**Looking Ahead: Module 10 and Textual Consolidation**

Next week, we move into **Module 10: Consolidation**.

Over the first nine modules, you learned and practiced every individual stage of the digital textual pipeline: cataloguing, imaging, transcription, reconciliation, normalization, rendering, lemmatization, and entity markup.

In Module 10, you will consolidate these diverse markup layers into a unified, publication-ready TEI master edition. You will resolve overlapping tags, streamline your `teiHeader`, and prepare your complete digital edition for final scholarly publication.

**Vocabulary.** *Textual Consolidation* — Merging and reconciling multiple markup layers into a unified, master digital edition. *Master Edition* — The definitive, fully encoded digital text that combines all analytical annotations.

**Takeaway:** Module 10 consolidates all nine digital markup layers into a unified, publication-ready master edition.

---

## **30 Content**

**The Final Stage Gate: Committing Your Completed Portfolio**

You have reached the final stage gate for Topic 9: Named Entities.

You mastered the three-step comparative cycle: establishing human ground truth, testing deterministic NLP pipelines, and auditing generative artificial intelligence. You held automated models accountable to historical facts and proved the necessity of human scholarship.

Stage and commit all remaining files to your repository on the `main` branch:
```bash
git add ai_entity_parser.py ground_truth_entities_ai.xml ENTITY_AUDIT.md
git commit -m "Week 9 Step 3: AI entity markup and three-way comparative audit"
```

Submit your portfolio on Moodle before 11:00 PM tonight. Congratulations on completing Module 9!

**Vocabulary.** *Portfolio Completion* — Successfully delivering all required policy, baseline, and audit files for a course module. *Final Stage Gate* — The concluding milestone that locks in all project deliverables for grading.

**Takeaway:** Committing your AI parser, markup, and capstone audit completes Module 9 and locks in your final portfolio for submission.

---
