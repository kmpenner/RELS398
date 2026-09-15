# Lesson 3.1 — IIIF Foundations: The Image API, the Presentation API, and the Canvas

*RELS 398 / ENGL 398 · Topic 3: IIIF Imaging · Meeting #6 (Tue Sep 15)*

*Infrastructure week — the three-step comparative cycle does not apply. This
week builds the imaging layer that Weeks 4 through 13 will transcribe from,
annotate, and publish against.*

---

## **01 Content**

**The Problem IIIF Was Built to Solve**

Before 2011, a scholar wanting to compare two manuscripts held in different
libraries faced a problem that had nothing to do with scholarship. Each
institution had digitized its holdings, and each had built its own viewer, its
own zoom mechanism, its own URL scheme, and its own download policy. The images
existed. They could not be brought together.

The situation is worth naming precisely, because the diagnosis determined the
cure. The failure was not a shortage of digitization — millions of folios had
been scanned. It was that each digitization project produced a **silo**: a
self-contained system whose images could be viewed only through the interface
its own institution had built. Comparing a Vatican folio with a British Library
folio meant opening two browser windows running two incompatible viewers, each
with its own controls, neither able to display the other's images.

The workaround was worse than the problem. Scholars downloaded enormous TIFF
files — gigabytes per manuscript — to compare them locally in image software.
This defeated most of the purpose of digitization: it reintroduced the
bottleneck of physical access in the form of bandwidth and storage, it produced
uncontrolled copies detached from their metadata, and it put the burden of
assembling a comparison entirely on the individual scholar (Griffin, 2023).

The International Image Interoperability Framework was designed to make the
image itself a networked, addressable resource rather than a file to be
transferred. Its central move is to standardize *how images are requested*, so
that any compliant viewer can display images from any compliant server.

**Vocabulary.** *Silo* — a system whose data can be accessed only through its own
interface. *Interoperability* — the capacity of independently built systems to
work together without prior coordination.

**Takeaway:** IIIF exists because digitization without shared
standards produced millions of images that could not be brought together.

---

## **02 Content**

**Interoperability as a Scholarly Requirement**

It would be easy to read the previous page as a technical convenience argument.
It is not. The inability to juxtapose witnesses is a *methodological* obstacle,
because juxtaposition is what textual criticism does.

Collation — the operation at the centre of this course, which you will perform
in Week 7 — means placing witnesses side by side and recording where they
differ. For most of the discipline's history this required physical
co-presence: the manuscripts in one room, or an editor travelling between
libraries with notes. The great critical editions of the nineteenth century were
built on exactly that labour, and their limitations reflect it.

Digitization promised to remove the constraint, and initially did not. An image
locked in an institutional viewer is available for reading but not for
juxtaposition, which means it supports consultation but not collation. The
scholar can look at it; they cannot work with it alongside anything else.

Codex Sinaiticus is the illustrative case. The manuscript is physically divided
across four institutions on three continents — the British Library, Leipzig
University Library, St Catherine's Monastery, and the National Library of
Russia — as a result of its nineteenth-century dispersal. Studying it as one
object formerly required either extensive travel or reliance on facsimiles.
Interoperable digital frameworks permit the virtual reunification of the
dispersed leaves, so that an integrated palaeographical analysis becomes
possible without the physical object ever being reassembled.

That is the claim worth holding onto: interoperability does not merely make
existing work more convenient, it makes some scholarly operations possible for
the first time.

**Takeaway:** Juxtaposing witnesses is the basic operation of
textual criticism, and image silos prevented it — so interoperability is a
methodological requirement, not a convenience.

---

## **03 Content**

**Two APIs, Two Different Jobs**

IIIF is not one specification but a family of them. Two are foundational, and
distinguishing their responsibilities is the key to understanding the whole
framework.

The **Image API** governs the delivery of a single image. It defines a URL syntax
by which a client requests a specific region of an image, at a specific size,
rotation, quality, and format, and receives exactly that (Griffin, 2023). It
knows nothing about books, pages, or order — its entire concern is: given this
image, return this part of it, thus transformed.

The **Presentation API** governs structure and meaning. It describes how images
assemble into an intellectual object — which images constitute a manuscript, in
what order, with what labels, carrying what metadata (IIIF Consortium, 2020). It
knows nothing about pixels; it refers to images by their Image API endpoints and
concerns itself with arrangement and description.

| Concern | Image API | Presentation API |
| --- | --- | --- |
| Answers | "Give me this part of this image" | "What is this object and how is it arranged?" |
| Format | An image (JPEG, PNG, TIFF) | JSON-LD |
| Knows about | Regions, sizes, rotation, quality | Manifests, canvases, ranges, metadata |
| Does not know about | Which manuscript this is | Pixels |
| Delivers | Image bytes | A description referring to Image API endpoints |

The separation is the design's central virtue. Because the two are independent, a
Presentation API manifest can reference images served by any compliant Image API
server anywhere in the world. A single manifest can assemble folios from the
Vatican, Leipzig, and Paris into one virtual codex — which is exactly the
Sinaiticus problem solved.

**Takeaway:** The Image API delivers pixels and the
Presentation API describes structure, and their independence is what lets one
manifest gather images from many institutions.

---

## **04 Content**

**The Image API URL Syntax**

The Image API's power comes from a single well-designed URL template. Every
compliant server accepts requests in the same form:

```text
{scheme}://{server}/{prefix}/{identifier}/{region}/{size}/{rotation}/{quality}.{format}
```

Each segment is a parameter, and reading a IIIF URL means reading off what was
requested:

| Segment | Meaning | Example values |
| --- | --- | --- |
| `identifier` | Which image | `Vat.gr.1209_0042` |
| `region` | Which part of it | `full`, `square`, `125,15,200,300`, `pct:10,10,50,50` |
| `size` | How large to return it | `max`, `1000,`, `,500`, `pct:50`, `!400,400` |
| `rotation` | Degrees clockwise; `!` mirrors | `0`, `90`, `!180` |
| `quality` | Colour treatment | `default`, `color`, `gray`, `bitonal` |
| `format` | File format | `jpg`, `png`, `tif`, `webp` |

A concrete request:

```text
https://digi.vatlib.it/iiif/MSS_Vat.gr.1209/full/1000,/0/default.jpg
```

