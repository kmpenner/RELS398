# Lesson 14.2 — Automated Alignment with CollateX

*RELS 398 / ENGL 398 · Topic 14: Collation · Meeting #18 (Wed Oct 21)*

***Step 2 of the three-step cycle: deterministic.** Today you configure CollateX
from Tuesday's method document, run it over the same passage, and measure how far
the algorithm reproduces your manual collation.*

---

## **01 Content**

**From Judgement to Configuration**

Yesterday you collated by hand and discovered, in the process, how many decisions
you were making without stating them. Today you state them, as configuration.

The shift is the one Tuesday's section 05 anticipated. Automated collation forces
the editor to make normalization rules explicit *before* alignment begins, moving
the critical philological labour away from the physical act of reading and comparing
and toward data modelling and algorithm configuration (Fradejas Rueda, 2022).

This is not a smaller task than yesterday's. It is a different one, and it is
frequently harder, because a decision you can make instantly on a particular case
may be genuinely difficult to state as a general rule — the same discovery Lesson
6.2 made about normalization.

What you gain is exactness and scale. Automated collation eliminates physical
fatigue and ensures absolute, mathematical reproducibility: every decision is
explicit (Fradejas Rueda, 2022). Where yesterday's twenty-eight lines took a
session, today's configuration will collate the same lines in under a second and the
next two hundred in not much longer.

What you must supply is everything your expertise supplied silently. Computers are
inherently, recalcitrantly literal: left unconfigured, the alignment algorithm will
flag a capital letter against a lowercase one as a substantive, sequence-breaking
variation (Fradejas Rueda, 2022).

**Vocabulary.** *Alignment* — establishing correspondences between tokens across
witnesses. *Tokenization* — dividing text into comparable units. *Normalization* —
here, neutralizing non-significant variation before alignment.

**Takeaway:** Configuration is not a smaller task than manual
collation, but a different one — stating as a rule what you decided case by case.

---

## **02 Content**

**The Gothenburg Model**

Before running anything, understand the architecture, because every configuration
decision belongs to a specific stage of it.

The modern architecture of automated collation was formalized in 2009 by the
Interedition project as the **Gothenburg Model**, which enforces a strict separation
of concerns, breaking collation into five modular operations so that individual
components can be upgraded or swapped without destabilizing the whole (Haentjens
Dekker & Middell, 2011).

| Stage | Function |
| --- | --- |
| Tokenization | Divide the character sequence into minimal units, typically words, identified by spaces, punctuation, or markup |
| Normalization | Prepare tokens for alignment by neutralizing non-significant variation — case folding, resolving abbreviations, neutralizing orthographic variance — without altering the archival transcription |
| Alignment | Establish mathematical correspondences between tokens across witnesses |
| Analysis | Optionally refine the initial alignment by statistical or heuristic means, such as correcting misaligned near-matches |
| Visualization | Render the alignment into human-readable or machine-actionable output: variant tables, graphs, or TEI |

Two properties of this design matter for your work.

The normalization stage **does not alter the underlying transcription**; it creates a
secondary processing layer (Haentjens Dekker & Middell, 2011). This is the same
architecture as Week 6's `<choice>`: the diplomatic text is preserved and a parallel
form is used for computation. Your `<reg>` layer is precisely what this stage is
designed to consume.

And the stages are **separable**, which means you can intervene at each. Most of
today's work is at stages 1 and 2 — deciding what a token is and what differences to
neutralize — while stage 3 runs unchanged. That distribution is typical: alignment is
the part that is solved, and preparation is the part that requires philology.

**Takeaway:** Alignment is the solved part; tokenization and
normalization are where the philology goes, and they are where you will spend today.

---

## **03 Content**

**Needleman–Wunsch: Optimal Global Alignment**

The algorithmic core, which you will recognize.

Developed in 1970, the Needleman–Wunsch algorithm is the foundational method for
optimal **global alignment** — the best possible alignment across the entire length
of two sequences, obtained by dividing the problem into sub-problems in a dynamic
programming matrix (Needleman & Wunsch, 1970).

If that sounds familiar, it should. It is the same dynamic programming technique as
the Wagner–Fischer algorithm you implemented in Lesson 5.2. The difference is the
objective: Wagner–Fischer minimizes edit distance, Needleman–Wunsch maximizes an
alignment score. They are the same machinery pointed at complementary goals.

The scoring system has three parameters (Needleman & Wunsch, 1970):

| Parameter | Applies to | Sign |
| --- | --- | --- |
| Match | Identical tokens | Positive score |
| Mismatch | Different tokens aligned to each other | Negative penalty |
| Indel | A token aligned with a gap | Negative penalty |

The matrix is O(mn) for sequences of length m and n, and each cell takes the maximum
of three preceding states: the diagonal plus the match-or-mismatch score, the cell
above plus the gap penalty, or the cell to the left plus the gap penalty. After the
matrix is populated, a **traceback** from the bottom-right cell follows the path of
highest scores to the top-left, reconstructing the optimal alignment (Needleman &
Wunsch, 1970).

That traceback is what produces the alignment rather than merely a score — and it is
the same operation as the back-trace that recovered error alignment in Lesson 5.2
section 03.

The adaptation to text rests on a structural observation: textual sequences behave
mathematically like nucleotide sequences, which is why algorithms designed for
biological alignment transfer to identifying textual homology.

**Takeaway:** Needleman–Wunsch is the same dynamic programming as
Wagner–Fischer, maximizing alignment score rather than minimizing edit distance.

---

## **04 Content**

**Affine Gap Penalties and Scribal Reality**

The refinement that makes the algorithm philologically appropriate, and the one
worth understanding in detail.

Basic Needleman–Wunsch uses a **linear gap penalty**: a gap of ten words is
penalized as ten independent, sequential omissions, each costing the same
(Gotoh, 1982).

That model is wrong about scribes. As Tuesday's section 08 established, a scribe
skipping a phrase does so in a single cognitive event — most often through
*homoioteleuton*, where the eye jumps from one similar ending to another further
down the page. Ten omitted words are one mistake, not ten.

