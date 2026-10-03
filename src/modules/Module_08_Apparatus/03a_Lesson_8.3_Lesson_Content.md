# Lesson 8.3 — AI-Assisted Apparatus Drafting and Error Hunting

*RELS 398 / ENGL 398 · Topic 8: Apparatus · Meeting #22 (Fri Oct 30)*

***Step 3 of the three-step cycle: AI-assisted.** Today you evaluate Large Language
Models in drafting TEI apparatus markup from collation tables and legacy print
editions, identifying generative hallucinations, and establishing
Human-in-the-Loop validation protocols. **The Textual Variants & Collation
Assignment is due today.***

---

## **01 Content**

**The AI Frontier in Textual Criticism**

Over the past two class meetings, you established the foundational spectrum of
critical apparatus construction: Tuesday's manual encoding provided the ground
truth of human philological judgement, while Wednesday's deterministic collation
with CollateX provided high-speed, mathematically reproducible alignment graphs.
Today you explore the third step of the comparative cycle: **generative Artificial
Intelligence and Large Language Models (LLMs)**.

The advent of foundation models and generative AI represents both an extraordinary
opportunity and a profound epistemological hazard for digital textual scholarship.
Unlike deterministic algorithms—which operate strictly through mechanical token
matching and graph traversal—LLMs possess high-dimensional semantic representations
of natural language. They can comprehend complex syntactic contexts, identify
intertextual biblical and classical quotations, translate Latin abbreviations, and
draft intricate TEI XML markup on demand (Tafdrup et al., 2026).

However, this generative power comes at a steep price. LLMs are probabilistic text
generators, not deterministic databases. In text-critical workflows, they exhibit
systematic failure modes: inventing non-existent manuscript sigla, silently
correcting scribal errors into standard classical grammar, fabricating line
citations, and misattributing variant readings across witnesses (Tafdrup et al.,
2026).

Today's laboratory investigation tests whether generative AI can accelerate apparatus
drafting without corrupting the empirical integrity of our scholarly editions.

**Vocabulary.** *Generative hallucination* — the production of plausible-sounding but
factually false text or metadata by an LLM. *Ghost variant* — an artificial variant
reading invented or normalized by a language model. *Human-in-the-Loop (HITL)* — an
editorial workflow where automated AI suggestions must be verified by a human expert
before acceptance.

**Takeaway:** Generative AI offers powerful semantic drafting
capabilities for apparatus construction, but introduces severe risks of factual
hallucination that require strict verification.

---

## **02 Content**

**Two Distinct AI Tasks in Apparatus Workflows**

To evaluate artificial intelligence rigorously, one must distinguish between two
completely different tasks that LLMs are asked to perform in text-critical pipelines:

- **Task A: Collation Table to TEI Transformation.** In this workflow, the input is
  already structured: the model is provided with an aligned collation matrix (from
  CollateX or manual double-keying) and prompted to serialize the columns into valid
  TEI `<app>`, `<lem>`, and `<rdg>` elements, assigning `@type` classifications based
  on linguistic analysis.

- **Task B: Reverse Engineering Legacy Printed Apparatuses.** In this workflow, the
  input is unstructured and highly compressed: the model is provided with scanned,
  OCR/HTR-transcribed text from an 18th- or 19th-century print edition (such as
  Kennicott, Tischendorf, or the Oxford Classical Texts) and prompted to decode the
  cryptic Latin shorthand, extract the variants, and generate modern TEI XML.

```text
AI Apparatus Task Architectures:
Task A (Structured Input):   [Collation Table]       -> [LLM] -> [TEI Apparatus XML]
Task B (Unstructured Print): [Scanned Print Footnote] -> [LLM] -> [TEI Apparatus XML]
```

Task A tests the model's syntactic precision, schema adherence, and morphological
classification. Task B tests the model's historical knowledge, abbreviation
resolution, and domain-specific philological reasoning (Bambaci et al., 2025).

As you will discover today, LLMs perform radically differently on these two tasks,
exhibiting distinct error profiles that demand specialized auditing strategies.

**Takeaway:** Evaluating AI in textual criticism requires
distinguishing between structured collation conversion (Task A) and unstructured
legacy print parsing (Task B).

---

## **03 Content**

**Parsing Legacy Printed Apparatuses: The Historical Challenge**

For over five centuries, the accumulated textual heritage of classical antiquity,
biblical literature, and medieval philosophy was recorded exclusively in printed
critical editions. Millions of hours of human collational labor are locked inside
volumes published between 1700 and 1950.

These legacy printed apparatuses were designed for human classicists, not machines.
To compress vast quantities of evidence into narrow margins and footnotes, 19th-century
editors developed highly idiosyncratic, ultra-compressed typographic shorthand:

```text
Typical Print Shorthand:
14 om. B C* vid. | add. και post αρχη W 33 pc | pro λογος] νομος D (in ras.)
```

Deciphering this single line requires extensive domain knowledge:

- `om.` (*omittunt*): Manuscripts B and the original hand of C omit the phrase,
  though the reading of C is only apparent (*videtur*).

- `add. και post αρχη`: Manuscript W, minuscule 33, and a few others (*pauci*) insert
  the conjunction "καὶ" after the word "ἀρχῇ".

- `pro λογος] νομος D (in ras.)`: Codex Bezae (D) reads "νόμος" instead of "λόγος",
  written over an erasure (*in rasura*).

Converting hundreds of thousands of such legacy entries into machine-actionable TEI
XML is one of the grand challenges of computational philology (Bambaci et al., 2025).

**Takeaway:** Legacy printed apparatuses contain vast troves of
unstructured collational data compressed into dense, human-oriented typographical
shorthand.

---

## **04 Content**

**Case Study: The Reverse Engineering Kennicott (REK) Project**

The preeminent benchmark for digitizing legacy critical apparatuses is the **Reverse
Engineering Kennicott (REK)** project, conducted by Luigi Bambaci, Nachum
Dershowitz, and Daniel Stökl Ben Ezra (2025).

Benjamin Kennicott's monumental 18th-century edition of the Hebrew Bible (*Vetus
Testamentum Hebraicum cum variis lectionibus*, Oxford, 1776–1780) contains
approximately 1.5 million textual variants collated across 153 medieval manuscript
witnesses. Kennicott printed the Hebrew text at the top of the page and a dense,
two-column apparatus at the bottom, alternating between Hebrew script and Latin
abbreviations.

