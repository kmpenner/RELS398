# Lesson 4.3 — LLM-Assisted Transcription: Hallucination, Bias, and the Specialization Gap

*RELS 398 / ENGL 398 · Topic 4: Transcription · Meeting #11 (Fri Sep 25)*

***Step 3 of the three-step cycle: AI-assisted. Remote delivery.** Today you give the same page to a general AI model — the kind you can paste a picture into — and compare all three versions. What you are testing is whether sheer size makes up for never having seen material like yours.*

---

## **01 Content**

**Today's Question**

By this evening you will have three versions of one page: yours, typed by hand on Tuesday; your trained model's, from Wednesday; and a general AI model's, from today.

The question is not which is best. It is **what each kind of system does when it goes wrong, and what that tells you about the system.** A program that fails by producing letter-strings that are not words, and a program that fails by producing smooth invented Greek, have failed in ways that matter very differently to an editor — far more than the overall score does.

You should go in with an expectation, from Wednesday's section 23. Published tests show these general models doing superbly on modern handwriting and collapsing on old scripts: 1.39% of characters wrong on modern English, against 52.23% on historical English, from the very same model (AlKendi et al., 2024). Today you check whether that holds for your manuscript.

An expectation is not a conclusion. Run it properly, record what happens, and report what you find — even if it contradicts the published pattern. That would be interesting and worth reporting.

**Vocabulary.** *Vision-language model (VLM)* — an AI that takes pictures as well as words and answers in words. *Zero-shot* — used straight out of the box, with no training on your material. *Hallucination* — confident output that is not based on what was actually there.

**Takeaway:** The question is not which system is best but what kind of error each makes — the kinds differ more than the rates.

---

## **02 Content**

**What These Models Are**

The difference from Wednesday's tool explains everything that follows.

Your trained model learned from strips of handwriting paired with text. That is all it knows: ink to letters. Whatever it grasps about language it picked up sideways, from patterns in those letters.

A general AI model learned from a colossal sweep of the internet — text, pictures, and how they relate. It can take a whole page and give you a transcription from a plain English instruction. No line-finding, no training, no examples needed (AlKendi et al., 2024).

| | Your trained model | General AI model |
| --- | --- | --- |
| Learned from | Line strips with text | The internet |
| Size | Millions of settings | Billions |
| Setup needed | Line-fixing, examples, training | A sentence of instruction |
| Takes | One line strip | A whole page |
| Knowledge of language | Slight | Enormous |
| How it fails | Impossible letter strings | Smooth invention |

Row three is a real advantage and should not be brushed aside. Wednesday cost you a whole session. Today costs a sentence. If the quality matched, the argument would be over.

Row six is why it does not. A model with deep knowledge of language brings that knowledge to bear on unclear ink — and using expectation to settle unclear evidence is exactly what a diplomatic transcription must never do. Its greatest strength on modern text is its worst liability on your manuscript.

**Vocabulary.** *Prompt* — the instruction you type to an AI model. *Parameter* — one of the adjustable settings inside a model; these have billions.

**Takeaway:** A VLM's linguistic knowledge is its strength on modern text and its liability on manuscripts, because it resolves ambiguous ink by expectation.

---

## **03 Content**

**The Specialization Gap, in Numbers**

Have this in front of you before you run your own test.

| Material | Model | Characters wrong | Words wrong |
| --- | --- | --- | --- |
| Modern English | GPT-4o | 1.39% | 3.46% |
| Modern English | Claude 3.5 Sonnet | 8.55% | 10.28% |
| Historical English | GPT-4o | 52.23% | 72.16% |
| Historical English | Claude 3.5 Sonnet | 40.87% | 59.41% |
| Historical German | GPT-4o | 77.42% | 97.59% |
| Historical German | Qwen2-VL-7B | 76.25% | 97.77% |
| Medieval Latin | Tuned specialist | 14.60% | — |
| Medieval Latin | DeepSeek-OCR | 63.00% | — |
| Medieval Latin | Mistral-OCR-3 | 84.70% | — |

Read rows one and three together. The same model. The same language. Nearly forty times worse, and the only thing that changed is the century (AlKendi et al., 2024).

Read the last three rows together. On identical medieval Latin pages, a tuned specialist a fraction of the size got 14.6% wrong, while two large commercial systems got 63.0% and 84.7% wrong (Mattingly et al., 2024).

Pause on the 97% word error on historical German. A word score near 100% means essentially nothing came out right. That is not weak performance. That is failure — at a job the same model does beautifully on modern material.

This is the **specialization gap**. The specialists win because they have actually been shown scribal handwriting, odd short forms, joined letters, and irregular pages (Mattingly et al., 2024). The internet holds very little Byzantine Greek.

**Vocabulary.** *Benchmark* — a shared test set for comparing tools fairly. *Zero-shot* — applied without any training on this kind of material.

**Takeaway:** The same model achieves 1.39% CER on modern handwriting and 52.23% on historical — the gap is period, not language.

---

## **04 Content**

**Making Things Look Older Than They Are**

Beyond simply being wrong, these models fail in ways specialized tools cannot. The strangest is well documented.

**Over-historicization** means the model inserts old-fashioned characters that are not in the document — letters from an *earlier* period than the manuscript itself. It was found in studies of eighteenth-century Russian printing, where models produced Church Slavonic letters that had been abolished from the alphabet decades before the documents were printed (Levchenko, 2024).

