# Lesson 1.2 — Unicode Polytonic Greek, the Editing Environment, and Manuscript Selection

*RELS 398 / ENGL 398 · Topic 1: Orientation · Meeting #2 (Fri Sep 4)*

*Orientation week — the three-step comparative cycle does not yet apply. This
meeting establishes the character-encoding foundation and the working
environment, and closes with the selection of the manuscript passage that every
subsequent assignment builds upon.*

---

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

**The takeaway for this page:** Identical appearance on screen does not imply
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

**The takeaway for this page:** Greek diacritics are a Hellenistic editorial
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

**The takeaway for this page:** Three accents encode pitch contour, and the grave
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

**The takeaway for this page:** Smooth breathing marks the positive absence of
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

**The takeaway for this page:** Iota subscript is a later editorial convention for
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

**The takeaway for this page:** Beta Code encoded Greek as ASCII sequences,
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

**The takeaway for this page:** Unicode provides both precomposed polytonic
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

**The takeaway for this page:** Precomposed and decomposed forms are canonically
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

**The takeaway for this page:** Use the canonical forms NFC and NFD, which are
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

**The takeaway for this page:** NFC is required because Week 5's error-rate
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

**The takeaway for this page:** Canonical Combining Class fixes the order of
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

**The takeaway for this page:** macOS tends to produce NFD and Windows NFC, so a
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

**The takeaway for this page:** `unicodedata.normalize("NFC", text)` is the whole
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

**The takeaway for this page:** Enforce NFC in the pre-commit hook and re-stage
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

**The takeaway for this page:** When Greek text behaves strangely, dump the code
points — the rendering cannot tell you what is stored.

---

## **16 Content**

**Fonts for Polytonic Greek**

A font maps code points to glyphs. If a font lacks a glyph for a code point, the
text is not wrong — it simply cannot be displayed, and you will see a replacement
box. Students routinely mistake this for data corruption and "fix" correct files.

Not every Unicode font covers the Greek Extended block, and coverage of rare
combinations is uneven even among fonts that advertise polytonic support. Choose
a font with documented coverage and use it consistently.

| Font | Coverage | Notes |
| --- | --- | --- |
| Gentium Plus | Full polytonic; extensive diacritics | Free; designed for linguistic and philological use |
| New Athena Unicode | Full polytonic, epigraphic and papyrological marks | Free; standard in classics |
| Brill | Full polytonic, extensive scholarly range | Free for academic use; excellent rendering |
| IFAO-Grec Unicode | Polytonic plus papyrological symbols | Free; strong for documentary texts |
| Noto Serif / Sans | Good polytonic coverage | Free; consistent cross-platform rendering |

Install at least two. When a character fails to render, the diagnostic step is to
view the file in a different font: if the second font shows the character, your
data is fine and the first font simply lacked the glyph. If every font shows a
box, the code point may genuinely be wrong — at which point you inspect code
points as in the previous section.

For your XML editor and terminal, set a polytonic-capable monospace or serif face
explicitly rather than accepting the default. A default font that silently fails
on rare combinations will cost you an afternoon in Week 6, when you are working
with exactly those combinations.

**The takeaway for this page:** A missing glyph is a font problem, not a data
problem; diagnose by changing fonts before changing files.

---

## **17 Content**

**Keyboard Layouts and Input Methods**

You will type a good deal of polytonic Greek this term, and the input method you
choose determines both your speed and — critically — the normalization form of
what you produce.

| Method | Platform | Approach | Typical output form |
| --- | --- | --- | --- |
| Greek Polytonic layout | Windows, macOS, Linux | System layout with dead keys for diacritics | NFC on Windows; often NFD on macOS |
| Keyman (Galaxie / classical layouts) | Cross-platform | Installable layout with mnemonic input | Configurable; usually NFC |
| Unicode hex input | All | Type the code point directly | Exactly what you type |
| Copy from a digital corpus | All | Reuse existing text | Whatever the source used — verify |

