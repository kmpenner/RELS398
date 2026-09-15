# Lesson 3.2 — Deterministic Computer-Assisted Imaging: IIIF, Image Processing, and File Storage

*RELS 398 / ENGL 398 · Topic 3: IIIF Imaging · Meeting #7 (Wed Sep 16)*

***Step 2 of the three-step cycle: deterministic.** Yesterday you measured a page by eye and typed the numbers yourself. Today the machine measures instead. Deterministic means the same input always gives the same output — no guessing, and you can check it.*

---

## **01 Content**

**The IIIF Vision: Solving the Image Silo Problem**

Libraries spent decades digitizing manuscripts, and each one built its own website to show them. Every site had its own viewer, its own zoom buttons, its own file formats. You could look at an image, but only in that library's window.

Scholars call this an **image silo**: the pictures are online, but locked to one portal. To compare a Dickinson poem at Harvard with one at Amherst, you opened two windows that could not talk to each other, or downloaded huge files onto your laptop.

IIIF (the International Image Interoperability Framework, said "triple-eye-eff") fixes this by agreeing on shared rules. Any library that follows them can be read by any viewer that follows them.

**Vocabulary.** *IIIF* — shared rules for publishing images so any compliant viewer can read them. *Image silo* — digitized material viewable only through one institution's own website.

**Takeaway:** IIIF replaces one-library-one-viewer silos with shared rules, so images from different institutions can be used in the same tool.

---

## **02 Content**

**The IIIF Image API: The Canonical Request URI Syntax**

The first half of IIIF is the **Image API**. It turns a web address into a request for exactly the piece of the image you want.

Every request follows the same pattern:

`{server}/{identifier}/{region}/{size}/{rotation}/{quality}.{format}`

Reading it left to right: *region* is which part of the image (`full`, or `x,y,w,h` in pixels), *size* is how big to send it back (`max`, or `600,` for 600 pixels wide), *rotation* is degrees clockwise, *quality* is `default`, `gray`, or `bitonal`, and *format* is usually `jpg`.

So `.../full/1000,/0/default.jpg` means the whole page, 1000 pixels wide, unrotated, in colour. Change one word and you get a different picture — no software required.

**Vocabulary.** *API* — an agreed way for one program to ask another for something. *Region* — the rectangle of the source image being requested.

**Takeaway:** A IIIF image address is a readable recipe: region, size, rotation, quality, format — so you can crop and resize a page by editing a URL.

---

## **03 Content**

**Deep Zoom and Image Tiling**

A good photograph of a large broadside can be 12,000 pixels across and hundreds of megabytes. No browser can load that before showing you anything.

IIIF servers solve it by cutting each image into **tiles**: small squares, typically 256 or 512 pixels, prepared in advance at several sizes. Together those sizes form a pyramid, with a small version at the top and the full-resolution one at the bottom.

When you zoom, the viewer works out which tiles are on your screen right now and asks only for those. Panning fetches a few more. You feel like you are moving around one enormous photograph, but you are downloading a handful of small ones.

**Vocabulary.** *Tile* — one small square piece of a large image. *Image pyramid* — the same image stored at several resolutions for fast zooming.

**Takeaway:** Deep zoom works by sending only the small tiles currently on screen, which is why a gigantic manuscript image opens instantly.

---

## **04 Content**

**The Image Information Document (`info.json`)**

Before a viewer can request tiles, it needs to know what it is dealing with. Every IIIF image service answers that at one address: add `/info.json` to the image's identifier.

What comes back is a short text file listing the image's real `width` and `height`, the tile size the server prefers, and which ready-made sizes it offers.

This matters for your own work. The JPEG you downloaded may be 1,000 pixels wide while the master behind it is 8,000. Your TEI `<surface>` coordinates describe **one specific image**, so you need to know which one you measured. `info.json` is where you check.

```
https://example.org/iiif/3/manuscript_f01r/info.json
```

**Vocabulary.** *info.json* — the small file describing an image's dimensions and capabilities. *Master* — the highest-resolution version an institution holds.

