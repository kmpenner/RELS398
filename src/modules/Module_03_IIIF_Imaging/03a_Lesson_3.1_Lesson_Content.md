# Lesson 3.1 — Manual Imaging, TEI Facsimile, and Document Autopsy

*RELS 398 / ENGL 398 · Topic 3: IIIF Imaging · Meeting #6 (Tue Sep 15)*

***Step 1 of the three-step cycle: manual.** Your header describes your document. This lesson attaches the picture — the TEI elements that hold an image, and what it takes to make an image worth holding.*

---

## **01 Content**

**From Text to Image: Why Digital Editions Require Facsimiles**

An edition that gives only a transcription asks the reader to take the editor's word for it. Every expanded abbreviation and every doubtful letter is a decision, and in print the reader could only check it by travelling to the archive.

Putting the image beside the text changes that. A reader can look at the stroke themselves and decide whether it is a mark of punctuation or a spot of ink.

This is the argument for facsimiles: they turn your claims into something checkable.

One caution to carry through the lesson. A photograph is not the object. It was made with particular light, at a particular angle, with particular settings — all of which you should record.

**Vocabulary.** *Facsimile* — a visual reproduction of a document. *Surrogate* — a digital stand-in used instead of the original.

**Takeaway:** Publishing the image alongside the transcription lets readers check editorial decisions, turning assertions into evidence.

---

## **02 Content**

**The TEI `<facsimile>` Element: Structure and Placement**

TEI holds images in a `<facsimile>` element, and where it sits is the first thing to learn:

```xml
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>  <!-- describes the document --> </teiHeader>
  <facsimile>  <!-- the images of its surfaces --> </facsimile>
  <text>       <!-- the transcription --> </text>
</TEI>
```

Three siblings, in that order. `<facsimile>` is not inside the header and not inside the text.

The reason is conceptual rather than technical. A page exists whether or not anyone has transcribed it. Photographs of a blank leaf, an illegible fragment, or a drawing are all legitimate, so TEI keeps the physical surfaces separate from the words.

Putting the block in the wrong place is the most common first error, and the schema will tell you immediately.

**Vocabulary.** *Element* — a tagged unit of XML. *Sibling* — an element at the same level as another.

**Takeaway:** `<facsimile>` sits between `<teiHeader>` and `<text>` as their sibling, keeping physical surfaces separate from transcription.

---

## **03 Content**

**Modeling Surfaces: The `<surface>` Element**

Inside `<facsimile>`, each physical writing face is one `<surface>`.

"Face" is literal. The front of a leaf is one surface and the back is another, even though they are one piece of paper. A single-sheet decree has two. An envelope kept with a letter is another again.

```xml
<surface xml:id="p1r">
  <graphic url="images/p1r.jpg"/>
</surface>
```

The `@xml:id` is what makes the surface usable: it is the name other parts of your file will point at. Without it the surface is invisible to the rest of the edition.

Choose ids you can still read in December — `treaty_sheet1_recto` rather than `s1` — and remember they cannot begin with a digit.

**Vocabulary.** *Surface* — one physical writing face. *xml:id* — a unique name allowing other elements to refer to this one.

**Takeaway:** Each physical face of the object is one `<surface>` with an `xml:id`, which is the handle everything else uses to point at it.

---

## **04 Content**

**Coordinates and Space: Declaring Coordinate Systems in `<surface>`**

To mark regions, the surface needs a coordinate system, declared with four attributes:

```xml
<surface xml:id="p1r" ulx="0" uly="0" lrx="4800" lry="6400">
```

Read as upper-left x, upper-left y, lower-right x, lower-right y. Here: origin at the top-left, and the image is 4800 pixels wide by 6400 tall.

Two things trip people up. First, **y increases downward**, unlike the graphs you learned in mathematics. Second, these are **corners**, not width and height — a mistake that silently doubles the size of every region you mark.

The numbers describe one specific image file. Crop or resize that file later and every coordinate you wrote becomes wrong, which is why processing comes before measuring.

**Vocabulary.** *Coordinate system* — the numbering used to locate points in an image. *Origin* — the (0,0) point, here the top-left corner.

**Takeaway:** `ulx/uly/lrx/lry` are corners with the origin at top-left and y increasing downward, and they describe one particular image file.

---

## **05 Content**

