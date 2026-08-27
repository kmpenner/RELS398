# Lesson 4.1 — Diplomatic Transcription by Hand: Building the Ground Truth

*RELS 398 / ENGL 398 · Topic 4: Transcription · Meeting #9 (Tue Sep 22)*

***Step 1 of the three-step cycle: manual.** Today you transcribe by hand, in a
plain text editor, at full zoom. What you produce is the ground truth against
which Wednesday's HTR model and Friday's LLM output will be measured in Week 5.*

---

## **01 Content**

**Why the Manual Step Comes First**

This week runs the same passage three ways: by hand today, through a trained HTR
model on Wednesday, and with LLM assistance on Friday. The order is not
arbitrary, and it is not a concession to tradition.

Wednesday and Friday produce output that must be *evaluated*. Evaluation requires
a reference — a transcription known to be correct, against which machine output
can be scored. Without it, an HTR model's output is simply text: plausible,
possibly accurate, impossible to assess. Character error rate, word error rate,
and every other metric in Week 5 are computed as a distance from a reference, and
the reference is what you produce today (AlKendi et al., 2024).

The thesis this week substantiates is that automated transcription — HTR and
vision-language models alike — fundamentally requires human diplomatic
transcription as an authoritative baseline. It is exclusively against that
baseline that error rates, algorithmic biases, and hallucinated readings can be
measured, evaluated, and mitigated (AlKendi et al., 2024).

There is a second reason, less obvious and equally important. Transcribing by
hand is how you learn what your manuscript actually contains — which letterforms
this scribe uses, which abbreviations recur, where the hand becomes difficult,
where the parchment is damaged. Wednesday you will correct an algorithm's layout
analysis and judge its output. You cannot do either without having read the page
yourself first.

**Vocabulary.** *Ground truth* — a transcription verified as correct, used as the
reference for measuring automated output. *Character error rate (CER)* — the
proportion of character-level edits needed to transform machine output into the
ground truth.

**Takeaway:** Today's transcription is the measuring instrument
for the rest of the term — every error rate you compute is a distance from it.

---

## **02 Content**

**Diplomatic Versus Normalized Transcription**

Two transcription conventions serve different purposes, and confusing them
produces a document that serves neither.

A **diplomatic transcription** reproduces the surface features of the manuscript
as precisely as the medium allows: original spelling, historical punctuation,
capitalization as written, word division as written, variant letterforms, line
divisions, and unexpanded scribal abbreviations. Its commitment is to what is on
the parchment (AlKendi et al., 2024).

A **normalized** or **interpretative transcription** modernizes orthography,
silently expands abbreviations, and regularizes punctuation to make the text
readable for a contemporary audience. Its commitment is to the text as a
linguistic object rather than to the page as an artefact (AlKendi et al., 2024).

| Feature | Diplomatic | Normalized |
| --- | --- | --- |
| Spelling | As written, including errors | Regularized |
| Abbreviations | Left unexpanded, or marked | Silently expanded |
| Punctuation | As in the manuscript | Modern conventions |
| Word division | As written, including *scriptio continua* | Modern word spacing |
| Line breaks | Preserved and recorded | Not preserved |
| Letterforms | Variants distinguished | Merged |
| Serves | Palaeography; HTR training; textual criticism | Reading; translation; teaching |

Today's transcription must be **diplomatic**. The reason is specific to what it
will be used for: an HTR model trained on normalized text learns to produce
normalized text, which means it learns to silently overwrite the historical record
with modern assumptions. Models trained on normalized ground truth tend to
over-normalize when they meet new material, and the resulting errors are invisible
because the output looks like clean text (AlKendi et al., 2024).

Normalization is Week 6's subject, and it is done *from* a diplomatic base, with
each decision recorded. Doing it now, silently, destroys the evidence Week 6 needs.

**Takeaway:** Transcribe diplomatically, because a model trained
on normalized text learns to silently modernize — and Week 6 needs the
unnormalized base.

---

## **03 Content**

**The Ordered Hierarchy and What TEI Assumes**

Encoding your transcription in TEI commits you to a particular model of what a
text is, and it is worth knowing what you are committing to.

TEI XML operates on the theoretical model of an **Ordered Hierarchy of Content
Objects** — the assumption that a text is a single nested tree: a work contains
divisions, which contain paragraphs, which contain sentences, which contain words
(AlKendi et al., 2024). XML enforces this: elements must nest properly, and
overlapping structures cannot be expressed directly.

Manuscripts routinely violate the assumption. The physical structure of the page —
folios, columns, lines — and the logical structure of the text — books, chapters,
sentences — are both real and they do not nest within each other. A sentence
begins mid-line and ends on the next page. A verse spans a column break. Neither
hierarchy contains the other.

TEI's solution is the **empty milestone element**. Rather than wrapping content,
`<pb/>` and `<lb/>` mark points in the stream:

```xml
<p>ἐν ἀρχῇ ἦν ὁ λόγος καὶ ὁ λόγος<lb n="2"/>
ἦν πρὸς τὸν θεόν καὶ θεὸς ἦν ὁ<lb n="3"/>
λόγος οὗτος ἦν ἐν ἀρχῇ<pb n="42v"/>
πρὸς τὸν θεόν</p>
```

The paragraph nests properly as XML requires; the line and page boundaries are
recorded as points within it. Physical structure is captured without competing
with the logical hierarchy.

This is why line breaks are preserved in a diplomatic transcription rather than
being treated as typographic accident. The line is a real feature of the artefact,
it is where HTR operates, and it is where your zone bindings from Lesson 3.3
attach.

**Takeaway:** Physical and logical structure both exist and do
not nest, so TEI records line and page boundaries as empty milestones within the
logical hierarchy.

---

## **04 Content**

**The Core Encoding Vocabulary**

A diplomatic transcription needs a small set of TEI elements used consistently.
Learn these; they cover the great majority of what you will encounter (TEI
Consortium, 2026; AlKendi et al., 2024).