**Takeaway:** Fetch `info.json` to learn an image's true dimensions, and record which version your coordinates actually describe.

---

## **05 Content**

**The IIIF Presentation API: The Shared Canvas Model**

The second half of IIIF is the **Presentation API**, and it handles structure: a book has pages in an order, a letter has a front and a back.

Its central idea is the **Canvas**. A Canvas is not a picture. It is an empty rectangle with a width and a height, standing for one physical surface — one page, one sheet, one side.

Pictures are then attached to that Canvas. That sounds like a technicality, but it buys something real: an ordinary photograph, an ultraviolet photograph, and a transcription can all be attached to the *same* Canvas, because they all describe the same physical surface.

The idea should feel familiar. It is the same move TEI makes when it separates `<surface>` from the `<graphic>` inside it.

**Vocabulary.** *Canvas* — an abstract rectangle standing for one physical surface, to which images and text are attached.

**Takeaway:** A IIIF Canvas represents the physical surface, not a file, so several images and a transcription can all be anchored to the same page.

---

## **06 Content**

**Anatomy of a IIIF Manifest: Structure and JSON-LD**

A **Manifest** is the file that packages an object for a viewer: its metadata, its Canvases, and the images attached to them. When someone gives you "a IIIF link", it is almost always a Manifest URL.

It is written in JSON, a format of labelled values in braces:

```json
{
  "type": "Manifest",
  "label": { "en": [ "Emily Dickinson, MS Am 1118.3 (338)" ] },
  "items": [
    { "type": "Canvas", "label": { "en": [ "Recto" ] },
      "width": 3200, "height": 4800 }
  ]
}
```

You will not be writing manifests from scratch. You should be able to open one and read it: what is this object, how many Canvases does it have, what did the institution choose to tell you about it, and what did it leave out.

**Vocabulary.** *Manifest* — the file describing one object: its metadata, its Canvases, and their images. *JSON* — a plain-text format of labelled values.

**Takeaway:** A Manifest is the package a viewer reads, and being able to open one and see what an institution published (and omitted) is a research skill.

---

## **07 Content**

**Multi-Page Structures: Sequences, Ranges, and Structures**

A one-sheet decree needs one or two Canvases. A bound register needs hundreds, and nobody wants to scroll through them.

IIIF handles this with **Ranges**, listed under a manifest's `structures`. A Range is a named group of Canvases: "Chapter 4", "Index", "Quire 2". Ranges can sit inside other Ranges, which is how a viewer builds the clickable table of contents down the side of the screen.

Ranges can also record physical structure rather than contents — which leaves belong to which gathering, where a leaf was cut out, which pages were separated when the volume was rebound.

That distinction is worth holding onto: how a document is *built* and how it is *organized* are two different descriptions of it, and IIIF keeps both.

**Vocabulary.** *Range* — a named group of Canvases. *Quire (gathering)* — sheets folded and sewn together as one unit of a book.

**Takeaway:** Ranges group Canvases into a table of contents or into physical gatherings, letting a manifest record both how a book reads and how it was made.

---

## **08 Content**

**Interoperable Juxtaposition: Comparing Witnesses in Mirador**

**Mirador** is a free viewer that shows several IIIF objects side by side. You paste in manifest URLs, and each opens in its own panel.

The point is comparison. Two copies of the same printed decree, held in different archives, can sit next to each other on your screen. Lock the panels together and zooming one zooms the other to the same spot.

For a textual scholar this replaces travel. Comparing two witnesses used to mean two trips, or ordering photographs and waiting weeks.

It only works when both institutions publish IIIF. When one does not, you are back to screenshots and guesswork — which is itself a finding worth recording about your own document.

**Vocabulary.** *Mirador* — an open-source viewer for comparing IIIF objects side by side. *Witness* — one surviving copy of a text.

**Takeaway:** Mirador puts witnesses from different institutions side by side with synchronized zoom, but only when each institution publishes IIIF.

---

## **09 Content**

**The Open-Source Imperative in Scholarly Imaging**

From here on this lesson is about tools you run yourself. They are all open source, and that is a scholarly choice rather than a budget one.

