# Lesson 5.2 — Character and Word Error Rates: Measuring the Machine Passes

*RELS 398 / ENGL 398 · Topic 5: Reconciliation · Meeting #13 (Fri Oct 2)*

***Step 2 of a two-step week.** Today you compute character and word error rates
for the HTR and AI passes against Tuesday's consensus text, interpret what the
numbers do and do not say, and write the reconciliation report. **The
Transcription Assignment is due today.***

---

## **01 Content**

**What a Measurement Requires**

You now have everything a measurement needs: a calibrated reference and two
hypotheses to score against it.

Tuesday produced the consensus text, verified by double-keying and adjudicated
against the images. Week 4 produced two machine transcriptions of the same lines,
each committed raw and tagged before correction. Today computes the distance
between them.

The word "distance" is literal. Character error rate and word error rate are
normalized edit distances — the minimum number of single-unit changes needed to
turn the machine's output into the reference, divided by the reference's length.
The whole apparatus rests on one algorithm, and understanding that algorithm is
what lets you interpret its output rather than merely quoting it.

Today has three parts. First, the mathematics: edit distance, the algorithm that
computes it efficiently, and the two rates derived from it. Second, the
interpretation: what the numbers mean, what they conceal, and why the relationship
between CER and WER is often more informative than either alone. Third, the report:
a formal audit document recording how your text moved from manuscript image to
encoded XML.

**Vocabulary.** *Reference* — the ground truth against which output is scored.
*Hypothesis* — the output being scored. *Edit distance* — the minimum number of
single-unit edits transforming one string into another.

**The takeaway for this page:** CER and WER are normalized edit distances, and
understanding the algorithm is what lets you interpret the numbers rather than
quote them.

---

## **02 Content**

**Levenshtein Distance**

The foundation is the **Levenshtein distance**, formulated by Vladimir Levenshtein
in 1965. It quantifies the dissimilarity of two sequences as the minimum number of
single-character edit operations required to transform one into the other, where
the permitted operations are insertion, deletion, and substitution (Haaf et al.,
2013).

Three operations, and no others. Transposition — swapping adjacent characters — is
*not* a permitted operation in the standard formulation, which means that typing
"teh" for "the" counts as two edits rather than one. Variants exist that permit
transposition, but the standard measure does not, and error rates in the literature
assume the standard.

| Operation | Effect | Example |
| --- | --- | --- |
| Insertion | Add a character | λόγος → λόγοις |
| Deletion | Remove a character | λόγοις → λόγος |
| Substitution | Replace a character | λόγος → λόγου |

The minimum matters. There are many ways to transform one string into another; the
distance is the cost of the cheapest. Computing that minimum is the algorithmic
problem, because the number of possible transformation sequences grows
combinatorially with string length.

The recursive definition is mathematically clean and computationally hopeless:
implemented directly it recomputes the same subproblems exponentially many times,
which makes it unusable for sequences of any real length (Haaf et al., 2013).

**The takeaway for this page:** Levenshtein distance is the *minimum* number of
insertions, deletions, and substitutions — and transposition is not one of the
permitted operations.

---

## **03 Content**

**The Wagner–Fischer Algorithm**

The inefficiency was resolved by the Wagner–Fischer algorithm in 1974, which
computes the edit distance by bottom-up dynamic programming in O(mn) time and
space, where m and n are the lengths of the two strings (Haaf et al., 2013).

The idea is to build a matrix *D* of dimensions (m+1) × (n+1), where D[i][j] holds
the edit distance between the first i characters of the reference and the first j
characters of the hypothesis. Each cell is computed from three neighbours, and the
answer lands in the bottom-right corner.

The extra row and column are the part that confuses people, and they are
mathematically necessary. They represent the **empty string** — a prefix of length
zero. The first row records the cost of building the hypothesis from nothing, which
is j insertions; the first column records the cost of reducing the reference to
nothing, which is i deletions (Haaf et al., 2013).

The recurrence:

```text
D[i][j] = min(
    D[i-1][j]   + 1,              # deletion
    D[i][j-1]   + 1,              # insertion
    D[i-1][j-1] + cost            # substitution or match
)
where cost = 0 if reference[i] == hypothesis[j], else 1
```

Each cell asks: what is the cheapest way to reach this state? Delete a character
from the reference and take the answer from above; insert a character into the
hypothesis and take the answer from the left; or match or substitute and take the
answer from the diagonal.

The value in D[m][n] is the Levenshtein distance. And by tracing the optimal path
backwards from D[m][n] to D[0][0], you recover the *alignment* — the precise
correspondence showing exactly where a model hallucinated a character or where a
transcriber skipped a word (Haaf et al., 2013).

**The takeaway for this page:** The extra row and column represent the empty
string, and back-tracing the matrix recovers not just the distance but the exact
alignment of errors.

---

## **04 Content**

**Implementing It**

Write this yourself rather than importing a library. The point is not the number
but understanding what produces it.

```python
import unicodedata


def edit_distance(ref, hyp):
    """Wagner-Fischer. ref and hyp are sequences (str or list of str)."""
    m, n = len(ref), len(hyp)
    # Row 0 is the cost of building hyp from the empty string.
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        # Column 0 is the cost of reducing ref to the empty string.
        cur = [i]
        for j in range(1, n + 1):
            cost = 0 if ref[i - 1] == hyp[j - 1] else 1
            cur.append(min(prev[j] + 1,          # deletion
                           cur[j - 1] + 1,       # insertion
                           prev[j - 1] + cost))  # substitution
        prev = cur
    return prev[n]


def cer(reference, hypothesis):
    r = unicodedata.normalize("NFC", reference)
    h = unicodedata.normalize("NFC", hypothesis)
    return edit_distance(r, h) / len(r) if r else 0.0


def wer(reference, hypothesis):
    r = unicodedata.normalize("NFC", reference).split()
    h = unicodedata.normalize("NFC", hypothesis).split()
    return edit_distance(r, h) / len(r) if r else 0.0
```

