# Lesson 3.3 — Building the Manifest and Binding It to TEI

*RELS 398 / ENGL 398 · Topic 3: IIIF Imaging · Meeting #8 (Fri Sep 18)*

*Infrastructure week — the three-step comparative cycle does not apply. Today
assembles the week into a working artefact: the manifest for your passage, bound
to your TEI encoding by canvas coordinates. **The Cataloguing & Metadata
Assignment is due today.***

---

## **01 Content**

**What Today Produces**

Two meetings of theory converge on one deliverable. By the end of today you will
have a IIIF manifest describing your passage, and a TEI document whose
transcription is bound to regions of that manifest's canvases.

Stated plainly, the artefact does this: a reader looking at a line of your
transcription can be taken to the exact patch of parchment that line transcribes,
and a reader looking at a region of the parchment can be taken to what you
transcribed there. The link runs both ways, and it is machine-actionable rather
than a matter of a reader consulting a plate number.

That capability is the difference between a transcription and a digital edition.
A printed edition asserts that folio 42r line 8 reads thus, and a reader wanting
to check must obtain a facsimile and count lines. A bound edition makes the
evidence one click away from the claim, which changes the standard a reader can
hold you to — and, more importantly, the standard you can hold yourself to while
working (Griffin, 2023).

The components are already in place. Lesson 3.1 established the manifest,
canvas, annotation, and fragment selector. Lesson 3.2 established what the images
are and how alternatives are expressed as a `Choice`. Week 2 produced your TEI
header. Today joins them.

**The takeaway for this page:** Today's artefact links each transcribed line to the
exact region of parchment it transcribes, in both directions and machine-actionably.

---

## **02 Content**

**Two Manifests, Two Situations**

Before building anything, determine which situation you are in, because it
determines what you build.

**Situation A: your institution publishes a manifest.** This is the common case
and the simpler one. The manifest exists, the images are served by the
institution, and your work is to *reference* it — recording canvas URIs and
building your TEI bindings against them. You do not build a manifest at all.

**Situation B: you need your own manifest.** This arises when your passage spans
witnesses in different institutions and you want them as one object; when the
institution serves images but no manifest; or when you are adding your own
derived images. Here you author a manifest that references images served
elsewhere.

| | Situation A | Situation B |
| --- | --- | --- |
| Who serves the images | The institution | The institution, still |
| Who authors the manifest | The institution | You |
| What you record | Canvas URIs from their manifest | Your own manifest, referencing their images |
| Where your manifest lives | Not applicable | Your repository, published in Week 13 |
| Main risk | Their URIs change | Your manifest drifts from their images |

Note what is true of both: **the images are served by the institution**. Situation
B does not mean hosting images yourself. You are authoring a description that
points at their Image API endpoints — which, as Lesson 3.1 established, is
referencing rather than republication, and therefore does not depend on the
licence permitting redistribution.

Most of you are in Situation A for your primary witness and Situation B for the
combined view of both witnesses. Today covers both.

**The takeaway for this page:** Authoring a manifest does not mean hosting images
— you describe an object that references the institution's Image API endpoints.

---

## **03 Content**

**Recording Canvas Identifiers**

Whichever situation applies, the foundation is an accurate record of the canvases
your passage occupies. Build it now, carefully, because every binding today
depends on it and an error propagates into all of them.

For each folio, extract from the institution's manifest:

| Field | Source in the manifest | Why needed |
| --- | --- | --- |
| Canvas `id` | The canvas object's `id` | The target of every binding |
| `height` and `width` | The canvas object | Coordinates are in canvas units |
| Label | The canvas `label` | Human-readable folio identification |
| Image `id` | The painting annotation's `body.id` | The Image API endpoint |
| Image service | `body.service` | Determines whether arbitrary regions are available |
| Image dimensions | `body.height`, `body.width` | May differ from canvas dimensions |

A script beats doing this by hand and is worth writing once:

```python
import json, urllib.request

url = "https://digi.vatlib.it/iiif/MSS_Vat.gr.1209/manifest.json"
m = json.load(urllib.request.urlopen(url))

for canvas in m["items"]:
    label = canvas.get("label", {}).get("en", ["?"])[0]
    body = canvas["items"][0]["items"][0]["body"]
    print(f"{label}\t{canvas['id']}\t{canvas['width']}x{canvas['height']}"
          f"\timg {body.get('width')}x{body.get('height')}")
```

Run it and read the output rather than trusting it. The last column exists to
surface the trap from Lesson 3.1 section 28: where image dimensions differ from
canvas dimensions, coordinates computed from the image are wrong by a scale
factor. If the two differ, note the ratio now.

Commit the output to `images/CANVASES.md`.

**The takeaway for this page:** Record canvas ids, canvas dimensions, and image
dimensions together — where the last two differ, every coordinate needs scaling.

---

## **04 Content**

**Determining Coordinates for a Region**

To bind a line of transcription to the parchment, you need the rectangle it
occupies in canvas coordinates. Several routes exist, of differing precision and
labour.

| Method | Precision | Effort | Best for |
| --- | --- | --- | --- |
| Mirador region selection | Good | Low | A handful of regions by hand |
| Image editor with coordinate readout | High | Moderate | Careful individual bindings |
| Annotation tool (Annotorious, Recogito) | High | Low per region | Many regions systematically |
| HTR layout analysis | High | Very low per line | Every line at once, from Week 4 |
| Arithmetic from line count | Rough | Very low | Provisional first pass |

The fourth row is the one that will do most of your work, and it is the reason
today's binding exercise is deliberately small. Next week's HTR layout analysis
emits a bounding box for every detected line automatically, in ALTO or PAGE XML,
already in image coordinates (eScriptorium/Kraken, 2024). Rather than hand-measuring
three hundred lines, you will transform that output.

