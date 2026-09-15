# Lesson 2.3 — AI-Assisted Metadata Enrichment, Entity Extraction, and Validation Auditing

*RELS 398 / ENGL 398 · Topic 2: Cataloguing · Meeting #5 (Fri Sep 11)*

***Step 3 of the three-step cycle: AI-assisted.** Today you prompt large language models and multimodal vision pipelines to extract codicological metadata, generate TEI headers, and reconcile entities, scoring their outputs directly against Tuesday's hand-written ground truth and Wednesday's schema constraints.*

---

## **01 Content**

**The Promise and the Peril of Automated Metadata Generation**

The global landscape of manuscript archives is defined by a profound scaling crisis. Across national libraries, monastic collections, and university archives worldwide, hundreds of thousands of premodern handwritten codices, fragments, and archival documents remain uncatalogued or described only in fragmentary nineteenth-century registers (De Cristofaro & Zilio, 2025). Manual codicological cataloguing—the meticulous hand-encoding you practiced on Tuesday—requires immense domain expertise in palaeography, codicology, ancient languages, and XML markup. It is an editorial process that measures progress in hours per folio, making the comprehensive manual cataloguing of global cultural heritage economically and temporally impossible (De Cristofaro & Zilio, 2025; Koho et al., 2021).

In response to this bottleneck, the digital humanities community has increasingly turned to Artificial Intelligence (AI), specifically Large Language Models (LLMs) and computer vision architectures, to automate metadata extraction, entity recognition, and TEI-XML generation (De Cristofaro & Zilio, 2025; Ignatowicz et al., 2025). Generative neural networks can ingest thousands of pages of raw archival text or digital catalogue prose and produce richly tagged XML headers in seconds.

However, this computational acceleration introduces a critical epistemological peril. Generative AI models are statistical prediction engines, not deterministic logic processors. When tasked with producing structured archival metadata, neural networks frequently invent plausible-sounding historical facts, hallucinate non-existent scribal hands, and generate syntactically broken XML markup (De Cristofaro & Zilio, 2025). The central question of today's meeting is not whether AI can catalogue manuscripts, but how scholarly editors can rigorously measure, constrain, and audit AI-generated metadata using deterministic schema validation.

**Takeaway:** Artificial intelligence offers unprecedented speed in manuscript metadata extraction, but its probabilistic nature introduces hallucinations that demand rigorous schema-based auditing.

---

## **02 Content**

**How Large Language Models Process Codicological Information**

To evaluate AI-generated metadata effectively, an editor must understand the underlying computational mechanisms of Large Language Models. Modern LLMs are autoregressive transformer architectures trained on vast corpora of multilingual text, code, and structured data. Their fundamental operational objective is *next-token prediction*: given a sequence of preceding tokens (a prompt), the model calculates a probability distribution across its vocabulary to predict the most statistically probable next token.

When an LLM processes a prompt containing Latin catalogue prose or an uncial Greek transcription, it does not "read" the document as a human scholar does. It transforms text strings into high-dimensional numerical vectors (embeddings). Within its latent attention layers, the model activates associative patterns between words like *membranaceus*, *saeculo VI*, *Alexandria*, and the corresponding TEI tags `<supportDesc material="parchment">`, `<origDate>`, and `<origPlace>` (De Cristofaro & Zilio, 2025).

Because the training corpora of models like GPT-4 and Claude 3.5 contain thousands of public TEI-XML files, GitHub repositories, and open-access library catalogues, these models possess an impressive surface familiarity with XML grammar. They can effortlessly generate standard XML opening and closing tags, populate common `<teiHeader>` containers, and mimic the discursive tone of professional archivists. However, because this generation is driven by statistical probability rather than formal grammar rules, the model has no innate awareness of whether its generated XML tree actually satisfies a project's specific RELAX NG schema (De Cristofaro & Zilio, 2025).

**Takeaway:** Large Language Models generate XML metadata via probabilistic next-token prediction, producing fluent surface structures without an innate understanding of formal schema constraints.

---

## **03 Content**

**The Epistemological Tension: Probabilistic Prediction vs. Deterministic Validation**

The integration of artificial intelligence into textual scholarship brings two fundamentally incompatible computational philosophies into direct conflict:

1. **The Probabilistic Paradigm (AI/LLM):** Operates on statistical likelihood, semantic association, and pattern generalization. It excels at fuzzy semantic reasoning, translating languages, and recognizing implied entities in messy, unstructured prose (De Cristofaro & Zilio, 2025).
2. **The Deterministic Paradigm (XML/RNG/Schematron):** Operates on formal grammars, tree automata, and Boolean logic. It demands absolute structural precision, rigid parent-child containment, strict datatype compliance, and perfect internal cross-referencing (Cummings, 2018; TEI Consortium, 2025).

| Dimension | Probabilistic AI Generation (LLMs) | Deterministic Schema Gate (RNG & Schematron) |
| --- | --- | --- |
| Operational Goal | Predict statistically probable next tokens | Enforce rigid mathematical tree grammar |
| Semantic Handling | Recognizes implied entities and nicknames | Ignores narrative meaning; validates markup types |
| Structural Rigor | Hallucinates invalid nesting and bad tags | Rejects broken hierarchies with compiler errors |
| Data Typing | Generates conversational date strings | Mandates strict ISO 8601 datatypes (`YYYY-MM-DD`) |

When an LLM generates a `<teiHeader>`, it prioritizes semantic plausibility over structural grammar. It may recognize that a paragraph discusses the physical dimensions of a leaf and spontaneously invent a tag like `<leafDimensions height="305" width="240"/>`—a tag that is semantically clear to a human reader, but completely illegal under the official TEI P5 schema (TEI Consortium, 2025). Deterministic schema validation is the indispensable auditor that exposes and corrects these probabilistic deviations.

**Takeaway:** Codicological cataloguing requires reconciling probabilistic AI text generation with the unyielding, deterministic constraints of XML schemas.

---

## **04 Content**

**Prompt Engineering for Structured XML-TEI Output**

To extract usable metadata from Large Language Models, digital editors must design sophisticated prompt engineering strategies. A naive prompt (such as "Convert this catalogue into TEI XML") produces disorganized, hallucinated markup that fails basic schema validation immediately.

Modern prompt architectures for TEI metadata extraction deploy structured multi-turn instructions and explicit operational constraints (De Cristofaro & Zilio, 2025):

