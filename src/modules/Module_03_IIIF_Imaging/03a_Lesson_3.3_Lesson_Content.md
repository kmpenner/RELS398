# Lesson 3.3 — AI-Assisted Imaging in Historical Document Studies

*RELS 398 / ENGL 398 · Topic 3: IIIF Imaging · Meeting #8 (Fri Sep 18)*

***Step 3 of the three-step cycle: AI-assisted.** You have measured a page by hand and then with tools that measure exactly. Today a model looks at the page and proposes answers. Your job is to judge them.*

---

## **01 Content**

**The AI Paradigm Shift: From Deterministic Filters to Statistical Vision Models**

The tools in Lesson 3.2 work on pixels. `-deskew` measures an angle; `-level` moves brightness values. None of them knows what a page *is*. They cannot tell a heading from a signature, because those are meanings, not numbers.

AI vision models work differently. They are trained on very large collections of images until they can recognize patterns: this shape is a line of writing, this block is a margin, this smudge is a stamp.

That is genuinely useful. It is also a different kind of claim. `-deskew` reports a measurement. A vision model reports a **guess** — usually a good one, sometimes confidently wrong.

**Vocabulary.** *Vision model* — software trained to recognize patterns in images. *Statistical* — based on what is probable, rather than calculated exactly.

**Takeaway:** Deterministic tools measure pixels; AI vision models recognize meaning by pattern, which makes their output a proposal rather than a measurement.

---

## **02 Content**

**Overcoming the Manual Bottleneck: Why AI in Archival Imaging?**

Wednesday you drew one zone by hand and it took a few minutes. Now imagine the same work for every line of a page, then every page of a register.

That arithmetic is why AI entered this field. A scholar's real bottleneck is not thinking; it is tracing rectangles and typing coordinates.

For your four projects the scale is modest. Olyvia's Maud Lewis letter or Andromeda's treaty sheet could be zoned by hand in an afternoon. For Ace's printed decree, with two columns of articles, hand-tracing every line would already be tedious. For an archive with thousands of leaves it is impossible.

The promise is simple: let the machine do the tracing, and spend your time on what the tracing is *for*.

**Vocabulary.** *Bottleneck* — the step that limits how much work can be finished.

**Takeaway:** AI targets the repetitive part of facsimile work — tracing and typing coordinates — so editors can spend time on interpretation instead.

---

## **03 Content**

**Computer Vision Foundations: Convolutional Networks, Vision Transformers, and Multimodal LLMs**

You do not need the mathematics, but the vocabulary appears in every tool's documentation, so here are the three families in plain terms.

- **Convolutional networks (CNNs)** slide small filters across an image, building up from edges and strokes to shapes like letters and text blocks. They are reliable for marking out regions.
- **Vision transformers (ViTs)** look at the whole page at once and weigh how distant parts relate. This helps when something in the margin belongs with something at the top.
- **Multimodal language models** — the image-capable versions of the assistants you met in Lesson 2.3 — take a picture and a written instruction together, and answer in words or coordinates.

The practical difference: the first two are specialists you run over many pages; the third is a generalist you can simply ask.

**Vocabulary.** *Model* — a trained program that makes predictions. *Multimodal* — able to handle images and text together.

**Takeaway:** CNNs and vision transformers are specialists for finding regions; multimodal language models are generalists you instruct in ordinary language.

---

## **04 Content**

**Machine-Readable Layout Analysis: Document Image Analysis (DIA)**

**Document Image Analysis** is the task of turning a picture of a page into a description of its parts. It comes in two layers.

*Physical* analysis finds where things are: ink here, blank paper there, a block of text in this rectangle.

*Logical* analysis says what those things are: this block is the main text, this one is a running header, this is a marginal note.

The two often disagree, and the disagreement is where scholarship lives. In a Dickinson poem, a line may physically run onto a second line because the paper ran out, while being one poetic line. Physically two, logically one. The machine sees the paper; you know the poem.

**Vocabulary.** *Layout analysis* — identifying the regions of a page and what they are. *Region* — a bounded area such as a text block or margin.

**Takeaway:** Layout analysis separates where marks sit from what they mean, and the gap between the two is exactly where editorial judgement is required.

---

## **05 Content**

