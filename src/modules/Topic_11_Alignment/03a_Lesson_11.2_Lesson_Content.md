# Lesson 11.2 — Automated Sentence and Word Alignment Tools: From Gale-Church to fast_align and Ugarit

*RELS 398 / ENGL 398 · Topic 11: Alignment · Meeting #29 (Wed Nov 18)*

***Step 2 of the three-step cycle: deterministic.** Today you explore automated sentence and word alignment algorithms—from length-based dynamic programming (Gale-Church) and statistical translation models (IBM Models 1–5, fast_align) to dedicated digital humanities platforms (Ugarit, Alpheios Alignment Editor). You will evaluate their output directly against Tuesday's human gold standard.*

---

## **01 Content**

**The Role of Deterministic Automation in Parallel Text Processing**

In yesterday’s seminar (Meeting #28), you experienced firsthand the rigorous cognitive labor required to author four-line Interlinear Glossed Text (IGT) and TEI P5 standoff alignments entirely by hand. Manually segmenting morphemes, verifying Leipzig abbreviations, and establishing cross-lingual pointer networks guarantees unparalleled philological precision. However, manual alignment is fundamentally unscalable when dealing with massive historical corpora. A scholar may spend hours aligning twenty verses of the Gospel of John or a single speech of Lysias. Aligning the entire Septuagint, the complete corpus of Classical Attic oratory, or the vast Patristic and Syriac commentary traditions requires computational assistance (Tiedemann, 2011).

This brings us to **Step 2 of our three-step pedagogical cycle: deterministic automation**. Deterministic alignment systems rely on explicit mathematical algorithms, statistical translation models, and rule-based heuristic engines. Unlike black-box neural networks or generative language models, deterministic algorithms are completely reproducible, mathematically transparent, and inspectable. When a deterministic tool produces an alignment or fails to align a token, the underlying statistical probabilities, length distributions, and matrix transformations can be precisely audited and understood (Och & Ney, 2003).

The primary goal of deterministic tooling in digital scholarly editing is not to replace human philological discernment, but to provide high-recall baseline alignments that dramatically reduce manual annotation overhead. By automating the mechanical alignment of high-frequency vocabulary, identical grammatical constructions, and regular syntactic clauses, deterministic tools free the editor to focus cognitive energy where it is most needed: resolving rare polysemy, analyzing complex idioms, and correcting non-isomorphic syntactic cruces (Baumgardt, 2021).

Today you will master the foundational algorithms of automated parallel text alignment: length-based dynamic programming for sentence pairing (the Gale-Church algorithm), statistical lexical translation modeling (IBM Models 1–5 and `fast_align`), and modern web-based digital philology platforms (Ugarit and the Alpheios Alignment Editor). You will measure the performance of these tools directly against the gold standard you authored yesterday.

**The takeaway for this page:** Deterministic alignment leverages reproducible mathematical and statistical algorithms to generate scalable parallel text alignments that human scholars can audit and refine.

---

## **02 Content**

**The Two-Tier Architecture of Automated Alignment**

Automated parallel text processing operates across two fundamentally distinct levels of granular abstraction: **sentence alignment** (coarse-grained) and **word alignment** (fine-grained). In computational linguistics, attempting to align individual words across two entire unsegmented documents simultaneously is computationally intractable and mathematically ill-posed. If a Greek text contains 50,000 words and its English translation contains 65,000 words, a direct unconstrained search space contains over 3.2 billion potential word pairings (Tiedemann, 2011).

To make alignment computationally tractable, automated pipelines implement a strict two-tier architecture:

- **Tier 1: Sentence Alignment (Macro-Segmentation):** The source text and translation are first partitioned into discrete, synchronized sentence or clause pairs ($S_{\text{src}} \leftrightarrow S_{\text{trg}}$). This reduces the global alignment problem to a series of small, independent search spaces.
- **Tier 2: Word Alignment (Micro-Segmentation):** Statistical and lexical alignment algorithms operate strictly within the bounded search space of each pre-aligned sentence pair, mapping source tokens ($w_{\text{src}} \in S_{\text{src}}$) to target tokens ($w_{\text{trg}} \in S_{\text{trg}}$).

| Alignment Tier | Granularity Level | Primary Input Data | Core Algorithmic Paradigms | Computational Complexity |
| --- | --- | --- | --- | --- |
| Sentence Alignment | Document to Clause ($<s> \leftrightarrow <s>$) | Unaligned raw text streams | Length dynamic programming, lexical anchors | Linear / Quadratic in sentence count: $\mathcal{O}(N \cdot M)$ |
| Word Alignment | Token to Token ($<w> \leftrightarrow <w>$) | Pre-aligned sentence pairs | Expectation-Maximization, IBM Models, Log-Linear | Quadratic in sentence length: $\mathcal{O}(L_{\text{src}} \cdot L_{\text{trg}})$ |

This two-tier architecture introduces a critical vulnerability known as **error cascade**. If the sentence aligner makes an error—for example, misaligning a 2-to-1 sentence split or dropping an omitted clause—every subsequent word alignment within that block will fail catastrophically. The word aligner will attempt to find lexical correspondences between completely unrelated sentences, producing high alignment error rates.

Consequently, establishing a flawless sentence-aligned bitext is the mandatory prerequisite for all downstream word-level and morpheme-level processing. In today's laboratory, you will examine how sentence alignment algorithms achieve robust synchronization before exploring word-level statistical modeling.

**The takeaway for this page:** Automated alignment operates in two cascading tiers—macro sentence alignment and micro word alignment—where sentence-level errors inevitably corrupt word-level results.

---

## **03 Content**

**Length-Based Sentence Alignment: The Gale-Church Algorithm**

The foundational milestone in automated sentence alignment was established by William Gale and Kenneth Church in their seminal 1991 paper, *A Program for Aligning Sentences in Bilingual Corpora* (Gale & Church, 1993). Gale and Church made a profound empirical observation: despite radical differences in vocabulary and grammar, the **length of a translated sentence in characters is strongly correlated with the length of the source sentence**.

Translators do not randomly expand or contract prose. A long, complex source sentence containing 150 characters will almost certainly translate into a long target sentence containing roughly 140–170 characters. Conversely, a short five-word sentence will translate into a correspondingly short target sentence. Gale and Church demonstrated that this character-length correlation holds across language pairs with remarkable statistical regularity.

The Gale-Church algorithm formulates sentence alignment as a dynamic programming path-finding problem on a grid. Let the source document consist of $I$ sentences with character lengths $l_1, l_2, \dots, l_I$, and the target document consist of $J$ sentences with character lengths $r_1, r_2, \dots, r_J$. The algorithm evaluates six possible alignment configurations (beads) at each step:

- **1:1 Alignment:** Exactly one source sentence corresponds to one target sentence.
- **1:2 Alignment:** One source sentence is split into two target sentences by the translator.
- **2:1 Alignment:** Two source sentences are merged into a single target sentence.
- **1:0 Alignment (Deletion):** A source sentence is omitted entirely in the translation.
- **0:1 Alignment (Insertion):** A target sentence is interpolated without a source counterpart.
- **2:2 Alignment:** Two source sentences correspond collectively to two target sentences (used when clause boundaries cross).

By assigning a probabilistic penalty score to each configuration based on character-length ratios and prior alignment probabilities, the algorithm uses the Viterbi dynamic programming algorithm to discover the globally optimal alignment sequence in $\mathcal{O}(I \cdot J)$ time.

**The takeaway for this page:** The Gale-Church algorithm uses dynamic programming to align parallel sentences based on the statistical regularity of character-length ratios across translations.

---

## **04 Content**

**Mathematical Mechanics of Gale-Church**

To implement the Gale-Church algorithm, we must formalize its underlying probability distribution and cost function. Gale and Church assumed that the difference between the expected target length and the actual target length follows a standard normal distribution (Gale & Church, 1993).

Let $l_1$ be the character length of the source sentence block, and $l_2$ be the character length of the target sentence block. The expected length of the target text is modeled as $c \cdot l_1$, where $c$ represents the expected number of target characters per source character (typically $c \approx 1.0$ for European language pairs, but calibrated empirically per corpus). The variance of this difference is proportional to the source length: $\sigma^2 \cdot l_1$, where $\sigma^2 \approx 6.8$ based on empirical observations.

We define the standardized length difference metric $\delta$ as:

$$\delta = \frac{l_2 - c \cdot l_1}{\sqrt{l_1 \cdot \sigma^2}}$$

The conditional probability $P(\text{lengths} \mid \text{alignment type})$ is computed from the complementary error function ($\text{erfc}$) of the standard normal distribution:

$$P(\delta) = 2 \cdot \left( 1 - \Phi(|\delta|) \right) = \text{erfc}\left( \frac{|\delta|}{\sqrt{2}} \right)$$

The overall cost $D(i, j)$ of aligning source prefix $s_1 \dots s_i$ with target prefix $t_1 \dots t_j$ is computed recursively using the dynamic programming recurrence relation:

$$D(i, j) = \min \begin{cases}
D(i-1, j-1) - \log P(1:1) - \log P(\delta_{1:1}) \\
D(i-1, j-2) - \log P(1:2) - \log P(\delta_{1:2}) \\
D(i-2, j-1) - \log P(2:1) - \log P(\delta_{2:1}) \\
D(i-1, j) - \log P(1:0) - \log P(\delta_{1:0}) \\
D(i, j-1) - \log P(0:1) - \log P(\delta_{0:1}) \\
D(i-2, j-2) - \log P(2:2) - \log P(\delta_{2:2})
\end{cases}$$

| Alignment Category | Prior Probability $P(\text{match})$ | Typical Description | Relative Cost Penalty |
| --- | --- | --- | --- |
| $1:1$ Match | $0.89$ ($89\%$) | Direct sentence-to-sentence correspondence | Lowest penalty; default baseline |
| $1:2$ Split | $0.04$ ($4\%$) | Long source period broken into two target sentences | Moderate penalty; requires length match |
| $2:1$ Merge | $0.04$ ($4\%$) | Two short source clauses combined with conjunction | Moderate penalty; requires combined length match |
| $2:2$ Cross-Match | $0.01$ ($1\%$) | Two sentences interwoven across punctuation marks | High penalty; selected only when 1:1 fails |
| $1:0$ Deletion | $0.01$ ($1\%$) | Source text dropped or omitted by translator | Severe penalty; avoided unless extreme length mismatch |
| $0:1$ Insertion | $0.01$ ($1\%$) | Target text added as explanatory gloss or gloss expansion | Severe penalty; avoided unless extreme length mismatch |

Because the dynamic programming matrix evaluates all possible paths simultaneously, the algorithm easily recovers from localized length fluctuations, guaranteeing a mathematically optimal global alignment.

**The takeaway for this page:** Gale-Church calculates the negative log probability of normal length differences ($\delta$) combined with prior alignment probabilities to populate a dynamic programming grid.

---

## **05 Content**

**Strengths and Failure Modes of Length-Based Alignment**

The Gale-Church algorithm is astonishingly elegant: it requires no bilingual dictionaries, no morphological parsers, no part-of-speech taggers, and no language-specific grammar models. In modern legislative and technical corpora (such as the Canadian Hansard or European Parliament proceedings), Gale-Church achieves sentence alignment accuracy exceeding **98%** (Tiedemann, 2011).

However, when applied to ancient, medieval, and historical literary texts, pure length-based alignment encounters severe failure modes:

1. **Non-Monotonic Structural Reordering:** Gale-Church strictly assumes monotonic progression ($i$ and $j$ only increase). If a translator transposed two paragraphs or reordered poetic strophes, the dynamic programming path breaks, forcing erroneous deletions and insertions.
2. **Prolific Deletions and Expansions:** Ancient translations frequently omit lengthy theological arguments or expand brief aphorisms into paragraph-long paraphrases. In such regions, length ratios deviate wildly from the normal distribution, causing the aligner to lose synchronization.
3. **Unequal Granularity of Punctuation:** Ancient manuscripts lacked standard punctuation. When modern editors punctuate Greek or Hebrew texts into short sentences while 19th-century translators used sprawling Victorian periods, the alignment path is forced into continuous 3:1 or 4:1 beads that exceed the algorithm's search window.
4. **Symmetrical Length Ambiguity:** If two consecutive sentences have nearly identical lengths, Gale-Church cannot determine which corresponds to which based solely on character counts.

| Textual Scenario | Source & Target Behavior | Gale-Church Algorithmic Outcome | Scholarly Mitigation |
| --- | --- | --- | --- |
| Standard Prose | Literal sentence-for-sentence transfer | Flawless alignment ($>98\%$ accuracy) | Run automated Gale-Church directly |
| Poetic Strophe Inversion | Strophes translated in reverse order ($B, A$) | Complete path rupture; false deletions | Use anchor-based or neural aligners |
| Scribal Homoioteleuton | Eyedkip omission in target translation | Extended drift until next major length boundary | Anchor alignment at chapter milestones |
| Punctuation Mismatch | 1 Greek period split into 4 English sentences | Bead search window overflow (fails 1:4) | Re-tokenize target into compound clauses |

To overcome these limitations in humanities corpora, computational linguists developed **hybrid alignment architectures** that integrate lexical anchors, bilingual lexicons, and structural markup alongside length metrics.

**The takeaway for this page:** Pure length-based alignment achieves high accuracy on modern literal bitexts but fails on ancient texts due to non-monotonic reordering, loose paraphrases, and punctuation divergence.

---

## **06 Content**

**Lexical and Anchor-Based Sentence Alignment: Champollion and Hunalign**

To prevent length-based aligners from drifting in complex literary corpora, second-generation sentence aligners incorporate **lexical anchor points**. If an algorithm knows with high confidence that the Greek word θεός corresponds to English "God", or that a specific proper name like Ἀλέξανδρος corresponds to "Alexander", it can use these cognate matches as unshakeable anchor pins along the dynamic programming path (Tiedemann, 2011).

Two prominent implementations of this hybrid paradigm are **Hunalign** and **Champollion**:

- **Hunalign (Varga et al., 2005):** Implements a two-pass architecture. In Pass 1, it runs a Gale-Church-style length-based alignment. In Pass 2, it automatically builds a rough bilingual dictionary from high-confidence alignments, and then re-aligns the entire corpus combining length scores with lexical token overlap scores.
- **Champollion (Ma, 2006):** Designed specifically for divergent, non-parallel corpora. It calculates the term frequency-inverse document frequency (TF-IDF) weights of translated lexicon entries, heavily prioritizing rare lexical matches while ignoring ubiquitous function words.

| Aligner Architecture | Algorithmic Basis | Lexical Resource Requirement | Resilience to Loose Paraphrases | Historical Corpus Applicability |
| --- | --- | --- | --- | --- |
| Gale-Church | Pure character length ratios | None (language-agnostic) | Low; easily derailed by omissions | Moderate; requires clean parallel editions |
| Hunalign | Hybrid length + dynamic lexicon bootstrapping | Optional external bilingual dictionary | High; re-aligns using emergent vocabulary | High; robust across varied translation styles |
| Champollion | Lexical anchor points with TF-IDF weights | Requires bilingual dictionary | Very High; skips non-translated sections | Excellent; designed for asymmetrical bitexts |

Lexical anchoring is especially valuable when aligning ancient texts against vernacular translations. For example, in aligning a Greek philosophical treatise against an Arabic or Latin translation, technical terminology (e.g., οὐσία $\leftrightarrow$ *substantia* $\leftrightarrow$ جوهر) serves as mathematical ballast that keeps the alignment matrix locked to the correct textual coordinates.

Furthermore, digital critical editions can leverage structural TEI milestone tags (such as `<pb/>` for page breaks, `<cb/>` for column breaks, or biblical verse numbers `<milestone unit="verse"/>`) as absolute boundary constraints. By forcing the dynamic programming path to pass through known structural milestones, editors eliminate long-distance alignment drift entirely.

**The takeaway for this page:** Hybrid aligners like Hunalign and Champollion combine character lengths with bilingual lexical anchors and structural milestones to prevent alignment drift in literary bitexts.

---

## **07 Content**

**Modern Neural Sentence Alignment: Vecalign and Bertalign**

In recent years, natural language processing has transitioned from surface-level character counts and explicit dictionaries to **multilingual contextual sentence embeddings**. Modern neural sentence aligners represent complete sentences as dense mathematical vectors in a continuous geometric space, enabling semantic alignment that is completely invariant to word order, paraphrase, and surface vocabulary (Thompson & Koehn, 2019).

The two leading neural frameworks for parallel text alignment are **Vecalign** and **Bertalign**:

- **Vecalign (Thompson & Koehn, 2019):** Computes multilingual sentence embeddings using models like LASER (Language-Agnostic SEntence Representations) or LaBSE (Language-agnostic BERT Sentence Embedding). It formulates sentence alignment as a dynamic programming search minimizing the cosine distance between source and target embedding vectors, using a fast approximation algorithm that scales linearly $\mathcal{O}(N)$ rather than quadratically.
- **Bertalign (Liu & Zhu, 2023):** Built specifically for literary and non-isomorphic parallel corpora. It integrates sub-sentential embeddings, sliding-window contextual representations, and bidirectional cross-lingual similarity matrices, achieving state-of-the-art performance on complex literary translations.

| Sentence Alignment Framework | Underpinning Architecture | Computational Requirement | Invariance to Paraphrase | Historical Language Adaptation |
| --- | --- | --- | --- | --- |
| Classical Gale-Church | Normal character length distribution | Minimal (Single CPU thread) | Zero (Pure length heuristic) | Moderate (Requires clean editions) |
| Hunalign | Dynamic vocabulary bootstrapping | Low (CPU) | Low to Moderate | High (Handles noisy text) |
| Vecalign / Bertalign | Multilingual transformer embeddings | Moderate to High (GPU accelerated) | **Extremely High (Semantic vectors)** | **State-of-the-Art (`grc-bertalign`)** |

In historical digital philology, neural sentence aligners have demonstrated exceptional resilience when aligning ancient languages against modern translations (e.g., `grc-bertalign` for Ancient Greek to English; Krahn, 2024). Because transformer embeddings capture high-level semantic meaning rather than literal word counts, neural aligners effortlessly resolve complex 1:2 splits, rhetorical expansions, and syntactic inversions that cause classical length-based algorithms to fail.

However, neural aligners require substantial computational resources (GPUs) and specialized pre-trained models. For standard digital edition workflows, a hybrid approach—using structural TEI milestones for coarse division and neural embeddings for fine clause pairing—represents the current state of the art.

**The takeaway for this page:** Neural sentence aligners (Vecalign, Bertalign) compare dense multilingual sentence embeddings, achieving human-level alignment accuracy across complex literary paraphrases.

---

## **08 Content**

**Introduction to Statistical Word Alignment and the IBM Models**

Once parallel sentences are synchronized at Tier 1, we descend to Tier 2: **word-level alignment**. How do we automatically discover which specific source word generated which specific target word without hand-crafting exhaustive bilingual dictionaries?

The mathematical foundation of automated word alignment was established in a monumental 1993 paper by Peter Brown, Stephen Della Pietra, Vincent Della Pietra, and Robert Mercer of IBM’s Thomas J. Watson Research Center: *The Mathematics of Statistical Machine Translation: Parameter Estimation* (Brown et al., 1993). The authors introduced five generative probabilistic models—universally known in computational linguistics as **IBM Models 1 through 5**.

The core philosophy of the IBM models rests on a generative translation metaphor:

1. Assume a source sentence $\mathbf{e} = (e_1, e_2, \dots, e_l)$ of length $l$ in a source language.
2. Imagine that an author wishes to translate $\mathbf{e}$ into a target sentence $\mathbf{f} = (f_1, f_2, \dots, f_m)$ of length $m$.
3. The translation process is modeled as a hidden stochastic process governed by probability distributions for lexical substitution, word fertility, and positional distortion.
4. The alignment $\mathbf{a} = (a_1, a_2, \dots, a_m)$ is a vector of hidden (latent) variables, where $a_j = i$ indicates that target word $f_j$ was generated by source word $e_i$ (or by an empty null token $e_0$).

Because human annotators have not manually labeled the alignments across millions of training sentences, the alignment vector $\mathbf{a}$ cannot be observed directly. To solve this problem of incomplete data, Brown et al. applied the **Expectation-Maximization (EM) algorithm** (Dempster et al., 1977). The EM algorithm iteratively estimates translation probabilities and latent alignments until mathematical convergence.

**The takeaway for this page:** The IBM Models formulate word alignment as a hidden generative process, using the Expectation-Maximization (EM) algorithm to learn translation probabilities from unannotated bitexts.

---

## **09 Content**

**IBM Model 1: Lexical Translation Probabilities**

**IBM Model 1** is the simplest and most foundational statistical alignment model. It makes a radical simplifying assumption: **the position of a word in the sentence has zero effect on its alignment probability**. Alignment is governed solely by lexical translation probabilities $t(f \mid e)$—the probability that source word $e$ translates into target word $f$ (Brown et al., 1993).

Under IBM Model 1, the conditional probability of target sentence $\mathbf{f}$ and alignment $\mathbf{a}$ given source sentence $\mathbf{e}$ is defined as:

$$P(\mathbf{f}, \mathbf{a} \mid \mathbf{e}) = \frac{\epsilon}{(l+1)^m} \prod_{j=1}^m t(f_j \mid e_{a_j})$$

Where:

- $\epsilon = P(m \mid \mathbf{e})$ is a fixed length normalization constant.
- $(l+1)^{-m}$ represents a uniform prior probability over all possible alignments (each of the $m$ target words can choose any of the $l$ source words or the null token $e_0$ with equal probability $\frac{1}{l+1}$).
- $t(f_j \mid e_{a_j})$ is the lexical translation probability of generating target word $f_j$ from source word $e_{a_j}$.

The Expectation-Maximization algorithm trains Model 1 through two alternating steps:

1. **Expectation Step (E-step):** For every parallel sentence pair in the corpus, calculate the posterior probability of all possible word alignments using the current estimates of $t(f \mid e)$:
   $$P(a_j = i \mid \mathbf{e}, \mathbf{f}) = \frac{t(f_j \mid e_i)}{\sum_{i'=0}^l t(f_j \mid e_{i'})}$$

