# Lesson 5.1 — Double-Keying and Building a Consensus Text

*RELS 398 / ENGL 398 · Topic 5: Reconciliation · Meeting #12 (Tue Sep 29)*

***Step 1 of a two-step week.** Wednesday September 30 is closed for Truth and
Reconciliation. This week is a two-step week by design: reconciliation is itself
the comparison, so the missing meeting costs nothing. Today you transcribe your
folio a second time, independently, and adjudicate the differences into a
consensus text.*

---

## **01 Content**

**Why the Ground Truth Needs Verifying**

Last week you produced a diplomatic transcription and treated it as ground truth.
Wednesday's HTR model was trained on it; Friday's comparison was scored against
it. Everything measured in Week 4 assumed it was correct.

It is not entirely correct. No single-pass manual transcription is. The errors are
few, but they exist, and their existence has three consequences that Week 4's
measurements silently absorbed.

A correct machine reading at a point where your transcription errs is scored as a
machine *error*, inflating the measured error rate. A model fine-tuned on the
flawed reference *learns* the error and reproduces it. And when you reconciled
differences on Friday, you would have resolved them toward your own reading —
because the ground truth was, by definition, the reference.

Today addresses this. The established method is **double-keying**: the same source
transcribed independently twice, the two versions compared computationally, and
every difference adjudicated to produce a consensus text (Haaf et al., 2013).

The logic is statistical and elegant. Two independent transcribers are unlikely to
commit the *same* error at the *same* character position. Where two independent
passes agree, the reading is very probably correct; where they disagree, an error
is very probably present in one of them. Disagreement localizes error precisely,
which is what makes correction efficient rather than exhaustive.

**Vocabulary.** *Double-keying* — independent duplicate transcription followed by
computational comparison and adjudication. *Consensus text* — the reconciled text
resulting from that adjudication.

**The takeaway for this page:** Two independent passes rarely err identically, so
disagreement between them localizes error precisely.

---

## **02 Content**

**The Accuracy Double-Keying Achieves**

The method's reputation rests on measured performance, and the figures are worth
knowing because they set the standard your own work is measured against.

Commercial data entry services employing double-keying routinely guarantee
character accuracy between 99.95% and 99.98%. The German Research Foundation's
practical guidelines on digitization stipulate a threshold of 99.997%, which
yields a corpus that is, in the phrase generally used, virtually error-free (Haaf
et al., 2013).

| Accuracy | Errors per 100,000 characters | Context |
| --- | --- | --- |
| 99.9% | 100 | Common vendor minimum |
| 99.95% | 50 | Typical commercial double-keying |
| 99.98% | 20 | High-end commercial double-keying |
| 99.997% | 3 | DFG digitization guideline |

Put those numbers against your own folio. A twenty-four-line folio of Greek
minuscule may contain around 1,500 characters. At 99.9% accuracy that is between
one and two errors on the page; at 99.997% it is a 5% chance of a single error.
The difference between those two states determines whether Week 5's measurements
are trustworthy at the precision you will report them.

Note also that these figures come from mass digitization of *printed* text — early
modern Fraktur, difficult but typographically regular. Manuscript transcription of
an unfamiliar hand is harder, and single-pass accuracy is correspondingly lower.
Your first pass is very unlikely to have been at 99.9%.

This is not a reason for discouragement. It is the reason double-keying exists, and
the reason today's session is a required step rather than an optional refinement.

**The takeaway for this page:** Double-keying reaches 99.95% or better on printed
text; a single manuscript pass is well below that, which is why today is required.

---

## **03 Content**

**The Non-Native Transcriber Insight**

One methodological detail of professional double-keying is genuinely
counter-intuitive and directly useful to you today.

The Deutsches Textarchiv outsourced its primary transcription to **non-native
speakers** working to a strict double-keying protocol — transcribers who could not
read German (Haaf et al., 2013). This was deliberate, not a cost measure alone.

The reasoning: by severing the transcriber's semantic comprehension from their
visual recognition of graphemes, the method neutralizes the psychological
phenomenon of auto-correction, in which a reader who understands the text
unconsciously modernizes a historical spelling or mentally supplies an omitted
character (Haaf et al., 2013).

This is the same failure you were warned about in Lesson 4.1 section 10: reading
what you expect rather than what is written. A transcriber who does not know the
language cannot make that error, because they have no expectations to impose. Their
disadvantage — no linguistic knowledge to resolve ambiguity — is precisely their
advantage.

You cannot un-know Greek for today's session. You can approximate the condition:

- Do not reread last week's transcription before starting. Independence is the whole point.
- Transcribe letter by letter rather than word by word, resisting the urge to read.
- On familiar passages, transcribe backwards from the end of the line.
- Cover the rest of the line so only the letters you are transcribing are visible.
- Take breaks; expectation errors increase with fatigue.

The first is the essential one and the most tempting to skip. A second pass
conducted with the first pass in view is not a second pass; it is proofreading,
which finds a different and smaller class of error.

**The takeaway for this page:** Professional double-keying uses transcribers who
cannot read the language, because comprehension causes auto-correction — so do not
reread your first pass.

---

## **04 Content**

**Two Classes of Error**

Evaluating a transcription requires distinguishing two error classes that behave
entirely differently, and conflating them is why some quality control fails.

**Typographical errors** occur at the character level: omissions, substitutions,
and insertions of textual content. They are what CER measures, and double-keying
addresses them directly.

**Structural errors** occur in the XML or TEI markup layer: a failure to capture
the semantic or physical architecture of the document. Misidentifying a marginal
note as a primary paragraph, misapplying a speaker tag, or attaching a line break
to the wrong place are structural errors, and no amount of character-level accuracy
detects them (Haaf et al., 2013).

