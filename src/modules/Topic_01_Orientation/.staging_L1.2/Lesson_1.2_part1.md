## **01 Content**

**Visual Identity Is Not Computational Identity**

Two strings of Greek appear on your screen. They are rendered by the same font at
the same size, and they are pixel-for-pixel identical. A search for one does not
find the other. Your XSLT transformation processes one and silently skips the
other. Your collation software reports a variant where you can see no difference
whatsoever.

This is not a malfunction. It is the single most important fact about digital
Greek, and the whole of this lesson follows from it: **what you see is not what
is stored.** The screen displays *graphemes* — units of writing — while the
computer stores *code points*, numeric values standing for characters. The
relationship between the two is not one-to-one, and for polytonic Greek it is
emphatically not one-to-one.

The consequence for a digital edition is severe, because every operation that
matters is performed on the stored bytes rather than on the rendered image.
Searching, sorting, collation, morphological analysis, error-rate measurement,
schema validation — all compare code point sequences. Two visually identical
readings that differ in their underlying encoding are, to every tool in your
pipeline, two different readings.

Boschetti (2010), working on the Homer Multitext and on improving OCR accuracy
for classical critical editions, treats orthographic and encoding normalization
as prerequisite to any analytical work rather than as cleanup afterwards. The
ordering is deliberate: analysis performed on inconsistently encoded text
produces results that are wrong in ways that do not announce themselves.

**Vocabulary.** *Grapheme* — the smallest unit of a writing system as a reader
perceives it. *Code point* — a numeric value in the Unicode standard, written
`U+03B1`. *Rendering* — the process by which a font turns code points into
visible marks.

**Takeaway:** Identical appearance on screen does not imply
identical storage, and every tool in your pipeline compares storage.

---


## **02 Content**

**The Hellenistic Invention of the Diacritical System**

The complexity you are about to encode is not an artifact of computing. It
originates in a scholarly intervention made more than two thousand years ago, for
reasons that are recognizably philological.

Ancient Greek was originally written without accents, breathings, or word
division — a continuous stream of capital letters known as *scriptio continua*.
This was adequate while the language was spoken natively, because readers
supplied pronunciation from competence. By the Hellenistic period that condition
was failing: Attic Greek of the classical authors was diverging from the spoken
Koine, the pitch accent was collapsing toward a stress accent, and readers at
Alexandria could no longer reliably reconstruct the pronunciation of the texts
they were preserving.

The response, associated with Aristophanes of Byzantium in the third and second
centuries BCE, was a system of marks recording exactly the information that was
being lost: the position and contour of the pitch accent, and the presence or
absence of initial aspiration. The diacritics are, in origin, a preservation
technology — an editorial apparatus for pronunciation, added by scholars to texts
that were already old.

This history explains a fact you will confront directly in Week 6. Diacritics are
*editorial*, not authorial. The manuscripts you will transcribe carry accentuation
supplied by scribes centuries after composition, applied inconsistently, and
sometimes wrongly. When you make normalization decisions about accents in Week 6,
you are adjudicating between editorial traditions rather than recovering an
author's intention — and the difference matters for how you justify the decision.

**Takeaway:** Greek diacritics are a Hellenistic editorial
apparatus for recording pronunciation, not part of the original written text.

---


## **03 Content**

**The Accents: Oxia, Varia, Perispomeni**

The polytonic system marks three accent contours, each originally denoting a
distinct pitch movement on the accented syllable.

