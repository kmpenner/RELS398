# Topic 08 (Topic_09_Lemmatization): Academic Deep Research Report

**Model:** 3.1 Pro (Deep Research)  
**Attachments:** 7 PDF(s)  
**Citations resolved:** 18

## Computational Morphology Tools Evaluation

ContentsShare & Export
Create

# Computational Morphology and Linguistic Annotation for Pre-Modern Corpora: A Comparative Methodological Evaluation

## Abstract and Executive Summary

The intersection of digital humanities, computational philology, and natural language processing (NLP) has fundamentally transformed the study of historical languages. For pre-modern linguistic corpora—such as Ancient Greek, Medieval Greek, and Latin—the dual tasks of assigning a dictionary headword to an inflected form (lemmatization) and categorizing its grammatical function within a syntactic hierarchy (part-of-speech or POS tagging) present profound computational challenges. Unlike modern, standardized languages, historical corpora are characterized by extreme morphological complexity, vast dialectal heterogeneity, and unstable orthography resulting from centuries of manuscript transmission. The primary thesis evaluated in this report posits that while automated morphological tagging and lemmatization pipelines, such as those provided by the Classical Language Toolkit (CLTK), enable the scalable linguistic annotation of pre-modern texts, both rule-based and neural taggers require systematic benchmarking against manual grammatical analysis to resolve dialectal ambiguity and non-standard orthography effectively.

This exhaustive analysis synthesizes the historical trajectory and current state of the art in computational morphology for ancient languages. It evaluates the paradigm shift from early finite-state transducers and rule-based systems, most notably Morpheus, to probabilistic Markov models like TreeTagger, and ultimately to contemporary neural architectures including transformer-based models (RoBERTa, T5) and Large Language Models (LLMs) such as GPT-4 and LLaMA. The comparative evaluation demonstrates that while machine-learning approaches excel in handling complex syntactic dependencies, they frequently falter when confronted with the orthographic noise of unedited manuscripts, such as Byzantine itacism, uncontracted Homeric forms, or the omission of the iota subscript. In these specific scenarios, hybrid approaches that combine neural sequence-to-sequence architectures with robust, manually curated lexicon lookups offer the highest accuracy and generalizability.

Furthermore, the serialization of these computational outputs into standardized interoperable frameworks—specifically the Text Encoding Initiative (TEI) P5 Chapter 18 guidelines and the Universal Dependencies (UD) schema—is essential for ensuring corpus longevity. Ultimately, the integration of these tools into textual editing curricula empowers scholars to conduct distant reading and large-scale intertextual analysis, provided that the inherent limitations of automated parsing are pedagogically addressed through human-in-the-loop validation and critical algorithmic literacy.

## Technical, Methodological, and Historical Foundations

To accurately assess the performance of modern computational toolkits, it is necessary to examine the underlying principles of lemmatization and morphological tagging, as well as the historical evolution of the algorithms designed specifically to process highly inflected historical languages.

### Lemmatization Principles and Morphological Complexity

Lemmatization is the algorithmic process of abstracting over morphological differences to map an inflected surface word form to its canonical dictionary headword (the lemma). For highly inflected languages like Ancient Greek and Latin, this task is inextricably linked to morphological tagging, which involves resolving token-lemma ambiguities by assigning grammatical categories based on the surrounding sentence context[1]. The complexity of lemmatization in historical contexts arises from three primary sources. First, morphological richness dictates that a single lemma may generate hundreds of unique surface forms through prefixation, thematic suffixation, and inflection. Second, token-lemma ambiguity requires sophisticated contextual modeling; for example, the Latin form *erat* must be recognized not merely as a generic verb, but specifically as the third-person singular imperfect active indicative of *sum* to differentiate it from homophonous forms[2]. Third, and most uniquely problematic for historical languages, spelling variation due to a lack of orthographic standardization creates sparse evidence for token-lemma mappings and conflates unrelated forms, vastly expanding the vocabulary space[1].

Historically, the dominant computational paradigm for automated lemmatization relied on binary edit-trees. In this approach, a token-lemma pair is analyzed to identify the longest common subsequence, and the algorithm recursively builds a decision tree detailing the prefix and suffix edits required to transform the token into the lemma[1]. While edit-tree induction effectively captures morphological regularity in languages relying heavily on predictable suffixation, it struggles profoundly with the irregular stem changes, ablaut, and reduplication characteristic of the Ancient Greek verbal system[3]. Consequently, contemporary state-of-the-art models increasingly treat lemmatization as a character-level string-transduction task utilizing encoder-decoder neural networks, which can learn complex, non-linear mappings from inflected forms to lemmas without relying on explicit, hand-crafted edit-rules[1].

### The Evolution of Computational Toolkits: From Morpheus to CLTK

The genesis of computational morphology for historical languages is inextricably linked to the Perseus Digital Library and the development of the Morpheus engine in 1991 by Gregory Crane[3]. Morpheus operates as a rule-based, finite-state morphological analyzer originally written in the C programming language[4]. It relies on a comprehensive stem dictionary and a finite-state engine that matches surface forms to potential morphological endings. While foundational to the discipline, Morpheus functions primarily as a morphological parser rather than a context-aware lemmatizer; it outputs all possible theoretical analyses for a given form, leaving the critical task of contextual disambiguation to human experts or subsequent statistical models[3].

The introduction of TreeTagger by Helmut Schmid in 1994 marked a significant shift toward probabilistic disambiguation in corpus linguistics[3]. TreeTagger employs a Markov Model augmented with decision trees to estimate contextual parameters, allowing it to predict both POS tags and lemmas simultaneously by calculating the most probable sequence of tags given the local surrounding context[3]. Because of its probabilistic nature and relatively low computational overhead, TreeTagger remains a highly competitive baseline and is frequently integrated into larger pipelines for historical text processing, bridging the gap between purely rule-based systems and massive neural networks[5].

The Classical Language Toolkit (CLTK) represents the contemporary synthesis of these approaches. Designed specifically to address the unique needs of pre-modern languages—which suffer from data sparsity, regional dialect variation, and the absence of native speakers—the CLTK provides a highly modular pipeline architecture[3]. The CLTK backoff lemmatizer for Ancient Greek exemplifies this hybrid methodology. It employs a cascading sequence of algorithms designed to maximize recall: it first attempts a dictionary-based lookup for frequently occurring indeclinable words, then falls back to a unigram-model lemmatizer trained on the Ancient Greek Dependency Treebank, utilizes regular expressions for predictable morphological patterns, and ultimately relies on the legacy Morpheus lexicon as a final safety net[3]. If all previous steps fail, the system conservatively returns the token itself as the lemma[3]. This ensemble approach achieves high accuracy in standardized, canonical texts but requires systematic benchmarking when applied to unedited or dialectally diverse corpora, where its reliance on fixed lexica becomes a liability[5].

### Universal Dependencies and TEI P5 Serialization

The utility of computational morphology relies entirely on the standardization of its output. The Universal Dependencies (UD) framework has emerged as the global standard for cross-linguistic syntactic annotation, providing a unified taxonomy for grammatical description[6]. UD defines a coarse-grained Universal Part-of-Speech (UPOS) tagset comprising 17 foundational categories (e.g., NOUN, VERB, CCONJ, ADJ)[2]. Because historical languages encode vast amounts of semantic and syntactic information at the morphological level, UPOS alone is insufficient. Therefore, UD also utilizes Language-Specific Part-of-Speech (XPOS) tags and a detailed FEATS column to capture nuanced inflectional data, such as case, gender, tense, and mood[2]. For example, the nine-position XPOS code `v3siia---` utilized by the Perseus treebank succinctly and deterministically encodes a verb in the third-person, singular, imperfect, indicative, active[2].

To integrate these complex annotations into digital editions without destroying the underlying text, the Text Encoding Initiative (TEI) P5 Guidelines—specifically Chapter 18, "Feature Structures" and "Simple Analytic Mechanisms"—provide a robust XML serialization schema[7]. The guidelines define linguistic segment categories, primarily the `<w>` (word), `<pc>` (punctuation character), `<m>` (morpheme), and `<c>` (character) elements, which allow for granular tokenization[8].

