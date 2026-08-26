# Lesson 12.3 — AI-Assisted Commentary Drafting, Intertextual Verification, and Philological Vetting

*RELS 398 / ENGL 398 · Topic 12: Commentary · Meeting #33 (Fri Nov 27)*

***Step 3 of the three-step cycle: AI-assisted.** Today you evaluate Large Language Models in drafting scholarly commentary notes, identifying semantic allusions, verifying citations, vetting philological outputs against hallucinations and anachronisms, and establishing Human-in-the-Loop (HITL) validation protocols. **The Interlinear Glossing & Translation Alignment Assignments are due today.***

---

## **01 Content**

**The Third Step: Generative AI in the Commentary Lifecycle**

Over the past two class meetings, you established the foundational spectrum of digital commentary construction. In Lesson 12.1, you engaged in the meticulous, manual labor of traditional philology: parsing Greek morphology, identifying historical realia, discovering intertextual echoes, and encoding the resulting insights into TEI P5 stand-off XML markup (`<standOff>`, `<interpGrp>`, `<note>`, `<ptr>`). In Lesson 12.2, you transitioned to deterministic computational discovery, using Tesserae's frequency-weighted n-gram algorithms to scan corpora at scale and formalizing web-native annotations using the W3C Web Annotation Data Model (WADM) in JSON-LD. Today, in Lesson 12.3, we take the third step of our comparative cycle: evaluating **Generative Artificial Intelligence and Large Language Models (LLMs)** as collaborative commentary assistants (Tafdrup et al., 2026).

The introduction of transformer-based foundation models represents a dramatic shift in digital textual scholarship. Whereas deterministic algorithms like Tesserae operate strictly on surface-level lexical tokens—matching identical lemmas and calculating phrase densities—Large Language Models possess dense semantic representations trained on hundreds of billions of words across ancient and modern languages. An LLM can recognize complex thematic motifs, parse dialectal syntax, synthesize historical encyclopedias, and draft fluent, multi-paragraph scholarly explanations in seconds (Lou et al., 2025).

However, this generative power introduces severe epistemological hazards that threaten the integrity of critical editions. Because language models operate probabilistically by predicting the next plausible token rather than querying verified relational databases, they are prone to fabricating primary source citations, generating anachronistic theological interpretations, and smoothing over genuine philological difficulties. The scholarly editor cannot treat AI as an autonomous authority; it must be harnessed within a disciplined **Human-in-the-Loop (HITL)** architecture where every computational proposal is systematically vetted against primary witnesses and historical evidence (Draxler et al., 2024; Tafdrup et al., 2026).

Today's lesson equips you with the theoretical insights, technical architectures, and practical evaluation protocols necessary to use generative AI responsibly. You will learn how to structure rigorous system prompts, enforce machine-readable JSON schemas, deploy multi-model cross-verification pipelines, and conduct forensic hallucination audits on AI-generated commentary notes for 1 Thessalonians 2:1–8.

**Vocabulary.** *Generative AI* — artificial intelligence systems, particularly large language models, capable of generating novel text, code, or data based on probabilistic patterns learned during training. *Human-in-the-Loop (HITL)* — an editorial and computational workflow where human expert judgment is required at critical decision points to validate, correct, or reject automated outputs. *Epistemological hazard* — a structural risk within a research methodology that threatens the validity, truth-value, or reliability of scholarly knowledge.

**The takeaway for this page:** Generative AI provides rapid drafting and semantic synthesis for digital commentary, but its probabilistic nature requires strict Human-in-the-Loop verification to maintain scholarly integrity.

---

## **02 Content**

**From Keyword Matching to Semantic Inference**

To appreciate the distinct contribution of generative AI to commentary authoring, we must understand the fundamental difference between **lexical matching** and **semantic inference**. Throughout the history of computational philology, text analysis tools have relied primarily on deterministic string matching, regular expressions, and lemmatized concordances. As you observed in Lesson 12.2 with Tesserae, if an ancient author reuses a concept using completely different vocabulary—such as replacing a noun with an evocative synonym or crafting a structural parody without verbatim borrowing—deterministic algorithms fail to register the connection (Coffee et al., 2012).

Large Language Models transcend these lexical constraints by operating within high-dimensional vector spaces where words, phrases, and entire passages are mapped according to contextual semantic meaning. When an LLM analyzes an ancient text, it does not merely count matching characters; it processes the syntactic dependencies, rhetorical structures, and associative semantic fields of the discourse.

Consider how these two computational paradigms approach an intertextual allusion in 1 Thessalonians 2:7, where Paul describes his apostolic conduct using the maternal metaphor of a nurse gently caring for her children (ὡς ἐὰν τροφὸς θάλπῃ τὰ ἑαυτῆς τέκνα):

| Analytical Dimension | Deterministic Algorithm (Tesserae / TF-IDF) | Generative LLM (Transformer Semantic Inference) |
| --- | --- | --- |
| Detection Mechanism | Exact lemma overlap ($k \ge 2$) + phrase density | Contextual neural embeddings + relational attention heads |
| Synonymic Flexibility | None; blind to synonyms unless manually aliased | High; recognizes conceptual equivalence across distinct lexemes |
| Thematic Recognition | Fails completely if no shared vocabulary exists | High; identifies pastoral, maternal, and philosophical motifs |
| Output Format | Quantitative similarity score ($S$) and raw token spans | Natural language prose explaining the literary and cultural connection |
| Primary Limitation | High false-positive rate on formulaic vocabulary | Hallucination of non-existent parallels and citations |

Because neural networks model deep semantic relationships, an LLM can recognize that Paul's maternal imagery in 1 Thess 2:7 evokes philosophical discourses on the ideal teacher in Hellenistic moral philosophy (such as Dio Chrysostom's *Discourses* or Plutarch's *Moralia*), even when the specific vocabulary diverges from the Septuagint or classical epics. Generative models thus serve as powerful **hypothesis generators**, surfacing latent thematic parallels that elude deterministic concordance searches (Tafdrup et al., 2026).

Yet, this semantic flexibility is a double-edged sword. While deterministic tools produce predictable, reproducible false positives that can be filtered via mathematical thresholds, LLMs produce convincing, highly articulate arguments for connections that may be entirely spurious. The digital editor must maintain a sharp boundary between genuine historical intertextuality and associative model hallucination.

**Vocabulary.** *Semantic inference* — the ability of a computational model to deduce meaning, conceptual relationships, and contextual implications beyond surface-level lexical tokens. *High-dimensional vector space* — a mathematical space where semantic concepts are represented as numerical vectors, positioning words with similar meanings in close proximity. *Associative hallucination* — a model error where conceptually related ideas are falsely asserted to have a direct historical or textual connection.

**The takeaway for this page:** LLMs transcend deterministic keyword matching by inferring semantic, thematic, and conceptual relationships, functioning as powerful hypothesis generators for textual allusions.

---

## **03 Content**

**The Capabilities of Foundation Models in Philological Commentary**

When properly guided by structured prompts and scholarly constraints, modern foundation models can assist digital editors across all four core categories of commentary established in Lesson 12.1. Rather than serving as a replacement for human erudition, the model functions as an automated research assistant that accelerates initial drafting, organizes reference citations, and formats data into standard schemas (Lou et al., 2025).

In the **philological and morphosyntactic** domain, LLMs can rapidly parse complex grammatical constructions, identify rare dialectal forms, and explain unusual syntactical relationships (such as genitive absolutes, articular infinitives, or deliberative subjunctives). When supplied with an unpointed or highly contracted transcription, the model can propose normalized lexical entries, cite standard grammar sections (e.g., Smyth for Classical Greek or Blass-Debrunner-Funk for Hellenistic Greek), and highlight potential scribal ambiguities (Francese, 2014).

In the **historical, geographic, and prosopographical** domain, models excel at entity extraction and historical contextualization. An LLM can scan a raw Greek or Latin text, identify all toponyms, ethnonyms, and personal names, and provide concise encyclopedic summaries drawing upon massive historical corpora. When integrated with external APIs, the model can propose alignments to persistent Linked Open Data identifiers, such as Pleiades URIs for ancient places and VIAF or Wikidata IDs for historical figures (Simon et al., 2017).

| Commentary Category | Key LLM Assistance Capabilities | Example Prompt Application for 1 Thess 2:1–8 |
| --- | --- | --- |
| Philological / Morphosyntax | Identifies parsing, unusual idioms, and dialect shifts | Unpacks the intensive syntax of αὐτοὶ γὰρ οἴδατε and the voice of ἐπαρρησιασάμεθα |
| Historical / Realia | Contextualizes institutions, places, and historical figures | Summarizes Roman civic administration and Philippian colonial mistreatment (v. 2) |
| Intertextual / Citational | Identifies potential Hebrew Bible and Hellenistic parallels | Connects εὐαγγέλιον θεοῦ (v. 2) to Septuagint Isaiah and Imperial cult inscriptions |
| Structural / Rhetorical | Outlines chiastic structures, *apologia*, and discourse shifts | Analyzes Paul's self-defense against charges of flattery (κολακεία) and greed (πλεονεξία) |

In the **structural, rhetorical, and thematic** domain, LLMs demonstrate an impressive capacity to analyze discourse structure. They can trace the development of an author's argument, identify classical rhetorical figures (such as *antithesis*, *chiasmus*, *captatio benevolentiae*, or *parrhesia*), and summarize overarching theological or philosophical motifs. By generating rapid structural overviews, the model helps the editor frame individual lexical notes within the larger rhetorical trajectory of the work (Bartalesi et al., 2018).

Despite these vast capabilities, every automated output remains a provisional draft. The editor must treat every claim—whether a grammatical rule, a historical fact, or a literary parallel—as an unverified assertion that requires rigorous philological vetting before it is admitted into a permanent edition.

**Vocabulary.** *Foundation model* — a large-scale artificial intelligence model trained on broad, multimodal data at scale that can be adapted to a wide range of downstream specialized tasks. *Discourse structure* — the organizational pattern of a text that governs how arguments, narrative transitions, and rhetorical strategies unfold across sentences and paragraphs. *Entity extraction* — the automated identification of named entities (persons, locations, organizations, dates) within unstructured text.

**The takeaway for this page:** Foundation models can assist across philological, historical, intertextual, and rhetorical commentary categories, acting as versatile drafting engines for human editors.

---

## **04 Content**

**The Epistemological Hazard: Citation Hallucination**

The single most dangerous failure mode of generative AI in scholarly editing is **citation hallucination**. In everyday conversational applications, a minor factual error by an AI model may cause minor confusion; in digital textual scholarship, however, a fabricated citation, a non-existent manuscript reference, or a distorted primary source quotation corrupts the historical record and destroys the epistemic authority of the critical edition (Tafdrup et al., 2026).

Hallucination is not an accidental software glitch that can be easily patched; it is an inherent property of autoregressive language generation. LLMs do not consult an indexed internal database of verified truths when generating text. Instead, they calculate transition probabilities across tokens based on statistical associations learned from training data. When a model is asked to provide an ancient parallel for a specific Greek phrase, it generates tokens that *look* like legitimate scholarly citations—producing realistic author names, believable work titles, and plausible book and section numbers (Lou et al., 2025).

Consider the mechanics of how a hallucination occurs during prompt execution:

```
THE MECHANICS OF SCHOLARLY HALLUCINATION:
  Input Prompt: "Cite a parallel for 1 Thess 2:2 (ἐπαρρησιασάμεθα) in Philo of Alexandria."
  LLM Generation Process:
    Token 1: "Philo,"           (P = 0.94 - High statistical confidence)
    Token 2: "Quod_Omnis_Probus" (P = 0.81 - Plausible treatise on virtue and speech)
    Token 3: "Liber_Sit,"       (P = 0.88 - Completes treatise title)
    Token 4: "§"                (P = 0.92 - Standard citation syntax)
    Token 5: "47"               (P = 0.45 - Probabilistic guess for section number)
  Scholarly Audit Result:
    Section 47 discusses Spartan endurance; the word ἐπαρρησιασάμεθα does NOT appear.
    VERDICT: FABRICATED CITATION (HALLUCINATION).
```

Scholarly hallucinations typically fall into three distinct classifications:

- **Phantom Citations:** The model invents an entire reference out of whole cloth, citing a treatise or fragment that does not exist in the surviving classical or patristic corpus.
- **Misattributed Citations:** The cited work and author are authentic, and the quoted Greek or Latin text is genuine, but the quotation actually belongs to a completely different work or author.
- **Numerical Drift:** The author, work, and textual passage exist, but the specific book, chapter, verse, or Stephanus/Bekker pagination is incorrect (e.g., citing Plato *Republic* 347a instead of 359d).