Gotoh's 1982 algorithm introduced **affine gap penalties** to model this: a heavy
penalty for *opening* a gap, and a much smaller penalty for *extending* one already
open. The penalty for a gap of length *l* is the opening cost plus the extension
cost multiplied by *l* − 1 (Gotoh, 1982).

| Gap model | Ten-word omission costs | Models |
| --- | --- | --- |
| Linear | 10 × the per-token penalty | Ten independent decisions |
| Affine | Open + 9 × extend | One extended event |

The consequence for your collation is concrete. Under a linear penalty, an algorithm
faced with a genuine ten-word omission will often prefer a mess of small scattered
alignments over the single large gap, because ten separate penalties outweigh the
cost of forcing spurious matches. Under an affine penalty the single gap is cheap
once opened, and the algorithm finds the omission as an omission.

This is a case where an algorithm's parameters encode a claim about the world. The
affine model asserts that omissions cluster because copying errors are events rather
than independent per-token decisions — which is a philological claim, and one your
own *homoioteleuton* analysis yesterday supports.

If your manual collation found a long omission, watch specifically for whether
today's alignment recovers it as one gap.

**Takeaway:** Affine gap penalties encode the philological claim
that omissions are single events — which is why the algorithm finds them as gaps
rather than as scattered mismatches.

---

## **05 Content**

**The Variant Graph**

Pairwise alignment uses a two-dimensional matrix. Aligning many witnesses
simultaneously needs a different data structure.

In 2009 Schmidt and Colomb proposed the **variant graph** to model overlapping
textual hierarchies and multi-version documents (Schmidt & Colomb, 2009). It is a
directed acyclic graph — the same formal object as Lesson 1.1's commit graph and as
a stemma.

Its parts:

| Component | Represents |
| --- | --- |
| Node | A textual reading or token |
| Edge | A sequence relationship: this token follows that one |
| Edge label | The witness sigla that take this path |
| Start node | A single empty node beginning the graph |
| End node | A single empty node terminating it |

Reading a witness means traversing the graph following edges bearing that witness's
siglum (Schmidt & Colomb, 2009). Where witnesses agree, they share nodes and the
graph is a single path; where they diverge, the graph branches and reconverges.

The acyclicity constraint is load-bearing rather than incidental. Because the graph
is acyclic it strictly prohibits backward loops, and this mathematical enforcement
preserves the linear, temporal reading order of the text — ensuring the model does
not generate infinite loops when rendering the document (Schmidt & Colomb, 2009).

That constraint is also what makes transpositions hard, as Tuesday's section 09
established and as section 14 today will demonstrate on your own data.

The elegance of the model is that it represents *all* witnesses in one structure
without privileging any. There is no base text in a variant graph — which is the
structural answer to the bias problem from Tuesday's section 02.

**Takeaway:** A variant graph represents all witnesses in one
acyclic structure with no base text — which is the structural answer to base-text
bias.

---

## **06 Content**

**CollateX and Progressive Alignment**

CollateX is the state-of-the-art implementation of the variant graph model,
developed under the Interedition project (Haentjens Dekker & Middell, 2011).

Its central technique is **progressive multiple alignment**. Rather than comparing
every witness against a fixed base text, it aligns witnesses iteratively, merging
each result into a growing variant graph. When a new witness is introduced it is
aligned against the *accumulated graph* rather than against any single historical
witness, which eliminates base-text bias (Haentjens Dekker & Middell, 2011).

| Method | Each witness compared against | Bias |
| --- | --- | --- |
| Base text | One chosen witness | Privileges the base |
| Pairwise, all pairs | Every other witness | None; combinatorially expensive |
| Progressive multiple | The accumulated graph | Minimal; order has slight effects |

CollateX is deployed primarily as a Python library, which lets you integrate the
engine directly into scripts and notebooks and intercept the Gothenburg pipeline
dynamically — injecting custom tokenization, supplying pre-tokenized JSON with dual
forms, and exporting to CSV, GraphViz DOT, or TEI parallel segmentation (Haentjens
Dekker & Middell, 2011).

That interception capability is what today uses. You are not running a black box;
you are configuring specific stages of a pipeline whose architecture you now
understand.

One caveat on progressive alignment: the order in which witnesses are added has
minor effects on the result, since each is aligned against what has accumulated so
far. With two witnesses this does not arise. With many, record the order.

**Takeaway:** Progressive alignment merges each witness into an
accumulated graph rather than comparing against a base — which removes the bias but
makes witness order slightly significant.

---

## **07 Content**

**A First, Deliberately Unconfigured Run**

Run CollateX on your raw text before configuring anything. The purpose is to see the
noise, and to test your prediction from Tuesday's section 27.

```python
from collatex import Collation, collate

c = Collation()
c.add_plain_witness("A", open("collation/witness_a.txt").read())
c.add_plain_witness("B", open("collation/witness_b.txt").read())

table = collate(c, layout="vertical")
print(table)
```

Count the reported differences and compare against your prediction.

| Measure | Predicted | Actual |
| --- | --- | --- |
| Total differences reported | From Tuesday | Record |
| Of which you recorded as variants | 34, say | Record |
| Of which you discounted | 63, say | Record |
| Reported but not in either list | 0 expected | Record |

The fourth row is the informative one. Differences the algorithm reports that appear
in neither of your lists are differences you did not notice at all — either genuine
variants missed through fatigue, as Tuesday's section 26 anticipated, or artifacts
of tokenization differing from your assumptions.

Investigate every one. This is the first concrete benefit of the automated method:
uniform attention where yours was not.

Expect the output to be fragmented and hard to read. Aligning un-normalized text
produces highly disjointed graphs saturated with non-genealogical noise (Haentjens
Dekker & Middell, 2011), and seeing that directly is the point of running
unconfigured first. Configuration from here is the work of removing the noise
without removing the signal.

Save this raw output. It is the baseline against which your configuration's effect
is measured.

