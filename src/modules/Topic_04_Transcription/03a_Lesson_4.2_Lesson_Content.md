# Lesson 4.2 — Layout Analysis and HTR Model Training in Transkribus

*RELS 398 / ENGL 398 · Topic 4: Transcription · Meeting #10 (Wed Sep 23)*

***Step 2 of the three-step cycle: deterministic.** Today you take yesterday's
ground truth into Transkribus, correct its layout analysis, and train a model
specific to your scribe. The model is a rule-governed statistical engine, not a
generative one — and its failure modes differ accordingly.*

---

## **01 Content**

**What "Deterministic" Means This Week**

The Wednesday step of each week uses specialized, rule-based or trained
computational tools rather than general-purpose generative models. The
distinction is worth stating precisely, because "deterministic" is doing specific
work here.

An HTR model is not deterministic in the sense of following hand-written rules. It
is a neural network whose behaviour is learned from data. It is deterministic in
two senses that matter: the same input produces the same output every time, and
the model's competence is bounded by what it was trained on. It cannot draw on
knowledge of the text's content, cannot consult its expectations about what a
sentence should say, and cannot invent material from outside its training
distribution.

That boundedness is a limitation and a guarantee simultaneously. A specialized HTR
model will fail on a hand it has not seen. It will not, in general, fabricate a
plausible sentence that is not on the page — because it has no model of what
sentences ought to look like beyond the character-level patterns it learned
(Puigcerver, 2017).

Friday's tools do have such a model, and that difference is the whole point of the
three-step cycle. Today establishes what a system that reads *only the image*
produces. Friday will show what a system that also brings linguistic expectation
produces, and Week 5 will measure both against yesterday's ground truth.

**Vocabulary.** *HTR* — handwritten text recognition. *Model* — a trained set of
parameters mapping images to characters. *Training* — the process of fitting those
parameters to labelled examples.

**The takeaway for this page:** A specialized HTR model is bounded by its training
data, which makes it fail rather than fabricate — the opposite of Friday's tools.

---

## **02 Content**

**The Pipeline: Layout Before Recognition**

Automated transcription is two problems, and conflating them causes most of the
confusion students have about why HTR fails.

**Document layout analysis** determines *where the text is*: which regions of the
page contain writing, how those regions divide into lines, and in what order the
lines should be read. **Recognition** determines *what the text says*, operating on
individual line images produced by the layout stage.

The order is strict, and so is the dependency. Recognition never sees the page. It
sees line images that layout analysis produced, and it can only transcribe what
those images contain.

| Stage | Input | Output | Failure produces |
| --- | --- | --- | --- |
| Region detection | Page image | Text regions | Whole passages omitted |
| Baseline detection | Text regions | Baselines per line | Lines merged or split |
| Polygon computation | Baselines | Line images | Truncated ascenders or descenders |
| Reading order | Line set | Sequence | Text in the wrong order |
| Recognition | Line images | Text per line | Character errors |

Errors in spatial segmentation cascade directly into the recognition phase
(AlKendi et al., 2024). This is the single most important operational fact about
HTR, and it explains a symptom that otherwise seems inexplicable: a model that
performs well on most of a page and produces nonsense on part of it usually has a
layout problem there, not a recognition problem.

The diagnostic habit that follows: when output is bad, look at the line images
before blaming the model. If the line image is wrong, no model can fix it.

**The takeaway for this page:** Recognition only ever sees line images that layout
analysis produced — so when output is bad, inspect the line images first.

---

## **03 Content**

**From Bounding Boxes to Baselines**

Layout analysis has a history worth knowing, because it explains why current tools
work as they do.

Early systems drew rectangular **bounding boxes** around perceived paragraphs and
lines. This works acceptably for printed text in regular columns. It works poorly
for manuscripts, which routinely have irregular layouts: marginal glosses,
interlinear additions, multi-column formats, and non-linear reading orders
(Perdiki & Konstantinidou, 2023). A rectangle cannot describe a line that slopes,
curves, or interleaves with an interlinear addition.

Modern systems instead predict **baselines** — the imaginary line on which
characters sit. A baseline is a polyline that can slope and curve, following the
actual course of the writing. From it, the system computes a **polygonal envelope**
around the ascenders and descenders, producing the line image that recognition
receives (AlKendi et al., 2024).

| Approach | Represents a line as | Handles |
| --- | --- | --- |
| Bounding box | An axis-aligned rectangle | Regular printed layout only |
| Pixel-wise segmentation | A labelled region of pixels | Irregular shapes; merges adjacent lines |
| Baseline plus polygon | A polyline with a computed envelope | Sloping, curving, crowded manuscript lines |
| Object detection (YALTAi) | Detected line objects | Complex historical layouts robustly |

Pixel-wise semantic segmentation — labelling every pixel as text or not — was an
intermediate step with a characteristic failure: it merges adjacent lines whose
ascenders and descenders touch, and splits single lines where writing is faint.
Both are common in manuscripts.

The object detection approach, exemplified by YALTAi, treats line-finding as
detecting discrete objects rather than as classifying pixels, and achieves
accurate baseline identification on complex historical manuscripts
(eScriptorium/Kraken, 2024; AlKendi et al., 2024). Transkribus and eScriptorium
both use baseline-oriented approaches, though their implementations differ.

**The takeaway for this page:** Modern layout analysis predicts sloping baselines
and computes envelopes around them, because manuscript lines do not fit rectangles.

---

## **04 Content**

**Importing Your Manuscript**

Begin the practical work. Transkribus ingests images from IIIF manifests, which is
why Lesson 3.3 insisted the manifest be reachable over HTTP.

The sequence:

- Create a collection in Transkribus for your edition.
- Import by manifest URI, not by file upload.
- Confirm the expected number of pages arrived.
- Confirm the images display at full resolution, not as thumbnails.
- Check that page order matches the manuscript.

If import fails, the causes are the ones Lesson 3.3 section 15 anticipated: the
manifest is not publicly reachable, image endpoints require authentication, or the
manifest is non-conformant in a way viewers tolerate and platforms do not. Diagnose
with `curl` from outside your own network before assuming the platform is at fault.

