# Lesson 11.3 — AI-Assisted Alignment and Gloss Generation

*RELS 398 / ENGL 398 · Topic 11: Alignment · Meeting #30 (Fri Nov 20)*

***Step 3 of the three-step cycle: AI-assisted.** Today you prompt AI models in VS Code to propose bilingual sentence links and four-line Leipzig glosses, auditing the results against your manual and deterministic files to produce reconciled scholarly editions.*

---

## **01 Content**

**Entering Step 3: AI-Assisted Text Alignment**

This week we have explored two very different methods for aligning historical texts. On Tuesday, you aligned sentences and authored Leipzig glosses completely by hand. On Wednesday, you tested automated length-based algorithms.

Today is Friday, Meeting #30. We arrive at Step 3 of our comparative cycle: **artificial intelligence**.

Large language models (such as Claude and Gemini) possess extensive training in multilingual grammar. Unlike simple length formulas, AI models understand syntax, vocabulary, and context. They can analyze historical French verbs, colonial treaty clauses, and informal English correspondence.

Today you will prompt an AI model directly inside VS Code to propose sentence alignments and four-line Leipzig glosses. Then you will conduct a rigorous audit against your Tuesday ground truth.

**Takeaway:** AI models bring semantic and grammatical understanding to alignment, offering powerful assistance that must be audited against human expertise.

---

## **02 Content**

**How AI Differs from Deterministic Algorithms**

It is important to understand how neural AI models differ from Wednesday's deterministic tools:

* **Deterministic Tools:** Follow rigid mathematical length formulas. They do not know what words mean. They never hallucinate, but they break when sentence structures shift.
* **AI Models:** Predict probable linguistic patterns based on vast multilingual training data. They understand grammar and semantics, but they can occasionally invent false facts.

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Method</th>
      <th style="width: 35%;">How It Operates</th>
      <th style="width: 40%;">Primary Risk</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Manual (Tuesday)</strong></td>
      <td>Human philological expertise.</td>
      <td>Slow; human fatigue on long texts.</td>
    </tr>
    <tr>
      <td><strong>Deterministic (Wed)</strong></td>
      <td>Character length formulas.</td>
      <td>Cascading domino errors on sentence splits.</td>
    </tr>
    <tr>
      <td><strong>AI-Assisted (Friday)</strong></td>
      <td>Neural pattern prediction.</td>
      <td>Hallucinated grammatical categories and tags.</td>
    </tr>
  </tbody>
</table>

Understanding these differences helps you choose the right tool for each editorial task.

**Takeaway:** While deterministic tools rely on fixed length calculations, AI models predict linguistic patterns and require supervision against hallucinations.

---

## **03 Content**

**AI Inside Visual Studio Code**

In RELS 398, you do not need to switch back and forth to an external web browser chat. You can interact with AI assistants directly inside Visual Studio Code.

Using AI in your editor offers major advantages:

* **Direct File Context:** The AI can see your open source XML and translation files simultaneously.
* **Inline Diff Views:** You can review AI suggestions in a split screen before accepting them into your document.
* **No File Copying:** You do not have to copy and paste sensitive historical files into third-party websites.

Having the AI embedded in your workspace makes the comparative audit fast and comfortable.

**Takeaway:** Working with AI directly inside VS Code allows you to review suggestions in split editor diff views without leaving your workspace.

---

## **04 Content**

**Prompt Engineering for Structured Alignment**

AI models are conversational by default. If you ask an AI casually to "align these sentences," it might write a chatty paragraph or invent its own informal formatting.

To produce scholarly data, you must write a **structured system prompt**:

* Define its exact role: "You are an expert computational philologist and TEI XML specialist."
* Specify the input files: Provide the exact source text with `xml:id` attributes.
* Define the output format: Demand a valid TEI `<linkGrp>` element with no conversational filler.
* State explicit constraints: Forbid the model from skipping sentences or inventing extra IDs.

Clear instructions produce clean, valid XML markup.

**From sentences to words.** Sentence links say which sentence translates which. Word links go one level down, inside a single sentence pair. Your source already has `<w>` elements from Module 8. For one pair:

1. Wrap the words of the target sentence in `<w>` too.
2. Give every `<w>` in both sentences an `xml:id` (`s1w1`, `s1w2` ... `t1w1`, `t1w2`).
3. Link the words in a second group, `<linkGrp type="word-alignment">`.