| | Typographical | Structural |
| --- | --- | --- |
| Occurs in | The character stream | The markup layer |
| Detected by | Double-keying comparison; CER | Schema validation; Schematron; human review |
| Example | ἐγένετο for ἐγένοντο | A gloss encoded as body text |
| Consequence | A wrong reading | The document misrepresents the object |
| Severity | Localized | Can invalidate downstream processing |

The separation is vital: typographical fidelity is meaningless if the structural
scaffolding renders the text computationally unreadable to parsing algorithms
(Haaf et al., 2013).

The DTA's experience is instructive here. Their typographical error rate from
double-keying was vanishingly small, while structural errors — the incorrect
demarcation of a marginal note, a misapplied speaker tag — required sophisticated
XML validation schemas such as Schematron and continuous quality control to resolve
(Haaf et al., 2013). The hard problem was not the characters.

Today addresses both. Double-keying finds your typographical errors; a separate
structural review finds the encoding ones. Do not assume that agreement on
characters implies agreement on markup.

**The takeaway for this page:** Double-keying finds character errors and cannot
find structural ones — perfect characters in wrong markup still misrepresent the
document.

---

## **05 Content**

**Running Your Second Pass**

Do this now, before reading further, because everything after depends on having a
genuinely independent second transcription.

- Open the same folio at the same zoom you used last week.
- Do **not** open last week's transcription. Do not glance at it.
- Create a new file: `transcription/f42r_pass2.xml`.
- Transcribe the full folio, with the same conventions as last week.
- Encode line breaks, abbreviations, uncertainty, and corrections as before.
- Mark uncertainty honestly, without trying to recall what you decided last time.
- Save, validate, and commit before comparing.

That last step matters procedurally. Commit the second pass *before* looking at the
first, so the repository records what you produced independently. If you compare
first and commit afterwards, the committed second pass may have been silently
influenced, and the independence claim is no longer verifiable.

```text
feat(transcription): second independent pass, f. 42r

Double-keying pass 2. Transcribed without reference to pass 1, at full
zoom, per the conventions in CONVENTIONS.md. Committed before comparison
so that independence is verifiable in the history.

Human-Verified: true
AI-Generated: false
```

Expect this pass to be faster than the first. You now know the hand, the
abbreviations, and the difficult regions. Speed is fine; the failure to guard
against is transcribing from memory of last week rather than from the image. If you
find yourself typing a line before reading it, stop and reread the image.

**The takeaway for this page:** Commit the second pass before comparing, so that
its independence is verifiable in the history rather than merely asserted.

---

## **06 Content**

**Comparing the Two Passes**

With both passes committed, compare them computationally. Do not compare by eye —
the differences are exactly the things eyes skip.

The simplest comparison uses tools you already have:

```bash
git diff --no-index transcription/f42r_pass1.xml transcription/f42r_pass2.xml
```

For a line-by-line view that separates textual from structural differences,
extract the text stream first:

```python
import re, unicodedata
from pathlib import Path

def lines(path):
    """Extract (line_number, text) pairs from a TEI transcription."""
    xml = Path(path).read_text(encoding="utf-8")
    xml = unicodedata.normalize("NFC", xml)
    out = []
    for m in re.finditer(r'<lb n="(\d+)"[^>]*/>(.*?)(?=<lb |</div>)', xml, re.S):
        text = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        out.append((m.group(1), text))
    return out

p1, p2 = lines("transcription/f42r_pass1.xml"), lines("transcription/f42r_pass2.xml")
for (n1, t1), (n2, t2) in zip(p1, p2):
    if t1 != t2:
        print(f"line {n1}\n  pass1: {t1}\n  pass2: {t2}\n")
```

Note the NFC normalization on input. Without it, two transcriptions typed in
different sessions may differ in normalization form and report differences at every
accented character — a false positive that would swamp the real findings. This is
Lesson 1.2 section 10 arriving in practice again.

Check the line counts first. If the two passes have different numbers of lines, one
contains a line skip, and you must find and fix it before any line-by-line
comparison is meaningful.

**The takeaway for this page:** Normalize to NFC before comparing, or every
accented character reports as a difference — and check line counts before anything
else.

---

## **07 Content**

**Reading the Disagreements**

Every difference between the passes is a place where at least one of them is
wrong. Adjudicate each one against the image.

The procedure for each disagreement:

- Open the line's region using the zone binding from Lesson 3.3.
- Look at the ink at full zoom. Do not reason from context first.
- Decide what the manuscript shows.
- Record the decision and the reason.
- If it remains genuinely unresolvable, encode `<unclear>` with the alternatives noted.

Resist two temptations. The first is choosing whichever reading makes better sense
— that is reasoning from expectation, the failure the whole method exists to
neutralize. Look at the ink. The second is assuming the first pass was right
because it was the one you trained on; if anything, the second pass is the better
informed, since you now know the hand.

Categorize as you go, because the categories are diagnostic:

| Disagreement type | Typical cause | What it tells you |
| --- | --- | --- |
| Confusable letterforms | Palaeographic similarity in this hand | Add to `HAND.md` |
| Diacritic present or absent | Faint mark; ambiguous placement | Region may need better imaging |
| Different accent type | Acute versus grave, contextual | Convention question, not a reading question |
| Abbreviation read differently | Unfamiliar mark | Add to the abbreviation repertoire |
| Word division differs | *Scriptio continua* | Convention question |
| A whole word differs | Expectation error in one pass | The dangerous kind; check carefully |
| Line skip | Position lost | Fix the alignment first |

The sixth row is the one to slow down for. Where two passes produce entirely
different words, one of them was almost certainly produced by reading rather than
seeing — and if the two words are both plausible in context, the ink is the only
arbiter.

**The takeaway for this page:** Adjudicate by looking at the ink, not by choosing
the reading that makes better sense — that is the error the method exists to
neutralize.

---

## **08 Content**

