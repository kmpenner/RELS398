# Lesson 12.2 — Deterministic Intertextual Discovery and Linked Web Annotation

*RELS 398 / ENGL 398 · Topic 12: Commentary · Meeting #32 (Wed Nov 25)*

***Step 2 of the three-step cycle: deterministic.** Today you apply algorithmic text reuse detection (Tesserae frequency-weighted n-gram scoring) and formalize annotations via the W3C Web Annotation Data Model (JSON-LD, selectors, motivations, and Hypothes.is linking), measuring algorithmic recall and precision against Tuesday's manual reference.*

---

## **01 Content**

**The Computational Turn in Intertextual Scholarship**

Yesterday, in Lesson 12.1, you drafted scholarly commentary notes by hand. You experienced firsthand the meticulous, labor-intensive nature of manual philology: reading a passage, recognizing potential literary allusions, consulting physical lexica and concordances, verifying citations, and formalizing the results in TEI stand-off XML. That manual effort produced a rich, nuanced ground truth, but it also exposed the fundamental constraint of traditional scholarship: human memory and reading speed cannot scale to massive corpora (Coffee et al., 2012).

In classical and medieval studies, the volume of surviving literature quickly overwhelms manual recall. The Latin corpus preserved in the *Patrologia Latina* spans 221 volumes and tens of millions of words; the ancient Greek corpus in the *Thesaurus Linguae Graecae* exceeds 110 million words. When an author composed a text in antiquity or the Middle Ages, they drew upon a vast canon of poetry, philosophy, scripture, and liturgy. A human scholar, no matter how erudite, cannot hold millions of lines of verse simultaneously in active memory (Tafdrup et al., 2026).

Consequently, manual intertextual commentary historically suffered from severe canonical bias: scholars recognized allusions to famous, heavily anthologized works (such as Homer's *Iliad* or Vergil's *Aeneid*) while completely overlooking pervasive verbal borrowing from obscure technical treatises, fragmentary epics, or minor poets (Coffee et al., 2012).

The computational turn in textual scholarship addresses this limitation through deterministic text-reuse algorithms. By modeling texts as machine-readable sequences of linguistic tokens, algorithms can scan hundreds of thousands of lines of verse in seconds, systematically detecting shared phrases, formulaic repetitions, and latent literary allusions across entire literary traditions (Coffee et al., 2012).

**Vocabulary.** *Intertextuality* — the relational interdependence of literary texts, whereby a work incorporates, echoes, or transforms preceding texts. *Text reuse* — the verbatim or near-verbatim reappearance of text passages across different documents or authors. *Canonical bias* — the tendency of scholars to search for and identify allusions only in famous, highly visible works.

**Takeaway:** Deterministic algorithms eliminate human memory bottlenecks and canonical bias by scanning massive historical corpora systematically for textual reuse.

---

## **02 Content**

**The Mechanics of Text Reuse: Lexical, Syntactic, and Thematic**

Before deploying an algorithm to find intertextual connections, an editor must understand the multi-dimensional mechanics of how authors reuse text. Literary borrowing is not a monolithic phenomenon; it operates along a spectrum ranging from strict verbatim copying to subtle conceptual echo (Coffee et al., 2012).

Computational philology categorizes text reuse into four distinct operational tiers:

| Text Reuse Tier | Structural Characteristic | Computational Detectability | Primary Algorithmic Mechanism |
| --- | --- | --- | --- |
| Verbatim Repetition | Identical sequences of surface word forms | Extremely High | Exact string matching, n-gram hashing |
| Morphosyntactic Reuse | Shared lexical roots with inflected variation | High | Lemmatized n-gram matching, bag-of-words |
| Syntactic / Structural Parallel | Identical grammatical patterns with different words | Moderate | Dependency parse tree alignment, POS sequences |
| Semantic / Thematic Allusion | Shared conceptual motifs with disparate vocabulary | Low for Deterministic | Neural vector embeddings, transformer models |

Deterministic algorithms operate primarily on the first two tiers: verbatim repetition and morphosyntactic reuse. In inflected historical languages like ancient Greek and classical Latin, surface word forms constantly change according to grammatical case, number, tense, and mood. If Vergil writes *arma virumque cano* ("I sing of arms and the man") in the accusative singular, and a later poet alludes to the passage using the ablative *armis*, an exact string-matching program will fail entirely (Coffee et al., 2012).

To capture authentic literary borrowing, deterministic algorithms must abstract surface characters into dictionary headwords (**lemmas**) and evaluate the statistical probability that two texts share an unusual combination of words purely by chance (Coffee et al., 2012).

**Vocabulary.** *Surface form* — the exact orthographic string of a word as it appears written in a text. *Inflection* — the modification of a word to express grammatical categories such as tense, case, voice, or number. *Bag-of-words* — a computational text representation that models a passage as an unordered collection of words.

**Takeaway:** Deterministic intertextual discovery requires abstracting inflected surface words into standardized lemmas to detect shared vocabulary across grammatical variations.

---

## **03 Content**

**The Tesserae Project: Architecture and Principles**

The premier deterministic engine for classical intertextual discovery is the **Tesserae Project**, developed at the University at Buffalo by Neil Coffee and an interdisciplinary team of classicists and computer scientists (Coffee et al., 2012).

Tesserae was designed to transform the discovery of literary allusions in Latin and ancient Greek poetry from a subjective art into a systematic, reproducible empirical science. The project takes its name from the Latin *tessera*—the small mosaic tile that forms part of a larger artistic pattern (Coffee et al., 2012).

The core architecture of Tesserae relies on a two-stage discovery pipeline:

| Pipeline Stage | Computational Operation | Primary Technical Function |
| --- | --- | --- |
| Stage 1: Candidate Extraction | Lemmatized cross-corpus search | Scans source and target corpora to find all passage pairs sharing two or more lemmas |
| Stage 2: Heuristic Scoring | Frequency-weighted density calculation | Evaluates candidate pairs using TF-IDF and distance metrics to rank significant allusions |

Rather than treating every shared word as equally important, Tesserae operates on a fundamental philological insight: *rare words placed in close syntactic proximity carry a vastly higher probability of intentional authorial allusion than common words spread far apart* (Coffee et al., 2012).

If two poetic passages share the common conjunction *et* ("and") and the preposition *in* ("in"), the connection is statistically meaningless. But if two passages share the rare noun *pelagus* ("open sea") and the rare verb *despicio* ("to look down upon from above") within a span of three words, the likelihood of a deliberate literary allusion is extraordinarily high (Coffee et al., 2012).

**Vocabulary.** *Tesserae* — an open-source computational tool for discovering intertextual parallels across classical Greek and Latin corpora. *Inverted index* — a database data structure mapping words to their exact storage locations across a document corpus. *Candidate pair* — a pair of passages from two different texts that satisfy minimum lexical overlap criteria.

**Takeaway:** Tesserae discovers classical allusions by identifying pairs of texts that share rare lemmas clustered in close syntactic proximity.

---

## **04 Content**

**Preprocessing for Intertextual Matching**

Before Tesserae can compare two literary works, the raw textual transcriptions must undergo rigorous preprocessing. Raw manuscript transcriptions contain orthographic anomalies, editorial punctuation, capital letters, and complex formatting that would blind an algorithmic comparison (Coffee et al., 2012).

The preprocessing pipeline executes four mandatory transformations:

| Preprocessing Step | Transformation Applied | Example Input | Example Output |
| --- | --- | --- | --- |
| 1. Tokenization & Case Normalization | Converts continuous text to lowercase tokens; strips punctuation | `Arma virumque cano, Troiae...` | `["arma", "virumque", "cano", "troiae"]` |
| 2. Enclitic Resolution | Separates attached enclitics into distinct tokens | `virumque` | `["virum", "que"]` |
| 3. Morphological Lemmatization | Maps inflected surface forms to dictionary lemmas | `cano` (verb) | `cano` (lemma) |
| 4. Stopword Classification | Identifies and flags high-frequency function words | `que`, `in`, `et`, `non` | Classified as stopwords |

In classical Latin, enclitics like *-que* ("and"), *-ve* ("or"), and *-ne* (interrogative particle) attach directly to the preceding word without a space. If *virumque* is not split into *virum* and *que*, the word *virum* will fail to match a parallel occurrence of *virum* in another text. Tesserae employs specialized morphological rule-parsers to detach enclitics prior to indexing (Coffee et al., 2012).

Once tokenized and decomposed, every word is mapped to its dictionary lemma using morphological databases such as the Perseus Morpheus engine or the Classical Language Toolkit (CLTK) (Lesson 8.1). The entire corpus is then indexed into an inverted table mapping every lemma to its exact CTS URN or line coordinates (Blackwell & Smith, 2014).