**Takeaway:** Run unconfigured first and investigate every
difference that appears in neither of your lists — those are what your attention
missed.

---

## **08 Content**

**Configuring Tokenization**

Stage 1 of the pipeline, and the decisions you settled in Tuesday's section 28.

CollateX's default tokenizer splits on whitespace and treats punctuation as attached
to adjacent words. If that does not match your decisions, supply your own.

```python
import re, unicodedata

PUNCT = r"[·.,;:··;]"

def tokenize(text, separate_punctuation=True, rejoin_line_breaks=True):
    text = unicodedata.normalize("NFC", text)
    if rejoin_line_breaks:
        # Join a word split across a line break: "λό-\nγος" -> "λόγος"
        text = re.sub(r"(\w)[-‐]?\n(\w)", r"\1\2", text)
    if separate_punctuation:
        text = re.sub(f"({PUNCT})", r" \1 ", text)
    return text.split()
```

The `rejoin_line_breaks` behaviour is the one Tuesday's section 28 flagged as
essential. Your two witnesses break lines at different points, and a tokenizer that
treats a line-broken word as two tokens will report a difference at every such break
— which is a large number of entirely spurious variants.

Test the tokenizer before collating:

```python
sample = "ἐν ἀρχῇ ἦν ὁ λό-\nγος καὶ ὁ λόγος·"
print(tokenize(sample))
```

Confirm that the line-broken word is rejoined and that the punctuation mark is its
own token if you decided it should be. A tokenizer that silently does the wrong
thing produces a collation that is wrong everywhere and looks plausible.

Feed the tokenizer's output to CollateX as a pre-tokenized witness rather than as
plain text, so that your decisions rather than the defaults govern.

**Takeaway:** Rejoin line-broken words in the tokenizer or your
witnesses will differ at every line break — a large source of entirely spurious
variants.

---

## **09 Content**

**Dual-Token JSON: The `t` and `n` Values**

Stage 2, and the most powerful configuration mechanism available.

CollateX accepts JSON input in which each token carries two values: an `n`
(normalized) value used strictly by the alignment algorithm, and a `t` (text) value
preserved for output. The diplomatic forms are aligned by their shared normalized
value while the archival spelling is preserved for the reader (Haentjens Dekker &
Middell, 2011).

```json
{
  "witnesses": [
    {
      "id": "A",
      "tokens": [
        {"t": "ἐν ", "n": "εν"},
        {"t": "ἀρχῇ ", "n": "αρχη"},
        {"t": "τιμι ", "n": "τιμη"}
      ]
    },
    {
      "id": "B",
      "tokens": [
        {"t": "ἐν ", "n": "εν"},
        {"t": "ἀρχῆ ", "n": "αρχη"},
        {"t": "τιμή ", "n": "τιμη"}
      ]
    }
  ]
}
```

Witness A's τιμι and witness B's τιμή share the normalized value τιμη, so the
algorithm aligns them as a match while the output preserves each witness's actual
spelling.

This is the mechanism that makes Week 6's work pay off. Your `<reg>` layer is
already the normalized form; generating dual-token JSON is a matter of pairing it
with the corresponding `<orig>`:

```python
def dual_tokens(tei_path):
    """Emit CollateX tokens with t from <orig> and n from <reg>."""
    for orig, reg in choice_pairs(tei_path):      # from Lesson 6.2
        yield {"t": orig + " ", "n": strip_accents(reg.lower())}
```

Note the further normalization applied to `n`: lowercasing and accent stripping. The
`n` value is *only* for matching, so it can be aggressively reduced — nothing in it
reaches the reader. Reduce it to exactly the features you consider significant for
alignment, and no more.

**Takeaway:** The `n` value is only for matching and never reaches
the reader, so reduce it to exactly the features you consider alignment-significant.

---

## **10 Content**

**Encoding Your Discounted List as Normalization**

Tuesday's discounted-differences list becomes the specification for the `n` value.
Work through it row by row.

| Discounted difference | Encode in `n` by |
| --- | --- |
| Orthographic spelling variation | Using the `<reg>` form |
| Capitalization | Lowercasing |
| Accents present or absent | Stripping diacritics |
| Punctuation | Excluding punctuation tokens from alignment, or normalizing to a single mark |
| Word division | Applying your editorial division consistently to both witnesses |
| Abbreviation expanded in one witness | Using the `<expan>` form for `n` in both |

```python
import unicodedata

def normalize_for_alignment(form):
    """Reduce a form to its alignment-significant features."""
    s = unicodedata.normalize("NFD", form.lower())
    s = "".join(ch for ch in s if not unicodedata.combining(ch))  # strip diacritics
    return unicodedata.normalize("NFC", s)
```

Note the deliberate NFD-then-NFC round trip: decomposing separates diacritics so
they can be filtered by combining class, then recomposing produces a clean result.
This is Lesson 1.2's normalization machinery used for a different purpose, and it is
the standard idiom for accent stripping.

Be deliberate about the accent decision. Stripping diacritics suppresses all
accentual variation between the witnesses — which is right if you decided accent
differences are non-substantive, and wrong if a difference of breathing distinguishes
two words. If your text has such cases, handle them by exception rather than
abandoning the reduction.

Record every reduction applied, in the method document. Each is an editorial claim
that a class of difference does not count.

**Takeaway:** Each reduction applied to the `n` value is an
editorial claim that a class of difference does not count — record them all.

---

## **11 Content**

**Near-Match: Fuzzy Alignment**

The alternative to pre-normalization, and one to use with care.

CollateX offers a `near_match` parameter evaluating tokens by Levenshtein distance
rather than strict equality. If the edit distance between two forms falls below a
threshold, they are counted as a match (Haentjens Dekker & Middell, 2011).

The attraction is obvious: it requires no lemmatization. Fradejas Rueda used exactly
this on the *Siete Partidas* to minimize orthographic noise — instructing the
algorithm to ignore capitalization differences — enabling the team to focus on
substantive morphosyntactic and lexical variants (Fradejas Rueda, 2022).

