# Lesson 4.1 — Diplomatic Transcription by Hand: Building the Ground Truth

*RELS 398 / ENGL 398 · Topic 4: Transcription · Meeting #9 (Tue Sep 22)*

***Step 1 of the three-step cycle: manual.** Today you type out a manuscript page by hand, reading it at high magnification. What you produce is the *ground truth* — the correct version that Wednesday's software and Friday's AI will be measured against.*

---

## **01 Content**

**Why the Manual Step Comes First**

This week you transcribe the same passage three times. Today by hand. Wednesday with software that learns handwriting. Friday with an AI model.

Doing it by hand first is not old-fashioned caution. Wednesday and Friday produce output that has to be *graded*, and grading needs an answer key. Without one, the software's output is just text on a screen. It might be right. You have no way to tell. Every accuracy score you calculate in Week 5 is measured against the file you build today (AlKendi et al., 2024).

There is a second reason. Typing a page out by hand is how you learn what your manuscript actually holds — how this scribe shapes each letter, which short forms keep appearing, where the page is damaged. Tomorrow you judge whether the software read the page correctly. You cannot judge that if you have never read the page yourself.

**Vocabulary.** *Ground truth* — a transcription checked and known to be correct, used as the answer key for scoring software. *Transcription* — a typed version of what is written on a page.

**Takeaway:** Today's transcription is the measuring instrument for the rest of the term — every error rate you compute is a distance from it.

---

## **02 Content**

**Diplomatic Versus Normalized Transcription**

There are two ways to type out a manuscript, and they serve opposite purposes.

A **diplomatic** transcription copies what is on the page, exactly: the original spelling, the original punctuation, the line breaks, the odd letter shapes, the abbreviations left short. It is loyal to the parchment.

A **normalized** transcription tidies all of that up. It fixes the spelling, spells out the abbreviations, and uses modern punctuation. It is loyal to the words, not to the page (AlKendi et al., 2024).

| Feature | Diplomatic | Normalized |
| --- | --- | --- |
| Spelling | As written, errors included | Corrected |
| Abbreviations | Left short, or marked | Quietly spelled out |
| Punctuation | As on the page | Modern |
| Word spacing | As written | Modern |
| Line breaks | Kept | Dropped |
| Letter shapes | Variants kept apart | Merged |
| Good for | Studying the hand; training software | Reading; translating |

Yours today must be diplomatic. Here is why. Software learns from the examples you give it. Feed it tidied-up text and it learns to tidy up — that is, to quietly replace what the scribe wrote with what a modern editor would write (AlKendi et al., 2024).

Tidying up is Week 6's job, done *from* a diplomatic copy, with every change written down. Doing it now, silently, destroys what Week 6 needs.

**Vocabulary.** *Diplomatic* — copying the document's own forms exactly. *Normalized* — cleaned up to modern convention.

**Takeaway:** Transcribe diplomatically, because a model trained on normalized text learns to silently modernize — and Week 6 needs the unnormalized base.

---

## **03 Content**

**One Text, Two Structures**

TEI is the set of rules you use to mark up a text in XML. Using it commits you to one idea about what a text is, and it helps to know what that idea is.

TEI assumes a text is a single nested stack of boxes: a work holds chapters, a chapter holds paragraphs, a paragraph holds sentences. XML forces this. Boxes must sit neatly inside other boxes. They may not overlap (AlKendi et al., 2024).

Manuscripts break that rule constantly. A page has a *physical* structure — leaves, columns, lines. The text has a *logical* structure — chapters, sentences. Both are real, and neither fits inside the other. A sentence starts halfway down a line and finishes on the next page.

TEI solves this with an empty tag that marks a *spot* rather than wrapping anything. `<pb/>` marks where a page starts. `<lb/>` marks where a line starts:

```xml
<p>ἐν ἀρχῇ ἦν ὁ λόγος καὶ ὁ λόγος<lb n="2"/>
ἦν πρὸς τὸν θεόν καὶ θεὸς ἦν ὁ<lb n="3"/>
λόγος οὗτος ἦν ἐν ἀρχῇ<pb n="42v"/></p>
```

The paragraph stays one tidy box. The page and line breaks are recorded as points inside it.

**Vocabulary.** *Milestone* — an empty tag that marks a point in the text instead of enclosing it. *Nesting* — putting one tag fully inside another, which XML requires.

**Takeaway:** Physical and logical structure both exist and do not nest, so TEI records line and page boundaries as empty milestones within the logical hierarchy.

---

## **04 Content**

**The Tags You Will Actually Use**

You need a small set of tags, used the same way every time. These cover most of what you will meet (TEI Consortium, 2026).

