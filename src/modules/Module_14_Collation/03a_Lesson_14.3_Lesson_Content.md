# Lesson 14.3 — AI-Assisted Variant Classification and Adjudication

*RELS 398 / ENGL 398 · Topic 14: Collation · Meeting #19 (Fri Oct 23)*

***Step 3 of the three-step cycle: AI-assisted.** Today you apply semantic methods
to variant identification and classification, testing whether they supply what
character-based alignment cannot — and at what cost in reproducibility. **The
Normalization Assignment is due today.***

---

## **01 Content**

**Today's Question**

Wednesday's alignment is exact, reproducible, and semantically blind. It aligned
your witnesses by the normalized values you supplied and reported every divergence
without differentiating a trivial spelling difference from a substantive lexical
substitution.

Two things it could not do define today's test.

It could not **classify**. Tuesday's taxonomy — orthographic, morphological,
lexical, omission, transposition — required knowing what kinds of variation matter
and why, and CollateX has no concept of philological value (Nury & Spadini, 2020).

It could not **recognize semantic equivalence**. It aligns words based solely on
character overlap or the normalization dictionaries you pre-coded (Haentjens Dekker
& Middell, 2011), so a scribe substituting a synonym produces a divergence the tool
records without understanding.

Language models operate differently. They calculate semantic proximity through
high-dimensional vector embeddings, and benchmarking studies show that integrating
them can improve identification of substantive variants by recognizing synonyms and
semantic equivalents without requiring explicit manual lemmatization (Nury &
Spadini, 2020).

The countervailing finding is equally documented: their stochastic, generative
nature currently lacks the strict mathematical reproducibility, transparency, and
deterministic rigour required to produce definitive critical apparatuses, which is
why deterministic algorithms remain the persistent gold standard for baseline
scholarly collation (Haentjens Dekker & Middell, 2011).

Today tests both claims on your data.

**Vocabulary.** *Embedding* — a numeric vector representing meaning, in which
similar meanings are near one another. *Semantic equivalence* — words differing in
form that mean the same thing.

**Takeaway:** The test is whether semantic capability supplies
what character-based alignment cannot, and whether it costs the reproducibility a
critical apparatus requires.

---

## **02 Content**

**Three Tasks, Not One**

Distinguish what you are asking the model to do, because they have different risk
profiles and should be evaluated separately.

| Task | What it produces | Risk |
| --- | --- | --- |
| Classification | A taxonomy tier for each known variant | Misclassification; low |
| Semantic identification | Variants alignment missed | Hallucinated variants; moderate |
| Adjudication | A judgement about which reading is prior | Unsupported assertion; high |

**Classification** operates on variants CollateX already found. The variant sites are
established; the model assigns each a tier. Errors here are visible and correctable
against your own classification, and the model cannot invent a variant because it is
working from a fixed list.

**Semantic identification** asks the model to find what alignment missed —
particularly synonym substitutions where character overlap is low. This is where the
claimed advantage lies, and where hallucination becomes possible: a model can report
a variant at a place where the witnesses agree.

**Adjudication** asks which reading is original. This is the deepest editorial
judgement in textual criticism, resting on manuscript evidence, transcriptional
probability, and the tendency of scribes to simplify difficulty. A model has no
access to the first and an unreliable grasp of the rest.

Run all three, evaluate them separately, and expect the risk to rise across them.
Reporting a single verdict on "AI collation" would conflate three different
questions with three different answers.

**Takeaway:** Classification, semantic identification, and
adjudication are three tasks with rising risk — evaluate them separately rather than
reaching one verdict.

---

## **03 Content**

**Designing the Experiment**

The same controls as previous weeks.

- **Same passage**, same witnesses, same lines as Tuesday and Wednesday.
- **Wednesday's variant list** as the input for classification, so the model works from established sites.
- **The full aligned text** for semantic identification, so it can report what alignment missed.
- **Raw output preserved** before any assessment.
- **Prompt recorded verbatim**; model, version, and access date recorded.
- **Run twice.** This is new and specific to today.

The last control tests reproducibility directly, which is the property the
literature identifies as the decisive weakness (Haentjens Dekker & Middell, 2011).
Run the identical prompt on the identical input twice, and compare the outputs.

| Result of the repeat run | Interpretation |
| --- | --- |
| Identical output | Deterministic under these settings |
| Minor differences in wording, same decisions | Substantively reproducible |
| Different classifications for some variants | Not reproducible; report the rate |
| Different variants identified | Seriously unreproducible |

Report the disagreement rate between runs. For a critical apparatus this figure
matters more than accuracy: an apparatus that changes when regenerated is not a
stable scholarly claim, and a reader who reruns your pipeline should obtain your
result.

Record the design in `logs/vlm-collation-w7.md` before starting.

**Takeaway:** Run the identical prompt twice and report the
disagreement rate — for an apparatus, instability matters more than accuracy.

---

## **04 Content**

**Task One: Classification**

Start with the lowest-risk task. Supply the variant list from Wednesday and ask for
taxonomy tiers.