Note three implementation details. The function keeps only the previous row rather
than the whole matrix, which reduces space from O(mn) to O(n) — fine for computing
a distance, though recovering the alignment requires the full matrix.

Both inputs are NFC-normalized. This is not optional, and it is the single most
common source of wrong error rates in student work. Comparing an NFC reference
against NFD machine output measures encoding difference rather than transcription
difference, and the inflation can be severe on polytonic Greek.

And `wer` is the same algorithm over a different unit: tokenize by whitespace and
run the identical matrix logic on lists of words rather than on characters (Haaf et
al., 2013).

Save this as `tools/cer.py` and commit it.

**The takeaway for this page:** WER is the same algorithm over whitespace tokens —
and NFC-normalizing both inputs is what stops you measuring encoding difference.

---

## **05 Content**

**The Definitions of CER and WER**

Formally, both rates normalize the raw edit distance against the length of the
reference (Haaf et al., 2013):

```text
CER = (S + D + I) / N
```

where S is substitutions, D is deletions, I is insertions, and N is the total
number of characters in the verified reference.

WER uses the identical formula with the token as the unit rather than the
character.

| | CER | WER |
| --- | --- | --- |
| Unit | Character | Whitespace-delimited token |
| Denominator | Characters in the reference | Words in the reference |
| Sensitive to | Individual character errors | Any error within a word |
| Typical magnitude | Lower | Higher |

One property surprises people and is worth stating explicitly: **CER can exceed
100%.** Insertions are added to the numerator without any corresponding increase in
the denominator N, so a model that generates long strings of garbage from a
degraded image can produce an error rate above 1.0 (Haaf et al., 2013).

This is not a bug in the metric; it is a correct report that the hypothesis
contains more wrong material than the reference contains material at all. If you
see a CER above 100% today, the model has hallucinated substantially, and that is
the finding.

WER is systematically higher than CER because a single wrong character within a
twenty-character word makes the whole word wrong under this evaluation (Haaf et
al., 2013). A model with 5% CER distributed across many words may have a WER
several times higher.

**The takeaway for this page:** CER can exceed 100% because insertions add to the
numerator but not the denominator — a rate above 1.0 means substantial
hallucination.

---

## **06 Content**

**The Relationship Between CER and WER**

The two numbers together carry diagnostic information that neither carries alone,
and this is the most useful analytical tool in today's session.

Because WER counts a word wrong for any character error within it, the ratio
between the rates depends on how errors are *distributed*. Errors concentrated in
few words produce a low WER relative to CER; errors scattered across many words
produce a high WER relative to CER.

| Pattern | Likely cause |
| --- | --- |
| CER low, WER proportionally low | Few errors, concentrated |
| CER low, WER disproportionately high | Errors scattered one per word — often diacritics |
| CER low, WER very high (2× or more than expected) | Systemic word-boundary failure |
| CER high, WER near 100% | Widespread failure |
| CER high, WER lower than expected | Errors concentrated in a damaged region |

The third row is the important diagnostic. A model producing 4% CER and 25% WER is
almost certainly suffering systemic tokenization or boundary detection failure —
arbitrarily inserting whitespace and fracturing cohesive lexical units into
fragments (Haaf et al., 2013). The characters are largely right; the word divisions
are not.

Two causes produce this in your material specifically. If your manuscript uses
*scriptio continua*, the model recognizes characters correctly and fuses them into
concatenated tokens, as Lesson 4.1 section 13 anticipated. And line-end hyphenation
is a persistent anomaly: models frequently fail to reconstruct a word fractured
across a line break, treating the two fragments as unrelated tokens, which inflates
WER and destroys semantic coherence (Bawden et al., 2026).

Compute both rates and report the ratio. If it is anomalous, diagnose it — the
explanation is a finding.

**The takeaway for this page:** Low CER with disproportionately high WER means
word-boundary failure, not character misreading — diagnose it rather than reporting
it flatly.

---

## **07 Content**

**Preparing the Texts for Comparison**

Before measuring, both texts must be reduced to comparable form. Decisions here
change the numbers, so make them deliberately and record them.

| Decision | Options | Recommendation for this course |
| --- | --- | --- |
| Markup | Strip tags, or compare encoded text | Strip; compare the text stream |
| Normalization | NFC, NFD, or as-is | NFC, both sides, always |
| Case | Preserve or fold | Preserve; case is diplomatic evidence |
| Whitespace | Preserve, collapse, or strip | Collapse runs to single spaces |
| Line breaks | Compare per line, or as one stream | Per line, where alignment permits |
| Punctuation | Include or exclude | Include; record the choice |
| Conversational framing | Strip before comparison | Strip; do not measure preamble |

Every one of these changes the result, which is why the reconciliation report must
state them. A CER of 6.2% computed with case folded and punctuation excluded is not
comparable to 6.2% computed strictly, and a report that omits the preprocessing is
not reproducible.

Extract the text stream from your TEI consensus:

```python
import re, unicodedata
from pathlib import Path

def text_stream(path):
    xml = Path(path).read_text(encoding="utf-8")
    body = re.search(r"<body>(.*?)</body>", xml, re.S).group(1)
    text = re.sub(r"<[^>]+>", "", body)            # strip markup
    text = re.sub(r"\s+", " ", text).strip()       # collapse whitespace
    return unicodedata.normalize("NFC", text)
```

One caution on stripping markup. `<expan>` contains editor-supplied expansions and
`<abbr>` contains what is on the page. Stripping all tags concatenates both, which
would compare a doubled text. Decide which layer you are measuring — for a
diplomatic comparison it is `<abbr>` — and extract that consistently from both
sides.

**The takeaway for this page:** Preprocessing decisions change the number, so
record them — and when stripping markup, choose the `<abbr>` or `<expan>` layer
deliberately.

---

## **08 Content**

**Measuring Per Line**

Whole-text figures hide the distribution. Measure per line and report both.

