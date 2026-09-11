# Lesson 3.1 — Manual Imaging, TEI Facsimile, and Document Autopsy

*RELS 398 / ENGL 398 · Topic 3: IIIF Imaging · Meeting #6 (Tue Sep 15)*

*The manual baseline for imaging historical witnesses: physical document handling, photographic studio setup across diverse media, optical and multispectral recovery, and the TEI facsimile architecture.*

---

## **01 Content**

**From Text to Image: Why Digital Editions Require Facsimiles**

A scholarly edition that offers only a transcription asks its reader to take the editor's word on faith. When an editor transcribes a line, expands an abbreviation, or resolves an ambiguous character, they make an interpretive decision. In print scholarship, readers could verify those decisions only by traveling to the archive or ordering expensive photographic plates. Digital scholarly editing changes this relationship by placing the primary evidence directly alongside the editorial argument.

A digital facsimile is not a mere decorative illustration. It is a visual surrogate of a physical artifact that serves as primary historical evidence. When readers can inspect the high-resolution image of a page, they can evaluate whether an ink stroke represents a punctuation mark or a stray blot, whether a damaged character supports a proposed reading, and how layout features like margins and indentation shape textual meaning. Digital facsimile integration turns a transcription from an opaque claim into a verifiable hypothesis.

Providing images alongside text transforms the nature of scholarly authority. Traditional print editions often suppressed visual complexity in favor of typographic uniformity. Features such as scribal corrections, interlinear additions, ink color shifts, and physical damage were relegated to brief Latin notes in a critical apparatus. In a digital edition, the image preserves the physical context that typography flattens. The facsimile anchors the digital text in material reality.

Scholars must also recognize that a digital photograph is itself a representation, not the artifact itself. Every image involves lighting angles, camera settings, lens distortion, and compression choices. Digital facsimiles provide indispensable access, but editors must record how those images were created so future researchers understand the limits of the visual evidence.

**Takeaway:** Digital facsimiles transform scholarly editions from unverifiable assertions into testable arguments by providing the visual evidence needed to audit transcriptions.

---

## **02 Content**

**The TEI `<facsimile>` Element: Structure and Placement**

The Text Encoding Initiative provides a rigorous architecture for representing the visual appearance of textual sources. While traditional TEI encoding focused heavily on transcribed words inside the `<text>` element, modern digital editions require explicit structures to link transcriptions to photographic evidence. The root element for this visual representation is `<facsimile>`.

In a TEI document, `<facsimile>` is a sibling of `<teiHeader>` and `<text>`. It sits directly inside the root `<TEI>` element. A typical minimal document structure follows this sequence:

```xml
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
    <!-- Metadata describing the source and encoding -->
  </teiHeader>
  <facsimile>
    <!-- Visual representations of the physical surfaces -->
  </facsimile>
  <text>
    <!-- Transcribed textual content -->
  </text>
</TEI>
```

Placing `<facsimile>` outside `<text>` is a deliberate architectural decision. A physical artifact exists as a material object regardless of whether its text has been transcribed, translated, or analyzed. An archive may possess images of a manuscript folio that contains illegible writing, musical notation, sketches, or blank space. By separating the visual description in `<facsimile>` from the textual stream in `<text>`, TEI allows encoders to document physical surfaces independently of linguistic transcription.

The `<facsimile>` element can contain one or more `<surface>` elements, nested `<surfaceGrp>` containers, or simple `<graphic>` elements when coordinates are not required. It provides the top-level container for all digital surrogates representing the source document.

**Takeaway:** The `<facsimile>` element sits inside `<TEI>` alongside `<teiHeader>` and `<text>`, separating physical surface representation from transcribed linguistic content.

---

## **03 Content**

**Modeling Surfaces: The `<surface>` Element**

Historical documents are written on physical surfaces: parchment membranes, papyrus sheets, paper leaves, wooden tablets, or stone slabs. In TEI encoding, each discrete two-dimensional writing support is represented by the `<surface>` element. A `<surface>` models a specific physical face rather than an abstract textual unit.

For a bound codex, each folio side requires its own `<surface>` element. Folio 1 recto is one surface; folio 1 verso is a second, distinct surface. Even though they belong to the same physical sheet of parchment or paper, they represent separate visual and spatial planes. In the case of a single-sheet letter, decree, or broadside, each side of the paper constitutes a surface. If an envelope or seal is preserved, it too may be encoded as a discrete surface within the facsimile structure.

A `<surface>` element typically groups together the digital images of that face and the coordinate zones defined upon it. At its simplest, a `<surface>` contains a `<graphic>` element that points to an external image file:

```xml
<surface xml:id="f1r">
  <graphic url="images/f1r_master.tif" width="4000px" height="6000px"/>
</surface>
```

The `@xml:id` attribute is essential because it gives the physical surface a unique, machine-readable identifier. Downstream transcription elements, milestone tags, and alignment scripts use this identifier to bind textual passages to their physical manifestation. Without a stable identifier on `<surface>`, programmatic connection between text and image becomes impossible.

**Takeaway:** The `<surface>` element models a single physical two-dimensional writing face, providing the foundational container for digital images and spatial zones.

---

## **04 Content**

**Coordinates and Space: Declaring Coordinate Systems in `<surface>`**

A digital image is a two-dimensional grid of pixels. To define regions of interest on a document, such as a paragraph, an initial letter, or a marginal gloss, an encoder must establish a coordinate system. The TEI `<surface>` element provides four core attributes to declare its two-dimensional spatial boundary: `@ulx`, `@uly`, `@lrx`, and `@lry`.

These attribute names represent coordinate geometry:

- `@ulx`: Upper-Left X coordinate (horizontal origin, typically 0).

- `@uly`: Upper-Left Y coordinate (vertical origin, typically 0).

- `@lrx`: Lower-Right X coordinate (total width).

- `@lry`: Lower-Right Y coordinate (total height).

Consider a high-resolution photograph measuring 4,800 pixels wide by 6,400 pixels high. The `<surface>` declaration establishes this space:

```xml
<surface xml:id="f12r" ulx="0" uly="0" lrx="4800" lry="6400">
  <graphic url="images/f12r.jpg"/>
</surface>
```

