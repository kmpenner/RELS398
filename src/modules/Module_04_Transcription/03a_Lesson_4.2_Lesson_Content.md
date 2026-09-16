# Lesson 4.2 — Layout Analysis and HTR Model Training in Transkribus

*RELS 398 / ENGL 398 · Topic 4: Transcription · Meeting #10 (Wed Sep 23)*

***Step 2 of the three-step cycle: deterministic.** Today you load yesterday's transcription into Transkribus, fix how it divides the page into lines, and train it to read your scribe's handwriting. This kind of program reads the ink and nothing else — which shapes the mistakes it makes.*

---

## **01 Content**

**What "Deterministic" Means This Week**

Every Wednesday this term you use a specialized tool rather than a general AI chatbot. The word *deterministic* is doing real work here, so it is worth pinning down.

Today's program is not deterministic in the sense of following rules a person wrote. It learns from examples. It is deterministic in two ways that matter. The same picture always produces the same answer. And it only knows what its examples taught it.

That boundary is a weakness and a protection at once. Hand it writing it has never seen and it will do badly. But it will not invent a convincing sentence that is not on the page, because it has no idea what sentences are supposed to look like. It only knows shapes of ink (Puigcerver, 2017).

Friday's tool does know what sentences look like. That difference is the entire point of the three-step cycle. Today shows you what a program produces when it reads *only the picture*. Friday shows what happens when it also brings expectations about language.

**Vocabulary.** *HTR* — handwritten text recognition, software that turns handwriting images into typed text. *Model* — the trained program that does the reading. *Training* — showing the program examples until it learns.

**Takeaway:** A specialized HTR model is bounded by its training data, which makes it fail rather than fabricate — the opposite of Friday's tools.

---

## **02 Content**

**Finding the Lines Comes Before Reading Them**

Automatic transcription is really two jobs, and mixing them up causes most of the confusion about why it fails.

The first job is **finding the text**: which parts of the page have writing, how that writing divides into lines, and what order to read them in. The second job is **reading**: working out what each line says.

The order is strict. The reading step never sees the page. It only ever sees the little strips of image that the first step cut out. It can only read what is in those strips.

| Stage | Gets | Produces | If it goes wrong |
| --- | --- | --- | --- |
| Find regions | The page picture | Blocks of writing | Whole passages missed |
| Find lines | Blocks of writing | One line each | Lines merged or split |
| Cut out strips | Lines | Strip images | Tops or tails chopped off |
| Decide order | The set of lines | A sequence | Text comes out jumbled |
| Read | Strip images | Text | Wrong letters |

Mistakes in the first job feed straight into the second (AlKendi et al., 2024). This is the most useful thing to know about how these tools fail, and it explains something otherwise baffling: when a program reads most of a page well and produces gibberish on one part, the trouble is almost always in how that part was cut up, not in the reading.

So build the habit now. When output is bad, look at the strip images before you blame the program. If the strip is wrong, no amount of cleverness can rescue it.

**Vocabulary.** *Layout analysis* — the step that finds the writing and divides it into lines. *Line image* — the strip cut from the page holding one line.

**Takeaway:** Recognition only ever sees line images that layout analysis produced — so when output is bad, inspect the line images first.

---

## **03 Content**

**Why Rectangles Do Not Work**

A short history, because it explains why today's tools behave as they do.

Early software drew a **rectangle** around each line. That is fine for printed books, where lines are straight and evenly spaced. It is poor for manuscripts. Manuscript pages have notes crammed in the margins, words squeezed between lines, two columns, and lines that wander (Perdiki & Konstantinidou, 2023). A rectangle cannot describe a line that slopes or curves.

Modern software finds the **baseline** instead — the invisible line the letters sit on. A baseline can bend and slope, following the writing wherever it goes. From it, the program works out a shape around the tall letters and the tails, and cuts out the strip (AlKendi et al., 2024).

| Approach | Describes a line as | Copes with |
| --- | --- | --- |
| Rectangle | A straight-sided box | Printed text only |
| Pixel labelling | A blob of marked pixels | Odd shapes; but merges close lines |
| Baseline plus shape | A bending line with a cut-out region | Sloping, crowded manuscript lines |
| Object detection | A detected line "thing" | Complicated historical pages |

Pixel labelling — marking every dot on the page as writing or not — was a step along the way, and it fails predictably. It glues together lines whose tall and low letters touch, and it breaks one line in two where the ink is faint. Both happen constantly in manuscripts.

Transkribus and eScriptorium both work from baselines, though they do it differently.

**Vocabulary.** *Baseline* — the invisible line letters sit on. *Ascender / descender* — the parts of letters that stick up above or hang below it.

**Takeaway:** Modern layout analysis predicts sloping baselines and computes envelopes around them, because manuscript lines do not fit rectangles.

---

## **04 Content**

**Loading Your Manuscript In**

Time to start. Transkribus pulls your images in from a web address — which is why Lesson 3.3 insisted your image listing had to work over the internet.

- Make a new collection in Transkribus for your edition.
- Import using the web address, not by uploading files.
- Check the right number of pages arrived.
- Check the images are full size, not thumbnails.
- Check the pages are in the right order.

If the import fails, the causes are the ones Lesson 3.3 warned about: the address is not reachable from outside, the library demands a login, or the listing is slightly malformed in a way that viewers forgive and platforms do not. Test it with `curl` from outside your own network before deciding Transkribus is broken.