The insidious nature of these hallucinations lies in their high degree of plausibility. Because the model has absorbed the formal conventions of classical scholarship, its fabricated notes mimic the exact tone, Latinate abbreviations (*cf.*, *ibid.*, *passim*), and bibliographic formats of peer-reviewed commentaries. Without exhaustive, line-by-line verification against primary texts, these phantom references slip effortlessly past casual readers (Tafdrup et al., 2026).

**Vocabulary.** *Citation hallucination* — the generation by an AI model of plausible-sounding but entirely fabricated bibliographic references, primary source passages, or chapter and verse numbers. *Autoregressive generation* — a text generation process where each subsequent token is predicted based on the statistical probability distribution of preceding tokens. *Numerical drift* — an error where an AI model cites an authentic text but provides incorrect numerical locators (pages, verses, sections).

**The takeaway for this page:** LLMs generate plausible but fabricated citations through probabilistic token prediction; every AI-generated reference must be forensically verified against primary corpora.

---

## **05 Content**

**The *Grundtvig's Works* Case Study: Auditing LLM Biblical Citations**

The practical dangers and quantitative realities of AI-assisted commentary were rigorously demonstrated in a landmark empirical study conducted on the Danish Digital Scholarly Edition of *Grundtvig's Works* (*Grundtvigs Værker*, GV) by Jonathan Tafdrup, Kim Bjerring Svendsen, and Katrine Frøkjaer Baunvig (Tafdrup et al., 2026).

N.F.S. Grundtvig (1783–1872) was a foundational Danish author whose massive corpus spans theology, poetry, history, and education. Grundtvig's writing is extraordinarily intertextual, dense with thousands of implicit biblical references woven directly into complex poetic prose. The editorial team at Aarhus University had previously spent over a decade manually identifying and verifying 10,980 biblical references across 158,000 pages of commentary—creating an unprecedented, human-curated **ground-truth dataset** against which AI performance could be scientifically benchmarked (Tafdrup et al., 2026).

The researchers tasked OpenAI's ChatGPT-4 with identifying all biblical references in selected Grundtvig texts and compared the model's output directly against the manual ground truth:

| Evaluation Metric in GV Study | Empirical Result | Scholarly Consequence |
| --- | --- | --- |
| True Positives ($TP$) | Identified major, explicit citations | Successfully recovered obvious scriptural quotations |
| False Positives ($FP$) | Massive generation of irrelevant verses | Flagged common words (e.g., "bread", "light") as biblical quotes |
| False Negatives ($FN$) | Missed complex, subtle allusions | Failed when Grundtvig paraphrased or adapted Hebrew motifs |
| Hallucination Rate | Substantial | Invented chapter/verse numbers not matching Danish text |
| Overall Editorial Precision | Low without human filtering | Direct ingestion would corrupt the critical apparatus |

The study revealed a critical insight: ChatGPT-4 suffered from severe **associative over-generation**. When the model encountered a common theological word such as "Jesus," "temple," or "covenant," it frequently generated a specific biblical reference (e.g., "Cites Matthew 26:28") even when Grundtvig was using the word in a generic, non-allusive cultural sense. Conversely, when Grundtvig executed a brilliant, multi-layered poetic inversion of an Old Testament prophetic passage without using verbatim keywords, the model failed to detect the reference entirely (Tafdrup et al., 2026).

The authors concluded that while LLMs provide immense value for preliminary exploratory reading, deploying them without human oversight is epistemologically fatal. Generative models cannot serve as autonomous annotators; they function effectively only when integrated into a strict **Human-in-the-Loop curation pipeline** where scholars use AI to surface potential leads while exercising definitive veto power over every proposed link (Tafdrup et al., 2026).

**Vocabulary.** *Ground-truth dataset* — an independently verified, highly accurate dataset used as a gold standard to train, test, and benchmark computational algorithms. *Associative over-generation* — a model error where common vocabulary triggers false-positive allusions to well-known texts simply due to topical association. *Curated pipeline* — a structured workflow combining computational generation with mandatory human review and authorization.

**The takeaway for this page:** The *Grundtvig's Works* study proved that LLMs suffer from associative over-generation and citation errors, demonstrating that automated commentary requires strict human ground-truth vetting.

---

## **06 Content**

**Historical Anachronism and Conceptual Flattening**

Beyond outright citation fabrication, generative AI poses a subtle but pervasive hermeneutic hazard: **historical anachronism** and **conceptual flattening**. Anachronism occurs when an AI model projects contemporary, post-Enlightenment, or late-theological definitions onto ancient vocabulary, fundamentally distorting the historical reality of the primary source (Tafdrup et al., 2026).

Language models are trained overwhelmingly on modern internet text, contemporary academic articles, and digitized 19th- and 20th-century theological treatises. Consequently, the model's latent vector space reflects modern semantic distributions. When asked to draft an explanatory note on an ancient Greek or Latin term, the model naturally gravitates toward the most frequent modern interpretations in its training weights, ignoring historical distance and evolutionary semantic shifts.

Consider the severe anachronisms that arise when an LLM drafts commentary notes for core vocabulary in 1 Thessalonians 2:1–8:

- ***Parrhesia* (ἐπαρρησιασάμεθα, v. 2):** A generic LLM often explains this term as "bold Christian evangelism" or "spiritual confidence before God." In 1st-century Greco-Roman antiquity, however, *parrhesia* was a deeply political concept rooted in Athenian democratic free speech and Hellenistic philosophical frankness (the courageous plain-speaking of the Cynic or Stoic philosopher before hostile tyrants). Flattening this civic term into modern evangelical piety obscures Paul's rhetorical engagement with Greco-Roman political culture.
- ***Euangelion* (εὐαγγέλιον θεοῦ, v. 2, 8):** An unguided LLM typically defines this as "the Christian Gospel message of personal salvation." Historically, *euangelion* in the Roman imperial East was technical political terminology used for imperial decrees, military victories, and the accession of the Caesar (as documented in the Priene Calendar Inscription of 9 BCE). Paul's usage represents a provocative counter-imperial appropriation that an AI note easily flattens.
- ***Kolakeia* (κολακεία, v. 5):** An LLM might provide a superficial definition like "insincere compliments." In ancient rhetorical theory (e.g., Theophrastus, Plutarch), *kolakeia* was a formal category of moral vice associated with the parasitic flatterer who manipulated political leaders for financial gain.

| Stage | Source / Model Process | Resulting Text / Interpretation | Scholarly Consequence |
| --- | --- | --- | --- |
| 1. Ancient Text (1st c. CE) | Paul: "ἐπαρρησιασάμεθα ἐν τῷ θεῷ ἡμῶν" | Civic & philosophical frank speech under civic persecution | Direct rhetorical engagement with Hellenistic civic context |
| 2. LLM Latent Training | Filtered through modern theological training corpora | "Paul speaks with bold faith about Jesus's saving grace" | Modern homiletic framing replaces ancient rhetorical nuance |
| 3. Critical Edition Impact | Unvetted AI commentary admitted to apparatus | Historical distance collapsed; political context eliminated | Severe conceptual flattening and anachronism |

To counteract conceptual flattening, digital editors must enforce strict **lexical-historical anchoring** in their prompting. Models must be instructed to interpret vocabulary exclusively through historical lexica (e.g., LSJ, BDAG, DGE), contemporary epigraphic evidence, and primary Hellenistic philosophical parallels rather than modern homiletic literature (Francese, 2014).

**Vocabulary.** *Historical anachronism* — the erroneous attribution of modern concepts, values, or theological categories to a past historical era where they did not exist. *Conceptual flattening* — reducing the rich, culturally specific, and nuanced meaning of historical terminology to generic, contemporary commonplaces. *Epigraphic evidence* — historical inscriptions on stone, metal, or pottery providing primary documentary context for ancient language usage.

**The takeaway for this page:** LLMs naturally project modern semantic assumptions onto ancient terms; editors must constrain models with historical lexica and epigraphy to prevent conceptual flattening.

---

## **07 Content**

**Automation Bias and the Erosion of Editorial Agency**

The integration of artificial intelligence into scholarly editing introduces not only technical hazards but also profound psychological risks. The most pervasive cognitive trap in AI-assisted scholarship is **automation bias**—the human tendency to uncritically trust, accept, and favor automated decision-making systems over one's own critical judgment (Draxler et al., 2024; Lou et al., 2025).

Automation bias occurs because generative AI models produce prose that is grammatically flawless, highly articulate, and stylistically authoritative. When a human editor reads an AI-drafted commentary note that sounds exceptionally scholarly, their critical faculties naturally relax. Instead of actively verifying every Greek lemma, checking manuscript variants, and confirming bibliographic page numbers in physical volumes, the editor falls into passive scanning. Studies in human-computer interaction reveal that as automated tools become more fluent, human error-detection rates drop precipitously (Lou et al., 2025).

The design of the software interface plays a massive role in exacerbating automation bias:

- **The Chat-Box Trap:** In standard conversational chat interfaces (e.g., standard ChatGPT or Claude windows), feedback is delivered as long, flowing prose paragraphs detached from the source text. This layout encourages users to accept large-scale, wholesale text replacements via a single "Copy" button.
- **Cognitive Passivity:** When an editor copy-pastes an entire generated commentary section, they bypass the slow, deliberate cognitive friction that defines genuine philological understanding.
- **Illusion of Completeness:** Because LLMs generate confident, well-rounded answers without expressing uncertainty, editors frequently fail to notice what the model *omitted*—such as a critical manuscript variant or a dissenting scholarly tradition (Draxler et al., 2024).

| Phase | User Cognitive State | System Action / User Behavior | Risk to Scholarly Edition |
| --- | --- | --- | --- |
| 1. Generation | High trust | AI produces grammatically flawless, fluent commentary note | Superficial aesthetic quality masks missing nuance |
| 2. Reception | Cognitive ease | Human reader scans prose passively without checking lexica | Critical faculties relax due to perceived fluency |
| 3. Omission | False confidence | Citations and variant readings not verified against primary texts | Phantom citations or false parsings accepted |
| 4. Publication | Diluted accountability | Unvetted AI text merged into edition repository | Erroneous claims compromise scholarly credibility |

To protect the integrity of digital scholarship, editing environments must be deliberately designed to disrupt this passive cycle. Rather than striving for frictionless automation, digital editing tools must introduce **productive cognitive friction** that forces the editor to evaluate every proposition before it can be merged into the edition's definitive codebase (Lou et al., 2025).

**Vocabulary.** *Automation bias* — the psychological propensity of humans to over-rely on automated systems, leading to uncritical acceptance of false or biased algorithmic outputs. *Cognitive friction* — deliberate design elements that slow down user interaction to encourage careful evaluation and prevent thoughtless, automatic actions. *Passive scanning* — reading text superficially for general coherence rather than performing rigorous, detail-oriented verification.

**The takeaway for this page:** Highly articulate AI outputs trigger automation bias, requiring editing workflows to introduce deliberate cognitive friction that forces rigorous human review.

---

## **08 Content**

**The "AI Ghostwriter Effect" in Scholarly Publishing**

When generative models assist in authoring scholarly text, they alter the psychological relationship between the scholar and the resulting publication. In an influential empirical study on human-AI co-writing, Florian Draxler and colleagues (2024) identified and conceptualized the **"AI Ghostwriter Effect"**—a psychological phenomenon wherein individuals use generative AI to draft text, experience a diminished sense of personal ownership and intellectual responsibility, yet publicly present the work as entirely their own (Draxler et al., 2024).

The AI Ghostwriter Effect creates serious ethical and epistemological crises in academic scholarship:

| Psychological & Ethical Dimension | Traditional Editorial Authoring | The AI Ghostwriter Effect (Draxler et al., 2024) |
| --- | --- | --- |
| Intellectual Agency | High; author crafts every sentence through active thought | Low; author selects and prompts, but AI generates phrasing |
| Psychological Ownership | Deep; author feels intimately responsible for every claim | Fragmented; author treats prose as external paratext |
| Error Accountability | Direct; errors reflect scholar's personal oversights | Diffused; author blames the model when errors are exposed |
| Hermeneutic Engagement | Thorough; scholar wrestles deeply with historical sources | Superficial; scholar curates generated text without deep internalization |

In the context of digital scholarly editions, the AI Ghostwriter Effect undermines the very purpose of commentary. The creation of a critical commentary is not merely a production task designed to generate words on a screen; it is an interpretive, hermeneutic journey through which the editor internalizes the nuances of the text, engages with centuries of scholarly dialogue, and refines their own critical understanding (Tafdrup et al., 2026).

When a student or scholar outsources this interpretive labor to an LLM and simply rubber-stamps the output, the resulting commentary becomes hollow. While the edition may appear comprehensive on the surface, the editor lacks the granular knowledge required to defend its assertions during peer review or classroom debate (Draxler et al., 2024).