Importing by manifest rather than by upload has an advantage worth noticing. The
images remain the institution's, served from their endpoints, at whatever
resolution they provide. You are not creating a detached copy that will drift from
the source, and the provenance chain from your training data back to the
institutional facsimile stays intact.

Import only the folios you intend to work on. A collection containing an entire
codex when you are working on four folios makes every subsequent operation slower
and every listing harder to read.

**The takeaway for this page:** Import by manifest URI so training data stays
linked to the institutional source rather than becoming a detached copy.

---

## **05 Content**

**Running and Reading Layout Analysis**

Run the platform's automatic layout analysis on your folios, then — before doing
anything else — inspect the result carefully. This inspection is today's most
important task.

Examine, for each page:

- Are all text regions detected? Check margins, headers, and any glosses.
- Is every line detected? Count against the manuscript.
- Are any two lines merged into one?
- Is any single line split into two?
- Does each baseline follow the writing, or does it drift?
- Is the reading order correct, particularly around marginalia?
- Do the polygons enclose the full height of the writing?

The last question is the one specific to Greek and the one you prepared for
yesterday. Polygons are computed from the baseline plus estimated ascender and
descender extents, and those estimates come from the general behaviour of the
script. A hand that places breathings and accents high above the letter body will
frequently have them fall outside a default polygon.

Perdiki and Konstantinidou (2023) report exactly this in Byzantine Greek work:
automated layout analysis frequently omitted breathings and suffix abbreviations
placed high above the primary line, and reaching a character error rate below 10%
required manually adjusting the polygon envelopes during ground truth preparation
so that peripheral diacritics were visually captured.

Zoom in on a line with a high breathing and look at where the polygon boundary
runs. If the breathing is outside it, every diacritic in your training data is
being discarded before the model ever sees it.

**The takeaway for this page:** Check whether polygons enclose high-placed
breathings and accents — if they do not, the model is being trained on Greek with
the diacritics cut off.

---

## **06 Content**

**Correcting Layout by Hand**

Where automatic analysis is wrong, correct it. This is tedious and it is the work
that determines everything downstream.

| Problem | Correction |
| --- | --- |
| Line not detected | Draw the baseline manually |
| Two lines merged | Split, then adjust both baselines |
| One line split | Merge the fragments |
| Baseline drifts off the writing | Drag control points onto the writing |
| Polygon truncates accents | Extend the upper boundary |
| Polygon truncates descenders | Extend the lower boundary |
| Reading order wrong | Renumber lines or regions |
| Marginal gloss merged into the main text | Separate into its own region |

Correct *every* page you intend to use for training. This is not optional
refinement: training data with truncated polygons teaches the model that Greek is
written without breathings, and the model will faithfully reproduce what it was
taught. The error will then appear in Week 5 as a systematically low diacritic
accuracy, and its cause will be invisible in the output.

A practical approach that saves time. Correct one page thoroughly, noting how much
vertical margin this hand actually requires above and below the baseline. If the
platform permits adjusting the layout analysis parameters, set them from that
measurement and re-run on the remaining pages — a global parameter change is far
faster than correcting each page by hand, and it addresses the cause rather than
the instances.

Whatever you do, verify by inspecting extracted line images directly. The line
image is what the model sees, and looking at it is the only direct check that your
corrections had the intended effect.

**The takeaway for this page:** Adjust the layout parameters from a measurement of
this hand rather than correcting page by page — and verify by looking at extracted
line images.

---

## **07 Content**

**Aligning Your Ground Truth to Lines**

With layout correct, associate yesterday's transcription with the detected lines.
Each line image must be paired with the text it contains.

Two routes:

The **manual route** is typing or pasting the transcription line by line into the
platform's editor. It is slow and it is entirely reliable, and for a single folio
it is often the right choice.

The **import route** uploads a transcription in a supported format and aligns it
to the detected lines automatically. It is fast and it depends on the line
divisions in your transcription matching the detected lines exactly — which is
precisely why yesterday's lesson insisted that `<lb/>` count equal `<zone>` count.

| Situation | Route | Risk |
| --- | --- | --- |
| One folio, ~25 lines | Manual | Typing errors |
| Several folios, line divisions verified | Import | Misalignment if counts differ |
| Line counts do not match | Fix the mismatch first | Silent systematic misalignment |

The third row is the important one. If your transcription has 24 lines and layout
analysis detected 25 — because one line was split — automatic alignment will pair
each transcription line with the wrong image from the split onwards. Every
subsequent pairing is off by one.

The resulting training data is not merely noisy; it is systematically wrong, and
it will produce a model that has learned to associate each line's image with the
next line's text. Such a model produces fluent-looking nonsense, and the cause is
extremely hard to diagnose from the output.

Verify alignment by spot-checking: pick three lines at random, look at the image,
read the paired text. If they match, the alignment is probably right. Do this
before training, every time.

**The takeaway for this page:** Verify line alignment by spot-checking image
against text — an off-by-one misalignment produces a model that has learned the
wrong pairing entirely.

---

## **08 Content**

**How Recognition Works: CRNN and CTC**

Understanding the architecture explains the errors you will see. Transkribus has
long used PyLaia, which exemplifies the convolutional-recurrent paradigm
(Puigcerver, 2017).

A line image passes through a deep **convolutional neural network**, which
extracts a sequence of localized visual feature maps — effectively, a description
of what the image looks like at each horizontal position. Those features feed into
**bidirectional long short-term memory** layers, a recurrent architecture that
models sequential dependencies in both directions, so that each position is
interpreted in the context of what precedes and follows it (AlKendi et al., 2024).

The mathematical innovation is the loss function. **Connectionist temporal
classification** (CTC) computes the probability of a target character sequence
summed over all possible alignments between image slices and output characters,
using a special "blank" token to handle repeated characters and non-text visual
noise (AlKendi et al., 2024).

Why this matters practically: CTC is **alignment-free**. It does not require you
to say which pixels correspond to which character. Training data needs only a line
image paired with the line's text — which is exactly what a diplomatic
transcription with line divisions provides, and it is why manual transcription is
directly usable as training data without any further annotation (Puigcerver,
2017).

