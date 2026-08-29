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

**Takeaway:** Today's artefact links each transcribed line to the
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

**Takeaway:** Authoring a manifest does not mean hosting images
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

**Takeaway:** Record canvas ids, canvas dimensions, and image
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

**Takeaway:** Bind a few regions by hand today so that you can
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

**Takeaway:** `<facsimile>` describes surfaces and zones
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

**Takeaway:** TEI names two corners and IIIF names a corner plus
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

**Takeaway:** `@facs` on `<pb>` and `<lb>` binds transcription to
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

**Takeaway:** Put the canvas URI on `<surface>` and record
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

**Takeaway:** Verify every binding by constructing the Image API
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

**Takeaway:** Generate manifests from a script rather than
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

**Takeaway:** Include the `service` block or deep zoom will not
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

**Takeaway:** A `Choice` expresses spectral alternatives on one
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

**Takeaway:** A range identifies your passage within the full
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

**Takeaway:** Validators check structure, not meaning — a
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

**Takeaway:** HTR platforms fetch manifests over HTTP, so a
manifest that exists only as a local file cannot be ingested.

---