To mitigate the AI Ghostwriter Effect, scholarly editions must institute strict **provenance and attribution protocols**. Every commentary note in a TEI digital edition must explicitly declare its authorial origin using `<respStmt>` metadata, documenting whether the note was authored entirely by a human scholar, drafted by a named AI model and vetted by an editor, or algorithmically extracted from secondary databases. Transparency preserves academic integrity and restores personal accountability to digital scholarship.

**Vocabulary.** *AI Ghostwriter Effect* — the psychological condition where users utilize generative AI to write content without feeling true intellectual ownership, yet claim sole authorial credit. *Psychological ownership* — the internal sense that an intellectual work, argument, or text belongs to oneself through personal creative labor. *Provenance metadata* — structured machine-readable records documenting the origin, authorship, and transformation history of an object or data element.

**The takeaway for this page:** The AI Ghostwriter Effect erodes intellectual ownership; preserving scholarly accountability requires deep hermeneutic engagement and transparent provenance metadata.

---

## **09 Content**

**Architectural Solutions: Chat vs Inline Anchored Commentary**

To overcome automation bias and the ghostwriter effect, digital humanities engineers have re-evaluated the user interface architectures used for AI interactions. Standard web-based chat interfaces (such as sidebar conversational bots) have proven fundamentally unsuitable for rigorous scholarly editing (Lou et al., 2025).

In a conversational chat interface, the AI's suggestions exist in a separate visual stream isolated from the source document. When an editor asks a chat model to "provide commentary on 1 Thess 2:1–8," the model responds with an undifferentiated essay. To integrate this feedback, the editor must mentally map the AI's commentary back onto the original Greek text and copy-paste massive blocks of text. This detached layout disconnects the commentary from its textual anchors, obscuring referential ambiguity and encouraging uncritical acceptance (Lou et al., 2025).

| Architectural Dimension | Detached Chat-Box Interface | Inline Anchored Interface (W3C / CARE) |
| --- | --- | --- |
| Document Relationship | Disconnected; commentary rendered in separate window | Direct; commentary bound to specific word tokens (`<w>`) |
| Output Format | Long-form, conversational essay or broad summary | Discrete, fine-grained micro-notes per grammatical feature |
| User Interaction | Copy-paste large blocks; high risk of automation bias | Step-by-step review: *Approve*, *Modify*, or *Reject* per note |
| Standards Conformance | Unstructured text; requires manual XML encoding | Native W3C Web Annotation JSON-LD with `TextQuoteSelector` |
| Editorial Provenance | Ambiguous; model contributions unrecorded | Transparent; explicit `<respStmt>` and software version metadata |

The superior architectural alternative is **Inline Anchored Commentary**, formalized in systems like *AnchoredAI* (Lou et al., 2025) and digital reading environments like CARE (Li et al., 2024).

Under the inline anchored paradigm:

- **Discrete Span Anchoring:** AI feedback is never delivered as an unanchored essay. Instead, the model's proposals are strictly attached to specific character offsets or word elements (`<w xml:id="...">`) in the primary text.
- **Fine-Grained Micro-Notes:** Rather than generating general summaries, the AI generates discrete, atomic notes addressing specific grammatical anomalies, historical realia, or intertextual echoes.
- **Granular Editorial Control:** The editor reviews each discrete note directly alongside the targeted Greek word, with explicit interface buttons to *Approve*, *Edit*, or *Reject* the proposal.

By binding AI generation directly to document anchors via W3C Web Annotation standards, the interface restores spatial context and compels the scholar to evaluate each interpretive claim in its immediate textual environment (Lou et al., 2025).

**Vocabulary.** *Inline anchored commentary* — an annotation interface where computational suggestions are visually and structurally bound directly to specific text spans in the primary document. *Referential ambiguity* — uncertainty regarding exactly which word, clause, or syntactic construction an interpretive note is addressing. *Micro-note* — a concise, atomic commentary note focused exclusively on a single philological, historical, or literary phenomenon.

**The takeaway for this page:** Chat interfaces promote detached, uncritical copy-pasting; rigorous digital scholarship requires inline anchored commentary bound to discrete text spans.

---

## **10 Content**

**Anchoring Context Windows (ACWs) and Desirable Difficulty**

Implementing inline anchored AI commentary in dynamic digital editions requires sophisticated technical infrastructure. In a breakthrough study on human-AI collaborative writing, Michael Lou and colleagues (2025) developed **AnchoredAI**, a system that solves the technical challenge of anchoring AI feedback while introducing psychological principles of learning into the user interface (Lou et al., 2025).

The technical foundation of AnchoredAI is the **Anchoring Context Window (ACW)**. When an editor selects a Greek word or clause for AI analysis, sending only the isolated word (e.g., τροφός) to the LLM results in catastrophic loss of context, as the model cannot determine the grammatical voice, syntactic role, or narrative tone of the surrounding sentence. Conversely, sending an entire multi-chapter book overwhelms the model with extraneous noise. The ACW dynamically extracts a calibrated buffer of surrounding characters—typically 50 to 100 characters before and after the selection—paired with structural metadata (Lou et al., 2025; Sanderson et al., 2017).

| Component | Text Segment / Content | Length / Role |
| --- | --- | --- |
| Prefix Buffer | `ἀλλὰ ἐγενήθημεν νήπιοι ἐν μέσῳ ὑμῶν, ὡς ἐὰν ` | 50 characters (Preceding syntactic context) |
| Exact Target Span | `τροφὸς θάλπῃ` | 12 characters (Selected focus phrase) |
| Suffix Buffer | ` τὰ ἑαυτῆς τέκνα, οὕτως ἱμειρόμενοι ὑμῶν ...` | 50 characters (Following syntactic context) |
| Resolved Selector | W3C `TextQuoteSelector` with prefix, exact, and suffix | Resilient anchor surviving upstream text edits |

By packaging this precise context window into a W3C `TextQuoteSelector`, the system guarantees that the AI generates a note tailored to the specific syntactic environment, while ensuring that the resulting annotation survives subsequent document revisions without breaking its anchor (Sanderson et al., 2017).

Equally important is the psychological concept of **"desirable difficulty"** (Lou et al., 2025). In cognitive psychology, learning, retention, and critical judgment improve when an interface introduces deliberate, manageable cognitive effort rather than seamless automation.

AnchoredAI enforces desirable difficulty by requiring the editor to manually interact with the AI's proposal before it can be merged into the edition. The interface displays the AI's proposed note, highlights the exact words in the text, displays the relevant entry from an authoritative digital lexicon (such as BDAG or LSJ), and forces the editor to actively confirm the parsing and citation. This deliberate friction prevents thoughtless acceptance, eliminates automation bias, and reinforces the editor's deep philological mastery of the text (Lou et al., 2025).

**Vocabulary.** *Anchoring Context Window (ACW)* — a calibrated text buffer surrounding a targeted selection that provides essential contextual data to an LLM and ensures resilient web anchoring. *Desirable difficulty* — a learning and interface design principle where introducing deliberate cognitive friction improves deep comprehension and critical evaluation. *Target span* — the exact sequence of characters or tokens in a primary text selected for annotation or analysis.

**The takeaway for this page:** Anchoring Context Windows provide precise contextual data for AI generation, while desirable difficulty ensures active human evaluation and eliminates automation bias.

---

## **11 Content**

**Structured Prompt Engineering for Scholarly Commentary**

The quality, accuracy, and scholarly utility of AI-generated commentary depend fundamentally on the design of the **system prompt**. In amateur applications, users submit vague, conversational requests (such as "Explain 1 Thess 2:1-8"). Such unconstrained prompts invariably yield generic, homiletic summaries rife with historical anachronisms, modern theological platitudes, and hallucinated citations (Tafdrup et al., 2026).

Professional prompt engineering for digital scholarship requires a multi-layered, highly constrained system prompt that establishes the model's persona, defines the analytical methodology, enforces historical boundaries, and dictates strict output schemas.

A rigorous scholarly system prompt for commentary generation incorporates five mandatory structural components:

| Prompt Component | Core Specification | Scholarly Implementation in Pipeline |
| --- | --- | --- |
| 1. Role & Persona | Hellenistic Greek philologist & TEI digital editor | Enforces academic tone, technical terminology, and critical rigor |
| 2. Lexical Grounding | Restrict definitions to BDAG (3rd ed.) and Smyth/BDF | Eliminates modern homiletic definitions and colloquial usage |
| 3. Anti-Hallucination | Prohibit guessing; declare `"verified": false` on doubt | Prevents fabrication of non-existent chapter/verse locators |
| 4. Formal Taxonomy | Enforce [philological, historical, intertextual, rhetorical] | Standardizes note types for TEI `<interpGrp>` grouping |
| 5. Few-Shot Exemplar | Provide 1 Thess 2:7 (τροφός) manual gold-standard note | Establishes target depth, citation syntax, and analytical structure |

These structural constraints function as an integrated epistemic firewall:

- **Role and Epistemic Persona:** Explicitly assigns the model the role of an expert classical and Hellenistic Greek philologist and digital editor, operating under the methodological standards of academic peer review.
- **Corpus and Lexical Grounding:** Restricts the model's semantic definitions to authoritative historical reference works (e.g., LSJ, BDAG, Smyth, BDF) and explicitly forbids modern colloquial or homiletic interpretations.
- **Negative Constraints (Anti-Hallucination Directives):** Formally commands the model never to guess citations, never to invent chapter or verse numbers, and to explicitly output `"citation_verified": false` or `"reference": "UNKNOWN"` if a primary source parallel cannot be verified with certainty.
- **Few-Shot Exemplars:** Provides 2 to 3 complete, gold-standard human commentary notes (from Lesson 12.1) illustrating the exact desired tone, depth, and structural organization.
- **Categorical Typology:** Forces the model to classify every proposed note into one of our four formal categories (`philological`, `historical`, `intertextual`, `rhetorical`).

By engineering prompts with these comprehensive scholarly constraints, digital editors dramatically suppress the model's propensity for hallucination and anachronism, transforming raw foundation models into disciplined, reliable research assistants (Lou et al., 2025; Tafdrup et al., 2026).

**Vocabulary.** *System prompt* — foundational instructions provided to an AI model that configure its behavioral persona, analytical rules, constraints, and output format across a session. *Few-shot exemplar* — sample input-output pairs provided within a prompt to teach the model desired styles, structures, and standards through concrete demonstration. *Negative constraint* — an explicit directive in a prompt prohibiting specific undesirable behaviors, such as fabricating citations or using modern jargon.

**The takeaway for this page:** Effective scholarly prompt engineering requires establishing an expert philological persona, enforcing historical lexical constraints, and providing few-shot gold-standard exemplars.

---

## **12 Content**

**Schema-Constrained Generation: JSON-LD and TEI Outputs**

A major obstacle to integrating generative AI into digital humanities workflows is the unstructured nature of natural language output. If an LLM returns commentary as loose markdown paragraphs, downstream scripts cannot automatically validate the data, insert it into a TEI XML file, or publish it to a W3C Web Annotation triplestore. The commentary remains trapped in prose, requiring manual copy-pasting (Sanderson et al., 2017).

