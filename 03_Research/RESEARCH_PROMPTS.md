# RELS 398 / ENGL 398: Research Prompts for Google Scholar Labs & Gemini Deep Research

This master compendium provides the complete two-stage research pipeline for all 13 weekly topics in **RELS 398.10 / ENGL 398.10 (ST: Digital Methods for Historical Documents)**, Fall 2026.

Adapted from the RELS 117 pipeline (see `117/src/RESEARCH_PROMPTS.md`), with the Stage 2 prompt re-templated for a digital humanities / textual scholarship register rather than bioethics.

## Two-Stage Research Pipeline Workflow:

1. **Stage 1: Google Scholar Labs Search**
   - Submit the exact natural-language question into [Google Scholar Labs](https://scholar.google.com/scholar_labs/search).
   - Review the AI synthesis and download up to **10 relevant, high-impact peer-reviewed PDFs** into `03_Research/` or the appropriate module folder.

2. **Stage 2: Gemini Deep Research**
   - Upload the downloaded Scholar Labs PDFs to Gemini Deep Research.
   - Run the structured Deep Research prompt below to generate an exhaustive, evidence-based research report with digital-edition case studies, technical comparison, and complete DOI/URL citations.

---

## Topic 1: Orientation & Polytonic Greek I/O
*Week 1 • Wed Sep 2 (#1) / Fri Sep 4 (#2)*

**Course Context & Primary Materials:** `Finney, "Manuscript Markup" (pp. 323–360); Griffitts §3.4.1; TEI Guidelines vi.2`

### Stage 1: Google Scholar Labs Natural-Language Query
```text
What technical and scholarly challenges arise in representing polytonic Greek text in digital environments, and how do Unicode standards and TEI markup address manuscript encoding needs?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: What technical and scholarly challenges arise in representing polytonic Greek text in digital environments, and how do Unicode standards and TEI markup address manuscript encoding needs?

Core Thesis to Substantiate & Evaluate: Digital editing of historical documents requires robust Unicode and font infrastructure for polytonic scripts alongside foundational markup conventions (TEI) and version control practices (Git) that together make manuscript transcription reproducible and interoperable.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities / textual editing instructors).
2. Technical, Methodological & Historical Foundations (Deep examination of the standards, tools, and scholarly traditions underlying the method).
3. Applied Implementation & Editorial Dimensions (Specific technical/editorial challenges: encoding decisions, data models, interoperability, quality control, reproducibility).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of existing digital editions/projects illustrating successful and problematic applications).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Actionable guidelines for students building their own digital edition).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs, including technical documentation).
```

---

## Topic 2: Manuscript Metadata & RDF
*Week 2 • Tue Sep 8 (#3) / Wed Sep 9 (#4) / Fri Sep 11 (#5)*

**Course Context & Primary Materials:** `Griffitts §3.4.2, 3.6.1, 4.1; TEI Guidelines v.1–3; Ceriani, Codex Marchalianus introduction`

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How do RDF linked-data models and the TEI Header standard structure manuscript metadata to support scholarly cataloguing and discoverability?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How do RDF linked-data models and the TEI Header standard structure manuscript metadata to support scholarly cataloguing and discoverability?

Core Thesis to Substantiate & Evaluate: Manuscript cataloguing in the digital age depends on structured metadata schemas (TEI Header, RDF triples) that formalize codicological description, provenance, and relationships between witnesses, enabling machine-actionable scholarly catalogues.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities / textual editing instructors).
2. Technical, Methodological & Historical Foundations (Deep examination of the standards, tools, and scholarly traditions underlying the method).
3. Applied Implementation & Editorial Dimensions (Specific technical/editorial challenges: encoding decisions, data models, interoperability, quality control, reproducibility).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of existing digital editions/projects illustrating successful and problematic applications).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Actionable guidelines for students building their own digital edition).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs, including technical documentation).
```

---

## Topic 3: IIIF & Image Storage Formats
*Week 3 • Tue Sep 15 (#6) / Wed Sep 16 (#7) / Fri Sep 18 (#8)*

**Course Context & Primary Materials:** `Griffitts §4.3–4.4; Havens, "Adobe Photoshop & Digital Paleography"`

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How does the International Image Interoperability Framework (IIIF) and multispectral imaging transform access to and analysis of historical manuscripts?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How does the International Image Interoperability Framework (IIIF) and multispectral imaging transform access to and analysis of historical manuscripts?

Core Thesis to Substantiate & Evaluate: IIIF-based image delivery combined with multispectral/high-resolution imaging techniques enables interoperable, scholarly-grade access to manuscript images while recovering textual evidence invisible to the naked eye (palimpsests, damaged folios).

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities / textual editing instructors).
2. Technical, Methodological & Historical Foundations (Deep examination of the standards, tools, and scholarly traditions underlying the method).
3. Applied Implementation & Editorial Dimensions (Specific technical/editorial challenges: encoding decisions, data models, interoperability, quality control, reproducibility).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of existing digital editions/projects illustrating successful and problematic applications).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Actionable guidelines for students building their own digital edition).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs, including technical documentation).
```