The risk is equally clear. Fuzzy matching may align distinct, substantive words that
coincidentally share characters, introducing false positives into the critical
apparatus (Nury & Spadini, 2020). Two short words differing in one letter may be a
spelling variant or may be entirely different words, and edit distance cannot tell
them apart.

| Approach | Effort | Precision | Risk |
| --- | --- | --- | --- |
| Dual-token `n` values | High; requires normalization | High | Only what you encode |
| `near_match` fuzzy | Low | Lower | Aligns coincidentally similar words |
| Both | High | Highest | Fuzzy applied only where `n` fails |

For your work the dual-token approach is preferable, because Week 6 already produced
the normalized layer that makes it available — the expensive part is done. Use
`near_match` as a supplement for forms your normalization did not cover, and inspect
what it aligns.

If you do use it, run with and without and compare. The additional alignments it
produces are exactly the cases to check by hand, and their quality tells you whether
the threshold is set sensibly for your text.

**Takeaway:** Fuzzy matching aligns coincidentally similar words —
prefer dual-token normalization, since Week 6 already did the expensive part.

---

## **12 Content**

**Running the Configured Collation**

Now collate with your configuration.

```python
import json
from collatex import Collation, collate

data = json.load(open("collation/witnesses.json"))
c = Collation()
for w in data["witnesses"]:
    c.add_witness(w)

table = collate(c, layout="vertical", near_match=False)
print(table)

csv_out = collate(c, output="csv")
open("collation/collatex_output.csv", "w").write(csv_out)
```

Setting `near_match=False` forces the algorithm to rely on the `n` values you
supplied rather than on fuzzy matching — which is what you want when you have
normalized deliberately, since it keeps the alignment governed by your explicit
decisions rather than by a distance threshold.

Export in several formats, since each supports different work:

| Format | Use |
| --- | --- |
| Vertical table | Reading the alignment during the session |
| CSV | Manual adjudication; import to a spreadsheet |
| GraphViz DOT | Visualizing the variant graph |
| TEI parallel segmentation | Week 8's apparatus |

The CSV is what you will work from today. Fradejas Rueda's workflow exported to CSV
precisely for manual adjudication, which allowed the detection of subtle linguistic
retrogressions between printed editions that a manual reading would have entirely
missed (Fradejas Rueda, 2022).

Commit the output with its configuration, so the run is reproducible:

```text
feat(collation): CollateX alignment of ff. 42r-43v, configured

Dual-token JSON with n values from the <reg> layer, lowercased and
diacritic-stripped. Punctuation tokenized separately. Line-broken words
rejoined. near_match disabled. Configuration in tools/collate.py,
rationale in collation/METHOD.md.

Human-Verified: false
Baseline-Commit: <collation-manual-w7>
```

**Takeaway:** Disable `near_match` when you have normalized
deliberately — it keeps alignment governed by your decisions rather than a distance
threshold.

---

## **13 Content**

**Measuring Against the Manual Collation**

The evaluation, structured as in Lesson 6.2 section 10.

Compare CollateX's variant sites against yesterday's record:

| Case | Manual | CollateX | Classification |
| --- | --- | --- | --- |
| Both report a variant at this site | Recorded | Reported | Agreement |
| Manual recorded, CollateX did not | Recorded | Aligned as match | False negative |
| CollateX reported, manual did not | Discounted | Reported | Noise; configuration incomplete |
| CollateX reported, manual missed it | Not noticed | Reported | Genuine find |
| Both report, different extent | Recorded | Different span | Boundary disagreement |

Compute:

```text
Recall    = variants found by CollateX / variants you recorded
Precision = variants you agree are variants / variants CollateX reported
```

Interpret carefully. Unlike Lesson 6.2's normalization, where you set the standard
by policy, here the standard is partly external — a variant either exists between the
witnesses or does not. But *what counts as a variant* is still a policy decision,
because it depends on your discounting rules.

So a low precision figure is ambiguous. It may mean the tool is over-reporting, or
it may mean your configuration has not yet encoded all your discounting rules. Check
the second before concluding the first.

The fourth row is the one to celebrate rather than to score. A variant CollateX found
that you missed is a correction to your manual work, and it is the direct benefit of
uniform machine attention over fatigued human attention (Fradejas Rueda, 2022).
Count these separately and report them.

**Takeaway:** Low precision usually means your configuration is
incomplete rather than that the tool is over-reporting — check that first.

---

## **14 Content**

**How the Algorithm Handled Your Omission**

Look specifically at what happened at the omission you found yesterday.

Under affine gap penalties the algorithm should have recovered it as a single
extended gap rather than as scattered mismatches (Gotoh, 1982). Check:

| Observation | Interpretation |
| --- | --- |
| One continuous gap of the right extent | Working as intended |
| Several small gaps with spurious matches between | Gap penalty tuning, or normalization noise |
| Gap boundaries differ from yours by a word or two | Ambiguity where boundary words repeat |
| No gap; text forced into alignment | Threshold or scoring problem |

The third row is interesting rather than erroneous and connects to Tuesday's
*homoioteleuton* discussion. Where an omission is bounded by repeated words, there
is genuine ambiguity about where it begins and ends — the algorithm and you may
place the boundary at different instances of the same word, and both placements
represent the same textual fact.

That ambiguity is itself evidence. An omission whose boundaries are ambiguous
*because the boundary word repeats* is very likely *homoioteleuton*, and the
algorithm's difficulty locating the boundary corroborates your diagnosis rather than
contradicting it.

Record what you find. If the algorithm recovered the omission cleanly, that is a
successful test of the affine model on your data. If it did not, investigate why —
and check whether normalization noise is preventing the surrounding text from
aligning.

**Takeaway:** Ambiguous gap boundaries where the boundary word
repeats corroborate a *homoioteleuton* diagnosis rather than indicating an alignment
failure.

---

## **15 Content**

**How the Algorithm Handled Your Transposition**

The known limitation, now observable on your own data.

