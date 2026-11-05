# Blueprint: Lesson 1.1 — The Scholarly Edition Pipeline
## Course: RELS 398 / ENGL 398 · Meeting #1

> **Source Specification:** [`SESSION_CONTENT_SPEC.md`](file:///home/kmpenner/projects/RELS/398/SESSION_CONTENT_SPEC.md) §1.1  
> **Key Reform:** Eliminates the software and tool survey (which is moved to subsequent lessons). Focuses purely on the **10 core tasks** of a scholarly digital edition, each framed across the **Three Modes** (Manual, Deterministic, AI).

---

### Core Learning Objectives
1. Understand the 10 distinct intellectual and technical tasks required to transform a physical manuscript into a published digital edition.
2. Differentiate how each task is executed across the three methodological modes: **Manual scholarship**, **Deterministic algorithms**, and **Generative AI models**.
3. Establish the course's non-negotiable benchmark: automated tools can only be evaluated against a human-verified manual ground truth.

---

### The 10 Tasks Across Three Modes

| Task | 1. Manual Mode | 2. Deterministic Mode | 3. Generative AI Mode |
| :--- | :--- | :--- | :--- |
| **1. Catalog** | Consulting physical library catalogues, measuring folios, identifying watermarks. | Querying SPARQL endpoints, VIAF/Wikidata APIs, OAI-PMH feeds. | Structured extraction of cataloguing metadata from auction notes. |
| **2. Photograph / Image** | Positioning manuscript on book cradle, setting color targets, raking light. | Automated IIIF tile generation, deskewing, ICC color profile transforms. | Document layout analysis, segmenting text blocks and marginalia. |
| **3. Transcribe (Diplomatic)** | Paleographical decipherment of scribal ink character-by-character. | OCR/HTR engines (PyLaia, Transkribus, TrOCR) with line segmentation. | Vision-language models (Gemini, Claude) transcribing directly from IIIF. |
| **4. Regularize (Normalized)** | Identifying archaic spelling slips and mapping to contemporary grammar. | Regex replacement pipelines (`sed`, Python regex), dictionary lookup tables. | Few-shot LLM prompts generating `<choice><orig><reg>` pairs. |
| **5. Collate** | Manual collation of multiple manuscript exemplars using physical sight. | Algorithmic alignment (CollateX, Gotoh/Needleman-Wunsch sequence matching). | Multi-witness LLM cross-examination identifying substantive variants. |
| **6. Parse (Lemma & MSD)** | Looking up headwords in OED/TLFi; recording case, tense, mood, gender. | Rule-based taggers and statistical models (TreeTagger, SpaCy, Stanza). | Context-aware LLM morphological disambiguation into UPOS + FEATS. |
| **7. Markup Named Entities** | Identifying historical persons, places, and organizations by hand. | Rule-based Gazetters, SpaCy EntityRuler regex dictionaries. | Zero-shot NER extraction linking entities to Wikidata QIDs. |
| **8. Translate** | Philological translation preserving historical rhetorical voice. | Statistical machine translation (DeepL, Google Translate). | Iterative LLM translation guided by custom glossaries and tone constraints. |
| **9. Comment** | Authoring historical notes, textual commentary, and explanatory glosses. | Cross-referencing digital gazetteers, Pleiades, CTS URN citations. | Synthetic historical background generation vetted against archival sources. |
| **10. Present / Publish** | Typesetting a physical codex or critical apparatus by hand. | Compiling TEI XML via XSLT / CSS Paged Media into static web and PDF editions. | Automated dynamic UI generation, searchable indices (Lunr.js), and interactive viewers. |

---

### In-Class Springboard & Exercise
* **Hook:** Show two versions of the 1760–1761 Halifax Peace and Friendship Treaty ("Truckhouse" clause and clan totem signatures): raw archival parchment scan (`NS Archives RG 1 vol. 430`) vs. interactive digital edition with multi-witness collation.
* **Anchor Demo Corpus:** The instructor introduces the **1760–1761 Halifax Treaties** (LaHave, Shubenacadie/Chibenaccadie, Richibucto, Miramichi exemplars) as the universal classroom demo across all 13 weeks.
* **Exercise:** Students select their individual project witness (either an assigned district exemplar of the 1760–1761 treaties for collaborative multi-witness editing, or an approved historical witness from the three genre tracks: Diplomatic/Legal, Administrative/Continental, or Epistolary/Vernacular).