**Automated Page Segmentation: Distinguishing Margins, Headers, and Text Blocks**

**Segmentation** is the first step: divide the page into functional blocks before worrying about words.

A model trained on historical documents typically returns blocks labelled as main text, header or page number, marginal note, decoration or illustration, and blank margin.

The output is a list of rectangles or polygons with labels and coordinates. That is exactly the shape of information a TEI `<zone>` needs, which is why this step matters to you: a good segmentation is a draft facsimile.

The failure to expect is over-confidence at the edges. Models routinely mark a water stain as a text block, or miss a faint marginal note because it does not look like the examples they were trained on.

**Vocabulary.** *Segmentation* — dividing an image into labelled regions. *Polygon* — a shape of several points, for regions that are not rectangles.

**Takeaway:** Segmentation returns labelled regions with coordinates, giving you a draft set of zones — including plausible-looking zones around stains.

---

## **06 Content**

**Baseline Detection and Text-Line Segmentation: Kraken, dhSegment, and Transkribus**

A **baseline** is the invisible line letters sit on, ignoring descenders like the tail of a *p*.

Why not just draw a box around each line? Because in real handwriting the boxes overlap. Maud Lewis's letter or a Dickinson draft will have a descender from one line crossing into the next, so a rectangle round line two also captures pieces of lines one and three.

Modern tools — **Kraken**, **dhSegment**, and **Transkribus**, which you will meet properly in Module 4 — therefore trace a wavy line along the bottom of each row of letters, then build a shape that follows the line's actual contour.

Those shapes become `<zone type="line">` elements, which is what lets a reader hover over a transcribed line and see the exact strokes light up.

**Vocabulary.** *Baseline* — the line letters sit on. *Descender* — the part of a letter below the baseline.

**Takeaway:** Baselines follow the wander of real handwriting, separating interlocking lines that rectangles cannot.

---

## **07 Content**

**Generating TEI `<zone>` Coordinates with AI: From Polygons to Bounding Boxes**

Models return coordinates in whichever format their authors chose. You will meet three:

- **Pixels as x, y, width, height** — the most common.
- **Fractions between 0 and 1** — relative to the page, so they survive resizing.
- **Lists of points** — for irregular shapes.

TEI wants none of those directly. It wants corners: `ulx`, `uly`, `lrx`, `lry`. So a short script does the conversion — the same conversion you did by hand on Wednesday with `make_surface.py`:

```
ulx = x            lrx = x + width
uly = y            lry = y + height
```

For genuinely irregular things — a wax seal, a diagonal note — TEI offers `@points` instead, taking a list of coordinate pairs.

The lesson worth keeping: converting between coordinate conventions is where silent errors enter. A zone that is offset or inside-out usually means a conversion, not a model, went wrong.

**Vocabulary.** *Bounding box* — the smallest rectangle containing a feature. *Normalized coordinates* — coordinates expressed as fractions of the page.

**Takeaway:** AI output must be converted from x/y/width/height into TEI's corner attributes, and most coordinate errors happen in that conversion rather than in the model.

---

## **08 Content**

**Addressing Complex Layouts: Multi-Column Broadsides and Interlinear Additions**

Reading order is the first thing a model gets wrong on a real document.

Ace's 1791 decree is printed in columns. A model that simply reads down the page will take a line from the left column, then a line from the right, and produce nonsense — text that is perfectly segmented and completely unreadable.

Jay's Dickinson manuscript fails differently. Dickinson wrote variant words above and beside her lines. A model sees another row of writing and calls it the next line, flattening a deliberate alternative into the middle of the poem.

Good tools estimate reading order as well as regions, and let you correct it. Always check the order before the coordinates: a beautifully placed zone attached to the wrong line is worse than no zone.

**Vocabulary.** *Reading order* — the sequence in which regions should be read. *Interlinear* — written between the lines.

**Takeaway:** Columns and interlinear variants break automatic reading order, so verify sequence before you trust any zone-to-text links.

---

## **09 Content**

**Vernacular and Irregular Handwriting: Overcoming Folk Script Challenges**

Models are trained mostly on tidy material: printed books, formal clerical hands, modern correspondence. Ordinary handwriting is a much harder case.