In standard computer graphics and TEI conventions, the coordinate origin `(0,0)` sits at the upper-left corner of the image. The X-axis increases horizontally from left to right, while the Y-axis increases vertically from top to bottom. This orientation differs from Cartesian mathematics where the Y-axis increases upward, but it matches the scanning raster of digital sensors and web display standards.

Encoders may use absolute pixel dimensions or normalized coordinate spaces (such as 0 to 1000). Absolute pixel coordinates have the advantage of matching the source capture directly, ensuring that bounding boxes map precisely to observable features on the master image.

**Takeaway:** Declaring `@ulx`, `@uly`, `@lrx`, and `@lry` on `<surface>` establishes an upper-left origin coordinate space for defining precise sub-regions.

---

## **05 Content**

**Defining Regions: The `<zone>` Element**

Documents rarely consist of a single uniform block of writing. A medieval codex contains primary text columns, running headers, rubricated chapter titles, illuminated initials, and interlinear annotations. A modern handwritten letter includes letterhead, dates, body paragraphs, signatures, and postmarks. In the TEI facsimile framework, these sub-regions are defined using the `<zone>` element.

The `<zone>` element sits inside a `<surface>` and defines a specific spatial area using the coordinate system established by the parent surface. Like `<surface>`, `<zone>` uses the four bounding coordinates `@ulx`, `@uly`, `@lrx`, and `@lry` to define a rectangular boundary:

```xml
<surface xml:id="f24v" ulx="0" uly="0" lrx="3000" lry="4500">
  <graphic url="images/f24v.jpg"/>
  <zone xml:id="z_header" ulx="450" uly="200" lrx="2550" lry="450"/>
  <zone xml:id="z_col1"   ulx="400" uly="500" lrx="1400" lry="3800"/>
  <zone xml:id="z_col2"   ulx="1500" uly="500" lrx="2500" lry="3800"/>
  <zone xml:id="z_gloss"  ulx="2550" uly="1200" lrx="2900" lry="2200"/>
</surface>
```

The `@type` attribute allows encoders to classify zones semantically, distinguishing between columns, marginalia, decorations, musical staves, or damage. Each `<zone>` must carry a unique `@xml:id` so that transcriptions, annotations, or computer vision models can reference it unambiguously.

For irregular, non-rectangular shapes such as curved marginal notes or diagonal stains, TEI provides the `@points` attribute. The `@points` attribute records a sequence of coordinate pairs `x,y` defining a closed polygon, giving encoders the geometric precision required for complex layouts.

**Takeaway:** The `<zone>` element identifies and measures specific rectangular or polygonal sub-regions on a surface, enabling fine-grained spatial targeting.

---

## **06 Content**

**Grouping Features: The `<surfaceGrp>` and Sub-surfaces**

Complex historical documents often require hierarchical spatial grouping that a flat list of `<surface>` elements cannot express. A bifolium consists of two conjoined leaves that form four distinct writing surfaces. A parchment scroll may be constructed from multiple sewn membranes. An archival file may contain folded enclosures or pasted flaps. To model these multi-part relationships, TEI provides `<surfaceGrp>`.

The `<surfaceGrp>` element acts as an organizational container for related surfaces. It can group all four surfaces of a folded bifolium, represent an open opening where facing recto and verso pages must be viewed simultaneously, or organize a multi-sheet foldout map:

```xml
<facsimile>
  <surfaceGrp type="opening" n="1">
    <surface xml:id="f01v" ulx="0" uly="0" lrx="3000" lry="4200">
      <graphic url="images/f01v.jpg"/>
    </surface>
    <surface xml:id="f02r" ulx="0" uly="0" lrx="3000" lry="4200">
      <graphic url="images/f02r.jpg"/>
    </surface>
  </surfaceGrp>
</facsimile>
```

Furthermore, TEI allows `<surface>` elements to be nested inside other `<surface>` elements to model physical attachments. When an 18th-century clerk pinned a small slip of paper over a corrected clause in a legal register, that correction slip is physically a distinct surface attached to a parent surface. Encoding the slip as a child `<surface>` preserves its independent coordinate system while representing its physical attachment to the primary leaf.

Using `<surfaceGrp>` prevents flat list flattening, allowing digital editions to preserve codicological assembly and physical hierarchy directly within the facsimile model.

**Takeaway:** `<surfaceGrp>` organizes related surfaces into openings, bifolia, or assemblies, while nested surfaces model physical attachments and corrections.

---

## **07 Content**

**Linking Facsimile to Text: The `@facs` Attribute**

Defining coordinate zones in `<facsimile>` creates a spatial map, but an edition requires a connection between those visual areas and the transcribed text. TEI establishes this link through the global `@facs` attribute. Any element inside `<text>` can carry `@facs` to point to a corresponding `<surface>` or `<zone>`.

The value of the `@facs` attribute is a URI pointing to the target element's `@xml:id`, preceded by a hash mark (`#`):

```xml
<!-- Inside <facsimile> -->
<surface xml:id="leaf1r" ulx="0" uly="0" lrx="2400" lry="3200">
  <zone xml:id="z_line1" ulx="250" uly="300" lrx="2100" lry="450"/>
  <zone xml:id="z_line2" ulx="250" uly="460" lrx="2150" lry="600"/>
</surface>

<!-- Inside <text> -->
<body>
  <pb facs="#leaf1r" n="1r"/>
  <p>
    <lb facs="#z_line1" n="1"/>To the Honourable the Council
    <lb facs="#z_line2" n="2"/>The Humble Petition of John Bushell
  </p>
</body>
```

Notice how `@facs` operates at multiple granularities. The page break element `<pb>` points to `#leaf1r`, signaling that the entire subsequent block of text appears on that physical surface. At a finer granularity, each line break element `<lb>` points directly to its specific coordinate bounding box (`#z_line1`, `#z_line2`).

This granular linking enables interactive interfaces where hovering over a transcribed line highlights the exact manuscript coordinates, or clicking an ink smudge displays the corresponding encoded text.

**Takeaway:** The `@facs` attribute binds textual elements like `<pb>`, `<div>`, `<p>`, or `<lb>` directly to `<surface>` or `<zone>` identifiers in the facsimile.

---

## **08 Content**

**Two-Way Alignment: `<zone>` Pointing to Text and Text Pointing to `<zone>`**

