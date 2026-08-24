# RELS 398 / ENGL 398: Research Prompts for Google Scholar Labs & Gemini Deep Research

This master compendium provides the complete two-stage research pipeline for all 13 weekly topics in **RELS 398.10 / ENGL 398.10 (ST: Digital Methods for Historical Documents)**, Fall 2026.

The curriculum follows a cumulative **learning-by-project** methodology where students select a manuscript passage in Week 1 and construct a complete, TEI-conformant digital critical edition across 10 progressive assessment layers. Standard weekly modules employ a **three-step comparative cycle**:
1. **Tuesday (Manual):** Plain-text authoring, transcription, or linguistic parsing to establish an authoritative **scholarly ground truth**.
2. **Wednesday (Deterministic):** Applying specialized, rule-based computational tools (e.g., Transkribus HTR models, CollateX, CLTK pipelines).
3. **Friday (AI-Assisted):** Evaluating LLMs and agentic assistants against the ground truth to calculate character/word error rates (CER/WER), audit hallucinations, and adjudicate editorial choices.

---

## Two-Stage Research Pipeline Workflow:

1. **Stage 1: Google Scholar Labs Search**
   - Submit the natural-language query into [Google Scholar Labs](https://scholar.google.com/scholar_labs/search).
   - Capture AI synthesis cards and download up to **10 relevant, peer-reviewed PDFs** into `03_Research/` (or `raw/readings/Topic_NN/`).
   - Log results in `SCHOLAR_LABS_PAPERS.md`.

2. **Stage 2: Gemini Deep Research**
   - Upload the downloaded Scholar Labs PDFs to Gemini Deep Research.
   - Run the structured prompt below to generate an exhaustive, evidence-based research report with comparative methodological evaluations, digital-edition case studies, and complete DOI/URL citations.

---

## Topic 1: Orientation, Polytonic Greek, Manuscript Selection & Local Git Version Control
*Week 1 • Wed Sep 2 (#1) / Fri Sep 4 (#2)*

**Course Context & Primary Materials:** `Finney, "Manuscript Markup" (pp. 323–360); Griffitts §3.4.1; TEI Guidelines vi.2`  
**Methodological Context:** *Orientation week (no three-step cycle).* Local Git version control fundamentals (repository initialization, staging, atomic commits, diffs, and commit log audit trails for tracking AI vs manual edits); Unicode polytonic Greek keyboards and fonts; Oxygen XML / VS Code; selection of primary manuscript passage by Fri Sep 4.

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How do local Git version control workflows and Unicode polytonic Greek standards support undergraduate digital scholarly editing, manuscript selection, and reproducible editorial audit trails?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How do local Git version control workflows and Unicode polytonic Greek standards support undergraduate digital scholarly editing, manuscript selection, and reproducible editorial audit trails?

Core Thesis to Substantiate & Evaluate: Digital editing of historical documents requires foundational local Git version control discipline (atomic commits, clear commit messages, diff tracking, and AI-usage logging) alongside robust Unicode polytonic Greek infrastructure to make undergraduate manuscript transcription reproducible, accountable, and pedagogically sound.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities / textual editing instructors).
2. Technical, Methodological & Historical Foundations (Unicode normalization forms NFC/NFD, polytonic Greek character sets, legacy encodings; Git version control architecture, tree objects, atomic commits, diff algorithms, and commit logs as editorial provenance).
3. Applied Implementation & Editorial Dimensions (Establishing a reproducible local editing repository, commit hygiene, documenting AI vs human interventions in git history, keyboard mappings, and font rendering across OS platforms).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of digital Greek editions illustrating character encoding challenges and version-controlled editorial workflows).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Actionable guidelines for establishing a reproducible editing environment and local Git workflow).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs, including Unicode, Git, and TEI specifications).
```

---

## Topic 2: Manuscript Cataloguing, Metadata & TEI XML Fundamentals
*Week 2 • Tue Sep 8 (#3) / Wed Sep 9 (#4) / Fri Sep 11 (#5)*

**Course Context & Primary Materials:** `Griffitts §3.4.2, 3.6.1, 4.1; TEI Guidelines v.1–3; Ceriani, Codex Marchalianus introduction`  
**Methodological Cycle:** **Tue** hand-write `teiHeader` in text editor; **Wed** validate against TEI schema in Oxygen and construct RDF triples / CTS URNs; **Fri** AI-assisted metadata enrichment and entity extraction scored against manual header.

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How do RDF linked-data models and TEI Header schemas structure manuscript metadata and document validation in digital scholarly editions, and how do rule-based validation and AI metadata enrichment compare?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How do RDF linked-data models and TEI Header schemas structure manuscript metadata and document validation in digital scholarly editions, and how do rule-based validation and AI metadata enrichment compare?

Core Thesis to Substantiate & Evaluate: Manuscript cataloguing in the digital age depends on structured data schemas (TEI Header, RDF triples, CTS URNs) that formalize codicological description and validation rules, establishing the architectural foundation for downstream encoding and discovery while serving as a baseline to evaluate AI-generated metadata.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities instructors).
2. Technical, Methodological & Historical Foundations (Codicological metadata standards, TEI `teiHeader` architecture, RDF linked open data, CTS URN citation ontologies, XML schema validation with RNG/XSD).
3. Comparative Methodological Evaluation (Manual header authoring vs Oxygen schema validation vs LLM metadata generation and entity enrichment; error types and hallucinated catalogue records).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies, e.g., Pinakes, Bibliotheca Laureshamensis, or Syriaca.org).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Step-by-step guidance on structuring a TEI Header for historical manuscripts).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs).
```