Pulling images in by address rather than uploading them has a real advantage. The pictures stay the library's, served from the library's computers, at whatever quality they offer. You are not making a private copy that slowly drifts out of date, and the trail from your training examples back to the original photographs stays unbroken.

Import only the leaves you will actually work on. A collection holding an entire book when you need four leaves makes everything afterwards slower.

**Vocabulary.** *Collection* — a Transkribus folder holding the pages of one project. *`curl`* — a command-line tool that fetches a web address so you can see what is really there.

**Takeaway:** Import by manifest URI so training data stays linked to the institutional source rather than becoming a detached copy.

---

## **05 Content**

**Running It, Then Checking It**

Run the automatic line-finding on your pages. Then, before anything else, look hard at what it did. This checking is today's most important task.

For each page, ask:

- Did it find all the writing, including margins and headers?
- Did it find every line? Count them against the manuscript.
- Did it glue any two lines together?
- Did it split any line in two?
- Does each baseline follow the writing, or wander off it?
- Is the reading order right, especially around margin notes?
- Do the cut-out strips include the full height of the writing?

That last question is the Greek one, and it is what you prepared for yesterday. The program guesses how tall a line is from how the script usually behaves. A scribe who puts breathing marks and accents high above the letters will often have them fall outside the strip.

Perdiki and Konstantinidou (2023) hit exactly this. Their software kept leaving out breathing marks and high abbreviation signs, and getting the error rate below 10% meant widening those strips by hand.

Zoom in on a line with a high breathing mark and look at where the strip boundary runs. If the mark is outside it, every accent in your training examples is being thrown away before the program ever sees it.

**Vocabulary.** *Reading order* — the sequence the program will read the lines in. *Region* — a block of the page marked as containing writing.

**Takeaway:** Check whether polygons enclose high-placed breathings and accents — if they do not, the model is being trained on Greek with the diacritics cut off.

---

## **06 Content**

**Fixing the Lines by Hand**

Where the automatic pass got it wrong, fix it. This is dull work and it decides everything that follows.

| Problem | Fix |
| --- | --- |
| A line was missed | Draw its baseline yourself |
| Two lines glued together | Split them, then adjust both |
| One line broken in two | Merge the pieces |
| Baseline wanders off the writing | Drag its points back onto the ink |
| Strip cuts off the accents | Extend the top edge |
| Strip cuts off letter tails | Extend the bottom edge |
| Lines in the wrong order | Renumber them |
| A margin note swallowed into the text | Split it into its own region |

Fix *every* page you plan to train on. This is not tidying. Training examples with chopped-off tops teach the program that Greek has no breathing marks, and it will learn that lesson perfectly. The damage shows up in Week 5 as poor accent accuracy, and nothing in the output will tell you why.

A shortcut that saves hours. Fix one page properly, noting how much room this scribe actually needs above and below the baseline. If Transkribus lets you change the line-finding settings, set them from that measurement and re-run the other pages. Changing one setting beats fixing fifty pages, and it treats the cause rather than the symptoms.

Whichever way you go, check by looking at the cut-out strips themselves. The strip is what the program sees. Looking at it is the only honest test.

**Vocabulary.** *Polygon* — the outline marking which part of the page belongs to one line. *Parameter* — a setting you can adjust before re-running a step.

**Takeaway:** Adjust the layout parameters from a measurement of this hand rather than correcting page by page — and verify by looking at extracted line images.

---

## **07 Content**

**Matching Your Text to the Right Lines**

With the lines correct, you now attach yesterday's typing to them. Each strip of image has to be paired with the words on it.

You have two options.

**By hand**: type or paste your transcription into Transkribus line by line. Slow, and completely reliable. For a single leaf it is often the right choice.

**By import**: upload your transcription and let Transkribus match it up automatically. Fast, and it depends on your line divisions matching the detected lines *exactly*. That is precisely why yesterday's lesson made you count `<lb/>` against `<zone>`.

| Your situation | Use | Risk |
| --- | --- | --- |
| One leaf, about 25 lines | By hand | Typing slips |
| Several leaves, line counts checked | Import | Everything shifts if counts differ |
| Counts do not match | Fix that first | Silent, systematic mismatch |

The third row is the dangerous one. Suppose your transcription has 24 lines and the program found 25, because it split one. Automatic matching will pair every line after the split with the wrong picture. Everything is off by one.

The result is not slightly noisy data. It is systematically wrong, and it teaches the program to match each line's picture to the *next* line's words. That produces output which reads smoothly and is completely wrong, and the cause is very hard to spot afterwards.

So check. Pick three lines at random, look at the picture, read the words paired with it. Do this before every training run.

**Vocabulary.** *Alignment* — pairing each line image with the text belonging to it. *Off-by-one* — an error where everything after a point is shifted by one position.

**Takeaway:** Verify line alignment by spot-checking image against text — an off-by-one misalignment produces a model that has learned the wrong pairing entirely.

---

## **08 Content**

**How the Reading Step Works**

You do not need the mathematics, but knowing roughly how the program works explains the mistakes you will see. Transkribus has long used a system called PyLaia (Puigcerver, 2017).

The strip of image goes through three stages.

First, the program scans across the strip from left to right, describing what the ink looks like at each position. Second, it passes that description through a stage that considers each position together with what comes before and after it — so a shape is interpreted in its neighbourhood rather than alone (AlKendi et al., 2024).

Third comes the clever part. The program does not need to be told which pixels belong to which letter. It considers every possible way of lining up the picture with the letters, and learns from all of them at once (AlKendi et al., 2024).