**Vocabulary.** *Enclitic* — a grammatically dependent word that attaches phonologically and orthographically to the preceding word. *Lemmatization* — the algorithmic process of grouping together inflected forms of a word so they can be analyzed as a single item. *Stopword* — a high-frequency function word filtered out or downweighted during information retrieval.

**Takeaway:** Textual preprocessing strips punctuation, separates enclitics, and resolves inflected words to lemmas to prepare corpora for algorithmic cross-comparison.

---

## **05 Content**

**The Tesserae Scoring Metric: Frequency and Density**

Once candidate passage pairs sharing two or more lemmas are extracted, Tesserae applies a sophisticated heuristic scoring formula. Without a scoring metric, an automated search between two epic poems generates tens of thousands of meaningless matches, creating massive noise that exhausts human readers (Coffee et al., 2012).

The Tesserae score ($S$) is calculated using a mathematical formula that balances **lexical rarity** against **syntactic phrase density**:

$$S = \ln \left( \frac{\sum_{i=1}^{k} \left( \frac{1}{f_T(w_i)} + \frac{1}{f_S(w_i)} \right)}{d_T + d_S} \right)$$

Where:

- $k$ represents the number of shared matching lemmas between the target passage ($T$) and the source passage ($S$).
- $f_T(w_i)$ is the corpus-wide frequency of the matching lemma $w_i$ in the target text.
- $f_S(w_i)$ is the corpus-wide frequency of the matching lemma $w_i$ in the source text.
- $d_T$ is the word-distance between the matching lemmas in the target passage.
- $d_S$ is the word-distance between the matching lemmas in the source passage.

The numerator calculates the combined rarity of the shared words: as word frequency ($f$) decreases, the reciprocal ($1/f$) increases exponentially. The denominator calculates the total syntactic spread: as the words are spaced further apart, the denominator increases, depressing the overall score (Coffee et al., 2012).

Taking the natural logarithm ($\ln$) scales the final output into an intuitive numerical range (typically from 2 to 10). A score of 2 or 3 represents weak, common verbal overlap; a score of 7, 8, or 9 represents an extraordinary concentration of rare words in tight proximity, signaling a highly probable authorial allusion (Coffee et al., 2012).

**Vocabulary.** *Scoring metric* — a mathematical function that assigns a quantitative value to an item to rank its relevance or quality. *Phrase density* — the spatial concentration or proximity of matching tokens within a given text window. *Natural logarithm ($\ln$)* — the logarithm to the base $e$, used to scale exponential growth into linear distributions.

**Takeaway:** The Tesserae scoring metric assigns high numerical values to rare shared words clustered closely together, elevating significant allusions above background noise.

---

## **06 Content**

**Calculating Rarity: TF-IDF and Inverted Corpus Frequency**

The rarity component of the Tesserae metric adapts the principles of **Term Frequency-Inverse Document Frequency (TF-IDF)** from modern information retrieval (Coffee et al., 2012).

In natural language corpora, word distributions follow Zipf's Law: a small handful of grammatical function words (prepositions, conjunctions, pronouns) account for the vast majority of all word occurrences, while thousands of rich semantic words occur only a few times. If an algorithm treated all words equally, search results would be completely dominated by meaningless matches on common words like *et* or *qui* (Coffee et al., 2012).

| Lexical Category | Corpus Frequency Class | Example Latin Lemmas | Weight in Tesserae Numerator ($1/f$) | Evidentiary Value for Allusion |
| --- | --- | --- | --- | --- |
| High-Frequency Stopwords | > 1,000 occurrences | *et*, *sum*, *in*, *qui*, *hic* | Extremely Small (< 0.001) | Negligible |
| Mid-Frequency Vocabulary | 100 – 1,000 occurrences | *rex*, *bellum*, *ignis*, *mare* | Moderate (0.01 – 0.001) | Low unless paired with rare terms |
| Low-Frequency Vocabulary | 10 – 100 occurrences | *pelagus*, *despicio*, *ululo* | High (0.1 – 0.01) | Significant |
| Extremely Rare / Hapax | < 10 occurrences | *semianimis*, *cornipes* | Exceptionally Large (> 0.1) | Extremely High (Virtually Definitive) |

By computing the inverse frequency ($1/f$), Tesserae dynamically downweights common vocabulary without requiring an arbitrary hard-coded stopword list. A match sharing three moderately common words can still achieve a respectable score if those words are tightly packed, while a match sharing two extremely rare poetic compounds will immediately shoot to the top of the ranked results (Coffee et al., 2012).

This statistical weighting models the subconscious intuition of the expert human philologist, who instantly dismisses common grammatical connective tissue to focus on distinctive lexical signatures.

**Vocabulary.** *TF-IDF* — Term Frequency-Inverse Document Frequency; a numerical statistic reflecting how important a word is to a document within a corpus. *Zipf's Law* — an empirical law stating that the frequency of any word is inversely proportional to its rank in the frequency table. *Lexical signature* — a distinctive combination of rare words characteristic of a specific author or passage.

**Takeaway:** Inverted frequency weighting computationally mirrors human philological intuition by suppressing high-frequency function words and elevating distinctive lexical signatures.

---

## **07 Content**

**Calculating Phrase Density: Distance-Based Decay Functions**

The second critical component of the Tesserae metric is **phrase density**—the spatial distance separating matching words within the source and target passages (Coffee et al., 2012).

When an author alludes to a poetic predecessor, they typically reproduce the distinctive words within a single metrical line, distich, or compact sentence. If an author uses one rare word in line 5 and another in line 120, the co-occurrence is far more likely to be coincidental than if both words appear together in line 5 (Coffee et al., 2012).

Tesserae quantifies phrase density by measuring the minimum token distance ($d$) between the matching lemmas in both passages:

| Distance Scenario | Target Phrase Layout | Source Phrase Layout | Total Distance ($d_T + d_S$) | Impact on Score |
| --- | --- | --- | --- | --- |
| Adjacent Tokens | `[w1] [w2]` ($d_T = 1$) | `[w1] [w2]` ($d_S = 1$) | 2 | Minimal divisor; maximum score boost |
| Single Verse Line | `[w1] ... [w2]` ($d_T = 4$) | `[w1] ... [w2]` ($d_S = 5$) | 9 | Moderate divisor; strong score |
| Cross-Stanza Spread | `[w1] ... (15 words) ... [w2]` ($d_T = 15$) | `[w1] ... (20 words) ... [w2]` ($d_S = 20$) | 35 | Large divisor; score significantly penalized |
| Distant Co-occurrence | `[w1] ... (50 words) ... [w2]` ($d_T = 50$) | `[w1] ... (60 words) ... [w2]` ($d_S = 60$) | 110 | Extreme divisor; score drops below threshold |

The distance divisor acts as a spatial penalty. By placing $d_T + d_S$ in the denominator, the algorithm ensures that allusions clustered in contiguous syntactic phrases receive a massive numerical premium over diffuse, scattered word co-occurrences (Coffee et al., 2012).

Furthermore, modern adaptations of the algorithm implement sliding window cutoffs (e.g., maximum distance of 20 or 30 words), completely pruning candidate pairs where the matching terms are too widely dispersed to represent an audible acoustic or rhetorical echo for historical listeners (Coffee et al., 2012).

**Vocabulary.** *Phrase density* — the compact grouping of matching words within a short textual window. *Distance divisor* — the denominator in the scoring formula that penalizes widely separated words. *Sliding window* — a constrained token range moved progressively across a text to analyze local contextual features.

**Takeaway:** Distance-based scoring penalizes diffuse word co-occurrences and rewards tight phrase density, capturing the compact acoustic nature of literary allusions.

---

## **08 Content**

**Tuning Precision and Recall in Tesserae**

When using deterministic tools like Tesserae, the digital editor must confront the fundamental trade-off of information retrieval: the balance between **precision** and **recall** (Coffee et al., 2012).

Precision measures the proportion of retrieved results that are authentic, interpretively meaningful allusions. Recall measures the proportion of all existing historical allusions that the algorithm successfully retrieves:

$$\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}$$

$$\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}$$

| Parameter Configuration | Score Threshold | Recall Impact | Precision Impact | Primary Editorial Consequence |
| --- | --- | --- | --- | --- |
| Permissive / Exploratory | Low (Score $\ge 3.0$) | Exceptionally High (~90%) | Very Low (~15%) | Floods editor with thousands of false positives; requires heavy manual filtering |
| Balanced / Standard | Medium (Score $\ge 5.5$) | Moderate (~65%) | Moderate (~50%) | Optimal balance for commentary drafting; surfaces major allusions with manageable noise |
| Restrictive / High-Confidence | High (Score $\ge 7.5$) | Low (~30%) | High (~85%) | Captures only near-verbatim borrowing and rare compounds; misses subtle allusions |