```text
You are assisting with the classification of textual variants in a Greek
manuscript collation. For each variant site below, classify the variation.

Categories:
- orthographic: spelling variation; the same word written differently
- morphological: a different form of the same word (number, case, tense)
- lexical: a different word substituted
- omission: text present in one witness and absent in the other
- transposition: text present in both but in different positions

For each site output:
{"n": <site number>, "category": "...", "confidence": "high|medium|low",
 "reason": "...", "same_lexeme": true|false}

Classify only. Do not judge which reading is original. Do not propose
readings not present in the witnesses. If a site does not fit these
categories, say so rather than forcing a classification.

Sites:
7. A: ἐγένετο | B: ἐγένοντο
8. A: τιμι    | B: τιμή
...
```

The `same_lexeme` field is doing analytical work. It forces the model to state
whether the two readings are forms of one word or two different words — which is
exactly the distinction separating the morphological tier from the lexical tier, and
the one with the largest difference in genealogical value (Nury & Spadini, 2020).

Requiring a reason is the second control. A classification with a stated reason can
be evaluated; a bare label cannot.

Note what the prompt forbids: judging priority, and proposing readings. Both are
constraints against the model exceeding the task, and both should be checked in the
output rather than assumed.

**Takeaway:** Asking whether two readings are forms of one lexeme
forces the distinction between the morphological and lexical tiers into the open.

---

## **05 Content**

**Evaluating the Classification**

Compare against your own classifications from Tuesday.

| Case | Manual | Model | Classification |
| --- | --- | --- | --- |
| Same tier | orthographic | orthographic | Agreement |
| Adjacent tier | morphological | lexical | Disagreement; check |
| Distant tier | orthographic | omission | Serious disagreement |
| Model declined | classified | "does not fit" | Check whether your tier was forced |

Compute agreement overall and per tier, since the tiers are not equally difficult:

| Tier | Expected difficulty |
| --- | --- |
| Omission | Easy; one witness has text and the other does not |
| Orthographic | Moderate; requires knowing the period's spelling norms |
| Morphological versus lexical | Hard; requires knowing whether two forms share a lexeme |
| Transposition | Hard; requires seeing beyond the local site |

The third row is where disagreement will concentrate, and it is where the stakes are
highest. The distinction determines whether a variant carries moderate or high
genealogical value: morphological variation may reveal regional scribal habit, while
a shared lexical substitution strongly indicates a shared exemplar (Nury & Spadini,
2020).

For a language with rich morphology like Greek, deciding whether two forms are the
same lexeme is a real linguistic question, and a model with genuine command of Greek
morphology should do it well. Whether yours does is worth measuring specifically.

Where you and the model disagree, decide which is right by consulting a lexicon
rather than by defaulting to your own classification. This is a domain where the
model may know more than you do.

**Takeaway:** Morphological versus lexical is where disagreement
concentrates and where genealogical stakes are highest — resolve it with a lexicon,
not by defaulting to your own answer.

---

## **06 Content**

**Task Two: Semantic Identification**

The claimed advantage, now tested.

Supply the aligned text and ask the model to identify substantive variants that
character-based alignment may have missed or mis-handled.

```text
Below is an aligned collation of two witnesses. Character-based alignment
may have missed variants where the witnesses use different words with
similar meaning, or mis-aligned where similar-looking words differ in
sense.

Identify any site where:
- The witnesses use different words meaning the same or similar things
  (synonym substitution), which alignment may have recorded as unrelated.
- The witnesses use similar-looking words with different meanings, which
  alignment may have wrongly treated as a match.

For each, output:
{"location": "...", "witness_a": "...", "witness_b": "...",
 "relation": "synonym|false_match|other", "reason": "..."}

Report only sites where the witnesses genuinely differ in the text
supplied. Do not propose readings that are not present. If you find
nothing, say so.
```

The last instruction is the essential guard. A model asked to find things will find
things, and a model asked to find things that may not exist will invent them. An
explicit permission to report nothing reduces that pressure, though it does not
eliminate it.

Check every reported site against the actual witness texts before accepting it. The
specific failure to look for: a reported variant at a location where both witnesses
read identically, which is a hallucinated variant and the most serious failure
available in this task.

The `false_match` category is worth including because it tests the opposite error.
Wednesday's `near_match` discussion noted that fuzzy alignment may align distinct
substantive words that coincidentally share characters, introducing false positives
(Nury & Spadini, 2020). If you used `near_match`, this is the check on it.

**Takeaway:** Verify every reported variant against the witness
texts — a variant reported where both witnesses agree is a hallucination, the most
serious failure here.

---

## **07 Content**

**Measuring Semantic Identification**

Assess what the model contributed and what it invented.

| Outcome | Count | Verification |
| --- | --- | --- |
| Genuine synonym substitution CollateX missed | Record | Check both witness texts |
| False match CollateX made, correctly identified | Record | Check the alignment |
| Site reported where witnesses agree | Record | Hallucination |
| Site reported that is a known orthographic variant | Record | Misclassification, not a find |
| Nothing found | — | Compare against your manual record |

The first row is the value case. If the model identified a genuine synonym
substitution that character-based alignment recorded as unrelated divergence, it
has done something CollateX structurally cannot — and that is the literature's claim
verified on your data (Nury & Spadini, 2020).

The third row is the cost case. Count it as a proportion of total reports, and
report the figure. A method contributing two genuine finds and three hallucinations
is not obviously useful, because the hallucinations must be checked, and checking
requires exactly the manual comparison the tool was meant to spare you.