The architectural consequence is that CTC decoders rely heavily on local visual
evidence and model broader linguistic context only weakly (AlKendi et al., 2024).
The model is, in effect, reading the ink rather than reading the language — which
is what produces the error profile in the next section.

**The takeaway for this page:** CTC training needs only line images paired with
line text, which is why your diplomatic transcription is directly usable as
training data.

---

## **09 Content**

**The Error Profile of a CTC Model**

The architecture determines the *kind* of mistakes, and knowing the kind is what
lets you correct efficiently.

Because CTC maps visual slices to characters with weak linguistic modelling, its
errors are localized to the visual evidence. It struggles with heavily abbreviated
words and dense ligatures, where the visual footprints of separate characters
overlap. But it rarely hallucinates whole words: given ambiguous evidence — faded
ink, a cross-out — it typically produces an orthographically impossible sequence
of letters rather than guessing a plausible word (AlKendi et al., 2024).

That behaviour is enormously valuable for post-correction, and it is worth
appreciating why.

| Model type | Behaviour on ambiguous ink | Consequence for the editor |
| --- | --- | --- |
| CTC (PyLaia) | Produces an impossible letter sequence | The error is conspicuous |
| Transformer (TrOCR) | Produces a plausible wrong word | The error is inconspicuous |
| Vision-language model | Produces fluent plausible text | The error may be invisible |

A CTC model that outputs `ἐγενθτο` has flagged its own uncertainty: the sequence is
not Greek, and you will notice it immediately. A model that outputs `ἐγένετο` where
the manuscript reads `ἐγένοντο` has produced a perfectly good Greek word that is
simply not what is written, and you will notice only by checking against the image.

This is the central trade-off in model selection. For consistent, formulaic texts
with minimal degradation, a CRNN-CTC model is computationally cheap, effective,
and will not hallucinate false words. For heavily damaged texts or extreme scribal
variance, transformer models offer superior contextual guessing — at the cost of
requiring exceptional vigilance during post-correction for hallucinated sequences
(AlKendi et al., 2024).

For a first model on a single hand, PyLaia's conspicuous failure mode is the right
choice.

**The takeaway for this page:** A CTC model's errors are conspicuous because it
produces impossible sequences rather than plausible wrong words — which makes
post-correction far more reliable.

---

## **10 Content**

**Transformer Architectures and TrOCR**

The alternative paradigm eliminates recurrence entirely, and you should understand
it because it underlies the "supermodels" you may use as a base.

**TrOCR** uses a pre-trained vision transformer to encode the line image into patch
embeddings, and an autoregressive text transformer to decode characters. The
decoder's cross-attention lets it attend simultaneously to disparate regions of
the image and to the text it has already produced (Li et al., 2023).

The consequence is strong contextual capability. The model can use what it has
read so far to interpret ambiguous ink — which produces robust recognition on
degraded text and complex layouts. It also produces the over-willingness to guess:
the model's language modelling drives it toward plausible completions, which
lowers word error rate while sometimes raising character error rate, and yields
output where the ink and the transcription disagree in ways that read perfectly
(AlKendi et al., 2024).

| | PyLaia (CRNN-CTC) | TrOCR (Transformer) |
| --- | --- | --- |
| Context modelling | Weak, local | Strong, global |
| Computational cost | Low | High |
| Performance on degraded text | Moderate | Better |
| Hallucination risk | Low | Meaningful |
| Error conspicuousness | High | Low |
| Suitable for | Consistent hands; first models | Damaged text; variable hands |

A refinement worth knowing: **AdapterTrOCR** injects specialized domain adapters —
one for historical language, one for handwriting style — into the generic TrOCR
framework, substantially reducing error rates for low-resource historical
languages without full-parameter fine-tuning (AlKendi et al., 2024). Adapters make
transformer models practical where training data is limited, which is the normal
condition in manuscript work.

If your hand is consistent, start with PyLaia. If it is highly variable or badly
degraded, a transformer base may serve better — but plan for more careful
post-correction.

**The takeaway for this page:** Transformers read context as well as ink, which
helps on degraded text and produces plausible wrong words that are hard to catch.

---

## **11 Content**

**Transfer Learning: Never Start From Scratch**

The most consequential decision you make today, and the one with the clearest
empirical answer.

Training a neural network from random initialization requires enormous quantities
of labelled data. Fine-tuning an existing model requires far less, because the base
model already encodes general knowledge about letterforms, ink, parchment, and
line structure; your data only needs to specialize it to your particular hand.

The guidance is unambiguous: never train from random initialization if a
foundational model exists. Fine-tuning a robust base — Transkribus Titan, a
Carolingian minuscule model, or `TrOCR-Medieval-Base` — on as few as 50 to 100
pages of new ground truth can drop the character error rate to usable levels while
drastically reducing compute time (Geelhaar, 2022; AlKendi et al., 2024).

The magnitude of the effect is worth seeing concretely. Perdiki and Konstantinidou
(2023) trained Byzantine Greek models on manuscripts from geographically distinct
libraries:

| Training paradigm | Source | Base model used | Resulting CER |
| --- | --- | --- | --- |
| Single model | Athos, Vatopedi 328 | No | 10.03% |
| Single model | Munich, Gr. 353 | No | 8.12% |
| General mixed model | Multi-manuscript | No | 17.18% |
| General mixed model | Multi-manuscript | Yes, transfer | 3.90% |

Read the last two rows together. The same mixed multi-manuscript training data
produced 17.18% CER from scratch and 3.90% with transfer learning — a fourfold
improvement from the single decision to start from a pre-trained base rather than
from random weights.

Their work also found that mixed-model training across multiple manuscripts
reduced the manual ground truth required per individual manuscript by up to 80%
without sacrificing accuracy (Perdiki & Konstantinidou, 2023). Diversity of
training material substitutes for volume.

**The takeaway for this page:** Transfer learning turned 17.18% CER into 3.90% on
identical data — always fine-tune from a base model rather than training from
scratch.

---

## **12 Content**

**Selecting a Base Model**

