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
