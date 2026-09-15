# Lesson 6.2 — Rule-Based Normalization: Building a Deterministic Script

*RELS 398 / ENGL 398 · Topic 6: Normalization · Meeting #15 (Wed Oct 7)*

***Step 2 of the three-step cycle: deterministic.** Today you implement yesterday's
orthographic policy as an executable rule set, run it over your text, and measure
its precision and recall against your manual decisions.*

---

## **01 Content**

**Formalizing a Policy**

Yesterday you wrote an orthographic policy in prose and applied it by hand. Today
you express it as a program.

The translation is harder than it sounds, and the difficulty is the point. Prose
policy tolerates imprecision: "regularize iotacism where the result is a standard
form" is a perfectly clear instruction to a human editor, who resolves the
unstated conditions by judgement without noticing that they were unstated. A
program has no judgement, so every condition must be explicit.

The consequence is that implementation *audits* the policy. Where you cannot write
a rule, one of three things is true: the policy is imprecise and needs sharpening;
the phenomenon genuinely requires contextual information a rule cannot access; or
you were applying an unstated criterion inconsistently. All three are worth
discovering, and only implementation discovers them.

The product is a verifiable baseline. Rule-based and distance-based methods provide
highly verifiable outputs: when a transducer maps a form to a normalized one, the
exact phonetic or graphemic rule applied is known, mathematically quantifiable, and
can be logged in the TEI header (Bollmann, 2019). That transparency is what makes
today's script the standard against which Friday's opaque method is checked.

**Vocabulary.** *Deterministic* — producing the same output for the same input, by
a stated procedure. *Finite-state transducer (FST)* — a formal machine mapping input
strings to output strings by state transitions. *Rule core* — a transformation
pattern derived from aligned historical and modern forms.

**Takeaway:** Implementing the policy audits it — every place you
cannot write a rule is imprecision, genuine context-dependence, or inconsistency.

---

## **02 Content**

**The Tradition: VARD, Norma, and Transducers**

Rule-based normalization has an established toolchain worth knowing, because your
script is a small instance of a well-developed method.

Early computational philology relied on substitution lists, dictionary lookups, and
rule-based finite-state transducers. Systems such as **VARD 2** for English and
**Norma** for German use hand-crafted or automatically derived context-aware
replacement rules, processing historical variants through character-replacement
transformations — historical *v* representing modern *u*, or ι mapping to ει
(Bollmann, 2019).

A finite-state transducer is the formal object underlying this. It reads an input
string character by character, moving between states, and emits output as it goes.
Because the machine's behaviour is entirely determined by its states and
transitions, its output is predictable and its reasoning inspectable.

| Approach | Mechanism | Suits |
| --- | --- | --- |
| Substitution list | Direct lookup: variant to standard | Known, enumerable variants |
| Character rewrite rules | Pattern substitution, optionally conditioned | Systematic phonological variation |
| Finite-state transducer | State machine over the input string | Complex conditioned rewriting |
| Weighted edit distance | Nearest lexicon entry under a cost model | Unseen variants |

Your script will combine the first, second, and fourth. A substitution list handles
forms you have enumerated; rewrite rules handle systematic patterns like iotacism;
and weighted edit distance proposes candidates for forms neither covers.

The important property they share is **inspectability**. For any output, you can
state which rule produced it. That is not true of the methods on Friday, and it is
the reason today's baseline is not simply a weaker alternative.

**Takeaway:** For any rule-based output you can state which rule
produced it — an inspectability that Friday's methods do not have.

---

## **03 Content**

**Rule Cores and Derived Rules**

Rules need not all be hand-written. They can be derived from aligned examples,
which is what the established systems do.

Deterministic systems generate **rule cores** from training data. Comparing a
historical variant against its modern equivalent generates transformation candidates
based on edit distance: aligning the two forms shows which characters changed, and
the change plus its context becomes a candidate rule. Those candidates are then
pruned by algorithms that select the most statistically useful (Bollmann, 2019).

You have training data: yesterday's manual normalizations are aligned pairs of
`<orig>` and `<reg>`.

```python
import re, unicodedata
from pathlib import Path
from collections import Counter

def pairs(path):
    """Extract (orig, reg) pairs from a TEI file."""
    xml = unicodedata.normalize("NFC", Path(path).read_text(encoding="utf-8"))
    out = []
    for m in re.finditer(
            r"<choice[^>]*>\s*<orig>(.*?)</orig>\s*<reg>(.*?)</reg>", xml, re.S):
        out.append((m.group(1).strip(), m.group(2).strip()))
    return out
```

From those pairs, derive the substitutions:

```python
def substitutions(orig, reg):
    """Character-level changes between two aligned forms, with context."""
    import difflib
    sm = difflib.SequenceMatcher(None, orig, reg)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != "equal":
            yield (orig[i1:i2], reg[j1:j2], orig[max(0, i1-1):i1])
```

Run this over your pairs and count. The frequent transformations are your rules; the
singletons are probably cases requiring individual treatment.

This is worth doing even though you already know your policy, because the derived
rules may not match the policy you thought you were applying. A discrepancy means
you applied something you did not state.

**Takeaway:** Derive rules from your own manual pairs — a
discrepancy with your stated policy means you were applying something unstated.

---

## **04 Content**

**Building the Substitution Layer**

Start with the simplest component: a direct lookup for forms you have enumerated.

