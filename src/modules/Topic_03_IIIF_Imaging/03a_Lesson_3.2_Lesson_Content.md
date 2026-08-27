# Lesson 3.2 — Raking Light, Multispectral Imaging, and Computational Palaeography

*RELS 398 / ENGL 398 · Topic 3: IIIF Imaging · Meeting #7 (Wed Sep 16)*

*Infrastructure week — the three-step comparative cycle does not apply. Yesterday
covered how images are delivered; today covers how they are made, and what can be
recovered from a manuscript that ordinary photography cannot show.*

---

## **01 Content**

**What the Eye Cannot See**

A manuscript page is not a text with some damage. It is a physical object whose
materials — parchment, iron-gall ink, carbon ink, pigments, binding media,
adhesives, and the products of centuries of chemical change — each interact with
light in their own way.

Human vision samples that interaction very coarsely. The eye responds to
wavelengths between roughly 400 and 700 nanometres, integrating everything in
that range into three broad channels. Any two materials that happen to produce
the same response in those three channels are, to the eye, the same colour —
regardless of how different they are chemically.

That limitation is the opening this lesson exploits. Iron-gall ink that has faded
to near-invisibility in visible light may absorb ultraviolet radiation strongly
while the surrounding parchment fluoresces under it. Carbon ink that is
indistinguishable from a stain to the eye remains strongly absorbent in the
near-infrared while the stain becomes transparent. The information was always
present in the object; it was inaccessible only because human vision does not
sample the wavelengths that carry it (Easton et al., 2003).

Multispectral imaging is the practice of sampling those wavelengths
systematically and then combining the results computationally. It is
non-destructive and non-invasive — the manuscript is illuminated and photographed,
nothing more — which is what makes it applicable to objects of extreme value
(Clausen et al., 2026).

**Vocabulary.** *Nanometre (nm)* — one billionth of a metre; the unit of
wavelength. *Fluorescence* — absorption of radiation at one wavelength followed by
emission at a longer one. *Non-destructive* — leaving the object unaltered.

**Takeaway:** Materials that look identical to the eye respond
differently outside the visible range, and multispectral imaging samples those
differences.

---

## **02 Content**

**Raking Light and Surface Relief**

Before any spectral technique, the simplest intervention is to change the *angle*
of illumination rather than its wavelength.

**Raking light** means illuminating the page from a very low angle, nearly
parallel to its surface, rather than from the front. Frontal illumination
minimizes shadow, which is what makes it good for reading ink. Grazing
illumination maximizes shadow, and every deviation in the surface — a ruling
furrow, an erasure, a dry-point gloss, a crease, a mould-made feature of the
parchment — casts a shadow proportional to its depth.

This recovers a class of evidence that carries no ink at all:

| Feature | Made by | Visible in frontal light? | Visible in raking light? |
| --- | --- | --- | --- |
| Ruling and pricking | Scoring or puncturing before writing | Rarely | Clearly |
| Dry-point gloss | Writing with a stylus, no ink | Almost never | Often |
| Erasure or scraping | Removing ink mechanically | Sometimes as discoloration | As surface disturbance |
| Blind tooling | Impressing a binding without pigment | No | Yes |
| Creases and cockling | Handling and humidity | Faintly | Clearly |

Dry-point glosses are the striking case. A reader annotating a manuscript with a
stylus rather than ink leaves an impression in the parchment and no colour at
all. Under ordinary illumination such annotations are effectively invisible, and
entire layers of medieval readership went unrecorded until raking light was
applied systematically.

Raking light requires no special equipment beyond a controllable light source,
which makes it the technique you are most likely to be able to apply yourself. If
your manuscript's repository offers raking-light captures, seek them out; they
frequently reveal ruling patterns that inform codicological description.

**Takeaway:** Raking light reveals evidence that has no colour —
ruling, erasure, and dry-point annotation — by turning depth into shadow.

---

## **03 Content**

**Reflectance Transformation Imaging**

Raking light has a limitation: one illumination angle reveals features
perpendicular to it and conceals features parallel to it. A furrow running
towards the light casts no shadow. The obvious remedy — many photographs from
many angles — produces a pile of images that a scholar must mentally combine.

**Reflectance Transformation Imaging** (RTI), developed at Hewlett-Packard
Laboratories as Polynomial Texture Mapping, automates that combination
(Malzbender et al., 2001). The manuscript is placed at the centre of a
hemispherical dome carrying many individually controllable lights, with the
camera fixed. Each light fires in turn, producing an image stack in which every
pixel has been recorded under many known illumination directions.

The computational step is what makes RTI more than a slideshow. For each pixel,
the sequence of luminance values is fitted — by least-squares approximation using
singular value decomposition — to a biquadratic polynomial in the light
direction. Six coefficients per pixel are stored, alongside unscaled colour
values (Malzbender et al., 2001).

Those six coefficients constitute a *model* of how that point on the surface
responds to light from any direction, including directions never photographed.
The viewer can therefore interpolate: the user drags a virtual light source
around the hemisphere and the surface re-renders continuously, in real time.

The result is not a photograph but an interactive surface model. A palaeographer
examining a suspected erasure can sweep the light through every angle and watch
how the disturbance responds — which is far more informative than any single
static image, and closer to what an examiner does when tilting a physical object
under a lamp.

**Takeaway:** RTI fits a polynomial per pixel to many
illumination angles, producing a relightable surface model rather than a fixed
photograph.

---

## **04 Content**

**What RTI Makes Visible**

Beyond relighting, the polynomial model supports mathematical enhancements that
have no photographic equivalent.

Because the polynomial describes how luminance varies with light direction, its
derivatives yield the **surface normal** at each pixel — the direction the
surface faces. Once normals are known, the software can exaggerate them
(Malzbender et al., 2001).

| Enhancement | Operation | Reveals |
| --- | --- | --- |
| Specular enhancement | Renders the surface as if glossy | Faint incisions and tooling |
| Diffuse gain | Amplifies the polynomial's curvature term | Shallow relief, invisible at any real angle |
| Normals visualization | Colour-maps surface direction | Surface structure independent of colour |
| Normals unsharp masking | Sharpens the normal field | Fine detail in worn or abraded surfaces |