Olyvia's project shows why. Maud Lewis lived with severe rheumatoid arthritis, and her hand reflects it: uneven letter sizes, changing pressure, lines that drift uphill on unruled paper.

A general model may lose the baseline halfway across, merge two drifting lines, or treat a whole passage as background. This is not a defect in the handwriting. It is a mismatch between the document and what the model was shown during training.

Two remedies: choose a model trained on handwriting rather than print, or fine-tune one on a few pages you have corrected yourself (section 23).

**Vocabulary.** *Vernacular hand* — ordinary everyday handwriting, as opposed to a formal trained script. *Training data* — the examples a model learned from.

**Takeaway:** Models fail on irregular everyday hands because their training data was tidier than the document, not because the document is deficient.

---

## **10 Content**

**Non-Textual Feature Detection: Identifying Seals, Signatures, and Totemic Marks**

Not everything on a page is writing, and the non-writing is often what gives a document its force.

Andromeda's treaty carries colonial seals, the signatures of British officials, and the marks made by Mi'kmaw signatories. Those marks are not decoration and not failed letters: they are how the agreement was signed.

Text recognition handles all of this badly. It either ignores such marks as noise or forces them into letters, producing nonsense where something important sits.

Object detection is the right tool, and the right encoding is a zone with an honest type — `<zone type="seal">`, `type="signature">`, `type="mark">` — recording where the feature is and what it is, without pretending it is text.

Choosing that type is an editorial decision about what the document *is*. No model should make it for you.

**Vocabulary.** *Object detection* — locating specific kinds of things in an image. *Non-textual feature* — a meaningful mark that is not writing.

**Takeaway:** Seals, signatures, and signatory marks should be encoded as typed zones rather than forced into text, and naming their type is an editorial judgement.

---

## **11 Content**

**Automated Image Organization: Clustering, Duplicate Detection, and Sorting**

A day's photography produces a mess: several shots of the same page, test exposures, frames of the colour target, the occasional blurred one.

Software can sort this. A model converts each image into a list of numbers describing its appearance, and images that look alike end up with similar numbers. From that you can group near-duplicates, separate calibration shots from real pages, and spot a gap in a sequence.

Note what is and is not being decided. The software groups by appearance. It does not know which of two near-identical shots is the one you want to keep. Deleting is still your call, and the safer habit is to move rejects aside rather than delete them.

**Vocabulary.** *Clustering* — grouping items that resemble one another. *Near-duplicate* — two captures of the same thing that differ slightly.

**Takeaway:** Clustering can group duplicates and flag gaps in a capture sequence, but which duplicate survives is an editorial decision.

---

## **12 Content**

**Smart Image Naming: Deriving Standardized File Names from Document Content**

`IMG_4829.jpg` tells you nothing. `nsarm_rg1_v430_no2_r.jpg` tells you the repository, the reference, and the side.

Renaming hundreds of files by hand is exactly the work AI should absorb. A model can read a printed page number or a pencilled folio mark, judge whether a leaf is a recto or a verso from where the binding shadow falls, and a script can then rename the file accordingly.

One caution, learned the hard way in this course: a wrong filename is worse than a meaningless one. `f01r` on an image that is actually the verso will propagate into your TEI, your citations, and your published edition, and nothing downstream will question it. Spot-check a sample before letting a script rename a whole directory.

**Vocabulary.** *Recto / verso* — the front and back of a leaf. *Canonical filename* — a name following an agreed, predictable pattern.

**Takeaway:** Automated renaming saves hours but writes its mistakes into every later citation, so verify a sample before renaming in bulk.

---

## **13 Content**

**Metadata Extraction at Scale: Reading Dates, Archival Stamps, and Catalog Numbers**

Documents collect marks from their custodians: accession stamps, shelfmarks, a cataloguer's pencilled date, an owner's initials. These belong in your header, under provenance.

A multimodal model can be asked directly: *list every stamp, number, and pencilled note in the margins of this image, with its position.* That is a good use of the technology, because finding these marks is tedious and recognizing them is easy.

Then the Lesson 2.3 rule applies without modification. A model reading a faint stamp will produce something plausible. An accession number that is right in form and wrong in one digit looks exactly like a correct one, and no schema will object.