Today you bind a few regions by hand, for two reasons. You need to understand what
the coordinates mean before accepting a machine's version of them, and you need at
least one hand-verified binding against which to check the automated ones next
week. A systematic offset in the transform is invisible unless you have a known-good
case to compare against.

For hand measurement, the arithmetic approach is a reasonable start: if a text
block runs from y=400 to y=3600 across 24 lines, each line occupies roughly 133
units, and line 8 begins near y=400+7×133=1331. Refine by inspection.

**The takeaway for this page:** Bind a few regions by hand today so that you can
verify next week's automated line coordinates against a known-good case.

---

## **05 Content**

**The TEI Facsimile Module**

TEI provides a dedicated structure for describing a document's physical surfaces
and the regions on them: the `<facsimile>` element and its children (TEI
Consortium, 2026).

| TEI element | Represents | IIIF equivalent |
| --- | --- | --- |
| `<facsimile>` | The set of surfaces constituting the document | The manifest |
| `<surface>` | One writing surface — a page or an opening | A canvas |
| `<zone>` | A region on a surface | A fragment selector on a canvas |
| `<graphic>` | An image of a surface or zone | An Image API endpoint |

The correspondence is close enough to be genuinely useful. A TEI `<surface>` maps
conceptually to a IIIF Canvas, and a `<zone>` corresponds to a bounding box on
that canvas — which is precisely the alignment that makes coordinate binding
possible (TEI Consortium, 2026).

The structure separates the *physical* description of the document from the
*textual* transcription. `<facsimile>` describes surfaces and regions; `<text>`
holds the transcription; and attributes link the two. This separation is
deliberate and important: it means the same transcription can be bound to
different image sets, and the same images can carry different transcriptions.

```xml
<facsimile>
  <surface xml:id="f42r" ulx="0" uly="0" lrx="3000" lry="4000">
    <graphic url="https://digi.vatlib.it/iiif/.../full/max/0/default.jpg"/>
    <zone xml:id="f42r_l01" ulx="420" uly="512" lrx="2580" lry="640"/>
    <zone xml:id="f42r_l02" ulx="420" uly="645" lrx="2580" lry="773"/>
  </surface>
</facsimile>
```

Note that TEI's native coordinate attributes name two corners — upper-left x and
y, lower-right x and y — whereas IIIF names a corner plus dimensions. Converting
between them is straightforward arithmetic, and the next section handles it.

**The takeaway for this page:** `<facsimile>` describes surfaces and zones
separately from the transcription, and TEI `<surface>` maps to a IIIF canvas.

---

## **06 Content**

**Two Coordinate Conventions**

TEI and IIIF express rectangles differently, and confusing them is the most common
source of misplaced bindings.

| | TEI zone attributes | IIIF fragment selector |
| --- | --- | --- |
| Form | `ulx`, `uly`, `lrx`, `lry` | `#xywh=x,y,w,h` |
| Specifies | Two opposite corners | One corner plus width and height |
| Example | `ulx="420" uly="512" lrx="2580" lry="640"` | `#xywh=420,512,2160,128` |

Converting between them:

```python
def tei_to_iiif(ulx, uly, lrx, lry):
    """TEI corner pair -> IIIF xywh."""
    return f"#xywh={ulx},{uly},{lrx - ulx},{lry - uly}"

def iiif_to_tei(x, y, w, h):
    """IIIF xywh -> TEI corner pair."""
    return {"ulx": x, "uly": y, "lrx": x + w, "lry": y + h}
```

The error to watch for is treating IIIF's third and fourth values as a second
corner. Doing so produces a region that starts in the right place and extends far
too far — and because the origin is correct, the binding looks plausible at low
zoom and is obviously wrong only when examined closely. If your zones are
consistently too large and overlap their neighbours, this is the cause.

Both conventions place the origin at the top-left with y increasing downwards, so
that at least is consistent. Both are also in *canvas* units, subject to the
scaling caveat from section 03.

Write the conversion once, as a tested function, and use it everywhere. Ad-hoc
arithmetic performed inline is where sign and ordering errors enter.

**The takeaway for this page:** TEI names two corners and IIIF names a corner plus
dimensions; treating IIIF's last two values as a corner produces regions that are
too large.

---

## **07 Content**

**Binding Transcription to Zones with `@facs`**

With zones defined, the transcription is linked to them by the `@facs` attribute,
available globally in TEI (TEI Consortium, 2026).

```xml
<facsimile>
  <surface xml:id="f42r">
    <graphic url="https://example.edu/iiif/42r/full/max/0/default.jpg"/>
    <zone xml:id="f42r_l01" ulx="420" uly="512" lrx="2580" lry="640"/>
  </surface>
</facsimile>

<text>
  <body>
    <div type="passage">
      <pb n="42r" facs="#f42r"/>
      <lb n="1" facs="#f42r_l01"/>ἐν ἀρχῇ ἦν ὁ λόγος
    </div>
  </body>
</text>
```

The `<pb>` (page beginning) carries `facs="#f42r"`, declaring that what follows is
on that surface. Each `<lb>` (line beginning) carries a `@facs` pointing at its
zone. A processor reading this knows, for every line of transcription, which
region of which surface it transcribes.

`@facs` can point in two ways, and the distinction matters:

| Form | Points to | Use when |
| --- | --- | --- |
| `facs="#f42r_l01"` | A `<zone>` in this document | Zones are declared locally, as above |
| `facs="https://…/canvas/p42#xywh=420,512,2160,128"` | A IIIF canvas region directly | Referencing an external manifest |