| TEI element | Records | Example |
| --- | --- | --- |
| `<pb/>` | Page or folio beginning | `<pb n="42v" facs="#f42v"/>` |
| `<lb/>` | Line beginning | `<lb n="8" facs="#f42r_l08"/>` |
| `<cb/>` | Column beginning | `<cb n="b"/>` |
| `<abbr>` | An abbreviation as written | `<abbr>θς</abbr>` |
| `<expan>` | The expanded form | `<expan>θεός</expan>` |
| `<choice>` | Wraps alternative encodings | `<choice><abbr/><expan/></choice>` |
| `<orig>` | The original form | `<orig>ἐγένετο</orig>` |
| `<reg>` | The regularized form | `<reg>ἐγένοντο</reg>` |
| `<unclear>` | Text that cannot be read confidently | `<unclear reason="faded"/>` |
| `<gap/>` | Missing or illegible material | `<gap reason="lacuna" extent="3" unit="chars"/>` |
| `<damage>` | A physically damaged region | `<damage agent="water"/>` |
| `<supplied>` | Text supplied by the editor | `<supplied reason="lacuna"/>` |
| `<del>` | Text deleted by a scribe | `<del rend="strikethrough"/>` |
| `<add>` | Text added by a scribe | `<add place="above"/>` |

The `<choice>` element is the structurally interesting one and deserves attention.
It does not *choose*; it holds alternatives so that a processor can select
according to purpose. A reading view renders the `<expan>`; a palaeographic view
renders the `<abbr>`; a search index may include both. One encoding serves several
presentations, which is exactly what separating data from presentation buys you
(AlKendi et al., 2024).

Today you will use `<pb/>`, `<lb/>`, `<unclear>`, `<gap/>`, and `<choice>` with
`<abbr>`/`<expan>` most heavily. Reserve `<orig>`/`<reg>` for Week 6 — recording
regularizations now would pre-empt decisions that week exists to make deliberately.

**Takeaway:** `<choice>` holds alternatives rather than deciding
between them, so one encoding can serve palaeographic, reading, and search views.

---

## **05 Content**

**Encoding Abbreviations**

Scribal abbreviation is pervasive in manuscript culture and is where diplomatic
transcription is most often done badly. Silently expanding abbreviations is the
single most common way students destroy the evidential value of a transcription.

The problem: an abbreviation is a mark on the page, and its expansion is an
editorial inference. Usually the inference is secure — a *nomen sacrum* with an
overline is unambiguous. Sometimes it is not, and a given abbreviation may admit
several expansions whose choice affects the sense.

Encode both:

```xml
<choice>
  <abbr>θς</abbr>
  <expan>θε<ex>ό</ex>ς</expan>
</choice>
```

The `<ex>` element inside `<expan>` marks specifically the characters *supplied by
the editor* rather than present in the manuscript. This is a real distinction: it
allows a processor to render the expansion with the supplied letters italicized,
which is the traditional print convention, and it records exactly where the ink
stops and the inference begins.

| Abbreviation type | Manuscript form | Encoding approach |
| --- | --- | --- |
| Nomen sacrum | Contracted with overline | `<abbr>` plus `<expan>` with `<ex>` |
| Suspension | Word truncated, mark added | Same |
| Contraction | Medial letters omitted | Same |
| Tironian *et* | A symbol standing for a word | `<abbr>` plus `<expan>` |
| Ambiguous expansion | Several readings possible | `<expan cert="medium">`, note alternatives |

For HTR training this encoding is directly consequential. The model must learn to
associate the *visual* form with the *diplomatic* characters, not with the
expansion. Where training data supplies expansions in place of the written form,
the model learns to hallucinate letters that are not on the page — which is
precisely the over-normalization failure described in section 02 (AlKendi et al.,
2024).

**Takeaway:** Encode the abbreviation and its expansion
separately with `<ex>` marking supplied letters, so the model learns what is
actually on the page.

---

## **06 Content**

**Encoding Uncertainty and Damage**

A diplomatic transcription must state the limits of decipherment explicitly. A
reading given without qualification asserts confidence, and asserting confidence
you do not have is a scholarly error regardless of whether the reading is right
(AlKendi et al., 2024).

Four distinct situations require four distinct encodings:

| Situation | Element | Meaning |
| --- | --- | --- |
| I can see marks but cannot read them confidently | `<unclear>` | A reading is offered with reduced confidence |
| Material is missing or wholly illegible | `<gap/>` | No reading is offered |
| The support is damaged, whether or not text is lost | `<damage>` | Documents a physical cause |
| I have supplied text not present in the witness | `<supplied>` | An editorial restoration |

The distinction between `<unclear>` and `<gap/>` is the one to get right.
`<unclear>` contains a reading — you are proposing text, with reduced confidence.
`<gap/>` is empty — you are proposing nothing and recording that something is
missing. Putting a guess inside a `<gap/>` misrepresents an inference as an
absence; leaving `<unclear>` empty misrepresents a difficult reading as a lacuna.

Qualify richly:

```xml
<unclear reason="faded" cert="medium" resp="#KMP"
         source="#uv365">ἐγένετο</unclear>
<gap reason="lacuna" extent="4" unit="chars"/>
<damage agent="water" extent="lower margin"/>
```

The `@source` attribute connects to Lesson 3.2: it records which imaging condition
supported the reading. `@resp` records who is responsible. `@extent` on a `<gap/>`
records how much is missing, which matters for restoration — a four-character
lacuna constrains the possibilities far more than an unmeasured one.

Be honest and be specific. In Week 5 these encodings become the record of which
readings were genuinely uncertain, and a transcription that marks nothing as
unclear will produce error rates that are wrong in an uninterpretable direction.

**Takeaway:** `<unclear>` proposes a reading with reduced
confidence and `<gap/>` proposes nothing — conflating them misrepresents inference
as absence or difficulty as loss.

---

## **07 Content**

**Scribal Corrections**

Manuscripts record their own editing. Scribes deleted, added, and corrected, and
those interventions are evidence about transmission — often the most informative
evidence a single witness offers.

