# Lesson 6.3 — AI-Assisted Normalization and the Risk of Over-Normalization

*RELS 398 / ENGL 398 · Topic 6: Normalization · Meeting #16 (Fri Oct 9)*

***Step 3 of the three-step cycle: AI-assisted.** Today you apply neural and
generative methods to the same normalization task and check their output against
your rule baseline. The specific danger being tested is over-normalization —
regularization that crosses silently into semantic alteration.*

---

## **01 Content**

**Today's Question**

You have normalized the same text twice: by hand on Tuesday, establishing a policy,
and by rule on Wednesday, implementing it. Today a third method attempts the same
task with capabilities the first two lack.

The question is not whether the AI method is more accurate. It is whether the
additional capability it brings — contextual disambiguation, generalization to unseen
variation — is worth the fidelity and accountability it costs.

That framing matters because normalization differs from transcription in a way
Lesson 6.2 section 29 established. Transcription has a fact of the matter: the ink
is what it is. Normalization is governed by a stated policy, which means "accuracy"
means consistency with a chosen standard rather than correspondence to a document.
A model that normalizes differently from you is not necessarily wrong; it may be
applying a different policy, and the interesting question is whether it is applying
*any* consistent policy at all.

The documented risk is specific. Generative models prioritize fluency over
diplomatic fidelity, and without strict constraints they over-normalize — altering
valid dialectal syntax or replacing an archaic lexeme with a modern synonym rather
than merely modernizing orthography (Bollmann, 2019).

Your rule baseline is the instrument for detecting exactly that, and today is when
it earns its cost.

**Vocabulary.** *Over-normalization* — regularization exceeding orthography into
morphology, lexis, or syntax. *Contextual disambiguation* — resolving an ambiguous
form using surrounding text.

**The takeaway for this page:** The question is whether contextual capability is
worth the fidelity and accountability it costs — not simply which method is more
accurate.

---

## **02 Content**

**Neural Normalization: The Sequence-to-Sequence Approach**

Before generative models, the established neural approach framed normalization as
translation — specifically character-based statistical and then neural machine
translation (Bollmann, 2019).

The architecture: a **bidirectional LSTM** encoder-decoder reads the input character
sequence in both directions, so that each position is interpreted with both left and
right context available. Basing the model on individual characters keeps the
vocabulary small, which reduces model complexity and the training data required
(Bollmann, 2019).

Framing normalization as translation is a genuinely good fit. Both are
sequence-to-sequence tasks mapping one string to another, with the mapping being
systematic but not fully rule-governed, and with context mattering.

Performance is strong given sufficient data. Across evaluations in English, German,
Hungarian, Icelandic, Spanish, Portuguese, Slovene, and Swedish, neural models
learned complex non-linear mappings between historical and modern orthographies
without hand-crafted lexicons. On the Anselm corpus of Early New High German,
bi-LSTM models reached an average word accuracy of 80.55%, outperforming
conditional random field taggers (Bollmann, 2019).

| Method | Requires | Handles unseen variants | Transparency |
| --- | --- | --- | --- |
| Rule-based | Hand-written rules | Only via distance fallback | Complete |
| Character SMT | Aligned training pairs | Yes, statistically | Limited |
| bi-LSTM seq2seq | Aligned training pairs | Yes, well | Poor |
| Language model | A prompt | Yes | Poor |

The critical constraint for you is the "requires" column. Neural methods need
aligned training pairs, and you have a few hundred from one folio. That is not
enough to train a sequence model from scratch, which is why today's practical work
uses a language model rather than a trained normalizer.

**The takeaway for this page:** Neural normalization is framed as character-level
translation and works well with data — which you do not have at the scale it needs.

---

## **03 Content**

**Data Sparsity and Multi-Task Learning**

The training data problem has a documented mitigation worth knowing, even though
you will not apply it today.

**Multi-task learning** trains a sequence-to-sequence model simultaneously on the
primary normalization task and an auxiliary task — grapheme-to-phoneme mapping, or
normalization of a related dialect. The shared encoder layers learn robust
representations that generalize across both, so the auxiliary data effectively
supplements the sparse primary data (Bollmann, 2019).

The empirical finding is more specific than "it helps," and the specificity matters:
multi-task learning provides significant error reduction **only when the target
dataset is exceptionally small** — around 5,000 tokens. Where abundant target data
exists, it can *degrade* performance through domain mismatch (Bollmann, 2019).

| Target data | Multi-task learning | Reason |
| --- | --- | --- |
| Around 5,000 tokens | Substantial benefit | Auxiliary data supplements sparse signal |
| Moderate | Marginal | Diminishing supplementation |
| Abundant | Can degrade | Domain mismatch dominates |

That is a useful shape to recognize, because it recurs across machine learning
applied to historical material: techniques that help in sparse-data conditions often
hurt in abundant ones, and the applicable regime depends on your corpus rather than
on the technique's general reputation.

For manuscript work the sparse regime is the normal one. A single manuscript, a
single hand, a term project — these are always small-data problems, which is why
Lesson 6.2 section 13's observation matters: rule-based systems reaching 83% accuracy
from 100 tokens are operating in the regime you actually inhabit (Bollmann, 2019).

Note this in your report. "Neural methods outperform rules given sufficient data,
and I do not have sufficient data" is a correct and useful conclusion.

**The takeaway for this page:** Multi-task learning helps only around 5,000 tokens
and degrades with abundant data — manuscript work is always the sparse regime.

---

## **04 Content**

**What Language Models Bring**

Generative models change the picture, because they require no task-specific training
at all.

Large language models excel at zero-shot and few-shot normalization without extensive
fine-tuning. They address the token-context limitation of character-based models: by
attending across an entire paragraph, a model can recognize the syntactic role of an
ambiguous historical spelling and normalize it accordingly (Bollmann, 2019).