That is why your work yesterday is directly usable. Training needs only a strip of image and the words on it. Nothing finer. Your line-by-line transcription is exactly that, with no extra labelling required (Puigcerver, 2017).

There is a catch, and it shapes everything in the next section. Because the program works from local ink, it barely models language at all. It is reading the ink, not reading Greek.

**Vocabulary.** *PyLaia* — the recognition system Transkribus has long used. *Neural network* — a program that learns patterns from examples rather than following written rules.

**Takeaway:** CTC training needs only line images paired with line text, which is why your diplomatic transcription is directly usable as training data.

---

## **09 Content**

**What Its Mistakes Look Like**

How the program works decides what *kind* of mistakes it makes, and knowing the kind is what lets you correct efficiently.

Because it reads ink and barely models language, its mistakes stay stuck to the ink. It struggles with heavily shortened words and with letters tangled together, where the shapes overlap. But it rarely invents whole words. Faced with faded ink, it usually produces a string of letters that is not a possible Greek word, rather than guessing a real one (AlKendi et al., 2024).

That behaviour is worth a great deal when you come to correct the output.

| Kind of program | On unclear ink | What that means for you |
| --- | --- | --- |
| PyLaia and similar | Impossible string of letters | You spot it instantly |
| Newer "transformer" models | A real word, wrongly chosen | Easy to miss |
| AI chatbots (Friday) | Smooth, believable text | You may never notice |

A program that outputs `ἐγενθτο` has told on itself. That is not Greek, and you will see it at once. A program that outputs `ἐγένετο` where the page reads `ἐγένοντο` has produced a perfectly good Greek word that simply is not there — and you will only catch it by checking against the picture.

This is the real trade-off when choosing a tool. For steady, formulaic writing, a PyLaia-style model is cheap, effective, and will not invent words. For badly damaged pages, the newer models guess better from context — but you must then watch every line for invented readings (AlKendi et al., 2024).

For a first model on one scribe, the loud failure mode is the right one to want.

**Vocabulary.** *Post-correction* — going through machine output and fixing it. *Ligature* — two or more letters written joined together.

**Takeaway:** A CTC model's errors are conspicuous because it produces impossible sequences rather than plausible wrong words — which makes post-correction far more reliable.

---

## **10 Content**

**The Newer Kind of Model**

There is a second family of programs, and you should know what they are because they may be offered to you as a starting point.

**TrOCR** is the best-known. Rather than scanning strictly left to right, it can look at any part of the picture at any moment, and it keeps track of the words it has already produced (Li et al., 2023).

The upside is that it uses context. It can lean on what it has read so far to make sense of unclear ink, which helps on damaged pages. The downside is the same mechanism: it is pulled toward whatever word would be *likely*, so it hands you believable readings that do not match the ink and read perfectly well (AlKendi et al., 2024).

| | PyLaia | TrOCR |
| --- | --- | --- |
| Uses context | Barely | Heavily |
| Computing cost | Low | High |
| On damaged pages | Fair | Better |
| Risk of invented words | Low | Real |
| Are mistakes obvious? | Yes | No |
| Best for | Steady hands; a first model | Damaged pages; variable hands |

One refinement worth knowing: smaller add-on pieces can be slotted into TrOCR — one for old languages, one for handwriting style — which cuts error rates sharply without retraining the whole thing (AlKendi et al., 2024). That makes these models practical when training examples are scarce, which is the normal situation in manuscript work.

If your scribe writes consistently, start with PyLaia. If the page is a mess, consider the other — but plan to check its output far more carefully.

**Vocabulary.** *Transformer* — a newer design that can attend to any part of its input at once. *Context* — surrounding text used to help interpret an unclear bit.

**Takeaway:** Transformers read context as well as ink, which helps on degraded text and produces plausible wrong words that are hard to catch.

---

## **11 Content**

**Never Start From Nothing**

This is the biggest decision you make today, and it has a clear answer.

Teaching a program to read from a completely blank start takes enormous amounts of example material. Starting from a program that already reads *something* takes far less, because it already knows about letters, ink, parchment, and lines. Your examples only have to teach it your particular scribe.

The advice is blunt: never start from nothing if any existing model is available. Starting from a solid one and adding 50 to 100 pages of your own can bring the error rate down to something usable, in a fraction of the time (Geelhaar, 2022; AlKendi et al., 2024).

The size of the effect is worth seeing. Perdiki and Konstantinidou (2023) trained Byzantine Greek models on manuscripts from different libraries:

| How they trained | Source | Started from an existing model? | Error rate |
| --- | --- | --- | --- |
| Single manuscript | Athos, Vatopedi 328 | No | 10.03% |
| Single manuscript | Munich, Gr. 353 | No | 8.12% |
| Several manuscripts mixed | Multiple | No | 17.18% |
| Several manuscripts mixed | Multiple | Yes | 3.90% |

Read the last two rows together. Identical training material. Starting from nothing: 17.18% wrong. Starting from an existing model: 3.90%. Four times better, from one decision.

They also found that mixing several manuscripts cut the hand-typing needed per manuscript by up to 80% with no loss of accuracy (Perdiki & Konstantinidou, 2023). Variety substitutes for volume.

**Vocabulary.** *Transfer learning* — starting from a model trained on something else and adjusting it. *Fine-tuning* — the adjusting step, using your own examples.

**Takeaway:** Transfer learning turned 17.18% CER into 3.90% on identical data — always fine-tune from a base model rather than training from scratch.

---

## **12 Content**

**Picking What to Start From**

Choose on purpose. A badly matched starting point wastes the typing you did yesterday.