This asks for the whole image, scaled to 1000 pixels wide, unrotated, in default
colour, as JPEG. Changing `full` to `1200,400,800,600` returns only that
rectangle — an 800×600 region whose top-left corner is at pixel (1200, 400).

Learn to read and write these by hand. It looks like a minor skill and is not:
once you can construct an Image API URL, you can extract any region of any folio
in any IIIF-compliant collection in the world, at any resolution, with a line of
text. In Week 12, when your commentary needs to reproduce the exact patch of
parchment supporting a disputed reading, this is how you will obtain it.

**Takeaway:** One URL template gives you any region of any
image in any IIIF collection, at any size — learn to write it by hand.

---

## **05 Content**

**Tiling and Deep Zoom**

The Image API's region-and-size parameters exist to support a specific behaviour:
**deep zoom**, the ability to navigate a very large image smoothly without
downloading it.

A high-resolution manuscript scan may be 10,000 by 14,000 pixels — around 140
megapixels, and hundreds of megabytes uncompressed. Transferring that to display
a page on a screen 1,500 pixels wide is absurd: the overwhelming majority of the
data cannot be displayed and is discarded on arrival.

Tiling inverts the arrangement. The server maintains the image at several
resolution levels, each divided into small square tiles, typically 256 or 512
pixels on a side. When a viewer displays the whole folio, it requests a handful
of tiles from a low-resolution level — enough to fill the screen at that scale.
When the user zooms into a word, it requests only the few tiles at the highest
resolution level that intersect the current viewport (Griffin, 2023).

| View | Level requested | Tiles fetched | Approximate data |
| --- | --- | --- | --- |
| Whole folio | Lowest | 4–12 | A few hundred kilobytes |
| Half page | Middle | 8–20 | Under a megabyte |
| One line, zoomed | Highest | 6–15 | Around a megabyte |
| Whole folio at full resolution | Highest | Over 2,000 | Hundreds of megabytes |

The last row is the one nobody ever requests, because there is no screen on which
it could be displayed. That is the insight: at any moment the user can only see
one screenful, so only one screenful ever needs to be transferred, regardless of
how large the underlying image is.

The practical consequence for you is that resolution is no longer something to
economize. You should seek the highest-resolution IIIF source available for your
passage, because the cost of high resolution is borne by the server's storage
rather than by your bandwidth.

**Takeaway:** Tiling means only the visible screenful is ever
transferred, so image resolution costs the viewer nothing.

---

## **06 Content**

**The Manifest: A Digital Object's Description**

Where the Image API handles pixels, the Presentation API's central document is
the **Manifest** — a JSON-LD file describing one intellectual object, such as a
manuscript, and everything a viewer needs to present it (IIIF Consortium, 2020).

A manifest states what the object is, what it is called, what metadata describes
it, what rights govern it, and — centrally — what sequence of canvases
constitutes it. It is the digital equivalent of a catalogue record fused with a
table of contents and a set of pointers to the images themselves.

A minimal manifest, reduced to its skeleton:

```json
{
  "@context": "http://iiif.io/api/presentation/3/context.json",
  "id": "https://example.edu/iiif/vat-gr-1209/manifest.json",
  "type": "Manifest",
  "label": { "en": ["Vaticanus graecus 1209, ff. 42r-43v"] },
  "summary": { "en": ["Fourth-century majuscule; selected folios"] },
  "rights": "http://creativecommons.org/licenses/by/4.0/",
  "requiredStatement": {
    "label": { "en": ["Attribution"] },
    "value": { "en": ["Biblioteca Apostolica Vaticana"] }
  },
  "items": [ ]
}
```

Three details are worth noticing now. The `id` is an HTTP URI at which the
manifest itself can be retrieved — manifests are web resources, not local files,
and that is what makes them shareable. Labels are objects keyed by language code
holding *arrays* of strings, which accommodates multilingual and multi-valued
descriptions natively. And `rights` and `requiredStatement` carry licensing and
attribution as structured data, so that a viewer can display the required credit
automatically wherever the manifest travels.

The `items` array — empty above — holds the canvases. That is the next section.

**Vocabulary.** *Manifest* — the JSON-LD document describing one digital object.
*JSON-LD* — JSON with a `@context` mapping its keys to shared vocabulary URIs, so
the data is machine-interpretable rather than merely machine-readable.

**Takeaway:** A manifest is a retrievable web document
describing one object — its identity, metadata, rights, and the sequence of
canvases that compose it.

---

## **07 Content**

**The Canvas: An Abstract Space, Not an Image**

The **Canvas** is the Presentation API's most important abstraction and the one
most often misunderstood. A canvas is *not* an image. It is an abstract
rectangular coordinate space, with a width and a height, onto which content is
painted (IIIF Consortium, 2020).

The distinction sounds scholastic and is in fact the source of the model's whole
expressive power. If a canvas were an image, then a page would have exactly one
image, and everything this week and next depends on would be impossible. Because
a canvas is a coordinate space, several things follow:

- Multiple images can be painted onto the same canvas — a natural-light photograph, an ultraviolet capture, and a processed composite, all sharing one coordinate system.
- Images can be painted onto part of a canvas, so that fragments recovered separately can be positioned within a reconstructed whole.
- Non-image content can be attached — transcriptions, translations, and annotations, targeted at coordinates.
- A canvas can exist with no image at all, representing a lost folio whose absence is part of the object's structure.

The canvas is therefore best understood as standing for *the page as an
intellectual entity*, while images are *evidence about* that page. A folio
photographed under five lighting conditions is one page with five pieces of
photographic evidence, and the model represents exactly that: one canvas, five
images.

This is the conceptual foundation for everything in Lesson 3.2, where a single
folio acquires visible-light, ultraviolet, infrared, and statistically processed
representations — and for Lesson 3.3, where your TEI transcription is bound to
canvas coordinates rather than to any particular photograph of the page.

**Takeaway:** A canvas is an abstract coordinate space standing
for the page itself, and images are evidence painted onto it — which is why one
page can carry many images.

---

## **08 Content**

**Annotations and the Painting Model**

If images are not properties of a canvas, how do they attach to it? Through
**annotation**. In Presentation API 3.0, an image is associated with a canvas by
an Annotation whose `motivation` is `painting` — a statement that this image
should be rendered onto that coordinate space (IIIF Consortium, 2020).