Transcribe from the image yourself before you write it into the header, and check the number against the institution's own catalogue.

**Vocabulary.** *Provenance* — the record of a document's ownership and custody. *Accession number* — the identifier an institution assigns on acquiring an item.

**Takeaway:** AI is good at finding marginal stamps and shelfmarks and unreliable at reading them exactly, so verify every extracted identifier against the catalogue.

---

## **14 Content**

**Automated Quality Control: Detecting Blur, Glare, Incomplete Scans, and Cropping Errors**

The worst moment in digitization is discovering months later that a page is out of focus — after the archive has closed the file or the trip is over.

Automatic checks can catch this at the time. Software can measure whether a frame is sharp, detect blown-out patches where a lamp reflected off the surface, check that all four edges of the page are inside the frame, and confirm the colour target was photographed for that session.

None of this is clever, and that is the point: it is a checklist run by a machine while you still have the object in front of you.

Even for a single page, ask the same four questions before you leave: is it sharp, is there glare, are the edges in, is there a scale reference.

**Vocabulary.** *Quality control* — checking that captures meet standard before work continues. *Glare* — a bright reflection obscuring the surface.

**Takeaway:** Automated checks for focus, glare, edges, and reference targets catch failures while the object is still accessible.

---

## **15 Content**

**AI-Assisted Super-Resolution and Denoising: Opportunities and Hallucination Risks**

**Super-resolution** enlarges a small image and fills in detail that was never captured. The results look remarkable, and for document scholarship the technique is dangerous.

The model is not recovering what was on the page. It is generating what pixels of that kind usually look like. On an ambiguous stroke it will produce something definite — turning a speck of foxing into a clean accent, or a blot into a comma.

That is fabricated evidence, and it is worse than a blurry image, because the blur is honest about its uncertainty.

The rule: never apply super-resolution to a master or to anything you transcribe from. If you use it to make a display image, say so plainly, and keep the original image available beside it.

**Vocabulary.** *Super-resolution* — enlarging an image by generating plausible extra detail. *Hallucination* — confident output that has no basis in the source.

**Takeaway:** Super-resolution invents detail rather than recovering it, so it must never inform transcription and must be disclosed wherever it is shown.

---

## **16 Content**

**Automated Contrast and Ink Recovery: Deep Learning for Faded and Stained Inks**

Sometimes the deterministic tools are not enough. When faded ink and a stain are the same brightness, `-level` cannot separate them: any adjustment hits both.

Trained models can do better, because they have learned what ink looks like as opposed to what damage looks like, and can enhance one without the other.

Two conditions make this legitimate:

- Keep the enhanced version as a **separate layer or file**, never overwriting the original photograph.
- Let the reader switch between them, so the evidence and the interpretation are both visible.

State the difference to yourself clearly: contrast stretching redistributes brightness that was recorded; a trained model produces an image where recorded and inferred detail are mixed together and cannot be told apart afterwards.

**Vocabulary.** *Ink recovery* — enhancing faded writing to make it legible. *Overlay* — an additional layer shown on top of the original image.

**Takeaway:** Model-based ink recovery may see through stains that arithmetic cannot, but it belongs in a separate, labelled layer beside the untouched original.

---

## **17 Content**

**Verso Show-Through and Bleed-Through Removal via Neural Image Separation**

You met bleed-through in Lesson 3.2 and removed it with evidence: photograph the back, flip it, subtract.

Models can do the same job without the second photograph, having learned what show-through looks like. That is convenient, and it is a weaker claim. The deterministic method proves where the ghost came from; the model infers it.

When you have both sides, prefer the deterministic route. When you have only one — a letter photographed from the front alone, a sheet mounted in a frame — the model may be your only option, and then the result should be labelled as a reading aid rather than a facsimile.

There is also a reason to leave ghosts alone. Visible show-through is evidence about the paper's thinness and the ink's acidity, and a perfectly clean image quietly deletes it.

**Vocabulary.** *Show-through* — writing on the reverse visible through a thin leaf. *Source separation* — splitting a mixed image into its underlying parts.

**Takeaway:** Use the two-sided deterministic method where you can, because removing ghosts from a single image is inference, and ghosts are themselves evidence.

---

## **18 Content**