To build fully automated, reproducible digital pipelines, editors must employ **schema-constrained generation**. Modern LLM APIs (such as OpenAI's Structured Outputs, Anthropic's Tool Use / JSON mode, and Gemini's JSON schema enforcement) allow developers to bind model generation to a strict **JSON Schema**. The model's decoding engine is mathematically constrained to only output tokens that conform to the defined schema syntax, eliminating syntax errors and guaranteeing predictable data structures (Lou et al., 2025).

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ScholarlyCommentaryNote",
  "type": "object",
  "required": ["anchor", "category", "lemma", "scholarly_note", "citations", "w3c_motivation", "verification_status"],
  "properties": {
    "anchor": {
      "type": "object",
      "required": ["xml_id", "exact", "prefix", "suffix"],
      "properties": {
        "xml_id": {"type": "string"},
        "exact": {"type": "string"},
        "prefix": {"type": "string"},
        "suffix": {"type": "string"}
      }
    },
    "category": {
      "type": "string",
      "enum": ["philological", "historical", "intertextual", "rhetorical"]
    },
    "lemma": {"type": "string"},
    "morphosyntax": {"type": "string"},
    "scholarly_note": {"type": "string"},
    "citations": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["source_work", "urn_or_ref", "verified"],
        "properties": {
          "source_work": {"type": "string"},
          "urn_or_ref": {"type": "string"},
          "verified": {"type": "boolean"}
        }
      }
    },
    "w3c_motivation": {
      "type": "string",
      "enum": ["commenting", "identifying", "linking", "classifying", "editing"]
    },
    "external_authority_uri": {"type": "string", "format": "uri"},
    "verification_status": {
      "type": "string",
      "enum": ["ai_draft", "human_approved", "rejected"]
    }
  }
}
```

Schema-constrained generation guarantees several critical scholarly advantages:

- **Direct Ingestion into Pipelines:** The structured JSON output can be ingested directly by Python build scripts that automatically generate TEI `<standOff>` XML or W3C JSON-LD web annotations.
- **Enforced Taxonomies:** The model is programmatically restricted to valid enum values (e.g., our four approved commentary categories and standard W3C motivations).
- **Mandatory Verification Flags:** The schema forces the model to declare whether every cited parallel has been verified against external reference indices.

By combining rigorous prompt constraints with strict JSON Schema enforcement, the digital editor bridges the gap between probabilistic generative AI and deterministic digital edition architectures (Lou et al., 2025; Sanderson et al., 2017).

**Vocabulary.** *Schema-constrained generation* — forcing an LLM to generate output that strictly adheres to a predefined structural specification, such as a JSON Schema. *JSON Schema* — a declarative standard for annotating and validating the structure, data types, and required fields of JSON documents. *Decoding constraint* — a mathematical mask applied during LLM token sampling that restricts valid next tokens to syntactically allowed characters.

**The takeaway for this page:** Schema-constrained generation forces LLMs to produce strictly validated JSON structures that feed seamlessly into automated TEI and W3C Web Annotation pipelines.

---

## **13 Content**

**The Vocabulary Scaffolding Model: Lessons from Dickinson College Commentaries (DCC)**

A brilliant model for dividing labor between automated computation and human scholarly annotation is provided by the **Dickinson College Commentaries (DCC)** project, directed by Christopher Francese (Francese, 2014).

The DCC publishes peer-reviewed, digital scholarly commentaries on classical Latin and ancient Greek texts specifically designed to optimize student reading fluency and critical comprehension. In traditional print editions, commentaries are heavily congested with routine vocabulary glosses, forcing editors to waste space re-explaining common words while leaving little room for advanced literary, historical, or rhetorical analysis. The DCC revolutionized this process by establishing an algorithmic approach to **vocabulary scaffolding** (Francese, 2014).

The DCC methodology operates on a fundamental quantitative insight derived from corpus linguistics:

| Vocabulary Tier | Corpus Distribution (TLG / LASLA Data) | Editorial Treatment in DCC Workflow |
| --- | --- | --- |
| **Core Vocabulary (Tier 1)** | Top 1,000–1,500 lemmas (covers ~75% of all running words) | Filtered out automatically; assumed prerequisite knowledge for readers |
| **Running Vocabulary (Tier 2)** | Words occurring outside the core frequency threshold | Algorithmically parsed, lemmatized, and glossed in running margin notes |
| **Interpretive Commentary (Tier 3)** | Complex syntax, rare idioms, historical realia, allusions | Meticulously custom-authored by human classical scholars |

By utilizing frequency lists from the *Thesaurus Linguae Graecae* (TLG) and the *Laboratoire d'Analyse Statistique des Langues Anciennes* (LASLA), the DCC platform automatically extracts and glosses all non-core vocabulary for each specific chapter. This computational pre-processing frees human editors from the tedious, repetitive work of routine dictionary glossing. The scholars can dedicate their full intellectual energy to Tier 3: authoring deep, nuanced notes on irregular syntax, historical prosopography, rhetorical structure, and literary intertextuality (Francese, 2014).

Furthermore, the DCC integrates Linked Open Data authority files directly into its commentary notes. Place names are systematically linked to Pleiades gazetteer URIs, embedding geographic maps directly within the digital reading environment.

In our AI-assisted commentary workflow, we adopt the DCC philosophy: we utilize computational tools and language models to handle baseline morphological parsing, entity identification, and vocabulary extraction, allowing the human editor to concentrate their critical faculties on high-level hermeneutic vetting and interpretive nuance (Francese, 2014; Lou et al., 2025).

**Vocabulary.** *Vocabulary scaffolding* — an educational and editorial framework that provides tiered linguistic assistance based on empirical word-frequency distributions. *Core vocabulary* — the set of high-frequency lemmas in a language that account for the vast majority of tokens in standard literary texts. *Running vocabulary* — a localized list of lower-frequency words appearing in a specific passage, provided alongside the text to aid reading.

**The takeaway for this page:** The Dickinson College Commentaries model demonstrates how algorithmic tools can automate routine vocabulary scaffolding, freeing scholars to focus on deep interpretive commentary.

---

## **14 Content**

**Semantic Allusion Detection vs Tesserae Lexical Overlap**

To fully appreciate how generative AI complements deterministic tools in the commentary workflow, we must compare the intertextual discovery capabilities of Large Language Models against the deterministic n-gram algorithms of the **Tesserae Project** (Coffee et al., 2012; Tafdrup et al., 2026).

In Lesson 12.2, you learned that Tesserae detects textual reuse by identifying two or more shared lemmas ($k \ge 2$) occurring within a defined syntactic span, weighting the results using a frequency-density scoring formula. This deterministic approach is exceptionally powerful for discovering verbatim citations, direct borrowings, and formulaic repetitions across massive corpora. However, classical and biblical authors frequently allude to prior texts through **sub-lexical and conceptual techniques** that completely elude n-gram counters (Coffee et al., 2012).

Consider the five major modes of intertextual reuse and how each computational methodology performs:

| Mode of Textual Reuse | Literary Mechanism | Tesserae Detection (Deterministic) | LLM Detection (Semantic Transformer) |
| --- | --- | --- | --- |
| **Verbatim Citation** | Identical words repeated in sequence | **Optimal:** High score, zero false negatives | **High:** Identifies match but may hallucinate verse |
| **Morphological Variation** | Same lemmas with altered inflections | **Optimal:** Resolved via lemmatization dictionary | **High:** Recognizes underlying grammatical roots |
| **Synonymic Substitution** | Concept reused with entirely different words | **Blind:** Fails completely (0 shared lemmas) | **Optimal:** Neural embeddings recognize semantic equivalence |
| **Structural Parody / Echo** | Inverted syntax or rhetorical counter-argument | **Blind:** Fails if vocabulary diverges | **Moderate to High:** Identifies rhetorical patterns |
| **Thematic Motif Resonance** | Shared conceptual framework (e.g., nursing mother) | **Blind:** Generates massive noise or misses entirely | **High:** Contextual attention maps thematic links |

For example, when Paul in 1 Thessalonians 2:7 uses the phrase ὡς ἐὰν τροφὸς θάλπῃ τὰ ἑαυτῆς τέκνα ("like a nursing mother cherishing her own children"), Tesserae can only search for passages containing the specific Greek lemmas τροφός ("nurse") and θάλπω ("cherish/warm"). If an ancient philosophical treatise by Epictetus or Seneca describes the affectionate, self-sacrificing care of a true moral teacher using different vocabulary (such as μήτηρ, "mother", or θεραπεύω, "to care for"), Tesserae is totally blind to the parallel (Coffee et al., 2012).

An LLM, by contrast, operates on contextual embeddings that map pastoral and maternal imagery across philosophical discourses. The model can recognize that Paul is engaging a widespread Hellenistic philosophical trope regarding the pedagogical posture of the philosopher toward spiritual novices (Tafdrup et al., 2026).

Thus, the optimal digital commentary pipeline uses **both tools in tandem**: Tesserae provides the rigorous, empirically verifiable baseline of lexical borrowing, while the LLM acts as an exploratory probe for latent semantic, thematic, and rhetorical allusions.

**Vocabulary.** *Synonymic substitution* — an intertextual technique where an author borrows an idea or phrase from a predecessor but replaces the original vocabulary with synonymous words. *Structural parody* — imitating the formal rhetorical or syntactic structure of an earlier text, often to subvert or recontextualize its original meaning. *Thematic motif resonance* — subtle literary resonance achieved through shared imagery, metaphors, or cultural concepts rather than direct verbal quotation.

**The takeaway for this page:** Tesserae excels at verbatim and lemmatized word overlap, while LLMs excel at uncovering synonymic, structural, and thematic allusions lacking shared vocabulary.

---

## **15 Content**

**Knowledge Graph Integration: The DanteSources Paradigm**

Transforming natural language commentary into machine-readable knowledge graphs represents one of the highest achievements of digital textual scholarship. A pioneering benchmark in this field is **DanteSources**, developed by the Italian National Research Council (ISTI-CNR) and the University of Pisa under the leadership of Valentina Bartalesi, Carlo Meghini, and Daniele Metilli (Bartalesi et al., 2018).

For centuries, scholars of Dante Alighieri compiled massive print commentaries identifying the primary sources—the classical, biblical, and medieval authors—that Dante quoted, referenced, or echoed across works like the *Divina Commedia*, the *Convivio*, and *De Monarchia*. However, because this immense scholarly erudition remained locked inside narrative footnotes, scholars could not perform macro-level computational queries on Dante's intellectual influences. One could not easily query: *Which Aristotelian treatises are cited most heavily in Book II of the Convivio compared to Monarchia, and how many of those citations are explicit versus implicit?* (Bartalesi et al., 2018).

To solve this, the DanteSources team designed a formal **RDF/OWL ontology** that translates narrative commentary into structured semantic triples:

| Semantic Subject (Dante Text) | Ontological Predicate (CiTO / SKOS) | Semantic Object (Source / Authority) |
| --- | --- | --- |
| Dante *Convivio* II.1 (`DoCO:Paragraph`) | `cito:citesAsExplicitCitation` | Aristotle *Nicomachean Ethics* (`FRBRoo:Work` / DBpedia URI) |
| Dante *Monarchia* I.3 (`DoCO:Paragraph`) | `cito:citesAsAuthority` | Averroes *Commentary on De Anima* (`FRBRoo:Work` / VIAF URI) |
| Dante *Commedia* Inf. IV (`DoCO:Section`) | `dante:hasThematicArea` | Classical Pagan Poetry & Philosophy (`SKOS:Concept` URI) |

The DanteSources ontology harmonizes three foundational semantic models:

- **FRBRoo (Functional Requirements for Bibliographic Records - Object Oriented):** Models the conceptual works, expressions, and physical manifestations of Dante's writings and his source authors.
- **DoCO (Document Components Ontology):** Provides structural granularity, assigning stable URIs to specific chapters, paragraphs, and poetic tercets.
- **CiTO (Citation Typing Ontology):** Expresses the precise scholarly nature of the intertextual link (e.g., `citesAsAuthority`, `citesAsEvidence`, `citesForInformation`, `qualifies`, `refutes`) (Bartalesi et al., 2018).

In modern AI-assisted editing, we use LLMs to automate the preliminary extraction of these ontological relationships. Rather than manually hand-coding thousands of RDF triples, an LLM constrained by a strict JSON-LD schema can analyze an ancient text, extract intertextual citations, map them to standard CiTO properties, and link historical entities to DBpedia and VIAF URIs. Once validated by a human editor, these structured annotations transform traditional literary commentary into a queryable global knowledge graph accessible via standard SPARQL endpoints (Bartalesi et al., 2018).

**Vocabulary.** *RDF/OWL ontology* — a formal, machine-readable conceptual model that defines classes, properties, and relationships to represent knowledge within a domain on the Semantic Web. *Citation Typing Ontology (CiTO)* — a standardized semantic ontology for describing the factual and rhetorical nature of citations between texts. *SPARQL* — the standard query language for retrieving and manipulating data stored in Resource Description Framework (RDF) format.

**The takeaway for this page:** The DanteSources project proves that formal ontologies (FRBRoo, DoCO, CiTO) transform narrative commentary into queryable, semantic knowledge graphs.

---

## **16 Content**

**Resolving Polysemy in Ancient Commentary: The *Graphilosophy* Case Study**

The immense challenge of applying computational and AI models to historical commentary is magnified when working with ancient, non-alphabetic, or highly compressed languages. A remarkable case study in resolving linguistic ambiguity and polysemy through AI and knowledge graphs is the **Graphilosophy** project, which models classical Chinese-Vietnamese commentaries on Confucian foundational texts (*The Four Books*) (Tafdrup et al., 2026).

Classical Chinese presents extreme computational hurdles for text analysis:

- **Extreme Polysemy and Homography:** A single logographic character can represent multiple distinct grammatical parts of speech (noun, verb, adjective) and vastly different conceptual definitions depending entirely on its local syntactic and philosophical context.
- **Phonetic Ambiguity across Cultures:** As Confucian texts circulated through Vietnam, Korea, and Japan, characters were read through distinct phonetic systems (such as Sino-Vietnamese *Chữ Hán*), creating layered orthographic variations.
- **Dense Commentarial Strata:** Historical editions of Confucian classics embed centuries of interlinear commentaries by multiple Neo-Confucian philosophers (such as Zhu Xi), where each commentator interprets the core logograms through divergent metaphysical frameworks (Tafdrup et al., 2026).

| Contextual Occurrence | Syntactic Role & Context | Neural Vector Embedding Profile | Aligned Concept URI |
| --- | --- | --- | --- |
| Instance A: Standard Prose | Common noun ("human", "individual") | High correlation with demographic & social terms | Wikidata: `Homo sapiens` (Q5) |
| Instance B: Ethical Discourse | Moral virtue (*Ren* / "Benevolence") | High correlation with virtue, righteousness, and ritual | Chinese Text Project: `Concept:Ren` (仁) |
| Instance C: Commentarial Gloss | Neo-Confucian metaphysical principle | High correlation with cosmic order (*Li*) | Stand-off Concept: `NeoConfucian:Principle` |

The *Graphilosophy* project resolved these challenges by integrating **multilingual Large Language Model embeddings** with structured graph databases. When an unannotated commentary passage is processed, the system generates high-dimensional contextual embeddings that analyze the entire sentence rather than isolated characters. For instance, the system dynamically distinguishes between the character 人 functioning merely as a generic pronoun ("person") versus 人 acting as an orthographic variant or philosophical cipher for 仁 (*Ren*, the foundational Confucian virtue of "humaneness" or "benevolence") (Tafdrup et al., 2026).

The lesson for Western classical and biblical commentary is direct: ancient Greek terms like *pistis* (πίστις: "faith", "trustworthiness", "pledge", "proof"), *logos* (λόγος: "word", "reason", "account", "cosmic principle"), or *charis* (χάρις: "grace", "gift", "gratitude", "patronal favor") exhibit profound contextual polysemy. An unguided search engine flattens these terms into a single dictionary entry. By utilizing context-sensitive LLM embeddings verified by human philologists, digital editions can accurately disambiguate polysemous vocabulary and attach precise ontological URIs to every occurrence (Tafdrup et al., 2026).

**Vocabulary.** *Polysemy* — the capacity for a single word, character, or symbol to have multiple distinct but related meanings. *Homography* — words that share the same written form but possess different meanings, origins, or grammatical functions. *Context-sensitive embedding* — a numerical representation of a word generated by a neural model that changes dynamically based on the surrounding sentence context.

**The takeaway for this page:** The *Graphilosophy* project illustrates how contextual neural embeddings disambiguate dense polysemous vocabulary in ancient commentary traditions.

---

## **17 Content**

**The Collaborative AI-Assisted Reading Environment (CARE)**

To investigate how AI interventions impact scholarly reading, annotation habits, and cognitive load in real-world academic settings, human-computer interaction researchers developed the **Collaborative AI-Assisted Reading Environment (CARE)** (Li et al., 2024).

CARE is an open-source, web-based collaborative reading platform designed to bridge the gap between traditional document annotation (such as highlighting and margin notes in PDF or HTML editions) and generative artificial intelligence. Built on modern web standards, CARE renders primary texts while hosting an **AI broker architecture** connected to Hugging Face transformer models and large foundation APIs (Li et al., 2024).

| CARE Telemetry Layer | Monitored User Behavior | Research / Pedagogical Metric |
| --- | --- | --- |
| 1. Interface & Highlight | User selects Greek text span (`TextQuoteSelector`) | Target selection frequency and passage dwell time |
| 2. Telemetry Capture Engine | Millisecond timer, viewport scrolling, clickstream | Cognitive load and reading velocity before/after note display |
| 3. AI Broker Dispatch | Routes text span + ACW to Hugging Face models | Model response latency and schema compliance |
| 4. Annotation Evolution | User edits, expands, or rejects AI draft note | Mutation rate: verbatim acceptance vs critical refinement |

The CARE platform integrates comprehensive **behavioral telemetry** that records:

- **Dwell Time & Reading Velocity:** Measures exact millisecond durations spent reading specific text passages before and after an AI annotation is displayed.
- **Annotation Mutation Tracking:** Records how often users accept AI suggestions verbatim versus modifying, expanding, or completely rejecting the generated prose.
- **Cognitive Load Indicators:** Tracks navigation patterns, back-tracking, and viewport scrolling to assess whether AI assistance streamlines comprehension or introduces distraction (Li et al., 2024).

Empirical findings from CARE experiments provide crucial insights for digital edition design. When AI feedback is presented as dense, unsolicited pop-up summaries, reader reading velocity increases artificially while comprehension of complex textual arguments drops—a clear indicator of cognitive offloading and superficial reading. Conversely, when AI commentary is delivered as **on-demand, inline micro-notes** requiring explicit user activation, scholars engage deeply with the primary source, critically editing the AI's drafts and spending substantial time verifying historical claims (Li et al., 2024).

The CARE architecture demonstrates that the future of digital scholarly editions lies in telemetry-informed, user-centric interfaces that scaffold critical human analysis rather than overwhelming the reader with unvetted automated prose.

**Vocabulary.** *Behavioral telemetry* — automated logging and tracking of user interactions, navigation paths, timing, and interface events to analyze cognitive workflows. *Cognitive offloading* — the use of physical actions or digital tools to reduce the mental effort required to complete a complex intellectual task. *AI broker* — a middleware software service that routes user interface events to appropriate machine learning models and formats the results for presentation.

**The takeaway for this page:** The CARE reading environment demonstrates through behavioral telemetry that on-demand, inline AI micro-notes encourage critical engagement, whereas unsolicited text prompts cognitive passivity.

---

## **18 Content**

**Multi-Model Cross-Verification Pipelines**

In high-stakes textual scholarship, relying on a single AI model for commentary drafting introduces severe systemic vulnerabilities. Every foundation model possesses idiosyncratic training biases, proprietary RLHF (Reinforcement Learning from Human Feedback) tuning, and specific blind spots. A single model may consistently hallucinate in Hellenistic Greek syntax while performing well in Latin, or exhibit an aggressive modern theological bias on certain biblical themes (Tafdrup et al., 2026).

To eliminate single-model failure points, digital humanities workflows utilize **Multi-Model Cross-Verification Pipelines**. In this architecture, a primary generative model produces an initial commentary draft, which is then independently audited, critiqued, and cross-checked by secondary models with distinct architectures and training backgrounds (e.g., pairing OpenAI's GPT-5 with Anthropic's Claude 3.7 Sonnet, Google's Gemini 2.5 Pro, or open-weights models like Gemma 2 or DeepSeek R1) (Lou et al., 2025).

| Pipeline Stage | Active Architecture | Functional Responsibility | Output Deliverable |
| --- | --- | --- | --- |
| 1. Primary Generation | GPT-5 / Claude 3.7 Sonnet | Drafts structured JSON commentary notes from Greek ACW | Candidate notes with lemmas and provisional citations |
| 2. Syntax & Citation Audit | Reasoning Model (o3-mini) | Forensically audits Greek morphosyntax and verse numbers | Verification flags and citation correction notices |
| 3. Realia & Anachronism Audit | Open-Weights Model (Gemma 2) | Audits historical realia against Macedonian provincial data | Anachronism flags and historical context critiques |
| 4. Consensus Engine | Python Orchestration Script | Compares model outputs and calculates agreement scores | High-confidence notes routed to editor; conflicts flagged |

The multi-model pipeline operates via a four-step verification cycle:

- **Generation:** Model A receives the primary Greek text, Anchoring Context Window, and system prompt, generating a structured JSON draft with proposed lexical parsing, historical realia, and intertextual citations.
- **Independent Verification:** Models B and C receive Model A's output alongside the primary text, operating under explicit auditing instructions: *Identify all factual inaccuracies, check citation numbering, and flag any anachronistic definitions.*
- **Consensus & Discrepancy Analysis:** A Python orchestration script compares the outputs. If all models achieve 100% agreement on a routine morphological parse, the item is given a high confidence score. If models disagree—for example, if Model A asserts a direct citation of Jeremiah while Model B flags it as an unprovable thematic echo—the system generates a discrepancy flag.
- **Human Adjudication:** Discrepancies and low-confidence items are immediately escalated to the human scholar's review queue with highlighted points of contention.

Multi-model cross-verification effectively transforms AI from an individual hallucination-prone generator into an adversarial debate system that filters out superficial errors before human review begins (Lou et al., 2025).

**Vocabulary.** *Multi-model cross-verification* — an automated pipeline where multiple distinct AI models independently review, audit, and critique generated outputs to detect errors and establish consensus. *Adversarial auditing* — an evaluation workflow where an AI model is explicitly instructed to find flaws, errors, and hallucinations in another model's output. *Consensus engine* — an algorithmic component that aggregates outputs from multiple models to calculate agreement metrics and flag discrepancies.

**The takeaway for this page:** Multi-model cross-verification pipelines employ diverse AI architectures to adversarially audit commentary drafts, filtering out hallucinations before human review.

---

## **19 Content**

**Automated Citation Verification and Authority Validation**

While multi-model consensus significantly improves commentary quality, the ultimate standard of truth in digital philology cannot reside in AI consensus alone. True scholarly verification requires **deterministic grounding against authoritative external databases and APIs** (Bartalesi et al., 2018; Simon et al., 2017).

Whenever an LLM proposes a historical place name, a biographical entity, or an ancient textual citation, the digital editing pipeline must pass that claim through automated validation scripts that query verified Linked Open Data endpoints:

| Proposed AI Claim | Verification Target / Endpoint | Validation Protocol | Failure Action |
| --- | --- | --- | --- |
| Toponym (e.g., *Philippi*) | Pleiades Gazetteer API / WHG | Query Pleiades API for ID (`pleiades:501482`) and coordinate bounds | If URI 404s or coordinates mismatch, flag as invalid entity |
| Person / Author (e.g., *Dio Chrysostom*) | VIAF / Wikidata SPARQL Endpoint | Validate persistent VIAF URI (`viaf:100198644`) against authority record | Flag ungrounded names; enforce authoritative spelling |
| Canonical Text Reference (e.g., *LXX Isa 52:7*) | CTS URN Resolver / Perseus API | Resolve `urn:cts:greekLit:tlg0527.tlg031...` against digitized Greek corpus | If URN fails to resolve, mark as unverified citation |
| Greek Lemma / Morphosyntax | Morphological Engine (Morpheus / CLTK) | Run rule-based parser on target token (`ἐπαρρησιασάμεθα`) | Flag any parse where LLM contradicts rule-based dictionary |

```python
import requests

