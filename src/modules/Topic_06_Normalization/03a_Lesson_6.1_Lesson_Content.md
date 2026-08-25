# Lesson 6.1 — Iotacism, Orthographic Variation, and Regularizing by Hand

*RELS 398 / ENGL 398 · Topic 6: Normalization · Meeting #14 (Tue Oct 6)*

***Step 1 of the three-step cycle: manual.** Today you regularize your consensus
text by hand, recording every decision. Those recorded decisions become the rules
Wednesday's script implements and the reference Friday's AI pass is measured
against.*

---

## **01 Content**

**The Problem Normalization Solves and Creates**

Your consensus text records what the scribe wrote. That is exactly what a
diplomatic transcription should do, and it creates a problem.

Historical scribes spelled inconsistently. The same word appears in several forms
across a single manuscript, sometimes across a single folio. A search for τιμή does
not find τιμι. A morphological parser cannot analyze a form it does not recognize.
A lexicon lookup fails. Every computational operation that assumes standard
orthography fails on text that does not have it.

The obvious remedy — standardize the spelling — destroys the evidence. Those
variant spellings are data. They record the scribe's dialect, education, and
region; they document the chronological development of the language; and in some
cases they are the only surviving evidence for how Greek was pronounced at a
particular time and place (Gignac, 1976).

The digital editor therefore faces a genuine dilemma. Transcribing exactly what is
on the page preserves vital evidence of dialect, education level, and linguistic
development. Failing to link those phonetic spellings to their standard lemmas
renders the text invisible to lexical search engines, corpus linguistics tools, and
automated morphological parsers (Gignac, 1976).

The resolution, which this week builds, is to refuse the choice. TEI permits both
layers to coexist, parallel rather than mutually exclusive, with the relationship
between them recorded explicitly. The text is simultaneously diplomatic and
searchable, and a reader or a program selects the layer appropriate to their
purpose.

**Vocabulary.** *Normalization* — mapping variant historical forms to standard ones.
*Regularization* — the same operation, the term TEI uses. *Lemma* — the dictionary
headword under which a form is listed.

**The takeaway for this page:** Standardizing spelling makes text searchable and
destroys linguistic evidence — TEI resolves this by keeping both layers in
parallel.

---

## **02 Content**

**Iotacism: The Chain Shift**

The dominant source of orthographic variation in Greek manuscripts is **iotacism**
— also called itacism — a phonetic-phonological phenomenon in which multiple vowels
and diphthongs progressively merged into the single close front unrounded vowel
/i/ (Gignac, 1976).

The merger was not a single event but a **chain shift** through the Hellenistic and
Roman periods. Its mechanics are worth following, because they explain why the
substitutions cluster as they do. The relative infrequency of ancient /iː/, and the
overcrowding caused by the new long /eː/, pulled /eː/ toward /iː/. That movement
caused the original /ɛː/ to shift toward the position /eː/ had abandoned, which in
turn caused the diphthong /ai/ to monophthongize to /ɛː/ (Gignac, 1976).

The result is a set of graphemes that had become homophones:

| Classical grapheme | Classical value | Hellenistic/Roman value | Common substitutions |
| --- | --- | --- | --- |
| ι (iota) | /i/ | /i/ | ει, η |
| ει (epsilon-iota) | /eː/ | /i/ | ι, η |
| η (eta) | /ɛː/ | /i/ via /eː/ | ι, ει |
| οι (omicron-iota) | /oi/ | /y/ then /i/ | υ |
| υ (upsilon) | /y/ | /y/ then /i/ | οι, ι, η |
| αι (alpha-iota) | /ai/ | /ɛː/ | ε |

A scribe who has learned to write by ear, or who is writing what is dictated,
selects among homophonous graphemes and will sometimes select differently from the
classical standard. So τιμή may appear as τιμι, and δει as δι (Gignac, 1976).

These are not random errors. They are systematic, predictable from the phonology,
and therefore *evidence*: the specific substitutions attested in a manuscript
constrain when and where it was written and how its scribe learned the language.

**The takeaway for this page:** Iotacism merged several graphemes into homophones,
so the substitutions are systematic evidence about date and provenance rather than
random error.

---

## **03 Content**

**Language Contact and Phonetic Spelling**

Iotacism was general, but its incidence varied with circumstance, and the variation
is itself informative.

Phonetic spelling was particularly prevalent in environments like Hellenistic
Egypt, where Greek was frequently used as a second language and was heavily
influenced by Egyptian-Coptic phonological transfer (Gignac, 1976). A writer whose
first language lacked certain Greek distinctions would not reliably reproduce them
in writing, and the resulting spellings record the contact situation.

This matters for how you interpret your own manuscript's variants. A high incidence
of a particular substitution may indicate:

| Observation | Possible interpretation |
| --- | --- |
| Systematic iotacism throughout | Post-classical date; phonetic spelling practice |
| One substitution type dominant | A specific phonological environment or dialect |
| Variation clustering in one section | A change of scribe, or of exemplar |
| Substitutions absent | A learned scribe, or a classicizing exemplar |
| Non-Greek phonological patterns | Language contact; a non-native writer |

The last row is where Gignac's papyrological work is most directly useful. The
phonetic baseline he established is what allows modern digital corpora to
systematically *classify* linguistic variation rather than dismissing it as error
(Gignac, 1976). A substitution that a nineteenth-century editor would have silently
corrected is, on this account, a datum.

For today's work the implication is a disposition rather than a technique. When you
encounter a non-standard form, the first question is not "what should this be?" but
"what kind of variation is this?" — because the answer determines which TEI
encoding is correct, as the next several pages establish.

**The takeaway for this page:** Ask what kind of variation a form represents before
asking what it should be — the answer determines the encoding.

---

## **04 Content**

**The Dual Ontology: Document and Work**

Behind the encoding lies a theoretical distinction that this week makes practical.