That capability is precisely aimed at the limitation Lesson 6.2 section 18 identified
as structural for your script. Your ambiguous set — forms where several rules propose
different standard forms — exists because character-level methods process tokens in
isolation. A model reading the sentence has the information needed.

Two further capabilities are documented:

**Retrieval-augmented generation** grounds normalizations in external domain-specific
knowledge bases — historical lexicons, grammars, aligned translations — which
significantly reduces hallucination rates (Bollmann, 2019).

**Direct TEI output.** Models can be prompted to produce structured TEI natively,
generating `<choice>`, `<orig>`, and `<reg>` in a single pass (Bollmann, 2019).

| Capability | Rule script | Language model |
| --- | --- | --- |
| Syntactic disambiguation | No | Yes |
| Unseen variation | Distance fallback only | Generalizes |
| Domain grounding | The lexicon you supply | RAG, where available |
| TEI generation | You write the projection | Native |
| Character-level alignment | Exact | Unreliable |
| Verifiability | Complete | None |

The bottom two rows are the costs, and the fifth is a practical problem you will meet
today: models struggle with the deterministic projection of character-level
alignments that strict TEI markup requires (Bollmann, 2019). A model may normalize
correctly and mis-align which original corresponds to which regularization.

**The takeaway for this page:** Models bring exactly the contextual capability your
rules structurally lack — and lose exact character alignment and verifiability doing
it.

---

## **05 Content**

**The Over-Normalization Risk**

The central danger, stated precisely, because today's evaluation is designed around
it.

Generative models are probabilistic and prioritize fluency over diplomatic fidelity.
Without strict architectural constraints, a model may over-normalize — altering
valid dialectal syntax, or replacing an archaic lexeme with a modern synonym, rather
than merely modernizing orthography (Bollmann, 2019).

The failure has a characteristic shape. It is not that the model produces nonsense;
it produces *better* text than the manuscript contains. Fluent, standard,
grammatical — and no longer a record of what the scribe wrote.

| Legitimate normalization | Over-normalization |
| --- | --- |
| τιμι → τιμή, a phonetic spelling regularized | A dialectal verb ending changed to the Attic form |
| Supplying an omitted accent | Replacing an archaic word with its modern equivalent |
| Regularizing a homophonic substitution | Adjusting word order to standard syntax |
| Expanding a documented abbreviation | Correcting a genuine variant reading |
| Standardizing a grapheme | Collapsing two distinct dialectal forms into one |

The last row names the most serious case. Processing historical texts with fluid
orthography, models frequently collapse historically significant dialectal variants
into a single standard form, permanently erasing linguistic evidence (Bollmann,
2019).

Why "permanently" is accurate: if the `<orig>` layer is preserved the information
survives, but a model generating both layers may generate an `<orig>` that has
already been partly normalized — in which case the diplomatic layer is not
diplomatic and nothing records the original form.

This is the specific thing to test for today, and section 12 gives the method.

**The takeaway for this page:** Over-normalization produces better text than the
manuscript contains — fluent, standard, and no longer a record of what was written.

---

## **06 Content**

**Designing Today's Experiment**

Run this as a measurement, with the same controls as Lesson 4.3 section 07.

- **Same text.** The diplomatic base from `gt-f42r-consensus`, exactly as Wednesday's script received it.
- **Same tokens.** Every token the script processed, including those it left alone.
- **Raw output preserved.** Captured before any correction.
- **Prompt recorded verbatim.**
- **Model and version recorded**, with the access date.
- **Structured output**, so per-token comparison is possible.

The second item matters and is easy to get wrong. If you supply the model only the
tokens your script flagged, you cannot measure over-application — the model never
sees the tokens it might wrongly normalize. Supply the whole text.

Three specific test sets to track through the session:

| Test set | Source | What it tests |
| --- | --- | --- |
| Ambiguous cases | Lesson 6.2 | Does context resolve what rules cannot? |
| Tokens deliberately left alone | Lesson 6.1 | Over-application |
| Proper names | Lesson 6.1 | Respect for the do-not-touch policy |
| `<sic>` forms | Lesson 6.1 | Variant-versus-error distinction |
| Dialectal or archaic forms | Lesson 6.1 | Over-normalization proper |

The first is where the model should win. The rest are where it may fail, and the
failures are more informative than the successes because they are the ones the
literature predicts.

Record the design in `logs/vlm-normalization-w6.md` before beginning.

**The takeaway for this page:** Supply the whole text, not just flagged tokens — a
model that never sees a token cannot demonstrate over-application.

---

## **07 Content**

**Prompting for Constrained Normalization**

A naive prompt guarantees over-normalization. Constrain explicitly.

```text
You are assisting with orthographic regularization of a Greek manuscript
transcription. Your task is narrowly limited.

For each token, decide whether it is a non-standard ORTHOGRAPHIC form of a
standard Greek word, and if so give the standard form.

Strict constraints:
- Regularize ORTHOGRAPHY ONLY. Do not change morphology, word order,
  vocabulary, or syntax.
- Do not replace a word with a synonym, however archaic the original.
- Do not alter dialectal forms. If a form is dialectal rather than
  misspelled, leave it and say so.
- Do not regularize proper names.
- Do not correct what appear to be textual variants or grammatical errors.
  Flag them instead.
- Where a form could be a scribal slip rather than a period-normal
  spelling, say so rather than choosing.
- Where you are uncertain, say so. Do not guess.
- Leave standard forms unchanged.

Output one JSON object per token:
{"token": "...", "action": "regularize|leave|flag",
 "proposed": "...", "type": "orthographic|dialectal|name|variant|slip",
 "confidence": "high|medium|low", "reason": "..."}

Output only JSON. No commentary.
```

Every constraint addresses a documented failure. The morphology and synonym clauses
target over-normalization; the dialect clause targets variant collapse; the name
clause targets the exclusion policy; the variant clause protects Week 7's collation;
and the slip clause targets the `<orig>`/`<sic>` judgement.