If your manual collation found a transposition, CollateX will very likely report it
as an omission in one location and a separate addition in another. This is not a
defect but a consequence of the data model: because the variant graph must remain
acyclic, an edge running backward would create a forbidden cycle, so transpositions
are identified by secondary heuristic passes after primary alignment and
superimposed as unlabelled dashed lines — metadata rather than structure (Schmidt &
Colomb, 2009).

The editorial consequence is that transpositions must be manually audited, since the
core algorithm treats moved text as a deletion in one place and a separate insertion
in another rather than as a single genetic scribal event (Schmidt & Colomb, 2009).

| What happened | What it means |
| --- | --- |
| Reported as omission plus addition | Expected; the DAG cannot express the move |
| Detected and marked as a transposition | The heuristic pass fired; verify its extent |
| Not detected at all | Below the heuristic's threshold; audit by hand |
| Text forced into alignment in place | Normalization noise, or a short transposition |

Record which occurred. This is a case where your manual work is straightforwardly
better than the algorithm's — you saw one event, and the model can only represent
two — and it is worth stating plainly in the report.

It also bears on Week 8. An apparatus generated automatically from this alignment
will contain two entries where one editorial fact exists, and correcting that is
manual work you should anticipate.

**Takeaway:** The DAG cannot express a backward move, so a
transposition arrives as two entries where one editorial fact exists — and correcting
that is manual.

---

## **16 Content**

**Iterating the Configuration**

Improve the configuration from the failure analysis, in this order.

- **Eliminate spurious variants first.** Each is noise, and noise is what makes the output unusable. Trace each to its cause — tokenization, an unencoded discounting rule, or a normalization gap.
- **Then address false negatives.** Variants you recorded and the tool missed usually mean the `n` values collapsed a distinction you consider significant.
- **Then tune boundaries.** Extent disagreements are lower priority and often genuinely ambiguous.

Record performance across iterations:

| Iteration | Change | Reported | Precision | Recall |
| --- | --- | --- | --- | --- |
| 0 | Unconfigured | Record | Record | Record |
| 1 | Tokenizer: rejoin line breaks | Record | Record | Record |
| 2 | `n` from `<reg>` | Record | Record | Record |
| 3 | Lowercase and strip diacritics | Record | Record | Record |
| 4 | Punctuation excluded | Record | Record | Record |

The trajectory is the interesting result. Each configuration step should
substantially reduce reported differences while leaving your recorded variants
intact — and a step that reduces both is over-normalizing, collapsing distinctions
you consider significant.

That is the same precision-recall trade-off as Lesson 6.2 section 10, and the same
warning applies: do not tune until the tool exactly reproduces your manual result.
Where they differ, ask which is right. Sometimes the tool is.

Note the specific danger here. Aggressive `n` reduction improves precision by
suppressing differences, and taken far enough it suppresses real variants. The
diacritic-stripping decision from section 10 is the usual culprit; check that no
recorded variant disappeared when you applied it.

**Takeaway:** A configuration step that reduces both reported
differences and recorded variants is over-normalizing — check that no real variant
disappeared.

---

## **17 Content**

**Case Study: Scaling to Eleven Million Words**

What the method makes possible, and the practical evidence for it.

The *Siete Partidas* of Alfonso X comprises approximately 100 witnesses and over 11
million words, with complex conflations across manuscript and early printed editions
(Fradejas Rueda, 2022).

Initial attempts to collate manually using spreadsheet colour-coding proved
unsustainable — which is the honest report of a method meeting a scale it cannot
handle. The project instead implemented Python scripts pipelining tokenized
transcriptions directly into CollateX, fully automating the alignment (Fradejas
Rueda, 2022).

The configuration decisions are the same ones you made today. `near_match` was used
to minimize orthographic noise, instructing the algorithm to ignore capitalization
differences, which let the team focus exclusively on substantive morphosyntactic and
lexical variants. Output was exported to CSV for manual adjudication (Fradejas
Rueda, 2022).

The payoff was a finding manual work could not have produced: the team detected
subtle linguistic retrogressions between the 1491 and 1555 printed editions that a
manual reading would have entirely missed (Fradejas Rueda, 2022).

That is the argument for automation stated precisely. It is not that the tool
collates better than a scholar — it is that at 11 million words there is no
alternative, and that systematic comparison at scale reveals patterns invisible to
sequential reading.

Note also what remained manual: adjudication. The tool produced the alignment; the
scholars decided what the variants meant. That division is the one this week is
teaching.

**Takeaway:** At eleven million words automation is not better
than manual collation — it is the only option, and it reveals patterns sequential
reading cannot.

---

## **18 Content**

**Case Study: Comparing the Tools**

A useful evaluation of the alternatives, which explains why this course uses
CollateX.

Mabille evaluated Juxta, CollateX, Stemmaweb, and TRAViz on the Old Spanish *Fuero
Juzgo*, establishing a stemma for 42 witnesses (Nury & Spadini, 2020).

| Tool | Strength | Limitation found |
| --- | --- | --- |
| Juxta | Intuitive visual heat maps | Fixed base text; no pre-alignment normalization; useless for genealogical discovery |
| Stemmaweb | Phylogenetic neighbour-joining overview | Could not process annotations distinguishing orthographic from substantive variants |
| TRAViz | Visualization | Not suited to rigorous *recensio* |
| CollateX | JSON pre-alignment normalization; CSV output for refinement | Requires programming |

Juxta's failure is instructive because it is the base-text problem from Tuesday's
section 02 in practice: a tool relying on a fixed base text and unable to normalize
before alignment was found largely useless for discovering overarching genealogical
relationships (Nury & Spadini, 2020).

Stemmaweb's failure is subtler and closer to your concerns. It produced a useful
overview of witness distances but could not process annotations distinguishing
orthographic from substantive variants (Nury & Spadini, 2020) — which means it
treated Tuesday's taxonomy as unavailable, and, as Tuesday's section 07 established,
those tiers differ enormously in genealogical value. A distance metric weighting
orthographic and lexical variants equally measures the wrong thing.