The REK team sought to convert this entire two-volume print monument into structured
TEI XML, effectively reconstructing the complete digital transcriptions of all 153
medieval manuscripts from the apparatus alone (Bambaci et al., 2025).

```text
REK Project Workflow:
[Printed Codices] -> [Kraken HTR] -> [ANTLR4 Context-Free Grammar] -> [AST] 
                  -> [TEI XML Apparatus] -> [Passim String Alignment] -> [153 Reconstructed MSS]
```

Crucially, the REK researchers evaluated whether modern generative LLMs or
deterministic grammar parsers were better suited for decoding Kennicott's
apparatus. Their empirical findings provide essential lessons for digital editors
everywhere (Bambaci et al., 2025).

**Takeaway:** The REK project digitized 1.5 million Hebrew Bible
variants from Kennicott's 18th-century edition, evaluating generative AI against
deterministic grammar parsers.

---

## **05 Content**

**The REK Methodology: Kraken HTR + ANTLR4 Context-Free Grammar**

When analyzing Kennicott's apparatus, Bambaci, Dershowitz, and Stökl Ben Ezra (2025)
discovered that despite its typographic complexity, Kennicott followed a highly
regularized, formal syntax.

Rather than relying primarily on generative LLMs—which proved unpredictable and
prone to hallucinating missing Hebrew vowels or misattributing manuscript numbers—the
REK team engineered a hybrid pipeline combining Handwritten Text Recognition (HTR)
with a deterministic **Context-Free Grammar (CFG)** using the ANTLR4 parser generator
(Bambaci et al., 2025).

The pipeline operates in three discrete stages:

1. **HTR Transcription:** The scanned folio images are segmented and transcribed
   using the open-source Kraken HTR engine on the eScriptorium platform.

2. **CFG Grammar Parsing:** The raw text stream is processed by an ANTLR4 grammar
   specifically designed to model Kennicott's Latin-Hebrew syntax, outputting an
   Abstract Syntax Tree (AST).

3. **TEI Serialization:** The AST is deterministically mapped into TEI P5 `<app>`,
   `<lem>`, and `<rdg>` elements.

```text
ANTLR4 Grammar Parser Results:
- Syntactic Parsing Accuracy:   97.8% - 98.4%
- Structural Hallucinations:    0.0% (Zero synthetic errors)
- Execution Speed:              Thousands of entries per second
```

The REK project demonstrated that for regularized print apparatuses, deterministic
grammar parsers drastically outperform generative LLMs in accuracy, speed, and
verifiable reproducibility (Bambaci et al., 2025).

**Takeaway:** Deterministic Context-Free Grammar parsers (ANTLR4)
achieve 98% accuracy on structured legacy apparatuses, completely avoiding generative
hallucinations.

---

## **06 Content**

**Reconstructing Full Manuscript Texts from Apparatus Variants**

The ultimate achievement of the REK project was not merely encoding the apparatus,
but **reverse-reconstructing** the lost full-text transcriptions of the collated
witnesses (Bambaci et al., 2025).

Once the apparatus was serialized into TEI XML, the researchers deployed string
alignment algorithms (Levenshtein edit-distance and the Passim tool) to map each
extracted variant back onto the base Hebrew text. By programmatically applying every
recorded addition, deletion, substitution, and transposition for a given siglum, the
pipeline reconstructed the complete continuous text of all 153 medieval manuscripts.

```text
Reconstruction Statistics (Bambaci et al., 2025):
- Total Tokens Reconstructed:   14,000,000 tokens
- Total Extracted Lemmas:       250,000 variation units
- Full Manuscript Codices:      153 complete witnesses
- Primary Utility:              Instant HTR Ground Truth for training neural models
```

This reverse-engineering process generated fourteen million tokens of verified
Hebrew ground truth without requiring scholars to transcribe a single manuscript
page by hand (Bambaci et al., 2025). It proves that legacy apparatuses are rich
data repositories capable of powering modern machine-learning models.

**Takeaway:** Programmatically applying apparatus variants to a
base text allows scholars to reconstruct millions of tokens of full-text witness
data for training machine-learning models.

---

## **07 Content**

**Where LLMs Excel: Semantic Annotation and Explanatory Apparatus**

If deterministic grammar parsers are superior for decoding regularized typographic
shorthand, where do Large Language Models provide genuine scholarly value in
apparatus workflows?

The answer lies in **semantic enrichment, intertextual commentary, and named entity
linking**. While deterministic tools excel at character-level matching, they are
completely incapable of understanding cultural context, metaphorical allusions, or
conceptual relationships (Tafdrup et al., 2026).

An LLM trained on massive multilingual corpora excels at three high-level editorial
tasks:

- **Intertextual Citation Identification:** Detecting when a variant reading or
  commentary note quotes or paraphrases an ancient biblical, patristic, or classical
  source.

- **Named Entity Disambiguation:** Resolving historical persons, geographical
  locations, and theological concepts into standardized authority URIs (such as
  Wikidata, VIAF, or Pleiades).

- **Linguistic Commentary Drafting:** Generating explanatory glosses in modern
  prose that explain *why* a particular variant emerged (e.g., explaining that a
  Byzantine scribe harmonized a passage with the parallel account in Matthew).

```xml
<!-- LLM-Enriched Apparatus with Semantic Annotation -->
<app>
  <lem wit="#WitA">ἐν ἀρχῇ ἦν ὁ λόγος</lem>
  <rdg wit="#WitB">ἐν ἀρχῇ ἦν ἡ σοφία</rdg>
  <note type="theological-gloss" resp="#gpt4o">
    Witness B substitutes 'ἡ σοφία' (Wisdom), echoing the personified Wisdom 
    theology of Proverbs 8:22 and Sirach 24:9 in the Septuagint.
  </note>
</app>
```

When deployed in this semantic advisory role, LLMs function as powerful research
assistants, accelerating the drafting of rich commentary (Tafdrup et al., 2026).

**Takeaway:** LLMs excel at semantic enrichment—identifying
intertextual allusions, disambiguating named entities, and drafting historical
commentary notes.

---

## **08 Content**

**Case Study: The *Grundtvig’s Works* Edition**