**Building the Consensus Text**

The reconciled result is the **consensus text**, and it should be built as a
distinct artefact rather than by editing one pass in place.

Create `transcription/f42r_consensus.xml`, and for each line record the adjudicated
reading. Where both passes agreed, the consensus is that reading. Where they
disagreed, the consensus is your adjudication. Where adjudication failed, the
consensus carries `<unclear>` with both candidate readings recorded.

Recording an unresolvable disagreement:

```xml
<lb n="14" facs="#f42r_l14"/>ἦν ὁ λόγος <choice>
  <unclear reason="faded" cert="low" resp="#KMP">ἐγένετο</unclear>
  <unclear reason="faded" cert="low" resp="#KMP">ἐγένοντο</unclear>
</choice> πρὸς
```

This is more honest than choosing. Two independent readings of the same ink
produced two different results and inspection did not resolve it — that is a fact
about the evidence, and recording it preserves information that choosing would
discard. In Week 8 this becomes an apparatus entry; in Week 12 it may become a
paragraph of commentary.

Keep all three files. The two passes and the consensus are separate evidence: the
passes document what independent transcription produced, and the consensus
documents what adjudication concluded. Deleting the passes once the consensus
exists destroys the record of how it was reached.

Commit the consensus separately, with a message recording how many disagreements
were found and how they were resolved.

**The takeaway for this page:** Keep both passes alongside the consensus — the
passes are the evidence for how the consensus was reached.

---

## **09 Content**

**Inter-Annotator Agreement**

Having compared two transcriptions, you can quantify how much they agreed — which
is a statement about the reliability of your ground truth rather than about its
correctness.

The naive measure is **percentage agreement**: the proportion of positions where
the two passes match. It is easy to compute and structurally flawed, because it
takes no account of agreement occurring by chance (Haaf et al., 2013).

Chance-adjusted metrics correct for this:

| Metric | Raters | Handles | Principal limitation |
| --- | --- | --- | --- |
| Cohen's kappa | Exactly 2 | Categorical data | Two raters only; kappa paradoxes on skewed data |
| Fleiss' kappa | More than 2 | Categorical data | Assumes raters drawn at random from a population |
| Krippendorff's alpha | Any number | Missing data; nominal, ordinal, continuous | Computationally complex; often needs bootstrapping |

Cohen's kappa compares observed agreement against the agreement expected by chance,
given each rater's marginal distribution. A value of 1 is perfect agreement; 0 is
agreement no better than chance (Haaf et al., 2013).

Its known weakness matters for manuscript work. Where a phenomenon is rare — a
specific scribal abbreviation appearing twice on a folio — highly skewed marginals
inflate the expected chance agreement, so high observed agreement can paradoxically
produce a low kappa (Haaf et al., 2013). Do not over-interpret a low kappa on rare
categories.

**Krippendorff's alpha** is the most robust for this domain. It computes observed
against expected *disagreement* rather than agreement, handles any number of
raters, accommodates missing data — a frequent occurrence when one annotator skips
a damaged word another attempts — and supports nominal, ordinal, and continuous
data (Haaf et al., 2013).

**The takeaway for this page:** Percentage agreement ignores chance; use a
chance-adjusted metric, and prefer Krippendorff's alpha because it handles missing
data.

---

## **10 Content**

**Computing Agreement on Your Passes**

For your two passes, a practical measure is per-character agreement over aligned
lines.

```python
def agreement(a: str, b: str) -> float:
    """Proportion of positions where two aligned strings match."""
    import unicodedata
    a = unicodedata.normalize("NFC", a)
    b = unicodedata.normalize("NFC", b)
    if not a and not b:
        return 1.0
    matches = sum(1 for x, y in zip(a, b) if x == y)
    return matches / max(len(a), len(b))
```

Compute it per line and overall. Report both, because the distribution is more
informative than the mean: agreement of 98% spread evenly across the folio means
something different from 100% on twenty lines and 75% on four.

| Observation | Interpretation |
| --- | --- |
| High agreement throughout | The transcription is probably reliable |
| High agreement, a few low lines | Those lines are where the evidence is hard |
| Uniformly moderate agreement | Convention inconsistency, or the hand is difficult |
| Agreement collapses after a point | Line skip; realign before interpreting anything |

The fourth row is worth checking for explicitly. If agreement is good for twelve
lines and then poor for the rest, you almost certainly have a line skip in one pass
rather than a genuinely harder second half. Realign and recompute.

For a two-rater comparison, a chance-adjusted metric adds relatively little on
character-level data, where the category space is large and chance agreement is
consequently low. The metric matters more for *categorical* judgements — whether a
mark is an accent or punctuation, whether a region is damage or discoloration —
where the category count is small. If you and a classmate adjudicate such
judgements independently, kappa is the appropriate measure.

**The takeaway for this page:** Report the distribution of agreement, not just the
mean — a sudden collapse means line skip, not difficulty.

---

## **11 Content**

**Case Study: The Deutsches Textarchiv**

The DTA is the reference implementation of mass double-keying and repays study,
because its choices were deliberate and its reasoning is documented.

Digitizing printed works in New High German from 1600 to 1900, the DTA **bypassed
OCR entirely** for its foundational texts. The decision acknowledged the severe
limitations of optical recognition on early modern Fraktur fonts, irregular
inking, and highly variable historical spelling. By January 2016 the archive held
2,331 texts, approximately 1.1 billion characters (Haaf et al., 2013).

Note what that decision implies. A major, well-resourced digitization project,
facing difficult typography and irregular orthography, concluded that manual
double-keying was more economical than OCR plus correction — which is the same
threshold argument from Lesson 4.2 section 14, applied at institutional scale.
Above a certain error rate, correction costs more than transcription.