The structure nests as follows: a Canvas contains an `items` array holding
AnnotationPages; each AnnotationPage contains an `items` array holding
Annotations; each Annotation has a `body` (the content) and a `target` (what it
applies to).

```json
{
  "id": "https://example.edu/iiif/canvas/42r",
  "type": "Canvas",
  "height": 4000,
  "width": 3000,
  "items": [{
    "id": "https://example.edu/iiif/page/42r/1",
    "type": "AnnotationPage",
    "items": [{
      "id": "https://example.edu/iiif/annotation/42r-image",
      "type": "Annotation",
      "motivation": "painting",
      "body": {
        "id": "https://example.edu/iiif/img/42r/full/max/0/default.jpg",
        "type": "Image",
        "format": "image/jpeg",
        "height": 4000,
        "width": 3000
      },
      "target": "https://example.edu/iiif/canvas/42r"
    }]
  }]
}
```

This is markedly more verbose than simply attaching an image URL to a page, and
the verbosity buys something specific. Because association is by annotation, the
same mechanism handles every kind of content: a transcription is an annotation
with motivation `supplementing`, a scholarly comment is one with motivation
`commenting`, and a translation is another. One uniform structure covers image,
text, and commentary alike.

Version 3.0 adopted the W3C Web Annotation Data Model for this purpose,
superseding the earlier Open Annotation model used in 2.1 (IIIF Consortium,
2020). The practical significance is that IIIF annotations are now instances of a
general web standard rather than a IIIF-specific invention, and tools built for
web annotation work with them.

**Takeaway:** Content attaches to a canvas by annotation, and
because the mechanism is uniform, images, transcriptions, and commentary all
attach the same way.

---

## **09 Content**

**Presentation API 2.1 and 3.0**

You will encounter both versions in the wild, because many institutions still
serve 2.1 manifests. The differences matter enough to be worth recognizing on
sight (IIIF Consortium, 2020).

| Feature | Presentation API 2.1 | Presentation API 3.0 |
| --- | --- | --- |
| Annotation model | Open Annotation | W3C Web Annotation |
| JSON-LD version | 1.0, using `@id` and `@type` | 1.1, using `id` and `type` |
| Image attachment | `images` array directly on the canvas | AnnotationPage holding `painting` annotations |
| Labels | Plain strings | Language maps: `{"en": ["..."]}` |
| Audio and video | Not supported | Native, via `duration` on the canvas |
| Layered alternatives | No standard mechanism | The `Choice` construct |
| Supplementary views | Modelled ad hoc | `accompanyingCanvas`, `placeholderCanvas` |

The quickest way to identify a manifest's version is the key style. If you see
`@id` and `@type`, you are reading 2.1; if you see bare `id` and `type`, it is
3.0. The `@context` value states it definitively.

Two of these changes matter directly for your work. The **language map** for
labels means that `"label"` in 3.0 is always an object keyed by language code
containing an array — a shape that trips up everyone writing their first manifest
by hand, because a bare string is invalid. And the **`Choice`** construct, absent
from 2.1, is what makes multi-spectral layering expressible at all; it is the
subject of Lesson 3.2 and the reason this course targets 3.0 specifically.

Write 3.0 for your own manifest. Read 2.1 when you must, and be aware that
converting between them is not purely mechanical, since 3.0 can express
structures 2.1 cannot.

**Takeaway:** `@id` means 2.1 and bare `id` means 3.0; write
3.0, because only it can express layered spectral alternatives.

---

## **10 Content**

**The Full Structural Hierarchy**

Assembling the pieces, a Presentation 3.0 document has a consistent nesting that
is worth committing to memory, since every error message you receive will refer
to some level of it.

| Level | Type | Holds | Corresponds to |
| --- | --- | --- | --- |
| 1 | Collection | Manifests and other collections | A library, or a group of manuscripts |
| 2 | Manifest | Canvases, ranges, metadata | One manuscript or one intellectual object |
| 3 | Canvas | AnnotationPages | One page or opening |
| 4 | AnnotationPage | Annotations | A layer of content on the page |
| 5 | Annotation | A body and a target | One assertion: paint this here |
| 6 | Body | Image, text, or Choice | The content being asserted |

Alongside canvases, a manifest may carry **Ranges** in a `structures` array.
Ranges group canvases into meaningful units without changing their order — quires
in a codex, books in a work, chapters, or the section of the manuscript your
passage occupies. A viewer renders ranges as a table of contents.

This matters for your edition. Your passage is a portion of a manuscript, and a
range expresses exactly that relationship: it identifies which canvases
constitute your passage while leaving them in place within the manuscript's full
sequence. In Week 13, when you publish, this is how a reader will navigate
directly to your text within the larger codex.

Two structural rules catch people out. Every canvas must declare `height` and
`width`, because those define the coordinate space that annotations target and
without them targeting is undefined. And every resource needs an `id` that is a
genuine HTTP URI, not an arbitrary local string — the identifiers are meant to be
dereferenceable.

**Takeaway:** Collection, manifest, canvas, annotation page,
annotation, body — and ranges group canvases into a table of contents without
disturbing their order.

---

## **11 Content**

**Case Study: DigitaVaticana and Scale**

The Vatican Apostolic Library's digitization programme demonstrates what IIIF
delivers at scale, and it is the case most directly relevant to your own source
selection.

The library holds roughly eighty thousand manuscripts. Digitizing that corpus
under the pre-IIIF model would have required pre-generating a full pyramid of
static zoom levels for every folio — every resolution, every tile, stored on disk
in advance. The storage implications are prohibitive, and the result would be
frozen: any change to tile size or zoom behaviour would require regenerating
everything.

The IIIF Image API removes the requirement. The library stores one
high-resolution master per folio and generates tiles dynamically in response to
requests. Storage scales with the number of folios rather than with the number of
folios multiplied by zoom levels, and the delivery behaviour can change without
touching the stored masters (Griffin, 2023).