Choose deliberately. The base model determines what your fine-tuned model starts
from, and a poorly matched base wastes your ground truth.

| Selection criterion | Preference |
| --- | --- |
| Script | The same script — Greek minuscule for Greek minuscule |
| Period | As close as possible to your manuscript's date |
| Language | The same language, or a related one |
| Training volume | Larger, other things being equal |
| Documented performance | Published CER on comparable material |
| Availability | Accessible within your platform |

Script match matters most. A model trained on Latin Carolingian minuscule has
learned Latin letterforms, and it will not transfer usefully to Greek regardless
of how well trained it is. Period and language matter next, because they determine
vocabulary and abbreviation repertoire.

The specialization gap makes this concrete. On the CATMuS medieval Latin dataset,
the domain-tuned `TrOCR-Medieval-Base` achieved 14.6% CER, while general-purpose
commercial models on identical samples produced 63.0% and 84.7% (Mattingly et al.,
2024). The domain-tuned model operates with orders of magnitude fewer parameters
and succeeds because it has been directly exposed to palaeographic variation,
scribal shorthand, idiosyncratic ligatures, and non-standard layouts (Mattingly et
al., 2024).

Bigger is not better; *matched* is better. This is the single most counter-intuitive
fact about applying machine learning to manuscripts, and it recurs on Friday in a
much starker form.

Record which base model you chose and why, in your repository. It is a
methodological decision, and Week 5's report should state it.

**The takeaway for this page:** A matched small model beats a large general one —
script match matters more than parameter count.

---

## **13 Content**

**Running the Training**

With ground truth aligned and a base model chosen, train. The parameters that
matter:

| Parameter | Meaning | Typical starting point |
| --- | --- | --- |
| Base model | The starting weights | A script- and period-matched model |
| Training set | Lines used to fit the model | Your corrected, aligned folios |
| Validation set | Lines held out to measure performance | 10–20% of your data |
| Epochs | Passes over the training data | Platform default; watch the curve |
| Learning rate | Step size in parameter updates | Platform default for fine-tuning |

The **validation set** is the one to understand rather than accept. It is data the
model is not trained on, used to measure performance on material it has not seen.
Without it you cannot distinguish a model that has learned your hand from one that
has memorized your specific lines — and the second performs perfectly on training
data and badly on everything else.

Ensure the validation set is *representative*. Holding out the last three lines of
one folio validates on material almost identical to the training data. Holding out
lines sampled across all your folios, including difficult ones, gives a measurement
that means something.

Training a fine-tuned model on a modest ground truth typically takes tens of
minutes rather than hours. Watch the validation error across epochs: it should
decline and then flatten. If it declines and then *rises*, the model is
overfitting — learning your specific lines rather than the hand — and training
should stop at the minimum.

Note that model training consumes credits from the course's shared allocation.
Plan your runs; do not launch speculative training repeatedly.

**The takeaway for this page:** Hold out a representative validation set and stop
when validation error stops falling — a rising validation curve means the model is
memorizing your lines.

---

## **14 Content**

**Reading the Results**

Training produces a model and a reported error rate. Interpret both carefully.

The reported CER is measured on the validation set — material the model has not
seen, drawn from the same manuscript and hand. It is a reasonable estimate of
performance on more of the same manuscript. It is *not* an estimate of performance
on a different hand, a different manuscript, or a substantially different page
layout.

Thresholds for interpreting the number (AlKendi et al., 2024):

| CER | Assessment | What it supports |
| --- | --- | --- |
| Under 5% | Excellent | Minimal correction; suitable for a semi-diplomatic edition after proofreading; reliable for downstream NLP |
| 5–10% | Good, usable | Localized errors on abbreviations, rare ligatures, punctuation; heavier post-editing for a critical edition; fine for corpus work |
| 10–15% | Marginal | Substantial correction required |
| Over 15% | Poor | Post-correction typically costs more than transcribing from scratch |

That last row is the practically decisive one and worth remembering as a rule.
Above roughly 15% CER, the cognitive load and time required to post-correct exceed
the time to transcribe manually from the beginning (AlKendi et al., 2024). A model
in that range is not a slow tool; it is a net loss, and the correct response is to
improve it or abandon it rather than to work through its output.

If your first model lands above 15%, the usual causes in order of likelihood are:
layout errors producing bad line images, misaligned ground truth, too little
training data, or a poorly matched base model. Check them in that order.

**The takeaway for this page:** Above 15% CER, correcting the output costs more
than transcribing from scratch — the model is a net loss, not a slow tool.

---

## **15 Content**

**Error Rates Do Not Tell You Everything**

A caution that Week 5 will develop and that you should carry into today's
evaluation.

CER is the Levenshtein distance between machine output and ground truth,
normalized by length — the minimum number of insertions, substitutions, and
deletions required to turn one into the other (AlKendi et al., 2024). It is a
single number summarizing every difference equally.

That equal weighting is the limitation. A substitution that changes an accent and
a substitution that changes a letter count identically, though their scholarly
consequences differ enormously. A model that systematically drops breathings
because of truncated polygons may show a modest CER while being useless for a
diplomatic edition.

Evaluate the *qualitative nature* of errors alongside the number:

| Error type | Effect on CER | Scholarly severity |
| --- | --- | --- |
| Dropped diacritics | Moderate | High for Greek; destroys diplomatic fidelity |
| Confused similar letters | Moderate | Moderate; usually caught in proofreading |
| Expanded abbreviations | Low | High; silently normalizes |
| Impossible letter sequences | Moderate | Low; conspicuous, easily corrected |
| Plausible wrong words | Low to moderate | High; inconspicuous |
| Omitted marginalia | Depends on volume | High; whole content lost |

The third row is the one that recurs. A model that silently expands abbreviations
produces clean readable text with a low CER and has destroyed exactly what a
diplomatic transcription exists to preserve. A CTC model with 8% CER that strictly
preserves palaeographic ligatures may be far more valuable to a philologist than a
model with 4% CER that modernizes (Levchenko, 2024).

Look at the errors, not only at the number. Week 5 will formalize this.

