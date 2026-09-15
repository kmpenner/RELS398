# Lesson 7.1 — Collating Two Witnesses by Hand

*RELS 398 / ENGL 398 · Topic 7: Collation · Meeting #17 (Tue Oct 20)*

***Step 1 of the three-step cycle: manual.** Today you collate two witnesses on
paper, building a variant taxonomy and a record of every difference. That record
is the reference for Wednesday's CollateX alignment and Friday's AI
classification.*

---

## **01 Content**

**What Collation Is For**

Collation is the systematic comparison of witnesses to record where they differ. It
is the operation at the centre of textual criticism, and everything the discipline
does with manuscript evidence depends on it.

The purpose is not to catalogue differences for their own sake. Differences are
evidence about *transmission* — about which manuscript was copied from which, which
readings are original and which are corruptions, and how the text moved through
time. A shared error between two witnesses suggests they share an ancestor. A long
omission in one suggests a specific scribal event. The collation is the dataset from
which those inferences are drawn.

For most of the discipline's history this was done exactly as you will do it today:
by eye, on paper, one variant at a time. John Manly and Edith Rickert's edition of
Chaucer's *Canterbury Tales* relied on a manual procedure involving thousands of
physical index cards, one for each variant site — the lemma from the base text
copied at the top, followed by the variants across all witnesses and notations of
missing lines (Robinson & Driscoll, 2016).

That is the method you are learning, and its limits are what motivate Wednesday.
The *Siete Partidas* tradition comprises roughly 100 witnesses and over 11 million
words, at which scale manual collation is practically insurmountable and highly
susceptible to fatigue-induced error (Fradejas Rueda, 2022).

**Vocabulary.** *Collation* — systematic comparison of witnesses to record
differences. *Witness* — a surviving manuscript or edition attesting a text.
*Variant site* — a point at which witnesses differ. *Lemma* — the reading adopted in
the base text at a variant site.

**Takeaway:** Collation records differences because differences
are evidence about transmission — not for their own sake.

---

## **02 Content**

**The Base Text Problem**

Before comparing anything, a methodological decision must be made, and it has
consequences you should understand before making it.

The traditional approach compares each witness against a single **base text**,
recording where each deviates. It is straightforward, it produces a readable
apparatus, and it was the only feasible method by hand.

It also carries a genealogical bias. Early computational programs relied on
base-text or pairwise methodology, comparing witnesses one by one against a master
text; while efficient for simple traditions, the choice of base text arbitrarily
dictates the structure of the collation results and fails to map the fluid nature of
manuscript transmission, where texts merge, diverge, and overlap (Robinson &
Driscoll, 2016).

The mechanism of the bias: differences are recorded *as deviations from the base*,
so the base's readings are structurally privileged as the norm and other witnesses
appear as departures from it. If the base happens to be a poor witness, the
apparatus records the good witnesses' correct readings as variants from a corrupt
norm.

| Approach | Records | Bias |
| --- | --- | --- |
| Base text | Deviations from one chosen witness | Privileges the base's readings |
| Pairwise | Each pair compared separately | No single privilege; combinatorially expensive |
| Multiple alignment | All witnesses against an emerging consensus | Minimal; requires computation |

Wednesday's tool uses the third approach — CollateX aligns witnesses progressively
against an accumulated variant graph rather than against a single historical
witness, eliminating base-text bias (Haentjens Dekker & Middell, 2011).

Today you have two witnesses and will use a base text, because with two witnesses
the distinction largely collapses. Understand that you are making a choice, record
which witness you chose as base, and note that Wednesday's method does not require
one.

**Takeaway:** A base text privileges one witness's readings as the
norm — with two witnesses this barely matters, and Wednesday's method avoids it
entirely.

---

## **03 Content**

**Which Layer to Collate**

The decision flagged at the end of Week 6, now due.

Your witnesses have two layers: `<orig>`, recording what each scribe wrote, and
`<reg>`, recording the regularized form. Collating on one produces a different
result from collating on the other.

| Collate on | Reports as variants | Suppresses | Suited to |
| --- | --- | --- | --- |
| `<orig>` | Every orthographic difference | Nothing | Studying scribal practice and orthography |
| `<reg>` | Substantive differences only | Orthographic variation | Establishing the text; the main apparatus |

Collating unnormalized text produces noise. When aligning un-normalized medieval
texts, deterministic algorithms fragment the alignment entirely, producing highly
disjointed graphs saturated with non-genealogical noise (Haentjens Dekker &
Middell, 2011). The same is true by hand: an apparatus recording every iotacism
difference between two witnesses buries the substantive variants under hundreds of
spelling differences.

But suppressing orthography discards evidence. Shared orthographic practice between
two witnesses can indicate shared descent, and a study of the scribes' spelling is a
legitimate scholarly object — as Lesson 6.1 established, the variation is data
(Gignac, 1976).

The standard practice is to do both, separately: collate on `<reg>` for the main
apparatus recording substantive variants, and analyze `<orig>` differences
separately as evidence about transmission and scribal habit.

Decide today, record the decision, and apply it consistently. Wednesday's tool will
require the same decision expressed as a configuration, and Friday's model will need
to be told which you are asking about.

**Takeaway:** Collate on `<reg>` for the substantive apparatus and
analyze `<orig>` separately — one collation cannot serve both purposes.

---

## **04 Content**

**Preparing the Witnesses**

Set up before comparing. The preparation determines whether the comparison is
tractable.

- Both witnesses transcribed for the same passage, line-aligned to their own facsimiles.
- Both validated against the TEI schema.
- Both NFC-normalized.
- Both with the layer you chose extracted to plain text.
- Line and folio references retained, so every variant can be located in both.