A manuscript is a **document** — a physical object with ink on a surface, made at a
particular time by a particular person. It is also a witness to a **work** — an
abstract text that exists across witnesses and of which no single manuscript is
identical to any other.

Editorial traditions differ in which they privilege, and the tension is a live
theoretical debate. Robinson warns against reducing scholarly editing to mere
documentary transcription, arguing instead for multi-witness critical editions that
use digital tools to enhance rather than replace traditional philological judgement
(Robinson & Driscoll, 2016).

The debate is worth understanding because both positions have a failure mode. An
edition that records only the document produces a transcription of one witness and
declines the editorial work that makes a text usable. An edition that records only
the work suppresses the evidence on which its own conclusions rest — which is
precisely what printed critical editions did when they silently corrected
orthography to classical norms, erasing vital sociolinguistic data (Robinson &
Driscoll, 2016).

TEI Chapter 11 accommodates the dual ontology by allowing parallel, multi-layered
encodings (TEI Consortium, 2026). This is not a compromise between the positions
but a refusal of the choice: the document layer and the work layer both exist in
the file, and the relationship between them is explicit and machine-readable.

That architecture is what today's work builds. You are not deciding whether your
edition is documentary or critical. You are recording both, and recording how they
relate.

**The takeaway for this page:** TEI's parallel layers refuse the choice between
documentary and critical editing — both exist in the file with their relationship
explicit.

---

## **05 Content**

**The `<choice>` Element**

The mechanism is `<choice>`, which groups alternative encodings for the same point
in the text, on the principle that a full representation requires those alternatives
to be treated as parallel rather than mutually exclusive (TEI Consortium, 2026).

`<choice>` does not choose. It holds alternatives, and a processor selects
according to purpose:

```xml
<choice>
  <orig>τιμι</orig>
  <reg>τιμή</reg>
</choice>
```

| Consumer | Selects | Purpose |
| --- | --- | --- |
| Diplomatic view | `<orig>` | Shows what the scribe wrote |
| Reading view | `<reg>` | Shows the standard form |
| Search index | Both | Finds the passage by either |
| Morphological parser | `<reg>` | Requires standard forms |
| Historical phonology study | `<orig>` | The variant is the data |
| Collation | Configurable | Depends on the question |

The last row anticipates Week 7 and matters more than it looks. When you collate
witnesses, whether two manuscripts "differ" at a point of orthographic variation
depends on which layer you compare. Collating on `<orig>` reports every phonetic
spelling as a variant; collating on `<reg>` reports none of them. Neither is wrong,
and the choice must be deliberate — which is only possible because both layers
exist.

This is the payoff for not normalizing during transcription, as Lesson 4.1 section
02 insisted. Had you silently regularized in Week 4, the `<orig>` layer would not
exist and none of these options would be available.

**The takeaway for this page:** `<choice>` holds alternatives rather than deciding
between them, which is what lets Week 7 collate on either layer deliberately.

---

## **06 Content**

**`<orig>`/`<reg>` Versus `<sic>`/`<corr>`**

TEI provides two element pairs inside `<choice>`, and choosing between them is the
central editorial judgement of this week.

**`<orig>` and `<reg>`** are used where a scribe employed a non-standard spelling
that was common, phonetic, or acceptable in their historical context — phonetic
spellings from iotacism, archaic or dialectal forms. `<orig>` holds the diplomatic
reading as it appears on the substrate; `<reg>` holds the standardized equivalent
(TEI Consortium, 2026).

**`<sic>` and `<corr>`** are reserved strictly for outright errors, blunders, or
*lapsus calami* — instances where the scribe wrote something unambiguously
incorrect even by the standards of their own time, requiring editorial emendation
to restore the archetype (TEI Consortium, 2026).

| | `<orig>` / `<reg>` | `<sic>` / `<corr>` |
| --- | --- | --- |
| Claim | This spelling was acceptable then | This was a mistake, then and now |
| Applies to | Phonetic spelling; dialect; archaism | Slips of the pen; omitted letters; dittography |
| The variant is | Linguistic evidence | Scribal error |
| Editorial act | Regularization | Emendation |
| Example | τιμι for τιμή (iotacism) | τμμήν for τιμήν (miswritten letter) |

The distinction is intensely debated, and the debate is real rather than
terminological. An idiosyncratic spelling might be interpreted as an outright error
by one editor and as evidence of an undocumented regional dialect by another (TEI
Consortium, 2026).

That ambiguity is why today's decision log matters. You will make this judgement
dozens of times, and the judgements must be consistent and defensible. Recording
the reason at the time is what makes them so; deciding case by case without a
principle produces an edition whose editorial policy cannot be stated.

**The takeaway for this page:** `<orig>`/`<reg>` claims a spelling was acceptable
then; `<sic>`/`<corr>` claims it was a mistake — and which applies is a genuine
editorial judgement.

---

## **07 Content**

**Drawing the Line in Practice**

A working procedure for the judgement, since the principle needs operationalizing.

Ask, in order:

- **Is the form attested elsewhere?** A spelling appearing repeatedly in this manuscript, or documented in the papyrological and epigraphic record, is a variant rather than a slip.
- **Is it phonologically motivated?** A substitution predicted by the chain shift in section 02 is a phonetic spelling.
- **Is it a plausible mechanical error?** A doubled syllable, an omitted letter, a letter formed as its neighbour — these suggest *lapsus calami*.
- **Would a contemporary have accepted it?** This is the criterion TEI states, and it is the one to return to when the others are inconclusive.
- **Does it recur in this scribe's hand?** Consistency suggests practice; isolation suggests slip.