```xml
<linkGrp type="word-alignment">  <!-- La Nation fait les assignats. -->
  <link target="#s1w1 #t1w1"/>        <!-- La : The -->
  <link target="#s1w3 #t1w3"/>        <!-- fait : creates -->
  <link target="#s1w5 #t1w5 #t1w6"/>  <!-- assignats : paper currency (1:2) -->
</linkGrp>
```

Most word links are 1:1, but one word can link to two (*assignats* becomes *paper currency*), and some words link to nothing. Ask the AI to propose the word links, then check each one yourself.

**Takeaway:** Structured prompts with explicit roles, input boundaries, and output formats force AI models to generate clean, valid TEI markup.

---

## **05 Content**

**Prompting for Four-Line Leipzig Glosses**

Prompting for Leipzig interlinear glosses requires even stricter guidelines. The model must maintain perfect vertical column alignment across four distinct lines.

In your prompt, specify the four required tiers:

1. `Line 1`: Exact historical surface text (no modernized spelling).
2. `Line 2`: Morpheme breakdown with hyphens (`-`).
3. `Line 3`: Uppercase grammatical labels and lowercase lexical roots.
4. `Line 4`: Fluent English translation in quotation marks.

Add a strict formatting rule:

* "Every word in Line 1 must correspond to exactly one vertical column in Line 2 and Line 3."
* "Separate columns with multiple spaces so they align visually on screen."

Giving the AI a concrete template prevents shifted columns.

**Takeaway:** Prompting for Leipzig glosses requires demanding four synchronized tiers, standard uppercase tags, and preserved historical surface orthography.

---

## **06 Content**

**Negative Constraints: What to Forbid**

In prompt engineering, what you forbid is often more important than what you request. These restrictions are called **negative constraints**.

Essential negative constraints for linguistic alignment:

* **Do NOT modernize Line 1:** Forbid the AI from silently fixing historical spelling or removing archaic accents.
* **Do NOT use hyphens for portmanteaux:** Remind the AI to follow Rule 2 (use periods `.` for fused grammatical categories).
* **Do NOT hallucinate Latin or Greek roots:** Ensure the AI glosses the actual words on the page rather than classical roots from unrelated languages.
* **Do NOT skip difficult words:** The AI must gloss every historical token.

Negative constraints act like guardrails, keeping the AI focused on rigorous scholarship.

**Takeaway:** Negative constraints prevent the AI from modernizing historical spelling, hallucinating classical roots, or violating Leipzig punctuation rules.

---

## **07 Content**

**AI Failure Mode 1: Silent Modernization**

The most common mistake modern AI models make is **silent modernization**.

AI models are trained on billions of modern web pages. Consequently, they have a powerful bias toward contemporary spelling:

* In Ace's 1791 French decree, the AI might change 18th-century *décréta* to modern *décrète*.
* In Andromeda's 1752 treaty, it might modernize *agree-d* to *agreed* or *compleat* to *complete*.
* In Maud Lewis's letter, it might correct informal colloquialisms into stiff formal English.

In a digital critical edition, silent modernization is an editorial crime. Line 1 must always reflect the authentic historical witness.

**Takeaway:** AI models naturally bias toward modern spelling; editors must audit Line 1 to ensure historical orthography was not silently altered.

---

## **08 Content**

**AI Failure Mode 2: The Portmanteau Confusion (Rule 2)**

The second common AI error involves Leipzig Rule 2: confusing hyphens (`-`) and periods (`.`).

AI models frequently make this mistake:

* They see the French third-person singular past verb *parla*.
* Instead of writing `speak-3SG.PST` with periods, they write `speak-3-SG-PST` with hyphens.
* This implies that *3*, *SG*, and *PST* are three separate physical letters that can be cut apart with scissors.

In French and English inflected forms, these categories are fused together in a single ending. You must manually correct hyphens to periods in Line 3.

**Takeaway:** AI models often use hyphens instead of periods for fused grammatical features, violating Leipzig Rule 2.

---

## **09 Content**

**AI Failure Mode 3: Hallucinated Grammatical Tags**

Large language models are probabilistic text generators. When they encounter an unfamiliar historical word, they sometimes invent plausible-sounding grammatical labels.

