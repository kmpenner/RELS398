# Lesson 8.2 — Rule-Based and Probabilistic Tagging with Morpheus, TreeTagger, and CLTK

*RELS 398 / ENGL 398 · Topic 8: Lemmatization · Meeting #21 (Wed Oct 28)*

***Step 2 of the three-step cycle: deterministic.** Today you configure and run specialized morphological engines and cascading taggers (Morpheus, TreeTagger, CLTK, Stanza/LatinCy), measuring how accurately deterministic pipelines handle regular and non-standard historical forms against your manual ground truth.*

---

## **01 Content**

**From Philological Intuition to Deterministic Execution**

Yesterday you parsed, lemmatized, and treebanked a passage entirely by hand. In doing so, you experienced the deep cognitive investment required to resolve ambiguous inflectional endings, identify rare principal parts, and determine syntactic head-dependent attachments. Manual analysis provides the indispensable gold standard for scholarly precision, but its rate of production—often fewer than fifty words per hour for complex historical prose or poetry—presents an insurmountable bottleneck when scaling to large digital libraries spanning millions of words.

Today, you transition to the second step of the comparative cycle: deterministic and probabilistic natural language processing (NLP). The objective of deterministic tooling is not to replace human philological discernment, but to operationalize grammatical rules into automated, reproducible software pipelines. A deterministic parser executes a fixed set of formal algorithms over an input string, producing identical outputs every time it encounters the same text under identical configurations.

By passing the passage you analyzed yesterday through automated engines—such as Morpheus, TreeTagger, and the Classical Language Toolkit (CLTK)—you will evaluate how effectively computational systems handle lexical lookup, morphological decomposition, and contextual disambiguation. Crucially, you will discover where deterministic rules succeed in accelerating corpus annotation and where historical anomalies cause them to falter.

Understanding the boundary between deterministic reliability and algorithmic failure is essential for digital editors. When software runs predictably, an editor can design automated filters and validation checks that isolate uncertain readings for human review, establishing a disciplined human-in-the-loop workflow. This comparative methodology ensures that computational speed never compromises philological rigor.

**Takeaway:** Deterministic pipelines operationalize grammatical rules into scalable, reproducible software, automating routine parsing while exposing algorithmic limitations.

---

## **02 Content**

**Finite-State Transducers and the Morpheus Engine**

The foundational milestone in computational morphology for pre-modern languages was the creation of Morpheus, developed by Gregory Crane in 1991 for the Perseus Digital Library (Crane, 1991). Written originally in the C programming language, Morpheus operates as a rule-based finite-state morphological analyzer designed specifically to parse the intricate inflectional morphology of Ancient Greek.

A finite-state transducer (FST) is a computational automaton that maps a relation between two sets of strings—in this context, mapping an inflected surface token to its underlying lexical root and grammatical feature bundle. Morpheus achieves this by decoupling lexical stems from inflectional endings:

- **Stem Lexicon:** An extensive database containing hundreds of thousands of base roots, categorized by semantic class and conjugation/declension paradigm.
- **Morphological Rules Engine:** A formal state transition network encoding the allowable prefixations (temporal augments, preverbs, reduplication) and suffixations (tense formatives, mood vowels, case/number/person terminations) for each paradigm class.

When an input token like *ἐπαιδεύσαμεν* is fed into Morpheus, the transducer traverses its state network: it strips the augment *ἐ-*, identifies the stem *παιδευ-*, matches the sigmatic aorist formative *-σ-*, and recognizes the secondary active personal ending *-αμεν*. It then outputs the canonical lemma *παιδεύω* alongside the full morphological tag (`v1paia---`).

The FST architecture transitions across a series of internal states:

1. `State 0 (Initial)`: Scans for possible prefixes, preverbs (e.g., *κατά*, *ἀπό*), or past-tense augments (*ἐ-* or temporal lengthening).
2. `State 1 (Stem Matching)`: Queries the root dictionary for stems that match the remaining substring.
3. `State 2 (Derivational/Tense Formative)`: Matches aspectual and tense suffixes (such as *-σα-*, *-θη-*, or *-κ-*).
4. `State 3 (Inflectional Termination)`: Matches personal endings or case/number/gender suffixes.
5. `State 4 (Accepting/Output)`: Verifies that the prefix, stem, and suffix are mutually compatible according to classical Greek grammatical rules, generating the lemma and feature bundle.

Because Morpheus models Greek morphology purely through formal grammatical rules, its derivations are transparent, predictable, and mathematically rigorous. It operates without probabilistic estimation, providing an exhaustive catalog of all morphologically possible interpretations of a given character sequence without stochastic drift.

**Takeaway:** The Morpheus engine uses finite-state transducers to match inflected surface forms against a comprehensive stem lexicon and morphological rule network.

---

## **03 Content**

**The Limits of Finite-State Transduction: Ambiguity and Out-of-Vocabulary Forms**

While finite-state transducers provide rigorous coverage for regular paradigms, they possess two fundamental limitations when deployed as standalone parsing pipelines: candidate explosion and out-of-vocabulary (OOV) failure.

First, Morpheus is a morphological *analyzer*, not a *disambiguator* (Crane, 1991). Because it evaluates words in isolation without access to sentence-level syntactic context, it outputs every theoretically valid grammatical analysis permitted by its rule network. For an ambiguous Greek form like *ταύτῃ*, Morpheus produces multiple candidate parses: dative singular feminine pronoun, instrumental adverb, and locative adverb. In large corpora, this candidate explosion leaves the burden of contextual selection entirely unresolved.

When thousands of words are processed, an editor using raw FST output is confronted with massive ambiguity arrays. For common verbs and substantives, a single token may yield five to ten competing analyses. For example, a third-declension neuter plural noun form like *γένη* can be parsed as nominative, accusative, or vocative plural, while an uncontracted verbal form might simultaneously match multiple dialectal subjunctive and optative terminations. Without a secondary disambiguation layer, an edition cannot automatically determine which parsing applies to the specific sentence under study.

Second, finite-state transducers are brittle when encountering out-of-vocabulary words, spelling variants, or unedited manuscript readings. If a stem is absent from the lexicon—or if a scribe writes an itacistic spelling such as *γινώσκει* instead of *γιγνώσκει*—the transducer fails to reach an accepting state and returns an empty analysis. Rule-based transducers possess zero native capacity to infer plausible parses for words outside their explicit rule set, halting automated annotation on non-standard texts.

**Takeaway:** Finite-state analyzers generate all theoretically possible parses without contextual disambiguation and fail completely on out-of-vocabulary spellings.

---

## **04 Content**

**Probabilistic Disambiguation and the TreeTagger Architecture**

To resolve the candidate explosion generated by rule-based analyzers, computational linguistics turned to probabilistic Markov models. In 1994, Helmut Schmid introduced TreeTagger, a probabilistic part-of-speech tagger that revolutionized corpus annotation by combining Markov models with decision tree induction (Schmid, 1994).

Traditional Hidden Markov Model (HMM) taggers calculate the most probable sequence of part-of-speech tags $T = (t_1, t_2, \dots, t_n)$ for a given sentence of words $W = (w_1, w_2, \dots, w_n)$ by finding the sequence that maximizes:

$$P(T|W) \propto \prod_{i=1}^n P(w_i | t_i) P(t_i | t_{i-1}, t_{i-2})$$

In this equation, $P(w_i | t_i)$ represents the **emission probability** (the likelihood that a word appears given a specific grammatical tag), and $P(t_i | t_{i-1}, t_{i-2})$ represents the **transition probability** (the likelihood of a tag given the preceding tag trigram). Finding the optimal path across the sentence is computed efficiently using the Viterbi dynamic programming algorithm.

However, standard HMMs suffer from severe data sparsity when estimating higher-order n-gram transitions in smaller historical corpora. TreeTagger overcomes this bottleneck by utilizing binary decision trees to estimate transition probabilities. When determining the tag of a given token, the decision tree recursively tests the preceding context words and tags, automatically pruning redundant context branches to avoid overfitting sparse data (Schmid, 1994). Furthermore, TreeTagger integrates an internal lexicon to look up candidate lemmas for predicted POS tags. Because of its exceptional computational efficiency and low memory footprint, TreeTagger remains one of the most widely deployed baseline tools in historical humanities research.

By evaluating the transition probabilities of surrounding tags, TreeTagger can determine whether *profundum* is governed by a preceding preposition (favoring a noun reading) or modifies an adjacent substantive (favoring an adjectival reading), bringing statistical context to morphological disambiguation. This probabilistic grounding allows scholars to process continuous historical prose with minimal human intervention.

**Takeaway:** TreeTagger uses decision-tree-augmented Markov models to calculate the most statistically probable sequence of grammatical tags in context.

---

## **05 Content**

**The Diorisis Ancient Greek Corpus Pipeline**

A prime example of applying probabilistic tagging to pre-modern scholarship is the Diorisis Ancient Greek Corpus, developed by Alessandro Vatri and Barbara McGillivray (Vatri & McGillivray, 2020). Designed to create a syntactically and morphologically searchable digital library of classical Greek literature comprising over ten million words, Diorisis combined exhaustive lexicon lookup with TreeTagger's statistical disambiguation.

The Diorisis pipeline addresses morphological ambiguity through a two-stage architecture:

- **Stage 1 (Lexicon Expansion):** The researchers compiled a massive database of over 900,000 parsed word forms extracted from the Perseus Project's curated lexica, mapping each inflected form to its valid lemmas and POS tags.
- **Stage 2 (Statistical Tagging):** When an input text is processed, TreeTagger—trained simultaneously on the Perseus AGLDT and PROIEL dependency treebanks—selects the most probable POS tag based on sentence context. The system then queries the expanded lexicon for the lemma corresponding to that specific POS tag (Vatri & McGillivray, 2020).

In blinded evaluations, the Diorisis system achieved 97% lemmatization accuracy on Classical Attic prose (Lysias) and 90% on Homeric epic (Vatri & McGillivray, 2020). The success of Diorisis demonstrates that pairing an exhaustive, manually verified morphological lexicon with a lightweight probabilistic POS tagger yields exceptionally high accuracy on standardized literary texts.

The Diorisis experiment highlighted a fundamental philological principle: when a lexicon is comprehensive enough to cover nearly all valid word forms, a lightweight statistical model can outperform far heavier neural systems by eliminating out-of-vocabulary search failures on standard vocabulary. Furthermore, the resulting database provides an invaluable reference resource for training downstream machine-learning models.

**Takeaway:** The Diorisis pipeline pairs a 900,000-form lexicon with TreeTagger's statistical model to achieve 97% accuracy on classical prose.

---

## **06 Content**

**The Classical Language Toolkit (CLTK) Architecture**

While standalone tools like Morpheus and TreeTagger solve specific subtasks, modern computational philology requires unified, modular programming frameworks. The Classical Language Toolkit (CLTK), developed by Kyle P. Johnson and an international consortium of digital humanists, provides an extensible Python framework tailored specifically to pre-modern languages (Johnson et al., 2021).

Historical languages present unique computational challenges that modern NLP libraries (such as NLTK, spaCy, or Hugging Face) were not originally designed to handle. These include:

- The total absence of native modern speakers to provide real-time annotations.
- Extreme data sparsity and dialectal fragmentation across centuries.
- Unstandardized orthographies, complex diacritical systems, and script variations.

| Pipeline Component | Grammatical Operation | Algorithmic Implementation |
|---|---|---|
| Ingestion & Tokenizer | Segment word and punctuation boundaries | Rule-based regex and enclitic splitters |
| Normalization Unit | Standardize Unicode and character variants | Unicode NFC conversion and diacritic repair |
| Part-of-Speech Tagger | Assign UPOS and XPOS categories | Pretrained Stanza neural models / Bi-LSTM |
| Lemmatization Engine | Map inflected forms to dictionary headwords | Cascading backoff: Lexicon, Unigram, Regex, Morpheus |
| Dependency Parser | Build Universal Dependencies trees | Deep biaffine neural graph parser |

The CLTK architecture organizes linguistic processing into modular, language-specific pipelines (`NLP(language='grc')` for Greek; `NLP(language='lat')` for Latin). Each pipeline sequences discrete processing units that transform raw text into fully annotated document objects conforming to Universal Dependencies standards (Johnson et al., 2021).

**Takeaway:** The Classical Language Toolkit (CLTK) provides a modular, language-specific NLP framework engineered to overcome the data sparsity and orthographic challenges of pre-modern corpora.

---

## **07 Content**

**The CLTK Cascading Backoff Lemmatizer**

The flagship component of the CLTK Greek morphology engine is its cascading backoff lemmatizer (Johnson et al., 2021). Rather than relying on a single algorithm, a cascading backoff system sequences multiple specialized lemmatizers in descending order of precision, passing unparsed tokens down the chain until a valid lemma is found.

The CLTK backoff lemmatizer executes a four-tier cascade:

- **Tier 1 (Closed-Class Dictionary Lookup):** Queries a curated dictionary of high-frequency, indeclinable function words (prepositions, conjunctions, particles). This resolves approximately 30–40% of running tokens instantly with 100% precision.
- **Tier 2 (Treebank Unigram Model):** Queries a statistical unigram frequency model trained on the Ancient Greek Dependency Treebank (AGLDT) and PROIEL. It assigns the most frequent historical lemma associated with the surface token.
- **Tier 3 (Regular Expression Rule Tagger):** Applies regular expression patterns to match predictable inflectional paradigms (e.g., standard third-declension nominal endings or regular future suffixes).
- **Tier 4 (Morpheus Fallback Engine):** Passes remaining unparsed tokens to the legacy Morpheus finite-state transducer, querying its comprehensive root dictionary.
- **Final Default:** If all four tiers fail, the system conservatively returns the surface token itself as the lemma.

Consider how an ambiguous token like *ἐπαιδεύθησαν* traverses this cascade:

1. `Tier 1`: Checked against indeclinable closed-class lookups; fails because it is a verb.
2. `Tier 2`: Checked against the unigram model; if attested in the AGLDT, it returns *παιδεύω* immediately.
3. `Tier 3`: If absent from the treebank unigrams, regular expressions match the passive formative *-θη-* and secondary ending *-σαν*.
4. `Tier 4`: If regex fails, Morpheus extracts the root *παιδευ-* and resolves the aorist passive paradigm.

By placing high-precision dictionary lookups at the front of the cascade, the pipeline avoids expensive computational operations on common words, reserving neural and rule-based parsing engines for ambiguous open-class substantives and verbs.

**Takeaway:** Cascading backoff lemmatizers maximize recall by chaining closed-class lookups, unigram frequency models, regex rules, and finite-state fallbacks.

---

## **08 Content**

**Memory-Based Learning: The GLEM Lemmatizer**

An alternative deterministic methodology to decision trees and rule cascades is Memory-Based Learning (MBL), exemplified by the Greek Lemmatizer (GLEM) developed by Maarten van Gompel and Antal van den Bosch (Vatri & McGillivray, 2020; Swaelens et al., 2024). Memory-Based Learning operates on the principle of k-nearest-neighbor classification: rather than inducing abstract rules or probabilistic trees during training, the system stores all training exemplars directly in memory.

When presented with an unseen surface token, GLEM compares its character n-grams and morphological context to the stored training instances, calculating similarity metrics to predict the appropriate lemma and morphological edit-tree:

- **Lexicon Cache:** GLEM first checks an exact-match lexicon for known words.
- **Memory-Based Induction:** For unknown or ambiguous tokens, GLEM evaluates the prefix, root, and suffix characters against nearest-neighbor clusters in its training memory, predicting the string transformations necessary to reconstruct the canonical lemma (Vatri & McGillivray, 2020).

In comparative benchmarks, GLEM achieved 93% accuracy on Classical Greek prose, outperforming simple unigram models on complex inflected verbs. However, because memory-based systems rely on surface character similarity, they remain vulnerable when scribes introduce non-standard phonological substitutions that distort character n-grams.

If a dialectal form or scribal error alters three or four characters in a word, the nearest-neighbor distance calculation is disrupted, causing GLEM to link the token to an unrelated lexical cluster. For instance, an itacistic spelling like *γεινωσκουσιν* might have higher character overlap with an unrelated noun stem than with the true root *γιγνωσκ-*, causing the memory-based classifier to output an erroneous lemma. This behavior illustrates the persistent trade-off between instance-based pattern matching and rule-based derivation.

**Takeaway:** Memory-Based Learning (GLEM) lemmatizes unknown forms by computing k-nearest-neighbor similarity against stored training exemplars.

---

## **09 Content**

**Modern Neural Pipeline Frameworks: Stanza and UDPipe**

Over the past decade, statistical taggers have increasingly been integrated with neural network backbones. Within the CLTK and wider NLP ecosystems, two frameworks dominate automated dependency parsing: Stanza (developed by the Stanford NLP Group) and UDPipe (developed by Charles University) (Johnson et al., 2021).

Both Stanza and UDPipe implement end-to-end neural pipelines trained directly on Universal Dependencies treebanks:

- **Tokenization & Sentence Segmentation:** Bi-LSTM character-level sequence models that identify sentence boundaries and split multi-word tokens.
- **POS Tagging & Morphological Features:** A character-level convolutional neural network (CNN) combined with word embeddings to predict UPOS, XPOS, and FEATS simultaneously.
- **Syntactic Dependency Parsing:** A deep biaffine neural attention parser that scores potential head-dependent links across the sentence, constructing maximum spanning trees to output full Universal Dependencies graphs.

In the CLTK, calling `NLP(language='grc')` loads pre-trained Stanza models trained on the PROIEL and Perseus treebanks. This allows editors to generate complete 10-column CoNLL-U trees programmatically in a single Python command, establishing a powerful baseline for digital edition workflows.

Because these neural models process whole sentences simultaneously, they capture non-local syntactic dependencies far more effectively than n-gram Markov models, significantly improving attachment accuracy on complex dependent clauses.

**Takeaway:** Stanza and UDPipe provide end-to-end neural pipelines trained on Universal Dependencies treebanks to generate synchronized POS tags and syntax trees.

---

## **10 Content**

**LatinCy and spaCy Pipelines for Latin**

For Latin computational philology, the LatinCy project—developed by Patrick J. Burns—integrates historical Latin language models into the industrial-strength spaCy framework (Burns, 2023). LatinCy bridges the gap between digital classics and modern NLP infrastructure, providing high-speed tokenization, POS tagging, lemmatization, and dependency parsing.

LatinCy distributes several pre-trained pipeline models:

- `la_core_web_sm`: Lightweight CPU model using convolutional neural networks and rule-based lemmatizers.
- `la_core_web_md` / `la_core_web_lg`: Larger models incorporating 300-dimensional fastText word vectors trained on the Classical Latin LASLA corpus and Perseus treebanks.
- `la_core_web_trf`: Transformer-based pipeline utilizing fine-tuned RoBERTa embeddings for high-accuracy contextual disambiguation.

LatinCy explicitly maps its outputs to the Universal Dependencies and Perseus XPOS schemas:

```python
import spacy

nlp = spacy.load("la_core_web_lg")
doc = nlp("Arma virumque cano Troiae qui primus ab oris.")

for token in doc:
  print(
      f"{token.text:<10} {token.lemma_:<10} {token.pos_:<6}"
      f" {token.tag_:<12} {token.dep_:<8} {token.head.text}"
  )
```

By leveraging spaCy's optimized C-extensions, LatinCy can process hundreds of thousands of words in seconds, making it the premier deterministic tool for bulk Latin corpus annotation. Its integration into spaCy allows scholars to construct custom rule matchers, entity recognizers, and text classification pipelines using standard modern software patterns. Furthermore, LatinCy's modular architecture allows editors to train custom statistical components on domain-specific subcorpora, such as Neo-Latin or legal texts.

**Takeaway:** LatinCy embeds classical Latin language models into the spaCy framework, providing high-speed, standards-compliant linguistic annotation.

---

## **11 Content**

**The Challenge of Historical Orthographic Noise**

When deterministic and statistical NLP engines are tested on standardized critical editions (such as Oxford Classical Texts or Teubner editions), they routinely achieve accuracy scores exceeding 90–95%. However, when the exact same pipelines are deployed on raw manuscript transcriptions or historical documents, their performance deteriorates sharply.

This degradation is driven by **orthographic noise**—the natural spelling variation, regional phonological shifts, and scribal idiosyncrasies present in historical witnesses (Bawden et al., 2026). Pre-modern scribes did not adhere to modern standardized orthography. In medieval Latin, diphthongs monophthongized (*ae* and *oe* became *e*, yielding *que* for *quae* or *hec* for *haec*), consonants doubled or simplified (*litera* for *littera*), and *u* and *v* were used interchangeably.

Because rule-based dictionaries and statistical n-gram tables are built on standardized training texts, unnormalized historical tokens fail to match known dictionary keys. A single orthographic substitution can cause a cascading series of pipeline errors: the tokenizer misidentifies word boundaries, the POS tagger defaults to an incorrect category, and the lemmatizer fails to return a valid lemma.