```python
results = []
for n, ref_line in consensus_lines:
    hyp_line = htr_lines.get(n, "")
    results.append({
        "line": n,
        "cer": cer(ref_line, hyp_line),
        "wer": wer(ref_line, hyp_line),
        "chars": len(ref_line),
    })

overall = sum(r["cer"] * r["chars"] for r in results) / sum(r["chars"] for r in results)
```

Note the weighting in the overall figure. A simple mean of per-line rates weights a
three-character line equally with a sixty-character one, which distorts the result.
Weight by reference length, or equivalently compute the total edit distance over
the total reference length.

Per-line results let you see what an aggregate conceals:

| Distribution | Interpretation |
| --- | --- |
| Uniform, low | The model handles this hand consistently |
| Uniform, moderate | A systematic issue — diacritics, conventions |
| Mostly low, a few very high | Localized difficulty: damage, a gloss, a layout fault |
| Rising through the folio | Possible alignment drift; check line correspondence |
| One line at 100%+ | That line's image is probably wrong — check the polygon |

The last two rows are diagnostic rather than descriptive. Steadily rising error
through a folio suggests the hypothesis has drifted out of alignment with the
reference — an off-by-one from a split or merged line — and the fix is realignment
rather than model improvement. A single catastrophic line usually means the layout
analysis produced a bad line image, which is the Lesson 4.2 section 02 cascade.

Report the distribution, not just the mean.

**The takeaway for this page:** Weight the overall rate by line length, and read
the per-line distribution — rising error means misalignment, not model failure.

---

## **09 Content**

**Aligning the Machine Outputs**

Before per-line measurement is possible, the hypothesis must be line-aligned with
the reference. This is straightforward for the HTR output and may not be for the
VLM output.

HTR output is line-aligned by construction: the model operated on line images, and
its output carries line structure, exported in ALTO or PAGE XML with coordinates
(eScriptorium/Kraken, 2024). Map its lines to your `<lb/>` numbering and verify by
spot-check.

VLM output may not be. If the model reflowed the text into continuous prose — the
failure documented in Lesson 4.3 section 06 — you have three options:

| Option | Method | Cost |
| --- | --- | --- |
| Realign manually | Insert line breaks by comparing against the image | Slow; accurate |
| Measure whole-text only | Compare as one stream; report the limitation | Fast; less informative |
| Align algorithmically | Use CTC-style alignment against character posteriors | Sophisticated; needs model access |

The third option is the Bullinger solution from Lesson 5.1 section 16 and is
probably beyond today's scope, but knowing it exists matters. Peer et al. (2025)
used a CTC alignment algorithm to insert line breaks into layout-free expert
transcriptions so they matched the visual layout of the page, using dynamic
programming over character posterior probabilities — and improved a PyLaia model's
CER by 1.1 points in the process.

For today, realign manually if the folio is short, and otherwise measure whole-text
and state the limitation clearly. A whole-text CER is a valid measurement; it simply
cannot support per-line analysis, and the report must say so.

Do not compare a line-aligned HTR figure against a whole-text VLM figure without
noting that they were computed differently. That comparison is not like for like.

**The takeaway for this page:** HTR output is line-aligned by construction and VLM
output often is not — never compare a per-line figure against a whole-text one
without saying so.

---

## **10 Content**

**Computing Against Both Ground Truths**

An analysis worth performing, because it quantifies the value of Tuesday's work.

Compute each machine output's CER twice: once against Week 4's original ground
truth (`gt-f42r`) and once against Tuesday's consensus (`gt-f42r-consensus`).

| Comparison | Tells you |
| --- | --- |
| HTR against original ground truth | What Week 4 measured |
| HTR against consensus | The corrected measurement |
| Difference between them | How much of the measured error was yours |
| Same pair for the VLM output | The same, for the AI pass |

The difference is informative in a specific way. If HTR error against the original
was 6.8% and against the consensus is 5.9%, then roughly 0.9 percentage points of
what Week 4 attributed to the model was in fact error in your reference.

Retrieving the tagged states is what makes this possible:

```bash
git show gt-f42r:transcription/f42r_pass1.xml > /tmp/gt_original.xml
git show gt-f42r-consensus:transcription/f42r_consensus.xml > /tmp/gt_consensus.xml
git show htr-w4-raw:transcription/htr_output.txt > /tmp/htr_raw.txt
```

This is the payoff for the tagging discipline from Weeks 4 and 5. Without tags, the
original ground truth is simply gone — overwritten by Tuesday's corrections — and
this comparison could not be made at all.

Report both figures. Reporting only the flattering one, or only the corrected one
without noting the change, conceals a real fact about the reliability of your
earlier measurements.

**The takeaway for this page:** Measuring against both ground truths quantifies how
much of Week 4's "machine error" was yours — and only the tags make it retrievable.

---

## **11 Content**

**Interpreting the Numbers Against Thresholds**

With figures in hand, interpret them against established thresholds (AlKendi et
al., 2024):

| CER | Assessment | Supports |
| --- | --- | --- |
| Under 5% | Excellent | Minimal correction; publishable after proofreading; reliable for downstream NLP |
| 5–10% | Good, usable | Localized errors on abbreviations and ligatures; heavier editing for a critical edition; fine for corpus work |
| 10–15% | Marginal | Substantial correction required |
| Over 15% | Poor | Correction costs more than transcribing from scratch |

Apply these to your own results and state what they imply for your edition. If your
fine-tuned HTR model is at 6%, it is usable: extend transcription with it,
correcting its output. If your VLM output is at 45%, it is not, and the honest
conclusion is that zero-shot VLM transcription is unsuitable for this manuscript.

Two cautions on the thresholds. They are conditional on layout, as Lesson 4.2
section 18 established — a figure measured on standard pages may not hold on glossed
ones. And they describe *correction economics*, not scholarly adequacy: a 4% CER
model is economically usable and its output still requires checking before it enters
an edition.