Examples of **hallucinated tags**:

* Labeling an ordinary English preposition as an ancient Greek particle (`PRT.HES`).
* Inventing complex case labels (like `ABL.LOC.INSTR`) that do not exist in French.
* Mistaking a proper personal name for a Latin verb.

When auditing Line 3, check every uppercase label against the official Leipzig list. If a tag looks unfamiliar, verify it in the standard guidelines.

**Takeaway:** AI models occasionally invent plausible but non-standard grammatical abbreviations, requiring human verification against standard Leipzig lists.

---

## **10 Content**

**AI Failure Mode 4: Word Order and Pronoun Enclisis**

In historical languages, pronouns and clitics often attach to verbs in complex ways. In French, pronouns invert in questions and legal formulas (*dit-il*, *donnez-moi*).

When an AI attempts word-by-word alignment:

* It often stumbles on inverted pronouns.
* It may gloss the verb correctly but drop the attached pronoun completely.
* Or it might swap the order of the glosses, causing vertical columns to collapse.

Watching for attached pronouns and clitics is essential when auditing Romance and Indigenous language alignments.

**Takeaway:** Inverted pronouns, clitics, and irregular word orders frequently cause AI models to drop tokens or shift alignment columns.

---

## **11 Content**

**The Three-Way Comparative Audit**

Today you will assemble all three versions of your text alignment side by side:

1. **Version A (Tuesday Manual):** Your verified human gold standard.
2. **Version B (Wednesday Deterministic):** Length-based Gale-Church algorithm.
3. **Version C (Friday AI):** Neural model proposed links and glosses.

In VS Code, you can open three editor columns or compare files side by side. 

Comparing all three versions simultaneously provides deep insight. You will see where simple mathematics succeeded, where neural models excelled, and where human judgment was required to resolve difficult passages.

**Takeaway:** The three-way comparative audit compares manual, deterministic, and AI-assisted outputs side by side to reveal the unique profile of each method.

---

## **12 Content**

**What to Watch For: AI on Ace's 1791 French Decree**

What should Ace check when Claude or Gemini aligns and glosses the decree (*Loi relative à la fabrication des assignats*)? These are things to look for, not results.

* **Sentence alignment:** If Wednesday's length formula mispaired a long sentence that Ace's translation split in two, see whether the AI links it 1:2. Because it reads meaning rather than counting characters, it often does, but check every link.
* **Leipzig glossing:** Check grammatical gender tags, such as `F.SG` on *nationale*.
* **Silent modernization:** Check Line 1 letter by letter. An AI may quietly change a historical spelling or spacing, such as `L' Assemblée` to `L'Assemblée`.

Any such change must be undone, so that Line 1 stays faithful to the 1791 print witness.

**Takeaway:** AI models handle complex 1:2 sentence splits effortlessly, but they require oversight to preserve historical spacing and orthography.

---

## **13 Content**

**What to Watch For: AI on Andromeda's 1752 Treaty**

What should Andromeda check when the AI aligns and glosses the treaty? These are things to look for, not results.

* **Sentence alignment:** Does the AI match every numbered article? Does it handle the formal preamble, where Wednesday's length formula may have slipped?
* **Linguistic glossing:** Check the modal *shall* (obligation or future?) and passive participles such as *renew-ed* (`renew-PST.PTCP`).
* **Invented roots:** An AI may gloss an archaic spelling with a made-up Latin root. Line 3 should use plain English roots (*agree*, *treaty*, *peace*).

**Takeaway:** Check that the AI's glosses of formal treaty language are accurate and that its roots stay in plain English.

---

## **14 Content**

**What to Watch For: AI on Olyvia's Maud Lewis Letters**

What should Olyvia check when the AI aligns Maud Lewis's 1967 letter with its regularized (or French) version? These are things to look for, not results.

* **Informal syntax:** Does the AI keep the sentence boundaries Olyvia chose, or does it merge or split them where periods are missing?
* **Regional expressions:** Does it render Maritime phrasing faithfully, or flatten it?
* **Over-correction:** An AI may try to "correct" Maud's grammar in Line 1. Any such change must be rejected: Line 1 records what she wrote.

**Takeaway:** Protect the authentic voice of personal correspondence from AI over-correction.