Extracting the collation layer:

```python
import re, unicodedata
from pathlib import Path

def layer(path, which="reg"):
    """Extract the <reg> or <orig> layer as a token list with references."""
    xml = unicodedata.normalize("NFC", Path(path).read_text(encoding="utf-8"))
    body = re.search(r"<body>(.*?)</body>", xml, re.S).group(1)
    other = "orig" if which == "reg" else "reg"
    body = re.sub(rf"<{other}>.*?</{other}>", "", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    return unicodedata.normalize("NFC", body).split()
```

Note what the function does with `<choice>`: it removes the layer you are *not*
collating, then strips remaining markup. Failing to remove the other layer
concatenates both, producing tokens like `τιμιτιμή` that match nothing — the same
trap as Lesson 5.2 section 26.

Print both witnesses' extracted text with line numbers, on paper, in two columns or
on facing sheets. Today is deliberately a paper exercise, and the reason is in the
next section.

If you have only transcribed one witness, transcribe at least twenty lines of the
second now. Collation requires two.

**Takeaway:** Remove the layer you are not collating before
stripping markup, or every `<choice>` produces a token that matches nothing.

---

## **05 Content**

**Why Today Is on Paper**

The manual step in previous weeks used a computer. Today deliberately does not, and
the reason is methodological rather than nostalgic.

Manual collation relies heavily on the scholar's implicit, internalized knowledge. A
human editor processes orthographic variation instantly, recognizing effortlessly
that two spellings represent the same lexical unit, and discards the insignificant
difference without formally recording the logic behind the decision (Haentjens
Dekker & Middell, 2011).

That effortlessness is the thing to notice. You will make dozens of judgements today
without registering them as judgements — deciding that a difference does not matter,
that two forms are the same word, that a variation is orthographic rather than
substantive. Every one of those is a decision an algorithm would have to be told how
to make.

Working on paper slows the process enough that the decisions become visible. That is
today's real product: not the list of variants, but the record of what you decided
and on what basis, which is what Wednesday must be told explicitly.

Automated collation forces the editor to make normalization rules explicit *before*
alignment begins, shifting the critical philological labour away from the physical
act of reading and comparing and toward data modelling and algorithm configuration
(Fradejas Rueda, 2022). Today is where you discover what those rules are, by
catching yourself applying them.

Keep a second sheet beside the collation for exactly this. Every time you decide a
difference does not count, write down why.

**Takeaway:** You will make dozens of tacit judgements today — the
record of them, not the variant list, is what Wednesday needs.

---

## **06 Content**

**The Collation Procedure**

Work systematically. Ad-hoc comparison misses variants and produces an incomplete
record.

- Set the two texts side by side, aligned at the start of the passage.
- Read in parallel, word by word, not sentence by sentence.
- At each difference, stop and record it before continuing.
- Note the line and word position in *both* witnesses.
- Record both readings verbatim.
- Classify the variant type.
- Note anything about the surrounding context that bears on the difference.
- Re-establish alignment before continuing.

The last item is the procedural difficulty. After an omission or an addition the two
texts are out of step, and you must find where they resynchronize. This is exactly
the problem the alignment algorithms in Wednesday's lesson solve mathematically, and
doing it by hand is what makes the algorithm's job intelligible.

Record on a structured sheet:

| Field | Example |
| --- | --- |
| Variant number | 7 |
| Witness A reading | ἐγένετο |
| Witness A location | f. 42r, line 8, word 4 |
| Witness B reading | ἐγένοντο |
| Witness B location | f. 17v, line 12, word 4 |
| Type | Morphological |
| Note | A agrees with the singular in line 7; B with the compound subject |

Manly and Rickert used one card per variant site, and the practice is sound — a card
or a row per variant keeps each one separable and reorderable, which matters when
you later group variants by type.

**Takeaway:** Re-establishing alignment after an omission is the
hard part by hand — and it is exactly what Wednesday's algorithm computes.

---

## **07 Content**

**The Variant Taxonomy**

Classifying variants is the analytical core of collation. Algorithmic output is
agnostic — it contains all deviations regardless of importance — and the human
editor must classify them to determine stemmatic relevance (Nury & Spadini, 2020).

Five tiers, in ascending order of genealogical value:

| Tier | Description | Stemmatic value |
| --- | --- | --- |
| Orthographic / graphematic | Spelling variation | Generally polygenetic; limited value |
| Morphological | Word form: number, tense, case | Moderate; may reveal regional habit or updating |
| Lexical substitution | One word replaced by another | High; shared substitution indicates shared exemplar |
| Omission / *homoioteleuton* | Missing blocks of text | Very high; long omissions strongly indicate descent |
| Transposition | Text moved to a different location | High; indicates deliberate intervention or misarranged folios |

The reasoning behind the ranking is worth understanding rather than memorizing.

**Orthographic** variants are of limited genealogical value because they are
*polygenetic* — two scribes can independently produce the same spelling variant,
since both are writing the same language in the same period under the same
phonological conditions. Shared orthography is therefore weak evidence of shared
descent.

**Omissions** are at the other extreme. A long, inexplicable omission is unlikely to
arise twice independently, so two witnesses sharing one very probably share an
ancestor in which it occurred (Gotoh, 1982, as applied in Haentjens Dekker &
Middell, 2011).

**Lexical substitution** is high-value for the same reason: replacing one word with
a different word is a specific event, and its independent recurrence is improbable.

Classify every variant as you record it. Reclassifying later means rereading.

**Takeaway:** Orthographic variants are weak evidence because two
scribes can produce them independently; long omissions are strong evidence because
they cannot.