The system polytonic layouts use *dead keys*: a key that produces no character
itself but modifies the next keystroke. Typing the smooth-breathing dead key
followed by alpha produces ἀ. Combinations chain, so breathing, accent, and iota
subscript can be entered in sequence. The layouts repay a few hours of practice
early in the term, and this weekend is the right time.

The last row of the table is the one to be careful about. Text copied from a
digital corpus, a PDF, or a website arrives in whatever form that source used,
which is frequently not NFC and occasionally not consistent within a single
document. Always normalize after pasting, and never assume that text which looks
right is encoded right.

Whatever method you adopt, verify its output once, deliberately: type a
multi-diacritic character such as ᾧ, dump its code points, and learn what your
own setup produces. Knowing your own tooling's default saves diagnosis later.

**The takeaway for this page:** Verify what normalization form your own keyboard
produces, and always normalize text pasted from external sources.

---

## **18 Content**

**Oxygen XML Editor**

Oxygen is the standard professional environment for TEI work and is available to
you through the university. Its advantage over a general text editor is that it
understands the schema your document declares.

The features that matter for this course:

- **Schema-aware completion.** With the TEI or EpiDoc schema associated, Oxygen offers only elements valid at the cursor position, which prevents a large class of encoding errors as you type (TEI Consortium, 2026; EpiDoc Guidelines, 2026).
- **Continuous validation.** Errors are flagged as you work rather than at commit time, with the specific rule violated.
- **Author mode.** A visual editing view driven by a stylesheet, useful when the raw markup becomes dense enough to obscure the text.
- **XPath evaluation.** Query your own document interactively — indispensable from Week 8, when the apparatus makes documents large.
- **Built-in XSLT and transformation scenarios.** Preview output without a separate toolchain.

Two configuration steps to take before Week 2. First, associate the TEI P5
schema with your documents so validation is live from the outset. Second, set the
editor font to a polytonic-capable face from the previous section, and set the
file encoding explicitly to UTF-8.

Oxygen also has Git integration adequate for staging and committing. It is
perfectly acceptable to use it — with the caveat from Lesson 1.1 that graphical
Git tools do not expose hooks, trailers, or pickaxe searches, so you will need
the command line for those.

**The takeaway for this page:** Oxygen's value is schema-aware validation as you
type, catching encoding errors before they enter the repository.

---

## **19 Content**

**VS Code as an XML and Git Environment**

VS Code is the alternative, and for many students the better one, because it
combines XML editing with the strongest available Git integration in a single
free tool.

| Extension | Provides | Needed from |
| --- | --- | --- |
| XML (Red Hat) | Schema validation, completion, formatting | Week 2 |
| Scholarly XML | TEI-aware completion and RelaxNG validation | Week 2 |
| GitLens | Inline blame, history, and authorship at each line | Week 4 |
| Git Graph | Visual DAG of the repository | Week 1 |
| Python | Running normalization and analysis scripts | Week 1 |

GitLens deserves specific mention for this course. It annotates each line of a
file with the commit that last changed it, the author, and the message —
transforming a static transcription into a document you can interrogate line by
line. Hovering over a reading in your edition shows when it entered and why,
provided you wrote a useful commit body. It renders the argument of Lesson 1.1
visible in the editor.

The practical advantage of consolidating on VS Code is that transcription,
validation, Python scripting, and version control happen in one window. The
practical disadvantage relative to Oxygen is a weaker Author mode and less mature
XSLT support. Many students in this course use both: Oxygen for heavy encoding
work, VS Code for scripting and Git.

Whichever you choose, configure it this weekend rather than in Week 2. Set the
font, set UTF-8, install the extensions, and verify that a deliberately invalid
XML file is flagged. Discovering that validation was never enabled is a poor way
to begin the cataloguing assignment.

**The takeaway for this page:** VS Code with the XML and GitLens extensions puts
encoding, scripting, and version history in one window.

---

## **20 Content**

**Accounts to Create This Week**

Three accounts are required, and all three should exist before Week 2 because
each has an approval or setup delay that will otherwise cost you class time.

