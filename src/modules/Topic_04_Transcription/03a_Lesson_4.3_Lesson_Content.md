# Lesson 4.3 — LLM-Assisted Transcription: Hallucination, Bias, and the Specialization Gap

*RELS 398 / ENGL 398 · Topic 4: Transcription · Meeting #11 (Fri Sep 25)*

***Step 3 of the three-step cycle: AI-assisted. Remote delivery.** Today you run
the same passage through a general-purpose vision-language model and compare all
three transcriptions. The finding you are testing is that scale does not
substitute for exposure to the material.*

---

## **01 Content**

**Today's Question**

Three transcriptions of one passage now exist or will by the end of today: yours,
produced by hand on Tuesday; your fine-tuned HTR model's, produced Wednesday; and a
general-purpose vision-language model's, produced today.

The question is not which is best. It is **what each kind of system does, and what
each kind of error tells you about the system that made it.** A model that fails by
producing impossible letter sequences and a model that fails by producing fluent
invented Greek have failed differently, and the difference matters far more to a
scholarly editor than the aggregate error rate does.

You should have an expectation going in, from Wednesday's section 23. Published
benchmarks show general vision-language models performing excellently on modern
handwriting and catastrophically on historical scripts — 1.39% CER on modern
English against 52.23% on historical English, from the same model (AlKendi et al.,
2024). Today you test whether that pattern holds on your manuscript.

An expectation is not a conclusion. Run the experiment properly, record what
happens, and report what you find — including if it contradicts the literature.
Your manuscript may be unusually well represented in training data, or unusually
legible. A negative result against the published pattern would be interesting and
worth reporting.

**Vocabulary.** *Vision-language model (VLM)* — a model accepting images and text
and producing text. *Zero-shot* — applied without task-specific training.
*Hallucination* — fluent output not grounded in the input.

**The takeaway for this page:** The question is not which system is best but what
kind of error each makes — the kinds differ more than the rates.

---

## **02 Content**

**What a Vision-Language Model Is**

The architectural difference from Wednesday's tool determines everything that
follows.

A specialized HTR model is trained on line images paired with transcriptions. Its
entire competence is the mapping from ink to characters, and its knowledge of
language is whatever the character-level patterns in its training data implied.

A vision-language model is trained on vast heterogeneous internet corpora — text,
images, and their relationships — and possesses billions of parameters. It can
ingest an entire high-resolution page and produce a transcription from a natural
language instruction, with no layout analysis, no fine-tuning, and no ground truth
(AlKendi et al., 2024).

| | Specialized HTR | Vision-language model |
| --- | --- | --- |
| Training data | Line images with transcriptions | Internet-scale text and images |
| Parameters | Millions | Billions |
| Setup required | Layout correction, ground truth, training | A prompt |
| Input | One line image | A full page |
| Language knowledge | Weak, implicit | Extensive, explicit |
| Failure mode | Impossible sequences | Fluent invention |

The third row is the genuine advantage and should not be understated. Wednesday
cost you a session of layout correction, alignment, and training. Today costs a
prompt. If quality were comparable, the comparison would be over.

The sixth row is why it is not. A model with extensive language knowledge applies
that knowledge to ambiguous ink — and applying linguistic expectation to ambiguous
evidence is precisely what a diplomatic transcription must not do. The model's
greatest strength on modern text is its principal liability on historical
manuscripts.

**The takeaway for this page:** A VLM's linguistic knowledge is its strength on
modern text and its liability on manuscripts, because it resolves ambiguous ink by
expectation.

---

## **03 Content**

**The Specialization Gap, Quantified**

The empirical picture, which you should have in front of you before running your
own test.

| Dataset and domain | Model | CER | WER |
| --- | --- | --- | --- |
| IAM, modern English | GPT-4o | 1.39% | 3.46% |
| IAM, modern English | Claude 3.5 Sonnet | 8.55% | 10.28% |
| Bentham, historical English | GPT-4o | 52.23% | 72.16% |
| Bentham, historical English | Claude 3.5 Sonnet | 40.87% | 59.41% |
| READ2016, historical German | GPT-4o | 77.42% | 97.59% |
| READ2016, historical German | Qwen2-VL-7B | 76.25% | 97.77% |
| CATMuS, medieval Latin | TrOCR-Medieval-Base | 14.60% | — |
| CATMuS, medieval Latin | DeepSeek-OCR | 63.00% | — |
| CATMuS, medieval Latin | Mistral-OCR-3 | 84.70% | — |

Read the first and third rows together. The same model, GPT-4o, produces 1.39% CER
on modern English handwriting and 52.23% on historical English — a nearly fortyfold
increase from the same system on the same language, differing only in period
(AlKendi et al., 2024).

Read the last three rows together. On identical medieval Latin samples, a
domain-tuned model with orders of magnitude fewer parameters achieved 14.6% while
large commercial models produced 63.0% and 84.7% (Mattingly et al., 2024).

The 97% word error rates on historical German are worth pausing on. A WER
approaching 100% means essentially no word is correct. This is not degraded
performance; it is failure, on a task the same model performs excellently in a
modern setting.

This differential is the **specialization gap**. Domain-tuned models succeed
because they have been directly exposed to palaeographic variation, scribal
shorthand, idiosyncratic ligatures, and non-standard physical layouts (Mattingly et
al., 2024). Internet-scale training contains very little Byzantine minuscule.

**The takeaway for this page:** The same model achieves 1.39% CER on modern
handwriting and 52.23% on historical — the gap is period, not language.

---

## **04 Content**

**Over-Historicization**

Beyond raw error rates, VLMs exhibit failure modes that specialized models do not,
and the most striking is documented in detail.