| Tag | What it records | Example |
| --- | --- | --- |
| `<pb/>` | A page starts here | `<pb n="42v" facs="#f42v"/>` |
| `<lb/>` | A line starts here | `<lb n="8" facs="#f42r_l08"/>` |
| `<cb/>` | A column starts here | `<cb n="b"/>` |
| `<abbr>` | A short form, as written | `<abbr>θς</abbr>` |
| `<expan>` | The same word, spelled out | `<expan>θεός</expan>` |
| `<choice>` | Holds two versions side by side | `<choice><abbr/><expan/></choice>` |
| `<orig>` / `<reg>` | Original / tidied spelling | `<reg>ἐγένοντο</reg>` |
| `<unclear>` | You can read it, but not confidently | `<unclear reason="faded"/>` |
| `<gap/>` | Something is missing or unreadable | `<gap reason="lacuna" extent="3"/>` |
| `<damage>` | The page itself is damaged here | `<damage agent="water"/>` |
| `<supplied>` | You added text that is not on the page | `<supplied reason="lacuna"/>` |
| `<del>` / `<add>` | The scribe crossed out / added text | `<add place="above"/>` |

`<choice>` is the clever one. It does not pick a winner. It holds both versions so a computer can pick later, depending on the job. A reading edition shows the spelled-out form. A handwriting study shows the short form. You encode once and get both.

Today you will mostly use `<pb/>`, `<lb/>`, `<unclear>`, `<gap/>`, and `<choice>`. Save `<orig>` and `<reg>` for Week 6.

**Vocabulary.** *Tag* — the angle-bracket label that marks a piece of text, like `<lb/>`. *Attribute* — extra information inside a tag, like the `n="8"` that numbers a line.

**Takeaway:** `<choice>` holds alternatives rather than deciding between them, so one encoding can serve palaeographic, reading, and search views.

---

## **05 Content**

**Short Forms and How to Record Them**

Scribes shortened words constantly, to save time and expensive parchment. Spelling those short forms out without saying so is the most common way students ruin a transcription.

Here is the problem. The short form is ink on the page — a fact. The spelled-out version is your guess — usually a safe guess, occasionally not. Record both:

```xml
<choice>
  <abbr>θς</abbr>
  <expan>θε<ex>ό</ex>ς</expan>
</choice>
```

The `<ex>` tag marks the letters *you* supplied, which the scribe did not write. It lets software print those letters in italics, the traditional convention, and it shows exactly where the ink stops and your guess starts.

| Kind of short form | What it looks like | How to encode it |
| --- | --- | --- |
| Sacred name | Squeezed, with a line above | `<abbr>` plus `<expan>` with `<ex>` |
| Cut-off word | Word stops, a mark added | Same |
| Squeezed word | Middle letters dropped | Same |
| Genuinely ambiguous | Could be two different words | `<expan cert="medium">`, note the other option |

This matters directly for Wednesday. The software has to learn that this *shape* means these *letters on the page*. Give it spelled-out versions instead and it learns to invent letters that were never written (AlKendi et al., 2024).

**Vocabulary.** *Abbreviation* — a shortened written form. *Expansion* — the full spelling of an abbreviated word. *Nomen sacrum* — a shortened sacred name marked with a line above it.

**Takeaway:** Encode the abbreviation and its expansion separately with `<ex>` marking supplied letters, so the model learns what is actually on the page.

---

## **06 Content**

**Saying What You Cannot Read**

Your transcription has to admit its own limits. Typing a word plainly is a claim that you read it confidently. Making that claim when it is not true is an error, even if the word turns out to be right.

Four different situations need four different tags.

| Situation | Tag | What it means |
| --- | --- | --- |
| I see marks but am unsure | `<unclear>` | Here is my best reading, held loosely |
| Nothing is there, or nothing readable | `<gap/>` | I offer no reading at all |
| The page is damaged | `<damage>` | Records a physical cause |
| I added text that is not there | `<supplied>` | An editor's restoration |

Getting `<unclear>` and `<gap/>` apart is the important part. `<unclear>` *has words inside it* — you are offering a reading. `<gap/>` is empty — you are offering nothing. Put a guess inside a `<gap/>` and you have disguised a guess as a hole in the page. Leave `<unclear>` empty and you have turned a hard reading into a loss.

```xml
<unclear reason="faded" cert="medium" resp="#KMP" source="#uv365">ἐγένετο</unclear>
<gap reason="lacuna" extent="4" unit="chars"/>
```

`source` records which photograph let you read it, which links back to Lesson 3.2. `extent` records how much is gone. A four-letter hole narrows the possibilities far more than an unmeasured one.

**Vocabulary.** *Lacuna* — a hole or loss in the page where text is gone. *`cert`* — an attribute stating how confident you are.

**Takeaway:** `<unclear>` proposes a reading with reduced confidence and `<gap/>` proposes nothing — conflating them misrepresents inference as absence or difficulty as loss.

---

## **07 Content**

**When the Scribe Corrected Themselves**

Manuscripts record their own editing. A scribe crossed a word out and wrote another above it. Somebody later did the same. Those marks are often the most useful evidence a single copy offers.

| What happened | Tag | What to record |
| --- | --- | --- |
| Something crossed out | `<del>` | `rend` — how it was cancelled |
| Something added | `<add>` | `place` — above, below, in the margin |
| One swapped for another | `<subst>` around both | Groups them as a single act |
| A different person wrote it | `hand` | Points to a hand listed in the header |

```xml
<subst>
  <del rend="strikethrough">ἐγένετο</del>
  <add place="above" hand="#hand2">ἐγένοντο</add>
</subst>
```