Consider also the base rate. If your two witnesses are closely related, there may be
no synonym substitutions to find, and a model reporting several has probably
invented them. Your manual collation from Tuesday is the check: you read the passage
word by word and would likely have noticed a substituted synonym.

Where the model found nothing and you found nothing, that is a consistent result and
worth reporting as such rather than as a failure of the exercise.

**Takeaway:** A method producing two genuine finds and three
hallucinations saves no labour, because verifying the hallucinations requires the
manual comparison it was meant to replace.

---

## **08 Content**

**Task Three: The Transposition Test**

The specific test set up on Wednesday, and the sharpest comparison available.

CollateX cannot represent a transposition as one event, because the variant graph
must remain acyclic and a backward edge would create a forbidden cycle; it identifies
transpositions by post-hoc heuristics and superimposes them as dashed metadata rather
than structure (Schmidt & Colomb, 2009).

A model reasoning about the text has no such constraint. Ask it directly:

```text
Below is an aligned collation showing an omission at location X and an
addition at location Y. Determine whether these represent two independent
events or a single transposition of the same text to a different position.

Consider: are the omitted and added passages the same text? If so, is the
relocation plausible as a scribal or editorial act?

Output: {"single_event": true|false, "relation": "...", "reason": "..."}
```

| Model response | Assessment |
| --- | --- |
| Correctly identifies a single transposition, with reasoning | The semantic method supplies what the graph cannot |
| Identifies it but cannot explain why | Right answer, unclear basis |
| Treats them as independent events | No advantage over CollateX |
| Reports a transposition where none exists | Hallucination |

The first row would be a genuine finding. It is a case where a data-model
limitation — the acyclicity constraint — is overcome by a method not bound by that
model, and it is the clearest illustration this week offers of what semantic
reasoning adds.

If you have no transposition, construct a test. Take a passage from your own text,
move a clause, and present the resulting alignment. It is artificial and it tests the
capability, which is worth knowing about even where your own witnesses do not
exercise it.

Record the result either way. This is the sharpest single comparison in the week.

**Takeaway:** Recognizing a transposition as one event is where a
model overcomes a limitation built into the graph model itself — construct a test if
your witnesses do not supply one.

---

## **09 Content**

**Task Four: Adjudication, and Its Limits**

The highest-risk task, approached carefully.

Ask which reading is prior, and observe what grounds the model offers.

Classical criteria for adjudicating between readings:

| Criterion | Principle |
| --- | --- |
| *Lectio difficilior potior* | The harder reading is likelier original; scribes simplify |
| *Lectio brevior potior* | The shorter reading is often original; scribes expand |
| Transcriptional probability | Which reading better explains the origin of the other |
| Intrinsic probability | Which reading better suits the author's style and sense |
| External evidence | The weight and character of the witnesses attesting each |

A model can apply the first four, which are reasoning about the text. It cannot
apply the fifth, because the weight of witnesses depends on their date, character,
and genealogical position — information not in the readings.

That limitation is not incidental. External evidence is frequently decisive, and an
adjudication resting only on internal criteria is a partial argument presented as a
conclusion.

Test whether the model acknowledges this:

| Model behaviour | Assessment |
| --- | --- |
| Applies internal criteria and names them | Reasoning transparently |
| Notes that external evidence is needed and unavailable | Appropriately limited |
| Reaches a confident verdict on internal grounds alone | Overreaching |
| Cites external evidence it cannot have | Fabrication |

The last row is the one to check for specifically. A model asserting that one
witness is "generally more reliable" or "of an earlier textual family" is asserting
something it has no basis for unless you supplied it — and if it did not come from
your prompt, it came from nowhere.

Do not adopt an adjudication you cannot independently justify. The lemma you choose
in Week 8 is your editorial claim regardless of what proposed it.

**Takeaway:** A model can apply internal criteria and cannot weigh
witnesses — an adjudication citing external evidence you did not supply is fabricated.

---

## **10 Content**

**Testing Reproducibility**

Run the repeat comparison from section 03 and report it.

```python
import json

a = json.load(open("collation/llm_run1.json"))
b = json.load(open("collation/llm_run2.json"))

disagreements = [
    (x["n"], x["category"], y["category"])
    for x, y in zip(a, b) if x["category"] != y["category"]
]
print(f"{len(disagreements)} of {len(a)} classifications differ between runs")
```

| Measure | Report |
| --- | --- |
| Classifications differing between runs | Count and proportion |
| Variants identified in one run only | Count |
| Adjudications differing | Count |
| Reasons differing while conclusions agree | Count |

The last row is worth separating. A model reaching the same classification by
different stated reasoning is substantively reproducible in its output and not in
its argument — which for a scholarly apparatus is an odd position: the claim is
stable and its justification is not.

Interpret the overall result against what an apparatus requires. Deterministic
algorithms remain the gold standard for baseline collation precisely because the
generative approach lacks the mathematical reproducibility and transparency a
definitive critical apparatus needs (Haentjens Dekker & Middell, 2011). Your figure
is the local measurement of that general claim.

If the runs agree exactly, note the settings — a temperature of zero or an equivalent
determinism setting may explain it, and the result is then conditional on that
configuration rather than a general property.

**Takeaway:** A model reaching the same conclusion by different
reasoning is reproducible in its claims and not in its argument — an odd position for
an apparatus.

---

## **11 Content**