| Accent | Greek name | Mark | Original phonetic value | Example |
| --- | --- | --- | --- | --- |
| Acute | oxia (ὀξεῖα) | ´ | Rising pitch | λόγος |
| Grave | varia (βαρεῖα) | ` | Suppressed or lowered pitch | ἀγαθὸς λόγος |
| Circumflex | perispomeni (περισπωμένη) | ῀ | Rising then falling on one syllable | δῶρον |

The grave is the one with an editorial dimension you should understand now.
It is not an independent accent so much as a contextual variant: an acute on a
final syllable is written as a grave when another word follows without
intervening punctuation. The same word therefore appears with different
accentuation depending on its position in the sentence.

This creates a genuine encoding problem rather than a merely orthographic one. If
you are collating witnesses, is ἀγαθός in one manuscript and ἀγαθὸς in another a
textual variant, or the same word in different syntactic environments? The answer
depends on context, and the decision must be made explicitly and recorded — it
cannot be delegated to software, which sees two different code point sequences
and will report a difference.

The circumflex introduces a separate problem, this time typographic. It is
represented in different traditions by a tilde-like mark or by an inverted breve,
and different fonts render the same code point differently. The code point is
unambiguous; the visual form is not. Judge encoding by inspecting code points,
never by inspecting the rendered glyph.

**Takeaway:** Three accents encode pitch contour, and the grave
is a positional variant of the acute — which makes it a collation decision, not
an automatic one.

---


## **04 Content**

**The Breathings: Dasia and Psili**

Every word-initial vowel in polytonic Greek carries a breathing mark, and initial
rho carries one too. There are two.

The **rough breathing** (dasia, δασεῖα), written as a mark resembling an opening
single quote, indicates initial aspiration — an /h/ sound preceding the vowel, as
in ὁδός (*hodos*, "road"). The **smooth breathing** (psili, ψιλή), resembling a
closing single quote, indicates the *absence* of aspiration, as in ὀδούς
(*odous*, "tooth").

The smooth breathing is worth pausing on, because it is where students most often
go wrong. It marks a negative: it asserts that there is no aspiration. A reader
might reasonably expect the absence of a sound to be represented by the absence
of a mark, but the system is explicit in both directions. A vowel-initial word
with *no* breathing mark at all is not "unaspirated" — it is *unmarked*, which is
a different claim, and in a diplomatic transcription it is a claim about the
manuscript rather than about the language.

This distinction becomes an editorial decision in Week 4. Many manuscripts,
particularly earlier ones and those in hands working quickly, omit breathings
irregularly. A diplomatic transcription must record the omission faithfully; a
normalized transcription supplies the missing mark. Recording which you have done
— and being able to move between the two — is precisely what the
`<orig>`/`<reg>` markup you meet in Week 6 exists to support (TEI Consortium,
2026).

Note also that breathings and accents co-occur on the same vowel constantly, and
their combination is where the encoding problems of the next several pages
originate: a single alpha may carry a breathing, an accent, and an iota subscript
simultaneously.

**Takeaway:** Smooth breathing marks the positive absence of
aspiration, so an unmarked vowel in a manuscript is a different fact from a
smooth-breathed one.

---


## **05 Content**

**Diaeresis, Iota Subscript, and Iota Adscript**

Three further marks complete the polytonic inventory, and each carries an
encoding consequence.

The **diaeresis** (¨) marks a vowel that is *not* part of a diphthong with the
preceding vowel — a separation instruction, as in ἀΐδιος, where the iota is
pronounced independently. Unlike accents and breathings it makes a claim about
syllabification rather than about pitch or aspiration, and it can co-occur with
an accent on the same vowel.

The **iota subscript** (ypogegrammeni, ῳ ῃ ᾳ) is the historical trace of a long
diphthong whose iota ceased to be pronounced. Ancient manuscripts wrote the iota
on the line, as a full letter — the **iota adscript** (ωι ηι αι). The subscript
form is a Byzantine and later editorial convention, introduced to record a letter
that was no longer sounded.

The distinction is directly consequential for your transcription. A manuscript
may write the adscript, may write the subscript, or may omit the iota entirely,
and these are three different states of the evidence:

| Manuscript form | Encoding | Editorial status |
| --- | --- | --- |
| Iota adscript (ωι) | Two code points: omega + iota | The older written practice; transcribe as written |
| Iota subscript (ῳ) | One precomposed point, or omega + U+0345 | Later convention; a normalization if supplied |
| Iota omitted (ω) | Omega alone | May be scribal error or may reflect pronunciation |

Deciding how to handle this in your own edition is a Week 6 task, but you should
be able to see the shape of the problem already: silently converting adscript to
subscript is an editorial intervention, and one that a reader cannot detect unless
you record it.

**Vocabulary.** *Ypogegrammeni* — the "written under" iota, U+0345. *Adscript* —
the same historical iota written as a full letter on the line.

**Takeaway:** Iota subscript is a later editorial convention for
an adscript the manuscripts wrote in full, so converting between them is an
intervention that must be recorded.

---


## **06 Content**

**Beta Code and the Legacy Encoding Era**

Before Unicode, representing this system on computers required improvisation, and
the improvisation that dominated classical scholarship was **Beta Code**.

Beta Code represents polytonic Greek using only the 7-bit ASCII character set —
the 128 characters available on early terminals and mainframes. Each Greek letter
maps to a Latin letter, and each diacritic to a punctuation mark, with the marks
following the letter in a defined order. The word ἀγαθός is written `*A)GAQO/S`,
in which `)` is the smooth breathing, `Q` is theta, and `/` is the acute.

The scheme was ingenious and it worked. The Thesaurus Linguae Graecae was built
on it, and an enormous quantity of digitized classical text still exists in Beta
Code or in formats derived from it. You will very likely encounter it this term
in older datasets.

Its cost, however, was structural rather than merely cosmetic. Beta Code
represents a single Greek grapheme as a *sequence* of ASCII characters, which
severs the graphemic unity of the character: to the computer, ἀ is not one thing
with properties but three unrelated symbols in a row. Sorting, searching, and
counting all operate on that sequence rather than on the letter, and every
program must implement its own logic to reassemble graphemes from it.

Boschetti (2010) notes a related loss in early digital libraries, which prized
breadth of coverage over depth of representation — digitizing the canonical texts
while discarding the critical apparatus and paratextual material that make an
edition scholarly. The two losses share a cause: an infrastructure that could not
represent complexity encouraged projects to shed it.

**Takeaway:** Beta Code encoded Greek as ASCII sequences,
severing the unity of the grapheme and forcing every program to reassemble
letters for itself.

---


## **07 Content**

**Unicode's Architecture for Greek**

Unicode replaced the legacy schemes with a single universal character set in
which Greek letters are Greek letters rather than repurposed Latin ones. For
polytonic Greek, three blocks matter (Unicode Consortium, 2025).

| Block | Range | Contains | Primary use |
| --- | --- | --- | --- |
| Greek and Coptic | U+0370–U+03FF | Basic letters, monotonic accented forms | Modern Greek; base letters for composition |
| Greek Extended | U+1F00–U+1FFF | Precomposed polytonic combinations | Ancient Greek with accents and breathings |
| Combining Diacritical Marks | U+0300–U+036F | Accents and breathings as separate marks | Building accented forms compositionally |

The Greek and Coptic block supplies the alphabet: alpha is U+03B1, omega is
U+03C9. These are the letters without polytonic diacritics, plus the accented
forms that modern monotonic Greek requires.

The Greek Extended block exists specifically for ancient Greek. It contains
**precomposed** characters — single code points standing for a base letter
together with all its diacritics. Alpha with smooth breathing and acute is one
code point, U+1F04. Alpha with smooth breathing, acute, and iota subscript is
also one code point, U+1F84. There are several hundred such combinations,
enumerated exhaustively.

The Combining Diacritical Marks block takes the opposite approach. Rather than
enumerating combinations, it supplies the marks as independent code points that
follow a base letter and modify it. Smooth breathing is U+0313, acute is U+0301,
ypogegrammeni is U+0345. Any combination can be built by concatenation, including
combinations for which no precomposed character exists (Unicode Consortium, 2025).

**Takeaway:** Unicode provides both precomposed polytonic
characters in Greek Extended and composable marks in Combining Diacritical Marks
— two routes to the same grapheme.

---


## **08 Content**

**The Two Ways to Write One Letter**

The existence of two routes is the source of the problem this lesson opened
with. Take ἀ — alpha with smooth breathing. It can be encoded as:

| Route | Code points | Length | Where it typically originates |
| --- | --- | --- | --- |
| Precomposed | U+1F00 | 1 character | Windows input; Greek Extended keyboards |
| Decomposed | U+03B1 U+0313 | 2 characters | macOS input; some web forms and OCR output |

Both render as ἀ. Any font that supports polytonic Greek displays them
identically, and no visual inspection can distinguish them. But their stored
representations differ in both length and content, and therefore:

- A byte-level comparison evaluates them as unequal.
- A character count returns 1 for one and 2 for the other.
- A search for one does not match the other.
- A regular expression matching a single character matches only the precomposed form.
- An XSLT template matching on the string processes only one of them.

For a longer word the divergence compounds. ᾧ — omega with rough breathing,
circumflex, and iota subscript — is one code point precomposed, and up to four
decomposed. A twenty-line transcription may differ in hundreds of code points
from a visually identical transcription of the same passage.

Unicode calls these two forms **canonically equivalent**: the standard asserts
that they represent the same abstract character and that conforming software
should treat them as the same (Unicode Consortium, 2025). The word "should" is
doing heavy lifting. Software that compares strings byte by byte — which is most
software, including Git, most search tools, and most XML processors — does not
implement canonical equivalence, and will treat them as different.

**Takeaway:** Precomposed and decomposed forms are canonically
equivalent by the standard but unequal to most software, which compares bytes.

---


## **09 Content**

**The Four Normalization Forms**

Unicode's solution is **normalization**: transforming text into a defined
canonical representation so that equivalent strings become identical strings.
Unicode Standard Annex #15 defines four forms (Unicode Consortium, 2025).

| Form | Full name | Operation | Lossy? |
| --- | --- | --- | --- |
| NFD | Normalization Form D | Canonical decomposition: split every character into base plus marks | No |
| NFC | Normalization Form C | Canonical decomposition, then canonical composition: prefer precomposed | No |
| NFKD | Normalization Form KD | Compatibility decomposition: also collapses formatting distinctions | Yes |
| NFKC | Normalization Form KC | Compatibility decomposition, then composition | Yes |

The distinction that matters is the **canonical / compatibility** split, not the
composed / decomposed one. Canonical forms — NFC and NFD — preserve all
information: converting between them is fully reversible, and no distinction the
text made is lost. Compatibility forms — NFKC and NFKD — deliberately discard
distinctions the standard regards as formatting rather than content.

The K forms are dangerous for philology, and it is worth being concrete about
why. Compatibility decomposition maps superscript characters to ordinary ones,
ligatures to their constituent letters, and various presentation variants to
base forms. In a scholarly context those distinctions are frequently the data:
a superscript abbreviation mark, a manuscript ligature, or a presentation form
recorded from the source is content, and NFKC silently destroys it.

**Never apply NFKC or NFKD to manuscript transcription.** They are appropriate for
search index construction, where collapsing distinctions is the point, and for
nothing else in this course.

**Takeaway:** Use the canonical forms NFC and NFD, which are
lossless; the compatibility forms NFKC and NFKD destroy distinctions that are
philological data.

---


## **10 Content**

**Why This Course Mandates NFC**

Between the two lossless forms, this course requires **NFC** — precomposed
wherever a precomposed character exists. Three reasons, in order of weight.

First, interoperability. NFC is the form specified for text on the Web and the
form assumed by the great majority of XML tooling, database collations, and text
processing libraries. Producing NFC means your edition behaves correctly in
software you did not write and cannot inspect, which describes nearly everything
your files will eventually pass through.

Second, compactness and predictability of length. In NFC, ᾧ is a single
character; in NFD it is up to four. Character offsets, line lengths, and the
character error rates you will compute in Week 5 all depend on what counts as a
character, and the NFC count corresponds to what a human reader would say if
asked how many letters a word has.

Third, and most important for this course, comparability. Every measurement you
perform in Week 5 compares a machine transcription against your manual ground
truth. If the two are in different normalization forms, the comparison is
meaningless — a character error rate computed across a normalization mismatch can
report tens of percent error on two transcriptions that are in fact identical.
You would then spend an afternoon correcting a model that was already correct.

The requirement is therefore not stylistic. Encode in NFC because in Week 5 you
will subtract one transcription from another, and that subtraction is only valid
if both are in the same form.

**Takeaway:** NFC is required because Week 5's error-rate
comparison is only meaningful if ground truth and machine output are in the same
normalization form.

---


## **11 Content**

**Canonical Combining Class and the Ordering of Marks**

One further mechanism is needed before normalization is well defined. When a
letter carries several marks — breathing, accent, and iota subscript together —
in what order are the combining code points stored? If the order were free, then
two decomposed sequences could contain the same marks in different orders and
still fail to compare equal, and normalization would not have solved the problem.

Unicode fixes the order using the **Canonical Combining Class** (CCC), a numeric
property assigned to every code point, ranging from 0 to 254. Marks are sorted by
CCC value during normalization, so a given set of marks always yields one
sequence (Unicode Consortium, 2025).

| Code point | Mark | CCC | Effect on ordering |
| --- | --- | --- | --- |
| U+0301 | Combining acute | 230 | Sorts among above-letter marks |
| U+0313 | Combining comma above (psili) | 230 | Sorts among above-letter marks |
| U+0345 | Combining ypogegrammeni | 240 | Sorts after above-letter marks |

The ypogegrammeni's higher class places it consistently at the end of a combining
sequence, which is why ᾆ decomposes to a fixed order rather than an arbitrary one
(Unicode Consortium, 2025). Marks with class 0 are not reordered at all; marks
sharing a class are left in their existing relative order, because for marks at
the same position the order can be visually significant.

You will not manipulate CCC values by hand. It matters because it is the reason
normalization is *deterministic* — the guarantee that normalizing the same
abstract text always produces the same bytes, on any platform, in any
implementation. That determinism is what lets you treat a normalized file's hash
as a meaningful identity, which is exactly what Lesson 1.1's argument about
content-addressable storage depends on.

**Takeaway:** Canonical Combining Class fixes the order of
multiple marks, which is what makes normalization deterministic across platforms.

---


## **12 Content**

**The macOS and Windows Divergence**

The abstract problem becomes a concrete classroom problem because operating
systems differ in which form they produce by default.

macOS has historically normalized filenames to a variant of NFD at the file
system level, and macOS input methods and text services tend to produce
decomposed sequences. Windows favours precomposed NFC, and its Greek keyboard
layouts emit precomposed characters from Greek Extended. Linux behaviour varies
by input method and application, and cannot be assumed either way.

The result in a mixed-platform class is a failure mode that is genuinely
invisible. Consider a peer review in Week 5. Your partner, on a Mac, transcribes a
passage in NFD. You, on Windows, open the file and correct three words, and your
editor writes your corrections in NFC. You commit. The diff shows changes on
lines you never touched, because those lines were rewritten from NFD to NFC by
your editor — or, worse, shows no changes on lines you did touch, because a
whitespace-collapsing viewer hid the difference.

Now recall the previous lesson: Git compares bytes. It will faithfully report a
difference it cannot explain, on lines whose rendered appearance is unchanged.
Students confronted with this conclude that Git is broken. Git is working
perfectly; the text is in two forms.

Worse still is the merge case. Two students edit the same line in different
normalization forms. Git reports a conflict. Both students look at the conflict
markers, see two identical-looking lines of Greek, and have no way to resolve it
by inspection — the difference is real, structural, and invisible.

**Takeaway:** macOS tends to produce NFD and Windows NFC, so a
mixed-platform team generates conflicts that are structurally real and visually
undetectable.

---


## **13 Content**

**Normalizing with Python's `unicodedata`**

The remedy is mechanical. Python's standard library includes `unicodedata`, whose
`normalize` function implements all four forms (Python Software Foundation, n.d.).

```python
import unicodedata