For textual scholars editing unstudied manuscript witnesses, understanding this noise bottleneck prevents naive assumptions about tool performance. An editor cannot assume that a 95% published benchmark applies equally to a ninth-century Carolingian codex or a twelfth-century Byzantine manuscript. Managing orthographic noise requires explicit pre-processing or multi-layered encoding strategies.

**Takeaway:** Historical orthographic variation causes severe performance degradation in deterministic parsers by creating out-of-vocabulary mismatches with standardized lexica.

---

## **12 Content**

**Byzantine Itacism and Vowel Mergers**

In the Greek linguistic tradition, the most pervasive source of orthographic noise is **itacism** (iotacism)—the historical phonological merger wherein six distinct ancient vowels and diphthongs (*ι*, *η*, *ει*, *οι*, *υ*, *υι*) converged into the single phonetic vowel sound [i] during the Hellenistic and Byzantine periods.

In medieval manuscripts, scribes wrote phonetically, freely substituting these characters based on sound rather than historical etymology. A scribe might write:

- *γινώσκει* or *γεινώσκει* for *γιγνώσκει*
- *κλῖμαξ* for *κλεῖμαξ*
- *ποιεῖτε* (present active indicative/imperative) written interchangeably with *ποιῆται* (present middle/passive subjunctive)

In a landmark empirical evaluation of unedited Byzantine book epigrams, Swaelens, De Vos, and Lefever (2023, 2024) demonstrated that itacism causes catastrophic accuracy drops across all standard NLP taggers:

| Lemmatization Pipeline | Target Corpus | Reported Accuracy | Primary Architecture |
|---|---|---|---|
| RNN Tagger | Classical Attic Prose | 91.29% | Bi-LSTM Neural Network |
| RNN Tagger | Unedited Byzantine Epigrams | 66.67% | Bi-LSTM Neural Network |
| GLEM | Classical Attic Prose | 93.00% | Memory-Based Learning (FROG) |
| GLEM | Unedited Byzantine Epigrams | 70.82% | Memory-Based Learning (FROG) |
| CLTK Cascading Backoff | Classical Attic Prose | 91.00% | Cascade: Unigram, Regex, Morpheus |
| CLTK Cascading Backoff | Unedited Byzantine Epigrams | 71.69% | Cascade: Unigram, Regex, Morpheus |

As the data proves, state-of-the-art tools lose 20 to 25 percentage points of accuracy when confronted with unstandardized Byzantine manuscript spelling (Swaelens et al., 2024).

This collapse occurs because standard lexica store only etymological classical spellings. When an itacistic spelling enters the pipeline, dictionary lookups fail, forcing taggers into statistical fallback modes that mispredict lemmas based on distorted surface characters. The error ripples through syntactic dependency parsing, where misidentified word classes distort entire sentence graphs.

**Takeaway:** Itacistic vowel mergers in Byzantine Greek cause a 20–25% accuracy collapse in deterministic taggers due to phonetic spellings violating dictionary headword stems.

---

## **13 Content**

**The Loss of Iota Subscript and Diacritical Noise**

A secondary, highly destructive vector of morphological error in historical Greek texts is the omission of the **iota subscript** (*ι subscriptum*). In classical Attic Greek, long diphthongs (*ᾳ*, *ῃ*, *ῳ*) carried a pronounced final [i] sound. By the medieval period, this offglide had ceased to be pronounced, and scribes routinely omitted the subscript iota in uncial and minuscule manuscripts.

The absence of the iota subscript eliminates vital grammatical distinctions:

- Dative singular nouns (*λόγῳ*) become orthographically identical to nominative/accusative dual or adverbial forms (*λόγω*).
- Subjunctive verb forms (*γράφῃ*) become orthographically identical to third-person singular indicative or imperative forms (*γράφει* or *γράφη*).
- First-declension feminine dative singular adjectives (*τῇ καλῇ*) lose their case-identifying terminations.

When a deterministic parser encounters *λογω* without an iota subscript, finite-state lookup engines fail to identify the word as a dative noun. If diacritical accents and breathings are also degraded or omitted on papyri and stone inscriptions, the out-of-vocabulary rate climbs exponentially, completely disabling dictionary-based lemmatizers.

In epigraphic and papyrological datasets, where text is inscribed entirely without diacritics in majuscule script, standard rule cascades drop below 50% accuracy unless preceded by an explicit accent restoration pass. Without the iota subscript, a deterministic parser cannot disambiguate whether a third-person verb is indicative (*ποιεῖ*) or subjunctive (*ποιῇ*), creating critical grammatical misinterpretations.

**Takeaway:** The loss of iota subscripts and diacritics strips words of essential case and mood markers, causing deterministic engines to misparse inflectional categories.

---

## **14 Content**

**Dialectal Variation: Epic, Ionic, and Koine vs. Classical Attic**