| Form | Analysis | Encoding |
| --- | --- | --- |
| τιμι for τιμή | Iotacism; phonologically motivated; attested widely | `<orig>`/`<reg>` |
| δι for δει | Iotacism | `<orig>`/`<reg>` |
| ἐγενετο for ἐγένετο | Accent omitted, common in this hand | `<orig>`/`<reg>` |
| τμμήν for τιμήν | Iota written as mu; no phonological basis | `<sic>`/`<corr>` |
| λογογος for λόγος | Dittography of a syllable | `<sic>`/`<corr>` |
| ἐγένετο for ἐγένοντο | Wrong number; could be either | Requires judgement; document it |

The last row is the genuinely hard case and will occur. A form that is grammatically
wrong in context might be a scribal slip or might reflect a real variant reading in
the tradition — in which case it belongs in Week 8's apparatus rather than being
corrected here at all.

When you cannot decide, record the uncertainty rather than resolving it silently.
`<choice>` can carry `@cert`, and a documented uncertainty is more useful to a later
editor than a confident misclassification.

**The takeaway for this page:** A recurring, phonologically motivated form is a
variant; an isolated mechanical slip is an error — and grammatically wrong forms may
belong in the apparatus instead.

---

## **08 Content**

**Case Study: The Duke Databank of Documentary Papyri**

Papyrology has been at the vanguard of digital humanities, and the DDbDP shows this
architecture operating at scale.

The Papyrological Navigator at Papyri.info hosts tens of thousands of Greek and
Latin documentary texts encoded in EpiDoc, the TEI customization designed for
epigraphic and papyrological documents (Gignac, 1976; TEI Consortium, 2026).

Greek documentary papyri are saturated with iotacism and phonetic spelling. In older
print editions, editors either silently corrected these forms or relegated them to
the apparatus criticus — noting, for instance, "l. βιβλίδιον" for *lege* βιβλίδιον
(Robinson & Driscoll, 2016). Both practices remove the variant from the text.

The DDbDP brings the variation into the inline markup, preserving the original.
Papyrologists encode regularizations using **Leiden+**, an input syntax that is
faster to type than XML: a papyrus reading φρόνδεισον where the standard is
φρόντισον is entered as `<:φρόντισον|reg|φρόνδεισον:>`, which the backend translates
into standard TEI:

```xml
<choice>
  <reg>φρόντισον</reg>
  <orig>φρόνδεισον</orig>
</choice>
```

Outright errors use a parallel syntax, `<:τιμὴν|corr|τμμὴν:>`, generating a
`<choice>` with `<corr>` and `<sic>` (TEI Consortium, 2026).

The payoff is quantitative. Because `<orig>` preserves the phonetic data while
`<reg>` maps to classical lemmas, downstream projects can isolate every instance
where ει was substituted for ι before a given consonant class — transforming what
was once dismissed as scribal error into a corpus for sociolinguistic study
(Gignac, 1976).

**The takeaway for this page:** The DDbDP's inline markup turned what print editions
discarded as scribal error into a queryable corpus for studying language change.

---

## **09 Content**

**Case Study: Codex Sinaiticus and the Dictation Theory**

A second case shows orthographic analysis bearing directly on a question of textual
transmission.

Codex Sinaiticus, the fourth-century majuscule Bible, is the subject of a long
debate over the **dictation theory**: the hypothesis that portions were copied from
dictation rather than by visual copying, which would explain a high prevalence of
phonetic spelling (Robinson & Driscoll, 2016).

The argument turns entirely on orthography. A scribe copying visually makes errors
of the eye — confusing similar letterforms, skipping from one occurrence of a word
to another. A scribe writing from dictation makes errors of the ear — substituting
homophones. Since fourth-century vowel mergers had made several graphemes
homophonous, dictation would inevitably produce homophonic substitutions (Robinson
& Driscoll, 2016).

| Error type | Suggests | Example mechanism |
| --- | --- | --- |
| Visually similar letters confused | Copying by eye | Two letterforms alike in this script |
| Homophonous graphemes substituted | Copying by ear | Iotacism substitutions |
| Line or phrase omitted between identical words | Copying by eye | Skip from one occurrence to the next |
| Word division differing from sense | Copying by ear | Heard as a different word boundary |

The methodological consequence is direct: capturing these substitutions without
silently standardizing them is critical for rigorous stemmatic analysis (Robinson &
Driscoll, 2016). An edition that regularized the orthography would have destroyed
the evidence on which the dictation debate depends.

The digital edition of Sinaiticus uses `<choice>` to let a reader filter
dynamically — reading the normalized text for theological study, or toggling to the
diplomatic transcription to study the lector's accent, the scribe's phonetic
idiosyncrasies, and the sequence of corrections recorded with `<del>`, `<add>`, and
`<handShift>` (Robinson & Driscoll, 2016).

If your own manuscript shows systematic homophonic substitution, this is a question
you can ask of it.

**The takeaway for this page:** Whether Sinaiticus was copied by ear or by eye is
decided by orthographic evidence — which a regularized edition would have destroyed.

---

## **10 Content**

**Beginning the Decision Log**

The cornerstone of this week's work is a **standardized orthographic decision log**,
documenting exactly where the boundary lies between a valid linguistic variant and
an outright error (TEI Consortium, 2026).

Create `transcription/ORTHOGRAPHY.md` and structure it as a policy document
followed by a case register.

The policy section states your general rules:

| Phenomenon | Policy | Rationale |
| --- | --- | --- |
| Iotacism substitutions | `<orig>`/`<reg>` | Phonologically motivated; period-normal |
| Missing accents | `<orig>`/`<reg>` | Consistent in this hand; not an error |
| Missing breathings | `<orig>`/`<reg>` | As above |
| Movable nu present or absent | `<orig>`/`<reg>` | Period-normal variation |
| Dittography | `<sic>`/`<corr>` | Mechanical error |
| Omitted letter with no phonological basis | `<sic>`/`<corr>` | Mechanical error |
| Wrong grammatical form | Case by case; may be apparatus | Could be a real variant reading |
| *Scriptio continua* word division | Editorial; declared in the header | Not orthographic variation |