The first is more maintainable, since coordinates live in one place and can be
corrected without touching the transcription. The second is more portable, since
the transcription carries its own image references and needs no accompanying
`<facsimile>`.

The recommended practice for this course is the first, with `<surface>` carrying
the canvas URI — which the next section covers.

**The takeaway for this page:** `@facs` on `<pb>` and `<lb>` binds transcription to
zones; declare zones locally so coordinates can be corrected in one place.

---

## **08 Content**

**Connecting `<surface>` to the IIIF Canvas**

The remaining link is between your TEI surfaces and the institution's canvases.
Carry the canvas URI on the `<surface>` itself:

```xml
<surface xml:id="f42r"
         facs="https://digi.vatlib.it/iiif/MSS_Vat.gr.1209/canvas/p42"
         ulx="0" uly="0" lrx="3000" lry="4000">
  <graphic url="https://digi.vatlib.it/iiif/MSS_Vat.gr.1209/full/max/0/default.jpg"
           width="3000" height="4000"/>
  <zone xml:id="f42r_l01" ulx="420" uly="512" lrx="2580" lry="640"/>
</surface>
```

Now the chain is complete in both directions. A line carries `facs="#f42r_l01"`,
which resolves to a zone, which sits within a surface, which carries the canvas
URI and the surface dimensions. A processor can compute the full IIIF fragment
URI for any line by combining the canvas URI with the zone's coordinates converted
to `xywh` form.

Two details make this robust. Declaring `ulx`/`uly`/`lrx`/`lry` on the `<surface>`
records the coordinate space the zones are expressed in, so a processor can detect
and correct a mismatch with the canvas dimensions rather than silently producing
wrong regions. And declaring `width` and `height` on `<graphic>` records the
image's own dimensions, making the scaling relationship from section 03 explicit
in the document.

This is a case where slight redundancy is worth its cost. Coordinate systems
misalign silently, and recording the dimensions at each level is what lets a
mismatch be caught by a check rather than discovered by a reader.

**The takeaway for this page:** Put the canvas URI on `<surface>` and record
dimensions at every level, so coordinate mismatches can be detected rather than
silently misplacing regions.

---

## **09 Content**

**Generating the Fragment URI**

With the structure in place, a short transform produces a resolvable IIIF URI for
any line — which is what a viewer or a published edition consumes.

```python
import xml.etree.ElementTree as ET

TEI = {"t": "http://www.tei-c.org/ns/1.0"}

def line_uri(tree, line_id):
    """Full IIIF fragment URI for a zone id such as 'f42r_l01'."""
    zone = tree.find(f".//t:zone[@xml:id='{line_id}']", TEI)
    surface = tree.find(f".//t:zone[@xml:id='{line_id}']/..", TEI)
    canvas = surface.get("facs")
    ulx, uly = int(zone.get("ulx")), int(zone.get("uly"))
    lrx, lry = int(zone.get("lrx")), int(zone.get("lry"))
    return f"{canvas}#xywh={ulx},{uly},{lrx - ulx},{lry - uly}"
```

Test it against a region you measured by hand, and verify by constructing the
equivalent Image API URL and opening it:

```text
https://digi.vatlib.it/iiif/MSS_Vat.gr.1209/420,512,2160,128/full/0/default.jpg
```

If that returns the line you expected, the binding is correct. If it returns a
different line, or part of two lines, your coordinates or your conversion are
wrong — and this check is how you find out now rather than in Week 13.

Make this verification a habit. Every binding you create should be checkable by
constructing an Image API URL and looking at what comes back. It takes seconds,
it requires no tooling beyond a browser, and it is the only direct test that a
coordinate is right.

**The takeaway for this page:** Verify every binding by constructing the Image API
URL for its region and confirming the returned image shows what you expected.

---

## **10 Content**

**Authoring a Manifest: The Skeleton**

For Situation B, author a manifest. Build it as a Python script rather than by
hand — you will regenerate it many times, and hand-editing JSON invites the errors
catalogued in Lesson 3.1 section 20.

```python
import json

def manifest(base, label, canvases):
    return {
        "@context": "http://iiif.io/api/presentation/3/context.json",
        "id": f"{base}/manifest.json",
        "type": "Manifest",
        "label": {"en": [label]},
        "rights": "http://creativecommons.org/licenses/by/4.0/",
        "requiredStatement": {
            "label": {"en": ["Attribution"]},
            "value": {"en": ["Biblioteca Apostolica Vaticana"]},
        },
        "items": canvases,
    }
```

The properties above are the ones a manifest should always carry. `id` must be the
HTTP URI at which the manifest will actually be retrievable — not a placeholder,
because viewers resolve it. `label` must be a language map holding an array.
`rights` and `requiredStatement` carry the licensing you recorded in Lesson 3.1
(IIIF Consortium, 2020).

Add descriptive properties as well: `summary` for a short description, `metadata`
for structured fields such as shelfmark, date, and material, and `homepage`
pointing at the institution's catalogue record. These are what make your manifest
a scholarly document rather than a bare pointer list.

Generate, validate, and commit the generator alongside the output. The script is
the reproducible artefact; the JSON is its product.

**The takeaway for this page:** Generate manifests from a script rather than
hand-editing JSON, and commit the generator alongside its output.

---

## **11 Content**

**Authoring a Manifest: Canvases**

Each canvas is constructed from a folio's image endpoint and dimensions.