---

## **08 Content**

***Homoioteleuton* and Mechanical Omission**

The most evidentially valuable variant type has a specific and identifiable
mechanism worth recognizing.

***Homoioteleuton*** — "similar ending" — is a copying error in which a scribe's eye
skips from one word ending to an identical or similar ending further down the page,
omitting everything between. The related *homoioarcton* involves similar beginnings.

The mechanism explains why omissions cluster where they do. A scribe copying looks
at the exemplar, holds a phrase in memory, writes it, and looks back to find their
place. If two similar sequences occur nearby, the eye may return to the second
rather than the first, and the intervening text is lost — in a single cognitive
event rather than as a series of decisions.

| Feature | Suggests |
| --- | --- |
| Omitted text bounded by identical or similar words | *Homoioteleuton*; a mechanical skip |
| Omission begins and ends mid-sentence | Mechanical rather than deliberate |
| Omitted text is exactly one line of the exemplar | Line-skip; tells you about the exemplar's layout |
| Omitted text is a coherent unit | Possibly deliberate; check for doctrinal or editorial motive |
| Omission leaves ungrammatical text | Mechanical; the scribe did not notice |

The third row is a genuinely useful inference. If an omission corresponds exactly to
one line of text, the exemplar's line length can be estimated — which is evidence
about a manuscript that may no longer exist.

This mechanism also matters for Wednesday. Gotoh's affine gap penalties exist
precisely to model it: a linear gap penalty treats a ten-word gap as ten independent
omissions, whereas the affine model applies a heavy penalty for opening a gap and a
small one for extending it, computing the omission of a ten-word phrase as a single
extended cognitive event rather than ten isolated decisions (Gotoh, 1982).

When you find an omission today, check its boundaries for similar endings and record
what you find.

**Takeaway:** Check every omission's boundaries for similar
endings — *homoioteleuton* is a single cognitive event, which is why Wednesday's
algorithm penalizes gap opening rather than gap length.

---

## **09 Content**

**Transpositions**

The variant type that will cause the most trouble on Wednesday, and which you should
identify carefully today.

A **transposition** is text moved from one location to a substantially different
one. It is not a substitution, since the words are the same; it is not an omission
plus an addition, though that is how an algorithm will see it.

Transpositions pose a severe mathematical challenge. Because the variant graph must
remain acyclic to preserve linear reading order, mapping a transposition by drawing
an edge backward to an earlier section would create a forbidden cycle, and an
algorithm traversing a cyclic graph would loop infinitely (Schmidt & Colomb, 2009).

CollateX circumvents this by identifying transposed passages through secondary
heuristic passes *after* the primary alignment, superimposing them as unlabelled
dashed lines — metadata layered onto the graph rather than structural components of
it. For the editor this means transpositions must often be manually audited, since
the core algorithm treats moved text as a deletion in one place and a separate
insertion in another rather than as a single genetic event (Schmidt & Colomb, 2009).

| Scale of transposition | Likely cause |
| --- | --- |
| Two adjacent words | Scribal slip, or a dialectal word-order preference |
| A phrase within a sentence | Scribal or stylistic |
| A sentence or clause | Deliberate editorial intervention |
| A passage or section | Physical misarrangement of folios in the exemplar |

The last row is the evidentially rich case. A large transposition may indicate that
the exemplar's leaves were bound out of order, which is a fact about a physical
object and can sometimes be confirmed by whether the transposed block corresponds to
a quire.

Mark transpositions distinctly in your record. Wednesday's tool will report them as
an omission and an addition, and your identification is what tells you the tool has
mis-modelled a single event.

**Takeaway:** Mark transpositions distinctly — Wednesday's
algorithm will report each as a separate omission and addition, and your record is
what shows that is wrong.

---

## **10 Content**

**Recording What You Discount**

The parallel record, and the one that Wednesday actually depends on.

Every time you look at a difference and decide it is not worth recording as a
variant, write it down anyway — in a separate list, with your reason.

| Difference | Why discounted |
| --- | --- |
| Two spellings of the same word | Orthographic; both regularize identically |
| Capitalization | Not significant in this script |
| Accent present in one, absent in the other | Period-normal; covered by the Week 6 policy |
| Punctuation | Scribal and editorial; treated separately |
| Word division | *Scriptio continua*; division is editorial |
| Abbreviation expanded in one witness | Same word; the abbreviation is a graphic variant |

This is the list that becomes Wednesday's normalization configuration. If left
unconfigured, the alignment algorithm will flag a capital letter against a lowercase
one as a substantive, sequence-breaking variation (Fradejas Rueda, 2022) — and every
row above is a case where you know it should not.

Notice also that the rows differ in kind. Some are *orthographic* decisions already
made in Week 6 and inherited here. Others — punctuation, word division — are
collation-specific decisions about what the unit of comparison is. Distinguish them,
because the first group is handled by collating on `<reg>` and the second must be
configured separately.

Keep this list beside the variant record throughout. It will be longer than you
expect, and its length is the measure of how much implicit knowledge manual
collation depends on.

**Takeaway:** The list of differences you discount becomes
Wednesday's configuration — and its length measures how much manual collation relies
on implicit knowledge.

---

## **11 Content**

**Punctuation**

A specific decision that illustrates the philosophical divide, and which you must
make explicitly today.

In early mainframe collation, punctuation was aggressively stripped from the input
to conserve memory and reduce variance noise (Haentjens Dekker & Middell, 2011).
That was a hardware constraint that became a convention.

Modern TEI-based editing treats punctuation as carrying semantic and historical
weight. Scribal punctuation is evidence about how a text was read and understood,
and discarding it discards that evidence.