| Service | Purpose | Needed by | Setup note |
| --- | --- | --- | --- |
| GitHub | Remote hosting, submission, peer review | Week 2 | Use your StFX address; match your Git `user.email` |
| Transkribus | HTR model training and transcription | Week 4 | Free tier sufficient; model training needs credits |
| THREAD | Collaborative transcription environment | Week 4 | Account approval is not instantaneous |

For GitHub, the email address matters more than it appears. Commits are
associated with an author by email; if your local `user.email` does not match a
verified address on your GitHub account, your commits will appear as an
unrecognized author and will not be attributed to you in the interface. Set the
same address in both places.

Enable two-factor authentication on GitHub, which is required for account
security and affects how you authenticate from the command line: password
authentication over HTTPS is not available, so you will use either a personal
access token or an SSH key. Generate an SSH key this weekend and add it to your
account; the alternative is discovering the requirement mid-class when you first
try to push.

For Transkribus, note that the free tier covers a good deal of transcription but
that HTR *model training* consumes credits. Week 4 will use a shared course
allocation, but create the account now and familiarize yourself with the
interface.

**The takeaway for this page:** Create all three accounts this week; GitHub's
email must match your Git configuration, and THREAD approval is not immediate.

---

## **21 Content**

**Case Study: Structure-Aware OCR of Greek Critical Editions**

A recent study illustrates why the encoding discipline in this lesson must
precede any use of automation, and it is worth examining in detail because you
will replicate a small version of it in Week 4.

Angleraud et al. (2026) address the digitization of printed Greek critical
editions — a genuinely hard problem because the printed page is *polycentric*.
A single page carries the primary text, a dense multi-layered apparatus at the
foot, marginal line numbers, and canonical reference milestones such as Stephanus
pagination embedded in the margins. Conventional OCR reads the page as a single
column of text and interleaves these registers into an unusable transcript.

The researchers fine-tuned vision-language models — Qwen3-VL and DeepSeek-OCR-2 —
on a synthetic corpus of 185,000 page images generated from TEI/XML sources with
controlled typographic variation. The models were trained to emit structured
output that explicitly separates the registers, marking milestones with `<ref>`
and marginalia with `<note>` rather than flattening them into the text
(Angleraud et al., 2026).

The results are worth reading carefully in both directions. The fine-tuned
Qwen3-VL-8B model achieved a median character error rate of 1.0% — excellent by
any standard, and better than most students achieve transcribing by hand. But the
same study documents "catastrophic page-level failures," in which the model's
output drifts entirely from the image and it generates fluent, grammatical,
entirely fabricated Greek. The models also struggled systematically with symbolic
ambiguity, particularly failing to distinguish alphabetic Greek numerals from
ordinary lexical tokens (Angleraud et al., 2026).

That combination — excellent median accuracy with occasional total fabrication —
is the defining risk profile of machine transcription, and it is why this course
records provenance in commit trailers and measures error rates against your own
ground truth. A model wrong 1% of the time uniformly could be trusted and spot-
checked. A model that is 99% correct and occasionally invents a page cannot.

**The takeaway for this page:** Machine transcription can achieve a 1.0% median
error rate while occasionally fabricating entire pages, which is why provenance
and ground truth are non-negotiable.

---

## **22 Content**

**What the OCR Case Study Implies for Your Workflow**

Draw out the consequences, because they shape how the rest of the term is
structured.

If failures were uniformly distributed, sampling would be a valid quality
control: check 10% of the output, estimate the error rate, and correct
proportionally. Catastrophic page-level failure defeats sampling entirely,
because the failures are concentrated and a sample may contain none of them while
the document contains several (Angleraud et al., 2026).

If failures were *visible*, they would be self-correcting: fluent output that is
obviously wrong gets caught. But a hallucinated page of Greek is grammatical and
plausible. It reads as competent Greek because the model is very good at
producing competent Greek — which is the source of the problem, not a mitigation
of it. The only detection method is comparison against the image.

| Failure profile | Effective control | Why |
| --- | --- | --- |
| Uniform low-rate errors | Sampling and spot-check | Sample is representative of the whole |
| Concentrated catastrophic failure | Full comparison against source | Sample may miss the affected region entirely |
| Fluent fabrication | Comparison against the image, not the text | Output is internally plausible and self-consistent |
| Symbolic ambiguity (numerals) | Targeted review of known-hard categories | Failure is systematic and therefore predictable |