---

## Topic 4: Transcription Platforms: Transkribus & THREAD
*Week 4 • Tue Sep 22 (#9) / Wed Sep 23 (#10) / Fri Sep 25 (#11, Remote Delivery)*

**Course Context & Primary Materials:** `Transkribus User Guide; THREAD Documentation; Clemens & Graham, Introduction to Manuscript Studies`

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How effective are Handwritten Text Recognition (HTR) platforms like Transkribus compared to manual transcription for producing accurate digital editions of historical manuscripts?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How effective are Handwritten Text Recognition (HTR) platforms like Transkribus compared to manual transcription for producing accurate digital editions of historical manuscripts?

Core Thesis to Substantiate & Evaluate: Automated HTR technologies (Transkribus) substantially accelerate manuscript transcription workflows but require baseline training data, human correction, and platform interoperability (THREAD) to reach publication-quality accuracy.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities / textual editing instructors).
2. Technical, Methodological & Historical Foundations (Deep examination of the standards, tools, and scholarly traditions underlying the method).
3. Applied Implementation & Editorial Dimensions (Specific technical/editorial challenges: encoding decisions, data models, interoperability, quality control, reproducibility).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of existing digital editions/projects illustrating successful and problematic applications).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Actionable guidelines for students building their own digital edition).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs, including technical documentation).
```

---

## Topic 5: Normalization & Orthographic Regularization
*Week 5 • Tue Sep 29 (#12) / Fri Oct 2 (#13) — Wed Sep 30 closed (Truth & Reconciliation)*

**Course Context & Primary Materials:** `TEI Guidelines ch. 11 (Representation of Primary Sources); Robinson, "Collation and Textual Criticism"`

### Stage 1: Google Scholar Labs Natural-Language Query
```text
What principles guide the normalization of orthographic variation (e.g., iotacism) in historical manuscript transcription, and how does TEI encode these editorial interventions?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: What principles guide the normalization of orthographic variation (e.g., iotacism) in historical manuscript transcription, and how does TEI encode these editorial interventions?