The consensus texts were produced by non-native speakers under strict double-keying
protocol, with vendors guaranteeing minimum character accuracy of 99.9%. Following
algorithmic reconciliation of the two data streams, the DTA applied linguistic
analysis and rule-based heuristics to normalize historical spellings to modern
lemmas, enabling phonetic and lemma-based search across the corpus (Haaf et al.,
2013).

The last point connects to Week 6. Normalization happened *after* reconciliation,
as a separate layer over a verified diplomatic base — not silently during
transcription. The diplomatic text and the normalized text both exist, and the
relationship between them is recorded. That is exactly the architecture your
edition is building.

**The takeaway for this page:** The DTA rejected OCR for difficult typography and
normalized only after reconciliation — a separate layer over a verified diplomatic
base.

---

## **12 Content**

**Structure and the Base Format**

The DTA's second contribution concerns the structural error class from section 04.

All DTA transcriptions were mapped to the **DTA Base Format** (DTABf), a strict
customized subset of TEI P5 designed to enforce standardized structural markup
across a massive heterogeneous collection (Haaf et al., 2013).

The reasoning is worth understanding, because it applies to your own edition. TEI
P5 is deliberately permissive: it offers many ways to encode the same phenomenon,
so that projects with different needs can all use it. That permissiveness is a
problem at scale, because two transcribers can both produce valid TEI that encodes
the same feature differently, and the resulting corpus is not uniformly
processable.

A customized subset removes the choice. By constraining which elements may be used
where, DTABf ensured that a marginal note is encoded one way across 2,331 texts —
which is what makes corpus-wide querying possible.

| Approach | Flexibility | Consistency | Suited to |
| --- | --- | --- | --- |
| Full TEI P5 | Maximal | Requires discipline | Single editions |
| A customized subset (ODD) | Constrained | Enforced by schema | Corpora; collaborative projects |
| Ad-hoc conventions | Maximal | None | Nothing |

The DTABf later evolved into DTABf-M for manuscripts, expanding the subset to
accommodate the physical architectures of handwritten documents — which
demonstrated, in the project's own terms, that transcription accuracy is
inseparable from structural encoding accuracy (Haaf et al., 2013).

For your edition, the practical equivalent is your `CONVENTIONS.md` from Lesson
4.1. It is an informal ODD: a statement of which encoding choices you make. Where
you find structural inconsistency between your two passes today, the remedy is to
make the convention explicit rather than to fix the instances.

**The takeaway for this page:** TEI permits several valid encodings of the same
feature, so consistency requires an explicit convention — your `CONVENTIONS.md` is
that document.

---

## **13 Content**

**Reviewing Structural Agreement**

Double-keying compares character streams. Structural agreement needs separate
review, and today is when to do it.

Compare the two passes for encoding decisions rather than for text:

| Question | Where inconsistency appears |
| --- | --- |
| Were the same abbreviations marked as abbreviations? | `<abbr>` counts differ |
| Were the same readings marked unclear? | `<unclear>` counts differ |
| Were gaps measured the same way? | `@extent` values differ |
| Were scribal corrections encoded the same way? | `<subst>` present in one pass only |
| Were line breaks placed identically? | `<lb/>` counts differ |
| Was word division applied consistently? | Whitespace differences throughout |

```bash
for f in transcription/f42r_pass1.xml transcription/f42r_pass2.xml; do
  echo "$f"
  for tag in lb abbr unclear gap subst; do
    printf "  %-8s %s\n" "$tag" "$(grep -o "<$tag[ />]" "$f" | wc -l)"
  done
done
```

Differences here are more informative than they look. If pass 1 marked six readings
unclear and pass 2 marked two, that is not a transcription disagreement — it is an
inconsistent threshold for what counts as uncertain. The remedy is to define the
threshold in `CONVENTIONS.md` and apply it uniformly, not to split the difference.

The same holds for abbreviations. If one pass marked a form as an abbreviation and
the other transcribed it as written without marking, you have discovered an
undecided convention. Decide it now.

Structural inconsistencies found today are cheap to fix. Found in Week 8, when the
apparatus depends on them, they require revisiting the whole transcription.

**The takeaway for this page:** Differing `<unclear>` counts signal an inconsistent
threshold, not a disagreement about the text — fix the convention, not the
instances.

---

## **14 Content**

**Consensus Without a Second Person**

An honest limitation. Professional double-keying uses two *different* transcribers.
You are doing two passes yourself, which is weaker.

The weakness is correlated error. Your two passes share a transcriber, which means
they share the same palaeographic misunderstandings, the same expectations about
the text, and the same blind spots. Where you consistently misread a letterform,
both passes will misread it identically, agreement will be perfect, and the error
will pass through undetected.

| Method | Catches | Misses |
| --- | --- | --- |
| Single pass | — | Everything undetected |
| Self double-keying | Lapses, slips, momentary misreadings | Systematic misunderstandings |
| Two transcribers | Both classes | Errors both make |
| Two transcribers, one without the language | Both classes; expectation errors | Little |

Mitigations available to you:

- **Exchange with a classmate.** Transcribe ten lines of each other's passage and compare. A second reader catches exactly what self-double-keying cannot.
- **Compare against the machine.** Where your two passes agree and both machine outputs disagree, examine that point specifically. Consistent human agreement against consistent machine disagreement may indicate a shared human misunderstanding.
- **Check your letterform inventory.** Review `HAND.md` against the manuscript, verifying that each identification is right rather than merely consistent.
- **Leave time between passes.** The longer the interval, the less the second pass is influenced by memory of the first.

The second mitigation is genuinely useful and connects the week's two halves. Your
HTR model has no expectations about Greek and no palaeographic misunderstandings —
only ink-level errors. Where it disagrees with both your passes, it is worth
looking at the ink again.

**The takeaway for this page:** Self double-keying cannot catch your systematic
misunderstandings — exchange lines with a classmate, and examine points where the
machine disagrees with both passes.