The point about diffuse gain deserves emphasis. It does not simulate a lighting
condition that could be physically arranged; it exaggerates the surface's
geometry beyond what any real illumination would produce. RTI can therefore make
visible what would remain invisible under direct examination with any lamp, at
any angle. This is a case where the digital surrogate exceeds autopsy outright.

For palaeographers the applications are specific: dry-point glosses, blind
tooling on bindings, and the topography of degraded parchment where ink has been
lost but the writing has left an impression. In severely deteriorated material
the surface may retain the trace of writing whose ink is entirely gone, and RTI
can recover it (Malzbender et al., 2001).

RTI equipment is not available to this course, but RTI datasets exist for many
manuscripts and viewers are freely available. If your manuscript has been imaged
this way, it is worth pursuing.

**Takeaway:** RTI's derived surface normals allow enhancements
that exceed any physically achievable lighting, recovering writing whose ink is
entirely lost.

---

## **05 Content**

**The Physics of Multispectral Recovery**

Returning to wavelength. The recovery of erased text rests on a straightforward
physical fact: parchment and historical inks respond differently to radiation
outside the visible range, and those differences are large.

Under **ultraviolet** illumination, parchment collagen fluoresces strongly,
absorbing UV and re-emitting visible light — the page glows. Iron-gall ink
absorbs UV and does not fluoresce. Where ink is present, even ink scraped away
centuries ago leaving only a chemical residue, the fluorescence is suppressed.
The residue appears as dark text against a glowing page, at a contrast far
exceeding anything visible under ordinary light (Easton et al., 2003).

In the **near-infrared**, the relationship differs. Carbon-based inks remain
strongly absorbent well into the infrared, while many organic dyes, stains, and
later overwriting become progressively transparent. Imaging at these wavelengths
can therefore see *through* an obscuring layer to carbon ink beneath (Clausen et
al., 2026).

| Wavelength range | Behaviour of parchment | Behaviour of ink | Application |
| --- | --- | --- | --- |
| UV, ~365 nm | Fluoresces strongly | Iron-gall absorbs, no fluorescence | Erased iron-gall text |
| Visible, 400–700 nm | Reflects broadly | Both ink types absorb | Baseline reference image |
| NIR, 700–940 nm | Increasingly transparent | Carbon remains absorbent | Seeing through stains and overwriting |
| IR, 900–1700 nm | Largely transparent | Carbon strongly absorbent | Carbon ink under heavy obscuration |

The palimpsest is the paradigm case. A **palimpsest** is a manuscript whose
original text — the *scriptio inferior* — was scraped or washed off so the
parchment could be reused for a new text, the *scriptio superior*. The lower text
is invisible not because it was destroyed but because too little remains for the
eye to detect against the parchment and the overwriting. Spectral imaging
recovers the contrast that the eye cannot (Easton et al., 2003).

**Vocabulary.** *Scriptio inferior* — the erased under-text of a palimpsest.
*Scriptio superior* — the later text written over it. *Iron-gall ink* — the
standard European ink, made from iron salts and tannins.

**Takeaway:** Parchment fluoresces under UV while iron-gall ink
does not, and carbon ink absorbs infrared while stains become transparent — two
different physical mechanisms for two different recovery problems.

---

## **06 Content**

**Acquisition: Building a Datacube**

A multispectral capture is a controlled procedure, and understanding it tells you
what the resulting data can and cannot support.

The manuscript is placed under a fixed high-resolution achromatic camera —
achromatic because a colour sensor's filter array would confound the narrow-band
measurements. Illumination comes from multispectral LED panels emitting narrow
bands from roughly 365 nm in the ultraviolet through to about 940 nm in the
near-infrared. Where carbon ink beneath heavy obscuration is the target, dedicated
infrared cameras operating between 900 and 1700 nm are used (Clausen et al.,
2026).

Each band is captured in turn, with the object and camera stationary. The output
is a stack of registered greyscale images — one per wavelength — collectively
called a **datacube**: a three-dimensional array whose x and y axes are spatial
position and whose z axis is wavelength (Easton et al., 2003).

| Axis | Represents | Typical extent |
| --- | --- | --- |
| x | Horizontal pixel position | Several thousand pixels |
| y | Vertical pixel position | Several thousand pixels |
| z | Spectral band | 12 to 30 bands |

The crucial property is that each pixel has a **spectrum** rather than a colour —
a vector of reflectance values across the sampled bands. Two points that are
identical in visible colour may have entirely different spectra, and it is that
difference the subsequent processing exploits.

Registration matters more than it sounds. The bands must align to the pixel, or
every subsequent operation combines misaligned data. Because different
wavelengths refract differently through the lens, chromatic aberration displaces
them slightly, and registration algorithms correct this along with any residual
distortion before processing begins (Clausen et al., 2026).

**Takeaway:** A datacube gives every pixel a spectrum rather
than a colour, and pixel-perfect registration across bands is what makes it
processable.

---

## **07 Content**

**Why Raw Bands Are Rarely Enough**

Students meeting multispectral data for the first time often expect that one
band will simply show the erased text. Occasionally it does. Usually it does not,
and the reason is instructive.

Any single band is one measurement per pixel. The erased under-text is present as
a small difference in reflectance, and that difference competes with everything
else varying across the page: parchment thickness, staining, cockling,
illumination gradients, the over-text, and sensor noise. In any individual band
the signal is real but small relative to that variation.

What distinguishes the under-text is not its magnitude in any one band but its
*pattern across bands*. Ink residue and clean parchment differ in how their
reflectance changes from 365 nm to 940 nm, even where they are similar at each
individual wavelength. That pattern is a property of the whole spectrum and is
invisible in any single slice of it.

The processing problem is therefore **signal separation**: mathematically
distinguishing ink from parchment, stains, and over-text by exploiting spectral
pattern rather than raw brightness (Easton et al., 2003). This is a statistical
operation across the z axis of the datacube, and it is where the real recovery
happens.