The case register then records each instance you encounter that the policy does not
straightforwardly settle: the form, its line, your analysis, the encoding chosen,
and the reason.

Two properties make this document worth the effort. It enforces consistency, which
is what makes an edition's orthographic policy statable. And it becomes Wednesday's
specification: the rules you write today are what the deterministic script
implements, and a rule you cannot state in this document is one you cannot
implement tomorrow.

**The takeaway for this page:** Today's decision log is tomorrow's specification —
a rule you cannot state here cannot be implemented as a script.

---

## **11 Content**

**Surveying Your Text**

Before encoding anything, survey the variation. You cannot write a policy for
phenomena you have not catalogued.

Work through your consensus text and record every non-standard form:

- The form as written.
- Its line and position.
- The standard form, if you can identify it.
- What kind of variation it appears to be.
- How many times this pattern occurs.

A script speeds the survey by finding candidates, though the judgement remains
yours:

```python
import re, unicodedata
from collections import Counter

IOTACISM = [
    (r"ει", "ι"), (r"ι", "ει"), (r"η", "ι"), (r"ι", "η"),
    (r"οι", "υ"), (r"υ", "οι"), (r"αι", "ε"), (r"ε", "αι"),
]

def candidates(word, lexicon):
    """Forms reachable from `word` by one iotacism substitution."""
    out = set()
    for src, dst in IOTACISM:
        for m in re.finditer(src, word):
            alt = word[:m.start()] + dst + word[m.end():]
            if alt in lexicon:
                out.add(alt)
    return out
```

A lexicon of standard forms makes this far more useful, and one is available from
any digital Greek corpus. Without one the script generates candidates you must
check by hand, which is still faster than reading for variants unaided.

Count the patterns. A substitution occurring eleven times is a systematic feature of
this scribe's practice and deserves a policy line; one occurring once may be a slip.
That frequency distinction is often the best available evidence for the
`<orig>`/`<sic>` judgement.

**The takeaway for this page:** Count how often each substitution pattern occurs —
frequency is often the best evidence for whether it is practice or slip.

---

## **12 Content**

**Encoding the Regularizations**

With the survey complete and the policy set, encode.

```xml
<lb n="3" facs="#f42r_l03"/>ἦν ὁ λόγος οὗτος ἦν ἐν ἀρχῇ πρὸς τὸν
<choice>
  <orig>θεον</orig>
  <reg>θεόν</reg>
</choice>
```

Several practical points.

**Encode at the word level.** A `<choice>` spanning several words makes the
correspondence between original and regularized ambiguous, and breaks any
processing that aligns the two layers token by token.

**Keep the layers parallel and complete.** Both `<orig>` and `<reg>` must be full
forms, not fragments. Encoding only the differing letters saves typing and makes the
markup unusable.

**Attribute responsibility.** `@resp` on the `<choice>` records who made the
regularization, which will matter on Friday when some regularizations are proposed
by a machine.

**Record certainty where it is genuinely uncertain.** `@cert` on `<reg>` records a
regularization you are not confident of.

```xml
<choice resp="#KMP" cert="medium">
  <orig>ἐγενετω</orig>
  <reg>ἐγένετο</reg>
</choice>
```

**Do not regularize inside `<unclear>`.** Where the reading itself is uncertain,
regularizing compounds one inference with another. Resolve the reading first, or
leave both unresolved and say so.

Work systematically through the text rather than opportunistically. Consistency is
the property that matters most, and it is easiest to achieve by handling one
phenomenon at a time across the whole text.

**The takeaway for this page:** Encode at the word level with complete forms in both
layers, and never regularize inside an `<unclear>` reading.

---

## **13 Content**

**What Not to Regularize**

An equally important set of decisions, and the one where over-eagerness does damage.

| Do not regularize | Reason |
| --- | --- |
| Genuine variant readings | These belong in Week 8's apparatus, not here |
| Uncertain readings | Compounds inference on inference |
| Forms you cannot identify | A guessed lemma is worse than none |
| Proper names | Frequently non-standard by nature; regularizing may be wrong |
| Dialectal morphology | Beyond orthography; changes the linguistic evidence |
| Scribal corrections | Already encoded with `<subst>`; do not layer on top |

The fourth row deserves emphasis because it recurs in the literature as a specific
constraint. In automated normalization pipelines, abbreviations and forms
corresponding to proper names lacking contextual clarity must remain unexpanded
rather than being algorithmically resolved (Bollmann, 2019). The same caution
applies to your manual work: a personal or place name spelled unusually may be
spelled correctly for its bearer, and normalizing it to a familiar form asserts an
identification you may not have.

The fifth row marks the boundary of the whole operation. Normalization is
**orthographic**. Changing a dialectal verb ending to the Attic form is not
regularizing spelling; it is altering the morphology, and it destroys exactly the
linguistic evidence the `<orig>` layer exists to preserve. The line between the two
is not always obvious, and where it is unclear the conservative choice is to leave
the form alone and note it.

The first row is the one that most often goes wrong. If your manuscript reads
ἐγένοντο where another witness reads ἐγένετο, that is a textual variant — evidence
about the transmission — and regularizing it here would silently resolve a question
Week 7 exists to investigate.

**The takeaway for this page:** Normalization is orthographic only — altering
morphology, resolving names, or fixing variant readings all destroy evidence other
weeks need.

---

## **14 Content**

**Silent Correction and What It Cost**

A historical note that motivates the whole architecture.

Traditional printed critical editions often suppressed orthographic variation
entirely, silently correcting forms to classical norms and thereby erasing vital
sociolinguistic data (Robinson & Driscoll, 2016). This was not carelessness; it
reflected a view of the editor's task as recovering the author's text, in which
scribal spelling was noise to be filtered out.

The cost became apparent only when the questions changed. When historical
linguistics began asking about the actual pronunciation of post-classical Greek, the
evidence had been removed from the printed editions and survived only in the
manuscripts themselves — which meant returning to the witnesses and redoing the
work.