decomposed = "ἀ"          # alpha + combining psili
composed = unicodedata.normalize("NFC", decomposed)

print(decomposed == composed)        # False - different code points
print(len(decomposed), len(composed))  # 2 1
print(f"{ord(composed):04X}")        # 1F00
```

The function takes the target form as a string and returns the normalized text.
It is available in every standard Python installation with no dependencies, which
matters for a course in which everyone must be able to run the same script.

A practical script for a whole file:

```python
import unicodedata
from pathlib import Path

def normalize_file(path: Path, form: str = "NFC") -> bool:
    """Rewrite path in the given normalization form. Return True if changed."""
    original = path.read_text(encoding="utf-8")
    normalized = unicodedata.normalize(form, original)
    if original == normalized:
        return False
    path.write_text(normalized, encoding="utf-8")
    return True
```

Two details deserve attention. The function returns whether it changed anything,
which lets a calling script report what it touched rather than rewriting files
silently — you want to know when normalization was needed. And the encoding is
declared explicitly on both read and write: relying on the platform default
encoding is exactly the kind of implicit platform dependence this lesson is
about.

**Takeaway:** `unicodedata.normalize("NFC", text)` is the whole
mechanism, available in any standard Python installation.

---


## **14 Content**

**Automating Normalization at Commit Time**

Knowing the remedy is insufficient, because normalization must be applied every
time and human memory does not work that way. Attach it to the `pre-commit` hook
introduced in Lesson 1.1, so that no unnormalized text can enter the history.

```bash
#!/bin/sh
# .git/hooks/pre-commit
python3 tools/normalize_nfc.py --staged || exit 1
```

The script should operate on the *staged* files specifically, obtainable with
`git diff --cached --name-only --diff-filter=ACM`. Having normalized a file, it
must re-stage it with `git add`, or the commit will record the pre-normalization
content while the working directory holds the normalized version — a
discrepancy that is confusing to diagnose.

| Step | Command or call | Purpose |
| --- | --- | --- |
| List staged text files | `git diff --cached --name-only --diff-filter=ACM` | Restrict work to what is being committed |
| Normalize each | `unicodedata.normalize("NFC", text)` | Convert to the mandated form |
| Re-stage changed files | `git add <file>` | Ensure the commit records normalized bytes |
| Report | print changed paths | Make the intervention visible, not silent |

Keep the script in a tracked `tools/` directory and install it into `.git/hooks/`
with a setup script, for the reason given in Lesson 1.1: hooks are not cloned.

The pedagogical argument for automation is that it removes a burden without
removing the understanding. You still need to know what NFC is, why it is
required, and how to detect a violation — that knowledge is examinable and is
what lets you diagnose the problem when it appears in someone else's files. What
you do not need is to remember to run a command every time, because that is the
part humans reliably fail at.

**Takeaway:** Enforce NFC in the pre-commit hook and re-stage
the normalized file, so unnormalized text cannot enter the repository.

---


## **15 Content**

**Verifying Encoding by Inspecting Code Points**

Because the problem is invisible on screen, you need a habit of looking beneath
the rendering. Learn to dump code points.

```python
import unicodedata