This records more than the final wording. It records that a change happened, which direction it went, and who made it. A second person correcting the first tells you somebody read this copy carefully — which bears on where the manuscript went and which other copies it is related to.

A tidied-up transcription would give you `ἐγένοντο` and nothing else. Same final wording. Evidence gone. In Week 7 you compare copies, and a correction in one copy that matches another copy's original reading is exactly what links them.

**Vocabulary.** *Hand* — one identified writer. A page may carry several. *Substitution* — replacing one reading with another, recorded as a single act.

**Takeaway:** Scribal corrections are transmission evidence, and recording only the corrected text destroys it while leaving the reading unchanged.

---

## **08 Content**

**Why Line Breaks Matter So Much Here**

In an ordinary typed document, where a line ends means nothing. Here it means three things.

**The software works line by line.** Tomorrow's program first chops the page into lines, then reads each line separately. So its training examples must be lines — each strip of image paired with the text on it (Puigcerver, 2017). A transcription with no line divisions cannot train anything.

**Your image links are per line.** In Lesson 3.3 you attached each `<lb>` to a box drawn on the photograph. Those links only work if lines are recorded.

**Line breaks are evidence.** Where a line ends tells you about the ruling and the scribe's habits, and a scribe copying line-for-line leaves clues about the book they copied from.

```xml
<lb n="1" facs="#f42r_l01"/>ἐν ἀρχῇ ἦν ὁ λόγος καὶ ὁ λό
<lb n="2" facs="#f42r_l02"/>γος ἦν πρὸς τὸν θεόν
```

Notice the word split across the two lines — `λό` then `γος`. Type it split, as written. Do not add a hyphen and do not quietly join it up. Whether you also mark the split with `break="no"` is your choice; pick one habit and keep it.

**Vocabulary.** *Layout analysis* — software finding the lines on a page before reading them. *Ruling* — the guide lines scored on the page for the scribe to write along.

**Takeaway:** Line divisions are structural here — HTR trains on lines, your zones bind per line, and line breaks are codicological evidence.

---

## **09 Content**

**Setting Up the File Before You Type**

Build the empty file first. Sorting out the structure now saves rearranging later.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader><!-- Your Week 2 header --></teiHeader>
  <facsimile><!-- Your Lesson 3.3 image boxes --></facsimile>
  <text><body>
      <div type="passage" n="1">
        <pb n="42r" facs="#f42r"/>
        <lb n="1" facs="#f42r_l01"/>
      </div>
  </body></text>