The threshold that matters most is the last row, and it is worth restating because
it converts a quality judgement into a decision. Above roughly 15% CER, the
cognitive load and time to post-correct exceed the time to transcribe from scratch
(AlKendi et al., 2024). A tool above that line is not slow help; it is a net loss.

**The takeaway for this page:** Above 15% CER a tool is a net loss, not slow help —
the threshold converts a quality judgement into a decision.

---

## **12 Content**

**Why the Number Is Not Enough**

The central methodological argument of today, and the one your report must engage.

CER treats every difference identically. A substitution that drops a breathing and
a substitution that changes a letter both count as one edit. But their scholarly
consequences differ enormously, and a single aggregate cannot distinguish them.

The finding from Lesson 4.3 section 04 makes this concrete. GPT-4o achieved 9.23%
CER on eighteenth-century Russian — considerably better than a generic PyLaia
baseline at 26.93% — while inserting anachronistic archaic characters in 59% of
processed files. PyLaia scored far worse by the metric and never once fabricated a
grapheme (Levchenko, 2024).

Which model is better for a diplomatic edition? By CER, GPT-4o. By fidelity, PyLaia,
unambiguously — because a transcription that invents period-specific orthography is
not a transcription of the document.

Hence the conclusion that standard metrics are insufficient for historical text: a
model may achieve low CER while destroying the diplomatic fidelity of the
transcription through temporal hallucination (Levchenko, 2024).

Two supplementary measures address this:

| Metric | Measures | Detects |
| --- | --- | --- |
| Historical Character Preservation Rate | Proportion of period-specific characters preserved | Silent modernization |
| Archaic Insertion Rate | Frequency of hallucinated earlier-period characters | Over-historicization |

For your Greek, compute analogues. What proportion of polytonic diacritics survived
correctly? Were abbreviations preserved or expanded? Was *scriptio continua*
preserved or divided? Each is a fidelity measure that CER does not capture.

**The takeaway for this page:** A model can score better on CER while destroying
diplomatic fidelity — compute fidelity measures alongside the error rate.

---

## **13 Content**

**Building an Error Typology**

Classify the errors rather than merely counting them. The classification is what
makes the report diagnostic rather than descriptive.

Use the alignment from the Wagner–Fischer back-trace to extract each error with its
context, then categorize:

| Category | Example | Diagnostic significance |
| --- | --- | --- |
| Confusable letterform | One letter read as a similar one | Palaeographic; add to `HAND.md` |
| Diacritic omitted | Breathing or accent missing | Possibly a polygon truncation fault |
| Diacritic wrong type | Acute for grave | Convention or contextual rule |
| Abbreviation expanded | θς rendered θεός | Silent normalization |
| Word boundary error | Two words fused or one split | Tokenization; inflates WER |
| Line-end fracture | Word split across lines not rejoined | Structural; a known HTR anomaly |
| Impossible sequence | Non-Greek letter sequence | CTC uncertainty; conspicuous, benign |
| Plausible wrong word | Correct Greek, wrong reading | Language-model substitution; dangerous |
| Fabricated text | Content with no ink behind it | Hallucination; the most serious |

The audit should classify the most frequent substitutions and identify systematic
bias — does the model consistently confuse a particular letter pair, or hallucinate
punctuation where none exists? Identifying these biases dictates the parameters
required for any subsequent normalization phase (Haaf et al., 2013).

The last two rows are the ones to report prominently if present. A plausible wrong
word is dangerous because post-correction will not catch it by reading; fabricated
text is more serious still. Both are language-model behaviours, and finding either
in your VLM output on your own manuscript is a substantive result.

Count each category and report counts alongside the aggregate rate.

**The takeaway for this page:** Categorized errors identify systematic bias; an
aggregate rate cannot — and plausible wrong words are the ones post-correction will
miss.

---

## **14 Content**

**Why Error Rates Matter Downstream**

A reason to care about these numbers beyond the assignment, and the strongest
available argument for post-correction.

Transcription noise degrades downstream computational analysis severely and
non-linearly. Standard NLP tools are trained overwhelmingly on clean modern
corpora, and noisy historical text harms them in ways that differ by task (van
Strien et al., 2020).

**Part-of-speech tagging** degrades roughly linearly with error rate, crossing into
uselessness at approximately 5% CER. The mechanism is specific: taggers rely
heavily on morphological suffixes to determine syntactic category, and suffixes are
exactly what character-level substitution corrupts (van Strien et al., 2020).

**Named entity recognition** fails catastrophically rather than gradually. NER
F-scores drop from an acceptable 90% to a useless 60% when WER rises from 1% to
just 7%, or when CER rises from 8% to 20% (van Strien et al., 2020).

| Task | Degradation | Threshold of uselessness |
| --- | --- | --- |
| POS tagging | Roughly linear | Around 5% CER |
| NER | Catastrophic cascade | 7% WER, or 20% CER |

The reason NER collapses is worth understanding. Named entities have low textual
redundancy: a common word misspelled once is recoverable from context and from its
other occurrences, but if a proper name is corrupted by a single character the
entire entity is lost to the index. Worse, named entities frequently *are* the
out-of-vocabulary terms that recognition models handle worst — so errors concentrate
precisely on the tokens that can least afford them (van Strien et al., 2020).

This bears directly on Week 9's lemmatization and Week 12's commentary. Without
post-correction, extracting historical actors and geographic networks from noisy
transcription is statistically invalid (van Strien et al., 2020).

**The takeaway for this page:** NER collapses from 90% to 60% F-score as WER goes
from 1% to 7%, because proper names have no redundancy to recover from.

---

## **15 Content**

**Pre-Editorial Normalization**

A method that bridges raw HTR output and the clean text downstream tools require,
and which anticipates next week.

**Pre-editorial normalization** algorithmically normalizes graphemic recognition
output according to standard editorial conventions before final human curation
(Bawden et al., 2026). The motivation is the gap identified in section 14: graphemic
models trained on specialized datasets preserve historical variation and generalize
well across hands, but produce output that breaks modern NLP tools.