- **System Role Definition:** Establish the model's persona as an expert codicologist and TEI P5 text encoder adhering strictly to ISO standards.
- **Explicit Schema Ingestion:** Provide the model with the exact RELAX NG element list and hierarchy rules governing `<fileDesc>`, `<msContents>`, and `<physDesc>`.
- **Few-Shot Exemplars:** Supply two or three complete, certified, schema-valid TEI Header examples showing the exact desired encoding patterns.
- **Structured Output Formatting:** Instruct the model to operate in strict XML mode, prohibiting conversational preamble, markdown code ticks, or unescaped HTML characters.
- **Temperature Minimization:** Lower the model's sampling temperature (e.g., `temperature=0.0` or `0.2`) to suppress creative divergence and maximize deterministic pattern replication (De Cristofaro & Zilio, 2025).

```
System Prompt Excerpt for Codicological Extraction:
"You are an expert digital philologist specializing in TEI P5 manuscript cataloguing.
Your task is to convert raw archival catalogue descriptions into valid TEI XML.
Rules:
1. Output ONLY a valid <teiHeader> element enclosed in <TEI xmlns='http://www.tei-c.org/ns/1.0'>.
2. Follow strict TEI P5 hierarchy: teiHeader -> fileDesc -> sourceDesc -> msDesc.
3. Every date attribute (@when, @notBefore, @notAfter) MUST conform to ISO 8601 (YYYY or YYYY-MM-DD).
4. Do NOT invent elements outside the TEI msdescription module.
5. Escape all ampersands as &amp;."
```

**Takeaway:** Effective TEI prompt engineering requires explicit system constraints, few-shot schema exemplars, low temperature settings, and strict XML output modes.

---

## **05 Content**

**The Ground-Truth Benchmark: Evaluating AI Against the Manual Header**

In scientific experimentation, an automated system cannot evaluate itself; it must be measured against an authoritative, independent reference standard. In our course methodology, that reference standard is the hand-written, validated header you produced on Tuesday and certified on Wednesday (De Cristofaro & Zilio, 2025).

Today, you will feed the raw cataloguing notes for your chosen manuscript passage into two state-of-the-art LLMs (OpenAI's ChatGPT-4 and Anthropic's Claude 3.5 Sonnet). You will capture their raw XML outputs and score them directly against your manual ground truth.

| Evaluation Dimension | Manual Ground Truth (Tue/Wed) | AI-Generated Metadata (Fri) | Scoring Metric |
| --- | --- | --- | --- |
| Syntactic Well-Formedness | 100% (Certified in Oxygen) | Variable (Prone to quote/entity defects) | Binary Pass/Fail |
| RELAX NG Schema Validity | 100% (0 errors in Jing) | Variable (Prone to illegal nesting) | Total Validation Error Count |
| Schematron Rule Compliance | 100% (0 pointer errors) | High Failure Rate (Broken `@hand` IDs) | Cross-Reference Error Count |
| Codicological Precision | Verified against facsimiles | Statistical approximation of notes | Precision, Recall, F1-Score |
| Entity Disambiguation | Manually linked to VIAF/TGN | Probabilistic entity linking | % Correct LOD URIs |

By establishing this rigorous scoring protocol, you transform subjective impressions of "how smart the AI seems" into quantitative, reproducible engineering data (De Cristofaro & Zilio, 2025).

**Takeaway:** Tuesday's manual header and Wednesday's schema validation serve as the gold-standard benchmark against which automated AI outputs are quantitatively scored.

---

## **06 Content**

**Empirical Benchmarks: The PubCINET Project Case Study**

To ground our analysis in contemporary computational literature, we examine the landmark empirical study conducted by De Cristofaro and Zilio (2025) for the PubCINET project. PubCINET is a digital humanities initiative reconstructing the intellectual networks of Italian publishing and cinema between the 1950s and 1980s by digitizing thousands of unpublished archival letters and manuscripts (De Cristofaro & Zilio, 2025).

Faced with a massive cataloguing backlog, De Cristofaro and Zilio designed a rigorous comparative benchmark to evaluate how effectively OpenAI's ChatGPT-4 and Anthropic's Claude 3.5 Sonnet could automate the XML-TEI encoding of unpublished archival correspondence (De Cristofaro & Zilio, 2025).

The authors established a strict experimental pipeline: each LLM was provided with a detailed system prompt, a reference file (`macro.xml`) containing authorized project entities and URIs, and the raw transcribed text of the letters. The resulting XML files were programmatically ingested into an automated validation pipeline running RELAX NG and Schematron parsers, scoring both models across structural validity, entity recognition, and semantic fidelity (De Cristofaro & Zilio, 2025).

The findings of the PubCINET study revealed dramatic, systematic divergences in how different neural architectures handle structured XML schemas, exposing the core behavioral profiles of modern frontier models (De Cristofaro & Zilio, 2025).

**Takeaway:** The PubCINET project established an empirical benchmark comparing ChatGPT-4 and Claude 3.5 in automated TEI encoding, measuring schema compliance and entity extraction.

---

## **07 Content**

**Behavioral Profile of ChatGPT-4 in TEI Encoding**

The PubCINET benchmark revealed that OpenAI's ChatGPT-4 exhibits a distinct behavioral profile characterized by high semantic autonomy and low structural discipline (De Cristofaro & Zilio, 2025).

ChatGPT-4 demonstrated remarkable capability in recognizing implied historical entities. When an archival letter mentioned a person only by a nickname, an informal first name, or an oblique cultural reference, ChatGPT-4 successfully deduced the individual's full historical identity and correctly linked them to external biographical knowledge, even when that entity was not explicitly pre-defined in the prompt's reference dictionary (De Cristofaro & Zilio, 2025).

However, this semantic brilliance was accompanied by severe structural fragility. ChatGPT-4 routinely failed deterministic XML schema validation. It frequently broke hierarchical containment rules, closed structural containers prematurely, and hallucinated unauthorized XML elements (De Cristofaro & Zilio, 2025). ChatGPT-4 prioritized capturing the *meaning* of the archival narrative at the expense of obeying the mathematical grammar of the RELAX NG schema.

```
ChatGPT-4 Performance Summary (De Cristofaro & Zilio, 2025):
- Semantic Entity Recognition: HIGH (Successfully infers unlisted historical figures)
- Contextual Deduction: HIGH (Maps nicknames to formal historical identities)
- XML Well-Formedness: MODERATE (Occasional quote and entity defects)
- RELAX NG Schema Validity: POOR (Frequent illegal nesting and premature tag closure)
- Schematron Compliance: POOR (Generates broken internal @target pointers)
```

**Takeaway:** ChatGPT-4 excels at inferring implicit historical entities from context, but frequently fails deterministic XML schema validation through illegal element nesting.

---

## **08 Content**

**Structural Hallucinations: Invalid Nesting, Premature Tag Closure, and Bad Entities**

Analyzing the specific failure modes of ChatGPT-4 in the PubCINET study reveals the precise nature of *structural hallucinations* in LLM text generation (De Cristofaro & Zilio, 2025).