---

## Topic 3: IIIF Image Delivery & Digital Paleography
*Week 3 • Tue Sep 15 (#6) / Wed Sep 16 (#7) / Fri Sep 18 (#8)*

**Course Context & Primary Materials:** `Griffitts §4.3–4.4; Havens, "Adobe Photoshop & Digital Paleography"`  
**Methodological Context:** *Infrastructure week (three-step cycle does not apply).* IIIF Image and Presentation APIs, manifest generation, canvas-to-text linking, multispectral imaging, and raking light paleography. *Cataloguing & Metadata Assignment due Fri Sep 18.*

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How does the International Image Interoperability Framework (IIIF) and multispectral imaging transform paleographical analysis and digital edition workflows for historical manuscripts?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How does the International Image Interoperability Framework (IIIF) and multispectral imaging transform paleographical analysis and digital edition workflows for historical manuscripts?

Core Thesis to Substantiate & Evaluate: IIIF image delivery combined with multispectral imaging standards enables interoperable, deep-zoom access to high-resolution manuscript witnesses, recovering damaged or palimpsestic readings and linking visual canvases directly to text transcription.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (Synthesis of image interoperability in manuscript scholarship).
2. Technical, Methodological & Historical Foundations (IIIF Image and Presentation APIs, Mirador/Universal Viewer integration, multispectral and reflectance transformation imaging [RTI], digital paleography methods).
3. Applied Implementation & Editorial Dimensions (Constructing IIIF manifests, spatial coordinates for folio/line binding, paleographical image enhancement in Photoshop).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies, e.g., Archimedes Palimpsest, Codex Sinaiticus, or Vatican Library IIIF implementations).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Practical checklist for building IIIF manifests and integrating image viewers).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs).
```

---

## Topic 4: Manuscript Transcription: Diplomatic Ground Truth, HTR & LLMs
*Week 4 • Tue Sep 22 (#9) / Wed Sep 23 (#10) / Fri Sep 25 (#11, Remote Delivery)*

**Course Context & Primary Materials:** `Transkribus User Guide; THREAD Documentation; Clemens & Graham, Introduction to Manuscript Studies; stoa.org transcription conventions`  
**Methodological Cycle:** **Tue** manual diplomatic transcription in text editor (establishing scholarly ground truth); **Wed** Transkribus baseline detection and HTR model inference; **Fri (remote)** multimodal LLM transcription and correction.

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How effective are Handwritten Text Recognition (HTR) platforms like Transkribus and large language models compared to manual diplomatic transcription in generating accurate text from historical manuscripts?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How effective are Handwritten Text Recognition (HTR) platforms like Transkribus and large language models compared to manual diplomatic transcription in generating accurate text from historical manuscripts?

Core Thesis to Substantiate & Evaluate: Automated HTR technologies (Transkribus) and multimodal LLMs substantially accelerate manuscript transcription workflows, but require human manual diplomatic transcription as an authoritative ground truth against which automated baselines, character error rates (CER), and hallucinated readings can be measured.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis of manual, HTR, and LLM transcription paradigms).
2. Technical, Methodological & Historical Foundations (Diplomatic vs normalized transcription conventions, line/region segmentation, neural HTR architectures [PyLaia], vision-language LLMs in historical paleography).
3. Comparative Methodological Evaluation (Manual keystroke ground truth vs Transkribus HTR vs Multimodal LLM OCR; characteristic error distributions, ligatures, abbreviations, and damaged text handling).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies illustrating HTR and AI transcription in Greek or Latin manuscript projects).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Guidelines for training HTR models and establishing transcription quality thresholds).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs).
```