Scholarly projects differ in their primary orientation. Text-centric projects begin with transcribed poetry or prose and attach coordinates as an enhancement. Image-centric projects, such as epigraphic surveys, scrapbooks, or heavily annotated charters, begin with the physical artifact and treat transcriptions as metadata attached to visual regions. TEI supports both approaches through reciprocal linking.

While the `@facs` attribute allows text elements to point into the facsimile, `<zone>` elements can also point directly into the text using the `@corresp` or `@target` attributes. This reciprocal relationship ensures that whichever model serves as the project's primary data structure, alignment remains explicit:

```xml
<!-- Direct link from image region to text -->
<zone xml:id="z_colophon" ulx="300" uly="2800" lrx="1900" lry="3150"
      corresp="#txt_colophon" type="colophon"/>

<!-- Text fragment carrying matching identifier -->
<div xml:id="txt_colophon" facs="#z_colophon" type="colophon">
  <p>Explicit liber tertius scriptus per manum Iohannis.</p>
</div>
```

Reciprocal alignment is vital when dealing with complex spatial features. If a scribe writes an interlinear addition that zig-zags between two lines, or writes a marginal gloss that wraps around three sides of a text block, the reading order in `<text>` does not match a clean rectangular coordinate box. In such cases, assigning multiple zones to a single text fragment, or linking a single `<zone>` to multiple distinct textual additions, preserves both the reading sequence and the material layout without compromising either.

Maintaining robust two-way pointers provides the semantic foundation that automated IIIF image viewers, transcription checkers, and machine-learning aligners rely on.

**Takeaway:** Two-way linking via `@facs` and `@corresp` allows flexible alignment whether an edition is organized primarily around textual structure or physical topography.

---

## **09 Content**

**The Materiality of the Witness: Media Diversity Across History**

A central premise of digital textual scholarship is that documents are material objects created through specific physical technologies. Too often, digitization workflows assume that all historical documents are flat paper sheets or uniformly bound codices. In practice, historical documents span thousands of years of human craftsmanship across vastly diverse media.

An epigraphic inscription cut into Roman limestone behaves differently under a camera lens than a 14th-century Italian parchment antiphonary, an 18th-century printed colonial proclamation, or a 20th-century folk artist's letter written on ruled stationery. Each medium presents distinct physical constraints:

- **Parchment:** Animal skin (calf, sheep, goat) characterized by follicle patterns, cockling, parchment shrinkage, and directional stiffness.

- **Papyrus:** Plant pith woven in perpendicular horizontal (recto) and vertical (verso) fiber layers, prone to fraying and fiber loss.

- **Rag Paper:** Handmade linen/cotton fibers carrying chain lines, wire lines, and watermarks, susceptible to foxing and water staining.

- **Stone and Bronze:** Rigid three-dimensional relief where text is incised or cast rather than deposited in colored ink.

Understanding the medium is not merely an archival nicety; it dictates the photographic methodology. A lighting technique that reveals iron-gall ink on paper can completely obscure an incised Greek inscription or blow out reflections on gilded illumination. Digitization begins with material autopsy: determining what the object is made of, how age has altered its stability, and what optical techniques are required to capture its text faithfully.

**Takeaway:** Every historical medium imposes distinct physical constraints; digitizers must tailor capture methods to the specific material properties of the witness.

---

## **10 Content**

**Epigraphs and Inscriptions: Stone, Metal, and Three-Dimensional Surfaces**

Epigraphy represents one of the oldest forms of written record, spanning classical monuments, boundary stones, funerary stelae, and bronze decrees. Unlike ink on parchment, an inscription does not communicate text through pigment absorption. It communicates text through three-dimensional relief: grooves chiselled into marble, letters stamped into brick, or incisions engraved into bronze.

Photographing an epigraph with flat, direct frontal lighting is almost always a failure. Under direct flash or perpendicular light, shadows disappear, causing shallow letterforms to blend invisibly into the stone's natural grain and weathering fissures. The text becomes unreadable because there is no luminance contrast between the incised strokes and the surrounding surface.

To capture an epigraphic inscription, the photographer must control the light angle to cast intentional shadows inside the carved strokes. Raking light—illumination directed at a shallow angle across the surface—creates dark shadows on the edges of the incision and bright highlights on the raised stone plane. 

Furthermore, stone stelae and bronze plaques are heavy, immobile, and frequently weathered by centuries of rain, lichen growth, and abrasion. Studio conditions rarely apply; scholars must use portable LED panels, diffusing baffles, and battery-powered rigs in museum galleries or archaeological sites. Capturing multiple exposures under differing illumination angles is essential for recovering severely eroded epigraphic texts.

**Takeaway:** Epigraphic inscriptions rely on carved surface depth rather than ink pigment, requiring low-angle raking illumination to create high-contrast shadows inside incisions.

---

## **11 Content**

**Papyri, Ostraca, and Fragile Organic Supports**

Papyrus was the dominant writing support of the Mediterranean world for millennia. Manufactured from the fibrous pith of the *Cyperus papyrus* reed, sheets were constructed by laying strips side by side in two perpendicular layers: horizontal fibers on the inside (recto) and vertical fibers on the outside (verso). Ostraca—broken fragments of pottery or limestone used for receipts, letters, and student exercises—represent another ubiquitous, fragile writing support.

Papyri present unique digitization challenges due to their extreme fragility and textured fiber structure:

1. **Fiber Interference:** The pronounced horizontal and vertical fiber lines create continuous visual noise that can mimic broken ink strokes. Lighting must be carefully diffused to avoid accentuating fiber shadows over carbon ink.

2. **Glass Encapsulation:** Most archival papyri are stored between glass plates to prevent flaking and crumbling. Photographing through glass introduces severe glare, internal reflections, and dust artifacts. Polarizing filters on both lights and lenses are required to eliminate surface reflections.

3. **Ink Fading and Carbon Inks:** Papyri were predominantly written with carbon ink (lampblack mixed with gum), which does not chemically fade like iron-gall ink but is vulnerable to physical flaking and surface abrasion.

4. **Ostraca Topography:** Ceramic sherds are curved, three-dimensional shards with uneven break lines and porous clay surfaces, requiring deep depth of field to keep the entire curved surface in sharp focus.

Handling papyri demands absolute care: they must never be subjected to drafts, pressure, or sudden humidity shifts during imaging.