It is worth thinking through why, because this is not a simple slip. The model has learned that old documents go with old-fashioned spelling. Shown a picture it recognizes as historical, it produces what it statistically expects historical text to look like — which can be older than the actual page. It is not misreading the ink. It is reading its own idea of the period.

What that costs:

| Model, whole-page mode | Characters wrong | Old letters inserted | How often |
| --- | --- | --- | --- |
| Tuned TrOCR | 1.83% | None | 0% |
| Gemini 2.5 Pro | 3.36% | Barely any | Low |
| Claude 3.5 Sonnet | 6.79% | Some | Medium |
| GPT-4o | 9.23% | Many | 59% of files |
| Transkribus PyLaia | 26.93% | None | 0% |

Compare rows four and five. GPT-4o scored far better than the plain PyLaia model — 9.23% against 26.93% — while inserting anachronistic letters in 59% of files. PyLaia scored much worse and never once invented an old letter (Levchenko, 2024).

**Vocabulary.** *Anachronism* — something from the wrong period. *Grapheme* — a single written character of a writing system.

**Takeaway:** GPT-4o beat a generic HTR baseline on CER while inventing anachronistic characters in 59% of files — the metric and the fidelity diverge.

---

## **05 Content**

**Why One Score Is Not Enough**

That table makes a point Week 5 builds on directly.

The character score treats every difference as equal. A model that puts an old-fashioned omega where the page has a plain o has made one substitution, counted the same as any other. But it is a different *kind* of mistake. It is not a misreading of ink. It is an invention of period spelling, and it wrecks exactly the evidence your transcription exists to hold.

The finding is stated plainly: the usual scores are not adequate for historical text, because a model can score well while destroying the very faithfulness that makes the transcription worth having (Levchenko, 2024).

Two extra measures have been proposed:

| Measure | Counts | Catches |
| --- | --- | --- |
| Historical Character Preservation Rate | Period-specific characters kept correctly | Quiet modernizing |
| Archaic Insertion Rate | Invented characters from earlier periods | Over-historicization |

The first catches a model that tidies the old away; the second catches one that lays old-fashioned spelling on thick (Levchenko, 2024). A model can score well on the usual number and badly on either.

For your Greek manuscript the questions are concrete. Does it keep the accents as written, or supply what it expects? Does it keep words run together, or impose modern spacing? Does it keep short forms, or spell them out? Does it keep the scribe's mistakes, or fix them?

Every one of those is a modernization the usual score would not reveal. Check them specifically today.

**Vocabulary.** *Preservation rate* — how much of the original's own character survives. *Silent modernization* — quietly updating old forms without saying so.

**Takeaway:** A model can score well on CER while silently modernizing or hallucinating archaism — check preservation and insertion separately.

---

## **06 Content**

**Mess, Chat, and Confident Gap-Filling**

A third kind of failure, different from misreading and from invention, and the one most likely to bite you today.

These models often read the words correctly and still ignore your instructions about line breaks and structure. They are also inclined to slip chat, background notes, or little history lessons straight into the transcription (AlKendi et al., 2024).

| Failure | What it looks like | Cost |
| --- | --- | --- |
| Line breaks lost | Text run together as paragraphs | Cannot match to your boxes; useless for training |
| Chat wrapping | "Here is the transcription:" | Must be stripped before scoring |
| Uninvited commentary | History notes mixed into the text | Corrupts the transcription |
| Modernized punctuation | Modern marks for scribal ones | Quiet normalizing |
| Short forms spelled out | Sacred names written in full | Faithfulness lost |
| Spaces inserted | Gaps put into unspaced writing | An unrecorded editorial act |
| Gaps quietly filled | Confident text over damage | Invention passed off as reading |

Row one is the practical problem. Wednesday's model produced line-by-line output because it worked on line strips. Today's model sees a whole page and hands back a block of prose. Without line breaks you cannot match it to your boxes, cannot train on it, and cannot compare it line by line against your own version.

Row seven is the scholarly problem. Asked to transcribe a damaged passage, these models will often supply plausible text for the damaged part without saying they have done so — inventing, in exactly the place where a `<gap/>` belongs.

Neither announces itself. You have to check for both.

**Vocabulary.** *Reflow* — running lines together into continuous prose. *Preamble* — introductory chat before the actual answer.

**Takeaway:** VLMs reflow lines, add commentary, and fill gaps confidently — none of which announces itself in the output.

---

## **07 Content**

**Setting Up a Fair Test**

Run this as a measurement, not a demonstration. The setup decides whether your results mean anything.

Hold these fixed:

- **The same passage.** Exactly the lines you typed on Tuesday and ran on Wednesday. Comparing different material is not comparing.
- **The same pictures.** Same leaves, same quality, same source.
- **Raw output kept.** Capture what comes back before you touch it.
- **The instruction written down.** Word for word.
- **The model and its version.** Behaviour changes between versions.
- **The date.** These services change without telling anyone.
- **One change at a time.** If you try several instructions, change one thing between them.

Items four and six are what make this repeatable, and they are what students skip. "The AI got 34% wrong" cannot be checked by anyone without the exact instruction and the version, because a different wording or a quietly updated model gives a different number.

Write your plan in `logs/vlm-method-w4.md` before you start. Then run it, and record what actually happened, including anything you changed halfway and why.

Treat surprises as findings, not mistakes. If it does far better than expected, that is worth chasing — but check first whether your passage is famous enough that the model may be reciting it from memory rather than reading it. Section 12 handles that.