CollateX proved the only viable engine, because its Python implementation allowed
JSON-based pre-alignment normalization and produced a CSV matrix the editor could
refine manually for rigorous *recensio* (Nury & Spadini, 2020).

The general lesson: a collation tool's value lies less in its alignment algorithm —
they are all doing Needleman–Wunsch — than in whether it lets the editor express
philological distinctions before and after alignment.

**Takeaway:** Collation tools differ less in their algorithms than
in whether they let the editor express philological distinctions before and after
alignment.

---

## **19 Content**

**Exporting for Week 8**

Produce the output the apparatus will consume.

CollateX exports TEI parallel segmentation directly, which is the encoding Week 8
uses:

```python
tei_out = collate(c, output="tei")
open("collation/collatex_output.xml", "w").write(tei_out)
```

The result looks like:

```xml
<app>
  <rdg wit="#A">ἐγένετο</rdg>
  <rdg wit="#B">ἐγένοντο</rdg>
</app>
```

Note what it does *not* contain: a `<lem>`. The tool records that the witnesses
differ; it does not decide which reading to adopt. That decision is editorial and is
Week 8's work.

Nor does it contain your taxonomy. Every variant site is encoded identically,
whether it is a trivial orthographic difference or a substantive lexical
substitution. Filtering the apparatus by significance requires the classification you
made yesterday, and merging it into this output is a task for Week 8.

| Present in the export | Absent |
| --- | --- |
| Variant sites | The adopted reading |
| Witness sigla | Variant classification |
| Readings | Contextual notes |
| Structure | Editorial judgement |

Commit the export alongside the CSV and the DOT visualization. Generating the
GraphViz output is worth doing even if you do not use it immediately:

```python
open("collation/variant_graph.dot", "w").write(collate(c, output="dot"))
```

Rendering it shows the variant graph as a graph, which makes the branching structure
of the differences visible in a way a table does not.

**Takeaway:** The TEI export records that witnesses differ but not
which reading is adopted or how significant it is — both are Week 8's editorial work.

---

## **20 Content**

**Recording the Method**

Extend `collation/METHOD.md` with today's configuration, in enough detail to be
reproducible.

- Tool and version.
- Tokenization rules, including line-break rejoining and punctuation handling.
- Source of the `n` values.
- Reductions applied to `n`: lowercasing, diacritic stripping, others.
- Whether `near_match` was used, and at what threshold.
- Witness order, if more than two.
- Output formats produced.
- Measured precision and recall against the manual collation.
- Variants the tool found that manual collation missed.
- Known limitations: transposition handling, boundary ambiguities.

The measured performance belongs in the record for the same reason as in Lesson 6.2
section 17: a reader evaluating your apparatus needs to know how the variant list
was produced and how reliable that production was.

State the configuration precisely enough that someone else could reproduce your
collation from the document. That is the standard, and it is achievable here in a
way it is not for Friday's method — the configuration is a finite list of explicit
decisions, and recording it completely is straightforward.

Commit with a `docs:` prefix.

**Takeaway:** The configuration is a finite list of explicit
decisions, so complete reproducibility is achievable here in a way it will not be on
Friday.

---

## **21 Content**

**What the Algorithm Cannot Do**

State the limits, since Friday's method claims some of them.

| Limitation | Reason |
| --- | --- |
| Classify variants by significance | No concept of philological value |
| Recognize a transposition as one event | The DAG forbids backward edges |
| Judge which reading is original | No model of the text or its history |
| Recognize semantic equivalence | Aligns by character or by your `n` value only |
| Interpret an omission's cause | No model of scribal behaviour |
| Weigh contextual evidence | Operates on sequences alone |

The fourth row is the one Friday tests. CollateX relies on deterministic dynamic
programming and possesses no semantic comprehension; it aligns words based solely on
character overlap or pre-coded normalization dictionaries (Haentjens Dekker &
Middell, 2011). Two words meaning the same thing but sharing no characters are, to
this algorithm, entirely different.

That is a real limitation for collation. A scribe substituting a synonym has made a
lexical variant of high genealogical value, and an alignment based on character
overlap will record it as a divergence without recognizing that the substitution is
semantically motivated.

The first row is the one that stays yours regardless. The taxonomy from Tuesday
requires knowing what kinds of variation matter and why, which is philological
knowledge rather than pattern matching — and no row in the table above is likely to
move to the machine column.

**Takeaway:** The algorithm aligns by character overlap and has no
semantic comprehension — a synonym substitution registers as divergence without
being recognized as one.

---

## **22 Content**

**Checklist Before You Leave**

Verify each.

- CollateX installed and running.
- Unconfigured run performed and its output saved.
- Prediction from Tuesday compared against the unconfigured result.
- Differences appearing in neither of your lists investigated.
- Tokenizer written and tested, with line-break rejoining verified.
- Dual-token JSON generated from `<orig>` and `<reg>`.
- Reductions applied to `n` documented individually.
- Configured collation run with `near_match` disabled.
- Precision and recall computed against the manual collation.
- Failures categorized; configuration gaps distinguished from tool limits.
- Variants the tool found and you missed identified and verified.
- Omission handling inspected.
- Transposition handling inspected and recorded.
- Configuration iterated, with performance recorded per iteration.
- Checked that no recorded variant disappeared under aggressive normalization.
- Exports produced: CSV, TEI, DOT.
- Method document updated.
- Committed and tagged.
- Costs recorded.

Tag today's output:

```bash
git tag -a collation-collatex-w7 -m "CollateX alignment, configuration v4"
```

**Takeaway:** Verify that no recorded variant disappeared under
normalization before accepting an improved precision figure.

---

## **23 Content**

**Common Problems Today**

Failures that recur.