| What to match | Aim for |
| --- | --- |
| Script | The same script — Greek for Greek |
| Date | As close to your manuscript as possible |
| Language | The same, or a close relative |
| Amount of training | More, all else being equal |
| Published results | A stated error rate on similar material |
| Availability | Something you can actually use |

Script matters most. A model trained on Latin handwriting has learned Latin letters. It will not help with Greek, however good it is. Date and language come next, because they decide the vocabulary and which short forms appear.

Here is how stark the effect is. On a medieval Latin test set, a small model tuned for medieval Latin got 14.6% of characters wrong. Two large general-purpose commercial systems, on the very same pages, got 63.0% and 84.7% wrong (Mattingly et al., 2024). The small specialist has a tiny fraction of the size and wins because it has actually seen scribal handwriting, odd joined letters, and unusual page layouts.

Bigger is not better. *Matched* is better. This is the most counter-intuitive fact in the whole topic, and Friday will show it to you in a far more dramatic form.

Write down which model you started from and why. That is a real methodological decision, and your Week 5 report has to state it.

**Vocabulary.** *Base model* — the existing model you start from. *Specialization gap* — the tendency of a small matched model to beat a huge general one on unusual material.

**Takeaway:** A matched small model beats a large general one — script match matters more than parameter count.

---

## **13 Content**

**Training the Model**

With your text attached to the right lines and a starting model chosen, train.

| Setting | What it is | Where to start |
| --- | --- | --- |
| Base model | What you start from | Matched for script and date |
| Training set | The lines it learns from | Your corrected leaves |
| Validation set | Lines held back to test it | 10–20% of your lines |
| Epochs | How many times it reviews the examples | The default; watch the graph |
| Learning rate | How big each adjustment is | The default |

The **validation set** is the one to understand rather than just accept. These are lines you keep back so the program never trains on them. They are how you find out whether it learned your scribe's handwriting or merely memorized your specific lines. A program that memorized will look perfect on its own examples and fall apart on anything else.

Make the held-back lines *representative*. Holding back the last three lines of one leaf tests it on material nearly identical to what it studied. Holding back lines from across all your leaves, including the ugly ones, gives a number that means something.

Training usually takes tens of minutes, not hours. Watch the error on the held-back lines as it goes: it should fall and then level off. If it falls and then starts *rising*, the program has begun memorizing, and you should stop at the lowest point.

Training spends credits from a shared class allowance. Plan your runs.

**Vocabulary.** *Validation set* — lines held back to test the model honestly. *Overfitting* — memorizing the examples instead of learning the pattern.

**Takeaway:** Hold out a representative validation set and stop when validation error stops falling — a rising validation curve means the model is memorizing your lines.

---

## **14 Content**

**Reading the Score**

Training gives you a model and a number. Read both carefully.

The number is the **character error rate**, or CER — the percentage of characters the model got wrong on the held-back lines. It tells you how the model does on *more of this manuscript, in this hand*. It says nothing about a different scribe, a different book, or a very different page layout.

What the number means (AlKendi et al., 2024):

| CER | Verdict | What it is good for |
| --- | --- | --- |
| Under 5% | Excellent | Light correction; usable after proofreading |
| 5–10% | Good | Scattered slips on short forms and punctuation; fine for bulk work |
| 10–15% | Borderline | Heavy correction needed |
| Over 15% | Poor | Correcting costs more than typing it yourself |

That last row is the one to remember as a rule. Past roughly 15%, fixing the output takes longer than typing the page from scratch (AlKendi et al., 2024). A model in that range is not merely slow. It is a net loss, and the right response is to improve it or abandon it — not to grind through its output.

If your first model lands above 15%, work through the likely causes in this order: bad line-finding producing bad strips, text attached to the wrong lines, too few examples, a badly matched starting model.

**Vocabulary.** *Character error rate (CER)* — the percentage of characters wrong. *Word error rate (WER)* — the same idea counted in whole words.

**Takeaway:** Above 15% CER, correcting the output costs more than transcribing from scratch — the model is a net loss, not a slow tool.

---

## **15 Content**

**The Score Does Not Tell You Everything**

A warning to carry into today's judging, which Week 5 will develop.

CER counts the smallest number of single-character fixes needed to turn the machine's output into yours, as a percentage (AlKendi et al., 2024). It is one number that treats every difference as equal.

That equal treatment is the problem. Losing an accent and swapping a letter count exactly the same, though what they cost a scholar is wildly different. A model that drops every breathing mark because the strips were cut too tight might post a respectable CER while being useless for your edition.

So look at the *kinds* of mistake as well as the number.

| Kind of mistake | Effect on the score | How bad it really is |
| --- | --- | --- |
| Accents dropped | Moderate | Severe for Greek; ruins fidelity |
| Similar letters confused | Moderate | Moderate; proofreading catches it |
| Short forms spelled out | Small | Severe; silently modernizes |
| Impossible letter strings | Moderate | Mild; obvious and easy to fix |
| Believable wrong words | Small | Severe; nearly invisible |
| Margin notes skipped | Varies | Severe; whole content lost |

The third row keeps coming back. A model that quietly spells out short forms gives you clean readable text with a good score, having destroyed exactly what a diplomatic transcription exists to protect. A model at 8% that keeps every joined letter may serve a scholar far better than one at 4% that modernizes (Levchenko, 2024).

Look at the mistakes, not just the number.

**Vocabulary.** *Edit distance* — the count of single-character changes between two texts. *Fidelity* — how faithfully the output matches what is on the page.