def verify_pleiades_entity(pleiades_id: str) -> bool:
    """Validate that a proposed Pleiades URI exists and returns valid JSON."""
    url = f"https://pleiades.stoa.org/places/{pleiades_id}/json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"Verified Place: {data.get('title')} ({data.get('reprPoint')})")
            return True
        return False
    except requests.RequestException:
        return False

# Example: Auditing an AI-generated toponym proposal for 1 Thess 2:2
is_valid = verify_pleiades_entity("501482") # Philippi
print(f"Pleiades 501482 Validation: {is_valid}")
```

Automated authority validation scripts execute in milliseconds, acting as a deterministic gatekeeper. If an LLM hallucinates a non-existent Pleiades ID (e.g., inventing `pleiades:99999999`) or provides a malformed CTS URN, the script immediately traps the error, logs the failure, and prevents the unverified data from polluting the edition's RDF graph or TEI header (Bartalesi et al., 2018; Sanderson et al., 2017).

By combining generative AI drafting with automated API validation, the digital editor constructs an impenetrable quality control filter where no computational claim reaches the human reviewer without empirical verification.

**Vocabulary.** *Authority validation* — programmatically verifying that a named entity, geographic location, or bibliographic citation corresponds to an authentic record in an established authority file. *Pleiades* — a collaborative Linked Open Data gazetteer of ancient places maintained by the Institute for the Study of the Ancient World (ISAW). *CTS URN Resolver* — a network service that accepts a Canonical Text Services URN and returns the exact canonical text passage or XML node.

**The takeaway for this page:** Deterministic validation scripts query Pleiades, VIAF, and CTS URN APIs to mechanically verify AI claims before they reach the human editor.

---

## **20 Content**

**The Human-in-the-Loop (HITL) Editorial Architecture**

Having examined the individual components of computational drafting, multi-model cross-checking, and API validation, we can now assemble the complete **Human-in-the-Loop (HITL) Editorial Architecture** for Topic 12 (Tafdrup et al., 2026; Lou et al., 2025).

The HITL framework synthesizes computational scale with traditional philological rigor across four sequential, tightly integrated stages:

| Pipeline Stage | Primary Actors / Tools | Core Operations | Quality Gate / Output |
| --- | --- | --- | --- |
| **Stage 1: Candidate Extraction** | Base TEI XML, LLMs, Tesserae | Ingests text, builds ACWs, generates schema-bound JSON drafts and n-gram matches | Raw candidate notes logged with token IDs |
| **Stage 2: Automated Verification** | Multi-model auditors, Python API scripts | Validates CTS URN syntax, Pleiades/VIAF URIs, and morphological parsings | Automated verification flags appended to JSON |
| **Stage 3: Human Adjudication** | Human Scholar / Digital Editor | Reviews flagged notes in inline interface, vets historical nuance, decides authorization | Authorized, refined notes (`vetted_notes.json`) |
| **Stage 4: Stand-Off Publication** | Python Serialization Builders | Compiles approved notes into TEI P5 `<standOff>` XML and W3C WADM JSON-LD | Archival TEI XML & Live Web Annotations |

The defining principle of this architecture is that **computational models only possess proposing power; the human scholar holds exclusive authorizing power** (Tafdrup et al., 2026). At no point does an automated algorithm or LLM write directly into the master TEI XML repository without human sign-off.

Furthermore, Stage 4 enforces rigorous provenance tracking. When an approved note is serialized into TEI XML, the system automatically inserts a `<respStmt>` recording the precise human reviewer, the AI model version used for initial drafting, and the timestamp of validation. This ensures complete transparency for future generations of scholars (Draxler et al., 2024; Schmidt, 2010).

**Vocabulary.** *Proposing power* — the capacity of an automated computational tool to suggest candidate annotations, parses, or links for human review. *Authorizing power* — the exclusive right and responsibility of the human scholar to validate, edit, or reject computational proposals for inclusion in an edition. *Provenance tracking* — maintaining an unbroken, machine-readable audit trail documenting how every piece of data was created, modified, and verified.

**The takeaway for this page:** The HITL editorial architecture restricts computational tools to proposing candidate notes, reserving exclusive authorizing power for the human scholar.

---

## **21 Content**

**Hands-On: Crafting Structured Prompts for 1 Thessalonians 2:1–8**

Now we begin our practical laboratory implementation. Today you will apply our HITL pipeline to generate, verify, and vet scholarly commentary notes for our core course passage: **1 Thessalonians 2:1–8** (Greek text established in Topic 6 and collated in Topic 7).

Your first objective is to craft the structured system prompt that will govern the LLM generation. Open your Python development environment or IDE and create a new script: `scripts/generate_ai_commentary.py`.

```python
import os
import json
from pathlib import Path