The technical difficulty is tokenization. If punctuation attaches to the preceding
word, the algorithm sees `λόγος` and `λόγος,` as a mismatch. If punctuation is
tokenized as independent nodes, the alignment works cleanly but the graph grows
substantially, increasing processing time and matrix size (Haentjens Dekker &
Middell, 2011).

| Approach | Effect on alignment | Effect on evidence |
| --- | --- | --- |
| Strip punctuation | Clean alignment | Punctuation evidence lost |
| Attach to preceding word | Spurious mismatches | Preserved but unusable |
| Tokenize separately | Clean alignment; larger graph | Preserved and comparable |

For your edition the third option is correct if your witnesses have meaningful
punctuation, and the first is acceptable if they do not — many manuscripts have
little or none, and stripping what is absent costs nothing.

Decide based on your actual witnesses rather than on principle. Look at whether they
punctuate, whether they punctuate differently, and whether the differences are
interesting. Record the decision and the reason.

**Takeaway:** Decide punctuation handling from what your witnesses
actually do — stripping absent punctuation costs nothing, stripping meaningful
punctuation costs evidence.

---

## **12 Content**

**Case Study: The Canterbury Tales Project**

The transition from your method to Wednesday's, made once historically.

Manly and Rickert's Chaucer edition used thousands of physical index cards, one per
variant site (Robinson & Driscoll, 2016). It was among the most laborious editorial
projects ever undertaken, and the labour was of exactly the kind you are performing
today.

Peter Robinson's *Canterbury Tales Project* marked the definitive transition from
those index cards to digital progressive multiple alignment, applying evolutionary
biology software to collation data from dozens of Chaucerian manuscripts (Howe et
al., 2012).

The method treats textual variants as genetic mutations. Distance matrix methods and
maximum parsimony algorithms construct unrooted phylogenetic trees; maximum
parsimony finds the genealogical tree requiring the minimum overall number of
changes to explain the observed data, and neighbour-joining clusters manuscripts
into families from the distance metrics that automated collation supplies (Howe et
al., 2012).

The conceptual claim underneath is worth stating: biological algorithms accurately
map human cultural transmission, because both are processes of copying with
modification and branching descent (Howe et al., 2012). The same structural
observation as Lesson 1.1 section 06 made about the DAG.

| Discipline | Copies | Errors | Genealogy |
| --- | --- | --- | --- |
| Biology | Cells and organisms | Mutations | Phylogenetic tree |
| Textual criticism | Scribal copies | Scribal errors | Stemma codicum |
| Version control | Commits | Edits | Commit graph |

What today's manual work produces is the input to all of this. The distance metrics
that phylogenetic algorithms consume are computed from collation data, and the
collation data is a record of variants — which someone has to produce, and which for
most of the discipline's history was produced exactly as you are producing it.

**Takeaway:** Phylogenetic stemmatics consumes collation data as
its input — the variant record you are building by hand is what those methods run
on.

---

## **13 Content**

**Case Study: The Editio Critica Maior and Contamination**

A case that complicates the genealogical model and is directly relevant to Greek
biblical and patristic texts.

The Institut für Neutestamentliche Textforschung uses automated collation at
unparalleled scale for the *Editio Critica Maior* of the Greek New Testament. The
tradition is **hyper-contaminated**: scribes frequently consulted several exemplars
simultaneously, weaving different textual lineages into a single manuscript (Howe et
al., 2012).

Contamination breaks classical stemmatics. Lachmannian method identifies shared
errors to build a family tree, which assumes each witness descends from exactly one
exemplar. A scribe consulting three manuscripts produces a witness with no single
parent, and the tree model fails entirely (Howe et al., 2012).

The response was the **Coherence-Based Genealogical Method**, which relies on
automated collation workflows and computational phylogenetics. Using libraries such
as `open-cbgm`, the project parses TEI collation data — for the Epistle of 3 John,
137 witnesses across 116 variation units — to calculate pre-genealogical coherence
between witnesses (Howe et al., 2012).

Rather than assuming a tree, the CBGM navigates contamination by statistically
evaluating the *directionality* of variants across the whole textual network,
identifying manuscripts that serve as potential ancestors even where their texts are
heavily mixed (Howe et al., 2012).

| Model | Assumes | Fails when |
| --- | --- | --- |
| Lachmannian stemma | Each witness has one exemplar | Scribes consult several |
| Phylogenetic tree | Branching descent without merging | Contamination |
| CBGM textual flow | Directional relations, not strict descent | Very sparse data |

If your passage is biblical or patristic Greek, contamination is likely and the
tree model may not fit. That is a limitation to state rather than to work around at
this scale — but knowing it exists prevents you from over-interpreting a
two-witness collation as evidence of a clean genealogical relation.

**Takeaway:** Contamination breaks tree models, and Greek biblical
traditions are heavily contaminated — do not over-interpret a two-witness collation
as clean descent.

---

## **14 Content**

**Working Through the Passage**

Do the collation now. A realistic target is twenty to thirty lines.

Practical advice from experience:

- Work in short sessions. Collation is fatiguing and error rates rise sharply with fatigue — the specific failure that makes manual collation of large traditions unreliable (Fradejas Rueda, 2022).
- Mark your place in both texts physically before pausing.
- After an omission, count words carefully to re-establish alignment; a mis-resynchronization propagates into every subsequent variant.
- Read aloud where the texts are hard to keep in step. It slows you to word level.
- Check any run of five or more lines with no variants; it may mean you have lost alignment rather than that the witnesses agree.