| Feature | Element | Attributes to record |
| --- | --- | --- |
| Deletion | `<del>` | `@rend` — strikethrough, expunction, erasure |
| Addition | `<add>` | `@place` — above, below, margin, inline |
| Substitution | `<subst>` wrapping `<del>` and `<add>` | Groups a correction as one act |
| Correction by another hand | `@hand` on the element | Points to a hand in the header |
| Text left standing though marked | `<del>` retained in the reading | Note the decision |

A substitution encoded properly:

```xml
<subst>
  <del rend="strikethrough">ἐγένετο</del>
  <add place="above" hand="#hand2">ἐγένοντο</add>
</subst>
```

This records more than the final text. It records that a correction occurred, in
which direction, and by which hand — and a second hand correcting the first is
evidence of a reader or a corrector at work, which bears on the manuscript's
history and possibly on its relation to other witnesses.

Note what a normalized transcription would produce here: `ἐγένοντο`, with the
correction invisible. The final text is the same and the evidence is gone. This is
the concrete cost of normalizing at the transcription stage, and it recurs
throughout the week.

Record corrections carefully today. In Week 7, when you collate witnesses, a
correction in one witness that agrees with another witness's uncorrected reading
is exactly the kind of evidence that establishes a relationship between them.

**Takeaway:** Scribal corrections are transmission evidence, and
recording only the corrected text destroys it while leaving the reading unchanged.

---

## **08 Content**

**Line Breaks and Why They Matter Here**

In a normalized transcription line breaks are typographic accident. In this
transcription they are structural, for three separate reasons.

First, **HTR operates on lines.** Layout analysis segments the page into lines,
and recognition runs per line. Training data must therefore be line-aligned:
each line image paired with its transcribed text (Puigcerver, 2017). A
transcription without line divisions cannot be used for training at all.

Second, **your zone bindings are per line.** Lesson 3.3 established `<lb>` elements
carrying `@facs` pointing at zones. Those bindings are what let a reading be
checked against the parchment, and they presuppose that lines are recorded.

Third, **line division is codicological evidence.** Where a line breaks tells you
about the scribe's practice, the ruling, and sometimes about the exemplar — a
scribe copying line-for-line from an exemplar produces breaks that carry
information about the source.

```xml
<lb n="1" facs="#f42r_l01"/>ἐν ἀρχῇ ἦν ὁ λόγος καὶ ὁ λό
<lb n="2" facs="#f42r_l02"/>γος ἦν πρὸς τὸν θεόν
```

Note the word broken across lines — `λό` / `γος` — recorded as written, without
hyphenation and without silently joining. Scribes broke words freely, and the
break is a fact about the page. Whether to mark the continuation with `@break="no"`
on the `<lb/>` is a convention decision; make one and apply it consistently, since
inconsistency here confuses both HTR training and any later tokenization.

Number your lines from 1 on each folio, matching the numbering in your zones.
Consistency between the two is what makes the bindings checkable.

**Takeaway:** Line divisions are structural here — HTR trains on
lines, your zones bind per line, and line breaks are codicological evidence.

---

## **09 Content**

**Setting Up the Transcription Document**

Build the file before transcribing. A structure established now saves
reorganization later.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
    <!-- Your Week 2 header goes here -->
  </teiHeader>
  <facsimile>
    <!-- Your Lesson 3.3 surfaces and zones go here -->
  </facsimile>
  <text>
    <body>
      <div type="passage" n="1">
        <pb n="42r" facs="#f42r"/>
        <lb n="1" facs="#f42r_l01"/>
      </div>
    </body>
  </text>