**The takeaway for this page:** CER weights every difference equally, so a model
that silently drops diacritics or expands abbreviations can score well while being
useless for a diplomatic edition.

---

## **16 Content**

**Applying the Model and Inspecting the Output**

Run the trained model over folios you have not transcribed, and examine what comes
back.

Work systematically rather than impressionistically:

- Read the output against the image, line by line, at full zoom.
- Categorize each error rather than merely correcting it.
- Note whether errors cluster — by region, by letterform, by feature.
- Check specifically whether diacritics are present and correct.
- Check whether abbreviations are preserved or expanded.
- Note any line where the output is nonsense, and inspect that line's image.

The last item connects to section 02. A line producing nonsense usually has a
layout problem — a merged line, a truncated polygon, a baseline that drifted. Look
at the extracted line image before concluding the model failed at recognition.

Record the categorized errors in your repository. This categorization is a
required component of the Week 5 reconciliation report, and doing it now while you
are looking at the output is far easier than reconstructing it later.

Expect specific patterns from a Greek model. Abbreviations and dense ligatures are
the hardest cases for CTC architectures, since separate characters overlap
visually (AlKendi et al., 2024). Diacritics will be imperfect even with good
polygons. And if your manuscript uses *scriptio continua*, expect word boundaries
to be wrong in ways that make word error rate uninterpretable — the system
recognizes characters correctly but fuses them into concatenated tokens, so that
distinct words emerge as a single string (Perdiki & Konstantinidou, 2023).

**The takeaway for this page:** Categorize errors rather than just correcting
them, and inspect the line image whenever output is nonsense — it is usually a
layout fault.

---

## **17 Content**

**Iterating: Correcting and Retraining**

HTR is iterative. The first model is a starting point, and the standard workflow
is a loop.

The cycle: apply the model to new pages, correct its output, add the corrected
pages to the training set, retrain, apply the improved model to further pages.
Each iteration produces ground truth more cheaply than the last, because you are
correcting rather than transcribing — and each iteration improves the model.

| Iteration | Ground truth | Effort per page | Expected CER |
| --- | --- | --- | --- |
| 1 | Manually transcribed | Highest | Baseline |
| 2 | Model output, corrected | Lower | Improved |
| 3 | Model output, corrected | Lower still | Improved further |
| n | Diminishing returns | Low | Plateau |

The economics are what make HTR worthwhile: after the initial investment, each
additional page costs progressively less. This is why the manual transcription in
Lesson 4.1 is an investment rather than a cost.

Two cautions. Correcting model output is subject to the anchoring problem from
Lesson 4.1 section 25 — you are judging plausibility rather than reading
independently. Correct at full zoom against the image, and be especially careful
with plausible-looking output.

And guard against feedback. If you correct carelessly and retrain, the model learns
your careless corrections and produces more output with the same errors, which you
then correct less carefully because it looks familiar. The loop can converge on a
confidently wrong model. Periodically transcribe a page independently, without
looking at model output, and compare — that is the check that breaks the loop.

**The takeaway for this page:** Each iteration makes ground truth cheaper, but
correcting model output risks a feedback loop — periodically transcribe a page
blind to break it.

---

## **18 Content**

**Layout Brittleness**

A limitation to understand before you rely on your model, because it will surprise
you otherwise.

HTR models are brittle with respect to layout. A model performing well on standard
pages can degrade sharply on pages whose layout differs, even when the hand and
language are identical.

Geelhaar's (2022) Carolingian Minuscule Model, trained on standardized Carolingian
texts of the ninth to eleventh centuries, achieved 5.1% CER on standard manuscript
pages. On pages carrying minuscule marginal glosses, the same model degraded to
13.6% — a shift from excellent to marginal, caused by changed vocabulary, heavier
localized abbreviation, and reduced effective resolution of the smaller script.

| Layout change | Typical effect | Cause |
| --- | --- | --- |
| Marginal glosses | Substantial degradation | Smaller script; different vocabulary; layout confusion |
| Interlinear additions | Lines merged | Layout analysis cannot separate them |
| Column changes | Reading order errors | Region detection |
| Damaged regions | Local failure | Polygons drawn around damage |
| Change of hand | Degradation | Outside the training distribution |

The practical implication is that CER should be interpreted as *conditional on
layout*. A model reporting 4% CER reports 4% on pages like the ones it was
validated on. Applied to a page with a different layout, its performance is
unknown until measured.

For your edition, this means checking whether your passage's pages are
homogeneous. If some carry glosses, marginalia, or a change of hand, expect the
model to perform differently there, and validate on those pages specifically rather
than assuming the general figure applies.

**The takeaway for this page:** A model's CER holds only for layouts like those it
was validated on — glossed or irregular pages need their own measurement.

---

## **19 Content**

**Transkribus and eScriptorium**

Two platforms serve this work, and it is worth knowing how they differ, since your
choice has consequences.

**Transkribus** is a commercial platform with a graphical interface, a substantial
library of pre-trained public models, and a credit-based pricing model for
training and recognition. **eScriptorium** is open-source, built on the Kraken
engine with YALTAi object detection for layout, and can be self-hosted
(eScriptorium/Kraken, 2024).

| | Transkribus | eScriptorium |
| --- | --- | --- |
| Licence | Commercial; credit-based | Open source |
| Interface | Mature GUI | Web interface |
| Model library | Large public collection | Smaller; growing |
| Layout engine | Proprietary | Kraken with YALTAi |
| Hosting | Hosted service | Hosted or self-hosted |
| Output formats | PAGE XML, ALTO, TEI | ALTO, PAGE XML |
| Reproducibility | Limited; proprietary models | High; open models and code |

The accessibility point is not trivial. Perdiki's work found that command-line
tools proved computationally inaccessible for many humanities scholars, while the
Transkribus graphical interface permitted rapid iterative training and visual
layout correction (Perdiki & Konstantinidou, 2023). The interface is a substantive
factor in whether the method gets used at all.

Against that, eScriptorium's openness matters for a reproducible edition. A model
you can inspect, share, and re-run is one a later scholar can verify; a proprietary
model may not be available in ten years, which makes any claim resting on it
unverifiable.