That last point is the analogue of the line-skip check from Lesson 4.1 section 10,
and it catches the same class of error. Perfect agreement over a long stretch is
possible and is also what mis-alignment looks like.

Number your variants sequentially as you go. The numbering becomes the key linking
today's manual record to Wednesday's automated output, and without it the comparison
is much harder to assemble.

When you finish, count:

| Quantity | Record |
| --- | --- |
| Lines collated | |
| Variants recorded | |
| Variants by type | |
| Differences discounted | |
| Discounted by category | |
| Time taken | |

The last row matters for Wednesday's comparison, as in every previous week.

**Takeaway:** A long run with no variants may mean lost alignment
rather than agreement — check before trusting it.

---

## **15 Content**

**Recording the Collation Digitally**

Transfer the paper record into a structured file, since Wednesday's comparison needs
it machine-readable.

```json
{
  "witnesses": {"A": "MS Vat. gr. 1209", "B": "BnF gr. 2934"},
  "base": "A",
  "layer": "reg",
  "variants": [
    {
      "n": 7,
      "readings": {
        "A": {"text": "ἐγένετο", "loc": "f.42r l.8 w.4"},
        "B": {"text": "ἐγένοντο", "loc": "f.17v l.12 w.4"}
      },
      "type": "morphological",
      "note": "A singular, B plural; compound subject in preceding line favours B"
    }
  ],
  "discounted": [
    {"a": "τιμι", "b": "τιμή", "reason": "orthographic; identical under <reg>"}
  ]
}
```

Two design points. The `discounted` array is as important as `variants`, for the
reason section 10 gave — it is Wednesday's configuration. And locations are recorded
per witness, because the same variant sits at different positions in each and both
are needed to check the alignment.

Save as `collation/manual_collation.json` and commit:

```text
feat(collation): manual collation of ff. 42r-43v against BnF gr. 2934

28 lines collated by hand on paper, then transcribed. 34 variants
recorded: 6 lexical, 11 morphological, 14 orthographic-but-substantive,
2 omissions, 1 transposition. 63 differences discounted as
non-substantive, categorized in the discounted array.

Collated on the <reg> layer; base witness A. Decisions documented in
collation/METHOD.md.

Human-Verified: true
AI-Generated: false
```

Tag it, as the reference for Wednesday:

```bash
git tag -a collation-manual-w7 -m "Manual collation reference, ff. 42r-43v"
```

**Takeaway:** Record discounted differences alongside variants —
they are Wednesday's configuration, not merely notes.

---

## **16 Content**

**Writing the Collation Method Document**

Alongside the data, record how you did it. `collation/METHOD.md` should state:

- Which witnesses, identified by shelfmark and folio range.
- Which layer you collated on, and why.
- Which witness served as base, and why.
- What counts as a token — words, punctuation, both.
- How punctuation was handled.
- How word division was handled.
- What differences were discounted, by category, with reasons.
- The variant taxonomy used.
- How omissions were bounded and recorded.
- How transpositions were identified.
- Anything you were unsure about.

This document is the analogue of Week 6's orthographic decision log, and it serves
the same three purposes: it enforces consistency, it becomes the specification for
the automated method, and it is the editorial statement a reader needs in order to
interpret your apparatus.

The point about specification is immediate. Automated collation forces the editor to
make normalization rules explicit *before* alignment begins (Fradejas Rueda, 2022),
and tomorrow you must configure CollateX. Every line of this document that you
cannot state precisely is a configuration decision you will make under time pressure
tomorrow, probably by accepting a default.

Write it now, while the decisions are fresh. You made most of them today without
noticing, and reconstructing them tomorrow means re-deriving rather than recording.

**Takeaway:** Every imprecise line in the method document becomes a
default you accept under time pressure tomorrow.

---

## **17 Content**

**What the Manual Method Gives You**

Before dismissing it as the slow option, note what it provides that automation does
not.

**Contextual judgement at every point.** You saw each variant in its setting and
could weigh it immediately — noticing that a plural agrees with a compound subject,
that an omission is bounded by similar endings, that a transposition matches a quire
boundary. An algorithm records the difference; you recorded what it means.

**Identification of transpositions as single events.** As section 09 established,
the algorithm will report a transposition as an omission plus an addition. You saw
it as one event, because you understood the text.

**Detection of the interesting cases.** You know which variants matter. The
algorithm will produce all of them undifferentiated, and the classification you did
today is work it cannot do.

**Discovery of your own rules.** Section 05's point: the discounted list exists only
because you noticed yourself discounting.

| | Manual | Automated |
| --- | --- | --- |
| Contextual interpretation | Continuous | None |
| Transposition as one event | Yes | No; post-hoc heuristic |
| Variant classification | As you go | Requires a separate pass |
| Scale | Tens of lines | Millions of words |
| Reproducibility | Depends on the method document | Exact |
| Fatigue error | Significant | None |

Read the last two rows against the first three. Neither column dominates, and the
week's conclusion should reflect that rather than ranking the methods.

**Takeaway:** Manual collation supplies interpretation and
classification that the algorithm cannot; the algorithm supplies scale and
reproducibility that you cannot.

---

## **18 Content**

**Preparing for Wednesday**

Bring:

- The manual collation, structured and committed.
- The discounted-differences list.
- The method document.
- Both witnesses' texts in the collation layer, as plain text or tokenized JSON.
- Your counts and timings.
- Python with CollateX installed.

Install CollateX before the session:

```bash
pip install collatex
```

Confirm it imports and runs on a trivial example. Installation problems are the
commonest way to lose the first half of Wednesday's session, and they are entirely
avoidable.

Wednesday configures CollateX to reproduce today's decisions and measures how well
it does. The specific tests:

- Does it find the variants you found?
- Does it report differences you discounted?
- How does it handle your omission?
- How does it handle your transposition?
- What configuration is needed to suppress the noise?

The second question is the one that requires the discounted list, and it is where
most of the configuration work will go.

**Takeaway:** Install and test CollateX before Wednesday —
installation failures are the commonest way to lose the session.

---

## **19 Content**

**Checklist Before You Leave**

Verify each.

- Both witnesses transcribed for the collated passage.
- Collation layer chosen, with the reason recorded.
- Base witness chosen and recorded.
- Punctuation and word-division policy decided.
- Collation performed systematically, word by word.
- Every variant recorded with readings and locations in both witnesses.
- Every variant classified by taxonomy tier.
- Omissions checked for similar endings at their boundaries.
- Transpositions identified and marked distinctly.
- Discounted differences recorded with reasons.
- Long runs without variants checked for lost alignment.
- Record transferred to structured JSON.
- Method document written.
- Counts and timings recorded.
- Committed and tagged.
- CollateX installed and tested.

If your collation found no omissions or transpositions, that is fine and worth
noting — two closely related witnesses may differ only in small ways. Wednesday's
comparison still works, and the absence of complex variance is itself a finding
about the relationship between your witnesses.

**Takeaway:** Finding no omissions or transpositions is a finding
about your witnesses' relationship, not a failed exercise.

---

## **20 Content**

**Common Problems Today**

Failures that recur.

| Symptom | Cause | Remedy |
| --- | --- | --- |
| Variants stop appearing partway | Lost alignment after an omission | Recount from the omission |
| Enormous numbers of variants | Collating on `<orig>` | Switch to `<reg>`, or expect orthographic noise |
| Tokens like `τιμιτιμή` | Both `<choice>` layers extracted | Remove the unused layer first |
| Cannot decide a variant's type | Genuine ambiguity | Record both classifications with a note |
| Two witnesses seem identical | Same textual family, or lost alignment | Verify alignment before concluding |
| Cannot locate a variant in witness B | Line references not recorded | Record locations for both witnesses always |
| Transposition recorded as two variants | Treated mechanically | Mark as one event with both locations |

The third row is the extraction trap and produces a collation that is entirely
meaningless — every token differs from every other. If your first pass shows
disagreement everywhere, check the extraction before concluding anything about the
witnesses.

The fifth row deserves a moment. Two witnesses agreeing closely is a real and
informative result: it suggests a close genealogical relationship, and it is exactly
what you would expect if one was copied from the other or both from a common
exemplar. Verify the alignment, then record the finding.

**Takeaway:** Disagreement everywhere usually means a broken
extraction, and agreement everywhere usually means either close kinship or lost
alignment — verify before concluding.

---

## **21 Content**

**What Good Work Looks Like Here**

The standard.

A minimally acceptable result is a list of differences between two witnesses.

Good work additionally:

- States which layer was collated and why.
- Records locations in both witnesses for every variant.
- Classifies every variant by taxonomy tier.
- Checks omission boundaries for *homoioteleuton* and reports what is found.
- Identifies transpositions as single events with both locations.
- Records discounted differences with categorized reasons.
- Notes contextual observations bearing on each significant variant.
- States the method precisely enough to configure a tool from it.
- Reports counts by type and the time invested.
- Notes what remains uncertain.

The sixth item is what makes today's work usable tomorrow, and the fourth is what
makes it scholarship. Recording that witness B omits eleven words is a datum;
recording that the omission runs from one occurrence of a word to the next
occurrence of the same word, and is therefore probably a mechanical skip rather than
a deliberate excision, is an interpretation supported by evidence — and it bears
directly on whether the omission counts as evidence of descent.

**Takeaway:** Recording that an omission is bounded by similar
endings turns a datum into an interpretation — and changes what the variant is
evidence for.

---

## **22 Content**

**Two Witnesses and Its Limits**

An honest note on scale, since your collation has exactly two witnesses.

With two witnesses you can record differences. You cannot, in general, determine
which reading is original, because there is no third party to break the tie. Where A
and B differ, the evidence alone does not say which is the corruption.

| Witnesses | Supports |
| --- | --- |
| 2 | Recording variants; identifying types |
| 3 | Majority readings; some directionality |
| Several, uncontaminated | Stemmatic reconstruction |
| Many, contaminated | CBGM-style textual flow analysis |

What you *can* do with two is substantial. You can identify the kinds of variation
present, characterize each scribe's habits, detect mechanical errors from their
mechanism, and make arguments about individual readings from internal evidence —
grammar, sense, and the tendency of scribes to simplify difficult readings.

You can also make a preliminary judgement about the relationship. Two witnesses
sharing a distinctive omission or lexical substitution probably share an ancestor in
which it arose; two witnesses differing in many small ways and agreeing in none of
the distinctive ones probably do not.

State these limits in your report. A two-witness collation supporting a claim about
the whole tradition would be overreaching, and saying what your evidence can and
cannot support is the same disposition Lesson 5.2 section 27 asked for.

**Takeaway:** Two witnesses record variation and cannot generally
determine which reading is original — state that limit rather than overreaching.

---

## **23 Content**

**Genetic Editing: A Different Application**

Worth knowing, because it broadens what collation is for and may apply to your own
later work.

Automated collation is not limited to scribal transmission; it is equally vital for
**genetic editing**, which traces the authorial development of a text. Projects on
the Charles Darwin manuscripts and the Beckett Digital Manuscript Project use
CollateX to map authorial revisions across drafts (Haentjens Dekker et al., 2015).