Three practices follow, and each has a place later in the course. Every page of
machine output is checked against the facsimile, not sampled. Machine output is
committed separately from your corrections, so that the raw state remains
recoverable and the error rate remains measurable. And known-hard categories —
numerals, abbreviations, marginalia — receive targeted review rather than being
trusted at the general rate.

**The takeaway for this page:** Concentrated, fluent failures defeat sampling, so
machine output must be compared page by page against the image.

---

## **23 Content**

**Machine Learning and Philological Judgement**

The OCR case study concerns transcription. A second body of work concerns
something more ambitious — machine assistance in *editorial* judgement — and it
frames a question this course returns to repeatedly.

Cowen-Breen et al. (2023) describe Logion, a BERT-based model trained on
premodern Greek, applied to the detection of scribal errors and the suggestion of
emendations. The model learns the statistical regularities of Greek as attested
in a large corpus, and can therefore identify passages that are anomalous with
respect to those regularities — which is, in a limited but real sense, what a
philologist does when a reading strikes them as wrong.

The limitation is precise and worth stating carefully. The model identifies
*statistical* anomaly, not *textual* error. A passage may be unusual because a
scribe erred, or because the author wrote something unusual — and authors of
literary interest are, notoriously, the ones who write unusual things. The model
cannot make that distinction, because the distinction requires knowing what the
author was doing, which is not in the training data (Cowen-Breen et al., 2023).

This maps directly onto the Friday step of every week from Week 4 onward. The
machine's proposal is evidence — genuinely useful evidence, of a kind that would
take a human a long time to assemble. It is not a conclusion. Your task on those
Fridays is to adjudicate the proposal against the manuscript and against your
knowledge of the text, and to record in the commit body why you accepted or
rejected it.

The pedagogical value of such tools may lie less in their proposals than in the
articulation they force. Explaining why a statistically anomalous reading is
nevertheless correct requires stating your reasoning explicitly — which is
exactly the reasoning that Giarratano's print editions failed to preserve.

**The takeaway for this page:** Language models detect statistical anomaly, not
textual error, so their proposals are evidence for your judgement rather than
substitutes for it.

---

## **24 Content**

**Codicological Description and the Vocabulary of the Object**

Before selecting a passage, you need enough descriptive vocabulary to say what
you are looking at. Comparative Oriental Manuscript Studies provides the standard
framework for describing manuscripts as physical objects, and its terminology is
what Week 2's cataloguing assignment will require (Bausi et al., 2015).

| Term | Refers to | Why it matters for selection |
| --- | --- | --- |
| Folio | A leaf; recto is the front, verso the back | Passage locations are cited as f. 42r, f. 42v |
| Quire / gathering | A bundle of folded leaves forming a unit | Quire boundaries often coincide with damage or loss |
| Ruling | Lines guiding the script | Affects legibility and line segmentation for HTR |
| Hand | The writing of one scribe | A change of hand mid-passage complicates model training |
| Lacuna | A physical gap where text is lost | Requires editorial restoration; adds difficulty |
| Palimpsest | A reused leaf with erased underwriting | Requires multispectral imaging; usually too hard for this term |
| Marginalia | Notes added in the margins | Must be encoded distinctly from the main text |
| Colophon | A scribal note, often with date and place | Valuable metadata for the Week 2 TEI header |

Bausi et al. (2015) emphasize that codicological description is not preliminary
to textual work but part of it: the physical structure of the book carries
evidence about how the text was transmitted, and an edition that ignores the
object is missing data.

For your purposes this week, this vocabulary is the checklist you take to the
selection decision. You should be able to state, of the passage you choose, how
many folios it spans, whether it is written in one hand, whether it contains
lacunae or marginalia, and whether a colophon is present anywhere in the
manuscript.

**The takeaway for this page:** You need codicological vocabulary to describe what
you have chosen, and the physical structure of the book is evidence, not context.