**Vocabulary.** *Control* — something held fixed so a comparison is fair. *Reproducible* — able to be repeated by someone else with the same result.

**Takeaway:** Record the prompt verbatim, the model version, and the date — without them the result is not reproducible.

---

## **08 Content**

**Writing the Instruction**

The wording matters, and a casual instruction guarantees every failure in section 06.

A poor instruction: *"Transcribe this manuscript."* That invites chat, run-together lines, spelled-out short forms, modernized spelling, and confidently filled gaps — the whole set at once.

A better one states every constraint:

```text
Transcribe the Greek text in this manuscript image.

Requirements:
- Preserve line breaks exactly as in the manuscript. One output line
  per manuscript line.
- Transcribe diplomatically: preserve the spelling as written,
  including apparent errors. Do not correct or modernize.
- Do not expand abbreviations. Transcribe the shortened form as
  written.
- Preserve all Greek accents and breathings exactly as written.
- Preserve word spacing exactly as in the manuscript. If the text is
  written without spaces, do not insert any.
- Where text is illegible or damaged, output [ILLEGIBLE] rather than
  supplying a reading.
- Where you are uncertain, output the reading followed by [?].
- Output only the transcription. No preamble, commentary, or summary.
```

Every line there targets a documented failure. Do not drop any of them on the grounds that it probably will not happen.

Two notes. Asking the model to flag its own doubts gives you useful data but *not* a reliable guide — these models are poor judges of their own uncertainty, and section 11 comes back to this. And even a good instruction only reduces these failures. Check the output against every requirement anyway.

Record the exact wording in your log.

**Vocabulary.** *Constraint* — a requirement you state explicitly in the instruction. *Calibration* — whether stated confidence matches actual accuracy.

**Takeaway:** Every constraint in the prompt addresses a documented failure mode, and a good prompt reduces those failures without eliminating them.

---

## **09 Content**

**Running It**

Do the experiment.

- Pick the same leaf you typed on Tuesday.
- Give it the picture at the best quality the interface accepts.
- Use the instruction from section 08, word for word.
- Capture the whole raw answer, untouched.
- Save it to a file before you do anything else.
- Commit it straight away, with the labels, before correcting anything.

That last step is Wednesday's discipline, and it matters just as much here. Raw output must be committed unchanged, because it is what gets scored in Week 5. Correct before committing and the measurement is gone.

```text
feat(transcription): VLM transcription of f. 42r, uncorrected

Transcribed by [model, version] with no training, accessed 2026-09-25.
Instruction recorded word for word in logs/vlm-method-w4.md. Raw
output; nothing corrected and nothing reformatted.

AI-Generated: true
Model: [model name and version]
Prompt-Ref: logs/vlm-method-w4.md
Human-Verified: false
Ground-Truth-Commit: a3f9c21
```

If you try more than one model or instruction, commit each result separately with its own labels. Several runs mixed into one file cannot be untangled afterwards.

Resist fiddling with the wording until the output looks good. That just produces an instruction tuned to this one passage, which is not what you set out to measure. Run the planned test; note any extra attempts separately.

**Vocabulary.** *Raw output* — exactly what came back, before any human touched it. *Trailer* — a labelled line at the end of a commit message.

**Takeaway:** Commit the raw output before correcting or reformatting anything — that state is what Week 5 measures.

---

## **10 Content**

**Reading the Output Sceptically**

Now judge it. Work through categories rather than by impression, because impressions are useless here — smooth text feels accurate.

| Check | Question | Why it comes where it does |
| --- | --- | --- |
| Line count | Same number of lines as the page? | Decides whether comparison is even possible |
| Chat | Any preamble, commentary, summary? | Must be stripped before scoring |
| Accents | Present and correct? | The most likely quiet loss |
| Short forms | Kept, or spelled out? | Quiet normalizing |
| Word spacing | As on the page, or imposed? | An unrecorded change |
| Damaged parts | Marked, or confidently filled? | Invention passed off as reading |
| Spelling | Kept, including apparent errors? | Quiet correcting |
| Believable wrong words | Does it match the ink? | Needs the picture |

The last row cannot be checked by reading the output. Smooth text reads as correct, and the mistakes that matter most are the ones that read perfectly. You have to compare against the picture, line by line, zoomed in — Tuesday's discipline again.

Row six deserves special attention. Find the damaged patch you identified back in Lesson 3.2 and look at what the model put there. If it supplied confident text where you recorded a `<gap/>`, you have caught invention on your own manuscript — worth far more in your report than any published figure.

Sort every mistake into a category. Counts by category are what Week 5 needs.

**Vocabulary.** *Impressionistic* — judging by overall feel rather than by checking. *Taxonomy* — a set of categories for sorting things.

**Takeaway:** Fluent output reads as correct, so check against the image — and look specifically at where you recorded damage.

---

## **11 Content**

**It Does Not Know What It Does Not Know**

You asked the model to flag doubts. Now judge whether the flags were any use.

These models are poor judges of their own uncertainty. Their stated confidence does not track their accuracy: they will flag readings that are right and state readings confidently that they invented. The `[?]` marks are data about the model's behaviour, not a trustworthy guide to where to look.

Test it on your own output. Take the flagged readings and the confident ones, and check both against the picture.

| What you find | What it means |
| --- | --- |
| Flagged ones mostly wrong, confident ones mostly right | Reasonably well judged here |
| Flags seem unrelated to accuracy | Self-report is useless as a guide |
| Confident text over a damaged patch | Invention; the most serious finding |
| No flags at all despite visible damage | It has no sense of its own limits |