The TEI attribute class `att.linguistic` equips the `<w>` element with a suite of attributes explicitly designed for lightweight linguistic annotation, effectively bypassing the need for overly complex standoff feature structures for basic NLP output[8]. These include `@lemma` to record the dictionary headword, `@pos` for the grammatical category, and `@msd` for morphosyntactic descriptions[8]. When processing historical corpora, tokenization and normalization become critical concerns. The TEI addresses this via the `att.lexicographic.normalized` class, providing the `@orig` attribute to preserve the manuscript's original diplomatic spelling and the `@norm` attribute to store the regularized form required by NLP parsers to successfully identify the token[8]. The interplay between normalized orthography for computational parsing and diplomatic orthography for textual scholarship forms the core tension in the digital editing of historical texts.

## Comparative Methodological Evaluation

Evaluating the performance of computational toolkits against manual grammatical parsing reveals the inherent trade-offs between computational scalability, linguistic precision, and algorithmic resilience to historical anomalies. The comparative analysis of rule-based systems, statistical taggers, neural transformers, and LLMs demonstrates that while automation drastically accelerates the annotation process, algorithmic fragility persists when confronted with non-standard orthography, dialectal shifts, and heavy morphological ambiguity.

### Handling Uncontracted Forms, Dialectal Shifts, and Ambiguous Inflections

The primary vector of failure for automated lemmatization pipelines in Ancient Greek is the deviation from standardized Attic morphology. The Greek verbal system is notoriously complex, utilizing entirely different aspectual stems (present, aorist, perfect) formed through combinations of reduplication, ablaut (vowel gradation), and thematic suffixation[3]. For instance, recognizing that the aorist participle *donti* derives from the present active indicative lemma *didōmi* requires either exhaustive dictionary mapping of all principal parts or an advanced neural model capable of highly non-linear string transduction[3].

When models trained exclusively on Classical Attic prose are deployed on Homeric epic or Byzantine epigrams, accuracy collapses. In the Homeric corpus, uncontracted forms, poetic vocabulary, and the retention of archaic suffixes routinely baffle statistical models that rely heavily on transition probabilities derived from classical training data[5]. The problem is vastly exacerbated in Medieval and Byzantine Greek due to orthographic inconsistency, particularly itacism—the phonological shift wherein multiple distinct vowels and diphthongs (such as eta, epsilon-iota, and omicron-iota) merged into a single [i] sound[3]. Scribes frequently substituted these characters interchangeably, resulting in surface forms that defy exact lexicon lookups. Furthermore, the frequent omission of the iota subscript in unedited manuscripts strips the text of critical morphological markers required to identify dative cases or subjunctive moods, rendering standard parsers effectively blind[3].

In controlled experiments evaluating unedited Byzantine book epigrams, state-of-the-art systems like the CLTK backoff lemmatizer, RNN Tagger, and the memory-based GLEM lemmatizer suffered a catastrophic accuracy drop of 20 to 25 percentage points compared to their baseline performance on standardized classical prose[3].

| Lemmatization System | Target Corpus | Reported Accuracy | Primary Methodology |
| --- | --- | --- | --- |
| **RNN Tagger** | Classical Greek | 91.29% | Bi-LSTM + Recurrent Neural Network[3] |
| **RNN Tagger** | Byzantine Epigrams | 66.67% | Bi-LSTM + Recurrent Neural Network[3] |
| **GLEM** | Classical Greek | 93.00% | Memory-based learning (FROG) + Lexicon[3] |
| **GLEM** | Byzantine Epigrams | 70.82% | Memory-based learning (FROG) + Lexicon[3] |
| **CLTK Backoff** | Classical Greek | ~91.00% | Cascade: Unigram, Regex, Morpheus Lexicon[3] |
| **CLTK Backoff** | Byzantine Epigrams | 71.69% | Cascade: Unigram, Regex, Morpheus Lexicon[3] |

The analysis demonstrates that a purely neural approach (such as fine-tuned RoBERTa embeddings) or a purely edit-tree approach fails to generalize to this specific type of orthographic noise[3]. The most successful mitigation strategy proved to be a hybrid methodology: combining a heavily augmented dictionary of closed-class words featuring all possible itacistic spelling variants with a neural edit-tree sequence-to-sequence model for open-class vocabulary[3].

### Neural Encoders vs. LLM Few-Shot Parsing

The advent of transformer architectures has bifurcated the field of computational philology into two distinct paradigms: specialized, fine-tuned encoder/decoder models (e.g., XLM-RoBERTa, T5) and generalized Large Language Models (e.g., GPT-4, LLaMA, Mixtral).

Specialized models trained explicitly on historical treebanks exhibit the highest deterministic accuracy. The development of models such as GreBERTa, PhilBERTa, GreTA, and PhilTA demonstrated that formulating lemmatization as an end-to-end character-level sequence-to-sequence task (using the T5 architecture) significantly outperforms pipeline-based systems like UDPipe[6]. By supplying the T5 model with the surrounding sentence context and the individual characters of the target word, the neural network learns to infer morphological indicators dynamically, entirely bypassing the need to predict intermediate POS tags[6]. Similarly, the Cracovia system, an XLM-RoBERTa model fine-tuned on the Latin LASLA corpus and UD treebanks, achieved state-of-the-art results in the EvaLatin 2022 campaign, generating an F​-measure of 0.9627 in strict POS tagging tasks[9].

Conversely, generalized LLMs exhibit powerful semantic reasoning but struggle with deterministic linguistic annotation and strict taxonomic adherence. Evaluations utilizing GPT-3.5 and GPT-4 for Latin POS tagging demonstrate a fundamental paradox: while GPT-4 achieves near-perfect precision (filtering out incorrect matches effectively), its recall significantly lags behind specialized models like the Cracovia system or even the legacy TreeTagger[9].

| Parsing System | Precision (%) | Recall (%) | F​-Measure | Architecture Type |
| --- | --- | --- | --- | --- |
| **Cracovia System** | 96.60 | 96.19 | 0.9627 | Fine-Tuned XLM-RoBERTa[9] |
| **TreeTagger (words)** | 95.29 | 94.28 | 0.9448 | Probabilistic Markov Model[9] |
| **CLTK** | 94.29 | 94.49 | 0.9445 | Stanza / Bi-LSTM Pipeline[9] |
| **LatinCy (trf)** | 97.76 | 92.18 | 0.9324 | Fine-Tuned Transformer[9] |
| **GPT-4 (Zero-Shot)** | 99.52 | 88.75 | 0.9071 | Generalized LLM[9] |
| **GPT-3.5 (Zero-Shot)** | 99.45 | 76.65 | 0.8033 | Generalized LLM[9] |

In a zero-shot setting, LLMs are prone to tagging errors on ambiguous words; for example, frequently misidentifying nouns as adpositions or failing to output data in a strictly parsable format[9]. Furthermore, LLMs frequently suffer from morphological hallucination when confronted with rare dialectal variants, attempting to force historical anomalies into modern linguistic structures due to the overwhelming presence of modern data in their pre-training corpora[10].

However, LLMs demonstrate exceptional utility when deployed in hybrid, few-shot, or retrieval-augmented configurations. Research on the GreekMMLU benchmark and historical Romance language datasets indicates that providing an LLM with a few-shot prompt containing expert-annotated examples of orthographic variability drastically improves performance, bridging the gap between rule-based rigidity and neural flexibility[11]. Furthermore, systems like LingoLLM leverage a morphological analyzer to segment words into morphemes, which are then fed into the LLM alongside grammatical rules, elevating the LLM's capacity to translate and parse critically low-resource texts from an incomprehensible baseline to functional legibility[12]. The consensus within the computational philology literature suggests that the "Alternative Annotator Test" must be strictly applied: LLMs should not replace fine-tuned models for bulk corpus tagging, but they are highly effective as a fallback mechanism to resolve specific intertextual ambiguities where traditional parsers disagree[10].

### The Impact of Joint Learning and Contextual Dependency

