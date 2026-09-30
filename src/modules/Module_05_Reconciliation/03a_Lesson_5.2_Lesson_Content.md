# Lesson 5.2 — Diffing and Reconciling Transcriptions in VS Code

*RELS 398 / ENGL 398 · Topic 5: Reconciliation · Meeting #13 (Fri Oct 2)*

***Step 2 of a two-step week.** Today you open your manual transcription (`witness.xml`) and your Gemini AI transcription (`transcription_ai.xml`) in VS Code's side-by-side diff viewer. You will evaluate every discrepancy against your primary manuscript image using our four-part error taxonomy, synthesize the authoritative reconciled consensus text into `transcription_reconciled.xml`, and compose your reflection report in `RECONCILIATION.md`. **The Transcription Assignment is due tonight by 11:00 PM.***

---

## **01 Content**

**The Reconciliation Objective: Synthesis Over Surrender**

Welcome to Meeting #13. Today you reach the culmination of Week 5: textual reconciliation. 

Over the past week, you generated two independent diplomatic transcriptions of your manuscript page. In Week 4, you keyed Pass 1 entirely by hand into `witness.xml`. On Tuesday (Meeting #12), you used Gemini in VS Code Antigravity to produce Pass 2 in `transcription_ai.xml`. 

Now, you sit with two completed drafts that disagree with each other. A novice might be tempted to simply pick one file and discard the other, or blindly trust the artificial intelligence model because its output looks clean and polished. In scholarly editing, this surrender is unacceptable.

Reconciliation is not about picking a winner. It is about **synthesis**. You are the senior editor of your digital edition. Your task today is to open both drafts side by side, inspect every line where they diverge, interrogate the physical evidence on your digital image, and synthesize the best readings into a third, authoritative file: `transcription_reconciled.xml`. Where Gemini caught a slip you made due to tired eyes, you accept its reading. Where Gemini hallucinated or smoothed historical spelling, you defend the physical ink. You are the ultimate judge.

**Vocabulary.** *Synthesis* — The intellectual act of evaluating multiple drafts to create a single superior, verified text.

**Takeaway:** Textual reconciliation is an active act of scholarly adjudication, not a passive acceptance of machine output.

---

## **02 Content**

**The Three-Pass Textual Architecture**

To understand your workflow today, you must keep the three-pass textual architecture clear in your mind:

- **Pass 1 (`witness.xml`):** The human manual diplomatic baseline. Authored in Week 4, this draft reflects your careful reading of handwriting, physical layout, and codicological features. It carries human perceptual fatigue and cognitive auto-correction, but also human common sense and historical context.
- **Pass 2 (`transcription_ai.xml`):** The machine diplomatic baseline. Generated on Tuesday via Gemini in VS Code Antigravity, this draft was produced under strict negative constraints. It never tires and reads microscopic letter strokes consistently, but it is prone to hallucination and silent modernization.
- **Pass 3 (`transcription_reconciled.xml`):** The reconciled consensus baseline. Synthesized today, this file represents your adjudicated ground truth. It adopts the strengths of both passes while eliminating the distinct flaws of each.

All three files use the exact same diplomatic XML vocabulary taught in Week 4: `<text>`, `<body>`, `<div>`, `<p>`, `<pb/>`, `<lb/>`, `<unclear>`, and `<gap/>` (plus `<lg>` and `<l>` for poetry). Furthermore, all three files must remain permanently in your repository. Preserving this three-pass lineage provides complete scholarly transparency: anyone inspecting your digital edition can trace exactly how your text evolved from raw image to finished consensus.

**Vocabulary.** *Textual architecture* — The systematic multi-stage progression of draft versions from raw witness to reconciled consensus.

**Takeaway:** Your repository preserves three distinct stages: Pass 1 (manual), Pass 2 (AI), and Pass 3 (reconciled consensus).

---

## **03 Content**

**Understanding the VS Code Diff Engine**

How do you compare two long XML files without reading them word-by-word with a magnifying glass? The answer is a computational tool called a **diff engine**.

The concept of a diff dates back to early Unix computing (specifically Douglas McIlroy's 1974 algorithm). A diff engine takes two text streams—a source and a target—and calculates the shortest sequence of edits (insertions, deletions, and replacements) necessary to transform the first into the second.

In modern code editors like Visual Studio Code, the diff engine is integrated into an interactive graphical interface. Rather than dumping cryptic terminal markers like `---` and `+++`, VS Code displays both files side-by-side in synchronized split panes:

- Red or light coral shading marks text present in the left file but absent in the right (deletions).
- Green or light mint shading marks text present in the right file but absent in the left (insertions).
- Synchronized scrolling ensures that as you move down the document, matching lines remain horizontally aligned.

By using the diff engine, you let the computer do what computers do best: pinpointing exact coordinate differences. This frees your human intellect to do what humans do best: evaluating the historical meaning of those differences against the manuscript.

**Vocabulary.** *Diff engine* — An algorithmic tool that computes and visually highlights character and line discrepancies between two files.

**Takeaway:** VS Code's diff engine compares two files line-by-line, highlighting deletions, insertions, and intra-line edits.

---

## **04 Content**

**Launching Side-by-Side Comparison in VS Code**

Opening two files for comparison in VS Code is straightforward and can be accomplished in two different ways:

**Method 1: Using the File Explorer (Graphical)**

1. Open the File Explorer sidebar in VS Code (`Ctrl+Shift+E` or `Cmd+Shift+E` on macOS).
2. Right-click on your manual transcription file (`witness.xml`) and select **Select for Compare**.
3. Right-click on your AI transcription file (`transcription_ai.xml`) and select **Compare with Selected**.
4. VS Code immediately opens a new tab titled `witness.xml ↔ transcription_ai.xml` showing both files side-by-side.

**Method 2: Using the Integrated Terminal (Command Line)**
You can also launch the diff view directly from the terminal prompt:
```bash
code --diff witness.xml transcription_ai.xml
```

Once the diff tab opens, configure your workspace for optimal adjudication. Split your physical monitor or position your windows so that your high-resolution manuscript image is visible alongside VS Code. You cannot reconcile text in a vacuum: your digital image is your primary source of truth, and you must consult it for every single highlighted diff chunk.

**Vocabulary.** *Split diff viewer* — A side-by-side editing interface that displays the original and modified files simultaneously.

**Takeaway:** Use the File Explorer or terminal to compare witness.xml and transcription_ai.xml in VS Code's split diff view.

---

## **05 Content**

**Navigating Diff Chunks: Insertions, Deletions, and Modifications**

When you open a diff, the editor groups contiguous differences into distinct units called **diff chunks**. A diff chunk can be as small as a single punctuation mark or as large as an entire paragraph where lineation diverged.

To navigate diff chunks efficiently without missing subtle one-character discrepancies:

1. **The Navigation Toolbar:** In the top right corner of the diff editor tab, look for the navigation arrows: **Go to Next Change** (down arrow) and **Go to Previous Change** (up arrow).
2. **Keyboard Shortcuts:** You can jump between differences instantly:
   - macOS: `Option+F5` (Next Change), `Shift+Option+F5` (Previous Change)
   - Windows/Linux: `Alt+F5` (Next Change), `Shift+Alt+F5` (Previous Change)
3. **The Overview Ruler (Minimap):** On the far right edge of the editor window, the vertical scrollbar displays colored tick marks showing the distribution of differences throughout the file. Blue or green tick marks represent additions; red marks indicate deletions.

Working through your file chunk-by-chunk using keyboard shortcuts ensures disciplined, comprehensive review. Never skim or scroll rapidly: an unexamined diff chunk might contain a critical scribal abbreviation or an AI hallucination.

**Vocabulary.** *Diff chunk* — A contiguous block of text containing one or more lines where two files differ.

**Takeaway:** Navigate methodically through diff chunks using keyboard shortcuts or the diff minimap rather than scrolling aimlessly.

---

## **06 Content**

**Reading Diff Highlighting: Block vs. Character-Level Changes**

VS Code uses a two-tier visual highlighting system to communicate exactly what kind of divergence has occurred:

1. **Line-Level Background Tinting:** When a line contains any difference, the entire line receives a pale, semi-transparent background color (light red/coral on the left, light green/mint on the right). This signals that the line as a whole does not match.
2. **Intra-Line Character Highlighting:** Within that tinted line, VS Code applies a darker, more saturated background color directly behind the specific characters that differ. 

For example, consider an 18th-century line where the manual pass keyed `the publick peace` and Gemini produced `the public peace`:

- The entire line is lightly shaded in both panes.
- In the left pane (`witness.xml`), the letter `k` in `publick` is highlighted with a rich, darker tint.
- In the right pane (`transcription_ai.xml`), the space following `public` is highlighted, indicating that the `k` is missing.

Learning to read this two-tier shading allows you to diagnose discrepancies in seconds. You don't have to re-read the entire sentence; your eye focuses immediately on the darker character-level highlights. That darker highlight tells you exactly what historical feature is under dispute.

**Vocabulary.** *Intra-line highlighting* — The darker shading within a diff line that pinpoints the exact character coordinates of a discrepancy.

**Takeaway:** Diff lines use pale background tinting for the changed line and darker highlighting for exact character differences.

---

## **07 Content**

**The Danger of Automated Merge: Why Manual Adjudication is Mandatory**

In software engineering, developers frequently use automated merge tools (`git merge`) to combine code branches. If Developer A changed line 10 and Developer B changed line 50, the git merge engine automatically merges both changes without asking questions.

In historical textual scholarship, **automated merging is strictly forbidden**.

Why? Because git merge algorithms possess zero historical consciousness. A merge algorithm cannot look at an 18th-century manuscript image. It does not know that an author used a quill pen, that ink faded across a fold, or that printers used the medial long-s (`ſ`). 

If an AI model silently 'corrected' an archaic word from `ye` to `the`, an automated merge tool might accept the AI's version simply because it looks like a modern dictionary word. In doing so, the algorithm destroys historical evidence and corrupts your edition.

Every difference between your passes represents a fork in scholarly interpretation. You cannot delegate that interpretation to a heuristic script. You must look at the primary manuscript image, inspect the physical ink, and make an active, documented editorial decision. That is why we create our third file manually through adjudication.

**Vocabulary.** *Automated merge* — A blind computational operation that accepts changes without contextual evaluation of historical evidence.

**Takeaway:** Never accept automated three-way merges on historical texts; every difference demands paleographical scrutiny.

---

## **08 Content**

**Establishing the Third File: transcription_reconciled.xml**

Now we begin hands-on construction. Before adjudicating any lines, you must create the container for your reconciled consensus text: `transcription_reconciled.xml`.

**Step-by-Step File Initialization:**

1. In the VS Code File Explorer, duplicate your manual transcription file (`witness.xml`) or create a new file in your repository root named `transcription_reconciled.xml`.
2. Ensure that this new file opens with the full standard TEI container hierarchy:
```xml
<text>
  <body>
    <div>
      <pb facs="#[surface-id]" n="[page-num]"/>
      <!-- Adjudicated paragraphs, lines, and milestones go here -->
    </div>
  </body>
</text>
```

3. Open `transcription_reconciled.xml` in an editor pane alongside your diff tab.

As you step through the diff chunks between `witness.xml` and `transcription_ai.xml`, you will build `transcription_reconciled.xml` line by line. If `witness.xml` is correct, keep its line. If `transcription_ai.xml` is superior, paste its reading into `transcription_reconciled.xml`. If both missed something, write the corrected reading directly into the reconciled file.

Notice the fundamental rule: **you do not edit witness.xml or transcription_ai.xml today**. Those two files remain frozen as historical records of Pass 1 and Pass 2. All edits occur exclusively in `transcription_reconciled.xml`.

**Vocabulary.** *Consensus document* — The third, authoritative file synthesized from the best verified readings of prior passes.

**Takeaway:** Create transcription_reconciled.xml as an independent file to house your reconciled readings without overwriting earlier passes.

---

## **09 Content**

**The Four Discrepancy Categories**

As you compare Pass 1 and Pass 2, you will encounter dozens of differences. To prevent cognitive overwhelm, textual scholars categorize discrepancies into a structured **error taxonomy**. 

In this course, every divergence falls into one of four distinct categories:

1. **Category A: Human Perceptual Fatigue (AI Correct).** You missed a letter, skipped an obscure word, or misread a clear character because your eyes were tired. Gemini caught it.
2. **Category B: AI Hallucination / Autoregressive Smoothing (Human Correct).** Gemini modernized spelling, expanded an abbreviation, invented words over smudges, or smoothed syntax. Your manual reading is faithful to the physical ink.
3. **Category C: Genuine Physical Ambiguity (Both Uncertain).** The manuscript itself is damaged, faded, torn, or stained. Both human and machine struggled.
4. **Category D: Layout and Structural Divergence.** Differences in line breaks (`<lb/>`), paragraph boundaries (`<p>`), or verse containers (`<lg><l>`).

Memorize these four categories. In Friday's lab and in tonight's assignment reflection (`RECONCILIATION.md`), you will formally report your diff results using this exact taxonomy.

**Vocabulary.** *Error taxonomy* — A structured classification system used to group and analyze different types of transcription discrepancies.

**Takeaway:** Classify every divergence into one of four categories: human fatigue, machine smoothing, physical ambiguity, or structural layout.

---

## **10 Content**

**Category A: Catching Human Perceptual Fatigue**

Let us examine Category A in detail. When you transcribed your page by hand in Week 4, you were reading unfamiliar historical scripts—perhaps 18th-century cursive or mid-20th-century folk handwriting. Close paleographical reading is exhausting. After thirty minutes, human attention degrades.

Common human fatigue errors include:

- Dropping small grammatical particles (e.g. skipping 'the', 'of', or 'and').
- Inverting adjacent letters (e.g. typing 'recieve' instead of 'receive' or vice-versa).
- Misreading unambiguous characters due to visual habit (e.g. reading an archaic letter 'e' as an 'o').

When you examine a diff chunk and see that Gemini transcribed a letter or word that you omitted, zoom in on your high-resolution image. Look closely at the physical ink. If the ink clearly shows the word that Gemini captured, celebrate! The AI model has served as an indefatigable second reader, catching an error caused by human fatigue.

**Your Action:** Accept Gemini's reading into `transcription_reconciled.xml`. Take note of this occurrence for your reflection report: human-machine double-keying has successfully caught a human slip.

**Vocabulary.** *Perceptual fatigue* — Cognitive exhaustion from prolonged close reading that causes transcribers to miss visual details.

**Takeaway:** When Gemini correctly reads characters that you misread due to fatigue, accept the machine reading into your consensus file.

---

## **11 Content**

**Cognitive Blind Spots: The Repetition and Skipping Effect**

One of the most pervasive cognitive phenomena in textual transmission is **eye-skip** (historically called *parablepsis* or *homoioteleuton*). 

When a historical text contains identical or similar words in close proximity, the human eye easily loses its place on the page:

```
Line 4: ...shall pay to the treasurer the sum of fifty pounds...
Line 5: ...and upon payment to the treasurer shall receive a receipt...
```

If a human transcriber looks away to type "to the treasurer" from Line 4, their eye often returns to the *second* occurrence on Line 5. As a result, the entire phrase between the two occurrences is silently omitted. Scribes in medieval scriptoria committed this exact error thousands of times, and modern students do the same.

Conversely, a computer vision model does not have an eye that wanders between lines. It processes visual patches systematically across pixel space. In a diff, an eye-skip appears as a sudden multi-word deletion in the manual pass.

When you see a large deletion chunk in `witness.xml`, check the manuscript image immediately. If you jumped a line, restore the missing text from `transcription_ai.xml` into `transcription_reconciled.xml`.

**Vocabulary.** *Eye-skip (parablepsis)* — An error where the transcriber's eye jumps between similar words or letters, skipping text in between.

**Takeaway:** Human readers frequently skip repeated words or jump lines; machine vision models reliably flag these omissions.

---

## **12 Content**

**Category B: Identifying Machine Hallucination**

Now we turn to Category B: machine failure. Large multimodal models like Gemini are autoregressive neural networks. They are trained to predict the most statistically probable next token given the prompt and the image context.

While this predictive power makes them remarkably fluent, it also creates their greatest paleographical danger: **hallucination**.

When an AI model encounters an ink smudge, a dark crease, or an ambiguous ligature, it does not stop and confess uncertainty unless forced to do so. Instead, the language model inside the vision architecture attempts to 'fill in the blank.' It predicts what word *ought* to appear in an 18th-century sentence, and emits that word as if it were plainly visible on the parchment!

In a diff, machine hallucination typically appears where `transcription_ai.xml` presents a complete, elegant sentence, but `witness.xml` contains an `<unclear>` tag or a partial word.

When you check the image, you will see the truth: there is only a smudge of faded ink. Gemini invented the word out of thin air.

**Your Action:** Reject the hallucination! Defend the physical document. Preserve your manual reading or mark the doubtful reading with `<unclear>` in `transcription_reconciled.xml`.

**Vocabulary.** *Hallucination* — A neural model error where the system generates plausible-sounding text unsupported by physical ink on the image.

**Takeaway:** Reject machine readings that invent missing letters or smooth out messy manuscript realities.

---

## **13 Content**

**The Modernization Reflex: Defending Archaic Orthography**

The most frequent Category B error is what we call the **modernization reflex** (or autoregressive smoothing). 

Multimodal foundation models are trained on billions of words of modern web text, news articles, and contemporary literature. Standard English orthography acts like a powerful gravitational pull on the model's outputs. Even when you instruct Gemini with strict negative constraints, the model will constantly attempt to 'correct' historical spelling:

- `publick` $\to$ modernized to `public`
- `compleat` $\to$ modernized to `complete`
- `shew` $\to$ modernized to `show`
- `Janry` $\to$ modernized to `January`
- `ye` $\to$ modernized to `the`

In the diff editor, these modernizations appear as crisp character-level discrepancies. Look at `witness.xml`: you transcribed `compleat` because the author wrote `c-o-m-p-l-e-a-t`. Look at `transcription_ai.xml`: Gemini emitted `complete`.

Remember: our goal this week is **diplomatic transcription**. We want to preserve the exact physical and orthographical testimony of the witness. Do not let the machine homogenize historical language.

**Your Action:** Reject Gemini's modernized spelling. Keep the authentic archaic spelling in `transcription_reconciled.xml`.

**Vocabulary.** *Archaic orthography* — Historical spelling practices that differ from modern standardized dictionaries.

**Takeaway:** When Gemini silently modernizes historical spellings like 'compleat' or 'publick', reject the edit and defend the authentic ink.

---

## **14 Content**

**Scribal Abbreviations vs. Silent AI Expansion**

A related failure mode in Category B is the **silent expansion of abbreviations**. 

Historical writers made extensive use of abbreviations. Paper and parchment were expensive, and writing with a quill pen was labor-intensive. Standard abbreviations included:

- Brevigraphs like `&` and `&c.` (et cetera)
- Suspensions like `Govr` (Governor) or `Honble` (Honorable)
- Superscript letters (e.g. `y^e` for *the*, `y^t` for *that*, `w^ch` for *which*)

When Gemini encounters `Govr`, its internal language model recognizes the semantic concept 'Governor'. Unless strictly constrained, it will often output `<p>Governor</p>` instead of `<p>Govr</p>`.

In Week 6 (Normalization), we will learn how to encode abbreviations and their modern expansions together using TEI elements like `<choice>`, `<abbr>`, and `<expan>`. 

**However, this week, normalization elements are strictly locked!** Today, we are establishing the pure, unexpanded diplomatic baseline. If Gemini expanded an abbreviation, it broke the diplomatic boundary.

**Your Action:** Reject the expanded word. Keep the unexpanded historical abbreviation in `transcription_reconciled.xml`.

**Vocabulary.** *Scribal abbreviation* — A shortened written form or symbol used by historical writers to conserve parchment, ink, or writing time.

**Takeaway:** Keep abbreviations like '&c.', 'ye', and 'Govr' exactly as written; do not let Gemini silently expand them.

---

## **15 Content**

**Long-s (ſ) and Historical Letterforms**

For students working with 18th-century printed texts (such as Ace's 1791 French Revolutionary Decree), one particular glyph creates continuous diff discrepancies: the **medial long-s (`ſ`)**.

In European printing from the Renaissance until around 1800, printers used two distinct lowercase forms of the letter 's':

- The short round 's' (`s`) was used at the end of words (e.g. `leurs`, `dans`).
- The long-s (`ſ`) was used at the beginning and in the middle of words (e.g. `aſſemblée`, `ſerment`, `neceſſaire`).

The long-s looks very similar to a lowercase 'f', but lacks the full right-hand horizontal crossbar.

Standard AI vision models constantly collapse the long-s into a modern round 's'. When viewing the diff of Ace's decree:

- `witness.xml` contains `aſſemblée` (using Unicode `U+017F`).
- `transcription_ai.xml` contains `assemblée` (using modern `s`).

While modernizing the long-s is common in popular reprints, in a diplomatic digital edition we preserve the exact typographic testimony of the 1791 printing press. 

**Your Action:** Preserve the historical long-s glyph (`ſ`) in `transcription_reconciled.xml`.

**Vocabulary.** *Medial long-s (ſ)* — An archaic lowercase letterform resembling an 'f' without a crossbar, used medially in 18th-century typography.

**Takeaway:** If Gemini normalized the long-s (ſ) into a modern 's', restore the historical glyph to preserve printed testimony.

---

## **16 Content**

**Category C: Genuine Physical Ambiguity on the Artifact**

Category C represents the moments where the disagreement between Pass 1 and Pass 2 is not caused by human error or machine bias, but by the physical condition of the artifact itself.

Manuscripts are physical objects that have survived decades or centuries of handling, folding, dampness, and chemical decay:

- Ink fades to faint yellowish ghosts of letters.
- Acidic iron-gall ink burns through paper fibers.
- Moisture creates water stains and cockling.
- Folds, tears, and seal wax obscure written lines.

When you reach a Category C diff chunk, you will notice that both you and Gemini hesitated:

- Perhaps you transcribed `p<unclear>ai</unclear>d` while Gemini guessed `part`.
- Perhaps you left a blank space while Gemini output `trans<unclear>action</unclear>`.

Neither reading is completely right or completely wrong. The physical reality of the page is genuinely ambiguous. 

In digital editing, you do not force a fake resolution. TEI provides specialized markup designed specifically to communicate scholarly uncertainty with mathematical precision: `<unclear>` and `<gap/>`.

**Vocabulary.** *Physical ambiguity* — Manuscript uncertainty caused by physical damage, ink fading, paper tears, or heavy smudges.

**Takeaway:** Where both human and machine struggle with damaged physical ink, resolve the disagreement with TEI scholarly markup.

---

## **17 Content**

**Adjudicating Faded Ink: The Decisive Use of unclear**

When you adjudicate a Category C reading where ink is faded but partially decipherable, the TEI `<unclear>` element is your primary tool.

A foundational principle of scholarly editing is: **never guess in silence**. 

If you or Gemini believe that a faded stroke represents the word "Tuesday", but the letters "es" are smeared by a thumbprint, do not output bare `Tuesday`. Typing bare text implies to the reader that the manuscript is pristine. 

Instead, enclose the uncertain reading inside `<unclear>`:
```xml
<p><lb n="12"/>paid on <unclear>Tuesday</unclear> last</p>
```

You can even apply `<unclear>` to individual characters within a word:
```xml
<p><lb n="12"/>paid on Tu<unclear>es</unclear>day last</p>
```

When someone views your digital edition, the rendering stylesheet will display `<unclear>` text with sublinear dots or brackets, alerting the reader to the editorial uncertainty. Using `<unclear>` demonstrates scholarly integrity: you provide your best paleographical hypothesis while honestly signaling the limits of physical evidence.

**Vocabulary.** *unclear element* — A TEI tag wrapping candidate readings that are probable but visually uncertain due to manuscript degradation.

**Takeaway:** Wrap ambiguous readings in the unclear tag rather than guessing silently or omitting doubtful characters.

---

## **18 Content**

**Documenting Lacunae: When to Deploy gap**

What happens when text is not merely faded, but physically non-existent? 

- A moth or bookworm ate a hole through the leaf.
- A wax seal tore away the corner of the letter when opened.
- Fire or water completely obliterated a three-word patch of script.

When there are zero surviving ink traces, you cannot use `<unclear>` because there are no candidate letters to wrap. Guessing words out of thin air is hallucination.

Instead, TEI provides the empty milestone element `<gap/>`. The `<gap/>` element records a physical **lacuna** without guessing the missing letters.

Scholarly standards require you to specify why the text is missing and approximately how much is lost:
```xml
<!-- Three characters lost to an ink blot -->
<p><lb n="5"/>paid to <gap reason="damage" unit="chars" extent="3"/> on arrival</p>

<!-- Approximately two whole words lost to a torn paper corner -->
<p><lb n="6"/>received from <gap reason="tear" unit="words" extent="2"/> upon receipt</p>
```

Notice that `<gap/>` is self-closing (`<gap ... />`). It never wraps text because there is no text to wrap. In `transcription_reconciled.xml`, use `<gap/>` to mark physical absence honestly.

**Vocabulary.** *Lacuna* — A physical gap or hole in the document surface where text has been completely destroyed.

**Takeaway:** Use empty milestone gap elements with reason and extent attributes when text is physically obliterated by damage.

---

## **19 Content**

**Category D: Structural and Layout Discrepancies**

Category D encompasses differences that are not about spelling or words, but about **XML structure and layout architecture**.

Common Category D discrepancies include:

1. **Missing Container Tags:** Gemini may have placed text directly inside `<div>` without wrapping it in `<p>` (prose) or `<lg><l>` (verse). This causes immediate schema validation failure against `msdesc.rng`.
2. **Displaced Page Milestones:** One pass placed `<pb facs="#..."/>` before `<div>`, while the other placed it inside `<div>`. In standard TEI, `<pb/>` sits inside `<div>` right before the first line of the page.
3. **Mismatched Line Breaks:** Gemini broke a line at word ten, while you broke it at word eleven.
4. **Column Flow Conflicts:** In a multi-column document, one pass read horizontally across columns while the other read vertically down Column 1 and then Column 2.

When resolving Category D discrepancies in `transcription_reconciled.xml`, your primary guide is the TEI structural grammar:

- `<text>` $\to$ contains `<body>` $\to$ contains `<div>`
- `<div>` $\to$ contains `<p>` (prose) or `<lg>` (verse)
- `<p>` $\to$ contains running text interleaved with `<lb/>` milestones

Ensure that your reconciled consensus document obeys this strict hierarchy from top to bottom.

**Vocabulary.** *Layout discrepancy* — A divergence between two passes concerning lineation, column boundaries, or structural tag hierarchy.

**Takeaway:** Resolve structural differences by enforcing valid TEI containment: text inside body inside div.

---

## **20 Content**

**Reconciling Physical Lineation: lb Milestones**

One of the most frequent diff differences between Pass 1 and Pass 2 involves the placement of `<lb/>` milestones.

In diplomatic transcription, `<lb/>` (line beginning) is an empty milestone element. It does not wrap words; it simply marks the spatial point where a writer or typesetter dropped to a new physical line on the page.

Consider this diff discrepancy:

- Pass 1 (`witness.xml`):
```xml
<p><lb n="1"/>To the Honorable Council of Safety
<lb n="2"/>Gentlemen</p>
```

- Pass 2 (`transcription_ai.xml`):
```xml
<p><lb n="1"/>To the Honorable Council of Safety Gentlemen</p>
```

Gemini omitted `<lb n="2"/>` because in modern English grammar, "Gentlemen" is a salutation that might sit on the same line in a flowing email. But on the physical artifact, the writer dropped down to a new line!

Look at the image. Did the author physically drop down? Yes. Therefore, Pass 1 is correct. 

**Formatting Best Practice:** In `transcription_reconciled.xml`, always place each `<lb/>` milestone on a new visual line in your editor:
```xml
<p>
  <lb n="1"/>To the Honorable Council of Safety
  <lb n="2"/>Gentlemen
</p>
```
This makes your XML mirror the visual lineation of the manuscript, making future proofreading effortless.

**Vocabulary.** *Physical lineation* — The literal arrangement of words across lines on the page, independent of grammar or metre.

**Takeaway:** Ensure lb milestones mark every physical line break on the artifact, aligning Pass 3 with the physical page coordinates.

---

## **21 Content**

**Reconciling Prose Paragraphs: p vs. Poetry lg and l**

During diff reconciliation, check how each pass handled high-level textual containers. TEI enforces a rigid distinction between prose and poetry:

- **Prose Documents (Ace, Olyvia, Andromeda):** Legal decrees, personal correspondence, and colonial treaties are continuous prose. All running text must be wrapped inside paragraph containers: `<p>`. 
- **Poetry Manuscripts (Jay):** Metrical verse cannot be wrapped in `<p>`. It must be organized into stanzas using line groups (`<lg>`), and each poetic metrical line must be wrapped in a line element (`<l>`).

If Gemini transcribed a prose document using `<l>` tags for every physical line, or transcribed Emily Dickinson's poem as a flat prose `<p>` paragraph, it made a major structural error!

In `transcription_reconciled.xml`, correct the container markup:
```xml
<!-- PROSE EXAMPLE (Ace, Olyvia, Andromeda) -->
<div>
  <p>
    <lb n="1"/>We the undersigned commissioners...
  </p>
</div>

<!-- POETRY EXAMPLE (Jay) -->
<div>
  <lg type="stanza">
    <l n="1"><lb n="1"/>I would not stop for Death –</l>
    <l n="2"><lb n="2"/>He kindly stopped for me –</l>
  </lg>
</div>
```
Enforcing proper paragraph and verse wrappers ensures your text validates cleanly against `msdesc.rng`.

**Vocabulary.** *Paragraph wrapper (p)* — The standard TEI container enclosing running prose sentences within a text division.

**Takeaway:** Wrap prose running text inside p containers, reserving lg and l for poetic verse.

---

## **22 Content**

**Cohort Adjudication: Jay and Dickinson's Variant Readings**

Now let us review the specific adjudication targets for each member of our four-person cohort.

For **Jay**, working with Emily Dickinson's poem manuscript (`MS Am 1118.3 [338]`):

1. **Idiosyncratic Dashes:** Dickinson wrote dashes of varying lengths, slants, and heights. Inspect the diff between Pass 1 and Pass 2:
   - Did you transcribe spaced hyphens (` - `) while Gemini output em-dashes (`—`)?
   - Adjudicate according to your editorial policy. In diplomatic transcription, recording an en-dash (`–`) or spaced dash is standard. Ensure consistency throughout `transcription_reconciled.xml`.
2. **Narrow Paper Line Wraps:** Dickinson's paper was narrow (~100 mm wide). Line 3 of a stanza might wrap onto a second physical line on the page. In `transcription_reconciled.xml`, verify that the metrical line is wrapped in `<l>`, with an empty `<lb/>` milestone marking the physical wrap:
   ```xml
   <l n="3"><lb n="3"/>The Carriage held but just Ourselves –
   <lb n="4"/>and Immortality.</l>
   ```

3. **Pencil Revisions:** Dickinson frequently wrote variant word choices in pencil above the pen-and-ink lines. Did Gemini skip the pencil variants or fuse them into the sentence? In Pass 3, decide whether to record the interlinear pencil reading or note it with `<unclear>`.

Document your adjudication of Dickinson's dashes and wraps in your reflection report!

**Vocabulary.** *Interlinear variant* — Alternative words or phrases written between lines or in margins by the author during revision.

**Takeaway:** For Jay's Dickinson poem, ensure stanza structures (lg/l) and line-wrap milestones (lb) correctly reflect the narrow manuscript sheet.

---

## **23 Content**

**Cohort Adjudication: Ace and Two-Column Decrees**

For **Ace**, working with the 1791 French Revolutionary National Assembly Decree:

1. **Sequential Column Flow:** The decree is printed in two parallel vertical columns separated by a central rule. A major AI failure mode in multi-column broadsides is reading horizontally across both columns (e.g. reading line 1 of Column 1, followed immediately by line 1 of Column 2).
   - In your diff, check whether Gemini read horizontally or vertically.
   - In `transcription_reconciled.xml`, enforce the correct reading order: transcribe completely down Column 1, then proceed down Column 2. You can use `<cb n="1"/>` and `<cb n="2"/>` (column break milestones) to mark column transitions.
2. **Historical Long-s (`ſ`):** Inspect every instance where Gemini replaced `ſ` with modern `s`. In `transcription_reconciled.xml`, restore the authentic 18th-century long-s glyph (`ſ`) to preserve the physical testimony of the Paris revolutionary press.
3. **Colophons and Attestations:** At the bottom of the decree, verify that official printing attestations, commissioner signatures, and legal dates are properly grouped in `<p>` blocks with `<lb/>` milestones.

Ace's reflection report should highlight whether Gemini respected columnar layout or required manual structural intervention.

**Vocabulary.** *Columnar reading order* — The vertical sequential flow of text down one printed column before starting the adjacent column.

**Takeaway:** For Ace's French Decree, verify that the reconciled text flows down Column 1 before Column 2, preserving historical typography.

---

## **24 Content**

**Cohort Adjudication: Olyvia and Maud Lewis's Folk Orthography**

For **Olyvia**, working with the handwritten personal letter by Nova Scotia folk artist Maud Lewis (1903–1970):

1. **Defending Vernacular Orthography:** Maud Lewis wrote with lively, informal, and phonetic spelling typical of rural mid-20th-century Nova Scotia. In your diff, look for instances where Gemini "corrected" Maud's spelling or grammar:
   - Did Maud write *bin* and Gemini changed it to *been*?
   - Did Maud write *dont* without an apostrophe and Gemini inserted the apostrophe?
   - In `transcription_reconciled.xml`, **reject every one of Gemini's corrections!** Maud's letter is a precious cultural artifact. Correcting her spelling is an act of patronizing editorial erasure. Defend Maud's authentic voice.
2. **Drifting Baselines and Faded Creases:** Because of severe arthritis in her hands, Maud's lines drift across the page. Where the paper was folded into an envelope, ink may be faded along the crease.
   - If both you and Gemini struggled with a crease, evaluate whether the reading is probable enough for `<unclear>` or if it should be marked with `<gap reason="faded"/>`.
   - Ensure `<lb/>` milestones capture where Maud started new lines as her script drifted.

Olyvia's reflection report will center on protecting folk-art historical expression from the homogenizing tendencies of large language models.

**Vocabulary.** *Folk orthography* — Informal, phonetic, and non-standard writing produced outside institutional schooling.

**Takeaway:** For Olyvia's Maud Lewis letter, vigorously defend Maud's authentic folk spelling against modern machine smoothing.

---

## **25 Content**

**Cohort Adjudication: Andromeda and Bilingual Treaty Margins**

For **Andromeda**, working with the 1752 Peace and Friendship Treaty between Governor Peregrine Thomas Hopson and Chief Major Jean-Baptiste Cope:

1. **Legal Article Structure:** The treaty is organized into a formal preamble followed by numbered articles. In `transcription_reconciled.xml`, verify that each article is properly enclosed in a `<p>` container with line breaks (`<lb/>`):
   ```xml
   <p>
     <lb n="15"/>1. It is agreed that the said Tribe of Mickmack Indians...
   </p>
   ```

2. **Capitalization and Honorifics:** 18th-century treaties feature heavy, idiosyncratic capitalization of legal nouns (*Tribe*, *Treaty*, *His Majesty*, *Peace*, *Friendship*). Check your diff: did Gemini lower-case any of these capitalized terms? Preserve the full 18th-century capitalization as written.
3. **Totem Marks and Signatures:** At the foot of the document, Chief Cope signed not with alphabetic English script, but with his personal totem mark. Check how Pass 1 and Pass 2 handled this mark:
   - If Gemini ignored the mark or output a random punctuation symbol, replace it in `transcription_reconciled.xml` with appropriate descriptive markup:
     `<figure><figDesc>Totem mark of Chief Major Jean-Baptiste Cope</figDesc></figure>`

   - Link the mark to its physical coordinates if calibrated in Module 3.

Andromeda's reflection will document the technical challenge of encoding non-alphabetic indigenous legal signatures within an XML transcription.

**Vocabulary.** *Diplomatic treaty layout* — Formal layout conventions separating preamble, numbered articles, signatures, and tribal totem marks.

**Takeaway:** For Andromeda's 1752 Treaty, ensure legal article headings, signatures, and Cope's totem mark are cleanly structured.

---

## **26 Content**

**Schema Validation: Driving transcription_reconciled.xml to Zero Errors**

With your line-by-line adjudication complete and `transcription_reconciled.xml` fully drafted, you must subject the file to strict automated quality control.

In the VS Code Terminal, run the schema validation command against the course grammar:
```bash
python3 -m jing msdesc.rng transcription_reconciled.xml
```
(Or use the XML extension's built-in validation indicator in the bottom status bar).

Your target is absolute: **0 errors**.

Common validation diagnostics and fixes:

1. **Error: `element "text" not allowed here`:** You placed text directly inside `<div>`. Wrap the sentences in `<p>...</p>` (or `<lg><l>...</l></lg>` for poetry).
2. **Error: `character "&" is the first character of a delimiter but must not start a general entity`:** You transcribed a literal ampersand (`&c.`). Escape every raw ampersand as `&amp;c.`.
3. **Error: `element "lb" not allowed here`:** You used a closing tag like `</lb>`. Change it to an empty milestone: `<lb/>`.
4. **Error: `required attribute "facs" missing`:** Your `<pb/>` tag is missing its surface pointer. Add `@facs="#your_surface_id"`.

Keep fixing and re-validating until the validator outputs zero warnings and zero errors. A file that fails schema validation cannot be accepted into the digital edition.

**Vocabulary.** *Deterministic validation* — Automated verification confirming that an XML document strictly obeys every rule of a schema grammar.

**Takeaway:** Validate transcription_reconciled.xml against msdesc.rng, resolving every syntax and hierarchy error to reach 0 errors.

---

## **27 Content**

**Writing the Reconciliation Reflection (RECONCILIATION.md)**

The final deliverable of Week 5 is not code; it is scholarly writing. In your repository root, create a markdown document named `RECONCILIATION.md`.

Your reflection report must be **300 to 500 words** and organized into three structured sections:

**1. Quantitative Overview:**

- How many total diff chunks separated your manual pass from your AI pass?
- What was the rough distribution across the four categories (e.g. "We identified 4 Category A human slips, 11 Category B machine smoothings, 2 Category C ink ambiguities, and 3 Category D lineation differences")?

**2. Qualitative Adjudication Analysis:**

- Provide at least one specific concrete example of a **Category A** slip where Gemini caught an error you made due to fatigue. What was the word? Why did you miss it?
- Provide at least one specific concrete example of a **Category B** failure where Gemini hallucinated or modernized spelling. How did you defend the manuscript ink?
- Discuss any **Category C** physical ambiguities. Did you choose `<unclear>` or `<gap/>`, and why?

**3. Tool Evaluation:**

- Based on your empirical results, what are the strengths and dangers of using multimodal AI in digital paleography?

Write with academic precision. This report proves to evaluators that your final consensus text is the product of deliberate scholarly methodology.

**Vocabulary.** *Methodological reflection* — A written scholarly explanation documenting editorial decisions, error patterns, and tool evaluation.

**Takeaway:** Compose a 300–500 word report in RECONCILIATION.md detailing what Gemini caught, where it failed, and how you adjudicated.

---

## **28 Content**

**Documenting Provenance: The Value of Negative Findings**

A common anxiety among student researchers is the fear of failure. When novice editors see that Gemini modernized dozens of words or hallucinated text over an ink smudge, they sometimes worry that they 'prompted the model incorrectly' or that their lab experiment failed.

In the digital humanities, **negative findings are primary scholarly data**.

When you document that Gemini 1.5 Pro or Gemini 2.0 consistently converted the 18th-century long-s (`ſ`) into a modern `s`, or that it modernized Maud Lewis's vernacular spelling despite three explicit prompt instructions forbidding modernization, you have discovered an empirical truth about the architecture of large language models!

You are proving that autoregressive foundation models have an innate bias toward contemporary standardization. That discovery is a valuable research finding. When published in your reflection, it alerts future historians, archivists, and editors to the specific vulnerabilities of AI transcription pipelines.

Do not conceal machine failures. Document them rigorously with line numbers, diff quotes, and comparative analysis in `RECONCILIATION.md`. Scholarly honesty is the hallmark of genuine research.

**Vocabulary.** *Negative finding* — An experimental result showing where a computational tool or model failed to perform accurately.

**Takeaway:** Documenting where AI failed (such as silent modernizations) is valuable scholarly research, not an embarrassing mistake.

---

## **29 Content**

**The Transcription Assignment Submission Checklist**

Tonight at **11:00 PM (Friday, Oct 2)**, the formal **Transcription Assignment** is due. 

Before you conclude your work session, review the final submission checklist to guarantee full marks:

1. **`witness.xml` (Pass 1):** Your manual diplomatic transcription from Week 4. Untouched today. Valid TEI.
2. **`transcription_ai.xml` (Pass 2):** Gemini's Antigravity AI transcription from Tuesday. Untouched today. Valid TEI.
3. **`transcription_reconciled.xml` (Pass 3):** Your newly synthesized consensus transcription. Fully adjudicated. Validates to **0 errors** against `msdesc.rng`.
4. **`RECONCILIATION.md`:** Your 300–500 word reflection report detailing quantitative diff metrics, concrete category examples, and AI tool evaluation.

**Git Submission Command:**
In your VS Code terminal, stage and commit the entire deliverable bundle:
```bash
git add witness.xml transcription_ai.xml transcription_reconciled.xml RECONCILIATION.md
git commit -m "Step 3: completed transcription reconciliation and reflection report"
```

Verify your commit using `git status` (should report 'working tree clean') and `git log -n 1 --stat`. You have completed the hardest technical milestone of the term!

**Vocabulary.** *Deliverable bundle* — The complete package of required files committed to version control and submitted for evaluation.

**Takeaway:** Verify that your repository contains all four required files: witness.xml, transcription_ai.xml, transcription_reconciled.xml, and RECONCILIATION.md.

---

## **30 Content**

**Looking Ahead: The Bridge to Week 6 Normalization**

Congratulations! By completing `transcription_reconciled.xml`, you have established an authoritative, verified diplomatic baseline for your historical document.

Take a moment to appreciate where you stand. You began with a raw high-resolution photograph. You calibrated its physical boundaries in Module 3. You transcribed its text by hand, tested an advanced AI model, and rigorously adjudicated every discrepancy. You have transformed ink on paper into clean, standardized, machine-readable digital data.

**What Happens Next Week (Week 6: Normalization)?**
In Meeting #14 on Tuesday, we finally unlock the editorial elements we deliberately kept locked all week:

- `<choice>`: The parent element linking original testimony to editorial intervention.
- `<orig>` and `<reg>`: Linking original historical spelling (e.g. `publick`) to modern standardized spelling (`public`).
- `<abbr>` and `<expan>`: Linking historical scribal abbreviations (`&c.`, `Govr`) to their full expansions (`et cetera`, `Governor`).

Because your diplomatic baseline in `transcription_reconciled.xml` is uncorrupted by silent modernizations, you will be able to apply these normalization elements with total scholarly confidence. Rest well this weekend; on Tuesday, we begin editorial normalization!

**Vocabulary.** *Editorial normalization* — The stage where historical orthography is linked to modern standardized forms via choice elements.

**Takeaway:** Your reconciled diplomatic baseline provides the uncorrupted foundation for next week's editorial normalization.

---