The corollary matters for how you interpret results. A processed composite is not
a photograph of the manuscript. It is the output of a statistical transformation,
in which apparent brightness corresponds to a computed quantity rather than to
reflected light. Reading it requires knowing what was computed — which is why the
processing must be documented alongside the image.

**Takeaway:** Erased text is identified by its pattern across
bands rather than its brightness in any one, so recovery is a statistical
operation and its output is not a photograph.

---

## **08 Content**

**Principal Component Analysis**

The first and most widely used separation method is **Principal Component
Analysis** (PCA), an orthogonal linear transformation that projects correlated
spectral bands into a new set of uncorrelated variables ordered by the variance
they capture (Easton et al., 2003).

The intuition: the spectral bands are highly redundant, since most of what varies
across a manuscript page — overall illumination, parchment tone — affects all
bands together. PCA finds the direction in spectral space along which the data
varies most, calls that the first principal component, then finds the direction
of greatest remaining variance orthogonal to it, and so on.

| Component | Typically captures | Palaeographic usefulness |
| --- | --- | --- |
| PC1 | Overall brightness and illumination | Usually little; dominated by lighting |
| PC2 | Major material contrast, often the over-text | Moderate |
| PC3–PC5 | Subtler material differences | Frequently where the under-text emerges |
| Higher | Progressively more noise | Occasionally useful; usually discarded |

The pattern in that table is the practical lesson. The under-text rarely appears
in the first component, because it is not the largest source of variance on the
page — illumination is. It typically emerges in the middle components, where
large-scale variation has already been captured and removed, leaving the material
differences that distinguish ink residue from parchment.

PCA maximizes variance, which is a good proxy for information but is not the same
thing. It has no concept of "ink" and cannot be directed at the under-text; it
simply reorganizes the data so that structure concentrates in early components.
Finding the under-text means inspecting the components and recognizing it.

**Takeaway:** PCA reorders spectral data by variance, and the
erased under-text usually emerges in the middle components rather than the first.

---

## **09 Content**

**Independent Component Analysis**

Where PCA maximizes variance, **Independent Component Analysis** (ICA) pursues a
different and, for palimpsests, more apt objective. ICA models the datacube as a
linear mixture of statistically independent, non-Gaussian source signals, and
recovers those sources (Easton et al., 2003).

The assumption fits the palimpsest exactly. A palimpsest folio genuinely *is* a
mixture of independent sources: the parchment substrate, the *scriptio inferior*,
and the *scriptio superior* were produced at different times by different hands
with different materials, and their spatial patterns are unrelated. What the
camera records at each pixel is a sum of their contributions.

This is the "cocktail party problem" of signal processing — several conversations
recorded by several microphones, each capturing a different mixture, from which
independent voices can be recovered given enough microphones. Here the spectral
bands are the microphones and the textual layers are the voices.

| Method | Objective | Best suited to |
| --- | --- | --- |
| PCA | Maximize variance in orthogonal components | General contrast enhancement; finding structure |
| ICA | Maximize statistical independence of sources | Separating overlapping texts into distinct outputs |
| MNF | Segregate noise from signal via cascaded PCAs | Very degraded material with high noise |

ICA is therefore exceptionally effective at cleanly separating *scriptio inferior*
from *scriptio superior* into distinct output bands — which is what a palimpsest
scholar actually wants, as opposed to a single image in which both texts are
visible and superimposed (Easton et al., 2003).

Its limitation is that it requires an assumption about the number of independent
sources and can produce components in an arbitrary order and sign. Interpretation
is required; the algorithm does not label its outputs.

**Takeaway:** ICA separates overlapping texts into distinct
outputs by recovering statistically independent sources, which suits palimpsests
precisely.

---

## **10 Content**

**Minimum Noise Fraction**

A third transformation addresses a problem the other two handle poorly. In
severely degraded material the signal of interest may be weaker than the sensor
noise in some bands, and PCA — which maximizes variance without distinguishing
signal from noise — will happily rank a noisy band highly.

**Minimum Noise Fraction** (MNF) applies two cascaded principal component
analyses. The first estimates and normalizes the noise, transforming the data so
that noise has unit variance and is uncorrelated between bands. The second
performs a standard PCA on that noise-whitened data. The result orders components
by *signal-to-noise ratio* rather than by raw variance (Easton et al., 2003).

The practical consequence is that MNF also estimates the data's inherent
dimensionality: it reveals how many components carry real signal before the
remainder degenerates into noise. That is useful information in itself, since it
tells you how many components are worth examining.

MNF is particularly effective for extracting trace elemental fluorescence in
heavily degraded palimpsests, where the residue is faint enough that noise
normalization is the difference between recovery and failure.

In practice the three methods are complementary rather than competing, and a
serious imaging project runs all of them. PCA gives a rapid overview of where
structure lies. MNF establishes how much real signal exists and suppresses noise.
ICA separates the layers once the signal is known to be there. The scholar
inspects outputs from each and selects what proves legible.

**Takeaway:** MNF orders components by signal-to-noise rather
than variance, which is what makes very degraded material tractable.

---

## **11 Content**

**False-Colour Composites**

Statistical components emerge as greyscale images, and a scholar comparing five
of them is doing difficult visual work. The standard presentation combines them
into a **false-colour composite**.

The method is simple: assign three chosen components to the red, green, and blue
display channels of a monitor. The result is a colour image in which colour
encodes computed quantities rather than reflected light. With appropriate
selection, the erased under-text appears vividly coloured — bright red or blue —
against a neutral background (Easton et al., 2003).

Practitioners typically build these in ENVI or Photoshop, using channel splitting,
blending modes, and opacity adjustment to tune the result. These enhanced images
then serve as the primary resource for transcription: the scholar transcribes
from the composite, not from the visible-light photograph.

| Channel | Commonly assigned | Effect |
| --- | --- | --- |
| Red | A component isolating the under-text | Under-text appears red |
| Green | A visible-light or reference band | Provides page context |
| Blue | A component isolating the over-text | Over-text appears blue |