**Over-historicization** is the algorithmic insertion of archaic characters that
are absent from the source document — characters belonging to an *earlier*
historical period than the manuscript being transcribed. The phenomenon was
documented in studies of eighteenth-century Russian texts printed in the Civil
font, where models hallucinated pre-Petrine Church Slavonic graphemes — the little
yus, omega, monograph uk, ot — that had been explicitly eliminated from the Russian
alphabet before the period being analyzed (Levchenko, 2024).

The mechanism is worth reasoning through, because it is not simple error. The
model has learned an association between "old document" and "archaic
orthography." Presented with an image it recognizes as historical, it produces
output matching its statistical expectation of what historical text looks like —
which may be more archaic than the actual document. The model is not misreading the
ink; it is reading its own expectation of the period.

The measured consequences:

| Model, full-page mode | Overall CER | Archaic insertions | Over-historicization prevalence |
| --- | --- | --- | --- |
| Fine-tuned TrOCR | 1.83% | None | 0% |
| Gemini 2.5 Pro | 3.36% | Minimal | Low |
| Claude 3.5 Sonnet | 6.79% | Moderate | Medium |
| GPT-4o | 9.23% | High | 59% of processed files |
| Transkribus PyLaia | 26.93% | None | 0% |

Note the fourth row against the fifth. GPT-4o achieved a far better CER than the
generic PyLaia baseline — 9.23% against 26.93% — while inserting anachronistic
characters in 59% of processed files. PyLaia performed worse by the metric and
never once fabricated an archaic grapheme (Levchenko, 2024).

**The takeaway for this page:** GPT-4o beat a generic HTR baseline on CER while
inventing anachronistic characters in 59% of files — the metric and the fidelity
diverge.

---

## **05 Content**

**Why CER Is Insufficient for Historical Text**

The table in the previous section makes a methodological point that Week 5 will
build on directly.

Character error rate treats all differences equally. A model that inserts an
archaic omega where the document has a plain o has made one substitution, counted
identically to any other substitution. But that substitution is a different *kind*
of error: it is not a misreading of ink, it is a fabrication of period-specific
orthography, and it corrupts precisely the evidence a diplomatic transcription
exists to preserve.

The finding is explicit: standard metrics like CER are insufficient for evaluating
historical texts, because a model may achieve a low CER while destroying the
diplomatic fidelity of the transcription through temporal hallucination
(Levchenko, 2024).

Two supplementary metrics have been proposed:

| Metric | Measures | Detects |
| --- | --- | --- |
| Historical Character Preservation Rate (HCPR) | Proportion of period-specific characters correctly preserved | Silent modernization |
| Archaic Insertion Rate (AIR) | Frequency of hallucinated characters from earlier epochs | Over-historicization |

HCPR isolates a system's tendency to silently modernize historical text; AIR tracks
the opposite failure, hallucinating archaism (Levchenko, 2024). A model can score
well on CER while failing badly on either.

For your Greek manuscript, the analogous questions are concrete. Does the model
preserve the polytonic diacritics as written, or supply what it expects? Does it
preserve *scriptio continua*, or impose modern word division? Does it preserve
abbreviations, or expand them? Does it preserve scribal errors, or correct them?

Each of those is a modernization that a low CER would not reveal. Plan to check
them specifically today.

**The takeaway for this page:** A model can score well on CER while silently
modernizing or hallucinating archaism — check preservation and insertion
separately.

---

## **06 Content**

**Structural and Formatting Failures**

A third category of VLM failure, distinct from both misreading and hallucination,
and the one most likely to affect you today.

General-purpose models suffer from prompt saturation and formatting
hallucinations. They may read the underlying text correctly and yet fail to adhere
to the strict line-break preservation and structural encoding a diplomatic
transcription requires. They are also prone to injecting external contextual
metadata, conversational filler, or unprompted historical summaries directly into
the transcription block (AlKendi et al., 2024).

| Failure | What it looks like | Consequence |
| --- | --- | --- |
| Line breaks not preserved | Text reflowed as continuous prose | Cannot align to zones; unusable for training |
| Conversational framing | "Here is the transcription of this manuscript:" | Must be stripped before measurement |
| Unprompted commentary | Historical notes interleaved with text | Corrupts the transcription |
| Modernized punctuation | Modern marks substituted for scribal ones | Silent normalization |
| Abbreviations expanded | Nomina sacra written in full | Diplomatic fidelity lost |
| Word division imposed | Spaces inserted into *scriptio continua* | Unrecorded editorial intervention |
| Silent gap filling | Damaged text confidently supplied | Invention presented as reading |

The first row is the practically serious one. Wednesday's model produces
line-aligned output because it operates on line images; today's model sees a full
page and produces a block of text. Without preserved line breaks that output cannot
be aligned to your zones, cannot be used for training, and cannot be compared
line by line against your ground truth.

The last row is the scholarly serious one. A model asked to transcribe a damaged
passage will frequently supply plausible text for the damaged region without
indicating that it has done so — presenting invention as reading, in exactly the
place where a `<gap/>` or `<unclear>` belongs.

Both are things you must check for explicitly, because neither announces itself.

**The takeaway for this page:** VLMs reflow lines, add commentary, and fill gaps
confidently — none of which announces itself in the output.

---

## **07 Content**

**Designing the Experiment**

Run this as a measurement, not a demonstration. The design determines whether the
results mean anything.

Controls to hold fixed:

- **The same passage.** Use exactly the lines you transcribed manually and ran through your HTR model. Comparison across different material is not comparison.
- **The same images.** The same folios, at the same resolution, from the same source.
- **Raw output preserved.** Capture the model's output before any correction, exactly as returned.
- **The prompt recorded.** Verbatim, including any system instruction.
- **The model and version recorded.** Model behaviour changes between versions.
- **The date recorded.** Hosted models change without notice.
- **One variable at a time.** If you test several prompts, change one thing between them.