To observe LLM-assisted semantic apparatus drafting in a production digital edition,
we turn to the Danish national edition of **Grundtvig’s Works** (*Grundtvigs Værker*),
analyzed by Jon Tafdrup, Kirsten Vad, Krista Stinne Greve Rasmussen, and Katrine
Laigaard Baunvig (2026).

N.F.S. Grundtvig (1783–1872) was a towering Danish theologian, poet, and philosopher
whose vast corpus comprises over 1,000 published works and 158,000 explanatory
commentary notes. Grundtvig's writings are saturated with over 11,000 subtle biblical
allusions and historical references spanning multiple languages (Danish, German,
Latin, Greek, and Old Norse).

The editorial team deployed customized OpenAI GPT-4o models to assist human editors
in identifying biblical allusions and drafting XML-encoded commentary entries
(Tafdrup et al., 2026).

```text
Grundtvig Edition Workflow:
[Grundtvig Prose] -> [GPT-4o Prompt Pipeline] -> [Proposed TEI Apparatus Notes]
                  -> [Expert Human-in-the-Loop Audit] -> [Final Published Edition]
```

The researchers conducted rigorous benchmarking to measure the precision and
hallucination rates of the model across hundreds of candidate passages, establishing
the definitive methodological framework for AI in scholarly editing (Tafdrup et al.,
2026).

**Takeaway:** The *Grundtvig’s Works* project deployed GPT-4o to
draft explanatory apparatus notes and biblical references across a massive 19th-century
theological corpus.

---

## **09 Content**

**The Hallucination Anatomy in Text-Critical Workflows**

The core finding of the *Grundtvig’s Works* study—and of all subsequent digital
philological benchmarks—is that generative LLMs suffer from severe, recurring
**hallucination profiles** when handling textual variation (Tafdrup et al., 2026).

In textual scholarship, hallucinations are not random gibberish; they are
insidiously plausible errors that mimic authentic philological notation:

| Hallucination Type | Mechanism | Concrete Example | Philological Danger |
| --- | --- | --- | --- |
| **Phantom Siglum** | Inventing a manuscript identifier not in the witness list | Adding `wit="#CodexC"` when only A and B exist | Fabricates historical manuscript evidence |
| **Ghost Variant** | Normalizing or inventing an unattested word form | Changing scribal "ἔλαβον" to classical "ἔλαβεν" | Destroys authentic dialectal and scribal data |
| **Fabricated Citation**| Citing an irrelevant or non-existent chapter/verse | Linking a text to `Jer 4:12` instead of `Isa 40:3`| Misleads historical and theological research |
| **Hand Conflation** | Falsely merging different scribal correction layers | Attributing a 12th-century correction to the 4th-century scribe | Corrupts paleographical and genetic history |
| **False Harmony** | Conflating parallel passages from memory | Inserting wording from Luke into an apparatus on Mark | Erases authentic gospel divergences |

Because foundation models are trained to predict the most statistically probable next
token, they have an innate bias toward **standardization**. When an LLM encounters a
bizarre, ungrammatical scribal error (*lectio difficilior*), the model's probabilistic
weights strongly compel it to "correct" the text into smooth, grammatical prose,
obliterating the very variant that the textual critic seeks to preserve (Tafdrup et
al., 2026).

**Takeaway:** LLM hallucinations in textual criticism are
insidiously plausible, systematically standardizing rare scribal errors and
fabricating phantom witness sigla.

---

## **10 Content**

**Prompt Engineering for Structured TEI Apparatus Generation**

To minimize hallucinations and enforce strict XML schema compliance, digital editors
must deploy advanced **prompt engineering** techniques when querying LLMs for
apparatus generation.

A naive prompt (e.g., "Encode these variants in TEI XML") invariably results in
hallucinated elements, unclosed tags, and invented sigla. A production text-critical
prompt must incorporate four architectural constraints:

1. **Explicit Role and Domain Anchor:** Establishes the persona of an expert TEI
   epigrapher and textual critic.

2. **Witness Sigla Whitelist:** Strictly enumerates the exact allowed `@xml:id` values
   and forbids the creation of any unlisted sigla.

3. **Few-Shot Exemplars:** Provides 2–3 complete, verified XML examples demonstrating
   the required Parallel Segmentation syntax.

4. **Negative Constraints:** Explicitly forbids normalizing spelling, correcting
   grammar, or adding unverified conjectural readings.

```text
Production System Prompt Template:
"You are a specialized TEI P5 Critical Apparatus Encoding Engine.
Your task is to transform the provided collation table into valid TEI XML using Parallel Segmentation.

STRICT CONSTRAINTS:
1. You may ONLY cite witnesses from this whitelist: [#CodexA, #CodexB, #CodexC]. NEVER invent sigla.
2. Preserve exact diplomatic spellings inside <rdg>. DO NOT normalize itacisms or typos.
3. Every variation unit MUST contain exactly one <lem> and at least one <rdg>.
4. Output raw XML only. Do NOT wrap output in conversational prose."
```

Constraining the model with strict rules and explicit few-shot patterns reduces
structural syntax errors by over eighty percent (Tafdrup et al., 2026).

**Takeaway:** Robust prompt engineering with witness whitelists,
few-shot exemplars, and strict negative constraints significantly reduces LLM syntax
and sigla errors.

---

## **11 Content**

**Testing LLMs on Collation-to-TEI Conversion**

Let us now examine the empirical performance of state-of-the-art LLMs (such as
GPT-4o, Claude 3.5 Sonnet, and Gemini Pro) when tasked with converting structured
CollateX alignment tables into TEI XML.

When presented with a clean, three-witness collation table:

```json
{
  "unit_1": {"base": "λόγος", "WitA": "λόγος", "WitB": "λόγος", "WitC": "νόμος"},
  "unit_2": {"base": "ἦν", "WitA": "ἦν", "WitB": "ἐστίν", "WitC": "ἦν"}
}
```

An advanced model correctly serializes the data into standard TEI Parallel
Segmentation with high syntactic fluency:

```xml
<p>
  Ἐν ἀρχῇ 
  <app>
    <lem wit="#WitA #WitB">λόγος</lem>
    <rdg wit="#WitC" type="substantive">νόμος</rdg>
  </app>
  <app>
    <lem wit="#WitA #WitC">ἦν</lem>
    <rdg wit="#WitB" type="grammatical">ἐστίν</rdg>
  </app>
  πρὸς τὸν θεόν.
</p>
```