</TEI>
```

Three checks before you type a single Greek letter.

Check the file says UTF-8 *and* that your editor is really saving UTF-8. If those disagree, every Greek character is corrupted, and fixing it afterwards is miserable.

Check the schema is attached, so your editor flags mistakes as you type. A *schema* is the rulebook saying which tags are allowed where.

Check your Week 1 pre-commit hook is working. That is the small script that runs automatically when you save to git. It fixes how accented characters are stored. Two different files can store the same accented letter in two different ways, and a mix of both makes Week 5's scores meaningless. Test it now: type an accented character, commit, confirm.

Then commit the empty file, so your typing shows up as a clean change.

**Vocabulary.** *Schema* — a rulebook listing which tags are legal and where. *Pre-commit hook* — a script git runs automatically each time you save work.

**Takeaway:** Verify UTF-8, live schema validation, and the NFC hook before typing — a mixed-normalization ground truth invalidates Week 5.

---

## **10 Content**

**How to Actually Do It**

The physical routine matters more than students expect. Most errors come from working too fast at too small a magnification.

- Zoom in until each letter is unmistakable. This is usually far closer than feels necessary.
- Do one line at a time. Do not read ahead.
- Type what you see, not what you expect to be there.
- Mark anything doubtful straight away. Do not settle it by guessing.
- Every five lines, check you are still on the line you think you are.

The third rule is the one that separates transcribing from reading. If you know the passage, you will read what you expect and never notice the difference. That is how real variants get erased.

A trick for hard lines: type them backwards, word by word from the end. It is slower, and it stops your brain predicting the next word.

The last rule guards against skipping a line. That is the worst error here. Skip one, and every line after it is attached to the wrong box on the photograph. Because the text still reads perfectly, nothing looks wrong.

**Vocabulary.** *Line skip* — missing a line out, which shifts every later line onto the wrong image box. *Variant* — a place where this copy's wording differs from another's.

**Takeaway:** Type what you see rather than what you expect, and check your line position regularly — line skip silently invalidates every binding after it.

---

## **11 Content**

**Getting to Know the Hand**

Before typing in bulk, spend fifteen minutes studying the handwriting. It saves hours.

Go through the alphabet. For each letter, find several clear examples and note how this particular scribe draws it. Pay most attention to letters that look alike.

| What to look at | Question to answer |
| --- | --- | 
| Letter shapes | How does this scribe draw each one? |
| Look-alike pairs | What tells them apart in this hand? |
| Joined letters | Which pairs get joined, and how? |
| Short forms | Which abbreviations keep coming up? |
| Accents | How high above the letter do they sit? |
| Word spacing | Regular, absent, or erratic? |
| Line ends | Are words split? Is writing squeezed? |

Byzantine Greek is awkward in specific ways. Words often run together with no spaces. Letters are joined into long chains. Some letters hang below the line instead of sitting on it. And the accent system uses at least five different marks, stacked in combinations (Perdiki & Konstantinidou, 2023).

Write what you find into a file called `transcription/HAND.md`. It keeps your reading honest, it documents your thinking for Week 12, and it is what you will check tomorrow when deciding whether a software mistake is the program's fault or the scribe's.

**Vocabulary.** *Hand* — one scribe's handwriting, treated as a system with its own rules. *Ligature* — two letters joined into one shape.

**Takeaway:** Characterize the hand before transcribing at volume, and record it — you will consult it on Wednesday to judge HTR errors.

---

## **12 Content**

**Accents and the Box Problem**

Greek accents and breathing marks sit *above* the letter, sometimes well above it. This causes a specific problem tomorrow, and today is when you can prepare for it.

Tomorrow's software draws a box around each line before reading it. It works out the box from where the letters sit. If it draws that box too tightly, accents floating high above the line fall outside it — and anything outside the box is simply not in the picture the program reads (Perdiki & Konstantinidou, 2023).

The result is baffling the first time you see it. The program gets every letter right and drops every accent. The text looks almost correct, and is wrong in exactly the marks that Lesson 1.2 spent a whole meeting showing were meaningful.

Perdiki and Konstantinidou (2023) hit this directly. Working on Byzantine Greek, their software kept cutting off breathing marks and high abbreviation signs. Getting the error rate under 10% meant widening those boxes by hand.

So today: type every accent carefully, because those are what the program will be tested on. And note how high this scribe puts them. Tomorrow you will widen boxes, and that note tells you how much to widen them by.

**Vocabulary.** *Bounding box* — the rectangle software draws around a line before reading it. *Breathing mark* — a Greek sign showing whether a word starts with an h-sound.

**Takeaway:** Layout polygons drawn too tightly cut off Greek accents entirely, so note how high this hand places diacritics — you will adjust for it tomorrow.

---

## **13 Content**

**When There Are No Spaces Between Words**

Many Greek manuscripts are written with no gaps between words at all. If yours is, decide today how you will handle it. Do not just drift into a habit.

The practice is called *scriptio continua*, and the reader was expected to work out where words ended. It puts you in a bind. Copying the page faithfully means typing with no spaces. But text with no spaces is nearly useless for comparing copies or looking up words. And adding spaces is an interpretation — the kind a diplomatic transcription is not supposed to make quietly.

| What you could do | Faithful to the page? | Useful later? |
| --- | --- | --- |
| Type it with no spaces | Completely | Poor; needs splitting later |
| Add spaces, say nothing | No; a hidden change | Good |
| Add spaces, say so in the header | Yes; the change is declared | Good |
| Record both with `<choice>` | Completely | Good, but very wordy |

Use the third. Put the spaces in, and state in your header that word spacing was added by you and is not on the page. The point is not to avoid intervening. It is to intervene openly.

Expect one knock-on effect. Perdiki and Konstantinidou (2023) found that unspaced text confuses word-counting scores: the program reads every letter correctly, then glues them together, so ἀλλὰ τί comes out as ἀλλατι. The letter score stays good while the word score becomes meaningless.

**Vocabulary.** *Scriptio continua* — writing with no spaces between words. *Word error rate (WER)* — a score counting how many whole words came out wrong.

**Takeaway:** Supply word division and declare it in the header — and expect *scriptio continua* to make word error rate uninterpretable in Week 5.

---

## **14 Content**

**Write Your Rules Down**

Transcribing throws up dozens of small decisions. The danger is not deciding badly. It is deciding differently on Tuesday than on Thursday.

Questions that will keep coming back: Do you keep the two shapes of sigma apart, or type them the same? What do you do with a mark that might be punctuation and might be an accent? How doubtful does a word have to be before it gets `<unclear>`? How do you handle a crossed-out word you cannot read?

Answer each one once. Write it in `transcription/CONVENTIONS.md`. Then follow it. That file is part of your edition — in Week 13 it becomes the statement a reader needs to make sense of your text.

Being inconsistent is worse than any single choice you could make. If you always mark the crescent-shaped sigma, a reader can interpret your text. If you mark it sometimes, they cannot — they have no way to tell whether an unmarked one was a different shape or one you missed. The software has the same problem, and will copy your inconsistency back at you unpredictably.

The CATMuS project shows this at scale. Its value comes from forcing one set of rules across 200 manuscripts (Clérice et al., 2024). That uniformity is what made 160,000 lines usable for training.

**Vocabulary.** *Convention* — a decision about how you will always encode a given feature. *Edition* — the finished scholarly presentation of a text, rules and all.

**Takeaway:** Write your conventions down and follow them — inconsistency is worse than any particular choice, for readers and for models alike.

---

## **15 Content**

**How Accurate Is a Hand Transcription?**

Less accurate than you would think. That matters, because Week 5 treats your file as the correct answer.

Typing a page once produces mistakes at a low but real rate. They are not scattered randomly. They cluster on unfamiliar letter shapes, on short forms, on damaged patches, and on passages you already knew — where you read instead of looking.

The standard fix is **double-keying**: type the same page twice, independently, then compare the two versions. Wherever they agree, you are almost certainly right. Wherever they differ is exactly where you need to look again.

| Method | Accuracy | Effort |
| --- | --- | --- |
| Type once | Good, with clustered errors | Baseline |
| Type once, then proofread | Better | About 1.3× |
| Type twice, settle the differences | Much better | About 2.2× |
| Two people type it | Best | 2×, plus coordinating |

That is Week 5's work, not today's. But knowing it is coming should shape how you type now: carefully enough that the second pass finds little. It should also make you cautious about Week 5's scores. Some of what looks like a machine error will turn out to be yours.

**Vocabulary.** *Double-keying* — typing the same text twice, independently, and comparing. *Proofreading* — checking a transcription against the original afterwards.

**Takeaway:** Your ground truth will contain errors, which is why Week 5 double-keys it — transcribe now so that the second pass finds few differences.

---

## **16 Content**

**How Much to Get Done Today**

Aim for **one page, done properly**, fully marked up. If your passage is short and the writing is clear, you may get further.

Do not trade care for quantity. One carefully typed page is a usable answer key. Three sloppy ones are worse than nothing, because tomorrow the software learns your mistakes.

| Priority | Task | Why |
| --- | --- | --- |
| 1 | One page typed completely and accurately | The smallest usable answer key |
| 2 | Markup complete: short forms, doubts, corrections | This is what makes it diplomatic |
| 3 | Every line linked to its image box | Lets anyone check your reading |
| 4 | Conventions file written | Keeps you consistent |
| 5 | Handwriting notes recorded | You need them tomorrow |
| 6 | More pages | Nice, but not at the cost of 1–5 |

Eventually you will need more than one page to train anything. Starting from a model that already knows a similar script, useful results come from roughly 50 to 100 new pages — and less than that when you are tuning it to a single scribe (Geelhaar, 2022). You will add pages through the week.

What matters today is that the first page is *right*. It sets the habits every later page follows, and fixing a habit later means redoing everything.

**Vocabulary.** *Folio* — one leaf of a manuscript, with a front and a back. *Markup* — the tags you add around the text.

**Takeaway:** One accurate folio beats three careless ones — today's conventions propagate into everything transcribed afterwards.

---

## **17 Content**

**Which Pages to Pick Later**

A decision for when you go beyond today's page.

The obvious approach is to work straight through: finish 42r, then 42v, then 43r. For building an edition, that is right. For teaching software to read, it is wrong.

Programs struggle with anything unlike what they were trained on. Train on fifty pages in a row and the program learns that stretch of the book — its particular ink, its particular layout — then stumbles on pages that differ. Spreading your pages across the whole manuscript shows it the variety it will actually face (Geelhaar, 2022).

| How you pick pages | What it teaches the program | Good for |
| --- | --- | --- |
| Straight through | One stretch of the book | Building the edition |
| Spread across the book | Changes in ink and parchment | Most manuscripts |
| Spread across time | How a hand changes | Books with several scribes |
| Deliberately awkward pages | Damage, notes, layout shifts | Robustness |
| Deliberately clean pages | The ordinary case | Baseline accuracy |

The fourth row is the one people skip. Clean pages are quicker to type, so that is what gets chosen — and the result is a program that works on easy pages and fails on the hard ones, which are the pages you needed help with.

This is documented. Geelhaar's (2022) model scored 5.1% error on ordinary pages but 13.6% on pages carrying small marginal notes — because the vocabulary shifted, the abbreviations got heavier, and the writing got smaller.

**Vocabulary.** *Training data* — the example pages a program learns from. *Marginal gloss* — a note written in the margin, often in smaller script.

**Takeaway:** Sample training pages across the corpus and deliberately include difficult ones, or the model will fail precisely where you need it.

---

## **18 Content**

**Checking Your Work Before You Save It**

Check two things: that the file is structurally sound, and that the reading is right.

| Check | How | Catches |
| --- | --- | --- |
| The XML is well formed | `xmllint --noout` | Unclosed or badly nested tags |
| The TEI is legal | `xmllint --relaxng tei_all.rng` | Tags used in the wrong place |
| Accents stored consistently | The Lesson 1.2 check | Mixed storage forms |
| Line count matches box count | Count `<lb/>` against `<zone>` | A skipped line |
| Every image link resolves | The Lesson 3.3 checker | Links pointing nowhere |
| Line numbers run in order | Script or eye | Repeated or missing numbers |
| Read it against the picture | Out loud, slowly | Actual misreadings |

The fourth check is what catches the line skip from section 10. If the number of lines does not match the number of boxes, either you missed a line or added one — and every link after that point is wrong. Run it every session:

```bash
echo "lb:   $(grep -c '<lb ' edition/edition.xml)"
echo "zone: $(grep -c '<zone ' edition/edition.xml)"
```

The last check cannot be automated and is the most valuable. Read your text against the photograph, line by line, zoomed in, after a break. Those errors are structurally perfect and substantively wrong, so no program will ever flag them.

Save to git only once all seven pass.

**Vocabulary.** *Well formed* — XML whose tags are all closed and properly nested. *Valid* — XML that also obeys its schema.

**Takeaway:** Count `<lb/>` against `<zone>` every session — a mismatch means line skip, and every binding after it is wrong.

---

## **19 Content**

**Saving It to Git Properly**

The commit habits from Week 1 matter especially here, because this file becomes the reference for everything measured later.

```text
feat(transcription): diplomatic transcription of f. 42r, lines 1-24