**Takeaway:** Papyrological imaging must manage surface glare from protective glass encapsulation and use cross-polarization to suppress distracting fiber shadows.

---

## **12 Content**

**Scrolls and Rotuli: Continuous Writing Surfaces**

Before the widespread adoption of the codex in the late Roman era, the primary vehicle for long-form literary and administrative text was the roll. A horizontal roll (*volumen*) unrolls from left to right in successive vertical columns, while a vertical roll (*rotulus*) unrolls from top to bottom as a continuous administrative record or liturgical text.

Digitizing a scroll breaks the basic paradigm of page-by-page capture. A scroll is a continuous physical membrane, often several meters long, constructed from multiple sheets sewn or pasted together at joins (*kolleseis*). Digitizers must choose between two strategies:

- **Segmented Column Capture:** Photographing the scroll in sequential overlapping frames, ensuring that column boundaries, margins, and sheet joins are captured consistently.

- **Continuous Composite Imaging:** Capturing frames with measured overlap and stitching them into a unified digital surrogate using photogrammetric software.

Curling tension presents a significant conservation hazard. Ancient parchment and papyrus rolls develop severe memory of their rolled shape. Forcing an ancient scroll flat under glass can crack brittle fibers or detach ink flakes. Conservators employ specialized scroll cradles with soft, weighted rollers that hold a small section planar under minimal tension while leaving the rolled portions supported without strain.

In the TEI framework, a scroll can be encoded as a single long `<surface>` with sub-zones for each textual column, or as a sequence of linked surfaces representing each sewn membrane.

**Takeaway:** Scrolls require continuous or overlapping segmented capture using tension-relieved cradles to prevent mechanical damage to rolled membranes.

---

## **13 Content**

**Codices, Manuscripts, and Bound Books: Structure and Gutter Shadows**

The codex—leaves folded into quires and bound along the spine—has been the standard book format for nearly two millennia. While familiar, bound codices are among the most mechanically complex objects to digitize. A book is an interconnected mechanical system of leaves, thread, glue, sewing supports, and wooden or cardboard boards.

The foremost digitization challenge in bound volumes is the **gutter**: the inner margin where leaves meet the spine. When a book cannot open flat to 180 degrees without breaking the sewing threads or cracking the spine glue, the page curves into the gutter. This curvature introduces two severe distortions:

1. **Geometric Foreshortening:** Text lines curving into the gutter appear compressed, distorted, and out of plane.

2. **Gutter Shadows:** Standard overhead lighting cannot penetrate deep into the spine fold, casting dark shadows over the inner text margin.

Under no circumstances should a digitizer force a rare book or manuscript flat under a piece of heavy glass. Forcing a tight binding flat causes catastrophic damage: spine delamination, broken sewing cords, and torn gatherings. 

Instead, digitizers must use specialized book cradles that support the volume at a gentle opening angle (typically 90 to 110 degrees). Imaging is performed either with two angled cameras capturing facing pages simultaneously, or by reorienting the cradle to photograph one page at a time with the optical axis aligned perpendicular to the page plane.

**Takeaway:** Bound codices must be digitized on conservation book cradles at limited opening angles to prevent spine fracture and eliminate gutter shadow distortion.

---

## **14 Content**

**Broadside Documents, Maps, Prints, and Oversize Sheets**

Single-sheet historical documents represent a vast spectrum of cultural heritage: imperial charters, Revolutionary decrees, colonial treaties, runaway slave notices, architectural plans, and cartographic maps. Single sheets eliminate the gutter problem of codices, but they introduce their own distinct imaging challenges.

Oversize sheets—such as large folding maps, nautical charts, or multi-membrane royal letters patent—often exceed the field of view of standard camera copy stands. When an object measures over one meter in width, photographing it in a single exposure requires moving the camera far away, drastically reducing the effective resolution (pixels per inch) across fine details.

To maintain archival resolution on oversize material, digitizers employ two main approaches:

- **High-Resolution Scanning Backs:** Ultra-high-resolution sensors (100 to 150 megapixels) mounted on stable overhead gantries.

- **Tiled Multi-Frame Stitching:** Moving the camera across the document on an automated XY-gantry, capturing a grid of overlapping high-resolution tiles, and stitching them together seamlessly using optical feature alignment.

Furthermore, single-sheet broadsides frequently exhibit fold lines, creasing, cockling, and tears. Edge curl must be controlled gently using conservation snake weights or gentle vacuum suction copyboards rather than heavy clamping.

In TEI encoding, a single sheet is modeled as an individual `<surface>`, but its physical status as a broadside should be documented in the header's `<objectDesc form="sheet">` or `form="broadside"`, ensuring that codicological assumptions like quires and foliation are not misapplied.

**Takeaway:** Oversize sheets and broadsides require high-resolution single-capture or tiled stitching workflows, controlled with non-destructive weights on flat copyboards.

---

## **15 Content**

**Document Handling and Preservation Ethics in the Studio**

The first rule of document digitization is absolute: **preservation takes precedence over photography**. A digital image is an invaluable surrogate, but capturing it must never compromise the longevity or physical integrity of the original witness. The digitizer acts as a temporary custodian of irreplaceable historical heritage.

Studio handling protocols follow strict conservation ethics:

- **Clean, Dry Hands vs. Gloves:** Modern conservation standards generally recommend clean, thoroughly washed and dried hands rather than white cotton gloves when handling parchment and paper manuscripts. Cotton gloves reduce tactile sensitivity, making handlers clumsy and far more likely to tear brittle paper edges or fold parchment corners. Gloves are reserved for metal bindings, photographic prints, and unvarnished wood where skin oils cause chemical etching.

- **Jewelry and Clothing:** Handlers must remove rings, watches, bracelets, and dangling lanyards that could snag or abrade manuscript surfaces.

- **Zero Pressure on Bindings:** Never force a resistant book open. If a binding resists opening beyond 80 degrees, stop immediately and adjust the cradle.

- **Studio Environment:** No food, drink, pens, or sharp instruments are permitted anywhere near the imaging table. Only soft pencils are allowed for documentation.

Handling historical objects requires deliberate, unhurried movement. Turning a brittle paper leaf must be done from the center of the outer margin, supporting the leaf across its plane rather than flicking it from the corner.

**Takeaway:** Conservation ethics dictate that the physical safety of the artifact always supersedes image capture; clean hands, unforced bindings, and deliberate handling are mandatory.