On top of that, the Presentation API supplies structure: each codex is described
by a manifest carrying its metadata and canvas sequence, served as JSON-LD. Those
manifests are consumed by Mirador, an open-source viewer that presents multiple
manifests side by side in a single workspace. A scholar can open a Vatican
manuscript alongside one from any other IIIF-compliant institution and compare
readings at full zoom, without either library having coordinated with the other
in any way (Griffin, 2023).

The last clause is the point worth dwelling on. The Vatican did not build an
interface for comparing its manuscripts with Leipzig's. It published standard
manifests, and comparison became possible as a consequence. That is what a
standard does: it makes cooperation happen without requiring coordination.

**Takeaway:** The Vatican stores one master per folio and
generates tiles on demand, and comparison with other libraries works because both
publish to the same standard — not because they cooperated.

---

## **12 Content**

**Viewers: Mirador and the Universal Viewer**

A manifest is inert data. A **viewer** is the client that interprets it and
renders a usable interface, and because manifests are standardized, viewers are
interchangeable.

| Viewer | Strengths | Best suited to |
| --- | --- | --- |
| Mirador 3 | Multiple manifests side by side; annotation support; layer toggling | Comparative work; collation; this course |
| Universal Viewer | Polished single-object presentation; strong accessibility | Public-facing publication |
| Annona | Lightweight web components; embeddable | Embedding in your own Week 13 site |
| Clover | Modern React interface; good audio-video handling | Presentation-focused projects |

Mirador is the one to learn first, because its defining capability is precisely
the operation this course is about: it opens several manifests in one workspace
and displays them simultaneously. Comparing two witnesses of your passage means
loading two manifests into one Mirador window and placing them side by side —
the digital equivalent of two manuscripts open on the same desk, which for most
of the discipline's history was an extraordinary privilege.

Two features you will use repeatedly. Mirador's workspace state can be saved and
shared, so a particular arrangement of witnesses at particular zoom levels can be
handed to a collaborator or an instructor as a reproducible view. And Mirador
renders the `Choice` construct as a layer selector, which is the interface
through which multispectral alternatives become usable — the subject of the next
lesson.

Install Mirador locally this week, or bookmark a hosted instance. You will use it
in every remaining week of the course.

**Takeaway:** Viewers are interchangeable because manifests are
standard, and Mirador is the one to learn because it juxtaposes witnesses.

---

## **13 Content**

**Finding IIIF Resources for Your Passage**

You selected a passage in Week 1 and confirmed a IIIF manifest existed. Now
locate and record the actual endpoints, because Lesson 3.3 requires them.

Most institutions expose the manifest URL through their viewer interface, though
the presentation varies:

- A "IIIF" logo or drag-and-drop badge, usually near the image — the badge itself is a link to the manifest.
- A "Share" or "Export" panel offering a manifest URL.
- A predictable URL pattern, such as `https://digi.vatlib.it/iiif/MSS_{shelfmark}/manifest.json`.
- The page source: search the HTML for `manifest.json`.
- The browser's network inspector: reload the viewer and look for the JSON request it makes.

The last method always works, because a IIIF viewer cannot function without
fetching a manifest. If the other routes fail, open the developer tools, filter
network requests for `manifest`, and reload.

Major repositories with reliable IIIF support include the Vatican Library, the
Bibliothèque nationale de France via Gallica, the British Library, e-codices for
Swiss manuscripts, the Bodleian's Digital Bodleian, Harvard, Yale's Beinecke, and
the Biblissima aggregator. Biblissima is particularly useful for locating
witnesses, since it indexes manifests across many institutions.

Record what you find in your repository now — manifest URL, Image API base URL,
canvas identifiers for your folios, and the licence and required attribution. A
manifest URL that worked in September and was not written down is a genuine
obstacle in December.

**Takeaway:** Every IIIF viewer must fetch a manifest, so the
network inspector always reveals the URL when the interface does not.

---

## **14 Content**

**Reading a Manifest Critically**

Having found a manifest, read it rather than merely feeding it to a viewer. It is
a scholarly document, and it makes claims you may need to evaluate or dispute.

```bash
curl -s https://digi.vatlib.it/iiif/MSS_Vat.gr.1209/manifest.json | python3 -m json.tool | head -60
```

Interrogate the following:

| Question | Where to look | Why it matters |
| --- | --- | --- |
| What version is this? | `@context` | Determines what constructs are available |
| How many canvases? | Length of `items` | Confirms the folio range you expected |
| What are the dimensions? | `height`, `width` on canvases | Determines coordinate precision for Lesson 3.3 |
| What licence applies? | `rights` | Governs what you may publish in Week 13 |
| What attribution is required? | `requiredStatement` | Must be reproduced in your edition |
| Is there structure? | `structures` | Ranges may already identify your passage |
| What metadata is asserted? | `metadata` | Date and origin claims you may need to assess |

The metadata deserves genuine scholarly scepticism. A manifest's assertions about
date, origin, and scribe are catalogue claims, sometimes inherited from
nineteenth-century descriptions and not always revised since. They are evidence
about the manuscript, of the same kind as any other catalogue statement, and they
can be wrong. Your Week 2 TEI header records *your* description, and where it
diverges from the manifest's, that divergence is a scholarly claim you should be
prepared to defend.

Clausen et al. (2026), arguing for open repositories that integrate manuscript
research data, make the related point that descriptive and material data about a
manuscript accumulate from many sources and must be kept traceable to those
sources rather than merged into an undifferentiated record.

**Takeaway:** A manifest's metadata is a catalogue claim that
can be wrong; read it as evidence, not as fact.

---

## **15 Content**

**Rights, Licensing, and What You May Publish**

Because your edition will be published in Week 13, licensing is a practical
constraint rather than a formality, and IIIF makes it explicit.

The `rights` property holds a URI identifying a licence — typically a Creative
Commons licence or a RightsStatements.org statement. The `requiredStatement`
holds attribution text that must be displayed wherever the images appear.

| Rights value | Permits | Constraint for Week 13 |
| --- | --- | --- |
| CC0 | Anything, no conditions | None |
| CC BY | Reuse with attribution | Reproduce the required statement |
| CC BY-NC | Non-commercial reuse only | Fine for coursework; limits later reuse |
| CC BY-SA | Reuse if derivatives share the licence | Your edition must adopt the same licence |
| InC (In Copyright) | Nothing by default | You may link, not reproduce |
| NoC-NC | Non-commercial use; no copyright known | Usually workable; read the statement |