```python
import json, unicodedata
from pathlib import Path

class Lexicon:
    """Known variant-to-standard mappings, plus a set of valid standard forms."""

    def __init__(self, mapping_path, standard_path):
        raw = json.loads(Path(mapping_path).read_text(encoding="utf-8"))
        self.mapping = {self._n(k): self._n(v) for k, v in raw.items()}
        self.standard = {
            self._n(w) for w in
            Path(standard_path).read_text(encoding="utf-8").split()
        }

    @staticmethod
    def _n(s):
        return unicodedata.normalize("NFC", s)

    def lookup(self, token):
        return self.mapping.get(self._n(token))

    def is_standard(self, token):
        return self._n(token) in self.standard
```

Two components, doing different jobs. The **mapping** holds variant-to-standard
pairs you have confirmed — populate it from yesterday's `<orig>`/`<reg>` pairs. The
**standard set** holds valid forms, and is what lets a rule check whether its output
is a real word.

Note the normalization applied at every boundary. A lexicon in NFD and text in NFC
will match nothing, and the failure is silent — the script simply finds no
candidates and reports that nothing needed normalizing, which looks like success.

Source your standard forms from a digital Greek corpus or lexicon. Without one, the
rule layer in the next section can generate candidates but cannot filter them, and
its precision will be poor.

Commit the lexicon files as data alongside the script.

**Takeaway:** The standard-form set is what lets a rule check its
own output — without it, rules generate candidates they cannot filter.

---

## **05 Content**

**Building the Rule Layer**

Now the systematic transformations. Express each rule as a pattern, a replacement,
and a condition.

```python
from dataclasses import dataclass
from typing import Callable, Optional
import re


@dataclass
class Rule:
    name: str
    pattern: str          # regex to match
    replacement: str      # what to substitute
    condition: Optional[Callable[[str, str], bool]] = None

    def apply(self, token, lexicon):
        """Yield (candidate, rule_name) for each position this rule matches."""
        for m in re.finditer(self.pattern, token):
            cand = token[:m.start()] + self.replacement + token[m.end():]
            if self.condition and not self.condition(token, cand):
                continue
            yield cand, self.name


def result_is_standard(lexicon):
    return lambda orig, cand: (lexicon.is_standard(cand)
                               and not lexicon.is_standard(orig))


IOTACISM_RULES = [
    Rule("ei-to-i",  "ει", "ι"),
    Rule("i-to-ei",  "ι",  "ει"),
    Rule("eta-to-i", "η",  "ι"),
    Rule("i-to-eta", "ι",  "η"),
    Rule("oi-to-y",  "οι", "υ"),
    Rule("y-to-oi",  "υ",  "οι"),
    Rule("ai-to-e",  "αι", "ε"),
    Rule("e-to-ai",  "ε",  "αι"),
]
```

The `condition` is what separates a usable rule from a destructive one. The
condition supplied above — the candidate is a standard form and the original is not
— encodes the reasoning you apply by hand: a non-standard form that becomes standard
under a phonologically motivated substitution is probably a phonetic spelling of
that standard form.

Note that each rule is *named*. That name is what makes the output auditable: for
every regularization the script proposes, it can report which rule fired, which is
exactly the transparency section 02 described.

**Takeaway:** Name every rule and require an explicit condition —
the name makes output auditable and the condition stops the rule being destructive.

---

## **06 Content**

**Rule Ordering and Interaction**

A complication you must handle deliberately, because handling it accidentally
produces silently wrong output.

Rules interact. Applying ει → ι and then ι → η in sequence produces a different
result from the reverse. Applying rules in one pass, taking the first match, gives a
different result from applying all rules and choosing among candidates.

| Strategy | Behaviour | Risk |
| --- | --- | --- |
| First rule that matches wins | Fast; order-dependent | Order encodes an unstated priority |
| Apply all rules; collect candidates | Order-independent | Must choose among candidates |
| Apply iteratively until stable | Handles chained changes | May not terminate; may over-apply |
| Apply once, single substitution only | Conservative | Misses forms needing two changes |

The recommended approach for this course is the second: generate all candidates from
all rules, then select. It is order-independent, which removes a hidden variable, and
it surfaces ambiguity rather than hiding it — if two rules produce two different
standard forms, you have found a case that requires contextual disambiguation, and
the script should say so rather than silently picking one.

```python
def candidates(token, rules, lexicon):
    """All standard-form candidates reachable by one rule application."""
    seen = {}
    for rule in rules:
        for cand, name in rule.apply(token, lexicon):
            seen.setdefault(cand, []).append(name)
    return seen        # {candidate: [rule names that produced it]}
```

A token yielding no candidates needs no normalization by these rules, or needs
something the rules do not cover. A token yielding exactly one candidate is a clean
case. A token yielding several is ambiguous, and section 12 addresses what to do
with it.

Report the counts of all three. The distribution tells you how much of your text the
rule method can actually decide.

**Takeaway:** Generate all candidates rather than taking the first
match — ambiguity then surfaces as multiple candidates instead of being hidden by
rule order.

---

## **07 Content**

**Weighted Edit Distance for Unseen Forms**

Rules handle the patterns you anticipated. For forms they miss, a distance-based
fallback proposes candidates.

The idea: find the standard forms nearest to the unknown token under an edit
distance, and propose the nearest. Plain Levenshtein — which you implemented in
Lesson 5.2 — treats all substitutions as equally costly, which is wrong here. A
substitution between two graphemes that had merged phonetically is far more likely
than one between unrelated letters.

A **context-sensitive weighted Levenshtein distance** encodes that (Bollmann, 2019).
Give phonologically motivated substitutions a low cost and others a high one:

```python
SUBSTITUTION_COST = {
    frozenset(("ι", "η")): 0.2,
    frozenset(("ι", "υ")): 0.3,
    frozenset(("ο", "ω")): 0.2,
    frozenset(("ε", "αι")): 0.2,
}
DEFAULT_COST = 1.0


def sub_cost(a, b):
    if a == b:
        return 0.0
    return SUBSTITUTION_COST.get(frozenset((a, b)), DEFAULT_COST)
```

Substituting the cost function into your Wagner–Fischer implementation yields a
distance in which phonetically plausible variants are close and implausible ones are
far. A threshold then decides whether the nearest standard form is close enough to
propose.

The weights are themselves an editorial statement about the phonology of your
manuscript's period, and they should be documented. Derive them from your own
observed substitution frequencies where you have enough data, and from the
phonological account in Lesson 6.1 section 02 otherwise.

Use this layer conservatively. It proposes candidates for forms your rules did not
recognize, and its proposals need review — it is a suggestion mechanism, not a
decision procedure.

**Takeaway:** Weight substitution costs by phonological
plausibility — the weights are an editorial claim about the period's phonology and
should be documented.

---

## **08 Content**

**Assembling the Script**

Combine the layers into a pipeline that processes a token and reports what it did
and why.

```python
def normalize_token(token, lexicon, rules, threshold=0.6):
    """Return (candidate, method, detail) or (None, 'unchanged', reason)."""
    if lexicon.is_standard(token):
        return None, "unchanged", "already standard"

    known = lexicon.lookup(token)
    if known:
        return known, "lexicon", "confirmed mapping"

    cands = candidates(token, rules, lexicon)
    if len(cands) == 1:
        cand, names = next(iter(cands.items()))
        return cand, "rule", ",".join(names)
    if len(cands) > 1:
        return None, "ambiguous", "; ".join(
            f"{c} ({','.join(n)})" for c, n in cands.items())

    near = nearest_standard(token, lexicon, threshold)
    if near:
        return near, "distance", f"weighted edit distance {near[1]:.2f}"

    return None, "unresolved", "no candidate"
```

Every return path carries a **method** and a **detail**. That is the design
requirement: the script must be able to say, for every token, what it decided and on
what basis. A script that returns only normalized text cannot be audited, and an
unauditable rule-based system has discarded its one advantage over the neural
methods.

Note that "ambiguous" returns no candidate. Where several rules propose different
standard forms, the script declines rather than choosing, and the case is routed to
human review. This is the correct behaviour: a rule-based system cannot resolve
syntactic ambiguity, since it processes tokens in isolation (Bollmann, 2019), and
guessing would trade a visible failure for an invisible error.

Save as `tools/normalize.py` and commit.

**Takeaway:** Every decision must carry its method and reason —
and where rules conflict, the script should decline rather than guess.

---

## **09 Content**

**Running It Over Your Text**

Apply the script to your diplomatic base — the consensus text *before* yesterday's
manual normalization — so that its output is comparable to what you did by hand.

```bash
git show gt-f42r-consensus:transcription/f42r_consensus.xml \
  > /tmp/diplomatic.xml
python3 tools/normalize.py --input /tmp/diplomatic.xml \
  --output normalization/script_output.json \
  --report normalization/script_report.md
```

The output should be structured data rather than modified XML at this stage. You
want a record of every decision, which is what the comparison in the next sections
consumes:

```json
{
  "token": "τιμι",
  "line": 7,
  "position": 4,
  "proposed": "τιμή",
  "method": "rule",
  "detail": "i-to-eta,i-to-ei"
}
```

Producing JSON rather than XML also keeps the script from touching your edition. The
script proposes; you dispose. Injecting proposals directly into the TEI would mix
machine and human decisions in a single state and destroy the comparison this week
depends on.

Report summary counts immediately:

| Category | Count |
| --- | --- |
| Tokens processed | Record |
| Already standard, unchanged | Record |
| Normalized by lexicon lookup | Record |
| Normalized by rule | Record |
| Normalized by distance | Record |
| Ambiguous, declined | Record |
| Unresolved, no candidate | Record |

**Takeaway:** Have the script emit structured proposals rather
than modified XML — mixing machine and human decisions in one state destroys the
comparison.

---

## **10 Content**

**Measuring Against Your Manual Work**

Now the evaluation, and it must run in both directions.

Retrieve yesterday's manual normalization and compare it against the script's
proposals, token by token.

| Case | Manual | Script | Classification |
| --- | --- | --- | --- |
| Both normalized, same result | Normalized | Same | True positive |
| Both normalized, different result | Normalized | Different | Wrong normalization |
| Manual normalized, script did not | Normalized | Unchanged | False negative (missed) |
| Script normalized, manual did not | Unchanged | Normalized | False positive (over-applied) |
| Neither normalized | Unchanged | Unchanged | True negative |
| Manual normalized, script declined | Normalized | Ambiguous | Correctly deferred |

From these, compute:

```text
Precision = true positives / (true positives + false positives + wrong)
Recall    = true positives / (true positives + false negatives + wrong)
```

**Precision** answers: when the script proposed a normalization, how often was it
right? **Recall** answers: of the normalizations you made, how many did the script
find?

The distinction is essential and was flagged in Lesson 6.1 section 21. A script with
high recall and low precision proposes many normalizations, most of them wrong, and
reviewing its output costs more than working by hand. A script with high precision
and low recall proposes few normalizations, nearly all correct, and leaves most of
the work undone — which is far more useful, because its output can be trusted and
the remainder handled manually.

Report both. A single accuracy figure conceals which failure mode you have.

**Takeaway:** High precision with low recall is useful; high
recall with low precision is worse than useless — a single accuracy figure hides
which you have.

---

## **11 Content**