Rows three and four are what to look for, and either is a substantial finding. A model that reads confidently where you know the page is illegible has shown, on your manuscript, that it cannot be trusted precisely where you most wanted help.

There is a hard consequence. If the flags do not line up with the mistakes, there is no way to know which parts need checking short of checking all of it — which means the tool saves you no checking work at all, whatever it saves in typing.

Record what you find. It bears directly on whether this method is usable here.

**Vocabulary.** *Self-report* — the model's own statement about its confidence. *Verification labour* — the work of checking output against the source.

**Takeaway:** If the model's uncertainty markers do not track its errors, you must check everything — and the tool saves no verification labour at all.

---

## **12 Content**

**Is It Reading, or Reciting?**

A check that matters if your passage is from a well-known text, and one almost nobody thinks to run.

A model trained on the internet has almost certainly met the *text* of your manuscript — not the pictures, but the words, in printed editions and scholarly discussion. Asked to transcribe a famous passage, it may produce the *edited* text from memory rather than reading the ink.

That would give you excellent-looking output that is worthless, because it would be reproducing a modern printed edition rather than your copy — and the differences between those two are exactly the readings your edition exists to record.

Two tests tell reading from reciting.

**The variant test.** If your manuscript has a reading that differs from the standard printed text, look at what the model produced there. Reading the ink gives you your manuscript's reading. Reciting gives you the printed one. This is the strongest test available, and it is why you should know your passage's variants in advance.

**The damage test.** Look at what it produced where you recorded illegible text. A model reading the ink cannot read what is not there. A model reciting fills the gap fluently *and correctly* — which is more damning than filling it wrongly.

| What you see | What it means |
| --- | --- |
| Your manuscript's odd reading reproduced | Reading the picture |
| The printed reading where your copy differs | Reciting from memory |
| Illegible patch left marked | Reading the picture |
| Illegible patch filled with the standard text | Reciting from memory |
| Illegible patch filled with plausible invention | Making it up |

Run both and report the result. For a well-known text this is the most important check you make today.

**Vocabulary.** *Variant* — a place where your copy's wording differs from another's. *Memorization* — reproducing training material rather than working from the input.

**Takeaway:** Where your manuscript differs from the printed text, a model reciting from memory gives the printed reading — that is the test.

---

## **13 Content**

**A Rough Score**

Proper measurement is Week 5's job, but a rough figure today gives you something to hold up.

The character score is the smallest number of single-character changes needed to turn the machine's text into yours, divided by the length of yours (AlKendi et al., 2024):

```python
def cer(reference: str, hypothesis: str) -> float:
    """Character error rate: edit distance / reference length."""
    import unicodedata
    r = unicodedata.normalize("NFC", reference)
    h = unicodedata.normalize("NFC", hypothesis)
    prev = list(range(len(h) + 1))
    for i, rc in enumerate(r, 1):
        cur = [i]
        for j, hc in enumerate(h, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1,
                           prev[j - 1] + (rc != hc)))
        prev = cur
    return prev[-1] / len(r) if r else 0.0
```

Notice both texts get normalized first. This is Lesson 1.2 arriving in practice: compare accents stored one way against accents stored the other way, and your score measures storage rather than transcription. The inflation can be huge. Always normalize both.

Two more warnings about today's figure. Strip any chat before comparing, or you score the preamble as error. And if line breaks were lost, you can only compare the whole text at once, and that number is not comparable to a line-by-line one.

Work out the same figure for Wednesday's output against the same reference, so the comparison is like for like. Record both, with the caveats.

**Vocabulary.** *Edit distance* — the count of single-character changes between two texts. *Normalize* — store accented characters in one consistent way.

**Takeaway:** Normalize both strings to NFC before computing CER, or you measure encoding difference rather than transcription difference.

---

## **14 Content**

**Where These Tools Genuinely Help**

Fairness is owed. The evidence is against using a general AI to transcribe old manuscripts cold. It is not against these tools in general, and dismissing them wholesale would be as thoughtless as adopting them wholesale.

| Task | Suitable? | Why |
| --- | --- | --- |
| Transcribing historical manuscripts cold | Poor | The specialization gap; invention; false archaism |
| Transcribing modern handwriting | Good | Well represented in training |
| Transcribing printed text in common languages | Good | Very well represented |
| Translating a transcription you already have | Good | A language job, not a reading job |
| Explaining a short form or a script feature | Useful | Retrieving documented knowledge |
| Suggesting parallels for a phrase | Useful, if you verify | Broad coverage |
| Drafting code for your workflow | Good | Very well supported |
| Tidying up reading output | Harmful | Documented to make things worse |

The advice is specific: unless your manuscript is a late modern document in a well-represented language, do not rely on a general AI for diplomatic transcription. The risk of false archaism, quiet modernizing, and mangled structure outweighs the setup time you save (AlKendi et al., 2024).

The last row is Wednesday's finding again. Adding AI tidying after a reading step makes the overall result worse (Mattingly et al., 2024). The tidying step cannot see the picture, so it corrects toward whatever sounds likely — which reliably damages the unusual readings that matter.

The thread running through the table: these tools are good where knowing language is the point, and bad where knowing language contaminates the evidence. Transcription is the second kind.

**Vocabulary.** *Contaminate* — to let outside knowledge alter the evidence. *Wholesale* — accepting or rejecting something entirely, without distinction.