**Assembling the Three-Way Comparison**

Bring the week's methods together.

| Capability | Manual | CollateX | Model |
| --- | --- | --- | --- |
| Find variants | Yes; fatigue-limited | Yes; exhaustive | Partial |
| Classify by tier | Yes | No | Record |
| Recognize semantic equivalence | Yes | No | Record |
| Transposition as one event | Yes | No | Record |
| Handle omissions | Yes | Yes; affine gaps | Record |
| Scale | Tens of lines | Millions of words | Moderate |
| Reproducible | No | Exactly | Record |
| Transparent | Via the method document | Fully | Prompt only |
| Cost | High per line | Setup, then negligible | Low |

Read the "Classify by tier" and "Reproducible" rows together. They point in opposite
directions, and that opposition is the week's finding: the method that can classify
is the one that cannot be reproduced, and the method that is exactly reproducible
cannot classify.

That suggests the division of labour the literature recommends and that Weeks 5 and
6 also reached: deterministic alignment for the baseline, semantic methods for the
judgements alignment cannot make, and human review of both.

Fill every "Record" cell with your own measurement. The table is the report's core,
and unmeasured cells are the difference between a finding and a summary of the
reading.

**Takeaway:** The method that can classify cannot be reproduced,
and the method that is exactly reproducible cannot classify — that opposition is the
week's finding.

---

## **12 Content**

**Where the Model Genuinely Helps**

Be fair to the tool, as in Lesson 4.3 section 14.

| Task | Suitability | Reason |
| --- | --- | --- |
| Classifying established variant sites | Good, with review | Working from a fixed list; errors visible |
| Identifying synonym substitution | Promising | The documented capability |
| Recognizing a transposition as one event | Promising | Not bound by the DAG |
| Explaining a variant's likely mechanism | Useful | Domain knowledge, verifiable |
| Suggesting parallels for a reading | Useful, with verification | Broad textual coverage |
| Producing the baseline alignment | Poor | Not reproducible; no advantage |
| Adjudicating priority | Poor | Cannot weigh external evidence |
| Generating the apparatus unreviewed | Poor | Unverifiable claims in a scholarly artefact |

The first row is the practical recommendation. Classification is a real bottleneck:
CollateX produces variant sites in bulk and every one needs a tier before the
apparatus can be filtered. That is repetitive work on a fixed list, where errors are
checkable against the readings themselves — precisely the conditions under which
machine assistance is safe.

The sixth row is the clear negative. Using a model to produce the alignment itself
would replace an exact, reproducible, well-understood algorithm with an approximate
unreproducible one, gaining nothing. Deterministic algorithms remain the gold
standard for baseline collation (Haentjens Dekker & Middell, 2011), and there is no
argument for displacing them here.

The pattern across the table is the one from Lesson 4.3: these tools help where
semantic knowledge is the point and harm where reproducibility is the point.
Collation baselines are the second kind; classification is the first.

**Takeaway:** Use the model for classification, where errors are
checkable against a fixed list — never for the baseline alignment, which is already
exact and reproducible.

---

## **13 Content**

**Recording Provenance**

Your collation now has three sources, and the apparatus that Week 8 builds must
distinguish them.

TEI's `@resp` and `@cert` carry this at the element level, and the same three-class
scheme as Week 6 applies:

| Source | `@resp` | Basis |
| --- | --- | --- |
| Manual collation | `#KMP` | Direct comparison of witnesses |
| CollateX alignment | `#collatex` | Deterministic alignment, configured |
| Model classification | `#llm` | Model proposal, reviewed |

Declare each in the header, naming the configuration or version:

```xml
<respStmt xml:id="collatex">
  <resp>Automated alignment</resp>
  <name>CollateX, configuration v4, commit 9a2f10c</name>
</respStmt>
<respStmt xml:id="llm">
  <resp>Variant classification, reviewed by the editor</resp>
  <name>[model and version], accessed 2026-10-23</name>
</respStmt>
```

Commit today's raw output with full trailers before any review, as in every previous
week:

```text
feat(collation): LLM variant classification, unreviewed

Classification of 34 CollateX variant sites via [model, version].
Prompt in logs/prompts/classify-v1.txt. Two runs performed; outputs in
llm_run1.json and llm_run2.json. Raw output, no review applied.

AI-Generated: true
Model: [name and version]
Model-Access-Date: 2026-10-23
Prompt-Ref: logs/prompts/classify-v1.txt
Human-Verified: false
Run-Disagreement: 3 of 34 classifications
```

The `Run-Disagreement` trailer is worth adding. It records the reproducibility
measurement in the history, where it can be queried alongside everything else.

**Takeaway:** Record the between-run disagreement rate as a commit
trailer — it belongs in the queryable history alongside the other provenance.

---

## **14 Content**

**Checklist Before You Leave**

Verify each.

- Same passage, witnesses, and lines as Tuesday and Wednesday.
- Classification run on Wednesday's established variant sites.
- Semantic identification run on the aligned text.
- Transposition test run, constructed if necessary.
- Adjudication run, with attention to what grounds are offered.
- Every run repeated once; disagreements counted.
- Raw output committed before review, with full trailers.
- Classification agreement computed overall and per tier.
- Every reported variant verified against the witness texts.
- Hallucinated variants counted and reported as a proportion.
- Adjudications checked for fabricated external evidence.
- Three-way comparison table completed with no unmeasured cells.
- Accepted classifications injected with `@resp="#llm"`.
- Header updated with all three responsible agents.
- Method document updated.
- Costs recorded for all three methods.
- Everything committed, tagged, and pushed.
- **Normalization Assignment submitted.**