The conceptual move is treating each revision campaign as a **witness**. Unlike
scribal copies, authorial drafts represent layers of revision within the same
document, and passing them through the same alignment machinery computes the
differences between intra-document layers automatically (Haentjens Dekker et al.,
2015).

The variant graph models these overlapping hierarchies successfully, allowing
interfaces to render heat maps or aligned barcodes highlighting exactly which
passages an author expanded, deleted, or transposed between versions (Schmidt &
Colomb, 2009).

| Application | Witnesses are | Variants represent |
| --- | --- | --- |
| Scribal transmission | Manuscript copies | Copying errors and interventions |
| Genetic editing | Authorial drafts | Authorial revision |
| Print history | Successive editions | Editorial and authorial change |
| Version control | Commits | Deliberate edits |

The fourth row should look familiar. Your Git history is a genetic edition of your
own edition, and `git diff` between two tagged states performs exactly this
operation on it. The structural identity that Lesson 1.1 argued for is not an
analogy — it is the same computation applied to different material.

**Takeaway:** Treating drafts as witnesses makes the same
machinery trace authorial revision — and your own Git history is a genetic edition
of your edition.

---

## **24 Content**

**Connecting to Week 8**

Where the collation goes.

| Week | Uses the collation as |
| --- | --- |
| 7 | The comparison itself |
| 8 | The source of apparatus entries |
| 12 | Evidence for commentary on contested readings |
| 13 | Published apparatus |

Week 8 is the immediate consumer. The apparatus criticus is a structured
presentation of collation results: for each variant site, the reading adopted
(`<lem>`) and the rejected readings (`<rdg>`) with their witnesses, encoded with the
TEI critical apparatus module.

Your taxonomy from today determines what enters the apparatus. Orthographic variants
are typically excluded from the main apparatus and treated separately — otherwise
the apparatus is unreadable. Lexical substitutions, omissions, and transpositions
belong in it.

That filtering decision is an editorial policy in the same sense as Week 6's, and it
should be recorded in the method document today. An apparatus that includes
everything is technically complete and practically useless; one that includes only
what the editor judged significant is usable and depends entirely on the judgement
being stated.

The **Normalization Assignment is due Friday October 23**, at the end of this week.

**Takeaway:** Your taxonomy determines what enters Week 8's
apparatus — including everything makes it unreadable, so the filtering policy must
be stated.

---

## **25 Content**

**Synthesis: The Judgement Behind the Comparison**

The argument of this meeting.

Collation looks mechanical. Two texts, compared word by word, differences recorded.
The mechanical description is accurate as far as it goes, and it omits everything
that makes collation scholarship.

At every point you made judgements. Whether a difference counts. What kind of
difference it is. Whether an omission was mechanical or deliberate. Whether moved
text is a transposition or a coincidence. Whether two spellings are the same word.
Most of those judgements were made without deliberation, which is what expertise
feels like from the inside (Haentjens Dekker & Middell, 2011).

Wednesday's tool makes none of them. It aligns tokens by a mathematical criterion
and reports every deviation without differentiation. Everything you did today
without noticing must be supplied to it as explicit configuration, and what cannot
be supplied — the interpretation, the classification, the recognition of a
transposition as one event — remains yours.

That is the sense in which automated collation does not do the philological work.
It provides a perfectly structured, mathematically sound dataset upon which rigorous
textual criticism can be performed (Nury & Spadini, 2020). The dataset is not the
criticism.

**For Wednesday.** Bring the six items in section 18, with CollateX installed and
tested. You will configure it to reproduce today's decisions and measure how far it
succeeds.

**Takeaway:** Automated collation produces the dataset on which
criticism is performed; today's judgements are the criticism, and they are what the
tool must be told.

---

## **26 Content**

**A Note on Fatigue and Reliability**

Worth recording honestly at the end of a demanding session.

Manual collation imposes an extreme cognitive load and is highly susceptible to
fatigue-induced errors (Fradejas Rueda, 2022). You will have felt this. Attention
degrades, and degraded attention on a comparison task produces missed variants
rather than obvious errors — the failure is silent.

This has a direct methodological consequence: your manual collation, unlike Week 4's
transcription, has not been verified. It is a single pass, and single passes on
comparison tasks miss things.

Wednesday's automated collation will find variants you missed. When it does, the
correct response is not to treat them as false positives but to check them — some
will be differences you discounted, and some will be variants your attention slipped
past.

| Wednesday reports | Likely explanation |
| --- | --- |
| A variant you recorded | Agreement |
| A difference you discounted | Configuration not yet applied |
| A variant you missed | Fatigue; genuine finding |
| A variant that is not there | Alignment fault; investigate |

The third row is the valuable one, and it is the same benefit as Lesson 6.2 section
15: the deterministic method's uniform attention catches what human attention
misses. Expect it, and record the corrections it prompts.

**Takeaway:** Wednesday will find variants you missed through
fatigue — treat those as findings rather than as the tool's false positives.

---

## **27 Content**

**Estimating What Automation Must Suppress**

A final analytical exercise, which sets Wednesday's target.

Count your discounted differences and compare them against your recorded variants.
The ratio predicts how much noise Wednesday's unconfigured run will produce.

| Measure | Meaning |
| --- | --- |
| Variants recorded | What should appear in the apparatus |
| Differences discounted | What configuration must suppress |
| Ratio of discounted to recorded | The signal-to-noise problem |

If you discounted sixty-three differences and recorded thirty-four variants, an
unconfigured collation will report roughly ninety-seven differences of which about
two-thirds are noise. That is the fragmentation the literature describes: aligning
un-normalized text produces highly disjointed graphs saturated with non-genealogical
noise (Haentjens Dekker & Middell, 2011).