The term "false colour" is doing important work and should be taken literally.
The colours are assigned, not measured. A red letterform in such an image does
not indicate red ink; it indicates that the pixel scored highly on whichever
component was assigned to the red channel. Presenting a false-colour composite
without stating what its channels contain is close to unintelligible, and in a
scholarly context it is misleading — a reader cannot evaluate the evidence
without knowing what they are looking at.

Whenever you cite such an image, record the processing: which method, which
components, which channel assignments.

**Takeaway:** False-colour composites encode computed
quantities as colour, so the channel assignments must be documented or the image
cannot be evaluated as evidence.

---

## **12 Content**

**Case Study: The Archimedes Palimpsest**

The Archimedes Palimpsest is the field's defining demonstration and repays close
study, because every technique above appears in it.

The object is a tenth-century Byzantine parchment manuscript containing unique
Greek copies of seven treatises by Archimedes — including the only surviving
witness to the *Method of Mechanical Theorems* and to *On Floating Bodies* in
Greek. In the thirteenth century the codex was unbound, its ink scraped away, the
leaves cut in half, rotated, and overwritten with a Euchologion, a Christian
prayer book, to reuse the valuable parchment (Easton et al., 2003).

Every possible obstacle was present. The under-text had been deliberately erased.
The leaves had been physically cut and reoriented, so the Archimedes text runs
perpendicular to the prayer book. Centuries of mould had damaged the parchment.
And, worst, in the twentieth century a forger had painted Byzantine-style gold-leaf
portraits onto several folios to raise the manuscript's sale value — completely
obscuring the parchment beneath.

The decade-long project applied multispectral imaging from ultraviolet through
near-infrared, then PCA and ICA to separate the layers, generating pseudocoloured
composites in which the thirteenth-century prayers were suppressed and Archimedes'
text and mathematical diagrams appeared in clarity (Easton et al., 2003).

For the gold-leaf folios even that failed, since no optical wavelength penetrates
metal foil. The solution was X-ray fluorescence imaging at the Stanford
Synchrotron Radiation Lightsource: an intense X-ray beam excited the iron atoms in
the tenth-century iron-gall ink, causing them to fluoresce through the gold leaf
and revealing the text beneath by its elemental composition rather than its
optical properties (Easton et al., 2003).

**Takeaway:** The Archimedes Palimpsest required optical
multispectral imaging, statistical separation, and finally X-ray fluorescence to
read text through gold leaf — no single technique sufficed.

---

## **13 Content**

**What the Archimedes Project Established**

Three consequences followed from that project, and each shapes practice today.

First, it demonstrated that historical documents must be treated as **multi-layered
chemical and topological matrices** rather than as surfaces bearing text. The
Archimedes text was recovered not by reading it but by identifying the chemical
signature of the ink that had once formed it. That reframing — the manuscript as
a material object with measurable properties, of which the visible text is only
one expression — underlies all of computational palaeography (Easton et al.,
2003).

Second, it created the requirement that IIIF later answered. The project produced
dozens of images per folio: raw bands, statistical components, composites,
XRF elemental maps. These are not alternative photographs to choose among; they
are complementary evidence, and a scholar needs to move between them freely while
looking at the same place on the page. That need is precisely what the canvas
abstraction and the `Choice` construct were designed for, and the palimpsest
projects drove their development (Easton et al., 2003).

Third, it established that recovery is a *collaboration* between imaging
scientists and philologists, neither of whom can complete the work alone. The
scientists produce candidate images; only a palaeographer can judge whether a
recovered form is a letter, and only a philologist can judge whether the resulting
sequence is plausible Greek. Where the two are separated, the imaging is
undirected and the interpretation is uncontrolled.

That third point is a live methodological issue for you. When you evaluate a
processed image this term, you are performing the philologist's half of that
collaboration, and the judgement required is palaeographic rather than technical.

**Takeaway:** Recovery requires imaging scientists and
philologists together — only a palaeographer can judge whether a recovered form
is a letter.

---

## **14 Content**

**Case Study: Princeton Garrett Ms. 24**

If Archimedes demonstrated what recovery can achieve, Princeton's Garrett Ms. 24
demonstrates the problem that follows success: making the results *usable*.

Garrett Ms. 24 is a tenth-century Greek palimpsest whose under-texts include
sixth- to ninth-century Greek and Christian Palestinian Aramaic material —
linguistically significant, since Christian Palestinian Aramaic is attested in a
small corpus and every additional witness matters. Multispectral capture and
processing generated dozens of processed images per folio, isolating different
scripts and material anomalies.

At that point Princeton faced a distribution problem rather than a recovery
problem. The data existed. Publishing it as downloadable datacubes would have
served almost nobody: the files are enormous, and interpreting them requires
software and expertise that most philologists do not have. The recovery would have
been real and effectively inaccessible.

Princeton's response was to host the enhanced images under IIIF and integrate a
compliant viewer directly into the online library catalogue. The viewer presents a
dropdown by which a researcher toggles between narrow-band captures at specific UV
or IR wavelengths and algorithmically processed PCA composites — all registered to
the same canvas, so the view does not shift when the layer changes.

The lesson the case is usually cited for is that **providing access to
multispectral data requires interface design as much as it requires imaging**.
Hosting raw datacubes is not access. Packaging complex optical physics into a
dropdown that a philologist can use without understanding PCA is what converts a
recovery into a usable scholarly resource — and IIIF `Choice` annotations are the
mechanism.

**Takeaway:** Recovery is not access; Princeton's contribution
was packaging multispectral results into an interface a philologist could actually
use.

---

## **15 Content**

**The `Choice` Construct**

Lesson 3.1 established that a canvas is a coordinate space onto which content is
painted. `Choice` is the construct that exploits it for spectral layering, and it
is available only in Presentation API 3.0 (IIIF Consortium, 2020).

When a folio has been imaged under natural colour, UV fluorescence, and as a PCA
composite, all three represent the identical physical space. The canvas is
instantiated with the dimensions of the highest-resolution image. The
AnnotationPage targeting that canvas holds an Annotation whose `body` is not a
single Image but a `Choice` object listing several Image resources as alternatives.