| Practice | What it preserves | What it discards |
| --- | --- | --- |
| Silent correction to classical norms | A readable text | All orthographic evidence |
| Correction noted in the apparatus | The text plus a record | Ease of systematic study |
| `<choice>` with both layers | Both, queryable | Nothing |

The middle row is the nineteenth-century compromise and it was a real improvement —
the DDbDP's "l. βιβλίδιον" notation records what was corrected. Its limitation is
practical: an apparatus note is readable by a human one instance at a time, and
cannot support the systematic quantitative study that section 08 described.

The general principle worth extracting: **the questions a future scholar will ask
are not knowable now.** An edition that discards evidence because the current
generation of scholarship does not use it forecloses questions that have not yet
been formulated. Recording both layers costs storage and effort; discarding one
costs information permanently.

**The takeaway for this page:** Editions that discarded orthographic evidence
foreclosed questions nobody had yet asked — which is the argument for recording both
layers.

---

## **15 Content**

**Documenting the Policy in the TEI Header**

The decision log lives in your repository. Its formal statement belongs in the TEI
header, where a reader of the file alone can find it.

Any normalization applied to a text must be documented in the `<encodingDesc>` and
`<editorialDecl>` elements of the header (TEI Consortium, 2026):

```xml
<encodingDesc>
  <editorialDecl>
    <normalization method="markup">
      <p>Orthographic variants are encoded with <gi>choice</gi> containing
        <gi>orig</gi> and <gi>reg</gi>. Phonetic spellings arising from
        iotacism, and omitted accents and breathings, are treated as
        period-normal variants rather than errors. Mechanical slips —
        dittography, letters without phonological motivation — are encoded
        with <gi>sic</gi> and <gi>corr</gi>. Proper names are not
        regularized. Full policy and case register in
        transcription/ORTHOGRAPHY.md.</p>
    </normalization>
    <correction>
      <p>Corrections are attributed with @resp and carry @cert where the
        emendation is uncertain.</p>
    </correction>
  </editorialDecl>
</encodingDesc>
```

The reason this matters becomes acute on Friday. A future researcher must know
precisely whether a given `<reg>` was produced by a human philologist, a
deterministic script, or a neural model, because that provenance determines the
data's reliability for downstream corpus linguistics (TEI Consortium, 2026).

By Friday your text will contain regularizations from all three sources. `@resp`
distinguishes them at the element level; the header states the policy; and your
commit trailers record the provenance of each batch. All three layers of
documentation are needed, and today is when the first two are established.

**The takeaway for this page:** A future researcher must be able to tell whether a
`<reg>` came from a human, a script, or a model — which needs `@resp`, the header,
and commit trailers together.

---

## **16 Content**

**The Recommended Workflow**

The literature proposes a systematic five-stage workflow, and this week enacts it
across three meetings (Bollmann, 2019; TEI Consortium, 2026).

| Stage | Operation | When |
| --- | --- | --- |
| 1 | Diplomatic transcription capturing the text as written | Weeks 4–5 |
| 2 | Algorithmic candidate generation from a deterministic rule-based script, establishing a verifiable baseline | Wednesday |
| 3 | AI-assisted contextual disambiguation ranking the candidates | Friday |
| 4 | Human-in-the-loop auditing where confidence is low or where baseline and neural output conflict | Friday |
| 5 | TEI projection into `<choice>`, so no historical data is overwritten | Throughout |

Note that today's manual work is not in that list, and the omission is deliberate on
their part and corrected on ours. The published workflow assumes an editor who
already knows the orthographic policy. You do not yet, which is why today comes
first: you are producing the policy that stages 2 and 3 will implement and be
measured against.

This is the same structure as Weeks 4 and 5. The manual step establishes the
reference; the deterministic and AI steps are measured against it. What differs is
that here the reference is a set of *rules* rather than a text — and Wednesday's
task is to express your rules formally enough that a script can apply them.

That reformulation is genuinely difficult and is the intellectual content of
tomorrow. A policy stated as "regularize iotacism where appropriate" cannot be
implemented. A policy stated as an ordered list of context-conditioned substitutions
can be.

**The takeaway for this page:** Today produces the policy that Wednesday must state
formally enough for a script — "regularize where appropriate" cannot be implemented.

---

## **17 Content**

**Writing Rules a Script Could Follow**

Begin the reformulation today, while the cases are in front of you.

For each policy line, ask what a program would need to know. A rule has three
parts: what to match, in what context, and what to produce.

| Informal policy | Formal rule | Context condition |
| --- | --- | --- |
| Regularize iotacism | ει → ι | Where the result is in the lexicon |
| Regularize iotacism | η → ι | Where the result is in the lexicon |
| Supply missing accents | Add the accent from the lemma | Where the form is otherwise standard |
| Regularize movable nu | Add or remove final ν | Before a vowel or pause, per convention |
| Do not regularize names | Skip | Where the token is capitalized mid-sentence, or in a name list |

The "context condition" column is where the difficulty lives. A bare substitution
ει → ι applied everywhere would produce nonsense, because many words legitimately
contain ει. The rule needs a condition — most simply, that the result is an attested
form and the original is not.

Two further complications you should anticipate.

**Rules interact.** Applying ει → ι and then ι → η in sequence produces a different
result from the reverse order. Ordering matters, and an ordered rule list is a
different object from an unordered set.

**Some rules are not expressible this way.** Where a variant maps to different
standard forms depending on syntactic context, no character-level rule can
disambiguate — pure dictionary lookups and character regex fail because they process
tokens in isolation (Bollmann, 2019). Mark those cases; they are exactly what
Friday's contextual step exists for.

**The takeaway for this page:** Formal rules need a context condition, and rule
order changes the result — cases needing syntax are what Friday's step is for.

---

## **18 Content**