This course uses Transkribus for its accessibility and model library. If your work
continues past this term, eScriptorium is worth learning for the reproducibility.

**The takeaway for this page:** Transkribus is more accessible; eScriptorium is
reproducible — and a proprietary model makes any claim resting on it unverifiable
later.

---

## **20 Content**

**Exporting: PAGE, ALTO, and TEI**

Getting output back out is where today's work rejoins your edition.

Both platforms export ALTO XML and PAGE XML, formats describing a page as a
hierarchy of regions, lines, and words with coordinates, each carrying recognized
text. These formats have structural equivalence to TEI and — critically — preserve
the pixel-coordinate bindings established during layout analysis
(eScriptorium/Kraken, 2024).

| ALTO element | Contains | TEI equivalent |
| --- | --- | --- |
| `<Page>` | One page | `<surface>` |
| `<TextBlock>` | A region of text | `<zone type="block">` |
| `<TextLine>` | One line with a baseline | `<zone type="line">` |
| `<String>` | One word with coordinates | `<w>` with `@facs` |

That coordinate preservation is the payoff. Rather than measuring line regions by
hand as you did for three lines in Lesson 3.3, you can transform ALTO's coordinates
into TEI zones for every line automatically.

The transformation requires care about coordinate spaces. ALTO coordinates are in
*image pixel* space. If your canvas dimensions differ from your image dimensions —
the ratio you recorded in Lesson 3.3 section 03 — every coordinate needs scaling
before it becomes a TEI zone.

This is exactly what your hand-measured zones are for. Transform the ALTO
coordinates, compare the result against the three lines you measured yourself, and
if they agree the transform is right. If they differ by a constant factor, you have
found the scaling error — and you found it because you had a control.

Export today, commit the raw export alongside your transformed TEI, and record the
scale factor you applied.

**The takeaway for this page:** ALTO preserves line coordinates in image pixels —
transform them into TEI zones and check the result against your hand-measured
control lines.

---

## **21 Content**

**Committing Machine Output**

The provenance discipline from Week 1 applies with full force today, and this is
the first commit where it does real work.

Commit machine output **separately from your corrections**. This is not a stylistic
preference; it is what makes Week 5's measurement possible. The raw model output
is what gets scored against the ground truth, and if it is committed already
corrected, the error rate cannot be computed at all.

```text
feat(transcription): HTR output for ff. 43r-44v, uncorrected

Applied model rels398-hand1-v2, fine-tuned from Transkribus Titan on 24
lines of manual ground truth from f. 42r. Validation CER 6.2%.

Raw model output, no corrections applied. Corrections follow in a
separate commit so that raw CER can be measured against this state in
Week 5.

AI-Generated: true
Model: Transkribus / PyLaia, rels398-hand1-v2
Base-Model: Transkribus Titan I
Human-Verified: false
Ground-Truth-Commit: a3f9c21
Validation-CER: 6.2
```

Then correct, and commit the corrections separately:

```text
fix(transcription): correct HTR output for ff. 43r-44v

Corrected 31 errors against the facsimile at full zoom. Categorized in
logs/htr-errors-w4.md: 14 diacritic omissions, 9 abbreviation errors,
5 ligature misreadings, 3 line-final truncations.

Human-Verified: true
```

The `Human-Verified: false` on the first commit is the work queue from Lesson 1.1
section 24 in action. Between those two commits, your repository contains
unverified machine text, and the trailer says so.

**The takeaway for this page:** Commit raw model output and your corrections
separately, or Week 5 cannot compute an error rate at all.

---

## **22 Content**

**What Today Establishes for Friday**

Friday runs the same passage through a general-purpose vision-language model, and
the comparison is the week's actual lesson. Today's results are the baseline for
it.

Record clearly, so Friday's comparison is possible:

| Quantity | Where recorded |
| --- | --- |
| Base model used | Repository note and commit trailer |
| Training data volume | Lines and folios used |
| Validation CER | Commit trailer and note |
| Error categorization | `logs/htr-errors-w4.md` |
| Layout corrections required | Note; how much manual work |
| Raw output, uncorrected | Its own commit, tagged |
| Time invested | Note; setup, correction, training |

The last row matters more than students expect. Friday's model requires no
training, no layout correction, and no ground truth — you paste an image and get
text. Comparing the *quality* of Wednesday's and Friday's output without also
comparing their *cost* misses half the question, and the honest assessment in Week
5 needs both.

Tag today's raw output state, so Week 5 can retrieve exactly what was measured:

```bash
git tag -a htr-w4-raw -m "Raw HTR output, model rels398-hand1-v2, before correction"
```

Expect Friday's model to be worse on this material, possibly dramatically. That is
the finding, not a failure of the exercise — and it will be more convincing for
having been measured than for having been asserted.

**The takeaway for this page:** Record cost as well as quality — Friday's tool
needs no training or ground truth, and the comparison is meaningless without that.

---

## **23 Content**

**Why the Specialized Model Usually Wins**

Anticipating Friday, because the result is counter-intuitive and worth
understanding before you see it.

Vision-language models have billions of parameters trained on vast heterogeneous
corpora. Your fine-tuned HTR model has orders of magnitude fewer and was trained on
a few dozen lines of your handwriting. Intuition says the larger model should win.

It generally does not, on historical material, and the gap is enormous. On the
CATMuS medieval Latin benchmark, the domain-tuned `TrOCR-Medieval-Base` achieved
14.6% CER while DeepSeek-OCR scored 63.0% and Mistral-OCR-3 scored 84.7% on
identical samples (Mattingly et al., 2024). On historical English from the Bentham
corpus, GPT-4o produced 52.23% CER; on historical German from READ2016, 77.42%
(AlKendi et al., 2024).

The same models are excellent on modern handwriting. GPT-4o achieves 1.39% CER on
the IAM modern English dataset — competitive with specialized architectures
operating zero-shot (AlKendi et al., 2024).