**Defining Regions: The `<zone>` Element**

A `<zone>` marks a region inside a surface, using the same four corner attributes.

```xml
<surface xml:id="p1r" ulx="0" uly="0" lrx="3000" lry="4500">
  <graphic url="images/p1r.jpg"/>
  <zone xml:id="z_head" type="heading" ulx="450" uly="200" lrx="2550" lry="450"/>
  <zone xml:id="z_sig"  type="signature" ulx="1800" uly="3900" lrx="2700" lry="4200"/>
</surface>
```

`@type` says what kind of thing the region is, and choosing it is an editorial act: calling something a *correction* rather than a *blot* is a claim about the document.

For shapes that are not rectangles — a seal, a diagonal note — use `@points` with a list of `x,y` pairs instead.

Zones are where your reading of the page becomes machine-readable. Mark what matters, not everything.

**Vocabulary.** *Zone* — a defined region within a surface. `@points` — an attribute holding a list of coordinates for irregular shapes.

**Takeaway:** Zones mark meaningful regions inside a surface, and the `@type` you assign is an interpretive claim about the document.

---

## **06 Content**

**Grouping Features: The `<surfaceGrp>` and Sub-surfaces**

Some objects are not a flat list of faces, and TEI offers two ways to say so.

`<surfaceGrp>` groups related surfaces — the two pages visible in an opening, the four faces of a folded bifolium, the sheets of a fold-out map:

```xml
<surfaceGrp type="opening" n="1">
  <surface xml:id="f1v">…</surface>
  <surface xml:id="f2r">…</surface>
</surfaceGrp>
```

A `<surface>` can also sit inside another. That models attachment: a slip pasted over a corrected clause, a label stuck to a broadside, a note pinned to a letter. The slip has its own coordinates and its own place on the parent page.

If your object is a single sheet, you need neither. Recognize them so you can read other people's editions.

**Vocabulary.** *Bifolium* — a sheet folded to make two leaves. *Opening* — the two pages visible when a book lies open.

**Takeaway:** `<surfaceGrp>` groups related faces and nested surfaces model attached slips, preserving how an object is physically assembled.

---

## **07 Content**

**Linking Facsimile to Text: The `@facs` Attribute**

Coordinates on their own are just a map. The link to the transcription is the `@facs` attribute, which any element in `<text>` may carry.

```xml
<body>
  <pb facs="#p1r" n="1"/>
  <p>
    <lb facs="#z_line1" n="1"/>To the Honourable the Council
    <lb facs="#z_line2" n="2"/>The Humble Petition of John Bushell
  </p>
</body>
```

The `#` is required: it means "the element with this id".

Notice the two scales. `<pb>` says the following text is on that whole surface; each `<lb>` points at one line's zone. You can be as precise as your zones allow.

This is what makes an edition interactive — hover a line, highlight the strokes — and the schema cannot check that your pointer leads anywhere. Verify those by eye.

**Vocabulary.** `@facs` — the attribute linking text to a surface or zone. *pb / lb* — page-beginning and line-beginning markers.

**Takeaway:** `@facs` links any text element to a surface or zone by its id, and nothing but your own checking confirms the target exists.

---

## **08 Content**

**Two-Way Alignment: `<zone>` Pointing to Text and Text Pointing to `<zone>`**

Editions differ in what they are built around. A poem is organized by its text; an inscription or an annotated charter is often organized by the object.

TEI supports both directions. Text can point into the image with `@facs`, and a zone can point back into the text with `@corresp`:

```xml
<zone xml:id="z_colophon" type="colophon" corresp="#txt_colophon"
      ulx="300" uly="2800" lrx="1900" lry="3150"/>
```

Two-way linking matters when the page will not behave. A gloss wrapping around three sides of a text block, or an addition squeezed between lines, has a reading position and a physical position that do not match. Linking both ways lets you record each without distorting the other.

**Vocabulary.** `@corresp` — an attribute recording that two elements correspond. *Colophon* — a closing note giving details of production.

**Takeaway:** Text can point at zones and zones at text, so an edition can be organized around either the words or the object.

---

## **09 Content**

**The Materiality of the Witness: Media Diversity Across History**

The second half of this lesson is about making the image in the first place. It starts with a fact that photography makes easy to forget: documents are physical things, made of different stuff.