```python
def canvas(base, ident, label, image_url, w, h):
    return {
        "id": f"{base}/canvas/{ident}",
        "type": "Canvas",
        "label": {"en": [label]},
        "height": h,
        "width": w,
        "items": [{
            "id": f"{base}/page/{ident}/1",
            "type": "AnnotationPage",
            "items": [{
                "id": f"{base}/annotation/{ident}-image",
                "type": "Annotation",
                "motivation": "painting",
                "body": {
                    "id": image_url,
                    "type": "Image",
                    "format": "image/jpeg",
                    "height": h,
                    "width": w,
                    "service": [{
                        "id": image_url.rsplit("/full/", 1)[0],
                        "type": "ImageService3",
                        "profile": "level2",
                    }],
                },
                "target": f"{base}/canvas/{ident}",
            }],
        }],
    }
```

The `service` block is what enables deep zoom. Without it a viewer treats the
image as a single static file and cannot request tiles, so zooming degrades to
scaling one downloaded image. Include it whenever the source offers a Level 2
service, and set `profile` to match what the source actually provides — claiming
`level2` for a Level 0 service produces failures that are hard to diagnose.

Set `height` and `width` on the canvas from the *image's* dimensions unless you
have a reason to do otherwise. Choosing arbitrary canvas dimensions is legal and
creates exactly the scaling mismatch discussed throughout this week.

**The takeaway for this page:** Include the `service` block or deep zoom will not
work, and set canvas dimensions from the image's own dimensions.

---

## **12 Content**

**Adding a `Choice` for Spectral Layers**

Where your manuscript has multiple imaging conditions, express them as
alternatives on one canvas rather than as separate canvases (IIIF Consortium,
2020).

```python
def choice_body(layers):
    """layers: list of (image_url, label, width, height)."""
    return {
        "type": "Choice",
        "items": [
            {"id": url, "type": "Image", "format": "image/jpeg",
             "width": w, "height": h, "label": {"en": [label]}}
            for url, label, w, h in layers
        ],
    }
```

Substituting this for the single image body gives a canvas whose painting
annotation offers alternatives, which Mirador renders as a layer selector.

Two points of practice carry over from Lesson 3.2. The first item is the viewer's
default, so put the natural-colour image first. And the labels are your scholarly
documentation of the imaging conditions — state them precisely:

| Poor label | Better label |
| --- | --- |
| `UV` | `UV fluorescence, 365 nm` |
| `Processed` | `ICA composite, IC2/visible 592 nm/IC4` |
| `Infrared` | `Near-infrared, 940 nm` |
| `Enhanced` | `PCA components 2-4, contrast stretched` |

The right-hand column lets a reader evaluate what they are looking at, which is
exactly the requirement established in Lesson 3.2 section 17. A `Choice` whose
labels say "UV" and "Processed" reproduces the failure of undocumented processing
inside a structure designed to prevent it.

If your manuscript has only visible-light imaging, omit the `Choice` — a single
image body is correct and simpler.

**The takeaway for this page:** A `Choice` expresses spectral alternatives on one
canvas, and its labels must state the imaging conditions precisely enough to be
evaluated.

---

## **13 Content**

**Ranges: Identifying Your Passage Within the Codex**

Your passage is part of a larger manuscript, and a **Range** expresses that
relationship without disturbing the canvas sequence (IIIF Consortium, 2020).

```json
"structures": [{
  "id": "https://example.edu/iiif/range/passage",
  "type": "Range",
  "label": { "en": ["Selected passage, ff. 42r-43v"] },
  "items": [
    { "id": "https://example.edu/iiif/canvas/42r", "type": "Canvas" },
    { "id": "https://example.edu/iiif/canvas/42v", "type": "Canvas" },
    { "id": "https://example.edu/iiif/canvas/43r", "type": "Canvas" },
    { "id": "https://example.edu/iiif/canvas/43v", "type": "Canvas" }
  ]
}]
```

A viewer renders this as a table of contents entry, so a reader can navigate
directly to your passage within the full codex. Ranges may nest, so a
manuscript's quire structure, its constituent works, and your selected passage can
coexist as different groupings of the same canvases.

This matters more than it may seem for the scholarly presentation of your edition.
Publishing your passage as an isolated set of images detaches it from its
codicological context — and the Week 2 cataloguing work established that context
as evidence, not background. A range keeps the passage identified *within* the
manuscript, which is the accurate representation of what it is.

Where the institution's manifest already carries ranges, check whether one
corresponds to your passage; you may be able to reference it rather than
constructing your own.

**The takeaway for this page:** A range identifies your passage within the full
codex rather than detaching it, preserving the codicological context as part of the
edition.

---

## **14 Content**

**Validating What You Have Built**

Run the full validation sequence from Lesson 3.1 section 20 before committing, and
in that order.

| Step | Command or tool | Catches |
| --- | --- | --- |
| 1. Well-formed JSON | `python3 -m json.tool manifest.json` | Syntax errors |
| 2. IIIF conformance | IIIF Presentation Validator | Missing or wrongly typed properties |
| 3. Image endpoints resolve | `curl -I` on each image `id` | Broken or moved URLs |
| 4. Renders in a viewer | Load into Mirador | Structural problems validators permit |
| 5. Regions are correct | Open Image API URLs for your zones | Coordinate errors |
| 6. TEI validates | `xmllint --relaxng` against the TEI schema | Encoding errors |
| 7. Bindings resolve | Your `line_uri` function, spot-checked | Broken `@facs` references |

Steps 5 and 7 are the ones specific to today and the ones most likely to fail
silently. A manifest can be perfectly conformant and render beautifully while
every one of its coordinates points at the wrong place — validators check
structure, not meaning.

A checking script for step 7:

```python
for lb in tree.findall(".//t:lb", TEI):
    ref = lb.get("facs", "")
    if ref.startswith("#") and tree.find(
            f".//t:zone[@xml:id='{ref[1:]}']", TEI) is None:
        print(f"broken facs reference: {ref}")
```