---

## **16 Content**

**Supporting the Binding: Book Cradles, Foam Wedges, and Straps**

When photographing bound manuscripts and early printed books, the primary tool for physical protection is the **book cradle**. A book cradle is a mechanical support that holds a volume open at a safe, restricted angle while keeping the leaves supported across their entire surface area.

Commercial conservation cradles feature adjustable V-shaped plates that move independently in height and angle:

1. **Self-Balancing Plates:** As leaves are turned from recto to verso, the weight distribution of the text block shifts. High-end cradles feature linked plates that automatically lower the thicker side and raise the thinner side, keeping the active page plane at a constant focal distance.

2. **High-Density Foam Wedges:** In field conditions where mechanical cradles are unavailable, digitizers construct customized supports using archival Ethafoam wedges, felt bolsters, and padded blocks. The volume must never be allowed to sag or hyperextend at the joint.

3. **Restraining Straps:** To hold a curved leaf planar during exposure, digitizers use transparent polyethylene straps (such as Melinex or archival polyester strips) or soft cloth-covered lead snake weights placed strictly in blank margins. Straps must apply only the gentlest contact pressure needed to prevent movement during exposure.

Improvised supports must never use abrasive materials, rubber bands, or adhesive tapes. Every surface touching the artifact must be chemically inert and physically smooth.

**Takeaway:** Conservation book cradles and foam wedges support delicate bindings at safe opening angles, using inert polyester straps to hold pages planar without stress.

---

## **17 Content**

**Camera Geometry: Sensor Alignment, Focal Plane, and Lens Selection**

Achieving archival-quality photographs requires strict mathematical control over camera geometry. If the camera sensor is not precisely parallel to the document surface, the resulting image suffers from **keystoning** (geometric perspective distortion) and uneven sharpness across the frame.

Key geometric and optical considerations include:

- **Planar Parallelism:** The camera sensor must align parallel to the document plane in both the pitch and roll axes. Digitizers verify alignment using precision spirit levels, laser leveling tools, or mirror targets placed on the copyboard. In a mirror target, the camera lens reflects directly back into the center of its own viewfinder when alignment is true.

- **Optical Axis Centering:** The center of the lens must point directly at the geometric center of the document capture area, avoiding off-axis perspective slant.

- **Lens Selection:** Standard zoom lenses introduce barrel or pincushion distortion that curves straight text lines. Archival photography requires **macro flat-field prime lenses** (typically 50mm to 100mm focal length). Flat-field lenses are optically corrected to produce a completely flat plane of focus from center to edge, eliminating corner softness and chromatic aberration.

- **Aperture Sweet Spot:** Shooting with the lens wide open (e.g., f/2.8) yields an extremely shallow depth of field, causing curved margins to blur. Conversely, stopping down too far (e.g., f/22) introduces optical diffraction that softens the entire image. Archival capture typically operates at the lens's optical sweet spot, between **f/8 and f/11**.

**Takeaway:** Archival capture requires macro flat-field prime lenses aligned perfectly parallel to the document plane, stopped down to f/8-f/11 for edge-to-edge sharpness.

---

## **18 Content**

**Controlled Illumination: Balanced Studio Lighting and Glare Reduction**

Lighting is the single most influential variable in document photography. Improper illumination creates hot spots, shadows, color casts, and blinding specular glare that can render large portions of a text completely unreadable.

A standard copy stand lighting setup utilizes **balanced bilateral illumination**:

- Two identical light sources positioned on opposite sides of the copyboard, angled at approximately 45 degrees to the document plane.

- The lights are set at equal distances and equal power outputs to cancel out surface shadows and provide an even, uniform field of luminance across the entire surface.

- The uniformity of the lighting field is verified using an incident light meter or by photographing a uniform gray card and measuring pixel values across the corners and center. Variations must not exceed 5%.

**Cross-Polarization for Glare Reduction:**
Glossy surfaces—such as burnished gold leaf illumination, heavily sized rag paper, fresh printer's ink, or protective mylar sleeves—produce intense specular reflections (glare). To eliminate glare without moving the lights, digitizers apply **cross-polarization**:

1. Linear polarizing filters are placed over both light sources, oriented in the same polarization plane.

2. A circular polarizing filter is mounted on the camera lens and rotated 90 degrees relative to the light filters.

Cross-polarization completely blocks specular bounce while allowing diffuse reflected light from the ink and substrate to reach the sensor, rendering text readable through stubborn reflections.

**Takeaway:** Balanced 45-degree bilateral illumination provides uniform luminance, while cross-polarization eliminates blinding specular glare from glossy inks and gold leaf.

---

## **19 Content**

**Flatbed and Overhead Planetary Scanners: Mechanics and Constraints**

While camera copy stands dominate modern archival digitization, dedicated scanning hardware remains widespread in libraries and archives. Understanding the operational differences between scanning technologies is vital for selecting the appropriate tool for a given historical artifact.

**Flatbed Scanners:**
Standard flatbed scanners employ a moving sensor bar beneath a glass platen. The object is placed face down on the glass.

- *Constraints:* Flatbeds are acceptable for unbound modern sheets, but they are **strictly forbidden for bound manuscripts, fragile papyri, or brittle documents**. Placing a bound codex face down on a flatbed glass requires applying downward pressure on the spine, risking immediate structural failure. Furthermore, moving paper face down across glass creates friction that can abrade flaking pigments.

**Overhead Planetary Scanners:**
Overhead planetary scanners position the scanning head and light source above an open copyboard or motorized book cradle.

- *Mechanics:* The document remains stationary, facing upward in its natural reading position. The scanning head sweeps a line-sensor across the field or uses an area sensor to capture the page in one exposure.

- *Cradles:* Professional planetary scanners incorporate glass platen bars that lower gently onto the page with calibrated pressure sensors, stopping automatically before exerting stress on the paper.

Planetary overhead scanners provide superior conservation safety and high throughput for bound volumes, whereas flatbeds are strictly confined to stable, modern, flat single sheets.

**Takeaway:** Flatbed scanners endanger historical bindings and must never be used on rare books; overhead planetary scanners safely capture upward-facing documents on cradles.

---

## **20 Content**

**Metric Calibration: Scale Bars and Spatial Resolution (DPI / PPI)**