---

## Topic 5: Transcription Reconciliation, Double-Keying & Error Rate Evaluation
*Week 5 • Tue Sep 29 (#12) / Fri Oct 2 (#13) — Wed Sep 30 closed (Truth & Reconciliation)*

**Course Context & Primary Materials:** `Haaf et al., "Measuring Correctness of Double-Keying"; Griffitts §4.5.2`  
**Methodological Cycle:** *Two-step comparative week.* **Tue** manual double-keying comparison and consensus text building; **Fri** quantitative character and word error rate (CER/WER) scoring of HTR and AI passes against manual ground truth. *Transcription Assignment due Fri Oct 2.*

### Stage 1: Google Scholar Labs Natural-Language Query
```text
What methods and metrics, such as double-keying and character/word error rate (CER/WER) calculation, govern the reconciliation of manual, HTR, and AI-generated manuscript transcriptions into a consensus text?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: What methods and metrics, such as double-keying and character/word error rate (CER/WER) calculation, govern the reconciliation of manual, HTR, and AI-generated manuscript transcriptions into a consensus text?

Core Thesis to Substantiate & Evaluate: Systematic text reconciliation through double-keying error analysis and CER/WER benchmarking against manual ground truth is essential for quantifying AI/HTR performance, detecting systematic biases, and establishing an empirically verified consensus text for scholarly editing.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (Synthesis of reconciliation methodologies and error metrics in digital philology).
2. Technical, Methodological & Historical Foundations (Double-keying methodology [Haaf et al.], Levenshtein distance, CER and WER mathematical definitions, inter-annotator agreement metrics [Cohen's Kappa]).
3. Comparative Methodological Evaluation (Reconciling human transcriber disagreement vs scoring HTR and LLM output; error typology: substitutions, deletions, insertions, punctuation anomalies).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies on large-scale double-keying and HTR post-correction projects, e.g., Deutsches Textarchiv, IMPACT project).
5. Pedagogical Takeaways & Synthesis for Digital Editors (A practical guide to calculating CER/WER in Python and writing an audit reconciliation report).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs).
```

---

## Topic 6: Normalization, Orthographic Regularization & TEI Primary Sources
*Week 6 • Tue Oct 6 (#14) / Wed Oct 7 (#15) / Fri Oct 9 (#16)*

**Course Context & Primary Materials:** `TEI Guidelines ch. 11 (Representation of Primary Sources); Griffitts §4.6.1; Sabel, "Encoding of Variant Taxonomies in TEI"`  
**Methodological Cycle:** **Tue** manual regularization of iotacisms/orthographic variants recording editorial rules; **Wed** deterministic rule-based regex/Python normalization script; **Fri** AI-assisted regularizer checked against rule set and encoded in `tei:orig`/`tei:reg` or `tei:choice`.

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How should orthographic variation such as iotacism be normalized in historical manuscripts, and how do rule-based scripts and AI models compare when encoding TEI orig and reg elements?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How should orthographic variation such as iotacism be normalized in historical manuscripts, and how do rule-based scripts and AI models compare when encoding TEI orig and reg elements?

Core Thesis to Substantiate & Evaluate: Editorial normalization of orthographic variants must balance diplomatic fidelity against semantic searchability, utilizing TEI's primary source markup (orig/reg, choice) where deterministic rule-based transformations provide verifiable baselines against which AI-assisted regularizations are audited.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (Synthesis of orthographic regularization in historical languages).
2. Technical, Methodological & Historical Foundations (Historical phonology, iotacism and phonetic spellings in Hellenistic/Byzantine Greek, TEI Chapter 11 mechanisms: `choice`, `orig`, `reg`, `sic`, `corr`).
3. Comparative Methodological Evaluation (Manual philological normalization vs deterministic regex dictionary scripts vs neural/LLM regularizers; over-normalization risks and morphological ambiguity).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies, e.g., Duke Databank of Documentary Papyri / Papyri.info, Codex Sinaiticus).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Workflow for establishing an orthographic decision log and applying TEI markup).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs).
```

---

## Topic 7: Computational Collation & Variant Alignment Algorithms
*Week 7 • Tue Oct 20 (#17) / Wed Oct 21 (#18) / Fri Oct 23 (#19)*

**Course Context & Primary Materials:** `CollateX Documentation; Haentjens Dekker et al. (2015); Griffitts §4.6.2–3, 4.7; Robinson, "Collation and Textual Criticism"`  
**Methodological Cycle:** **Tue** manual collation of two witnesses on paper/table; **Wed** automated token alignment using CollateX (Gotoh alignment algorithm); **Fri** AI-assisted variant classification and adjudication. *Normalization Assignment due Fri Oct 23.*

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How do computational collation tools such as CollateX automate witness alignment and textual variant identification across manuscript traditions compared to manual collation?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How do computational collation tools such as CollateX automate witness alignment and textual variant identification across manuscript traditions compared to manual collation?

Core Thesis to Substantiate & Evaluate: Automated collation algorithms (CollateX) transform textual criticism by systematically aligning witnesses and generating reproducible variant tables, though algorithmic alignment must be checked against manual collation and adjudicated with rigorous variant taxonomy.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (Synthesis of automated text collation principles and algorithms).
2. Technical, Methodological & Historical Foundations (Traditional collation methods, Needleman-Wunsch / Gotoh alignment algorithms, variant graph data models, CollateX architecture).
3. Comparative Methodological Evaluation (Manual two-column collation vs CollateX alignment graph vs LLM variant identification; transpositions, omissions, additions, and punctuation handling).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies, e.g., ECM [Editio Critica Maior], Charles Darwin Manuscripts, Canterbury Tales Project).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Step-by-step CollateX Python tutorial and variant taxonomy classification guide).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs).
```