Two practical rules follow. First, *linking is not reproducing*. Referencing a
canvas URI in your TEI and letting a viewer fetch the image from the
institution's server is not republication — the image is served by its owner
under its own terms. Copying the image file into your repository is
republication, and requires the licence to permit it. Prefer linking; it is both
safer and better practice, since the image stays connected to its source.

Second, attribution is not optional and not a matter of politeness. Where
`requiredStatement` is present, displaying it is a licence condition. Build it
into your edition's interface rather than adding it at the end.

If your chosen manuscript is In Copyright, raise it this week. It is workable —
you link rather than reproduce — but it changes what Week 13 can publish, and
that is better known now than in December.

**Takeaway:** Linking to a canvas is not republication; copying
the image file is — so prefer linking, and always display the required
attribution.

---

## **16 Content**

**JSON-LD: Why the Format Is Not Just JSON**

Manifests are JSON-LD, not plain JSON, and the difference is the reason IIIF data
composes with other scholarly data.

Plain JSON is *machine-readable*: a program can parse it into a data structure.
But the meaning of its keys is a private convention. A `"date"` key might hold a
manuscript's date of production, its date of digitization, or the date the record
was edited, and nothing in the JSON says which. A program must be told, by a
human, what the publisher meant.

JSON-LD adds a `@context` that maps keys to URIs in shared vocabularies (IIIF
Consortium, 2020). Once `"label"` is defined as a specific term in the IIIF
vocabulary, its meaning is stated in the data rather than assumed. The document
becomes *machine-interpretable*: a program that has never encountered this
institution's manifests can still determine what each field asserts.

This makes manifests **Linked Data** — part of a graph in which resources are
identified by URIs and can be referenced from outside. The consequence for
scholarship is that a manuscript's canvas can be cited from anywhere: your TEI
transcription in Lesson 3.3 will reference a Vatican canvas URI directly, and
that reference is meaningful to any system that understands the vocabulary.

The connection to Week 2 is direct. The RDF triples you built for your TEI header
and IIIF's JSON-LD are two serializations of the same underlying model —
subject, predicate, object, with URIs as identifiers. Your metadata and your
images are already in the same graph, which is what will let Week 13 publish them
as a single connected resource.

**Vocabulary.** *Linked Data* — data published with URI identifiers and shared
vocabularies so that it can be referenced and combined across sources. *`@context`*
— the JSON-LD element mapping keys to vocabulary URIs.

**Takeaway:** JSON-LD states the meaning of its keys in the
data, which is what lets a manifest be cited from and combined with other
scholarly data.

---

## **17 Content**

**Canvas Coordinates and Fragment Selectors**

Since a canvas is a coordinate space, any region of it can be addressed
precisely. The mechanism is the **fragment selector**, appended to a canvas URI
with `#`:

```text
https://example.edu/iiif/canvas/42r#xywh=1200,400,800,600
```

The `xywh` selector names four integers: the x and y coordinates of the region's
top-left corner, then its width and height, all in canvas coordinate units.
Coordinates originate at the top-left of the canvas, with x increasing rightwards
and y increasing downwards — the standard convention in computer graphics, and
the opposite of mathematical convention on the y axis, which catches people out.

| Selector | Addresses |
| --- | --- |
| `#xywh=0,0,3000,4000` | The entire canvas, if it is 3000 by 4000 |
| `#xywh=1200,400,800,600` | An 800 by 600 region at (1200, 400) |
| `#xywh=pct:25,10,50,15` | A percentage-based region, resolution-independent |

The percentage form deserves attention. Absolute pixel coordinates are tied to a
particular canvas size; if the manifest is ever regenerated from a rescanned
master at different dimensions, every absolute coordinate silently becomes wrong.
Percentage coordinates survive that change. For a course edition the absolute
form is generally acceptable and is what most tools emit, but record the canvas
dimensions alongside your coordinates so that the values can be recomputed if
needed.

This is the mechanism that binds text to image, and it is the crux of Lesson 3.3.
A line of your transcription will carry a `@facs` attribute pointing at exactly
the region of the canvas that shows it — so that a reader clicking a word is
taken to the parchment.

**Takeaway:** `#xywh=x,y,w,h` addresses any rectangle of a
canvas, and this is the mechanism that will bind your transcription to the image.

---

## **18 Content**

**Palaeography and the Digital Surrogate**

A methodological question arises before the technical work goes further. What is
the epistemological status of the digital image relative to the manuscript?

The traditional answer was that the surrogate is a degraded substitute:
photography loses information — colour fidelity, surface texture, the physical
sense of the object — and serious palaeographical judgement therefore requires
autopsy, direct inspection of the original. On that view digitization is a
convenience for preliminary work, with real conclusions reserved for the
manuscript itself.

That answer is now only partly right, and the qualification is the point of this
week. In some respects the surrogate remains poorer: no photograph conveys the
weight and drape of a codex, and colour is never fully faithful. In other respects
the surrogate is *better than autopsy* — it can be magnified beyond what the eye
resolves, illuminated in wavelengths the eye cannot see, and processed to
separate signals the eye cannot distinguish (Easton et al., 2003).

Griffin (2023), surveying digital infrastructures for epigraphy and palaeography,
describes this as a genuine shift in what these disciplines can investigate,
rather than as improved access to unchanged objects. The digital surrogate is not
a photograph of the manuscript; it is a dataset derived from it, and its relation
to the original is more like that of a scientific instrument's output than of a
picture.

The practical corollary matters for your own claims. When you assert a reading
this term, you should be able to say what evidence supports it and under what
conditions that evidence was produced — which image, which wavelength, which
processing. Lesson 3.2 concerns exactly those conditions, and Lesson 3.3 concerns
recording them.

**Takeaway:** A digital surrogate is a dataset derived from the
manuscript, not a picture of it, and in some respects it shows more than autopsy
can.

---

## **19 Content**

**Case Study: Codex Sinaiticus and Virtual Reunification**

Sinaiticus makes the interoperability argument concrete, and it is worth
following the case through.

Written in the fourth century, it is among the oldest substantially complete
manuscripts of the Christian Bible and a witness of the first importance for the
text of both Testaments. In the nineteenth century its leaves were dispersed, and
they now rest in four institutions: the British Library, Leipzig University
Library, St Catherine's Monastery in Sinai, and the National Library of Russia.