Core Thesis to Substantiate & Evaluate: Editorial normalization of orthographic variants must balance fidelity to the manuscript witness against readability and searchability, with TEI's apparatus for representing primary sources providing a standardized mechanism to encode both the diplomatic and normalized forms.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities / textual editing instructors).
2. Technical, Methodological & Historical Foundations (Deep examination of the standards, tools, and scholarly traditions underlying the method).
3. Applied Implementation & Editorial Dimensions (Specific technical/editorial challenges: encoding decisions, data models, interoperability, quality control, reproducibility).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of existing digital editions/projects illustrating successful and problematic applications).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Actionable guidelines for students building their own digital edition).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs, including technical documentation).
```

---

## Topic 6: Textual Variants & CollateX
*Week 6 • Tue Oct 6 (#14) / Wed Oct 7 (#15) / Fri Oct 9 (#16)*

**Course Context & Primary Materials:** `CollateX Documentation; Haentjens Dekker et al. (2015); Aland & Aland, Text of the New Testament (ch. 5)`

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How do computational collation tools like CollateX automate the identification of textual variants across multiple manuscript witnesses, and what are the implications for constructing a critical apparatus?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How do computational collation tools like CollateX automate the identification of textual variants across multiple manuscript witnesses, and what are the implications for constructing a critical apparatus?

Core Thesis to Substantiate & Evaluate: Automated collation algorithms (CollateX) transform the traditionally labor-intensive practice of textual criticism by systematically aligning witnesses and generating a reproducible apparatus criticus, though algorithmic alignment still requires scholarly judgment in variant taxonomy.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities / textual editing instructors).
2. Technical, Methodological & Historical Foundations (Deep examination of the standards, tools, and scholarly traditions underlying the method).
3. Applied Implementation & Editorial Dimensions (Specific technical/editorial challenges: encoding decisions, data models, interoperability, quality control, reproducibility).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of existing digital editions/projects illustrating successful and problematic applications).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Actionable guidelines for students building their own digital edition).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs, including technical documentation).
```

---

## Topic 7: TEI XML Schema & Linguistic Markup
*Week 7 • Tue Oct 20 (#17) / Wed Oct 21 (#18) / Fri Oct 23 (#19)*

**Course Context & Primary Materials:** `TEI P5 Guidelines (Core & Text Structure); Burnard, What is the Text Encoding Initiative?`

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How does the TEI P5 XML schema structure textual and linguistic markup to support validation, interoperability, and long-term preservation of digital scholarly editions?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How does the TEI P5 XML schema structure textual and linguistic markup to support validation, interoperability, and long-term preservation of digital scholarly editions?

Core Thesis to Substantiate & Evaluate: The TEI Guidelines provide an extensible, standards-based XML vocabulary for structural and linguistic markup that, when rigorously validated (e.g., in Oxygen XML), ensures digital editions remain interoperable, sustainable, and scholarly credible.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities / textual editing instructors).
2. Technical, Methodological & Historical Foundations (Deep examination of the standards, tools, and scholarly traditions underlying the method).
3. Applied Implementation & Editorial Dimensions (Specific technical/editorial challenges: encoding decisions, data models, interoperability, quality control, reproducibility).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of existing digital editions/projects illustrating successful and problematic applications).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Actionable guidelines for students building their own digital edition).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs, including technical documentation).
```

---

## Topic 8: Morphological Tagging & POS Analysis
*Week 8 • Tue Oct 27 (#20) / Wed Oct 28 (#21) / Fri Oct 30 (#22)*

**Course Context & Primary Materials:** `CLTK (Classical Language Toolkit) Documentation; Schmid, "TreeTagger for Historical Languages"`

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How do computational tools such as the Classical Language Toolkit (CLTK) and TreeTagger perform morphological tagging and part-of-speech analysis on historical and classical language corpora?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How do computational tools such as the Classical Language Toolkit (CLTK) and TreeTagger perform morphological tagging and part-of-speech analysis on historical and classical language corpora?

Core Thesis to Substantiate & Evaluate: Automated morphological tagging and lemmatization pipelines (CLTK, TreeTagger) enable large-scale linguistic analysis of historical texts, but require adaptation to handle the orthographic and grammatical irregularities typical of pre-modern language corpora.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities / textual editing instructors).
2. Technical, Methodological & Historical Foundations (Deep examination of the standards, tools, and scholarly traditions underlying the method).
3. Applied Implementation & Editorial Dimensions (Specific technical/editorial challenges: encoding decisions, data models, interoperability, quality control, reproducibility).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of existing digital editions/projects illustrating successful and problematic applications).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Actionable guidelines for students building their own digital edition).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs, including technical documentation).
```