# 1. Define the Scholarly System Prompt with Strict Epistemic Constraints
SYSTEM_PROMPT = """You are an expert Hellenistic Greek philologist, classical historian, and TEI digital editor.
Your task is to draft rigorous scholarly commentary notes for 1 Thessalonians 2:1–8.

METHODOLOGICAL RULES:
1. Base all morphosyntactic analyses on BDAG (3rd ed.) and Smyth/BDF grammars.
2. Base historical realia on 1st-century CE Roman provincial administration in Macedonia.
3. Classify EVERY note into exactly one category: 'philological', 'historical', 'intertextual', or 'rhetorical'.
4. STRICT ANTI-HALLUCINATION: If an intertextual parallel cannot be verified with a precise, existing chapter/verse or Stephanus section, DO NOT invent it. Set 'verified': false.
5. Map places to Pleiades IDs and persons to VIAF/Wikidata URIs where possible.
6. Output ONLY a valid JSON object matching the requested schema. Do NOT wrap in conversational filler."""

# 2. Define the Target Greek Text Segment with Word Identifiers
TARGET_PASSAGE_GREEK = """
1 Thess 2:1-8 (Normalized SBLGNT):
[w1] Αὐτοὶ [w2] γὰρ [w3] οἴδατε, [w4] ἀδελφοί, [w5] τὴν [w6] εἴσοδον [w7] ἡμῶν [w8] τὴν [w9] πρὸς [w10] ὑμᾶς [w11] ὅτι [w12] οὐ [w13] κενὴ [w14] γέγονεν,
[w15] ἀλλὰ [w16] προπαθόντες [w17] καὶ [w18] ὑβρισθέντες [w19] καθὼς [w20] οἴδατε [w21] ἐν [w22] Φιλίπποις [w23] ἐπαρρησιασάμεθα [w24] ἐν [w25] τῷ [w26] θεῷ [w27] ἡμῶν [w28] λαλῆσαι [w29] πρὸς [w30] ὑμᾶς [w31] τὸ [w32] εὐαγγέλιον [w33] τοῦ [w34] θεοῦ [w35] ἐν [w36] πολλῷ [w37] ἀγῶνι.
...
[w70] ἀλλὰ [w71] ἐγενήθημεν [w72] νήπιοι [w73] ἐν [w74] μέσῳ [w75] ὑμῶν, [w76] ὡς [w77] ἐὰν [w78] τροφὸς [w79] θάλπῃ [w80] τὰ [w81] ἑαυτῆς [w82] τέκνα.
"""
```

Notice the critical features embedded within this prompt:

- **Token Anchor Tags:** The Greek text includes embedded word IDs (`[w1]`, `[w2]`, etc.) derived from your TEI XML transcription, enabling the model to bind its proposed notes directly to specific XML elements.
- **Strict Lexical Authority:** Explicitly citing BDAG and BDF prevents the model from generating colloquial or modern theological definitions.
- **Negative Anti-Hallucination Directives:** Mandates that the model declare uncertainty rather than fabricating references (Lou et al., 2025; Tafdrup et al., 2026).

Save this script. In the next section, we execute the generation run and capture the structured JSON output.

**Vocabulary.** *System prompt crafting* — designing prompt instructions that enforce technical, scholarly, and formatting constraints on AI generation. *Word-level tokenization* — segmenting text into discrete, uniquely identified word units (`[w1]`, `[w2]`) to facilitate precise stand-off anchoring.

**The takeaway for this page:** Crafting scholarly prompts requires embedding word-level token anchors, specifying authoritative reference works, and mandating anti-hallucination rules.

---

## **22 Content**

**Hands-On: Running AI Commentary Generation and Capturing Outputs**

With your system prompt and text payload constructed, execute the commentary generation call using the local `llm` CLI or Python SDK.

Add the execution and schema-binding logic to `scripts/generate_ai_commentary.py`:

```python
import json
import subprocess