```json
{
  "type": "Annotation",
  "motivation": "painting",
  "body": {
    "type": "Choice",
    "items": [
      { "id": "https://example.edu/iiif/42r-color/full/max/0/default.jpg",
        "type": "Image", "label": { "en": ["Natural colour"] } },
      { "id": "https://example.edu/iiif/42r-uv/full/max/0/default.jpg",
        "type": "Image", "label": { "en": ["UV fluorescence, 365 nm"] } },
      { "id": "https://example.edu/iiif/42r-pca/full/max/0/default.jpg",
        "type": "Image", "label": { "en": ["PCA composite, components 2-4"] } }
    ]
  },
  "target": "https://example.edu/iiif/canvas/42r"
}
```

A compliant viewer such as Mirador 3 renders this as a layer selector, letting
the scholar toggle between representations, or blend them with an opacity
control, directly in the browser.

Two details of practice. The labels are the scholarly documentation and should
state the imaging condition precisely — "UV fluorescence, 365 nm" rather than
"UV". And the first item in the list is what a viewer displays by default;
put the natural-colour image first unless there is a reason not to.

**Takeaway:** `Choice` lists alternative images for one canvas,
and its labels are where the imaging conditions are documented.

---

## **16 Content**

**Why Layering Changes the Workflow**

The ability to cross-fade spectral layers in real time is not merely convenient;
it changes how a questionable reading is verified.

Consider the pre-IIIF procedure. A scholar uncertain about a letterform obtains
the UV image, opens it in image software, locates the relevant region, compares it
mentally with the visible-light image open in another window, then perhaps
consults a PCA composite in a third. Each transition costs minutes and requires
re-locating the same spot in a differently sized image. In practice, most readings
were checked against one image because checking against four was too expensive.

With layered canvases, the scholar zooms to the letterform once and toggles. The
region stays fixed because all layers share the canvas coordinate space. Comparing
four spectral conditions costs seconds, so it happens routinely rather than
exceptionally.

| Aspect | Pre-IIIF workflow | Layered canvas workflow |
| --- | --- | --- |
| Data transfer | Download full datacubes | Tiles for the current viewport |
| Locating a region | Re-find it in each image | Fixed; the canvas does not move |
| Cost of one comparison | Minutes | Seconds |
| Practical consequence | Check against one image | Check against all, routinely |

The last row is the substantive change. When verification is cheap it becomes the
default, and readings get checked that previously would have been accepted on the
strength of a single image. That is a change in evidential standards produced by
an infrastructural improvement — which is a recurring pattern in this course, and
worth noticing as such.

**Takeaway:** Layered canvases make multi-spectral verification
cheap enough to be routine, which raises the evidential standard for a reading.

---

## **17 Content**

**Documenting Provenance of Processed Images**

A processed image is a scientific result, and the standards that apply to
scientific results apply to it. Yet processed manuscript images circulate
constantly with no record of how they were made, which makes them uninterpretable
as evidence.

Consider what is unrecoverable from a bare composite image: which bands were
captured and at what wavelengths, which transformation was applied, which
components were selected, how they were assigned to channels, what contrast
adjustments followed. Two composites of the same folio produced with different
choices can support different readings, and a scholar shown only the images has no
way to adjudicate.

Record at minimum:

| Field | Example |
| --- | --- |
| Capture wavelengths | 365, 450, 505, 592, 625, 700, 780, 850, 940 nm |
| Camera and illumination | Phase One IQ260; multispectral LED panel |
| Registration method | Applied; chromatic aberration corrected |
| Transformation | ICA, 6 components assumed |
| Components used | IC2 to red, visible 592 nm to green, IC4 to blue |
| Post-processing | Contrast stretch; no sharpening |
| Software and version | ENVI 5.6 |
| Operator and date | Name; 2026-09-16 |

Clausen et al. (2026), arguing for open repositories integrating manuscript
research data, treat exactly this linkage as the core requirement: material
analyses must remain connected to the structural and textual encodings they
inform, rather than circulating as detached images.

The IIIF `metadata` block on a canvas or annotation is the natural home for this,
and the `Choice` labels carry the summary. Your Week 1 commit discipline is the
other half: when you use a processed image, record in the commit body which layer
you read from.

**Takeaway:** A processed image without its processing
parameters cannot be evaluated as evidence, so record wavelengths, method,
components, and channel assignments.

---

## **18 Content**

**Interpretive Risk: Seeing What Is Not There**

A caution that belongs in the middle of this lesson rather than at its end,
because it qualifies everything preceding.

Statistical transformations amplify differences. That is their purpose, and they
amplify whatever differences exist — including differences arising from noise,
staining, parchment texture, mould, and the transformation's own artefacts. A PCA
component can present structure that resembles letterforms and originates in none.

The risk is compounded by expectation. A scholar processing a palimpsest is
looking for text, knows roughly what script to expect, and often has a hypothesis
about the content. Human pattern recognition is extraordinarily willing to find
letterforms in noise under those conditions, and the willingness increases with
the strength of the prior expectation.

Controls that constrain this:

- **Multiple methods.** A reading that appears under PCA, ICA, and MNF is more credible than one appearing under a single transformation.
- **Multiple parameterizations.** A reading that persists across different component selections is more credible than one that depends on a specific choice.
- **Palaeographic plausibility.** Recovered letterforms must be consistent with a real script executed by a real hand, with plausible ductus and proportion.
- **Linguistic plausibility.** The result must be possible in the language, and *un*expected readings are stronger evidence than expected ones.
- **Independent verification.** Another scholar, ideally without knowledge of the expected reading, should see it too.

The fourth point deserves care. A recovered reading that confirms what you
expected is weaker evidence than one that surprises you, because the confirming
case is exactly the one your expectation could have produced. Treat readings that
conveniently support your hypothesis with more scepticism than readings that
complicate it.

**Takeaway:** Statistical enhancement amplifies noise as readily
as signal, and expectation makes false letterforms easy to see — so require
persistence across methods and parameters.

---

## **19 Content**

**Recording Confidence in the Transcription**