Beyond scribal spelling errors, pre-modern corpora exhibit profound structural dialectal variation. Classical NLP taggers are overwhelmingly trained on Classical Attic prose (such as the speeches of Lysias or Plato's dialogues). When these models are deployed on archaic epic poetry, Ionic prose, or post-classical Koine, they encounter morphological structures that violate Attic grammar rules.

In the Homeric epic dialect:

- Verbs frequently appear in **uncontracted** forms (e.g., *ὁράουσι* instead of Attic *ὁρῶσι*; *ἄειδε* instead of *ᾖδε*).
- Nouns retain archaic case endings (e.g., genitive singular in *-οιο* alongside *-ου*; instrumental/locative in *-φι*).
- Third-person plural verbs retain unaugmented or athematic endings (e.g., *ἔβαν* for *ἔβησαν*).

In Koine Greek (such as the Septuagint and New Testament), the dual number disappeared entirely, second aorist verbs adopted first aorist endings (e.g., *εἶπαν* instead of *εἶπον*), and classical optative moods were largely replaced by subjunctive constructions (Haug & Jøhndal, 2008).

When Vatri and McGillivray (2020) benchmarked lemmatization across corpora, accuracy on Homer dropped to 90% compared to 97% on Lysias, precisely because epic dialectal forms were underrepresented in the statistical transition models.

These findings highlight that a model trained on fifth-century BCE Athenian oratory cannot be treated as a universal parser for all periods of Greek literature. Digital humanists must match their models and lexica to the specific dialect and era of the text, curating specialized treebanks for epic, biblical, and Byzantine corpora.

**Takeaway:** Morphological taggers trained on Classical Attic prose suffer systematic accuracy drops when processing Homeric uncontracted forms or Koine inflectional shifts.

---

## **15 Content**

**Benchmarking Deterministic Accuracy: Precision, Recall, and F1**

To rigorously evaluate deterministic pipelines against your Tuesday manual ground truth, you must apply standard quantitative metrics from computational evaluation:

- **True Positives ($TP$):** The number of tokens where the automated tagger’s prediction matches the manual gold standard exactly.
- **False Positives ($FP$):** The number of tokens where the tagger predicted a grammatical tag that contradicts the gold standard.
- **False Negatives ($FN$):** The number of gold-standard grammatical features that the tagger failed to identify.

$$\text{Precision} = \frac{TP}{TP + FP}$$

$$\text{Recall} = \frac{TP}{TP + FN}$$

$$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

For lemmatization, **Accuracy** is calculated as the total number of correct lemmas divided by the total number of tokens. For morphological tagging, scores are calculated both as an **Exact Match Ratio** (where all nine morphological positions must be correct simultaneously) and as individual feature-level F1 scores (measuring accuracy on Case, Number, Tense, and Mood independently).

Computing these metrics across distinct word classes allows editors to pinpoint exact algorithmic weaknesses. For instance, a tagger might achieve 98% precision on common nouns but drop to 70% recall on irregular verbs, signaling where post-processing validation is required. These empirical calculations ensure that evaluations remain grounded in objective mathematical measurement.

**Takeaway:** Precision, Recall, F1, and Exact Match ratios provide the mathematical framework for benchmarking automated tagger performance against manual gold standards.

---

## **16 Content**

**Normalizing Before Parsing: The `att.lexicographic.normalized` TEI Schema**

Because historical orthographic noise degrades deterministic parsing, digital editors must implement a disciplined two-layer architecture: normalizing the text to enable accurate computational parsing while preserving the manuscript's diplomatic spelling for scholarly fidelity (Bawden et al., 2026).

The Text Encoding Initiative provides the `att.lexicographic.normalized` attribute class within Chapter 18 to formalize this dual-layer encoding (TEI Consortium, 2026):

- `@orig`: Stores the original diplomatic reading attested in the manuscript witness (including itacisms, uncontracted forms, or omitted iotas).
- `@norm`: Stores the regularized, etymological form required by NLP lexica and parsers to successfully identify the token.
- `@lemma`, `@pos`, `@msd`: Store the resulting linguistic annotations generated from the normalized form.

```xml
<!-- Encoding a Byzantine itacistic reading in TEI P5 Chapter 18 -->
<w xml:id="w42" 
   orig="γεινώσκει" 
   norm="γιγνώσκει" 
   lemma="γιγνώσκω" 
   pos="VERB" 
   msd="Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act">γεινώσκει</w>
```

This serialization achieves complete scholarly transparency: downstream search engines and treebank visualizers query `@norm`, `@lemma`, and `@pos`, while the digital edition displays the diplomatic `@orig` reading to the reader.

This architecture ensures that digital editions satisfy both computational and paleographical demands. A paleographer examining scribal orthography can extract all `@orig` strings, while a computational linguist analyzing syntax operates over clean `@norm` and `@lemma` attributes. Encoding both layers inside the `<w>` element eliminates the need for redundant duplicate files.

**Takeaway:** TEI `@orig` and `@norm` attributes maintain diplomatic fidelity while providing normalized strings for NLP parsing pipelines.

---

## **17 Content**

**Constructing Preprocessing Normalization Scripts**

To bridge the gap between diplomatic manuscript transcriptions and deterministic parsers, digital editors author automated preprocessing scripts in Python. A preprocessing script regularizes systematic orthographic shifts before the text is passed into the NLP engine.

A standard historical normalization script executes four sequential operations:

1. **Unicode Standardization:** Converts all characters to Unicode Normalization Form C (NFC), standardizing precomposed polytonic Greek characters and resolving combining diacritic inconsistencies (Topic 1).
2. **Orthographic Standardization:** Regularizes interchange of *u/v* and *i/j* in Latin texts, or standardizes lunate sigma (*ϲ*) to word-internal (*σ*) and word-final (*ς*) sigmas in Greek.
3. **Diacritic Restoration:** Applies rule-based heuristics or character-level language models to restore omitted iota subscripts and breathing marks on high-frequency nouns and verbs.
4. **Abbreviation Expansion:** Resolves common scribal ligatures, suspensions, and nomina sacra into full lexical strings.

```python
import unicodedata, re


def normalize_greek_for_nlp(text):
  # Step 1: Normalize Unicode to NFC precomposed form
  text = unicodedata.normalize("NFC", text)
  # Step 2: Replace lunate sigma with standard sigmas
  text = re.sub(r"ϲ\b", "ς", text)
  text = text.replace("ϲ", "σ")
  # Step 3: Expand common itacisms in known closed-class particles
  text = re.sub(r"\bγεινώσκ", "γιγνώσκ", text)
  text = re.sub(r"\bγινώσκ", "γιγνώσκ", text)
  return text
```

By running this preprocessing script over raw transcriptions, editors can eliminate up to 70% of out-of-vocabulary mismatches before querying Morpheus or TreeTagger. When building your pipeline, each normalization rule should be logged in an audit trail, ensuring that every transformation from diplomatic character to normalized token is recorded and reversible.

**Takeaway:** Python preprocessing scripts normalize Unicode forms, expand abbreviations, and regularize scribal spelling shifts prior to NLP ingestion.

---

## **18 Content**

**Configuring the CLTK Greek Pipeline**

To execute deterministic tagging over your benchmark passage, you will configure the Classical Language Toolkit in a local Python environment. The CLTK pipeline allows you to customize which analytical modules are executed and in what sequence (Johnson et al., 2021).

```python
from cltk.languages.pipelines import GreekPipeline
from cltk.nlp import NLP

# Initialize CLTK NLP pipeline for Ancient Greek
cltk_nlp = NLP(language="grc", custom_pipeline=GreekPipeline)

# Process your benchmark text passage
sample_text = (
    "Ὅτι μὲν ὑμεῖς, ὦ ἄνδρες Ἀθηναῖοι, πεπόνθατε ὑπὸ τῶν ἐμῶν λόγων, οὐκ οἶδα."
)
cltk_doc = cltk_nlp.analyze(text=sample_text)

# Inspect generated tokens, lemmas, and UPOS tags
for word in cltk_doc.words:
  print(f"{word.string:<12} {word.lemma:<12} {word.upos:<8} {word.xpos}")
```

When executing this code, CLTK tokenizes the text, normalizes diacritics, queries its cascading backoff lemmatizer, and invokes its pre-trained Stanza neural model to predict Universal Dependencies UPOS, XPOS, and dependency relations (Johnson et al., 2021). The resulting `Doc` object contains a fully parsed linguistic graph stored in memory.

Editors can inspect the internal properties of each `Word` object, accessing morphological features, syntactic governor indices, and stopword classifications to perform automated quality checks across entire documents. Advanced configurations allow users to inject custom lexicon dictionaries directly into the pipeline before runtime.

**Takeaway:** The CLTK Python API configures modular pipelines to execute tokenization, lemmatization, and dependency parsing across Ancient Greek texts.

---

## **19 Content**

**Configuring LatinCy and TreeTagger for Latin**

For Latin corpora, configuring LatinCy within spaCy provides a high-performance deterministic and transformer-based annotation environment (Burns, 2023).

```python
import spacy

# Load the large Classical Latin pipeline model
nlp_lat = spacy.load("la_core_web_lg")

# Process a benchmark Latin sentence
latin_text = "Arma virumque cano, Troiae qui primus ab oris."
doc = nlp_lat(latin_text)

# Extract linguistic attributes
for token in doc:
  print(
      f"Token: {token.text:<10} | Lemma: {token.lemma_:<10} | POS:"
      f" {token.pos_:<6} | Dep: {token.dep_:<8} | Head: {token.head.text}"
  )
```

To run TreeTagger directly over the same text for comparative benchmarking, you can invoke the TreeTagger binary via the `treetaggerwrapper` Python package:

```python
import treetaggerwrapper

tagger = treetaggerwrapper.TreeTagger(TAGLANG="la")
tags = tagger.tag_text(latin_text)

for tag_line in tags:
  word, pos, lemma = tag_line.split("\t")
  print(f"{word:<12} {pos:<10} {lemma}")
```

Running both tools side by side allows editors to compare the probabilistic decision-tree predictions of TreeTagger against the neural embeddings of LatinCy. Comparing their outputs reveals where statistical n-grams agree with neural attention and where differences require human adjudication. This dual-execution strategy ensures high confidence across standard grammatical structures.

**Takeaway:** Python interfaces for LatinCy and TreeTagger enable side-by-side execution and comparative benchmarking across Latin corpora.

---

## **20 Content**

**Executing the Deterministic Benchmark Experiment**

With your environments configured, you will now run the automated pipelines over the exact 200–300 word passage you manually parsed on Tuesday. This empirical experiment establishes the concrete performance gap between human philological analysis and deterministic machine tagging.

The testing protocol requires three synchronized steps:

1. **Ingestion:** Pass the raw, unannotated text of your benchmark passage through the CLTK Greek pipeline (or LatinCy for Latin).
2. **Export:** Export the machine-generated predictions into a candidate CoNLL-U file: `machine_output.conllu`.
3. **Alignment:** Align the machine-generated tokens line-by-line with your Tuesday gold standard (`gold_standard.conllu`).

Any discrepancy in tokenization (such as an automated tokenizer failing to split an enclitic *-que* or treating punctuation differently) will cause index misalignment. Aligning tokens first ensures that subsequent POS, lemma, and dependency evaluations are scored on identical token spans.

Running this comparison establishes your quantitative benchmark: you will compute overall accuracy, tokenization error rate, and feature-by-feature precision scores, creating the empirical foundation for Friday's AI evaluation. Logging these metrics in an experimental lab notebook ensures that all methodological comparisons remain fully documented.

**Takeaway:** Running automated pipelines over the manual benchmark passage and exporting aligned CoNLL-U files is the prerequisite for empirical scoring.

---

## **21 Content**

**Evaluating Tokenization Alignment**

The first diagnostic evaluation in benchmarking deterministic tools is measuring tokenization accuracy. In natural language processing, tokenization errors propagate downstream: if a tokenizer splits a single compound word into two tokens, or fails to split an enclitic, every subsequent POS tag, lemma, and dependency link for that span will be evaluated as incorrect.

Common tokenization failure modes in classical NLP pipelines include:

- **Enclitic and Proclitic Mergers:** The pipeline treats *senatusque* as a single token, assigning it a nonexistent lemma *senatusque* rather than splitting it into *senatus* and *-que*.
- **Punctuation Attachment:** The pipeline fails to separate trailing punctuation (e.g., colons, Greek question marks `;`, or middots `·`) from surface word strings, creating corrupted token keys like `λόγων,`.
- **Crasis Failure:** The pipeline fails to recognize *κἀγώ* as a contracted multi-word token, attempting to look up *καγω* in the lexicon.

| Token Index | Gold Form | Machine Form | Alignment Status |
|---|---|---|---|
| 1 | Ὅτι | Ὅτι | MATCH |
| 2 | μὲν | μὲν | MATCH |
| 3 | ὑμεῖς | ὑμεῖς | MATCH |
| 4 | , | , | MATCH |
| 11 | λόγων | λόγων, | MISALIGNMENT (Trailing Comma Attached) |

Digital editors must inspect tokenization alignment reports, adjusting tokenizer regular expressions to ensure 100% token correspondence before scoring morphology.

**Takeaway:** Tokenization errors propagate to all subsequent layers; automated token streams must be strictly aligned with gold tokens prior to morphological evaluation.

---

## **22 Content**

**Evaluating Part-of-Speech Accuracy: Generating Confusion Matrices**

Once tokens are aligned, you will evaluate Part-of-Speech tagging accuracy by generating a **confusion matrix**. A confusion matrix is a two-dimensional grid where rows represent the true human gold-standard UPOS tags and columns represent the machine-predicted UPOS tags.

```
Sample UPOS Confusion Matrix (100 Sample Tokens):
Gold \ Pred   NOUN   VERB   ADJ   PRON   DET   ADV   PART
NOUN           45      0      3      1     0     0      0
VERB            0     28      1      0     0     0      0
ADJ             4      0     12      0     0     1      0
PRON            0      0      0      8     1     0      0
DET             0      0      0      2     9     0      0
ADV             0      0      1      0     0     5      1
PART            0      0      0      0     0     1      6
```

Analyzing the off-diagonal cells of the confusion matrix reveals systematic algorithmic confusions:

- **Adjective vs. Noun Confusion:** Substantivized adjectives (e.g., *τὰ καλά* = "the good things") are frequently misclassified by statistical taggers as pure adjectives (`ADJ`) rather than substantives (`NOUN`).
- **Pronoun vs. Determiner Confusion:** Demonstrative pronouns used as determiners (*hic vir*) vs. independent pronouns (*hic dixit*) are routinely conflated by n-gram models that evaluate only local two-word windows.
- **Participle Classification:** Pipelines frequently disagree on whether participles should be tagged as `VERB` with `VerbForm=Part` or as `ADJ`.

By inspecting the confusion matrix, an editor can determine whether errors stem from true model confusion or from minor taxonomic disagreements between the annotation manual and the training treebank.

**Takeaway:** Confusion matrices expose systematic grammatical misclassifications, such as conflations between substantivized adjectives, pronouns, and determiners.

---

## **23 Content**

**Evaluating Lemmatization Accuracy: Exact Match vs. Normalized Match**

Lemmatization evaluation measures whether the automated pipeline identified the correct canonical dictionary headword. In evaluating pre-modern lemmatizers, editors distinguish between two scoring metrics:

- **Exact Match Accuracy:** The predicted lemma string must match the gold-standard lemma string character-for-character, including all polytonic Greek diacritics and accents.
- **Normalized Match Accuracy:** The predicted and gold lemmas are normalized (stripping accents, standardizing *u/v* or *i/j*, and converting to lowercase) before comparison.

| Surface Token | Gold Standard Lemma | Machine Predicted Lemma | Exact Match Result | Normalized Match Result |
|---|---|---|---|---|
| ἔγνωσαν | γιγνώσκω | γινώσκω | FAIL | PASS (Dialect Variant) |
| rexit | rego | rego | PASS | PASS |
| πόλεσιν | πόλις | πόλις | PASS | PASS |
| haesit | haereo | haesito | FAIL | FAIL (Lexical Error) |

In typical benchmarks across Classical Greek prose:

- CLTK cascading backoff achieves ~91% exact match accuracy.
- TreeTagger / Diorisis achieves ~94–97% exact match accuracy.
- On unedited medieval manuscripts with itacism, exact match accuracy plummets to ~66–71%, while normalized match accuracy recovers to ~82% (Swaelens et al., 2024).

This disparity proves that the primary bottleneck in historical lemmatization is not algorithmic failure to recognize morphology, but orthographic divergence from standard dictionary headword spelling.

**Takeaway:** Distinguishing exact match from normalized match accuracy demonstrates that spelling variation, rather than grammatical parsing, is the primary driver of lemmatization errors.

---

## **24 Content**

**Evaluating Morphological Feature Accuracy**

Beyond coarse POS tags and lemmas, pre-modern philology requires granular morphological features (Case, Number, Gender, Tense, Mood, Voice, Person). Evaluating morphological feature accuracy requires measuring individual feature dimensions independently.

A comprehensive evaluation script iterates across all tokens, calculating feature-level F1 scores:

| Feature Dimension | Gold Feature Count | Correct Predictions | Feature Precision | Feature Recall | Feature F1 |
|---|---|---|---|---|---|
| `Case` (Nom/Gen/Dat/Acc/Voc/Abl) | 120 | 112 | 94.1% | 93.3% | 0.937 |
| `Number` (Sing/Plur/Dual) | 185 | 179 | 97.3% | 96.7% | 0.970 |
| `Gender` (Masc/Fem/Neut) | 120 | 108 | 91.5% | 90.0% | 0.907 |
| `Tense` (Pres/Past/Fut/Perf) | 65 | 59 | 92.2% | 90.7% | 0.914 |
| `Mood` (Ind/Sub/Opt/Imp/Inf) | 65 | 61 | 95.3% | 93.8% | 0.945 |
| `Voice` (Act/Mid/Pass) | 65 | 58 | 90.6% | 89.2% | 0.899 |

Empirical analysis reveals that **Gender** and **Voice** exhibit the lowest accuracy among morphological features. Gender is an inherent lexical property of nouns that cannot be deduced from surface endings alone in third-declension forms, while Voice is frequently obscured in Greek and Latin due to deponent verbs and ambiguous middle/passive morphology.

When evaluating automated parsing for a digital edition, knowing that Gender and Voice carry higher error rates allows editors to focus manual proofreading passes specifically on these vulnerable feature dimensions.

**Takeaway:** Feature-level evaluation reveals that Gender and Voice exhibit the highest error rates due to third-declension nominal syncretism and deponent verbal systems.

---

## **25 Content**

**Evaluating Syntactic Dependency Parsing: UAS and LAS**

To evaluate the syntactic dependency trees generated by neural parsers (such as Stanza or LatinCy) against your manual treebank, computational linguistics relies on two standard attachment metrics:

- **Unlabeled Attachment Score (UAS):** The percentage of words that have been assigned the correct syntactic head index, regardless of whether the dependency relation label is correct.
- **Labeled Attachment Score (LAS):** The percentage of words that have been assigned *both* the correct head index and the correct Universal Dependencies relation label (`DEPREL`).

$$\text{UAS} = \frac{\text{Count of tokens with correct HEAD}}{\text{Total Tokens}}$$

$$\text{LAS} = \frac{\text{Count of tokens with correct HEAD and correct DEPREL}}{\text{Total Tokens}}$$

In classical treebank evaluations:

- On standardized classical prose with short sentences (under 15 words), Stanza and UDPipe achieve UAS $\approx 84\%$ and LAS $\approx 78\%$.
- On complex historical poetry (Homer, Virgil) featuring hyperbaton and non-projective dependencies, scores drop significantly: UAS $\approx 72\%$ and LAS $\approx 64\%$.

Dependency parsers struggle most acutely with long-distance attachments, coordinated structures (`conj`/`cc`), and prepositional phrase attachment ambiguity. Because dependency relations model the hierarchical architecture of the sentence, a single misattached head near the root can cascade errors across all subordinate clauses.

**Takeaway:** Unlabeled Attachment Score (UAS) and Labeled Attachment Score (LAS) quantify the structural accuracy of automated syntactic dependency trees against manual gold standards.

---

## **26 Content**

**Serializing Pipeline Output to TEI XML**

Once automated tagging is complete, the predictions stored in memory or CoNLL-U format must be serialized into valid TEI P5 XML conforming to Chapter 18 guidelines (TEI Consortium, 2026). Digital editors write Python scripts to automate this conversion, transforming pipeline `Doc` objects into structured XML trees.

```python
import xml.etree.ElementTree as ET


def serialize_doc_to_tei(doc, output_path):
  s_elem = ET.Element("s", {"xml:id": "s1", "n": "1"})

  for i, token in enumerate(doc, start=1):
    if token.is_punct:
      pc = ET.SubElement(
          s_elem,
          "pc",
          {
              "xml:id": f"s1_pc{i}",
              "force": "strong" if token.text in ".?!" else "weak",
          },
      )
      pc.text = token.text
    else:
      w = ET.SubElement(
          s_elem,
          "w",
          {
              "xml:id": f"s1_w{i}",
              "lemma": token.lemma_,
              "pos": token.pos_,
              "msd": token.tag_ if token.tag_ else "_",
          },
      )
      w.text = token.text

  tree = ET.ElementTree(s_elem)
  tree.write(output_path, encoding="utf-8", xml_declaration=True)
```

This automated script creates standardized `<w>` and `<pc>` elements, injecting `@lemma`, `@pos`, and `@msd` attributes directly from the pipeline output. Serializing machine predictions into standard TEI XML allows editors to visualize and edit automated parses directly within digital scholarly editing environments.

By maintaining a clean separation between text nodes and analytical attributes, the serialized XML document remains fully compliant with TEI validation schemas while encoding rich linguistic metadata for downstream web applications.

**Takeaway:** Python serialization scripts convert NLP pipeline document objects into TEI P5 Chapter 18 XML elements carrying full `att.linguistic` attributes.

---

## **27 Content**

**Serializing Pipeline Output to Validated CoNLL-U**

To ensure interoperability with treebank validation suites and machine learning frameworks, automated pipeline outputs must also be serialized into strictly validated 10-column CoNLL-U files.

The serialization script iterates over each sentence in the document, extracting the token index, surface form, lemma, UPOS, XPOS, FEATS string, head index, and dependency relation:

```python
def export_conllu(doc, file_path):
  with open(file_path, "w", encoding="utf-8") as f:
    f.write("# sent_id = test_passage_01\n")
    f.write(f"# text = {doc.text}\n")
    for i, token in enumerate(doc, start=1):
      head_idx = token.head.i + 1 if token.head != token else 0
      dep_rel = token.dep_.lower() if token.dep_ else "dep"
      feats = token.morph.to_json() if token.morph else "_"
      f.write(
          f"{i}\t{token.text}\t{token.lemma_}\t{token.pos_}\t{token.tag_}\t"
          f"{feats}\t{head_idx}\t{dep_rel}\t_\t_\n"
      )
    f.write("\n")
```

Once exported, the CoNLL-U file must be checked against official Universal Dependencies format specifications using automated linters:

```bash
python3 shared/scripts/validate_conllu.py --lang grc machine_output.conllu
```

Validating the CoNLL-U export ensures that downstream scoring scripts and cross-platform repositories can parse the generated dependency trees without syntax errors. This guarantees that your automated outputs can be directly integrated into international treebank collections.

**Takeaway:** Exporting pipeline predictions to validated CoNLL-U files ensures adherence to Universal Dependencies specifications and enables automated scoring.

---

## **28 Content**

**Strengths and Vulnerabilities of Rule-Based vs. Statistical Taggers**

Comparing the results of finite-state transducers (Morpheus), decision-tree taggers (TreeTagger / Diorisis), and neural pipelines (CLTK / Stanza) against your manual ground truth highlights fundamental trade-offs in computational linguistics:

- **Rule-Based Systems (Morpheus):**
  - *Strengths:* 100% deterministic precision on valid stems; transparent, explainable grammatical derivations; no stochastic variation.
  - *Vulnerabilities:* Zero contextual disambiguation; complete failure on out-of-vocabulary spellings and itacisms; cannot score probabilities.
- **Statistical / Markov Systems (TreeTagger):**
  - *Strengths:* Rapid contextual disambiguation; low computational overhead; robust performance when paired with large lexica (Diorisis).
  - *Vulnerabilities:* Limited context window (n-grams); vulnerable to sparse data on rare constructions; cannot model long-distance hyperbaton.
- **Neural Pipelines (Stanza / LatinCy):**
  - *Strengths:* Deep contextual embeddings; end-to-end dependency parsing; higher resilience to complex syntax.
  - *Vulnerabilities:* High computational cost; vulnerability to out-of-distribution dialect shifts; potential for non-transparent errors.

Understanding these trade-offs allows digital scholars to select the optimal tool for each specific philological corpus. A project editing standardized Classical Latin prose may rely safely on LatinCy or TreeTagger, whereas a project editing non-standard medieval epigrams requires custom normalization and rule cascades.

**Takeaway:** Rule-based tools offer deterministic precision but zero disambiguation, while statistical and neural models provide contextual tagging at the cost of vulnerability to dialectal noise.

---

## **29 Content**

**Building a Hybrid Mitigation Pipeline**

The empirical findings of recent research—particularly Swaelens et al. (2024) and Vatri and McGillivray (2020)—demonstrate that no single deterministic or statistical architecture handles all challenges of pre-modern corpora. The state of the art in digital philology relies on **hybrid mitigation pipelines**.

A modern hybrid pipeline integrates the complementary strengths of each architecture:

- **Layer 1 (Preprocessing Normalizer):** A rule-based Python script standardizes Unicode NFC, resolves ligatures, and expands high-frequency itacistic spelling variants.
- **Layer 2 (Curated Closed-Class Lookup):** A static dictionary resolves 100% of indeclinable particles, prepositions, and conjunctions.
- **Layer 3 (Expanded Morphological Lexicon):** An expanded database (such as Diorisis' 900,000-form cache) provides valid candidate lemmas for known inflected forms.
- **Layer 4 (Neural Contextual Disambiguator):** A neural transformer (Stanza or LatinCy) selects the most probable POS tag and dependency tree in context.
- **Layer 5 (Finite-State Fallback):** Morpheus evaluates rare open-class words that failed lexicon lookup.

By combining preprocessing normalization with layered statistical and rule-based lookups, hybrid pipelines mitigate itacistic accuracy loss, boosting unedited manuscript lemmatization from 66% back above 88% (Swaelens et al., 2024).

This multi-tiered architecture ensures that high-confidence regular forms are processed at lightning speed, while ambiguous and non-standard tokens are progressively escalated to deeper analytical models.

**Takeaway:** Hybrid pipelines combine rule-based normalizers, static closed-class lookups, large morphological lexica, and neural disambiguators to maximize parsing accuracy on noisy historical texts.

---

## **30 Content**

**Synthesis: What Deterministic Pipelines Deliver and Where They Stop**

Today’s deterministic experiments demonstrate the immense power and clear boundaries of automated morphological tagging. In seconds, deterministic and statistical pipelines can parse thousands of lines of classical text, assigning lemmas, POS tags, and dependency structures that match human ground truth with 90–95% accuracy on standardized prose.

However, your benchmarking also exposed the rigid boundaries of deterministic software:

- Rule-based engines cannot disambiguate homophony without statistical context.
- Statistical taggers falter when confronted with historical itacisms, uncontracted Homeric forms, and manuscript orthographic noise.
- Dependency parsers struggle with the non-projective hyperbaton of classical poetry.

These limitations define the motivation for Friday’s lesson (Lesson 8.3). On Friday, you will evaluate Large Language Models (LLMs) and deep transformer architectures (GreBERTa, PhilBERTa, GPT-4), testing whether generative AI can resolve the semantic and orthographic ambiguities that deterministic tools leave behind—and measuring the precision-recall trade-offs of artificial intelligence in classical philology.

By completing today's deterministic benchmarking, you have acquired the quantitative baseline necessary to critically evaluate whether modern generative models represent a genuine breakthrough or merely an expensive, less predictable alternative to structured pipelines.

**Takeaway:** Deterministic pipelines deliver rapid, scalable annotation for standard texts, but orthographic noise and complex syntax require advanced neural architectures or human intervention.

---

## References

Bawden, R., Clérice, T., Glaise, A., Pinche, A., & Smith, D. (2026). *Pre-editorial normalization for automatically transcribed medieval manuscripts in Old French and Latin* (arXiv:2602.13905). https://arxiv.org/abs/2602.13905

Burns, P. J. (2023). *Updating LatinCy XPOS Tags*. Exploratory Philology. https://exploratoryphilology.org/posts/latincy-xpos-tags/

Crane, G. (1991). Generating and parsing Classical Greek. *Literary and Linguistic Computing*, 6(4), 243–245.

Haug, D. T. T., & Jøhndal, M. (2008). Creating a parallel treebank of the Old Indo-European Bible translations (PROIEL). In *Proceedings of the Second Workshop on Language Technology for Cultural Heritage Data (LaTeCH 2008)*, 27–34.

Johnson, K. P., Verma, P., & Gorman, K. (2021). The Classical Language Toolkit: An NLP framework for pre-modern languages. In *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL 2021)*, 20–29.

Schmid, H. (1994). Probabilistic part-of-speech tagging using decision trees. In *Proceedings of the International Conference on New Methods in Language Processing*, 44–49.

Swaelens, C., De Vos, I., & Lefever, E. (2023). Linguistic annotation of Byzantine book epigrams. *Language Resources and Evaluation*, 57(3), 1125–1152.

Swaelens, C., De Vos, I., & Lefever, E. (2024). Lemmatisation of medieval Greek: Against the limits of transformer's capabilities? In *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*, 899–908.

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/

Vatri, A., & McGillivray, B. (2020). Lemmatization for Ancient Greek: An experimental assessment of the state of the art. *Journal of Greek Linguistics*, 20(2), 179–196.