**Takeaway:** CER weights every difference equally, so a model that silently drops diacritics or expands abbreviations can score well while being useless for a diplomatic edition.

---

## **16 Content**

**Running the Model and Looking at What Comes Back**

Turn your trained model loose on leaves you have not typed, and study the result.

Work through it properly rather than skimming:

- Read the output against the picture, line by line, zoomed in.
- Sort each mistake into a category instead of just fixing it.
- Notice whether mistakes bunch together — in one area, on one letter, on one feature.
- Check specifically whether the accents are there and right.
- Check whether short forms were kept or spelled out.
- Note any line that comes out as gibberish, and look at that line's strip.

That last point goes back to section 02. A gibberish line usually has a line-finding fault behind it — two lines glued, a chopped strip, a wandering baseline. Look at the strip before deciding the model cannot read.

Keep your sorted list of mistakes in the repository. It is a required part of the Week 5 report, and writing it now while you are staring at the output is much easier than reconstructing it in a fortnight.

Expect certain patterns in Greek. Short forms and tangled letters are hardest, because the shapes overlap (AlKendi et al., 2024). Accents will be imperfect even with good strips. And if your manuscript runs words together, expect word boundaries to be wrong in ways that make the word score meaningless — the letters are right, then glued into one long string (Perdiki & Konstantinidou, 2023).

**Vocabulary.** *Error category* — a group of mistakes sharing a cause. *Gibberish* — output that is not a possible word, usually signalling a layout fault.

**Takeaway:** Categorize errors rather than just correcting them, and inspect the line image whenever output is nonsense — it is usually a layout fault.

---

## **17 Content**

**Going Round Again**

This work is a loop, not a one-off. Your first model is a starting point.

The cycle: run the model on new pages, correct what it produces, add those corrected pages to the training pile, train again, run the better model on more pages. Each time round, getting new material costs less — because you are correcting rather than typing — and each time round the model improves.

| Round | Where the text comes from | Effort per page | Expected score |
| --- | --- | --- | --- |
| 1 | You typed it | Highest | Baseline |
| 2 | Model output, corrected | Lower | Better |
| 3 | Model output, corrected | Lower still | Better again |
| Later | Diminishing returns | Low | Levels off |

That falling cost is what makes the whole method worth doing, and it is why yesterday's typing is an investment rather than a chore.

Two warnings. Correcting output has the anchoring problem from Lesson 4.1 — you are judging whether something looks right rather than reading it fresh. Correct zoomed in, against the picture, and be most suspicious of output that looks fine.

And beware of a loop that feeds on itself. Correct carelessly, retrain, and the model learns your careless corrections. Its next output carries the same mistakes, which now look familiar, so you correct even less carefully. The loop can settle on a model that is confidently wrong. The fix: every so often, type a page from scratch without looking at the model's version, and compare. That breaks the circle.

**Vocabulary.** *Iteration* — one pass round the correct-and-retrain loop. *Feedback loop* — a cycle where output feeds back in as input and errors compound.

**Takeaway:** Each iteration makes ground truth cheaper, but correcting model output risks a feedback loop — periodically transcribe a page blind to break it.

---

## **18 Content**

**Models Are Fragile About Layout**

Something to understand before you trust your model, because it catches people out.

A model that does well on ordinary pages can collapse on pages laid out differently — even when the scribe and the language are identical.

Geelhaar's (2022) model, trained on ninth- to eleventh-century Latin, got 5.1% of characters wrong on ordinary pages. On pages with small notes in the margins, the very same model got 13.6% wrong. Excellent to borderline, because the vocabulary changed, there were more short forms, and the smaller writing gave it less to work with.

| What changed | Usual effect | Why |
| --- | --- | --- |
| Notes in the margin | Big drop | Smaller writing; different words |
| Words added between lines | Lines glued together | Line-finding cannot separate them |
| Two columns instead of one | Jumbled order | Region detection |
| Damaged patches | Local failure | Strips drawn around the damage |
| A different scribe | Drop | Outside what it was trained on |

So read any score as being *about a layout*. A model reporting 4% reports 4% on pages like the ones it was tested on. On a page laid out differently, its performance is simply unknown until you measure it.

For your own edition, check whether your pages are alike. If some carry margin notes, or a second scribe takes over, expect different behaviour there — and test on those pages specifically instead of assuming the headline number covers them.

**Vocabulary.** *Brittle* — working well in familiar conditions and failing sharply outside them. *Marginal gloss* — a note written in the margin, usually smaller.

**Takeaway:** A model's CER holds only for layouts like those it was validated on — glossed or irregular pages need their own measurement.

---

## **19 Content**

**Transkribus and eScriptorium**

Two platforms do this work and it is worth knowing how they differ.

**Transkribus** is a commercial product with a polished interface, a big library of ready-made models, and charges credits for training. **eScriptorium** is free and open source, and you can run it on your own computer if you want to (eScriptorium/Kraken, 2024).

| | Transkribus | eScriptorium |
| --- | --- | --- |
| Cost | Commercial; credits | Free, open source |
| Interface | Polished | Web-based, plainer |
| Ready-made models | Large library | Smaller |
| Where it runs | Their computers | Theirs or yours |
| Can others check your work? | Limited; models are secret | Yes; models and code are open |

The ease-of-use point is not trivial. Perdiki's work found that command-line tools were simply out of reach for many humanities scholars, while Transkribus's interface let them train and fix layouts quickly (Perdiki & Konstantinidou, 2023). How usable a tool is decides whether the method gets used at all.