If some recovered readings are less certain than others, the transcription must
say so. TEI provides the apparatus (TEI Consortium, 2026).

| Element or attribute | Records | Use here |
| --- | --- | --- |
| `<unclear>` | Text that cannot be read with confidence | A letterform visible but ambiguous |
| `@reason` | Why it is unclear | `reason="faded"`, `reason="palimpsest"` |
| `@cert` | Degree of certainty | `cert="low"`, `cert="medium"`, `cert="high"` |
| `@resp` | Who is responsible for the reading | Points to an editor in the header |
| `<supplied>` | Text supplied by the editor, not in the witness | Restoration of a lacuna |
| `<gap>` | Material that is missing or illegible | With `@extent` and `@unit` |
| `<damage>` | A physical region affected by damage | Documents the material cause |

A worked example:

```xml
<unclear reason="palimpsest" cert="medium" resp="#KMP"
         source="#uv365">ἐγένετο</unclear>
```

The `@source` attribute pointing at a documented imaging condition is the move
that connects this lesson to your edition. It states not merely that the reading
is uncertain but *what evidence it rests on* — a reader can go to the UV image and
evaluate the claim.

This is the concrete difference between a transcription and a scholarly
transcription. The first asserts what the text says; the second asserts what the
text says, how confident the editor is, who is responsible, and what evidence
supports it. Where recovery is involved, the second is the only defensible form.

**Takeaway:** Encode recovered readings with `<unclear>`,
`@cert`, `@resp`, and a `@source` pointing at the imaging condition that supports
them.

---

## **20 Content**

**Imaging and Handwritten Text Recognition**

The imaging layer feeds directly into next week's transcription work, and the
connection runs through IIIF.

HTR platforms — Transkribus and eScriptorium prominently — ingest manuscript
images via manifest URI rather than by file upload, which eliminates transferring
gigabytes of TIFFs by hand (eScriptorium/Kraken, 2024). The manifest you build on
Friday is therefore literally the input to Week 4.

Within eScriptorium, imported images undergo automatic layout analysis. The
platform builds on the Kraken OCR/HTR engine and the YALTAi object detection
framework, which takes an object-detection approach to layout rather than
traditional region segmentation, achieving accurate baseline identification on
complex historical manuscripts (eScriptorium/Kraken, 2024).

| Stage | Operation | Output |
| --- | --- | --- |
| Ingestion | Import images by manifest URI | Images registered in the platform |
| Layout analysis | YALTAi object detection; baseline identification | Zones and baselines per page |
| Ground truth | Manual transcription of a training sample | Aligned text and image regions |
| Model training | Neural network trained on the ground truth | A model specific to this scribe |
| Prediction | Apply the model to remaining folios | ALTO or PAGE XML with coordinates |

Custom models can be trained on relatively small samples of manually transcribed
ground truth — often as few as fifty pages — after which the model generates
bounding boxes and text predictions for the remainder (eScriptorium/Kraken,
2024). Output is ALTO XML or PAGE XML, formats that have structural equivalence to
TEI and, critically, preserve the pixel-coordinate bindings established during
layout analysis.

That coordinate preservation is what makes the pipeline coherent: the
transcription arrives already bound to positions on the page, which is exactly the
binding Lesson 3.3 builds by hand.

**Takeaway:** HTR platforms ingest manifests directly and emit
coordinate-bound ALTO or PAGE XML, so Friday's manifest is Week 4's input.

---

## **21 Content**

**Which Images to Transcribe From**

A decision that must be made explicitly, because it is otherwise made by default
and never recorded.

When several representations of a folio exist, transcription proceeds from one of
them — and different choices produce different transcriptions. The visible-light
image is the conservative default: it shows the manuscript as a reader would have
seen it, and readings taken from it require no methodological defence. A processed
composite may show more, and for a palimpsest it may show the only legible form of
the text at all.

| Source | Advantage | Cost |
| --- | --- | --- |
| Visible light | Uncontroversial; matches direct examination | May not show the text at all |
| Single narrow band | Direct measurement; simple to document | Often insufficient alone |
| PCA or ICA composite | Maximum legibility for erased text | Interpretation depends on processing |
| Several, compared | Strongest evidential basis | Slower |

The defensible practice is the last: transcribe from the composite that renders
the text most legible, verify each uncertain reading against other layers, and
record which layer supported each contested reading. The layer toggle described
in section 16 is what makes this affordable.

What is not defensible is transcribing from a processed image without saying so.
A transcription presented as a reading of the manuscript, silently derived from an
ICA composite whose parameters are unrecorded, makes a claim its reader cannot
assess — and, in the palimpsest case, a claim that could not have been made from
the object itself under any illumination.

Record your choice in your repository now, before Week 4 begins, so that the
decision is deliberate.

**Takeaway:** Transcribe from the most legible layer, verify
against the others, and always record which layer supported a contested reading.

---

## **22 Content**

**Practical Access to Multispectral Data**

You will not produce multispectral images this term — the equipment is not
available. You may well be able to *use* them, and the distinction matters for
your own edition.

Where to look:

- **The manifest itself.** Additional captures frequently appear as extra canvases or as `Choice` alternatives, without being surfaced in the default viewer. Search the JSON for `ultraviolet`, `infrared`, `UV`, `IR`, `processed`, `PCA`, or `multispectral`.
- **Dedicated project sites.** Major palimpsest projects publish separately from the holding library's catalogue.
- **The Sinai Palimpsests Project**, which has published extensive multispectral data for St Catherine's Monastery manuscripts.
- **Institutional imaging labs**, whose datasets sometimes exist but are not linked from the catalogue record.
- **Direct enquiry.** Curators frequently hold imaging data that has never been published, and a polite, specific request from a student with a clear purpose is often answered.

The last route is worth attempting if your passage has damaged or erased regions.
An email stating the manuscript, the folios, your purpose, and your institutional
affiliation costs nothing and occasionally yields a dataset.

If no multispectral data exists for your manuscript — which is the common case —
you are not disadvantaged for this course. Weeks 4 through 13 proceed from
visible-light images. This week's content remains necessary because it is what
lets you read the imaging literature on your manuscript, evaluate published
recovered readings, and understand what the images in your edition are and are not.

