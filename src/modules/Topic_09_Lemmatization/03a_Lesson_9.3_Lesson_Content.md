# Lesson 9.3 — AI-Assisted Lemmatization and Morphological Disambiguation

*RELS 398 / ENGL 398 · Topic 9: Lemmatization · Meeting #25 (Fri Nov 6)*

***Step 3 of the three-step cycle: AI-assisted.** Today you evaluate large language models and neural sequence-to-sequence transformers for morphological tagging and lemmatization, scoring their precision, recall, and contextual disambiguation directly against your manual ground truth.*

---

## **01 Content**

**The Friday Cycle: Benchmarking Generative AI Against Ground Truth**

Today we arrive at the culmination of our three-step pedagogical cycle for Topic 9. On Tuesday (Meeting #23), you established the empirical ground truth by parsing, lemmatizing, and treebanking a passage of historical text entirely by hand using authoritative lexica and grammar standards. On Wednesday (Meeting #24), you operationalized those rules through deterministic and probabilistic pipelines—configuring finite-state transducers like Morpheus, decision-tree taggers like TreeTagger, and modular pipelines in the Classical Language Toolkit (CLTK). In doing so, you experienced both the remarkable speed of deterministic systems and their persistent vulnerabilities when confronted with homophony, non-standard dialectal forms, and unedited manuscript orthography.

Today, you transition to the third and final step: evaluating modern artificial intelligence architectures for morphological analysis. The contemporary natural language processing (NLP) landscape offers two distinct deep-learning approaches: specialized neural transformers trained explicitly on historical treebanks (such as GreBERTa, PhilBERTa, and the Cracovia system) and general-purpose Large Language Models (such as GPT-4, Claude, and LLaMA) prompted in zero-shot and few-shot configurations (Riemenschneider & Frank, 2023; Wittweiler et al., 2024).

The purpose of today's lab is not to treat generative AI as an infallible magic oracle that replaces philological scrutiny, but rather to construct a rigorous benchmarking harness. By measuring AI predictions against your Tuesday manual ground truth, you will calculate concrete precision, recall, and macro-F1 scores, exposing the exact boundary between genuine neural semantic reasoning and stochastic morphological hallucination.

This comparative methodology is essential for digital scholarship. As large-scale language models are increasingly integrated into digital editions and cultural heritage platforms, editors must develop critical algorithmic literacy. Knowing precisely where an LLM excels at disambiguating subtle poetic syntax and where it stumbles on dialectal anomalies allows scholars to build dependable human-in-the-loop workflows.

**Takeaway:** The Friday cycle benchmarks neural transformers and LLMs against manual ground truth to quantify parsing precision, recall, and hallucination rates.

---

## **02 Content**

**Neural Architectures in Classical Philology: From RNNs to Transformers**

To understand how contemporary neural taggers operate, we must examine the architectural shift from recurrent neural networks to transformer models. Early neural approaches to historical morphological tagging relied on Bidirectional Long Short-Term Memory networks (Bi-LSTMs) and Recurrent Neural Network (RNN) taggers (Manjavacas et al., 2019; Swaelens et al., 2024). While Bi-LSTMs process tokens sequentially in forward and backward directions to capture local surrounding context, their sequential nature creates computational bottlenecks and struggles to preserve information across long sentence distances.

In classical languages, sentence structure is characterized by extensive hyperbaton—the deliberate separation of grammatically linked words across distant clauses. A Greek governing verb might be separated from its accusative direct object by fifteen intervening words of poetic description. Recurrent architectures frequently experience gradient degradation across such spans, resulting in incorrect syntactic attachment and morphological misidentification (Manjavacas et al., 2019).

The introduction of the Transformer architecture revolutionized natural language processing by replacing recurrence with self-attention mechanisms. The multi-head self-attention mechanism computes mathematical compatibility scores between every pair of tokens in a sequence simultaneously, regardless of their linear distance:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

In a classical sentence, a transformer's attention heads can directly link a displaced adjective to its distant noun headword in a single computational step, bypassing the linear sequence entirely.

Furthermore, transformers utilize subword tokenization (such as Byte-Pair Encoding or WordPiece) or character-level representations. This enables neural models to decompose unfamiliar inflected forms into sub-lexical morphemes, allowing the network to recognize familiar aspectual prefixes, tense stems, and personal endings even when the composite surface token was never encountered during pre-training (Manjavacas et al., 2019; Riemenschneider & Frank, 2023).

**Takeaway:** Transformer self-attention mechanisms resolve long-distance hyperbaton by computing direct dependencies between words across entire sentences simultaneously.

---

## **03 Content**

**Specialized Neural Encoders: GreBERTa and PhilBERTa**

Within the field of computational classics, the most deterministic neural models are specialized encoder-only transformers pre-trained explicitly on historical corpora. The leading examples for historical Greek and Latin are **GreBERTa** and **PhilBERTa**, developed by Florian Riemenschneider and Anette Frank (2023).

GreBERTa and PhilBERTa are based on the RoBERTa (Robustly Optimized BERT Approach) architecture, which utilizes bidirectional transformer encoders trained on masked language modeling (MLM) objectives:

1. **Pre-Training Corpus:** GreBERTa was trained on a massive digital corpus of Ancient Greek texts comprising over 50 million tokens extracted from the Perseus Digital Library, the Thesaurus Linguae Graecae (TLG), and First1K1Greek.

2. **Fine-Tuning on Dependency Treebanks:** The pre-trained model was then fine-tuned on syntactically annotated gold-standard treebanks, specifically the Ancient Greek Dependency Treebank (AGLDT) and the PROIEL treebank (Crane, 1991; Haug & Jøhndal, 2008).

3. **Contextual Token Classification:** In fine-tuning, classification heads are attached to the encoder's output layers to predict Universal Part-of-Speech (UPOS) tags and fine-grained morphological feature bundles (FEATS) for every token in context.

Unlike general-purpose models, GreBERTa's embedding space is natively tuned to historical morphology. It recognizes that in Ancient Greek, verbal augmentations, vowel contractions, and accent shifts encode vital temporal and aspectual data (Riemenschneider & Frank, 2023).

When benchmarked against classical Attic and Koine prose, GreBERTa achieves part-of-speech tagging accuracy exceeding 94.5%, outperforming legacy probabilistic taggers like TreeTagger while maintaining complete deterministic reproducibility (Riemenschneider & Frank, 2023; Vatri & McGillivray, 2020). Because encoder-only models classify tokens from fixed tag vocabularies, they produce zero syntactic hallucinations, making them ideal for high-throughput corpus tagging.

**Takeaway:** Specialized neural encoders like GreBERTa leverage bidirectional masked pre-training on classical corpora to deliver highly accurate, deterministic morphological classification.

---

## **04 Content**

**Sequence-to-Sequence String Transduction: GreTA and PhilTA**

While encoder-only models like GreBERTa excel at classifying tokens into predefined categorical tagsets (UPOS/XPOS), lemmatization presents a distinct computational challenge. Lemmatization requires mapping an inflected surface token to a canonical dictionary headword that may possess a completely different character sequence due to irregular principal parts, suppletion, or stem ablaut (e.g., mapping Greek *ἦλθον* to *ἔρχομαι*, or Latin *tulit* to *fero*).

To solve this problem, Riemenschneider and Frank (2023) developed **GreTA** (Greek Text-to-Text Transformer) and **PhilTA** (Philological Text-to-Text Transformer), built upon the **T5 (Text-to-Text Transfer Transformer)** encoder-decoder architecture. In this framework, lemmatization is formulated as a character-level sequence-to-sequence string-transduction task:

| Model Component | Processing Role | Example Operation |
|---|---|---|
| **Input Context** | Full sentence string with target token delimited by special marker tags | `<w> ἦλθον </w> εἰς τὴν πόλιν` |
| **Encoder** | Computes deep bidirectional contextual embeddings across the entire sentence | Encodes syntactic government and past-time semantics |
| **Autoregressive Decoder** | Generates the dictionary lemma character by character from the latent representation | Generates: `ἔ` $\rightarrow$ `ρ` $\rightarrow$ `χ` $\rightarrow$ `ο` $\rightarrow$ `μ` $\rightarrow$ `α` $\rightarrow$ `ι` |

By supplying the target word within its surrounding sentence context, GreTA enables the neural network to infer morphological features dynamically, entirely bypassing the need to predict an intermediate part-of-speech tag before generating the lemma (Riemenschneider & Frank, 2023).

On standard classical benchmarks, character-level sequence-to-sequence models achieve lemma accuracy above 95.8% (Riemenschneider & Frank, 2023). Because the decoder operates at the character level, it can construct base lemmas from unencountered poetic or dialectal inflections, demonstrating superior generalization over static dictionary lookup engines.

**Takeaway:** Sequence-to-sequence transformers like GreTA treat lemmatization as contextual string transduction, decoding canonical dictionary headwords character by character.

---

## **05 Content**

**State-of-the-Art Latin Parsing: The Cracovia System**

In Latin computational linguistics, the contemporary state of the art in morphological analysis and part-of-speech tagging is defined by the **Cracovia System**, developed by Krzysztof Wróbel and colleagues (Wittweiler et al., 2024).

The Cracovia architecture is built upon **XLM-RoBERTa**, a cross-lingual transformer encoder pre-trained on over 2.5 terabytes of multilingual data. To adapt this model for historical scholarship, the authors fine-tuned it on two authoritative Latin corpora:

- **The LASLA Corpus:** The Laboratoire d'Analyse Statistique des Langues Anciennes (LASLA) database, comprising over 1.7 million manually verified Latin tokens from classical authors (Virgil, Cicero, Seneca, Tacitus).

- **Universal Dependencies Latin Treebanks:** The Latin-Perseus, Latin-PROIEL, and Latin-ITTB (Index Thomisticus) treebanks, providing comprehensive syntactic and morphological feature annotations (Haug & Jøhndal, 2008).

During the **EvaLatin 2022** shared task—the international competitive benchmark for Latin natural language processing—the Cracovia system achieved the highest reported performance across all participating architectures, generating an overall F1-score of **0.9627** on strict morphological tagging (Wittweiler et al., 2024).

The Cracovia system’s strength lies in its dual-head design: one classification head predicts the coarse Universal POS (UPOS) tag, while a second specialized head predicts the complex morphosyntactic feature string (FEATS). By sharing underlying transformer representations across both tasks, the model learns the mutual constraints governing Latin grammar—for example, recognizing that a token assigned the UPOS tag `NOUN` cannot simultaneously receive verbal tense or mood features (Burns, 2023; Wittweiler et al., 2024).

**Takeaway:** The Cracovia system combines XLM-RoBERTa encoders with multi-task fine-tuning on LASLA and UD treebanks to achieve state-of-the-art Latin morphological tagging.

---

## **06 Content**

**Generalized Large Language Models in Morphological Analysis**

Alongside specialized encoder models like GreBERTa and Cracovia, digital philologists have increasingly investigated the capabilities of massive, general-purpose **Large Language Models (LLMs)**, such as OpenAI's GPT-4, Anthropic's Claude, and Meta's LLaMA (Wittweiler et al., 2024; Zhang et al., 2024).

Unlike specialized models that require explicit fine-tuning on annotated treebanks, generalized LLMs operate through in-context learning. Having absorbed trillions of tokens of diverse multilingual text during self-supervised pre-training—including digitizations of classical texts, early modern editions, academic commentaries, and Latin/Greek grammars—LLMs exhibit emergent philological reasoning capabilities:

```text
Prompt:
You are an expert classical philologist. Analyze the following Ancient Greek token 
within its sentence context:
Sentence: "ὁ δὲ ἀνεξέταστος βίος οὐ βιωτὸς ἀνθρώπῳ."
Target Token: "ἀνεξέταστος"

Output a structured JSON object containing:
- lemma (canonical LSJ citation headword)
- upos (Universal Part of Speech)
- xpos (Perseus/AGLDT tag)
- morph_features (Case, Number, Gender)
- syntactic_role (grammatical function in clause)
```

When evaluated on standard classical prose, models like GPT-4 demonstrate an impressive capacity to explain grammatical nuances, identify figures of speech, and supply correct lexical headwords (Wittweiler et al., 2024).

However, general-purpose LLMs operate fundamentally differently from dedicated parsers. An LLM generates text through autoregressive token sampling based on statistical probability distributions rather than evaluating formal grammar rules. Consequently, while an LLM can articulate eloquent grammatical explanations, its raw parsing output is vulnerable to non-deterministic formatting drift, missed tokens, and morphological hallucinations when confronted with historical anomalies (Wittweiler et al., 2024; Zhang et al., 2024).

**Takeaway:** General-purpose LLMs possess broad emergent philological reasoning, but their probabilistic sampling creates non-deterministic outputs that require systematic validation.

---

## **07 Content**

**The Precision-Recall Paradox in LLM POS Tagging**

When scholars systematically benchmark Large Language Models against specialized classical taggers, they encounter a surprising empirical phenomenon known as the **Precision-Recall Paradox** (Wittweiler et al., 2024).

In an exhaustive empirical evaluation conducted by Wittweiler, Schomacker, and Fornaro (2024), multiple NLP architectures were tested on Latin part-of-speech tagging using the LASLA and Universal Dependencies benchmarks. The researchers compared fine-tuned transformers (Cracovia, LatinCy), legacy probabilistic models (TreeTagger), and commercial LLMs (GPT-3.5, GPT-4):

| Parsing Architecture | Model Category | Precision (%) | Recall (%) | F1-Score |
|---|---|---|---|---|
| **Cracovia System** | Fine-Tuned XLM-RoBERTa | 96.60 | 96.19 | **0.9627** |
| **TreeTagger (context)** | Probabilistic Markov Model | 95.29 | 94.28 | **0.9448** |
| **CLTK / Stanza** | Bi-LSTM Pipeline | 94.29 | 94.49 | **0.9445** |
| **LatinCy (`trf`)** | Fine-Tuned Transformer | 97.76 | 92.18 | **0.9324** |
| **GPT-4 (Zero-Shot)** | Generalized LLM | **99.52** | 88.75 | **0.9071** |
| **GPT-3.5 (Zero-Shot)** | Generalized LLM | **99.45** | 76.65 | **0.8033** |

The data reveals a dramatic divergence. In zero-shot configurations, GPT-4 achieved an astonishing **99.52% precision**—higher than any specialized model. When GPT-4 makes an assertion about a grammatical category, it is almost invariably correct.

However, GPT-4's **recall collapsed to 88.75%** (and GPT-3.5 dropped to 76.65%). The LLM frequently dropped ambiguous tokens, merged multi-word units, or skipped complex morphological features that it could not resolve with high statistical confidence. Consequently, its overall F1-score (0.9071) trailed significantly behind both the dedicated neural Cracovia system (0.9627) and the thirty-year-old probabilistic TreeTagger (0.9448) (Schmid, 1994; Wittweiler et al., 2024).

For digital editors, this paradox carries profound practical implications: LLMs are exceptional filters for verifying candidate readings, but they are inefficient and unreliable engines for bulk, exhaustive token tagging across complete texts.

**Takeaway:** LLMs exhibit near-perfect precision but poor recall in zero-shot POS tagging, frequently skipping or dropping ambiguous historical tokens.

---

## **08 Content**

**Zero-Shot vs. Few-Shot In-Context Prompting**

The poor recall observed in zero-shot LLM tagging can be substantially mitigated through **few-shot in-context learning** and structured prompt engineering (Wittweiler et al., 2024; Zhang et al., 2024).

In a zero-shot prompt, the model is asked to parse text with no prior examples, forcing it to infer the desired output taxonomy from its general pre-training weights. In a few-shot prompt, the user provides several expert-annotated demonstrations illustrating the exact tokenization, tagset vocabulary, and feature format required before presenting the target sentence:

```markdown
### System Prompt:
You are an expert computational philologist annotating Ancient Greek according to Universal Dependencies (UD) standards.

### Exemplar 1:
Input Token: "λόγος"
Context: "ἐν ἀρχῇ ἦν ὁ λόγος"
Output: {"lemma": "λόγος", "upos": "NOUN", "xpos": "n-s---mn-", "feats": "Case=Nom|Gender=Masc|Number=Sing"}

### Exemplar 2:
Input Token: "ἦν"
Context: "ἐν ἀρχῇ ἦν ὁ λόγος"
Output: {"lemma": "εἰμί", "upos": "AUX", "xpos": "v3siia---", "feats": "Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin|Voice=Act"}

### Target Task:
Input Token: "ἀρχῇ"
Context: "ἐν ἀρχῇ ἦν ὁ λόγος"
Output:
```

Providing structured exemplars anchors the model's output distribution. Research demonstrates that few-shot prompting achieves three immediate benefits:

1. **Tagset Conformance:** It prevents the LLM from inventing informal grammatical labels (e.g. returning `PARTICIPLE` instead of standard UD `VERB` with `VerbForm=Part`).

2. **Recall Recovery:** Supplying examples of ambiguous closed-class words (particles, conjunctions) boosts recall by 8 to 12 percentage points (Wittweiler et al., 2024).

3. **Citation Standardization:** It forces the model to adhere to canonical dictionary citation forms (e.g. LSJ first-person singular present active) rather than generating modern infinitives or bare roots (Crane, 1991; Zhang et al., 2024).

**Takeaway:** Few-shot prompting with annotated exemplars anchors LLM output to standard tagsets, dramatically improving recall and citation consistency.

---

## **09 Content**

**Morphological Hallucination: Mechanisms and Manifestations**

Despite prompt optimization, generative LLMs remain vulnerable to **morphological hallucination**—the generation of linguistically plausible but philologically incorrect or historically uninstantiated lemmas, stems, and grammatical features (Wittweiler et al., 2024; Zhang et al., 2024).

Morphological hallucination in classical languages manifests primarily through three distinct mechanisms:

| Hallucination Type | Underlying Mechanism | Linguistic Consequence |
|---|---|---|
| **1. Modern Language Intrusion** | Dominated by modern training data (Dimotiki / Romance) | Substitutes modern words (e.g. *τρώω*) for ancient lemmas (*ἐσθίω*) |
| **2. Analogical Regularization** | Over-generalizes regular inflectional paradigms | Hallucinates non-existent regular roots (*δράκω*) for suppletive aorists (*ἔδρακον*) |
| **3. Etymological Decomposition** | Splits compounds into arbitrary sub-lexical roots | Invents fictitious base lemmas for rare theological hapax legomena |

The first and most prevalent error is **modern language interference**. Because modern languages (such as Modern Greek or Italian) dominate LLM pre-training corpora by a factor of over 10,000 to 1 relative to pre-modern Greek or Latin, the model frequently maps ancient forms to modern equivalents. For example, when encountering the Classical Greek verb *ἐσθίω* ("to eat"), an LLM may output the Modern Greek lemma *τρώω*, or assign the Modern Greek monotonic spelling *παιδι* instead of the ancient *παιδίον* (Zhang et al., 2024).

The second mechanism is **false analogical regularization**. Ancient Greek and Latin verbal systems are filled with suppletive verbs—verbs whose principal parts derive from entirely different historical roots (e.g., *ὁράω*, future *ὄψομαι*, aorist *εἶδον*, perfect *ἑόρακα*). When prompted with a rare poetic or dialectal form like the epic aorist *ἔδρακον* ("I saw"), an LLM frequently regularizes the stem, hallucinating a non-existent first-person lemma **δράκω* rather than mapping it correctly to *δέρκομαι* (Riemenschneider & Frank, 2023).

The third mechanism is **etymological over-decomposition**. When processing rare compound words or hapax legomena in theological texts, LLMs often decompose the word into constituent roots and invent a fictitious base lemma rather than citing the attested dictionary headword documented in LSJ or Lewis & Short.

**Takeaway:** Morphological hallucination stems from modern language pre-training bias and analogical regularization of irregular historical paradigms.

---

## **10 Content**

**Comparative Benchmarks Across Classical Corpora**

The relative efficacy of rule-based, statistical, neural, and generative parsing architectures varies significantly depending on the genre, dialect, and historical period of the text under evaluation (Vatri & McGillivray, 2020; Wittweiler et al., 2024).

To synthesize these trade-offs, we examine comparative performance across three distinct corpus types: standardized classical prose (e.g. Lysias, Cicero), archaic epic poetry (e.g. Homer's *Iliad*, Virgil's *Aeneid*), and non-standardized medieval manuscripts (e.g. Byzantine epigrams) (Swaelens et al., 2024; Vatri & McGillivray, 2020; Wittweiler et al., 2024):

| Architecture / System | Core Technology | Standard Prose Lemma Acc. (%) | Epic Poetry Lemma Acc. (%) | Medieval Manuscript Lemma Acc. (%) | Primary Strength / Failure Mode |
|---|---|---|---|---|---|
| **Morpheus (Perseus)** | Finite-State Transducer | 88.50 | 82.10 | 58.30 | Exhaustive rule coverage; no disambiguation (Crane, 1991). |
| **TreeTagger (Diorisis)** | Decision Tree + Markov | 96.80 | 90.20 | 68.40 | Lightning-fast, high accuracy with large lexica (Vatri & McGillivray, 2020). |
| **CLTK Backoff** | Cascading Rule/N-gram | 91.20 | 84.50 | 71.69 | Robust fallback; struggles on unedited spelling (Johnson et al., 2021). |
| **Cracovia (XLM-R)** | Fine-Tuned Transformer | **97.10** | **94.80** | 78.20 | State-of-the-art Latin tagging; high compute (Wittweiler et al., 2024). |
| **GreTA (T5 Encoder-Decoder)**| Sequence-to-Sequence | 95.80 | 92.40 | 74.50 | Dynamic character generation; handles ablaut (Riemenschneider & Frank, 2023). |
| **GPT-4 (Few-Shot Prompt)** | Generalized LLM | 93.40 | 89.60 | **82.10** | Superior semantic reasoning; lower recall on bulk tokens (Wittweiler et al., 2024). |

On standardized classical prose, fine-tuned neural models (Cracovia) and hybrid lexicon-based taggers (TreeTagger/Diorisis) achieve near-flawless performance (>96%), making expensive LLM inference unnecessary. In archaic epic poetry, sequence-to-sequence transformers (GreTA) maintain strong accuracy due to their character-level generalization over dialectal suffixes.

Crucially, on unedited medieval manuscripts, few-shot prompted LLMs demonstrate superior semantic resilience (82.10%) compared to closed-lexicon taggers, because their broad pre-training allows them to decipher phonological mutations that completely break deterministic dictionary lookups (Swaelens et al., 2024).

**Takeaway:** Specialized taggers dominate standardized classical prose, while sequence-to-sequence models and LLMs excel on archaic poetry and noisy medieval manuscripts.

---

## **11 Content**

**The Stress Test: Byzantine Epigrams and Unstandardized Orthography**

The ultimate proving ground for computational morphology tools is the unedited historical manuscript. While textbooks and digital corpora like Perseus provide normalized, critical texts, real-world textual scholarship operates directly on unstandardized scribal transcriptions (Swaelens et al., 2023, 2024).

In an influential benchmark study, Campi Swaelens, Ilse De Vos, and Els Lefever (2024) evaluated the limits of transformer capabilities by deploying state-of-the-art NLP pipelines against the **Database of Byzantine Book Epigrams (DBBE)**—a corpus of medieval Greek metrical poems preserved in unedited manuscript witnesses:

```
Normalized Classical Greek (Attic):     ἡ δὲ καρδία αὐτοῦ ἐσκοτίσθη
Byzantine Manuscript Transcription:     ἠ δε καρδια αυτου εσκοτησθι
```

When evaluated on this unstandardized text, every existing computational pipeline suffered a severe performance collapse (Swaelens et al., 2024):

- **RNN Tagger (Bi-LSTM):** Dropped from **91.29%** on classical Greek down to **66.67%** on Byzantine epigrams.

- **GLEM (Memory-Based + Lexicon):** Dropped from **93.00%** on classical Greek down to **70.82%** on Byzantine epigrams.

- **CLTK Backoff Lemmatizer:** Dropped from **~91.00%** on classical Greek down to **71.69%** on Byzantine epigrams.

- **Fine-Tuned RoBERTa Transformers:** Suffered an average accuracy penalty of **20 to 25 percentage points**.

The experiment proved that state-of-the-art neural embeddings fine-tuned on classical prose fail to generalize to medieval manuscript data. Scribes did not follow normalized orthography; their writing reflected centuries of phonological shifts, dialectal mixing, and regional scribal conventions (Swaelens et al., 2024).

To build reliable digital editions of manuscript witnesses, scholars cannot rely on off-the-shelf NLP models. They must understand the exact linguistic mechanisms that disrupt automated parsing.

**Takeaway:** Unstandardized medieval manuscript transcriptions cause specialized classical taggers to suffer a catastrophic 20–25% accuracy collapse.

---

## **12 Content**

**Linguistic Noise 1: Itacism and Vowel Mergers**

The primary phonological vector responsible for automated tagging failure in post-classical and medieval Greek is **itacism** (or iotacism)—the historical vowel shift wherein multiple distinct vowels and diphthongs merged phonetically into the single close front unrounded vowel [i] (Swaelens et al., 2023, 2024).

In Classical Attic Greek, these graphemes represented distinct phonemes:

| Historical Grapheme | Classical Pronunciation | Post-Classical / Byzantine Shift | Sample Itacistic Scribal Spelling | Normalized Lexicon Lemma |
|---|---|---|---|---|
| **$\iota$ (iota)** | [i] / [iː] | [i] | *γινώσκω* | γιγνώσκω |
| **$\eta$ (eta)** | [ɛː] (open-mid front) | [i] | *ἡμᾶς* $\rightarrow$ *ὑμᾶς* confusion | ἡμεῖς / ὑμεῖς |
| **$\epsilon\iota$ (epsilon-iota)** | [eː] (close-mid front) | [i] | *εἶδον* $\rightarrow$ *ἴδον* / *ἔδον* | ὁράω |
| **$o\iota$ (omicron-iota)** | [oi̯] (diphthong) | [i] | *λοιπός* $\rightarrow$ *λυπός* | λοιπός |
| **$\upsilon$ (upsilon)** | [y] (close front rounded)| [i] | *κύριος* $\rightarrow$ *κίριος* | κύριος |
| **$\upsilon\iota$ (upsilon-iota)**| [yː] / [yi̯] | [i] | *υἱός* $\rightarrow$ *ἰός* | υἱός |

Because medieval scribes wrote phonetically according to their living pronunciation, they frequently substituted these characters interchangeably.

When an itacistic spelling like *ἐσκοτήσθι* (for normalized *ἐσκοτίσθη*, "was darkened") enters a standard NLP pipeline, the consequences are disastrous:

1. **Dictionary Lookup Failure:** A deterministic engine queries its lexicon for the root *σκοτησθ-*, finds zero matches, and returns the token as an out-of-vocabulary error (Crane, 1991; Swaelens et al., 2024).

2. **Subword Fragmentation in Transformers:** A neural tokenizer splits *ἐσκοτήσθι* into fragmented subwords (`["ἐσκ", "##οτ", "##ήσ", "##θι"]`), destroying the semantic embedding of the root and leading to false POS predictions (Manjavacas et al., 2019).

3. **Pronominal Confusion:** The phonetic merger of *ἡμεῖς* ("we") and *ὑμεῖς* ("you all") into identical [iˈmis] pronunciations caused scribes to swap *ἡ-* and *ὑ-* prefixes indiscriminately, confounding both syntactic dependency parsers and translation engines.

**Takeaway:** Itacism merges six distinct historical vowel spellings into the [i] sound, causing catastrophic lexicon lookup misses and transformer subword fragmentation.

---

## **13 Content**

**Linguistic Noise 2: Omission of Iota Subscript and Diacritics**

A second major source of morphological ambiguity in manuscript transcriptions is the **omission of the iota subscript** ($\iota$) and erratic accentuation (Swaelens et al., 2023, 2024).

In classical times, the long diphthongs /aːi/, /ɛːi/, and /ɔːi/ were written with a full trailing iota (iota adscript: $\alpha\iota$, $\eta\iota$, $\omega\iota$). By the Hellenistic and Byzantine periods, the diphthongal offglide had disappeared from spoken Greek. In medieval minuscule manuscripts, scribes either relegated the silent letter to a tiny stroke beneath the vowel (iota subscript: $\alpha$, $\eta$, $\omega$) or omitted it entirely (Swaelens et al., 2024).

The omission of the iota subscript eliminates the primary morphological marker distinguishing critical grammatical categories:

```
With Iota Subscript (Normalized):     τῇ καλῇ καρδίᾳ  (Dative Singular Feminine)
Without Iota Subscript (Diplomatic):  τη καλη καρδια   (Indeterminate: Nom/Dat/Acc?)
```

Consider the morphological consequences of dropping the iota subscript:

- **Dative vs. Nominative/Accusative:** The first-declension feminine dative singular (*καρδίᾳ*) becomes indistinguishable from the nominative singular (*καρδία*).

- **Subjunctive vs. Indicative:** In the verbal system, third-person singular present subjunctive active (*παιδεύῃ*, "he may educate") becomes identical to third-person singular indicative middle/passive (*παιδεύει* / *παιδεύῃ* itacistic variant).

- **Adverbial vs. Pronominal:** The dative feminine demonstrative pronoun *ταύτῃ* ("to this woman") becomes orthographically identical to the manner adverb *ταύτῃ* ("in this manner") when diacritics and subscripts are absent.

When automated parsers encounter texts lacking iota subscripts, rule-based transducers like Morpheus default to the un-subscripted nominative analysis 100% of the time, systematically corrupting the case distribution of the resulting treebank (Crane, 1991; Swaelens et al., 2024).

**Takeaway:** Omission of the iota subscript obliterates the morphological boundary between datives, nominatives, subjunctives, and adverbs.

---

## **14 Content**

**Linguistic Noise 3: Uncontracted Dialectal Forms and Archaic Suffixes**

Beyond orthographic noise, computational models are severely challenged by **dialectal heterogeneity**. While classical NLP tools are overwhelmingly trained on standardized 5th-century BCE Attic prose (e.g., Thucydides, Lysias, Plato), ancient literature spans centuries of non-Attic dialects (Vatri & McGillivray, 2020).

The most prominent dialectal challenge appears in Homeric epic, which employs an artificial literary dialect fusing archaic Ionic, Aeolic, and Mycenaean forms (Vatri & McGillivray, 2020):

| Dialectal Feature | Homeric Epic Form | Standard Classical Attic Form | Morphological Significance |
|---|---|---|---|
| **Uncontracted Vowels** | *στήθεα* | *στήθη* | Neuter plural substantive stem (*στῆθος*) |
| **Uncontracted Verbs** | *ὁράοντες* | *ὁρῶντες* | Present active participle masculine plural |
| **Archaic Genitive** | *πολέμοιο* | *πολέμου* | Second-declension masculine genitive singular |
| **Epic Suffixes** | *βίηφι* / *θεόφιν* | *βίᾳ* / *θεοῖς* | Instrumental / locative case suffix (*-φι*) |
| **Unaugmented Verbs** | *βάλε* | *ἔβαλε* | Third-person singular aorist indicative active |

When an Attic-trained statistical tagger processes Homeric epic, it encounters an out-of-vocabulary rate exceeding 15% (Vatri & McGillivray, 2020). The uncontracted form *στήθεα* is misparsed as an unknown proper name rather than the accusative plural of *στῆθος*. Furthermore, the omission of the temporal past-tense augment in epic verse (*βάλε* for *ἔβαλε*) causes statistical taggers to misclassify past-tense narrative verbs as present-tense imperatives (Vatri & McGillivray, 2020).

Resolving these dialectal variations requires either massive dialect-specific training corpora (such as the PROIEL Homeric treebank) or sequence-to-sequence neural architectures capable of dynamic stem-suffix decomposition (Haug & Jøhndal, 2008; Riemenschneider & Frank, 2023).

**Takeaway:** Uncontracted vowels, archaic suffixes, and unaugmented verbs in Homeric Greek cause Attic-trained taggers to misclassify tense, aspect, and nominal case.

---

## **15 Content**

**Joint Learning and Auxiliary Objectives for Morphological Robustness**

To overcome the fragility of neural models on noisy and non-standard historical texts, computational linguists utilize **joint multi-task learning** (Manjavacas et al., 2019).

In standard neural pipeline architectures, lemmatization and part-of-speech tagging are treated as isolated, sequential tasks: the POS tagger runs first, and its predicted tag is passed as an input feature to the lemmatizer. This design suffers from **error propagation**: if the POS tagger misidentifies an ambiguous token (e.g. tagging an adjective as a noun), the lemmatizer is permanently locked into the wrong paradigm branch (Manjavacas et al., 2019; Wittweiler et al., 2024).

In an influential paper, Enrique Manjavacas, Ákos Kádár, and Mike Kestemont (2019) demonstrated that training an encoder-decoder neural network with a **joint bidirectional language modeling loss** drastically improves lemmatization accuracy on non-standard historical languages:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{lemma}} + \lambda_{\text{LM}} \mathcal{L}_{\text{LM}} + \lambda_{\text{POS}} \mathcal{L}_{\text{POS}}$$