If an editor sets the score threshold too low, Tesserae acts like a strip-mining operation: it catches nearly every real allusion in the text (high recall), but buries the scholar under an avalanche of thousands of spurious grammatical coincidences (low precision) (Coffee et al., 2012).

Conversely, if the threshold is set too high, the output is exceptionally clean (high precision), but subtle poetic echoes, partial paraphrases, and two-word allusions are filtered out entirely (low recall).

The digital editor’s responsibility is to tune these parameters methodically, selecting thresholds appropriate to the genre, authorial style, and research questions of the edition (Coffee et al., 2012).

**Vocabulary.** *Precision* — the fraction of retrieved instances that are relevant. *Recall* — the fraction of relevant instances that are retrieved. *True positive* — a genuine literary allusion correctly identified by the algorithm. *False positive* — a coincidence of common words incorrectly flagged as an allusion.

**Takeaway:** Editors must deliberately calibrate score thresholds to balance high recall (capturing subtle echoes) against high precision (filtering out coincidental noise).

---

## **09 Content**

**What Deterministic Algorithms Catch**

Deterministic algorithms like Tesserae excel brilliantly at discovering specific types of textual reuse that frequently evade human memory (Coffee et al., 2012).

Because the algorithm evaluates the entire corpus uniformly without human fatigue or bias, it consistently surfaces:

| Text Reuse Category | Why Deterministic Algorithms Excel | Classical Literature Example |
| --- | --- | --- |
| Verbatim Quotations | Exact lexical matching across corpora | Early Christian apologies quoting Septuagint proof-texts verbatim |
| Formulaic Epic Repetitions | Identical metrical phrases across authors | Recurring Homeric or Vergilian dactylic hexameter half-lines |
| Shared Rare Compounds | Mathematically spikes the $1/f$ rarity score | Two poets sharing an exotic compound like *altisonus* ("high-sounding") |
| Obscure Sub-Canonical Borrowings | Algorithm searches non-canonical authors equally | Lucan echoing minor Hellenistic astronomical treatises rather than Vergil |

In an extensive empirical benchmark of Latin hexameter poetry, Coffee et al. (2012) demonstrated that Tesserae discovered dozens of verified literary allusions in Vergil, Ovid, and Lucan that had never been recorded in two centuries of printed commentary. Human commentators had missed these connections simply because the source passages were located in obscure, rarely read authors.

Furthermore, deterministic matching provides completely objective, reproducible empirical evidence: the shared lemmas, their exact line locations, and their mathematical frequency scores are transparently recorded, eliminating subjective hand-waving in literary debates (Coffee et al., 2012).

**Vocabulary.** *Formulaic repetition* — the standardized repetition of set phrases, epithets, or half-lines characteristic of oral and epic poetry. *Sub-canonical author* — a historical author not included in the traditional literary canon. *Reproducibility* — the capacity of an experiment or computational procedure to be replicated exactly by other researchers.

**Takeaway:** Deterministic tools excel at surfacing verbatim loans, formulaic repetitions, and obscure borrowings from sub-canonical literature that human readers miss.

---

## **10 Content**

**What Deterministic Algorithms Miss**

Despite their extraordinary processing power, deterministic algorithms suffer from fundamental hermeneutic blind spots. Because Tesserae relies strictly on lexical matching (shared lemmas), it is completely blind to any form of literary allusion that does not share surface vocabulary (Coffee et al., 2012).

Deterministic algorithms consistently fail to detect four major categories of intertextuality:

```
[ HERMENEUTIC PHENOMENA INVISIBLE TO DETERMINISTIC ALGORITHMS ]
  |
  +--> 1. Synonymic Substitution (Expressing the identical poetic image using different words)
  |
  +--> 2. Thematic & Structural Parody (Mocking an epic battle schema in an elegiac love poem)
  |
  +--> 3. Cross-Linguistic Allusions (A Latin poet translating a Greek lyric poem into Latin)
  |
  +--> 4. Conceptual & Metaphorical Resonances (Shared philosophical frameworks without shared lemmas)
```

For example, in the opening line of Ovid’s *Amores* (1.1.1: *Arma gravi numero violentaque bella parabam / edere*), Ovid famously alludes to the opening of Vergil’s *Aeneid* (1.1: *Arma virumque cano*). While Tesserae detects the shared lemma *arma*, it completely misses the metapoetic irony: Ovid is parodying Vergil’s grand martial epic by preparing to write warfare poetry in dactylic hexameter, only to have Cupid steal a metrical foot to force him into writing elegiac love poetry (Coffee et al., 2012).

Similarly, when Catullus translates Sappho’s famous Greek lyric poem (Fragment 31: φαίνεταί μοι κῆνος ἴσος θέοισιν) into Latin hendecasyllabics (Poem 51: *Ille mi par esse deo videtur*), a monolingual lexical algorithm discovers zero shared lemmas because the languages are completely different (Coffee et al., 2012).

Deterministic algorithms detect *lexical overlap*; they do not understand *meaning, irony, or literary convention*.

**Vocabulary.** *Synonymic substitution* — alluding to a source text by replacing key words with semantic equivalents or synonyms. *Metapoetics* — poetry that reflects upon the nature and composition of poetry itself. *Cross-linguistic allusion* — an allusion that translates or adapts a passage from another language.

**Takeaway:** Deterministic algorithms are blind to synonymic substitutions, structural parodies, cross-linguistic translations, and thematic resonances that lack shared lemmas.

---

## **11 Content**

**Auditing Tesserae Output Against Tuesday's Manual Ground Truth**

Today’s comparative exercise bridges the manual work of Lesson 12.1 with algorithmic automation. You will run Tesserae across your Week 12 test passage and systematically audit the algorithmic results against your manual ground-truth notes (Coffee et al., 2012).

To perform a rigorous scholarly audit, construct a comparative evaluation matrix:

| Audit Dimension | Evaluation Criterion | Method of Verification |
| --- | --- | --- |
| True Positive Identification | Did Tesserae find the intertextual references you manually drafted in Lesson 12.1? | Check if manual citations appear in Tesserae ranked candidate list |
| False Positive Discovery Rate | How many high-scoring Tesserae candidates represent meaningless lexical coincidences? | Manually inspect all candidates with score $\ge 6.0$ for genuine literary relevance |
| False Negative Rate (Silence) | Did Tesserae miss any subtle or synonymic allusions you found by hand? | Analyze why missed manual allusions failed (e.g., lack of shared lemmas, stopword filtering) |
| Novel Discovery Yield | Did Tesserae surface any authentic literary parallels that you completely overlooked? | Philologically evaluate candidate matches from obscure or unconsidered authors |

In typical pedagogical benchmarks, students discover that Tesserae reproduces obvious, verbatim citations with high scores (8.0+), but generates numerous false positives on common narrative formulas (e.g., descriptions of morning or sacrifices sharing generic verbs) (Coffee et al., 2012).

Most importantly, students frequently discover at least one or two genuine, surprising parallels in obscure contemporary literature that they never would have found by hand. This audit demonstrates the true role of the computational algorithm: not to replace the human editor, but to serve as a high-powered **heuristic discovery engine** whose leads must be critically vetted by a human-in-the-loop (Tafdrup et al., 2026).

**Vocabulary.** *Audit matrix* — a structured grid used to evaluate the performance of an algorithm against a known reference standard. *Heuristic* — a practical problem-solving approach or rule-of-thumb that aids in discovery but does not guarantee optimal theoretical proof. *Human-in-the-loop (HITL)* — a system architecture where human judgment actively guides, verifies, and refines automated algorithmic outputs.

**Takeaway:** Auditing algorithmic output against manual ground truth reveals that algorithms function as powerful heuristic discovery engines requiring human critical vetting.

---

## **12 Content**

**Moving from Document-Internal Markup to Linked Open Annotations**

While TEI stand-off XML (Lesson 12.1) provides a robust architecture for internal document management, it remains fundamentally anchored to the single-document XML ecosystem. In the modern Semantic Web, digital editions cannot remain isolated XML files on local servers; they must participate in distributed, cross-institutional knowledge networks (Sanderson et al., 2017).

Consider the limitations of purely document-internal markup:

- **Interoperability Silos:** If Project A encodes commentary in TEI XML and Project B uses a relational SQL database, their commentary layers cannot interact or merge without complex custom converters.
- **Web-Native Annotation:** Modern readers consume editions in web browsers, PDF readers, and mobile applications where client-side JavaScript cannot natively manipulate large TEI XML trees.
- **Decoupled Ownership:** A scholar at University X may wish to publish a critical commentary on an edition hosted by University Y without needing write access to University Y’s source repository (Sanderson et al., 2017).