**Takeaway:** Verify every model-reported variant against the
witness texts — that check is what separates a contribution from a hallucination.

---

## **15 Content**

**Common Problems Today**

Failures that recur.

| Symptom | Cause | Remedy |
| --- | --- | --- |
| Model reports many variants | Asked to find, so it finds | Verify each against the texts |
| Variant reported where witnesses agree | Hallucination | Count and report; do not accept |
| Classifications differ between runs | Stochastic generation | Report the rate; it is the finding |
| All variants classified "lexical" | Not distinguishing lexeme identity | Check the `same_lexeme` field |
| Confident adjudication on internal grounds | Overreaching | Do not adopt; note it |
| Model cites witness reliability | Fabricated external evidence | Serious; report it |
| Output not valid JSON | Format instruction ignored | Compliance failure; record it |
| Model refuses to classify anything | Over-constrained prompt | Loosen one constraint |

The second and sixth rows are the reportable failures rather than problems to fix. A
hallucinated variant and a fabricated claim about witness reliability are both
findings about the method, and cleaning them up quietly would discard the result.

The fourth row is worth checking specifically. If every variant comes back
classified as lexical, the model is not making the morphological distinction at all,
and the `same_lexeme` field is what reveals it — a model reporting `same_lexeme:
false` for two forms of the same verb has failed at Greek morphology rather than at
classification.

**Takeaway:** Hallucinated variants and fabricated witness claims
are findings to report, not problems to quietly clean up.

---

## **16 Content**

**What Good Work Looks Like Here**

The standard.

A minimally acceptable result is model classifications compared against your own.

Good work additionally:

- Separates the three tasks and evaluates each on its own terms.
- Runs everything twice and reports the disagreement rate.
- Verifies every reported variant against the witness texts.
- Counts hallucinations as a proportion of reports.
- Tests the transposition case specifically, constructing one if needed.
- Checks adjudications for fabricated external evidence.
- Computes classification agreement per tier, not only overall.
- Resolves morphological-versus-lexical disagreements with a lexicon.
- Fills every cell of the three-way comparison with a measurement.
- Reaches a division-of-labour conclusion supported by its own figures.

The second item is the one most specific to today. Reproducibility is the property
the literature identifies as decisive for critical apparatus work (Haentjens Dekker &
Middell, 2011), and it is measurable in ten minutes by running the same prompt
twice. A report that assesses accuracy without assessing stability has measured the
less important property.

**Takeaway:** Measuring stability takes ten minutes and assesses
the property that actually decides whether a method can produce an apparatus.

---

## **17 Content**

**Drawing the Conclusion**

State a specific finding.

> On 34 variant sites between MS Vat. gr. 1209 and BnF gr. 2934 (ff. 42r–43v),
> [model] classified variants in agreement with manual classification at 29 of 34
> sites (85%). Disagreement concentrated in the morphological–lexical distinction
> (4 of 5 disagreements); lexicon consultation supported the model in 3 of those 4.
> Repeated runs differed at 3 of 34 classifications (9%). Semantic identification
> reported 5 sites; 2 were genuine synonym substitutions CollateX had recorded as
> unrelated divergence, 2 were known orthographic variants, and 1 was a site where
> both witnesses read identically. The model correctly identified the transposition
> at lines 14–16 as a single event, which CollateX reported as an omission and a
> separate addition. Adjudication was attempted at 6 sites; at 2 the model asserted
> that witness A was "generally more reliable," which is unsupported by anything in
> the supplied data.
>
> The model is therefore useful for classifying established variant sites and for
> identifying transposition, subject to review, and unsuitable for producing the
> baseline alignment or adjudicating priority.

Quantified, specific, and reaching a division of labour rather than a verdict on the
technology. Note that it reports both a genuine advantage — the transposition, which
CollateX structurally cannot represent — and a serious failure, the fabricated
reliability claim.

Include cost. The model classified 34 sites in under a minute, against the session
your manual classification took, and that difference matters for a real edition with
several hundred sites.

**Takeaway:** Report both the genuine advantage and the serious
failure — a conclusion reporting only one of them is not a measurement.

---

## **18 Content**

**Consolidating the Week**

What Topic 14 established across three meetings.

**Tuesday.** Collation records where witnesses differ, and the record is evidence
about transmission. Variant types differ enormously in genealogical value:
orthographic variation is polygenetic and proves little, while a long inexplicable
omission is very unlikely to arise twice and proves a great deal (Nury & Spadini,
2020). Classification is judgement, and working by hand made visible how many
judgements were being made silently.

**Wednesday.** Sequence alignment is solved. Needleman–Wunsch gives optimal global
alignment, Gotoh's affine gap penalties match the mechanics of scribal omission, and
the variant graph represents many witnesses without privileging any (Needleman &
Wunsch, 1970; Gotoh, 1982; Schmidt & Colomb, 2009). What required work was
tokenization and normalization — stages 1 and 2 of the Gothenburg Model, where the
philology lives (Haentjens Dekker & Middell, 2011).