---

## **25 Content**

**Choosing Your Passage: The Criteria That Matter**

The selection due today governs the entire term. Every assignment from Week 2 to
Week 13 operates on this passage, and a poor choice cannot be corrected in
November. Weigh the following.

| Criterion | Target | Why |
| --- | --- | --- |
| Length | 20–40 lines | Enough for meaningful collation; small enough to encode fully |
| Legibility | Clear, consistent hand | HTR training in Week 4 requires readable baselines |
| Witnesses | At least 2, ideally 3 | Week 7 collation requires more than one witness |
| Image availability | Open-licensed, high resolution | Week 3 IIIF work requires images you may use |
| Textual interest | Known variants or cruxes | Weeks 8 and 12 need something to discuss |
| Prior editions | At least one available | Provides a comparison for your editorial decisions |
| Script | Not a difficult minuscule or palimpsest | Manageable within a thirteen-week term |

The witness requirement is the one students most often underestimate. A passage
surviving in a single manuscript makes Week 7's collation exercise impossible in
any real sense — you cannot align witnesses you do not have, and substituting
printed editions is a poor approximation of the exercise. Confirm that at least
two witnesses are digitized and accessible *before* committing to a passage.

Image licensing is the second common failure. Many manuscript images are online
but under restrictive terms; a IIIF manifest you cannot legally build or share
undermines Week 3 and the final publication in Week 13. Prefer institutions with
explicit open licensing — the Vatican Library, the British Library, the
Bibliothèque nationale, e-codices, and similar repositories that publish IIIF
endpoints openly.

Resist the temptation toward difficulty. A famously contested passage in a
notoriously difficult hand is a compelling choice in September and an
unfinishable one in November. Textual interest matters, but tractability matters
more, and a clean passage encoded completely is worth more than an ambitious one
abandoned in Week 9.

**The takeaway for this page:** Confirm at least two accessible witnesses and open
image licensing before committing; those two constraints eliminate most
unworkable choices.

---

## **26 Content**

**Verifying Your Choice Before Committing to It**

Do not select from a catalogue description alone. Run the following checks, all
of which are quick and any of which can disqualify a passage.

- **Open the images.** Confirm the resolution is sufficient to read individual letters when zoomed, not merely to identify the page.
- **Locate the IIIF manifest.** Most major repositories expose a manifest URL; find it now, because Week 3 depends on it and its absence is a serious obstacle.
- **Check the licence explicitly.** Find the stated terms, not an assumption. Note the required attribution formula.
- **Identify the second witness.** Confirm it is digitized, accessible, and covers the same passage — not merely the same work.
- **Read ten lines.** Actually attempt to read them. A hand that looks clear at page scale can be much harder at line scale.
- **Find one prior edition.** Confirm a published text exists for comparison.
- **Check for a change of hand.** Scan the passage boundaries for a shift in script.

If a passage fails on witnesses or on licensing, discard it and choose again —
those two are not recoverable later. Failing on textual interest is survivable;
failing on legibility is survivable if the passage is short. Failing on image
resolution is not, because everything downstream depends on being able to read
the source.

Bring the results of these checks to Week 2. The cataloguing assignment, due
Friday September 18, will ask you to produce a TEI header describing this
manuscript, and much of what the header needs — repository, shelfmark, date,
material, extent, hand — is what you are gathering now (Bausi et al., 2015; TEI
Consortium, 2026).

**The takeaway for this page:** Verify images, manifest, licence, and second
witness before committing to a passage; the first four checks are the ones that
cannot be fixed later.

---

## **27 Content**

**Recording the Choice in the Repository**

The selection is ungraded but not informal. Record it in your repository, as your
first substantive commit, in a form that a reviewer can evaluate.

Your `README.md` should state:

- The work, author, and passage reference (book, chapter, line, or folio range).
- The primary manuscript: repository, shelfmark, date, and folio range.
- The second and any further witnesses, with the same identifying detail.
- The image source, IIIF manifest URL, and licence terms.
- At least one prior edition, cited.
- Two or three sentences on why you chose this passage.