Parchment is animal skin, and it cockles and stiffens with humidity. Papyrus is plant fibre in two crossed layers, and it frays. Rag paper carries chain lines and watermarks, and foxes with age. Stone and metal carry no ink at all — the text is a shape cut into a surface.

Material dictates method. Light that reveals ink on paper can make an inscription vanish, and a technique that saves a faded letter can damage a fragile one.

So digitization begins with a question: what is this thing made of, and what has time done to it?

**Vocabulary.** *Witness* — a surviving copy of a text. *Cockling* — the rippling of parchment or paper with moisture.

**Takeaway:** Every material behaves differently under light and handling, so capture method follows from what the object is made of.

---

## **10 Content**

**Epigraphs and Inscriptions: Stone, Metal, and Three-Dimensional Surfaces**

An inscription has no ink. Its text is depth: grooves cut into stone, letters stamped into bronze.

Photograph it head-on with a flash and the text disappears. Flat light fills the grooves evenly, so there is no contrast between the cut and the surface, and the letters vanish into the stone's own mottling.

The solution is shadow. Light the surface from a shallow angle — **raking light** — and each groove casts a dark line beside a bright edge. The text appears because you made it cast shadows.

Conditions are rarely ideal: stelae are heavy, weathered, and fixed where they stand, so this is portable-lamp work in a gallery or a field, usually with several exposures from different directions.

**Vocabulary.** *Epigraphy* — the study of inscriptions. *Raking light* — light directed across a surface at a shallow angle.

**Takeaway:** Inscriptions are read through shadow, so they require light raked across the surface rather than aimed at it.

---

## **11 Content**

**Papyri, Ostraca, and Fragile Organic Supports**

Papyrus is fibrous and brittle, and it presents three specific problems.

**Fibres** run horizontally on one side and vertically on the other, producing a texture that mimics broken strokes. Diffuse light keeps the fibre shadows down.

**Glass.** Most papyri are conserved between glass plates and cannot be taken out. Photographing through glass means reflections, solved with polarizing filters on the lights and the lens.

**Ink.** Carbon ink does not fade chemically, but it flakes off physically, so the surface must never be rubbed or brushed.

Ostraca — potsherds used for receipts and notes — add curvature, which means part of the surface will be out of focus unless the aperture is chosen for depth.

**Vocabulary.** *Ostracon* — a pottery fragment used as a writing surface. *Polarizing filter* — a filter that blocks reflected glare.

**Takeaway:** Papyri need diffuse light for fibre texture and polarizers for their protective glass, and their ink flakes rather than fades.

---

## **12 Content**

**Scrolls and Rotuli: Continuous Writing Surfaces**

A scroll breaks the assumption behind every camera setup: that a document is a page.

It is a continuous membrane, sometimes metres long, made of sheets joined at seams, written in columns across (a *volumen*) or down (a *rotulus*).

Two approaches: photograph it in overlapping sections and keep them as a sequence, or photograph with measured overlap and stitch the frames into one long image.

The conservation problem is memory. An old roll holds its curl, and forcing it flat cracks fibres and detaches ink. Conservators unroll a short section at a time in a cradle with soft weights, leaving the rest supported.

In TEI you can model a scroll as one long surface with a zone per column, or as a sequence of surfaces for the joined sheets.

**Vocabulary.** *Volumen / rotulus* — a horizontal or vertical scroll. *Stitching* — combining overlapping photographs into one image.

**Takeaway:** Scrolls are captured in overlapping sections under tension-relieving support, never flattened whole.

---

## **13 Content**

**Codices, Manuscripts, and Bound Books: Structure and Gutter Shadows**

A bound book is a mechanism — leaves, sewing, glue, boards — and it resists being photographed flat.

The trouble sits in the **gutter**, the inner margin at the spine. When a volume will not open fully, the page curves in toward the sewing, which does two things: text near the spine compresses and distorts, and the overhead light cannot reach in, so the inner margin falls into shadow.

The wrong fix is to press the book flat under glass. That breaks sewing, cracks spines, and tears gatherings, and it is unacceptable regardless of how good the resulting image is.

The right fix is a cradle holding the volume at a limited opening angle, typically 90 to 110 degrees, with the camera moved instead of the book.

**Vocabulary.** *Gutter* — the inner margin where leaves meet the spine. *Cradle* — a support holding a book open safely.