---

## Topic 8: Critical Apparatus Encoding & TEI Apparatus Structures
*Week 8 • Tue Oct 27 (#20) / Wed Oct 28 (#21) / Fri Oct 30 (#22)*

**Course Context & Primary Materials:** `TEI P5 Guidelines, Critical Apparatus module; Burnard, What is the Text Encoding Initiative?`  
**Methodological Cycle:** **Tue** hand-encode a critical apparatus entry in TEI XML; **Wed** automate apparatus generation from CollateX output and validate; **Fri** AI-assisted apparatus drafting, variant annotation, and consistency auditing. *Textual Variants & Collation Assignment due Fri Oct 30.*

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How does the TEI P5 Critical Apparatus module (tei:app, lem, rdg) structure manuscript variants, and how can automated pipelines and AI assistants support apparatus construction and error detection?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How does the TEI P5 Critical Apparatus module (tei:app, lem, rdg) structure manuscript variants, and how can automated pipelines and AI assistants support apparatus construction and error detection?

Core Thesis to Substantiate & Evaluate: Encoding a critical apparatus using TEI's `app`, `lem`, and `rdg` elements formalizes textual variance into machine-actionable data, allowing automated transformation from collation outputs while requiring human verification to catch structural and attribution errors.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (Synthesis of critical apparatus markup in digital textual scholarship).
2. Technical, Methodological & Historical Foundations (Print vs digital apparatus paradigms, TEI apparatus methods: location-referenced, double-end-point, parallel segmentation; `app`, `lem`, `rdg`, `witDetail`).
3. Comparative Methodological Evaluation (Hand-crafted TEI apparatus vs CollateX-to-TEI automated export vs AI-assisted apparatus generation; validation using TEI Critical Apparatus Toolbox).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies, e.g., Greek New Testament Virtual Manuscript Room [NTVMR], Homer Multitext).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Best practices for parallel segmentation and witness list encoding).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs).
```

---

## Topic 9: Lemmatization, Morphological Analysis & Historical POS Tagging
*Week 9 • Tue Nov 3 (#23) / Wed Nov 4 (#24) / Fri Nov 6 (#25)*

**Course Context & Primary Materials:** `CLTK (Classical Language Toolkit) Documentation; TEI Guidelines ch. 18; Schmid, "TreeTagger for Historical Languages"`  
**Methodological Cycle:** **Tue** parse and lemmatize passage by hand with print/digital lexicon (Liddell-Scott-Jones); **Wed** run deterministic CLTK / Morpheus / TreeTagger pipelines; **Fri** LLM-assisted morphological parsing scored against manual ground truth.

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How do computational toolkits like CLTK, Morpheus, and TreeTagger perform morphological tagging and lemmatization on historical language corpora compared to LLM-based parsing and manual lexicon lookups?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How do computational toolkits like CLTK, Morpheus, and TreeTagger perform morphological tagging and lemmatization on historical language corpora compared to LLM-based parsing and manual lexicon lookups?

Core Thesis to Substantiate & Evaluate: Automated morphological tagging and lemmatization pipelines (CLTK) enable scalable linguistic annotation of pre-modern corpora, but rule-based and neural taggers require systematic benchmarking against manual grammatical analysis to resolve dialectal ambiguity and non-standard orthography.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (Synthesis of computational morphology for ancient Greek and historical languages).
2. Technical, Methodological & Historical Foundations (Lemmatization principles, Universal Dependencies POS tagging, finite-state transducers [Morpheus], CLTK architecture, TEI Chapter 18 linguistic segment markup `w`, `m`, `lemma`, `pos`).
3. Comparative Methodological Evaluation (Manual grammatical parsing vs CLTK/TreeTagger pipelines vs LLM few-shot parsing; handling uncontracted forms, dialectal shifts, and ambiguous inflections).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies, e.g., Perseus Digital Library, PROIEL Treebank, Open Greek and Latin Project).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Tutorial on running CLTK lemmatizers and serializing output to TEI XML).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs).
```