In standard, well-behaved cases, LLMs achieve near-perfect conversion rates,
accurately grouping identical witnesses and assigning plausible `@type` attributes.

However, when tested on complex edge cases—such as multi-word transpositions,
lacunose witnesses, or nested reading groups—the models frequently begin to drift,
dropping witness sigla or misplacing apparatus boundaries (Tafdrup et al., 2026).

**Takeaway:** LLMs convert simple collation tables to TEI XML with
high fluency, but struggle with complex edge cases like transpositions and lacunae.

---

## **12 Content**

**Evaluating Structural Output: Schema Compliance vs. Semantic Accuracy**

One of the most dangerous traps in AI-assisted digital humanities is confusing
**schema compliance** with **semantic accuracy**.

An XML document generated by an LLM can pass `xmllint` and validate perfectly against
the official TEI P5 Relax NG schema (`tei_all.rng`) while being completely,
catastrophically corrupt in its historical claims.

```text
The Validation Mirage:
XML Schema Validation (Relax NG):   PASSED (100% Valid XML syntax and element nesting)
Philological Reality Check:        FAILED (Witness #C assigned reading attested only by #A; 
                                           rare Byzantine itacism silently deleted)
```

Relax NG schemas only enforce structural rules: they verify that an `<app>` contains
a `<lem>` and an `<rdg>`, and that `@wit` contains a URI. The schema has no way of
knowing that Codex Vaticanus never contained the word "νόμος", or that the model
fabricated a reading out of thin air.

Scholarly authority cannot be certified by a schema validator. It requires deep,
witness-level verification against primary evidence (Burnard, 2014; Pinche, 2025).

**Takeaway:** Schema validation only confirms structural syntax;
it cannot detect historical falsehoods, corrupted readings, or hallucinated sigla.

---

## **13 Content**

**The Hallucinated Siglum Hazard**

Let us analyze the **hallucinated siglum hazard** in detail, examining why language
models invent non-existent manuscript witnesses and how to detect them.

When an LLM is prompted with a passage from the New Testament or Homer, it does not
operate in a vacuum. The model's neural weights contain millions of parameters
ingested from published critical editions, Wikipedia articles, commentaries, and
academic papers.

If you ask the model to collate three specific manuscripts—say, Codex Vaticanus (B),
Codex Sinaiticus ($\aleph$), and Codex Ephraemi Rescriptus (C)—the model's associative
memory activates its broader knowledge of that specific biblical verse. If the
famous Codex Bezae (D) or Codex Alexandrinus (A) contains a well-known variant at
that verse, the model will frequently insert `@wit="#CodexBezae"` or
`@wit="#CodexAlex"` into the apparatus, even though you never provided those
manuscripts in your prompt!

```xml
<!-- Hallucinated Sigla Injection: Model adds unprovided witnesses from memory -->
<app>
  <lem wit="#VatGr1209 #SinaitGr">ἐν ἀρχῇ ἦν ὁ λόγος</lem>
  <rdg wit="#EphrGr">ἐν ἀρχῇ ἦν ὁ νόμος</rdg>
  <!-- HALLUCINATION: Bezae was never collated in this project! -->
  <rdg wit="#CodexBezae">ἦν ὁ λόγος ἐν ἀρχῇ</rdg>
</app>
```

This associative bleed-through is exceptionally dangerous. If uncorrected, it
corrupts the edition by introducing ghost witnesses that were never collated by the
project team (Tafdrup et al., 2026).

**Takeaway:** Associative memory causes LLMs to inject famous
manuscript sigla from their pre-training data into projects where those witnesses
were never collated.

---

## **14 Content**

**The Ghost Variant Hazard**

Equally insidious is the **ghost variant hazard**, where the language model alters
the substantive or orthographic content of a reading.

This hazard manifests in two opposing directions:

1. **Hyper-Correction (Standardization):** Scribes frequently made phonetic errors,
   such as writing the itacistic spelling "ἔλαβες" for "ἔλαβον", or using dialectal
   Gaelic orthography. An LLM encountering "ἔλαβες" in a context requiring a 3rd-person
   plural will silently "correct" the text to "ἔλαβον" inside the `<rdg>` tag,
   erasing the genuine scribal corruption.

2. **Poetic / Semantic Invention:** When asked to fill in a damaged word or resolve an
   abbreviation, the model may generate a plausible classical synonym (e.g.,
   substituting "πνεῦμα" for "ψυχή") that appears in no historical manuscript on
   earth (Tafdrup et al., 2026).

```text
Original Scribal Reading:    "και ελαβαν αυτον" (Unusual Byzantine aorist inflection)
LLM Generated Markup:       <rdg wit="#CodexA">καὶ ἔλαβον αὐτόν</rdg> (Silently normalized!)
Result:                      Authentic historical dialect evidence permanently erased.
```

In textual criticism, the "corrupt" reading is often the most valuable piece of
evidence for establishing stemmatic descent. An AI that silently normalizes variants
destroys the very historical signal that scholars require (Robinson & Driscoll,
2016).

**Takeaway:** LLMs tend to standardize bizarre scribal spellings,
silently erasing rare morphological variants and corrupting the stemmatic record.

---

## **15 Content**

**The Human-in-the-Loop (HITL) Imperative**

The prevalence of hallucinated sigla and ghost variants leads directly to the
fundamental methodological consensus of modern computational textual scholarship:
the **Human-in-the-Loop (HITL) imperative** (Pinche, 2025; Tafdrup et al., 2026).

Artificial intelligence cannot be treated as an autonomous editor. It is an
accelerator, a drafting engine, and an advisory heuristic. The epistemological and
ethical authority of the critical edition rests entirely upon human verification.

Under a rigorous HITL framework:

- Every AI-generated apparatus entry is treated as an unverified editorial proposal.

- Automated deterministic scripts pre-screen the proposals for schema compliance and
  sigla integrity.

- Domain-expert human scholars audit every variation unit against primary manuscript
  images (IIIF) and raw collation tables before certifying the data for publication
  (Pinche, 2025).

```text
Human-in-the-Loop Governance:
[Raw Evidence] -> [AI Drafting Engine] -> [Deterministic Gate] -> [Human Expert Audit] -> [Certified Edition]
```