Implementations use byte-level sequence-to-sequence transformers such as ByT5,
which ingest graphemic output and generate a pre-edited text — resolving scribal
abbreviations contextually, normalizing ramist letters on vocalic or consonantal
usage, and rectifying standard recognition confusions such as a minim sequence read
as one letter rather than another (Bawden et al., 2026).

The danger is over-normalization. Processing historical texts with fluid
orthography, such models frequently collapse historically significant dialectal
variants into a single standard form, permanently erasing linguistic evidence. They
may also hallucinate whole strings when encountering severe recognition noise,
generating grammatically coherent but entirely fabricated prose to bridge an
illegible gap (Bawden et al., 2026).

Hence strict constraints are required: abbreviations corresponding to proper names
without contextual clarity must remain unexpanded, and continuous spans of severe
noise must be flagged for human review rather than algorithmically overwritten.
Under those constraints, a tightly controlled ByT5 model achieved 6.7% CER on
medieval manuscripts while substantially accelerating the human editorial workflow
without sacrificing palaeographic integrity (Bawden et al., 2026).

The architecture to note: normalization is a *separate layer* over a preserved
graphemic base, with explicit constraints and human review of uncertain regions.
That is exactly Week 6's design.

**The takeaway for this page:** Automated normalization works under strict
constraints — unexpanded proper names, human review of noisy spans — and erases
dialectal evidence without them.

---

## **16 Content**

**The Reconciliation Audit Report**

Today's deliverable. The report ensures epistemological transparency, recording
exactly how the text moved from raw manuscript image to final encoded XML (Haaf et
al., 2013).

Five required components (Haaf et al., 2013):

**1. Ground truth sampling and agreement validation.** Define which material was
double-keyed to serve as ground truth. Document inter-annotator agreement to
establish that the transcribers reached high consensus, which is what verifies the
reference's reliability before anything is benchmarked against it.

**2. Error rate benchmarking.** Declare CER and WER for all automated outputs.
Identify divergence between the two: if CER is 4% and WER is an anomalous 25%, the
audit must explicitly identify systemic tokenization or boundary detection failure.

**3. Error typology and systematic bias.** Classify the most frequent
substitutions. Does the model systematically confuse particular letterforms? Does
it hallucinate punctuation absent from the source? These biases dictate the
parameters for any subsequent normalization.

**4. Structural versus typographical divergence.** Differentiate characters misread
by the recognition system from XML structural errors. A missing closing tag is a
structural failure compromising the entire document object model, and it takes
absolute precedence over a minor typographical substitution.

**5. LLM parameterization and constraints.** Where a language model was used, append
the exact prompt. Demonstrate that the model was explicitly instructed to preserve
historically significant orthography, and include a statistical evaluation of its
false-positive rate for unprompted anachronistic normalizations.

Write these as `logs/reconciliation-report-w5.md`. Each has a direct counterpart in
work you have already done, and the report assembles rather than generates.

**The takeaway for this page:** The audit report has five required components, and
structural errors take precedence over typographical ones in reporting.

---

## **17 Content**

**Writing Component 1: Ground Truth Validation**

Assemble from Tuesday's work.

State which material was double-keyed, when each pass was made, and what interval
separated them. Confirm that pass 2 was independent, and cite the commit order as
evidence — this is a claim the repository substantiates rather than one you merely
assert.

Report agreement: overall character agreement between the passes, the per-line
distribution, and the number of disagreements adjudicated. Note how many resolved
toward each pass, since a strong skew is worth explaining.

Report the limitation honestly. Your double-keying used one transcriber twice
rather than two transcribers, which cannot catch systematic misunderstandings, as
Lesson 5.1 section 14 established. If a classmate reviewed lines, say which and what
that found.

Finally, report the figure from section 21 of Lesson 5.1: how far the original
ground truth was from the consensus. This is the quantified statement of how much
verification was needed.

| Validation item | Your figure |
| --- | --- |
| Lines double-keyed | Record |
| Interval between passes | Record |
| Disagreements found | Record |
| Resolved toward pass 1 / pass 2 / unresolved | Record |
| Overall character agreement | Record |
| Pass 1 CER against consensus | Record |
| Independent second reader | Record whether, and scope |

A reader of this section should be able to judge how much confidence your reference
deserves. That judgement conditions every number in the rest of the report.

**The takeaway for this page:** Component 1 lets a reader judge how much confidence
your reference deserves — including the limitation of self-double-keying.

---

## **18 Content**

**Writing Component 2: Error Rate Benchmarking**

Report the measurements, with their preprocessing.

| Output | Reference | CER | WER | Alignment | Preprocessing |
| --- | --- | --- | --- | --- | --- |
| HTR raw | Consensus | Record | Record | Per line | NFC; tags stripped; whitespace collapsed |
| HTR raw | Original GT | Record | Record | Per line | Same |
| VLM raw | Consensus | Record | Record | Record | Same, plus framing stripped |
| VLM raw | Original GT | Record | Record | Record | Same |

Then analyze the CER-to-WER relationship for each, per section 06. If the ratio is
anomalous, diagnose it and say so: *scriptio continua* fusing tokens, line-end
hyphenation fracturing words, or arbitrary whitespace insertion.

State preprocessing explicitly. A figure computed with punctuation excluded is not
comparable to one computed with it included, and a report whose preprocessing is
unstated is not reproducible.

Report the per-line distribution, not only the aggregate. A note that error is
uniform except for two lines over a damaged region is more informative than the
mean, and it tells a reader where the model's difficulty actually lies.

Include the difference between measurements against the two references, per section
10, with a sentence on what it implies for Week 4's reported figures.

**The takeaway for this page:** Report preprocessing, the per-line distribution,
and the CER-to-WER relationship — an aggregate alone is neither reproducible nor
diagnostic.

---

## **19 Content**

**Writing Components 3 and 4: Typology and Structure**

Component 3 assembles your error categorization from section 13. Report counts per
category for each machine output, and identify what is systematic.