Against that, openness matters for an edition anyone can check. A model you can inspect and re-run is one a later scholar can verify. A secret model might not exist in ten years — and any claim resting on it becomes impossible to check.

This course uses Transkribus, for the interface and the model library. If you carry on past this term, eScriptorium is worth learning.

**Vocabulary.** *Open source* — software whose code anyone may inspect and run. *Reproducibility* — whether someone else can repeat your work and get your result.

**Takeaway:** Transkribus is more accessible; eScriptorium is reproducible — and a proprietary model makes any claim resting on it unverifiable later.

---

## **20 Content**

**Getting the Text Back Out**

Exporting is where today's work rejoins your edition.

Both platforms export formats called **ALTO** and **PAGE**. Both describe a page as regions, lines, and words, each with its position on the image and the text found there. They map onto TEI closely, and — this is the valuable part — they keep the coordinates worked out during line-finding (eScriptorium/Kraken, 2024).

| ALTO element | Holds | TEI equivalent |
| --- | --- | --- |
| `<Page>` | One page | `<surface>` |
| `<TextBlock>` | A block of writing | `<zone type="block">` |
| `<TextLine>` | One line | `<zone type="line">` |
| `<String>` | One word, with its position | `<w>` with `@facs` |

Those kept coordinates are the payoff. In Lesson 3.3 you measured three line boxes by hand. Now you can convert ALTO's coordinates into TEI zones for *every* line automatically.

One trap. ALTO's numbers are in image pixels. If the viewer's canvas size differs from the image size — the ratio you noted in Lesson 3.3 — every number needs scaling before it becomes a TEI zone.

This is exactly what your hand-measured boxes are for. Convert the ALTO numbers, compare against the three lines you measured yourself, and if they agree your conversion is right. If they are out by a consistent factor, you have found the scaling error — and you found it because you had something to check against.

Export today, commit the raw export next to your converted TEI, and record the scale factor you used.

**Vocabulary.** *ALTO / PAGE* — XML formats for page layout plus recognized text. *Control* — a known-good measurement used to check an automated one.

**Takeaway:** ALTO preserves line coordinates in image pixels — transform them into TEI zones and check the result against your hand-measured control lines.

---

## **21 Content**

**Saving Machine Output to Git**

The labelling habit from Week 1 does real work today for the first time.

Commit the machine's output **separately from your corrections**. This is not neatness. It is what makes Week 5's measurement possible at all. The raw output is the thing being scored. Commit it already corrected and there is nothing left to score.

```text
feat(transcription): HTR output for ff. 43r-44v, uncorrected

Applied model rels398-hand1-v2, built from Transkribus Titan plus 24
lines of my own transcription from f. 42r. Score on held-back lines:
6.2% of characters wrong.

Raw output, nothing corrected. Corrections follow in a separate commit
so the raw score can be measured against this state in Week 5.

AI-Generated: true
Model: Transkribus / PyLaia, rels398-hand1-v2
Base-Model: Transkribus Titan I
Human-Verified: false
Ground-Truth-Commit: a3f9c21
Validation-CER: 6.2
```

Then correct, and commit that separately:

```text
fix(transcription): correct HTR output for ff. 43r-44v

Fixed 31 errors against the photograph at full zoom. Sorted in
logs/htr-errors-w4.md: 14 dropped accents, 9 short-form errors,
5 joined-letter misreadings, 3 chopped line ends.

Human-Verified: true
```

The `Human-Verified: false` on the first commit is your to-do list working as designed. Between those two commits your repository holds unchecked machine text, and the label says so out loud.

**Vocabulary.** *Trailer* — a labelled line at the end of a commit message. *Raw output* — machine text before any human correction.

**Takeaway:** Commit raw model output and your corrections separately, or Week 5 cannot compute an error rate at all.

---

## **22 Content**

**Setting Friday Up**

On Friday you run the same passage through a general AI model, and the comparison is the week's real lesson. Today's results are what it gets compared against.

Record all of this so that comparison is possible:

| What to record | Where |
| --- | --- |
| Which model you started from | Repository note and commit trailer |
| How much training material | Lines and leaves used |
| Score on held-back lines | Commit trailer and note |
| Sorted list of mistakes | `logs/htr-errors-w4.md` |
| How much line-fixing it took | A note |
| Raw uncorrected output | Its own commit, tagged |
| Time spent | A note: setup, fixing, training |

That last row matters more than students expect. Friday's tool needs no training, no line-fixing, and no typed examples. You hand it a picture and get text back. Comparing the *quality* of Wednesday's and Friday's output without comparing the *cost* misses half the question.

Tag today's raw output so Week 5 can retrieve exactly what was measured:

```bash
git tag -a htr-w4-raw -m "Raw HTR output, model rels398-hand1-v2, before correction"
```

Expect Friday's output to be worse on this material, possibly much worse. That is the finding, not a failed exercise — and it counts for more having been measured than asserted.

**Vocabulary.** *Baseline result* — the result everything else gets compared against. *Cost* — the time, effort, and money a method actually takes.

**Takeaway:** Record cost as well as quality — Friday's tool needs no training or ground truth, and the comparison is meaningless without that.

---

## **23 Content**

**Why the Small Specialist Usually Wins**

Worth understanding before Friday, because the result goes against instinct.

The general AI models are enormous, trained on staggering amounts of material. Your model is tiny and learned from a few dozen lines of one scribe. Instinct says the big one should win.