A digital photograph contains pixels, but pixels have no inherent physical size. An image measuring 3,000 pixels wide could represent a tiny postage stamp photographed under a microscope or a massive architectural blueprint photographed from a high ladder. Without physical calibration, a digital surrogate divorces the text from its real-world scale.

To preserve physical dimension, every archival exposure must include a **calibrated metric scale bar** placed within the frame, positioned adjacent to the document along the same focal plane:

- The scale bar provides millimeter and centimeter markings that allow researchers to verify the exact physical dimensions of script height, margins, line spacing, and damage holes.

- The scale bar must sit at the same height as the document surface. If the scale sits on the baseboard three centimeters below the elevated book cradle, depth-of-field perspective will distort the scale calculation.

**Calculating Spatial Resolution (Pixels Per Inch / PPI):**
Spatial resolution measures how many sensor pixels correspond to one physical inch on the object:
$$\text{PPI} = \frac{\text{Pixel Count between scale marks}}{\text{Physical Distance in inches}}$$

Archival standards established by initiatives such as FADGI (Federal Agencies Digital Guidelines Initiative) and Metamorfoze define strict spatial resolution tiers:

- **300 PPI:** Minimum baseline for modern printed books and general reference.

- **400–600 PPI:** Archival standard for historical manuscripts, fine handwriting, and detailed prints.

- **800–1000+ PPI:** Required for microscopic script, papyrus fiber analysis, or seal engravings.

Recording PPI in the TEI header ensures that downstream digital scholarship accurately reflects the material scale of the witness.

**Takeaway:** Every capture must include a coplanar metric scale bar to establish physical dimensions and verify spatial resolution against archival standards (400-600 PPI).

---

## **21 Content**

**Color Fidelity: Color Calibration Targets and Color Management**

Human color perception is notoriously subjective, and digital camera sensors possess native spectral sensitivities that do not match human vision. Furthermore, monitor displays, ambient room light, and software rendering engines all interpret color values differently. Archival digitization requires objective color calibration to ensure that parchment tones and ink pigments are documented truthfully.

Color fidelity is achieved through standard **color calibration targets** (such as the ColorChecker Classic or Digital SG):

- These targets feature scientifically formulated color patches with known, internationally standardized spectral reflectance values.

- Patches include primary colors, additive secondaries, skin tones, and a calibrated neutral grayscale ramp ranging from optical white to deep black.

**The Calibration Workflow:**

1. **Target Capture:** At the start of an imaging session, under identical studio lighting, the digitizer photographs the color target placed on the copyboard.

2. **Profile Generation:** Calibration software analyzes the captured patch values against the known laboratory reference data, generating an **ICC color profile** (or DNG camera profile) that mathematically corrects the camera sensor's specific chromatic biases.

3. **White Balance:** The neutral gray patch (typically 18% reflectance) is used to calculate custom white balance, neutralizing unwanted color temperature shifts from studio lamps.

4. **Batch Application:** The resulting ICC profile is applied non-destructively across all raw exposures captured under that lighting setup.

Without color management, an editor cannot determine whether a yellowed page reflects ancient parchment aging or an uncalibrated warm halogen lamp.

**Takeaway:** Color calibration targets and custom ICC profiles mathematically correct sensor chromatic bias, guaranteeing objective color fidelity across the digital edition.

---

## **22 Content**

**Environmental Stability: Temperature, Relative Humidity, and Light Exposure**

Digitization studios are working environments where sensitive historical artifacts are exposed to active lighting and handling. Archives enforce strict environmental parameters to prevent physical degradation during the imaging process.

**Relative Humidity (RH) and Temperature:**
Organic materials like parchment, paper, and leather are **hygroscopic**: they absorb and release moisture in equilibrium with the surrounding air.

- **Parchment Cockling:** Parchment is exceptionally responsive to humidity shifts. If the imaging studio is too dry, parchment contracts rapidly, causing severe planar cockling, buckling, and ink flaking. If humidity is too high, gelatinization and biological mold risks increase.

- *Standard Parameters:* Archival studios maintain temperature between 18°C and 22°C (64°F–72°F) and relative humidity between 45% and 55%, with continuous monitoring.

**Light Exposure and Thermal Damage:**
Old-fashioned tungsten or halogen studio lamps generate intense infrared radiation (heat). Directing halogen lamps at an ancient manuscript dries the substrate within minutes, causing dramatic curling and cracking.

- Modern digitization studios exclusively use **high-CRI (Color Rendering Index > 95) cold LED lighting**. LED lamps emit virtually zero infrared radiation and zero ultraviolet (UV) radiation in their visible output, protecting sensitive pigments from thermal shock and photochemical fading.

- Total lux exposure must be minimized: lights are extinguished when setting up or taking breaks, illuminating the manuscript only during active framing and exposure.

**Takeaway:** Imaging studios must maintain stable temperature and 45-55% relative humidity while using cold LED illumination to prevent thermal shock and photochemical damage.

---

## **23 Content**

**The Electromagnetic Spectrum in Manuscript Autopsy**

Human vision occupies a very narrow slice of the electromagnetic spectrum, perceiving radiation only between wavelengths of approximately 400 nanometers (violet) and 700 nanometers (red). However, physical documents interact with electromagnetic radiation far beyond these human biological limits.

The basic physics of light-matter interaction underpins all advanced manuscript imaging:

- **Reflection:** Photons bounce off the surface at the same wavelength.

- **Absorption:** Material absorbs incident energy, converting it to heat or chemical potential.

- **Transmission:** Photons pass through the substrate.

- **Fluorescence (Photoluminescence):** High-energy, short-wavelength photons (such as ultraviolet) are absorbed by a material, exciting electrons to higher energy states. When the electrons relax, they emit lower-energy, longer-wavelength photons in the visible spectrum.

Different historical writing materials exhibit radically different chemical behaviors across these spectral bands. Iron-gall ink, carbon ink, madder lake, vermilion, verdigris, and animal collagen all possess unique **spectral reflectance curves**. 

When ink has faded to human invisibility, or when a text has been deliberately erased to create a palimpsest, standard visible photography records only white parchment. But by probing the manuscript with non-visible wavelengths—ultraviolet and infrared—scholars can exploit chemical differences between ink residues and parchment to recover lost text.