---

## **15 Content**

**Where Human and Machine Errors Differ**

The reconciliation of human disagreement operates on different premises from the
scoring of machine output, and understanding the difference shapes how you
adjudicate.

Human disagreement is weighted toward **cognitive substitutions** — misreading one
letterform as a palaeographically similar one — and mechanical transposition
errors from typing. Consensus is reached by targeted manual arbitration against the
document, often using agreement metrics to identify which transcriber is
consistently deviating from the palaeographic reality (Haaf et al., 2013).

Machine error topology is systematically different. HTR models struggle with
macro-structural preservation, exhibiting high insertion and deletion rates at the
physical boundaries of text lines. Line-end hyphenation is a persistent anomaly:
models frequently fail to reconstruct a word fractured across lines, treating the
fragment at the end of one line and the beginning of the next as unrelated tokens
— which inflates word error rate and destroys semantic coherence (Bawden et al.,
2026).

| | Human transcriber | HTR model | Language model |
| --- | --- | --- | --- |
| Characteristic error | Cognitive substitution; typing slip | Line-boundary insertion and deletion | Statistically expected substitution |
| Behaviour on the unfamiliar | Transcribes what is seen, even if meaningless | Produces an impossible sequence | Substitutes a probable word |
| Line-end hyphenation | Handled by comprehension | Frequently fractured | Frequently silently joined |
| Out-of-vocabulary forms | Transcribed as seen | Attempted from ink | Replaced with a higher-probability word |

The bottom row states the essential difference. AI transcriptions are susceptible
to out-of-vocabulary failures: a unique toponym or idiosyncratic spelling absent
from training data is often replaced by a visually similar but linguistically
incorrect word with higher probability in the model's lexicon (Haaf et al., 2013).

The formulation worth remembering: **human transcribers transcribe what they see,
even when it makes no sense; models transcribe what they statistically expect to
see** — which introduces pervasive anachronism (Haaf et al., 2013).

Your job in adjudication is to be the first kind of reader.

**The takeaway for this page:** Humans transcribe what they see even when it makes
no sense; models transcribe what they expect — which is why unique forms are
exactly where models fail.

---

## **16 Content**

**Line-End Hyphenation and CTC Alignment**

A specific reconciliation problem worth knowing, because it may affect your
measurements on Friday and because its solution is instructive.

The Bullinger dataset comprises 3,622 sixteenth-century letters in Latin and
premodern German. Expert historians had produced highly accurate transcriptions —
but as continuous paragraphs, with no spatial layout information, which made them
useless for training layout-aware HTR systems. When automated tools aligned these
transcriptions to line images, they introduced systematic hyphenation errors,
fracturing words spanning line breaks (Peer et al., 2025).

The solution used a **connectionist temporal classification alignment algorithm**.
It takes the layout-free expert transcription together with the character posterior
probabilities produced by HTR models, and uses dynamic programming to find the
optimal placement of line breaks in the continuous text so that it matches the
visual layout of the page (Peer et al., 2025).

The result contained a genuine paradox worth noting. Alignment accuracy was
frequently *higher* using a weakly trained HTR model than a highly optimized one —
because the weaker model had not yet overfitted to the faulty, hyphen-broken
training data (Peer et al., 2025). A more accurate model had learned the error and
reproduced it; a less accurate one had not.

By iteratively filtering alignments on a confidence threshold and retraining, the
researchers improved the PyLaia model's CER by 1.1 percentage points without further
manual labour (Peer et al., 2025).

The lesson for your reconciliation: establishing a consensus text is not only about
correcting characters but about reconciling the transcription with the physical
coordinates of the page. Your `<lb/>` elements and their `@facs` bindings are that
reconciliation, which is why the line-count check in section 06 comes first.

**The takeaway for this page:** Consensus means reconciling text with the page's
physical coordinates, not only correcting characters — which is why line alignment
is checked first.

---

## **17 Content**

**Consensus as a Living Document**

An alternative model worth knowing, because it applies to your Week 13 publication.

The Australian Newspaper Digitisation Program faced conditions where double-keying
was financially impossible. Raw OCR accuracy on historical newspapers ranged from
71% to 98%, well below the threshold for reliable full-text search, and the IMPACT
project estimated manual keying at roughly one euro per page — so a single large
volume could consume upwards of a thousand euros in transcription alone (Haaf et
al., 2013).

Their hybrid response: contractors manually corrected only the high-value
structural and metadata elements — article titles, subtitles, and the first four
lines of text — to a guaranteed 99.5% accuracy. For the remaining body text, the
programme exposed raw OCR alongside the scanned image through the Trove platform
and let volunteers reconcile it line by line (Haaf et al., 2013).

Complementing human effort, institutions also deploy **Recognizer Output Voting for
Error Reduction** (ROVER), which aligns the hypotheses of several different OCR
engines on the same image and uses majority voting with dynamic programming to
select the most probable character at each position, driving down error before
human intervention (Haaf et al., 2013).

The structural insight is the interesting one: a consensus text does not
necessarily need to be complete before publication. The digital edition can
function as a living document that asymptotically approaches accuracy through
continuous decentralized post-correction (Haaf et al., 2013).

This bears on Week 13. Your edition need not claim finality. An edition that
publishes its text with recorded uncertainty, exposes the images alongside it, and
provides a mechanism for correction is more honest than one that presents a
settled text — and the version control history is precisely the mechanism that
makes such correction traceable.

**The takeaway for this page:** A published edition can be a living document that
improves through recorded correction, rather than a text claiming finality.

---

## **18 Content**

**ROVER and Your Three Transcriptions**

The voting idea applies directly to what you now have.