def inspect(text: str) -> None:
    for ch in text:
        print(f"U+{ord(ch):04X}  {unicodedata.name(ch, '<unnamed>')}")

inspect("ᾧ")
```

For a file already in NFC, the output names one character. For the same grapheme
in NFD, it names a base letter followed by combining marks. This is the ground
truth about your data, and it is the only reliable way to answer the question
"what is actually in this file?"

Command-line equivalents are worth knowing, since you will often want to check a
file without opening Python:

| Task | Command |
| --- | --- |
| Dump code points of a file | `python3 -c "import sys;[print(f'U+{ord(c):04X}') for c in sys.stdin.read()]" < file.xml` |
| Check whether a file is already NFC | `python3 -c "import sys,unicodedata as u;t=sys.stdin.read();print(t==u.normalize('NFC',t))" < file.xml` |
| Show bytes with offsets | `xxd file.xml` |
| Count characters versus bytes | `wc -m file.xml` and `wc -c file.xml` |

The second command is the one to reach for when a diff looks wrong. If it prints
`False`, the file is not normalized and that is very likely your explanation.

Build the habit now, on files you understand. In Week 5, when an error rate comes
back implausibly high, the first hypothesis to test is a normalization mismatch,
and you will want the check to be reflexive rather than something you have to
work out under time pressure.

**Takeaway:** When Greek text behaves strangely, dump the code
points — the rendering cannot tell you what is stored.

---