| Dataset | Model | CER |
| --- | --- | --- |
| IAM, modern English | GPT-4o | 1.39% |
| Bentham, historical English | GPT-4o | 52.23% |
| READ2016, historical German | GPT-4o | 77.42% |
| CATMuS, medieval Latin | TrOCR-Medieval-Base | 14.6% |
| CATMuS, medieval Latin | Mistral-OCR-3 | 84.7% |

This is the **specialization gap**. Domain-tuned models operate with vastly fewer
parameters and succeed precisely because they have been directly exposed to
palaeographic variation, scribal shorthand, idiosyncratic ligatures, and
non-standard layouts (Mattingly et al., 2024). General models have seen the
internet, which contains very little Byzantine minuscule.

Scale does not substitute for exposure to the specific material. That is the
week's central empirical finding, and Friday will let you verify it on your own
manuscript.

**The takeaway for this page:** General models are excellent on modern handwriting
and catastrophic on historical scripts — scale does not substitute for exposure to
the material.

---

## **24 Content**

**The Complexity Paradox**

A related finding worth knowing before Friday, because it will shape what you try.

The intuition when building a pipeline is that more components help: an OCR model,
then a language model to correct its output, perhaps retrieval-augmented generation
to supply domain knowledge. Each component addresses a real weakness.

Empirically, this fails. A simple pipeline — a specialized OCR model feeding
directly into a VLM translator — substantially outperforms multi-component variants
that add retrieval-augmented generation or LLM-based post-OCR correction. The
additional generative steps introduce prompt saturation and cascading error
propagation that degrade aggregate quality (Mattingly et al., 2024).

| Pipeline | Components | Outcome |
| --- | --- | --- |
| Simple | Specialized OCR to VLM translator | Best |
| With RAG | Adds retrieval-augmented context | Degraded |
| With LLM post-correction | Adds generative correction of OCR | Degraded |
| Both | All of the above | Worst |

The mechanism is that each generative step can introduce errors as well as fix
them, and errors introduced late in a pipeline are not caught by anything
downstream. An LLM correcting OCR output has no access to the image; it corrects
toward linguistic plausibility, which means it will "fix" correct unusual readings
into incorrect common ones. In a manuscript context, unusual readings are
frequently the interesting ones.

The lesson for Friday: do not attempt to improve today's HTR output by passing it
through an LLM for correction. That is precisely the configuration the evidence
says degrades quality, and you would be degrading the output while feeling you had
improved it.

**The takeaway for this page:** Adding LLM post-correction to OCR degrades quality
— it corrects toward plausibility, and unusual readings are the interesting ones.

---

## **25 Content**

**Checklist Before You Leave**

Verify each item.

- Manuscript imported into Transkribus by manifest URI.
- Layout analysis run on all working folios.
- Every line detected; no merges or splits remaining.
- Polygons verified to enclose high-placed diacritics.
- Ground truth aligned to lines; alignment spot-checked.
- Base model selected, with the reason recorded.
- Model trained, with a representative validation set.
- Validation CER recorded.
- Model applied to at least one untranscribed folio.
- Output inspected line by line at full zoom.
- Errors categorized in `logs/htr-errors-w4.md`.
- Raw output committed separately, with provenance trailers.
- Raw output state tagged.
- ALTO or PAGE export committed.
- Coordinates checked against your Lesson 3.3 control lines.
- Time invested recorded.

If your model's validation CER exceeds 15%, do not proceed to correction — the
output is not worth correcting. Diagnose instead, in the order given in section 14:
layout, alignment, data volume, base model.

**The takeaway for this page:** If validation CER exceeds 15%, diagnose rather than
correct — check layout, then alignment, then data volume, then base model.

---

## **26 Content**

**Common Problems Today**

Failures that recur, with their diagnoses.

| Symptom | Likely cause | Check |
| --- | --- | --- |
| Import fails | Manifest not publicly reachable | `curl` from outside your network |
| Some lines undetected | Faint ink; layout parameters | Inspect and correct manually |
| Output missing all diacritics | Polygons truncating accents | Look at extracted line images |
| Output is fluent nonsense | Ground truth misaligned by one line | Spot-check image against text |
| CER much worse than expected | Base model mismatched to script | Confirm script and period |
| Model good on one folio, bad on another | Layout differs between them | Validate per layout type |
| Training error falls, validation error rises | Overfitting | Stop at the validation minimum |
| Words fused together | *Scriptio continua* | Expected; note for Week 5 |
| Abbreviations expanded in output | Base model trained on normalized text | Choose a diplomatic base model |

The third and fourth rows are today's characteristic failures and both are
invisible in the output. Missing diacritics produce text that reads as unaccented
Greek and looks like a recognition weakness rather than a layout fault. Misaligned
ground truth produces text that is internally coherent and simply belongs to
different lines.

The remedy for both is the same and is worth stating as a general principle: when
output is wrong in a way you cannot explain, look at what the model actually saw.
The extracted line image is the ground truth about the input, and almost every
inexplicable failure is visible there.

**The takeaway for this page:** When output is inexplicably wrong, look at the
extracted line image — that is what the model actually saw.

---

## **27 Content**

**Recording the Methodology**

Your Week 5 report will need a methodological account of today's work, and writing
it now is easier than reconstructing it.

Record in `logs/htr-method-w4.md`:

- Platform and version used.
- Base model, with its documented training material and reported performance.
- Ground truth: which folios, how many lines, how produced.
- Layout corrections required, and of what kind.
- Whether polygon parameters were adjusted, and to what.
- Training configuration: validation split, epochs, stopping criterion.
- Validation CER, and what it was measured on.
- Folios the model was applied to.
- Error categories observed, with counts.
- Time invested at each stage.

This is a methods section. Its purpose is to let a reader — or you, in December —
determine what was done and whether the results mean what they appear to mean. A
CER of 6.2% is uninterpretable without knowing the base model, the training volume,
and what the validation set contained.

It also protects you. If your Week 5 results are surprising, this record is what
lets you diagnose why. Without it, a strange error rate is simply strange, and the
only remedy is redoing the work.

Commit it with a `docs:` prefix.

**The takeaway for this page:** A CER figure is uninterpretable without its base
model, training volume, and validation set — record the methodology today.

---

## **28 Content**