The last item is the one that matters intellectually. Stating your reasons now
produces a record you can evaluate later — in Week 10's consolidation session you
will reread it and see whether the passage delivered what you expected, and in
Week 13's publication you will have the beginning of an editorial introduction
already written.

Commit it with a message that follows the conventions from Lesson 1.1:

```text
docs(readme): select MS Vat. gr. 1209 ff. 42r-43v as edition passage

Chosen for a clear tenth-century minuscule hand, two further digitized
witnesses (BnF gr. 2934, BL Add. 17210), and open IIIF access via the
Vatican Library. Passage covers 34 lines with two known variants
discussed in the Wachtel edition, giving material for the Week 8
apparatus.
```

Note what that body does: it states the choice, gives the reasons against the
selection criteria, and records the evidence that the criteria were met. Three
months from now it is the only surviving record of why you are working on this
text.

**The takeaway for this page:** Record the passage and your reasons for choosing
it as a committed document; it becomes the seed of your editorial introduction.

---

## **28 Content**

**How the Encoding Foundation Carries Through the Term**

It is worth seeing where each element of this lesson reappears, because the
material can feel like unmotivated preliminaries until it becomes load-bearing.

| Established here | Becomes essential in | Consequence of neglect |
| --- | --- | --- |
| NFC normalization | Week 5 error rates | Error rate inflated by encoding mismatch, not transcription error |
| Pre-commit hook | Every week | Unnormalized text accumulates and must be fixed retroactively |
| Code point inspection | Weeks 5–7 | Encoding faults misdiagnosed as transcription or collation faults |
| Polytonic font | Weeks 4–6 | Correct data mistaken for corruption; correct files "repaired" |
| Diacritic vocabulary | Week 6 normalization | Cannot state what is being normalized or justify the decision |
| Adscript / subscript distinction | Week 6 | Silent normalization of an editorial convention |
| Codicological vocabulary | Week 2 TEI header | Header incomplete; cataloguing assignment weakened |
| Passage with 2+ witnesses | Week 7 collation | Collation exercise cannot be performed as designed |
| Open image licence | Weeks 3 and 13 | IIIF manifest unbuildable; edition unpublishable |

The pattern is that encoding problems do not present as encoding problems. They
present as inexplicable error rates, spurious collation variants, mysterious diff
noise, and files that look corrupted but are not. Every one of those symptoms
sends students hunting in the wrong place, and the hours lost are hours not spent
on the text.

This is why the course front-loads the infrastructure. Boschetti (2010) makes the
same argument about corpus preparation: normalization is prerequisite to
analysis, and analysis performed on unnormalized data yields results that are
wrong without appearing wrong.

**The takeaway for this page:** Encoding faults present as inexplicable error
rates and phantom variants, which is why they must be eliminated before the
analysis that would otherwise be blamed.

---

## **29 Content**

**A Complete Setup Checklist**

Consolidate everything from both meetings of Week 1 into a verifiable list.
Complete it before Week 2 begins.

**Version control (Lesson 1.1).**

- `git config --global user.name` and `user.email` set, matching your GitHub account.
- `git config --global init.defaultBranch main` set.
- `git config --global diff.algorithm histogram` set.
- Repository created with the directory structure from Lesson 1.1.
- `.gitattributes` committed with `* text=auto eol=lf`.
- `.gitignore` committed, covering `.DS_Store`, editor backups, and `.vscode/`.

**Encoding (this lesson).**

- At least two polytonic fonts installed and verified on a multi-diacritic character.
- A polytonic input method installed, and its output normalization form verified.
- `tools/normalize_nfc.py` written and committed.
- `pre-commit` hook installed and tested on a deliberately decomposed file.

**Environment.**

- Oxygen or VS Code installed, with TEI schema validation confirmed working.
- Editor font set to a polytonic face; encoding set to UTF-8.
- Python 3 available on the command line.

**Accounts.**

- GitHub account with verified StFX email, 2FA enabled, SSH key added.
- Transkribus account created.
- THREAD account requested.

**Passage.**