The fourth and sixth items are what make this reproducible, and they are the ones
students skip. A result reported as "the LLM produced 34% CER" is not reproducible
without the prompt and the model version, because a different prompt or a silently
updated model produces a different number.

Record your experimental design in `logs/vlm-method-w4.md` before you begin. Then
run it, and record what actually happened, including anything you changed
mid-experiment and why.

Treat unexpected results as findings rather than as mistakes. If the model performs
far better than the literature predicts, that is worth investigating and reporting —
but check first whether your passage is from a text so well known that the model
may be reproducing it from memory rather than reading it. Section 12 addresses that
possibility.

**The takeaway for this page:** Record the prompt verbatim, the model version, and
the date — without them the result is not reproducible.

---

## **08 Content**

**Prompting for Diplomatic Transcription**

The prompt matters, and a naive prompt guarantees the failures in section 06.

A poor prompt: *"Transcribe this manuscript."* This invites conversational framing,
reflowed text, expanded abbreviations, modernized orthography, and confident gap
filling — every failure mode at once.

A better prompt states the constraints explicitly:

```text
Transcribe the Greek text in this manuscript image.

Requirements:
- Preserve line breaks exactly as in the manuscript. One output line
  per manuscript line.
- Transcribe diplomatically: preserve the orthography as written,
  including apparent errors. Do not correct or modernize.
- Do not expand abbreviations. Transcribe the abbreviated form as
  written.
- Preserve all polytonic diacritics exactly as written.
- Preserve word division exactly as in the manuscript. If the text is
  written without word division, do not insert spaces.
- Where text is illegible or damaged, output [ILLEGIBLE] rather than
  supplying a reading.
- Where you are uncertain, output the reading followed by [?].
- Output only the transcription. No preamble, commentary, or summary.
```

Each line addresses a documented failure mode. Do not omit any of them on the
grounds that the model probably will not make that mistake.

Two notes. Instructing the model to mark uncertainty gives you a self-report, which
is useful data and is *not* reliable — models are poorly calibrated about their own
uncertainty, and section 11 returns to this. And even a well-designed prompt will
not eliminate these failures; it reduces them. Check the output against every
requirement regardless.

Record the exact prompt in your log.

**The takeaway for this page:** Every constraint in the prompt addresses a
documented failure mode, and a good prompt reduces those failures without
eliminating them.

---

## **09 Content**

**Running the Transcription**

Execute the experiment.

- Select the same folio you transcribed manually.
- Supply the image at the highest resolution the interface accepts.
- Use the prompt from section 08, verbatim.
- Capture the complete raw output, unedited.
- Save it to a file before doing anything else.
- Commit it immediately, with provenance trailers, before correcting anything.

That last step is the discipline from Wednesday's section 21, and it matters
equally here. Raw output must be committed unmodified, because it is what gets
scored in Week 5. Correcting before committing destroys the measurement.

```text
feat(transcription): VLM transcription of f. 42r, uncorrected

Zero-shot transcription via [model, version], accessed 2026-09-25.
Prompt recorded verbatim in logs/vlm-method-w4.md. Raw output, no
corrections and no reformatting applied.

AI-Generated: true
Model: [model name and version]
Prompt-Ref: logs/vlm-method-w4.md
Human-Verified: false
Ground-Truth-Commit: a3f9c21
```

If you test more than one model or more than one prompt, commit each result
separately with its own trailers. Mixing several runs in one file makes the
comparison impossible to reconstruct.

Resist the urge to iterate on the prompt until the output looks good. That
converges on a prompt tuned to this passage, which is not what you are measuring
and which will not generalize. Run the designed experiment; note separately any
additional prompts you tried and what changed.

**The takeaway for this page:** Commit the raw output before correcting or
reformatting anything — that state is what Week 5 measures.

---

## **10 Content**

**Reading the Output Critically**

Now assess. Work through categories rather than reading impressionistically,
because impressions here are unreliable — fluent output feels accurate.

Check, in this order:

| Check | Question | Why first |
| --- | --- | --- |
| Line count | Does the output have the same number of lines as the manuscript? | Determines whether comparison is possible |
| Framing | Is there preamble, commentary, or summary? | Must be stripped before measurement |
| Diacritics | Are polytonic marks present and correct? | The most likely silent loss |
| Abbreviations | Preserved as written, or expanded? | Silent normalization |
| Word division | As in the manuscript, or imposed? | Unrecorded intervention |
| Damaged regions | Marked, or confidently filled? | Invention presented as reading |
| Orthography | Preserved, including apparent errors? | Silent correction |
| Plausible wrong words | Does the text match the ink? | Requires image comparison |

The last row cannot be checked by reading the output. Fluent text reads as correct,
and the errors that matter most are the ones that read perfectly. You must compare
against the image, line by line, at full zoom — the same discipline as Tuesday.

The sixth row deserves specific attention. Find the damaged region you identified
in Lesson 3.2's exercise and look at what the model produced there. If it supplied
confident text where you recorded a `<gap/>`, you have a documented instance of
hallucination on your own manuscript, which is worth far more in your Week 5 report
than any published benchmark.

Categorize every error. Counts by category are what Week 5's comparison needs.

**The takeaway for this page:** Fluent output reads as correct, so check against
the image — and look specifically at where you recorded damage.

---

## **11 Content**

**Self-Reported Uncertainty Is Unreliable**

You asked the model to mark uncertainty. Assess whether it did so usefully.

Language models are poorly calibrated about their own uncertainty. A model's
expressed confidence does not reliably track its accuracy: it will mark uncertainty
on readings that are correct and produce confident output on readings that are
fabricated. The `[?]` markers are data about the model's behaviour, not a reliable
guide to which readings to check.