Four reasons:

- **You can check it.** If your edition says an image was sharpened, another scholar must be able to run the same operation and get the same pixels. A secret algorithm cannot be verified.
- **It lasts.** Editions outlive software companies, licence terms, and subscriptions.
- **It scripts.** Three hundred pages cannot be adjusted by hand without drift.
- **Anyone can run it.** No subscription stands between a student and the evidence.

The working set is small: **GIMP** for looking and experimenting, **ImageMagick** for scripted batches, **libvips** for very large files.

**Vocabulary.** *Open source* — software whose code anyone may read, run, and modify. *Batch* — running the same operation over many files at once.

**Takeaway:** Scholarly imaging uses open-source tools because a claim about an image is only verifiable if someone else can rerun the exact operation.

---

## **10 Content**

**Interactive Editing with GIMP: Manual Adjustments and Layer Inspection**

**GIMP** is a free image editor, and in this course it is the place you *look* before you script. Three things it is good for:

**Curves** (`Colors > Curves`) let you drag a line to darken faint ink and lighten stained paper, watching the effect live. When it looks right, you note the numbers and put them in a script.

**Channels** show the red, green, and blue layers separately. Faded iron-gall ink is often far more legible in the blue channel alone than in the full-colour image. This is free evidence, and it costs one click.

**Layer masks** let you try a change on part of an image without destroying the original underneath.

Use GIMP to decide *what* to do. Use a script to actually do it, so the operation is recorded.

**Vocabulary.** *Channel* — the red, green, or blue component of a colour image. *Layer mask* — a stencil controlling where an edit applies.

**Takeaway:** GIMP is for exploring an image and finding the right settings; the settings you find then go into a script that can be rerun and audited.

---

## **11 Content**

**Scripting with ImageMagick: Command-Line Batch Automation**

**ImageMagick** does image editing from the command line. One command, typed once, can be applied to one file or three hundred.

```bash
magick input.tif -quality 85 output.jpg
```

Operations can be chained, and they run in the order written:

```bash
magick page.tif -deskew 40% -level 12%,88% -colorspace Gray out.tif
```

That single line straightens the page, stretches the contrast, and converts to grey.

The advantage over clicking is not speed. It is that the command **is** the record. Paste it into your notes and anyone can reproduce your image exactly, including you in December.

**Vocabulary.** *Command line* — typing instructions to the computer as text. *Chaining* — combining several operations in one command.

**Takeaway:** An ImageMagick command applies identical treatment to every page and doubles as the written record of what was done.

---

## **12 Content**

**High-Performance Processing with libvips: Memory Efficiency and Tiling**

ImageMagick usually loads a whole image into memory. For a 100-megapixel photograph of an oversize map, that can exhaust a laptop.

**libvips** works differently: it streams the image through in narrow strips, so it needs only a fraction of the memory and uses all your processor cores. On very large files it is several times faster.

Its main job here is making the tile pyramids from section 3:

```bash
vips dzsave master.tif output_zoom --tile-size 512
```

You are unlikely to need libvips for a single page. Know that it exists, and that "my computer ran out of memory" has an answer.

**Vocabulary.** *Streaming* — processing an image in small pieces instead of loading it whole. *Pyramid* — the multi-resolution form used for deep zoom.

**Takeaway:** libvips streams large images in strips, so gigapixel files can be processed and tiled on ordinary hardware.

---

## **13 Content**

**Reproducible Processing: Logging Parameters and Scripting Pipelines**

Here is the rule that makes the rest of this lesson scholarship rather than photo editing: **never change your original, and always write down what you did.**

In practice that means three habits:

1. **Keep the original untouched.** Downloaded or camera files go in one folder and are never edited in place. Every operation writes a new file.
2. **Put the commands in your repository.** A short shell script next to your TEI is better than a memory of which sliders you dragged.
3. **Record the settings with the output.** Tool, version, and exact numbers.

You already know why: this is the same argument as your Git commit history from Module 1. Work you cannot retrace is work another scholar cannot check.

**Vocabulary.** *Reproducible* — able to be redone by someone else with the same result. *Pipeline* — a fixed sequence of processing steps.