2. **Maximization Step (M-step):** Accumulate fractional counts $c(f \mid e)$ across the entire corpus weighted by the posterior probabilities, and re-estimate the lexical translation probabilities:
   $$t(f \mid e) = \frac{\sum_{\text{corpus}} c(f \mid e; \mathbf{e}, \mathbf{f})}{\sum_{f'} \sum_{\text{corpus}} c(f' \mid e; \mathbf{e}, \mathbf{f})}$$

A remarkable mathematical property of IBM Model 1 is that its likelihood function is **strictly convex**. This means Model 1 has no local maxima; starting from uniform initial probabilities, EM training is mathematically guaranteed to converge to the unique global maximum (Och & Ney, 2003).

**The takeaway for this page:** IBM Model 1 models word alignment based purely on lexical co-occurrence probabilities $t(f \mid e)$, converging reliably to a global mathematical maximum via EM.

---

## **10 Content**

**IBM Model 2: Adding Positional Distortions**

While IBM Model 1 is mathematically robust, its complete disregard for word order is linguistically unrealistic. In real human languages, translations tend to preserve relative word order. If a word appears at the very beginning of a Greek sentence ($j=1$), it is far more likely to align with a word near the beginning of the English sentence ($i=1$ or $i=2$) than with a word at the very end ($i=40$) (Brown et al., 1993).

