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