To solve these challenges, the World Wide Web Consortium (W3C) formalized the **W3C Web Annotation Data Model (WADM)** in 2017 (Sanderson et al., 2017).

The W3C standard externalizes commentary into standalone, web-native **Linked Open Data (LOD)** resources serialized in **JSON-LD**. Under this paradigm, an annotation is a first-class web citizen with its own global URI, capable of linking any digital commentary to any target document anywhere on the internet (Sanderson et al., 2017).

**Vocabulary.** *W3C Web Annotation Data Model (WADM)* — the official W3C Recommendation specifying a structured data model and ontology for web annotations. *JSON-LD* — JavaScript Object Notation for Linked Data; a lightweight syntax for encoding RDF graphs in JSON. *First-class citizen* — an entity that supports all operations generally available to other entities, such as having a persistent URI and independent addressability.

**Takeaway:** The W3C Web Annotation Data Model transforms commentary from document-internal XML into independent, web-native Linked Open Data graphs.

---

## **13 Content**

**The W3C Web Annotation Data Model**

The architecture of the W3C Web Annotation Data Model is built around a deceptively simple, highly expressive tripartite graph structure (Sanderson et al., 2017).

Every web annotation consists of three core components:

```
                      +-----------------------------+
                      |         Annotation          |
                      | (Metadata: Author, Date, ID)|
                      +-----------------------------+
                                     |
               +---------------------+---------------------+
               | hasBody                                   | hasTarget
               v                                           v
+-----------------------------+             +-----------------------------+
|            Body             |             |           Target            |
|  (The Commentary / Gloss)   |             | (The Historical Text Span)  |
+-----------------------------+             +-----------------------------+
```

1. **The Annotation:** The central node representing the act of annotating. It carries administrative and provenance metadata, including the creator, creation timestamp, software agents used, and the primary **motivation** for the annotation.
2. **The Body:** The content or resource that is being attached as an annotation. The body can be a textual commentary note, an external translation, an image, an audio recording, or a linked open data URI (such as a Pleiades gazetteer record).
3. **The Target:** The resource that is being annotated. The target specifies the document URI, and uses specialized **selectors** to pinpoint the exact passage, character range, image coordinate, or audio timestamp.

Crucially, an annotation can have multiple bodies (e.g., a textual note *and* a Pleiades URI) or multiple targets (e.g., linking a single commentary note simultaneously to both a Greek text and its Latin translation) (Sanderson et al., 2017).

This clean, relational separation ensures that annotations are completely decoupled from the underlying storage mechanism of the target document.

**Vocabulary.** *Body* — the payload or interpretive content of an annotation in the WADM. *Target* — the resource or specific region of a resource being annotated in the WADM. *Tripartite graph* — a network structure consisting of three distinct classes of interconnected nodes.

**Takeaway:** The W3C Web Annotation model structures commentary into three decoupled components: the Annotation metadata node, the interpretive Body, and the targeted Text.

---

## **14 Content**

**JSON-LD Serialization of Web Annotations**

The native serialization format for W3C Web Annotations is **JSON-LD** (JavaScript Object Notation for Linked Data) (Sanderson et al., 2017). JSON-LD combines the universal developer-friendly syntax of JSON with the formal semantic graph capabilities of RDF (Resource Description Framework).

A standard scholarly commentary note encoded in W3C JSON-LD follows this structure:

```json
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "id": "https://example.org/annotations/note-12-1",
  "type": "Annotation",
  "motivation": "commenting",
  "creator": {
    "id": "https://orcid.org/0000-0002-1825-0097",
    "name": "Ken M. Penner",
    "type": "Person"
  },
  "created": "2026-11-25T10:30:00Z",
  "body": {
    "type": "TextualBody",
    "value": "The verb ἐπαρρησιασάμεθα denotes bold civic speech in Athenian democracy, adapted here for courageous apostolic proclamation.",
    "format": "text/markdown",
    "language": "en"
  },
  "target": {
    "source": "https://example.org/editions/1thess/chapter2.html",
    "selector": {
      "type": "TextQuoteSelector",
      "exact": "ἐπαρρησιασάμεθα",
      "prefix": "ἀλλὰ προπαθόντες καὶ ὑβρισθέντες καθὼς οἴδατε ἐν Φιλίπποις ",
      "suffix": " ἐν τῷ θεῷ ἡμῶν"
    }
  }
}
```

Key JSON-LD properties include:

- `@context` — Points to the official W3C ontology defining the terms and relationships.
- `id` — The globally unique URI identifying this specific annotation instance.
- `type` — Declares the node as a formal `Annotation`.
- `motivation` — Declares the scholarly intent behind the annotation (e.g., `commenting`).
- `creator` — Provenance object identifying the author (ideally using an ORCID URI).
- `body` — Contains the textual commentary with format and language declarations.
- `target` — Identifies the base web document (`source`) and its anchoring mechanism (`selector`).

JSON-LD allows web applications to parse annotations effortlessly using standard JavaScript, while enabling semantic triplestores to ingest the data as pure RDF graphs (Sanderson et al., 2017).

**Vocabulary.** *JSON-LD* — a JSON-based format to serialize Linked Data. `@context` — the JSON-LD keyword defining the mapping from JSON keys to RDF ontology URIs. *ORCID* — Open Researcher and Contributor ID; a persistent digital identifier for scholars.

**Takeaway:** JSON-LD serializes W3C Web Annotations into standard web-native objects that combine developer simplicity with semantic RDF graph power.

---

## **15 Content**

**The Taxonomy of Scholarly Motivations in W3C WADM**

A major innovation of the W3C Web Annotation Data Model is the mandatory or strongly recommended `motivation` property (Sanderson et al., 2017).

In traditional web comments (such as social media threads), all annotations are treated as undifferentiated text blurbs. In scholarly editing, however, an annotation that corrects a typographical error performs a fundamentally different epistemic function than one that identifies an ancient place or provides an exegesis of a theological metaphor.

The W3C specification defines a controlled taxonomy of standard motivations:

| W3C Motivation | Scholarly Function | Digital Commentary Application |
| --- | --- | --- |
| `commenting` | Providing critical commentary or interpretation | Explicating theological themes, rhetorical figures, or historical context |
| `identifying` | Declaring the real-world identity of a named entity | Linking a toponym to Pleiades or a historical figure to VIAF/Wikidata |
| `linking` | Creating an active semantic bridge to another resource | Connecting a citation or allusion to its primary source passage |
| `classifying` | Assigning a taxonomic or ontological label | Tagging a clause with an `<interp>` rhetorical figure (e.g., *chiasmus*) |
| `editing` | Proposing a text-critical correction or emendation | Recording a variant reading or scribal correction in the apparatus |
| `describing` | Providing objective factual or physical metadata | Describing the physical paleography, ink color, or parchment tear |
| `highlighting` | Visually marking a passage for user attention | Emphasizing core vocabulary for language pedagogy |

By explicitly declaring motivations, digital edition platforms can programmatically sort and filter annotations. A student reader can configure their interface to show only `identifying` annotations (giving place names on a map) and `highlighting` annotations (scaffolding vocabulary), while hiding advanced `editing` apparatus notes (Sanderson et al., 2017).

**Vocabulary.** *Motivation* — the W3C property explicitly declaring the intent or reason why an annotation was created. *Semantic filtering* — querying and displaying data based on the declared meaning and intent of its attributes.

**Takeaway:** The W3C motivation taxonomy (`commenting`, `identifying`, `linking`, `classifying`) formally declares scholarly intent, enabling multi-layered interface filtering.

---

## **16 Content**

**Anchoring Challenges on the Dynamic Web**

While attaching an annotation inside an XML file is relatively straightforward using element IDs, anchoring annotations across the open, dynamic web presents immense technical hazards (Sanderson et al., 2017).

On the web, target documents are constantly changing:

- **CMS and Template Updates:** A university library redesigns its digital edition website, altering the HTML class names, `div` nesting, and CSS structure.
- **Dynamic JavaScript Rendering:** Single Page Applications (SPAs) dynamically inject text into the browser DOM at runtime without stable static HTML elements.
- **Document Revisions:** An editor fixes a typo in paragraph 1, shifting the character indices of every subsequent paragraph across the entire webpage.

```
THE WEB ANCHORING VULNERABILITY:
  [ Original Document ]                     [ Revised Document (Typo Fixed) ]
  "In the begining was the Word..."   -->   "In the beginning was the Word..."
   ^---- Anchor: Offset 7, Len 8             ^---- Offset 7 now matches "eginnin" (BROKEN!)
```