---

## Topic 9: Interlinear Glossing & Word Alignment
*Week 9 • Tue Nov 3 (#23) / Wed Nov 4 (#24) / Fri Nov 6 (#25)*

**Course Context & Primary Materials:** `Leipzig Glossing Rules; TEI Link & Alignment module; Baumgardt, "Digital Interlinear Editions"`

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How do the Leipzig Glossing Rules and TEI's linguistic alignment mechanisms structure interlinear glosses and word-level alignment for digital editions of historical texts?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How do the Leipzig Glossing Rules and TEI's linguistic alignment mechanisms structure interlinear glosses and word-level alignment for digital editions of historical texts?

Core Thesis to Substantiate & Evaluate: Standardized interlinear glossing (Leipzig Rules) and word-level alignment markup make morphosyntactic and translational relationships explicit and machine-readable, supporting both pedagogical use and computational linguistic research on historical corpora.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities / textual editing instructors).
2. Technical, Methodological & Historical Foundations (Deep examination of the standards, tools, and scholarly traditions underlying the method).
3. Applied Implementation & Editorial Dimensions (Specific technical/editorial challenges: encoding decisions, data models, interoperability, quality control, reproducibility).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of existing digital editions/projects illustrating successful and problematic applications).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Actionable guidelines for students building their own digital edition).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs, including technical documentation).
```

---

## Topic 10: Translation Alignment & Parallel Texts
*Week 10 • Tue Nov 10 (#26) / Fri Nov 13 (#27) — Wed Nov 11 closed (Remembrance Day)*

**Course Context & Primary Materials:** `Tiedemann, "Parallel Data Extraction"; TEI §16.1; DCNS Translation Guidelines`

### Stage 1: Google Scholar Labs Natural-Language Query
```text
What methods and standards govern sentence-level alignment of parallel translated texts, and how does this support comparative and multilingual digital editions?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: What methods and standards govern sentence-level alignment of parallel translated texts, and how does this support comparative and multilingual digital editions?

Core Thesis to Substantiate & Evaluate: Sentence alignment techniques for parallel corpora (informed by TEI §16.1 and established translation-alignment methodologies) enable digital editions to present source and target texts in dynamically linked, scholarly-navigable parallel view.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities / textual editing instructors).
2. Technical, Methodological & Historical Foundations (Deep examination of the standards, tools, and scholarly traditions underlying the method).
3. Applied Implementation & Editorial Dimensions (Specific technical/editorial challenges: encoding decisions, data models, interoperability, quality control, reproducibility).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of existing digital editions/projects illustrating successful and problematic applications).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Actionable guidelines for students building their own digital edition).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs, including technical documentation).
```

---

## Topic 11: Scholarly Commentary & Digital Annotations
*Week 11 • Tue Nov 17 (#28) / Wed Nov 18 (#29) / Fri Nov 20 (#30)*

**Course Context & Primary Materials:** `TEI §17 (Simple Analytic Mechanisms); Open Annotation Data Model; Vander Meulen, "Digital Commentary"`

### Stage 1: Google Scholar Labs Natural-Language Query
```text
How do TEI's analytic mechanisms and the Open Annotation Data Model structure scholarly commentary and annotations within digital editions?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: How do TEI's analytic mechanisms and the Open Annotation Data Model structure scholarly commentary and annotations within digital editions?