**Interpreting the Failures**

Categorize the disagreements, because the categories tell you what to fix.

| Failure | Likely cause | Response |
| --- | --- | --- |
| Missed a form you normalized | No rule covers it | Add a rule, or add to the lexicon |
| Over-applied to a standard form | Condition too weak | Strengthen the condition |
| Over-applied to a proper name | No name exclusion | Add a name list or a capitalization check |
| Over-applied to a variant reading | Cannot distinguish these | Expected; exclude by hand |
| Wrong candidate among several | Ambiguity resolved wrongly | Should have declined; check the logic |
| Correctly declined an ambiguous case | Working as designed | Not a failure; count separately |
| Normalized a form you left as `<sic>` | Cannot distinguish variant from error | Expected limitation |

The last two rows are the important ones conceptually. A script that declines
ambiguous cases has behaved correctly, and counting those as failures understates
its usefulness — the whole point of the declining behaviour is to route hard cases
to a human. Report them separately.

And the `<sic>`/`<orig>` distinction from Lesson 6.1 section 06 is one a
character-level script structurally cannot make. Whether a form is period-normal
usage or a mechanical slip depends on knowing what was acceptable at the time, which
is not information in the string. A script will treat both alike, and that is a
limitation of the method rather than a defect in your implementation.

Note both explicitly in your report. Distinguishing "the script failed" from "the
method cannot do this" is the analytical work of today's evaluation.

**Takeaway:** Distinguish implementation failures from method
limitations — a script structurally cannot tell period-normal usage from a scribal
slip.

---

## **12 Content**

**Handling the Ambiguous Cases**

The cases where several rules proposed different standard forms are exactly the ones
Lesson 6.1 section 18 identified as requiring context.

Pure dictionary lookups and character-level regex fail to disambiguate because they
process tokens in isolation. If a historical spelling can map to several modern
lemmas depending on syntactic context, no character-level method resolves it
(Bollmann, 2019).

Compare the script's ambiguous list against the list you flagged yesterday:

| Comparison | Interpretation |
| --- | --- |
| Script's ambiguous set matches your flagged set | Your analysis was accurate |
| Script found ambiguities you missed | Cases you resolved by unconscious context |
| You flagged cases the script resolved cleanly | Your caution exceeded the actual ambiguity |
| Both sets differ substantially | Worth investigating; may indicate a rule fault |

The second row is the interesting one. If the script surfaces ambiguity at a token
you regularized without hesitation, you used contextual information without
noticing — which means the decision was less mechanical than your policy implies.
Those cases are worth documenting, because they mark where your editorial judgement
is doing work your stated rules do not capture.

That is not a criticism of the policy. It is a finding about the limits of
formalization, and it is the honest answer to the question of how much of editorial
practice can be made explicit.

Record the ambiguous set carefully. Friday's method claims to resolve exactly these,
and this set is the test.

**Takeaway:** Ambiguities the script finds where you hesitated not
at all mark where your judgement uses context your stated rules do not capture.

---

## **13 Content**

**Performance in Low-Resource Conditions**

An argument for the rule-based method that is easy to miss when comparing it against
neural approaches.

Rule-based systems excel in extremely low-resource environments. Research indicates
that the Norma tool achieves over 83% accuracy on English texts with as few as 100
tokens of training data (Bollmann, 2019).

That figure matters for your situation specifically. You have one folio of manual
normalization — a few hundred tokens at most. Neural methods trained on that would
have almost nothing to learn from; a rule-based system derived from it can perform
well, because rules generalize from few examples in a way that statistical models do
not.

| Training data available | Rule-based | Neural |
| --- | --- | --- |
| ~100 tokens | Effective | Not viable |
| ~5,000 tokens | Effective | Viable; multi-task learning helps |
| Large corpus | Effective; may plateau | Generally superior |

The middle row anticipates Friday. Data sparsity in historical corpora can be
mitigated by multi-task learning — training a sequence-to-sequence model
simultaneously on normalization and an auxiliary task, so that shared encoder layers
learn robust representations. But this helps most only when the target dataset is
exceptionally small, around 5,000 tokens; with abundant data, multi-task learning can
degrade performance through domain mismatch (Bollmann, 2019).

The general shape: rule-based methods are the appropriate technology at your scale,
and neural methods become preferable as data grows. For a term project on one
manuscript, today's method is not the primitive precursor to Friday's — it is
plausibly the better tool, and Friday will test that.

**Takeaway:** Rule-based systems reach 83% accuracy from 100
tokens — at your scale today's method may simply be the better tool, not the
primitive one.

---

## **14 Content**

**Iterating on the Rules**

Improve the script now, using the failure analysis from section 11.

Work in this order, because it addresses the most damaging failures first:

- **Fix over-applications.** These are false positives, and they are the failure that makes a script unusable. Strengthen conditions; add exclusions.
- **Add missing rules.** Cover patterns you normalized manually that no rule caught.
- **Extend the lexicon.** Add confirmed variant-to-standard pairs.
- **Tune the distance threshold.** A lower threshold means fewer, safer proposals.
- **Add exclusion lists.** Proper names, technical terms, and forms you deliberately leave alone.

After each change, re-run and re-measure. Keep a record of precision and recall
across iterations, because the trajectory is informative — and because it is easy to
improve recall while damaging precision without noticing.

| Iteration | Change | Precision | Recall |
| --- | --- | --- | --- |
| 1 | Initial rules | Record | Record |
| 2 | Added name exclusion | Record | Record |
| 3 | Strengthened conditions | Record | Record |
| 4 | Extended lexicon | Record | Record |