The distinction to draw is between random and systematic error. A model that
misreads one letter once has made an error; a model that misreads the same letter
in eleven of fourteen occurrences has a systematic bias, and that bias is both more
serious and more tractable — it can be addressed by more training data on that
letterform, or by a targeted correction pass.

| Finding | Evidence to give |
| --- | --- |
| Systematic letterform confusion | The pair, occurrence count, proportion affected |
| Systematic diacritic loss | Which diacritics, and whether polygons were implicated |
| Silent abbreviation expansion | Count; which abbreviations |
| Hallucinated punctuation | Count; where it appears |
| Fabricated text | Line references; what the manuscript shows there |

Component 4 addresses structural divergence, which is measured differently.
Character-level metrics do not detect XML structural error at all, so this section
reports validation results rather than rates.

State whether each output was structurally valid, what structural errors were
present, and how they compare in severity to the typographical ones. The principle
is explicit: a missing closing tag compromises the entire document object model and
takes absolute precedence over a minor typographical substitution (Haaf et al.,
2013).

If your VLM output lost line structure entirely, that is a structural failure of the
first magnitude and belongs in this section rather than being absorbed into the
error rate.

**The takeaway for this page:** Systematic errors are more serious and more
tractable than random ones — and structural failure takes precedence over
typographical error.

---

## **20 Content**

**Writing Component 5: Model Parameterization**

The disclosure component, and the one that makes the study reproducible.

For the HTR model, record: the platform and version, the base model, the volume and
provenance of training data, the layout corrections applied, the training
configuration, the validation split, and the reported validation CER.

For the language model, record: the model name and version, the access date, the
verbatim prompt including any system instruction, and any parameters you controlled.

Then evaluate the constraint compliance. You instructed the model to preserve line
breaks, preserve orthography, leave abbreviations unexpanded, preserve word
division, and mark rather than fill illegible regions. Report, for each, whether it
complied.

| Instruction | Complied? | Evidence |
| --- | --- | --- |
| Preserve line breaks | Record | Line count comparison |
| Do not expand abbreviations | Record | Count of expansions |
| Preserve orthography | Record | Count of modernizations |
| Preserve word division | Record | Whitespace comparison |
| Mark illegible rather than fill | Record | Behaviour at known gaps |
| Output only the transcription | Record | Presence of framing |

That table is the statistical evaluation of the model's false-positive rate for
unprompted anachronistic normalization (Haaf et al., 2013). It states, on your
manuscript, how far explicit instruction constrained the model's behaviour — which
is more useful than any general claim about whether such models can be prompted into
diplomatic fidelity.

If you ran the memorization tests from Lesson 4.3 section 12, report them here.

**The takeaway for this page:** Report constraint compliance instruction by
instruction — that table measures how far explicit prompting actually constrained
the model.

---

## **21 Content**

**Drawing the Conclusion**

The report needs a conclusion, and it should be specific rather than general.

A weak conclusion: *AI transcription is unreliable for historical manuscripts.*
This repeats what you were told and is supported by your data only incidentally.

A strong conclusion states what you measured, on what material, with what
consequence:

> For MS Vat. gr. 1209, ff. 42r–43v — a tenth-century Greek minuscule imaged at
> 3000×4000 — a PyLaia model fine-tuned from Transkribus Titan on 24 lines of
> double-keyed ground truth achieved 5.9% CER and 18.2% WER against the consensus
> text. The CER-to-WER ratio reflects systematic word-boundary failure attributable
> to *scriptio continua*. Errors concentrate on breathings (14 of 41) and on the
> scribe's *kai* abbreviation (7 of 9 occurrences). Zero-shot transcription with
> [model] produced 38.4% CER, expanded all *nomina sacra* despite explicit
> instruction, and supplied confident readings at both regions encoded as `<gap/>`.
> The HTR model is therefore suitable for extending transcription across the
> remaining folios with per-line correction; the language model is not suitable for
> primary transcription of this manuscript.

That paragraph is defensible, specific, quantified, and actionable. It also
constitutes a real finding about a real manuscript, which is what the exercise is
for.

Include the cost comparison from Lesson 4.3 section 27. A conclusion about which
tool to use must weigh setup cost against per-folio saving, and for a short passage
the honest answer may be that manual transcription is competitive.

**The takeaway for this page:** State what you measured, on what material, with
what consequence for your edition — a general claim about AI is not a finding.

---

## **22 Content**

**The Transcription Assignment**

Due today. Its components, and where each comes from.

| Component | Source | Requirement |
| --- | --- | --- |
| Diplomatic transcription | Week 4 Tuesday | TEI-valid; fully encoded |
| Second independent pass | Week 5 Tuesday | Committed before comparison |
| Consensus text | Week 5 Tuesday | Adjudicated; unresolved cases preserved |
| HTR output, raw | Week 4 Wednesday | Committed separately; tagged |
| VLM output, raw | Week 4 Friday | Committed separately; tagged |
| Error rate measurements | Today | Both metrics, both references, preprocessing stated |
| Error typology | Today | Categorized with counts |
| Reconciliation report | Today | The five components |
| Conventions document | Week 4, amended Week 5 | Explicit and followed |
| Commit history | Throughout | Atomic, typed, with rationale and provenance trailers |

The last row is assessed, as it has been since Lesson 1.1. Provenance trailers on
machine-generated commits are part of it: a submission where machine output and
human transcription are indistinguishable in the history has not met the
requirement, regardless of the quality of the text.

Verify before submitting:

- All XML validates against the TEI schema.
- All text is NFC-normalized.
- All tags are pushed to the remote.
- The reconciliation report includes all five components.
- Preprocessing decisions are stated for every reported figure.
- The submission state is tagged.

**The takeaway for this page:** The commit history with provenance trailers is
assessed alongside the text — indistinguishable machine and human commits fail the
requirement.

---

## **23 Content**

**Tagging the Submission**

Mark the submitted state so it remains retrievable.

```bash
git tag -a submission-transcription \
  -m "Transcription Assignment as submitted, 2 Oct 2026"
git push --tags
```