</TEI>
```

Three checks before you start typing. Confirm the file is declared UTF-8 and that
your editor is actually saving UTF-8 — a mismatch here corrupts every Greek
character and is tedious to repair. Confirm the TEI schema is associated so that
validation is live. And confirm your pre-commit normalization hook from Week 1 is
installed, since you are about to generate a large quantity of polytonic Greek and
you want it normalized to NFC from the start.

That last point is not hypothetical. Your input method may produce NFD, as Lesson
1.2 section 12 discussed, and a ground truth in mixed normalization forms will
produce meaningless error rates in Week 5. Test the hook now: type a
multi-diacritic character, commit, and confirm the committed bytes are NFC.

Commit the skeleton before transcribing, so that the transcription itself appears
as a clean diff.

**Takeaway:** Verify UTF-8, live schema validation, and the NFC
hook before typing — a mixed-normalization ground truth invalidates Week 5.

---

## **10 Content**

**Transcription Method: Working at Full Zoom**

The mechanics matter more than students expect, and the commonest source of error
is working too fast at too low a magnification.

Establish a routine:

- Open the folio in your IIIF viewer at a zoom where individual letterforms are unambiguous — this is generally much closer than feels necessary.
- Transcribe one line at a time, left to right, resisting the urge to read ahead.
- Type what you see, not what you expect the text to say.
- Mark uncertainty immediately rather than resolving it by guessing.
- At the end of each line, compare your transcription against the image once more.
- Every five lines, verify you are still on the line you think you are.

The third item is the discipline that distinguishes transcription from reading. If
you know the text — and for a well-known work you may — you will read what you
expect rather than what is written, and you will not notice. This is precisely how
genuine variants get transcribed away, and it is the single largest threat to your
ground truth's accuracy.

A counter-technique worth using: transcribe a difficult passage backwards, word by
word from the end of the line. It is slower and it disrupts the linguistic
prediction that causes expectation errors. Reserve it for lines where you suspect
you are reading rather than seeing.

The sixth item guards against line skip, which is the error that produces the
worst downstream consequences. A skipped line puts every subsequent line out of
alignment with its zone, so all your bindings become wrong from that point.
Because the transcription still reads correctly, nothing looks broken.

**Takeaway:** Type what you see rather than what you expect, and
check your line position regularly — line skip silently invalidates every binding
after it.

---

## **11 Content**

**Recognizing the Hand**

Before transcribing at volume, spend time characterizing the hand. Fifteen minutes
here saves hours of misreading.

Work through the alphabet systematically. For each letter, find several clear
instances and note how this scribe forms it. Pay particular attention to letters
that are commonly confused in the script you are reading, and record the
distinguishing features you can rely on.

| Feature to characterize | Question to answer |
| --- | --- |
| Letterform inventory | How does this scribe form each letter? |
| Confusable pairs | What distinguishes them in this hand? |
| Ligatures | Which letter combinations are joined, and how? |
| Abbreviation repertoire | Which abbreviations recur, and what do they mean? |
| Punctuation | What marks are used, and what do they signify? |
| Accent placement | Where are accents placed relative to the letter? |
| Word division | Is it consistent, absent, or irregular? |
| Line-end behaviour | Are words broken? Is there compression? |

Byzantine Greek presents specific difficulties worth anticipating. The script
frequently uses *scriptio continua*, with no clear word boundaries. It employs
extensive networks of enclitic ligatures. It has hanging lines, where characters
descend below the ruled baseline rather than sitting on it. And its polytonic
accentuation involves at least five distinct accent characters in multiple
vertical combinations (Perdiki & Konstantinidou, 2023).

Record your findings as a document in the repository — `transcription/HAND.md` is
a reasonable location. It serves three purposes: it disciplines your reading, it
documents your palaeographic reasoning for your Week 12 commentary, and it is what
you will consult on Wednesday when judging whether an HTR error reflects the model
or the hand.

**Takeaway:** Characterize the hand before transcribing at
volume, and record it — you will consult it on Wednesday to judge HTR errors.

---

## **12 Content**

**Diacritics and the Polygon Problem**

A specific issue that will matter on Wednesday and is worth understanding today.

Greek polytonic accents and breathings sit *above* the letter, sometimes well
above it. In a manuscript hand with generous accent placement, a breathing may
rise substantially above the main body of the line.

HTR layout analysis draws a polygonal envelope around each detected line — a
boundary computed from the baseline and the extent of ascenders and descenders. If
that polygon is drawn too tightly, accents and breathings positioned high above
the line fall outside it and are simply not present in the image the recognizer
sees (Perdiki & Konstantinidou, 2023).

The consequence is systematic and initially baffling: the model reads the letters
correctly and omits the diacritics, producing text that is right in its
consonants and vowels and wrong in exactly the features that Lesson 1.2 spent a
meeting establishing as significant.

Perdiki and Konstantinidou (2023) report this directly. In their Byzantine Greek
work, automated layout analysis frequently omitted breathings and suffix
abbreviations placed high above the line, and achieving a character error rate
below 10% required manually adjusting the polygon envelopes during ground truth
preparation to ensure peripheral diacritics were captured.

For today, this means two things. Transcribe every diacritic accurately, since
they are exactly what the model will be tested on. And note, as you work, how high
above the line this scribe places accents — because tomorrow you will be adjusting
polygons, and knowing how much vertical margin the hand requires tells you what to
adjust them to.

**Takeaway:** Layout polygons drawn too tightly cut off Greek
accents entirely, so note how high this hand places diacritics — you will adjust
for it tomorrow.

---

## **13 Content**

***Scriptio Continua* and Word Boundaries**

If your manuscript is written without word division, a decision must be made
explicitly today rather than by default.

*Scriptio continua* — continuous writing without spaces — is standard in early
Greek manuscripts and common in Byzantine hands. The text runs as an unbroken
sequence of letters, and word division is supplied by the reader.

This creates a genuine conflict for diplomatic transcription. Reproducing the
manuscript faithfully means writing without spaces. But an unspaced transcription
is barely usable for collation, tokenization, or lemmatization — and word division
is an interpretive act that a diplomatic transcription is supposed to avoid making
silently.

| Approach | Diplomatic fidelity | Downstream usability |
| --- | --- | --- |
| Reproduce unspaced | Complete | Poor; requires later segmentation |
| Insert spaces silently | Compromised; unrecorded intervention | Good |
| Insert spaces, record the practice in the header | Acceptable; the intervention is declared | Good |
| Encode both with `<choice>` | Complete | Good; verbose |

The third is the standard compromise and what this course recommends: divide
words, and state in your header that word division has been supplied by the editor
and is not present in the witness. The intervention is then declared rather than
concealed, which is the actual requirement.

Be aware of the downstream consequence for HTR. Perdiki and Konstantinidou (2023)
found that *scriptio continua* confounds automated tokenizer metrics — the system
correctly recognizes individual characters but fuses them into meaningless
concatenated tokens, so that ἀλλὰ τί emerges as ἀλλατι. Character error rate
remains low while word error rate becomes uninterpretable, and downstream
word-boundary detection is required.

If this applies to your manuscript, expect Week 5's WER to behave oddly and know
why.

**Takeaway:** Supply word division and declare it in the header
— and expect *scriptio continua* to make word error rate uninterpretable in Week 5.

---

## **14 Content**

**Consistency and the Transcription Convention Document**

Every transcription requires dozens of small conventional decisions, and the
danger is not making them badly but making them inconsistently.

Questions you will face repeatedly:

- Do you distinguish sigma variants — lunate, medial, final — or normalize them?
- Do you record accents that are ambiguously placed between two letters?
- How do you treat a mark that may be punctuation or may be an accent?
- Do you record scribal punctuation exactly, or map it to modern equivalents?
- At what confidence threshold does a reading become `<unclear>`?
- Do you mark word-final breaks across lines with `@break="no"`?
- How do you handle a correction whose original reading is illegible?

Answer each once, write the answer down, and follow it. The document —
`transcription/CONVENTIONS.md` — is part of your edition, and in Week 13 it becomes
the editorial statement that a reader needs in order to interpret your text.

Inconsistency is more damaging than any particular choice. A transcription that
records lunate sigma consistently is interpretable; one that records it sometimes
is not, because a reader cannot tell whether an unmarked instance means the scribe
used a different form or means you did not notice. The same applies to the HTR
model, which will learn whatever inconsistency you supply and reproduce it
unpredictably.

The CATMuS project makes exactly this point at scale: its value derives from
enforcing a uniform framework for semi-diplomatic transcription across 200
manuscripts, balancing visual diversity by merging variant character
representations while preserving crucial scribal abbreviations (Clérice et al.,
2024). Uniformity of convention is what made a 160,000-line dataset trainable.

**Takeaway:** Write your conventions down and follow them —
inconsistency is worse than any particular choice, for readers and for models
alike.

---

## **15 Content**

**Double-Keying and Accuracy**

How accurate is a hand transcription? Less than transcribers believe, and the
gap matters because Week 5 treats yours as correct.

Single-pass manual transcription typically contains errors at a low but non-zero
rate. The errors are not random: they cluster on unfamiliar letterforms,
abbreviations, damaged regions, and — critically — on passages where the
transcriber knew the text and read rather than saw.

The established remedy is **double-keying**: the same text transcribed
independently twice, with the two versions compared and every difference
adjudicated. Differences localize errors precisely, since a point where two
independent transcriptions agree is very likely correct, and a point where they
disagree is exactly where attention is needed.

| Method | Typical accuracy | Cost |
| --- | --- | --- |
| Single pass | Good, with clustered errors | Baseline |
| Single pass plus proofread | Better | Roughly 1.3× |
| Double-keyed, differences adjudicated | Substantially better | Roughly 2.2× |
| Double-keyed by two people | Best | 2× plus coordination |

This is Week 5's subject — Tuesday of that week is double-keying and consensus
text building by hand — so you are not doing it today. Knowing it is coming should
shape how you work now: transcribe carefully enough that the second pass finds
few differences, and mark uncertainty honestly so that the adjudication has
something to work with.

It should also temper how you interpret Week 5's error rates. A machine transcription
scored against a ground truth containing errors is scored against a moving target,
and some apparent machine errors will be your errors. Week 5's reconciliation
exists partly to find those.

**Takeaway:** Your ground truth will contain errors, which is why
Week 5 double-keys it — transcribe now so that the second pass finds few
differences.

---

## **16 Content**

**How Much to Transcribe Today**

A realistic target, since the temptation is to transcribe everything and the
consequence is transcribing everything badly.

Aim for **one folio, fully and carefully**, with complete encoding. If your
passage is short and your hand is clear, you may finish more. Do not sacrifice
care for coverage: an accurately transcribed folio is a usable ground truth, while
three carelessly transcribed folios are a liability, because they will teach the
model your errors.

| Priority | Task | Rationale |
| --- | --- | --- |
| 1 | One folio transcribed completely and accurately | The minimum viable ground truth |
| 2 | Encoding complete: abbreviations, uncertainty, corrections | What makes it diplomatic |
| 3 | Zones bound for every line | Enables verification |
| 4 | Conventions document written | Enables consistency |
| 5 | Hand characterization recorded | Informs Wednesday's judgements |
| 6 | Further folios | Useful; not at the cost of 1–5 |

For HTR training you will eventually need more than one folio. Transfer learning
from an existing base model can reach usable error rates with as few as 50 to 100
pages of new ground truth, and for a fine-tuning task on a single hand rather
less — but more than one folio (Geelhaar, 2022; AlKendi et al., 2024). You will
extend the ground truth through the week and into Week 5.

What matters today is that the first folio is *right*, because it establishes the
conventions everything after it follows. Errors in convention made today
propagate into every folio you transcribe subsequently, and correcting them later
means revisiting all of it.

**Takeaway:** One accurate folio beats three careless ones —
today's conventions propagate into everything transcribed afterwards.

---

## **17 Content**

**Sampling for Training Data**

A related decision, which matters when you extend beyond today's folio.

The instinct is to transcribe consecutive folios: finish 42r, do 42v, then 43r.
For building an edition this is right. For building HTR training data it is
wrong.

Neural models struggle with material unlike their training data. A model trained
on fifty consecutive pages learns those pages' particular vocabulary, ink
condition, and layout — and degrades on pages that differ. Sampling across the
corpus exposes the model to the variance it will actually encounter (Geelhaar,
2022).

| Sampling strategy | Exposes the model to | Suitable for |
| --- | --- | --- |
| Consecutive pages | One region's characteristics | Building the edition |
| Chronologically spread | Changes in hand over time | Multi-scribe manuscripts |
| Spread across quires | Variation in parchment and ink | Most manuscripts |
| Deliberately including difficult pages | Damage, glosses, layout shifts | Robustness |
| Deliberately including clean pages | The typical case | Baseline accuracy |

The fourth row repays attention. The temptation is to build training data from
clean, legible pages, because they are faster to transcribe. The result is a model
that performs well on clean pages and fails on exactly the pages where you needed
help. Include difficult material deliberately.

The brittleness is documented. Geelhaar's (2022) Carolingian Minuscule Model
achieved 5.1% CER on standard manuscript pages, but degraded to 13.6% on pages
carrying minuscule marginal glosses — a substantial deterioration caused by
shifting vocabulary, heavier local abbreviation, and reduced effective resolution.
Even a strong model remains brittle when the layout topography changes.

Plan your sampling now, before transcribing more, so that the ground truth you
build through the week is diverse by design rather than by accident.

**Takeaway:** Sample training pages across the corpus and
deliberately include difficult ones, or the model will fail precisely where you
need it.

---

## **18 Content**

**Validating the Transcription**

Before committing, validate — structurally and substantively.

| Check | Method | Catches |
| --- | --- | --- |
| Well-formed XML | `xmllint --noout` | Unclosed tags, bad nesting |
| Schema-valid TEI | `xmllint --relaxng tei_all.rng` | Invalid elements or attributes |
| NFC normalization | The Lesson 1.2 check | Mixed normalization forms |
| Line count matches zones | Count `<lb/>` against `<zone>` | Line skip; binding drift |
| Every `@facs` resolves | The Lesson 3.3 checker | Broken references |
| Line numbering sequential | Script or inspection | Duplicated or missing numbers |
| Reading check | Read the transcription aloud against the image | Substantive misreadings |

The fourth check is the one that catches the error from section 10. A count
mismatch between `<lb/>` elements and zones means either a line was skipped or an
extra was recorded, and either way every binding after that point is wrong. Run it
every session:

```bash
echo "lb:  $(grep -c '<lb ' edition/edition.xml)"
echo "zone: $(grep -c '<zone ' edition/edition.xml)"
```

The last check has no automation and is the most valuable. Read your transcription
against the image, line by line, at full zoom, after a break. Fresh eyes on a
familiar text find errors that no amount of structural validation can, because the
errors are substantively wrong and structurally perfect.

Commit only after all seven pass.

**Takeaway:** Count `<lb/>` against `<zone>` every session — a
mismatch means line skip, and every binding after it is wrong.

---

## **19 Content**

**Committing the Ground Truth**

The commit discipline from Week 1 applies with particular force here, because this
file becomes the reference for everything measured afterwards.

```text
feat(transcription): diplomatic transcription of f. 42r, lines 1-24