Test this directly on your own output. Take the readings the model marked uncertain
and the readings it produced confidently, and check both against the image.

| What you find | What it means |
| --- | --- |
| Marked-uncertain readings are mostly wrong; confident ones mostly right | The model is reasonably calibrated here |
| Uncertainty markers appear unrelated to accuracy | Self-report is not usable as a guide |
| Confident output in a damaged region | Hallucination; the most serious finding |
| No uncertainty markers at all despite damage | The model does not represent its own limits |

The third and fourth rows are the ones to look for specifically, and either is a
substantial finding for your report. A model that produces confident readings in a
region you know to be illegible has demonstrated, on your manuscript, that its
output cannot be trusted where you most need help.

This has a direct methodological consequence. If the model's uncertainty markers do
not correlate with its errors, then there is no way to identify which parts of the
output need checking short of checking all of it — which means the tool provides no
reduction in verification labour, whatever it does for transcription labour.

Record what you find. It bears directly on whether this method is usable for your
manuscript.

**The takeaway for this page:** If the model's uncertainty markers do not track its
errors, you must check everything — and the tool saves no verification labour at
all.

---

## **12 Content**

**Memorization Versus Reading**

A control that matters if your passage is from a well-known text, and one that
students almost never think to run.

A vision-language model trained on internet-scale data has very likely encountered
the text of your manuscript — not the manuscript images, but the text, in printed
editions, digital corpora, and scholarly discussion. A model asked to transcribe a
famous passage may produce the *edited* text from memory rather than reading the
ink.

This would produce excellent-looking output that is scholarly worthless, because
the model would reproduce a modern critical edition rather than your witness — and
the differences between them are precisely the variant readings your edition
exists to record.

Two tests distinguish memorization from reading:

**The variant test.** If your manuscript has a reading that differs from the
standard printed text, look at what the model produced there. A model reading the
ink produces the manuscript's reading; a model reciting from memory produces the
standard text. This is the strongest available test, and it is why you should have
identified your passage's known variants in advance.

**The damage test.** Look at what the model produced in regions you recorded as
illegible. A model reading the ink cannot read what is not there; a model reciting
from memory fills the gap fluently and correctly, which is more damning than
filling it incorrectly.

| Observation | Interpretation |
| --- | --- |
| Manuscript's variant reading reproduced | Reading the image |
| Standard edition's reading where the manuscript differs | Reciting from memory |
| Illegible region left marked | Reading the image |
| Illegible region filled with the standard text | Reciting from memory |
| Illegible region filled with plausible invention | Hallucinating |

Run both tests and report the result. For a well-known text this is the single most
important check you make today.

**The takeaway for this page:** Where your manuscript differs from the printed
text, a model reciting from memory gives the printed reading — that is the test.

---

## **13 Content**

**Computing a Preliminary Error Rate**

Full measurement is Week 5's work, but a rough figure today gives you something to
compare.

Character error rate is the Levenshtein distance between machine output and ground
truth, normalized by the ground truth's length (AlKendi et al., 2024):

```python
def cer(reference: str, hypothesis: str) -> float:
    """Character error rate: edit distance / reference length."""
    import unicodedata
    r = unicodedata.normalize("NFC", reference)
    h = unicodedata.normalize("NFC", hypothesis)
    # Levenshtein distance
    prev = list(range(len(h) + 1))
    for i, rc in enumerate(r, 1):
        cur = [i]
        for j, hc in enumerate(h, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1,
                           prev[j - 1] + (rc != hc)))
        prev = cur
    return prev[-1] / len(r) if r else 0.0
```

Note the normalization on both inputs. This is Lesson 1.2 section 10 arriving in
practice: comparing NFC ground truth against NFD model output produces an error
rate reflecting encoding difference rather than transcription difference, and the
inflation can be severe. Normalize both, always.

Two further cautions on today's number. Strip conversational framing before
comparing, or you will measure the preamble as error. And if line breaks were not
preserved, a whole-text comparison is the only option available, and the resulting
figure is not comparable to a line-aligned measurement.

Compute the same figure for Wednesday's HTR output against the same ground truth,
so you have a like-for-like comparison. Record both, with the caveats.

**The takeaway for this page:** Normalize both strings to NFC before computing CER,
or you measure encoding difference rather than transcription difference.

---

## **14 Content**

**Where LLMs Are Genuinely Useful**

Balance is owed. The evidence is against zero-shot VLM transcription of historical
manuscripts; it is not against these tools generally, and dismissing them wholesale
would be as unexamined as adopting them wholesale.

| Task | Suitability | Reason |
| --- | --- | --- |
| Zero-shot diplomatic transcription of historical MSS | Poor | Specialization gap; hallucination; over-historicization |
| Transcription of modern handwriting | Good | Well represented in training data |
| Transcription of printed text in common languages | Good | Very well represented |
| Translating an established transcription | Good | A language task, not a reading task |
| Explaining an abbreviation or a palaeographic feature | Useful | Retrieval of documented knowledge |
| Suggesting parallels for a phrase | Useful, with verification | Broad textual coverage |
| Drafting code for your pipeline | Good | Well-supported task |
| Post-correcting OCR output | Counter-productive | Documented to degrade quality |

The guidance is specific: unless the manuscript is a late nineteenth- or
twentieth-century document in a well-represented language, do not rely on zero-shot
VLMs for diplomatic transcription. The risk of archaic insertion, silent
modernization, and structural hallucination outweighs the setup time saved
(AlKendi et al., 2024).