| Symptom | Cause | Remedy |
| --- | --- | --- |
| Everything reported as a variant | `n` values not supplied, or both `<choice>` layers extracted | Check the JSON; verify extraction |
| Differences at every line break | Line-broken words not rejoined | Fix the tokenizer |
| Nothing reported as a variant | `n` reduction too aggressive | Check that real variants survive |
| Alignment collapses after an omission | Gap penalties, or noise preventing resynchronization | Improve normalization first |
| Transposition reported as two events | The DAG limitation | Expected; audit by hand |
| Output unreadable | Too many witnesses or columns for the layout | Export CSV instead |
| Results differ between runs | Witness order, with several witnesses | Fix and record the order |
| Precision improves as recall falls | Over-normalizing | Check which variants disappeared |

The first row is the extraction trap from Tuesday's section 20, arriving in a new
form. If the alignment reports disagreement everywhere, inspect the actual `n`
values before concluding anything — a JSON in which every `n` is a concatenation of
both `<choice>` layers will match nothing.

The third row is the mirror image and is more insidious, because an output with few
variants looks like a clean result. If aggressive lowercasing and diacritic
stripping have collapsed a real distinction, the tool reports agreement where the
witnesses differ, and nothing signals the loss. Always verify against your recorded
variants.

**Takeaway:** Few reported variants looks like a clean result and
may mean your normalization collapsed real distinctions — verify against the manual
record.

---

## **24 Content**

**What Good Work Looks Like Here**

The standard.

A minimally acceptable result is CollateX run over both witnesses with output
produced.

Good work additionally:

- Runs unconfigured first and uses the result to test a prior prediction.
- Traces each configuration decision to a specific line of the discounted list.
- Documents every reduction applied to the `n` value as an editorial claim.
- Measures precision and recall separately against the manual collation.
- Distinguishes configuration gaps from genuine tool limitations.
- Verifies that normalization did not suppress recorded variants.
- Inspects omission and transposition handling specifically.
- Identifies and verifies variants the tool found that manual work missed.
- Records the configuration precisely enough to be reproducible.
- Reports cost alongside quality.

The eighth item is the one that most changes the conclusion. A student who reports
that CollateX agreed with 91% of their manual variants has measured a tool. A
student who reports that it additionally surfaced four variants their manual
collation missed, three of which they verified against the facsimile as genuine, has
used the tool to improve the edition — and has evidence for the claim that
automation catches what fatigue does not.

**Takeaway:** Reporting the variants the tool found that you
missed is what turns a measurement of the tool into an improvement of the edition.

---

## **25 Content**

**Preparing for Friday**

Bring:

- The configured alignment, tagged, in CSV and TEI.
- Precision and recall figures with the failure categorization.
- The list of variants requiring semantic judgement — synonyms, and cases where alignment by character overlap seems wrong.
- Your manual variant classifications.
- The transposition, if you have one.
- Costs recorded.

Friday applies AI methods to variant identification and classification. The specific
tests:

- Can it classify variants by taxonomy tier as you did?
- Can it identify semantic equivalence that character-based alignment misses?
- Does it recognize the transposition as one event?
- Does it hallucinate variants that are not there?
- Is its output reproducible?

The third item is the interesting one. CollateX cannot represent a transposition as
a single event because of the acyclicity constraint (Schmidt & Colomb, 2009). A
model reasoning about the text rather than aligning sequences has no such constraint
— and whether it recognizes the move is a genuine test of whether semantic
understanding adds something the graph model cannot supply.

The fifth is the concern. The stochastic, generative nature of language models
currently lacks the strict mathematical reproducibility, transparency, and
deterministic rigour required to produce definitive critical apparatuses, which is
why deterministic algorithms remain the gold standard for baseline collation
(Haentjens Dekker & Middell, 2011). Friday tests that claim on your data.

**Takeaway:** Whether a model recognizes your transposition as one
event tests directly whether semantic reasoning supplies what the graph model
structurally cannot.

---

## **26 Content**

**The Reproducibility Property**

Worth stating explicitly, as in Lesson 6.2 section 27.

Your collation is now reproducible. The tokenizer, the normalization, the
configuration, and the input are all committed; anyone with the repository can run
it and obtain identical output. Automated collation ensures absolute, mathematical
reproducibility, because every decision is explicit (Fradejas Rueda, 2022).

That property is not shared by either of the other two methods this week. Your
manual collation depends on your attention on a particular afternoon and cannot be
exactly reproduced even by you. Friday's method depends on a hosted model that may
change.

| Method | Same input, same output | Procedure inspectable |
| --- | --- | --- |
| Manual | No | Only via the method document |
| CollateX | Yes, exactly | Fully |
| Language model | Not guaranteed | Only the prompt |

For a critical apparatus this matters more than it might elsewhere. An apparatus is
a claim about what the witnesses read, and a reader who doubts it should be able to
re-derive it. With today's method they can: the configuration is a finite list of
stated decisions applied by a deterministic algorithm.

That is why deterministic algorithms remain the persistent gold standard for
baseline scholarly collation (Haentjens Dekker & Middell, 2011) — not because they
are the most capable, but because a baseline needs to be reproducible before it
needs to be clever.

**Takeaway:** A baseline needs to be reproducible before it needs
to be clever — which is why deterministic alignment remains the standard.

---

## **27 Content**

**Where Today's Labour Went**

Take stock of the shift, because it is the week's methodological point.

Yesterday's labour was *reading*: comparing two texts word by word, sustaining
attention, recognizing differences. Today's labour was *modelling*: deciding what a
token is, what differences count, how to represent your judgements as data.

The philological content did not diminish. It moved.

| | Manual collation | Automated collation |
| --- | --- | --- |
| Where effort goes | Reading and comparing | Tokenization and normalization |
| Where judgement is applied | At each variant | Before alignment, as policy |
| When decisions are made | Continuously | In advance |
| Failure mode | Fatigue; missed variants | Misconfiguration; systematic error |
| Error character | Random | Systematic |

The bottom two rows deserve attention because they characterize the risk profiles.
Manual collation fails randomly: attention lapses, and a variant is missed here and
there. Automated collation fails systematically: a tokenization error affects every
line break in the text, and a normalization error affects every instance of a class.