The comparative evaluation of tagging methodologies repeatedly underscores the absolute supremacy of sentence-level context over isolated word analysis. The challenge of homophony—where forms like the Latin *profundum* function either as a noun ("the depth") or an adjective ("deep") depending entirely on syntactic government—renders context-free taggers obsolete[9]. TreeTagger, when stripped of context, fails to differentiate these usages, highlighting the limitations of narrow-window probabilistic models[9].

Implementing joint learning strategies, wherein a model is trained simultaneously to predict lemmas and to perform language modeling (predicting the next word in a sequence), forces the neural network to develop robust, context-sensitive embeddings[1]. Empirical analysis by Manjavacas et al. demonstrates that hierarchical sentence encoders trained with a joint bidirectional language modeling loss reduce lemmatization errors significantly, particularly for morphologically rich languages exhibiting high ambiguity[1]. The joint loss acts as an architectural regularizer, ensuring that the model's internal representations encode deep morphosyntactic relationships rather than merely memorizing orthographic surface strings. This mechanism is particularly vital for historical languages where spelling variation artificially inflates the vocabulary size and dilutes the statistical evidence for token-lemma mappings[1].

## Real-World Digital Edition Case Studies

To contextualize the theoretical evaluation of these computational toolkits, an examination of large-scale digital editing projects illustrates how automated morphology pipelines operate in practice. These case studies highlight the ongoing tension between the necessity for manual scholarly disambiguation and the drive for absolute corpus scalability.

### Case Study 1: The Perseus Digital Library and AGLDT

The Perseus Digital Library is the foundational infrastructure for digital classical philology[4]. At its core lies the implementation of Morpheus, which has provided the morphological engine for the repository since the early 1990s. Because Morpheus is a non-probabilistic parser, it generates multiple valid morphological analyses for ambiguous tokens, unable to determine which is correct in a given sentence[3]. To construct the Ancient Greek and Latin Dependency Treebank (AGLDT), the project required a massive, semi-automated workflow[13]. Tokens were processed by Morpheus to generate the candidate list, but the final disambiguation of lemmas, POS tags, and syntactic dependency relations was executed manually by human annotators[13]. This rigorous, manual curation established the AGLDT as the definitive gold standard for historical linguistic data, providing the highly accurate, syntactically parsed training data strictly necessary for every subsequent machine-learning model developed for classical languages, including the CLTK and modern transformer architectures[6].

### Case Study 2: The PROIEL Treebank

The Pragmatic Resources in Old Indo-European Languages (PROIEL) project represents a critical expansion in the scope of annotated historical texts beyond classical antiquity. PROIEL encompasses the Greek New Testament and selections from Herodotus, providing a crucial dataset for understanding Koine and Ionic Greek[3]. The PROIEL treebank is particularly significant because its annotations have been automatically converted to strictly conform to the Universal Dependencies (UD) schema, standardizing the representation of lemmas, UPOS, XPOS, and FEATS[14]. The public availability of the PROIEL corpus directly facilitated the development of advanced neural taggers. For example, the Stanza NLP toolkit—which serves as the default lemmatization engine within the CLTK pipeline—was pre-trained extensively on the PROIEL data[3]. The reliance on PROIEL demonstrates the critical pipeline dependency within the digital humanities: machine learning models are fundamentally constrained by the dialectal and temporal scope of their foundational treebanks.

### Case Study 3: The Diorisis Ancient Greek Corpus

The Diorisis corpus exemplifies the successful application of large-scale, automated linguistic annotation relying on probabilistic models rather than deep neural networks. Developed specifically to facilitate distant reading, the Diorisis project compiled a massive word-form list containing over 900,000 parsed forms generated by the Perseus project's tools[5]. To resolve ambiguities where a single form could map to multiple lemmas with different parts of speech, Diorisis applied the TreeTagger, trained simultaneously on both the Perseus and PROIEL treebanks[5].

In a blinded evaluation comparing Diorisis to the CLTK backoff lemmatizer and the memory-based GLEM system, Diorisis achieved exceptional accuracy: 90% on the highly poetic and dialectally complex first book of the Iliad, and 97% on the classical Attic prose of Lysias[5]. The success of Diorisis validates the hypothesis that, for highly standardized classical texts, the combination of an exhaustively comprehensive lexicon and a computationally lightweight probabilistic POS tagger can match or even exceed the accuracy of more complex machine-learning algorithms that suffer from smaller training dictionaries[5].

## Pedagogical Takeaways & Synthesis for Digital Editors

The integration of computational morphological pipelines into an undergraduate or graduate curriculum for textual editing requires a pedagogical framework that emphasizes critical algorithmic literacy. Students must be explicitly taught not to treat NLP toolkits as infallible "black boxes," but rather as probabilistic engines whose outputs require rigorous scholarly validation, particularly when applied to unedited manuscripts or non-standard dialects.

### Workflow Integration and TEI XML Serialization

For digital editors, the transition from a raw historical text to a linguistically annotated, interoperable digital edition involves a strict multi-stage pipeline. The pedagogical focus must be on executing this pipeline programmatically and serializing the output into TEI XML.

1. **Ingestion and Tokenization:** The text must be ingested and tokenized accurately. Historical texts often feature *scriptio continua*, complex editorial punctuation, or abbreviations that can profoundly disrupt sequence-to-sequence models[5]. Students must learn to utilize specialized tokenizers (such as those provided by CLTK or LatinCy) designed to handle historical enclitics (e.g., the Latin *-que*, or Greek *te*) correctly, separating them from their host words for accurate parsing[15].
2. **Tagging and Lemmatization:** The tokenized stream is passed through an NLP pipeline. For Latin, utilizing the Cracovia system or the `la_core_web_lg` spaCy model provided by LatinCy yields high-accuracy UPOS and XPOS tags[9]. For Ancient Greek, applying the CLTK Stanza pipeline or the GreBERTa transformer provides deep contextual lemmatization[3].
3. **Serialization:** The computational output must be mapped to the TEI P5 Chapter 18 schema. Students should be taught to iterate over the pipeline output arrays and construct XML nodes dynamically.

The serialization process involves wrapping each linguistic token in a `<w>` (word) or `<pc>` (punctuation character) element. The analytical data generated by the tagger is injected into the attributes provided by the `att.linguistic` class[8].

Consider the hypothetical processing of a Latin phrase (*haesit vox faucibus*). The raw text is passed to LatinCy, which outputs the lemma, the Universal Part of Speech, and the morphological features. The digital editor serializes this into TEI XML as follows:

XML

```
<s n="1">
 <w xml:id="w1" lemma="haereo" pos="VERB" msd="Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin">haesit</w>
 <w xml:id="w2" lemma="vox" pos="NOUN" msd="Case=Nom|Gender=Fem|Number=Sing">vox</w>
 <w xml:id="w3" lemma="faux" pos="NOUN" msd="Case=Abl|Gender=Fem|Number=Plur">faucibus</w>
 <pc xml:id="pc1" force="weak">,</pc>
</s>
```

This specific serialization achieves absolute interoperability. The surface text is preserved for traditional diplomatic reading, while the attributes provide a highly structured, queryable database for intertextual analysis, syntax tracking, and automated vocabulary extraction.

### Managing Orthographic Variance

A crucial pedagogical takeaway involves the computational management of spelling variations, such as unstandardized orthography in Early Modern Latin or severe itacism in Byzantine Greek[16]. If diplomatic texts are fed directly into a neural parser, the high out-of-vocabulary rate will cause the tagger to fail or hallucinate. Therefore, editors must employ the `att.lexicographic.normalized` class. The student must learn to construct a preprocessing script that normalizes the text (e.g., expanding abbreviations, standardizing u/v and i/j, or correcting itacistic vowels) before passing the string to the lemmatizer. The TEI serialization then records both the normalized form utilized by the algorithm and the original diplomatic form found in the manuscript:

XML

```
<w lemma="volo" pos="VERB" norm="voluit" orig="uolvit">uolvit</w>
```

This dual-layer encoding ensures that the corpus serves both the computational linguist requiring standardized data streams to train future models, and the paleographer analyzing localized scribal habits and phonological shifts[8].