The last row is Wednesday's complexity paradox. Adding LLM-based post-OCR
correction degrades aggregate quality through prompt saturation and cascading error
propagation (Mattingly et al., 2024). The correction has no access to the image and
corrects toward linguistic plausibility — which reliably damages exactly the
unusual readings that matter.

The distinction running through the table: these tools are good at tasks where
linguistic knowledge is the point, and bad at tasks where linguistic knowledge
contaminates the evidence. Transcription is the second kind.

**The takeaway for this page:** These tools help where linguistic knowledge is the
point and harm where it contaminates evidence — transcription is the second kind.

---

## **15 Content**

**The Human-in-the-Loop Position**

Where this leaves the method, stated as a working position rather than a
prohibition.

HTR and VLMs do not replace the palaeographer; they shift the palaeographer's
labour from initial decipherment toward validation and semantic enrichment
(AlKendi et al., 2024). That reallocation is real and valuable — but it holds only
where the automated output is good enough that validating it costs less than
transcribing.

The threshold from Wednesday applies: above roughly 15% CER, post-correction costs
more than transcribing from scratch (AlKendi et al., 2024). A tool above that
threshold is not a labour saving with quality costs; it is a labour *increase*.

Today's likely finding is that a general VLM sits above that threshold on your
manuscript while your fine-tuned HTR model sits below it. If so, the conclusion is
not that AI is useless but that *the specialized tool is the right one for this
task*, and that conclusion is now supported by your own measurement rather than by
assertion.

The three-step cycle is designed to produce exactly this kind of grounded judgement.
You have now seen what human reading, a bounded specialized model, and an unbounded
general model each produce on the same lines. That comparison is the basis for
choosing tools deliberately for the rest of the term — and for defending the choice
in your Week 12 commentary.

**The takeaway for this page:** Automation saves labour only below the threshold
where correction costs less than transcription — and you have now measured where
your tools sit.

---

## **16 Content**

**Documenting AI Use in the Repository**

Provenance discipline, applied to today's work specifically. The syllabus requires
disclosure of AI use, and the repository is where disclosure lives.

Every commit containing machine-generated content carries trailers recording the
model, the prompt, and the verification status. For today:

```text
AI-Generated: true
Model: [name and version]
Model-Access-Date: 2026-09-25
Prompt-Ref: logs/vlm-method-w4.md
Human-Verified: false
Ground-Truth-Commit: a3f9c21
```

`Model-Access-Date` matters more for hosted models than for local ones. A hosted
model can change without notice and without a version number changing, so the date
is often the only record of which system actually produced the output. A result
reported without it may not be reproducible even by the same person a month later.

The audit queries from Lesson 1.1 section 25 now return meaningful results:

| Question | Command |
| --- | --- |
| What in my edition is machine-generated? | `git log --grep="AI-Generated: true"` |
| What remains unverified? | `git log --grep="Human-Verified: false"` |
| Which models did I use? | `git log --pretty=format:"%(trailers:key=Model)"` |
| How much is machine-assisted? | `git rev-list --all --grep="AI-Generated: true" --count` |

Run the second one now. It should list Wednesday's raw HTR output and today's raw
VLM output — the two states in your repository that a machine wrote and you have
not verified. That is an accurate picture of your edition's current condition, and
it is exactly the kind of statement a reader of a digital edition should be able to
obtain.

**The takeaway for this page:** Record the model access date — a hosted model can
change without notice, making the date the only record of what produced the output.

---

## **17 Content**

**Assembling the Three-Way Comparison**

Bring the three transcriptions together. This is the week's actual product.

Build a comparison document — `logs/three-way-w4.md` — with a table per line:

| Line | Manual (ground truth) | HTR output | VLM output | Notes |
| --- | --- | --- | --- | --- |
| 1 | ἐν ἀρχῇ ἦν ὁ λόγος | ἐν ἀρχῇ ἦν ὁ λόγος | ἐν ἀρχῇ ἦν ὁ λόγος | All agree |
| 2 | θν καὶ θς | θν καὶ θς | θεόν καὶ θεός | VLM expanded abbreviations |
| 3 | ἦν ὁ λόγος οὗτος | ἦν ὁ λογος οὑτος | ἦν ὁ λόγος οὗτος | HTR dropped diacritics |
| 4 | [gap, 6 chars] | [nonsense sequence] | διʼ αὐτοῦ πάντα | VLM filled the gap |

That fourth row is the finding. Where the manuscript is damaged, your transcription
records a measured gap, the HTR model produces something visibly wrong, and the VLM
produces fluent plausible Greek that is not on the parchment. Three systems, three
characteristic behaviours, one line.

Generating the comparison is easier with a diff:

```bash
git diff gt-f42r:edition/edition.xml htr-w4-raw:edition/htr-output.txt
```

This is where the tags from Tuesday and Wednesday earn their keep, and where the
`diff.algorithm histogram` setting from Lesson 1.1 section 21 makes the output
readable.

Complete the comparison for at least ten lines, including every line where you
recorded uncertainty or damage. Those lines are the informative ones — agreement on
easy lines tells you little, and divergence on hard lines tells you what each
system does when the evidence runs out.

**The takeaway for this page:** Compare on the lines where you recorded uncertainty
— agreement on easy lines is uninformative, and divergence on hard lines is the
finding.

---

## **18 Content**

**Error Taxonomy Across the Three**

Categorize what you found, because the categories are what your Week 5 report
argues from.

| Error category | Manual | Specialized HTR | Vision-language model |
| --- | --- | --- | --- |
| Misread letterform | Occasional | Common | Common |
| Dropped diacritics | Rare | Common, often layout-caused | Variable |
| Expanded abbreviations | Never, if diplomatic | Rare | Common |
| Modernized orthography | Never, if diplomatic | Rare | Common |
| Impossible letter sequences | Never | Occasional | Rare |
| Plausible wrong words | Rare | Rare | Common |
| Fabricated text in damaged regions | Never | Never | Documented |
| Line breaks lost | Never | Never | Common |
| Commentary injected | Never | Never | Common |
| Reading rather than seeing | Occasional | Never | By construction |