Requiring a `type` field is doing analytical work. It forces the model to state what
kind of variation it thinks it has found, which is exactly the judgement Lesson 6.1
section 06 identified as the editorial crux — and it lets you check whether the
model's classification matches yours.

Record the prompt verbatim. It is a required component of the audit under the
framework in Lesson 5.2 section 16.

**The takeaway for this page:** Requiring the model to state the *type* of variation
forces the editorial judgement into the open where it can be checked.

---

## **08 Content**

**Running It**

Execute the experiment and preserve the output before assessing anything.

```bash
python3 tools/run_llm_normalization.py \
  --input /tmp/diplomatic.xml \
  --prompt logs/prompts/normalize-v1.txt \
  --output normalization/llm_output.json
git add normalization/llm_output.json logs/prompts/normalize-v1.txt
git commit -m "feat(normalization): LLM normalization proposals, uncorrected

Zero-shot orthographic regularization via [model, version], accessed
2026-10-09. Prompt in logs/prompts/normalize-v1.txt. Raw proposals, no
review applied.

AI-Generated: true
Model: [name and version]
Model-Access-Date: 2026-10-09
Prompt-Ref: logs/prompts/normalize-v1.txt
Human-Verified: false
Baseline-Commit: <the norm-script-w6 commit>"
```

Commit before reviewing, for the same reason as every previous week: the raw state
is what gets measured, and reviewing before committing destroys the measurement.

Do not inject proposals into your TEI yet. As in Wednesday's section 09, the model
proposes and you dispose — and mixing unreviewed machine proposals into the edition
would put unverified claims into a scholarly artefact.

If the model refuses to produce clean JSON, or wraps it in commentary despite the
instruction, record that. It is a structural compliance failure of exactly the kind
Lesson 4.3 section 06 catalogued, and it belongs in the report rather than being
quietly cleaned up.

**The takeaway for this page:** Commit the raw proposals before reviewing, and do
not inject them into the TEI — the model proposes, you dispose.

---

## **09 Content**

**The Three-Way Comparison**

Extend Wednesday's comparison table with the model's column, and analyze.

| Token | Manual | Script | Model | Analysis |
| --- | --- | --- | --- | --- |
| τιμι | τιμή | τιμή (rule i-to-eta) | τιμή | All agree |
| A form with two candidates | Resolved by hand | Declined, ambiguous | Resolved | Test case; check correctness |
| A proper name | Left alone | Left alone | Regularized | Model over-applied |
| A dialectal form | Left alone | Left alone | Modernized | Over-normalization |
| A `<sic>` form | Marked as error | Normalized | Normalized | Neither machine distinguishes |
| A standard form | Left alone | Left alone | Left alone | All correct |

Compute, for the model as you did for the script on Wednesday:

```text
Precision = correct proposals / all proposals
Recall    = correct proposals / regularizations you made
```

And compute the figures that matter more here than precision and recall do:

| Measure | Definition |
| --- | --- |
| Over-normalization rate | Proposals exceeding orthography, over all proposals |
| Name violation rate | Proper names regularized, over proper names present |
| Dialectal collapse rate | Dialectal forms modernized, over dialectal forms present |
| Ambiguity resolution accuracy | Correct resolutions, over ambiguous cases |
| Type classification accuracy | Agreement with your classification of variation type |

The first three are the fidelity measures that Lesson 5.2 section 12 argued
aggregate error rates cannot capture. A model with excellent precision and a 12%
over-normalization rate is not a good normalizer for a diplomatic edition; it is a
good modernizer.

**The takeaway for this page:** Compute over-normalization, name violation, and
dialectal collapse rates — precision and recall alone cannot show a model is
modernizing rather than regularizing.

---

## **10 Content**

**Using the Baseline as a Detector**

The mechanism Wednesday's script was built to provide, now applied.

The reasoning: a rule-based baseline performs only character-level substitution. If a
model's proposal deviates *far* from what any character-level rule could produce,
the model has done something other than orthographic regularization.

By using TEI primary-source markup where deterministic rule-based transformations
provide verifiable baselines, editors create a transparent audit trail. If a neural
model converts an archaic regionalism into a modern standard word, the rule-based
baseline — which only performs character-level substitution — flags a massive
morphological deviation, immediately alerting the editor that the model has crossed
from orthographic regularization into semantic alteration (Bollmann, 2019).

Implement the detector:

```python
def deviation(original, proposal, rules, lexicon):
    """How far is `proposal` from what character rules could produce?"""
    reachable = set(candidates(original, rules, lexicon))
    if proposal in reachable:
        return 0.0, "reachable by rule"
    # Weighted edit distance from the original, normalized by length
    d = weighted_distance(original, proposal) / max(len(original), 1)
    return d, "not reachable by rule"


THRESHOLD = 0.4     # tune against your own manual regularizations
```

Run it over every model proposal and flag those exceeding the threshold. Then
inspect each flagged case by hand.

| Deviation | Interpretation |
| --- | --- |
| Zero; reachable by rule | Orthographic; probably legitimate |
| Small | Orthographic variation your rules did not cover |
| Moderate | Check: may be morphological |
| Large | Very likely lexical substitution or semantic alteration |

Calibrate the threshold on your own manual regularizations: none of them should
exceed it, since all were orthographic by policy. A threshold that flags your own
work is set too low.

**The takeaway for this page:** Proposals unreachable by any character-level rule
are where the model stopped regularizing orthography — that is the detector.

---

## **11 Content**

**Reading the Flagged Cases**

Inspect every flagged proposal individually. Each is a potential finding.

For each, determine:

- What did the model propose?
- Is the proposal a different *word* from the original, or the same word spelled differently?
- Does it change morphology — number, case, tense, person?
- Is the original a documented dialectal or archaic form?
- Does the model's stated `type` field match your analysis?
- What reason did the model give?