You hold, or will by Friday, four transcriptions of the same lines: two independent
manual passes, the HTR output, and the VLM output. ROVER's logic — align multiple
hypotheses and take the majority at each position — can be applied to them.

It should be applied *carefully*, because the hypotheses are not equally reliable
and majority voting treats them as if they were.

| Configuration | Sensible? | Reason |
| --- | --- | --- |
| Vote across your two manual passes | Yes, in effect | This is double-keying |
| Vote across HTR and VLM outputs | No | Both unreliable; the majority may be wrong |
| Vote across all four equally | No | Weights two machine outputs above your adjudication |
| Use machine agreement as a flag for review | Yes | Points at places worth re-examining |

The fourth row is the usable version. Where both machine outputs agree with each
other and disagree with both your passes, that point deserves another look at the
ink. It may be a shared machine error — both models misreading the same ambiguous
form — or it may be that both machines read the ink correctly and you brought an
expectation to it twice.

That configuration is exactly the mitigation from section 14 for self-double-keying's
weakness. Your two passes are correlated; the machines' errors are not correlated
with yours. Their agreement against you is a signal precisely because it comes from
a different error distribution.

Note the points where this occurs and check them Friday when the full comparison is
assembled.

**The takeaway for this page:** Where both machines agree against both your passes,
look again — their errors are uncorrelated with yours, so their agreement is a real
signal.

---

## **19 Content**

**Recording the Reconciliation**

Document today's process, since Friday's report requires it and reconstruction is
harder than recording.

In `logs/reconciliation-w5.md`, record:

- When each pass was made, and the interval between them.
- Confirmation that pass 2 was made without reference to pass 1.
- Line counts for both passes, and whether they matched.
- The number of disagreements found.
- Each disagreement: line, both readings, the adjudicated result, the reason.
- Disagreements that remained unresolved, and how they were encoded.
- Structural inconsistencies found, and the conventions decided as a result.
- Overall and per-line agreement figures.
- Whether a classmate reviewed any lines, and what that found.

The per-disagreement record is the valuable part and the part students compress.
"Line 14: pass 1 ἐγένετο, pass 2 ἐγένοντο; adopted ἐγένοντο on inspection at full
zoom — the fourth letter has a clear nasal stroke; pass 1 was an expectation error
from the parallel at line 11" is a scholarly note. "Line 14: fixed" is not.

This document is a required component of the Transcription Assignment due Friday
October 2, and its quality is a substantial part of what is assessed. It is also
the raw material for your Week 12 commentary, where several of these adjudications
will need to be explained to a reader.

Commit it with a `docs:` prefix.

**The takeaway for this page:** Record each disagreement with both readings, the
adjudication, and the reason — that record is the assignment and the seed of your
commentary.

---

## **20 Content**

**Committing the Consensus**

The consensus text becomes your new ground truth. Commit it accordingly.

```text
feat(transcription): consensus text for f. 42r from double-keying

Reconciled pass 1 (commit a3f9c21) and pass 2 (commit 7d2e814) by
adjudicating all differences against the facsimile at full zoom.

19 disagreements over 24 lines. 14 resolved in favour of pass 2, 3 in
favour of pass 1, 2 unresolved and encoded as <unclear> with both
candidates recorded. Adjudications documented individually in
logs/reconciliation-w5.md.

Three structural inconsistencies found and resolved by amending
CONVENTIONS.md: the threshold for <unclear>, the treatment of
line-final word breaks, and whether ambiguous accents are recorded.

Overall character agreement between passes: 97.8%.

Human-Verified: true
AI-Generated: false
Supersedes-Ground-Truth: gt-f42r
```

Then tag it, because Friday's measurements will be computed against this state
rather than against last week's:

```bash
git tag -a gt-f42r-consensus -m "Consensus ground truth, f. 42r, after double-keying"
```

Keep the original `gt-f42r` tag. It records what Week 4's measurements were
actually computed against, and deleting it would make those measurements
irreproducible. Friday will compute against the consensus, and the difference
between the two sets of figures is itself informative — it shows how much of Week
4's measured error was your error rather than the machines'.

**The takeaway for this page:** Tag the consensus but keep the original ground
truth tag — the difference between measurements against each shows how much error
was yours.

---

## **21 Content**

**How Much Did the Ground Truth Change?**

A quick analysis worth doing today, because it directly conditions Friday's
interpretation.

Compute the character error rate of your *original* pass 1 against the consensus.
This treats the consensus as correct and measures how wrong your Week 4 ground
truth was.

```bash
python3 tools/cer.py \
  --reference transcription/f42r_consensus.xml \
  --hypothesis transcription/f42r_pass1.xml
```

Suppose it returns 1.4%. That figure has a direct consequence: every machine error
rate you measured in Week 4 was computed against a reference that was itself 1.4%
wrong, and some proportion of what was scored as machine error was your error.

| Pass 1 error against consensus | Implication for Week 4 figures |
| --- | --- |
| Under 0.5% | Week 4 figures approximately valid |
| 0.5–2% | Machine error rates modestly inflated |
| Over 2% | Week 4 figures should be recomputed against the consensus |
| Over 5% | The original ground truth was not fit for purpose |

Report this figure in your reconciliation report. It is an honest statement about
the reliability of your own measurements, and reporting it is what distinguishes a
careful study from one that treats its reference as unquestionable.

It is also the empirical justification for double-keying, produced from your own
work. If pass 1 was 1.4% wrong, then double-keying improved your ground truth by
that margin — and you can say so with a number rather than on authority.

**The takeaway for this page:** Measure pass 1 against the consensus — that number
states how much of Week 4's measured machine error was actually yours.

---

## **22 Content**

**Preparing for Friday**

Friday computes CER and WER for both machine passes against the consensus, and
produces the reconciliation report.

Bring:

- The consensus text, validated, committed, and tagged.
- Both individual passes, committed.
- The reconciliation log with per-disagreement records.
- Week 4's raw HTR output, tagged `htr-w4-raw`.
- Week 4's raw VLM output, tagged `vlm-w4-raw`.
- The error categorizations from Week 4.
- Your timings for all methods.
- The pass 1 against consensus error rate from section 21.

Everything must be **line-aligned** for Friday's measurement to be meaningful. If
the VLM output lost line breaks — the failure from Lesson 4.3 section 06 — you will
need either to realign it manually or to compute whole-text figures and state the
limitation. Decide which today rather than discovering the problem on Friday.

Verify the tags exist and are pushed:

```bash
git tag -l && git ls-remote --tags origin
```

Tags existing only locally are not available if you work from another machine, and
Friday's measurement retrieves the tagged states.

**The takeaway for this page:** Ensure all outputs are line-aligned and all tags
are pushed — Friday's measurement retrieves tagged states and needs line alignment.

---

## **23 Content**

**A Note on Today's Date**

Wednesday September 30 is the National Day for Truth and Reconciliation, and the
university is closed.

The schedule notes that this week is a two-step week by design: reconciliation is
itself the comparison, so the missing Wednesday costs nothing methodologically.
The week runs manual on Tuesday and measurement on Friday, and the deterministic
step is not needed because the comparison *is* the deterministic step.

The coincidence of terminology is worth acknowledging rather than passing over.
"Reconciliation" in this week's technical sense — the computational adjudication of
divergent text streams — has no connection to the meaning the national day carries.
The word does double duty in English, and the overlap is accidental.

It is a reasonable moment to note that the methods in this course are not neutral
with respect to whose documents get preserved, described, and edited. Digitization
programmes, cataloguing standards, and the corpora that train recognition models
all reflect decisions about what is worth the investment — and those decisions have
historically favoured some archives and some traditions over others. The
specialization gap you measured last week is partly a statement about which scripts
and languages are well represented in the data the world has chosen to create.

That observation is not this week's assignment. It is worth holding as you work.

**The takeaway for this page:** The week's technical sense of "reconciliation" is
unrelated to the national day; the coincidence is a reasonable moment to notice
whose documents digitization has prioritized.

---

## **24 Content**

**Checklist Before You Leave**

Verify each.

- Pass 2 transcribed independently, without consulting pass 1.
- Pass 2 committed before any comparison was made.
- Line counts compared; any skip found and fixed.
- Both passes NFC-normalized before comparison.
- All differences identified computationally, not by eye.
- Each difference adjudicated against the image at full zoom.
- Each adjudication recorded with its reason.
- Unresolvable differences encoded with both candidates.
- Structural inconsistencies identified and conventions amended.
- Consensus text built as a separate file.
- Consensus validated against the TEI schema.
- Agreement figures computed, overall and per line.
- Pass 1 error rate against the consensus computed.
- Reconciliation log written.
- Consensus committed and tagged; original tag retained.
- Tags pushed.

If the second pass is unfinished, finish it before Friday. Friday's measurements
are computed against the consensus, and without a consensus there is nothing to
measure against but the unverified Week 4 text.

**The takeaway for this page:** Friday measures against the consensus, so an
unfinished second pass blocks the session.

---

## **25 Content**

**Common Problems Today**

Failures that recur.

| Symptom | Cause | Remedy |
| --- | --- | --- |
| Differences at every accented character | Passes in different normalization forms | NFC-normalize both before comparing |
| Agreement collapses partway through | Line skip in one pass | Realign, then recompare |
| Almost no differences found | Pass 2 was not independent | Redo, without consulting pass 1 |
| Very many differences | Convention drift between passes | Decide conventions; recompare |
| Line counts differ by one | Skip, or a split or merged line | Find it before anything else |
| Adjudications all favour pass 1 | Anchoring to the first reading | Re-examine; the ink decides |
| `<unclear>` counts differ substantially | No agreed uncertainty threshold | Define it in `CONVENTIONS.md` |

The third row deserves comment because it is common and self-deceiving. If your two
passes are nearly identical, the likeliest explanation is not that your
transcription is excellent but that the second pass was influenced by memory of the
first. Genuine independence produces genuine disagreement — a folio of unfamiliar
Greek should produce a meaningful number of differences, and their near-absence is
evidence about the method rather than about the accuracy.

The sixth row is the subtler bias. If every adjudication resolves toward pass 1,
ask whether you are examining the ink or defending your first reading. Pass 2 was
made with more knowledge of the hand and has, if anything, the better claim.

**The takeaway for this page:** Near-identical passes usually mean the second was
not independent — genuine independence produces genuine disagreement.

---

## **26 Content**

**What Good Work Looks Like Here**

The standard.

A minimally acceptable result is a second pass, a comparison, and a consensus text.

Good work additionally:

- Achieves genuine independence and can demonstrate it from the commit order.
- Compares computationally with normalization applied.
- Adjudicates every difference against the image rather than by plausibility.
- Records each adjudication with its palaeographic reason.
- Preserves unresolvable disagreements rather than choosing arbitrarily.
- Separates structural from typographical disagreement.
- Amends conventions where inconsistency is found, rather than patching instances.
- Quantifies agreement and reports its distribution.
- Measures how wrong the original ground truth was, and says so.
- Notes points where machine outputs agree against both human passes.

The ninth item is the one that most distinguishes careful work. Reporting that your
Week 4 ground truth was 1.4% inaccurate is an admission, and it is also the single
most useful thing you can tell a reader about the reliability of your Week 4
measurements. An editor who reports the limitations of their own reference is one
whose figures can be trusted.

**The takeaway for this page:** Reporting how wrong your own ground truth was is
what makes your other figures trustworthy.

---

## **27 Content**

**The Epistemology of the Consensus Text**

A conceptual note, since "consensus text" can suggest something it is not.