### The Role of Large Language Models in the Curriculum

Finally, the curriculum must critically address the deployment of Large Language Models. While LLMs (such as GPT-4 or LLaMA) should not serve as the primary automated parser due to massive efficiency constraints, cost, and their propensity for morphological hallucination, they represent an extraordinarily powerful asset for few-shot error correction[10].

Digital editors should be taught to deploy LLMs strategically at the very end of the pipeline. In studies of intertextuality, such as tracking citations of Virgil in Jerome's epistles, scholars utilize the Historical Text-Reuse Grammar (HTRG) filter, which posits that true citations are most reliably identified by matching specific noun-noun or verb-verb combinations rather than high-frequency conjunctions[9]. When an ensemble of traditional parsers (e.g., TreeTagger and CLTK) disagree on the lemma of a highly ambiguous form crucial to an HTRG filter, a script can prompt an LLM via API with the surrounding context, the conflicting parser outputs, and a set of few-shot morphological rules, asking the LLM to act as an intelligent tie-breaker[17]. This hybrid "LLM-in-the-loop" methodology teaches students the immense value of deterministic statistical parsing combined with generative semantic reasoning.

## Comprehensive Academic and Technical Bibliographic Synthesis

The rapid advancement of computational morphology for historical languages reflects a continuous dialectic between the necessity for rule-based precision and the adaptability of statistical machine learning. The foundations of the discipline were established by Gregory Crane in 1991, whose Morpheus system provided the vital, finite-state morphological data required to build the first generation of classical treebanks[3]. Because Morpheus output multiple potential analyses without contextual disambiguation, the field naturally evolved toward probabilistic methods. Helmut Schmid’s 1994 publication on TreeTagger applied Markov models and decision trees to select the most statistically probable tag sequence, an approach that remains highly viable today when paired with exhaustive, manually curated lexica, as demonstrated by Vatri and McGillivray's development of the Diorisis corpus in 2020[3].

As datasets expanded, primarily driven by the Perseus AGLDT and the PROIEL treebanks, the limitations of simple edit-tree lemmatizers and transition probabilities became apparent, particularly regarding unedited manuscripts and dialectal variance[13]. Bary et al. (2017) attempted to bridge this gap with GLEM, combining memory-based learning with lexicon lookups, while the developers of the Classical Language Toolkit (Johnson et al., 2021) engineered cascading pipeline architectures that deploy multiple fallback algorithms to ensure maximum coverage across pre-modern texts[3]. However, research by Swaelens et al. (2024) exposed the fragility of these systems, noting catastrophic accuracy drops when processing unstandardized Byzantine Greek epigrams, thereby confirming that morphological tools require systematic benchmarking against texts exhibiting severe orthographic noise[3].