This matters for the same reason as every other tag this term. The edition will
continue to change: Week 6 normalizes, Week 7 collates, Week 8 builds an apparatus.
Without a tag, the state that was submitted becomes unrecoverable within weeks, and
neither you nor an assessor can retrieve what was actually handed in.

Use the semantic versioning scheme from Lesson 1.1 section 26 if you prefer, tagging
this as `v1.0.0` and treating each subsequent assignment as a release. Either
convention is fine; consistency matters more than the choice.

Confirm the tag reached the remote. Tags are not pushed by default, and a tag
existing only in your local clone protects nothing.

```bash
git ls-remote --tags origin | grep submission
```

**The takeaway for this page:** Tag and push the submitted state — within three
weeks of further work it becomes otherwise unrecoverable.

---

## **24 Content**

**What the Two Weeks Established**

Consolidate, because Weeks 4 and 5 form one continuous argument.

Automated transcription requires a human diplomatic ground truth, because error
rates, biases, and hallucinated readings can be measured only against such a
baseline (AlKendi et al., 2024). That is the thesis, and you have now enacted every
part of it.

You produced the baseline by hand, diplomatically, at full zoom. You calibrated it
by double-keying, and quantified how far the uncalibrated version was off. You
trained a specialized model and measured it. You ran a general model and measured
it. And you have now reported all of it in a form that lets a reader evaluate the
claims.

| Week 4 | Week 5 |
| --- | --- |
| Manual diplomatic transcription | Double-keying and consensus |
| Layout correction and HTR training | — |
| Zero-shot VLM transcription | CER and WER measurement |
| Error categorization | Error typology and audit report |

The empirical findings — the specialization gap, over-historicization, the
CER-to-WER diagnostic, the correction threshold, the downstream NLP cascade — are
not opinions about technology. They are measurements, several of which you have
now replicated on your own manuscript.

That replication is the point. You are no longer relying on the literature's
account of what these tools do; you have a figure for your own material, produced
by a method you can defend.

**The takeaway for this page:** You now have measured figures for your own
manuscript rather than the literature's account — which is what makes your tool
choices defensible.

---

## **25 Content**

**Checklist Before Submitting**

Verify each.

- `tools/cer.py` written, tested, and committed.
- Both machine outputs extracted from their tags.
- Text streams prepared identically for both sides.
- Both sides NFC-normalized.
- CER and WER computed for both outputs against the consensus.
- The same computed against the original ground truth.
- Per-line distributions computed and inspected.
- CER-to-WER relationship analyzed and any anomaly diagnosed.
- Errors categorized with counts.
- Fidelity measures computed: diacritic preservation, abbreviation preservation.
- Structural validity checked for both outputs.
- Constraint compliance evaluated for the language model.
- Reconciliation report written with all five components.
- Preprocessing stated for every figure.
- Conclusion drawn specifically, with cost as well as quality.
- Everything committed, tagged, and pushed.

If any figure cannot be computed — because the VLM output could not be line-aligned,
for instance — state that as a limitation rather than omitting it. A reported
limitation is a finding; a silent gap is not.

**The takeaway for this page:** State what could not be computed as a limitation
rather than omitting it — a silent gap is worse than a reported one.

---

## **26 Content**

**Common Problems Today**

Failures that recur.

| Symptom | Cause | Remedy |
| --- | --- | --- |
| CER implausibly high | Normalization mismatch | NFC both sides |
| CER above 100% | Hallucinated insertions | Correct behaviour; report it as a finding |
| WER far above CER | Word-boundary failure | Diagnose; likely *scriptio continua* or hyphenation |
| Error rises steadily through the folio | Alignment drift | Realign; recompute |
| One line at enormous error | Bad line image from layout | Check the polygon |
| HTR and VLM figures not comparable | Different alignment methods | State the difference explicitly |
| Rate differs from the platform's report | Different preprocessing | Expected; state yours |
| Markup inflating the comparison | Tags not stripped, or both layers included | Extract one layer consistently |

The last row catches people and produces wildly wrong numbers. If you strip all
tags from a `<choice><abbr>θς</abbr><expan>θεός</expan></choice>` you get `θςθεός` —
both layers concatenated — which will not match anything and will inflate the error
rate substantially. Extract the `<abbr>` layer for a diplomatic comparison, and do
it the same way on both sides.

The seventh row is worth stating in the report rather than resolving. Transkribus
computes its validation CER with its own preprocessing, which may differ from yours.
Your figure is not wrong because it differs; it is computed differently, and saying
so is the correct response.

**The takeaway for this page:** Stripping all tags concatenates `<abbr>` and
`<expan>` into nonsense — extract one layer consistently on both sides.

---

## **27 Content**

**What Good Work Looks Like Here**

The standard for the report.

A minimally acceptable report gives CER and WER for both outputs and describes the
errors.

Good work additionally:

- States all preprocessing so the figures are reproducible.
- Measures against both references and explains the difference.
- Reports per-line distributions rather than aggregates alone.
- Diagnoses the CER-to-WER relationship rather than reporting it flatly.
- Computes fidelity measures that CER cannot capture.
- Distinguishes systematic from random error with evidence.
- Separates structural from typographical failure.
- Reports the language model's constraint compliance instruction by instruction.
- Weighs cost against quality.
- Reaches a specific, actionable conclusion about this manuscript.
- States its own limitations, including the weakness of self-double-keying.

The last item is the one that most distinguishes a careful report. Every study has
limitations, and a report that names its own — the reference was verified by one
person twice; the VLM output could not be line-aligned; the measurement covers one
folio of one hand — is more trustworthy than one that presents its figures without
qualification.

That is a general property of scholarly work, and it is the disposition this course
is trying to build.

**The takeaway for this page:** A report that names its own limitations is more
trustworthy than one presenting figures without qualification.

---

## **28 Content**

**Looking Ahead to Week 6**

Next week normalizes, and it returns to the full three-step cycle.