**Aligning Images with Transcriptions: The Text-Image Alignment Problem**

Here is the problem this whole module has been building toward. You have an image. You have a transcription. Which pixels correspond to which words?

Done by hand, this means creating a zone for every line, then pasting its identifier into the text. For one page, tedious. For a manuscript, prohibitive.

**Forced alignment** solves it in a way worth understanding, because it is the most trustworthy AI method in the lesson. The model reads the image and produces its best guess at the text. But it is also *given* the correct transcription — yours. So it never has to decide what a word says. It only has to decide **where** on the page that known word sits.

Removing the guesswork about content is exactly what makes the result reliable. The machine is answering a question it is good at, while you keep the one you are good at.

**Vocabulary.** *Text-image alignment* — matching transcribed text to its position on the page. *Forced alignment* — alignment that is given the correct text in advance.

**Takeaway:** Forced alignment is reliable precisely because the transcription is supplied: the model locates known words instead of guessing unknown ones.

---

## **19 Content**

**Automated Insertion of `<facsimile>`, `<surface>`, and `<graphic>` in TEI XML**

Once coordinates exist, building the XML is mechanical, and mechanical work should be scripted.

A script reads each image's real dimensions, writes a `<surface>` with those as `lrx` and `lry`, adds a `<graphic>` pointing at the file, adds a `<zone>` for each detected region with a predictable identifier, and inserts the whole block between `</teiHeader>` and `<text>`.

You have already run a small version of this: `make_surface.py` does steps one through three. Nothing in this section is beyond what you did on Wednesday; it is the same job with more zones.

Note where the AI actually sits in that pipeline. The dimensions are measured, the XML is assembled by rule, and only the zone coordinates come from a model. Knowing which parts are certain and which are proposals is what lets you check the right things.

**Vocabulary.** *Script* — a saved sequence of commands. *xml:id* — the unique name that lets other elements point at this one.

**Takeaway:** Assembling the facsimile block is scripted and deterministic; only the zone coordinates are predictions, and that is where checking belongs.

---

## **20 Content**

**Linking Text Elements to Image Zones: Automating `@facs` and `@corresp`**

The last step is the link. `@facs` on a `<pb>`, `<lb>`, `<p>`, or `<div>` points at a zone; `@corresp` points the other way, or ties commentary to a region.

When alignment has matched line to zone, a script can insert every pointer at once. The result is the behaviour readers expect from a digital edition: click a line of the transcription and the corresponding strokes highlight on the image.

One warning carried over from Wednesday. The schema checks that `@facs` is a well-formed value. It does **not** check that the thing it points to exists. A whole file of pointers aiming at identifiers that were renamed will validate cleanly and highlight nothing.

Test by using it: open the edition, click a few lines, and see whether the right region lights up.

**Vocabulary.** *Pointer* — an attribute referring to another element by its id. *Dangling pointer* — a reference to something that does not exist.

**Takeaway:** Scripts can insert every `@facs` pointer at once, but only clicking through the result proves the pointers land where they should.

---

## **21 Content**

**Multi-Witness Alignment: Cross-Referencing Manuscript Variants**

Many works survive in more than one copy, and comparing copies is the heart of textual criticism.

Dickinson is a clear case: she made multiple copies of poems, sending one and keeping another, with words and line breaks differing between them. Jay's project sits directly on this.

Alignment tools can line up two transcriptions and show where they diverge, and a IIIF viewer can put the two images side by side with synchronized zoom, so you see the variant in both hands at once.

What the software gives you is a list of differences. What it cannot give you is their meaning — whether a change is a correction, a revision for a particular reader, or a copying slip. Module 7 takes up that question properly; for now, notice that alignment is a finding aid, not an argument.

**Vocabulary.** *Witness* — one surviving copy of a text. *Collation* — systematic comparison of witnesses to find differences.

**Takeaway:** Alignment tools find where witnesses differ; deciding what a difference means remains the editor's work.

---

## **22 Content**

**IIIF Annotation Generation: Producing Web Annotation Data Model JSON-LD with AI**

TEI is not the only way to attach text to a region. IIIF uses **annotations**: small records saying *this text belongs on this part of this Canvas*.