The scholarly consequence was severe. The manuscript is one object and one
scribal undertaking, but no scholar could examine it as such. Study meant
travelling between four institutions across three continents, or relying on
photographic facsimiles that fixed a single interpretation of each page and could
not be re-examined under different conditions.

Digitization with interoperable delivery permits virtual reunification: the
dispersed leaves are described by manifests, and a viewer assembles them into
their original sequence regardless of where each is physically held. Imaging that
enhanced the faded carbon inks additionally revealed textual variants and scribal
corrections that had not been legible in earlier facsimiles.

Note the double gain, because it recurs throughout the week. Interoperability
solved a *distribution* problem — the leaves could be brought together. Imaging
solved a *legibility* problem — the text could be read. Neither addresses the
other, and both were needed. Lesson 3.2 takes up the second.

**Takeaway:** Sinaiticus needed two distinct advances —
interoperability to reunite dispersed leaves, and enhanced imaging to make the
ink legible.

---

## **20 Content**

**Validating a Manifest**

Manifests you write by hand will contain errors, and a viewer's response to an
invalid manifest is usually to display nothing with no explanation. Validate
deliberately.

| Check | Tool | Catches |
| --- | --- | --- |
| Well-formed JSON | `python3 -m json.tool` | Trailing commas, unclosed brackets, bad quoting |
| IIIF conformance | The IIIF Presentation Validator | Missing required properties; wrong types |
| Renders correctly | Load into Mirador | Structural problems the validator permits |
| Images resolve | `curl -I` on each image URI | Broken or moved image endpoints |

Run them in that order, since each presupposes the previous. Malformed JSON
cannot be checked for conformance; a non-conformant manifest will not render; a
manifest that renders may still point at images that have moved.

The errors that recur most often when writing 3.0 by hand:

- A label given as a plain string instead of a language map — `"label": "f. 42r"` rather than `"label": {"en": ["f. 42r"]}`.
- A canvas without `height` and `width`, leaving the coordinate space undefined.
- Images attached directly to the canvas in the 2.1 style, instead of through an AnnotationPage.
- An `id` that is not an HTTP URI.
- A `target` naming a canvas id that does not exist, usually a typo.

Add validation to your pre-commit hook, exactly as you did for XML in Week 1. A
malformed manifest committed on a Tuesday and discovered on a Friday is an
avoidable loss.

**Takeaway:** Validate as JSON, then for IIIF conformance, then
by rendering, then by checking that the images actually resolve.

---

## **21 Content**

**Level 0 and Level 2 Image Services**

Not every IIIF image server offers the same capabilities, and the difference will
affect what you can do with a given source. The Image API defines compliance
levels.

| Level | Supports | Typical implementation |
| --- | --- | --- |
| Level 0 | Only pre-generated static sizes and regions | Static files on ordinary web hosting |
| Level 1 | Region and size requests; limited transformation | Lightweight servers |
| Level 2 | Arbitrary regions, sizes, rotation, quality, formats | Full image servers: Cantaloupe, IIPImage, Loris |

The distinction becomes concrete in Week 13. A Level 2 service permits any region
at any size on demand, which is what dynamic deep zoom requires. A Level 0
service serves only the derivatives that were generated in advance — a request
for an arbitrary region simply fails.

The reason this matters to you is that Level 0 is often the practical option for
publishing your own images. Running Cantaloupe requires a server you administer;
generating a fixed tile pyramid and serving it as static files requires only web
hosting, and works on GitHub Pages. If in Week 13 you publish your own derived
images — a processed composite, for instance — you will most likely produce a
Level 0 service with a tool such as `iiif_static.py`.

The manifest declares the level in each image body's `service` block, so you can
determine in advance what a source supports. If you plan to extract arbitrary
regions from an institution's images for your commentary, confirm Level 2 before
depending on it.

**Takeaway:** Level 2 serves arbitrary regions on demand; Level
0 serves only pre-generated derivatives, and is what static hosting supports.

---

## **22 Content**

**Content Search and Navigation APIs**

Two further IIIF specifications are worth knowing, because they become relevant
to your published edition in Week 13.

The **Content Search API** defines a standard way to search annotations attached
to a manifest and to receive results with their canvas coordinates. Where a
transcription has been attached as annotations, a viewer implementing Content
Search lets a reader search the *text* and be taken to the corresponding place on
the *image*. For a digital edition this is the capability that makes the
transcription usable rather than merely present.

The **Change Discovery API** publishes a stream of changes to a collection, so
that aggregators can learn when manifests are added or updated without polling.
This is what allows services like Biblissima to index manifests across dozens of
institutions and keep the index current.

| API | Purpose | Relevance to your edition |
| --- | --- | --- |
| Image | Deliver image regions | Every week from now on |
| Presentation | Describe structure | Lesson 3.3 |
| Content Search | Search annotations, return coordinates | Week 13 publication |
| Change Discovery | Announce updates to a collection | Aggregation; contextual |
| Authentication | Control access to restricted images | Only if your source is restricted |

You are not required to implement Content Search this term. It is worth knowing
that the capability is standardized, because it shapes what you should aim at:
if your transcription is bound to canvas coordinates — which is precisely what
Lesson 3.3 does — then a searchable image-linked edition is a matter of
configuration rather than of redesign.

**Takeaway:** Binding your transcription to canvas coordinates
now is what makes a searchable, image-linked edition possible later.

---

## **23 Content**

**Where IIIF Fits in the Course Pipeline**

Situate this week within the whole, because the imaging layer is what several
later weeks silently depend on.

| Week | Operation | Dependency on IIIF |
| --- | --- | --- |
| 3 | Build the manifest | The work itself |
| 4 | Transcription and HTR | Transkribus and eScriptorium ingest manifests directly |
| 5 | Reconciliation | Comparing readings against the image requires deep zoom |
| 6 | Normalization | Checking orthography against the manuscript |
| 7 | Collation | Witnesses juxtaposed in Mirador |
| 8 | Apparatus | Each variant anchored to its canvas region |
| 12 | Commentary | Reproducing the exact region under discussion |
| 13 | Publication | Viewer integration; the edition's image layer |