Add steps 1, 2, and 6 to your pre-commit hook. Steps 5 and 7 are worth running
manually today and scripting as your edition grows.

**The takeaway for this page:** Validators check structure, not meaning — a
conformant manifest can have every coordinate wrong, so verify regions visually.

---

## **15 Content**

**Preparing for HTR Ingestion**

Next Tuesday begins transcription, and Wednesday's HTR work ingests what you build
today. Make sure it is ingestible.

HTR platforms accept manifests by URI and import the images they reference
(eScriptorium/Kraken, 2024). For that to work:

- The manifest must be retrievable over HTTP by the platform, not merely a local file.
- Image endpoints must be publicly reachable, without authentication.
- Canvas dimensions must be declared, since layout analysis works in that space.
- The `service` block should be present so tiles can be requested efficiently.
- The manifest must be conformant, since platforms are less tolerant than viewers.

The first requirement catches people. A manifest sitting in your repository as a
local file cannot be ingested by an external platform. If you built one in
Situation B, it must be published somewhere reachable — GitHub Pages serves this
purpose adequately and is what most of you will use.

If your primary witness is Situation A, you can ingest the institution's manifest
directly, which is simpler and is the recommended route for Week 4. Reserve your
own manifest for the combined multi-witness view, which matters from Week 7.

Test ingestion today if you can. Discovering on Wednesday that a manifest cannot
be imported costs a session; discovering it now costs ten minutes.

**The takeaway for this page:** HTR platforms fetch manifests over HTTP, so a
manifest that exists only as a local file cannot be ingested.

---

## **16 Content**

**From ALTO to TEI: What Next Week Produces**

Understanding the format HTR emits tells you what Week 4 will hand you and why
today's structure matters.

ALTO XML and PAGE XML both describe a page as a hierarchy of regions, lines, and
words, each with coordinates, each carrying recognized text (eScriptorium/Kraken,
2024). Structurally this is very close to TEI's `<surface>`/`<zone>` model — which
is why conversion is a transformation rather than a re-encoding.

| ALTO element | Corresponds to | TEI equivalent |
| --- | --- | --- |
| `<Page>` | One page image | `<surface>` |
| `<TextBlock>` | A block of text | `<zone type="block">` |
| `<TextLine>` | One line, with a baseline | `<zone type="line">` |
| `<String>` | One word, with coordinates | `<w>` with `@facs` |

The coordinates in ALTO are in *image pixel* space, which is the scaling issue
from section 03 arriving in practical form. If your canvas dimensions differ from
your image dimensions, every ALTO coordinate needs scaling before it becomes a TEI
zone, and the scale factor is the ratio you recorded.

This is precisely why today's hand-built bindings matter. When you transform ALTO
output next week, you will have a small number of hand-verified zones to check the
result against. If the transformed coordinates agree with your hand measurements,
the transform is right. If they are consistently off by a constant factor, you
have found the scaling error — and you found it because you had a control.

**The takeaway for this page:** ALTO coordinates are in image pixels, so today's
hand-verified zones are the control that will catch a scaling error in next week's
transform.

---

## **17 Content**

**What Belongs in the Repository**

Consolidate the week's outputs into a structure that will still make sense in
December.

| Path | Contents |
| --- | --- |
| `images/SOURCES.md` | Manifest URLs, rights, attribution, spectral layers |
| `images/CANVASES.md` | Canvas ids, dimensions, image dimensions, scale factors |
| `images/manifest.json` | Your own manifest, if Situation B |
| `images/build_manifest.py` | The generator that produced it |
| `edition/edition.xml` | TEI with `<facsimile>` and bound transcription |
| `tools/line_uri.py` | The binding-resolution helper |
| `tools/check_facs.py` | The broken-reference checker |

Two principles govern this. Generated artefacts are committed *alongside their
generators*, so that anyone — including you in December — can see how the JSON was
produced and regenerate it. And recorded facts about external resources are
committed as documents, because external resources change and your record of what
they were at the time is the only durable evidence.

That second principle is the one students skip. A manifest URL that resolved in
September and was never written down is genuinely difficult to recover in
December, and canvas dimensions that changed after a rescan will silently
invalidate every coordinate you computed unless you recorded the originals.

Commit with a Conventional Commits message, and tag the state you submit for
today's assignment as discussed in Lesson 1.1.

**The takeaway for this page:** Commit generators alongside generated files, and
record external resources as documents because they change without notice.

---

## **18 Content**

**The Cataloguing & Metadata Assignment**

Today's assignment, due at the standard deadline, draws on Week 2 and this week
together.

Expected components:

| Component | Source | Requirement |
| --- | --- | --- |
| TEI header | Week 2 | Valid against the TEI schema |
| Manuscript description | Weeks 1–2 | Repository, shelfmark, date, material, extent, hand |
| RDF triples | Week 2 | Correctly formed; identifiers resolvable |
| Image documentation | This week | Manifest URLs, rights, attribution |
| Canvas record | This week | Ids and dimensions for every folio |
| At least one binding | Today | A `<zone>` and an `@facs` reference that resolves |
| Commit history | Weeks 1–3 | Atomic, typed, with rationale in bodies |

The last row is assessed, as Lesson 1.1 stated. A submission with correct content
and a commit log reading "updates," "more work," and "final" has not met the
course's requirements, because the process record is part of the deliverable.

The `<msDesc>` component is where the codicological vocabulary from Lesson 1.2
section 24 is exercised. Describe the object as an object: support, extent,
layout, hand, decoration, binding, provenance. Where your description differs from
the institution's catalogue, say so and say why — that divergence is a scholarly
claim and one of the more interesting things you can contribute at this stage.