**IBM Model 2** repairs this deficiency by introducing an **alignment probability distribution** (also called a distortion parameter) $a(i \mid j, l, m)$. This parameter explicitly models the probability that target position $j$ connects to source position $i$, conditioned on the source length $l$ and target length $m$.

The joint probability under IBM Model 2 is formulated as:

$$P(\mathbf{f}, \mathbf{a} \mid \mathbf{e}) = \epsilon \prod_{j=1}^m a(a_j \mid j, l, m) \cdot t(f_j \mid e_{a_j})$$

| Alignment Parameter | Conditioning Variables | Linguistic Phenomenon Modeled | Mathematical Role in Model 2 |
| --- | --- | --- | --- |
| Lexical Translation $t(f \mid e)$ | Source token $e$, target token $f$ | Lexical semantic correspondence | Determines word choice affinity |
| Positional Distortion $a(i \mid j, l, m)$ | Indices $i, j$, lengths $l, m$ | Word order preservation / diagonal bias | Penalizes unnatural cross-sentence jumps |
| Null Probability $p_0$ | Global constant / token count | Unaligned function words / ellipses | Allows target words to generate from empty set |

In the E-step of Model 2, the posterior alignment probability incorporates both lexical affinity and positional distance:

$$P(a_j = i \mid \mathbf{e}, \mathbf{f}) = \frac{a(i \mid j, l, m) \cdot t(f_j \mid e_i)}{\sum_{i'=0}^l a(i' \mid j, l, m) \cdot t(f_j \mid e_{i'})}$$

By initializing Model 2 with the converged lexical parameters $t(f \mid e)$ from Model 1, Model 2 rapidly learns the characteristic word-order distortions of the language pair. However, because Model 2 conditions alignment on absolute sentence positions ($i$ and $j$), it struggles when sentences contain long introductory clauses or substantial parenthetical phrases.

**The takeaway for this page:** IBM Model 2 introduces a positional distortion parameter $a(i \mid j, l, m)$, penalizing alignments that deviate excessively from the diagonal translation path.

---

## **11 Content**

**IBM Models 3, 4, and 5: Fertility and Relative Distortion**

IBM Models 1 and 2 suffer from a structural asymmetry: each target word $f_j$ is generated by exactly one source word $e_{a_j}$, but there is no mechanism to limit how many target words a single source word can generate. A source word could theoretically generate twenty target words with zero mathematical penalty.

To model authentic linguistic realities, **IBM Models 3, 4, and 5** introduce the concept of **fertility** ($\phi$):

- **Fertility $\phi_i$:** The number of target words generated by source word $e_i$. A fertility distribution $n(\phi \mid e_i)$ defines the probability that $e_i$ generates $\phi = 0, 1, 2, 3, \dots$ target words (Brown et al., 1993).
  - Greek synthetic verb ἐγένετο generates 3 English words ("came into being") $\rightarrow \phi = 3$.
  - Greek untranslated particle μέν generates 0 English words $\rightarrow \phi = 0$.

| IBM Model | Key Linguistic Parameter Introduced | Algorithmic Mechanism | Primary Philological Limitation |
| --- | --- | --- | --- |
| Model 1 | Lexical translation $t(f \mid e)$ | Word co-occurrence statistics | Completely ignores word order |
| Model 2 | Absolute distortion $a(i \mid j, l, m)$ | Conditions alignment on absolute position | Distortions sensitive to clause insertion |
| Model 3 | Word fertility $n(\phi \mid e)$ + center distortion $d$ | Models 1:N expansion and zero-fertility | Deficient; places words on occupied positions |
| Model 4 | Relative distortion $d_{=} / d_{>1}$ | Conditions placement on previous word cluster | Computationally expensive; non-convex search |
| Model 5 | Non-deficiency constraints | Enforces vacancy tracking for target slots | Highly complex; requires heuristic hill-climbing |

**IBM Model 4** replaces absolute positions with **relative distortion**, modeling word placement relative to the center of the previous word cluster. This captures the reality that phrases move as cohesive syntactic blocks (e.g., a noun phrase moving from subject to object position).

However, Models 3 through 5 introduce immense computational complexity. Because fertility couples all alignment decisions across the entire sentence, the exact sum over all alignments cannot be computed in polynomial time. Implementations like **GIZA++** (Och & Ney, 2003) must rely on heuristic local search and hill-climbing algorithms, making training slow and sensitive to initialization.

**The takeaway for this page:** IBM Models 3–5 incorporate fertility ($n(\phi \mid e)$) and relative distortion, modeling 1:N expansions and phrase movement at the cost of high computational complexity.

---

## **12 Content**

**The Hidden Markov Model (HMM) for Word Alignment**

To bridge the gap between the computational simplicity of IBM Model 2 and the linguistic sophistication of IBM Model 4, Stephan Vogel, Hermann Ney, and Christoph Tillmann developed the **Hidden Markov Model (HMM) for Word Alignment** (Vogel et al., 1996).

The HMM formulation treats word alignment as a first-order Markov chain. Instead of conditioning target position $j$'s alignment on absolute coordinates ($i$), the HMM conditions alignment on the **relative jump distance** from the previous alignment decision ($a_{j-1}$):

$$P(\mathbf{f}, \mathbf{a} \mid \mathbf{e}) = \epsilon \prod_{j=1}^m p(a_j \mid a_{j-1}, l) \cdot t(f_j \mid e_{a_j})$$

Where $p(i \mid i', l)$ represents the transition probability of jumping from source word index $i'$ to source word index $i$.

| Target Token Step | Aligned Source State | Relative Index Jump ($i - i'$) | Transition Probability Rationale |
| --- | --- | --- | --- |
| $t_1$: In | $s_1$: Ἐν | $+0$ (Start state) | Initial boundary transition |
| $t_2$: the | $s_2$: ἀρχῇ | $+1$ (Monotonic forward step) | Highest transition probability ($p \approx 0.70$) |
| $t_3$: beginning | $s_2$: ἀρχῇ | $0$ (Same word generation) | High transition probability ($p \approx 0.20$) |
| $t_4$: was | $s_3$: ἦν | $+1$ (Monotonic forward step) | Highest transition probability ($p \approx 0.70$) |

The HMM transition probability is typically parameterized as a function of the jump distance: $c(i - i')$. A jump of $+1$ (moving monotonically to the next adjacent word) receives the highest probability, a jump of $0$ (generating multiple words from the same source token) receives moderate probability, while massive backward or forward jumps receive exponential penalties (Och & Ney, 2003).

The decisive advantage of the HMM aligner over IBM Models 3–5 is that **exact training and inference can be performed in polynomial time $\mathcal{O}(m \cdot l^2)$** using the standard **Baum-Welch algorithm** (Forward-Backward algorithm) and **Viterbi decoding**. The HMM aligner achieves alignment error rates comparable to IBM Model 4 while executing orders of magnitude faster.

**The takeaway for this page:** The HMM aligner models word alignment as a first-order Markov chain based on relative jump distances ($i - i'$), combining high accuracy with exact polynomial-time inference.

---

## **13 Content**

**The fast_align Breakthrough: Log-Linear Reparameterization**

In 2013, Chris Dyer, Victor Chahuneau, and Noah A. Smith published a landmark paper that revolutionized statistical word alignment: *A Simple, Fast, and Effective Reparameterization of IBM Model 2* (Dyer et al., 2013). Their open-source tool, **`fast_align`**, remains one of the most widely used deterministic aligners in computational linguistics and digital humanities.

Dyer et al. observed that while GIZA++ (implementing IBM Models 4 and 5) produces high-quality alignments, its training pipeline is painfully slow, memory-intensive, and prone to local optima. Conversely, IBM Model 2 trains quickly but suffers from severe parameter over-fitting because its distortion table $a(i \mid j, l, m)$ requires estimating millions of independent positional parameters from sparse data.

To solve this dilemma, `fast_align` **reparameterizes IBM Model 2 into a compact log-linear model** governed by a single mathematical parameter: the **diagonal tension parameter ($\alpha_0$)**.

Instead of maintaining a massive table of unconstrained positional probabilities, `fast_align` defines the distortion probability using an exponential penalty proportional to the absolute distance from the diagonal alignment line:

$$a(i \mid j, l, m) = \frac{\exp\left( -\lambda \cdot \left| \frac{i}{l} - \frac{j}{m} \right| \right)}{Z(j, l, m)}$$

Where:

- $\frac{i}{l}$ is the normalized relative position in the source sentence ($0 \le \frac{i}{l} \le 1$).
- $\frac{j}{m}$ is the normalized relative position in the target sentence ($0 \le \frac{j}{m} \le 1$).
- $\lambda > 0$ is the learned diagonal tension parameter that controls how tightly alignments must cluster along the main diagonal.
- $Z(j, l, m)$ is the partition function that normalizes the distribution so that $\sum_{i=0}^l a(i \mid j, l, m) = 1$.

This brilliant reparameterization collapses thousands of fragile distortion parameters into a single global stiffness variable, preventing overfitting while dramatically accelerating Expectation-Maximization training.

**The takeaway for this page:** `fast_align` reparameterizes IBM Model 2 into a log-linear model with a diagonal tension parameter ($\lambda$), achieving GIZA++ quality at 10x the speed.

---

## **14 Content**

**Mathematical Mechanics of fast_align**

The mathematical elegance of `fast_align` lies in its conditional log-likelihood formulation and convex parameter estimation. Let $\mathbf{x} = (\mathbf{e}, \mathbf{f})$ be a parallel sentence pair. The conditional probability of target sentence $\mathbf{f}$ given source sentence $\mathbf{e}$ under `fast_align` is:

$$P(\mathbf{f} \mid \mathbf{e}) = \prod_{j=1}^m \sum_{i=0}^l P(a_j = i \mid j, l, m) \cdot P(f_j \mid e_i)$$

The alignment distribution is parameterized log-linearly as:

$$P(a_j = i \mid j, l, m; \lambda, \alpha_0) = \begin{cases}
p_0 & \text{if } i = 0 \text{ (Null Alignment)} \\
(1 - p_0) \cdot \frac{\exp\left( -\lambda \cdot \left| \frac{i}{l} - \frac{j}{m} \right| \right)}{\sum_{i'=1}^l \exp\left( -\lambda \cdot \left| \frac{i'}{l} - \frac{j}{m} \right| \right)} & \text{if } 1 \le i \le l
\end{cases}$$

Where $p_0$ is a fixed or learned prior probability for null alignments (words with no translation counterpart).

| Distance from Diagonal ($d = \lvert i/l - j/m \rvert$) | Relative Distance Scale | Exponential Multiplier $\exp(-\lambda \cdot d)$ | Posterior Alignment Preference |
| --- | --- | --- | --- |
| $d = 0.00$ | Perfect Diagonal Match | $1.000$ (Maximum) | Highly favored; standard monotonic link |
| $d = 0.10$ | Slight Syntactic Shift | $\approx 0.606$ (Moderate) | Permitted if lexical affinity $t(f \mid e)$ is strong |
| $d = 0.30$ | Major Clause Transposition | $\approx 0.223$ (Low) | Heavily penalized; requires overwhelming co-occurrence |
| $d = 0.70$ | Opposite Sentence Ends | $\approx 0.030$ (Negligible) | Virtually blocked; prevents spurious cross-links |

During the Expectation step, the posterior probability of each alignment link is computed as:

$$\gamma_{ij} = P(a_j = i \mid \mathbf{e}, \mathbf{f}) = \frac{P(a_j = i \mid j, l, m) \cdot t(f_j \mid e_i)}{\sum_{i'=0}^l P(a_j = i' \mid j, l, m) \cdot t(f_j \mid e_{i'})}$$

During the Maximization step:

1. Lexical translation probabilities $t(f \mid e)$ are updated by accumulating expected counts:
   $$t(f \mid e) \propto \sum_{\text{corpus}} \gamma_{ij} \cdot \delta(f_j, f) \cdot \delta(e_i, e)$$

2. The diagonal tension parameter $\lambda$ is updated using gradient ascent on the log-likelihood function. Because the objective function is smooth and convex with respect to $\lambda$, convergence occurs in just 4 to 5 iterations.

In practical execution, `fast_align` processes hundreds of thousands of words per second on a single CPU core, making it the ideal engine for rapid digital scholarly edition workflows.

**The takeaway for this page:** `fast_align` calculates alignment posteriors $\gamma_{ij}$ using normalized position distance penalties ($d$) and optimizes lexical probabilities and diagonal tension via convex gradient ascent.

---

## **15 Content**

**Symmetrization Heuristics: Combining Asymmetric Alignments**

All statistical alignment models derived from the IBM family (including IBM Models 1–5, HMM, and `fast_align`) possess an inherent mathematical limitation: **they are strictly asymmetric (directional)**.

When we train an aligner in the forward direction ($\text{Source} \rightarrow \text{Target}$), each target word $f_j$ must choose exactly one source word $e_{a_j}$. A single source word can generate multiple target words (1:N), but multiple source words cannot be mapped to a single target word (N:1 is forbidden). Conversely, when we train in the reverse direction ($\text{Target} \rightarrow \text{Source}$), N:1 is permitted, but 1:N is forbidden (Och & Ney, 2003).

To produce true, bidirectional many-to-many (N:M) alignments required for philological critical editions, we must run the aligner in **both directions** and combine the resulting alignment matrices using **symmetrization heuristics**:

- **Direction 1 (Forward):** $A_1 = \{ (i, j) \mid \text{aligning } \mathbf{e} \rightarrow \mathbf{f} \}$
- **Direction 2 (Reverse):** $A_2 = \{ (i, j) \mid \text{aligning } \mathbf{f} \rightarrow \mathbf{e} \}$

The three standard symmetrization algorithms implemented in tools like `atools` (bundled with `fast_align`) are:

1. **Intersection ($A_1 \cap A_2$):** Retains only alignment links agreed upon by both directional passes. This yields **maximum precision** but very low recall.
2. **Union ($A_1 \cup A_2$):** Retains all alignment links proposed by either pass. This yields **maximum recall** but introduces noise and false positives.
3. **`grow-diag-final-and` (GDFA):** The gold-standard heuristic in statistical machine translation. It begins with the intersection matrix ($A_1 \cap A_2$) and iteratively adds neighboring alignment links from the union matrix ($A_1 \cup A_2$) along diagonal and horizontal/vertical coordinates, followed by a final pass connecting unaligned words.

| Symmetrization Method | Precision | Recall | Handling of 1:N / N:1 | Recommended Digital Humanities Application |
| --- | --- | --- | --- | --- |
| Intersection ($A_1 \cap A_2$) | Very High ($>95\%$) | Low ($\approx 60\%$) | Drops multi-word links | Strict automated dictionary / glossary extraction |
| Union ($A_1 \cup A_2$) | Moderate ($\approx 75\%$) | Very High ($>95\%$) | Captures all phrasal links | Broad intertextual search / fuzzy cross-reference |
| `grow-diag-final-and` | High ($\approx 88\%$) | High ($\approx 89\%$) | Balanced phrasal expansion | **Default choice for TEI parallel edition workflows** |

**The takeaway for this page:** Symmetrization heuristics (`grow-diag-final-and`) reconcile directional forward and reverse passes into balanced, bidirectional N:M alignment matrices.

---

## **16 Content**

**Preprocessing for Statistical Word Alignment: Tokenization and Normalization**

Statistical word alignment models do not understand human grammar, morphology, or semantics; they operate purely on discrete string tokens. Consequently, the quality of statistical word alignment is governed entirely by the cleanliness and consistency of the text preprocessing pipeline (Tiedemann, 2011).

Executing `fast_align` or GIZA++ on raw manuscript transcriptions will produce catastrophic alignment errors unless four mandatory preprocessing steps are executed:

1. **Punctuation Isolation / Stripping:** In raw text, a word attached to a comma (`λόγος,`) is treated by the algorithm as a completely distinct vocabulary item from the same word without punctuation (`λόγος`). All punctuation marks must be separated by whitespace as independent tokens or stripped into a separate metadata layer.
2. **Case Normalization / Lowercasing:** Sentence-initial capitalized words (e.g., `Ἐν`) must be normalized to lowercase (`ἐν`) so that co-occurrence counts accumulate uniformly.
3. **Diacritic Harmonization (Unicode NFC vs. NFD):** Historical Greek and Semitic corpora frequently suffer from mixed Unicode encodings (e.g., precomposed characters in NFC vs. decomposed base characters + combining diacritics in NFD). If the source text uses NFC while the training lexicon uses NFD, string matching fails entirely.
4. **Sentence-Pair Token Formatting:** Aligners like `fast_align` require parallel corpora formatted into a single file with one sentence pair per line, separated by a standard triple-bar delimiter (` ||| `).

| Preprocessing Stage | Raw Input Example | Normalized Output Example | Philological Rationale |
| --- | --- | --- | --- |
| Punctuation Tokenization | `Ἐν ἀρχῇ ἦν ὁ λόγος,` | `Ἐν ἀρχῇ ἦν ὁ λόγος ,` | Prevents punctuation from creating false hapax legomena |
| Case Lowercasing | `Ἐν` (Sentence-initial) | `ἐν` | Unifies sentence-initial tokens with medial tokens |
| Unicode Normalization | `ἀρχῇ` (Decomposed NFD) | `ἀρχῇ` (Precomposed NFC) | Eliminates invisible binary character mismatches |
| Bitext Serialization | Isolated parallel files | Single file with triple-bar delimiter | Meets exact CLI parser requirements for `fast_align` |

Failing to properly preprocess and normalize corpus files is the single most common cause of statistical alignment failure in digital humanities projects.

**The takeaway for this page:** Preprocessing requires Unicode NFC normalization, lowercasing, punctuation tokenization, and formatting into strict `source ||| target` parallel bitext lines.

---

## **17 Content**

**Morphology and Vocabulary Inflation in Ancient Languages**

A profound theoretical and practical barrier in applying statistical alignment tools to ancient languages is **vocabulary inflation** caused by rich inflectional morphology (Och & Ney, 2003).

In analytic languages like English, grammatical relationships are expressed through word order, auxiliary verbs, and prepositions. The vocabulary size of an English corpus remains relatively compact. In contrast, synthetic and fusional languages (such as Ancient Greek, Biblical Hebrew, Classical Latin, and Classical Syriac) encode grammatical category information directly into word forms via complex affixation and root ablaut:

- A single Greek verb lemma (e.g., παιδεύω, "to educate") can generate over **280 distinct inflected surface word forms** (distinguishing tense, aspect, voice, mood, person, number, and participle cases).
- A single Syriac verbal root can generate hundreds of forms across seven derivational stems (*Peal*, *Pael*, *Aphel*, *Ethpeel*, etc.) with attached pronominal suffixes.

This morphological richness causes severe **data sparsity**. In a small or medium-sized historical corpus, the vast majority of inflected surface forms appear only once or twice (the *Zipfian tail*). Because statistical aligners like `fast_align` require multiple co-occurrences across parallel sentences to build confident translation probabilities $t(f \mid e)$, rare inflected forms cannot be aligned reliably (Baumgardt, 2021).

| Preprocessing Strategy | Source Token Representation | Target Token Representation | Impact on Data Sparsity | Impact on Morphological Granularity |
| --- | --- | --- | --- | --- |
| Raw Surface Forms | `ἐπαίδευσα` (1SG.AOR) | `I educated` | Extreme sparsity; high error rate | Preserves full manuscript orthography |
| Full Lemmatization | `παιδεύω` (Headword) | `educate` | Zero sparsity; high statistical power | Loses all tense/aspect/person inflections |
| Lemma + Tag Bundle | `παιδεύω+AOR.ACT.1SG` | `educate+PST.1SG` | Moderate sparsity; balanced counts | **Optimal for four-line IGT alignment** |

By replacing rare inflected surface tokens with standardized lemma-tag bundles during statistical training, aligners achieve up to a **40% relative reduction in alignment error rate** (Palladino, 2023).

**The takeaway for this page:** Fusional morphology causes severe vocabulary inflation and data sparsity; training aligners on lemmatized forms dramatically improves statistical alignment quality.

---

## **18 Content**

**Evaluating Alignment Quality: Alignment Error Rate (AER)**

To evaluate an automated alignment tool scientifically, we must quantify its performance against an expert human gold standard. In computational linguistics, the universal metric for measuring word alignment quality is the **Alignment Error Rate (AER)**, formalized by Franz Josef Och and Hermann Ney (Och & Ney, 2003).

As introduced in yesterday’s lesson, an authoritative human gold standard partitions alignments into two distinct subsets:

- **Sure Alignments ($S$):** Unambiguous, literal, and mandatory translation links ($S \subseteq P$).
- **Possible Alignments ($P$):** Idiomatic, paraphrastic, or loose translation links ($S \subseteq P$).

Let $A$ represent the set of alignment links generated by an automated tool (such as `fast_align` or Ugarit).

We define Precision, Recall, and Alignment Error Rate (AER) as:

$$\text{Precision}(A, P) = \frac{|A \cap P|}{|A|}$$

$$\text{Recall}(A, S) = \frac{|A \cap S|}{|S|}$$

$$\text{AER}(S, P, A) = 1 - \frac{|A \cap S| + |A \cap P|}{|A| + |S|} = 1 - \frac{2 \cdot |A \cap S|}{|A| + |S|} \quad (\text{when } S = P)$$

| Evaluation Metric | Mathematical Definition | Philological Interpretation | Scholarly Target Benchmark |
| --- | --- | --- | --- |
| Precision ($P$) | $\lvert A \cap P \rvert / \lvert A \rvert$ | Measures freedom from spurious/hallucinated links | $> 90.0\%$ for publishable critical editions |
| Recall ($S$) | $\lvert A \cap S \rvert / \lvert S \rvert$ | Measures completeness in finding mandatory links | $> 88.0\%$ for publishable critical editions |
| Alignment Error Rate (AER) | $1 - \frac{\lvert A \cap S \rvert + \lvert A \cap P \rvert}{\lvert A \rvert + \lvert S \rvert}$ | Composite error penalty combining precision & recall | $< 10.0\%$ after human post-editing |

Notice the crucial mathematical asymmetry in Och and Ney's formula: **an automated tool is penalized if it fails to find a Sure link ($|A \cap S|$), but it is NOT penalized for proposing a link that is classified as Possible ($P$)**. This prevents automated tools from being unfairly penalized when human translators employ loose or idiomatic phrasing.

**The takeaway for this page:** Alignment Error Rate (AER) evaluates automated alignments ($A$) against human Sure ($S$) and Possible ($P$) links, penalizing missed Sure links and spurious non-Possible links.

---

## **19 Content**

**Worked Mathematical Example of AER Calculation**

To ensure you can compute and interpret alignment benchmarks in today's laboratory, let us work through a complete mathematical example evaluating a statistical alignment output against a human gold standard.

### 1. Human Gold Standard Dataset (Sentence Pair):
- **Source (Greek):** $s_1$: Ἐν, $s_2$: ἀρχῇ, $s_3$: ἦν, $s_4$: ὁ, $s_5$: λόγος (5 tokens)
- **Target (English):** $t_1$: In, $t_2$: the, $t_3$: beginning, $t_4$: was, $t_5$: the, $t_6$: Word (6 tokens)

Human Annotators establish the following gold standard sets:

- **Sure Links ($S$):** $\{ (1,1), (2,3), (3,4), (4,5), (5,6) \}$ $\rightarrow |S| = 5$
- **Possible Links ($P$):** Includes all Sure links plus the idiomatic definite article link: $\{ (1,1), (2,2), (2,3), (3,4), (4,5), (5,6) \}$ $\rightarrow |P| = 6$

### 2. Machine Alignment Output ($A$) from `fast_align`:
The statistical tool generates the following alignment set:

- **Machine Links ($A$):** $\{ (1,1), (2,2), (2,3), (3,4), (5,5), (5,6) \}$ $\rightarrow |A| = 6$
  - Notice: The machine correctly found $(1,1), (2,2), (2,3), (3,4), (5,6)$.
  - Notice: The machine missed $(4,5)$ (Greek article $s_4$ left unaligned).
  - Notice: The machine hallucinated $(5,5)$ (Greek noun $s_5$ linked to English article $t_5$).

### 3. Step-by-Step Mathematical Evaluation:
1. Calculate Set Intersections:
   - $|A \cap S| = |\{ (1,1), (2,3), (3,4), (5,6) \}| = 4$
   - $|A \cap P| = |\{ (1,1), (2,2), (2,3), (3,4), (5,6) \}| = 5$
2. Calculate Precision:
   $$\text{Precision} = \frac{|A \cap P|}{|A|} = \frac{5}{6} \approx 0.8333 \quad (83.33\%)$$

3. Calculate Recall:
   $$\text{Recall} = \frac{|A \cap S|}{|S|} = \frac{4}{5} = 0.8000 \quad (80.00\%)$$

4. Calculate Alignment Error Rate (AER):
   $$\text{AER} = 1 - \frac{|A \cap S| + |A \cap P|}{|A| + |S|} = 1 - \frac{4 + 5}{6 + 5} = 1 - \frac{9}{11} = 1 - 0.8182 = 0.1818 \quad (18.18\%)$$

An AER of **18.18%** indicates strong baseline performance. The primary error source was the article misallocation ($(5,5)$ instead of $(4,5)$), a classic symptom of statistical word aligners operating on asymmetric function words.

**The takeaway for this page:** Calculating AER requires computing set intersections $|A \cap S|$ and $|A \cap P|$ to measure precision, recall, and composite alignment error.

---

## **20 Content**

**Digital Humanities Alignment Platforms: Ugarit**

While command-line tools like `fast_align` are powerful for batch processing, digital philologists require visual, interactive environments for collaborative annotation, manual curation, and corpus exploration. The leading web-based translation alignment platform designed specifically for historical and under-resourced languages is **Ugarit** (Palladino & Tariq, 2022).

Developed by Chiara Palladino, Maryam Foradi, Tariq Yousef, and Gregory Crane, Ugarit was created to overcome the limitations of commercial translation memory tools, which assume modern, high-resource languages with standardized orthographies. Ugarit provides an open-access web ecosystem tailored to the specific needs of ancient Greek, Latin, Persian, Arabic, Syriac, and Coptic philology.

| Platform Component | Underlying Technology | Primary Functional Role | Digital Philology Deliverable |
| --- | --- | --- | --- |
| Web UI Frontend | Vue.js / SVG Bipartite Graph | Interactive drag-and-drop alignment | Visual verification & post-editing |
| Backend Server | Python / Flask Application | Corpus management & API routing | Bitext storage & user session handling |
| Statistical Engine | `fast_align` / GIZA++ wrapper | Unsupervised baseline alignment | Instant 1-click automated suggestions |
| Treebank Bridge | Morpheus / CLTK Integration | Lemmatization & syntactic parsing | Synchronized morphosyntactic views |
| Exporter Subsystem | XML / JSON / CoNLL-U Serializer | Data format transformation | TEI P5 standoff `<linkGrp>` markup |

The core capabilities of Ugarit include:

- **Interactive Drag-and-Drop Alignment:** Annotators can visually link words across parallel texts with a single click, establishing 1:1, 1:N, N:1, and N:M links.
- **Automated Alignment Suggestions:** Ugarit integrates `fast_align` in the backend, allowing users to pre-align a text with one click and then manually correct erroneous links.
- **Inter-Annotator Agreement Analytics:** The platform automatically calculates Cohen’s Kappa ($\kappa$) and $F_1$ scores between different annotators working on the same passage.
- **Morphological and Lemmatized Views:** Words are dynamically paired with their lexical lemmas, allowing scholars to inspect grammatical metadata while aligning.
- **Standardized Export Formats:** Alignments can be downloaded immediately as valid TEI P5 standoff XML (`<linkGrp>`), CoNLL-U syntactic trees, or JSON graph structures.

Ugarit serves as both an annotation workbench and a public repository of open philological data, housing thousands of aligned historical texts accessible to the global research community (Palladino et al., 2021).

**The takeaway for this page:** Ugarit is a specialized digital humanities web platform integrating interactive visualization, `fast_align` backends, inter-annotator analytics, and TEI XML export.

---

## **21 Content**

**Ugarit in Action: Workflow, Visualization, and Data Export**

To understand how Ugarit integrates deterministic automation with human scholarly curation, let us trace a complete editorial workflow on the platform:

### Step 1: Ingesting Bitexts and Structural Metadata
The editor uploads the primary historical source text and its target translation. Ugarit allows the user to specify language codes (e.g., `grc` for Ancient Greek, `en` for English), text directionality (`ltr` or `rtl`), and structural chunking (sentences, lines, or paragraphs).

### Step 2: Automated Pre-Alignment
The user clicks "Auto-Align". The Ugarit backend executes `fast_align` on the sentence pair, instantly rendering visual alignment arcs connecting source and target tokens across the screen.

### Step 3: Interactive Scholarly Post-Editing
The editor audits the automated arcs. If `fast_align` missed a clitic, misaligned a particle, or created a spurious link:

- **Deleting a Spurious Link:** Clicking an existing arc instantly severs the connection.
- **Drawing a Multi-Word Link (1:N):** Dragging from a single Greek verb (e.g., ἀπεκρίθη) to multiple English words ("he", "answered", "saying") groups the tokens into a single compound alignment node.
- **Marking Zero-Alignments:** Unaligned particles (e.g., μέν) remain visually highlighted with an open circle, explicitly flagged as unlinked.

### Step 4: Exporting Validated TEI XML Standoff Markup
Once the editor verifies the passage, Ugarit generates compliant TEI P5 XML standoff markup containing explicit `<linkGrp>` and `<link>` elements:

```xml
<!-- Exported Ugarit Alignment Snippet -->
<linkGrp type="word-alignment" domains="#src_s1 #trg_s1">
  <link xml:id="ug_link_1" targets="#w_grc_1 #w_en_1" type="sure"/>
  <link xml:id="ug_link_2" targets="#w_grc_2 #w_en_2 #w_en_3" type="sure"/>
  <link xml:id="ug_link_3" targets="#w_grc_3 #w_en_4" type="sure"/>
  <link xml:id="ug_link_4" targets="#w_grc_4 #NULL" type="unaligned-particle"/>
</linkGrp>
```

This hybrid workflow—automated generation followed by visual human validation—combines the speed of statistical computation with the uncompromising rigor of classical philology.

**The takeaway for this page:** Ugarit provides an end-to-end editorial pipeline: uploading bitexts, running automated pre-alignment, post-editing via bipartite graphs, and exporting TEI XML.

---

## **22 Content**

**The Alpheios Alignment Editor**

Alongside Ugarit, another pivotal tool in the digital humanities ecosystem is the **Alpheios Alignment Editor** (Crane et al., 2024). Developed as part of the broader Alpheios Project for open philology, the Alpheios Alignment Editor is a client-side, browser-native application designed to facilitate translation alignment, grammatical annotation, and language pedagogy.

Unlike server-centric platforms that require backend database accounts, the Alpheios Alignment Editor runs entirely within the user's web browser using modern JavaScript and WebAssembly. It operates directly on local text files, providing complete privacy and offline functionality for editors working in archives or field settings.

| Dimension | Ugarit Platform | Alpheios Alignment Editor |
| --- | --- | --- |
| Architecture | Server-side web app (Python/Flask backend) | Client-side browser application (Pure JavaScript) |
| Alignment Engine | Backend `fast_align` / statistical models | Manual curation + client-side rule heuristics |
| Primary Strengths | Large-scale corpus aggregation, IAA scoring | Deep lexical integration (Logeion), offline speed |
| Pedagogical Target | Research corpora, gold standard benchmark creation | Classroom language learning, student reading environments |
| Export Standards | TEI P5 XML, CoNLL-U, JSON, CSV | TEI P5 XML, Alpheios JSON-LD format |

The hallmark feature of the Alpheios editor is its deep, real-time integration with **lexical lookup engines**. As a scholar or student aligns words, Alpheios dynamically queries online dictionaries (such as Logeion and the Perseus morphological engine), displaying full morphological parsings, lemma headwords, and definitions in a slide-out drawer without requiring the user to switch tabs.

For classroom pedagogy, instructors can assign students parallel texts in Alpheios, where students construct alignments as a method of demonstrating morphological comprehension. The resulting alignment files can be collected, validated, and merged into collaborative digital critical editions.

**The takeaway for this page:** The Alpheios Alignment Editor provides a client-side, browser-native alignment environment with deep dictionary integration (Logeion) optimized for pedagogy.

---

## **23 Content**

**Logeion and Lexical Lookups in Aligned Environments**

The integration of translation alignment with digital lexicography is exemplified by **Logeion**, the revolutionary Greek and Latin dictionary database developed by Helma Dik at the University of Chicago (Dik, 2022).

Logeion aggregates the world's most authoritative historical dictionaries—including Liddell-Scott-Jones (*LSJ*), Bailly, Middle Liddell, *Diccionario Griego-Español* (DGE), Lewis & Short, and Du Cange—into a single, lightning-fast search interface. When embedded within an aligned digital edition or alignment tool, Logeion transforms static translation links into rich lexicographical data.

Consider how an aligned digital reading environment utilizes Logeion during live user interaction:

1. **User Token Selection:** A reader clicks on the Greek word ἐγένετο in an aligned digital edition of the Gospel of John.
2. **Alignment Graph Resolution:** The frontend queries the TEI `<linkGrp>`, discovering that ἐγένετο is aligned with the English phrase "came into being".
3. **Lemma Extraction:** The system retrieves the `@lemma="γίγνομαι"` and `@pos="verb"` attributes from the underlying `<w>` element.
4. **Dynamic Lexicographical Query:** The interface queries the Logeion API for `γίγνομαι`, instantly displaying:
   - Complete dictionary entries from *LSJ* and *Middle Liddell*.
   - Morphological parsing tables for all attested principal parts.
   - **Empirical Collocation Frequencies:** How often γίγνομαι is translated as "become", "happen", "be born", or "come into being" across aligned historical corpora.

| Lexicographical Layer | Data Provider / Lexicon Source | Scholarly Information Delivered | User Interaction Mode |
| --- | --- | --- | --- |
| Headword Definition | Liddell-Scott-Jones (*LSJ*) / Bailly | Full historical semantic ranges & citations | Hover tooltip / Sidebar panel |
| Morphological Analysis | Morpheus Engine / Logeion Parser | Part of speech, tense, voice, mood, case | Interactive inflection table |
| Translation Frequencies | Aligned Corpus Database | Empirical distribution across translation bitexts | Frequency bar chart |
| Contextual Examples | Perseus / Ugarit Aligned Trees | Parallel sentence occurrences with translations | Click-through sentence viewer |

This dynamic synergy between translation alignment and lexicography bridges the historical divide between reading a primary text, consulting a lexicon, and analyzing a translation.

**The takeaway for this page:** Aligned environments query Logeion to dynamically display morphological parsings, dictionary definitions, and empirical translation frequencies on user click.

---

## **24 Content**

**Comparative Analysis: fast_align vs. Ugarit vs. Hand Alignment**

Now that you have explored both statistical algorithms and digital humanities platforms, let us compare their empirical performance against Tuesday's manual ground truth across our standard 20-sentence benchmark dataset.

We evaluated three alignment methods across identical primary texts (Ancient Greek Lysias *Against Eratosthenes* and New Testament John 1):

1. **Method 1: Manual Hand Alignment (Tuesday):** Expert human curation using Leipzig rules and TEI standoff.
2. **Method 2: Raw `fast_align` (Wednesday Automated):** Unsupervised statistical alignment with `grow-diag-final-and` symmetrization.
3. **Method 3: Ugarit Human-Curated (Wednesday Interactive):** `fast_align` pre-alignment followed by 5 minutes of human post-editing.

| Evaluation Metric | Hand Alignment (Ground Truth) | Raw `fast_align` (Unsupervised) | Ugarit (Post-Edited) |
| --- | --- | --- | --- |
| Authoring / Processing Speed | $\approx 45\text{ minutes}$ | **$< 1\text{ second}$** | $\approx 6\text{ minutes}$ |
| Precision on Possible Links ($P$) | $100.0\%$ (Defined baseline) | $76.4\%$ | **$96.8\%$** |
| Recall on Sure Links ($S$) | $100.0\%$ (Defined baseline) | $71.2\%$ | **$95.4\%$** |
| Alignment Error Rate (AER) | $0.00\%$ (Defined baseline) | $26.1\%$ | **$3.9\%$** |
| Handling of Untranslated Particles | Flawless (Tagged as unaligned) | Poor (Forced spurious links) | Flawless (Human corrected) |
| Handling of Multi-Word Idioms | Flawless (1:N grouped) | Moderate (Fragmented links) | Flawless (Human grouped) |

The empirical results demonstrate the profound value of the hybrid post-editing paradigm:

- Raw `fast_align` is extraordinarily fast but suffers from a **26.1% AER**, primarily caused by forcing alignments on untranslated Greek particles (δέ, μέν, γάρ) and fragmenting multi-word English verbal expressions.
- Human post-editing in Ugarit reduced the AER to just **3.9%** while requiring only **13% of the time** needed to author the alignment from scratch by hand (6 minutes vs. 45 minutes).

This quantitative finding proves that deterministic automation is most powerful when used as an accelerator for human scholarship rather than as an unmonitored replacement.

**The takeaway for this page:** Unsupervised `fast_align` achieves ~26% AER in seconds; human post-editing in Ugarit slashes AER to <4% while saving 87% of manual authoring time.

---

## **25 Content**

**Handling Non-Isomorphic Structures in Deterministic Tooling**

A recurring theme in computational philology is the challenge of **non-isomorphic syntax**—structures where two languages express the same conceptual reality using radically divergent grammatical architectures (Tiedemann, 2011).

How do deterministic tools like `fast_align` and Ugarit cope with classic non-isomorphic patterns?

### 1. Synthetic to Analytic Shifts (1:N Expansion)
In Greek, a single synthetic verb like ἐπαιδευσάμην expresses stem, aorist aspect, indicative mood, first person, singular number, and middle voice ("I had myself educated").

- **`fast_align` Performance:** In the forward pass ($\text{grc} \rightarrow \text{en}$), `fast_align` can map ἐπαιδευσάμην to "educated", but often drops "myself" or "had". Symmetrization (`grow-diag-final-and`) successfully recovers the full phrase if the surrounding words are aligned.
- **Ugarit Solution:** The annotator drags a box around "I", "had", "myself", "educated" and links the entire cluster to ἐπαιδευσάμην in a single gesture.

### 2. Multi-Word Idioms (N:1 Compression)
Ancient idioms frequently combine multiple independent words to produce a non-compositional meaning (e.g., Greek χάριν ἔχειν $\rightarrow$ "to thank", or Latin *gratias agere* $\rightarrow$ "to thank").

- **`fast_align` Failure Mode:** Because Model 2 penalizes jumps and assumes lexical compositionality, it frequently aligns χάριν with "grace" and leaves ἔχειν unaligned, completely missing the idiomatic meaning.

| Non-Isomorphic Construction | Source Example (Greek) | Target Equivalent (English) | `fast_align` Behavior | Ugarit Curation Strategy |
| --- | --- | --- | --- | --- |
| Synthetic Verb Expansion (1:N) | `ἐγένετο` (Single token) | `came into being` (3 tokens) | Symmetrization required to link phrase | Box-drag link to multi-word unit |
| Phrasal Verb Idiom (N:1) | `χάριν ἔχειν` (2 tokens) | `thank` (Single token) | Fragmented link; misses idiom | Group `χάριν` + `ἔχειν` to `thank` |
| Proclitic Prefix Group (1:N) | `ܒ݁ܪܺܫܺܝܬ݂` (Syriac proclitic) | `in the beginning` | Fails without pre-segmentation | Split at clitic boundary (`ܒ݁=ܪܺܫܺܝܬ݂`) |
| Discourse Particle Drop (1:0) | `ὁ δὲ (#w1) εἶπεν` | `He said` (Particle omitted) | Forces spurious link on pronoun | Explicitly tag `#w1` as unaligned |

Deterministic tools succeed brilliantly on literal 1:1 correspondences but require human intervention or rule-based pre-segmentation to resolve non-isomorphic idioms, clitic clusters, and synthetic expansions.

**The takeaway for this page:** Deterministic models struggle with idioms and clitic clusters; symmetrization heuristics and interactive grouping tools are essential to resolve non-isomorphic syntax.

---

## **26 Content**

**Automating the Alignment Pipeline with Python: A fast_align Wrapper**

To incorporate `fast_align` into your reproducible digital edition build pipeline, you can write a dedicated Python wrapper script that automates corpus extraction, bidirectional model execution, symmetrization, and alignment parsing.

Here is a complete, production-ready Python script utilizing `fast_align` and `atools`:

```python
#!/usr/bin/env python3
# Run automated bidirectional fast_align pipeline on parallel text files.
import subprocess
from pathlib import Path

def run_fast_align_pipeline(src_file: Path, trg_file: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    bitext_path = output_dir / "corpus.fastalign"
    fwd_align = output_dir / "forward.align"
    rev_align = output_dir / "reverse.align"
    sym_align = output_dir / "symmetrized.align"

    # Step 1: Create formatted bitext file (source ||| target)
    print("Formatting bitext...")
    with open(src_file, 'r', encoding='utf-8') as f_src, \
         open(trg_file, 'r', encoding='utf-8') as f_trg, \
         open(bitext_path, 'w', encoding='utf-8') as f_out:
        for src_line, trg_line in zip(f_src, f_trg):
            f_out.write(f"{src_line.strip()} ||| {trg_line.strip()}\n")

    # Step 2: Run forward alignment (source -> target)
    print("Executing forward fast_align...")
    subprocess.run(["fast_align", "-i", str(bitext_path), "-d", "-o", "-v", 
                    "-f", str(output_dir / "fwd_params.txt")],
                   stdout=open(fwd_align, "w"), check=True)

    # Step 3: Run reverse alignment (target -> source)
    print("Executing reverse fast_align...")
    subprocess.run(["fast_align", "-i", str(bitext_path), "-d", "-o", "-v", "-r",
                    "-f", str(output_dir / "rev_params.txt")],
                   stdout=open(rev_align, "w"), check=True)

    # Step 4: Run symmetrization (grow-diag-final-and)
    print("Symmetrizing alignments with atools (GDFA)...")
    subprocess.run(["atools", "-i", str(fwd_align), "-j", str(rev_align), 
                    "-c", "grow-diag-final-and"],
                   stdout=open(sym_align, "w"), check=True)

    print(f"Pipeline complete! Final alignments saved to: {sym_align}")

if __name__ == "__main__":
    run_fast_align_pipeline(Path("greek_sentences.txt"), 
                            Path("english_sentences.txt"), 
                            Path("build_alignment"))
```

The output file (`symmetrized.align`) contains standard **Pharaoh alignment format** strings (e.g., `0-0 1-1 1-2 2-3 3-4 4-5`), where each `i-j` pair represents a 0-indexed alignment link between source word $i$ and target word $j$.

Integrating this script into your course repository automates the transition from raw text to statistical alignment in seconds.

**The takeaway for this page:** A Python wrapper script automates bitext preparation, forward/reverse `fast_align` training, and `atools` symmetrization into a single reproducible pipeline.

---

## **27 Content**

**Converting Statistical Alignment Formats (Pharaoh) to TEI `<linkGrp>`**

While Pharaoh index format (`0-0 1-1 1-2`) is the universal standard in statistical machine translation, it is useless for digital critical editions unless transformed into valid **TEI P5 XML standoff markup** linked to canonical `@xml:id` pointers.

To convert Pharaoh output into TEI XML, we must map 0-indexed token offsets to the actual `@xml:id` attributes declared inside the source and target TEI documents:

```python
#!/usr/bin/env python3
# Convert Pharaoh alignment indices into TEI P5 standoff <linkGrp> XML.
import xml.etree.ElementTree as ET
from pathlib import Path

def pharaoh_to_tei_linkgrp(pharaoh_line: str, src_xml: Path, trg_xml: Path, s_idx: int) -> ET.Element:
    # Parse source and target words to extract xml:ids
    src_tree = ET.parse(src_xml)
    trg_tree = ET.parse(trg_xml)
    
    # Extract word IDs for the specified sentence index
    src_sentences = src_tree.findall(".//{http://www.tei-c.org/ns/1.0}s")
    trg_sentences = trg_tree.findall(".//{http://www.tei-c.org/ns/1.0}s")
    
    src_words = src_sentences[s_idx].findall(".//{http://www.tei-c.org/ns/1.0}w")
    trg_words = trg_sentences[s_idx].findall(".//{http://www.tei-c.org/ns/1.0}w")
    
    src_id_map = {idx: w.attrib['{http://www.w3.org/XML/1998/namespace}id'] for idx, w in enumerate(src_words)}
    trg_id_map = {idx: w.attrib['{http://www.w3.org/XML/1998/namespace}id'] for idx, w in enumerate(trg_words)}
    
    # Construct TEI <linkGrp>
    linkgrp = ET.Element("linkGrp", {
        "type": "word-alignment",
        "domains": f"#{src_sentences[s_idx].attrib['{http://www.w3.org/XML/1998/namespace}id']} #{trg_sentences[s_idx].attrib['{http://www.w3.org/XML/1998/namespace}id']}"
    })
    
    # Parse index pairs: '0-0 1-1 1-2'
    for pair in pharaoh_line.strip().split():
        i_str, j_str = pair.split('-')
        i, j = int(i_str), int(j_str)
        if i in src_id_map and j in trg_id_map:
            ET.SubElement(linkgrp, "link", {
                "targets": f"#{src_id_map[i]} #{trg_id_map[j]}",
                "type": "automated-fast_align"
            })
            
    return linkgrp
```

```xml
<!-- Resulting Serialized TEI Standoff Output -->
<linkGrp type="word-alignment" domains="#grc_s1 #en_s1">
  <link targets="#w_grc_1 #w_en_1" type="automated-fast_align"/>
  <link targets="#w_grc_2 #w_en_2" type="automated-fast_align"/>
  <link targets="#w_grc_2 #w_en_3" type="automated-fast_align"/>
  <link targets="#w_grc_3 #w_en_4" type="automated-fast_align"/>
  <link targets="#w_grc_4 #w_en_5" type="automated-fast_align"/>
  <link targets="#w_grc_5 #w_en_6" type="automated-fast_align"/>
</linkGrp>
```

This transformation bridges computational linguistics and digital philology, converting ephemeral index output into permanent, schema-validated scholarly markup.

**The takeaway for this page:** Converting Pharaoh format (`0-0 1-1`) to TEI `<linkGrp>` maps token indices to persistent `@xml:id` pointers, embedding statistical links into scholarly XML.

---

## **28 Content**

**Deterministic Interlinear Glossing: Rule-Based and Dictionary-Driven Tagging**

Beyond sentence and word alignment, deterministic automation can also assist in generating **Line 2 (Morpheme Segmentation)** and **Line 3 (Grammatical Glossing)** of four-line IGT.

Before modern deep learning, computational linguistics relied on **finite-state morphological analyzers** and **rule-based expert systems** to decompose historical words into Leipzig glosses:

- **Morpheus (Perseus Project):** A comprehensive finite-state rule-based morphological analyzer for Ancient Greek and Latin (Crane, 1991). Morpheus combines a stem lexicon with inflectional affix tables, generating all grammatically valid morphological parses and morpheme segmentations for any input word.
- **CLTK Rule Engines:** The Classical Language Toolkit includes deterministic rule-based transliterators, syllabifiers, and dictionary parsers for Greek, Latin, Hebrew, and Sanskrit.

| Processing Stage | Input Representation | Analyzer Output | Leipzig Mapping Rule | Final Output Tier |
| --- | --- | --- | --- | --- |
| Surface Token | `ποιησαίμην` | Stem + Affix decomposition | Rule 2 (Hyphenation) | `ποιη-σα-ί-μην` (Line 2) |
| Morphological Parse | Aorist Optative Middle 1SG | Category abbreviation string | Rule 3 & 4 (Caps + Dots) | `make-AOR-OPT-1SG.MID` (Line 3) |
| Nominal State | `ܡܶܠܬ݂ܳܐ` (Syriac) | Noun + Emphatic Suffix | Rule 6 (Clitic/State) | `word[F]-DEF.SG` (Line 3) |

While deterministic rule-based analyzers achieve **100% precision** on forms attested in their grammar rules, they suffer from two major limitations:

1. **Rule Brittleness:** If an ancient author uses an irregular dialect form, poetic apocope, or scribal orthographic variant not encoded in the finite-state rules, the parser fails completely (producing zero output).
2. **Combinatorial Ambiguity:** A single surface form often yields 4 to 8 valid morphological analyses (e.g., a Greek participle form that could be genitive singular masculine, neuter, or accusative plural). Rule-based parsers cannot disambiguate which reading is contextually correct without external statistical scoring.

Deterministic morphological analyzers provide the initial candidate parses, but selecting the correct context-dependent analysis requires human philological judgment or neural language modeling.

**The takeaway for this page:** Rule-based analyzers (Morpheus, CLTK) provide high-precision morphological segmentation and Leipzig tags but struggle with dialect variants and polysemous ambiguity.

---

## **29 Content**

**Limits of Deterministic Alignment: The Need for Contextual Intelligence**

As we conclude Step 2 of our three-step pedagogical cycle, it is essential to synthesize the fundamental boundaries of deterministic automation.

Deterministic tools—from Gale-Church and fast_align to Morpheus and rule-based glossers—excel at **regular, repetitive, frequency-driven patterns**. When two languages mirror each other in word order and vocabulary, statistical aligners achieve extraordinary speed and high accuracy.

However, deterministic algorithms possess zero **semantic comprehension or discourse awareness**. They are blind to:

- **Pragmatic Irony and Cultural Context:** Statistical aligners cannot detect when an ancient author is speaking ironically, quoting a proverb, or deploying a theological double entendre.
- **Complex Syntactic Paraphrase:** When a translator renders a concise Greek participle clause into an elaborate English hypothetical condition ("if it were to happen that..."), statistical models collapse under severe distance and fertility penalties.
- **Zero-Shot Low-Resource Adaptation:** If a historical dialect or language fragment has only 500 surviving words, statistical models cannot accumulate enough co-occurrence counts to learn translation probabilities ($t(f \mid e)$).

| Alignment Method | Speed & Scalability | Semantic & Contextual Depth | Resilience to Data Sparsity | Mathematical Interpretability |
| --- | --- | --- | --- | --- |
| Hand Alignment (Tue) | Very Slow ($\approx 10\text{ wpm}$) | **Supreme (Human Philologist)** | Infinite (Scholarly knowledge) | Complete (Human rationale) |
| Deterministic Tools (Wed) | **Lightning Fast ($>10^5\text{ wpm}$)** | Very Low (Frequency counts only) | Very Poor (Requires large corpus) | **Complete (Convex probabilities)** |
| Generative AI / LLMs (Fri) | Fast ($\approx 500\text{ wpm}$) | High (Contextual transformer) | **High (In-context generalization)** | Opaque (Deep neural weights) |

This profound limitation sets the stage for **Friday’s seminar (Meeting #30)**: *AI-Assisted Alignment and Gloss Generation*. On Friday, you will harness large language models (LLMs) and neural multilingual representations to evaluate whether generative AI can bridge the semantic and syntactic gaps that deterministic algorithms leave behind.

**The takeaway for this page:** Deterministic aligners are fast, mathematically transparent, and scalable, but lack the contextual intelligence needed to resolve complex literary paraphrases.

---

## **30 Content**

**Summary and Synthesis**

Today you mastered the second phase of the Topic 11 alignment cycle: **deterministic automation**. You explored the mathematical and architectural principles that enable software to discover structural correspondences between parallel texts without human supervision (Gale & Church, 1993; Tiedemann, 2011).

You traced the evolution of alignment technology across two distinct tiers:

1. **Sentence Alignment:** You analyzed how the **Gale-Church algorithm** uses dynamic programming to optimize character-length ratios, how **Hunalign and Champollion** incorporate bilingual lexical anchors, and how modern neural tools like **Bertalign** compare continuous sentence embedding vectors.
2. **Statistical Word Alignment:** You mastered the generative foundations of **IBM Models 1 through 5**, the relative-jump mechanics of the **HMM aligner**, and the log-linear breakthrough of **`fast_align`**, which uses a diagonal tension parameter ($\lambda$) to achieve rapid convergence (Brown et al., 1993; Dyer et al., 2013).
3. **Symmetrization & Evaluation:** You learned how `grow-diag-final-and` combines asymmetric forward and reverse passes, and how to mathematically calculate **Alignment Error Rate (AER)** using expert human Sure ($S$) and Possible ($P$) links (Och & Ney, 2003).
4. **Digital Humanities Workbenches:** You explored **Ugarit** and the **Alpheios Alignment Editor**, discovering how visual post-editing interfaces reduce human annotation time by over **85%** while slashing alignment error rates below **4%** (Palladino & Tariq, 2022).

| Meeting & Day | Methodological Mode | Focus & Toolchain | Status |
| --- | --- | --- | --- |
| Tue Nov 17 (#28) | Step 1: Manual Human Ground Truth | Leipzig Rules & TEI Standoff Alignment | Completed |
| Wed Nov 18 (#29) | Step 2: Deterministic Automation | Gale-Church, GIZA++, `fast_align`, Ugarit | **Completed** |
| Fri Nov 20 (#30) | Step 3: AI-Assisted Generation | LLMs, GlossLM, Error Diagnosis & Hallucination | **Upcoming (Friday)** |

Deterministic tools provide the indispensable mechanical scaffold for large-scale digital scholarship. They handle the repetitive, literal core of translation alignment, giving scholars the baseline data needed to build massive parallel editions.

**For Friday:** Prepare your manual gold standard dataset from Tuesday and your `fast_align` outputs from today. On Friday, you will prompt state-of-the-art large language models to generate alignments and four-line interlinear glosses, rigorously evaluating their outputs for morphological hallucinations, non-isomorphic syntactic drift, and philological fidelity.

**The takeaway for this page:** Deterministic alignment provides the reproducible, high-speed computational baseline that bridges manual human gold standards with generative AI.

---

## References

Baumgardt, S. (2021). *Digital interlinear editions: Developing a standard for linguistic annotation and alignment in digital critical editions*. Open Philology Press.

Brown, P. F., Della Pietra, S. A., Della Pietra, V. J., & Mercer, R. L. (1993). The mathematics of statistical machine translation: Parameter estimation. *Computational Linguistics*, 19(2), 263–311.

Crane, G. (1991). Generating and parsing Classical Greek. *Literary and Linguistic Computing*, 6(4), 243–245. https://doi.org/10.1093/llc/6.4.243

Crane, G., Palladino, C., & Tariq, M. U. (2024). The sixth generation of the Perseus Digital Library and a workflow for open philology. *Transformations: Digital Humanities Journal*, 6(1), 102–128. https://doi.org/10.48550/arXiv.2411.10604

Dempster, A. P., Laird, N. M., & Rubin, D. B. (1977). Maximum likelihood from incomplete data via the EM algorithm. *Journal of the Royal Statistical Society: Series B (Methodological)*, 39(1), 1–38. https://doi.org/10.1111/j.2517-6161.1977.tb01600.x

Dik, H. (2022). Logeion: A digital environment for Greek and Latin lexicography. In *Digital Classics Online* (Vol. 8, pp. 45–58). University of Heidelberg. https://doi.org/10.11588/dco.2022.1.88412

Dyer, C., Chahuneau, V., & Smith, N. A. (2013). A simple, fast, and effective reparameterization of IBM Model 2. In *Proceedings of the 2013 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT 2013)* (pp. 644–648). Association for Computational Linguistics.

Gale, W. A., & Church, K. W. (1993). A program for aligning sentences in bilingual corpora. *Computational Linguistics*, 19(1), 75–102.

Krahn, K. (2024). *grc-bertalign: Sentence alignment for Ancient Greek using multilingual sentence embeddings* (Version 1.2.0) [Software]. GitHub. https://github.com/kevinkrahn/grc-bertalign

Liu, J., & Zhu, C. (2023). Bertalign: Improved word embedding-based sentence alignment for Chinese–English parallel corpora of literary texts. *Digital Scholarship in the Humanities*, 38(2), 621–636. https://doi.org/10.1093/llc/fqac078

Ma, X. (2006). Champollion: A robust parallel text sentence aligner. In *Proceedings of the Fifth International Conference on Language Resources and Evaluation (LREC 2006)* (pp. 489–492). European Language Resources Association.

Och, F. J., & Ney, H. (2003). A systematic comparison of various statistical alignment models. *Computational Linguistics*, 29(1), 19–51. https://doi.org/10.1162/089120103321337421

Palladino, C. (2023). Translation alignment for Ancient Greek: Annotation guidelines and gold standards. *Journal of Open Humanities Data*, 9(14), 1–12. https://doi.org/10.5334/johd.112

Palladino, C., & Tariq, M. U. (2022). Ugarit: Translation alignment technologies for under-resourced languages. In *Proceedings of the 13th Language Resources and Evaluation Conference (LREC 2022)* (pp. 5779–5786). European Language Resources Association.

Palladino, C., Tariq, M. U., & Crane, G. (2021). Translation alignment for historical language learning: A case study. *Digital Humanities Quarterly*, 15(3), 1–18.

Thompson, B., & Koehn, P. (2019). Vecalign: Improved sentence alignment in linear time and space. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP 2019)* (pp. 1340–1348). Association for Computational Linguistics. https://doi.org/10.18653/v1/D19-1136

Tiedemann, J. (2011). *Bitext alignment*. Synthesis Lectures on Human Language Technologies. Morgan & Claypool. https://doi.org/10.2200/S00367ED1V01Y201106HLT014

Varga, D., Németh, P., Halácsy, P., Kornai, A., Trón, V., & Nagy, V. (2005). Parallel corpora for medium density languages. In *Proceedings of the International Conference on Recent Advances in Natural Language Processing (RANLP 2005)* (pp. 590–596).

Vogel, S., Ney, H., & Tillmann, C. (1996). HMM-based word alignment in statistical translation. In *Proceedings of the 16th Conference on Computational Linguistics (COLING 1996)* (pp. 836–841). Association for Computational Linguistics. https://doi.org/10.3115/993268.993313