Guard against a specific trap: do not tune the script until it exactly reproduces
your manual decisions. That is fitting to a sample of one folio, and the resulting
rules will encode your particular choices rather than a general policy. The script
should implement your *policy*, and where it disagrees with a manual decision, the
first question is whether the manual decision was consistent with the policy.

Sometimes the script is right and you were not. Record those cases; they are
corrections to your text, and they are the most valuable thing today produces.

**Takeaway:** Do not tune until the script reproduces your
decisions exactly — where it disagrees, check whether your decision followed your own
policy.

---

## **15 Content**

**When the Script Is Right and You Were Not**

Expect this and treat it seriously. It is the most useful outcome of the exercise.

A deterministic script applies its rules uniformly. A human applies rules
inconsistently — differently when tired, differently at the start and end of a
session, differently when a form appears in a familiar phrase. Where the script
disagrees with your manual work, a real possibility is that you were inconsistent.

Diagnose by checking whether the same phenomenon was handled the same way
throughout:

```python
from collections import defaultdict

by_pattern = defaultdict(list)
for orig, reg in pairs("edition/edition.xml"):
    for src, dst, ctx in substitutions(orig, reg):
        by_pattern[(src, dst)].append((orig, reg))

for (src, dst), examples in sorted(by_pattern.items()):
    print(f"{src} -> {dst}: {len(examples)} instances")
```

Then look for the same source pattern left unnormalized elsewhere in the text. If ι
→ η was applied eleven times and there are three further tokens where it would apply
and was not, those three are inconsistencies rather than deliberate exceptions —
unless you documented them as exceptions, which is precisely what the decision log
is for.

Correct them, and commit the correction separately with an explanatory message:

```text
fix(normalization): regularize three iotacism instances missed manually

Script comparison surfaced three tokens at lines 9, 16, 21 where the
i-to-eta rule applies and manual normalization did not fire. Checked
against the facsimile; all three are the same phonetic spelling
regularized elsewhere. No documented exception applies.

Human-Verified: true
```

This is the deterministic step improving the manual step, which is worth noticing:
the three-step cycle is not a ranking with the human at the top.

**Takeaway:** The script's uniformity catches your inconsistency —
the deterministic step improves the manual one, not only the reverse.

---

## **16 Content**

**Projecting the Results into TEI**

Once the script's proposals are reviewed, inject the accepted ones into the edition
with their provenance recorded.

```xml
<choice resp="#script" cert="high">
  <orig>τιμι</orig>
  <reg>τιμή</reg>
</choice>
```

The `@resp` pointing at the script rather than at you is the essential detail. A
future researcher must know precisely whether a given `<reg>` was generated by a
human philologist, a deterministic transducer, or a neural network, because that
provenance determines the data's reliability for downstream corpus linguistics (TEI
Consortium, 2026).

Declare the script as a responsible agent in the header:

```xml
<respStmt xml:id="script">
  <resp>Automated orthographic regularization</resp>
  <name>tools/normalize.py, rule set v3, commit 7d2e814</name>
</respStmt>
```

Naming the commit is what makes the attribution meaningful. "Generated by a script"
is not reproducible; "generated by `tools/normalize.py` at commit 7d2e814 with rule
set v3" identifies the exact procedure, which anyone can retrieve and re-run.

Record the rule that fired, where it is useful to do so — a `@source` attribute or a
note can carry the rule name, which turns the edition into a record of not just what
was normalized but why.

Do not inject proposals you have not reviewed. A `<reg>` in your edition is a claim
you are making, whatever produced it, and attributing it to the script does not
transfer the responsibility.

**Takeaway:** Attribute machine regularizations to a named script
at a named commit — "generated by a script" is not reproducible attribution.

---

## **17 Content**

**Logging the Method in the Header**

Extend yesterday's `<editorialDecl>` to record the automated stage.

```xml
<encodingDesc>
  <editorialDecl>
    <normalization method="markup">
      <p>Orthographic regularization proceeded in two stages. Manual
        regularization of f. 42r established the policy documented in
        transcription/ORTHOGRAPHY.md. A deterministic rule-based script
        (tools/normalize.py, rule set v3) was then applied to the
        diplomatic text; its proposals were reviewed individually and
        accepted proposals are attributed @resp="#script". The script
        declines tokens for which several rules propose different
        standard forms; those cases were resolved manually.</p>
      <p>Script precision against manual regularization: 0.94.
        Recall: 0.81. Measured on f. 42r, 312 tokens.</p>
    </normalization>
  </editorialDecl>
</encodingDesc>
```

Including the measured performance in the header is unusual and worth doing. It
tells a reader how reliable the automated layer is, which is information they cannot
obtain any other way and which bears directly on how much weight to place on the
`<reg>` layer.

This is the same principle as the imaging provenance in Lesson 3.2 and the AI
trailers in Lesson 1.1. Machine-produced content in a scholarly edition needs its
production conditions recorded, because the reader's ability to evaluate the content
depends on knowing them.

Commit the header change with the script output.

**Takeaway:** Record the script's measured precision and recall in
the header — a reader cannot otherwise judge how much weight the `<reg>` layer bears.

---

## **18 Content**

**What the Script Cannot Do**

State the limits explicitly, because Friday's method claims to address exactly them.

| Limitation | Reason | Friday's claim |
| --- | --- | --- |
| Syntactic disambiguation | Processes tokens in isolation | Attention over the whole sentence |
| Distinguishing variant from error | Requires period knowledge, not string information | Contextual and world knowledge |
| Unseen variation types | Only applies rules it was given | Generalizes from training |
| Morphological analysis | Character-level only | Some morphological capability |
| Semantic plausibility | No model of meaning | Language model |