A structural hallucination occurs when a model generates an XML sequence that is plausible in general text but violates the formal grammar of the active schema. De Cristofaro and Zilio (2025) identified several recurring structural error typologies:

- **Premature Container Closure:** The model frequently closed parent containers before inserting mandatory child elements. For example, it would generate `</profileDesc>` and then immediately output `<langUsage><language ident="grc">Greek</language></langUsage>`, creating orphaned elements outside their required container (De Cristofaro & Zilio, 2025).
- **Illegal Tag Insertion:** The model repeatedly injected standard HTML tags into TEI contexts, such as inserting `<p>` or `<br>` inside `<closer>` or `<signed>`, where the TEI schema strictly permits only phrasing elements (De Cristofaro & Zilio, 2025).
- **Unauthorized Character Entities:** The model hallucinated HTML-style named entities (such as `&copy;`, `&nbsp;`, or `&eacute;`) that are valid in HTML5 but completely undefined in standard XML without an explicit DTD declaration, causing instant fatal parsing crashes (De Cristofaro & Zilio, 2025).

| Structural Hallucination Type | Invalid LLM Output | RELAX NG Error Diagnosis |
| --- | --- | --- |
| Premature container closure | `</profileDesc><langUsage>...</langUsage>` | Element `langUsage` not allowed outside `profileDesc` |
| Illegal child tag | `<closer><p>Yours faithfully,</p></closer>` | Element `p` not permitted inside `closer` |
| Undefined entity | `<p>Copyright &copy; 2026</p>` | Entity `copy` not declared; fatal well-formedness crash |
| Attribute type hallucination | `<supportDesc support="parchment">` | Attribute `support` is invalid; expected `material` |

**Takeaway:** Structural hallucinations—such as premature tag closure, illegal HTML tags, and undefined character entities—are the primary cause of LLM validation failures.

---

## **09 Content**

**Behavioral Profile of Claude 3.5 Sonnet in TEI Encoding**

In stark contrast to ChatGPT-4, Anthropic's Claude 3.5 Sonnet demonstrated an opposing behavioral profile in the PubCINET evaluation: exceptional structural discipline paired with conservative semantic literalism (De Cristofaro & Zilio, 2025).

Claude 3.5 Sonnet exhibited near-perfect adherence to XML well-formedness and RELAX NG schema validation rules. When provided with the project's system prompt and schema constraints, Claude 3.5 produced clean, valid TEI documents on its first generation pass, without requiring secondary correction prompts (De Cristofaro & Zilio, 2025). It strictly respected parent-child hierarchies, formatted ISO 8601 dates flawlessly, and avoided illegal HTML tag injections.

However, Claude 3.5 displayed significant semantic limitations. It operated with rigid literalism, refusing to extrapolate beyond the provided reference file (`macro.xml`). If an archival text mentioned an unpublished draft work or an obscure historical figure not explicitly catalogued in the reference dictionary, Claude 3.5 frequently ignored the entity entirely or tagged it as generic text, resulting in substantial data omissions (De Cristofaro & Zilio, 2025).

```
Claude 3.5 Sonnet Performance Summary (De Cristofaro & Zilio, 2025):
- Semantic Entity Recognition: MODERATE (Conservative; misses unlisted entities)
- Contextual Deduction: LOW (Strictly literal; avoids autonomous extrapolation)
- XML Well-Formedness: EXCELLENT (100% clean syntactic output)
- RELAX NG Schema Validity: EXCELLENT (Flawless element hierarchy and containment)
- Schematron Compliance: HIGH (Strictly adheres to authorized URI dictionaries)
```

**Takeaway:** Claude 3.5 Sonnet produces near-flawless schema-valid XML markup, but its semantic literalism causes it to omit historical entities not pre-defined in reference files.

---

## **10 Content**

**The Semantic-Structural Trade-Off in LLM Architectures**

The empirical findings of the PubCINET project expose a fundamental **semantic-structural trade-off** in the application of generative AI to textual scholarship (De Cristofaro & Zilio, 2025).

No single current frontier model excels simultaneously at autonomous semantic deduction and rigid grammatical compliance. Editors are forced to navigate a structural dichotomy:

| Model Architecture | Primary Core Competence | Primary Vulnerability | Optimal Editorial Role |
| --- | --- | --- | --- |
| **ChatGPT-4** | Deep semantic reasoning, contextual entity deduction | High rate of schema validation failures, broken XML trees | Draft entity discovery, fuzzy prosopographical linking |
| **Claude 3.5 Sonnet** | Rigid schema compliance, precise structural hierarchy | Omission of implicit or uncatalogued entities | Direct TEI Header generation, structured data transformation |

This specialization gap demonstrates why automated metadata pipelines cannot rely on a single unmonitored LLM. A robust digital editing workflow must combine the semantic discovery strengths of one model with the structural precision of another, governed at every step by deterministic schema validation (De Cristofaro & Zilio, 2025).

**Takeaway:** Digital editors must navigate a trade-off between ChatGPT-4's semantic discovery and Claude 3.5's structural obedience, combining models strategically within audited pipelines.

---

## **11 Content**

**Authority File Integration: Supplying Context via `macro.xml`**

A critical finding in automated cataloguing research is that LLMs cannot accurately link entities to Linked Open Data (LOD) authorities without external reference scaffolding (De Cristofaro & Zilio, 2025; Koho et al., 2021). If an LLM is simply asked to "add VIAF URIs," it will frequently hallucinate plausible-looking URL strings that lead to dead pages or point to entirely wrong historical persons.

To solve this, De Cristofaro and Zilio (2025) developed the **`macro.xml` reference architecture**. Before prompting the LLM, the project compiles an authoritative reference XML document containing controlled vocabulary registers:

```xml
<!-- Excerpt of a project macro.xml reference file -->
<authorityList>
  <personList>
    <person xml:id="pers_origen" ref="https://viaf.org/viaf/34454471">
      <persName>Origen of Alexandria</persName>
      <floruit notBefore="0210" notAfter="0254"/>
    </person>
    <person xml:id="pers_marchal" ref="https://viaf.org/viaf/88890041">
      <persName>René Marchal</persName>
      <role>Abbot of Saint-Nom, Collector</role>
    </person>
  </personList>
  
  <placeList>
    <place xml:id="place_alexandria" ref="https://pleiades.stoa.org/places/727070">
      <placeName>Alexandria (Egypt)</placeName>
    </place>
    <place xml:id="place_rome" ref="https://vocab.getty.edu/tgn/7001303">
      <placeName>Rome (Vatican City)</placeName>
    </place>
  </placeList>
</authorityList>
```