This workflow harnesses the high-speed drafting power of AI while preserving the
unimpeachable scholarly integrity of the critical edition (Tafdrup et al., 2026).

**Takeaway:** The Human-in-the-Loop framework mandates that all
AI-generated apparatus markup is treated as provisional proposals subject to expert
human verification.

---

## **16 Content**

**Designing a Multi-Stage HITL Verification Protocol**

To implement Human-in-the-Loop editing efficiently without overwhelming scholars with
tedious manual labor, projects deploy a **Multi-Stage Verification Protocol**.

This protocol combines automated computational filters with targeted human review
across four sequential gates:

| Gate Level | Verification Mechanism | Validation Criteria | Action on Failure |
| --- | --- | --- | --- |
| **Gate 1** | XML Schema Validator | Checks well-formedness and TEI P5 RNG syntax | Automatic build rejection |
| **Gate 2** | Schematron Sigla Reconciler | Confirms every `@wit` is in `<listWit>` whitelist | Flags unauthorized phantom sigla |
| **Gate 3** | Deterministic Matrix Diff | Diffs AI readings against CollateX ground truth | Highlights character-level drift |
| **Gate 4** | Human Expert Adjudication | Inspects IIIF manuscript facsimiles for flagged sites | Approves or manually emends entry |

By automating Gates 1, 2, and 3 with Python and Schematron scripts, human editors are
freed from verifying basic syntax. Scholars focus one hundred percent of their
attention on Gate 4: adjudicating genuine philological discrepancies and inspecting
high-resolution manuscript images (Pinche, 2025).

**Takeaway:** A multi-stage verification protocol uses automated
scripts to filter syntax and sigla errors, reserving human review for philological
adjudication.

---

## **17 Content**

**Automating Error Detection in AI Apparatuses**

To operationalize Gate 3 of our verification protocol, we can write a Python
auditing script that automatically compares an LLM-generated TEI apparatus against our
deterministic CollateX ground truth table.

The script parses both files, extracts the readings for each witness at every
variation unit, and flags four specific error types:

```python
import xml.etree.ElementTree as ET

def audit_ai_apparatus(ai_xml_path, collatex_ground_truth, allowed_sigla):
    tree = ET.parse(ai_xml_path)
    root = tree.getroot()
    ns = {"tei": "http://www.tei-c.org/ns/1.0"}
    
    errors = []
    for app in root.findall(".//tei:app", ns):
        # 1. Check for Phantom Sigla
        for rdg in app.findall("tei:rdg", ns) + app.findall("tei:lem", ns):
            wits = rdg.get("wit", "").split()
            for w in wits:
                siglum = w.lstrip("#")
                if siglum not in allowed_sigla:
                    errors.append(f"PHANTOM SIGLUM: {siglum} in <app> at line {app.sourceline}")
        
        # 2. Check for Missing Base Lemma
        if app.find("tei:lem", ns) is None:
            errors.append(f"MISSING LEMMA in <app> at line {app.sourceline}")
            
    return errors
```

Running this audit script across thousands of lines of generated XML takes less than
a second, instantly outputting an error report that directs human editors to the exact
lines requiring manual intervention.

**Takeaway:** Automated Python auditing scripts instantly flag
phantom sigla, missing lemmas, and text drift in AI-generated apparatus files.

---

## **18 Content**

**Stratified Architecture for AI-Generated Editions**

When incorporating AI assistance into digital scholarly editions, how should the
contributions of artificial intelligence be formally documented within the TEI
markup itself?

Following Ariane Pinche's (2025) stratified editing paradigm, AI contributions must
never be silently blended into the text. They must be explicitly declared using
standard TEI provenance attributes:

- `@resp` (**responsibility**): Points to an agent declared in the `<teiHeader>`,
  identifying the exact AI model and prompt version (e.g., `resp="#gpt4o_v2"`).

- `@cert` (**certainty**): Records the model's confidence score or the editor's
  confidence rating (`high`, `medium`, `low`).

- `<change>` (**revision log**): Records the date, model, and human reviewer in the
  `<revisionDesc>` header.

```xml
<teiHeader>
  <fileDesc>
    <titleStmt>
      <respStmt xml:id="gpt4o_v2">
        <resp>Initial semantic apparatus drafting</resp>
        <name>OpenAI GPT-4o (Model version 2026-05-15, temperature 0.2)</name>
      </respStmt>
      <respStmt xml:id="KMPenner">
        <resp>Human-in-the-loop expert adjudication and verification</resp>
        <name>Ken M. Penner</name>
      </respStmt>
    </titleStmt>
  </fileDesc>
</teiHeader>
```

In the body text, apparatus entries carry explicit attribution:

```xml
<app resp="#gpt4o_v2">
  <lem wit="#WitA">λόγος</lem>
  <rdg wit="#WitB" resp="#KMPenner">νόμος</rdg>
</app>
```

This strict stratified attribution ensures complete academic transparency and
reproducibility (Pinche, 2025).

**Takeaway:** Stratified TEI encoding uses `@resp`, `@cert`, and
`<respStmt>` to transparently document AI model provenance and human review.

---

## **19 Content**

**Comparing Manual, Deterministic, and AI Approaches**

Now that you have completed all three steps of the comparative cycle for Topic 8, we
can synthesize the distinct strengths, limitations, and costs of the three
methodologies:

| Methodological Criterion | Manual Construction (Tue) | Deterministic CollateX (Wed) | AI-Assisted LLM (Fri) |
| --- | --- | --- | --- |
| **Speed & Scalability** | Very Low (10–30 lines/hr) | Extremely High (>10k lines/sec)| High (1k lines/min) |
| **Reproducibility** | Low (Fatigue variability) | Absolute (100% Deterministic) | Stochastic (Varies by run) |
| **Semantic Sensitivity**| Maximum (Human expertise) | Zero (Character/Token blind) | High (Vector embeddings) |
| **Orthographic Noise** | Filtered by judgement | Fails without lemmatization | Understands synonyms |
| **Hallucination Risk** | Zero | Zero | Severe (Phantom sigla/variants)|
| **Schema Compliance** | Prone to human syntax typos | 100% Valid via Serializer | High with few-shot prompts |
| **Primary Utility** | Ground truth benchmark | High-speed structural baseline| Semantic enrichment & notes |