The first row is the fundamental one. A rule-based system cannot resolve a variant
that maps to several standard forms depending on syntax, because the information
required is not in the token (Bollmann, 2019). Your ambiguous set is the concrete
instance of this, and it is the test case for Friday.

The third row is the practical one. Your rules cover the patterns you observed on
one folio. A different folio, a different hand, or a different section of the
manuscript may present variation your rules do not anticipate, and the script will
silently leave those forms unnormalized. Recall measured on the folio you derived
the rules from is optimistic — it is measured on the training data.

If you have time, test on a second folio you did not derive rules from. The drop in
recall between the two is a measure of how well your rules generalize, and it is a
more honest figure than the one from the folio the rules came from.

**Takeaway:** Recall measured on the folio the rules came from is
optimistic — test on a folio you did not use, and report the drop.

---

## **19 Content**

**Preparing the Friday Comparison**

Friday runs AI-assisted normalization and checks it against your rules. Structure
today's output so that comparison is straightforward.

Produce a per-token record covering all three sources:

| Field | Source |
| --- | --- |
| Token | The diplomatic text |
| Line and position | The diplomatic text |
| Manual decision | Lesson 6.1 |
| Manual reasoning | The decision log |
| Script proposal | Today |
| Script method and rule | Today |
| Script confidence or distance | Today |
| Flagged ambiguous | Today and Lesson 6.1 |

Save as `normalization/comparison.json`. On Friday you add the AI proposal as a
further column, and the three-way comparison assembles itself.

Tag today's state:

```bash
git tag -a norm-script-w6 -m "Rule-based normalization output, rule set v3"
git push --tags
```

Also record today's costs, as in previous weeks: time to write the script, time to
iterate, and time to review its proposals. Friday's method requires almost no setup,
and the comparison must weigh that against quality.

**Takeaway:** Build the per-token comparison table today so
Friday's AI proposals become a column rather than a new analysis.

---

## **20 Content**

**Checklist Before You Leave**

Verify each.

- Rules derived from your manual pairs and compared against your stated policy.
- Lexicon and standard-form set built and NFC-normalized.
- Rules implemented with explicit named conditions.
- All candidates generated rather than first-match.
- Ambiguous cases declined rather than guessed.
- Weighted edit distance implemented, with weights documented.
- Every decision carries a method and a reason.
- Script run over the diplomatic base, not the normalized text.
- Output emitted as structured data, not injected XML.
- Precision and recall computed in both directions.
- Failures categorized; method limits distinguished from implementation faults.
- Ambiguous set compared against yesterday's flagged set.
- Rules iterated, with performance recorded per iteration.
- Inconsistencies in your manual work identified and corrected.
- Accepted proposals injected with `@resp="#script"`.
- Header `<editorialDecl>` updated with method and measured performance.
- Script, rules, and lexicon committed.
- State tagged and pushed.
- Costs recorded.

**Takeaway:** Run the script against the diplomatic base rather
than the normalized text, or you measure it against its own target.

---

## **21 Content**

**Common Problems Today**

Failures that recur.

| Symptom | Cause | Remedy |
| --- | --- | --- |
| Script proposes nothing | Lexicon and text in different normalization forms | NFC everywhere |
| Script normalizes everything | Condition missing or too weak | Require the result to be standard and the original not |
| Precision high, recall near zero | Conditions too strict; lexicon too small | Loosen carefully; extend the lexicon |
| Recall high, precision poor | Over-application | Add exclusions; strengthen conditions |
| Proper names normalized | No name handling | Add an exclusion list |
| Results differ between runs | Rule order dependence, or a set iteration | Generate all candidates; sort deterministically |
| Script "fixes" a `<sic>` form | Cannot distinguish error from variant | Expected; exclude by hand |
| Perfect agreement with manual work | Rules over-fitted to this folio | Test on a second folio |

The first row is the one that wastes the most time and looks least like an error. A
script that proposes nothing reports that the text needs no normalization, which is
indistinguishable from success if you do not check. Test with a token you know is
non-standard before trusting a clean run.

The last row is the subtler trap. A script that reproduces your manual decisions
exactly has probably been tuned until it did, which means it has learned your folio
rather than your policy. Perfect agreement is a warning sign rather than a success
criterion.

**Takeaway:** A script proposing nothing looks identical to a text
needing nothing — test with a known non-standard token before trusting a clean run.

---

## **22 Content**

**What Good Work Looks Like Here**

The standard.

A minimally acceptable result is a working script that proposes normalizations.

Good work additionally:

- Derives rules from the manual pairs and reports discrepancies with the stated policy.
- Gives every rule an explicit, documented condition.
- Generates all candidates and declines on ambiguity rather than guessing.
- Emits a method and a reason for every decision.
- Measures precision and recall separately.
- Categorizes failures and separates method limits from implementation faults.
- Reports correctly-declined cases separately from failures.
- Identifies inconsistencies in the manual work and corrects them.
- Documents the distance weights as a phonological claim.
- Tests generalization on a folio the rules were not derived from.
- Records measured performance in the TEI header.

The eighth item is the one that most distinguishes a genuine evaluation from a
demonstration. A student who reports that the script agreed with them 94% of the
time has compared two things. A student who reports that the script surfaced three
places where their manual work was inconsistent with their own stated policy, and
corrected them, has used the comparison to improve the edition.

**Takeaway:** Using the comparison to correct your own
inconsistencies is what makes it an evaluation rather than a demonstration.

---

## **23 Content**

**The Transparency Argument**