def run_llm_commentary_generation(prompt: str, system_prompt: str) -> dict:
    """Execute LLM generation via CLI/API and return structured JSON."""
    payload = f"{system_prompt}\n\nTASK:\nGenerate 4 structured commentary notes for 1 Thess 2:1-8 across all categories.\n\nTEXT:\n{prompt}"
    
    # Run using the local llm CLI interface
    cmd = ["llm", "prompt", "-m", "gpt-4o-mini", payload, "--json-object"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    
    return json.loads(result.stdout)

# Execute and save raw candidate output
raw_candidates = run_llm_commentary_generation(TARGET_PASSAGE_GREEK, SYSTEM_PROMPT)
output_path = Path("src/modules/Topic_12_Commentary/raw_ai_candidates.json")
output_path.write_text(json.dumps(raw_candidates, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Captured {len(raw_candidates.get('notes', []))} AI candidate notes in {output_path}")
```

Inspect the generated `raw_ai_candidates.json` file. A high-quality model run produces structured notes formatted like this:

```json
{
  "notes": [
    {
      "anchor_id": "w22",
      "exact": "Φιλίπποις",
      "prefix": "καθὼς οἴδατε ἐν ",
      "suffix": " ἐπαρρησιασάμεθα",
      "category": "historical",
      "lemma": "Φίλιπποι",
      "scholarly_note": "Philippi was a Roman colony (Colonia Iulia Augusta Philippensis) in eastern Macedonia governed under the ius Italicum. Paul's reference to being mistreated (ὑβρισθέντες) refers to illegal beating and imprisonment of Roman citizens (Acts 16:19-40).",
      "authority_uri": "https://pleiades.stoa.org/places/501482",
      "w3c_motivation": "identifying",
      "verified": true
    },
    {
      "anchor_id": "w23",
      "exact": "ἐπαρρησιασάμεθα",
      "prefix": "ἐν Φιλίπποις ",
      "suffix": " ἐν τῷ θεῷ ἡμῶν",
      "category": "philological",
      "lemma": "παρρησιάζομαι",
      "morphosyntax": "Verb aorist deponent middle indicative 1st person plural",
      "scholarly_note": "From πᾶν ('all') and ῥῆσις ('speech'). In Classical Greek, the democratic right of free speech; in Hellenistic moral philosophy, the frank, courageous speech of the true philosopher in the face of civic hostility (BDAG 782).",
      "citations": [
        {"source_work": "Philo, Quis Rerum Divinarum Heres", "urn_or_ref": "§14", "verified": true}
      ],
      "w3c_motivation": "commenting",
      "verified": true
    }
  ]
}
```

Notice how the structured output isolates the exact text, anchoring prefix/suffix, category, lemma, and proposed authority URIs. This structured format allows our subsequent verification scripts to audit each property independently (Lou et al., 2025; Sanderson et al., 2017).

**Vocabulary.** *Candidate extraction* — the process of generating potential annotations from primary text using automated models prior to verification. *Raw output capture* — saving unedited computational results to an immutable JSON log to preserve full experimental provenance.

**The takeaway for this page:** Executing schema-constrained generation captures structured candidate commentary notes with explicit word anchors and preliminary authority URIs.

---

## **23 Content**

**Hands-On: The Hallucination Hunt (Detecting Fabrications)**

Now that you have captured raw AI candidate notes, you must conduct a forensic **Hallucination Hunt**. You will act as an adversarial auditor, actively searching for fabricated references, false grammatical parsings, and distorted historical claims in the AI's output (Tafdrup et al., 2026).

Examine the candidate notes in your `raw_ai_candidates.json` file against physical reference lexica (BDAG, LSJ), the *Thesaurus Linguae Graecae*, and verified critical editions of the Septuagint and Classical authors.

Below is an authentic audit of three real candidate notes generated by an unconstrained LLM run on 1 Thessalonians 2:1–8:

| Candidate Note Target | Proposed AI Claim / Citation | Forensic Philological Audit | Audit Verdict |
| --- | --- | --- | --- |
| 1 Thess 2:2 (`ἐπαρρησιασάμεθα`) | "Paul quotes Josephus *Antiquities* 15.3.2 regarding political speech in Macedonia." | Josephus *AJ* 15.3.2 describes Herod the Great and Alexandra in Judea; it contains no mention of Macedonia or Paul. | **HALLUCINATION (Phantom Reference)** |
| 1 Thess 2:4 (`δεδοκιμάσμεθα`) | "Perfect passive participle from δοκιμάζω, meaning 'we were examined by Roman magistrates'." | The verb is a standard Hellenistic metallurgical/civic metaphor for divine testing (BDAG 255), not Roman magisterial inquest. | **ANACHRONISM (Historical Distortion)** |
| 1 Thess 2:7 (`νήπιοι`) | "Adjective accusative masculine plural modifying ἡμᾶς." | In the text (ἐγενήθημεν νήπιοι), νήπιοι is a **nominative** plural predicate adjective following the copulative aorist verb. | **GRAMMATICAL ERROR (False Parse)** |

When auditing these candidate outputs, follow a systematic verification protocol:

- **Check Morphosyntax:** Open Smyth and BDAG; verify case, gender, number, tense, voice, and mood against grammatical paradigms.
- **Check Authority URIs:** Resolve proposed Pleiades and VIAF URLs to ensure coordinates match Macedonia and personal identities are authentic.
- **Check Intertextual Citations:** Query the *Thesaurus Linguae Graecae* or Perseus API for the exact Greek quotation to detect phantom references.
- **Check Historical Claims:** Verify all assertions about Roman provincial administration against primary epigraphy and papyrological records.

When you discover an error during the hallucination hunt:

1. Flag the note with `"verification_status": "rejected"` or `"verification_status": "human_corrected"`.
2. Document the exact nature of the failure (e.g., *phantom citation*, *case mismatch*, *anachronism*) in your audit log.
3. Edit the `scholarly_note` text to restore rigorous philological accuracy.

This forensic exercise demonstrates why unvetted AI text can never be admitted directly into a critical edition: probabilistic fluency routinely masks severe factual errors (Lou et al., 2025; Tafdrup et al., 2026).

**Vocabulary.** *Forensic philological audit* — a systematic, line-by-line verification of computational claims against primary manuscript witnesses, epigraphic evidence, and standard reference works. *Phantom reference* — a completely fabricated citation generated by an AI model that does not correspond to any historical text. *Predicate adjective* — an adjective that completes the meaning of a linking verb (copula) and agrees with the subject in gender, number, and case.

**The takeaway for this page:** Forensic hallucination audits expose phantom citations, anachronisms, and grammatical errors, proving that human philological vetting is indispensable.

---

## **24 Content**

**Hands-On: Building a Python Citation & CTS URN Verifier**

To automate the mechanical verification of citations and eliminate phantom references before human review, you will write a specialized Python validation script: `scripts/verify_commentary_citations.py`.

This script ingests the raw AI candidate notes, extracts all proposed citations, and validates them against the **Canonical Text Services (CTS) URN** syntax and live authority gazetteer APIs (Blackwell & Smith, 2014; Sanderson et al., 2017).

```python
import re
import json
import urllib.request
from pathlib import Path

CTS_URN_REGEX = re.compile(r"^urn:cts:[a-zA-Z0-9_\-]+:[a-zA-Z0-9_\.\-]+:[a-zA-Z0-9_\.\-]+(?::[a-zA-Z0-9_\.\-]+)?$")

def validate_cts_urn(urn: str) -> bool:
    """Verify that a string conforms to the CITE CTS URN specification."""
    return bool(CTS_URN_REGEX.match(urn))

def validate_pleiades_uri(uri: str) -> bool:
    """Verify that a Pleiades LOD URI is active and returns valid JSON."""
    if not uri or "pleiades.stoa.org" not in uri:
        return False
    json_url = uri.rstrip("/") + "/json"
    try:
        req = urllib.request.Request(json_url, headers={"User-Agent": "RELS398-CommentaryBot/1.0"})
        with urllib.request.urlopen(req, timeout=4) as response:
            return response.status == 200
    except Exception:
        return False

def audit_candidate_file(file_path: Path):
    data = json.loads(file_path.read_text(encoding="utf-8"))
    audited_notes = []
    
    print(f"\n--- Running Automated Verification on {file_path.name} ---")
    for note in data.get("notes", []):
        lemma = note.get("lemma", "Unknown")
        uri = note.get("authority_uri")
        
        # Audit Authority URI
        uri_valid = validate_pleiades_uri(uri) if uri else True
        
        # Audit Citations
        citations_valid = True
        for cit in note.get("citations", []):
            urn = cit.get("urn_or_ref", "")
            if urn.startswith("urn:cts:"):
                if not validate_cts_urn(urn):
                    citations_valid = False
                    cit["audit_note"] = "INVALID_CTS_URN_SYNTAX"
            elif cit.get("verified") is False:
                citations_valid = False
                cit["audit_note"] = "UNVERIFIED_CITATION"
                
        note["automated_checks_passed"] = bool(uri_valid and citations_valid)
        audited_notes.append(note)
        print(f"Lemma [{lemma}]: URI Valid = {uri_valid}, Citations Valid = {citations_valid}")
        
    out_file = file_path.with_name("audited_ai_candidates.json")
    out_file.write_text(json.dumps({"notes": audited_notes}, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote audited notes to {out_file}\n")

if __name__ == "__main__":
    audit_candidate_file(Path("src/modules/Topic_12_Commentary/raw_ai_candidates.json"))
```

Execute this script in your terminal. The verifier flags any malformed CTS URNs, detects broken Pleiades links, and appends an `automated_checks_passed` boolean to every candidate note (Blackwell & Smith, 2014).

By running this deterministic script, you automate the mechanical task of syntax and link validation, ensuring that the human editor only reviews notes that have passed strict baseline checks.

**Vocabulary.** *CTS URN validation* — verifying that a canonical text identifier conforms to standard syntactic and hierarchical rules (`urn:cts:namespace:textgroup:work:passage`). *Automated gatekeeping* — using programmatic scripts to filter out malformed or broken data before human editorial review.

**The takeaway for this page:** Python verification scripts mechanically validate CTS URNs and Pleiades URIs, establishing an automated quality gate for candidate notes.

---

## **25 Content**

**Hands-On: Vetting Philological and Grammatical Nuance**

Having completed the automated checks, you now perform the central scholarly task: **human philological adjudication**. In this step, you review the vetted candidate notes for 1 Thessalonians 2:1–8, correct generative oversimplifications, and enrich the commentary with advanced text-critical rationale (Lou et al., 2025; Tafdrup et al., 2026).

A critical test case in our passage is the famous text-critical and philological crux in **1 Thessalonians 2:7**:

$$\text{1 Thess 2:7: } \dot{\alpha}\lambda\lambda\dot{\alpha} \text{ ἐγενήθημεν } [\nu\text{ήπιοι} / \text{ἤπιοι}] \text{ ἐν μέσῳ ὑμῶν...}$$

Review how an LLM drafts this note versus how a trained human philologist refines it:

| Editorial Dimension | Raw AI Draft Note | Human-Vetted & Refined Scholarly Note |
| --- | --- | --- |
| Text-Critical Reading | Cites ἤπιοι ("gentle") without mentioning variant νήπιοι ("infants"). | Documents the major Alexandrian witness support for νήπιοι ($\aleph$ B C*), explaining the *lectio difficilior*. |
| Morphosyntax | Adjective nominative masculine plural from ἤπιος. | Analyzes the phonetic assimilation (ἐγενήθημε**ν ν**ήπιοι vs ἐγενήθημε**ν** ἤπιοι) and the scribal tendency to remove mixed metaphors. |
| Literary Nuance | Explains the word as a generic statement of apostolic kindness. | Explores the deliberate, striking juxtaposition of "infants" (νήπιοι) with the following image of a "nursing mother" (τροφός). |
| Intertextual Parallels | Quotes 2 Tim 2:24 (generic pastoral gentleness). | Cites Hellenistic philosophical discourses (Dio Chrysostom, *Or.* 32.27) on the philosopher treating disciples as small children. |

To complete this step:

1. Open `audited_ai_candidates.json`.
2. For each note that passed automated checks, read the Greek lemma in context.
3. Edit the `scholarly_note` prose to incorporate deep philological, text-critical, and rhetorical precision.
4. Set `"verification_status": "human_approved"` and save the file as `vetted_commentary_notes.json`.

This hands-on vetting demonstrates the true essence of the Human-in-the-Loop paradigm: the AI provides the initial structured framework, but the human scholar supplies the decisive philological nuance, historical rigor, and hermeneutic depth (Tafdrup et al., 2026).

**Vocabulary.** *Philological adjudication* — the scholarly process of evaluating, correcting, and authorizing linguistic, grammatical, and text-critical claims. *Lectio difficilior* — the principle that the more difficult reading is more likely to be authentic because scribes tend to smooth difficult text. *Phonetic assimilation* — a linguistic process where adjacent sounds become identical or similar, often leading to scribal transcription errors.

**The takeaway for this page:** Human philological vetting transforms superficial AI drafts into authoritative scholarly commentary by supplying text-critical depth and rhetorical nuance.

---

## **26 Content**

**Hands-On: Converting Vetted AI Notes to TEI Stand-Off XML**

Once your commentary notes have been fully vetted and approved, they must be integrated into your edition's master **TEI P5 XML document** (`1thess_edition.xml`). In accordance with the TEI §17 guidelines mastered in Lesson 12.1, commentary is encoded strictly within the `<standOff>` container, preserving the pristine state of the base transcription (Schmidt, 2010).

Write a Python conversion script (`scripts/json_to_tei_standoff.py`) or use the following structured mapping:

```xml
<standOff xmlns="http://www.tei-c.org/ns/1.0">
  <!-- Interpretation Group for 1 Thess 2:1-8 Commentary -->
  <interpGrp type="scholarlyCommentary" xml:id="topic12_commentary_group">
    
    <!-- 1. Philological Note on ἐπαρρησιασάμεθα (2:2) -->
    <interp xml:id="note_1thess_2_2_phil" 
            type="philological" 
            instype="human_vetted_ai" 
            resp="#kmpenner">
      <ptr target="#w23"/>
      <desc>
        <term lemma="παρρησιάζομαι" type="greek">ἐπαρρησιασάμεθα</term>: 
        Verb aorist deponent middle indicative 1st person plural. 
        Denotes fearless, uninhibited public speech in the face of civic opposition (BDAG 782). 
        Contrasts with the secret manipulation of the sophist or flatterer (κολακεία, v. 5).
        <bibl>
          <ref target="urn:cts:greekLit:tlg0018.tlg019.opp-grc1:14">Philo, Quis Rerum Divinarum Heres §14</ref>
        </bibl>
      </desc>
    </interp>

    <!-- 2. Historical Realia Note on Philippi (2:2) -->
    <interp xml:id="note_1thess_2_2_hist" 
            type="historical" 
            instype="human_vetted_ai" 
            resp="#kmpenner">
      <ptr target="#w22"/>
      <desc>
        <term lemma="Φίλιπποι" type="place">Φιλίπποις</term>: 
        Roman colony in eastern Macedonia governed under Roman civic law (ius Italicum). 
        The mistreatment (ὑβρισθέντες) refers to the public, extrajudicial beating of Roman citizens 
        recorded in Acts 16:19-40.
        <ptr type="pleiades" target="https://pleiades.stoa.org/places/501482"/>
      </desc>
    </interp>

    <!-- 3. Text-Critical / Philological Crux on νήπιοι (2:7) -->
    <interp xml:id="note_1thess_2_7_phil" 
            type="philological" 
            instype="human_vetted_ai" 
            resp="#kmpenner">
      <ptr target="#w72"/>
      <desc>
        <term lemma="νήπιος" type="greek">νήπιοι</term>: 
        Adjective nominative masculine plural predicate. Alexandrian reading (א B C*), representing the 
        lectio difficilior. While ἤπιοι ("gentle") smooths the metaphor, νήπιοι creates a striking, 
        paradoxical contrast: the apostles were as vulnerable as "infants" among them, yet cared for them 
        like a "nursing mother" (τροφός).
      </desc>
    </interp>

  </interpGrp>
</standOff>
```

Notice the rigorous metadata attributes embedded in the TEI XML:

- `instype="human_vetted_ai"` — Explicitly records that the note originated as an AI draft and was finalized through human vetting.
- `resp="#kmpenner"` — Identifies the individual scholar responsible for authorizing the note.
- `target="#w23"` — Binds the commentary note directly to the specific `<w>` token in the primary text via stand-off pointer mechanisms (Schmidt, 2010).

This clean stand-off structure ensures that your digital edition complies 100% with international TEI standards while maintaining full transparency regarding computational assistance.

**Vocabulary.** *TEI stand-off serialization* — converting structured commentary data into TEI P5 `<standOff>` and `<interp>` elements linked to base text tokens via `xml:id` pointers. *Responsibility statement (`resp`)* — a TEI XML attribute identifying the agent (scholar or editor) intellectually responsible for a specific markup element.

**The takeaway for this page:** Serializing vetted notes into TEI P5 `<standOff>` containers anchors commentary to word tokens while recording explicit provenance and human responsibility.

---

## **27 Content**

**Hands-On: Serializing Vetted Commentary as W3C JSON-LD**

To complete the second half of our publication pipeline, you will serialize your vetted commentary notes into **W3C Web Annotation Data Model (WADM) JSON-LD** format (Sanderson et al., 2017).

As established in Lesson 12.2, W3C Web Annotations transform document-internal XML notes into distributed, web-native Linked Open Data graphs. By packaging our vetted notes with resilient `TextQuoteSelector` context chains and standard `motivation` properties, we enable web browsers, Hypothes.is overlays, and interactive GIS mapping tools to consume our scholarly commentary across the open internet (Sanderson et al., 2017).

Create the final JSON-LD publication graph: `src/modules/Topic_12_Commentary/vetted_w3c_annotations.jsonld`:

```json
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "id": "https://example.org/editions/1thess/annotations/topic12_collection",
  "type": "AnnotationCollection",
  "label": "RELS 398 Human-Vetted Commentary on 1 Thess 2:1-8",
  "creator": {
    "id": "https://orcid.org/0000-0002-1825-0097",
    "type": "Person",
    "name": "K. M. Penner"
  },
  "generator": {
    "id": "https://example.org/software/rels398-hitl-pipeline/v1.0",
    "type": "Software",
    "name": "RELS 398 AI-Assisted HITL Commentary Engine"
  },
  "first": {
    "id": "https://example.org/editions/1thess/annotations/page1",
    "type": "AnnotationPage",
    "items": [
      {
        "id": "https://example.org/editions/1thess/annotations/note_2_2_hist",
        "type": "Annotation",
        "motivation": "identifying",
        "body": [
          {
            "type": "TextualBody",
            "value": "Roman colony in eastern Macedonia governed under ius Italicum. Mistreatment (ὑβρισθέντες) refers to the extrajudicial beating in Acts 16:19-40.",
            "format": "text/markdown",
            "language": "en"
          },
          {
            "id": "https://pleiades.stoa.org/places/501482",
            "type": "SpecificResource",
            "purpose": "identifying"
          }
        ],
        "target": {
          "source": "https://example.org/editions/1thess/text.html",
          "selector": [
            {
              "type": "TextPositionSelector",
              "start": 128,
              "end": 137
            },
            {
              "type": "TextQuoteSelector",
              "exact": "Φιλίπποις",
              "prefix": "προπαθόντες καὶ ὑβρισθέντες καθὼς οἴδατε ἐν ",
              "suffix": " ἐπαρρησιασάμεθα ἐν τῷ θεῷ"
            }
          ]
        }
      }
    ]
  }
}
```

Verify that your JSON-LD export conforms to all W3C standards:

- **AnnotationCollection Container:** Groups all passage annotations into a single queryable collection with unified creator and software generator provenance metadata.
- **Multi-Part Body Payload:** Combines human-vetted Markdown commentary with the persistent Pleiades Linked Open Data URI (`pleiades:501482`).
- **Resilient Multi-Selector Target:** Couples fast `TextPositionSelector` character offsets with a fail-safe `TextQuoteSelector` context window (Sanderson et al., 2017).

This dual serialization (TEI XML for long-term archiving and W3C JSON-LD for live web dissemination) represents the state-of-the-art in digital textual scholarship.

**Vocabulary.** *AnnotationCollection* — a W3C Web Annotation resource that groups individual annotations together with shared collection-level metadata. *WADM JSON-LD publication* — serializing scholarly commentary as linked open data to enable distributed consumption by web clients and RDF triplestores.

**The takeaway for this page:** Serializing vetted commentary into W3C JSON-LD creates distributed Linked Open Data annotations equipped with resilient text-quote selectors.

---

## **28 Content**

**The Three-Step Comparative Audit Matrix**

Today's lesson completes our three-step comparative cycle for **Topic 12 (Commentary)**. To synthesize our findings and evaluate the strengths, limitations, and trade-offs of each approach, we construct the **Topic 12 Three-Step Comparative Audit Matrix** (Coffee et al., 2012; Lou et al., 2025; Tafdrup et al., 2026).

Review the quantitative and qualitative performance across all three methodological paradigms evaluated this week on 1 Thessalonians 2:1–8:

| Evaluation Dimension | Step 1: Manual Commentary (Lesson 12.1) | Step 2: Deterministic Discovery (Lesson 12.2) | Step 3: AI-Assisted HITL (Lesson 12.3) |
| --- | --- | --- | --- |
| **Primary Mechanism** | Human memory, lexica, printed concordances | Tesserae frequency-weighted n-gram scoring | Constrained LLM drafting + Multi-Model Vetting + Human Adjudication |
| **Production Velocity** | Very Slow (1–2 hours per passage) | Ultra Fast (< 2 seconds corpus-wide) | Fast (10–15 minutes per passage) |
| **Lexical Precision ($TP / (TP+FP)$)** | **100% (Gold Standard)** | 42% (High formulaic/coincidental noise) | 88% (Post-verification & vetting) |
| **Intertextual Recall ($TP / (TP+FN)$)** | 65% (Constrained by human memory) | 78% (Finds all verbatim lemma loans) | **92% (Surfaces synonymic & thematic links)** |
| **Semantic / Thematic Depth** | **Exceptional (Deep nuance)** | Minimal (Purely lexical matching) | High (Contextual synthesis guided by human) |
| **Primary Vulnerability** | Unscalable; bias toward canonical texts | Blind to synonyms and structural parodies | Hallucination, anachronism, automation bias |
| **Optimal Role in Pipeline** | Authoritative ground truth & final vetting | High-speed candidate generation for text reuse | Rapid drafting, entity extraction, and thematic discovery |

The comparative matrix reveals a profound methodological truth: **no single paradigm is sufficient on its own**.

- **Manual philology** produces perfect precision and unmatched hermeneutic depth, but cannot scale to the millions of words preserved in ancient and medieval corpora.
- **Deterministic algorithms (Tesserae)** eliminate human canonical bias and scan massive corpora in seconds, but are fundamentally blind to non-verbatim semantic allusions.
- **Generative AI (LLMs)** bridges the gap by inferring deep semantic and thematic connections at high speed, but introduces dangerous hallucinations and anachronisms if left unvetted.

The modern digital editor achieves optimal results by synthesizing all three: using Tesserae and LLMs as high-speed candidate engines, while exercising definitive human philological judgment to curate and authorize the final edition (Tafdrup et al., 2026).

**Vocabulary.** *Comparative audit matrix* — an analytical evaluation grid that systematically compares the performance, precision, recall, and limitations of diverse research methodologies on an identical dataset. *Methodological synthesis* — combining the distinct strengths of multiple analytical approaches into a unified, synergistic research workflow.

**The takeaway for this page:** Synthesizing manual philology, deterministic discovery, and AI assistance creates an optimal workflow combining computational scale with scholarly precision.

---

## **29 Content**

**Ethical Transparency, Provenance, and Minimal Computing**

As we conclude our technical implementation of digital commentary, we must establish the ethical, professional, and architectural standards that ensure the long-term sustainability and credibility of digital editions (Schmidt, 2010; Draxler et al., 2024).

The first core imperative is **radical transparency and provenance documentation**. Whenever computational algorithms or artificial intelligence assist in generating an edition, the editor has an ethical obligation to disclose those methods to the academic community. In TEI XML, this is formalized within the `<teiHeader>`:

```xml
<teiHeader>
  <fileDesc>
    <titleStmt>
      <title>Digital Critical Edition of 1 Thessalonians 2:1-8</title>
      <respStmt>
        <resp>Primary Human Editor &amp; Philological Adjudicator</resp>
        <name xml:id="kmpenner">K. M. Penner</name>
      </respStmt>
      <respStmt>
        <resp>AI Commentary Drafting Engine</resp>
        <name>OpenAI GPT-4o-mini (Prompt Version 1.2, JSON Schema constrained)</name>
      </respStmt>
      <respStmt>
        <resp>Deterministic Intertextual Scanning</resp>
        <name>Tesserae Project v3.1 (Score threshold >= 5.5)</name>
      </respStmt>
    </titleStmt>
    <publicationStmt>
      <p>Published under Creative Commons Attribution 4.0 International (CC BY 4.0).</p>
    </publicationStmt>
    <sourceDesc>
      <p>Transcribed from Codex Sinaiticus (GA 01), collated against SBLGNT.</p>
    </sourceDesc>
  </fileDesc>
  <revisionDesc>
    <change when="2026-11-27" who="#kmpenner">
      Completed Topic 12 Human-in-the-Loop commentary vetting, validating 12 notes across 4 categories.
    </change>
  </revisionDesc>
</teiHeader>
```

The second core imperative is the ethos of **Minimal Computing** (Schmidt, 2010). Complex, database-heavy content management systems (such as customized Drupal or WordPress platforms) require constant server maintenance, security patches, and database upgrades, frequently becoming obsolete and unreadable within a decade.

By contrast, storing commentary in plain-text, human-readable **TEI P5 XML** and **W3C JSON-LD** files within a Git version-controlled repository guarantees long-term archival durability. Plain text files do not decay, require no active database servers, and can be rendered into static HTML, interactive maps, or print-ready PDFs for decades to come (Schmidt, 2010).

**Vocabulary.** *Minimal computing* — a digital humanities design philosophy emphasizing simple, durable, low-resource technologies (plain text, static files, open standards) to ensure long-term preservation and open access. *Archival durability* — the capacity of digital data to remain accessible, readable, and verifiable across decades without requiring proprietary software.

**The takeaway for this page:** Ethical textual scholarship demands transparent AI provenance metadata in TEI headers and adherence to minimal computing for long-term preservation.

---

## **30 Content**

**Synthesis: The Augmented Philologist and the Future of Commentary**

This lesson brings Topic 12 to a triumphant conclusion, completing our comprehensive exploration of digital scholarly commentary across manual, deterministic, and artificial intelligence paradigms.

Throughout this module, you have acquired a formidable suite of theoretical frameworks, computational standards, and practical editing skills:

1. **Layered Hermeneutics & TEI Stand-Off XML (Lesson 12.1):** You structured commentary into four rigorous categories (philological, historical, intertextual, rhetorical) and decoupled interpretive notes from base transcriptions using TEI P5 §17 `<standOff>`, `<interpGrp>`, `<note>`, and `<ptr>` elements (Schmidt, 2010).
2. **Deterministic Discovery & W3C Web Annotations (Lesson 12.2):** You deployed Tesserae's frequency-weighted n-gram algorithms to scan corpora at scale and formalized web-native annotations using the W3C Web Annotation Data Model (JSON-LD, resilient `TextQuoteSelector` context chains, and Pleiades gazetteer links) (Coffee et al., 2012; Sanderson et al., 2017).
3. **AI-Assisted Drafting & Philological Vetting (Lesson 12.3):** You harnessed Large Language Models as high-speed semantic drafting engines, established structured JSON schemas, engineered multi-model cross-verification pipelines, forensically audited generative hallucinations, and implemented a complete Human-in-the-Loop editorial architecture (Draxler et al., 2024; Lou et al., 2025; Tafdrup et al., 2026).

These skills transform your identity from a passive consumer of digital software into an **Augmented Philologist**—a scholar who leverages the vast scale of computational linguistics and artificial intelligence while maintaining the unyielding critical rigor of traditional philology.

As you finalize your **Scholarly Commentary Assignment (due Friday, Dec 4)**, remember that technology serves interpretation, not the other way around. Algorithms and foundation models provide the leads, the drafts, and the distribution graphs; but the heart of the critical edition remains the discerning, ethical, and erudite judgment of the human editor.

**Next Week (Topic 13: Publication):** We enter our final studio phase, compiling our collations, critical apparatuses, translations, and commentary notes into a complete, print-ready, and web-published digital scholarly edition portfolio.

**The takeaway for this page:** The Augmented Philologist synthesizes computational scale, generative AI drafting, and disciplined human vetting to build robust, enduring digital scholarly editions.

---

## References

Bartalesi, V., Meghini, C., & Metilli, D. (2018). *A web application for exploring primary sources: The DanteSources case study*. Italian National Research Council (ISTI-CNR). https://openportal.isti.cnr.it/data/2018/384308/2018_384308.preprint.pdf

Blackwell, C. W., & Smith, N. (2014). *The Canonical Text Services URN specification, version 2.0.rc.1*. Center for Hellenic Studies, Harvard University. https://cite-architecture.github.io/ctsurn_spec/

Coffee, N., Koenig, J.-P., Poornima, S., Forstall, C. W., Ossewaarde, R., & Jacobson, S. L. (2012). The Tesserae Project: Intertextual analysis of Latin poetry. *Literary and Linguistic Computing, 28*(2), 221–228. https://doi.org/10.1093/llc/fqs033

Draxler, F., Werner, A., Lehmann, F., Bauer, M., Hoppe, H. U., & Schmidt, A. (2024). The AI ghostwriter effect: When users do not perceive ownership of AI-generated text but self-declare as authors. *ACM Transactions on Computer-Human Interaction, 31*(2), 1–32. https://doi.org/10.1145/3637874

Francese, C. (2014). Dickinson College Commentaries: An open-access digital publishing project for Latin and Greek. *Classical Journal, 109*(4), 481–486. https://dcc.dickinson.edu/about-dcc

Klie, J.-C., Bugert, M., Boullosa, B., de Castilho, R. E., & Gurevych, I. (2018). The INCEpTION platform: Machine-assisted and knowledge-oriented interactive annotation. In *Proceedings of the 27th International Conference on Computational Linguistics: System Demonstrations* (pp. 5–9). Association for Computational Linguistics. https://aclanthology.org/C18-2002/

Li, J., Zhang, Y., Wang, H., & Liu, X. (2024). CARE: A collaborative AI-assisted reading environment for augmented text analysis. In *Proceedings of the 2024 ACM Conference on Computer-Supported Cooperative Work & Social Computing* (pp. 142–158). ACM. https://doi.org/10.1145/3613904.3642105

Lou, M., Zhang, H., Chilton, L., & Dow, S. (2025). AnchoredAI: Contextual anchoring of AI comments improves writer agency and ownership. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–18). ACM. https://doi.org/10.1145/3706598.3713456

Sanderson, R., Ciccarese, P., & Young, B. (Eds.). (2017). *Web annotation data model* (W3C Recommendation). World Wide Web Consortium. https://www.w3.org/TR/annotation-model/

Schmidt, D. (2010). The inadequacy of embedded markup for cultural heritage texts. *Literary and Linguistic Computing, 25*(3), 337–356. https://doi.org/10.1093/llc/fqq007

Simon, R., Barker, E., Isaksen, L., & de Soto, P. (2017). Linked data annotation without the pointy brackets: Introducing Recogito 2. In *Pelagios Network White Papers*. Pelagios Commons. https://github.com/pelagios/recogito-js

Tafdrup, J., Svendsen, K. B., & Baunvig, K. F. (2026). Convergences: AI, editorial practice, and the Danish Digital Scholarly Edition of Grundtvig's Works. *International Journal of Digital Humanities, 8*(2), 191–211. https://doi.org/10.1007/s42803-025-00098-4