On historical manuscripts it usually does not, and the gap is huge. On a medieval Latin test set, a model tuned for medieval Latin got 14.6% of characters wrong, while two large commercial systems scored 63.0% and 84.7% on identical pages (Mattingly et al., 2024). On historical English, GPT-4o got 52.23% wrong; on historical German, 77.42% (AlKendi et al., 2024).

The same models are superb on *modern* handwriting. GPT-4o gets 1.39% wrong on a modern English test set — as good as purpose-built tools (AlKendi et al., 2024).

| Material | Model | Wrong |
| --- | --- | --- |
| Modern English | GPT-4o | 1.39% |
| Historical English | GPT-4o | 52.23% |
| Historical German | GPT-4o | 77.42% |
| Medieval Latin | Tuned specialist | 14.6% |
| Medieval Latin | Large general model | 84.7% |

This is the **specialization gap**. The specialists are far smaller and win because they have actually been shown scribal handwriting, odd short forms, joined letters, and irregular layouts (Mattingly et al., 2024). The general models have seen the internet, and the internet contains very little Byzantine Greek minuscule.

Size does not substitute for having seen the material. Friday you check this on your own manuscript.

**Vocabulary.** *Benchmark* — a standard test set used to compare tools fairly. *General-purpose model* — one trained on everything rather than for one job.

**Takeaway:** General models are excellent on modern handwriting and catastrophic on historical scripts — scale does not substitute for exposure to the material.

---

## **24 Content**

**More Steps Can Make It Worse**

A related finding, worth knowing before Friday because it will shape what you try.

The instinct when assembling a workflow is that more helpers must help: a reading program, then an AI to tidy its mistakes, maybe a lookup step to supply background knowledge. Each addition fixes something real.

In practice it backfires. A plain workflow — one specialist reading program feeding one translator — beats versions with extra AI steps bolted on. The extra generative steps introduce their own errors, and those errors then travel downstream unchecked (Mattingly et al., 2024).

| Workflow | Extra pieces | Result |
| --- | --- | --- |
| Plain | None | Best |
| Plus background lookup | One | Worse |
| Plus AI tidying of the reading | One | Worse |
| Both | Two | Worst |

The mechanism is simple. Every generative step can break things as well as fix them, and something broken late in the chain has nothing after it to catch the problem. An AI tidying up reading output cannot see the picture. It corrects toward whatever sounds most likely — which means it will "fix" a correct but unusual reading into a wrong but ordinary one. In manuscripts, the unusual readings are frequently the interesting ones.

So, for Friday: do not try to improve today's output by passing it through an AI to clean up. That is exactly the setup the evidence says makes things worse, and you would be degrading your text while feeling you had improved it.

**Vocabulary.** *Pipeline* — a chain of processing steps, each feeding the next. *Error propagation* — a mistake made early travelling onward unnoticed.

**Takeaway:** Adding LLM post-correction to OCR degrades quality — it corrects toward plausibility, and unusual readings are the interesting ones.

---

## **25 Content**

**Checklist Before You Leave**

Check each one.

- Manuscript imported into Transkribus by web address.
- Line-finding run on every leaf you are using.
- Every line found; no merges or splits left.
- Strips checked to include the high accents.
- Your transcription attached to the right lines, spot-checked.
- Starting model chosen, with the reason written down.
- Model trained, with a representative set of lines held back.
- Score recorded.
- Model run on at least one untyped leaf.
- Output read line by line, zoomed in.
- Mistakes sorted in `logs/htr-errors-w4.md`.
- Raw output committed on its own, with the labels.
- Raw output tagged.
- ALTO or PAGE export committed.
- Coordinates checked against your Lesson 3.3 measured lines.
- Time spent recorded.

If your score is worse than 15%, do not start correcting. The output is not worth the effort. Diagnose instead, in the order from section 14: line-finding, then alignment, then how much training material, then the starting model.

**Vocabulary.** *Spot-check* — verifying a few samples rather than everything. *Diagnose* — work out the cause before attempting a fix.

**Takeaway:** If validation CER exceeds 15%, diagnose rather than correct — check layout, then alignment, then data volume, then base model.

---

## **26 Content**

**Things That Go Wrong Today**

The failures that keep happening, and what they mean.

| Symptom | Likely cause | What to check |
| --- | --- | --- |
| Import fails | Address not reachable publicly | `curl` from outside your network |
| Some lines not found | Faint ink; settings | Look, then fix by hand |
| No accents at all in the output | Strips cutting them off | Look at the extracted strips |
| Fluent nonsense | Text attached one line out | Spot-check picture against words |
| Score far worse than expected | Starting model wrong for the script | Confirm script and date |
| Good on one leaf, bad on another | Different layouts | Test each layout separately |
| Training improves, held-back lines worsen | Memorizing | Stop at the low point |
| Words glued together | Words run together on the page | Expected; note it for Week 5 |
| Short forms spelled out | Starting model learned tidy text | Pick a diplomatic starting model |

Rows three and four are today's signature failures, and both are invisible in the output itself. Missing accents look like the program being weak at Greek rather than a strip problem. Text attached one line out reads perfectly and simply belongs somewhere else.

The remedy for both is the same, and it is worth keeping as a general rule: when output is wrong in a way you cannot explain, go and look at what the program actually saw. The extracted strip is the truth about the input, and nearly every baffling failure is visible there.

**Vocabulary.** *Symptom* — what you observe going wrong. *Cause* — the underlying fault, often several steps earlier.

**Takeaway:** When output is inexplicably wrong, look at the extracted line image — that is what the model actually saw.