| Finding | Report as |
| --- | --- |
| Same word, spelling regularized by an uncovered pattern | A gap in your rules; add it |
| Same word, morphology altered | Over-normalization |
| Different word, modern synonym | Over-normalization; lexical substitution |
| Dialectal form standardized | Dialectal collapse |
| Proper name normalized | Policy violation |
| Genuine variant reading "corrected" | Serious; pre-empts Week 7 |

The first row is a real possibility and should not be assumed away. A flagged case
may be the model correctly identifying orthographic variation your rules did not
anticipate — which is a legitimate contribution and the reason to inspect rather
than reject automatically.

The last row is the most serious and worth checking for specifically. If your
manuscript has a known variant reading, look at what the model did with it. A model
that regularizes a genuine variant into the standard text has removed the evidence
Week 7's collation exists to find, and has done so invisibly.

Record every flagged case with your determination. These are the substance of
today's findings.

**The takeaway for this page:** Inspect flagged cases individually — some are gaps
in your rules, and some are the model quietly removing evidence Week 7 needs.

---

## **12 Content**

**Testing the Ambiguous Set**

The cases where the model should demonstrate its advantage.

Your ambiguous set comprises forms where several rules proposed different standard
forms, and which you resolved by hand using syntactic context. This is precisely the
capability the contextual model claims.

For each ambiguous case:

| Check | Question |
| --- | --- |
| Did the model resolve it? | Or did it also decline? |
| Did it resolve correctly? | Against your hand resolution |
| Did it give a contextual reason? | Or an unmotivated assertion? |
| Was its confidence calibrated? | High confidence on correct resolutions? |

The third column is the one worth attention. A model that resolves an ambiguous form
correctly and explains why — citing the agreement, the construction, the surrounding
sense — has demonstrated the contextual reasoning it claims. A model that resolves
correctly with the reason "this is the standard form" has produced the right answer
without demonstrating the capability, and may have got there by frequency rather
than by context.

Test this deliberately where you can. If a form's correct resolution depends on the
number of its subject, check whether the model's reason mentions the subject.

Report the resolution accuracy as a proportion, with the count. If your ambiguous
set has six members, "resolved five of six correctly, with contextual reasons given
for four" is the honest statement — and a set of six does not support a percentage.

This is the model's strongest case, and it should be reported as fairly as the
failures.

**The takeaway for this page:** Check whether correct resolutions come with genuine
contextual reasons — a right answer without the reasoning has not demonstrated the
capability.

---

## **13 Content**

**The Downstream Paradox**

A finding that complicates the whole enterprise and belongs in your report.

Normalization is rarely an end in itself. It is preprocessing for part-of-speech
tagging, morphological parsing, and corpus querying (Bollmann, 2019). The
justification for the effort is that downstream tasks work better on normalized text.

The evidence for that justification is weaker than expected. While neural models
generalize exceptionally well to unseen variant spellings, they do not consistently
yield statistically significant improvements in downstream POS tagging compared with
a naive memorization baseline (Robertson & Goldwater, 2018).

Read that carefully. A sophisticated neural normalizer that handles unseen variants
beautifully may deliver no measurable downstream benefit over simply memorizing the
variant-to-standard pairs seen in training.

| Claim | Evidence |
| --- | --- |
| Normalizing beats not normalizing | Supported; raw noisy text tags worse |
| Neural normalization generalizes to unseen variants | Supported |
| Neural normalization improves downstream tagging over memorization | Not consistently supported |
| Aggressive sentence-level normalization is safe | Not supported; incurs precision penalties |

The fourth row is the practical warning. Aggressive sentence-level neural
normalization can incur precision penalties if the model incorrectly splits, merges,
or over-corrects tokens that should remain unchanged (Bollmann, 2019).

The conclusion the literature draws is the one this week has been building toward:
evaluation of an AI regularizer must involve auditing its outputs against a
verifiable rule-based baseline, to ensure that morphological ambiguity is preserved
rather than collapsed by generative fluency (Bollmann, 2019).

That is exactly what section 10's detector does, and it is why Wednesday preceded
today.

**The takeaway for this page:** Neural normalization generalizes well and may
deliver no downstream benefit over memorization — which is why auditing against a
rule baseline is the recommended practice.

---

## **14 Content**

**Retrieval-Augmented Grounding**

An approach worth understanding, and worth attempting if you have the means.

Retrieval-augmented generation grounds a model's normalizations in external
domain-specific knowledge — historical lexicons, grammars, aligned translations —
which significantly reduces hallucination rates (Bollmann, 2019).

The mechanism: rather than relying on what the model absorbed in training, relevant
reference material is retrieved and supplied in the prompt, so the model's output is
conditioned on sources you control.

For normalization this is directly applicable. Supply, alongside the token:

- Its immediate context, a sentence or line either side.
- Candidate standard forms from your lexicon.
- The phonological account of the relevant substitution from your policy.
- Your decision-log entries for similar cases already resolved.

```text
Token: τιμι
Context: ... πρὸς τὸν τιμι τοῦ ...
Candidate standard forms from lexicon: τιμή, τιμῇ, τιμᾷ
Relevant policy: iotacism substitutions ι/ει/η are period-normal in this
  manuscript and are regularized with <orig>/<reg>.
Similar case already resolved: line 7, δι -> δεῖ, iotacism, regularized.
```

This is a lighter-weight version of full RAG and captures most of its benefit for
your scale. Constraining the model to candidates from your own lexicon in particular
prevents the model from proposing forms outside the attested vocabulary, which is a
substantial part of the over-normalization risk.

If you have time, run both the unconstrained and the grounded prompt and compare.
The difference in over-normalization rate between them is a genuinely interesting
result and directly tests the literature's claim.

**The takeaway for this page:** Supplying candidates from your own lexicon
constrains the model to attested forms — a lightweight grounding that removes much
of the over-normalization risk.

---

## **15 Content**

**Direct TEI Generation and Its Failure**