An annotation has three parts — why it exists (transcription, comment), what it says, and where it points, using a coordinate fragment such as `#xywh=400,600,1200,80`.

The shape should look familiar: an annotation is a zone plus content, in a different notation. A pipeline that produces TEI zones can emit IIIF annotations from the same coordinates.

The advantage is reach. Annotations in this standard form can be opened in any IIIF viewer, and other scholars can layer their own onto your images without touching your files.

**Vocabulary.** *Annotation* — a record linking content to a region of an image. *Media fragment* — the coordinate part of an address, such as `#xywh=`.

**Takeaway:** IIIF annotations express the same coordinates as TEI zones in a form any viewer can read, so one pipeline can publish both.

---

## **23 Content**

**Fine-Tuning Vision Models on Historical Hands and Document Types**

When a general model fails on your document — as it will on Maud Lewis's hand or on 18th-century French typography with its long *s* — you have a better option than giving up.

**Fine-tuning** takes a model that already understands pages in general and shows it a small sample of *your* material, corrected by you. Ten to twenty carefully checked pages is a realistic amount, not thousands.

The logic is worth noticing, because it inverts the usual worry about AI. The model becomes accurate on your document precisely because a human produced perfect examples first. Your manual work is not replaced by the model; it is what the model is built from.

You will not fine-tune anything in this course. You should recognize the option, and recognize that the ground truth it needs is the kind of work you are already doing.

**Vocabulary.** *Fine-tuning* — adapting a trained model with additional examples. *Ground truth* — verified correct data used for training or evaluation.

**Takeaway:** Fine-tuning adapts a general model using a few pages you corrected yourself, so manual accuracy is the foundation of machine accuracy.

---

## **24 Content**

**Active Learning and Human-in-the-Loop: Correcting AI Predictions Iteratively**

The productive way to use these tools is a loop rather than a handoff.

The model processes a batch and reports which results it is least sure about. You review those first, correcting what is wrong. Your corrections go back in, and the next batch is better.

This arrangement is usually called **human-in-the-loop**, and it puts your attention where it is worth most: on the hard cases, rather than spread evenly over pages that were already right.

It also produces something valuable as a by-product — a record of what the machine got wrong and how often. That record is what lets you say, in a published edition, how the material was processed and how far the automation was trusted.

**Vocabulary.** *Human-in-the-loop* — a workflow where a person reviews and corrects machine output. *Batch* — a group of items processed together.

**Takeaway:** Review the model's least confident output first, feed corrections back, and keep the record of what it got wrong.

---

## **25 Content**

**Confidence Scoring and Error Detection: When Does the Vision Model Fail?**

Most models report a **confidence** number with each prediction. It is useful and it is not a probability of being right — a model can be confidently wrong, and often is in the same few situations:

- **Gutter shadows** in bound volumes read as dark text blocks.
- **Stains and foxing** attract zones around blank paper.
- **Curving lines** on warped or cockled leaves make a baseline wander off mid-line.
- **Faint marginal notes** are missed entirely, which is the dangerous failure, because a missing zone looks like nothing at all.

A practical habit: set a threshold, send everything below it for review, and mark uncertain results in your markup. TEI provides `@cert` for exactly this — a way of saying in the file itself that a value is less than certain.

**Vocabulary.** *Confidence score* — the model's own rating of how sure it is. *False positive* — a detection of something that is not there.

**Takeaway:** Confidence scores triage review but do not guarantee correctness; record uncertainty in the markup with `@cert` rather than hiding it.

---

## **26 Content**

**Ethical and Scholarly Integrity: The Risk of Generative Hallucination in Archival Images**

One line matters more than anything else in this lesson: **never publish invented evidence as evidence.**

Generative tools can fill a tear, complete a missing word, or smooth a damaged edge. The results are convincing. They are also fabrication, and publishing them as a facsimile is falsification, whatever the intent.

Three working rules:

- Do not generate missing content in an image that represents a document.
- Keep every enhancement as a labelled derivative, with the original always available.
- Disclose what you used. The `<encodingDesc>` in your header is where the method statement belongs: which tool, which version, which settings.

Note the asymmetry that makes this urgent. A reader can check a transcription against the image. They cannot check the image against the object — most will never see it. The image is where their trust ends up, which is why altering it silently is the most serious thing you can do.