---

## Topic 10: Edition Consolidation, GitHub Collaboration, Peer Review & Schema Validation
*Week 10 • Tue Nov 10 (#26) / Fri Nov 13 (#27) — Wed Nov 11 closed (Remembrance Day)*

**Course Context & Primary Materials:** *No new external readings; review project repository and edition files to date.*  
**Methodological Context:** *Consolidation and collaborative peer review week (no three-step cycle).* GitHub collaborative workflows (remotes, forks, pull requests, issue tracking); collaborative rubric-based peer review of editions in progress; validation sweep of every TEI file built so far; catch-up slack. *Linguistic Markup Assignment due Fri Nov 13.*

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How do GitHub collaborative workflows (forks, pull requests, issue tracking) combined with XML schema validation and structured peer review improve data integrity and student learning in digital scholarly editing projects?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How do GitHub collaborative workflows (forks, pull requests, issue tracking) combined with XML schema validation and structured peer review improve data integrity and student learning in digital scholarly editing projects?

Core Thesis to Substantiate & Evaluate: Cumulative digital scholarly editions require structured mid-project consolidation, combining distributed GitHub workflows (forking, pull requests, issue tracking, and peer review) with automated XML/Schematron schema validation to ensure data integrity, detect encoding inconsistencies, and foster collaborative scholarly critique.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (Synthesis of collaborative version control, quality control, and validation strategies in digital humanities projects).
2. Technical, Methodological & Historical Foundations (Distributed version control architectures, GitHub peer-review paradigms in humanities education, Schematron business rules, XML validation engines, and continuous integration [CI] in digital editing).
3. Applied Implementation & Editorial Dimensions (Managing forks and pull requests for textual review, designing structured peer-review rubrics for TEI XML documents, resolving encoding merge conflicts, and automated linting).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies, e.g., TEI Quality Assurance pipelines, Scholastic Commentaries and Texts Archive [SCTA], Perseids collaborative editing).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Audit checklist and GitHub peer-review rubric for evaluating an intermediate TEI edition).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs).
```

---

## Topic 11: Translation Alignment, Interlinear Glossing & Parallel Corpora
*Week 11 • Tue Nov 17 (#28) / Wed Nov 18 (#29) / Fri Nov 20 (#30)*

**Course Context & Primary Materials:** `Leipzig Glossing Rules; TEI §16.1 (Link & Alignment); Tiedemann, "Parallel Data Extraction"; Baumgardt, "Digital Interlinear Editions"`  
**Methodological Cycle:** **Tue** manual word glossing (Leipzig rules) and sentence alignment; **Wed** deterministic alignment software (Alpheios Alignment Editor, GIZA++); **Fri** AI-assisted alignment and gloss drafting, verified by hand.

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How do the Leipzig Glossing Rules and TEI linguistic alignment standards structure word-level glossing and sentence-level translation alignment in digital critical editions, and how do automated aligners and LLMs compare?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How do the Leipzig Glossing Rules and TEI linguistic alignment standards structure word-level glossing and sentence-level translation alignment in digital critical editions, and how do automated aligners and LLMs compare?

Core Thesis to Substantiate & Evaluate: Standardized interlinear glossing and parallel sentence alignment (TEI §16.1) bridge source-language morphology with target-language translation, creating dynamically linked bilingual editions that expose translational decisions to scholarly scrutiny.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (Synthesis of translation alignment and interlinear glossing in digital editions).
2. Technical, Methodological & Historical Foundations (The Leipzig Glossing Rules, sentence/word alignment algorithms [GIZA++, fast_align], TEI alignment mechanisms: `linkGrp`, `link`, `align`, `corresp`).
3. Comparative Methodological Evaluation (Manual glossing and alignment vs Alpheios/Ugarit toolkits vs LLM bilingual alignment; handling non-isomorphic syntax, idioms, and ellipsis).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies, e.g., Ugarit Translation Alignment Editor, Perseids Project, Interlinear Glossed Texts [IGT] repositories).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Step-by-step guide for authoring 4-line interlinear glosses and TEI alignment markup).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs).
```