Read the last four rows down. The bottom four failure categories are essentially
exclusive to the vision-language model, and none of them is a *recognition* error —
they are consequences of the system being a language model applied to a reading
task. It reformats because it produces prose; it comments because it converses; it
fabricates because it completes.

Read the last row across. Your own characteristic failure — reading what you expect
rather than what is written, from Lesson 4.1 section 10 — is one the HTR model
structurally cannot make, because it has no expectations to impose. The VLM makes
it by construction, since imposing linguistic expectation is what it does.

That is a genuinely useful symmetry. The specialized model is a check on your
expectation-driven errors, and you are a check on its ink-level errors. The two
complement each other, which is what human-in-the-loop actually means in practice.

**The takeaway for this page:** The VLM's distinctive failures are not recognition
errors but consequences of being a language model — and the HTR model cannot make
your expectation-driven errors.

---

## **19 Content**

**Reporting Negative Results**

If today produced poor VLM output, that is a result and should be reported as one.

There is a tendency in coursework to treat a failed technique as a failed
assignment, and to report only what worked. This is the opposite of what is wanted.
A documented negative result — this model, this prompt, this manuscript, this error
rate — is a genuine contribution, and it is what lets a future scholar avoid
repeating the attempt.

Report:

- The model and version, and the date accessed.
- The exact prompt.
- The raw output, committed unmodified.
- The measured error rate, with its caveats.
- The error categories, with counts.
- What specifically failed: diacritics, abbreviations, line breaks, damaged regions.
- Whether memorization was tested for, and what was found.
- Your assessment of whether the method is usable for this manuscript.

That last item is the scholarly judgement. It is not "the model was bad" but
something like: *for this hand, in this script, at this resolution, zero-shot VLM
transcription produced a CER of X with systematic expansion of abbreviations and
fabricated text in damaged regions, and is therefore unsuitable as a primary
transcription method for this edition; it may remain useful for [specific task].*

That statement is defensible, specific, and useful. It is also exactly the kind of
claim the Week 5 reconciliation report asks for.

**The takeaway for this page:** A documented failure — this model, this prompt,
this manuscript, this rate — is a contribution, and vague dismissal is not.

---

## **20 Content**

**Remote Session Practicalities**

Today is remote, and a few things are worth verifying rather than assuming.

- Your repository is pushed and your local clone is current.
- Your manifest is reachable from your current network.
- Your polytonic input method works on this machine.
- Your XML editor validates against the TEI schema here.
- Python and your normalization tooling run here.
- Your pre-commit hook is installed in this clone.

The last item is the one that catches people. Hooks live in `.git/hooks/` and are
**not cloned**, as Lesson 1.1 section 23 established. If you are working from a
fresh clone today, your NFC normalization hook does not exist here, and every
commit you make will bypass it.

Install it now, from your tracked `tools/` directory, before committing anything:

```bash
cp tools/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

Then test it: create a file with decomposed Greek, stage it, commit, and confirm
the committed bytes are NFC. An untested hook on a new machine is not a control.

Push before you finish. Today's work must be available on whatever machine you use
next week, and a remote session's output left on a laptop is a common way to lose a
session's work.

**The takeaway for this page:** Hooks are not cloned — install and test your NFC
hook on this machine before committing anything today.

---

## **21 Content**

**What Wednesday and Friday Together Established**

Consolidate the week's empirical findings, since they are what Week 5 argues from.

| Finding | Evidence |
| --- | --- |
| Transfer learning is decisive | 17.18% CER from scratch versus 3.90% with transfer, same data (Perdiki & Konstantinidou, 2023) |
| Domain match beats scale | TrOCR-Medieval 14.6% versus Mistral-OCR-3 84.7%, same samples (Mattingly et al., 2024) |
| VLMs collapse on historical material | GPT-4o 1.39% modern versus 52.23% historical English (AlKendi et al., 2024) |
| Low CER can hide fidelity loss | GPT-4o 9.23% CER with archaic insertions in 59% of files (Levchenko, 2024) |
| Layout errors cascade into recognition | Truncated polygons remove Greek diacritics entirely (Perdiki & Konstantinidou, 2023) |
| Pipeline complexity degrades quality | Simple OCR-to-translator beats RAG and post-correction variants (Mattingly et al., 2024) |
| Models are brittle to layout change | CMM 5.1% standard versus 13.6% glossed (Geelhaar, 2022) |
| Above 15% CER, correction costs more than transcription | (AlKendi et al., 2024) |

These are not opinions about AI. They are measurements, from published benchmarks,
which you have now partially replicated on your own manuscript.

The unifying claim is the week's thesis: automated transcription substantially
accelerates the workflow *and* fundamentally requires human diplomatic
transcription as an authoritative ground truth, because it is exclusively against
that baseline that error rates, biases, and hallucinated readings can be measured,
evaluated, and mitigated (AlKendi et al., 2024).

Every row in that table is a measurement made against a ground truth someone
produced by hand.

**The takeaway for this page:** Every finding in the table is a measurement against
a hand-produced ground truth — which is the week's thesis in operation.

---

## **22 Content**

**Checklist Before You Finish**

Verify each.

- VLM transcription run on the same folio as Tuesday and Wednesday.
- Prompt recorded verbatim in `logs/vlm-method-w4.md`.
- Model name, version, and access date recorded.
- Raw output committed unmodified, with provenance trailers.
- Output checked against every requirement in section 10.
- Damaged regions specifically examined for fabricated text.
- Memorization tested, if your text is well known.
- Self-reported uncertainty assessed against actual accuracy.
- Preliminary CER computed for both machine outputs, NFC-normalized.
- Three-way comparison table built for at least ten lines.
- Errors categorized by type, with counts.
- Time invested recorded for each of the three methods.
- Everything committed and pushed.

The seventh item applies only to well-known texts but is the most important check
available when it does apply. A model reproducing a printed edition from memory
produces excellent-looking output that is worthless as a witness transcription, and
nothing else in this checklist would detect it.

**The takeaway for this page:** For a well-known text, the memorization test is the
most important check available — nothing else detects a recited printed edition.

---

## **23 Content**

**Looking Ahead to Week 5**

Next week reconciles and measures, and it is a two-step week by design — Wednesday
September 30 is closed for Truth and Reconciliation, and the schedule notes that
reconciliation is itself the comparison, so the missing meeting costs nothing.

| Meeting | Step | Activity |
| --- | --- | --- |
| Tue Sep 29 (#12) | Manual | Double-keying; building a consensus text by hand |
| Fri Oct 2 (#13) | Measurement | CER and WER for the HTR and AI passes against your ground truth |

Tuesday's double-keying addresses the problem raised in Lesson 4.1 section 15: your
ground truth contains errors, and treating it as perfect makes every measurement
against it partly wrong. Transcribing independently a second time and adjudicating
the differences produces a substantially more accurate reference.

Friday computes the measurements properly — line-aligned, normalized, categorized,
with the qualitative assessment that section 05 argued CER alone cannot supply.

**The Transcription Assignment is due Friday October 2**, and it includes the
reconciliation report. Everything you have recorded this week — methodology,
comparisons, error categories, timings — is material for it. Students who kept
those records assemble the report; students who did not, redo the work.

**The takeaway for this page:** Week 5 double-keys the ground truth and then
measures against it — and the Transcription Assignment on October 2 includes the
reconciliation report.

---

## **24 Content**

**What Good Work Looks Like Here**

The standard for today.

A minimally acceptable result is a VLM transcription, committed, with a computed
error rate.

Good work additionally:

- Uses a prompt designed against documented failure modes, recorded verbatim.
- Preserves the raw output unmodified before any assessment.
- Checks the output against every category in section 10, not impressionistically.
- Examines damaged regions specifically for fabrication.
- Tests for memorization where the text is well known.
- Assesses self-reported uncertainty against actual accuracy.
- Normalizes both strings before computing any error rate.
- Reports cost alongside quality for all three methods.
- Draws a specific, defensible conclusion about applicability to *this* manuscript.
- Reports negative results fully.

The ninth item is what the whole week is for. A conclusion of the form "AI is
unreliable for manuscripts" is a repetition of what you were told. A conclusion of
the form "for this tenth-century Greek minuscule at this resolution, model X
produced a CER of Y with systematic abbreviation expansion and fabricated text in
two damaged regions, against my fine-tuned model's Z" is a finding you established.

The difference between them is the difference between having read about the
specialization gap and having measured it.

**The takeaway for this page:** A specific measured conclusion about *your*
manuscript is the deliverable; a general claim about AI is a repetition of what you
were told.

---

## **25 Content**

**A Note on Tool Choice for the Rest of the Term**

Today's results should inform how you work from Week 6 onward, and it is worth
being explicit about how.

If your fine-tuned HTR model performs well — under about 10% CER — use it to extend
your transcription across the remaining folios, correcting its output against the
images and committing raw and corrected states separately. That is the
human-in-the-loop workflow operating as intended.

If it performs poorly, diagnose before abandoning it. The order from Wednesday's
section 14 applies: layout, alignment, training volume, base model. Most poor first
models are fixable, and the commonest fix is more or better-sampled ground truth.

For the VLM, the honest position based on today is likely that it is unsuitable for
primary transcription of your manuscript, and that it remains useful for other
tasks — explaining palaeographic features, drafting pipeline code, suggesting
parallels for verification, translating an established transcription.

What you should not do, from Wednesday's section 24, is pass your HTR output
through an LLM for correction. That configuration is documented to degrade quality
(Mattingly et al., 2024), and it will damage precisely the unusual readings your
edition exists to record.

Record your tool decisions and your reasons. Week 12's commentary will need to state
what methods produced the text, and a decision recorded at the time is worth more
than one reconstructed in December.

**The takeaway for this page:** Let today's measurement set your tool choices for
the term, and record the reasons at the time rather than reconstructing them later.

---

## **26 Content**

**The Broader Methodological Point**

Step back from transcription, because the pattern generalizes and will recur every
week for the rest of the term.

Each week runs the same operation three ways: by hand, with a specialized
deterministic tool, and with AI assistance. That structure is not about
transcription specifically. It is a general method for evaluating computational
tools in a scholarly context, and its logic is the same each time.

The manual step establishes a reference and, equally, establishes *your*
understanding of the material. The deterministic step shows what a bounded,
domain-specific tool produces — fast, consistent, limited to what it was built for.
The AI step shows what an unbounded general tool produces — faster, more flexible,
and capable of failure modes the other two structurally cannot exhibit.

The comparison yields something none of the three yields alone: a measured account
of what each tool is good for on *this* material, which is the only basis on which
tools should be chosen.

Notice that this method requires the manual step to come first and to be done
properly. Every measurement is a distance from the reference, and a compromised
reference compromises everything computed from it. That is why Tuesday is not a
warm-up.

**The takeaway for this page:** The three-step cycle is a general method for
evaluating tools against material, and it collapses if the manual reference is
compromised.

---

## **27 Content**

**Honest Assessment of Cost**

One more comparison, because quality without cost is half an argument.

| Method | Setup | Per-folio cost after setup | Quality on your manuscript |
| --- | --- | --- | --- |
| Manual transcription | None | Highest | Reference |
| Fine-tuned HTR | A session: layout, alignment, training | Low, plus correction | Record your figure |
| Zero-shot VLM | Minutes | Very low, plus correction | Record your figure |

Fill in the right-hand column from today's measurements, and the middle column
from your own timings.

The comparison is genuinely three-dimensional and resists a simple ranking. Manual
transcription has no setup cost and the highest marginal cost. HTR has a
substantial setup cost and a low marginal cost, which means it pays off across many
folios and does not pay off across four. The VLM has almost no cost of either kind
and, on historical material, quality that may make its output not worth correcting.

The threshold governs: above roughly 15% CER, correction costs more than
transcription, and a tool's low cost per folio is irrelevant if its output must be
discarded (AlKendi et al., 2024).

For a passage of twenty to forty lines — your edition — the honest calculation may
well be that manual transcription is competitive with HTR, because the setup cost
never amortizes. Say so if you find it. The exercise's value is in having measured
the trade-off on real material, not in reaching a predetermined conclusion about
which tool wins.

**The takeaway for this page:** For a short passage, HTR's setup cost may never
amortize — say so if you find it, because the measurement is the point.

---

## **28 Content**

**Committing and Pushing**

Close out the week properly.

Everything committed today should carry complete provenance. Verify with the audit
queries:

```bash
git log --grep="AI-Generated: true" --oneline
git log --grep="Human-Verified: false" --oneline
```

The second query lists what a machine wrote and you have not verified. If you have
corrected today's output, commit the corrections separately and the corrected state
should carry `Human-Verified: true`.

Tag today's raw output:

```bash
git tag -a vlm-w4-raw -m "Raw VLM output, [model/version], before correction"
git push --tags
```

Push everything, including tags. Tags are not pushed by default, and the three
tagged states from this week — `gt-f42r`, `htr-w4-raw`, `vlm-w4-raw` — are what
Week 5's measurement retrieves. A tag existing only locally is a tag that Week 5
cannot use if you work from another machine.

Verify the push succeeded and the tags are present on the remote before you finish.
A remote session that ends with unpushed work is a session that may need to be
repeated.

**The takeaway for this page:** Push tags explicitly — they are not pushed by
default, and Week 5's measurement retrieves the tagged states.

---

## **29 Content**

**Consolidating the Week**

What Topic 4 established, across three meetings.

Tuesday: diplomatic transcription preserves what the manuscript shows, including
abbreviations, uncertainty, corrections, and damage; it is produced by hand, at
full zoom, by someone reading rather than expecting; and it serves as training
data, comparison reference, verification object, and measurement baseline
simultaneously.

Wednesday: layout analysis precedes recognition and its errors cascade; polygons
must enclose Greek diacritics or the model never sees them; transfer learning from
a matched base model is decisive; and a specialized model's bounded competence
makes it fail conspicuously rather than fluently.

Friday: general vision-language models collapse on historical material despite
excelling on modern; they exhibit failure modes specialized models do not —
over-historicization, fluent fabrication, structural reformatting; and low CER can
coexist with the destruction of diplomatic fidelity.

The connecting thesis: automation accelerates the work and requires a
hand-produced diplomatic ground truth, because that is the only thing against which
its errors can be measured (AlKendi et al., 2024).

Week 5 takes that ground truth, improves it by double-keying, and performs the
measurement properly.

**The takeaway for this page:** Three meetings, one thesis — automation accelerates
transcription and depends absolutely on a hand-produced reference to be evaluated
at all.

---

## **30 Content**

**Synthesis: Fluency Is Not Fidelity**

The finding worth carrying out of this week.

A vision-language model applied to a historical manuscript produces fluent text.
It reads well. Its Greek is grammatical, its vocabulary is plausible, its sentences
complete properly. And on historical material it may be wrong at rates approaching
80% character error, may insert orthography from centuries earlier than the
document, and may supply confident readings for parchment that carries no legible
ink (AlKendi et al., 2024; Levchenko, 2024).

Fluency and fidelity are independent properties, and the systems that maximize the
first are not the systems that maximize the second. This is the week's central
lesson, and it generalizes well beyond transcription: the more a tool can produce
plausible output, the less its plausibility tells you about its accuracy, and the
more you must verify against the source.

This is why the specialized model's conspicuous failures are a virtue. Output that
announces its own uncertainty by being obviously wrong is safer than output that
conceals uncertainty by being fluent. A CTC model producing an impossible letter
sequence has told you something true about the ink; a language model producing a
perfect word has told you something about its expectations.

And it is why the manual step is irreducible. Only a person who has read the
parchment can tell the difference — and having read it, they hold the reference
against which everything else is measured.

**Due Friday October 2.** The Transcription Assignment, including the
reconciliation report, at the end of Week 5.

**For Tuesday.** Week 5 begins with double-keying: transcribe your folio again,
independently, without consulting Tuesday's version. Do not review it beforehand.
The independence is what makes the comparison informative.

**The takeaway for this page:** Fluency and fidelity are independent, and the more
plausible a tool's output, the less its plausibility tells you about its accuracy.

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

Colavizza, G., Ehrmann, M., & Bunout, E. (2022). Benchmarking large language
models for handwritten text recognition. *Journal of Documentation*.

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

Puigcerver, J. (2017). *PyLaia: A deep learning toolkit for handwritten document
analysis*. https://github.com/jpuigcerver/PyLaia

Romein, C. A., et al. (2025). *Assessing advanced handwritten text recognition
engines for digitizing historical documents*.

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/