If an annotation client relies exclusively on **character offsets** (start: 500, end: 520) or **CSS/XPath selectors** (`/html/body/main/div[3]/p[2]`), the annotation will break ("orphan") the moment any structural or textual edit occurs upstream (Sanderson et al., 2017).

To ensure that scholarly commentary endures across website redesigns and text revisions, the W3C Web Annotation Data Model established a sophisticated suite of **resilient selectors** (Sanderson et al., 2017).

**Vocabulary.** *Orphaned annotation* — an annotation whose target anchor can no longer be resolved in the source document due to edits. *DOM (Document Object Model)* — the tree structure representation of an HTML document created by a web browser. *Dynamic rendering* — generating webpage content client-side using JavaScript rather than static HTML files.

**Takeaway:** Dynamic web environments cause brittle character offsets and DOM paths to break; resilient web commentary requires robust multi-layered selectors.

---

## **17 Content**

**Resilient Selectors: `TextQuoteSelector` and Context Windows**

The most resilient anchoring mechanism defined in the W3C specification is the **`TextQuoteSelector`** (Sanderson et al., 2017).

Rather than storing arbitrary numerical offsets, the `TextQuoteSelector` records the exact text string being annotated, flanked by an **Anchoring Context Window (ACW)** comprising a preceding `prefix` and a following `suffix`:

```json
"selector": {
  "type": "TextQuoteSelector",
  "exact": "ἐπαρρησιασάμεθα",
  "prefix": "ἀλλὰ προπαθόντες καὶ ὑβρισθέντες καθὼς οἴδατε ἐν Φιλίπποις ",
  "suffix": " ἐν τῷ θεῷ ἡμῶν λαλῆσαι"
}
```

The `TextQuoteSelector` operates via a three-part contextual algorithm:

1. `exact` — The specific textual substring targeted for commentary.
2. `prefix` — A snippet of text immediately preceding the target (typically 30–50 characters).
3. `suffix` — A snippet of text immediately following the target (typically 30–50 characters).

Why this architecture is exceptionally resilient:

- **Survives Document Restructuring:** Even if the entire HTML structure is rebuilt from scratch (moving the text into entirely new `div` or `table` tags), the browser can search the plain text stream for the `exact` string.
- **Disambiguates Identical Words:** If a common word (like *God* or *Caesar*) appears 50 times on a page, the `prefix` and `suffix` provide unique contextual triangulation, guaranteeing that the annotation re-attaches to the exact intended sentence.
- **Enables Fuzzy Recovery:** If an editor makes a minor typographical correction inside the passage, client software can use approximate string matching (Levenshtein distance) across the prefix-exact-suffix window to relocate and heal the anchor automatically (Sanderson et al., 2017).

**Vocabulary.** *TextQuoteSelector* — a W3C selector that identifies a text target using an exact string paired with prefix and suffix context strings. *Contextual triangulation* — using surrounding text strings to uniquely locate a target among identical word occurrences. *Fuzzy matching* — algorithmic string matching that tolerates minor misspellings or character edits.

**Takeaway:** The `TextQuoteSelector` ensures anchor survival across website redesigns by storing exact target strings bounded by prefix and suffix context windows.

---

## **18 Content**

**Positional Selectors: `TextPositionSelector` and Fragment Selectors**

While `TextQuoteSelector` provides maximum resilience against text edits, processing large corpora requires fast computational retrieval. To optimize performance, the W3C specification pairs quote selectors with **positional selectors** (Sanderson et al., 2017).

The **`TextPositionSelector`** records the absolute start and end character positions as Unicode code point offsets from the beginning of the text stream:

```json
"selector": {
  "type": "TextPositionSelector",
  "start": 1420,
  "end": 1436
}
```

For media resources (such as high-resolution IIIF manuscript images or audio recordings), the W3C model provides the **`FragmentSelector`**, conforming to W3C Media Fragments URI syntax:

```json
"selector": {
  "type": "FragmentSelector",
  "conformsTo": "http://www.w3.org/TR/media-frags/",
  "value": "xywh=160,240,800,600"
}
```

| Selector Type | Targeted Resource | Anchor Syntax | Primary Performance Advantage |
| --- | --- | --- | --- |
| `TextPositionSelector` | Plain text / HTML text | `start: 1420, end: 1436` | Instantaneous character extraction; zero search latency |
| `FragmentSelector` (Spatial) | IIIF Manuscript Image | `xywh=160,240,800,600` | Pinpoints exact bounding box on high-resolution manuscript image |
| `FragmentSelector` (Temporal) | Audio / Video Recording | `t=120,145` | Binds commentary to specific audio playback interval (seconds) |
| `XPathSelector` | XML / HTML Document | `//p[@n='2']/w[4]` | Directly addresses XML nodes in structured editing platforms |

By combining positional and media fragment selectors, a digital edition can link a single commentary note simultaneously to a word in a TEI transcription, an interactive bounding box on a IIIF manuscript image (Topic 3), and a timestamped recording of the text recited in reconstructed historical pronunciation (Sanderson et al., 2017).

**Vocabulary.** *TextPositionSelector* — a W3C selector recording start and end Unicode code point character offsets. *FragmentSelector* — a W3C selector targeting spatial bounding boxes or temporal intervals in media. *Media Fragments* — W3C standard for addressing sub-regions of images, audio, and video via URI syntax.

**Takeaway:** Positional and fragment selectors provide high-speed character indexing and multi-modal spatial anchoring to IIIF manuscript images.

---

## **19 Content**

**Composing Selector Chains for Maximum Durability**

In professional digital scholarly editions, an editor should never rely on a single selector mechanism. A production-grade web annotation uses a **Selector Chain** (or `Composite` / `List` selector), combining multiple selectors in a cascading fallback hierarchy (Sanderson et al., 2017).

The W3C specification models this using the `refinedBy` property or a composite selector list:

```json
"target": {
  "source": "https://example.org/editions/1thess/chapter2.html",
  "selector": {
    "type": "RangeSelector",
    "startSelector": {
      "type": "XPathSelector",
      "value": "//div[@id='ch2']/p[1]/span[@class='verse'][2]"
    },
    "refinedBy": {
      "type": "TextQuoteSelector",
      "exact": "ἐπαρρησιασάμεθα",
      "prefix": "καθὼς οἴδατε ἐν Φιλίπποις ",
      "suffix": " ἐν τῷ θεῷ ἡμῶν"
    }
  }
}
```

When a web annotation client attempts to render this annotation, it executes a prioritized resolution cascade:

| Cascade Priority | Selector Evaluated | Resolution Strategy | Fallback Condition |
| --- | --- | --- | --- |
| Priority 1 | `XPathSelector` / `RangeSelector` | Locates the specific verse `div` in the DOM tree | If DOM structure was refactored, proceed to Priority 2 |
| Priority 2 | `TextPositionSelector` | Jumps to the exact character offset coordinates | If character offset text does not match, proceed to Priority 3 |
| Priority 3 | `TextQuoteSelector` | Searches document for `exact` string flanked by `prefix`/`suffix` | If exact match fails, proceed to Priority 4 |
| Priority 4 | Fuzzy Heuristic Re-anchoring | Calculates approximate string distance across context window | Prompts editor for manual verification if ambiguous |

This multi-tiered selector cascade guarantees maximum durability: annotations load instantly via fast positional indexes under normal conditions, but gracefully fall back to resilient text-quote context matching whenever the underlying webpage undergoes structural updates (Sanderson et al., 2017).

**Vocabulary.** *Selector chain* — a compound W3C selector combining multiple selection strategies to establish robust fallback resolution. *Resolution cascade* — a prioritized sequence of fallback attempts executed by an annotation client to locate a target. *Graceful degradation* — the ability of a computer system to maintain functionality when certain components fail.

**Takeaway:** Selector chains combine fast DOM/positional lookups with resilient text-quote context matching to provide robust, fail-safe web anchoring.

---

## **20 Content**

**Collaborative Annotation with Recogito 2**

The practical power of the W3C Web Annotation Data Model is exemplified in **Recogito 2**, an open-source semantic annotation platform developed by Rainer Simon and the Pelagios Network (Simon et al., 2017).

Recogito was created to solve a major user-interface bottleneck in digital humanities: traditional XML encoding requires scholars to manually write complex "pointy-bracket" markup, which creates steep technical barriers for domain specialists. Recogito provides an intuitive, browser-based graphical user interface where scholars can highlight text spans or draw bounding boxes on IIIF manuscript images, and immediately link those selections to global authority files (Simon et al., 2017).