Verify against the schema before submitting. An invalid header is the most common
avoidable failure on this assignment.

**The takeaway for this page:** The commit history is assessed alongside the
content, and an invalid TEI header is the most common avoidable failure.

---

## **19 Content**

**Common Errors in Today's Work**

The failures that recur, so you can recognize rather than rediscover them.

| Symptom | Cause | Fix |
| --- | --- | --- |
| Region is right place, far too large | IIIF `w,h` treated as a second corner | Use the conversion function |
| Every region offset by a constant factor | Canvas and image dimensions differ | Apply the scale factor from section 03 |
| Regions correct on one folio, wrong on others | Coordinates copied without adjusting per folio | Measure per surface |
| `@facs` resolves to nothing | Zone `xml:id` typo | Run the checker in section 14 |
| Manifest renders, images blank | Wrong image URI, or authentication required | `curl -I` each endpoint |
| No deep zoom | `service` block omitted or wrong profile | Add it; verify the level |
| Viewer shows `[object Object]` | Label given as a string, not a language map | Use `{"en": ["..."]}` |
| Validator passes, viewer shows nothing | `target` names a canvas id that does not exist | Check for typos in ids |

The second row is worth dwelling on because it is systematic rather than random.
Every region is wrong by the same ratio, which means the bindings look internally
consistent — they are all shifted and scaled together — and nothing looks obviously
broken until you compare one against the image. This is exactly the class of error
that a single hand-verified control catches immediately and that no amount of
internal consistency checking will reveal.

Check one binding visually before trusting a hundred computed ones.

**The takeaway for this page:** A scaling error makes every binding wrong by the
same ratio, so it looks internally consistent — only visual comparison catches it.

---

## **20 Content**

**Exercise: Build the Binding**

Complete the following before leaving today's meeting.

- Extract canvas ids and dimensions for every folio of your passage into `images/CANVASES.md`.
- Note the ratio between canvas and image dimensions, if they differ.
- Write the `<facsimile>` element with a `<surface>` per folio, each carrying its canvas URI.
- Measure the first three lines of your first folio and declare a `<zone>` for each.
- Transcribe those three lines, with `<lb>` elements carrying `@facs`.
- Verify each zone by constructing its Image API URL and confirming what it returns.
- Run the broken-reference checker.
- Validate the TEI against the schema.
- Commit with a Conventional Commits message and a body recording how you measured.

Three lines is deliberately small. The purpose is not volume but a verified,
understood binding you can check next week's automated output against.

If your passage's second witness is available, repeat the first two steps for it.
Week 7's collation needs both witnesses' canvas records, and gathering them now
while the procedure is fresh is cheaper than reconstructing it in October.

**The takeaway for this page:** Three verified lines are worth more than three
hundred unverified ones — the point is a control you understand.

---

## **21 Content**

**Bidirectionality and What It Enables**

A note on why the binding is worth the effort, since three lines of coordinates
can feel like a lot of work for a small return.

The binding is bidirectional. Given a line of text, a processor can find its
region; given a region, it can find the text. Neither direction is available from
a printed edition, and each supports operations that were previously impractical.

| Direction | Operation | Where it matters |
| --- | --- | --- |
| Text to image | Click a reading, see the parchment | Weeks 8, 12: apparatus and commentary |
| Image to text | Select a region, see the transcription | Weeks 4, 5: verification |
| Text to image | Reproduce the exact region in an argument | Week 12: commentary |
| Image to text | Search the text, jump to the page | Week 13: the published edition |
| Both | Align witnesses by region | Week 7: collation |

The Week 5 case is the immediate one. Reconciling your manual transcription
against HTR output means, repeatedly, asking what the manuscript actually shows at
a given point. With a binding that question is one click; without it, it is a hunt
through a facsimile. The difference determines how many uncertain readings you
actually check, which determines the quality of your ground truth, which
determines whether Week 5's error rates mean anything.

That is the recurring pattern: infrastructure that makes verification cheap raises
the standard of the work, because verification that is cheap actually happens.

**The takeaway for this page:** The binding makes verification cheap, and cheap
verification is verification that actually happens.

---

## **22 Content**

**Coordinate Stability Over the Term**

Your coordinates must survive until December, and several things can invalidate
them.

| Risk | Effect | Mitigation |
| --- | --- | --- |
| Institution rescans at new dimensions | Every coordinate wrong by a factor | Record canvas dimensions with coordinates |
| Manifest restructured; canvas ids change | Bindings resolve to nothing | Record canvas ids and access date |
| You switch to a different image source | Coordinates may not transfer | Re-verify a control region |
| Percentage versus absolute confusion | Regions in the wrong place | Use one convention; state it |
| Zone ids renumbered | `@facs` references break | Run the checker after any renumbering |

The first is the most damaging and the least detectable. If a library rescans a
manuscript and republishes with different canvas dimensions, your coordinates
silently address the wrong regions — nothing errors, and every binding continues
to resolve to *something*. The mitigation is to record the dimensions you computed
against, so that a mismatch can be detected and a correction factor applied.

Consider recording percentage coordinates alongside absolute ones for a few
control regions. Percentages survive rescaling and give you a way to recover if
absolute coordinates are invalidated:

```python
def to_percent(x, y, w, h, canvas_w, canvas_h):
    return (f"#xywh=pct:{100*x/canvas_w:.4f},{100*y/canvas_h:.4f},"
            f"{100*w/canvas_w:.4f},{100*h/canvas_h:.4f}")
```

This is defensive work, and most of you will never need it. The cost is a few
lines in a record file, and the alternative failure is silent.

**The takeaway for this page:** Record the canvas dimensions your coordinates were
computed against, because a rescan invalidates them silently.

---