---

## **15 Content**

**Measuring AI Performance: A Three-Way Scorecard**

To complete your comparative audit, build a summary scorecard in your notes:

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Evaluation Metric</th>
      <th style="width: 25%;">Manual (Tue)</th>
      <th style="width: 25%;">Deterministic (Wed)</th>
      <th style="width: 25%;">AI-Assisted (Fri)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Sentence Precision</strong></td>
      <td>Reference (by definition)</td>
      <td>Your number</td>
      <td>Your number</td>
    </tr>
    <tr>
      <td><strong>Execution Speed</strong></td>
      <td>Your time</td>
      <td>Your time</td>
      <td>Your time</td>
    </tr>
    <tr>
      <td><strong>Grammar Depth</strong></td>
      <td>High (Careful glosses)</td>
      <td>None (Length only)</td>
      <td>High (Needs Rule 2 audit)</td>
    </tr>
    <tr>
      <td><strong>Orthographic Fidelity</strong></td>
      <td>Your check</td>
      <td>Your check</td>
      <td>Your check</td>
    </tr>
  </tbody>
</table>

Fill in this scorecard with your own measurements. Precision for the manual alignment is the reference the others are scored against, so it is not a measurement. Expect the length formula to slip on split sentences and the AI to modernize spelling, but report what you actually found.

**Takeaway:** A comparative scorecard documents precision, speed, depth, and orthographic fidelity across all three alignment approaches.

---

## **16 Content**

**Synthesizing the Reconciled Alignment File**

Now you will create your final alignment deliverable: `alignment_reconciled.xml`.

How to synthesize your reconciled file:

1. Start with your clean TEI document structure.
2. Adopt the sentence pairings that were verified across both manual and AI runs.
3. Where the AI proposed a better handling of a 1:2 split, adopt the AI's link.
4. Where the AI hallucinated or modernized spelling, enforce your manual ground truth.
5. Ensure all `xml:id` targets and `#` hash marks are valid and well-formed.

This synthesized file represents the best of human expertise and computational assistance.

**Takeaway:** The reconciled alignment file merges the speed of AI suggestions with the rigorous fidelity of human ground truth.

---

## **17 Content**

**Synthesizing Reconciled Leipzig Glosses**

Next, create your final gloss deliverable: `gloss_reconciled.xml`.

Steps for the reconciled gloss:

* Select three rich, representative sentences from your primary witness.
* Check Line 1 letter-by-letter against your facsimile image to guarantee 100% historical authenticity.
* Verify Line 2 morpheme hyphens.
* Verify Line 3 uppercase grammatical labels and ensure periods are used for portmanteaux.
* Polish Line 4 to ensure the modern English translation is natural, fluent, and placed in quotation marks.

Your completed gloss stands as a permanent contribution to digital philology.

**Takeaway:** The reconciled gloss file delivers three verified, publication-ready Leipzig glosses that combine historical accuracy with linguistic precision.

---

## **18 Content**

**TEI Header Attribution for AI Assistance**

Scholarly integrity requires total transparency about computational tools. If an AI model assisted in generating alignments or glosses, that assistance must be documented in the `<teiHeader>`.

In your TEI header, add a `<change>` record inside `<revisionDesc>`:

```xml
<revisionDesc>
  <change when="2026-11-20" who="#ken" resp="#ai">
    Sentence alignment audited against Gale-Church and Claude AI. 
    AI suggestions adopted for 1:2 splits; historical surface text verified by hand.
  </change>
</revisionDesc>
```

You can also use the `@resp` attribute on individual `<linkGrp>` or `<link>` elements (`resp="#ai"` or `resp="#manual"`).

Transparency builds trust with your readers and peers.

**Takeaway:** Transparent TEI header documentation explicitly records AI assistance, detailing which suggestions were adopted and who verified the text.

---

## **19 Content**

**Validating Reconciled XML in VS Code**

Before saving your final files, run a complete validation check inside Visual Studio Code:

1. Open `alignment_reconciled.xml` and `gloss_reconciled.xml`.
2. Inspect the bottom status bar for XML errors. Ensure it displays "No Problems."
3. Run `xmllint --noout` in your VS Code terminal to verify well-formed syntax.
4. Verify that every sentence ID inside `<standOff>` points to an existing `<s xml:id="...">` tag.