- Passage selected against the criteria in section 25.
- All seven verification checks in section 26 completed.
- `README.md` committed recording the choice and the reasons.

Test the hook rather than assuming it works: create a file containing decomposed
Greek, stage it, commit, and confirm the committed content is NFC. An untested
hook is not a control.

**The takeaway for this page:** Complete and verify the checklist before Week 2;
test the pre-commit hook rather than assuming it functions.

---

## **30 Content**

**Synthesis: Infrastructure as Editorial Method**

The two meetings of this week have covered version control and character
encoding, which look like technical preliminaries to the real work of the course.
They are not preliminaries. They are the conditions that make the real work
possible, and the argument connecting them is worth stating explicitly.

An edition makes claims: this manuscript reads thus, this variant is to be
preferred, this reading is corrupt. A *scholarly* edition additionally makes those
claims inspectable — a reader can see what the evidence was and how the editor
reasoned from it. Huskey (2024) frames this as reproducibility and explainability,
and identifies version control as the mechanism that delivers both for a digital
edition.

Character encoding is the same argument one level down. Before a claim about a
reading can be inspected, the reading must be represented unambiguously. Text
that is sometimes NFC and sometimes NFD does not make one claim; it makes a claim
that varies by platform and by tool. Normalization is what makes the object of the
claim stable enough to be argued about (Unicode Consortium, 2025).

Both, finally, are about the same thing: making your work *checkable*. The commit
history lets a reader check your reasoning. Consistent encoding lets a machine
check your text. The three-step cycle that begins in Week 2 — manual, then
deterministic, then AI-assisted — is an extended exercise in checking, and it
depends entirely on the two foundations laid this week.

**Due today, Friday September 4.** Your manuscript passage, selected against the
criteria in section 25, verified by the checks in section 26, and recorded in a
committed `README.md`. The selection is ungraded. Every graded assignment for the
next twelve weeks builds on it.

**Next week.** Topic 2 begins the three-step cycle: Tuesday you hand-write a TEI
header in a plain text editor, Wednesday you validate it against the schema in
Oxygen and build RDF triples, and Friday you compare AI-generated metadata against
the header you wrote yourself.

**The takeaway for this page:** Version control makes your reasoning checkable and
normalization makes your text checkable; the whole course is an exercise in
checking, and this week built its preconditions.

---

## References

Angleraud, N., Karamolegkou, A., Sagot, B., & Clérice, T. (2026).
*Structure-aware text recognition for ancient Greek critical editions* (arXiv:
2603.02803v3). Inria.

Bausi, A., Borbone, P. G., Briquel-Chatonnet, F., Buzi, P., Gippert, J., Macé,
C., Maniaci, M., Melis, Z., Parodi, L. E., Witakowski, W., & Sokolinski, E.
(Eds.). (2015). *Comparative Oriental manuscript studies: An introduction*.
COMSt.

Boschetti, F. (2010). Analytical developments for the Homer Multitext:
Palaeography, orthography, morphology. In *Improving OCR accuracy for classical
critical editions*.

Chacon, S., & Straub, B. (2014). *Pro Git* (2nd ed.). Apress.
https://git-scm.com/book/en/v2

Cowen-Breen, C., Brooks, C., Graziosi, B., & Haubold, J. (2023). Machine
learning and the future of philology: A case study. *Transactions of the American
Philological Association, 153*(1), 253–284.

EpiDoc Guidelines. (2026). *Critical apparatus*.
https://epidoc.stoa.org/gl/latest/supp-apparatus.html

Huskey, S. J. (2024). Committing to reproducibility and explainability: Using
Git as a research journal. *International Journal of Digital Humanities, 6*,
9–21. https://doi.org/10.1007/s42803-023-00076-9

Python Software Foundation. (n.d.). *unicodedata — Unicode database*. Python 3.12
documentation. https://docs.python.org/3/library/unicodedata.html

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange* (Version 4.12.0). https://tei-c.org/guidelines/p5/

Unicode Consortium. (2025). *Unicode Standard Annex #15: Unicode normalization
forms* (Revision 57). https://www.unicode.org/reports/tr15/