---

## Topic 12: Scholarly Commentary, Intertextuality & Linked Open Annotation
*Week 12 • Tue Nov 24 (#31) / Wed Nov 25 (#32) / Fri Nov 27 (#33)*

**Course Context & Primary Materials:** `TEI §17 (Simple Analytic Mechanisms); Open Annotation Data Model; Vander Meulen, "Digital Commentary"`  
**Methodological Cycle:** **Tue** manual drafting and TEI encoding of philological commentary notes; **Wed** deterministic intertextual search (Tesserae) and Open Annotation / Hypothes.is linking; **Fri** AI-assisted commentary drafting, cross-referencing, and critical vetting for hallucinations. *Interlinear Glossing & Translation Alignment Assignments due Fri Nov 27.*

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How do TEI analytic mechanisms and the W3C Web Annotation / Open Annotation data model structure scholarly commentary and intertextual linking in digital editions, and what are the capabilities and hazards of AI-assisted commentary?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How do TEI analytic mechanisms and the W3C Web Annotation / Open Annotation data model structure scholarly commentary and intertextual linking in digital editions, and what are the capabilities and hazards of AI-assisted commentary?

Core Thesis to Substantiate & Evaluate: Structuring scholarly commentary as linked open annotations and machine-readable cross-references transforms traditional static footnotes into an extensible knowledge graph, though AI-drafted commentary must be strictly vetted for hallucinated citations, anachronistic interpretations, and missing context.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (Synthesis of digital commentary models and annotation standards).
2. Technical, Methodological & Historical Foundations (Genre of the critical commentary, TEI Chapter 17 `interpGrp`, `note`, `ptr`, W3C Web Annotation Data Model, Tesserae intertextual discovery algorithm).
3. Comparative Methodological Evaluation (Manual scholarly note drafting vs automated intertext matching vs LLM commentary generation; evaluating depth, factual accuracy, and philological nuance).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies, e.g., Dickinson College Commentaries, Digital Siris, Net7 Pundit / Recogito).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Guidelines for categorizing commentary notes [philological, historical, intertextual] and linking them to base text).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs).
```

---

## Topic 13: Digital Edition Introductions, Editorial Principles & Multi-Modal Publication
*Week 13 • Tue Dec 1 (#34) / Wed Dec 2 (#35) / Fri Dec 4 (#36 — Wednesday timetable 10:30 AM; Thu Dec 3 Closed)*

**Course Context & Primary Materials:** `Sahle, Digital Scholarly Editions (vol. 2); Pierazzo, Digital Textual Scholarship (ch. 4–5); TEI Publisher documentation`  
**Methodological Context:** *Studio and publication assembly week (no three-step cycle).* Constructing stemma codicum; formulating explicit editorial principles; TEI Publisher / CSS transformation; compiling web, HTML, and print-ready PDF packages. *Scholarly Commentary Assignment due Fri Dec 4.*

### Stage 1: Google Scholar Labs Natural-Language Query
```text
What scholarly conventions govern the introduction, stemma codicum, and editorial rationale of a digital critical edition, and what technical standards enable dual web and print publication from TEI XML sources?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: What scholarly conventions govern the introduction, stemma codicum, and editorial rationale of a digital critical edition, and what technical standards enable dual web and print publication from TEI XML sources?

Core Thesis to Substantiate & Evaluate: A professional digital scholarly edition demands a transparently argued introduction defining editorial principles and stemma codicum, coupled with modular publication pipelines (e.g., TEI Publisher, CSS/XSL-FO) that preserve academic rigor across web and print outputs.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (Synthesis of digital edition publication pipelines and introductory essays).
2. Technical, Methodological & Historical Foundations (Sahle's criteria for Digital Scholarly Editions [DSE], Pierazzo's digital editing theories, stemma codicum construction [graph theory / stemmatology], TEI Processing Model and TEI Publisher).
3. Applied Implementation & Editorial Dimensions (Publishing pipelines: XSLT, CSS Paged Media, Typst/LaTeX rendering from TEI XML; licensing, open access, long-term archival sustainability).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of finished digital editions, e.g., Jane Austen Fiction Manuscripts, Carl Maria von Weber Gesamtausgabe, Shelley-Godwin Archive).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Final assembly checklist for the Comprehensive Digital Edition Portfolio).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs).
```