**Takeaway:** These tools help where linguistic knowledge is the point and harm where it contaminates evidence — transcription is the second kind.

---

## **15 Content**

**Where That Leaves the Method**

A working position rather than a ban.

These tools do not replace the person who reads manuscripts. They move that person's effort from deciphering toward checking and interpreting (AlKendi et al., 2024). That shift is real and valuable — but only where the output is good enough that checking it costs less than typing it.

Wednesday's threshold applies: past roughly 15% of characters wrong, correcting costs more than typing from scratch (AlKendi et al., 2024). A tool above that line is not a saving with a quality cost. It is extra work.

Today's likely finding is that the general model sits above that line on your manuscript while your trained model sits below it. If so, the conclusion is not that AI is useless. It is that *the specialized tool is the right one for this job* — and that conclusion now rests on your own measurement rather than on being told.

The three-step cycle exists to produce exactly this kind of grounded judgement. You have now seen what a person, a bounded specialist, and an unbounded generalist each produce on the same lines. That is the basis for choosing tools deliberately for the rest of the term, and for defending the choice in your Week 12 commentary.

**Vocabulary.** *Threshold* — the point at which the sensible choice flips. *Grounded* — supported by evidence you gathered yourself.

**Takeaway:** Automation saves labour only below the threshold where correction costs less than transcription — and you have now measured where your tools sit.

---

## **16 Content**

**Recording AI Use in the Repository**

The syllabus requires you to disclose AI use, and the repository is where that disclosure lives.

Every commit holding machine-made content carries labels recording the model, the instruction, and whether a person has checked it. For today:

```text
AI-Generated: true
Model: [name and version]
Model-Access-Date: 2026-09-25
Prompt-Ref: logs/vlm-method-w4.md
Human-Verified: false
Ground-Truth-Commit: a3f9c21
```

`Model-Access-Date` matters more than it looks. These services run on someone else's computers and can change overnight without the version number moving, so the date is often the only record of what actually produced your text. A result reported without it may not be repeatable even by you, a month later.

The audit commands from Lesson 1.1 now return something meaningful:

| Question | Command |
| --- | --- |
| What in my edition was machine-made? | `git log --grep="AI-Generated: true"` |
| What has nobody checked? | `git log --grep="Human-Verified: false"` |
| Which models did I use? | `git log --pretty=format:"%(trailers:key=Model)"` |
| How much is machine-assisted? | `git rev-list --all --grep="AI-Generated: true" --count` |

Run the second one now. It should list Wednesday's raw output and today's — the two places in your repository where a machine wrote something and nobody has verified it. That is an honest picture of your edition's current state, and it is exactly what a reader of a digital edition should be able to ask for.

**Vocabulary.** *Disclosure* — stating openly where machine assistance was used. *Audit* — checking a record to see what was actually done.

**Takeaway:** Record the model access date — a hosted model can change without notice, making the date the only record of what produced the output.

---

## **17 Content**

**Putting the Three Side by Side**

Bring the three versions together. This is the week's real product.

Build `logs/three-way-w4.md` with a row per line:

| Line | Yours (reference) | Trained model | General AI | Notes |
| --- | --- | --- | --- | --- |
| 1 | ἐν ἀρχῇ ἦν ὁ λόγος | ἐν ἀρχῇ ἦν ὁ λόγος | ἐν ἀρχῇ ἦν ὁ λόγος | All three agree |
| 2 | θν καὶ θς | θν καὶ θς | θεόν καὶ θεός | AI spelled the short forms out |
| 3 | ἦν ὁ λόγος οὗτος | ἦν ὁ λογος οὑτος | ἦν ὁ λόγος οὗτος | Trained model dropped accents |
| 4 | [gap, 6 chars] | [nonsense] | διʼ αὐτοῦ πάντα | AI filled the gap |

Row four is the finding in miniature. Where the page is damaged, you recorded a measured gap, the trained model produced something visibly wrong, and the AI produced fluent plausible Greek that is not on the parchment. Three systems, three characteristic behaviours, one line.

A diff makes this easier to build:

```bash
git diff gt-f42r:edition/edition.xml htr-w4-raw:edition/htr-output.txt
```

This is where Tuesday's and Wednesday's tags earn their keep.

Do at least ten lines, and make sure they include every line where you recorded doubt or damage. Those are the informative ones. Agreement on easy lines tells you almost nothing; what each system does when the evidence runs out tells you everything.

**Vocabulary.** *Diff* — a comparison showing what differs between two versions. *Three-way comparison* — setting three versions of the same thing against each other.

**Takeaway:** Compare on the lines where you recorded uncertainty — agreement on easy lines is uninformative, and divergence on hard lines is the finding.

---

## **18 Content**

**Sorting the Mistakes**

Categorize what you found, because the categories are what your Week 5 report argues from.

| Kind of mistake | You | Trained model | General AI |
| --- | --- | --- | --- |
| Misread letter | Occasional | Common | Common |
| Dropped accents | Rare | Common, usually a strip fault | Varies |
| Short forms spelled out | Never, if diplomatic | Rare | Common |
| Spelling modernized | Never, if diplomatic | Rare | Common |
| Impossible letter strings | Never | Occasional | Rare |
| Believable wrong words | Rare | Rare | Common |
| Text invented over damage | Never | Never | Documented |
| Line breaks lost | Never | Never | Common |
| Commentary inserted | Never | Never | Common |
| Reading what you expected | Occasional | Never | By design |