Systematic errors are more dangerous *and* more tractable. More dangerous because
they are uniform and therefore invisible — nothing looks anomalous when everything
is wrong the same way. More tractable because once found, one fix corrects all of
them.

That is the argument for measuring against a manual baseline. A systematic
configuration error produces plausible output, and the only way to detect it is
comparison against work produced differently.

**Takeaway:** Automated collation fails systematically rather than
randomly — uniform errors are invisible without a differently-produced baseline to
compare against.

---

## **28 Content**

**The Epistemological Burden**

The point the literature is careful to make, and worth registering before Friday.

Comparative evaluations of collation tools conclude that while algorithms can
perfectly align character strings, the epistemological burden of defining and
interpreting textual variance ultimately remains with the human scholar (Nury &
Spadini, 2020).

"Defining" is doing as much work in that sentence as "interpreting." The algorithm
did not decide what counts as a variant; you did, when you specified the `n` values.
Its output is a function of your definitions, and a different editor with different
definitions would obtain a different collation from the same witnesses — both
correct, and answering different questions.

This is why the method document is not documentation in the ordinary sense. It is
the statement of what question the collation answers.

| Question | Configuration |
| --- | --- |
| Where do the witnesses differ substantively? | `n` from `<reg>`, diacritics stripped |
| Where do the scribes spell differently? | `n` from `<orig>` |
| Where do they differ in punctuation? | Punctuation tokenized, other differences suppressed |
| Where do they differ at all? | No normalization |

All four are legitimate collations of the same two witnesses. The output differs
completely between them, and nothing in the tool indicates which you performed.

Only the method document does — which makes it a load-bearing part of the edition
rather than an appendix to it.

**Takeaway:** Different configurations produce different, equally
correct collations of the same witnesses — only the method document says which
question yours answers.

---

## **29 Content**

**Connecting to Week 8**

Where this goes, in specific terms.

Next week builds the apparatus criticus from today's output, using the TEI critical
apparatus module: `<app>`, `<lem>`, `<rdg>`.

| Meeting | Step | Activity |
| --- | --- | --- |
| Tue Oct 27 (#20) | Manual | Encode an apparatus entry by hand |
| Wed Oct 28 (#21) | Deterministic | Generate the apparatus from CollateX output; validate |
| Fri Oct 30 (#22) | AI-assisted | AI-assisted apparatus drafting and error hunting |

The Wednesday step consumes exactly what you exported today. Three things must be
added to it:

**The lemma.** Today's export records readings without adopting one. Choosing the
lemma at each variant site is the editorial act at the centre of a critical edition.

**The classification.** Tuesday's taxonomy determines which variants enter the main
apparatus. An apparatus containing every orthographic difference is unusable.

**The witness sigla, formalized.** Your `<listWit>` in the header must declare each
witness so that `@wit` references resolve.

The **Textual Variants & Collation Assignment is due Friday October 30**, at the end
of Week 8, and this week's work is its foundation.

**Takeaway:** Week 8 adds the lemma, the classification, and the
formal sigla to today's export — the export is the raw material, not the apparatus.

---

## **30 Content**

**Synthesis: Alignment Solved, Definition Not**

The argument of this meeting.

Sequence alignment is a solved problem. Needleman and Wunsch established optimal
global alignment by dynamic programming in 1970; Gotoh's affine gap penalties in
1982 made the gap model match the mechanics of scribal omission; and Schmidt and
Colomb's variant graph in 2009 provided a data structure representing many witnesses
without privileging any (Needleman & Wunsch, 1970; Gotoh, 1982; Schmidt & Colomb,
2009). CollateX implements all three, and the alignment stage required no work from
you today.

What required work was everything around it. What is a token. Which differences
count. How to express your judgements as normalized values. Those are stages 1 and 2
of the Gothenburg Model, and they are where the philology lives (Haentjens Dekker &
Middell, 2011).

The tool's advantages are real: exactness, scale, reproducibility, and uniform
attention that catches what fatigue misses. Its limitations are structural: no
semantic comprehension, no variant classification, and a data model that cannot
represent a transposition as the single event it is (Schmidt & Colomb, 2009;
Haentjens Dekker & Middell, 2011).

And the burden of defining and interpreting textual variance remains with the
scholar (Nury & Spadini, 2020). The algorithm answers the question you configured it
to ask, and the configuration is the question.

**For Friday.** Bring the six items in section 25. Friday tests whether semantic
methods supply what character-based alignment cannot — and at what cost in
reproducibility.

**Due Friday October 23.** The Normalization Assignment, from Topic 6.

**Takeaway:** Alignment is solved; defining what counts as a
variant is not, and that definition is the configuration you wrote today.

---

## References

Fradejas Rueda, J. M. (2022). *Resources and challenges for the automatic collation
of medieval texts: The 7PartidasDigital project*.

Gotoh, O. (1982). An improved algorithm for matching biological sequences.
*Journal of Molecular Biology, 162*(3), 705–708.

Haentjens Dekker, R., & Middell, G. (2011). Computer-supported collation with
CollateX: Managing textual variance in an environment with varying requirements. In
*Supporting Digital Humanities*.

Haentjens Dekker, R., van Hulle, D., Middell, G., Neyt, V., & van Zundert, J.
(2015). Computer-supported collation of modern manuscripts: CollateX and the
Beckett Digital Manuscript Project. *Digital Scholarship in the Humanities, 30*(3),
452–470.

Howe, C. J., Connolly, R., & Windram, H. F. (2012). Responding to criticisms of
phylogenetic methods in stemmatology. *Studies in Bibliography*.

Needleman, S. B., & Wunsch, C. D. (1970). A general method applicable to the search
for similarities in the amino acid sequence of two proteins. *Journal of Molecular
Biology, 48*(3), 443–453.

Nury, E., & Spadini, E. (2020). From giant despair to a new heaven: The early years
of automatic collation. *it – Information Technology, 62*(2), 61–73.

Schmidt, D., & Colomb, R. (2009). A data structure for representing multi-version
texts online. *International Journal of Human-Computer Studies, 67*(6), 497–514.

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/