Typed at full zoom from the Vatican photograph, natural light. Word
spacing added by me; recorded in the header and in CONVENTIONS.md.
Three readings marked unclear: lines 8, 14, 19, all from ink loss in
the lower outer corner. Line 14 still unresolved after checking the
ultraviolet image.

Short forms left in <abbr> with spellings in <expan>; letters I
supplied marked with <ex>.

Human-Verified: true
AI-Generated: false
```

Those last two lines matter from now on. This text is human-made, and saying so is what makes Wednesday's and Friday's machine-made commits tell apart from it. If only some commits carry those labels, their absence means nothing.

Now tag this state. A tag is a permanent bookmark on one version:

```bash
git tag -a gt-f42r -m "Ground truth, f. 42r, typed by hand"
```

Week 5 measures against this exact version. If you later correct the file — and you will — the tag still points at what was actually measured, so the old numbers stay meaningful and the correction is visible as a change.

**Vocabulary.** *Commit* — one saved snapshot of your work in git. *Tag* — a permanent name attached to one particular commit.

**Takeaway:** Tag the ground truth state, because Week 5's measurements are only reproducible against the exact version that was measured.

---

## **20 Content**

**What Rides on Getting This Right**

Every number you report this term is calculated against this one file. If it contains a mistake, three things follow, and each is worse than it sounds.

A correct machine reading at that spot gets marked *wrong*, which pushes the error rate up. A program trained on the file *learns* the mistake and repeats it everywhere. And in Week 5, when you compare machine output against your file and find a difference, you will probably "fix" the machine to match your own error — because your file is the reference.

| Your file's condition | Effect on the numbers | Effect on training |
| --- | --- | --- |
| Accurate and diplomatic | Scores reflect the program | It learns the manuscript |
| Contains typing errors | Scores inflated, direction unclear | It learns your errors |
| Quietly tidied up | Program looks accurate; fidelity gone | It learns to modernize |
| Rules applied inconsistently | Scores unstable | It learns the inconsistency |
| Accents stored two ways | Scores badly inflated | It learns contradictions |

The third row is the dangerous one, and it connects back to section 02. A program trained on quietly tidied text produces tidied output — and because that output is clean and readable, nothing signals that the historical spelling has been overwritten. The usual scores will not catch it: a program can post a low error rate while systematically destroying the old orthography (Levchenko, 2024).

That is why the diplomatic rule is not fussiness.

**Vocabulary.** *Orthography* — the spelling system a text uses. *Fidelity* — how closely a transcription matches the page.

**Takeaway:** A silently normalized ground truth produces a model that modernizes invisibly — and standard error metrics will not detect it.

---

## **21 Content**

**Why the Human Stays in the Loop**

It is worth saying where today's labour sits in the argument, because "do it by hand first" can sound like a classroom exercise.

The idea is that handwriting software does not replace the person who reads manuscripts. It moves their work. Instead of spending hours deciphering, they spend that time checking and interpreting (AlKendi et al., 2024). The judgement is still needed. What changes is where it gets applied.

The teaching order follows from that. You start by typing and marking up by hand, because dealing with short forms, damage, and shifting layout forces you to confront the actual object. Only then do you move to the software, where you have to correct its line-finding before it will train — which shows you it is a statistics engine fed on examples, not an oracle (AlKendi et al., 2024).

That is exactly this week: by hand today, software tomorrow, AI on Friday. And it is why the order cannot be flipped. A student who starts from machine output and corrects it has never read the page alone. They can only judge whether a reading looks plausible, which is a much weaker test than whether it is right.

**Vocabulary.** *Human-in-the-loop* — a workflow where a person checks and corrects the machine at defined points. *Post-correction* — fixing machine output afterwards.

**Takeaway:** Correcting a machine transcription tests plausibility; transcribing independently tests correctness, and only the second gives you grounds for judgement.

---

## **22 Content**

**What to Bring Tomorrow**

Tomorrow you load this transcription into Transkribus — a web program that learns to read handwriting from examples you give it. You will correct how it divides the page into lines, then train it on your page. Bring all of this.

- Today's transcription, checked, saved to git, and tagged.
- Every line linked to its box on the image, verified.
- Your handwriting notes.
- Your conventions file.
- A Transkribus account, made in Week 1 and actually logged into.
- The web address of your manuscript images, confirmed working.
- Your note of how high this scribe puts the accents.

That last item is section 12's homework. Tomorrow's first real task is widening the line boxes so accents fall inside them, and your note is what tells you how far.

Two practical warnings. Transkribus pulls images in by web address rather than file upload, so check that address works from outside your own machine — a file sitting on your laptop will not load. And training costs credits from a shared class allowance, so do not start practice runs before the session.

**Vocabulary.** *Transkribus* — a web platform that trains software to read a particular handwriting. *Credits* — the paid units Transkribus charges for training.

**Takeaway:** Bring a validated, tagged transcription and a note of this hand's diacritic height — polygon correction is Wednesday's first task.

---

## **23 Content**

**Friday Is Remote**

**Friday September 25 you work from wherever you are**, on your own machine, without the room's support. Check these before then.

- Your work is pushed to git, so you can get at it from any machine.
- Your images load from outside the campus network.
- Your XML editor and its schema checking work on that machine.
- Python and your accent-fixing tools are installed there.
- Your Greek keyboard is installed there.
- Your Transkribus login works off campus.

The keyboard catches people out. A Greek layout installed on a lab machine is not installed on your laptop, and finding that out on Friday morning costs you the session.

The image point matters if you built your own image listing in Lesson 3.3 and ran it locally. An address starting `localhost` works on the machine serving it and nowhere else — the exact trap Lesson 3.3 described. If yours is not published, publish it before Friday.

Do this today, not Thursday night. Each item takes two minutes now and none of them takes two minutes in a panic.

**Vocabulary.** *Remote delivery* — a class session held without meeting in the room. *localhost* — an address meaning "this computer", unreachable from anywhere else.

**Takeaway:** Test your full toolchain on the machine you will use Friday — push your repository, publish your manifest, install your keyboard.

---

## **24 Content**

**Studying Your Own Mistakes**

When you finish the page, look back over it — not for individual slips, but for the *kinds* of slip you make. Patterns tell you something single errors do not.

| Pattern | Likely cause | What to do |
| --- | --- | --- |
| Mixing up one pair of letters | You do not know this hand yet | Add it to your handwriting notes |
| Dropped accents | Working too fast, zoomed too far out | Slow down, zoom in |
| Reading the expected word | You already know the text | Type hard lines backwards |
| Errors bunched in one patch | Damage, or tiredness | Recheck that patch when rested |
| Short forms handled differently | No rule decided | Decide one, write it down |
| A skipped line | Losing your place at line ends | Check position every five lines |

Write down what you find. It becomes genuinely useful in Week 5, when you are settling differences between your version and the machine's. Knowing that you regularly confuse two particular letters in this hand tells you when to suspect yourself rather than the program.

There is a subtler reason too. In Week 5 you will be tempted to call every difference a machine error, because your file is the reference by definition. An honest list of your own habits is what lets you notice the cases where the machine is right and you are not. Those cases exist.

**Vocabulary.** *Error pattern* — a mistake you make repeatedly for the same reason. *Reconciliation* — settling differences between two versions of the same text.

**Takeaway:** Record the patterns in your own errors, because in Week 5 they tell you when to suspect yourself rather than the machine.

---

## **25 Content**

**Why Not Just Start with the Machine?**

A fair question, and one that will occur to you about three hours in. Why not run the software first and fix its output? Correcting is easier than typing from scratch. Three answers, in rising order of importance.

The practical one: an untrained program on unfamiliar handwriting produces output bad enough that fixing it takes longer than typing would have. Past roughly 15% of characters wrong, correcting costs more effort than starting fresh (AlKendi et al., 2024). A general-purpose program on Byzantine Greek will clear that threshold easily.

The circular one: the program has to learn from something. Training needs correct examples, and correct examples have to be typed by a person. The question was never whether to type by hand, only how much.

The decisive one: fixing machine output only tests whether a reading is *believable*. You are shown a suggestion and asked if it looks right. Typing it yourself tests whether it is *correct* — you have to work out what is there with nothing prompting you. Those two tests differ most on exactly the hard readings where it matters, because a suggestion anchors your judgement.

There is a specific trap here. These models would rather guess than leave a blank, so they produce believable words that do not match the ink — and a believable wrong word is almost impossible to catch while correcting (AlKendi et al., 2024).

**Vocabulary.** *Hallucination* — a confident, plausible output that does not match the source. *Anchoring* — letting a suggestion pull your judgement toward it.

**Takeaway:** Correcting machine output tests plausibility and anchors your judgement, which is exactly the wrong test on the hard readings.

---

## **26 Content**

**A Worked Example**

A short passage with everything marked up, so you can see the tags working together.

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

Look at what this records besides the words. Two sacred names kept as written, with their spellings attached. One doubtful reading, with a reason, a confidence level, a named editor, and the photograph it was read from. A correction by a second person, recorded in both directions. A hole, with its size measured. A word left split across two lines.

A tidied-up version of the same passage would read beautifully and keep none of it. Every one of those tags is evidence some later week needs — the short forms for Week 6, the correction for Week 7, the doubtful reading and the hole for Weeks 8 and 12.

**Vocabulary.** *Worked example* — a complete small case showing the method end to end. *Apparatus* — the record of variant readings printed alongside an edited text.

**Takeaway:** The encoding records abbreviation, uncertainty, correction, and loss — all evidence that later weeks need and that a clean transcription discards.

---

## **27 Content**

**Checklist Before You Leave**

Check these rather than assuming them.

- One page typed completely, at full zoom.
- Every line has an `<lb/>` with a number and an image link.
- The `<lb/>` count equals the `<zone>` count.
- Short forms encoded with `<choice>`, `<abbr>`, `<expan>`, `<ex>`.
- Doubtful readings marked `<unclear>` with a reason and a confidence.
- Holes marked `<gap/>` with a measured size.
- Scribal corrections encoded with `<subst>`, `<del>`, `<add>`.
- The file passes schema validation.
- Accents stored consistently; the hook ran.
- `transcription/CONVENTIONS.md` written and committed.
- `transcription/HAND.md` written and committed.
- Accent height noted for tomorrow.
- Committed with the provenance labels.
- The ground truth version tagged.

Finish anything outstanding before Wednesday rather than carrying it over. Tomorrow's work builds straight on this file, and an unchecked transcription stops the session.

**Vocabulary.** *Provenance labels* — the commit lines recording whether text was made by a person or a machine. *Validation* — checking a file against its schema.

**Takeaway:** Finish and validate before Wednesday — tomorrow's work builds directly on this file.

---

## **28 Content**

**Where This Leads**

| Meeting | Step | What you do | Today's file serves as |
| --- | --- | --- | --- |
| Tue Sep 22 (#9) | Manual | Type it by hand | The product |
| Wed Sep 23 (#10) | Software | Correct lines, train a model | Training examples |
| Fri Sep 25 (#11) | AI, remote | LLM transcription and correction | Comparison reference |
| Week 5 Tue (#12) | Manual | Type it twice, settle differences | The text being checked |
| Week 5 Fri (#13) | Measurement | Score both machine attempts | The answer key |

Notice that today's file does a different job each time. Training examples on Wednesday. A comparison on Friday. The thing being checked in Week 5. The answer key at the end of Week 5. One file, four jobs — which is why its quality spreads so far.

The **Transcription Assignment is due Friday October 2**, at the end of Week 5, and includes your reconciliation report. These two weeks are really one task: type it, automate it, compare, settle, measure, report.

**Vocabulary.** *Reconciliation report* — your written account of the differences between versions and how you settled them. *Model* — the trained program that converts handwriting images into text.

**Takeaway:** Today's file serves as training data, comparison reference, verification object, and measurement reference — four roles, one artefact.

---

## **29 Content**

**What Good Work Looks Like Here**

"A transcription" and "a good transcription" are different things.

An acceptable one is accurate, covers the whole page, and passes validation.

A good one also:

- Marks doubt honestly, including where you would rather not admit it.
- Keeps short forms as written instead of quietly spelling them out.
- Keeps scribal corrections in both directions.
- Measures holes rather than just noting them.
- States its own rules.
- Records which photograph supported each difficult reading.
- Says what is still unresolved after checking every image.
- Has a commit history explaining the decisions.

The first is the hardest and the most telling. Marking a word `<unclear>` feels like admitting defeat, and the temptation is to pick the likelier reading and type it plainly. Resist that. An honest `<unclear>` is more useful to every later reader — including you in Week 8, building the apparatus — than a confident guess. It is the difference between recording evidence and announcing a conclusion.

**Vocabulary.** *Apparatus* — the list of variant and doubtful readings accompanying an edition. *Evidence* — what the page shows, as distinct from what you concluded from it.

**Takeaway:** Marking uncertainty honestly is the hardest and most diagnostic part of good transcription — a confident guess destroys the record of what was actually legible.

---

## **30 Content**

**Synthesis: The Anchor**

One idea holds this meeting and the whole week together.

Automated transcription is always measured *against something*. A character score is a distance from a reference. A word score is a distance from a reference. Every claim that a program is accurate, or better than another program, or good enough for a given manuscript, is a claim about distance from a reference. Without one, the output is text of unknown quality, and no amount of cleverness in the program supplies what the reference supplies (AlKendi et al., 2024).

That reference has to be made by hand, diplomatically, by someone who has read the page. This is not a shortcoming of today's technology that a better model will fix one day. It is structural. A ruler cannot be checked against itself, and a program's own output cannot show whether the program is right.

That is what makes the manual step unavoidable rather than merely traditional, and why Tuesday comes before Wednesday every week of this course. The three-step cycle is not hand work followed by better machine work. It is building a measuring instrument, then taking two measurements with it.

**For Wednesday.** Bring the seven items in section 22, especially your note on accent height. You will be correcting line boxes before you train anything.

**For Friday.** Remote. Check your whole setup per section 23 before then.

**Vocabulary.** *Reference* — the correct version everything else is scored against. *Three-step cycle* — this course's weekly pattern of manual, then deterministic, then AI-assisted work.

**Takeaway:** Automation is always measured against a reference, and a reference cannot be produced by the thing it measures — which is why the manual step is irreducible rather than merely traditional.

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