Test the claim that models can produce TEI markup natively (Bollmann, 2019).

Prompt for `<choice>` output directly and inspect what comes back:

```xml
<choice>
  <orig>τιμι</orig>
  <reg>τιμή</reg>
</choice>
```

Check specifically:

| Check | Common failure |
| --- | --- |
| Is the XML well-formed? | Unclosed or mismatched tags |
| Is it schema-valid TEI? | Invalid element placement |
| Does `<orig>` match the manuscript exactly? | Partly normalized already |
| Is the alignment correct? | Wrong original paired with a regularization |
| Are surrounding tags preserved? | `<lb/>` and `@facs` dropped |
| Is the whole text returned? | Truncation |

The third and fourth rows are the serious ones and correspond to a documented
weakness: models struggle with the deterministic projection of character-level
alignments that strict TEI markup requires (Bollmann, 2019).

An `<orig>` that has been partly normalized is the worse of the two. It defeats the
entire architecture: the diplomatic layer is supposed to record exactly what the
scribe wrote, and if the model has silently adjusted it, the edition contains a
diplomatic layer that is not diplomatic and no record of the actual form. This is
the mechanism by which over-normalization becomes permanent, as section 05 noted.

The fifth row is a practical destroyer. If the model returns `<choice>` elements
having dropped your `<lb/>` milestones and `@facs` attributes, the output cannot be
merged back into your edition without losing the coordinate bindings that Lesson 3.3
built.

Test it, record what happens, and do not use the output directly if it fails these
checks. Extracting the model's *decisions* and projecting them into TEI yourself is
safer and is what section 16 recommends.

**The takeaway for this page:** A model-generated `<orig>` that has been partly
normalized destroys the diplomatic layer silently — check it character by character.

---

## **16 Content**

**Projecting Accepted Proposals**

For proposals you accept after review, inject them with provenance distinguishing
them from both the manual and the script layers.

```xml
<choice resp="#llm" cert="medium">
  <orig>τιμι</orig>
  <reg>τιμή</reg>
</choice>
```

And declare the agent:

```xml
<respStmt xml:id="llm">
  <resp>AI-assisted orthographic regularization, reviewed by the editor</resp>
  <name>[model name and version], accessed 2026-10-09</name>
</respStmt>
```

Your edition now contains three provenance classes, and a reader can distinguish
them:

| `@resp` | Produced by | Reliability basis |
| --- | --- | --- |
| `#KMP` | The editor, by hand | Editorial judgement |
| `#script` | The rule set, reviewed | Verifiable rule plus review |
| `#llm` | The model, reviewed | Model output plus review |

That distinction is the requirement stated in Lesson 6.1 section 15: a future
researcher must know precisely whether a `<reg>` came from a human philologist, a
deterministic transducer, or a neural network, because the provenance determines the
data's reliability for downstream corpus linguistics (TEI Consortium, 2026).

Note that all three are reviewed. Nothing enters the edition unreviewed, and the
`@resp` records what *proposed* the regularization rather than what decided it. You
decided all of them.

Where you accept a model proposal that your script did not reach, note it — those
are the cases where the AI step contributed something, and counting them is how you
state its value.

**The takeaway for this page:** `@resp` records what proposed a regularization, not
what decided it — you decided all three classes, and nothing enters unreviewed.

---

## **17 Content**

**Assembling the Week's Findings**

Bring the three methods together into a comparative assessment.

| Measure | Manual | Rule script | Language model |
| --- | --- | --- | --- |
| Regularizations proposed | Record | Record | Record |
| Precision against policy | By definition | Record | Record |
| Recall | By definition | Record | Record |
| Ambiguous cases resolved | All, by hand | None; declined | Record |
| Over-normalization instances | None | None, structurally | Record |
| Proper names violated | None | Record | Record |
| Dialectal collapse | None | None, structurally | Record |
| Verifiable | Via the log | Completely | Not at all |
| Reproducible | Via the log | Exactly | Not guaranteed |
| Setup cost | High | Moderate | Minimal |
| Per-token cost | High | Negligible | Low |

Two rows say "structurally" for the script, and the word is doing real work. The
rule script *cannot* over-normalize or collapse dialectal forms, because it performs
only character-level substitution conditioned on lexicon membership. It is not that
it happened not to; it is incapable of it. That is a guarantee, and guarantees are
rare and valuable.

The model has no such guarantee, and the empty cells in its column must be filled
with measurements rather than assumptions.

Read the bottom two rows together with the rest. The model's setup cost is minimal
and its capability is broader, and those are real advantages. Whether they outweigh
the loss of verifiability depends on what the edition needs, and that is the
judgement your conclusion should make explicitly.

**The takeaway for this page:** The rule script *cannot* over-normalize, which is a
guarantee rather than an observation — the model's equivalent cells must be measured.

---

## **18 Content**

**Drawing the Conclusion**

State a specific finding, as in Lesson 5.2 section 21.

A weak conclusion: *AI over-normalizes historical text.* True, documented, and not
something you established.

A strong conclusion:

> On f. 42r of MS Vat. gr. 1209 (312 tokens, 47 manual regularizations), the
> rule-based script achieved precision 0.94 and recall 0.81, declining 5
> contextually ambiguous cases. [Model] achieved precision 0.79 and recall 0.94,
> resolving 4 of the 5 ambiguous cases correctly with contextual reasons given for
> 3. However, 9 of its 56 proposals (16%) exceeded orthographic regularization:
> 4 regularized proper names, 3 altered morphology, and 2 substituted modern lexemes
> for archaic forms. All 9 were detected by deviation from the rule baseline.
> Grounding the prompt with lexicon candidates reduced the over-normalization rate
> to 7%. The model is therefore useful for contextual disambiguation of cases the
> rule script declines, and unsuitable as a primary normalizer for this edition.