The consensus text is not the *true* text of the manuscript. It is the best
reconstruction available from two independent readings plus adjudication against
the image. It remains a hypothesis, held with more confidence than either pass
alone, and revisable.

This is worth stating because the term invites a false confidence. "Consensus"
suggests settlement, and the text you produce today is the current state of an
argument rather than its conclusion. Three folios later you may understand the hand
well enough to see that a reading you settled today was wrong.

The version-controlled architecture is what accommodates this. A consensus text
that turns out to be wrong is corrected by a further commit, with the reason
recorded, and the earlier state remains retrievable. Nothing is lost, and the
history of the reading is preserved — which is exactly the capability Lesson 1.1
argued Giarratano's print editions destroyed.

| Stage | Confidence | Revisable? |
| --- | --- | --- |
| Single pass | Low | Yes |
| Consensus of two passes | Higher | Yes |
| Consensus reviewed by a second person | Higher still | Yes |
| Published edition | Stated with recorded uncertainty | Yes, with a version history |

Note that the bottom row is still revisable. Section 17's living-document model
applies: publication is a state, not a termination, and an edition that records its
own uncertainty invites the correction that improves it.

**The takeaway for this page:** The consensus text is the current state of an
argument, not the true text — and the version history is what lets it be corrected
without loss.

---

## **28 Content**

**Extending Beyond One Folio**

A practical question. You have double-keyed one folio. Your edition covers more.

Full double-keying of every folio is expensive — roughly doubling transcription
cost, as section 02's table implied and as the IMPACT project's costings confirm
(Haaf et al., 2013). For a term project it is likely infeasible across the whole
passage.

The defensible compromise is stratified verification:

| Material | Verification | Rationale |
| --- | --- | --- |
| The training folio | Full double-keying | It determines model quality |
| Folios used for measurement | Full double-keying | Metrics depend on them |
| Difficult or damaged regions | Full double-keying | Highest error probability |
| Clean regions transcribed from HTR | Single careful correction pass | Machine output plus review |
| Regions with known variants | Full double-keying | Scholarly stakes are highest |

Whatever you choose, **state it**. An edition that double-keyed one folio and
single-passed the rest is perfectly respectable; an edition that implies uniform
verification it did not perform is not. The Week 13 editorial statement should say
exactly which parts of the text received which treatment.

This is the same principle as the imaging provenance in Lesson 3.2 and the AI
trailers in Lesson 1.1: the reader needs to know how each part of the edition was
produced in order to weigh it. Uniform presentation of non-uniform work is the
thing to avoid.

**The takeaway for this page:** Stratify verification by stakes and state which
parts received which treatment — uniform presentation of non-uniform work is the
failure.

---

## **29 Content**

**Connecting to Week 6**

Next week is normalization, and today's work is its precondition in a specific way.

Week 6 regularizes orthography: iotacism, orthographic variants, `<orig>` and
`<reg>` markup, hand-recorded decisions on Tuesday, a rule-based script on
Wednesday, AI-assisted normalization on Friday.

Every one of those operates *on the consensus text*. Normalizing an unverified
transcription means normalizing its errors, and worse, it means the normalization
decisions become entangled with transcription corrections — so that a later reader
cannot tell whether a difference between the diplomatic and normalized layers is a
regularization or a fix.

The DTA architecture from section 11 is the model: reconcile first, normalize
after, keep both layers, record the relationship. Your consensus text is the
diplomatic layer; Week 6 builds the normalized layer over it; and `<choice>` with
`<orig>` and `<reg>` records how each form relates to the other.

This is why the course order is what it is, and why normalizing during
transcription — the temptation Lesson 4.1 section 02 warned against — would have
foreclosed Week 6 entirely. The decisions are only available to be made
deliberately because they were not made silently.

**The takeaway for this page:** Week 6 normalizes over the consensus text — and
normalizing before reconciling would entangle regularizations with corrections
irrecoverably.

---

## **30 Content**

**Synthesis: Calibrating the Instrument**

The argument of this meeting.

Week 4 built a measuring instrument — a hand-produced diplomatic transcription
against which automated output could be scored. Today you calibrated it.

The calibration matters because an uncalibrated instrument produces measurements
that look precise and are not. A ground truth containing errors reports machine
error where none exists, teaches those errors to any model trained on it, and
biases every adjudication toward the reference's mistakes. None of this announces
itself: the error rates come out as numbers, and the numbers look fine.

Double-keying calibrates by exploiting a statistical fact: two independent readings
rarely err identically, so their disagreement localizes error precisely (Haaf et
al., 2013). The method reaches accuracies of 99.95% and better in professional use,
and the DTA's deliberate use of transcribers who could not read the language shows
how seriously the field takes the expectation problem you were warned about in
Week 4.

You have now also measured how far your original reference was off, which converts
"the ground truth was probably imperfect" into a number you can report.

**For Friday.** Bring the eight items in section 22, with everything line-aligned
and tagged. Friday computes CER and WER against the consensus and produces the
reconciliation report.

**Due Friday October 2.** The Transcription Assignment, including the
reconciliation report.

**The takeaway for this page:** An uncalibrated ground truth produces measurements
that look precise and are not — double-keying calibrates it, and the amount of
correction is itself a reportable figure.

---

## References

Bawden, R., Clérice, T., Glaise, A., Pinche, A., & Smith, D. (2026).
*Pre-editorial normalization for automatically transcribed medieval manuscripts in
Old French and Latin* (arXiv:2602.13905). https://arxiv.org/abs/2602.13905

Haaf, S., Wiegand, F., & Geyken, A. (2013). Measuring the correctness of
double-keying: Error classification and quality control in a large corpus of
TEI-annotated historical text. *Journal of the Text Encoding Initiative*, (4).
https://doi.org/10.4000/jtei.739

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