## **23 Content**

**Looking Ahead: Week 4 and the Three-Step Cycle**

This week was an infrastructure week without the three-step cycle. Next week the
cycle begins in earnest, and today's work is its precondition.

| Meeting | Step | Activity | Depends on today |
| --- | --- | --- | --- |
| Tue Sep 22 (#9) | Manual | Diplomatic transcription by hand — your ground truth | Reading from the image at full zoom |
| Wed Sep 23 (#10) | Deterministic | Baseline detection and HTR training in Transkribus | Manifest ingestion |
| Fri Sep 25 (#11) | AI-assisted | LLM-assisted transcription and correction | Comparison against ground truth |

Tuesday's manual transcription is the foundation of everything measured
afterwards. It is the ground truth against which Wednesday's HTR and Friday's LLM
output are scored in Week 5, which means its accuracy determines whether those
measurements mean anything. Transcribe carefully, at full zoom, checking uncertain
readings against every available layer.

Note also that Friday September 25 is a remote delivery session. Ensure your
environment works away from campus: the manifest must be reachable, your
repository must be pushed, and your tooling must run on the machine you will
actually use.

Today's binding supports Tuesday directly. Transcribing with `<lb>` elements
already bound to zones means each line's region can be brought up as you work,
which is materially faster than locating lines by eye and substantially reduces
line-skip errors.

**The takeaway for this page:** Tuesday's manual transcription is the ground truth
that every later measurement depends on, and today's binding is what makes
transcribing accurately affordable.

---

## **24 Content**

**Publishing the Manifest**

If you authored a manifest, it must eventually be reachable at its declared `id`.
Setting this up now saves difficulty later.

The simplest route is GitHub Pages, which serves static files from your repository
over HTTPS at a predictable URL. Placing `manifest.json` in a `docs/` directory and
enabling Pages makes it available at
`https://<username>.github.io/<repository>/manifest.json`.

Two requirements are specific to IIIF and are easy to miss:

The `id` in the manifest must equal the URL at which it is served. A manifest
declaring one `id` and living at another is non-conformant, and some viewers
reject it. Set the `id` from the publication URL in your generator rather than
hard-coding a placeholder.

CORS headers must permit cross-origin requests, or viewers hosted elsewhere cannot
load it — the accidental-silo failure from Lesson 3.1 section 27, this time
produced by you. GitHub Pages sets permissive CORS headers by default, which is
one reason to prefer it over hosting you configure yourself.

| Host | Suitable | Note |
| --- | --- | --- |
| GitHub Pages | Yes | Free, HTTPS, permissive CORS by default |
| Netlify or Vercel | Yes | Free tiers; CORS configurable |
| University web space | Usually | Confirm HTTPS and CORS |
| A local file | No | Not retrievable by viewers or HTR platforms |

Test by loading the published URL into Mirador from a different machine. If it
renders, it is genuinely reachable; if it renders only locally, something is
serving it that will not be available in Week 13.

**The takeaway for this page:** The manifest's `id` must equal its actual URL, and
CORS must permit cross-origin loading or only your own machine can use it.

---

## **25 Content**

**The Week in the Arc of the Course**

Situating this week within the whole, now that it is complete.

Week 1 established how work is *recorded* — version control, atomic commits,
provenance. Week 2 established how the manuscript is *described* — the TEI header,
metadata, RDF. Week 3 established how the manuscript is *seen* — image delivery,
imaging techniques, coordinate binding.

Those three are the infrastructure. Everything remaining is the edition itself,
and each layer attaches to what this week built:

| Week | Layer | Attaches via |
| --- | --- | --- |
| 4 | Transcription | Zones bound to lines |
| 5 | Reconciliation | Comparison against the image |
| 6 | Normalization | `<orig>`/`<reg>` over bound text |
| 7 | Collation | Witnesses aligned by canvas region |
| 8 | Apparatus | Variants anchored to regions in each witness |
| 9 | Lemmatization | Linguistic annotation over bound text |
| 11 | Alignment | Translation aligned to bound text |
| 12 | Commentary | Argument citing exact regions |
| 13 | Publication | Viewer over the manifest and TEI |

Read down the "attaches via" column and the point is visible: nearly every entry
refers to something established this week. The canvas coordinate space is what the
entire edition hangs on, which is why an infrastructure week sits this early and
why today's small binding exercise matters more than its size suggests.

**The takeaway for this page:** Nearly every remaining layer of the edition
attaches to the canvas coordinate space built this week.

---

## **26 Content**

**Interoperability as a Scholarly Value**

A closing conceptual point, returning to where Tuesday began.

IIIF is a technical standard, but the argument for it is not primarily technical.
Standards make cooperation possible without coordination. The Vatican did not
negotiate with Leipzig about how to make their manuscripts comparable; both
implemented the same specification, and comparability followed (Griffin, 2023).

This has a scholarly analogue that is worth making explicit. Citation conventions,
critical sigla, and the apparatus criticus are all standards in the same sense:
they let scholars who have never communicated read one another's work precisely.
An edition using idiosyncratic sigla with no key is exactly analogous to an image
in a proprietary viewer — the content exists and cannot be used by anyone else.

Your edition should be interoperable in both senses. Its images should be
addressable by standard URIs; its encoding should follow TEI rather than a private
scheme; its metadata should use shared vocabularies; its identifiers should be
resolvable. None of this is about convenience. It is about whether your work can
be used by anyone who did not build it — which is a reasonable definition of
whether it is scholarship at all.

Clausen et al. (2026) make the same argument for research data: heterogeneous
analyses of a manuscript are worth far more when they can be related to one
another than when each sits in its own repository, and relating them requires
shared standards rather than shared institutions.

**The takeaway for this page:** Standards let scholars cooperate without
coordinating, and an edition that only its author can use is not yet scholarship.

---

## **27 Content**

**A Checklist Before You Leave**

Verify each item now rather than assuming it.

- Manifest URLs for both witnesses recorded in `images/SOURCES.md`.
- Rights statement and required attribution recorded for each.
- Canvas ids and dimensions for every folio in `images/CANVASES.md`.
- Canvas-to-image scale factor noted where they differ.
- `<facsimile>` written, with one `<surface>` per folio carrying its canvas URI.
- At least three `<zone>` elements declared with measured coordinates.
- At least three `<lb>` elements carrying `@facs` references.
- Each zone verified by opening its Image API URL.
- Broken-reference checker run and clean.
- TEI validated against the schema.
- Manifest validated, if you authored one.
- Manifest published and reachable, if you authored one.
- Everything committed with typed messages and informative bodies.
- Submission state tagged.
- Cataloguing & Metadata Assignment submitted.

The item most often skipped is the eighth, and it is the one that catches the
errors the others cannot. Structural validation confirms your document is
well-formed; only opening the image confirms your coordinates mean what you
intended.

**The takeaway for this page:** Verify zones by opening their Image API URLs —
structural validation cannot tell you whether a coordinate is right.

---

## **28 Content**

**If Your Manuscript Lacks IIIF**

A contingency, since a minority of you will find your chosen manuscript is not
served through IIIF at all.

Options, in order of preference:

| Option | Approach | Cost |
| --- | --- | --- |
| Find another digitization | The same manuscript elsewhere, or a IIIF-served witness | Low; often available |
| Build a Level 0 service | Generate a static tile pyramid from downloaded images | Moderate; needs permission |
| Use plain images with TEI zones | `<graphic>` and `<zone>` without canvas URIs | Low; loses deep zoom |
| Change witnesses | Select a different manuscript | High this late; possible |

The second deserves explanation. A Level 0 IIIF service can be generated from
ordinary images with a tool such as `iiif_static.py`, producing a directory of
pre-rendered tiles that can be served as static files from GitHub Pages. This
gives genuine deep zoom without running a server. The constraint is that it
requires a downloaded copy of the images, which requires the licence to permit it
— so check `rights` before going this route.

The third option is a legitimate fallback. TEI's `<facsimile>` model works with
plain images: `<graphic>` points at an image file and `<zone>` gives coordinates
in its pixel space. You lose deep zoom and interoperability, and you keep the
coordinate binding, which is the part the rest of the course depends on.

Raise this today if it applies to you. It is workable, but it changes what Week 13
can publish and is much easier to address now than in November.

**The takeaway for this page:** Without IIIF you can still bind coordinates using
plain images and TEI zones — you lose deep zoom, not the binding the course depends
on.

---

## **29 Content**

**What Good Work Looks Like Here**

A standard to measure your own submission against, since "valid" and "good" are
different.

A minimally acceptable submission has a valid TEI header, records the manifest
URL, and demonstrates one working binding.

A good submission additionally:

- Describes the manuscript in its own terms, noting where the description diverges from the institution's catalogue and why.
- Records image provenance completely, including any spectral layers and what they show.
- Documents the coordinate system used and the canvas-to-image relationship.
- Verifies bindings visually and says so in the commit record.
- Identifies the least legible regions of the passage and assesses what would be needed to resolve them.
- Carries a commit history in which each decision is a typed commit with rationale.
- Notes what was attempted and did not work, including negative results.

The last two are what distinguish scholarship from completion. An edition that
records only successes presents a false picture of how it was made, and the
failures are frequently the more informative record — they tell a later reader
what has already been tried.

This is the standard the whole course is oriented toward. The assignments are
occasions for producing a defensible scholarly artefact, and the criterion is
whether a reader can evaluate your claims from what you have recorded.

**The takeaway for this page:** A good submission records divergences, negative
results, and the reasoning behind decisions — not only what worked.

---

## **30 Content**

**Synthesis: The Coordinate Space as the Edition's Spine**

Three meetings have built one thing: a coordinate space that everything else
attaches to.

Tuesday established that images become scholarly resources when they are
*addressable* — when any region of any folio can be requested by a rule anyone can
apply, and when structure is described in a shared vocabulary so any viewer can
render it. The canvas emerged as the central abstraction: not a picture, but a
coordinate space standing for the page (IIIF Consortium, 2020).

Wednesday established what the images are. They are instruments' outputs, not
photographs — sometimes showing more than the eye could see under any
illumination, always requiring documentation of how they were produced before they
can be evaluated as evidence (Easton et al., 2003; Malzbender et al., 2001).

Today bound the two to the text. `<surface>` to canvas, `<zone>` to region,
`@facs` from transcription to zone — a chain that lets a reading and its evidence
be brought together in one click, in either direction (TEI Consortium, 2026).

What remains is to build the edition on that spine. Every subsequent layer —
transcription, normalization, collation, apparatus, lemmatization, translation,
commentary — attaches to the same coordinates, which is what will make them one
object rather than seven documents about the same manuscript (Clausen et al.,
2026).

**Due today.** The Cataloguing & Metadata Assignment, per section 18.

**For Tuesday.** Week 4 begins the three-step cycle with manual diplomatic
transcription — your ground truth for everything measured thereafter. Come with
your bindings working and your images loading at full zoom.

**The takeaway for this page:** The canvas coordinate space is the spine of the
edition; every layer from transcription to commentary attaches to it, which is what
makes them one object.

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

Malzbender, T., Gelb, D., & Wolters, H. (2001). *Polynomial texture maps*.
Hewlett-Packard Laboratories.

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/