That paragraph is quantified, specific, and actionable, and it reaches a hybrid
recommendation — which is where the literature lands (Bollmann, 2019) and which you
have now derived from your own measurement rather than adopted on authority.

Include the downstream caveat from section 13. A conclusion that normalization
improves downstream processing should note that the improvement over a naive
memorization baseline is not consistently demonstrated (Robertson & Goldwater,
2018).

**The takeaway for this page:** A hybrid conclusion derived from your own
measurements is worth more than the same conclusion adopted from the literature.

---

## **19 Content**

**Guarding Against Black Boxes**

The pedagogical point the literature makes explicitly, and worth internalizing.

When a model normalizes a text, it tends to project modern grammatical sensibilities
onto historical syntax, and students must be trained to treat neural and generative
regularizers with deep scepticism (Bollmann, 2019).

"Deep scepticism" is not refusal. It is a working practice, and this week has
enacted it:

- Establish the standard yourself first, so you know what right looks like.
- Build a verifiable baseline, so deviation is detectable.
- Constrain the model explicitly against documented failure modes.
- Measure fidelity separately from accuracy.
- Inspect every proposal that deviates from what rules could produce.
- Review everything before it enters the edition.
- Record provenance so a reader can weight the layers differently.

Each step addresses a specific way that unreviewed model output damages an edition.
None of them requires rejecting the tool.

The alternative practice — running a model over the text and accepting its output —
produces a cleaner-looking edition faster, and produces it with no way of knowing
what was altered. That is the black box, and the objection is not that models are
inaccurate but that an edition whose transformations cannot be inspected is a weaker
scholarly claim regardless of its accuracy.

This is the same argument as Lesson 6.2 section 23, and it is the disposition to
carry into the remaining weeks.

**The takeaway for this page:** Scepticism is a working practice — establish the
standard, build a detector, constrain explicitly, measure fidelity, review
everything, record provenance.

---

## **20 Content**

**Updating the Header**

Record all three stages in `<editorialDecl>`, since the edition now contains
regularizations from all of them.

```xml
<encodingDesc>
  <editorialDecl>
    <normalization method="markup">
      <p>Orthographic regularization proceeded in three stages. Manual
        regularization of f. 42r established the policy in
        transcription/ORTHOGRAPHY.md (@resp="#KMP"). A deterministic
        rule-based script (tools/normalize.py v3, commit 7d2e814) was
        applied to the diplomatic text; reviewed proposals are attributed
        @resp="#script" (precision 0.94, recall 0.81). AI-assisted
        contextual disambiguation ([model, version], accessed
        2026-10-09, prompt in logs/prompts/normalize-v1.txt) was applied
        to cases the script declined; reviewed proposals are attributed
        @resp="#llm" (precision 0.79, recall 0.94; over-normalization
        rate 16% before grounding, 7% after).</p>
      <p>All proposals from automated stages were reviewed individually
        against the facsimile before acceptance. Model proposals deviating
        beyond character-level rule reachability were inspected
        individually; 9 were rejected as exceeding orthographic
        regularization.</p>
    </normalization>
  </editorialDecl>
</encodingDesc>
```

Reporting the over-normalization rate in the header is unusual and is the right
thing to do. It tells a reader how far the automated stage was constrained, which
bears directly on how much confidence the `<reg>` layer deserves — and it is
information available nowhere else.

Note also what the second paragraph does: it states the *review practice*, not just
the methods. A reader learns that nothing entered unreviewed and how the review was
targeted.

**The takeaway for this page:** Record the review practice, not only the methods —
a reader needs to know that nothing entered unreviewed and how review was targeted.

---

## **21 Content**

**Checklist Before You Leave**

Verify each.

- Experiment designed with the whole text supplied, not only flagged tokens.
- Prompt written against documented failure modes, recorded verbatim.
- Model, version, and access date recorded.
- Raw output committed before any review.
- Three-way comparison table completed.
- Precision and recall computed for the model.
- Over-normalization rate computed.
- Proper name violation rate computed.
- Dialectal collapse rate computed.
- Ambiguous set tested; resolution accuracy and reasoning quality recorded.
- Deviation detector run over all proposals; flagged cases inspected individually.
- Direct TEI generation tested, with `<orig>` checked character by character.
- Grounded prompt tried and compared, if time allowed.
- Accepted proposals injected with `@resp="#llm"`.
- Header updated with all three stages and measured performance.
- Everything committed, tagged, and pushed.
- Costs recorded for all three methods.

**The takeaway for this page:** Check model-generated `<orig>` character by
character — a silently normalized diplomatic layer is the failure that cannot be
recovered from.

---

## **22 Content**

**Common Problems Today**

Failures that recur.

| Symptom | Cause | Remedy |
| --- | --- | --- |
| Model returns prose, not JSON | Instruction not followed | Record as a compliance failure; re-prompt |
| Model normalizes everything | Constraints too weak or ignored | Strengthen; ground with lexicon candidates |
| `<orig>` differs from the manuscript | Model normalized the diplomatic layer | Do not use its TEI; extract decisions only |
| Alignment wrong in generated TEI | Character-level projection failure | Expected; project yourself |
| Model declines everything | Over-constrained prompt | Loosen one constraint at a time |
| Confidence uncorrelated with accuracy | Poor calibration | Expected; do not use confidence to target review |
| Model "corrects" a variant reading | No concept of textual criticism | Exclude by hand; report it |
| Over-normalization rate near zero | Check whether it normalized anything at all | Verify recall before celebrating |

The sixth row repeats the finding from Lesson 4.3 section 11 and holds here too. If
the model's confidence does not track its accuracy, you cannot use confidence to
decide what to review, which means reviewing everything — and the tool saves
proposal labour without saving review labour.

The last row is the trap. A model that proposes almost nothing has an excellent
over-normalization rate and is useless. Always read the fidelity measures alongside
recall; either alone is misleading.