The Week 4 dependency is the most immediate. HTR platforms ingest images by
manifest URI rather than by file upload, which means the manifest you build on
Friday is the input to next week's transcription work (eScriptorium/Kraken,
2024). A manifest that is malformed or incomplete on Friday is a blocked Tuesday.

The Week 8 dependency is the most interesting scholarly one. An apparatus entry
recording a variant reading can carry the canvas region showing that reading in
each witness — so that a reader evaluating your editorial decision sees the
parchment rather than taking your word for it. That is a genuine advance over
print, where the apparatus can only assert.

**Takeaway:** Friday's manifest is Tuesday's HTR input, and
every later week's verification against the manuscript runs through it.

---

## **24 Content**

**The Multimodal Repository Argument**

Clausen et al. (2026) extend the interoperability argument beyond images, and
their framing is useful for understanding where this is all heading.

Their observation is that a manuscript under modern investigation generates
many kinds of data. Multispectral imaging produces datacubes. X-ray fluorescence
produces elemental maps. Raman spectroscopy characterizes pigments. Codicological
examination produces structural description. Transcription produces TEI. Each has
traditionally been held by the discipline that produced it, in its own format, in
its own repository — and the connections between them, which are where the
interesting questions live, are lost.

Their proposal is an open repository integrating these heterogeneous datasets
around the physical object, linking material analyses to structural textual
encodings so that a question spanning them can be asked at all (Clausen et al.,
2026).

| Data type | Produced by | Traditionally held in |
| --- | --- | --- |
| Multispectral datacube | Imaging science | Imaging lab archives |
| XRF elemental map | Conservation science | Conservation records |
| Raman pigment analysis | Materials chemistry | Chemistry publications |
| Codicological description | Manuscript studies | Library catalogues |
| Transcription and apparatus | Textual criticism | Editions and TEI repositories |

IIIF is a substantial part of the answer, because the canvas provides a shared
coordinate space that every one of these can target. An elemental map, a
processed composite, and a transcribed line can all address the same region of
the same canvas — which is exactly what makes them relatable.

Your own edition is a small instance of this. By Week 13 it will link
codicological description, images under multiple conditions, transcription,
apparatus, and commentary, all anchored to a common coordinate space.

**Takeaway:** The canvas is a shared coordinate space that
imaging, materials analysis, and transcription can all target, which is what makes
them relatable.

---

## **25 Content**

**Persistent Identifiers and Citation**

An edition that cannot be cited stably is not scholarship, and IIIF resources are
identified by URIs — which are notoriously unstable.

The problem is real. Institutions reorganize, domains lapse, platforms migrate,
and a canvas URI cited in a 2026 article may resolve to nothing in 2036. This is
the digital equivalent of a shelfmark changing after a library recatalogues, with
the difference that the digital failure is silent and total.

Mitigations, in order of reliability:

| Approach | Mechanism | Durability |
| --- | --- | --- |
| DOI | Registered persistent identifier with maintained resolution | High; the scholarly standard |
| ARK | Archival Resource Key, widely used by libraries | High where the institution maintains it |
| Purl | Redirection service under the publisher's control | Moderate |
| Institutional URI | The library's own URL scheme | Variable; depends on institutional stability |
| Ad-hoc URL | Whatever the current platform emits | Low |

For your own citations this term, record the DOI or ARK where one exists, and the
full canvas URI in every case. Where a manifest carries a `seeAlso` block, follow
it — institutions frequently link the persistent catalogue record there.

Also record what you saw and when. A citation of the form "MS Vat. gr. 1209,
f. 42r, canvas `https://…/canvas/p42`, accessed 15 September 2026, image dimensions
3000×4000" survives partial link rot: even if the URI stops resolving, a reader
can identify the folio and the exact region you meant. Your Week 1 commit
discipline is the mechanism here — record the identifiers in the repository, at
the time you use them.

**Takeaway:** Record DOIs, full canvas URIs, dimensions, and
access dates, so that your citations survive the link rot that will eventually
occur.

---

## **26 Content**

**A Practical Exercise for This Meeting**

Work through the following now, on your own passage. Everything in Lesson 3.3
assumes it is complete.

- Locate the manifest URL for your primary witness and record it in your repository.
- Retrieve it with `curl` and pretty-print it; do not merely open it in a viewer.
- Identify the canvases corresponding to your folios and record their ids.
- Record each canvas's `height` and `width`.
- Extract the `rights` value and the `requiredStatement`.
- Construct an Image API URL by hand that returns the full folio at 1000 pixels wide, and open it.
- Construct a second that returns only the region containing the first line of your passage.
- Load the manifest into Mirador and confirm it renders.
- Repeat for your second witness.
- Commit all of it as a structured note in your repository.

The hand-constructed URLs matter more than they appear. Anyone can drag a
manifest into a viewer; being able to write an Image API request from scratch is
what lets you extract precisely the evidence you need, script it over many
folios, and diagnose failures when a viewer shows nothing.

Record the results as a Markdown file in your repository — `images/SOURCES.md` is
a reasonable location — and commit it with a Conventional Commits message. In
Week 13 this file is the basis of your edition's image documentation.

**Takeaway:** Write the Image API URLs by hand; that skill is
what makes you independent of any particular viewer.

---

## **27 Content**

**Common Failures and Their Diagnosis**

Predictable failures, so you recognize them rather than rediscovering them.

| Symptom | Likely cause | Diagnosis |
| --- | --- | --- |
| Viewer shows nothing, no error | Invalid manifest | Run the IIIF validator |
| Manifest loads, images blank | Image endpoints moved or restricted | `curl -I` each image URI |
| Images load in one viewer, not another | Version mismatch, 2.1 versus 3.0 | Inspect `@context` |
| Cross-origin error in the browser console | Server lacks CORS headers | Check response headers; contact the institution |
| Zoom stops at low magnification | Level 0 service; no higher tiles exist | Inspect the `service` block |
| Coordinates address the wrong region | Canvas dimensions differ from image dimensions | Compare canvas `height`/`width` with the image |
| Labels display as `[object Object]` | Language map handled as a string, or vice versa | Check the label's shape against the version |