When this `macro.xml` file is injected into the LLM's prompt context, the model is instructed to retrieve entity URIs *exclusively* from this pre-verified list (De Cristofaro & Zilio, 2025). This technique eliminates URI hallucination, transforming open-ended generative prediction into a constrained entity-matching operation.

**Takeaway:** Providing LLMs with pre-compiled `macro.xml` authority dictionaries constrains entity linking and eliminates hallucinated LOD URIs.

---

## **12 Content**

**Automated Named Entity Recognition and Disambiguation (NERD)**

Named Entity Recognition and Disambiguation (NERD) is the computational process of locating proper names in unstructured text and mapping them to unambiguous unique identifiers (Koho et al., 2021; Koho et al., 2023).

In historical manuscript cataloguing, NERD presents severe challenges that defeat traditional rule-based Natural Language Processing (NLP) tools:

- **Archaic Spelling Variants:** Scribes spell names idiosyncratically across Latin, Greek, and vernacular dialects (e.g., *Marchalianus*, *Marchal*, *Marcialis*).
- **Palaeographical Homonyms:** Multiple historical figures share identical names (e.g., dozens of medieval bishops named *Johannes* or *Theodorus*).
- **Oblique Scribal Attributions:** Scribes frequently omit formal names entirely, referring to authors by ecclesiastical titles (*«ὁ μακάριος ἐπίσκοπος»*).

While LLMs demonstrate powerful semantic reasoning in resolving these ambiguous phrases (De Cristofaro & Zilio, 2025), their entity disambiguations must be verified. If an LLM encounters a note attributing a marginal reading to "Theodotion," it must correctly determine whether the text refers to the 2nd-century Jewish translator of the Old Testament (VIAF 59880157) or a later Byzantine copyist.

**Takeaway:** Automated NERD leverages LLM semantic reasoning to resolve ambiguous historical names, but requires human verification to prevent identity misattributions.

---

## **13 Content**

**Hallucination of Historical Facts and Chronologies**

Beyond structural XML defects, generative AI models pose a severe risk of **historical fact hallucination**. Because LLMs operate via probabilistic pattern completion, they are prone to filling gaps in archival records with fictional historical narratives that appear extraordinarily convincing (De Cristofaro & Zilio, 2025).

Consider a practical example from manuscript cataloguing. If an LLM is provided with a fragmentary catalogue description stating:

`"Vat. gr. 2125: 6th-century prophetic codex, uncial script, damaged at beginning, provenance Egypt."`

A generative model prompted to write a full `<history>` element may fabricate an elaborate, plausible provenance narrative:

```xml
<!-- HALLUCINATED PROVENANCE GENERATED BY LLM -->
<provenance notBefore="0700" notAfter="0750">
  <p>Transferred in 722 CE to the Monastery of Saint Catherine at Mount Sinai by the monk Dorotheus, where it was recorded in the 8th-century library inventory.</p>
</provenance>
```

This output is syntactically well-formed and schema-valid XML. It uses proper TEI elements and valid ISO dates. Yet every historical detail—Mount Sinai, the monk Dorotheus, the date 722 CE—is a complete computational fiction synthesized from the model's general knowledge of monastic manuscript history.

This hazard illustrates why schema validation alone is insufficient: a schema tests *structural validity*, but only human editorial expertise can certify *historical truth*.

**Takeaway:** LLMs can generate schema-valid but completely fabricated historical narratives, underscoring that structural validity does not equal historical truth.

---

## **14 Content**

**Computer Vision in Codicological Metadata Extraction**

Textual catalogue descriptions provide only a fraction of codicological knowledge. A manuscript is a physical, visual artifact whose most vital metadata—layout geometry, ruling patterns, decorative initials, binding stamps, and physical damage—resides entirely in its visual materiality (Ignatowicz et al., 2025).

To extract metadata directly from digital facsimiles, the digital humanities community is deploying advanced Computer Vision (CV) neural networks (Ignatowicz et al., 2025). Rather than relying on transcribed text, visual models process high-resolution IIIF image pixels to identify, segment, and classify physical codicological features.

| Pipeline Stage | Computational Engine | Input / Output Representation |
| --- | --- | --- |
| Visual Segmentation | YOLOv11 / Detectron2 | Scans IIIF facsimile to detect ROIs (stamps, initials, columns) |
| Micro Analysis & OCR | Bounding Polygon Crop | Isolates cropped image patches of initials and text lines |
| Semantic Transcription | BLIP-2 / Mistral-7B | Transcribes text, identifies iconography, maps to Wikidata URIs |
| Schema Integration | TEI Header Generator | Emits valid `<physDesc>` XML and RDF semantic triples |

Visual AI pipelines bridge the gap between image pixels and structured metadata, automating the extraction of layout dimensions, ink colors, and decorative elements (Ignatowicz et al., 2025).

**Takeaway:** Computer vision neural networks extract codicological metadata directly from manuscript image pixels, automating layout segmentation and visual feature detection.

---

## **15 Content**

**The Metadata Enrichment Model (MEM) and Multilayer Vision**

A leading state-of-the-art framework for visual manuscript metadata extraction is the **Metadata Enrichment Model (MEM)**, developed by Ignatowicz, Kutt, and Nalepa (2025) for the digitized incunabula and medieval manuscripts of the Jagiellonian Digital Library.

In cultural heritage collections, standard flat object detection fails because codicological features are deeply nested: a manuscript page contains a text block, which contains a decorated initial, which contains an embedded figurative icon, surrounded by an owner's stamp containing an ink inscription (Ignatowicz et al., 2025).

To overcome this, the MEM architecture introduces a **Multilayer Vision Mechanism (MVM)** (Ignatowicz et al., 2025):

1. **Layer 1 (Macro Segmentation):** Fine-tuned object detection networks (such as YOLOv11 and Detectron2) scan the entire folio to detect high-level architectural components: text columns, bounding boxes, marginal gloss regions, and major decorative blocks.
2. **Layer 2 (Micro Cropping & Extraction):** The detected regions of interest (ROIs) are programmatically cropped and passed to specialized neural models.
3. **Layer 3 (Multimodal Semantic Fusion):** Multimodal vision-language models (such as BLIP-2 or fine-tuned Mistral-7B) analyze the cropped ROIs, transcribe embedded text, evaluate iconographic motifs, and map the visual data to RDF knowledge graphs linked to Wikidata (Ignatowicz et al., 2025).

**Takeaway:** The MEM framework uses Multilayer Vision Mechanisms (YOLOv11 + multimodal LLMs) to hierarchically segment and enrich nested visual manuscript metadata.

---

## **16 Content**

**Detecting Codicological Regions of Interest (ROI)**