**The takeaway for this page:** An excellent over-normalization rate on a model that
proposed almost nothing is meaningless — read fidelity measures alongside recall.

---

## **23 Content**

**What Good Work Looks Like Here**

The standard.

A minimally acceptable result is model output, committed, with a comparison against
your manual work.

Good work additionally:

- Supplies the whole text so over-application is measurable.
- Constrains the prompt against each documented failure mode.
- Requires the model to classify the type of variation and checks that classification.
- Preserves raw output before any review.
- Computes fidelity measures separately from precision and recall.
- Runs the rule baseline as a deviation detector and inspects every flagged case.
- Tests the ambiguous set specifically and assesses reasoning, not only answers.
- Checks model-generated `<orig>` character by character.
- Compares grounded and unconstrained prompting.
- Records all three provenance classes in the edition and the header.
- Reaches a hybrid conclusion supported by its own figures.

The sixth item is the methodological centre of the day. A student who compares
model output against their manual work has run a comparison. A student who uses
their rule baseline to detect where the model exceeded orthographic regularization
has built an instrument and used it — and that instrument is the literature's own
recommended safeguard (Bollmann, 2019).

**The takeaway for this page:** Using the rule baseline as a detector — rather than
merely as a competitor — is what makes today an audit rather than a comparison.

---

## **24 Content**

**Connecting to the Weeks Ahead**

Where this leaves your edition.

| Week | Uses this week's work as |
| --- | --- |
| 7 | Collation must choose `<orig>` or `<reg>` to align on |
| 8 | Apparatus distinguishes orthographic from substantive variants |
| 9 | Lemmatization operates on the `<reg>` layer |
| 11 | Alignment of translation works from regularized text |
| 12 | Commentary may discuss orthography as evidence of transmission |
| 13 | Publication offers both layers to the reader |

Week 7 is next and its choice is immediate. Collating on `<orig>` treats every
phonetic spelling difference between witnesses as a variant, swamping the apparatus.
Collating on `<reg>` suppresses them, revealing substantive variants — and
suppressing evidence of shared orthographic practice, which can indicate shared
descent.

The usual practice is to collate on `<reg>` for the main apparatus and analyze
`<orig>` separately for transmission evidence. Decide this deliberately on Tuesday,
and record the decision.

Week 9's dependency is the payoff for the whole week's effort. Morphological parsers
require standard forms, and lemmatization on unnormalized text fails on exactly the
forms iotacism produced. The `<reg>` layer is what makes that week's work possible —
subject to the caveat from section 13 that the downstream benefit over naive
memorization is not consistently demonstrated.

**The takeaway for this page:** Week 7 must choose a layer to collate on — `<reg>`
for substantive variants, `<orig>` for evidence of shared descent.

---

## **25 Content**

**The Week's Three Methods, Reviewed**

Consolidate what Topic 6 established.

Tuesday: normalization is an editorial judgement, not a mechanical operation. The
`<orig>`/`<reg>` and `<sic>`/`<corr>` distinction is genuinely contestable — the same
form may be period-normal usage to one editor and error to another (TEI Consortium,
2026) — and it must therefore be stated as policy, applied consistently, and
documented case by case. Iotacism makes this pervasive in Greek, and the variation is
evidence about date, dialect, and language contact rather than noise (Gignac, 1976).

Wednesday: the policy can be partly formalized. Rules are verifiable, reproducible,
and effective at small scale, and writing them audits the policy — exposing unstated
conditions and inconsistent application. They cannot resolve syntactic ambiguity or
distinguish variant from error, because both require information not in the token
(Bollmann, 2019).

Friday: contextual models reach what rules cannot, and bring risks rules do not
have. They over-normalize, collapsing dialectal variants and substituting modern
lexemes, and standard accuracy metrics do not detect this (Bollmann, 2019). The
rule baseline is the detector, and the recommended practice is hybrid — deterministic
transformation where it suffices, contextual models for disambiguation, human
judgement for the variant-versus-error decision.

The through-line: **each method's limits define the next method's job.** That is why
the cycle is ordered as it is, and why none of the three steps is redundant.

**The takeaway for this page:** Each method's limits define the next one's job —
which is why none of the three steps is redundant.

---

## **26 Content**

**A Note on What Was Preserved**

Worth pausing on, at the end of a week spent regularizing.

Your edition now contains a regularized layer, and it contains everything it
contained before. Not one original form was overwritten. The `<orig>` layer records
exactly what the scribe wrote, and every regularization sits beside it with an
attribution.

That is the whole architecture, and it is worth registering as an achievement rather
than as bookkeeping. Print editions faced the same choice and resolved it by
standardizing, and the sociolinguistic evidence was lost — recoverable only by
returning to the manuscripts (Robinson & Driscoll, 2016).

| Question a future scholar might ask | Answerable from your edition? |
| --- | --- |
| What did the scribe actually write? | Yes; the `<orig>` layer |
| What is the standard form? | Yes; the `<reg>` layer |
| Which regularizations did a human make? | Yes; `@resp` |
| Which did a script make, and by what rule? | Yes; `@resp` and the rule log |
| Which did a model propose? | Yes; `@resp` |
| How reliable was the automated stage? | Yes; the header records the measurements |
| What was the editorial policy? | Yes; the decision log |
| Which forms were deliberately left alone? | Yes; documented |

Every row is answerable, which is unusual. It is the product of decisions made
across six weeks — not normalizing during transcription, keeping both layers,
attributing provenance, documenting policy — and none of those decisions was
individually difficult. They were simply made deliberately rather than by default.

**The takeaway for this page:** Not one original form was overwritten — that is the
week's actual achievement, and it came from ordinary decisions made deliberately.

---

## **27 Content**

**Preparing for Week 7**

Next week is collation, and it returns to the full three-step cycle.