| Step | Annotation Phase | Technical Operations | Output / Standards Alignment |
| --- | --- | --- | --- |
| 1 | Ingest Primary Source | Ingest plain text, TEI XML, or IIIF manuscript manifests | IIIF Image & Presentation APIs |
| 2 | Interactive Selection | User highlights text spans or draws image bounding boxes | W3C Web Annotation Selectors |
| 3 | Authority Alignment | Matches toponyms to Pleiades/WHG, persons to VIAF/Wikidata | Linked Open Data URI Bodies |
| 4 | Semantic Graph Export | Outputs standard JSON-LD, RDF Turtle, and CSV edge lists | W3C WADM Graph Serializations |

Under the hood, Recogito operates entirely on W3C Web Annotation standards (Simon et al., 2017). When a user highlights the ancient city *Philippi* and selects the matching record from the Pleiades gazetteer, Recogito automatically generates a WADM JSON-LD annotation with `motivation: "identifying"`, anchoring the note via `TextQuoteSelector` and storing the Pleiades URI in the body.

Because Recogito natively exports W3C JSON-LD and RDF Turtle graphs, annotations created by an individual researcher can be ingested directly into external GIS mapping systems, network analysis platforms, or digital scholarly editions across the globe (Simon et al., 2017).

**Vocabulary.** *Recogito* — an open-source web platform for semantic annotation of text and images, developed by the Pelagios Network. *Pelagios Network* — an international digital humanities collective connecting historical geographic data across online resources. *Turtle (Terse RDF Triple Language)* — a compact, human-readable serialization format for RDF graphs.

**Takeaway:** Recogito 2 demonstrates how intuitive graphical interfaces can generate standards-compliant W3C Web Annotations aligned with global gazetteers.

---

## **21 Content**

**Semantic Annotation with Net7 Pundit**

While Recogito focuses heavily on geographic and prosopographical entity alignment, **Pundit**, developed by Net7 and the SemLib project, extends the W3C annotation model into advanced semantic knowledge graph creation (Grassi et al., 2013).

Pundit was designed as a browser-based semantic annotation extension that enables researchers to create structured, machine-readable scholarly assertions directly on live web pages and digital library repositories. Rather than simply highlighting text and attaching free-text notes, Pundit allows scholars to construct formal **RDF triples** (Subject $\rightarrow$ Predicate $\rightarrow$ Object) anchored to the text (Grassi et al., 2013).

```
+-------------------------------------------------------------------------+
| PUNDIT STRUCTURED SCHOLARLY ASSERTION MODEL                             |
+-------------------------------------------------------------------------+
| Subject (Text Span Target) : "ἐπαρρησιασάμεθα" (1 Thess 2:2)            |
| Predicate (Ontological Link) : <http://purl.org/spar/cito/citesAsEcho>    |
| Object (Linked Authority)  : <urn:cts:greekLit:tlg0527.tlg027:52.7>     |
+-------------------------------------------------------------------------+
```