**Takeaway:** Physical documents interact with radiation beyond the visible 400-700 nm band; exploiting reflection, absorption, and fluorescence across the spectrum reveals hidden text.

---

## **24 Content**

**Raking Light: Revealing Dry-Point, Ruling, and Surface Topography**

Not all textual and codicological evidence involves ink. Scribes used metal styluses, bone folders, and lead points to execute **pricking and ruling**—the geometric grid that guided text alignment across the page. Readers used dry-point styluses to scratch glosses, translations, and musical notation into margins without ink. Over centuries, parchment leaves also retain the structural memory of erased text, scraping marks, seals, and bookbinding impressions.

Under direct, perpendicular illumination, these physical depressions are invisible because they contain no colored pigment. **Raking light** solves this problem by using directional visible light cast at a very shallow, grazing angle (5 to 15 degrees) across the document plane.

The optical mechanics of raking light rely on three-dimensional surface topography:

- When grazing light strikes an indented groove, the near lip of the depression casts a deep shadow into the trough, while the far raised lip catches a bright highlight.

- This creates extreme local luminance contrast that transforms microscopic depth variations into prominent 2D shadow patterns.

- Rotating the light around the document exposes features running in different directions: horizontal ruling lines require light from the top or bottom, while vertical prickings require light from the sides.

Raking light is a non-destructive, purely optical technique that requires no specialized sensors—only a directional lamp and careful angle adjustment.

**Takeaway:** Raking light illuminates surfaces at shallow grazing angles, casting sharp shadows inside inkless depressions to reveal dry-point glosses, ruling, and erased topography.

---

## **25 Content**

**Reflectance Transformation Imaging (RTI): Mathematical Surface Normal Modeling**

While manual raking light photography creates compelling visual evidence, it produces only static photographs tied to one specific lighting angle. **Reflectance Transformation Imaging (RTI)**—incorporating Polynomial Texture Mapping (PTM)—is an advanced computational imaging technique that models the continuous three-dimensional shape and surface reflectance of an artifact.

**The RTI Capture Workflow:**

1. The camera is fixed on a rigid tripod directly above the document, facing perpendicular to the surface. Neither the camera nor the document moves during the entire session.

2. A small, shiny black sphere (such as a polished bearing ball) is placed on the copyboard next to the object.

3. An operator fires a movable flash or LED light from dozens of different angles, forming a virtual hemisphere over the document (typically 36 to 64 exposures).

4. In every shot, the shiny sphere captures a bright specular highlight. RTI software uses the position of this highlight on the sphere to calculate the exact 3D vector of the incoming light source for that exposure.

**Mathematical Synthesis:**
RTI software does not build a simple image stack. It fits a mathematical function (a biquadratic polynomial) to the luminance variation of *every individual pixel* across all lighting directions. This calculates the **surface normal vector**—the precise perpendicular direction of the physical plane at each pixel.

In the interactive RTI viewer, scholars can synthetically move a virtual light source in real time across the document. Furthermore, algorithmic enhancement modes like **diffuse gain** and **specular enhancement** can strip away distracting surface color, exaggerating micro-topography beyond what physical light could ever reveal.

**Takeaway:** RTI calculates mathematical surface normal vectors from dozens of known light angles, generating an interactive, relightable 3D surface model of the document.

---

## **26 Content**

**Ultraviolet (UV) Fluorescence: Recovering Erased Iron-Gall Inks and Palimpsests**

In the Middle Ages, writing parchment was costly and scarce. When an older text was deemed obsolete, scribes frequently scraped off the ink with pumice stones and knives, washed the membrane with weak acids, and wrote a new text over the cleaned surface. This recycled manuscript is known as a **palimpsest** (from the Greek for "scraped again"). The original underlying writing is termed the *scriptio inferior*; the newer upper text is the *scriptio superior*.

To the naked eye, the *scriptio inferior* is often completely erased. However, chemical scraping rarely removes all iron-gall ink. Iron-gall ink is formed by reacting oak gall tannins with ferrous sulfate (vitriol). The resulting iron tannate complexes penetrate deep into the collagen fiber matrix of the animal skin.

**The Physics of UV Fluorescence:**
When irradiated with narrowband **ultraviolet light (typically ~365 nm UV-A)**, parchment collagen undergoes natural photoluminescence: it absorbs high-energy UV radiation and fluoresces brightly in the pale greenish-blue visible spectrum.

However, residual iron compounds in the erased ink act as **fluorescence quenchers**:

- Iron ions absorb both the incoming UV excitation and the emitted visible fluorescence, preventing the parchment beneath the ink strokes from glowing.

- As a result, the erased writing stands out in stark, dark contrast against the brightly glowing parchment background.

- Photographing UV fluorescence requires a UV-blocking barrier filter on the camera lens, ensuring the sensor captures only the visible fluorescent emission, not reflected UV glare.

UV fluorescence imaging is the cornerstone method for uncovering lost classical and biblical texts hidden beneath later medieval liturgies.

**Takeaway:** UV-A radiation excites bright fluorescence in parchment collagen while residual iron-gall ink quenches it, causing erased palimpsest text to reappear as dark strokes.

---

## **27 Content**

**Infrared (IR) Reflectography: Penetrating Over-Inking, Soot, and Pigments**

While ultraviolet radiation operates at shorter, higher-energy wavelengths than visible light, **infrared (IR) reflectography** operates at longer wavelengths, typically in the near-infrared band between 750 nanometers and 1100 nanometers (and extending to 2500 nm in short-wave IR).

Infrared imaging exploits a fundamental chemical distinction between historical writing materials:

- **Carbon Ink:** Made from soot, charcoal, or bone black suspended in gum Arabic. Carbon particles are exceptionally stable and absorb electromagnetic radiation uniformly across visible and infrared wavelengths. Carbon ink remains pitch black under IR.

- **Iron-Gall Ink:** Highly absorptive in visible light, but becomes increasingly transparent at wavelengths above 800 nm.

- **Organic Inks and Stains:** Many organic pigments, blood, soot deposits, and chemical corrosion products become entirely transparent under infrared illumination.

**Applications in Document Recovery:**

1. **Censored and Redacted Text:** If an inquisitor or modern censor used iron-gall ink or organic dyes to cross out text written in carbon ink, illuminating the document with infrared light causes the obscuring ink to turn transparent, exposing the underlying carbon text cleanly.