Core Thesis to Substantiate & Evaluate: Encoding scholarly commentary as structured, linked annotations (via TEI and Open Annotation) transforms static footnotes into a queryable, extensible apparatus that preserves the interpretive layer of critical editing as data.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities / textual editing instructors).
2. Technical, Methodological & Historical Foundations (Deep examination of the standards, tools, and scholarly traditions underlying the method).
3. Applied Implementation & Editorial Dimensions (Specific technical/editorial challenges: encoding decisions, data models, interoperability, quality control, reproducibility).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of existing digital editions/projects illustrating successful and problematic applications).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Actionable guidelines for students building their own digital edition).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs, including technical documentation).
```

---

## Topic 12: Edition Introductions & Editorial Principles
*Week 12 • Tue Nov 24 (#31) / Wed Nov 25 (#32) / Fri Nov 27 (#33)*

**Course Context & Primary Materials:** `Sahle, Digital Scholarly Editions (vol. 2); Pierazzo, Digital Textual Scholarship (ch. 4–5)`

### Stage 1: Google Scholar Labs Natural-Language Query
```text
What editorial principles and rhetorical conventions govern the scholarly introduction to a digital critical edition, including the presentation of manuscript stemma and editorial methodology?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: What editorial principles and rhetorical conventions govern the scholarly introduction to a digital critical edition, including the presentation of manuscript stemma and editorial methodology?

Core Thesis to Substantiate & Evaluate: A digital scholarly edition's introduction must transparently justify its editorial principles (base text selection, stemma, normalization choices) to establish scholarly authority and reproducibility, following conventions established in print textual criticism and adapted for digital publication.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities / textual editing instructors).
2. Technical, Methodological & Historical Foundations (Deep examination of the standards, tools, and scholarly traditions underlying the method).
3. Applied Implementation & Editorial Dimensions (Specific technical/editorial challenges: encoding decisions, data models, interoperability, quality control, reproducibility).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of existing digital editions/projects illustrating successful and problematic applications).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Actionable guidelines for students building their own digital edition).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs, including technical documentation).
```

---

## Topic 13: Final Project Assembly & Publication
*Week 13 • Tue Dec 1 (#34) / Wed Dec 2 (#35) / Fri Dec 4 (#36) — Thu Dec 3 closed (Feast Day)*

**Course Context & Primary Materials:** `Final validation of TEI XML schemas, CSS stylesheet rendering, and PDF output`

### Stage 1: Google Scholar Labs Natural-Language Query
```text
What technical and scholarly standards govern the final validation, styling, and dual web/print publication of a completed digital scholarly edition?
```

### Stage 2: Gemini Deep Research Prompt (Attach Downloaded Papers)
```text
Role: You are an expert scholar in digital humanities, textual scholarship, computational philology, and manuscript studies.
Objective: Conduct an exhaustive academic deep research report investigating the following central inquiry for an undergraduate digital methods / textual editing curriculum:

Central Inquiry: What technical and scholarly standards govern the final validation, styling, and dual web/print publication of a completed digital scholarly edition?

Core Thesis to Substantiate & Evaluate: Publishing a digital scholarly edition to a professional standard requires rigorous schema validation, considered visual presentation (CSS/print stylesheets), and adherence to sustainability and interoperability best practices so the edition remains usable and citable beyond the course.

Attached Literature: Analyze and synthesize the attached peer-reviewed papers downloaded from Google Scholar Labs in dialogue with broader literature in digital humanities, computational philology, and manuscript studies.

Required Report Structure & Depth:
1. Abstract & Executive Summary (High-level synthesis for digital humanities / textual editing instructors).
2. Technical, Methodological & Historical Foundations (Deep examination of the standards, tools, and scholarly traditions underlying the method).
3. Applied Implementation & Editorial Dimensions (Specific technical/editorial challenges: encoding decisions, data models, interoperability, quality control, reproducibility).
4. Real-World Digital Edition Case Studies (2-3 detailed case studies of existing digital editions/projects illustrating successful and problematic applications).
5. Pedagogical Takeaways & Synthesis for Digital Editors (Actionable guidelines for students building their own digital edition).
6. Comprehensive Academic & Technical References (Complete bibliographic entries with active DOIs/URLs, including technical documentation).
```

---