**Takeaway:** Bound volumes are photographed in a cradle at a limited opening angle; forcing one flat to remove gutter shadow damages the binding.

---

## **14 Content**

**Broadside Documents, Maps, Prints, and Oversize Sheets**

Single sheets — decrees, proclamations, treaties, maps, letters — escape the gutter problem and bring their own.

**Size.** A large map may not fit the frame. Backing away to include it all reduces resolution until fine detail is unreadable. The alternatives are a higher-resolution camera or photographing in overlapping tiles and stitching them.

**Flatness.** Sheets that lived folded do not lie flat. Creases cast shadows and curled edges go out of focus. Use soft weights in blank margins; never tape, pins, or heavy glass.

**Description.** Be careful with vocabulary in your header: a printed broadside has no quires and no scribal hand, and `<objectDesc form="sheet">` is more honest than forcing codex terms onto it.

**Vocabulary.** *Broadside* — a document printed on one side of a single sheet. *Snake weight* — a soft covered weight used to hold pages down.

**Takeaway:** Oversize sheets need tiled capture or higher resolution and gentle flattening, and they should be described as sheets rather than as codices.

---

## **15 Content**

**Document Handling and Preservation Ethics in the Studio**

One rule outranks every other in this lesson: **the object matters more than the photograph.** A failed capture can be repeated. A torn leaf cannot.

Practical form:

- **Clean, dry hands** are now preferred to cotton gloves for paper and parchment. Gloves dull your touch and make tearing more likely. Gloves are for metal, photographic prints, and anything a fingerprint would corrode.
- **Nothing that can catch.** Rings, bracelets, dangling lanyards, and ID cards all snag.
- **Never force.** If a binding resists, stop and change the support.
- **Nothing wet or sharp** near the table — no drinks, no pens. Pencil only.

Turn a leaf from the middle of its outer edge, supporting it as it moves, rather than flicking a corner.

**Vocabulary.** *Conservation* — the practice of preserving objects from damage. *Handling protocol* — the agreed rules for touching an object.

**Takeaway:** Preservation outranks capture: clean hands, no snagging jewellery, no forcing, and deliberate page turns.

---

## **16 Content**

**Supporting the Binding: Book Cradles, Foam Wedges, and Straps**

A **cradle** is what makes photographing a bound book safe. It holds the volume at a fixed, gentle angle and supports the whole leaf rather than letting it hang.

Good cradles adjust as you work: as pages turn, one side gets thicker, and the supports move to keep the page you are photographing at the same height and angle.

Without one, foam wedges and soft supports improvised for the specific volume will do — provided the book never sags at the joint.

To hold a curling page still, use clear polyester strips or soft covered weights, placed in blank margins only, with the least pressure that works.

What never touches the object: rubber bands, adhesive tape, paperclips, and anything abrasive.

**Vocabulary.** *Foam wedge* — a shaped support holding a volume at an angle. *Joint* — the hinge where the cover meets the spine.

**Takeaway:** Cradles and wedges support the whole leaf at a safe angle, and only inert strips or soft weights in blank margins hold pages still.

---

## **17 Content**

**Camera Geometry: Sensor Alignment, Focal Plane, and Lens Selection**

Good document photography is mostly geometry.

**Keep the camera parallel to the page.** If it tilts, the rectangle photographs as a trapezoid — **keystoning** — and straight lines bow. That ruins measurement, and your zones will no longer fit the text. A spirit level, or a small mirror on the page showing the lens back to itself, confirms alignment.

**Centre the lens** on the middle of the page, not off to one side.

**Use a flat-field or macro lens if you have one.** Ordinary zoom lenses bend straight lines near the frame edge.

**Choose a middle aperture**, around f/8 to f/11. Wide open, the edges of a slightly curved page blur; stopped fully down, the whole image softens.

With a phone: no digital zoom, and hold it square to the page.

**Vocabulary.** *Keystoning* — the trapezoid distortion caused by tilting the camera. *Aperture* — the lens opening, which controls depth of field.

**Takeaway:** Keep the sensor parallel and centred and use a middle aperture, because tilt distorts every coordinate you later measure.

---

## **18 Content**

**Controlled Illumination: Balanced Studio Lighting and Glare Reduction**

Lighting decides whether an image is usable.