| Meeting | Step | Activity |
| --- | --- | --- |
| Tue Oct 20 (#17) | Manual | Collate two witnesses by hand on paper |
| Wed Oct 21 (#18) | Deterministic | Automated alignment with CollateX |
| Fri Oct 23 (#19) | AI-assisted | AI variant classification and adjudication |

Note the two-week gap: **Fall Study Break falls Oct 12–16**, with Thanksgiving on
Monday October 12. Week 7 resumes Tuesday October 20.

Bring back:

- Your edition with both layers, validated.
- The second witness's transcription, at least for the lines you will collate.
- Your decision on which layer to collate against.
- Your normalization policy, since orthographic variants must be distinguished from substantive ones.

The second item is the one to check now rather than on October 20. Collation
requires two witnesses, and if you have transcribed only your primary witness you
will have nothing to collate. Use the break to transcribe the corresponding lines of
your second witness — the HTR model from Week 4 can extend the work if it performs
adequately on that hand, though a different scribe may need its own model.

**The **Normalization Assignment is due Friday October 23**, at the end of Week 7.**

**The takeaway for this page:** Use the study break to transcribe your second
witness — Week 7's collation needs two witnesses and cannot proceed with one.

---

## **28 Content**

**What the Assignment Will Require**

The Normalization Assignment, due Friday October 23, draws on this week.

Expected components:

| Component | Source |
| --- | --- |
| Diplomatic base with regularized layer | This week |
| Orthographic policy document | Lesson 6.1 |
| Case register with individual reasoning | Lesson 6.1 |
| Rule script, rules, and lexicon | Lesson 6.2 |
| Precision and recall for the script | Lesson 6.2 |
| Model comparison with fidelity measures | Today |
| Over-normalization analysis | Today |
| Three-way comparative assessment | Today |
| TEI header documenting all stages | Today |
| Commit history with provenance | Throughout |

The over-normalization analysis is the component most specific to this week and the
one most likely to be underdone. It requires the deviation detector, individual
inspection of flagged cases, and a rate computed against a stated denominator — not
an impression that the model seemed to normalize too much.

Write what you can of the report today, while the analysis is fresh. The break
intervenes, and reconstructing today's reasoning in three weeks is substantially
harder than recording it now.

**The takeaway for this page:** Write the over-normalization analysis today — the
study break intervenes and reconstructing today's reasoning later is much harder.

---

## **29 Content**

**A Note on Judgement**

A reflective point, at the end of the first week where the task had no fact of the
matter.

Weeks 4 and 5 measured methods against the ink. Week 6 measured them against your
policy — a standard you chose. That difference has run through the week and is worth
naming.

It does not make the measurement less rigorous. A stated policy consistently applied
is a real standard, and consistency with it is measurable. What it changes is where
the authority lies: the policy is defensible or not on scholarly grounds, and if it
is poorly chosen then everything measured against it inherits the problem.

This is the position an editor is always in, and digital methods make it explicit
rather than creating it. A print editor who silently standardized orthography was
also applying a policy; the difference is that theirs was unstated and unmeasurable,
so the question of whether it was well chosen could not be raised.

| | Print practice | This edition |
| --- | --- | --- |
| Policy exists | Yes | Yes |
| Policy stated | Rarely, or in general terms | Explicitly, with a case register |
| Consistency measurable | No | Yes |
| Original recoverable | No | Yes |
| Policy contestable by a reader | Only in principle | In practice, case by case |

The bottom row is the point. Making the policy explicit does not make it right. It
makes it *arguable*, which is the condition under which it can be improved — by you
in Week 12, or by a reader in ten years.

**The takeaway for this page:** Stating the policy does not make it right; it makes
it arguable, which is the condition under which it can be improved.

---

## **30 Content**

**Synthesis: Fluency Against Fidelity, Again**

The week's conclusion, which restates Week 4's in a new domain.

A language model normalizing historical text produces good text. Standard,
grammatical, readable, consistent — and progressively less like what the scribe
wrote. Its failure mode is not error but *improvement*: it makes the text better
than the manuscript, which for a diplomatic edition is the same as making it wrong
(Bollmann, 2019).

That is the same finding as Lesson 4.3's — fluency and fidelity are independent
properties, and systems optimized for the first are not thereby good at the second.
What differs here is that the failure is harder to see. A hallucinated transcription
can be caught by comparing against the image. An over-normalized text has no image
to compare against; the standard is a policy, and a model applying a different policy
consistently produces output that looks entirely reasonable.

Hence the rule baseline. Its value is not that it normalizes better — it normalizes
less — but that it is *verifiable*, and verifiable output can serve as a detector
for output that is not. A proposal unreachable by any character-level rule is a
proposal that did something other than regularize orthography, and that test is
available only because the rule layer exists (Bollmann, 2019).

The recommended practice is hybrid, and you have now derived it: deterministic
transformation where it suffices, contextual models for disambiguation they alone
can perform, human judgement for the decision no method can make — whether a
variation is usage or error.

**Due Friday October 23.** The Normalization Assignment, at the end of Week 7.

**For Week 7, resuming Tuesday October 20 after the study break.** Collation. Bring
both witnesses transcribed, and your decision about which layer to align on.

**The takeaway for this page:** The model's failure mode is improvement rather than
error, and improvement has no image to check against — which is why the verifiable
baseline is the detector.

---

## References

Bollmann, M. (2019). *A large-scale comparison of historical text normalization
systems* (arXiv:1904.02036). https://arxiv.org/abs/1904.02036

Gignac, F. T. (1976). *A grammar of the Greek papyri of the Roman and Byzantine
periods*. Istituto Editoriale Cisalpino.

Robertson, A., & Goldwater, S. (2018). Evaluating historical text normalization
systems: How well do they generalize? In *Proceedings of NAACL-HLT*. Association
for Computational Linguistics.

Robinson, P., & Driscoll, M. J. (Eds.). (2016). *Digital scholarly editing:
Theories and practices*. Open Book Publishers.
https://doi.org/10.11647/OBP.0095

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/