**Takeaway:** Keep originals unedited and commit the commands you ran, so every published image can be traced back to the file it came from.

---

## **14 Content**

**Coordinate-Based Cropping: Isolating Folios and Zones**

A photograph of a page usually includes things that are not the page: the table, a clip, a ruler. Cropping removes them.

ImageMagick crops by numbers, not by dragging:

```bash
magick master.tif -crop 5100x7000+450+600 +repage cropped.tif
```

That reads: take a rectangle 5100 wide and 7000 tall, starting 450 pixels from the left and 600 from the top.

`+repage` matters. Without it the file remembers its old size, and viewers can place your cropped image oddly.

Notice that these are the same four numbers as your TEI zone, arranged differently: tools take **x, y, width, height**, while TEI takes **corners**. Converting between them is where mistakes happen.

**Vocabulary.** *Crop* — cut a rectangle out of an image. *Offset* — how far the rectangle starts from the top-left corner.

**Takeaway:** Cropping is specified as x, y, width, height — convert carefully, because TEI's `ulx/uly/lrx/lry` are corners instead.

---

## **15 Content**

**Deskewing and Geometric Alignment: Rectifying Rotational Drift**

Pages are rarely photographed perfectly straight. A degree or two of tilt is called **skew**.

Your eye compensates automatically. Software does not. Skewed lines wander across the rows a computer is trying to read, and a rectangular zone can no longer sit tightly around a tilted column of text.

ImageMagick can measure and correct it:

```bash
magick crooked.tif -deskew 40% straight.tif
```

One caution: rotating an image by a fraction of a degree means every pixel has to be recalculated from its neighbours. Done once at high quality this is harmless. Done repeatedly, it softens fine pen strokes. Straighten once, from the original.

**Vocabulary.** *Skew* — unintended rotation of the page in the image. *Interpolation* — calculating new pixel values when an image is rotated or resized.

**Takeaway:** Deskewing straightens a tilted page so lines and zones align, but rotate once from the original, because each rotation costs sharpness.

---

## **16 Content**

**Contrast Adjustment and Dynamic Range Optimization**

Old documents are often low contrast: ink has faded to brown, paper has darkened to beige, and the two are closer together than they once were.

Contrast adjustment pulls them apart. The tool for thinking about it is the **histogram**, a chart of how many pixels fall at each brightness. A faded page shows one narrow hump in the middle: no true blacks, no true whites.

```bash
magick page.tif -level 15%,85%,1.2 better.tif
```

Anything below 15% brightness becomes black, anything above 85% becomes white, and the middle is adjusted by 1.2.

The danger is **clipping**: push too far and faint pen strokes vanish into solid black while watermarks disappear into white. You have not enhanced the evidence, you have deleted it.

**Vocabulary.** *Histogram* — a chart of how many pixels have each brightness. *Clipping* — pushing tones to pure black or white, destroying detail.

**Takeaway:** Contrast stretching separates faded ink from darkened paper, but over-adjusting deletes the faintest evidence entirely.

---

## **17 Content**

**White Balance and Color Calibration: Applying ICC Profiles and Neutral Ramps**

Photograph the same page under a desk lamp and by a window and you get two different colours. The lamp adds yellow; daylight adds blue.

This is a scholarly problem, not an aesthetic one. If your image is yellow, nobody can tell whether the paper aged or your lamp was warm.

**White balance** fixes it by anchoring to something known to be neutral. Photograph a grey card next to the page, then tell the software that the card is grey; everything else shifts with it.

An **ICC profile** goes further, correcting a specific camera's colour bias using a printed target of known patches. This is why section 3.1 asked for a colour reference in the frame: it is what makes the correction possible afterwards.

**Vocabulary.** *White balance* — correcting a colour cast so neutral things look neutral. *ICC profile* — a file describing a device's colour behaviour.

**Takeaway:** Photograph a grey or colour reference with the page, so later viewers can tell ageing from lighting.

---

## **18 Content**

**Spatial Filtering: Sharpening and Unsharp Masking**