**Ambiguity That Rules Cannot Resolve**

Identify these cases today, because they define the boundary between Wednesday's
method and Friday's.

The classic illustration from the literature: the historical English form *ther*
could represent modern *their* or *there*, and no character-level rule distinguishes
them, because the information needed is syntactic rather than orthographic
(Bollmann, 2019).

Greek analogues you may encounter:

| Ambiguous form | Possible regularizations | Disambiguated by |
| --- | --- | --- |
| A form where ι could stand for ει or η | Two different lemmas | Syntax and sense |
| αυτου | αὐτοῦ or αὑτοῦ | Breathing; reflexive or not |
| A verb form ambiguous in number after iotacism | Singular or plural | Agreement with the subject |
| ει as conjunction or verb ending | Different words entirely | Position and construction |

For each such case in your text, record it in the decision log with a note that it
requires contextual resolution. Resolve it yourself today, by hand, and record the
reason — that resolution is the reference against which Friday's contextual
disambiguation is measured.

This is the analytical heart of the week. Wednesday's deterministic script will
handle the cases that rules can handle, and will either fail or produce a wrong
answer on these. Friday's model will attempt them with contextual information. Your
hand resolutions are what determine which of them got it right.

Count these cases. The proportion of your variants that require contextual
resolution is a real property of your text, and it predicts how much value the
Friday method can add.

**The takeaway for this page:** Cases needing syntax to resolve are the boundary
between Wednesday's method and Friday's — resolve them by hand today as the
reference.

---

## **19 Content**

**Morphological Complexity Beyond Spelling**

A case worth studying, because it shows how far a form can be from its lemma and
what is lost when the analysis fails.

In the Old Hungarian *Lament of Mary*, the scribe wrote *szegekkel* — "with nails" —
as `ſcegegkel`. Careful morphological analysis shows this is not a random
misspelling: it reflects a truncated stem where the final vowel dropped, combined
with an archaic graphical variant of the instrumental suffix undergoing place
assimilation, and a historical phonological change (Bollmann, 2019).

A naive stemmer or model processing this form without historical context might
falsely detect plurality from the medial consonant, or fail to recognize the root
*szeg*, "nail," at all.

The consequence is not merely lexical. The Hungarian poem parallels a Latin sequence
on the Passion, where the Latin variants read either *spinas*, thorns, or *clavos*,
nails. The Hungarian depends on the root *szeg*. If normalization fails and the word
is lost or mistranslated, the theological emphasis shifts from the physical
brutality of the crucifixion to the mockery of the crown of thorns (Bollmann, 2019).

That is a large interpretive consequence resting on one morphological analysis, and
it illustrates the general point: normalization errors are not typographic
inconveniences. They propagate into the meaning of the text and into any argument
built on it.

The solution used a hybrid pipeline — neural recognition to read the manuscript, a
rule-based transducer to reconstruct stem and suffix assimilation deterministically,
and a noisy channel model combining edit distance with a trigram language model to
rank candidates, with output encoded in TEI separating graphemic, phonological, and
morphological layers (Bollmann, 2019).

**The takeaway for this page:** A failed morphological normalization shifted a
poem's theological emphasis — normalization errors propagate into meaning, not just
searchability.

---

## **20 Content**

**Working Through Your Text**

Do the encoding now. A realistic target is the folio you double-keyed.

- Work through one phenomenon at a time across the whole folio, not line by line.
- Start with the most frequent pattern from your survey.
- Encode each instance with `<choice>`, `@resp`, and `@cert` where uncertain.
- Add each non-obvious case to the decision register with its reason.
- Flag cases requiring contextual resolution.
- Validate after each phenomenon rather than at the end.

Handling one phenomenon at a time is the key procedural advice. It produces
consistency almost automatically, because you are applying one judgement repeatedly
rather than switching between judgements. Working line by line invites inconsistency,
since the same phenomenon encountered twenty lines apart may be handled differently.

Count as you go. By the end you should be able to say how many regularizations you
made, of what kinds, and how many cases you could not resolve by rule. Those counts
are Wednesday's target: the script should reproduce your rule-resolvable decisions,
and its failures on the rest are expected rather than a defect.

Commit when the folio is complete:

```text
feat(normalization): regularize orthography for f. 42r

47 regularizations encoded as <choice> with <orig>/<reg>: 31 iotacism
substitutions, 12 omitted accents, 4 movable nu. 3 mechanical slips
encoded as <sic>/<corr>. 5 cases flagged as requiring contextual
resolution and resolved by hand, documented individually in
ORTHOGRAPHY.md.

All regularizations attributed @resp="#KMP".

Human-Verified: true
AI-Generated: false
```

**The takeaway for this page:** Work one phenomenon at a time across the whole
folio — consistency follows almost automatically, and line-by-line work does not
produce it.

---

## **21 Content**

**Counting for Tomorrow**

Assemble the figures Wednesday needs as its target.

| Quantity | Why Wednesday needs it |
| --- | --- |
| Total tokens in the folio | Denominator for accuracy |
| Total regularizations made | What the script should reproduce |
| Regularizations by rule type | Per-rule accuracy targets |
| Cases requiring context | Expected script failures |
| Mechanical errors encoded | Should not be touched by the script |
| Tokens deliberately left alone | Script must not over-apply |

The last row is the one students forget and the one that matters most for
evaluation. A script that regularizes everything it can will also regularize things
it should not — a standard form that happens to be reachable by an iotacism rule, a
proper name, a genuine variant reading. Measuring only whether the script found your
regularizations misses that failure entirely.

Tomorrow's evaluation therefore needs both directions:

- **Recall.** Of the regularizations you made, how many did the script make?
- **Precision.** Of the regularizations the script made, how many were correct?

A script with perfect recall and poor precision is worse than useless, because
correcting its over-applications costs more than making the regularizations by hand.
This is the same threshold logic as Lesson 4.2 section 14, applied to a different
operation.