Transcribed at full zoom from the Vatican IIIF facsimile, natural-light
image. Word division supplied editorially; recorded in the header and in
CONVENTIONS.md. Three readings marked unclear: lines 8, 14, 19, all from
ink loss in the lower-outer corner. Line 14 remains unresolved after
checking against the UV layer.

Abbreviations left unexpanded in <abbr> with expansions in <expan>;
supplied characters marked with <ex>.

Human-Verified: true
AI-Generated: false
```

The trailers matter from this commit onward. This is human-produced text, and
saying so explicitly is what makes Wednesday's and Friday's machine-produced
commits distinguishable from it. A repository where only some commits carry
provenance trailers is one where absence is ambiguous.

Tag this state. It is the ground truth for Week 5's measurement, and being able to
retrieve exactly the state that was measured — rather than a later corrected
version — is what makes those measurements reproducible:

```bash
git tag -a gt-f42r -m "Ground truth, f. 42r, manual diplomatic transcription"
```

If you later correct the ground truth — and Week 5 will — the tag preserves what
was actually used for the original measurement, so the comparison remains valid
and the correction is visible as a change.

**Takeaway:** Tag the ground truth state, because Week 5's
measurements are only reproducible against the exact version that was measured.

---

## **20 Content**

**What Ground Truth Quality Determines**

The stakes, stated plainly, since the care today's work requires needs
justification.

Every quantitative claim you make for the rest of the term is computed against
this file. If it contains an error, three things follow, and each is worse than it
first appears.

A correct machine reading at that point is scored as an *error*, inflating the
measured error rate. A model fine-tuned on the flawed ground truth *learns* the
error and reproduces it systematically. And in Week 5, reconciling machine output
against the ground truth, you will find a difference and — because the ground
truth is the reference — likely "correct" the machine toward your own mistake.

| Ground truth condition | Effect on measurement | Effect on training |
| --- | --- | --- |
| Accurate and diplomatic | Error rates reflect model performance | Model learns the manuscript |
| Contains transcription errors | Error rates inflated; direction unclear | Model learns your errors |
| Silently normalized | Model appears accurate; diplomatic fidelity destroyed | Model learns to modernize |
| Inconsistent conventions | Metrics unstable | Model learns inconsistency |
| Mixed Unicode normalization | Error rates grossly inflated | Model learns contradictory targets |

The third row is the insidious one, and it connects directly to section 02. A
model trained on silently normalized ground truth produces normalized output, and
because that output is clean, readable, and internally consistent, nothing signals
that the diplomatic record has been overwritten. Standard metrics do not detect
it: a model can achieve a low character error rate while systematically destroying
the historical orthography (Levchenko, 2024).

That is why the diplomatic requirement is not pedantry. It is the difference
between a ground truth that measures what you think it measures and one that
does not.

**Takeaway:** A silently normalized ground truth produces a model
that modernizes invisibly — and standard error metrics will not detect it.

---

## **21 Content**

**Human-in-the-Loop as a Methodological Commitment**

Situate today's labour within the week's argument, because "transcribe by hand
first" can sound like a pedagogical exercise rather than a methodological
requirement.

The human-in-the-loop philosophy holds that HTR does not replace the
palaeographer but *amplifies* them, shifting their labour from initial
decipherment to high-level validation and semantic enrichment (AlKendi et al.,
2024). The palaeographer's judgement remains necessary; what changes is where it
is applied.

The pedagogical sequence follows from this. Training begins with manual diplomatic
transcription in TEI, because encoding abbreviations, layout shifts, and damage
forces confrontation with the materiality of the manuscript. Only afterwards does
the student move to Transkribus or eScriptorium, where they must correct
algorithmic baselines and polygon envelopes before training a model — which
demystifies the automation, framing it as a statistical engine requiring curated
domain-specific data rather than as an oracle (AlKendi et al., 2024).

That sequence is exactly this week: manual today, algorithmic tomorrow,
generative Friday. And it is exactly why the order cannot be reversed. A student
who begins with a machine transcription and corrects it has never read the page
independently, and has no basis for judging whether the machine's reading is right
— they can only judge whether it is plausible, which is a different and much
weaker test.

**Takeaway:** Correcting a machine transcription tests
plausibility; transcribing independently tests correctness, and only the second
gives you grounds for judgement.

---

## **22 Content**

**Preparing for Wednesday**

Tomorrow you take this transcription into Transkribus, correct its layout
analysis, and train a model. Bring the following.

- Today's transcription, validated, committed, and tagged.
- Line-level zone bindings verified against the images.
- Your hand characterization document.
- Your conventions document.
- A Transkribus account, created in Week 1 and tested.
- The manifest URI for your witness, confirmed reachable.
- A note of how high above the line this scribe places diacritics.

The last item is the specific preparation from section 12. Tomorrow's first
substantive task is correcting polygon envelopes so that accents and breathings
fall inside the line images, and knowing how much vertical margin this hand
requires is what tells you whether the default polygons are adequate.

Two practical points. Ingestion is by manifest URI rather than file upload
(eScriptorium/Kraken, 2024), so confirm the manifest is reachable from outside
your machine — a local file will not import. And model training consumes credits;
the course has a shared allocation, so do not begin speculative training runs
before Wednesday's session.

**Takeaway:** Bring a validated, tagged transcription and a note
of this hand's diacritic height — polygon correction is Wednesday's first task.

---

## **23 Content**

**Note: Friday Is Remote**

A logistical matter with practical consequences worth settling today.

**Friday September 25 is a remote delivery session.** You will work from wherever
you are, on whatever machine you have, without the room's support.

Verify before Friday:

- Your repository is pushed, so the work is available from any machine.
- Your manifest and images are reachable from outside the campus network.
- Your XML editor and schema validation work on the machine you will use.
- Python and your normalization tooling are available there.
- Your polytonic input method is installed there.
- Your Transkribus and THREAD credentials work from off campus.

The fifth item catches people. A polytonic keyboard layout installed on a lab
machine is not installed on a personal laptop, and discovering this on Friday
morning costs the session. Test it now.

The second item matters if you built your own manifest in Lesson 3.3 and served it
locally. A manifest at `localhost` works on the machine that serves it and nowhere
else, which is the failure mode Lesson 3.3 section 24 described. If your manifest
is not published, publish it before Friday.

Do this today rather than Thursday evening. Every item is quick when there is time
and none of them is quick at nine on Friday morning.

**Takeaway:** Test your full toolchain on the machine you will
use Friday — push your repository, publish your manifest, install your keyboard.

---

## **24 Content**

**Reading Your Own Errors**

A reflective exercise worth doing while today's work is fresh.

When you finish your folio, review it specifically for the *kinds* of error you
made rather than for individual mistakes. Patterns are informative in a way that
individual errors are not.

| Error pattern | Likely cause | Remedy |
| --- | --- | --- |
| Confusing a specific letter pair | Unfamiliarity with this hand | Add to the hand document |
| Missing accents | Working too fast, or too low a zoom | Slow down; zoom in |
| Reading expected rather than written text | Familiarity with the work | Transcribe backwards on hard lines |
| Errors clustered in one region | Damage, or fatigue | Re-check that region when rested |
| Inconsistent abbreviation handling | No convention decided | Decide it; record it |
| Line skip | Losing position at line ends | Check position every five lines |

Record what you find. This document is genuinely useful in Week 5, when you
adjudicate differences between your transcription and machine output: knowing that
you systematically confuse two particular letterforms in this hand tells you where
to suspect yourself rather than the machine.

It also matters for a subtler reason. In Week 5 you will be tempted to treat every
difference as a machine error, because the ground truth is by definition the
reference. Having an honest account of your own error patterns is what will let
you notice the cases where the machine is right and you are not — and those cases
exist.

**Takeaway:** Record the patterns in your own errors, because in
Week 5 they tell you when to suspect yourself rather than the machine.

---

## **25 Content**

**Why Not Simply Start with the Machine?**

The obvious objection, addressed directly, since it will occur to you around the
third hour of transcription.

Why not run HTR first and correct the output? It would be faster, and correcting
is easier than transcribing from scratch. Several reasons, in increasing order of
importance.

The practical reason: an untrained model on an unfamiliar hand produces output
poor enough that correction is slower than transcription. Above roughly 15% CER,
the cognitive load of post-correction exceeds the time required to transcribe from
scratch (AlKendi et al., 2024). A generic model on a Byzantine Greek hand will
often exceed that threshold comfortably.

The training reason: the model has to be trained on something. Fine-tuning
requires ground truth, and ground truth requires manual transcription. The
question is not whether to transcribe by hand but how much.

The evidential reason, which is decisive: correcting machine output tests only
whether a reading is *plausible*. You are shown a proposal and asked whether it
looks right. Transcribing independently tests whether a reading is *correct* —
you must determine what is there without a suggestion to anchor you. The two
differ most exactly where it matters most, on genuinely difficult readings, and
anchoring is a well-documented failure of human judgement.

There is also a specific failure this guards against. Transformer models exhibit
an over-willingness to guess, producing plausible but visually incorrect words —
errors that are exceptionally difficult for a human editor to catch during
post-correction, because the hallucinated word reads perfectly and does not match
the ink (AlKendi et al., 2024). Only an independent reading catches those.

**Takeaway:** Correcting machine output tests plausibility and
anchors your judgement, which is exactly the wrong test on the hard readings.

---

## **26 Content**

**A Worked Example**

A short passage, encoded fully, showing the elements in combination.

```xml
<pb n="42r" facs="#f42r"/>
<lb n="1" facs="#f42r_l01"/>ἐν ἀρχῇ ἦν ὁ λόγος καὶ ὁ λό
<lb n="2" facs="#f42r_l02"/>γος ἦν πρὸς τὸν <choice>
    <abbr>θν</abbr>
    <expan>θε<ex>ό</ex>ν</expan>
  </choice> καὶ <choice>
    <abbr>θς</abbr>
    <expan>θε<ex>ό</ex>ς</expan>
  </choice>