| Meeting | Step | Activity |
| --- | --- | --- |
| Tue Oct 6 (#14) | Manual | Regularize by hand, recording each decision |
| Wed Oct 7 (#15) | Deterministic | Rule-based normalization with a script |
| Fri Oct 9 (#16) | AI-assisted | AI normalization, checked against your own rules |

The subject is iotacism, orthographic variants, and `<orig>`/`<reg>` markup. The
architecture is the one section 15 described and the DTA exemplified: normalization
as a separate layer over a preserved diplomatic base, with both retained and the
relationship recorded.

Your consensus text is that base. Everything Week 6 does operates on it, and
because it is verified, the normalization decisions will be decisions about
orthography rather than entangled corrections of transcription error.

Note the caution that carries forward. Automated normalization tends to collapse
historically significant dialectal variants into standard forms, erasing linguistic
evidence permanently (Bawden et al., 2026). Week 6's Friday step will test exactly
that behaviour, and your hand-recorded rules from Tuesday will be the reference —
the same structure as this week, applied to a different operation.

**The takeaway for this page:** Week 6 normalizes as a separate layer over your
verified consensus, with Tuesday's hand-recorded rules as Friday's reference.

---

## **29 Content**

**The Method Generalizes**

A closing observation about what these two weeks have actually taught.

The procedure was: establish a reference by hand, verify the reference, apply
automated methods, measure the distance, categorize the differences, and report
with limitations stated. Nothing in that procedure is specific to transcription.

Week 6 will apply it to normalization: hand-recorded rules as reference, a
deterministic script and an AI pass measured against them. Week 7 will apply it to
collation: hand collation as reference, CollateX and AI variant classification
measured against it. Weeks 8 through 12 continue the pattern.

| Week | Reference established by hand | Measured against it |
| --- | --- | --- |
| 4–5 | Diplomatic transcription | HTR; vision-language model |
| 6 | Normalization decisions | Rule-based script; AI normalization |
| 7 | Manual collation | CollateX; AI variant classification |
| 8 | Hand-encoded apparatus | Generated apparatus; AI drafting |
| 9 | Manual lemmatization | CLTK pipeline; AI parsing |

Read the middle column. Every week requires you to do the thing yourself first,
and every week the reason is the same one this week made explicit: you cannot
measure a tool against a reference the tool produced, and a reference you have not
verified produces measurements that look precise and are not.

That is the course's method, and after two weeks of executing it you should be able
to state why it is ordered as it is.

**The takeaway for this page:** Every remaining week repeats this procedure on a
different operation — establish a reference by hand, verify it, measure against it.

---

## **30 Content**

**Synthesis: What the Numbers Are For**

The argument of this meeting.

Character and word error rates are normalized edit distances computed by an
algorithm from 1974 over a metric from 1965 (Haaf et al., 2013). They are precise,
cheap, and comparable across texts of different lengths, and they are the standard
currency of evaluation in document analysis.

They are also insufficient on their own, in three specific ways this session has
developed. They weight every difference equally, so a lost breathing counts the same
as a lost letter. They can be excellent while diplomatic fidelity is destroyed, as
GPT-4o's 9.23% CER with archaic insertion in 59% of files demonstrates (Levchenko,
2024). And they are conditional on preprocessing, alignment, and layout in ways that
make an unqualified figure close to meaningless.

What makes them useful is everything around them: a verified reference, stated
preprocessing, per-line distribution, error typology, fidelity measures, structural
validation, and honest limitations. That surrounding apparatus is the reconciliation
report, and it is why the report rather than the number is today's deliverable.

The disposition to carry forward is that a measurement is an argument. It has
premises — the reference, the preprocessing, the alignment — and its conclusion is
only as good as they are. An editor who reports a figure without them has asserted
rather than measured.

**Due today.** The Transcription Assignment, including the reconciliation report.
Tag and push the submitted state.

**For Tuesday.** Week 6 begins normalization, working over your consensus text.
Bring it validated, and bring your conventions document — Tuesday's regularization
decisions extend it.

**The takeaway for this page:** A measurement is an argument whose premises are the
reference, the preprocessing, and the alignment — reporting a figure without them is
assertion, not measurement.

---

## References

AlKendi, W., Gechter, F., Heyberger, L., & Guyeux, C. (2024). Advancements and
challenges in handwritten text recognition: A comprehensive survey. *Journal of
Imaging*.

Bawden, R., Clérice, T., Glaise, A., Pinche, A., & Smith, D. (2026).
*Pre-editorial normalization for automatically transcribed medieval manuscripts in
Old French and Latin* (arXiv:2602.13905). https://arxiv.org/abs/2602.13905

eScriptorium/Kraken. (2024). *eScriptorium platform documentation*.
https://escriptorium.eu/about

Haaf, S., Wiegand, F., & Geyken, A. (2013). Measuring the correctness of
double-keying: Error classification and quality control in a large corpus of
TEI-annotated historical text. *Journal of the Text Encoding Initiative*, (4).
https://doi.org/10.4000/jtei.739

Levchenko, M. A. (2024). *Evaluating LLMs for historical document OCR: A
methodological framework for digital humanities*.

Peer, M., Scius-Bertrand, A., & Fischer, A. (2025). CTC transcription alignment of
the Bullinger letters: Automatic improvement of annotation quality. In *ICCV
Workshop Proceedings*. IEEE.

Singh, L. G., & Middleton, S. E. (2025). Tabular context-aware optical character
recognition and tabular data reconstruction for historical records.
*International Journal on Document Analysis and Recognition, 28*.
https://doi.org/10.1007/s10032-025-00543-9

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/

van Strien, D., Beelen, K., Ardanuy, M. C., Hosseini, K., McGillivray, B., &
Colavizza, G. (2020). Assessing the impact of OCR quality on downstream NLP tasks.
In *Proceedings of the 12th International Conference on Agents and Artificial
Intelligence*. INSTICC. https://doi.org/10.5220/0009169004840496