A document that fails validation cannot be rendered or published. Taking two minutes to validate guarantees your work is sound.

**Takeaway:** Always run xmllint and editor validation checks to ensure reconciled alignment files are well-formed and schema-compliant.

---

## **20 Content**

**Documenting Methodology in ALIGNMENT.md**

Every scholarly edition includes an editorial methodology report. In your project repository, open `ALIGNMENT.md` and complete the final section:

Include the following sections:

* **The Corpus:** Description of your primary witness and parallel translation.
* **The Manual Baseline:** Summary of your Tuesday 10-sentence hand alignment.
* **Deterministic Evaluation:** Gale-Church accuracy, precision, recall, and abbreviation traps.
* **AI Evaluation:** AI model used, prompt design, strengths, and failure modes (modernization, Rule 2 errors).
* **Editorial Synthesis:** Rationale for your final reconciled decisions.

This report documents your intellectual journey across the three-step cycle.

**Takeaway:** The ALIGNMENT.md report provides a complete scholarly record of your corpus, methodology, metrics, and editorial synthesis.

---

## **21 Content**

**Building Bilingual Reading Interfaces**

Why did we do all this alignment work? What does it look like to the public reader?

When your edition is published on the web:

* A reader can view your historical witness and English translation in parallel columns.
* Clicking any historical sentence highlights the corresponding English sentence instantly.
* Hovering over a glossed word reveals its Leipzig grammatical breakdown and dictionary definition.
* Scholars can search for specific grammatical forms (such as all occurrences of past subjunctive verbs) across the bilingual corpus.

Alignment transforms static manuscripts into dynamic, interactive reading environments.

**Takeaway:** Sentence alignment and interlinear glossing power dynamic web interfaces with sentence highlighting, word hovers, and cross-lingual search.

---

## **22 Content**

**Connecting Alignment to the Semester Portfolio**

Let us look at how Module 11 fits into your overall term portfolio:

* **Module 2:** Codicological cataloguing and TEI header.
* **Module 3:** Facsimile images and IIIF canvases.
* **Module 4 & 5:** Diplomatic transcription and AI reconciliation.
* **Module 6:** Regularization and normalized reading text.
* **Module 7:** CSS and HTML rendering views.
* **Module 8 & 9:** Linguistic lemmatization and named entity markup.
* **Module 10:** Git consolidation, CI/CD, and peer review.
* **Module 11 (Today):** Bilingual translation alignment and Leipzig glossing.

Your digital edition is now nearly complete! You have constructed an edition with deep scholarly metadata and bilingual accessibility.

**Takeaway:** Module 11 provides the bilingual translation and linguistic glossing layer of your comprehensive digital edition portfolio.

---

## **23 Content**

**Ethical Considerations in AI Philology**

Using AI in historical textual scholarship introduces important ethical responsibilities:

* **Attribution:** Never pretend AI output was produced entirely by your own hand.
* **Historical Accuracy:** Never allow an AI model to smooth over historical prejudice, difficult syntax, or archaic vocabulary.
* **Indigenous Contexts:** In treaty scholarship, translations carry real legal and political weight. AI models must never alter treaty meanings without indigenous consultation.
* **Preserving Student Voice:** Use AI as an editorial assistant, not as a replacement for your own critical thinking.

Ethical scholarship prioritizes historical truth and transparent human accountability.

**Takeaway:** Ethical digital scholarship requires honest attribution, preservation of difficult historical truths, and active human accountability.

---

## **24 Content**

**Git Hygiene: Staging and Committing Module 11**

With your alignment files reconciled and verified, it is time to record your work in Git.

Open your VS Code terminal and run clean, disciplined Git commands:

1. Check repository status: `git status`
2. Stage your Module 11 deliverables: `git add alignment_reconciled.xml gloss_reconciled.xml ALIGNMENT.md`
3. Commit with a meaningful commit message: `git commit -m "Module 11: complete three-way alignment audit and synthesize reconciled TEI files"`
4. Push to your GitHub remote: `git push origin main`

Disciplined version control ensures your hard work is backed up and safe on the cloud.

**Takeaway:** Stage and commit your reconciled alignment files with descriptive commit messages, pushing your progress safely to GitHub.

---