Using Pundit, a classical commentator can select a text passage, choose a formal relationship from a controlled ontology (such as CiTO's `citesAsAuthority`, `critiques`, or `translates`), and select a target object from DBpedia, Wikidata, or an external library catalogue (Grassi et al., 2013).

Because Pundit outputs standard Open Annotation / W3C Linked Data, the resulting annotations do not remain trapped inside the commentary page. They can be ingested into institutional triplestores, enabling scholars to run complex SPARQL queries across hundreds of distributed digital editions simultaneously (Grassi et al., 2013).

**Vocabulary.** *Pundit* — an open-source semantic web annotation tool allowing users to build structured RDF triple annotations on web documents. *RDF triple* — a foundational data entity in the Semantic Web composed of a subject, predicate, and object. *SemLib* — the Semantic Digital Libraries project that pioneered early linked open annotation tools.

**Takeaway:** Net7 Pundit formalizes commentary into machine-readable RDF triples, bridging textual notes with global semantic knowledge graphs.

---

## **22 Content**

**Open Web Annotation in Practice: Hypothes.is**

The most widely adopted implementation of the W3C Web Annotation standard in modern digital scholarship and pedagogy is **Hypothes.is** (Sanderson et al., 2017).

Hypothes.is is an open-source, non-profit platform that provides a universal, client-side annotation layer over the entire web. Utilizing a lightweight browser extension or an embedded JavaScript snippet, Hypothes.is allows scholars, students, and reading groups to annotate any public webpage, digital critical edition, or online PDF document without requiring administrative access to the host server (Sanderson et al., 2017).

| Architectural Feature | Hypothes.is Implementation | Pedagogical / Scholarly Benefit |
| --- | --- | --- |
| Client-Side Injection | Injects sidebar overlay via `annotator.js` | Works over any static HTML edition or repository PDF |
| Standard Compliance | Fully implements W3C WADM in JSON-LD | Annotations are exportable and interoperable via REST API |
| Collaborative Groups | Public, private, and institutional group layers | Supports peer review, classroom seminars, and editorial teams |
| Multi-Layer Anchoring | Combines XPath, `TextPosition`, and `TextQuote` | Robust anchor persistence across website CMS updates |

In digital humanities workflows, Hypothes.is serves as a powerful collaborative commentary environment. An editorial team can deploy a draft digital edition as a lightweight static HTML site, create a private Hypothes.is group for peer review, and collaboratively author, critique, and refine commentary notes directly on the live webpage (Sanderson et al., 2017).

Furthermore, because Hypothes.is exposes a robust RESTful API, developers can write Python scripts to query the Hypothes.is API, extract student commentary notes in W3C JSON-LD, and automatically transform them into permanent TEI `<standOff>` XML files for formal archival publication (Sanderson et al., 2017).

**Vocabulary.** *Hypothes.is* — an open-source platform providing a standards-compliant collaborative annotation layer for the web. *Client-side injection* — adding functionality to a webpage dynamically in the user's browser using JavaScript. *REST API* — an Application Programming Interface adhering to representational state transfer principles for data exchange.

**Takeaway:** Hypothes.is provides an open, collaborative web annotation layer that implements W3C standards and connects directly to digital edition workflows via REST APIs.

---

## **23 Content**

**Case Study: DanteSources and Knowledge Graphs**

The **DanteSources** project, developed by Valentina Bartalesi, Carlo Meghini, and Daniele Metilli at the Italian National Research Council (ISTI-CNR) and the University of Pisa, represents a pinnacle in transforming literary commentary into formal linked knowledge graphs (Bartalesi et al., 2018).

For centuries, scholars studying Dante Alighieri’s *Divine Comedy*, *Convivio*, and *Monarchia* produced massive printed commentaries documenting Dante’s encyclopedic primary sources—the classical Latin poets, Aristotle, Christian theologians, and Islamic philosophers whom Dante quotes, echoes, or debates. However, this vast repository of knowledge remained locked in unstructured natural language prose, making it impossible to perform macro-analysis or quantitative querying of Dante’s intellectual influences (Bartalesi et al., 2018).

```
DANTESOURCES INTEGRATED ONTOLOGY STACK:
+-------------------------------------------------------------------------+
| FRBRoo / LRMoo (Functional Requirements for Bibliographic Records)      |
| -> Models Dante's works, expressions, and physical manuscript editions  |
+-------------------------------------------------------------------------+
| DoCO (Document Components Ontology)                                     |
| -> Models the internal structural hierarchy (Canto, Stanza, Line)       |
+-------------------------------------------------------------------------+
| CiTO (Citation Typing Ontology)                                         |
| -> Categorizes the citation relationship (citesAsAuthority, refutes...) |
+-------------------------------------------------------------------------+
```

To structure this knowledge, Bartalesi et al. (2018) developed an integrated RDF/S ontology combining **FRBRoo** (for modeling literary works and expressions), **DoCO** (for modeling document structural components like cantos and lines), and **CiTO** (for characterizing citation types).

They developed semi-automated tools to extract thousands of scholarly references from authoritative commentaries, verified each citation with human domain experts, and mapped every reference to external DBpedia and VIAF authority URIs. The resulting digital library allows researchers to visualize Dante's intellectual universe, discovering which classical authors dominated specific cantos and tracing how Dante’s philosophical allegiances evolved across his lifetime (Bartalesi et al., 2018).

**Vocabulary.** *FRBRoo* — an object-oriented ontology combining the Functional Requirements for Bibliographic Records with CIDOC CRM. *DoCO* — Document Components Ontology; an ontology describing the structural parts of documents. *Knowledge graph* — a programmatic network of real-world entities and their semantic relationships stored as linked data.

**Takeaway:** DanteSources illustrates how integrating formal ontologies (FRBRoo, DoCO, CiTO) transforms traditional narrative commentary into queryable knowledge graphs.

---

## **24 Content**

**SPARQL Querying of Intertextual Networks**

The ultimate payoff of formalizing scholarly commentary into Linked Open Data is the ability to execute complex, cross-corpus queries using **SPARQL** (SPARQL Protocol and RDF Query Language) (Bartalesi et al., 2018).

In a traditional printed edition or flat PDF, a researcher cannot easily answer relational questions such as: *"Find all instances where an early Christian author quotes an Old Testament prophet, but where the citation is explicitly filtered through a Hellenistic Jewish sapiential framework."* In an RDF triplestore, this becomes a straightforward SPARQL query:

```sparql
PREFIX cito: <http://purl.org/spar/cito/>
PREFIX doco: <http://purl.org/spar/doco/>
PREFIX oa:   <http://www.w3.org/ns/oa#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?canto ?line ?sourceWork ?authorName
WHERE {
  ?annotation a oa:Annotation ;
              oa:motivatedBy cito:citesAsExplicitCitation ;
              oa:hasTarget ?target ;
              oa:hasBody ?body .
              
  ?target doco:isContainedBy ?canto ;
          doco:hasLineNumber ?line .
          
  ?body cito:hasCitedWork ?sourceWork ;
        rdfs:label ?authorName .
        
  FILTER (CONTAINS(?authorName, "Aristotle"))
}
ORDER BY ?canto ?line
```

This query searches the entire knowledge graph for annotations with the motivation `citesAsExplicitCitation`, extracts the exact canto and line coordinates from the target document components, and retrieves all cited works attributed to Aristotle (Bartalesi et al., 2018).

SPARQL transforms digital editions from passive reading sites into computational research environments. Scholars can perform "distant reading" over thousands of commentary notes, generating interactive network graphs, heatmaps of literary influence, and diachronic visualizations of intellectual history (Bartalesi et al., 2018).

**Vocabulary.** *SPARQL* — the standard query language for retrieving and manipulating data stored in Resource Description Framework (RDF) format. *Distant reading* — computational analysis of large textual corpora without reading individual texts linearly. *Triplestore* — a specialized graph database optimized for storing and querying RDF triples.

**Takeaway:** SPARQL queries allow researchers to execute relational, distant-reading analyses across linked intertextual commentary networks.

---

## **25 Content**

**Hands-On Exercise: Running Tesserae on the Test Corpus**

Now you will execute a deterministic intertextual search on your course test corpus using the Tesserae algorithm. You will configure search parameters, process the target and source texts, and capture the candidate match output (Coffee et al., 2012).

Follow this step-by-step procedure:

| Step | Operation | Execution Command / Action | Output Artifact |
| --- | --- | --- | --- |
| 1 | Select Corpus Texts | Define Target text (e.g., *1 Thess 2*) and Source corpus (e.g., *LXX Prophets* or *Classical Verse*) | Ingested source files |
| 2 | Set Stoplist Parameters | Configure stoplist size (e.g., top 30 high-frequency words filtered) | Stopword configuration |
| 3 | Define Distance Window | Set maximum token distance cutoff ($d \le 20$ words) | Spatial window parameter |
| 4 | Run Lemmatized Search | Execute Tesserae cross-matching algorithm | Raw candidate pair list |
| 5 | Extract Ranked Scores | Sort candidate results by frequency-weighted score ($S \ge 5.0$) | Scored matches table |

When running Tesserae, pay close attention to the impact of lemmatization: verify that inflected verbal forms (such as Greek aorist forms or Latin perfects) are correctly aligned with their base dictionary headwords (Coffee et al., 2012).

Inspect the top 10 highest-scoring candidates returned by the algorithm. Note the exact lemmas shared, the token distances in both passages, and the numerical score calculated.

**Vocabulary.** *Target text* — the primary text under analysis whose allusions are being investigated. *Source corpus* — the broader library of antecedent literature searched for potential model texts. *Score cutoff* — the minimum numerical score required for a candidate match to be included in results.

**Takeaway:** Running Tesserae with configured stoplists and distance cutoffs generates a scored, ranked list of candidate intertextual matches.

---

## **26 Content**

**Hands-On Exercise: Scoring and Filtering Deterministic Matches**

With your raw Tesserae results generated, conduct a systematic evaluation to calculate the precision and recall of the deterministic engine against your Lesson 12.1 manual ground truth (Coffee et al., 2012).

Examine each candidate match in the output table and assign it to an audit category:

| Candidate Rank | Target Tokens | Source Passage | Tesserae Score | Manual Ground-Truth Match? | Audit Classification |
| --- | --- | --- | --- | --- | --- |
| 1 | `#w22-#w25` (εὐαγγέλιον θεοῦ) | LXX Isa 52:7 | 8.4 | Yes (Found in 12.1) | **True Positive** |
| 2 | `#w1-#w3` (οἴδατε ἀδελφοί) | 1 Cor 15:58 | 6.8 | No (Generic Greeting) | **False Positive** (Formula) |
| 3 | `#w14` (ἐπαρρησιασάμεθα) | Josephus *AJ* 15.3 | 6.2 | No (Civic Speech) | **True Positive** (Novel Discovery) |
| 4 | `#w8` (Φιλίπποις) | Polybius 8.10 | 5.5 | No (Toponym only) | **False Positive** (Noise) |

Now compute the quantitative metrics for your deterministic run:

1. **Total Candidates Returned (Score $\ge 5.5$):** Count total matches above threshold.
2. **True Positives ($TP$):** Number of genuine, verified literary allusions.
3. **False Positives ($FP$):** Number of meaningless coincidences or generic formulas.
4. **False Negatives ($FN$):** Number of genuine allusions from your Lesson 12.1 manual notes that the algorithm failed to return.
5. **Precision:** Calculate $\frac{TP}{TP + FP}$.
6. **Recall:** Calculate $\frac{TP}{TP + FN}$.

Document these metrics in your lab notes. These figures provide the empirical baseline against which Friday's AI commentary generation will be compared (Tafdrup et al., 2026).

**Vocabulary.** *Quantitative evaluation* — assessing performance through numerical metrics like precision, recall, and F1-score. *Formulaic noise* — non-allusive matches caused by recurring genre conventions or standard conversational formulas.

**Takeaway:** Evaluating candidate matches against manual ground truth produces quantitative precision and recall metrics that benchmark algorithmic efficiency.

---

## **27 Content**

**Hands-On Exercise: Converting TEI Annotations to W3C JSON-LD**

Now you will bridge your TEI XML stand-off commentary from Lesson 12.1 into the global Linked Open Data cloud by converting your TEI `<note>` elements into W3C Web Annotation JSON-LD format (Sanderson et al., 2017).

Take one of your manual historical or intertextual notes from `03a_Lesson_12.1_Lesson_Content.md` and map its components to W3C JSON-LD:

```json
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "id": "https://example.org/annotations/12-2-philippi",
  "type": "Annotation",
  "motivation": "identifying",
  "creator": {
    "id": "https://orcid.org/0000-0002-1825-0097",
    "name": "Ken M. Penner",
    "type": "Person"
  },
  "created": "2026-11-25T14:00:00Z",
  "body": [
    {
      "type": "TextualBody",
      "value": "Philippi: Roman colony (colonia Iulia Augusta Philippensis) with ius Italicum; mistreatment violated Lex Julia.",
      "format": "text/markdown",
      "language": "en"
    },
    {
      "type": "SpecificResource",
      "source": "https://pleiades.stoa.org/places/501482",
      "purpose": "identifying"
    }
  ],
  "target": {
    "source": "https://example.org/editions/1thess2.html",
    "selector": [
      {
        "type": "TextPositionSelector",
        "start": 84,
        "end": 93
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
```

Verify that your JSON-LD object:

- Uses a multi-part `body` array containing both the textual commentary and the Pleiades LOD URI.
- Uses a multi-part `selector` array combining `TextPositionSelector` with a resilient `TextQuoteSelector`.
- Sets `motivation` to `identifying` (for historical entities) or `linking` (for intertextual references).

**Vocabulary.** *Multi-body annotation* — an annotation containing more than one body payload, such as combining textual prose with a semantic URI. *LOD conversion* — transforming document-internal markup into linked open data serializations.

**Takeaway:** Converting TEI stand-off notes into W3C JSON-LD creates multi-body, multi-selector web annotations ready for distributed semantic consumption.

---

## **28 Content**

**Hands-On Exercise: Deploying Annotations via Hypothes.is / Web Client**

To complete today’s technical implementation, you will deploy your structured annotations into a live web environment using the Hypothes.is API and client-side annotation interface (Sanderson et al., 2017).

Follow this deployment workflow:

| Step | Action | Technical Protocol | Verification Check |
| --- | --- | --- | --- |
| 1 | Create Hypothes.is Account | Register at `hypothes.is` and generate personal API token | API token secured |
| 2 | Open Web Edition | Load your published HTML edition in a browser with Hypothes.is active | Sidebar overlay loads |
| 3 | Attach Annotation | Highlight the targeted passage and paste your formatted commentary note | Visual highlight appears |
| 4 | Assign Semantic Tags | Add standardized tags: `#philology`, `#history`, `#intertext`, `#lod` | Tags indexed in sidebar |
| 5 | Fetch via API | Run a Python `curl` / `requests` script to query Hypothes.is REST API | JSON-LD payload retrieved |

To verify that your web annotations conform to W3C standards, execute a simple Python API retrieval:

```python
import requests

API_TOKEN = "your_token_here"
URL_TARGET = "https://example.org/editions/1thess2.html"

headers = {"Authorization": f"Bearer {API_TOKEN}"}
params = {"uri": URL_TARGET}

response = requests.get("https://api.hypothes.is/api/search", headers=headers, params=params)
data = response.json()

print(f"Retrieved {data['total']} live annotations from Hypothes.is")
for row in data["rows"]:
    print(f"Target: {row['target'][0]['selector']}")
    print(f"Text: {row['text']}\n")
```

This round-trip verification demonstrates that your commentary is live on the open web, decoupled from underlying servers, and accessible to any third-party research tool.

**Vocabulary.** *API token* — a secure credential used by software programs to authenticate requests to a web API. *Round-trip verification* — testing a workflow by publishing data to an external service and programmatically retrieving it back.

**Takeaway:** Deploying annotations to Hypothes.is and fetching them via REST APIs confirms live web interoperability and distributed accessibility.

---

## **29 Content**

**Comparing XML Stand-Off vs Linked Open Data Graphs**

Having built commentary in both TEI XML stand-off markup (Lesson 12.1) and W3C Web Annotation JSON-LD (Lesson 12.2), we must compare these two architectural paradigms. Both are foundational to digital scholarship, but they serve different phases of the editorial lifecycle (Sanderson et al., 2017; Schmidt, 2010).

| Architectural Dimension | TEI Stand-Off XML (P5 §17) | W3C Web Annotation (JSON-LD) |
| --- | --- | --- |
| Primary Design Philosophy | Document preservation and textual fidelity | Distributed web interoperability and open linking |
| Storage Environment | Local repository / Git version control | Distributed web servers, triplestores, REST APIs |
| Querying Technology | XPath, XQuery, XSLT | SPARQL, JSON REST APIs, graph algorithms |
| Anchor Mechanism | Document-internal `xml:id` and CTS URNs | Web URLs + `TextQuoteSelector` context chains |
| Collaboration Model | Asynchronous Git pull requests / XML validation | Real-time web overlays (Hypothes.is, Recogito) |
| Long-Term Archival Durability | Exceptional (Static, human-readable plain text) | High (Requires active web endpoints or triplestore) |

The optimal digital humanities workflow does not choose between these standards; it utilizes both in a complementary pipeline:

- **Authoring & Archival:** Editors author, collate, and preserve the authoritative commentary in **TEI stand-off XML** within a Git repository to ensure immutable version control and textual integrity (Lesson 12.1).
- **Publication & Dissemination:** Downstream build scripts automatically transform TEI stand-off notes into **W3C Web Annotation JSON-LD** files and RDF graphs, exposing them for web browsers, interactive maps, and global SPARQL endpoints (Lesson 12.2).

**Vocabulary.** *Editorial lifecycle* — the progression of a digital edition from transcription and collation to publication and long-term archiving. *Immutable* — unchanging over time or unable to be modified without creating a new version.

**Takeaway:** TEI stand-off XML provides optimal document archiving and version control, while W3C Web Annotations provide optimal web publication and linked open data integration.

---

## **30 Content**

**Synthesis: The Complementarity of Algorithmic Discovery and Formal Annotation**

Today’s lesson completed Step 2 of our three-step comparative cycle for Topic 12.

We have demonstrated that:

1. **Algorithmic Intertextual Discovery:** Deterministic text-reuse engines like Tesserae overcome human memory limits and canonical bias by scanning massive corpora using lemmatization, inverted frequency weighting (TF-IDF), and phrase density scoring (Coffee et al., 2012).
2. **Deterministic Limits:** Purely lexical algorithms excel at surfacing verbatim loans, formulaic phrases, and sub-canonical echoes, but are completely blind to synonymic substitutions, structural parodies, and thematic metaphors that lack shared lemmas (Coffee et al., 2012).
3. **Web-Native Annotation:** The W3C Web Annotation Data Model (WADM) externalizes commentary into web-native JSON-LD graphs, establishing a tripartite architecture (Annotation, Body, Target) with standardized motivations (Sanderson et al., 2017).
4. **Resilient Anchoring:** Complex selector chains combining `TextPositionSelector` and `TextQuoteSelector` ensure that web annotations survive CMS redesigns and document revisions (Sanderson et al., 2017).
5. **Linked Open Data Ecosystems:** Platforms like Recogito, Pundit, Hypothes.is, and DanteSources demonstrate how structured annotations transform isolated footnotes into queryable global knowledge networks (Bartalesi et al., 2018; Simon et al., 2017).

Deterministic tools provide the *leads*; formal web annotations provide the *distribution*. However, neither provides semantic reasoning or automated drafting of prose explanations.

**For Friday:** Review the research report on Generative AI and LLM commentary generation; examine the epistemological hazards of citation hallucination, historical anachronism, and automation bias (Draxler et al., 2024; Lou et al., 2025; Tafdrup et al., 2026).

**Takeaway:** Deterministic discovery algorithms and W3C linked web annotations empower digital editors to surface, structure, and publish intertextual networks across the global Semantic Web.

---

## References

Bartalesi, V., Meghini, C., & Metilli, D. (2018). *A web application for exploring primary sources: The DanteSources case study*. Italian National Research Council (ISTI-CNR). https://openportal.isti.cnr.it/data/2018/384308/2018_384308.preprint.pdf

Blackwell, C. W., & Smith, N. (2014). *The Canonical Text Services URN specification, version 2.0.rc.1*. Center for Hellenic Studies, Harvard University. https://cite-architecture.github.io/ctsurn_spec/

Coffee, N., Koenig, J.-P., Poornima, S., Forstall, C. W., Ossewaarde, R., & Jacobson, S. L. (2012). The Tesserae Project: Intertextual analysis of Latin poetry. *Literary and Linguistic Computing, 28*(2), 221–228. https://doi.org/10.1093/llc/fqs033

Draxler, F., Werner, A., Lehmann, F., Bauer, M., Hoppe, H. U., & Schmidt, A. (2024). The AI ghostwriter effect: When users do not perceive ownership of AI-generated text but self-declare as authors. *ACM Transactions on Computer-Human Interaction, 31*(2), 1–32. https://doi.org/10.1145/3637874

Grassi, M., Morbidoni, C., Nucci, M., Piazza, S., & Fundarò, M. (2013). Pundit: Semantically structured annotations for web contents and digital libraries. *CEUR Workshop Proceedings, 912*, 1–12. https://ceur-ws.org/Vol-912/paper4.pdf

Lou, M., Liu, Y., Zhao, K., & Chilton, L. B. (2025). *AnchoredAI: Contextual anchoring of AI comments improves writer agency and ownership*. arXiv. https://arxiv.org/abs/2509.16128

Sanderson, R., Ciccarese, P., & Young, B. (Eds.). (2017). *Web Annotation Data Model* (W3C Recommendation 23 February 2017). World Wide Web Consortium. https://www.w3.org/TR/annotation-model/

Schmidt, D. (2010). The inadequacy of embedded markup for cultural heritage texts. *Literary and Linguistic Computing, 25*(3), 337–356. https://doi.org/10.1093/llc/fqq007

Simon, R., Barker, E., Desoto, P., & Isaksen, L. (2017). *Linked data annotation without the pointy brackets: Introducing Recogito 2*. Pelagios Network. https://www.researchgate.net/publication/316865029_Linked_Data_Annotation_Without_the_Pointy_Brackets_Introducing_Recogito_2

Tafdrup, J., Bjerring-Hansen, J., & Hansen, J. N. (2026). Convergences. AI, editorial practice, and the Danish Digital Scholarly Edition of Grundtvig’s Works. *International Journal of Digital Humanities, 8*, 191–211. https://doi.org/10.1007/s42803-026-00125-z