Record both sets of counts today so tomorrow's measurement is straightforward.

**The takeaway for this page:** Record what you deliberately left alone — a script
is evaluated on precision as well as recall, and over-application is the worse
failure.

---

## **22 Content**

**Checklist Before You Leave**

Verify each.

- Consensus text surveyed for all non-standard forms.
- Variation patterns catalogued with frequencies.
- Policy written in `transcription/ORTHOGRAPHY.md`.
- Each policy line expressed formally enough to implement, or marked as requiring context.
- Regularizations encoded with `<choice>`, `<orig>`, `<reg>`.
- Mechanical errors encoded with `<sic>`, `<corr>`.
- `@resp` on every regularization.
- `@cert` where the regularization is uncertain.
- Contextually ambiguous cases resolved by hand and documented.
- Nothing regularized inside `<unclear>`.
- No proper names regularized.
- No variant readings resolved.
- TEI header `<editorialDecl>` documenting the policy.
- Counts recorded for tomorrow, including tokens left alone.
- File validates against the TEI schema.
- Committed with provenance trailers.
- State tagged for tomorrow's comparison.

Tag today's state, because Wednesday's script will be measured against it:

```bash
git tag -a norm-manual-f42r -m "Manual normalization reference, f. 42r"
```

**The takeaway for this page:** Tag today's state — Wednesday's script is measured
against it, and it must remain retrievable after the script modifies the text.

---

## **23 Content**

**Common Problems Today**

Failures that recur.

| Symptom | Cause | Remedy |
| --- | --- | --- |
| Same phenomenon encoded two ways | Worked line by line rather than by phenomenon | Sweep by phenomenon |
| `<orig>`/`<reg>` used for a clear slip | Policy boundary not applied | Check against the section 07 criteria |
| `<sic>`/`<corr>` used for iotacism | Treating period-normal spelling as error | Check phonological motivation |
| Regularization changes morphology | Crossed from orthography into grammar | Revert; note the form instead |
| `<choice>` spanning several words | Encoded at phrase level | Re-encode word by word |
| Proper name regularized | Over-application | Revert; add to the do-not-touch list |
| A variant reading "corrected" | Confused normalization with emendation | Revert; reserve for Week 8 |
| Schema validation fails | `<choice>` in an invalid position | Check the content model |

The fourth and seventh rows are the substantive errors, as against the procedural
ones. Both involve doing more than normalization is licensed to do: changing the
morphology alters the linguistic evidence, and resolving a variant reading pre-empts
the collation Week 7 exists to perform.

If you find you have done either, revert rather than patching. Both are cases where
the correct state is the unmodified original with a note, and reconstructing that
from a partial correction is harder than starting again from the tagged consensus.

**The takeaway for this page:** Changing morphology or resolving variant readings
both exceed what normalization licenses — revert rather than patch.

---

## **24 Content**

**Preparing for Wednesday**

Bring:

- The normalized text, validated, committed, and tagged.
- The decision log with policy and case register.
- Policy lines expressed as formal rules where possible.
- The list of contextually ambiguous cases.
- All counts from section 21.
- Python available and working.

Wednesday implements your rules as a deterministic script and measures its output
against today's manual work. The intellectual task is the formalization: turning
"regularize iotacism where the result is a real word" into an ordered, conditioned,
executable rule set.

Expect the formalization to expose imprecision in your policy. A rule you thought
was clear will turn out to have unstated conditions, and discovering that is part of
the exercise — it means the policy was less determinate than it appeared, which is
worth knowing about your own editorial practice.

Come prepared to revise today's decisions. If implementing a rule reveals that you
applied it inconsistently, the remedy is to fix the inconsistency in the text and
amend the policy, not to weaken the rule until it matches what you happened to do.

**The takeaway for this page:** Formalizing your rules will expose imprecision in
them — that discovery is the point, and the remedy is fixing the text rather than
weakening the rule.

---

## **25 Content**

**What Good Work Looks Like Here**

The standard.

A minimally acceptable result is a normalized text with `<choice>` markup that
validates.

Good work additionally:

- Surveys the variation systematically before encoding, with frequency counts.
- States a policy that covers the observed phenomena.
- Distinguishes `<orig>`/`<reg>` from `<sic>`/`<corr>` on stated criteria.
- Applies the distinction consistently across the whole text.
- Documents each non-obvious case with its reasoning.
- Identifies and flags cases that rules cannot resolve.
- Declines to regularize names, morphology, and variant readings.
- Records the policy in the TEI header as well as the repository.
- Attributes every regularization with `@resp`.
- Records counts in both directions for tomorrow's evaluation.

The sixth item is what makes today's work usable tomorrow, and the seventh is what
makes it defensible. An edition that regularizes conservatively and documents its
boundaries is one whose editorial policy a reader can evaluate. An edition that
regularizes freely produces a cleaner text and a weaker claim, because a reader
cannot tell what was changed or on what principle.

**The takeaway for this page:** Conservative regularization with documented
boundaries produces a weaker-looking text and a stronger claim.

---

## **26 Content**

**Why the Manual Step Is First, Again**

The reason is the same as in Weeks 4 and 5, and it is worth restating because the
object has changed.

In Week 4 the manual step produced a reference *text*. Here it produces a reference
*policy* — a set of decisions about how variation should be treated, with worked
examples.

Both are references in the same sense. Wednesday's script cannot be evaluated
without knowing what the right answer is, and the right answer for normalization is
not given by the manuscript alone: it depends on editorial judgement about what
counts as a variant, what counts as an error, and what should be left alone. Only a
human editor can supply that judgement, and having supplied it, they hold the
standard.

There is a further reason specific to this operation. Normalization decisions are
*policy* decisions with corpus-wide consequences. Deciding that omitted accents are
period-normal variants rather than errors affects every instance in the edition, and
such a decision made ad hoc by a script — or by a model, in the absence of stated
policy — is a decision nobody made deliberately.