## **25 Content**

**Common Novice Pitfalls in AI Alignment**

As you finalize your work today, beware of these four common AI pitfalls:

1. **Accepting AI Modernization:** Failing to notice that the AI changed an 18th-century spelling into modern English in Line 1.
2. **Ignoring Leipzig Rule 2:** Leaving hyphens in Line 3 where periods are required for fused grammatical categories.
3. **Conversational AI Chatter in XML:** Forgetting to remove introductory AI text like *"Here is your TEI XML file:"* before saving.
4. **Unbalanced Line Counts:** Submitting a gloss where Line 1 has four words but Line 2 has five words.

A careful final pass in VS Code will catch all four errors.

**Takeaway:** Common AI alignment errors include silent spelling modernization, Rule 2 hyphen confusion, leftover conversational text, and unbalanced columns.

---

## **26 Content**

**The Role of Human Judgment in Digital Philology**

This week has demonstrated a profound truth of digital humanities scholarship.

No algorithm—whether a 1993 mathematical formula or a 2026 neural network—can replace human historical understanding:

* An algorithm can count letters.
* An AI can predict likely grammar tags.
* Only a human scholar understands the cultural context, emotional nuance, and political consequences of historical writing.

Computers provide speed and scale. Humans provide judgment, empathy, and truth.

**Takeaway:** Computational tools provide speed and scale, but human scholars provide the critical judgment and historical empathy that define scholarly editions.

---

## **27 Content**

**Reviewing the Week 11 Milestone Checklist**

Before leaving class today, verify that you have completed all deliverables for Module 11:

* [x] **Tuesday:** Hand-aligned 10 sentences (`alignment_manual.xml`) and authored 3 Leipzig glosses (`gloss_manual.xml`).
* [x] **Wednesday:** Ran automated Gale-Church alignment and audited precision/recall (`alignment_deterministic.xml`).
* [x] **Friday:** Prompted AI in VS Code, conducted three-way comparative audit, and synthesized `alignment_reconciled.xml` and `gloss_reconciled.xml`.
* [x] **Methodology Report:** Documented metrics and reflection in `ALIGNMENT.md`.
* [x] **Validation:** All XML files pass `xmllint --noout` with zero errors.

Checking off these items confirms you have mastered bilingual text alignment.

**Takeaway:** Verifying all five milestone deliverables ensures your repository meets professional standards for bilingual digital scholarship.

---

## **28 Content**

**Preparing for Next Week: Module 12 (Scholarly Commentary)**

Next week, we move into **Module 12: Scholarly Commentary and Annotation**.

Now that your text is transcribed, regularized, lemmatized, aligned, and glossed, you are ready to write scholarly commentary:

* Explaining historical context, people, and legal debates.
* Linking passages to external historical archives and encyclopedias.
* Encoding scholarly annotations using TEI `<note>`, `<annotation>`, and the Open Annotation Data Model.

Your edition is growing from a raw manuscript into a rich, interactive educational resource.

**Takeaway:** Module 12 builds upon text alignment by introducing scholarly commentary notes and linked historical annotations.

---

## **29 Content**

**Peer Review and Classroom Discussion**

Take five minutes to look at your neighbor's screen in MULH 3032:

* Compare how Ace's French decree handles gender agreement compared to Andromeda's English treaty verbs.
* Look at Olyvia's Maud Lewis glosses and discuss how vernacular handwriting challenges AI translation models.
* Share one interesting AI mistake you caught during today's lab.

Discussing computational errors with your peers transforms mistakes into valuable learning moments.

**Takeaway:** Sharing alignment challenges and AI failure modes with peers deepens your collective understanding of digital philology.

---

## **30 Content**

**Conclusion: Mastery of the Three-Step Cycle**

Congratulations on completing Module 11!

This week you achieved a major milestone:

* You practiced manual scholarship, experiencing the intellectual discipline of word-by-word glossing.
* You explored deterministic algorithms, demystifying how computers calculate sentence correspondence.
* You supervised generative AI, discovering its incredible linguistic power and learning to catch its subtle errors.

You have proven that you can harness modern technology while upholding the highest standards of historical scholarship.

**Takeaway:** Mastering the Three-Step Comparative Cycle empowers you to lead digital humanities research with computational skill and critical human judgment.