A conceptual point to carry into Friday.

Today's method has a property the neural methods do not: for any output, the exact
transformation applied is known, mathematically quantifiable, and loggable in the
TEI header (Bollmann, 2019).

That is not a minor engineering convenience. It determines whether the normalized
layer of your edition is *evidence* or *assertion*.

Consider a reader encountering `<reg>τιμή</reg>` for `<orig>τιμι</orig>`. If the
edition can say this was produced by the rule ι → η, conditioned on the result being
attested and the original not, then the reader can evaluate the claim: they can
check the rule, check the condition, and disagree if they think the analysis wrong.
If the edition can only say a model produced it, the reader must either trust the
model or redo the work.

| Method | Reader can | Reader must |
| --- | --- | --- |
| Rule-based | Inspect the rule and its condition | Nothing |
| Neural | Inspect the training data, at best | Trust, or redo |
| Language model | Inspect the prompt | Trust, or redo |

An edition is an argument, and an argument whose steps cannot be inspected is a
weaker argument regardless of whether its conclusions are correct. That is the case
for the deterministic baseline, and it holds even where the neural method is more
accurate.

Friday will likely show the AI method resolving cases your rules could not. Hold
this alongside that result: greater capability and lesser accountability, and the
edition has to decide which it needs where.

**Takeaway:** A rule-based `<reg>` is a claim the reader can
check; a neural one is a claim they must trust — which matters independently of
accuracy.

---

## **24 Content**

**The Hybrid Position**

Where the literature actually lands, which is not "rules good, neural bad."

Modern computational philology pipelines propose a **hybrid** approach: constrained,
rule-based transducers for deterministic stem and affix normalization, and language
models purely for contextual disambiguation and lacuna detection (Bollmann, 2019).

The division of labour follows the capabilities:

| Task | Best method | Why |
| --- | --- | --- |
| Systematic phonological substitution | Rule-based | Deterministic, verifiable, sufficient |
| Known variant lookup | Lexicon | Exact |
| Unseen variant proposal | Weighted distance | Generalizes without training |
| Syntactic disambiguation | Contextual model | Requires sentence-level information |
| Lacuna detection | Contextual model | Requires expectation about what should be there |
| Deciding variant against error | Human | Requires period knowledge and judgement |

The Old Hungarian case from Lesson 6.1 section 19 is the worked example: a neural
recognizer read the manuscript, a rule-based transducer reconstructed stem and
suffix assimilation deterministically, and a noisy channel model ranked candidates —
each component doing what it does best (Bollmann, 2019).

Note the last row. No row assigns the `<orig>`/`<sic>` decision to a machine, and the
reason is the one from Lesson 6.1: that decision is a claim about what was
acceptable in a historical context, which is editorial judgement rather than pattern
recognition.

Friday should be approached in this spirit. The question is not whether the AI
method beats your script, but which parts of the task each should handle.

**Takeaway:** The literature's position is hybrid — rules for
deterministic substitution, models for context, humans for the variant-versus-error
judgement.

---

## **25 Content**

**Preparing for Friday**

Bring:

- The script, rules, and lexicon, committed and tagged.
- The per-token comparison table.
- Precision and recall figures, with the failure categorization.
- The ambiguous set — the test cases for Friday.
- The generalization figure from a second folio, if you produced one.
- The corrections the script prompted in your manual work.
- Costs recorded.

Friday applies AI-assisted normalization and checks it against your rules. The
specific things to test:

- Does it resolve the ambiguous cases correctly?
- Does it over-normalize — collapsing dialectal variants or replacing archaic lexemes with modern synonyms?
- Does it respect the `<orig>`/`<sic>` distinction, or treat all variation alike?
- Does it leave proper names alone?
- Can it produce valid TEI `<choice>` markup directly?

The second item is the documented danger and the one to look for hardest. When
language models process texts with fluid orthography, they frequently collapse
historically significant dialectal variants into a single standard form, permanently
erasing linguistic evidence (Bollmann, 2019). Your rule baseline is what detects
this: a script performing only character-level substitution will flag a large
morphological deviation where the model has crossed from orthographic regularization
into semantic alteration.

That detection mechanism is the concrete payoff of today's work, and it is worth
knowing you have built it.

**Takeaway:** Your rule baseline is the detector for Friday's
over-normalization — a large deviation from character-level substitution marks where
the model altered meaning.

---

## **26 Content**

**Synthesis: The Verifiable Baseline**

What today established.

A deterministic script is a formal statement of an editorial policy. Writing it
forces the policy to be precise, and the forcing is valuable independently of the
script — it exposes unstated conditions, inconsistent application, and cases where
judgement was doing work the policy did not describe.

The script's output is verifiable in a way no other method's is. Every proposal
carries the rule that produced it and the condition that licensed it, and both can
be inspected, logged in the TEI header, and disagreed with (Bollmann, 2019).

Its limits are structural rather than incidental. It processes tokens in isolation,
so it cannot resolve syntactic ambiguity. It applies rules it was given, so it does
not generalize to unseen variation. And it has no access to what was acceptable in a
historical context, so it cannot distinguish period-normal usage from scribal error
(Bollmann, 2019).

Within those limits it performs well at small scale — rule-based systems reaching
83% accuracy on 100 tokens of training data — which is the scale you are actually
working at (Bollmann, 2019).

It also improved your manual work, by surfacing inconsistencies that uniform
application makes visible and human application conceals. That direction of benefit
is worth remembering: the three-step cycle is a comparison among methods, not a
ranking with the human at the top.