**Vocabulary.** *Generative* — producing new content rather than describing existing content. *Derivative* — a processed copy, as opposed to the master.

**Takeaway:** Never generate missing content in a facsimile; enhancements are labelled derivatives and the method belongs in the header.

---

## **27 Content**

**The Black Box Problem: Explainability and Reproducibility in AI Imaging Workflows**

Wednesday's command can be rerun in ten years and give identical pixels. That is not true here.

Two reasons. A model with millions of internal parameters cannot explain why it drew a zone where it did — the **black box** problem. And the model itself may not survive: commercial services are updated and retired, and the same request can return different results next year, or an error.

For work meant to last, this suggests some preferences: favour models whose weights you can download and keep, record the exact version and settings you used, and store the model's output in your repository so the result survives even if the tool does not.

The deeper point is about what you publish. Publish the *output* you checked, not a promise that a service will still be there.

**Vocabulary.** *Black box* — a system whose internal reasoning cannot be inspected. *Model weights* — the trained numbers that make a model work.

**Takeaway:** AI results are not reliably reproducible, so record versions and settings and keep the checked output rather than depending on a service.

---

## **28 Content**

**Integrating AI Pipelines with Open-Source Deterministic Tools**

In practice the three steps of this week are not rivals; they run in sequence.

Deterministic tools go first: straighten, crop, correct colour. Models perform better on clean, consistent input, and these corrections are recorded and reversible.

The model goes second, proposing regions, lines, and alignments.

Deterministic tools go last: the accepted coordinates are used to cut derivatives and build the tiles a viewer serves.

Notice that the AI is a middle step, bracketed on both sides by operations you can verify — and that the model's proposals only become part of the edition once you have accepted them.

**Vocabulary.** *Pipeline* — a chain of processing steps. *Derivative* — an image generated from the master for a particular use.

**Takeaway:** In production, deterministic processing brackets the AI step on both sides, and its proposals enter the edition only after review.

---

## **29 Content**

**Building an End-to-End AI Imaging Pipeline: From Raw Scans to Validated TEI/IIIF**

The whole module, as one sequence:

1. **Capture and check** — photograph or download, and verify focus, glare, edges, and reference targets.
2. **Normalize** — deskew, crop, colour-correct with recorded commands; keep the master untouched.
3. **Organize** — group and rename files predictably, spot-checking the names.
4. **Analyse layout** — detect regions, lines, and non-textual features.
5. **Align** — match your transcription to the page with forced alignment.
6. **Build the TEI** — assemble `<facsimile>`, `<surface>`, `<zone>`, and insert `@facs` pointers; validate.
7. **Publish derivatives** — tiles, a IIIF service, annotations.
8. **Review** — click through the edition and confirm the links land correctly.

Steps 1, 2, 6, and 7 are deterministic. Steps 4 and 5 are proposals. Steps 3 and 8 are yours. Knowing which is which is the skill this module was teaching.

**Vocabulary.** *End-to-end* — covering the whole process from source to publication.

**Takeaway:** In the full pipeline only layout analysis and alignment are AI proposals; the rest is measured, scripted, or editorial.

---

## **30 Content**

**The Methodological Triad: Synthesizing Manual, Deterministic, and AI-Assisted Imaging**

Three lessons, three relationships to the same page.

**Manual** (3.1) taught you what a facsimile *is*: surfaces, zones, coordinates, and the physical facts of photographing an object without damaging it. Slow, and the source of your standards.

**Deterministic** (3.2) gave you tools that measure and transform exactly, and can be rerun by anyone. Fast, verifiable, and blind to meaning.

**AI** (3.3) recognizes meaning at speed, and cannot prove anything. It proposes; you dispose.

The order matters, and it is the same order the course repeats every week. You do it by hand to learn what correct looks like. You automate to work at scale. You bring in the machine last, because only now can you tell when it is wrong.

Module 4 applies the same three steps to transcription, where the stakes are higher: there, a confident machine error becomes words in your edition.

**Vocabulary.** *Methodological triad* — the course's three-step manual, deterministic, and AI-assisted cycle.

**Takeaway:** Manual work sets the standard, deterministic tools scale it, and AI proposes at speed — which is only safe in that order.