**Takeaway:** Check your manifest for unlisted spectral layers,
and ask curators directly; if none exists, the course proceeds from visible light.

---

## **23 Content**

**Beyond Optics: XRF and Materials Analysis**

The Archimedes gold-leaf problem introduced a technique that goes beyond
photography, and it is worth situating within the wider range of manuscript
analysis.

**X-ray fluorescence** (XRF) imaging does not measure reflected light. An X-ray
beam excites atoms in the sample, which emit characteristic X-rays at energies
specific to each element. Mapping those emissions produces an image of *elemental
distribution* — where the iron is, where the copper is — rather than an image of
appearance (Easton et al., 2003).

For iron-gall ink this is decisive: the ink contains iron, the parchment does not,
and iron's characteristic emission passes through overlying material that stops
visible light entirely. Hence the recovery of Archimedes text beneath gold leaf.

| Technique | Measures | Reveals |
| --- | --- | --- |
| Multispectral imaging | Reflectance across wavelengths | Ink residue; layered texts |
| RTI | Surface response to light direction | Relief; dry-point; erasure |
| XRF | Elemental composition | Ink chemistry through obscuring layers |
| Raman spectroscopy | Molecular vibration | Pigment identification |
| Fibre optic reflectance | Reflectance spectra at points | Pigment and binder characterization |

Clausen et al. (2026) argue that these heterogeneous datasets — multispectral,
XRF, Raman — belong in a unified repository alongside the TEI encoding and
structural metadata, because the questions worth asking span them. Dating an ink
by its chemistry bears on the dating of a hand; identifying a pigment bears on
localization; and both bear on the textual argument.

This is where the canvas abstraction pays off most fully. An elemental map, a
spectral composite, and a transcribed line can all target the same canvas region —
which is what allows a chemical observation and a palaeographic one to be stated
about the same place.

**Takeaway:** XRF maps elemental composition rather than
appearance, and the canvas is what lets chemical and textual observations refer to
the same place on the page.

---

## **24 Content**

**The Manuscript as Data**

Step back to the conceptual claim these techniques collectively support, because
it reframes what your edition is.

The traditional model treats a manuscript as a *carrier* of text. The text is the
object of study; the parchment is the medium that conveys it; and the editor's job
is to extract the text and present it accurately. Codicological description
belongs to the introduction, as context.

The techniques in this lesson do not fit that model. They recover text from
chemical residue, from surface topography, from elemental distribution — from
properties of the object that are not text at all, and would be discarded as
irrelevant medium under the traditional view. The Archimedes recovery worked
precisely because the manuscript was treated as a chemical and topological matrix
rather than as a surface bearing writing (Easton et al., 2003).

The alternative model treats the manuscript as a *dataset* of which the visible
text is one projection. Other projections — spectral, topographic, elemental —
carry information that is often complementary and occasionally the only surviving
witness to the text.

This is not merely a technical shift. It changes what counts as evidence in a
textual argument. A claim about a reading may now be supported by an elemental
map or a spectral component rather than by an appeal to what an examiner can see,
and evaluating such a claim requires understanding how the evidence was produced —
which is why this lesson exists in a philology course.

**Takeaway:** Recovery techniques treat the manuscript as a
dataset with many projections rather than a surface bearing text, which changes
what can count as evidence for a reading.

---

## **25 Content**

**Limits and Honest Reporting**

Balance is owed. The cases in this lesson are the celebrated successes, and
success is not the usual outcome.

Multispectral imaging fails frequently. Where erasure was thorough, no residue may
remain. Where the substrate is papyrus rather than parchment, fluorescence
behaviour differs and UV recovery is often ineffective. Where ink was
carbon-based, the UV mechanism does not apply, since carbon does not present the
fluorescence contrast that iron-gall does. Where damage is severe enough, the
signal is simply absent.

| Condition | Likelihood of recovery | Reason |
| --- | --- | --- |
| Iron-gall on parchment, lightly washed | Good | Residue remains; strong UV contrast |
| Iron-gall on parchment, thoroughly scraped | Variable | Depends on penetration into the substrate |
| Carbon ink, obscured by stains | Good with IR | Carbon absorbs; stains become transparent |
| Carbon ink, erased | Poor | Sits on the surface; leaves little residue |
| Any ink on papyrus | Variable | Different fluorescence behaviour |
| Fire or water damage, severe | Poor | Substrate structure destroyed |

Reporting failure is part of the method. A project that images a palimpsest and
recovers nothing has produced a real result — the negative finding constrains what
future work should attempt, and prevents the same folios being reimaged
repeatedly. In practice negative results are underreported, which means the
literature overstates the technique's reliability.

Apply the same standard in your own edition. If you attempt to resolve a
questionable reading against a spectral layer and it remains unresolved, record
that. An `<unclear>` element with `@cert="low"` and a note that UV was consulted
without resolution is a more useful scholarly statement than a confident reading
or a silent omission.

**Takeaway:** Recovery often fails, and a documented negative
result is a real finding — record what you consulted even when it resolved
nothing.

---

## **26 Content**

**An Exercise for This Meeting**

Work through the following on your own manuscript.

- Search both witnesses' manifests for non-visible-light or processed images, using the search terms in section 22.
- If any exist, load the manifest into Mirador and confirm whether a layer selector appears.
- If a `Choice` is present, examine its labels and record what imaging conditions are documented.
- Identify the most damaged or least legible region of your passage.
- Compare that region across every available layer, at full zoom.
- Record what each layer does and does not resolve.
- Search the scholarly literature for imaging work on your manuscript.
- Commit your findings as a note in your repository.

If no additional layers exist, do the second half anyway. Identify the least
legible region of your passage under visible light, record precisely what is
uncertain about it, and note what imaging technique would be appropriate given the
ink type and damage. That is a real scholarly assessment, and it will inform your
`<unclear>` encoding in Week 4.

Add the results to `images/SOURCES.md` alongside yesterday's record and commit
with a Conventional Commits message. By Friday this file documents your edition's
entire image basis.