2. **Fire and Smoke Damage:** In documents salvaged from fires (such as the Cotton Library fire of 1731), soot and charred paper obscure the text. Infrared penetrates the surface soot, reflecting off the uncharred paper fibers below.

3. **Underdrawings in Illuminations:** Infrared reflectography penetrates opaque pigment layers (such as lapis lazuli or lead white) in manuscript miniatures, revealing the artist's original carbon-drawn preliminary sketches.

Standard digital cameras have an internal IR-cut filter over their sensors; archival IR photography requires cameras with this filter removed ("full-spectrum conversions") fitted with screw-on IR bandpass filters.

**Takeaway:** Infrared reflectography exploits the transparency of iron-gall inks and organic pigments at longer wavelengths to penetrate stains, redactions, and charring.

---

## **28 Content**

**Multispectral and Hyperspectral Imaging: Multi-Band Capture and Spectral Stacks**

While raking light, UV, and IR each offer powerful qualitative tools, **multispectral imaging (MSI)** unites them into a rigorous, quantitative scientific framework. Rather than capturing a single exposure, an MSI system captures an aligned stack of narrowband photographic exposures spanning the ultraviolet, visible, and infrared spectra (typically 365 nm to 950 nm).

A standard multispectral imaging workflow employs:

- **Narrowband LED Arrays:** Illuminating the document sequentially with 12 to 24 distinct, monochromatic LED wavelengths in rapid succession.

- **Monochrome Scientific Sensors:** High-resolution monochrome sensors (without color Bayer filters) that maximize quantum efficiency across all wavelengths.

- **Filter Wheels:** Combining broadband illumination with liquid crystal tunable filters (LCTF) or optical interference bandpass filters in front of the lens.

**The Image Cube:**
The result of an MSI capture is an **image cube**: a spatial grid of pixels where every pixel contains a discrete spectral reflectance curve across dozens of measured wavelengths.

Because materials possess unique spectral signatures, advanced computational algorithms can process this data cube:

- **Principal Component Analysis (PCA):** Mathematical dimensionality reduction that compresses variance across dozens of bands into high-contrast false-color composite images, separating faint erased palimpsest text from dominant over-text.

- **Independent Component Analysis (ICA) and Spectral Angle Mapping:** Isolating and segmenting specific chemical ink recipes based on their mathematical spectral profiles.

Multispectral imaging represents the gold standard of non-destructive document recovery, responsible for recovering the Archimedes Palimpsest, the 1752 French Declaration drafts, and ancient Dead Sea Scroll fragments.

**Takeaway:** Multispectral imaging captures aligned narrow-band exposures from UV to IR, producing an image cube that mathematical algorithms process to separate illegible inks.

---

## **29 Content**

**Archival Capture Workflows: From Sensor to Unprocessed Master**

A successful digitization campaign relies on an undisrupted, standardized data pipeline. If photographic files are captured in lossy formats, named haphazardly, or modified destructively during shooting, the integrity of the digital surrogate is permanently degraded.

Archival capture adheres strictly to the **master file preservation model**:

1. **RAW Sensor Capture:** All exposures must be captured in the camera's uncompressed, proprietary RAW format (or open DNG). RAW files contain the unprocessed linear sensor data directly from the analog-to-digital converter, before white balance, tone curves, or color matrix interpolation are applied.

2. **Non-Destructive Processing:** In post-capture processing software (such as Lightroom, Capture One, or open-source RawTherapee), lens correction profiles and custom ICC color targets are applied. No sharpening or lossy compression is introduced at this stage.

3. **Uncompressed Archival Masters:** Processed files are exported as uncompressed, 16-bit or 8-bit **TIFF files** (Tagged Image File Format). The TIFF file serves as the permanent archival master surrogate.

4. **Metadata Preservation:** Camera EXIF metadata (shutter speed, aperture, ISO, sensor serial number) must remain embedded in the file headers. Archival technical metadata (operator name, equipment model, light source, color profile) is recorded in accompanying technical logs.

Standardized file naming is non-negotiable. File names must reflect repository, collection, shelfmark, and surface sequence (e.g., `NSA_RG1_v430_no2_f01r_master.tif`).

**Takeaway:** Archival workflows capture uncompressed RAW sensor data, exporting uncompressed TIFF masters with embedded technical metadata and systematic shelfmark file naming.

---

## **30 Content**

**The Digital Surrogate: Integrating Physical Capture into the TEI Edition**

We arrive at the synthesis of physical document autopsy and digital text encoding. Digitization is not the end of the scholarly workflow; it is the physical foundation upon which the entire digital scholarly edition rests. The high-resolution master captures produced in the studio find their intellectual home inside the TEI architecture.

When physical capture is complete, the images are integrated into the edition's `<facsimile>` structure:
```xml
<facsimile>
  <surface xml:id="nsa_treaty_1752_sheet" ulx="0" uly="0" lrx="4800" lry="6000">
    <graphic url="derivatives/nsa_rg1_v430_no2_master.jpg" width="4800px" height="6000px"/>
    <!-- English column zone -->
    <zone xml:id="z_eng_col" ulx="350" uly="800" lrx="2300" lry="5200" type="column" corresp="#txt_eng"/>
    <!-- French column zone -->
    <zone xml:id="z_fr_col"  ulx="2500" uly="800" lrx="4450" lry="5200" type="column" corresp="#txt_fr"/>
    <!-- Bushell printer colophon -->
    <zone xml:id="z_colophon" ulx="350" uly="5300" lrx="4450" lry="5700" type="colophon" corresp="#txt_colophon"/>
  </surface>
</facsimile>
```

In the `<teiHeader>`, the `<physDesc>` element documents the physical autopsy findings: support material, dimensions, condition, and evidence of ruling or seals. The `<encodingDesc>` records the photographic hardware, lens, lighting equipment, and resolution parameters used during capture.

By tying physical handling, calibrated photography, multispectral analysis, and TEI facsimile encoding into a continuous chain of evidence, the digital edition achieves the highest standard of modern scholarship: complete transparency from the material atom to the encoded digital tag.

**Takeaway:** A mature digital edition integrates physical autopsy findings into the `<teiHeader>` and anchors photographic surrogates directly into `<facsimile>` zones and coordinates.