**Friday.** Semantic methods supply what character-based alignment structurally
cannot: variant classification, recognition of synonym substitution, and
transposition as a single event. They cost reproducibility, transparency, and
reliability — which is why deterministic algorithms remain the baseline standard
(Haentjens Dekker & Middell, 2011).

The through-line, again: each method's limits define the next one's job.

**Takeaway:** Alignment is solved, definition is configuration, and
classification needs semantics — three meetings, three distinct problems.

---

## **19 Content**

**The Epistemological Burden, Restated**

The claim worth carrying out of this week.

Comparative evaluation of collation tools concludes that while algorithms can
perfectly align character strings, the epistemological burden of defining and
interpreting textual variance ultimately remains with the human scholar (Nury &
Spadini, 2020).

Three things this week demonstrated concretely support that.

**Defining.** Wednesday's collation was a function of your `n` values. Four
different configurations produce four different, equally correct collations of the
same two witnesses, and only the method document says which question yours answers.

**Classifying.** The taxonomy determining genealogical value is philological
knowledge. The model can assist, with review, and its 85% agreement means one site
in seven needs your correction.

**Interpreting.** What a variant means for the relationship between witnesses — that
an omission bounded by similar endings is mechanical, that a shared lexical
substitution indicates a shared exemplar — is inference from evidence, and no method
this week performed it.

The tools produce a perfectly structured, mathematically sound dataset upon which
rigorous textual criticism can be performed (Nury & Spadini, 2020). The dataset is
not the criticism, and this week's work was largely about the difference.

**Takeaway:** The tools produce the dataset; defining what counts,
classifying it, and interpreting it remain the scholarship.

---

## **20 Content**

**Preparing for Week 8**

Next week builds the apparatus criticus.