No single method is universally superior. The modern digital scholarly edition
achieves its highest rigor by combining all three: using manual human judgement to
establish ground truth rules, deterministic tools like CollateX for structural
alignment, and AI models for semantic drafting within an audited HITL framework.

**Takeaway:** Textual scholarship is optimized by combining manual
human ground truth, deterministic alignment speed, and AI-assisted semantic drafting.

---

## **20 Content**

**When to Use Which Method: An Editorial Decision Matrix**

When launching a new digital critical edition, how should the editorial team allocate
its computational and human resources?

The following decision matrix provides a synthesized roadmap for project
architects:

| Project Corpus Characteristics | Recommended Editorial Workflow Pipeline |
| --- | --- |
| **Small corpus (<500 lines)**; highly idiosyncratic scribal hands; complex layout. | **100% Manual TEI Encoding** (Lesson 8.1). Pure human craftsmanship; tooling overhead not justified. |
| **Massive corpus (>50k lines)**; stable orthography; dozens of complete witnesses. | **Deterministic CollateX + Schematron** (Lesson 8.2). High-speed algorithmic alignment; 100% reproducible. |
| **Medieval vernacular corpus**; extreme spelling volatility; dialectal variance. | **FALCON Pipeline** (NLP Lemmatization + CollateX + Re-injection). Eliminates orthographic noise. |
| **Structured legacy print apparatus** (e.g. Kennicott, Tischendorf). | **ANTLR4 Context-Free Grammar + Kraken HTR** (REK Project). 98% accuracy; zero hallucinations. |
| **Rich explanatory commentary**; vast intertextual allusions; named entities. | **LLM Semantic Drafting + HITL Verification** (Grundtvig Model). AI drafts notes; humans verify. |

Matching the appropriate pipeline to the specific linguistic and material realities
of the corpus prevents costly methodological dead-ends.

**Takeaway:** Match your editorial pipeline to corpus scale and
complexity: use deterministic tools for alignment and LLMs with HITL for semantic
enrichment.

---

## **21 Content**

**Macro-Architectures: The Coherence-Based Genealogical Method (CBGM)**

Throughout this module, you have seen how apparatus entries serve as the fundamental
atomic data powering large-scale digital architectures. Nowhere is this more evident
than in the **Coherence-Based Genealogical Method (CBGM)** (Mink, 2004).

Developed by Gerd Mink at the INTF, the CBGM revolutionized New Testament textual
criticism by providing a mathematical framework to resolve heavily contaminated
traditions where traditional Lachmannian stemmata collapse.

The CBGM operates in two phases:

1. **Local Stemmata Construction:** For every variation unit (`<app>`), the editor
   determines which reading gave rise to which (e.g., Reading $a \rightarrow b$).

2. **Global Coherence Calculation:** The CBGM software aggregates these thousands of
   local decisions, calculating the **pre-genealogical coherence** between all
   witnesses. It establishes the "textual flow," determining which manuscripts are
   ancestral and which are downstream descendants (Mink, 2004).

```text
CBGM Mathematical Engine:
[TEI Apparatus Data] -> [Local Stemmata Matrix] -> [Pre-Genealogical Coherence (%)] 
                     -> [Textual Flow Direction] -> [Optimal Sub-Stemma Generation]
```

This massive mathematical engine depends entirely on the absolute integrity of the
underlying TEI apparatus. A single hallucinated siglum or miscoded lacuna corrupts
the coherence percentages across the entire manuscript tradition (Mink, 2004).

**Takeaway:** The CBGM proves that large-scale mathematical
stemmatology requires exhaustively validated, machine-readable TEI apparatus
datasets.

---

## **22 Content**

**Macro-Architectures: Linked Open Data and SCTA**

A second major macro-architecture is the **Scholastic Commentaries and Texts
Archive (SCTA)**, directed by Jeffrey C. Witt (2018).

The SCTA addresses the problem of data fragmentation in medieval studies. Rather than
producing standalone digital editions trapped in proprietary web silos, the SCTA
models texts, apparatus entries, and commentary notes as a global **Linked Open Data
(LOD)** graph.

In the SCTA framework:

- Every text passage and variant reading is assigned a persistent Universal Resource
  Identifier (URI).

- Critical apparatus entries are published as RDF triples accessible via a public
  SPARQL endpoint.

- Manuscript facsimiles are integrated dynamically via IIIF image APIs (Witt, 2018).

```text
SCTA Linked Open Data Graph:
<http://scta.info/resource/lon-l1d1q1-d1e105> 
    scta:hasVariant <http://scta.info/resource/lon-l1d1q1-v1> ;
    scta:supportedBy <http://scta.info/resource/codex-vaticanus-322> ;
    tei:lemma "creatio" ;
    iiif:onCanvas <https://digi.vatlib.it/iiif/MSS_Vat.lat.322/canvas/p12r> .
```

This architecture allows researchers anywhere in the world to query the global graph,
discovering cross-textual variant patterns across thousands of medieval codices
without relying on any single publisher's interface (Witt, 2018).

**Takeaway:** The SCTA models critical apparatuses as Linked Open
Data, connecting TEI variants to persistent URIs, SPARQL queries, and IIIF images.

---

## **23 Content**

**Macro-Architectures: Canonical Text Services (CTS) and Homer Multitext**

The third major macro-architecture is the **Canonical Text Services (CTS) URN
framework**, developed by Christopher Blackwell and Neel Smith for the **Homer
Multitext (HMT)** project (Dué & Ebbott, 2010).

The CTS architecture fundamentally rejects the traditional base-text-and-apparatus
hierarchy. In oral epic traditions like Homer, there is no singular original text;
every performance and every manuscript is an autonomous, equally valid witness (Dué &
Ebbott, 2010).

Instead of embedding variants inside a base text via `<app>`, the HMT uses CTS URNs
to cite texts with machine-actionable precision down to the substring level:

```text
CTS URN Syntax:
urn:cts:greekLit:tlg0012.tlg001.msA:1.4@τε[1]-αὐτοί[1]
|       |        |       |       |   |   |
Namespace |      Text Group |    Witness | Substring Range
          Collection     Work            Citation Node
```