<lb n="3" facs="#f42r_l03"/>ἦν ὁ λόγος οὗτος <unclear reason="faded"
    cert="medium" resp="#KMP" source="#natural">ἦν</unclear> ἐν
<lb n="4" facs="#f42r_l04"/>ἀρχῇ πρὸς τὸν <subst>
    <del rend="strikethrough">θεόν</del>
    <add place="above" hand="#hand2">κύριον</add>
  </subst>
<lb n="5" facs="#f42r_l05"/><gap reason="lacuna" extent="6" unit="chars"/>
  διʼ αὐτοῦ ἐγένετο
```

Read what this records beyond the text itself. Two *nomina sacra* are preserved as
written with their expansions marked. One reading is flagged as uncertain, with a
stated cause, a confidence level, a responsible editor, and the image it was read
from. A scribal correction by a second hand is recorded in both directions. A
lacuna is recorded with its measured extent. The word broken across lines 1 and 2
is left broken.

A normalized transcription of the same passage would read cleanly and would
preserve none of it. Every element above is evidence that Weeks 6 through 12 will
draw on — the abbreviations for Week 6, the correction for Week 7's collation, the
uncertain reading and the lacuna for Week 8's apparatus and Week 12's commentary.

**Takeaway:** The encoding records abbreviation, uncertainty,
correction, and loss — all evidence that later weeks need and that a clean
transcription discards.

---

## **27 Content**

**Checklist Before You Leave**

Verify rather than assume.

- One folio transcribed completely, at full zoom.
- Every line carries an `<lb/>` with `@n` and `@facs`.
- `<lb/>` count equals `<zone>` count.
- Abbreviations encoded with `<choice>`, `<abbr>`, `<expan>`, and `<ex>`.
- Uncertain readings marked with `<unclear>`, with `@reason`, `@cert`, `@resp`.
- Lacunae marked with `<gap/>` and a measured `@extent`.
- Scribal corrections encoded with `<subst>`, `<del>`, `<add>`.
- File validates against the TEI schema.
- Text is NFC-normalized; the hook fired.
- `transcription/CONVENTIONS.md` written and committed.
- `transcription/HAND.md` written and committed.
- Diacritic height above the line noted for tomorrow.
- Committed with provenance trailers.
- Ground truth state tagged.

Anything unfinished should be finished before Wednesday rather than carried
forward. Tomorrow's work builds on this file directly, and an incomplete or
unvalidated transcription blocks the session.

**Takeaway:** Finish and validate before Wednesday — tomorrow's
work builds directly on this file.

---

## **28 Content**

**The Week Ahead**

Where this leads, so today's care has visible purpose.

| Meeting | Step | Activity | Uses today's work as |
| --- | --- | --- | --- |
| Tue Sep 22 (#9) | Manual | Diplomatic transcription | The product |
| Wed Sep 23 (#10) | Deterministic | Transkribus layout correction and HTR training | Training data |
| Fri Sep 25 (#11) | AI-assisted, remote | LLM transcription and correction | Comparison reference |
| Week 5 Tue (#12) | Manual | Double-keying and consensus building | The text being verified |
| Week 5 Fri (#13) | Measurement | CER and WER for both machine passes | The reference for scoring |

Notice that today's transcription plays a different role in each. It is training
data on Wednesday, a comparison reference on Friday, the object of verification in
Week 5, and the measurement reference at the end of Week 5. A single artefact
serving four functions, which is why its quality propagates so widely.

The **Transcription Assignment is due Friday October 2**, at the end of Week 5, and
includes the reconciliation report. The work of these two weeks is one continuous
task: transcribe, automate, compare, reconcile, measure, report.

**Takeaway:** Today's file serves as training data, comparison
reference, verification object, and measurement reference — four roles, one
artefact.

---

## **29 Content**

**What Counts as Good Work Here**

The standard, since "a transcription" and "a good transcription" differ
substantially.

A minimally acceptable transcription is accurate, complete for the folio, and
validates.

A good transcription additionally:

- Marks uncertainty honestly, including readings the transcriber would rather resolve.
- Records abbreviations as written rather than expanding them silently.
- Preserves scribal corrections in both directions.
- Measures lacunae rather than merely noting them.
- Documents its own conventions explicitly.
- Records which image supported each contested reading.
- Notes what remains unresolved after consulting every available layer.
- Carries a commit history in which decisions are recorded with rationale.

The first item is the hardest and the most diagnostic. Marking a reading
`<unclear>` feels like an admission of failure, and the temptation is to resolve
uncertainty by choosing the more likely reading and presenting it plainly. Resist
it. An honest `<unclear>` is more useful to every subsequent reader — including
you in Week 8, building the apparatus — than a confident guess, and it is the
difference between recording evidence and asserting conclusions.

**Takeaway:** Marking uncertainty honestly is the hardest and
most diagnostic part of good transcription — a confident guess destroys the record
of what was actually legible.

---

## **30 Content**

**Synthesis: The Anchor**

One idea underlies today's meeting and the week that follows it.

Automated transcription — HTR and vision-language models alike — is measured
against something. Character error rate is a distance from a reference. Word error
rate is a distance from a reference. Every claim that a model is accurate, that
one model outperforms another, or that automation is viable for a given
manuscript, is a claim about distance from a reference. Without one, the output is
text of unknown quality, and no amount of sophistication in the model supplies
what the reference supplies (AlKendi et al., 2024).

The reference must be produced by hand, diplomatically, by someone who has read
the page. That is not a limitation of current technology awaiting a better model.
It is structural: a measuring instrument cannot be calibrated against itself, and a
model's own output cannot establish whether the model is right.

This is what makes the manual step irreducible, and it is why Tuesday comes before
Wednesday in every week of this course. The three-step cycle is not manual work
followed by better automated work. It is the construction of a measuring
instrument, followed by two measurements taken with it.

**For Wednesday.** Bring the seven items in section 22, particularly your note on
diacritic height. You will correct layout analysis before training anything.

**For Friday.** Remote delivery — verify your full toolchain per section 23 before
then.

**Takeaway:** Automation is always measured against a reference,
and a reference cannot be produced by the thing it measures — which is why the
manual step is irreducible rather than merely traditional.

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

eScriptorium/Kraken. (2024). *eScriptorium platform documentation*.
https://escriptorium.eu/about

Geelhaar, T. (2022). *Carolingian minuscule model CMM 9th–11th c.* Transkribus
Model. https://www.transkribus.org/models/latin-carolingian-minuscule

Levchenko, M. A. (2024). *Evaluating LLMs for historical document OCR: A
methodological framework for digital humanities*.

Perdiki, E., & Konstantinidou, M. (2023). Preparing big manuscript data for
hierarchical clustering with minimal HTR training. *Journal of Data Mining &
Digital Humanities*. https://jdmdh.episciences.org/12664/pdf

Puigcerver, J. (2017). *PyLaia: A deep learning toolkit for handwritten document
analysis*. https://github.com/jpuigcerver/PyLaia

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/