In the MEM pipeline, the computer vision engine is trained on specialized cultural heritage datasets to detect distinct codicological Regions of Interest (ROIs) (Ignatowicz et al., 2025).

These visual ROIs map directly to specific TEI `<physDesc>` and `<decoDesc>` elements:

- **Institutional Stamps & Armorial Marks:** Detected via bounding boxes and classified by shape (circular, oval, shield). The cropped image is passed to OCR to extract institutional shelfmarks, mapping to `<provenance>` and `<sealDesc>`.
- **Illuminated Initials & Miniatures:** Segmented by bounding polygon, measuring height in lines and identifying pigment palettes, mapping to `<decoNote type="initials">` (Ignatowicz et al., 2025).
- **Ruling Patterns & Bounding Boxes:** Edge-detection algorithms trace dry-point or lead ruling lines, calculating column widths and margin proportions for `<layoutDesc>`.
- **Physical Damage & Flaws:** Neural networks detect ink corrosion, wormholes, moisture stains, and trimming losses, automatically generating machine-readable `<condition>` assessments.

| Visual Manuscript Feature | CV Detection Mechanism | Mapped TEI XML Element |
| --- | --- | --- |
| Library ownership stamp | YOLOv11 Bounding Box + OCR | `<sealDesc>` / `<provenance>` |
| Decorated uncial initial | Detectron2 Instance Segmentation | `<decoDesc><decoNote type="initials">` |
| Text column boundaries | Line-segmentation Hough transform | `<layout columns="1" writtenLines="29">` |
| Parchment leaf dimensions | Pixel-to-millimeter scale calibration | `<extent><dimensions unit="mm">` |
| Margin annotations | Bounding polygon extraction | `<additions><p>Marginal glosses...</p></additions>` |

**Takeaway:** Computer vision models segment specific manuscript ROIs—stamps, initials, layouts, and damage—mapping visual coordinates directly to TEI elements.

---

## **17 Content**

**Multimodal Entity Mapping to Knowledge Graphs**

Once visual ROIs are cropped, the MEM architecture uses multimodal LLMs to transform visual features into Linked Open Data knowledge graphs (Ignatowicz et al., 2025; Koho et al., 2023).

When the vision pipeline detects an owner's stamp or heraldic coat of arms on a manuscript leaf, the multimodal model analyzes the image, identifies the heraldic devices (e.g., "three fleurs-de-lis under a cardinal's hat"), and matches the visual pattern against Wikidata and Getty AAT authority files (Ignatowicz et al., 2025).

The pipeline automatically outputs verified RDF semantic triples:

```turtle
# RDF Triples Generated Automatically by Multimodal MEM Pipeline
@prefix crm: <http://erlangen-crm.org/current/> .
@prefix wd: <http://www.wikidata.org/entity/> .
@prefix aat: <http://vocab.getty.edu/aat/> .

<http://example.org/manuscript/vat_gr_2125> 
    crm:P56_bears_feature <http://example.org/feature/stamp_001> .

<http://example.org/feature/stamp_001>
    a aat:300028744 ; # Getty AAT concept for "library stamps"
    crm:P2_has_type wd:Q213878 ; # Wikidata URI for Biblioteca Apostolica Vaticana
    crm:P3_has_note "Oval ink stamp of the Vatican Library on fol. 1r" .
```

This multimodal fusion transforms inert digital images into dynamic, machine-queryable nodes within global Linked Open Data networks (Ignatowicz et al., 2025; Koho et al., 2021).

**Takeaway:** Multimodal AI translates visual heraldic stamps and illuminations into RDF semantic triples, connecting manuscript images directly to Wikidata knowledge graphs.

---

## **18 Content**

**Vision Model Failure Modes: Degradation, Noise, and Eurocentric Bias**

Despite their extraordinary capabilities, computer vision models exhibit severe failure modes when applied to historical manuscripts (Ignatowicz et al., 2025).

Historical codices are degraded physical objects. Over centuries of use, manuscripts accumulate physical noise—faded ink, bleed-through from verso pages, water stains, mold spots, and worm damage. Computer vision models trained primarily on modern documents or clean print incunabula frequently misinterpret these anomalies (Ignatowicz et al., 2025):

- **False Positive Decorations:** CV models frequently misclassify dark water stains, grease spots, or clusters of ink bleed-through as decorative miniatures or historical ownership stamps.
- **Bounding Box Fragmentation:** Severe mold damage or parchment tearing can cause segmentation models to split a single continuous text column into multiple disconnected fragments.
- **Eurocentric Iconographic Bias:** Because the majority of open-access training datasets originate from Western European collections, vision models frequently misclassify or completely fail to recognize non-Western script structures, Syriac estrangela flourishes, Coptic initials, or Ethiopic decorative headpieces (*harag*) (Ignatowicz et al., 2025).

These vulnerabilities demonstrate why automated computer vision outputs must never be ingested directly into archival databases without systematic human review.

**Takeaway:** Vision models suffer from physical noise misclassification, column fragmentation, and Eurocentric training bias, requiring rigorous manual filtering.

---

## **19 Content**

**Designing an Automated Evaluation Metric for Header Metadata**

To evaluate AI-generated metadata scientifically, digital philologists deploy formal statistical metrics borrowed from information retrieval: **Precision**, **Recall**, and the harmonic **F1-Score** (De Cristofaro & Zilio, 2025).

When an AI model extracts codicological metadata from an archival description, its outputs are compared against the human ground truth across discrete metadata attributes (e.g., shelfmark, date of origin, support material, leaf height, line count, and scribal hands):

$$\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}$$

$$\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}$$

$$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

- **True Positive (TP):** An attribute correctly extracted and formatted by the AI (e.g., `@notBefore="0550"` matching ground truth).
- **False Positive (FP):** An attribute hallucinated or incorrectly assigned by the AI (e.g., `@material="paper"` when the manuscript is parchment).
- **False Negative (FN):** A mandatory attribute present in the ground truth that the AI omitted entirely (e.g., failing to extract the shelfmark or quire formula).

A model with high Precision but low Recall (like Claude 3.5 Sonnet) produces highly accurate data but leaves significant omissions. A model with high Recall but low Precision (like ChatGPT-4) captures every detail but injects numerous hallucinations and formatting errors (De Cristofaro & Zilio, 2025).

**Takeaway:** Information retrieval metrics—Precision, Recall, and F1-Score—quantify the trade-off between AI metadata completeness and accuracy against human ground truth.

---

## **20 Content**

**Scoring XML Structural Validity Programmatically**

In addition to evaluating semantic accuracy, an automated cataloguing pipeline must evaluate **structural validity** (De Cristofaro & Zilio, 2025).