**Takeaway:** Assess the least legible region of your passage
against every layer available, and record what remains unresolved.

---

## **27 Content**

**Reading Imaging Scholarship Critically**

You will encounter published recovered readings, and you need to be able to
evaluate them rather than accept them.

Questions to ask of any published recovery:

| Question | What a weak answer looks like |
| --- | --- |
| What wavelengths were captured? | Unspecified, or "multispectral imaging was used" |
| What transformation produced this image? | Not stated |
| Which components, and how assigned to channels? | Not stated |
| Was the reading confirmed by another method? | Only one composite is shown |
| Who read it, and with what expertise? | No palaeographer involved |
| Was the reading expected in advance? | Confirms a prior hypothesis, with no discussion |
| Are negative results reported? | Only successful folios are shown |

Publications answering most of these poorly should be treated as preliminary
reports rather than as established readings. This is not scepticism about the
techniques, which are sound; it is the ordinary requirement that a method be
described sufficiently for a reader to evaluate its application.

The sixth row is the subtle one and connects to section 18. A recovery that
confirms an expected reading is the case where confirmation bias operates most
strongly, and a careful publication acknowledges this — typically by having the
reading confirmed by someone unaware of the expectation.

Where a published recovery bears on your own passage, cite it with its
qualifications intact. "Smith reads X, from an ICA composite; components and
parameters unreported" is honest and lets your reader weigh it. Repeating the
reading as established fact passes along a confidence the evidence may not support.

**Takeaway:** Evaluate published recoveries by whether the
imaging and processing are described well enough for you to assess them, and cite
them with their qualifications intact.

---

## **28 Content**

**Preparing for Lesson 3.3**

Friday assembles both meetings into a working artefact: the IIIF manifest for
your passage, bound to your TEI transcription by canvas coordinates.

Everything so far is input to it. Lesson 3.1 gave the structural model — manifest,
canvas, annotation, fragment selector. This lesson gave the imaging model — what
the images are, how they were produced, and how alternatives are expressed as a
`Choice`. Friday joins them and connects the result to your TEI.

Bring the following:

- Manifest URLs for both witnesses, recorded and verified.
- Canvas identifiers and dimensions for every folio of your passage.
- Rights statements and required attribution text.
- A record of any additional spectral layers and what they show.
- Your Week 2 TEI header, in a valid state.
- Your assessment of the least legible region of your passage.

The TEI header is required because Friday binds the manifest to the encoding, and
that is also **the Cataloguing & Metadata Assignment, due Friday September 18** —
the same day. Ensure the header validates before Friday's meeting; debugging
schema errors while attempting to build coordinate bindings is a poor use of the
session.

**Takeaway:** Friday joins the structural and imaging models to
your TEI, and the cataloguing assignment is due the same day — validate your
header beforehand.

---

## **29 Content**

**Consolidating the Week's Concepts**

A summary table of what has been established across both meetings, which is worth
holding as a whole before Friday.

| Concept | Established in | Function in your edition |
| --- | --- | --- |
| Image API | 3.1 | Retrieve any region of any folio at any size |
| Presentation API | 3.1 | Describe your passage as a structured object |
| Canvas | 3.1 | The coordinate space every layer and annotation targets |
| Fragment selector | 3.1 | Address the exact region supporting a reading |
| Raking light | 3.2 | Reveal ruling, erasure, and dry-point |
| RTI | 3.2 | Model surface relief; recover ink-less writing |
| Multispectral imaging | 3.2 | Recover erased or obscured text |
| PCA, ICA, MNF | 3.2 | Separate ink from parchment and over-text |
| False-colour composite | 3.2 | Present computed components legibly |
| `Choice` | 3.2 | Express spectral alternatives on one canvas |
| Provenance documentation | 3.2 | Make processed images evaluable as evidence |

The unifying idea is that the canvas is a shared coordinate space. Every technique
in the right-hand column ultimately produces something that targets a region of a
canvas — an image painted onto it, an annotation attached to it, a transcription
bound to it. That is what allows the imaging, the transcription, the apparatus,
and the commentary to be parts of one object rather than four separate documents
about the same manuscript (Clausen et al., 2026).

Keep that in view on Friday. The manifest you build is not a container for
pictures; it is the coordinate framework the rest of your edition attaches to.

**Takeaway:** Every technique this week produces something that
targets a canvas region, which is what makes the imaging, transcription, and
apparatus one object.

---

## **30 Content**

**Synthesis: Instruments, Not Photographs**

The claim this meeting has developed is that the digital surrogate is not a
picture of the manuscript but the output of an instrument applied to it.

A visible-light photograph is already an instrument's output, with a spectral
response, a dynamic range, and a colour rendering that are properties of the
camera rather than the object. A UV fluorescence capture is more obviously so. An
ICA composite is unambiguously so: nothing in it corresponds to what any eye could
see under any illumination, and its brightness values represent computed
statistical quantities (Easton et al., 2003).

Two consequences follow, and they pull in opposite directions.

The first is expansive. Instruments can exceed the eye. Erased text becomes
legible; ink-less writing is recovered from surface relief; text is read through
gold leaf by elemental fluorescence. Readings that were permanently lost become
available, and the Archimedes treatises are the demonstration (Easton et al.,
2003).

The second is restrictive. An instrument's output must be interpreted in light of
how it was produced, and an image whose production is undocumented cannot be
evaluated. Statistical enhancement amplifies noise as readily as signal, and
expectation makes false letterforms easy to see. The discipline that makes
recovery trustworthy is documentation and cross-verification, not the technique
itself.

Both are why this lesson sits in a philology course rather than a physics course.
You will not operate this equipment. You will read, cite, and rely on its output,
and doing that responsibly requires knowing what the output is.

**For Friday.** Bring the six items listed in section 28. **The Cataloguing &
Metadata Assignment is due Friday September 18**, and Friday's meeting builds your
manifest and binds it to your TEI.

**Takeaway:** Every manuscript image is an instrument's output,
which is why it can show more than the eye and why it cannot be evaluated without
its documentation.

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