| Meeting | Step | Activity |
| --- | --- | --- |
| Tue Oct 27 (#20) | Manual | Encode an apparatus entry by hand |
| Wed Oct 28 (#21) | Deterministic | Generate the apparatus from CollateX output; validate |
| Fri Oct 30 (#22) | AI-assisted | AI-assisted apparatus drafting and error hunting |

Bring:

- Wednesday's TEI parallel segmentation export.
- The classified variant list, with provenance recorded.
- Your taxonomy and the filtering policy it implies.
- Both witnesses' sigla, ready to formalize in `<listWit>`.
- The transposition, and a note that it arrives as two entries.

Week 8 adds three things to what you have: the **lemma** at each site, which is the
central editorial act; the **filtering** by significance, which your taxonomy
determines; and the **formal sigla** that make `@wit` references resolve.

Note also that **mid-term grades are due Monday October 26**, and the **Textual
Variants & Collation Assignment is due Friday October 30**.

**Takeaway:** Week 8 adds the lemma, the significance filter, and
the formal sigla — the three things this week's output deliberately lacks.

---

## **21 Content**

**Due Today**

The **Normalization Assignment**, from Topic 6, is due today.

Its components, from Lesson 6.3 section 28:

| Component | Source |
| --- | --- |
| Diplomatic base with regularized layer | Week 6 |
| Orthographic policy document | Lesson 6.1 |
| Case register with individual reasoning | Lesson 6.1 |
| Rule script, rules, and lexicon | Lesson 6.2 |
| Precision and recall for the script | Lesson 6.2 |
| Model comparison with fidelity measures | Lesson 6.3 |
| Over-normalization analysis | Lesson 6.3 |
| Three-way comparative assessment | Lesson 6.3 |
| TEI header documenting all stages | Lesson 6.3 |
| Commit history with provenance | Throughout |

Verify before submitting:

- All XML validates against the TEI schema.
- All text is NFC-normalized.
- Every regularization carries `@resp`.
- The header documents all three normalization stages with measured performance.
- Every figure states its preprocessing.
- Tags are pushed.

Tag the submitted state:

```bash
git tag -a submission-normalization \
  -m "Normalization Assignment as submitted, 23 Oct 2026"
git push --tags
```

**Takeaway:** Tag and push the submitted state — three more weeks
of work will otherwise make it unrecoverable.

---

## **22 Content**

**A Note on What Collation Cannot Settle**

An honest limitation to carry into Week 8.

You have collated two witnesses. Week 8 will ask you to choose a lemma at each
variant site — to say which reading your edition adopts.

With two witnesses that choice frequently cannot be settled by the evidence. Where A
and B differ and both readings are grammatical and sensible, nothing in the collation
determines which is prior. You will be choosing on internal criteria — the harder
reading, the shorter reading, transcriptional probability — which are principles of
judgement rather than decisive evidence.

| Situation | Settleable? |
| --- | --- |
| One reading is ungrammatical | Usually; the other is prior |
| One witness omits by evident *homoioteleuton* | Usually; the fuller text is prior |
| Both readings are sound | Not by two witnesses alone |
| One reading explains the origin of the other | Arguably; state the reasoning |

Week 8's apparatus must therefore record uncertainty as well as decisions. TEI's
`@cert` on `<lem>` exists for this, and a lemma chosen on balance with the
alternative recorded is more honest than a confident selection.

This is the same disposition asked for in Lesson 4.1's `<unclear>` and Lesson 6.1's
`@cert`: record what the evidence supports, and mark where you have gone beyond it.

**Takeaway:** With two witnesses, many lemma choices cannot be
settled by evidence — record them as judgements with the alternative preserved.

---

## **23 Content**

**Synthesis: Three Instruments, One Task**

The argument of this week.

Collation is the comparison of witnesses to record difference. It is a single task
and this week applied three instruments to it, each with a distinct character.

**Manual collation** supplies interpretation continuously. You saw each variant in
context, classified it as you went, recognized a transposition as one event, and —
most importantly — discovered the rules you were applying without stating them. It
does not scale and it fails through fatigue, randomly and silently (Fradejas Rueda,
2022).

**Automated alignment** supplies exactness, scale, and reproducibility. The
algorithms are settled and the alignment stage needed no work from you; what needed
work was defining what a token is and which differences count, which is philology
expressed as configuration (Haentjens Dekker & Middell, 2011). It fails
systematically, which makes its errors invisible without an independent baseline and
correctable once found.

**Semantic methods** supply what neither of the others does at scale: classification
by significance, recognition of semantic equivalence, and the ability to see a
transposition as one event despite the graph model's constraint (Nury & Spadini,
2020; Schmidt & Colomb, 2009). They fail by fabrication, and they are not
reproducible — which disqualifies them from producing a baseline apparatus
(Haentjens Dekker & Middell, 2011).

No instrument dominates. The division of labour follows from the failure modes, and
your report should state it as a recommendation for your own edition rather than as a
general verdict.

**Due today.** The Normalization Assignment.

**For Tuesday, October 27.** Week 8 builds the apparatus criticus. Bring the five
items in section 20.

**Takeaway:** Three instruments with three failure modes — random,
systematic, and fabricating — and the division of labour follows from which failure
you can afford where.

---

## **24 Content**

**The Course So Far**

Worth a moment's consolidation, at the halfway point of the term.

| Week | Layer built | Manual reference established |
| --- | --- | --- |
| 1 | Version control and encoding | Commit discipline; NFC policy |
| 2 | Metadata and TEI header | Manuscript description |
| 3 | Image layer and coordinate binding | Canvas records; hand-measured zones |
| 4 | Transcription | Diplomatic ground truth |
| 5 | Verified transcription | Consensus text by double-keying |
| 6 | Normalized layer | Orthographic policy |
| 7 | Collation | Variant record and taxonomy |

Read the right-hand column. Every week produced a hand-made reference, and every
week the automated methods were measured against it. That is not incidental
repetition; it is the course's method, and by now the reason should be plain.

An automated method cannot be evaluated against its own output. Some independently
produced standard is required, and for editorial tasks that standard is a scholar's
judgement, recorded as policy and applied by hand. The manual step is not the
traditional way of doing what the tools now do faster; it is the thing that makes
the tools assessable.

The layers also accumulate. Your edition now has images bound to coordinates,
transcription bound to images, a normalized layer parallel to the diplomatic one, and
a collation against a second witness — each attached to the canvas coordinate space
Week 3 established.

**Takeaway:** Every week produced a hand-made reference because an
automated method cannot be evaluated against its own output.

---

## **25 Content**

**What Remains**

The second half of the term, so today's work has visible destination.

| Week | Topic | Builds on |
| --- | --- | --- |
| 8 | Apparatus | This week's collation |
| 9 | Lemmatization | The `<reg>` layer |
| 10 | Consolidation | Everything; no new method |
| 11 | Alignment | Transcription and translation |
| 12 | Commentary | All layers; the decision logs |
| 13 | Publication | The complete edition |

Week 12 is where this week's contextual notes pay off. An apparatus entry states
that witnesses differ; a commentary explains what the difference means, and the
explanation rests on observations made while looking at the passage — which you made
on Tuesday and recorded.

Week 10 is the consolidation week, with no new method and deliberate slack. It is
the point at which the accumulated layers are reconciled and gaps addressed, and it
is worth knowing it exists: work that slips in the next two weeks has somewhere to
land.

Week 13 publishes. Everything from Week 1's `.gitattributes` to today's variant
classification becomes part of a single artefact, and the decision logs written along
the way become its editorial introduction.

**Takeaway:** Week 10 is deliberate slack with no new method — work
that slips in Weeks 8 and 9 has somewhere to land.

---

## **26 Content**

**A Note on Accumulated Documentation**

Something worth noticing about what you now hold.

Your repository contains, alongside the edition itself, a set of documents recording
how each layer was made:

| Document | Records |
| --- | --- |
| `images/SOURCES.md` | Manifest URLs, rights, spectral layers |
| `images/CANVASES.md` | Canvas identifiers, dimensions, scale factors |
| `transcription/HAND.md` | The scribe's letterforms and habits |
| `transcription/CONVENTIONS.md` | Transcription policy |
| `transcription/ORTHOGRAPHY.md` | Normalization policy and case register |
| `collation/METHOD.md` | Collation and configuration policy |
| `logs/` | Measurements, prompts, error categorizations |

None of these was individually laborious. Together they constitute something a
printed edition puts in its introduction and usually compresses to a few pages — and
yours is more detailed, case-by-case, and searchable.

In Week 13 these become the edition's front matter. In Week 12 they are the source
of the commentary. And at any point, they are what lets a reader evaluate a claim
rather than accept it.

That is the concrete answer to a question worth asking about this course: why so
much recording? Because an edition is an argument, and an argument whose premises are
not stated cannot be assessed. The recording is not overhead on the scholarship; it
is a substantial part of what makes it scholarship.

**Takeaway:** The accumulated method documents are the edition's
front matter and the source of its commentary — the recording is the scholarship, not
overhead on it.

---

## **27 Content**

**Costs Across the Week**

Complete the cost comparison, since the week's recommendation depends on it.

| Method | Setup | Per-variant-site cost | Scales to |
| --- | --- | --- | --- |
| Manual collation | None | High | Tens of lines |
| CollateX | A session's configuration | Negligible | Millions of words |
| Model classification | A prompt | Low, plus review | Hundreds of sites |

Fill in your own figures. The comparison for a term project differs from the
comparison for a large edition, and it is worth being explicit about which you are
reasoning about.

For your passage — twenty to forty lines, two witnesses — manual collation is
genuinely competitive, because CollateX's configuration cost never amortizes over so
few lines. That is an honest finding and should be reported if it is what you
measured.

For the *Siete Partidas* at 11 million words and 100 witnesses, manual collation is
not slow but impossible, and the configuration cost is trivial against the
alternative (Fradejas Rueda, 2022).

The general shape, which has recurred all term: **automation's value scales with the
work, and configuration cost is fixed.** Below some threshold the manual method wins
on cost and quality both; above it, there is no manual method.

Say where your own passage falls. The answer is not embarrassing in either
direction, and stating it is the difference between a measurement and an
endorsement.

**Takeaway:** Configuration cost is fixed and automation's value
scales with the work — say honestly which side of that threshold your passage falls
on.

---

## **28 Content**

**Reproducibility as an Editorial Value**

A final conceptual point, drawing together three weeks.

Week 5 established that a measurement is an argument whose premises are the
reference and the preprocessing. Week 6 established that a rule-based `<reg>` is a
claim a reader can check while a neural one is a claim they must trust. This week
established that an apparatus which changes when regenerated is not a stable
scholarly claim.

The common thread is that **an edition's claims should be re-derivable**. Not merely
correct, but reconstructible from stated premises by anyone with the materials.

| Component of your edition | Re-derivable? |
| --- | --- |
| Image coordinates | Yes; recorded with dimensions |
| Transcription | No; but the method is documented |
| Consensus text | Yes; both passes and the log are committed |
| Normalized layer, rule-produced | Yes; the script is committed |
| Normalized layer, model-produced | No; recorded as such |
| Collation | Yes; configuration committed |
| Variant classification | Partly; the prompt is recorded |

The rows answering "no" are not failures. Transcription cannot be re-derived because
it depends on a person reading a manuscript, and that is in the nature of the task.
What matters is that the edition *says which rows are which*, so a reader knows
which claims they can check and which they must take on the editor's authority.

That distinction — between what is verifiable and what is attested — is old in
scholarship and predates any of these tools. Digital methods make it explicit and
measurable, which is most of what they have contributed to editing.

**Takeaway:** Some claims can be re-derived and some rest on the
editor's authority — what matters is that the edition says which are which.

---

## **29 Content**

**Before You Go**

Final verification for the week and for the assignment.

- Normalization Assignment submitted and tagged.
- Today's raw model output committed with full trailers before review.
- Between-run disagreement measured and recorded.
- Three-way comparison table complete, with no unmeasured cells.
- Every model-reported variant verified against the witness texts.
- Hallucinations counted and reported.
- Adjudications checked for fabricated external evidence.
- Accepted classifications injected with `@resp="#llm"`.
- All three responsible agents declared in the header.
- `collation/METHOD.md` updated with today's methods and measurements.
- Costs recorded for all three methods.
- Everything pushed, including tags.

Confirm the push:

```bash
git status && git ls-remote --tags origin | tail -5
```

An unpushed week's work is a week's work at risk, and the study break has already
demonstrated how easily context is lost across a gap.

**Takeaway:** Confirm tags reached the remote — an unpushed week is
a week at risk.

---

## **30 Content**

**Synthesis: The Dataset and the Criticism**

The week's conclusion.

Automated collation does not do the philological work. It provides a perfectly
structured, mathematically sound dataset upon which rigorous textual criticism can
be performed (Nury & Spadini, 2020).

That sentence has been the week's argument, and each meeting supplied a different
part of the evidence for it.

Tuesday showed how much judgement collation requires, by slowing it down until the
judgements became visible. Wednesday showed that the alignment problem is solved and
that the remaining work is definitional — what a token is, which differences count —
which is philology expressed as configuration. Today showed that semantic methods
reach what alignment cannot, at a cost in reproducibility that a baseline apparatus
cannot pay.

What none of the three methods did was interpret. Whether a shared omission indicates
a shared exemplar; whether a lexical substitution is a scribal error or an editorial
intervention; which reading a critical edition should adopt — these are inferences
from evidence, and the evidence is what this week produced.

Week 8 begins making those inferences, in the form of an apparatus criticus. It will
require, at every variant site, a decision that no method here can make for you.

**Due today.** The Normalization Assignment.

**For Tuesday, October 27.** Week 8: the apparatus criticus. Bring the five items in
section 20, and expect to choose a lemma at every site you collated.

**Takeaway:** This week produced the evidence; Week 8 begins the
inference, one editorial decision at a time.

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