In production environments, structural validity is scored automatically using Python scripts wrapping standard XML validation libraries (`lxml` for well-formedness and XML Schema, `jing` for RELAX NG, and `saxon` for ISO Schematron).

```python
#!/usr/bin/env python3
"""Programmatic validation scoring script for AI-generated TEI files."""
import subprocess, sys
from pathlib import Path
from lxml import etree

def score_tei_document(xml_path: Path, rng_path: Path) -> dict:
    results = {"well_formed": False, "rng_valid": False, "rng_errors": []}
    
    # 1. Test Well-Formedness
    try:
        doc = etree.parse(str(xml_path))
        results["well_formed"] = True
    except etree.XMLSyntaxError as e:
        results["rng_errors"].append(f"Fatal XML Syntax Error: {e}")
        return results
    
    # 2. Test RELAX NG Schema Validity via Jing
    cmd = ["jing", str(rng_path), str(xml_path)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode == 0:
        results["rng_valid"] = True
    else:
        results["rng_errors"] = proc.stdout.strip().splitlines()
        
    return results
```

Executing this script across hundreds of AI-generated files produces a quantitative **Schema Validity Rate** ($\text{SVR} = \frac{\text{Valid Files}}{\text{Total Files}}$), providing an unvarnished mathematical measure of model reliability (De Cristofaro & Zilio, 2025).

**Takeaway:** Programmatic validation scripts running Jing and lxml calculate objective Schema Validity Rates for AI-generated XML documents.

---

## **21 Content**

**The Self-Correction Loop: Compiler Error Reflection Prompts**

When an LLM produces an invalid XML document, human editors do not need to fix every tag manually. Instead, the computational pipeline can deploy a **self-correction reflection loop** (De Cristofaro & Zilio, 2025).

In a self-correction loop, the automated validation script captures the exact compiler error logs raised by Jing or Schematron and feeds those errors back into the LLM as a high-priority reflection prompt:

| Step | Pipeline Stage | Operational Action in Self-Correction Loop |
| --- | --- | --- |
| 1 | Initial Generation | LLM converts raw catalogue notes into initial TEI XML draft |
| 2 | Automated Audit | Jing parser tests draft against RELAX NG schema (`msdesc.rng`) |
| 3 | Decision Gate | If 0 errors, commit file; if errors detected, capture compiler error log |
| 4 | Reflection Prompt | Feed exact error log back into LLM with repair instructions |
| 5 | Re-Generation | LLM outputs repaired XML file and resubmits to validation gate |

```
Reflection Prompt Example:
"Your previous TEI generation failed RELAX NG validation with the following 2 errors:
1. line 14: element 'supportDesc' not allowed here; expected child of 'objectDesc'
2. line 28: value 'ca. 550' does not conform to datatype xsd:date
Please correct these errors and return ONLY the repaired, valid XML file."
```

Research demonstrates that frontier LLMs can resolve over 80% of their structural syntax errors when provided with explicit compiler error reflection prompts (De Cristofaro & Zilio, 2025).

**Takeaway:** Feeding compiler error logs back into LLMs in an automated reflection loop enables neural models to self-correct structural schema violations.

---

## **22 Content**

**Benchmarking Self-Correction: How Many Passes to Reach Schema Validity?**

While self-correction loops are powerful, they are not infinite. De Cristofaro and Zilio (2025) benchmarked how many iterative self-correction passes are required for different LLM architectures to reach schema validity.

The empirical data demonstrates distinct convergence trajectories:

| Model Architecture | Pass 1 Validity (Zero-Shot) | Pass 2 Validity (1st Reflection) | Pass 3 Validity (2nd Reflection) | Permanent Failure Rate |
| --- | --- | --- | --- | --- |
| **ChatGPT-4** | 35% | 78% | 91% | 9% (Infinite loop on complex nesting) |
| **Claude 3.5 Sonnet** | 88% | 98% | 100% | 0% (Rapid convergence) |
| **Open-Source 8B Model**| 5% | 22% | 41% | 59% (Repeats identical syntax errors) |

Claude 3.5 Sonnet converges to 100% validity within two reflection passes, making it exceptionally cost-effective in automated pipelines (De Cristofaro & Zilio, 2025). ChatGPT-4 improves dramatically on Pass 2, but occasionally enters degenerative loops where fixing one nesting error introduces another illegal HTML tag. Smaller open-source models lack the latent reasoning depth to interpret complex compiler logs, failing to converge even after multiple iterations.

**Takeaway:** Claude 3.5 converges to schema validity in 1–2 reflection passes, whereas ChatGPT-4 requires multiple passes and smaller models frequently fail to converge.

---

## **23 Content**

**Cross-Walking AI Outputs into Canonical Identifiers (CTS / CITE)**

A critical test of AI capability in textual scholarship is whether neural models can generate valid Canonical Text Services (CTS) URNs and CITE identifiers (Blackwell & Smith, 2019; Tiepmar & Heyer, 2014).

When an LLM is prompted to assign a CTS URN to an extracted biblical passage, it must correctly construct the multi-part identifier (`urn:cts:greekLit:tlg0527.tlg001.vat-gr-2125:1.1-1.5`).

Common AI failure modes in canonical citation include:

- **Namespace Confusion:** Inventing fictional namespaces (e.g., `urn:cts:bible:` instead of `urn:cts:greekLit:`).
- **Work ID Hallucination:** Misremembering TLG (Thesaurus Linguae Graecae) numbers (e.g., assigning `tlg0012` [Homer] to Isaiah).
- **Sub-Reference Drift:** Hallucinating word token indices in sub-references (e.g., generating `@καὶ[5]` when the word *καὶ* occurs only three times in the verse) (Blackwell & Smith, 2019).

To prevent citation drift, automated pipelines must cross-walk AI-generated URNs against authoritative CTS service inventories (`GetCapabilities` endpoints) before committing records to publication (Tiepmar & Heyer, 2014).

**Takeaway:** AI-generated CTS URNs must be validated against authoritative CTS capability inventories to prevent hallucinated work IDs and token index drift.

---

## **24 Content**

**Reconciling AI Discrepancies with the Manual Ground Truth**

Today's central analytical exercise is performing a systematic discrepancy reconciliation between your manual ground truth and the AI-generated metadata records.