Read the bottom four rows down the columns. Those four failures belong almost entirely to the general AI, and not one of them is a *reading* mistake. They follow from it being a language machine pointed at a reading job. It reformats because it writes prose. It chats because it converses. It invents because it completes.

Read the last row across. Your own signature failure — reading what you expect rather than what is written — is one the trained model structurally cannot make, because it has no expectations. The general AI makes it by design, since applying expectation is exactly what it does.

That is a useful symmetry. The trained model is a check on your expectation-driven slips, and you are a check on its ink-level slips. That mutual checking is what "human in the loop" actually means in practice.

**Vocabulary.** *Failure mode* — a characteristic way a system goes wrong. *By construction* — following necessarily from how something is built.

**Takeaway:** The VLM's distinctive failures are not recognition errors but consequences of being a language model — and the HTR model cannot make your expectation-driven errors.

---

## **19 Content**

**Reporting a Result That Did Not Work**

If today's AI output was poor, that is a result. Report it as one.

There is a habit in coursework of treating a technique that failed as an assignment that failed, and reporting only the parts that worked. That is the opposite of what is wanted here. A documented negative result — this model, this instruction, this manuscript, this score — is a real contribution, and it saves the next person from repeating the attempt.

Report:

- The model and version, and the date you used it.
- The exact instruction.
- The raw output, committed unchanged.
- The measured score, with its caveats.
- The kinds of mistake, with counts.
- What specifically failed: accents, short forms, line breaks, damaged patches.
- Whether you tested for reciting, and what you found.
- Your judgement on whether the method is usable for this manuscript.

That last item is the scholarly part. Not "the model was bad", but something like: *for this hand, in this script, at this resolution, an untrained general model produced X% character error with systematic spelling-out of short forms and invented text in damaged regions, and is therefore unsuitable as a primary transcription method for this edition, though it may remain useful for [specific task].*

That statement is specific, defensible, and useful — and it is exactly what the Week 5 report asks for.

**Vocabulary.** *Negative result* — a finding that something does not work, which is still a finding. *Defensible* — able to be supported when questioned.

**Takeaway:** A documented failure — this model, this prompt, this manuscript, this rate — is a contribution, and vague dismissal is not.

---

## **20 Content**

**Working Remotely Today**

Today is remote. A few things are worth checking rather than assuming.

- Your repository is pushed, and your local copy is up to date.
- Your images load from the network you are on.
- Your Greek keyboard works on this machine.
- Your XML editor checks against the TEI rulebook here.
- Python and your accent tools run here.
- Your pre-commit hook is installed *in this copy*.

The last one catches people. Hooks live in `.git/hooks/`, and that folder is **not copied** when you clone a repository. If you are working from a fresh copy today, your accent-fixing hook does not exist here, and every commit you make will slip past it.

Install it now, from your tracked `tools/` folder, before you commit anything:

```bash
cp tools/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

Then test it: make a file with decomposed Greek, stage it, commit, and check the stored bytes. An untested hook on a new machine is not a safeguard.

Push before you finish. Today's work has to be available on whatever machine you use next week, and leaving a remote session's output on a laptop is a common way to lose it.

**Vocabulary.** *Clone* — your own copy of a repository. *Hook* — a script git runs automatically at a set moment.

**Takeaway:** Hooks are not cloned — install and test your NFC hook on this machine before committing anything today.

---

## **21 Content**

**What This Week Established**

Pull the week's findings together, since Week 5 argues from them.

| Finding | Evidence |
| --- | --- |
| Starting from an existing model is decisive | 17.18% wrong from scratch versus 3.90% with it, same data (Perdiki & Konstantinidou, 2023) |
| Matching the material beats being big | Tuned specialist 14.6% versus a large model's 84.7%, same pages (Mattingly et al., 2024) |
| General AI collapses on old material | GPT-4o 1.39% modern versus 52.23% historical English (AlKendi et al., 2024) |
| A good score can hide lost faithfulness | GPT-4o 9.23% while inserting old letters in 59% of files (Levchenko, 2024) |
| Line-finding faults ruin the reading | Chopped strips delete Greek accents entirely (Perdiki & Konstantinidou, 2023) |
| More steps make it worse | Plain workflow beats versions with extra AI stages (Mattingly et al., 2024) |
| Models break when the layout changes | 5.1% on plain pages versus 13.6% on glossed ones (Geelhaar, 2022) |
| Past 15% wrong, correcting costs more than typing | (AlKendi et al., 2024) |

These are not opinions about AI. They are measurements, from published tests, which you have now partly repeated on your own manuscript.

The claim that ties them together is the week's thesis: automated transcription genuinely speeds the work *and* absolutely depends on a hand-made diplomatic reference, because that reference is the only thing against which error, bias, and invention can be measured at all (AlKendi et al., 2024).

Every row in that table is a measurement against a reference somebody made by hand.

**Vocabulary.** *Thesis* — the central claim an argument sets out to establish. *Replicate* — repeat a study to see whether the result holds.

**Takeaway:** Every finding in the table is a measurement against a hand-produced ground truth — which is the week's thesis in operation.

---

## **22 Content**

**Checklist Before You Finish**

Check each one.

- AI transcription run on the same leaf as Tuesday and Wednesday.
- Instruction recorded word for word in `logs/vlm-method-w4.md`.
- Model name, version, and date recorded.
- Raw output committed unchanged, with the labels.
- Output checked against every item in section 10.
- Damaged patches specifically examined for invented text.
- Reciting tested for, if your text is well known.
- The model's own doubt flags checked against actual accuracy.
- Rough score worked out for both machine versions, both normalized.
- Three-way comparison table built for at least ten lines.
- Mistakes sorted by kind, with counts.
- Time recorded for all three methods.
- Everything committed and pushed.

Item seven applies only to well-known texts, but where it applies it is the most important check available. A model reproducing a printed edition from memory gives you excellent-looking output that is worthless as a record of *your* copy, and nothing else on this list would catch it.

**Vocabulary.** *Checklist* — a list checked item by item rather than from memory. *Witness* — one manuscript copy of a text, treated as evidence.

**Takeaway:** For a well-known text, the memorization test is the most important check available — nothing else detects a recited printed edition.

---

## **23 Content**

**Looking Ahead to Week 5**

Next week reconciles and measures. It is a two-meeting week by design — Wednesday September 30 is closed for Truth and Reconciliation, and nothing is lost, because reconciliation *is* the comparison.

| Meeting | Step | What you do |
| --- | --- | --- |
| Tue Sep 29 (#12) | Manual | Type it twice; settle the differences by hand |
| Fri Oct 2 (#13) | Measurement | Score both machine versions against your reference |

Tuesday tackles the problem raised in Lesson 4.1: your reference has mistakes in it, and treating it as perfect makes every measurement partly wrong. Typing it independently a second time and settling the differences gives you a much better reference.

Friday does the measuring properly — line by line, normalized, sorted by kind, with the judgement that section 05 argued a single number cannot supply.

**The Transcription Assignment is due Friday October 2**, and it includes the reconciliation report. Everything you recorded this week — methods, comparisons, categories, timings — is material for it. Students who kept those records write the report. Students who did not, do the work again.

**Vocabulary.** *Reconciliation* — settling the differences between versions of the same text. *Consensus text* — the agreed version produced after settling them.

**Takeaway:** Week 5 double-keys the ground truth and then measures against it — and the Transcription Assignment on October 2 includes the reconciliation report.

---

## **24 Content**

**What Good Work Looks Like Here**

An acceptable result is an AI transcription, committed, with a score.

Good work also:

- Uses an instruction built against the documented failures, recorded word for word.
- Keeps the raw output untouched before any judging.
- Checks against every category in section 10, not by impression.
- Looks specifically at damaged patches for invention.
- Tests for reciting where the text is well known.
- Checks the model's doubt flags against its actual mistakes.
- Normalizes both texts before working out any score.
- Reports cost as well as quality, for all three methods.
- Draws a specific, defensible conclusion about *this* manuscript.
- Reports failures fully.

The ninth item is what the whole week is for. "AI is unreliable for manuscripts" repeats what you were told. "For this tenth-century Greek minuscule at this resolution, model X produced Y% character error with systematic spelling-out of short forms and invented text in two damaged regions, against my trained model's Z%" is something you established.

The difference between those two sentences is the difference between having read about the specialization gap and having measured it.

**Vocabulary.** *Deliverable* — the finished thing you are expected to produce. *Specific* — naming the actual material, model, and numbers involved.

**Takeaway:** A specific measured conclusion about *your* manuscript is the deliverable; a general claim about AI is a repetition of what you were told.

---

## **25 Content**

**Choosing Tools for the Rest of the Term**

Today's results should shape how you work from Week 6 on.

If your trained model does well — under about 10% wrong — use it to extend your transcription across the remaining leaves, correcting against the pictures and committing raw and corrected states separately. That is the intended workflow, working as intended.

If it does badly, diagnose before giving up. Wednesday's order applies: line-finding, alignment, amount of training material, starting model. Most poor first models are fixable, and the usual fix is more or better-chosen examples.

For the general AI, the honest position after today is probably that it is unsuitable for your primary transcription, while remaining useful for other things — explaining script features, drafting workflow code, suggesting parallels you then verify, translating a transcription you already have.

What you should not do, from Wednesday, is pass your trained model's output through an AI to clean up. That setup is documented to make things worse (Mattingly et al., 2024), and it will damage precisely the unusual readings your edition exists to record.

Write down your tool decisions and your reasons. Week 12's commentary has to state what produced the text, and a reason recorded now is worth far more than one reconstructed in December.

**Vocabulary.** *Workflow* — the sequence of steps you use to do the work. *Amortize* — spread a one-off cost across enough uses to be worth it.

**Takeaway:** Let today's measurement set your tool choices for the term, and record the reasons at the time rather than reconstructing them later.

---

## **26 Content**

**The Bigger Point**

Step back from transcription, because this pattern returns every week for the rest of the term.

Each week runs the same job three ways: by hand, with a specialized tool, and with AI. That structure is not about transcription. It is a general way of judging computational tools in scholarly work, and the logic is the same each time.

The manual step builds a reference and, just as importantly, builds *your* understanding of the material. The specialized step shows what a bounded, purpose-built tool produces — fast, consistent, limited to what it was made for. The AI step shows what an unbounded general tool produces — faster still, more flexible, and capable of failures the other two structurally cannot commit.

Comparing them gives you something none of the three gives alone: a measured account of what each is good for on *this* material. That is the only sound basis for choosing tools.

Notice that the method needs the manual step to come first and to be done properly. Every measurement is a distance from the reference, and a damaged reference damages everything computed from it. That is why Tuesday is not a warm-up.

**Vocabulary.** *Bounded* — limited to a defined range. *Unbounded* — not restricted to any particular domain.

**Takeaway:** The three-step cycle is a general method for evaluating tools against material, and it collapses if the manual reference is compromised.

---

## **27 Content**

**Counting the Cost Honestly**

One more comparison, because quality without cost is half an argument.

| Method | Setup | Cost per leaf afterwards | Quality here |
| --- | --- | --- | --- |
| By hand | None | Highest | The reference |
| Trained model | A whole session | Low, plus correcting | Your figure |
| General AI | Minutes | Very low, plus correcting | Your figure |

Fill the right column from today's measurements and the middle from your own timings.

The comparison genuinely has three dimensions and resists a simple ranking. Typing by hand costs nothing to set up and the most per leaf. The trained model costs a session to set up and little per leaf — so it pays off across many leaves and does not pay off across four. The general AI costs almost nothing either way and, on old material, may produce output not worth correcting at all.

The threshold governs. Past roughly 15% wrong, correcting costs more than typing, and a tool being cheap per leaf is irrelevant if its output has to be thrown away (AlKendi et al., 2024).

For a passage of twenty to forty lines — your edition — the honest sum may well be that typing by hand beats the trained model, because the setup never pays for itself. Say so if you find it. The value of the exercise is in having measured the trade-off on real material, not in reaching a conclusion someone decided in advance.

**Vocabulary.** *Setup cost* — the one-off effort before any output. *Marginal cost* — what each additional unit costs after that.

**Takeaway:** For a short passage, HTR's setup cost may never amortize — say so if you find it, because the measurement is the point.

---

## **28 Content**

**Committing and Pushing**

Close the week out properly.

Everything committed today should carry full provenance. Check with the audit commands:

```bash
git log --grep="AI-Generated: true" --oneline
git log --grep="Human-Verified: false" --oneline
```

The second lists what a machine wrote and nobody has checked. If you have corrected today's output, commit the corrections separately, and that commit should say `Human-Verified: true`.

Tag today's raw output:

```bash
git tag -a vlm-w4-raw -m "Raw VLM output, [model/version], before correction"
git push --tags
```

Push everything, tags included. **Tags are not pushed by default.** The three tagged states from this week — `gt-f42r`, `htr-w4-raw`, `vlm-w4-raw` — are what Week 5's measurement goes and fetches. A tag that exists only on this laptop is a tag Week 5 cannot use if you work from anywhere else.

Check the push worked and the tags are on the remote before you stop. A remote session that ends with unpushed work is a session you may have to repeat.

**Vocabulary.** *Remote* — the copy of your repository on the server. *Push* — send your commits to it.

**Takeaway:** Push tags explicitly — they are not pushed by default, and Week 5's measurement retrieves the tagged states.

---

## **29 Content**

**Pulling the Week Together**

What Topic 4 established, across three meetings.

Tuesday: a diplomatic transcription keeps what the manuscript shows — short forms, doubts, corrections, damage. It is made by hand, zoomed in, by somebody reading rather than expecting. And it serves at once as training material, as a comparison, as the thing being checked, and as the answer key.

Wednesday: finding the lines comes before reading them, and faults in the first wreck the second. The strips must include Greek accents or the model never sees them. Starting from a matched existing model is decisive. And a specialist's limited competence makes it fail loudly rather than smoothly.

Friday: general AI models collapse on historical material despite excelling on modern. They fail in ways specialists cannot — inventing old spellings, fabricating fluently, mangling the structure. And a good score can sit alongside the destruction of everything that made the transcription faithful.

The thread: automation speeds the work and depends on a hand-made diplomatic reference, because that is the only thing its errors can be measured against (AlKendi et al., 2024).

Week 5 takes that reference, improves it by typing it twice, and does the measuring properly.

**Vocabulary.** *Topic* — one week's unit of this course. *Ground truth* — the hand-made reference everything is scored against.

**Takeaway:** Three meetings, one thesis — automation accelerates transcription and depends absolutely on a hand-produced reference to be evaluated at all.

---

## **30 Content**

**Synthesis: Reading Well Is Not Reading Right**

The finding worth carrying out of this week.

A general AI model pointed at a historical manuscript produces fluent text. It reads well. The Greek is grammatical, the vocabulary is plausible, the sentences finish properly. And on old material it may be wrong at rates approaching 80% of characters, may insert spellings from centuries before the document, and may supply confident readings for parchment carrying no legible ink at all (AlKendi et al., 2024; Levchenko, 2024).

Reading well and being right are independent properties. The systems best at the first are not the systems best at the second. That is the week's central lesson, and it reaches well past transcription: the better a tool is at producing plausible output, the less its plausibility tells you about its accuracy — and the more you must check against the source.

This is why the specialist's loud failures are a virtue. Output that announces its own doubt by being obviously wrong is safer than output that hides its doubt by being smooth. A model producing an impossible letter string has told you something true about the ink. A model producing a perfect word has told you something about its own expectations.

And it is why the manual step cannot be removed. Only somebody who has read the parchment can tell those apart — and having read it, they hold the reference everything else is measured against.

**Due Friday October 2.** The Transcription Assignment, including the reconciliation report, at the end of Week 5.

**For Tuesday.** Week 5 opens with double-keying: type your leaf again, independently, without looking at Tuesday's version first. The independence is what makes the comparison worth anything.

**Vocabulary.** *Fluency* — reading smoothly and naturally. *Fidelity* — matching the source faithfully. They are not the same thing.

**Takeaway:** Fluency and fidelity are independent, and the more plausible a tool's output, the less its plausibility tells you about its accuracy.

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