| Key Literature & Technical Specifications | Primary Contribution & DOI/URL |
| --- | --- |
| **Swaelens, C., et al. (2024).** *Lemmatisation of Medieval Greek: Against the Limits of Transformers' Capabilities?* | Benchmarked CLTK and GLEM against unedited Byzantine Greek, establishing the necessity for hybrid neural/dictionary models. [URL: uploaded:01_A_pilot_study_for_BERT_language_modelling_and_morphological_analysis_for_ancient.pdf][3] |
| **Riemenschneider, F., & Frank, A. (2023).** *Exploring Large Language Models for Classical Philology.* | Introduced GreBERTa, PhilBERTa, GreTA, and PhilTA; proved T5 encoder-decoder models outperform legacy pipelines on PROIEL/Perseus data. [URL: uploaded:03_Linguistic_annotation_of_Byzantine_book_epigrams_C._Swaelens_et_al..pdf][6] |
| **Vatri, A., & McGillivray, B. (2020).** *Lemmatization for Ancient Greek: An experimental assessment of the state of the art.* | Demonstrated that Diorisis (TreeTagger + large lexicon) outperformed neural baselines on Homer and Lysias. [URL: uploaded:05_Digital_tools_applied_on_Ancient_Greek_texts.pdf][5] |
| **Wittweiler, M., et al. (2024).** *On the implementation of Latin part-of-speech taggers in intertextuality analysis...* | Evaluated Cracovia (XLM-RoBERTa), LatinCy, and GPT-4 for intertextual citation detection using HTRG filters. [URL: uploaded:08_On_the_implementation_of_Latin_part-of-speech_taggers_in_intertextuality_analysi.pdf][9] |
| **Manjavacas, E., et al. (2019).** *Improving Lemmatization of Non-Standard Languages with Joint Learning.* | Proved that a joint bidirectional LM loss drastically improves contextual embeddings for historically ambiguous tokens. [URL: uploaded:10_Improving_lemmatization_of_non-standard_languages_with_joint_learning.pdf][1] |
| **TEI Consortium. (2026).** *TEI P5: Guidelines for Electronic Text Encoding and Interchange (Chapter 18).* | Formalized the `att.linguistic` and `att.lexicographic.normalized` classes for embedding NLP output into digital editions. [URL: https://www.tei-c.org/release/doc/tei-p5-doc/en/html/AI.html][8] |

To overcome the limitations of feature-engineered pipelines, researchers have successfully applied deep neural networks. Manjavacas et al. (2019) demonstrated that recurrent encoder-decoder models, particularly when trained with a joint language modeling loss, generate superior contextual embeddings that significantly improve accuracy on ambiguous and highly synthetic historical datasets[1]. This trajectory culminated in the deployment of transformer architectures. Riemenschneider and Frank (2023) developed GreBERTa and PhilBERTa (encoder-only) alongside GreTA and PhilTA (encoder-decoder T5 models), establishing that sequence-to-sequence string transduction handles the extreme non-linearities of ancient morphology far better than legacy systems[6]. Concurrently, Wróbel and Nowak’s Cracovia system applied XLM-RoBERTa to set new accuracy benchmarks for Latin tagging[9].

Presently, the frontier of computational philology lies in evaluating the efficacy of Large Language Models. Analyses by Wittweiler et al. (2024) confirm that while LLMs like GPT-4 demonstrate profound zero-shot and few-shot reasoning capabilities, they currently lag behind specialized, fine-tuned transformer models in strict recall and parsing consistency[9]. Consequently, the consensus within the current literature dictates the implementation of hybrid architectures. State-of-the-art pipelines utilize highly fine-tuned neural encoders (e.g., LatinCy or GreBERTa) to execute the bulk morphological tagging and lemmatization, subsequently serializing the data into the TEI P5 XML schema utilizing `att.linguistic` parameters[8]. Generative LLMs are then reserved for targeted, few-shot prompting to resolve deep semantic ambiguities where deterministic parsers fail[18]. This synthesis of strict algorithmic tokenization, neural syntactic parsing, and generative semantic resolution provides digital scholars with the robust, scalable methodologies required to annotate the vast expanse of the pre-modern textual record.

Sources used in the report

09_Comparative_Evaluation_of_Latin_Natural_Language_Processing_Tools_for_Pedagogica.pdf

10_Improving_lemmatization_of_non-standard_languages_with_joint_learning.pdf

[exploratoryphilology.org

Updating LatinCy XPOS Tags - Exploratory Philology Blog

 Opens in a new window](https://exploratoryphilology.org/posts/latincy-xpos-tags/)

02_Lemmatisation_of_Medieval_Greek_Against_the_Limits_of_Transformer's_Capabilities.pdf

03_Linguistic_annotation_of_Byzantine_book_epigrams_C._Swaelens_et_al..pdf

[jlm.ipipan.waw.pl

A practitioner's view: a survey and comparison of lemmatization and morphological tagging in German and Latin - Journal of Language Modelling

 Opens in a new window](https://jlm.ipipan.waw.pl/index.php/JLM/article/download/205/218/1757)[researchgate.net

The Sixth Generation of the Perseus Digital Library and a Workflow for Open Philology -- DRAFT - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/385921029_The_Sixth_Generation_of_the_Perseus_Digital_Library_and_a_Workflow_for_Open_Philology_--_DRAFT)[academia.edu

A computational approach to Latin verbs: new resources and methods - Academia.edu

 Opens in a new window](https://www.academia.edu/3560804/A_computational_approach_to_Latin_verbs_new_resources_and_methods)[loterre.istex.fr

TreeTagger - ThesoTM - Loterre

 Opens in a new window](https://loterre.istex.fr/LTK/en/page/-RFLN8D9Z-N)

05_Digital_tools_applied_on_Ancient_Greek_texts.pdf

08_On_the_implementation_of_Latin_part-of-speech_taggers_in_intertextuality_analysi.pdf

[aclanthology.org

The Classical Language Toolkit: An NLP Framework for Pre-Modern Languages - ACL Anthology

 Opens in a new window](https://aclanthology.org/2021.acl-demo.3.pdf)[researchgate.net

The Classical Language Toolkit: An NLP Framework for Pre-Modern Languages

 Opens in a new window](https://www.researchgate.net/publication/353492044_The_Classical_Language_Toolkit_An_NLP_Framework_for_Pre-Modern_Languages)[spraakbanken.gu.se

FCS Aggregator – Content Search - Språkbanken Text

 Opens in a new window](https://spraakbanken.gu.se/ws/fcs/2.0/aggregator/)[tei-c.org

18 Feature Structures - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/Vault/P5/3.4.0/doc/tei-p5-doc/en/html/FS.html)[tei-c.org

18 Simple Analytic Mechanisms - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/AI.html)[github.com

att.linguistic for and · Issue #1670 · TEIC/TEI - GitHub

 Opens in a new window](https://github.com/TEIC/TEI/issues/1670)[tei-c.org

TEI element w (word) - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/Vault/P5/4.12.0/doc/tei-p5-doc/it/html/ref-w.html)

01_A_pilot_study_for_BERT_language_modelling_and_morphological_analysis_for_ancient.pdf

[arxiv.org

Opportunities and Challenges of Large Language Models for Low-Resource Languages in Humanities Research - arXiv

 Opens in a new window](https://arxiv.org/html/2412.04497v4)[aclanthology.org

GreekMMLU: A Native-Sourced Multitask Benchmark for Evaluating Language Models in Greek - ACL Anthology

 Opens in a new window](https://aclanthology.org/2026.findings-acl.448.pdf)[arxiv.org

From Traditional Taggers to LLMs: A Comparative Study of POS Tagging for Medieval Romance Languages - arXiv

 Opens in a new window](https://arxiv.org/pdf/2605.09147)[cs.cmu.edu

Learning Endangered Languages in LLMs with In-Context Linguistic Descriptions - CMU School of Computer Science

 Opens in a new window](http://www.cs.cmu.edu/~leili/pubs/zhang2024hire.pdf)[aclanthology.org

From Lemmatization to Legal Terminology: Assessing an Hybrid Pipeline on Justinian's Digest - ACL Anthology

 Opens in a new window](https://aclanthology.org/anthology-files/anthology-files/pdf/lt4hala/2026.lt4hala-1.43.pdf)[universaldependencies.org

UD Ancient Greek Perseus - Universal Dependencies

 Opens in a new window](https://universaldependencies.org/treebanks/grc_perseus/index.html)[universaldependencies.org

UD Ancient Greek PROIEL - Universal Dependencies

 Opens in a new window](https://universaldependencies.org/treebanks/grc_proiel/index.html)[gist.github.com

shawngraham's gists · GitHub

 Opens in a new window](https://gist.github.com/shawngraham)[tei-c.org

TEI element pc (punctuation character) - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-pc.html)[scribd.com

POS Tagging 16th-Century Latin with GPT | PDF | Linguistics - Scribd

 Opens in a new window](https://www.scribd.com/document/888186127/2024-latechclfl-1-18)
Sources read but not used in the report
[tei-c.org

3 Elements Available in All TEI Documents - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html)[tei-c.org

17 Simple Analytic Mechanisms - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/Vault/P5/3.1.0/doc/tei-p5-doc/en/html/AI.html)[dingo.sbs.arizona.edu

A Rationale for the TEI Recommendations for Feature-Structure Markup - The University of Arizona

 Opens in a new window](https://dingo.sbs.arizona.edu/~langendoen/TEI-FSmarkup.htm)[tei-c.org

TEI element lem (lemma) - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-lem.html)[arxiv.org

NLP for the Greek language: a longer survey - arXiv

 Opens in a new window](https://arxiv.org/html/2408.10962v1)[aclanthology.org

Proceedings of the 10th SIGHUM Workshop on Language Technology for Cultural Heritage, Social Sciences, and Humanities (LaTeCH) - ACL Anthology

 Opens in a new window](https://aclanthology.org/W16-21.pdf)[github.com

alekkeersmaekers/glaux-nlp - GitHub

 Opens in a new window](https://github.com/alekkeersmaekers/glaux-nlp)[researchgate.net

Joint Learning of POS and Dependencies for Multilingual Universal Dependency Parsing

 Opens in a new window](https://www.researchgate.net/publication/334115866_Joint_Learning_of_POS_and_Dependencies_for_Multilingual_Universal_Dependency_Parsing)[lirias.kuleuven.be

Adapting transformer models to morphological tagging of two highly

 Opens in a new window](https://lirias.kuleuven.be/retrieve/418a9c85-a3d7-4c63-a52f-70d945cf8006)[nlp.stanford.edu

Stanford's Graph-based Neural Dependency Parser at the CoNLL 2017 Shared Task

 Opens in a new window](https://nlp.stanford.edu/pubs/dozat2017stanford.pdf)[aclanthology.org

CoNLL 2017 Shared Task: Multilingual Parsing from Raw Text to Universal Dependencies - ACL Anthology

 Opens in a new window](https://aclanthology.org/K17-3001.pdf)[tei-c.org

An Introduction to TEI simplePrint - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/release/doc/tei-p5-exemplars/html/tei_simplePrint.doc.html)[tei-c.org

18 Simple Analytic Mechanisms - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/Vault/P5/4.10.0/doc/tei-p5-doc/de/html/AI.html)[arxiv.org

Learning Endangered Languages in LLMs with In-Context Linguistic Descriptions - arXiv

 Opens in a new window](https://arxiv.org/html/2402.18025v2)[aclanthology.org

Language Technologies for Historical and Ancient Languages (2026) - ACL Anthology

 Opens in a new window](https://aclanthology.org/events/lt4hala-2026/)[huskiecommons.lib.niu.edu

Limitations of Scientific Articles and Navigated Future Directions with LLM and RAG - Huskie Commons

 Opens in a new window](https://huskiecommons.lib.niu.edu/cgi/viewcontent.cgi?article=9047&context=allgraduate-thesesdissertations)[mdpi.com

A Novel Llama 3-Based Prompt Engineering Platform for Textual Data Generation and Labeling - MDPI

 Opens in a new window](https://www.mdpi.com/2079-9292/14/14/2800)[arxiv.org

GreekMMLU: A Native-Sourced Multitask Benchmark for Evaluating Language Models in Greek - arXiv

 Opens in a new window](https://arxiv.org/html/2602.05150v2)[lrec-conf.org

RespondeoQA: A Benchmark for Bilingual Latin-English Question Answering - LREC

 Opens in a new window](http://www.lrec-conf.org/proceedings/lrec2026/pdf/2026.lrec2026-1.80.pdf)[loterre.istex.fr

: ThesoTM: TreeTagger - Loterre - Istex

 Opens in a new window](https://loterre.istex.fr/LTK/fr/page/-RFLN8D9Z-N?clang=en&anylang=on)[aclanthology.org

Sense-Based Annotation of Geographical Nouns in Ancient Greek and Latin: A Diachronic Study with LLMs - ACL Anthology

 Opens in a new window](https://aclanthology.org/2026.latechclfl-1.26.pdf)[tei-c.org

TEI class att.lexicographic.normalized - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/Vault/P5/4.12.0/doc/tei-p5-doc/zh-TW/html/ref-att.lexicographic.normalized.html)[tei-c.org

Appendix D Attributes - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/release/doc/tei-p5-doc/en/html/REF-ATTS.html)[giada-collab.github.io

Édition numérique des "Considérations" de Germaine de Staël - GitHub Pages

 Opens in a new window](https://giada-collab.github.io/considerations/documentation_stael/manuscrit_vol_1_docum.html)[lex-0.org

13. FAQs - TEI Lex-0 — A baseline encoding for lexicographic data

 Opens in a new window](https://lex-0.org/faq.html)[clarin-eric.github.io

The structure and encoding of PressMint corpora - GitHub Pages

 Opens in a new window](https://clarin-eric.github.io/PressMint/)[tei-c.org

TEI element w (word) - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-w.html)[lex-0.org

TEI Lex-0 — A baseline encoding for lexicographic data — Clarity for lexicographers. Stability for data. Compatibility for the future.

 Opens in a new window](https://lex-0.org/)[clarin-eric.github.io

The structure and encoding of ParlaMint corpora - GitHub Pages

 Opens in a new window](https://clarin-eric.github.io/ParlaMint/)[lex-0.org

4. Senses - TEI Lex-0 — A baseline encoding for lexicographic data

 Opens in a new window](https://lex-0.org/senses.html)[huggingface.co

Daily Papers - Hugging Face

 Opens in a new window](https://huggingface.co/papers?q=ROOTS%20corpus)[ancientnlp.com

Proceedings of the Ancient Language Processing Workshop (ALP 2023) associated with RANLP'2023

 Opens in a new window](https://www.ancientnlp.com/alp2023/accepted_papers/ALP2023pro.pdf)[mdpi.com

Harnessing Language Models for Studying the Ancient Greek Language: A Systematic Review - MDPI

 Opens in a new window](https://www.mdpi.com/2504-4990/7/3/71)[eprints.sztaki.hu

Morphology in the Age of Pre-trained Language Models - SZTAKI Publication Repository

 Opens in a new window](https://eprints.sztaki.hu/10909/4/thesis.pdf)[cs.uoregon.edu

ENHANCING MULTILINGUAL INFORMATION EXTRACTION TOWARDS GLOBAL LINGUISTIC INCLUSIVITY by MINH NGUYEN A DISSERTATION Presented to t - Computer Science - University of Oregon

 Opens in a new window](https://www.cs.uoregon.edu/Reports/PHD-202404-Nguyen.pdf)[aclanthology.org

Fifteenth Language Resources and Evaluation Conference - ACL Anthology

 Opens in a new window](https://aclanthology.org/events/lrec-2026/)
Thoughts

Establishing Research Context

Synthesizing the foundational trade-offs between legacy rule-based tools, neural taggers, and modern large language models when applied to historical languages. I am examining how automated pipelines handle orthographic variability, dialectal shifts, and complex morphological ambiguity in pre-modern texts compared to manual grammatical analysis.

Identifying Methodological Gaps

Evaluating key performance disparities across computational approaches, specifically contrasting traditional finite-state transducers and decision-tree taggers with recent Transformer-based architectures. I am looking to resolve performance bottlenecks in lemmatizing non-standard medieval orthographies and dialectal variants.

Next Action Plan

Gathering technical specifications on historic morphological architectures, TEI P5 linguistic annotation standards, digital treebank implementations, and recent empirical benchmarks for few-shot large language model parsing.

[tei-c.org

18 Feature Structures - The TEI Guidelines - Text Encoding Initiative](https://www.tei-c.org/Vault/P5/3.4.0/doc/tei-p5-doc/en/html/FS.html)[tei-c.org

3 Elements Available in All TEI Documents - The TEI Guidelines - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html)[tei-c.org

17 Simple Analytic Mechanisms - The TEI Guidelines - Text Encoding Initiative](https://tei-c.org/Vault/P5/3.1.0/doc/tei-p5-doc/en/html/AI.html)[tei-c.org

18 Simple Analytic Mechanisms - The TEI Guidelines - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/AI.html)[tei-c.org

18 Simple Analytic Mechanisms - The TEI Guidelines - Text Encoding Initiative](https://www.tei-c.org/Vault/P5/4.10.0/doc/tei-p5-doc/de/html/AI.html)[dingo.sbs.arizona.edu

A Rationale for the TEI Recommendations for Feature-Structure Markup - The University of Arizona](https://dingo.sbs.arizona.edu/~langendoen/TEI-FSmarkup.htm)[tei-c.org

TEI element lem (lemma) - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-lem.html)

TEI XML Annotation Standards

Analyzing the standard specifications for encoding linguistic features in XML structures reveals two main approaches: lightweight inline attributes (`lemma`, `pos`, `msd`) directly attached to token elements (`w`, `pc`), and complex feature structures using dedicated tags (`fs`, `f`) for highly granular or ambiguous morphosyntactic analyses.

Limitations of Lightweight Markup

Evaluating lightweight token annotations highlights key trade-offs, such as restricting a document to a single tokenization schema and tagset. Complex linguistic phenomena like disjoint compounds or overlapping syntactic boundaries require advanced mechanisms like feature structures or standoff markup to represent ambiguous or multi-layered analyses.

Deepening Empirical and Computational Research

Investigating historical language processing tools, including rule-based analyzers like Morpheus, Universal Dependencies tagsets for Greek and Latin, and modern benchmark performance of Large Language Models on morphological tagging tasks.

[academia.edu

A computational approach to Latin verbs: new resources and methods - Academia.edu](https://www.academia.edu/3560804/A_computational_approach_to_Latin_verbs_new_resources_and_methods)[jlm.ipipan.waw.pl

A practitioner's view: a survey and comparison of lemmatization and morphological tagging in German and Latin - Journal of Language Modelling](https://jlm.ipipan.waw.pl/index.php/JLM/article/download/205/218/1757)[arxiv.org

NLP for the Greek language: a longer survey - arXiv](https://arxiv.org/html/2408.10962v1)[aclanthology.org

Proceedings of the 10th SIGHUM Workshop on Language Technology for Cultural Heritage, Social Sciences, and Humanities (LaTeCH) - ACL Anthology](https://aclanthology.org/W16-21.pdf)[universaldependencies.org

UD Ancient Greek PROIEL - Universal Dependencies](https://universaldependencies.org/treebanks/grc_proiel/index.html)[universaldependencies.org

UD Ancient Greek Perseus - Universal Dependencies](https://universaldependencies.org/treebanks/grc_perseus/index.html)[github.com

alekkeersmaekers/glaux-nlp - GitHub](https://github.com/alekkeersmaekers/glaux-nlp)[researchgate.net

Joint Learning of POS and Dependencies for Multilingual Universal Dependency Parsing](https://www.researchgate.net/publication/334115866_Joint_Learning_of_POS_and_Dependencies_for_Multilingual_Universal_Dependency_Parsing)[exploratoryphilology.org

Updating LatinCy XPOS Tags - Exploratory Philology Blog](https://exploratoryphilology.org/posts/latincy-xpos-tags/)[lirias.kuleuven.be

Adapting transformer models to morphological tagging of two highly](https://lirias.kuleuven.be/retrieve/418a9c85-a3d7-4c63-a52f-70d945cf8006)[nlp.stanford.edu

Stanford's Graph-based Neural Dependency Parser at the CoNLL 2017 Shared Task](https://nlp.stanford.edu/pubs/dozat2017stanford.pdf)[aclanthology.org

CoNLL 2017 Shared Task: Multilingual Parsing from Raw Text to Universal Dependencies - ACL Anthology](https://aclanthology.org/K17-3001.pdf)[spraakbanken.gu.se

FCS Aggregator – Content Search - Språkbanken Text](https://spraakbanken.gu.se/ws/fcs/2.0/aggregator/)

Mapping Structural and Technical Requirements

Analyzing the full technical framework needed for the final synthesis of ancient language NLP tools. I am mapping out the precise specifications for finite-state transducer architectures, Universal Dependencies tagging schemes, and TEI XML linguistic markup elements to ensure comprehensive technical coverage.

Addressing Dialectal and Orthographic Challenges

Focusing on resolving complex edge cases in Ancient Greek and Latin morphology, including uncontracted Homeric forms, itacistic spellings in Medieval Greek, and non-standard orthography in Vulgar and Medieval Latin. I am organizing comparative benchmarks across legacy parsers, specialized neural models, and broad-coverage language models.

Next Action Plan

Executing targeted searches to extract precise benchmark accuracy metrics across treebanks, retrieve exact API invocation patterns for historical NLP libraries, and compile standard TEI XML schemas for linguistic annotation.

[aclanthology.org

The Classical Language Toolkit: An NLP Framework for Pre-Modern Languages - ACL Anthology](https://aclanthology.org/2021.acl-demo.3.pdf)[github.com

att.linguistic for and · Issue #1670 · TEIC/TEI - GitHub](https://github.com/TEIC/TEI/issues/1670)[tei-c.org

An Introduction to TEI simplePrint - Text Encoding Initiative](https://tei-c.org/release/doc/tei-p5-exemplars/html/tei_simplePrint.doc.html)[clarin-eric.github.io

The structure and encoding of PressMint corpora - GitHub Pages](https://clarin-eric.github.io/PressMint/)[tei-c.org

TEI element pc (punctuation character) - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-pc.html)[giada-collab.github.io

Édition numérique des "Considérations" de Germaine de Staël - GitHub Pages](https://giada-collab.github.io/considerations/documentation_stael/manuscrit_vol_1_docum.html)[tei-c.org

TEI element w (word) - Text Encoding Initiative](https://www.tei-c.org/Vault/P5/4.12.0/doc/tei-p5-doc/it/html/ref-w.html)[tei-c.org

18 Simple Analytic Mechanisms - The TEI Guidelines - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/AI.html)[tei-c.org

18 Simple Analytic Mechanisms - The TEI Guidelines - Text Encoding Initiative](https://www.tei-c.org/Vault/P5/4.10.0/doc/tei-p5-doc/de/html/AI.html)[tei-c.org

Appendix D Attributes - The TEI Guidelines - Text Encoding Initiative](https://tei-c.org/release/doc/tei-p5-doc/en/html/REF-ATTS.html)[researchgate.net

The Sixth Generation of the Perseus Digital Library and a Workflow for Open Philology -- DRAFT - ResearchGate](https://www.researchgate.net/publication/385921029_The_Sixth_Generation_of_the_Perseus_Digital_Library_and_a_Workflow_for_Open_Philology_--_DRAFT)

Architectural Patterns in Classical NLP Toolkits

Examining the modular design of classical language processing libraries reveals a reliance on standardized pipelines that sequence language-specific tokenization, part-of-speech tagging, and lemmatization tasks. Observing these implementations highlights how modern frameworks balance pre-configured defaults for historical languages while accommodating custom algorithmic extensions.

Standards for Textual and Morphological Markup

Resolving questions around standardized digital encoding reveals how specialized attribute classes allow word and punctuation tokens to carry base forms, morphosyntactic descriptions, and part-of-speech labels directly within textual markup schemes. This provides a unified format for distributing linguistically annotated historical corpora alongside canonical passage identifiers.

Targeting Exact Academic Citations and Benchmarks

Conducting targeted searches for precise bibliographic identifiers, canonical text repository conventions, legacy C-based morphological parsing architectures, and empirical accuracy evaluations contrasting traditional taggers with zero-shot and few-shot modern language model capabilities.

[arxiv.org

Opportunities and Challenges of Large Language Models for Low-Resource Languages in Humanities Research - arXiv](https://arxiv.org/html/2412.04497v4)[arxiv.org

Learning Endangered Languages in LLMs with In-Context Linguistic Descriptions - arXiv](https://arxiv.org/html/2402.18025v2)[aclanthology.org

Language Technologies for Historical and Ancient Languages (2026) - ACL Anthology](https://aclanthology.org/events/lt4hala-2026/)[huskiecommons.lib.niu.edu

Limitations of Scientific Articles and Navigated Future Directions with LLM and RAG - Huskie Commons](https://huskiecommons.lib.niu.edu/cgi/viewcontent.cgi?article=9047&context=allgraduate-thesesdissertations)[cs.cmu.edu

Learning Endangered Languages in LLMs with In-Context Linguistic Descriptions - CMU School of Computer Science](http://www.cs.cmu.edu/~leili/pubs/zhang2024hire.pdf)[aclanthology.org

GreekMMLU: A Native-Sourced Multitask Benchmark for Evaluating Language Models in Greek - ACL Anthology](https://aclanthology.org/2026.findings-acl.448.pdf)[mdpi.com

A Novel Llama 3-Based Prompt Engineering Platform for Textual Data Generation and Labeling - MDPI](https://www.mdpi.com/2079-9292/14/14/2800)[mdpi.com

Harnessing Language Models for Studying the Ancient Greek Language: A Systematic Review - MDPI](https://www.mdpi.com/2504-4990/7/3/71)[arxiv.org

GreekMMLU: A Native-Sourced Multitask Benchmark for Evaluating Language Models in Greek - arXiv](https://arxiv.org/html/2602.05150v2)[lrec-conf.org

RespondeoQA: A Benchmark for Bilingual Latin-English Question Answering - LREC](http://www.lrec-conf.org/proceedings/lrec2026/pdf/2026.lrec2026-1.80.pdf)[loterre.istex.fr

TreeTagger - ThesoTM - Loterre](https://loterre.istex.fr/LTK/en/page/-RFLN8D9Z-N)[loterre.istex.fr

: ThesoTM: TreeTagger - Loterre - Istex](https://loterre.istex.fr/LTK/fr/page/-RFLN8D9Z-N?clang=en&anylang=on)

Categorizing Fine-Grained Morphological Errors

Analyzing systematic failure modes in ancient language processing reveals distinct error categories across historical corpora. In Byzantine Greek, performance drops significantly due to dialectal form mismatches, irregular verbal aspect stems, nominal stem assimilation, and missing iota subscripts. For Classical Greek, primary bottlenecks stem from homophony, connected speech phenomena like elision and crasis, parsing failures on rare forms, and improper handling of clitic accentuation.

Resolving TEI XML Structural Representations

Synthesizing the structural differences between inline attribute encoding and complex feature structures in TEI P5 Chapter 18. Inline attributes (`lemma`, `pos`, `msd`) offer compact token annotations, whereas complex feature structures utilizing dedicated feature tags provide the expressive power necessary to represent overlapping syntactic boundaries, discontinuous compounds, and multi-layered morphosyntactic ambiguity.

Gathering Target Technical Specifications

Executing focused searches to collect empirical accuracy metrics across historical treebank benchmarks for neural and legacy taggers, alongside concrete Python integration patterns for classical NLP pipelines and formal XML serialization schemas.

[gist.github.com

shawngraham's gists · GitHub](https://gist.github.com/shawngraham)[researchgate.net

The Classical Language Toolkit: An NLP Framework for Pre-Modern Languages](https://www.researchgate.net/publication/353492044_The_Classical_Language_Toolkit_An_NLP_Framework_for_Pre-Modern_Languages)[aclanthology.org

Sense-Based Annotation of Geographical Nouns in Ancient Greek and Latin: A Diachronic Study with LLMs - ACL Anthology](https://aclanthology.org/2026.latechclfl-1.26.pdf)[tei-c.org

18 Simple Analytic Mechanisms - The TEI Guidelines - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/AI.html)[tei-c.org

TEI class att.lexicographic.normalized - Text Encoding Initiative](https://www.tei-c.org/Vault/P5/4.12.0/doc/tei-p5-doc/zh-TW/html/ref-att.lexicographic.normalized.html)[tei-c.org

Appendix D Attributes - The TEI Guidelines - Text Encoding Initiative](https://tei-c.org/release/doc/tei-p5-doc/en/html/REF-ATTS.html)[giada-collab.github.io

Édition numérique des "Considérations" de Germaine de Staël - GitHub Pages](https://giada-collab.github.io/considerations/documentation_stael/manuscrit_vol_1_docum.html)[lex-0.org

13. FAQs - TEI Lex-0 — A baseline encoding for lexicographic data](https://lex-0.org/faq.html)[clarin-eric.github.io

The structure and encoding of PressMint corpora - GitHub Pages](https://clarin-eric.github.io/PressMint/)[tei-c.org

TEI element w (word) - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-w.html)[lex-0.org

TEI Lex-0 — A baseline encoding for lexicographic data — Clarity for lexicographers. Stability for data. Compatibility for the future.](https://lex-0.org/)[clarin-eric.github.io

The structure and encoding of ParlaMint corpora - GitHub Pages](https://clarin-eric.github.io/ParlaMint/)[lex-0.org

4. Senses - TEI Lex-0 — A baseline encoding for lexicographic data](https://lex-0.org/senses.html)

Integrating TEI Standards for Historical Tokens

Synthesizing the exact schema requirements for representing multi-layered morphosyntactic data within Text Encoding Initiative structures. Observing how specific attribute classes handle normalized forms alongside original orthographic representations clarifies how historical text editions maintain diplomatic fidelity while supporting downstream computational analysis.

Rule-Based Core Mechanics vs Modern Pipelines

Dissecting the inner workings of legacy C-based finite-state transducers reveals how underlying lexicons and morphological rules decouple lexical lookup from surface-level accentuation and inflection. Resolving how these classic engines integrate with modular spaCy pipelines and neural frameworks provides a clear blueprint for hybrid NLP workflows.

Finalizing Empirical Benchmarks and Prompts

Executing targeted queries to retrieve exact XML code examples for Ancient Greek annotation, extract precise architectural details of rule-based engines, and construct standardized few-shot prompt formats for dependency treebank parsing with large language models.

[huggingface.co

Daily Papers - Hugging Face](https://huggingface.co/papers?q=ROOTS%20corpus)[aclanthology.org

From Lemmatization to Legal Terminology: Assessing an Hybrid Pipeline on Justinian's Digest - ACL Anthology](https://aclanthology.org/anthology-files/anthology-files/pdf/lt4hala/2026.lt4hala-1.43.pdf)[arxiv.org

From Traditional Taggers to LLMs: A Comparative Study of POS Tagging for Medieval Romance Languages - arXiv](https://arxiv.org/pdf/2605.09147)[ancientnlp.com

Proceedings of the Ancient Language Processing Workshop (ALP 2023) associated with RANLP'2023](https://www.ancientnlp.com/alp2023/accepted_papers/ALP2023pro.pdf)[mdpi.com

Harnessing Language Models for Studying the Ancient Greek Language: A Systematic Review - MDPI](https://www.mdpi.com/2504-4990/7/3/71)[eprints.sztaki.hu

Morphology in the Age of Pre-trained Language Models - SZTAKI Publication Repository](https://eprints.sztaki.hu/10909/4/thesis.pdf)[cs.uoregon.edu

ENHANCING MULTILINGUAL INFORMATION EXTRACTION TOWARDS GLOBAL LINGUISTIC INCLUSIVITY by MINH NGUYEN A DISSERTATION Presented to t - Computer Science - University of Oregon](https://www.cs.uoregon.edu/Reports/PHD-202404-Nguyen.pdf)[scribd.com

POS Tagging 16th-Century Latin with GPT | PDF | Linguistics - Scribd](https://www.scribd.com/document/888186127/2024-latechclfl-1-18)[aclanthology.org

Fifteenth Language Resources and Evaluation Conference - ACL Anthology](https://aclanthology.org/events/lrec-2026/)

Benchmarking Prompting vs. Fine-Tuning in Historical NLP

Synthesizing recent empirical evaluations of large language models on historical texts reveals a distinct performance boundary. While zero-shot and few-shot prompting demonstrate competitive reasoning on ambiguous morphological forms, dedicated fine-tuned models and hybrid architectures consistently achieve higher overall precision when resolving complex inflected paradigms in historical corpora.

Resolving Technical and Structural Coverage

Verifying that all structural components—including finite-state transducer rules, Universal Dependencies feature schemes, TEI P5 linguistic attributes, and case studies of major digital libraries—have been fully mapped against established computational linguistics standards.

Transitioning to Synthesis and Report Construction

Finalizing the data gathering process and proceeding to synthesize the findings into a comprehensive technical overview, featuring comparative performance benchmarks, structural XML serialization patterns, and practical implementation guidelines.

The initial research has returned a lot of information. I'm sorting through it and organizing it. This will make sure the whole thing flows well and hits all the key points you asked for.

This is it! I’m bringing it all together. Jotting down my final thoughts, polishing everything up, and making sure I give you my very best work.

## References (APA)

1. exploratoryphilology.org. (n.d.). *Updating LatinCy XPOS Tags - Exploratory Philology Blog*. https://exploratoryphilology.org/posts/latincy-xpos-tags/
2. researchgate.net. (n.d.). *The Sixth Generation of the Perseus Digital Library and a Workflow for Open Philology -- DRAFT*. https://www.researchgate.net/publication/385921029_The_Sixth_Generation_of_the_Perseus_Digital_Library_and_a_Workflow_for_Open_Philology_--_DRAFT
3. academia.edu. (n.d.). *A computational approach to Latin verbs: new resources and methods - Academia.edu*. https://www.academia.edu/3560804/A_computational_approach_to_Latin_verbs_new_resources_and_methods
4. researchgate.net. (n.d.). *The Classical Language Toolkit: An NLP Framework for Pre-Modern Languages*. https://www.researchgate.net/publication/353492044_The_Classical_Language_Toolkit_An_NLP_Framework_for_Pre-Modern_Languages
5. tei-c.org. (n.d.). *18 Simple Analytic Mechanisms - The TEI Guidelines - Text Encoding Initiative*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/AI.html
6. loterre.istex.fr. (n.d.). *TreeTagger - ThesoTM - Loterre*. https://loterre.istex.fr/LTK/en/page/-RFLN8D9Z-N
7. arxiv.org. (n.d.). *From Traditional Taggers to LLMs: A Comparative Study of POS Tagging for Medieval Romance Languages*. https://arxiv.org/pdf/2605.09147
8. cs.cmu.edu. (n.d.). *Learning Endangered Languages in LLMs with In-Context Linguistic Descriptions - CMU School of Computer Science*. http://www.cs.cmu.edu/~leili/pubs/zhang2024hire.pdf
9. github.com. (n.d.). *att.linguistic for and · Issue #1670 · TEIC/TEI*. https://github.com/TEIC/TEI/issues/1670
10. gist.github.com. (n.d.). *shawngraham's gists · GitHub*. https://gist.github.com/shawngraham
11. tei-c.org. (n.d.). *TEI element pc (punctuation character) - Text Encoding Initiative*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-pc.html
12. tei-c.org. (n.d.). *3 Elements Available in All TEI Documents - The TEI Guidelines - Text Encoding Initiative*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html
13. dingo.sbs.arizona.edu. (n.d.). *A Rationale for the TEI Recommendations for Feature-Structure Markup - The University of Arizona*. https://dingo.sbs.arizona.edu/~langendoen/TEI-FSmarkup.htm
14. tei-c.org. (n.d.). *TEI element lem (lemma) - Text Encoding Initiative*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-lem.html
15. tei-c.org. (n.d.). *TEI element w (word) - Text Encoding Initiative*. https://www.tei-c.org/Vault/P5/4.12.0/doc/tei-p5-doc/it/html/ref-w.html
16. universaldependencies.org. (n.d.). *UD Ancient Greek PROIEL - Universal Dependencies*. https://universaldependencies.org/treebanks/grc_proiel/index.html
17. tei-c.org. (n.d.). *17 Simple Analytic Mechanisms - The TEI Guidelines - Text Encoding Initiative*. https://tei-c.org/Vault/P5/3.1.0/doc/tei-p5-doc/en/html/AI.html
18. scribd.com. (n.d.). *POS Tagging 16th-Century Latin with GPT | PDF | Linguistics*. https://www.scribd.com/document/888186127/2024-latechclfl-1-18

_38 citation marker(s) carried no resolvable source in the DOM and were dropped; see the `*_citations.json` sidecar._