**For Friday.** Bring the seven items in section 25, especially the ambiguous set.
Friday tests whether contextual methods resolve what rules cannot, and whether they
cost more in fidelity than they return in coverage.

**Takeaway:** The script's value is a verifiable baseline and an
audit of your own consistency — not merely automation of what you already did.

---

## **27 Content**

**A Note on Reproducibility**

One further property of today's method worth stating.

Your script, its rules, its lexicon, and its weights are all committed. Anyone with
your repository can run it and obtain identical output. That is reproducibility in
the strict sense, and it is rare in computational scholarship.

Friday's method will not have it. A hosted model may change without notice, as
Lesson 4.3 section 16 established; the same prompt on the same image may produce
different output next month; and even where the model is fixed, sampling makes the
output non-deterministic unless temperature is set to zero and even then not
reliably across versions.

| Property | Rule script | Hosted model |
| --- | --- | --- |
| Same input, same output | Guaranteed | Not guaranteed |
| Procedure inspectable | Fully | Not at all |
| Runnable in ten years | If Python runs | Only if the service exists |
| Auditable by a third party | Yes | Only the prompt |

The third row is the one that matters for a scholarly edition with any expected
lifespan. A `<reg>` produced by your script can be re-derived from your repository
indefinitely. A `<reg>` produced by a hosted model in October 2026 may be
underivable by 2030, which means the edition contains claims whose basis has
evaporated.

This is a strong argument for the hybrid position in section 24: use models where
their capability is needed, and prefer the reproducible method where it suffices.
And record the provenance either way, so a later reader knows which they are looking
at.

**Takeaway:** Your script's output can be re-derived indefinitely;
a hosted model's cannot — which means claims resting on it may become underivable.

---

## **28 Content**

**Extending Beyond the Folio**

A practical note for the rest of the term.

Your rules were derived from one folio and measured on it. To use the script across
your whole passage:

- Run it on the remaining folios.
- Review every proposal, at least initially.
- Add newly encountered variation to the rules and lexicon.
- Re-measure periodically on a folio you have normalized by hand.
- Record the version of the rule set used for each folio.

The last item matters because the rule set will change as you extend it. A folio
normalized with rule set v3 and one normalized with v7 have been treated
differently, and if the difference is not recorded the edition is inconsistent in a
way nobody can detect. Record the rule set version in the commit for each batch.

The review requirement is the expensive part and should not be dropped. Precision
measured on one folio is an estimate, and precision on new material is unknown until
measured — the generalization caution from section 18. Reviewing every proposal is
the safe practice until you have evidence that the script's precision holds on
unseen text.

As confidence grows, you can review selectively: all proposals from the distance
layer, which is the least reliable, and a sample from the rule layer. State in the
header what review practice was applied to which folios.

**Takeaway:** Record which rule set version normalized each folio
— otherwise the edition is inconsistent in a way nobody can detect.

---

## **29 Content**

**What This Week Is Actually Testing**

Step back to the week's structure, now that two of its three steps are done.

Week 4 compared three methods on a *reading* task: what does the ink say?
Week 6 compares three methods on a *judgement* task: how should this variation be
treated?

The difference is worth noticing. Reading has a fact of the matter — the ink is what
it is, and a transcription is right or wrong about it. Normalization does not, in
the same way. Whether τιμι should be regularized to τιμή, left alone, or marked as
an error is an editorial decision governed by a policy, and the policy is chosen
rather than discovered.

This changes what "accuracy" means. Today's precision and recall measure agreement
with *your* decisions, which are the standard only because you set the policy. A
different editor with a different policy would produce different figures for the
same script, and neither set would be wrong.

| Task | Standard | "Accuracy" means |
| --- | --- | --- |
| Transcription | The ink | Correspondence to the document |
| Normalization | The stated policy | Consistency with a chosen standard |
| Collation (Week 7) | The witnesses | Correspondence, given an alignment policy |
| Apparatus (Week 8) | Editorial judgement | Consistency with a stated method |

Read down the right-hand column. The course moves progressively from tasks with a
fact of the matter toward tasks governed by stated policy — which is why the
documentation requirement intensifies as the term proceeds. Where there is no
external fact to appeal to, the stated policy *is* the standard, and an unstated
policy leaves nothing to evaluate against.

**Takeaway:** Normalization has no fact of the matter, so the
stated policy is the standard — which is why documentation matters more here than in
transcription.

---

## **30 Content**

**Synthesis: Rules as Explicit Editorial Practice**

The argument of this meeting, in its own terms.

Editorial practice is a set of decisions applied repeatedly. When applied by a
person those decisions are partly tacit: an editor knows what to do without always
being able to say why, and applies criteria they have not articulated. That tacit
component is real expertise, and it is also where inconsistency lives.

Writing the script makes the practice explicit. Every condition must be stated,
every exception enumerated, every ordering decided. What survives that process is a
policy; what does not survive is either genuine context-dependence — the ambiguous
set — or inconsistency you did not know you had.

The result is a baseline that is verifiable, reproducible, and inspectable, which is
what a scholarly edition needs from its automated components (Bollmann, 2019). And
it performs well at the scale you are working at, which is small.

It cannot do everything. Syntactic ambiguity, unseen variation, and the judgement
between period-normal usage and scribal error are outside its reach, structurally.
Friday tests whether contextual methods reach them, and at what cost in fidelity and
accountability.

**For Friday.** Bring the seven items in section 25. The ambiguous set is the test
case, and your rule baseline is the detector for over-normalization.

**Takeaway:** Writing the rules made your tacit editorial practice
explicit — what survived is policy, and what did not is either genuine
context-dependence or inconsistency you did not know about.

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