Every lens softens edges slightly. Careful sharpening restores definition, which matters when you are deciding whether a mark is a punctuation point or a blot.

The standard method is confusingly named **unsharp masking**: the software blurs a copy, compares it to the original to find the edges, and strengthens those edges.

```bash
magick page.tif -unsharp 0x1.0+1.0+0.05 sharper.tif
```

The numbers control how wide an edge is affected, how strong the effect is, and how much difference is needed before anything is sharpened at all — that last one keeps the paper grain from being sharpened into speckles.

Over-sharpening leaves bright halos around strokes and thickens letters. For palaeography that is damage: it changes what the hand looks like.

**Vocabulary.** *Unsharp masking* — sharpening by detecting edges and boosting their contrast. *Halo* — a bright fringe left by over-sharpening.

**Takeaway:** Modest sharpening clarifies letterforms; heavy sharpening thickens strokes and misrepresents the hand.

---

## **19 Content**

**Noise Reduction and Defect Masking**

Noise comes from two places: the camera (grain in dim reading rooms) and the object (dust, foxing, fibres).

Removing it is tempting and risky. A filter strong enough to erase specks is usually strong enough to erase a faint accent, a hairline stroke, or a point of punctuation.

Choose the gentlest tool that works:

- A **median filter** replaces each pixel with the middle value of its neighbours. It removes isolated dust specks and leaves lines alone.
- **Gaussian blur** smooths everything, edges included. Rarely right for text.

```bash
magick dusty.tif -statistic Median 3x3 clean.tif
```

The rule: never let the filter be bigger than the smallest mark that carries meaning.

**Vocabulary.** *Noise* — unwanted speckle from the sensor or the object. *Median filter* — a filter that removes specks while preserving edges.

**Takeaway:** Use the gentlest possible noise filter, because anything that removes dust can also remove the faintest real marks.

---

## **20 Content**

**Thresholding and Binarization: From Grayscale to Pure Black and White**

For reading, you want the full-colour image. For handing a page to transcription software, you often want **binarization**: every pixel forced to black (ink) or white (background).

Doing this well is harder than it sounds. The simple approach picks one brightness cut-off for the whole page, which fails badly on real documents: a shadowed corner turns solid black while faint text in a bright area disappears.

The better approach decides **locally**, choosing a cut-off for each small neighbourhood based on what is around it. A stained corner is judged against its own surroundings rather than against the whole page.

```bash
magick page.tif -colorspace Gray -negate -lat 25x25+10% -negate bw.png
```

Keep the grey version. Binarization always throws information away.

**Vocabulary.** *Binarization* — converting an image to pure black and white. *Local threshold* — a cut-off calculated separately for each small area.

**Takeaway:** Local thresholding handles stains and shadows that a single whole-page cut-off ruins, but always keep the greyscale original.

---

## **21 Content**

**Masking and Layer Compositing: Isolating Text from Background**

Some damage cannot be filtered away. The common case is **bleed-through**: ink from the back of a thin leaf showing faintly on the front, producing mirror-image ghost text.

The deterministic remedy uses the back of the leaf as evidence. Photograph both sides, flip the back horizontally so it lines up with the front, and use it as a **mask** — a stencil marking where the ghosts must be. Combining the two mathematically cancels the ghosts while leaving the real text.

```bash
magick recto.tif \( verso_flipped.tif -colorspace Gray \) \
  -compose Screen -composite cleaned.tif
```

The important word is *evidence*. Nothing is invented here. The ghost is removed because a second photograph proves where it came from — which is exactly the difference between this and the AI methods on Friday.

**Vocabulary.** *Bleed-through* — ink from the reverse side showing through the leaf. *Compositing* — combining images mathematically.

**Takeaway:** Bleed-through can be cancelled using a photograph of the other side, removing ghosts with evidence rather than guesswork.

---

## **22 Content**

**The Taxonomy of Digital Image Formats**

The rest of this lesson is about file formats, because choosing the wrong one destroys evidence permanently.

Four properties tell you what a format can do:

- **Bit depth** — how finely tones are recorded. 8-bit gives 256 levels per colour; 16-bit gives tens of thousands, and holds detail in faint ink and dark parchment.
- **Colour space** — which range of colours the numbers refer to. `sRGB` is the safe choice for the web.
- **Compression** — *lossless* shrinks the file and gives every pixel back exactly; *lossy* makes it much smaller by discarding detail forever.
- **Metadata** — whether the file can carry camera settings, dates, and rights inside it.

One principle covers most decisions: **preserve in one format, publish in another.**

**Vocabulary.** *Bit depth* — how many tonal levels a file can store. *Lossless / lossy* — compression that keeps every pixel, or discards some permanently.

**Takeaway:** Bit depth, colour space, compression, and metadata decide what a format can carry — preserve in one format and publish in another.

---

## **23 Content**

**TIFF: The Gold Standard for Archival Preservation**

**TIFF** is the format archives use for preservation masters, and national digitization standards require it.

Three reasons: its compression is lossless, so the file is identical to what came out of the camera; it supports 16-bit depth, holding gradations that 8-bit formats flatten; and it carries technical metadata inside the file.

The cost is size. A 16-bit TIFF of a large page can run to several hundred megabytes, which is why nobody serves TIFFs to the public. They sit in storage as the authoritative copy, and everything else — the JPEG on the website, the tiles in the viewer — is generated from them.

If you photograph your own document, keep a TIFF or the camera's raw file. Every later decision can be revisited from it.

**Vocabulary.** *Preservation master* — the authoritative high-quality file everything else is derived from. *Derivative* — a smaller copy made for delivery.

**Takeaway:** TIFF is the preservation master because it is lossless and deep-toned; derivatives for the web are generated from it, never the reverse.

---

## **24 Content**

**Pyramidal TIFF: The Foundation of Local IIIF Servers**

A plain TIFF is excellent for storage and useless for serving: to send one small tile, the server would have to open the whole file.

A **pyramidal TIFF** solves this by storing the image at several resolutions inside one file, each already cut into tiles. The server jumps straight to the tile it needs and sends it.

```bash
vips tiffsave master.tif pyramid.tif --tile --pyramid --compression deflate
```

This is what sits behind the IIIF servers from the start of the lesson. The sequence is worth remembering as a whole: photograph the page, keep a TIFF master, generate a pyramidal copy, let a IIIF server publish it, point your TEI `<facsimile>` at the result.

**Vocabulary.** *Pyramidal TIFF* — a TIFF holding several resolutions, pre-cut into tiles for fast serving.

**Takeaway:** Pyramidal TIFFs let a IIIF server deliver single tiles instantly, bridging archival storage and public zooming.

---

## **25 Content**

**JPEG: Discrete Cosine Transform and the Cost of Lossy Compression**

**JPEG** made photographs practical on the web by throwing data away — deliberately, and permanently.

It works by cutting the image into small blocks and describing each approximately, discarding the fine detail human eyes are least likely to miss. A 100 MB master becomes a 3 MB file that still looks fine.

Two consequences matter for scholarship:

- **The loss is permanent.** The discarded detail is gone; saving at higher quality later does not bring it back.
- **The loss accumulates.** Every open-edit-save cycle throws away more. Edit the TIFF, export a JPEG at the end.

JPEG is the right format for delivery and the wrong one for preservation.

**Vocabulary.** *Lossy compression* — permanently discarding detail to reduce file size. *Generation loss* — degradation accumulating over repeated saves.

**Takeaway:** JPEG is ideal for publishing and unacceptable as a master, because its discarded detail never comes back and repeated saving compounds the loss.

---

## **26 Content**

**PNG: Lossless Web Delivery and Alpha Transparency**

**PNG** sits between the two: compressed for the web, but lossless. Saving and re-saving costs nothing, which makes it the right choice for anything with hard edges — screenshots, diagrams, charts, and images with text.

Its distinctive feature is **transparency**. A PNG pixel can be fully transparent, fully opaque, or anywhere between, so non-rectangular things can be shown without a white box around them.