The standard arrangement is two matched lights, one on each side, at about 45 degrees to the page, at equal distance and equal power. Matching them is what cancels shadows and gives an even field across the page.

Test it cheaply: photograph a blank grey sheet and look at the corners against the centre. Visible falloff means the lights are uneven.

**Glare** is the other enemy — on glossy paper, fresh ink, gilding, or a mylar sleeve. Moving the lights helps. When it does not, **cross-polarization** does: polarizing filters on the lights, another on the lens, rotated until the reflection disappears while the text stays.

Improvised version: window light with a white sheet as a diffuser, and a piece of card reflecting light back from the shadow side.

**Vocabulary.** *Diffuse light* — soft light from a broad source. *Cross-polarization* — using paired polarizing filters to remove reflections.

**Takeaway:** Two matched lights at 45 degrees give an even field, and cross-polarization removes glare that repositioning cannot.

---

## **19 Content**

**Flatbed and Overhead Planetary Scanners: Mechanics and Constraints**

Two kinds of scanner, with very different uses.

A **flatbed** scans from below, through glass, with the document face down. It gives even light and consistent geometry, and it is fine for a modern loose sheet. It is forbidden for bound volumes and fragile material: putting a book face down means pressing the spine, and dragging a flaking surface across glass abrades it.

An **overhead (planetary) scanner** works the other way: the document lies face up, supported, and the scanning head and lights are above. Better models include a cradle and a glass bar that lowers with controlled pressure.

The general rule: face down on glass is for stable modern sheets; everything historical is photographed or scanned face up.

**Vocabulary.** *Flatbed scanner* — a scanner with a glass platen, used face down. *Planetary scanner* — an overhead scanner for face-up capture.

**Takeaway:** Flatbeds suit stable loose sheets only; bound and fragile material must be captured face up on a support.

---

## **20 Content**

**Metric Calibration: Scale Bars and Spatial Resolution (DPI / PPI)**

A pixel has no size. An image 3,000 pixels wide could be a stamp or a wall.

So every capture should include a **scale bar** — a ruler with clear millimetre marks, laid beside the document at the same height as its surface, inside the frame. From it, anyone can measure letter heights, margins, and the size of a tear.

Height matters: a ruler resting on the table while the page sits raised in a cradle will measure wrongly.

**Resolution** is how many pixels cover one inch of the object. Common archival targets are 300 ppi for printed material, 400–600 for manuscripts and detailed hands, and higher for tiny script or fine engraving.

Record the figure. It belongs with your image and in your header.

**Vocabulary.** *Scale bar* — a ruler included in the frame for measurement. *PPI* — pixels per inch of the physical object.

**Takeaway:** A coplanar scale bar gives pixels a physical size, and the resulting resolution figure should be recorded with the image.

---

## **21 Content**

**Color Fidelity: Color Calibration Targets and Color Management**

Colour in a photograph depends on the light it was taken in, and cameras disagree with each other and with your eye.

For scholarship this is not cosmetic. If your image is yellow, no reader can tell whether the paper aged or your lamp was warm — and paper colour is evidence.

The remedy is to photograph a **colour target**: a printed card of patches whose true values are known, including a neutral grey. One frame with the target, at the start of each lighting setup, lets software correct every later frame by comparison.

The grey patch alone fixes the overall cast; the full target lets the software build a **profile** correcting that camera under that light.

Minimum viable version: include a grey card. It costs nothing and makes correction possible later.

**Vocabulary.** *Colour target* — a card of patches with known colour values. *Colour profile* — a file describing and correcting a device's colour behaviour.

**Takeaway:** Photograph a colour or grey reference under each lighting setup so ageing can later be distinguished from illumination.

---

## **22 Content**

**Environmental Stability: Temperature, Relative Humidity, and Light Exposure**

Photography exposes an object to heat, light, and a room that may not suit it.

Parchment and paper absorb and release moisture. Dry air makes parchment contract and cockle and can flake ink; damp air invites mould. Archives therefore hold about 18–22°C and 45–55% relative humidity, and a reading room's rules exist for this reason, not to be difficult.

Light is the other risk. Old tungsten and halogen lamps produce heat that dries and curls a leaf within minutes. Modern LED panels emit little heat and no useful ultraviolet, which is why they are standard.

Total exposure counts too: switch lights off while you set up and turn pages, and on only to shoot.