**Preparing for Friday**

Friday is remote, and it applies vision-language models to the same passage.

Bring, or rather have available from wherever you will be:

- Your repository, pushed.
- Yesterday's ground truth, tagged.
- Today's raw HTR output, tagged.
- Today's error categorization and methodology notes.
- Your manifest, reachable from outside your network.
- Working polytonic input on the machine you will use.
- Access to a vision-language model.

The comparison Friday makes is three-way: your manual transcription, today's
specialized model, and Friday's general model, all on the same lines. Having all
three states retrievable by tag is what makes the comparison exact rather than
approximate.

Set an expectation now, so the result is a measurement rather than a surprise.
Based on the published benchmarks in section 23, Friday's output will likely be
substantially worse than today's on historical Greek — plausibly by a large
factor. It will also be produced in minutes rather than in a session's work.
Holding both facts together is what Week 5's assessment requires.

Verify your remote toolchain today, per Lesson 4.1 section 23. Every item on that
list is quick now and none of them is quick on Friday morning.

**The takeaway for this page:** Tag all three states so Friday's three-way
comparison is exact, and expect the general model to be much worse and much faster.

---

## **29 Content**

**What Good Work Looks Like Here**

The standard for today, since "trained a model" and "trained a model well" differ.

A minimally acceptable result is a trained model with a recorded CER and inspected
output.

Good work additionally:

- Corrects layout thoroughly, including polygon envelopes for diacritics.
- Verifies ground truth alignment by spot-checking rather than assuming.
- Chooses a base model deliberately and records the reason.
- Uses a representative validation set rather than a convenient one.
- Categorizes errors rather than merely counting them.
- Distinguishes layout failures from recognition failures.
- Records cost — time and effort — alongside quality.
- Commits raw output separately from corrections, with full provenance.
- Notes what the model does badly and hypothesizes why.

The last item is what makes this scholarship rather than tool operation. A model
with 6% CER that drops breathings on a specific letterform, fails on one scribe's
abbreviation for *kai*, and degrades on the glossed folio is a much more useful
finding than "6% CER" — because it tells you what to fix, what to check manually,
and what to say about the method's applicability to this manuscript.

**The takeaway for this page:** Reporting *what* the model gets wrong and why is
the scholarly contribution; the CER number alone is tool operation.

---

## **30 Content**

**Synthesis: A Bounded Instrument**

What today established about the deterministic step.

A specialized HTR model is a **bounded instrument**. It reads ink and produces
characters, and its competence extends exactly as far as its training data. Within
that boundary, on a hand it has seen, it is fast, cheap, consistent, and — because
its architecture models language weakly — inclined to fail conspicuously rather
than to fabricate (Puigcerver, 2017; AlKendi et al., 2024).

Its performance depends on things you control. Layout analysis must be corrected,
because recognition only sees what layout produces, and truncated polygons remove
Greek diacritics before the model ever sees them (Perdiki & Konstantinidou, 2023).
Ground truth must be aligned, diplomatic, and consistent. The base model must match
the script. Transfer learning must be used, because it is the difference between
17% and 4% CER on identical data (Perdiki & Konstantinidou, 2023).

And its evaluation requires more than a number. A CER figure holds only for layouts
like those it was validated on, weights every difference equally, and can look
excellent while the model silently normalizes away the diplomatic fidelity the
edition exists to preserve (Levchenko, 2024).

Friday tests the opposite kind of instrument: unbounded, trained on everything,
capable of drawing on linguistic expectation — and consequently able to produce
fluent text that is not on the page. The comparison between the two is the point of
the week.

**For Friday.** Remote delivery. Bring the seven items in section 28, with all three
states tagged.

**The takeaway for this page:** An HTR model reads ink within the bounds of its
training and fails conspicuously; Friday's instrument reads expectation too, and
fails fluently.

---

## References

AlKendi, W., Gechter, F., Heyberger, L., & Guyeux, C. (2024). Advancements and
challenges in handwritten text recognition: A comprehensive survey. *Journal of
Imaging*.

Clérice, T., Pinche, A., Chagué, A., Camps, J.-B., Vlachou-Efstathiou, M., Levenson,
M. G., Brisville-Fertin, O., Boschetti, F., & Fischer, F. (2024). CATMuS Medieval:
A multilingual large-scale cross-century dataset in Latin script for handwritten
text recognition and beyond. In *International Conference on Document Analysis and
Recognition (ICDAR)*.

eScriptorium/Kraken. (2024). *eScriptorium platform documentation*.
https://escriptorium.eu/about

Geelhaar, T. (2022). *Carolingian minuscule model CMM 9th–11th c.* Transkribus
Model. https://www.transkribus.org/models/latin-carolingian-minuscule

Levchenko, M. A. (2024). *Evaluating LLMs for historical document OCR: A
methodological framework for digital humanities*.

Li, M., Lv, T., Chen, J., Cui, L., Lu, Y., Florencio, D., Zhang, C., Li, Z., & Wei,
F. (2023). TrOCR: Transformer-based optical character recognition with pre-trained
models. *Proceedings of the AAAI Conference on Artificial Intelligence, 37*(11),
13094–13102.

Mattingly, W. J. B., et al. (2024). *When simpler is better: Evaluating translation
pipelines for medieval Latin manuscripts*.

Perdiki, E., & Konstantinidou, M. (2023). Preparing big manuscript data for
hierarchical clustering with minimal HTR training. *Journal of Data Mining &
Digital Humanities*. https://jdmdh.episciences.org/12664/pdf

Perdiki, E. (2021). Review of Transkribus. *RIDE: A Review Journal for Digital
Editions and Resources*. https://ride.i-d-e.de/issues/issue-15/transkribus/

Puigcerver, J. (2017). *PyLaia: A deep learning toolkit for handwritten document
analysis*. https://github.com/jpuigcerver/PyLaia

Romein, C. A., et al. (2025). *Assessing advanced handwritten text recognition
engines for digitizing historical documents*.

Ströbel, P. B., Clematide, S., Volk, M., & Hodel, T. (2023). *The adaptability of a
transformer-based OCR model for historical documents*.