Predict the number before running the tool tomorrow, and record the prediction. It
is a genuine test of whether you understand what the tool does, and a substantial
discrepancy between your prediction and the result is informative in either
direction — either your discounted list is incomplete, or the tool's default
tokenization differs from your assumptions.

This is also the argument for collating on `<reg>`. Most of your discounted
differences are orthographic, and collating on the regularized layer suppresses them
before alignment rather than requiring configuration to filter them afterwards. The
work Week 6 did is what makes Wednesday tractable.

**Takeaway:** Predict tomorrow's raw difference count from your
discounted list — a large discrepancy means either your list is incomplete or the
tool tokenizes differently than you assume.

---

## **28 Content**

**Tokenization as a Decision**

One further configuration matter to settle today, because it is the first stage of
tomorrow's pipeline.

**Tokenization** is the division of a character sequence into minimal units,
typically words, identified by spaces, punctuation, or markup (Haentjens Dekker &
Middell, 2011). It sounds trivial and is not, because what counts as a token
determines what can be compared.

Decisions your text forces:

| Question | Options | Consequence |
| --- | --- | --- |
| Are punctuation marks tokens? | Yes / attached / stripped | Section 11's trade-off |
| Is a word broken across lines one token? | Yes / two | Affects alignment at line ends |
| Is an abbreviation one token or its expansion? | `<abbr>` / `<expan>` | Determines what is compared |
| Is *scriptio continua* tokenized by your division? | Yes / by character | Your division is editorial |
| Are enclitics separate tokens? | Yes / joined | Affects Greek word counts |

The second row is a real problem for manuscript text and connects to Lesson 5.2
section 06: models frequently fail to reconstruct a word fractured across a line
break, treating the two fragments as unrelated tokens, which inflates apparent
difference (Bawden et al., 2026, as discussed in Week 5). Your own transcription
recorded such breaks as written, and tokenization must rejoin them or your two
witnesses will differ wherever their line breaks fall differently — which is
everywhere.

That is a substantial and easily missed source of spurious variants. Decide now that
line-broken words are rejoined before tokenization, and record it.

**Takeaway:** Rejoin words broken across lines before tokenizing,
or your witnesses will differ wherever their line breaks fall differently.

---

## **29 Content**

**What Today Produced**

Take stock, because the outputs are more numerous than the variant list.

| Output | Role |
| --- | --- |
| The variant record | The reference for Wednesday and Friday |
| Variant classifications | What Week 8's apparatus filters on |
| Contextual notes | Material for Week 12's commentary |
| The discounted list | Wednesday's normalization configuration |
| The method document | The specification, and the editorial statement |
| Tokenization decisions | Wednesday's pipeline configuration |
| Counts and timings | The cost side of Wednesday's comparison |
| Your own uncertainty | Honest limits for the report |

Four of those eight are configuration for tomorrow rather than results of today,
which is the shape this course's manual steps consistently take. The manual step
produces a reference *and* the specification for automating the same task, and the
second is often the more laborious product.

The contextual notes deserve a mention. They will be worth more in Week 12 than
anything else on this list, because an apparatus entry states that witnesses differ
and a commentary explains what the difference means — and the explanation depends on
observations made while looking at the passage, which is now.

**Takeaway:** Half of today's outputs are configuration for
tomorrow rather than results — the manual step specifies the automation as well as
providing the reference.

---

## **30 Content**

**Synthesis: Recording Difference, Interpreting Descent**

The argument of this meeting, in its own terms.

Collation records where witnesses differ. That record is not the goal; it is the
evidence base for inferences about transmission — which manuscripts descend from
which, which readings are original, what happened as the text was copied.

The inferences depend on classification, because variant types differ enormously in
evidential value. Orthographic variation is polygenetic and proves little; a long
inexplicable omission is very unlikely to arise twice and proves a great deal (Nury
& Spadini, 2020). An editor who records differences without classifying them has
produced data without the analysis that makes it usable.

Classification is judgement, and today's method made that judgement visible by
slowing it down. You discovered rules you were applying without stating them, which
is precisely what an automated method requires you to state.

The manual method's limits are real: it does not scale past tens of lines, it is
fatiguing, and single-pass comparison misses variants (Fradejas Rueda, 2022). Those
limits motivate Wednesday. What Wednesday does not supply is the interpretation, and
the week's conclusion should say so without ranking the methods.

**For Wednesday.** CollateX installed and tested; the six items in section 18. You
will configure the tool from today's method document and measure how far it
reproduces today's decisions.

**Due Friday October 23.** The Normalization Assignment, from Topic 6.

**Takeaway:** Collation produces evidence for inferences about
descent, and the inferences depend on a classification only judgement supplies.

---

## References

Bawden, R., Clérice, T., Glaise, A., Pinche, A., & Smith, D. (2026).
*Pre-editorial normalization for automatically transcribed medieval manuscripts in
Old French and Latin* (arXiv:2602.13905). https://arxiv.org/abs/2602.13905

Fradejas Rueda, J. M. (2022). *Resources and challenges for the automatic collation
of medieval texts: The 7PartidasDigital project*.

Gignac, F. T. (1976). *A grammar of the Greek papyri of the Roman and Byzantine
periods*. Istituto Editoriale Cisalpino.

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

Robinson, P., & Driscoll, M. J. (Eds.). (2016). *Digital scholarly editing:
Theories and practices*. Open Book Publishers.
https://doi.org/10.11647/OBP.0095

Schmidt, D., & Colomb, R. (2009). A data structure for representing multi-version
texts online. *International Journal of Human-Computer Studies, 67*(6), 497–514.

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/