**Vocabulary.** *Relative humidity* — how much moisture the air holds relative to its capacity. *Hygroscopic* — readily absorbing moisture.

**Takeaway:** Stable humidity and cool LED light protect the object; keep the lamps off except during the exposure itself.

---

## **23 Content**

**The Electromagnetic Spectrum in Manuscript Autopsy**

The remaining sections are about seeing what ordinary light cannot show, and they rest on one fact: your eyes use a narrow band, roughly 400 to 700 nanometres, of a much wider spectrum.

Materials respond differently across that spectrum. Light striking a surface may be reflected, absorbed, or passed through — and some materials **fluoresce**, absorbing invisible high-energy light and re-emitting it as visible light.

Crucially, different inks and supports respond differently from one another. Carbon ink, iron-gall ink, and parchment each have their own pattern.

That is the entire principle behind what follows. Where ink has faded into the page in visible light, a wavelength your eye cannot use may still separate them.

**Vocabulary.** *Wavelength* — the measure distinguishing kinds of light, in nanometres. *Fluorescence* — re-emission of absorbed light at a visible wavelength.

**Takeaway:** Inks and supports respond differently across the spectrum, so invisible wavelengths can separate what visible light has merged.

---

## **24 Content**

**Raking Light: Revealing Dry-Point, Ruling, and Surface Topography**

Not all evidence is ink. Scribes ruled guidelines with a hard point, pricked margins to lay them out, and readers scratched notes with a stylus. Bindings and seals leave impressions. Erasures leave scraped texture.

None of it has colour, so straight-on light shows nothing.

**Raking light** is the fix, and it needs no special equipment: put a lamp almost level with the surface, at 5 to 15 degrees, and each depression casts a shadow on one side and catches a highlight on the other.

Direction matters. Light from the top reveals horizontal ruling; light from the side reveals vertical pricking. Shoot several exposures from different angles.

This is the cheapest technique in the lesson and often the most revealing, and it is entirely non-destructive.

**Vocabulary.** *Dry-point* — writing scratched without ink. *Ruling* — guide lines laid out for writing.

**Takeaway:** Raking light from several directions reveals inkless evidence — ruling, pricking, scratched notes, and erasures.

---

## **25 Content**

**Reflectance Transformation Imaging (RTI): Mathematical Surface Normal Modeling**

Raking light gives one photograph from one angle. **RTI** gives the surface from every angle at once.

The method is simple to describe. The camera stays fixed above the object. A shiny black sphere sits beside it. An operator fires a light from dozens of positions around the object, one exposure each. The reflection on the sphere tells the software exactly where the light was.

From that set, the software calculates how each point on the surface is tilted, and builds a model you can relight interactively — moving a virtual light around the object on screen, long after you have left the room.

It can also exaggerate the shape, stripping away colour to show topography alone, which makes very shallow traces readable.

**Vocabulary.** *RTI* — imaging that captures how a surface responds to light from many directions. *Relighting* — changing the light direction after capture.

**Takeaway:** RTI captures dozens of exposures with known light positions, producing a surface you can relight and exaggerate afterwards.

---

## **26 Content**

**Ultraviolet (UV) Fluorescence: Recovering Erased Iron-Gall Inks and Palimpsests**

Parchment was expensive, so scribes scraped old texts away and wrote again. The result is a **palimpsest**: a lower, erased text beneath an upper one.

Scraping rarely removes everything. Iron-gall ink bites into the skin, and traces of iron remain in the fibres.

Under ultraviolet light, parchment glows — it fluoresces a pale blue-green. The residual iron does not, and it also suppresses the glow around it. So the erased writing appears as dark strokes against a luminous page: the text returns not because the ink is visible, but because the parchment around it lights up.

Practically, this needs a UV source and a filter on the lens so the camera records the glow rather than the UV itself. It also needs care: UV is energetic, so keep exposure short.

**Vocabulary.** *Palimpsest* — a manuscript reused after its first text was erased. *Iron-gall ink* — ink made from oak galls and iron salts.

**Takeaway:** Under UV, parchment fluoresces while residual iron-gall ink does not, so erased text reappears as dark strokes on a glowing page.

---

## **27 Content**

**Infrared (IR) Reflectography: Penetrating Over-Inking, Soot, and Pigments**