Using computational diff tools (such as `git diff` or Python's `difflib`), you will align your validated Tuesday/Wednesday XML against the AI output and classify every discrepancy into one of four categories:

1. **AI Error (Structural):** Illegal XML nesting, unquoted attributes, bad entity escaping, or non-ISO dates.
2. **AI Error (Factual):** Fabricated historical dates, false scribal attributions, or incorrect physical dimensions.
3. **AI Superiority (Completeness):** Instances where the AI successfully recognized a subtle historical detail or bibliographic cross-reference that you overlooked during manual inspection.
4. **Valid Editorial Divergence:** Differences in descriptive wording where both the human and AI interpretations are defensible.

```
Discrepancy Audit Log Example:
- Line 42 (<origDate>): Human="0550-0599" | AI="0500-0600" -> [Valid Divergence: AI used broader century range]
- Line 58 (<supportDesc>): Human="parchment" | AI="parchment" -> [Match: 100% Agreement]
- Line 89 (<handNote>): Human="h1, h2, h3" | AI="h1" -> [AI Error: Omission of marginal hands h2 and h3]
- Line 112 (<decoNote>): Human="None" | AI="Hexaplaric asterisks" -> [AI Superiority: AI caught marginal signs]
```

Documenting these discrepancies produces the empirical data required for your Topic 02 comparative report.

**Takeaway:** Reconciling AI outputs against human ground truth reveals AI errors, omissions, and occasional surprising discoveries, providing empirical data for editorial evaluation.

---

## **25 Content**

**The Economics and Scalability of AI Cataloguing**

Beyond philological fidelity, scholarly editors must evaluate the practical economics and computational scalability of AI-assisted cataloguing pipelines (De Cristofaro & Zilio, 2025).

A comprehensive economic assessment balances API infrastructure costs against human labor hours:

| Workflow Phase | Manual Method (Tue) | Deterministic Method (Wed) | AI-Assisted Method (Fri) |
| --- | --- | --- | --- |
| **Cataloguing Time per Codex** | 8–15 Hours | 1–2 Hours (Validation & Linking) | 30–60 Seconds (Generation) |
| **Human Labor Cost** | High (Expert Postdoc/Faculty) | Moderate (Technical Editor) | Low (Review & Audit Only) |
| **Computational API Cost** | $0.00 | $0.00 (Open-source tools) | ~$0.05–$0.20 per record |
| **Scalability across 10,000 MSS** | Impossible without massive grants | Highly scalable if structured | Instantaneous batch processing |
| **Error Rate (Structural)** | Moderate (Human typographical) | 0% (Enforced by schema gate) | Variable (5–20% without self-repair) |
| **Error Rate (Factual)** | Very Low (Expert verification) | Very Low (Authoritative LOD) | High (Requires human audit) |

AI-assisted cataloguing dramatically reduces data entry costs, but shifts the human labor burden from *authoring* to *auditing and error reconciliation* (De Cristofaro & Zilio, 2025).

**Takeaway:** AI cataloguing reduces processing time from hours to seconds, shifting human expertise from manual data entry to critical schema auditing and fact-checking.

---

## **26 Content**

**Ethics, Provenance, and AI Attribution in Digital Editions**

When artificial intelligence models contribute to the generation of cultural heritage metadata, intellectual transparency demands explicit documentation of algorithmic provenance (De Cristofaro & Zilio, 2025; TEI Consortium, 2025).

A scholarly digital edition must never conceal the role of AI. If an LLM generated the initial manuscript description or extracted entities, this contribution must be formally recorded in the `<teiHeader>` using `<respStmt>` and `<change>` audit logs:

```xml
<teiHeader>
  <fileDesc>
    <titleStmt>
      <title>Diplomatic Edition of Codex Marchalianus (Vat. gr. 2125)</title>
      <respStmt>
        <resp>Manual codicological ground truth and human editorial audit</resp>
        <name xml:id="JD">Jane Doe</name>
      </respStmt>
      <respStmt>
        <resp>AI-assisted metadata extraction and entity linking</resp>
        <orgName xml:id="AI_Claude">Anthropic Claude 3.5 Sonnet (API Version 2024-10-22)</orgName>
      </respStmt>
    </titleStmt>
  </fileDesc>
  
  <revisionDesc>
    <change when="2026-09-11" who="#AI_Claude">
      Initial automated draft of msDesc generated via Claude 3.5 Sonnet using system prompt v2.1.
    </change>
    <change when="2026-09-11" who="#JD">
      Manual audit, error reconciliation, and RELAX NG schema validation certification.
    </change>
  </revisionDesc>
</teiHeader>
```

Explicit algorithmic attribution preserves the historical integrity of the scholarly record, ensuring future researchers know exactly which assertions were generated by neural networks and verified by human editors (De Cristofaro & Zilio, 2025).

**Takeaway:** Transparency requires documenting AI models in `<respStmt>` and recording automated drafting steps in `<revisionDesc>` change logs.

---

## **27 Content**

**Building the Production Pipeline: CI/CD for Human-in-the-Loop Cataloguing**

The culmination of this week's technical learning is the design of an automated **Continuous Integration / Continuous Deployment (CI/CD)** pipeline for hybrid, human-in-the-loop manuscript cataloguing (De Cristofaro & Zilio, 2025; Cummings, 2018).

In modern digital publishing, repositories use automated workflows (such as GitHub Actions) to govern the cataloguing lifecycle:

```yaml
# Conceptual GitHub Actions CI/CD Workflow for Automated TEI Auditing
name: TEI Metadata Validation Gate
on: [push, pull_request]

jobs:
  validate-tei:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Install Jing RELAX NG Validator
        run: sudo apt-get install -y jing

      - name: Validate AI-Generated TEI Files
        run: |
          echo "Auditing TEI XML files against msdesc.rng..."
          jing schemas/msdesc.rng src/modules/Topic_02_Cataloguing/*.xml

      - name: Audit Schematron Cross-References
        run: |
          python3 scripts/audit_schematron.py --dir src/modules/Topic_02_Cataloguing/
```

When an AI model commits an updated manuscript description to Git, the CI/CD pipeline immediately executes the Jing RELAX NG validator and Schematron scripts. If the AI commit violates schema rules, the build fails automatically, blocking publication and notifying the human editor to intervene (Cummings, 2018).

**Takeaway:** CI/CD pipelines automate RELAX NG and Schematron validation on every Git commit, creating an automated gate that prevents invalid AI markup from entering production.

---

## **28 Content**

**Hands-On: Running the AI Metadata Extraction on Your Passage**

Now you execute the comparative AI laboratory experiment for Meeting #5.

Follow this experimental protocol:

1. **Prepare Raw Input:** Extract the raw, unformatted cataloguing notes and Latin/English description for your primary witness into a plain text file.
2. **Execute Prompting:** Run the extraction prompt across two frontier models:
   - **Pass A (ChatGPT-4):** Execute the structured codicological prompt with `temperature=0.2`.
   - **Pass B (Claude 3.5 Sonnet):** Execute the identical prompt and `macro.xml` reference dictionary.
3. **Capture Raw Outputs:** Save the unedited XML outputs as:
   - `03a_Lesson_2.3_AI_Draft_GPT4.xml`
   - `03a_Lesson_2.3_AI_Draft_Claude35.xml`
4. **Execute Validation Scoring:** Run the programmatic validation script against both files, recording well-formedness errors, RELAX NG schema violations, and Schematron warnings.
5. **Execute Self-Correction Pass:** For any file that failed validation, feed the compiler error logs back into the model in a reflection prompt and capture the repaired output.
6. **Score Precision & Recall:** Compare the final AI files against your Tuesday manual ground truth, calculating the F1-score across core metadata fields.

Save all test files and your scoring matrix in your personal Git branch.

**Takeaway:** The hands-on lab executes structured AI metadata extractions across ChatGPT-4 and Claude 3.5, scoring raw outputs, self-correction passes, and F1 metrics against ground truth.

---

## **29 Content**

**Compiling the Topic 02 Comparative Evaluation Report**

Before concluding today's session, you will synthesize your findings from Tuesday, Wednesday, and Friday into the **Topic 02 Comparative Evaluation Report**.

Your report must present a clear, quantitative comparison across the three steps of the cycle:

| Metric / Dimension | Manual Method (Tue) | Deterministic Method (Wed) | AI-Assisted Method (Fri) |
| --- | --- | --- | --- |
| Authoring / Execution Time | 4.5 Hours | 45 Minutes | 45 Seconds |
| Initial Schema Validity Rate | N/A (Unvalidated) | 100% (After manual fix) | Pass 1: 60% / Pass 2: 95% |
| RELAX NG Error Count (Initial) | 7 Errors | 0 Errors | 12 Errors (GPT) / 1 (Claude) |
| Schematron Pointer Broken Rate | 3 Broken IDs | 0 Broken IDs | 4 Broken IDs |
| Entity Disambiguation Precision | 100% (Manual VIAF) | 100% (Certified LOD) | 85% (Factual hallucinations) |
| F1 Codicological Score | 1.00 (Reference) | 1.00 (Ground Truth) | 0.88 (Composite F1) |

Follow the standard RELS 398 analytical structure:

- **§1 Methodological Overview:** State the passage, witness, and tools evaluated.
- **§2 Quantitative Results:** Present the validation error counts, F1-scores, and convergence passes.
- **§3 Qualitative Error Analysis:** Detail specific structural hallucinations and factual misattributions.
- **§4 Editorial Recommendation:** Formulate an evidence-based recommendation on how your project will deploy AI tools responsibly within a schema-governed pipeline.

**Takeaway:** The comparative evaluation report synthesizes quantitative error rates, F1-scores, and qualitative analyses across the manual, deterministic, and AI passes.

---

## **30 Content**

**Synthesis: The Schema as the Indispensable Anchor of AI Philology**

This week has walked you through the full arc of computational manuscript cataloguing:

- **Tuesday (Manual):** You hand-authored a complete TEI Header, confronting the material complexities of physical codices and establishing an authoritative human ground truth (Le Bœuf, 2012; TEI Consortium, 2025).
- **Wednesday (Deterministic):** You subjected your markup to the uncompromising gate of RELAX NG and Schematron validation in Oxygen, linked your entities to RDF knowledge graphs, and established persistent CTS URNs (Cummings, 2018; Koho et al., 2021; Blackwell & Smith, 2019).
- **Friday (AI-Assisted):** You deployed frontier Large Language Models and computer vision pipelines to automate cataloguing, discovering both the immense speed of neural generation and the critical necessity of schema auditing (De Cristofaro & Zilio, 2025; Ignatowicz et al., 2025).

```
The Complete Three-Step Comparative Cycle — Topic 02:
[X] Tue: Manual — Hand-written TEI Header and msDesc (Human Ground Truth)
[X] Wed: Deterministic — RELAX NG & Schematron validation in Oxygen, RDF LOD, CTS URNs
[X] Fri: AI-Assisted — LLM metadata extraction scored against your manual baseline
```

The grand conclusion of Topic 02 is that **Artificial Intelligence does not replace text encoding schemas; it makes them more essential than ever.** In an era where neural networks can generate infinite volumes of plausible, probabilistic text, the formal, deterministic schema—enforced by RELAX NG, Schematron, and rigorous human editorial judgement—is the sole anchor that preserves academic truth, structural integrity, and historical reality in digital scholarship.

**Takeaway:** Generative AI accelerates cataloguing, but deterministic schemas and human editorial judgement remain the indispensable anchors of scholarly integrity.

---

## References

Blackwell, C., & Smith, N. (2019). The CITE Architecture: A conceptual and practical overview. In M. Berti (Ed.), *Digital Classical Philology: Ancient Greek and Latin in the Digital Revolution* (pp. 73–94). De Gruyter Saur.

Cummings, J. (2018). The Text Encoding Initiative and the study of literature. In R. Siemens & S. Schreibman (Eds.), *A Companion to Digital Literary Studies* (pp. 451–476). Blackwell.

De Cristofaro, M., & Zilio, D. (2025). Automating XML-TEI encoding of unpublished correspondence: A comparative analysis of two LLM approaches. *AIUCD 2025 Proceedings: Diversity, Equity, and Inclusion: Challenges and Opportunities for Digital Humanities in the Age of Artificial Intelligence*.

Ignatowicz, J., Kutt, K., & Nalepa, G. J. (2025). Metadata Enrichment Model: Integrating neural networks and semantic knowledge graphs for cultural heritage applications. *arXiv preprint*. https://arxiv.org/abs/2505.23543

Koho, M., Burrows, T., Hyvönen, E., Ikkala, E., Page, K., Ransom, L., ... & Wijsman, H. (2021). Harmonizing and publishing heterogeneous premodern manuscript metadata as Linked Open Data. *Journal of the Association for Information Science and Technology*, 73(2), 240–257. https://doi.org/10.1002/asi.24499

Koho, M., Coladangelo, L. P., Ransom, L., & Emery, D. (2023). Wikibase model for premodern manuscript metadata harmonization, linked data integration, and discovery. *ACM Journal on Computing and Cultural Heritage*, 16(3), Article 56. https://doi.org/10.1145/3594723

Le Bœuf, P. (2012). Modeling rare and unique documents: Using FRBRoo/CIDOC CRM. *Journal of Archival Organization*, 10(2), 96–106.

TEI Consortium. (2025). *TEI P5: Guidelines for Electronic Text Encoding and Interchange*. Version 4.8.0. https://tei-c.org/release/doc/tei-p5-doc/en/html/

Tiepmar, J., & Heyer, G. (2014). A new implementation for Canonical Text Services. In *Proceedings of the Workshop on Human-Computer Tractable Data for the Digital Humanities* (pp. 1–8).