That is the deeper argument for today. It is not only that a reference is needed for
measurement. It is that the editorial policy of your edition should be authored
rather than emergent.

**The takeaway for this page:** Normalization policy has corpus-wide consequences,
so it should be authored deliberately rather than emerging from whatever a script or
model happens to do.

---

## **27 Content**

**Connecting to the Weeks Around It**

Where this fits.

| Week | Relation to normalization |
| --- | --- |
| 4–5 | Produced the diplomatic base being normalized |
| 6 | Adds the regularized layer in parallel |
| 7 | Collation must choose which layer to align on |
| 8 | Apparatus distinguishes orthographic from substantive variants |
| 9 | Lemmatization operates on the `<reg>` layer |
| 12 | Commentary may discuss orthography as evidence |
| 13 | Publication offers both layers to the reader |

Row 7 is the immediate consequence and worth thinking about now. Next week you
collate two witnesses. If you collate on the `<orig>` layer, every difference of
phonetic spelling between the witnesses appears as a variant, and the apparatus will
be swamped with orthographic noise. If you collate on `<reg>`, orthographic
differences vanish and only substantive variants appear — but genuine evidence about
the relationship between the witnesses may vanish with them, since shared spelling
practice can indicate shared descent.

The usual answer is to collate on `<reg>` for the main apparatus and to analyze
`<orig>` separately for what it says about transmission. That is a decision to make
deliberately next week, and it is available only because both layers exist.

Row 9 explains why the `<reg>` layer earns its cost. Morphological parsers require
standard forms, and lemmatization on unnormalized text fails on exactly the forms
that iotacism produced.

**The takeaway for this page:** Next week's collation must choose a layer — `<reg>`
for substantive variants, `<orig>` for evidence of shared descent — and the choice
exists only because both layers do.

---

## **28 Content**

**A Note on Scale**

An honest observation about what this method costs.

Manual normalization guarantees high precision and deep contextual understanding,
and is fundamentally unscalable for large corpora (Robinson & Driscoll, 2016). You
have normalized one folio. A full manuscript would take many times longer, and a
corpus is out of reach entirely.

That is the motivation for Wednesday and Friday. The automated methods exist because
the manual method does not scale, and the question this week answers is how much of
the manual method's quality they retain.

| Method | Precision | Scale | Transparency |
| --- | --- | --- | --- |
| Manual philology | Highest | Lowest | Complete, if documented |
| Rule-based script | Verifiable | High | Complete |
| Neural sequence models | Good with data | High | Limited |
| Language models | Contextually strong | High | Poor |

Read the transparency column. It is the one that matters most for a scholarly
edition and the one that degrades fastest. A rule-based transformation is
mathematically quantifiable and can be logged in the header: when a transducer maps
a form, the exact rule applied is known (Bollmann, 2019). A neural normalization is
a number that came out of a model.

This is why Wednesday precedes Friday, and why the rule-based baseline is not merely
a weaker alternative to the neural method. It is the *verifiable* method, and its
role on Friday is to serve as the transparent standard against which the opaque one
is checked.

**The takeaway for this page:** Rule-based normalization is transparent and neural
normalization is not — which makes the rule baseline the check on the model, not
merely a weaker alternative.

---

## **29 Content**

**The Log as a Scholarly Document**

A closing note on the decision log, which is easy to treat as bookkeeping.

It is the statement of your edition's editorial policy. When a reader asks why a
particular form was regularized and another was not, the log is the answer. When a
later scholar wants to redo your analysis with different assumptions, the log tells
them what your assumptions were. When you yourself return in December to write the
commentary, it is the record of reasoning you will otherwise have to reconstruct.

Printed editions carry this document too, as the editorial introduction — the
section explaining the editor's treatment of orthography, punctuation, and
abbreviation, which readers routinely skip and specialists read carefully. Yours
differs only in being maintained as work proceeds rather than written afterwards,
which makes it more accurate.

It also differs in being *queryable*. A case register recording every non-obvious
decision with its line reference is something a reader can search, and a printed
introduction is not.

Write it accordingly. Not "regularized iotacism where needed," but a policy with
stated criteria, a case register with individual reasoning, and an explicit list of
what was deliberately left alone.

**The takeaway for this page:** The decision log is your edition's editorial
introduction, written as you work rather than reconstructed afterwards — and
queryable in a way a printed one is not.

---

## **30 Content**

**Synthesis: Both Layers, Explicitly Related**

The argument of this meeting.

Historical spelling varies, and the variation is simultaneously an obstacle and
evidence. It obstructs every computational operation that assumes standard
orthography — search, parsing, lexical lookup. And it records dialect, education,
date, and language contact, and in cases like the Sinaiticus dictation debate it is
the evidence on which a question of transmission turns (Gignac, 1976; Robinson &
Driscoll, 2016).

Print editions resolved the tension by choosing: they standardized, and the evidence
was lost. TEI resolves it by refusing to choose — `<choice>` holds both encodings as
parallel alternatives, and downstream consumers select the layer suited to their
purpose (TEI Consortium, 2026).

Making that work requires an editorial judgement TEI cannot supply: which variation
is period-normal usage and which is scribal error, `<orig>`/`<reg>` against
`<sic>`/`<corr>`. That judgement is genuinely contestable, which is why it must be
stated as policy, applied consistently, and documented case by case.

Today you produced that policy. It is the reference for the rest of the week, in
exactly the sense that Week 4's transcription was: the automated methods will be
measured against it, and only a human editor could have produced it.

**For Wednesday.** Bring the six items in section 24. You will implement your policy
as a deterministic script and measure it against today's work — recall and
precision both.

**The takeaway for this page:** TEI keeps both layers, but deciding which variation
is usage and which is error is editorial judgement no standard supplies — that
judgement is today's product.

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