Infrared sits at the other end: wavelengths longer than visible light, which behave as if some materials were not there.

Carbon ink absorbs infrared completely and stays black. Iron-gall ink, many organic dyes, stains, and soot become transparent.

That difference has three classic uses. Text crossed out in a different ink can reappear when the covering ink turns transparent. Documents damaged by fire can be read through surface soot. And in illuminated manuscripts, infrared passes through paint layers to show the artist's underdrawing.

The equipment is the obstacle: ordinary cameras contain a filter blocking infrared, so this needs a converted camera and an infrared-pass filter. Some conservation labs and university imaging centres have one.

**Vocabulary.** *Infrared reflectography* — imaging with infrared light to see through certain materials. *Underdrawing* — a preparatory drawing beneath paint.

**Takeaway:** Infrared keeps carbon ink black while many stains and covering inks turn transparent, revealing censored, sooted, or underdrawn text.

---

## **28 Content**

**Multispectral and Hyperspectral Imaging: Multi-Band Capture and Spectral Stacks**

**Multispectral imaging** combines the previous three sections into one method. Instead of choosing a wavelength, the system photographs the page many times, each under a different narrow band from ultraviolet through visible to infrared, always from the same fixed position.

The result is a stack of aligned images. Every point on the page now has a set of measurements describing how it responds across the spectrum — and different inks have different signatures.

Software compares the layers and combines them to maximize the difference between two materials, producing a composite in which erased writing separates from the text above it.

This is the strongest non-destructive recovery method there is, used on the Archimedes Palimpsest and the Dead Sea Scrolls. It is also specialist equipment — the point is knowing it exists, so that "illegible" can mean "not yet imaged properly".

**Vocabulary.** *Multispectral imaging* — capturing aligned images across many narrow wavelength bands. *Spectral signature* — the pattern of a material's response across the spectrum.

**Takeaway:** Multispectral imaging measures how every point responds across many wavelengths, letting software separate inks that visible light merges.

---

## **29 Content**

**Archival Capture Workflows: From Sensor to Unprocessed Master**

Good technique is wasted if the files are handled carelessly. Four habits:

**Shoot raw if you can.** A raw file holds the sensor's own data before the camera makes decisions about colour and contrast, leaving them open to you.

**Keep an untouched master.** Convert to an uncompressed TIFF, store it, and never edit it in place. Everything else is generated from it.

**Keep the technical metadata.** The camera records shutter speed, aperture, and lens inside the file. Do not strip it, and record separately what the file cannot know: who shot it, what lighting, which target.

**Name files systematically.** `nsarm_rg1_v430_no2_r.tif` will still make sense in December. `IMG_4829.jpg` will not.

This is the same discipline as your Git repository, applied to pixels: keep the original, record what you did.

**Vocabulary.** *Raw file* — unprocessed sensor data from the camera. *Master* — the authoritative file all derivatives come from.

**Takeaway:** Shoot raw, keep an unedited TIFF master with its metadata intact, and name files so they identify themselves.

---

## **30 Content**

**The Digital Surrogate: Integrating Physical Capture into the TEI Edition**

The two halves of this lesson meet here. The photograph you took with a cradle, a scale bar, and matched lights is the image your `<facsimile>` points at, and the same numbers appear in both.

```xml
<facsimile>
  <surface xml:id="treaty_sheet1" ulx="0" uly="0" lrx="4800" lry="6000">
    <graphic url="images/nsarm_rg1_v430_no2.jpg" width="4800px" height="6000px"/>
    <zone xml:id="z_eng" type="column" ulx="350" uly="800" lrx="2300" lry="5200"/>
    <zone xml:id="z_marks" type="mark" ulx="350" uly="5300" lrx="4450" lry="5700"/>
  </surface>
</facsimile>
```

Two other parts of your header carry the rest: `<physDesc>` records what you found in the object itself, and `<encodingDesc>` records how the image was made — equipment, lighting, resolution.

Together they let a reader trace the chain from the physical object to the encoded tag. That is the whole ambition of this module, and Wednesday you build the middle of it with tools that measure for you.

**Vocabulary.** *Digital surrogate* — the image standing in for the object. *encodingDesc* — the header section describing how the edition was produced.

**Takeaway:** The facsimile block ties your capture to your encoding, and recording how the image was made completes the chain from object to tag.