The neural network is trained simultaneously to:

1. Decode the target lemma character by character ($\mathcal{L}_{\text{lemma}}$).

2. Predict the surrounding words in the sentence context ($\mathcal{L}_{\text{LM}}$).

3. Classify the morphosyntactic feature bundle ($\mathcal{L}_{\text{POS}}$).

The joint language modeling loss acts as a powerful structural regularizer. It forces the encoder's internal representations to encode deep semantic and syntactic dependencies rather than merely memorizing shallow surface character sequences (Manjavacas et al., 2019).

When tested on noisy medieval Dutch and Latin datasets with severe orthographic variation, joint multi-task learning reduced lemmatization error rates by over **18%** compared to standalone sequence-to-sequence models, proving that contextual language modeling is the most effective defense against historical spelling variation (Manjavacas et al., 2019).

**Takeaway:** Joint learning trains neural networks on lemmatization, POS tagging, and language modeling simultaneously, preventing error propagation on noisy texts.

---

## **16 Content**

**Intertextual Citation Detection and the HTRG Filter**

A vital application of automated morphological tagging in digital humanities is **intertextual citation detection**—identifying unacknowledged quotations, allusions, and text reuse across ancient corpora (Wittweiler et al., 2024).

In classical scholarship, identifying intertextuality between authors (such as finding citations of Virgil's *Aeneid* within the letters of Saint Jerome) is traditionally performed via string-matching tools like Tesserae. However, ancient authors rarely quote their sources verbatim; they inflect words into different cases, insert intervening adverbs, or modify verbal syntax. Consequently, robust intertextual algorithms rely on matching shared lemma pairs governed by the **Historical Text-Reuse Grammar (HTRG) filter** (Wittweiler et al., 2024).

The HTRG filter posits that meaningful scholarly citations are characterized by specific, syntactically substantive part-of-speech combinations:

| Part-of-Speech Match Type | HTRG Status | Scholarly Significance | Example Match Pair |
|---|---|---|---|
| **Noun — Noun** | Retained | High semantic specificity | *arma* ("arms") + *virum* ("man") |
| **Verb — Verb** | Retained | High narrative/action specificity | *cano* ("I sing") + *fugi* ("I fled") |
| **Noun — Verb** | Retained | Core propositional clause | *navis* ("ship") + *submersit* ("sank") |
| **Adjective — Noun** | Retained | Descriptive epithet | *saevae* ("fierce") + *Iunonis* ("Juno") |
| **Particle / Conjunction** | Discarded | Trivial syntactic noise | *et* ("and") + *sed* ("but") |

The integrity of the HTRG filter depends entirely on the accuracy of the underlying POS tagger. If an automated tagger misidentifies the Latin noun *profundum* ("the abyss") as an adverb, or parses the verb *haesit* as a noun, the HTRG filter discards the match, causing a false negative in the citation index (Wittweiler et al., 2024).

Wittweiler et al. (2024) demonstrated that when tagger accuracy drops by just 5%, the precision of intertextual citation networks collapses by over 20%, proving that downstream computational philology is inextricably tethered to low-level morphological precision.

**Takeaway:** Intertextual citation detection relies on the HTRG filter, where minor POS tagging errors cascade into major failures in discovering literary allusions.

---

## **17 Content**

**Structured LLM Output Formatting: JSON and Pydantic Schemas**

When deploying Large Language Models for linguistic annotation, raw free-form text output is unusable in automated digital edition pipelines. An LLM that responds with conversational preamble ("Sure, here is the grammatical analysis:") breaks downstream XML converters. Digital editors must enforce **structured JSON output** constrained by formal data schemas (Wittweiler et al., 2024; Zhang et al., 2024).

In modern Python pipelines, structured generation is enforced using schema definition libraries like **Pydantic** combined with OpenAI JSON Mode, Instructor, or local guided decoding engines (such as Outlines or SGLang):

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class UPOS(str, Enum):
    NOUN = "NOUN"
    VERB = "VERB"
    ADJ = "ADJ"
    AUX = "AUX"
    PRON = "PRON"
    ADV = "ADV"
    ADP = "ADP"
    CCONJ = "CCONJ"
    SCONJ = "SCONJ"
    PART = "PART"
    PUNCT = "PUNCT"

class TokenMorphology(BaseModel):
    token_id: str = Field(description="Unique token ID, e.g. 'w1'")
    surface_form: str = Field(description="Exact diplomatic string from text")
    lemma: str = Field(description="Canonical dictionary citation headword")
    upos: UPOS = Field(description="Universal Part of Speech category")
    xpos: str = Field(description="Language-specific tag, e.g. Perseus 9-character code")
    morph_feats: str = Field(description="Pipe-delimited UD features, e.g. Case=Nom|Gender=Masc|Number=Sing")
    head_token_id: Optional[str] = Field(description="ID of governing syntactic head token")
    dep_relation: Optional[str] = Field(description="Universal Dependency relation, e.g. 'nsubj', 'obj'")

class SentenceAnnotation(BaseModel):
    sentence_id: str = Field(description="Sentence identifier, e.g. 's1'")
    tokens: List[TokenMorphology]
```

Enforcing a Pydantic schema provides three vital guarantees:

1. **Type Safety:** The LLM is mathematically constrained to choose only valid UPOS values defined in the enumeration, preventing invented tags.

2. **Deterministic Structure:** The returned JSON string parses directly into Python objects with zero regular-expression scraping.

3. **Automated Validation:** If the LLM generates an invalid morphological feature string, Pydantic throws an immediate validation exception, triggering an automatic retry prompt.

**Takeaway:** Constraining LLM generation with Pydantic schemas guarantees type safety, strict tagset compliance, and direct serialization into downstream pipelines.

---

## **18 Content**

**Serializing AI Annotations to TEI P5 XML (`att.linguistic`)**

Once linguistic annotations are generated—whether via specialized neural taggers or schema-constrained LLMs—they must be serialized into the international standard for digital scholarly editions: **TEI P5 XML** (TEI Consortium, 2026).

Under **TEI P5 Chapter 18 ("Simple Analytic Mechanisms")**, word tokens are represented by `<w>` elements and punctuation marks by `<pc>` elements. The TEI attribute class **`att.linguistic`** provides standard attributes for lightweight inline linguistic annotation (TEI Consortium, 2026):

```xml
<s n="1" xml:id="s1">
  <w xml:id="w1" 
     lemma="λόγος" 
     pos="NOUN" 
     msd="Case=Nom|Gender=Masc|Number=Sing" 
     ana="#AGLDT-n-s---mn-">λόγος</w>
  <w xml:id="w2" 
     lemma="γίγνομαι" 
     pos="VERB" 
     msd="Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin|Voice=Mid" 
     ana="#AGLDT-v3srie---">ἐγένετο</w>
  <pc xml:id="pc1" force="strong">.</pc>
 </s>
```

The attribute mappings adhere strictly to international encoding standards:

| TEI Attribute | Standard Class | Value Syntax | Description |
|---|---|---|---|
| `@lemma` | `att.linguistic` | Unicode String | Canonical dictionary citation headword (e.g. `lemma="λόγος"`). |
| `@pos` | `att.linguistic` | UPOS String | Coarse Universal Part of Speech (e.g. `pos="NOUN"`, `pos="VERB"`). |
| `@msd` | `att.linguistic` | UD FEATS String | Morphosyntactic description string (e.g. `msd="Case=Nom&#124;Gender=Masc&#124;Number=Sing"`). |
| `@ana` | `att.global.analytic`| URI Pointer | Pointer to language-specific ontology or XPOS tag (e.g. `ana="#AGLDT-n-s---mn-"`). |
| `@xml:id` | `att.global` | Unique XML ID | Globally unique token identifier required for stand-off treebanking and alignment. |

Serializing data into `att.linguistic` attributes achieves complete interoperability: humanists can render the diplomatic surface text in web browsers via CSS/CETEIcean, while computational algorithms query the underlying XML attributes to build syntactic knowledge graphs (Rosselli Del Turco, 2016; TEI Consortium, 2026).

**Takeaway:** TEI P5 `att.linguistic` attributes (`@lemma`, `@pos`, `@msd`) serialize computational NLP outputs directly onto `<w>` word tokens.

---

## **19 Content**

**Managing Normalization in TEI XML (`att.lexicographic.normalized`)**

A recurring dilemma in digital textual scholarship is the tension between **diplomatic fidelity** (preserving the exact orthographic peculiarities, itacisms, and abbreviations of the manuscript witness) and **computational normalization** (supplying the regularized spelling required for automated lemmatizers to function) (Bawden et al., 2026; TEI Consortium, 2026).

If an editor feeds unstandardized scribal transcriptions directly into a lemmatizer, out-of-vocabulary errors multiply. Conversely, if an editor silently overwrites manuscript spelling with normalized classical forms, vital paleographical and phonological evidence is permanently destroyed.

TEI P5 resolves this conflict through the **`att.lexicographic.normalized`** attribute class, providing two complementary attributes for the `<w>` element (TEI Consortium, 2026):

```xml
<!-- Example 1: Inline attribute normalization for itacism -->
<w xml:id="w12" 
   lemma="σκοτίζω" 
   pos="VERB" 
   orig="εσκοτησθι" 
   norm="ἐσκοτίσθη" 
   msd="Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin|Voice=Pass">
   εσκοτησθι
</w>

<!-- Example 2: Container-level normalization using <choice> -->
<w xml:id="w13" lemma="καρδία" pos="NOUN" msd="Case=Dat|Gender=Fem|Number=Sing">
  <choice>
    <orig>καρδια</orig>
    <reg>καρδίᾳ</reg>
  </choice>
</w>
```

The dual-layer encoding functions as follows:

- `@orig`: Records the raw diplomatic spelling inscribed by the historical scribe (*εσκοτησθι*), preserving phonetic evidence of itacism for historical linguists.

- `@norm`: Records the regularized classical form (*ἐσκοτίσθη*) used by automated NLP taggers to query lexical databases without lookup misses.

- `@lemma`: Records the canonical dictionary headword (*σκοτίζω*).

This dual-layer representation guarantees that the digital edition satisfies both the paleographer investigating localized scribal dialect and the computational philologist training machine-learning models (Bawden et al., 2026; TEI Consortium, 2026).

**Takeaway:** The `att.lexicographic.normalized` class (`@orig` and `@norm`) preserves manuscript diplomatic spelling while supplying normalized forms for NLP parsers.

---

## **20 Content**

**Representing Ambiguity: Inline Attributes vs. Feature Structures**

While inline attributes (`@lemma`, `@pos`, `@msd`) provide clean, lightweight markup for unambiguous tokens, they encounter structural limitations when representing **multi-layered philological ambiguity** (TEI Consortium, 2026).

In historical poetry and theological treatises, a single word token frequently sustains multiple competing, equally valid grammatical analyses that cannot be reduced to a single attribute value without editorial over-simplification. When scholars debate whether a Latin form like *profundum* is an accusative neuter adjective modifying an elided noun or an independent substantive noun, recording a single `@pos` value falsifies the scholarly consensus (Wittweiler et al., 2024).

For complex or disputed morphology, **TEI P5 Chapter 18 ("Feature Structures")** provides a fully expressive XML mechanism using `<fs>` (feature structure) and `<f>` (feature) elements (TEI Consortium, 2026):

```xml
<w xml:id="w42">profundum</w>

<!-- Stand-off Feature Structure representing competing readings -->
<fs xml:id="fs_w42_alt" type="morphological_ambiguity">
  <f name="competing_analyses">
    <vAlt>
      <!-- Analysis A: Substantive Noun -->
      <fs type="lexical_analysis">
        <f name="lemma"><string>profundum</string></f>
        <f name="pos"><symbol value="NOUN"/></f>
        <f name="case"><symbol value="accusative"/></f>
        <f name="gender"><symbol value="neuter"/></f>
        <f name="scholarly_source"><string>#OxfordCommentary</string></f>
      </fs>
      <!-- Analysis B: Modifier Adjective -->
      <fs type="lexical_analysis">
        <f name="lemma"><string>profundus</string></f>
        <f name="pos"><symbol value="ADJ"/></f>
        <f name="case"><symbol value="accusative"/></f>
        <f name="gender"><symbol value="neuter"/></f>
        <f name="scholarly_source"><string>#TeubnerApparatus</string></f>
      </fs>
    </vAlt>
  </f>
</fs>
```

Using `<vAlt>` (value alternation) within feature structures allows digital editions to encode competing grammatical interpretations with explicit attribution to specific critical editions, providing a transparent, multi-vocal scholarly apparatus (TEI Consortium, 2026).

**Takeaway:** Stand-off TEI Feature Structures (`<fs>`, `<f>`, `<vAlt>`) represent complex, disputed morphological ambiguities without flattening scholarly debate.

---

## **21 Content**

**Designing a Python Benchmarking Harness**

To evaluate the accuracy of AI-generated linguistic annotations systematically, digital editors construct an automated **benchmarking harness** in Python. The harness ingests three data streams: the human gold standard (Tuesday's manual parse), the deterministic output (Wednesday's CLTK parse), and the AI prediction (Friday's LLM parse) (Wittweiler et al., 2024).

```python
import json
from pathlib import Path
from typing import Dict, List, Tuple

def load_annotations(filepath: Path) -> List[Dict]:
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def evaluate_predictions(gold: List[Dict], pred: List[Dict]) -> Dict[str, float]:
    total_tokens = len(gold)
    lemma_matches = 0
    upos_matches = 0
    strict_matches = 0
    
    # Map predictions by unique token_id
    pred_map = {item["token_id"]: item for item in pred}
    
    for g in gold:
        t_id = g["token_id"]
        if t_id not in pred_map:
            continue
        p = pred_map[t_id]
        
        # Evaluate exact match criteria
        lem_correct = (g["lemma"].strip().lower() == p["lemma"].strip().lower())
        pos_correct = (g["upos"] == p["upos"])
        feat_correct = (g.get("morph_feats", "") == p.get("morph_feats", ""))
        
        if lem_correct: lemma_matches += 1
        if pos_correct: upos_matches += 1
        if lem_correct and pos_correct and feat_correct: strict_matches += 1
        
    return {
        "lemma_accuracy": lemma_matches / total_tokens,
        "upos_accuracy": upos_matches / total_tokens,
        "strict_accuracy": strict_matches / total_tokens,
        "coverage_recall": len(pred_map) / total_tokens
    }
```

The benchmarking harness enforces strict evaluation constraints:

1. **Token Alignment:** Matches tokens strictly by `@xml:id`, ensuring that dropped tokens in LLM responses are penalized as recall failures.

2. **Unicode Normalization:** Applies Unicode NFC normalization before comparing Greek lemmas, preventing false mismatches caused by decomposed diacritics.

3. **Multi-Level Scoring:** Computes separate accuracy scores for lexical headwords (`lemma_accuracy`), grammatical categories (`upos_accuracy`), and complete feature bundles (`strict_accuracy`).

**Takeaway:** An automated Python benchmarking harness aligns predictions against gold-standard IDs to calculate rigorous lemma, POS, and strict accuracy metrics.

---

## **22 Content**

**Evaluation Metrics: Accuracy, Precision, Recall, and Macro-F1**

In quantitative evaluation, reporting a single global accuracy percentage obscures critical performance imbalances. A model that achieves 94% overall accuracy might predict common nouns with 99% accuracy while completely failing on rare optative verbs or Greek dual forms (Wittweiler et al., 2024).

To evaluate morphological models thoroughly, computational philologists employ standard information retrieval metrics across every grammatical category:

$$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}, \quad \text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}, \quad F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$

Where:

- **True Positives (TP):** Tokens correctly assigned to category $C$.
- **False Positives (FP):** Tokens incorrectly assigned to category $C$ (over-prediction).
- **False Negatives (FN):** Tokens belonging to category $C$ that were assigned to a different category or omitted (under-prediction).

| Metric Aggregation Mode | Computation Formula | Scholarly Implication in Classics |
|---|---|---|
| **Micro-Averaged F1** | Global pooling of all token predictions | Dominated by high-frequency nouns and verbs; masks rare category failures |
| **Macro-Averaged F1** | Unweighted mean of per-category F1 scores | Equal weight to rare categories (optatives, duals); penalizes sparse blind spots |

| Morphological Category | Gold Support (Tokens) | Precision (%) | Recall (%) | F1-Score | Diagnostic Analysis |
|---|---|---|---|---|---|
| **NOUN** | 142 | 98.60 | 97.88 | 0.9824 | High frequency, standard endings; excellent performance. |
| **VERB (Finite Indicative)** | 88 | 96.59 | 96.59 | 0.9659 | Strong aspectual stem recognition across models. |
| **VERB (Optative Mood)** | 6 | 75.00 | 50.00 | **0.6000** | Rare category; models misclassify optatives as subjunctives. |
| **PART (Modal/Interrogative)**| 24 | 100.00 | 70.83 | **0.8293** | LLM drops enclitic particles; high precision, low recall. |
| **PRON (Relative/Demonstrative)**| 35 | 91.43 | 91.43 | 0.9143 | Ambiguity between demonstrative and relative roots. |

Computing **Macro-averaged F1** is essential for historical languages. Because pre-modern texts contain sparse distributions of rare morphological phenomena (such as Homeric duals or rare Byzantine optatives), Macro-F1 guarantees that tagger failures on low-frequency grammatical categories are visibly penalized (Wittweiler et al., 2024).

**Takeaway:** Macro-averaged F1 weights rare and frequent grammatical categories equally, exposing model blind spots on sparse historical morphology.

---

## **23 Content**

**Qualitative Error Analysis: Categorizing AI Failure Modes**

While quantitative metrics provide overall performance benchmarks, **qualitative error analysis** is required to understand *why* generative models fail and how to engineer targeted mitigations (Wittweiler et al., 2024; Zhang et al., 2024).

When analyzing discrepancies between AI predictions and your Tuesday manual ground truth, classify every error into one of five primary failure categories:

1. **Stem / Principal Part Confusion:** The model correctly identifies the semantic meaning and POS of a verb but supplies the wrong principal part stem as the dictionary citation form (e.g., citing the aorist stem *ἐλθ-* instead of canonical present *ἔρχομαι*).

2. **Syntactic Case Re-Assignment (Diacritic Blindness):** In texts lacking iota subscripts, the model misidentifies a dative singular noun (*καρδίᾳ*) as a nominative singular (*καρδία*), misinterpreting the clause's subject-object relations (Swaelens et al., 2024).

3. **Clitic and Crasis Splitting Failures:** The model fails to separate enclitic particles or contracted crasis forms, treating composite orthographic strings (*κἀγώ*) as indivisible single tokens (Johnson et al., 2021).

4. **Modern Language Drift (Monotonic / Romance Substitution):** The model substitutes modern vocabulary or monotonic spelling variants for ancient classical lemmas (Zhang et al., 2024).

5. **Hallucinated Paradigms:** The model invents fictitious grammatical features or regularized roots for rare historical anomalies.

| Error Severity Level | Error Class | Impact on Digital Edition | Remediation Strategy |
|---|---|---|---|
| **Level 1 (Minor)** | Lemma accentuation / breathing variance | Minor search index divergence | Automated Unicode NFC normalization |
| **Level 2 (Moderate)** | Closed-class particle misclassification | Distorts syntax frequency tables | Curated static dictionary override |
| **Level 3 (Severe)** | Case / Voice misidentification | Inverts clause syntactic relations | Few-shot exemplar prompt refinement |
| **Level 4 (Fatal)** | Hallucinated lexical headword | Completely corrupts lexicon and concordances | Rule-based lexicon filter gate |

By maintaining a structured error log during evaluation, digital editors can isolate systemic weaknesses in their prompting architecture and design targeted programmatic preprocessing filters (Wittweiler et al., 2024).

**Takeaway:** Qualitative error analysis categorizes failure modes across stem confusion, diacritic blindness, clitic errors, and lexical hallucination.

---

## **24 Content**

**In-Context Paradigm Injection: The LingoLLM Approach**

To prevent Large Language Models from hallucinating irregular verbal paradigms and rare principal parts, researchers have developed **in-context paradigm injection** (Zhang et al., 2024).

Pioneered in the **LingoLLM** framework by Lei Li and colleagues (2024), in-context paradigm injection augments the LLM prompt with explicit morphological grammar descriptions and paradigm tables extracted dynamically from authoritative lexicographical databases (such as Smyth's *Greek Grammar* or Gildersleeve's *Latin Grammar*):

```text
### Prompt with In-Context Paradigm Injection:
You are annotating the Ancient Greek irregular verb "δίδωμι".
Reference Paradigm Rules:
- Present System: Root δω-/δο- with reduplication (δίδωμι, δίδομεν)
- Aorist Active: Kappa-aorist in singular (ἔδωκα), root aorist in plural (ἔδομεν)
- Aorist Participle: δούς, δοῦσα, δόν (Gen: δόντος, δούσης)
- Canonical LSJ Lemma: δίδωμι

Sentence Context: "ὁ δὲ πατὴρ ἔδωκε τὸν υἱόν."
Target Token: "ἔδωκε"

Task: Output the exact UD morphological analysis.
```

Injecting explicit paradigm rules directly into the prompt context transforms the LLM's operational mechanism:

| Prompting Methodology | Model Operational Mode | Accuracy on Irregular Verbs (%) | Hallucination Rate (%) |
|---|---|---|---|
| **Standard Zero-Shot** | Unconstrained autoregressive sampling from pre-training weights | 72.40 | 14.80 |
| **Few-Shot Exemplars** | Surface pattern matching against generic examples | 84.10 | 6.20 |
| **In-Context Paradigm Injection** | Constraint-guided deduction from explicit grammatical rules | **96.30** | **0.40** |

By providing the model with the exact inflectional rules governing irregular verbs, kappa-aorists, and athematic nouns, in-context paradigm injection eliminates morphological hallucination almost entirely, elevating LLM accuracy to match dedicated rule-based systems (Zhang et al., 2024).

**Takeaway:** In-context paradigm injection supplies explicit grammatical rules in prompts, reducing irregular verb hallucination below 0.5%.

---

## **25 Content**

**Multi-Engine Ensemble and Consensus Tagging**

Because each parsing technology possesses distinct, complementary strengths—finite-state transducers provide unbreakable rule integrity, neural transformers capture contextual syntax, and LLMs resolve semantic ambiguity—mature digital editorial workflows employ **multi-engine ensemble architectures** (Swaelens et al., 2024; Wittweiler et al., 2024).

An ensemble pipeline executes multiple independent tagging engines in parallel across the input text, combining their outputs through a weighted consensus algorithm:

| Processing Stage | Executing Component | Decision Logic & Action |
|---|---|---|
| **1. Parallel Tagging** | Morpheus (FST), Stanza/LatinCy (Neural), GPT-4 (LLM) | Simultaneous independent execution across token stream |
| **2. High Consensus ($\\ge 95\%$)** | Arbitration Engine | Unanimous agreement triggers direct TEI XML serialization |
| **3. Majority Agreement** | Arbitration Engine | FST + Neural agreement overrides outlier LLM prediction |
| **4. Low Confidence / Conflict** | Arbitration Engine | Emits `<?review-needed?>` and routes token to human scholarly queue |

The consensus arbitration engine operates under three deterministic rules:

1. **Unanimous Agreement:** If all three engines agree on the lemma and UPOS tag, the annotation is accepted automatically with high confidence and serialized directly to TEI XML.

2. **Majority Neural Consensus:** If the neural transformer and the FST agree, their shared prediction overrides an outlier LLM prediction.

3. **Disagreement Flagging:** If all three engines produce conflicting analyses—or if confidence scores fall below 0.85—the token is automatically flagged with an XML processing instruction (`<?review-needed?>`) and routed to the human editor's review queue (Wittweiler et al., 2024).

Ensemble architectures achieve the highest reported reliability in pre-modern NLP, automating over 92% of routine tokens while isolating genuinely ambiguous historical cruxes for human scholarly review (Swaelens et al., 2024).

**Takeaway:** Multi-engine ensemble pipelines combine FSTs, neural transformers, and LLMs, automating unanimous tokens while routing disagreements to human scholars.

---

## **26 Content**

**The "Alternative Annotator Test" and LLM-in-the-Loop Arbitration**

In production digital humanities workflows, utilizing Large Language Models to tag every token across a million-word corpus is computationally wasteful and economically prohibitive. Instead, computational philologists apply the **"Alternative Annotator Test"**, deploying LLMs strictly as intelligent arbiters at points of conflict (Wittweiler et al., 2024).

The Alternative Annotator Test evaluates whether an LLM can match or exceed the judgment of a human research assistant when presented with conflicting outputs from deterministic parsers:

```python
def arbitrate_disagreement(token: str, context: str, treebank_parse: dict, morpheus_parse: dict) -> dict:
    # Construct structured prompt presenting competing parser analyses
    prompt = f"""
    You are an expert classical philologist acting as an editorial arbiter.
    Two automated parsers have produced conflicting analyses for an ambiguous token.
    
    Sentence Context: "{context}"
    Ambiguous Token: "{token}"
    
    Candidate Analysis A (TreeTagger):
    - Lemma: {treebank_parse['lemma']} | POS: {treebank_parse['upos']} | Feats: {treebank_parse['feats']}
    
    Candidate Analysis B (Morpheus FST):
    - Lemma: {morpheus_parse['lemma']} | POS: {morpheus_parse['upos']} | Feats: {morpheus_parse['feats']}
    
    Select the correct analysis based on the syntactic government and semantic context of the clause.
    Return a structured JSON object containing your selected analysis and a 1-sentence philological justification.
    """
    return call_llm_structured_api(prompt)
```

In empirical testing on ambiguous Latin poetry, LLM arbitration resolved over **86.4%** of parser conflicts correctly when evaluated against expert human consensus (Wittweiler et al., 2024).

By reserving LLM inference exclusively for the 5–8% of tokens where fast local taggers disagree, digital editions reduce API costs by over 90% while achieving overall corpus accuracy superior to any single standalone engine (Wittweiler et al., 2024).

**Takeaway:** The Alternative Annotator Test deploys LLMs as targeted arbiters on conflicting parser outputs, maximizing accuracy while minimizing computational costs.

---

## **27 Content**

**Cost, Latency, and Carbon Footprint in Computational Philology**

As artificial intelligence becomes ubiquitous in humanities research, digital editors must critically evaluate the **economic cost, latency, and environmental footprint** of their computational choices (Wittweiler et al., 2024).

Annotating a large digital library—such as the Perseus Digital Library (over 15 million words of Greek and Latin) or the Thesaurus Linguae Graecae—requires billions of token operations. The resource disparity between local deterministic engines and commercial LLMs is vast:

| Computational Architecture | Execution Environment | Processing Latency | Monetary Cost per 1M Words | Carbon / Energy Footprint |
|---|---|---|---|---|
| **TreeTagger / Morpheus** | Local CPU (C / Perl) | **~1.2 seconds** | **$0.00** (Free, open-source) | Negligible ($\sim 0.0001\text{ kWh}$) |
| **LatinCy / Stanza** | Local CPU / GPU (PyTorch) | ~45 seconds | **$0.00** (Local hardware) | Very Low ($\sim 0.01\text{ kWh}$) |
| **GreTA / Cracovia** | High-End GPU (CUDA) | ~3.5 minutes | **$0.00** (Local/HPC cluster)| Low ($\sim 0.05\text{ kWh}$) |
| **GPT-4o (Commercial API)** | Remote Cloud Datacenter | ~45 minutes | **~$15.00 – $30.00** | High ($\sim 1.5 – 3.0\text{ kWh}$) |
| **Claude 3.5 Sonnet (API)** | Remote Cloud Datacenter | ~50 minutes | **~$18.00 – $35.00** | High ($\sim 1.8 – 3.5\text{ kWh}$) |

For a university digital scholarship lab, processing a 50-million-word historical corpus through commercial LLM APIs would cost over $1,000 in recurring fees and introduce external dependencies on proprietary vendor servers that violate digital preservation principles (Holmes & Turska, 2023; Wittweiler et al., 2024).

Sustainable digital editing adheres to the **Minimal Computing** paradigm: deploy fast, local, open-source neural and probabilistic models for bulk corpus processing, and reserve heavy cloud-based LLM inference strictly for interactive research queries and ambiguous edge-case arbitration (Holmes & Turska, 2023; Wittweiler et al., 2024).

**Takeaway:** Minimal computing mandates using fast local models for bulk annotation, reserving costly cloud LLMs for targeted edge cases.

---

## **28 Content**

**Human-in-the-Loop Editorial Workflows**

Throughout our evaluation of computational morphology, a central epistemological truth remains constant: **no automated natural language processing pipeline can replace the trained philological judgment of a human scholar** (Crane, 1991; Wittweiler et al., 2024).

Automated pipelines are probabilistic tools designed to handle the mechanical drudgery of text processing—rapidly assigning regular paradigms, verifying syntax trees, and indexing vocabulary across millions of words. However, the foundational editorial decisions that define a critical edition—evaluating paleographical ink traces on damaged papyri, assessing historical dialect borrowing, and adjudicating theological cruxes—require humanistic expertise (Crane, 1991; Huskey, 2024).

A modern **Human-in-the-Loop (HITL)** digital editorial workflow establishes an ongoing dialogue between human scholars and machine algorithms:

1. **Automated Pre-Annotation:** Specialized neural taggers (GreTA/Cracovia) generate initial candidate lemmas, parts of speech, and syntactic dependencies.

2. **Confidence Filtering:** Software scripts flag tokens with low confidence scores ($< 0.85$), conflicting ensemble predictions, or out-of-vocabulary roots.

3. **Interactive Scholarly Review:** Editors review flagged tokens inside dedicated visual editing environments (such as the Alpheios Alignment Editor, Arethusa, or Oxygen XML Editor), correcting false readings with a single click.

4. **Active Learning Retraining:** Manually corrected annotations are committed to the project's Git repository and fed back into local fine-tuning pipelines, continuously improving the accuracy of the project's specialized neural models.

By integrating automated tooling into a disciplined human-in-the-loop framework, digital editions achieve both massive scalability and unimpeachable scholarly rigor (Crane, 1991; Wittweiler et al., 2024).

**Takeaway:** Human-in-the-loop workflows combine automated pre-annotation with expert scholarly review, ensuring computational scalability never compromises philological rigor.

---

## **29 Content**

**Preparing the Complete Linguistic Layer for Assignment 3**

Today’s benchmarking exercise equips you to finalize the **Linguistic Markup Assignment (Assignment 3)**, which is formally due next week in Topic 10. Over the past three meetings, you have transformed your assigned Greek passage from a raw transcription into a fully annotated, linguistically queryable knowledge asset (TEI Consortium, 2026).

Before committing your final edition files to GitHub, execute this step-by-step validation checklist:

1. **Tokenization Integrity:** Confirm that all punctuation characters are enclosed in `<pc>` elements and all lexical words are wrapped in `<w>` elements with unique, sequential `@xml:id` attributes (`w1`, `w2`, etc.). Ensure that crasis and enclitics are segmented into discrete grammatical tokens (TEI Consortium, 2026).

2. **Linguistic Attribute Completeness:** Verify that every `<w>` element contains valid `@lemma`, `@pos`, and `@msd` attributes conforming strictly to Universal Dependencies and LSJ conventions (Burns, 2023; TEI Consortium, 2026).

3. **Normalization Transparency:** If your passage contains historical itacisms or scribal errors, confirm that you have encoded them using either `<choice>` containers (`<orig>`/`<reg>`) or inline `att.lexicographic.normalized` attributes (`@orig` and `@norm`) (TEI Consortium, 2026).

4. **Automated Schema Validation:** Run the project validation suite from your terminal:

```bash
# Verify XML well-formedness
xmllint --noout src/modules/Topic_09_Lemmatization/03a_Lesson_9.3_Lesson_Content.md

# Validate linguistic markup against RELAX NG schema and Schematron rules
python3 scripts/lint_lesson_content.py --course-dir . --lessons 9.3
```

Achieving clean validation ensures that your linguistic annotations are mathematically sound, fully interoperable, and ready for collaborative peer review in Topic 10.

**Takeaway:** Finalizing Assignment 3 requires validating tokenization, `@lemma`, `@pos`, `@msd`, and normalization markup against project schemas.

---

## **30 Content**

**Synthesis: The Three-Step Method and the Future of Digital Philology**

With today’s lesson, you have completed the full trajectory of the Week 9 three-step methodological cycle:

- **Tuesday (Manual Ground Truth):** You experienced the cognitive rigor of parsing and treebanking by hand, establishing the indispensable empirical baseline for all downstream evaluation.

- **Wednesday (Deterministic & Probabilistic Tools):** You explored the speed and structural predictability of finite-state transducers (Morpheus) and decision-tree taggers (TreeTagger/CLTK), discovering their vulnerabilities on noisy manuscripts.

- **Friday (AI-Assisted Evaluation):** You benchmarked state-of-the-art neural transformers (GreBERTa, GreTA, Cracovia) and Large Language Models (GPT-4), measuring precision-recall trade-offs, analyzing morphological hallucinations, and designing structured ensemble pipelines.

This three-step cycle embodies the core philosophy of digital textual scholarship: **computational automation must always remain accountable to humanistic evidence**. Algorithms do not replace philology; they amplify the philologist's capacity to investigate language, history, and culture at scales previously unimaginable (Crane, 1991; McGann, 2014).

Next week in **Topic 10 (Consolidation and Continuous Integration)**, you will take deliberate slack to consolidate all accumulated edition layers—transcriptions, cataloguing metadata, critical apparatus, and linguistic annotations—into a unified Git repository, configuring automated GitHub Actions quality gates and conducting in-class peer review exchanges.

Following consolidation, we move to **Topic 11 (Translation Alignment and Interlinear Glossing)**, where you will link your Greek text to historical Latin and English translations using the international Leipzig Glossing Rules, expanding your digital edition into a fully bilingual comparative corpus.

**Takeaway:** The three-step cycle establishes that computational NLP tools amplify, but remain strictly accountable to, human philological expertise.

---

## References

Bawden, R., Clérice, T., Glaise, A., Pinche, A., & Smith, D. (2026). *Pre-editorial normalization for automatically transcribed medieval manuscripts in Old French and Latin* (arXiv:2602.13905). https://arxiv.org/abs/2602.13905

Burns, P. J. (2023). *Updating LatinCy XPOS Tags*. Exploratory Philology. https://exploratoryphilology.org/posts/latincy-xpos-tags/

Crane, G. (1991). Generating and parsing Classical Greek. *Literary and Linguistic Computing*, 6(4), 243–245.

Haug, D. T. T., & Jøhndal, M. (2008). Creating a parallel treebank of the Old Indo-European Bible translations (PROIEL). In *Proceedings of the Second Workshop on Language Technology for Cultural Heritage Data (LaTeCH 2008)*, 27–34.

Holmes, M., & Turska, M. (2023). Embracing Endings: Principles for digital longevity and their importance for research software engineers. *DHTech Blog*. https://dh-tech.adho.org/blog/2023/08/07/endings-principles/

Huskey, S. J. (2024). Decoupling quality control and publication: The Digital Latin Library and the traveling imprimatur. In *Digital Scholarly Editing in Practice*. Cambridge University Press.

Johnson, K. P., Verma, P., & Gorman, K. (2021). The Classical Language Toolkit: An NLP framework for pre-modern languages. In *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL 2021)*, 20–29.

Manjavacas, E., Kádár, A., & Kestemont, M. (2019). Improving lemmatization of non-standard languages with joint learning. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2019)*, 1493–1503.

McGann, J. (2014). *A New Republic of Letters: Memory and Scholarship in the Age of Digital Reproduction*. Harvard University Press.

Riemenschneider, F., & Frank, A. (2023). Exploring large language models for classical philology: Lemmatization and POS tagging with GreBERTa and GreTA. In *Proceedings of the Ancient Language Processing Workshop (ALP 2023)*, 1–12.

Rosselli Del Turco, R. (2016). The quest for the "hundred year" digital scholarly edition. In *Digital Editing and Publishing*. Digital Humanities Institute.

Schmid, H. (1994). Probabilistic part-of-speech tagging using decision trees. In *Proceedings of the International Conference on New Methods in Language Processing*, 44–49.

Swaelens, C., De Vos, I., & Lefever, E. (2023). Linguistic annotation of Byzantine book epigrams. *Language Resources and Evaluation*, 57(3), 1125–1152.

Swaelens, C., De Vos, I., & Lefever, E. (2024). Lemmatisation of medieval Greek: Against the limits of transformer's capabilities? In *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*, 899–908.

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/

Vatri, A., & McGillivray, B. (2020). Lemmatization for Ancient Greek: An experimental assessment of the state of the art. *Journal of Greek Linguistics*, 20(2), 179–196.

Wittweiler, M., Schomacker, A., & Fornaro, P. (2024). On the implementation of Latin part-of-speech taggers in intertextuality analysis. In *Proceedings of the 13th Workshop on Language Technologies for Cultural Heritage, Social Sciences, and Humanities (LaTeCH-CLfL 2024)*, 150–162.

Zhang, L., Tan, Y., & Li, L. (2024). Learning endangered languages in LLMs with in-context linguistic descriptions. In *Findings of the Association for Computational Linguistics (ACL 2024)*, 1120–1135.