The CORS case is worth explaining, since it produces the most bewildering
symptom. A browser refuses to let a page fetch data from another domain unless
that domain's server explicitly permits it with a Cross-Origin Resource Sharing
header. If an institution's server omits the header, its manifest works in that
institution's own viewer and fails everywhere else — an accidental silo,
reproducing the exact problem IIIF was built to eliminate. Nothing on your side
can fix it; the remedy is to report it to the institution, which usually treats
it as the bug it is.

The last row is the classic hand-authoring error and the one most likely to bite
you on Friday. In 2.1 a label is a string; in 3.0 it is a language map holding
arrays. Mixing them produces exactly this symptom.

**Takeaway:** Diagnose in order — validate the manifest, check
the image endpoints, then check the version — and recognize CORS failures as the
institution's bug, not yours.

---

## **28 Content**

**What a Canvas Is Not**

A consolidating exercise, since the canvas abstraction is where conceptual errors
concentrate and each error has a characteristic downstream symptom.

| Misconception | Why it is wrong | Consequence |
| --- | --- | --- |
| "A canvas is an image" | It is a coordinate space; images are painted onto it | Cannot model multispectral layers |
| "A canvas has one image" | It may carry many, including alternatives | Cannot model a `Choice` |
| "Canvas dimensions are image dimensions" | They may differ; images are scaled to fit | Coordinates address the wrong region |
| "A canvas must have an image" | An empty canvas can represent a lost folio | Cannot model lacunae in a codex |
| "A canvas is a page" | It is an abstraction that usually *stands for* a page | Cannot model an opening, a fragment, or a reconstruction |

The third row causes the most practical trouble and is worth stating carefully.
Canvas dimensions define the coordinate space, and images are painted into that
space — scaled if their pixel dimensions differ. If a canvas is 3000×4000 while
the image is 6000×8000, then canvas coordinate (1500, 2000) corresponds to image
pixel (3000, 4000). Fragment selectors address *canvas* coordinates. Computing a
region from the image's pixel dimensions when the canvas differs puts your
annotation in the wrong place, and the error is systematic rather than random —
everything is off by the same factor, which makes it easy to miss and easy to
correct once seen.

Always read the canvas dimensions from the manifest, and never assume they match
the image.

**Takeaway:** Fragment selectors address canvas coordinates, not
image pixels, and the two frequently differ by a scale factor.

---

## **29 Content**

**Preparing for Lesson 3.2**

Wednesday moves from delivery to acquisition — from how images are served to how
they are made, and to what can be recovered from a manuscript that ordinary
photography cannot show.

The connection is the canvas abstraction established today. Multispectral imaging
produces many images of one folio: visible light, ultraviolet, several infrared
bands, and statistically processed composites. In a model where a page has one
image, these are unrelated files that a scholar must manage by hand. In the IIIF
model they are alternative content painted onto a single canvas, and a viewer can
present them as toggleable layers over one coordinate space.

That is why this week is ordered as it is. The `Choice` construct introduced
tomorrow is meaningless without today's understanding that a canvas is a space
rather than a picture, and the coordinate binding on Friday is meaningless
without both.

Before Wednesday:

- Complete the exercise in section 26 for both witnesses.
- Confirm Mirador renders both manifests.
- Note whether either institution provides non-visible-light images — search the manifest for terms such as `ultraviolet`, `infrared`, `UV`, `IR`, or `processed`.
- Read the `rights` statements and record what they permit.

The third item is genuinely worth doing. Multispectral captures exist for many
manuscripts but are frequently not surfaced in the default viewer, appearing only
as additional entries in the manifest. If your manuscript has them, Wednesday's
work applies directly to your own edition rather than to an example.

**Takeaway:** The canvas-as-space abstraction is what makes
tomorrow's spectral layering expressible; check now whether your own manuscript
has non-visible-light captures.

---

## **30 Content**

**Synthesis: Images as Addressable Scholarly Resources**

The argument of this meeting, stated once more in its own terms.

Digitization alone produced silos. Millions of manuscript images existed, each
accessible only through the interface of the institution that made it, which
meant that the fundamental operation of textual criticism — juxtaposing witnesses
— remained obstructed. The obstruction was not technical scarcity but the absence
of a shared standard.

IIIF resolves it by making images *addressable*. The Image API gives every region
of every image a URL constructed by a rule anyone can apply. The Presentation API
describes objects in a shared vocabulary, so that any viewer can render any
institution's manifest. Cooperation happens without coordination, because both
parties implement the same specification (Griffin, 2023; IIIF Consortium, 2020).

The abstraction that carries the most weight is the canvas: a coordinate space
standing for the page, onto which evidence is painted. This is what permits many
images of one page, transcriptions bound to regions of it, annotations targeting
its coordinates, and the whole multimodal integration that Clausen et al. (2026)
argue manuscript scholarship now requires.

**For Wednesday.** Complete the section 26 exercise for both witnesses, confirm
both render in Mirador, and check your manifests for non-visible-light captures.

**For Friday.** The **Cataloguing & Metadata Assignment is due Friday September
18**, and Friday's meeting builds the manifest for your passage and binds it to
your TEI. Everything recorded today is the input to that work.

**Takeaway:** IIIF makes every region of every image
addressable by a shared rule, and the canvas — a coordinate space, not a picture —
is what lets images, text, and analysis all refer to the same place.

---

## References

Clausen, H., Brenner, S., Schreiner, M., & Vetter, W. (2026). Multimodal
manuscript representation: Toward an open repository for manuscript research
data. *The European Physical Journal Plus*.
https://doi.org/10.1140/epjp/s13360-025-07133-y

Easton, R. L., Knox, K. T., & Christens-Barry, W. A. (2003). Multispectral
imaging of the Archimedes palimpsest. In *32nd Applied Imagery Pattern
Recognition Workshop*. https://doi.org/10.1109/AIPR.2003.1284258

eScriptorium/Kraken. (2024). *eScriptorium platform documentation*.
https://escriptorium.eu/about

Griffin, S. M. (2023). Digital libraries, epigraphy and paleography: Bringing
records from the distant past to the present. *International Journal on Digital
Libraries*. https://doi.org/10.1007/s00799-023-00381-2

IIIF Consortium. (2020). *IIIF Presentation API 3.0 specification*.
https://iiif.io/api/presentation/3.0/

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/