---

## **27 Content**

**Writing Down What You Did**

Your Week 5 report needs an account of today's work. Writing it now is far easier than reconstructing it later.

Record in `logs/htr-method-w4.md`:

- Which platform, and which version.
- Which model you started from, what it was trained on, how it performs.
- Your own material: which leaves, how many lines, how produced.
- What line-fixing was needed, and of what kind.
- Whether you changed the line-finding settings, and to what.
- How you trained: how many lines held back, how many passes, when you stopped.
- The score, and what it was measured on.
- Which leaves you then ran the model over.
- The kinds of mistake you saw, with counts.
- Time spent at each stage.

This is a methods section. Its job is to let a reader — or you in December — see what was done and judge whether the results mean what they seem to. A score of 6.2% means nothing without knowing the starting model, how much material, and what was in the held-back set.

It also protects you. If your Week 5 results are surprising, this record is what lets you work out why. Without it, a strange number is simply strange, and your only option is doing the work again.

Commit it with a `docs:` prefix.

**Vocabulary.** *Methods section* — the part of a report saying exactly what was done. *Provenance* — the documented history of how something was made.

**Takeaway:** A CER figure is uninterpretable without its base model, training volume, and validation set — record the methodology today.

---

## **28 Content**

**Preparing for Friday**

Friday is remote, and it puts the same passage through a general AI model.

Have all of this available from wherever you will be:

- Your repository, pushed.
- Yesterday's transcription, tagged.
- Today's raw output, tagged.
- Today's sorted mistakes and methods notes.
- Your images, reachable from outside your network.
- A working Greek keyboard on the machine you will use.
- Access to an AI model that accepts pictures.

Friday's comparison is three-way: your typing, today's specialist model, and Friday's general model, all on the same lines. Having all three saved under tags is what makes that comparison exact rather than roughly right.

Set your expectation now, so the result is a measurement rather than a shock. Going by the published figures in section 23, Friday's output will probably be much worse than today's on historical Greek. It will also arrive in minutes instead of a whole session. Week 5 needs you to hold both of those facts at once.

Check your setup today, following Lesson 4.1 section 23. Every item takes two minutes now and none of them takes two minutes on Friday morning.

**Vocabulary.** *Three-way comparison* — measuring three versions of the same passage against each other. *Tag* — a permanent name on one saved version.

**Takeaway:** Tag all three states so Friday's three-way comparison is exact, and expect the general model to be much worse and much faster.

---

## **29 Content**

**What Good Work Looks Like Here**

"Trained a model" and "trained a model well" are different achievements.

An acceptable result is a trained model with a recorded score and output you have looked at.

Good work also:

- Fixes the line-finding thoroughly, including the strips around accents.
- Checks that text is attached to the right lines instead of assuming it.
- Chooses a starting model deliberately and says why.
- Holds back a representative set of lines, not a convenient one.
- Sorts mistakes into kinds rather than just counting them.
- Tells line-finding failures apart from reading failures.
- Records cost — time and effort — alongside quality.
- Commits raw output separately from corrections, fully labelled.
- Says what the model does badly, and offers a reason.

That last one is what makes this scholarship rather than button-pushing. "6% wrong, and it drops breathings on one particular letter, fails on this scribe's short form for *kai*, and falls apart on the glossed leaf" is far more useful than "6% wrong" — because it tells you what to fix, what to check by hand, and what to say about whether this method suits this manuscript.

**Vocabulary.** *Qualitative* — concerning the kind of thing, not the amount. *Hypothesis* — a proposed explanation you can go on to test.

**Takeaway:** Reporting *what* the model gets wrong and why is the scholarly contribution; the CER number alone is tool operation.

---

## **30 Content**

**Synthesis: An Instrument with Edges**

What today established about the machine step.

A specialized reading model is an instrument with **edges**. It reads ink and produces letters, and it is competent exactly as far as its examples went. Inside that boundary, on handwriting it has seen, it is fast, cheap, consistent, and — because it barely models language — inclined to fail loudly rather than to invent (Puigcerver, 2017; AlKendi et al., 2024).

How well it works depends on things you control. The line-finding has to be fixed, because the reading step only ever sees what line-finding produced, and chopped strips delete Greek accents before the model lays eyes on them (Perdiki & Konstantinidou, 2023). Your text must be attached to the right lines. The starting model must match the script. And you must start from an existing model, because that alone was the difference between 17% and 4% on identical material (Perdiki & Konstantinidou, 2023).

Judging it takes more than a number. A score holds only for pages laid out like the ones it was tested on, treats every difference as equal, and can look excellent while the model quietly modernizes away the very fidelity your edition exists to preserve (Levchenko, 2024).

Friday tests the opposite kind of instrument: no edges, trained on everything, able to draw on what language usually does — and therefore able to produce fluent text that is not on the page. Comparing the two is the point of the week.

**For Friday.** Remote. Bring the seven items in section 28, with all three versions tagged.

**Vocabulary.** *Bounded* — limited to a defined range of material. *Fluent* — reading smoothly, which is not the same as being correct.

**Takeaway:** An HTR model reads ink within the bounds of its training and fails conspicuously; Friday's instrument reads expectation too, and fails fluently.

---

## References

AlKendi, W., Gechter, F., Heyberger, L., & Guyeux, C. (2024). Advancements and
challenges in handwritten text recognition: A comprehensive survey. *Journal of
Imaging*.

eScriptorium/Kraken. (2024). *eScriptorium platform documentation*.
https://escriptorium.eu/about

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