That is useful in editions: a wax seal or an irregular fragment can be displayed against any background, and semi-transparent overlays — for example colour-coding two scribal hands — can sit on top of a page image without hiding it.

PNGs are larger than JPEGs. Use them when edges or transparency matter.

**Vocabulary.** *Transparency (alpha)* — per-pixel information about how opaque a pixel is.

**Takeaway:** PNG is lossless and supports transparency, making it right for diagrams, overlays, and cut-out features like seals.

---

## **27 Content**

**GIF and Modern Web Formats: WebP, AVIF, and 8-Bit Palettes**

**GIF** is the oldest web image format and the wrong tool here. It allows only 256 colours in an image, so a photograph of a parchment leaf is reduced to a mottled approximation, and its transparency is all-or-nothing, leaving jagged edges.

Two newer formats do better. **WebP** and **AVIF** both compress substantially harder than JPEG at the same visible quality, support transparency, and come in lossless versions. On a busy image server that saves real bandwidth.

For your projects, the practical guidance is unchanged: master in TIFF, publish in JPEG or PNG, and treat WebP or AVIF as an optimization for later if a viewer supports them.

**Vocabulary.** *Palette* — a limited set of colours an image is restricted to.

**Takeaway:** GIF's 256-colour palette makes it unsuitable for documents; WebP and AVIF are the modern delivery formats, but JPEG and PNG remain the safe defaults.

---

## **28 Content**

**PDF as an Archival Wrapper: PDF/A Standards and Pitfalls**

Archives often hand you a **PDF** of a whole item. A PDF is not an image format; it is a container that can hold images, text, and fonts together.

Two traps follow. First, PDFs usually compress the images inside them with JPEG, so the page you extract may be markedly worse than the institution's master — always ask whether a better image exists. Second, many library PDFs carry a hidden text layer from automatic recognition, uncorrected. Copy text out of one and you may quietly inherit recognition errors into your edition.

**PDF/A** is the archival variant, which embeds its fonts and forbids anything that may stop working later. Use it for reports, not as a substitute for image masters.

**Vocabulary.** *Container format* — a file holding several kinds of content together. *Text layer* — invisible machine-read text stored behind a page image.

**Takeaway:** PDFs recompress images and often hide uncorrected recognition text, so never treat one as your image master or your transcription.

---

## **29 Content**

**The Conversion Pipeline: From Master TIFF to Tiled IIIF Pyramid**

Here is the whole lesson as one sequence, for a single page:

1. **Keep the master.** The camera file or the best download you are entitled to, stored unedited.
2. **Normalize, in one recorded command.** Deskew, crop, correct colour, sharpen modestly — written down as a command, not a series of clicks.
3. **Build the pyramid.** Produce the tiled version if you are serving the image yourself.
4. **Publish a derivative.** A JPEG sized for readers, or a IIIF service.
5. **Point your TEI at it.** Your `<surface>` coordinates must describe *the image you published* — because cropping and deskewing change every coordinate on the page.

Step 5 is the one students forget. Process the image first, then measure it.

**Vocabulary.** *Normalization* — the standard corrections applied to every image in a project.

**Takeaway:** Process first and measure second: cropping or deskewing an image invalidates every coordinate already written about it.

---

## **30 Content**

**The Deterministic Contract: Transparent Surrogates in the Digital Edition**

Everything in this lesson shares one property. Give these tools the same file and the same numbers and they return the same result, every time, on any machine. That is what **deterministic** means, and it is why this is Step 2 rather than Step 3.

It matters because your reader is looking at a photograph, not the object. They are trusting that what they see reflects the parchment and not your editing. That trust is only warranted if you can show your work: the original file kept, the commands recorded, the settings published.

Friday introduces tools that do not offer this. An AI can propose zones and redraw damaged letters, but it cannot tell you *why*, and running it twice may not give the same answer. Today is the baseline you will measure that against.

**Vocabulary.** *Deterministic* — always producing the same output from the same input. *Surrogate* — the digital stand-in for a physical object.

**Takeaway:** Deterministic tools let a reader verify that an image was corrected rather than altered, which is the standard Friday's AI methods will be measured against.