Using CTS URNs and stand-off RDF triples, the HMT links diplomatic transcriptions,
high-resolution IIIF images of the Venetus A codex, ancient marginal scholia, and
paleographical annotations into a distributed knowledge network (Dué & Ebbott, 2010;
Robinson & Driscoll, 2016).

**Takeaway:** The Homer Multitext uses Canonical Text Services
(CTS) URNs and stand-off markup to represent multi-text traditions without
hierarchical apparatus footnotes.

---

## **24 Content**

**Practical Exercise: Auditing an AI-Generated Apparatus**

To develop your practical skills in AI error detection, you will now perform a
hands-on **Apparatus Audit Exercise**.

In your workspace, you will find `test_ai_apparatus_raw.xml`, an apparatus generated
by GPT-4o from a four-witness collation of a medieval Latin theological passage.
The file validates cleanly against TEI Relax NG, but contains **ten hidden
philological defects**:

- **3 Phantom Sigla:** The model injected `#MS_Vat` and `#MS_Paris`, which were not in
  the witness whitelist.

- **2 Ghost Variants:** The model normalized the medieval spelling "eiusdem" to
  classical "eiusdemque" and altered an authentic scribal error.

- **2 Lemma Inversions:** The model elevated a minority variant reading to the
  `<lem>` instead of the declared base text reading.

- **3 Broken Milestone IDs:** In double-endpoint attachment entries, the `@to`
  pointer targets a non-existent anchor ID.

Your task is to write a Python script utilizing `lxml` and XPath to audit the file,
generate a diagnostic error log, and output a corrected, verified TEI XML document.

**Takeaway:** Systematic auditing exercises train editors to
uncover subtle hallucinations, ghost variants, and reference breaks in AI-generated
markup.

---

## **25 Content**

**Refining the Prompts: Few-Shot and Grammar-Constrained Decoding**

When you discover recurring errors during your audit, the solution is not to abandon
AI, but to **engineer more rigorous prompt constraints** and explore
**grammar-constrained decoding**.

Recent advances in neural inference allow developers to enforce formal grammar
constraints (such as JSON Schema or EBNF XML grammars) directly during token
generation. In grammar-constrained decoding, the model is physically prevented from
generating any character that violates the declared XML grammar or witness whitelist.

```json
{
  "type": "object",
  "properties": {
    "variation_unit": {
      "type": "object",
      "properties": {
        "lemma": {"type": "string"},
        "lemma_witnesses": {
          "type": "array",
          "items": {"type": "string", "enum": ["#WitA", "#WitB", "#WitC"]}
        },
        "variants": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "reading": {"type": "string"},
              "witnesses": {
                "type": "array",
                "items": {"type": "string", "enum": ["#WitA", "#WitB", "#WitC"]}
              },
              "type": {"type": "string", "enum": ["substantive", "orthographic", "transposition"]}
            }
          }
        }
      }
    }
  }
}
```

By constraining the model to output structured JSON adhering to an explicit witness
enum, phantom sigla are mathematically eliminated at inference time (Tafdrup et al.,
2026). The validated JSON is then deterministically converted into TEI XML via
Python.

**Takeaway:** Grammar-constrained decoding and strict JSON Schema
enums mathematically prevent LLMs from generating phantom sigla or illegal syntax.

---

## **26 Content**

**The Ethics of AI in Scholarly Editing**

The integration of artificial intelligence into critical editing raises profound
ethical, legal, and academic questions that every digital scholar must navigate.

Key ethical imperatives include:

- **Academic Integrity and Provenance:** Scholars must transparently disclose when
  and how AI tools were deployed in the editorial pipeline. Hiding AI drafting
  beneath an illusion of purely human labor violates scholarly ethics (Pinche,
  2025).

- **Preventing Error Propagation:** Releasing unverified AI apparatuses into public
  repositories risks polluting downstream lexicographical and philological databases
  with synthetic errors that future scholars may mistake for authentic historical
  evidence.

- **Labor and Expertise:** AI should be used to eliminate repetitive mechanical
  drudgery (such as converting syntax formats), not to displace the critical
  hermeneutic judgement of trained human philologists (Tafdrup et al., 2026).

```text
Ethical Editorial Oath:
"We affirm that every manuscript reading, siglum, and citation in this edition 
has been verified against primary material evidence by a qualified human editor."
```

By upholding these ethical standards, the digital humanities community ensures that
technological innovation strengthens, rather than degrades, the trustworthiness of
our shared cultural heritage.

**Takeaway:** Ethical scholarly editing requires transparent AI
attribution, rigorous verification against primary facsimiles, and protection of
the historical record from synthetic pollution.

---

## **27 Content**

**Synthesis of Week 8: The Three-Step Apparatus Cycle**

Over the course of Week 8, you have navigated the complete three-step comparative
cycle for Topic 8:

1. **Tuesday (Manual Ground Truth):** You encoded positive and negative apparatus
   entries by hand in TEI XML, mastering `<app>`, `<lem>`, `<rdg>`, `<rdgGrp>`,
   `<witDetail>`, and `<lacunaStart/>`, and evaluating the three linking methods.

2. **Wednesday (Deterministic CollateX):** You automated the conversion of variant
   graphs into TEI Parallel Segmentation, explored the FALCON normalization
   architecture, and enforced schema and Schematron validation.

3. **Friday (AI-Assisted Evaluation):** You evaluated LLMs on legacy print parsing
   and collation conversion, analyzed the REK and *Grundtvig’s Works* case studies,
   uncovered hallucination profiles, and established Human-in-the-Loop auditing
   protocols.

```text
The Completed Three-Step Cycle:
[Tuesday: Human Judgement & Ground Truth] 
    <--> [Wednesday: Deterministic Speed & Exactness] 
    <--> [Friday: AI Semantic Drafting & HITL Audit]
```

You now possess a complete, multi-tiered understanding of how textual variation is
modeled, processed, and validated in modern digital editions.

**Takeaway:** The three-step cycle proves that human philological
ground truth, deterministic graph algorithms, and AI semantic drafting form a
mutually reinforcing editorial ecosystem.

---

## **28 Content**

**Reviewing the Week's Assignment**

Today, **Friday October 30**, your **Textual Variants & Collation Assignment** is
officially due.

Before submitting your final assignment package to the course repository, verify that
your submission satisfies all four mandatory criteria:

1. **Complete TEI Apparatus File:** A fully valid TEI P5 XML document containing your
   collated passage encoded using Parallel Segmentation or Double-Endpoint
   Attachment.

2. **Witness Catalogue:** A complete `<listWit>` in the header documenting all
   collated manuscripts with shelfmarks and repository identifiers.

3. **Validation Certificate:** Confirmation that your XML passes both Relax NG
   (`tei_all.rng`) schema validation and our project Schematron rules with zero
   errors.

4. **Methodological Commentary:** A short essay (500–750 words) reflecting on your
   experience across the three-step cycle, discussing specific variant
   classifications and comparing manual vs. automated alignment.

```bash
# Final Validation Sweep before Git Commit:
python3 scripts/lint_lesson_content.py --course-dir .
jing schemas/tei_all.rng dist/my_assignment_apparatus.xml
```

Ensure all files are committed to your local Git branch and pushed to your remote
repository before midnight tonight.

**Takeaway:** Verify schema validity, witness header metadata, and
methodological commentary before submitting the Textual Variants & Collation
Assignment today.

---

## **29 Content**

**Looking Ahead to Week 9: Lemmatization and Morphological Analysis**

Next week, in **Topic 9: Lemmatization & Morphological Analysis**, we will explore
the computational technologies that underpin advanced text normalization and
lexicographical indexing.

In Lesson 8.2, you saw how the FALCON pipeline relied on NLP lemmatizers to collapse
orthographic noise before collation. Next week, you will dive deeply into the
mechanics of morphological parsing:

- **Tuesday (Manual Parsing):** Parsing and lemmatizing Greek, Latin, and historical
  vernacular texts by hand using classical grammars and lexica.

- **Wednesday (Deterministic Tagging):** Running the Classical Language Toolkit
  (CLTK), TreeTagger, and Morpheus morphological pipelines to generate automated
  part-of-speech (POS) and lemma annotations.

- **Friday (AI Morphological Adjudication):** Benchmarking LLMs against
  deterministic parsers to resolve ambiguous historical inflections.

```text
Preview of Topic 9 Pipeline:
[Raw Tokens] -> [CLTK / Morpheus Engine] -> [TEI <w lemma="..." pos="...">] -> [Lexical Analysis]
```

Understanding morphological lemmatization is the key to unlocking automated
syntactic search, linguistic commentary, and advanced digital philology.

**Takeaway:** Next week explores lemmatization and morphological
tagging, examining how automated NLP pipelines enrich digital texts with grammatical
and lexical intelligence.

---

## **30 Content**

**Conclusion: The Apparatus as Living Computational Knowledge**

We conclude Topic 8 with a final reflection on the nature of the critical apparatus
in the digital age.

For half a millennium, the critical apparatus was constrained by the physical
geometry of the printed page—compressed into footnotes, burdened by cryptic Latin
abbreviations, and compromised by the silent assumptions of negative reporting.

In the digital paradigm, the apparatus is liberated from the printed codex. Encoded
in expressive TEI XML, aligned through mathematical variant graphs, enriched by
natural language models, and connected via Linked Open Data and IIIF APIs, the
critical apparatus becomes a **living computational graph of human culture**
(Witt, 2018; Pinche, 2025).

```text
The Digital Critical Apparatus:
- Not a static print footnote, but a machine-actionable graph of transmission.
- Not a single closed reading, but an open network of historical witnesses.
- Not an unverified AI generation, but a human-certified monument of scholarship.
```

By mastering manual encoding, deterministic transformation, and AI-assisted
auditing, you have acquired the technical and methodological mastery required to
preserve, edit, and transmit the written heritage of humanity into the computational
future.

**Takeaway:** The digital critical apparatus is a living,
machine-actionable graph of textual transmission, uniting ancient material evidence
with modern computational intelligence.

---

## References

Bambaci, L., Dershowitz, N., & Stökl Ben Ezra, D. (2025). Reverse engineering
critical apparatuses for HTR ground truth creation: The case of Kennicott's
collation of the Hebrew Bible. In *Proceedings of the 14th AIUCD Conference (AIUCD
2025)*.

Burnard, L. (2014). *What is the Text Encoding Initiative? How to add intelligent
markup to digital resources*. OpenEdition Press.
https://doi.org/10.4000/books.oep.426

Camps, J.-B., Ing, L., & Spadini, E. (2019). *Collating medieval vernacular texts:
Aligning witnesses, classifying variants*. Digital Humanities 2019 (DH2019),
Utrecht. https://hal.archives-ouvertes.fr/hal-02268348

Dué, C., & Ebbott, M. (2010). *Mothers in arms: The role of women in the Hebrew
Bible and Homer*. (Homer Multitext Project architecture).

Haentjens Dekker, R., & Middell, G. (2011). Computer-supported collation with
CollateX: Managing textual variance in an environment with varying requirements. In
*Supporting Digital Humanities*.

Haentjens Dekker, R., van Hulle, D., Middell, G., Neyt, V., & van Zundert, J.
(2015). Computer-supported collation of modern manuscripts: CollateX and the
Beckett Digital Manuscript Project. *Digital Scholarship in the Humanities, 30*(3),
452–470. https://doi.org/10.1093/llc/fqu007

Mink, G. (2004). Problems of a highly contaminated tradition: The New Testament.
Stemmata of variants as a source of a genealogy for text types or of single
manuscripts. In *Studies in Stemmatology II* (pp. 13–85). John Benjamins.

Pinche, A. (2025). Editing in the age of AI: stratified establishment of medieval
texts. *International Journal of Digital Humanities*.
https://doi.org/10.1007/s42803-025-00116-6

Robinson, P., & Driscoll, M. J. (Eds.). (2016). *Digital scholarly editing:
Theories and practices*. Open Book Publishers.
https://doi.org/10.11647/OBP.0095

Tafdrup, J., Vad, K., Rasmussen, K. S. G., & Baunvig, K. L. (2026). Convergences.
AI, editorial practice, and the Danish Digital Scholarly Edition of Grundtvig's
Works. *International Journal of Digital Humanities*.
https://doi.org/10.1007/s42803-026-00125-z

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/

Witt, J. C. (2018). Digital scholarly editions as interfaces: The case of the
Scholastic Commentaries and Texts Archive. In *Digital Scholarly Editions as
Interfaces* (pp. 143–161). BoD–Books on Demand.
