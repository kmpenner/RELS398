# Topic 03 (Topic_03_IIIF_Imaging): Academic Deep Research Report

**Model:** 3.1 Pro (Deep Research)  
**Attachments:** 3 PDF(s)  
**Citations resolved:** 30

## Digital Humanities IIIF Manuscript Report

ContentsShare & Export
Create

# The Digital Canvas: Synthesizing the International Image Interoperability Framework and Multispectral Imaging in Historical Manuscript Scholarship

## 1. Abstract & Executive Summary

The transition from physical autopsy to the digital surrogate represents a profound epistemological and methodological paradigm shift in textual scholarship, computational philology, and manuscript studies. Historically, the paleographical analysis of medieval manuscripts—particularly damaged witnesses, palimpsests, and severely degraded fragments—relied on direct visual inspection under natural or raking light, which often failed to reveal texts obscured by time, deliberate erasure, or environmental decay. However, the convergence of advanced optical physics and standardized digital architectures has fundamentally redefined the ontological status of the manuscript surrogate. This report investigates the intersection of two pivotal technologies: the International Image Interoperability Framework (IIIF) and multispectral imaging (MSI). Together, these innovations transform the digital edition workflow from a static text-image binary into a dynamic, interoperable, and multimodal investigative environment.

The core thesis substantiated throughout this analysis posits that IIIF image delivery, when combined with multispectral imaging standards, enables interoperable, deep-zoom access to high-resolution manuscript witnesses. This technological convergence recovers damaged or palimpsestic readings that are otherwise invisible to the naked eye, subsequently linking these enriched visual canvases directly to Text Encoding Initiative (TEI) XML transcriptions. For an undergraduate digital methods and textual editing curriculum located in Antigonish, Nova Scotia, Canada, integrating these advanced paradigms offers a robust pedagogical framework. It equips students with the technical proficiencies required to navigate the modern digital humanities landscape, bridging the gap between applied computer science, optical physics, and traditional humanities research.

This exhaustive analysis evaluates the technical foundations of MSI, Reflectance Transformation Imaging (RTI), and IIIF Presentation API 3.0. It proceeds to outline the applied implementation of these technologies in editorial workflows, emphasizing the construction of JSON-LD manifests and spatial coordinate binding. Through a detailed examination of real-world implementations—most notably the Archimedes Palimpsest, the Vatican Library's digital initiatives, and the Princeton Garrett Ms. 24 Palimpsest—the theoretical frameworks are grounded in empirical success. Finally, the analysis provides a comprehensive pedagogical synthesis designed to guide undergraduate digital editors in the construction and management of interoperable manuscript data, culminating in an integrated bibliographic analysis of the foundational literature.

## 2. Technical, Methodological & Historical Foundations

To comprehend the transformative impact of digital imaging and interoperability frameworks on paleography, it is necessary to examine the underlying scientific and architectural principles that govern these technologies. The digital surrogate is no longer a mere photograph; it is a complex data matrix containing spatial, spectral, and semantic information that can be computationally queried and manipulated.

### Multispectral Imaging (MSI) and Material Analysis

Multispectral imaging constitutes a non-destructive, non-invasive computational photography technique that captures image data across discrete, narrow bands of the electromagnetic spectrum, extending beyond human vision into the ultraviolet (UV) and near-infrared (NIR) ranges[1]. The fundamental principle underlying MSI in manuscript studies is that different historical materials—such as parchment collagen, iron-gall ink, carbon-based pigments, and varied binding agents—exhibit distinct optical properties when exposed to specific wavelengths of light[1].

A standard MSI acquisition setup involves a highly controlled illumination environment. High-resolution achromatic cameras, such as the Phase One IQ260 (× pixels), are paired with multispectral LED panels capable of emitting narrow-band radiation from approximately 365 nm (UV) to 940 nm (NIR)[1]. For specific materials like carbon ink or charcoal, infrared cameras operating between 900 nm and 1700 nm are employed[1].

When examining a palimpsest—a manuscript whose original text (*scriptio inferior*) was scraped or washed away to accommodate subsequent writing (*scriptio superior*)—MSI capitalizes on fluorescence and absorption discrepancies. Under UV illumination, parchment typically exhibits intense fluorescence, emitting visible light[1]. Conversely, historical iron-gall inks absorb UV radiation and do not fluoresce, creating a stark contrast ratio that reveals faded or erased underwriting[1]. Infrared imaging operates on a different axis; while carbon inks remain highly absorbent (and thus visible) in the NIR spectrum, many organic dyes and modern over-writings become transparent, allowing scholars to computationally strip away obscuring layers[2].

The raw output of an MSI session is a "datacube"—a three-dimensional array where the x and y axes represent spatial coordinates (pixels), and the z-axis represents the spectral band[3]. This datacube undergoes rigorous registration algorithms to ensure pixel-perfect alignment across all wavelengths, correcting for chromatic aberration and lens distortion prior to advanced signal processing[4].

### Reflectance Transformation Imaging (RTI)

While MSI resolves spectral differentiation, Reflectance Transformation Imaging (RTI)—formerly known as Polynomial Texture Mapping (PTM)—addresses topological phenomena. Developed at Hewlett-Packard Laboratories, RTI captures the microscopic surface geometry of an object by photographing it under varying lighting conditions from a fixed camera position[5].

In a typical RTI dome setup, a manuscript or inscribed artifact is placed at the center of a hemispherical array containing numerous discrete light sources. An image is captured as each light is individually triggered, resulting in an image stack that records how the surface luminance of each pixel changes as a function of the illumination angle[5]. To compute the interactive surface model, the sequence of luminance samples for each pixel is fitted to a biquadratic polynomial equation using Least Squares approximation and Singular Value Decomposition (SVD)[5].

The mathematical model for computing the resultant surface luminance L at local texture coordinates (u,v) given normalized light vectors (lu​,lv​) is expressed as:

L(u,v;lu​,lv​)=a​(u,v)lu​+a​(u,v)lv​+a​(u,v)lu​lv​+a​(u,v)lu​+a​(u,v)lv​+a​(u,v)

By storing the six coefficients (a​ through a​) per pixel in the RTI file, alongside unscaled RGB color values, the rendering software can dynamically interpolate the surface reflectance for any arbitrary light position chosen by the user[5]. Analyzing the derivatives of these polynomials allows for the extraction of surface normal vectors, enabling mathematical specular enhancement and normals unsharp masking[6]. For paleographers studying dry-point glosses, blind tooling, or severely degraded parchment topography, RTI mathematically exaggerates microscopic surface relief, rendering invisible incisions legible[7].

### The International Image Interoperability Framework (IIIF)

The acquisition of high-fidelity MSI and RTI datasets generates massive computational files. Historically, the sheer size of these files resulted in data silos, forcing scholars to download gigabytes of raw data for local processing. The International Image Interoperability Framework (IIIF) resolves this bottleneck by standardizing how images and their structural metadata are delivered across the web[8].

IIIF relies on two foundational application programming interfaces (APIs):

1. **The Image API**: Defines a RESTful web service that returns an image (or a specific region of an image) based on a standardized URL syntax requesting region, size, rotation, quality, and format. This enables dynamic deep-zooming via tiling, where the browser only requests the specific high-resolution tiles required for the current viewport[9].
2. **The Presentation API**: Provides the structural metadata necessary to assemble disparate image tiles into a coherent intellectual object (such as a book). It utilizes JSON-LD (JavaScript Object Notation for Linked Data) to describe the object's physical and conceptual hierarchies[10].

The release of Presentation API 3.0 represents a significant architectural evolution. Moving beyond static images, API 3.0 integrates time-based media (audio and video) by assigning a temporal `duration` dimension to the foundational abstraction of the `Canvas`[11]. Furthermore, version 3.0 mandates the use of JSON-LD 1.1 and the W3C Web Annotation Data Model, shifting away from the deprecated Open Annotation model[11].

| Feature | IIIF Presentation API 2.1 | IIIF Presentation API 3.0 |
| --- | --- | --- |
| **Data Model** | Open Annotation Data Model | W3C Web Annotation Data Model |
| **Context** | JSON-LD 1.0 (`@id`, `@type`) | JSON-LD 1.1 (`id`, `type`) |
| **A/V Support** | Minimal / Non-standard | Native (`duration` property on Canvas) |
| **Image Attachment** | `images` array directly on Canvas | `AnnotationPage` containing `painting` Annotations |
| **Supplemental Material** | Often modeled as structural metadata | `accompanyingCanvas` and `placeholderCanvas` properties |

This abstraction—treating the image not as the page itself, but as an asset *painted* onto a virtual coordinate space via an `AnnotationPage`—is crucial for paleographical analysis[10]. It allows digital editors to paint multiple, distinct image layers onto the exact same spatial dimensions, a feature explicitly utilized in multispectral workflows where scholars must transition seamlessly between visible, ultraviolet, and mathematically processed datasets[12].

## 3. Applied Implementation & Editorial Dimensions

For the digital humanities curriculum in Antigonish, moving from theoretical optics to applied textual editing requires bridging the gap between raw spectral data, IIIF manifest construction, and the Text Encoding Initiative (TEI). This section outlines the applied implementation of these workflows.

### Paleographical Image Enhancement and Signal Separation

Raw multispectral datacubes are rarely legible without post-processing. The primary objective of computational paleography is signal separation: mathematically distinguishing the ink (the signal) from the parchment, stains, and over-text (the noise). Two highly effective statistical transformations dominate this space: Principal Component Analysis (PCA) and Independent Component Analysis (ICA)[2].

| Statistical Method | Analytical Mechanism | Paleographical Application |
| --- | --- | --- |
| **Principal Component Analysis (PCA)** | Orthogonal linear transformation projecting correlated spectral bands into uncorrelated variables (Principal Components). | Maximizes variance. Isolates faded ink signatures into high-contrast grayscale components, separating general parchment texture from distinct material variations. |
| **Independent Component Analysis (ICA)** | Models the datacube as a linear mixture of independent, non-Gaussian source signals to maximize statistical independence. | Untangles overlapping texts. Exceptionally powerful for cleanly separating *scriptio inferior* from *scriptio superior* into distinct output bands. |
| **Minimum Noise Fraction (MNF)** | Two cascaded PCAs determining the inherent dimensionality of image data, segregating noise from relevant data. | Normalizes noise variance across bands, highly effective for extracting trace elemental fluorescence in heavily degraded palimpsests. |

Once these mathematical components are generated, scholars frequently use software such as ENVI or Adobe Photoshop to create "False Color Composites"[13]. By assigning specific PCA, ICA, or MNF output bands to the Red, Green, and Blue (RGB) display channels of a standard digital monitor, editors can produce synthetic images where the erased text appears vividly colored (e.g., bright red or blue) against a neutral background[3]. Through channel splitting, blending modes, and opacity adjustments, these artificially enhanced visual witnesses become the primary resources for subsequent textual transcription[13].

### Constructing the Multimodal IIIF Manifest

To serve these enhanced images to the scholarly community, they must be organized within a IIIF Presentation API 3.0 Manifest. A critical feature of API 3.0 for MSI data is the `Choice` mechanism[12].

When a single manuscript folio has been imaged in natural color, UV fluorescence, and as a PCA false-color composite, these three images represent the exact same physical space. In the IIIF manifest, the `Canvas` is instantiated with the pixel dimensions of the highest-resolution image. The `AnnotationPage` targeting that Canvas contains an Annotation whose `body` is not a single Image, but a `Choice` object[12]. The `Choice` object lists multiple Image resources, allowing compliant IIIF viewers (such as Mirador 3 or Universal Viewer) to render a user interface where the scholar can toggle, blend, or adjust the opacity between the natural light image, the UV image, and the enhanced PCA composite directly in the browser[12].

This capability to superimpose and cross-fade spectral layers in real-time fundamentally alters the paleographer's workflow. It permits the rapid verification of questionable readings by alternating between the spectral conditions that best highlight distinct ink formulations, without necessitating the downloading of monolithic datasets[14].

### Spatial Coordinates and TEI-XML Binding

The definitive act of digital textual scholarship is linking the visual evidence to the critical transcription. The Text Encoding Initiative (TEI) P5 guidelines provide specific modules for representing primary sources. Within the TEI framework, the physical document is modeled using the `<facsimile>`, `<surface>`, and `<zone>` elements[15].

To create a bidirectional link between the TEI transcription and the IIIF visual architecture, the coordinate systems must be synchronized. The TEI `<surface>` element conceptually maps to the IIIF `Canvas`, while the TEI `<zone>` element corresponds to a specific bounding box on that Canvas[16]. Using the `att.global.facs` module, editors can inject IIIF fragment selectors directly into the TEI code[17]. For example, if a scholar transcribes a specific line of text corresponding to a heavily damaged region, the TEI `<line>` or `<zone>` element uses the `@facs` attribute to reference the IIIF Canvas URI appended with a spatial fragment identifier in the format `#xywh=x,y,width,height`[18].

XML

```
<facsimile>
 <surface xml:id="folio_1v" facs="https://example.edu/iiif/canvas/p1">
 <zone xml:id="line_1" facs="https://example.edu/iiif/canvas/p1#xywh=150,300,2000,120"/>
 </surface>
</facsimile>
<text>
 <body>
 <pb facs="#folio_1v"/>
 <lb facs="#line_1"/>Incipit tractatus de scientia venandi per aves...
 </body>
</text>
```

This interoperable syntax allows advanced digital edition platforms to parse the TEI document and automatically render the corresponding IIIF image tile side-by-side with the text. When a user interacts with a line of transcription, the IIIF viewer automatically pans and zooms to the exact pixel coordinates of the erased ink, facilitating a seamless verification process between the editorial assertion and the material witness[17].

### Integration with Handwritten Text Recognition (HTR)

The manual transcription of digitized manuscripts is highly labor-intensive. Consequently, the digital edition workflow increasingly incorporates machine learning platforms for Handwritten Text Recognition (HTR) and Optical Character Recognition (OCR), most notably Transkribus and eScriptorium[19].

These platforms leverage the IIIF architecture to ingest manuscript images directly via Manifest URIs, eliminating the need to transfer vast gigabytes of TIFF files manually[19]. Within a platform like eScriptorium—which utilizes the Kraken open-source OCR/HTR engine and the YALTAi (You Actually Look Twice At it) object detection framework—the imported IIIF images undergo automatic layout analysis[19]. YALTAi utilizes an object detection approach rather than traditional region segmentation, achieving highly accurate baseline identification on complex historical manuscripts[20].

Scholars can train custom neural network models on small samples of manually transcribed ground truth (often as few as 50 pages). As the models learn the distinct paleographical characteristics of a specific scribe, they automatically generate bounding boxes (zones) and text predictions for the remainder of the manuscript[21]. The output is typically structured in ALTO XML or PAGE XML formats, which possess native structural equivalence to TEI and maintain the vital pixel-coordinate bindings established during the HTR layout analysis phase[19]. This alignment between digital texts and manuscript images significantly reduces the cost of training character recognition models[22]. For students, this human-in-the-loop AI workflow represents the vanguard of modern textual production[19].

## 4. Real-World Digital Edition Case Studies

The theoretical integration of MSI, IIIF, and TEI is best understood through the lens of monumental real-world applications that have redefined the boundaries of textual recovery.

### The Archimedes Palimpsest

The Archimedes Palimpsest stands as the most famous modern example of computational text recovery. The artifact is a 10th-century parchment manuscript containing unique Greek copies of seven treatises by the mathematician Archimedes. In the 13th century, the parchment was unbound, scraped of its ink, cut in half, and overwritten with a Christian prayer book (the Euchologion) to recycle the valuable substrate[23].

When traditional visible-light photography failed to penetrate the Euchologion over-text, a decade-long multidisciplinary project was initiated. Imaging scientists captured MSI data ranging from ultraviolet to near-infrared. Furthermore, because certain folios had been coated in forged Byzantine gold leaf in the 20th century—completely obscuring the parchment—scientists employed X-ray fluorescence (XRF) imaging at the Stanford Synchrotron Radiation Lightsource. The intense X-ray beams caused the iron atoms in the 10th-century iron-gall ink to fluoresce, penetrating the gold leaf entirely[3].

By feeding the multispectral and XRF datacubes through PCA and ICA algorithms, researchers generated pseudocolored composite images that visually suppressed the 13th-century prayers and illuminated Archimedes' mathematical diagrams and text in stark clarity[2]. This project demonstrated unequivocally that historical documents must be treated as complex, multi-layered chemical and topological matrices, paving the way for the subsequent development of IIIF models capable of handling multi-layer object representation[24].

### DigitaVaticana and the Vatican Apostolic Library

While the Archimedes project proved the efficacy of MSI, the Vatican Apostolic Library demonstrated the scalability of the IIIF Presentation API. The Vatican holds one of the world's most significant collections of historical manuscripts. To digitize and disseminate this immense corpus, they launched the DigitaVaticana initiative, fully embracing IIIF standards[2].

By utilizing the IIIF Image API, the Vatican avoids pre-generating static zoom-level images for every manuscript. Instead, high-resolution master files are dynamically tiled and served upon request. Through the Presentation API, the metadata and structural sequence of the codices are mapped into JSON-LD manifests. These manifests are consumed by the Mirador viewer, an open-source, web-based workspace. Mirador enables scholars globally to open multiple Vatican manuscripts side-by-side, compare variant readings of classical texts, and utilize deep-zoom capabilities without taxing local institutional bandwidth[25]. The Vatican's deployment validated IIIF as the premier architecture for massive-scale cultural heritage dissemination.

### The Princeton Garrett Ms. 24 Palimpsest

At Princeton University Library, the Garrett Ms. 24 manuscript provided an exceptional test case for the integration of MSI viewing within standard library catalog interfaces. Garrett Ms. 24 is a 10th-century Greek palimpsest concealing 6th to 9th-century Greek and Christian Palestinian Aramaic undertexts[26].

Following multispectral capture, scholars generated dozens of processed images per folio to isolate different scripts and material anomalies. Utilizing IIIF, Princeton hosted the enhanced images and integrated a IIIF-compliant viewer directly into their online catalog. The implementation allows researchers to utilize a dropdown interface within the viewer to seamlessly toggle between narrow-band captures (e.g., specific UV or IR wavelengths) and algorithmically processed PCA composites[26]. This case study emphasizes that providing access to MSI data requires robust user interface design; simply hosting raw datacubes is insufficient. By leveraging IIIF `Choice` annotations, Princeton effectively packaged complex optical physics into a manageable, accessible web interface for philologists[26].

### Codex Sinaiticus and Early Biblical Witnesses

The principles of image interoperability and multispectral analysis extend prominently into the preservation of early biblical texts, such as the Codex Sinaiticus. As one of the oldest extant manuscripts of the Christian Bible, the physical artifact is distributed across four distinct international institutions (the British Library, Leipzig University Library, St Catherine's Monastery, and the National Library of Russia). Prior to interoperable standards, scholarly unification of the text required immense logistical coordination. Digital facsimile projects surrounding the Codex Sinaiticus utilized advanced imaging to enhance faded carbon inks on ancient parchment, revealing textual variants and scribal corrections[27]. The subsequent virtual unification of these globally dispersed fragments via standardized digital frameworks exemplifies how interoperability transcends physical geography, allowing an integrated paleographical analysis of the recovered text.

## 5. Pedagogical Takeaways & Synthesis for Digital Editors

For the undergraduate curriculum in Antigonish, Nova Scotia, synthesizing these advanced methodologies into a manageable pedagogical framework is essential. The modern digital editor must possess hybrid expertise: an understanding of traditional paleography and codicology, competence in optical imaging theory, and literacy in linked data architectures.

To operationalize this curriculum, a structured pathway—broken into sequential lab modules—provides practical checklists for students developing digital editions.

| Pedagogical Stage | Core Competencies & Deliverables | Practical Checklist for Students |
| --- | --- | --- |
| **1. Image Acquisition & Spectral Processing** | Understanding material optics (UV fluorescence, IR absorbance). Handling raw TIFF datacubes and applying dimensionality reduction (PCA, ICA, MNF). | - [ ] Identify substrate and ink properties. - [ ] Import MSI datacube into ImageJ/ENVI. - [ ] Execute PCA/ICA separation algorithms. - [ ] Export false-color composite TIFFs isolating *scriptio inferior*[1]. |
| **2. Constructing the IIIF Manifest (API 3.0)** | Formatting JSON-LD 1.1. Constructing `Manifest`, `Canvas`, and `AnnotationPage` objects. Implementing the `Choice` mechanism for layering. | - [ ] Define Manifest metadata (`id`, `label`, `summary`). - [ ] Map dimensions to the Canvas object. - [ ] Build `AnnotationPage` targeting the Canvas. - [ ] Embed a `Choice` array within the Annotation body containing RGB, UV, and PCA image variants[11]. |
| **3. Machine Learning Integration (HTR/OCR)** | Interfacing IIIF with AI platforms (eScriptorium, Transkribus). Training custom neural networks on historical scripts. | - [ ] Ingest IIIF Manifest URI into eScriptorium. - [ ] Run YALTAi/Kraken layout analysis. - [ ] Manually transcribe a 50-page Ground Truth dataset. - [ ] Train custom model and export results to ALTO/PAGE XML[19]. |
| **4. TEI-XML Encoding & Spatial Binding** | Transforming ALTO/PAGE XML to TEI P5. Binding transcriptions to spatial coordinates using IIIF fragment selectors. | - [ ] Structure document using `<facsimile>` and `<text>`. - [ ] Define `<surface>` mapping to IIIF Canvas URI. - [ ] Define `<zone>` utilizing `#xywh=x,y,w,h` selector. - [ ] Link transcription tags (e.g., `<lb>`) via `@facs` to specific zones[15]. |
| **5. Dissemination & Viewer Integration** | Deploying the multimodal edition via compliant workspaces (Mirador 3, Universal Viewer). | - [ ] Load Manifest into Mirador 3. - [ ] Verify successful rendering of the `Choice` layer toggle. - [ ] Integrate TEI XML parser to display synchronized text/image panes[28]. |

By traversing this pipeline, students internalize the reality that a digital edition is not a static representation, but a dynamic, queryable database. The integration of IIIF viewers into their final web projects allows them to present an interactive edition where users can zoom into a manuscript, toggle to a multispectral layer to reveal an erased text, and click on an augmented TEI bounding box to view the diplomatic transcription simultaneously[29].

## 6. Comprehensive Academic & Technical References

The maturation of digital manuscript studies, as evidenced by the convergence of multispectral analysis and interoperable frameworks, is heavily documented across several foundational pillars of academic and technical literature. The following bibliographic synthesis provides a comprehensive overview of the core texts, algorithms, and specifications that underpin the methodologies discussed in this report.

| Author(s) / Organization | Title / Source | Contribution / Relevance to Field | Persistent Identifier (DOI/URL) |
| --- | --- | --- | --- |
| **Clausen, H., Brenner, S., Schreiner, M., & Vetter, W.** | *Multimodal manuscript representation: toward an open repository for manuscript research data* (Eur. Phys. J. Plus, 2026) | Establishes the framework for integrating heterogeneous CIMA datasets (MSI, XRF, Raman spectroscopy, TEI, METS) into a unified, interoperable digital repository. Highlights the necessity of linking physical material analyses to structural textual encodings[1]. | [https://doi.org/10.1140/epjp/s13360-025-07133-y](https://doi.org/10.1140/epjp/s13360-025-07133-y) [Download PDF](https://libkey.io/libraries/3054/articles/704889479/full-text-file?utm_source=nomad) |
| **Griffin, S. M.** | *Digital Libraries, Epigraphy and Paleography: Bring Records from the Distant Past to the Present* (Int. J. on Digital Libraries, 2023) | Analyzes the evolution of scholarly infrastructures supporting epigraphy and paleography. Discusses the impact of IIIF, deep-zoom visualization (Mirador), and AI-driven HTR (Transkribus, Kraken) on accelerating textual recovery[1]. | [https://doi.org/10.1007/s00799-023-00381-2](https://doi.org/10.1007/s00799-023-00381-2) [Download PDF](https://libkey.io/libraries/3054/articles/585996952/full-text-file?utm_source=nomad) |
| **IIIF Consortium** | *IIIF Presentation API 3.0 Specification* (2020) | The definitive technical standard for delivering complex, compound digital objects on the web. Details the transition to JSON-LD 1.1, the W3C Web Annotation Data Model, the implementation of Canvas `duration`, and the `Choice` mechanism[30]. | [https://iiif.io/api/presentation/3.0/](https://iiif.io/api/presentation/3.0/) |
| **Easton, R. L., Knox, K. T., & Christens-Barry, W. A.** | *Multispectral imaging of the Archimedes palimpsest* (32nd Applied Imagery Pattern Recognition Workshop, 2003) | A seminal text detailing the application of MSI and advanced signal processing (PCA, ICA) to recover the *scriptio inferior* of the Archimedes Palimpsest. Validated the necessity of computational optics in textual preservation[23]. | [https://doi.org/10.1109/AIPR.2003.1284258](https://doi.org/10.1109/AIPR.2003.1284258) |
| **Malzbender, T., Gelb, D., & Wolters, H.** | *Polynomial Texture Maps* (Hewlett-Packard Laboratories, 2001) | Introduces the mathematical foundation for Reflectance Transformation Imaging (RTI). Explains the extraction of surface normal vectors and specular enhancement through biquadratic polynomial modeling[5]. | [http://www.hpl.hp.com/research/ptm/papers/ptm.pdf](http://www.hpl.hp.com/research/ptm/papers/ptm.pdf) |
| **eScriptorium / Kraken** | *eScriptorium Platform Documentation* (2024) | Details the architecture of an open-source platform integrating HTR and OCR for historical documents. Explains the ingestion of IIIF Manifests and the application of YALTAi object detection for complex layout analysis[19]. | [https://escriptorium.eu/about](https://escriptorium.eu/about) |
| **Text Encoding Initiative (TEI)** | *TEI P5: Guidelines for Electronic Text Encoding and Interchange* (2026) | The standard for digitally representing textual structures. Explains the use of the `<facsimile>`, `<surface>`, and `<zone>` elements in conjunction with `#xywh` fragment selectors to bind transcriptions to specific IIIF Canvas coordinates[15]. | [https://www.tei-c.org/release/doc/tei-p5-doc/en/html/](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/) |

This synthesis of foundational optical physics, evolving data standards, and applied machine learning models encapsulates the interdisciplinary rigor required of modern manuscript studies. By grounding textual scholarship in the empirical realities of material science and linked open data, the digital humanities curriculum ensures the preservation and recovery of global cultural heritage for subsequent generations of scholars.

Sources used in the report

04_Multimodal_manuscript_representation_toward_an_open_repository_for_manuscript_re.pdf

[scholarsarchive.byu.edu

Multispectral Analysis of a Vatican Library Palimpsest - BYU ScholarsArchive

 Opens in a new window](https://scholarsarchive.byu.edu/cgi/viewcontent.cgi?article=3822&context=jur)[image.ntua.gr

hyperspectral imaging: potential in non-destructive analysis of palimpsests

 Opens in a new window](http://image.ntua.gr/iva/files/Hyperspectral%20imaging%20-%20Potential%20in%20non-destructive%20analysis%20of%20palimpsests%20-%20K.%20Rapantzikos2005.pdf)[researchgate.net

Multispectral imaging of the Archimedes palimpsest | Request PDF - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/4067608_Multispectral_imaging_of_the_Archimedes_palimpsest)[repository.rit.edu

"Multispectral imaging and analysis of the Archimedes Palimpsest" by D. Michael Hansen

 Opens in a new window](https://repository.rit.edu/theses/7957/)[repositum.tuwien.at

Restoration of Multispectral Images of Ancient Documents - reposiTUm

 Opens in a new window](https://repositum.tuwien.at/bitstream/20.500.12708/19463/1/Hollaus%20Fabian%20-%202021%20-%20Restoration%20of%20multispectral%20images%20of%20ancient%20documents.pdf)[researchgate.net

Palimpsest Research Based on Hyperspectral Information | Request PDF - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/370616291_Palimpsest_Research_Based_on_Hyperspectral_Information)[cceh.github.io

Introduction to RTI — RTI 0.1.1 documentation

 Opens in a new window](https://cceh.github.io/rti/intro.html)[bibalex.org

3D Surface Reconstruction Using Polynomial Texture Mapping - Bibliotheca Alexandrina

 Opens in a new window](https://www.bibalex.org/isis/UploadedFiles/Publications/3D%20Surface%20Reconstruction%20Using%20Polynomial%20Texture%20Mapping.pdf)[researchgate.net

(PDF) Polynomial texture maps - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/220720751_Polynomial_texture_maps)[spiedigitallibrary.org

Enhancing manuscript analysis with reflectance transformation imaging: a user study on interactive visualization options - SPIE Digital Library

 Opens in a new window](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/13569/135690L/Enhancing-manuscript-analysis-with-reflectance-transformation-imaging--a-user/10.1117/12.3062630.full)[mdpi.com

Close-Range Photogrammetry and RTI for 2.5D Documentation of Painted Surfaces: A Tiryns Mural Case Study - MDPI

 Opens in a new window](https://www.mdpi.com/2079-6412/15/4/388)[europeana.atlassian.net

IIIF APIs - Europeana Knowledge Base - Confluence

 Opens in a new window](https://europeana.atlassian.net/wiki/spaces/EF/pages/1627914244/IIIF+APIs+Documentation)[iiif.io

IIIF Announces Final Release of 3.0 Specifications

 Opens in a new window](https://iiif.io/news/2020/06/04/IIIF-C-Announces-Final-Release-of-3.0-Specifications/)[loc.gov

Image Services | Microservices | APIs at the Library of Congress

 Opens in a new window](https://www.loc.gov/apis/micro-services/image-services/)[iiif.io

API Specifications - International Image Interoperability Framework™ — IIIF

 Opens in a new window](https://iiif.io/api/)[mattmcgrattan.github.io

IIIF Presentation API 3.0 (quick introduction) - GitHub Pages

 Opens in a new window](https://mattmcgrattan.github.io/Washington%20Annotation%20Workshop/IIIF%20Presentation%20API%203.0%20(quick%20introduction).html)[iiif.io

Presentation API 3.0 Change Log — IIIF | International Image Interoperability Framework

 Opens in a new window](https://iiif.io/api/presentation/3.0/change-log/)[iiif.io

Content Search API 2.0 Change Log — IIIF | International Image Interoperability Framework

 Opens in a new window](https://iiif.io/api/search/2.0/change-log/)[iiif.io

Multiple Choice of Images in a Single View (Canvas) — IIIF

 Opens in a new window](https://iiif.io/api/cookbook/recipe/0033-choice/)[iiif.io

Composition from Multiple Images — IIIF | International Image Interoperability Framework

 Opens in a new window](https://iiif.io/api/cookbook/recipe/0036-composition-from-multiple-images/)[projects.history.qmul.ac.uk

Multi-Spectral Imaging – Hidden in Plain Sight - QMUL History Projects

 Opens in a new window](https://projects.history.qmul.ac.uk/inplainsight/multi-spectral-imaging/)[rdr.ucl.ac.uk

Real and simulated multispectral imaging of a palimpsest - UCL Research Data Repository

 Opens in a new window](https://rdr.ucl.ac.uk/articles/dataset/Real_and_simulated_multispectral_imaging_of_a_palimpsest/28920179)[avenza.com

Creating a false-color composite image with Geographic Imager for Adobe Photoshop

 Opens in a new window](https://www.avenza.com/resources/blog/2010/06/03/creating-false-color-composite-image-geographic-imager-adobe-photoshop/)[support.avenza.com

False-Colour Composite with Multiple Images Tutorial - Avenza Systems

 Opens in a new window](https://support.avenza.com/hc/en-us/articles/360059420592-False-Colour-Composite-with-Multiple-Images-Tutorial)[doc.esri.com

Apply transparency and blending modes | ArcGIS Pro documentation - Esri

 Opens in a new window](https://doc.esri.com/en/arcgis-pro/latest/help/mapping/layer-properties/apply-visual-effects.html)[iiif.io

Presentation API 3.0 — IIIF | International Image Interoperability Framework

 Opens in a new window](https://iiif.io/api/presentation/3.0/)[digitalcollections.lib.washington.edu

Mirador 3 Viewer - University of Washington Digital Collections

 Opens in a new window](https://digitalcollections.lib.washington.edu/digital/custom/mirador3?manifest=https://digitalcollections.lib.washington.edu//iiif/info/eurasia/5784/manifest.json)[github.com

vanda/iiif-features: Code and demos around the use of IIIF - GitHub

 Opens in a new window](https://github.com/vanda/iiif-features)[tei-c.org

Example: - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/examples-line.html)[tei-c.org

TEI element facsimile - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-facsimile.html)[palimpsest.stmarytx.edu

Streamlining Text Encoding Initiative (TEI), International Image Interoperability Framework (IIIF), and Mirador: Theoretical and Practical Considerations for Interactive Critical Editions - The Jubilees Palimpsest Project

 Opens in a new window](https://palimpsest.stmarytx.edu/thanneken/2024/dh/)[sfu.ca

TEI element line

 Opens in a new window](https://www.sfu.ca/~takeda/tei-guidelines/issue_2382_eventName/html/ref-line.html)[iiif.io

Open a specific region of a Canvas in a viewer — IIIF

 Opens in a new window](https://iiif.io/api/cookbook/recipe/0485-contentstate-canvas-region/)[iiif.io

Represent Canvas Fragment as a Geographic Area in a Web Mapping Client — IIIF

 Opens in a new window](https://iiif.io/api/cookbook/recipe/0139-geolocate-canvas-fragment/)[escriptorium.eu

About - eScriptorium

 Opens in a new window](https://escriptorium.eu/about)[transkribus.org

Transkribus for Digital Humanities — AI-Powered Historical Document Analysis

 Opens in a new window](https://www.transkribus.org/digital-humanities)[help.transkribus.org

1. Uploading - Transkribus Help Center

 Opens in a new window](https://help.transkribus.org/uploading-files-to-transkribus)[researchgate.net

You Actually Look Twice At it (YALTAi): using an object detection approach instead of region segmentation within the Kraken engine - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/376848716_You_Actually_Look_Twice_At_it_YALTAi_using_an_object_detection_approach_instead_of_region_segmentation_within_the_Kraken_engine)[ub-mannheim.github.io

Training with eScriptorium (a step-by-step guide) - UB Mannheim - GitHub Pages

 Opens in a new window](https://ub-mannheim.github.io/eScriptorium_Dokumentation/Training-with-eScriptorium-EN.html)[github.com

GitHub - Freymat/from_eScriptorium_to_Passim_and_back: Pipeline for ground truth creation to train text recognition models. Extracts OCR results from eScriptorium, prepare them for alignment with passim and import the valid alignments back to eScriptorium.

 Opens in a new window](https://github.com/Freymat/from_eScriptorium_to_Passim_and_back)[archimedespalimpsest.org

Imaging of the Archimedes Palimpsest

 Opens in a new window](https://www.archimedespalimpsest.org/about/imaging/)[semanticscholar.org

Multispectral imaging of the Archimedes palimpsest - Semantic Scholar

 Opens in a new window](https://www.semanticscholar.org/paper/Multispectral-imaging-of-the-Archimedes-palimpsest-Easton-Knox/fb9460a2110734406508a14de0678c96399487ea)[researchgate.net

Digital Transcription of the Archimedes Palimpsest [Applications Corner] - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/3322061_Digital_Transcription_of_the_Archimedes_Palimpsest_Applications_Corner)[iiif.io

Vatican Library — IIIF - International Image Interoperability Framework

 Opens in a new window](https://iiif.io/guides/guides/vatlib.it/)[specialcollections.princeton.edu

Multispectral Imaging of an Aramaic and Greek Palimpsest - Special Collections

 Opens in a new window](https://specialcollections.princeton.edu/2023/07/multispectral-imaging-of-an-aramaic-and-greek-palimpsest/)

03_SPECIAL_PROJECTS_CASES_AND_CONTENT_ANALYSIS.pdf

05_Digital_Libraries,_Epigraphy_and_Paleography_Bring_Records_from_the_Distant_Past.pdf

Sources read but not used in the report
[iiif.io

Linking external Annotations targeting a Canvas to a Manifest — IIIF

 Opens in a new window](https://iiif.io/api/cookbook/recipe/0306-linking-annotations-to-manifests/)[teibyexample.org

Tutorials | Module 8: Customising TEI, ODD, Roma

 Opens in a new window](https://teibyexample.org/exist/tutorials/TBED08v00.htm)[iiif.io

Addressing a Spatial Region — IIIF | International Image Interoperability Framework

 Opens in a new window](https://iiif.io/api/cookbook/recipe/0299-region/)[medium.com

Beyond the Viewer: fragments and links in annotation space | by Tom Crane | digirati-ch

 Opens in a new window](https://medium.com/digirati-ch/beyond-the-viewer-fragments-and-links-in-annotation-space-b3284e25f34)[semanticscholar.org

Polynomial texture mapping and 3D representations - Semantic Scholar

 Opens in a new window](https://www.semanticscholar.org/paper/Polynomial-texture-mapping-and-3D-representations-MacDonald-Robson/98c832a2b8a3e22f7d45308d1cfc064bc0305354)[crs4.it

Light calibration and quality assessment methods for Reflectance Transformation Imaging applied to artworks' analysis - CRS4

 Opens in a new window](https://www.crs4.it/vic/data/papers/spie2015-rti.pdf)[pmc.ncbi.nlm.nih.gov

Performance of Principal Component Analysis and Independent Component Analysis with Respect to Signal Extraction from Noisy Positron Emission Tomography Data - a Study on Computer Simulated Images - PMC

 Opens in a new window](https://pmc.ncbi.nlm.nih.gov/articles/PMC2703833/)[transkribus.org

Transkribus for Researchers - The Controllable Pipeline for Historical Documents

 Opens in a new window](https://www.transkribus.org/for-researchers)[iiif.io

Transkribus and IIIF: beneficial possibilities between image sharing and Handwritten Text Recognition frameworks

 Opens in a new window](https://iiif.io/event/2019/goettingen/program/26/)[atrium-research.eu

Workflows - ATRIUM Project

 Opens in a new window](https://atrium-research.eu/workflows/)[researchgate.net

Multispectral imaging for analyzing ancient manuscripts - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/228983565_Multispectral_imaging_for_analyzing_ancient_manuscripts)[iiif.io

Providing Alternative Representations — IIIF | International Image Interoperability Framework

 Opens in a new window](https://iiif.io/api/cookbook/recipe/0046-rendering/)[arxiv.org

[2312.11116] Implementation of the IIIF Presentation API 3.0 based on Software Support: Use Case of an Incremental IIIF Deployment within a Citizen Science Project - arXiv

 Opens in a new window](https://arxiv.org/abs/2312.11116)[stackoverflow.com

How to implement search with hit highlight in Universal Viewer - Stack Overflow

 Opens in a new window](https://stackoverflow.com/questions/62888923/how-to-implement-search-with-hit-highlight-in-universal-viewer)[github.com

Support for IIIF Content Search API · Issue #187 · tify-iiif-viewer/tify - GitHub

 Opens in a new window](https://github.com/tify-iiif-viewer/tify/issues/187)[scispace.com

Multispectral imaging of the Archimedes palimpsest (2003) | Roger L. Easton | 114 Citations

 Opens in a new window](https://scispace.com/papers/multispectral-imaging-of-the-archimedes-palimpsest-4okkk6vs40)[scilit.com

Multispectral imaging of the archimedes palimpsest - Scilit

 Opens in a new window](https://www.scilit.com/publications/bb47f8e0db09bf995945c78ef9873801)[iiif-ml-workshop.netlify.app

More about annotations - IIIF for Machine Learning

 Opens in a new window](https://iiif-ml-workshop.netlify.app/docs/annotations-and-iiif/more-about-annotations)[iiif.io

The Cookbook of IIIF Recipes - International Image Interoperability Framework

 Opens in a new window](https://iiif.io/get-started/cookbook/)[iiif-prezi.github.io

Composition from Multiple Images - iiif-prezi3 - GitHub Pages

 Opens in a new window](https://iiif-prezi.github.io/iiif-prezi3/recipes/0036-composition-from-multiple-images/)[github.com

awesome-iiif/readme.md at main - GitHub

 Opens in a new window](https://github.com/IIIF/awesome-iiif/blob/main/readme.md)[iiif.io

Code Samples — IIIF | International Image Interoperability Framework

 Opens in a new window](https://iiif.io/api/cookbook/recipe/code/)[iiif.io

Full recipe list — IIIF | International Image Interoperability Framework

 Opens in a new window](https://iiif.io/api/cookbook/recipe/all/)[iiif.io

IIIF Content State API 0.3 - International Image Interoperability Framework

 Opens in a new window](https://iiif.io/api/content-state/0.3/)[github.com

IIIF-Commons/presentation-3-types - GitHub

 Opens in a new window](https://github.com/IIIF-Commons/presentation-3-types)[iiif.io

Annotate specific images or layers — IIIF

 Opens in a new window](https://iiif.io/api/cookbook/recipe/0326-annotating-image-layer/)[iiif.io

Grouping Annotations into Collections - International Image Interoperability Framework

 Opens in a new window](https://iiif.io/api/cookbook/recipe/0309-annotation-collection/)[iiif.io

Presentation API 2.1.1 — IIIF | International Image Interoperability Framework

 Opens in a new window](https://iiif.io/api/presentation/2.1/)
Thoughts

Technical Foundations and Protocols

I am evaluating how image interoperability standards and advanced imaging techniques intersect to enhance manuscript scholarship. My investigation focuses on analyzing the underlying structural APIs that enable high-resolution visual rendering, dynamic zoom, and standardized metadata sharing across digital repositories.

Integrating Visual Artifacts with Textual Data

I am exploring how spatial coordinate systems bridge the gap between spectral imagery and textual transcription. By linking specific canvas coordinates directly to encoded diplomatic editions, I am mapping out workflows that connect revealed historical text fragments directly to scholarly annotations.

Planned Research Actions

I will search for precise specification details regarding presentation manifests, image request formats, and encoding schemes for spatial boundaries. Additionally, I will examine real-world manuscript recovery projects and multispectral transformation algorithms to illustrate these integrated workflows.

[mattmcgrattan.github.io

IIIF Presentation API 3.0 (quick introduction) - GitHub Pages](https://mattmcgrattan.github.io/Washington%20Annotation%20Workshop/IIIF%20Presentation%20API%203.0%20(quick%20introduction).html)[github.com

IIIF-Commons/presentation-3-types - GitHub](https://github.com/IIIF-Commons/presentation-3-types)[iiif.io

Presentation API 3.0 Change Log — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/3.0/change-log/)[europeana.atlassian.net

IIIF APIs - Europeana Knowledge Base - Confluence](https://europeana.atlassian.net/wiki/spaces/EF/pages/1627914244/IIIF+APIs+Documentation)[iiif.io

Linking external Annotations targeting a Canvas to a Manifest — IIIF](https://iiif.io/api/cookbook/recipe/0306-linking-annotations-to-manifests/)[iiif.io

Presentation API 3.0 — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/3.0/)[loc.gov

Image Services | Microservices | APIs at the Library of Congress](https://www.loc.gov/apis/micro-services/image-services/)

Mapping TEI Text to IIIF Canvases

Analyzing how spatial coordinates link diplomatic text transcriptions directly to manuscript image regions. I am examining how TEI XML structures, such as facsimile surfaces and zone definitions, map bounding box coordinates to IIIF Presentation API 3.0 fragment selectors using standard alignment attributes.

Spectral Image Processing and Analytical Algorithms

Evaluating image enhancement techniques for recovering damaged, erased, or palimpsestic text. I am reviewing manual workflows in graphic tools—such as channel splitting, false-color composites, and curve adjustments—alongside statistical algorithms like Principal Component Analysis and Independent Component Analysis to separate overlapping ink layers.

Case Study Integration and Practical Workflows

Synthesizing real-world applications across major manuscript projects, including the multispectral and X-ray recovery of the Archimedes Palimpsest, the cross-repository digital collation of the Codex Sinaiticus, and large-scale digitizations at the Vatican Library. I am now structuring these findings into a curriculum and technical framework for digital editing labs.

[teibyexample.org

Tutorials | Module 8: Customising TEI, ODD, Roma](https://teibyexample.org/exist/tutorials/TBED08v00.htm)[palimpsest.stmarytx.edu

Streamlining Text Encoding Initiative (TEI), International Image Interoperability Framework (IIIF), and Mirador: Theoretical and Practical Considerations for Interactive Critical Editions - The Jubilees Palimpsest Project](https://palimpsest.stmarytx.edu/thanneken/2024/dh/)[iiif.io

Open a specific region of a Canvas in a viewer — IIIF](https://iiif.io/api/cookbook/recipe/0485-contentstate-canvas-region/)[tei-c.org

TEI element facsimile - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-facsimile.html)[tei-c.org

Example: - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/examples-line.html)[iiif.io

Represent Canvas Fragment as a Geographic Area in a Web Mapping Client — IIIF](https://iiif.io/api/cookbook/recipe/0139-geolocate-canvas-fragment/)[iiif.io

Addressing a Spatial Region — IIIF | International Image Interoperability Framework](https://iiif.io/api/cookbook/recipe/0299-region/)[sfu.ca

TEI element line](https://www.sfu.ca/~takeda/tei-guidelines/issue_2382_eventName/html/ref-line.html)[medium.com

Beyond the Viewer: fragments and links in annotation space | by Tom Crane | digirati-ch](https://medium.com/digirati-ch/beyond-the-viewer-fragments-and-links-in-annotation-space-b3284e25f34)[avenza.com

Creating a false-color composite image with Geographic Imager for Adobe Photoshop](https://www.avenza.com/resources/blog/2010/06/03/creating-false-color-composite-image-geographic-imager-adobe-photoshop/)[support.avenza.com

False-Colour Composite with Multiple Images Tutorial - Avenza Systems](https://support.avenza.com/hc/en-us/articles/360059420592-False-Colour-Composite-with-Multiple-Images-Tutorial)[iiif.io

Vatican Library — IIIF - International Image Interoperability Framework](https://iiif.io/guides/guides/vatlib.it/)

Mathematical and Imaging Fundamentals

I am examining the mathematical models and physical mechanisms required for advanced artifact recovery. This involves analyzing polynomial texture mapping equations for surface normal estimation, evaluating statistical pixel-separation algorithms like principal and independent component analysis for unmixing overwritten text layers, and outlining multispectral wavelength setups across ultraviolet and infrared bands.

Case Study Architectures

I am studying landmark digital restoration initiatives to observe these techniques in practice. My analysis centers on how synchrotron-based X-ray fluorescence mapped hidden text in the Archimedes Palimpsest, how multi-repository collation and raking-light capture were applied in the Codex Sinaiticus project, and how large-scale digital manuscript repositories handle high-fidelity storage formats and manifest generation.

Deep Technical Exploration

I will conduct targeted queries to capture exact mathematical formulations for surface enhancement techniques, precise excitation-emission parameters for manuscript recovery, and technical details regarding multi-spectral layer opacity blending within interactive viewers.

[researchgate.net

(PDF) Polynomial texture maps - ResearchGate](https://www.researchgate.net/publication/220720751_Polynomial_texture_maps)[cceh.github.io

Introduction to RTI — RTI 0.1.1 documentation](https://cceh.github.io/rti/intro.html)[semanticscholar.org

Polynomial texture mapping and 3D representations - Semantic Scholar](https://www.semanticscholar.org/paper/Polynomial-texture-mapping-and-3D-representations-MacDonald-Robson/98c832a2b8a3e22f7d45308d1cfc064bc0305354)[bibalex.org

3D Surface Reconstruction Using Polynomial Texture Mapping - Bibliotheca Alexandrina](https://www.bibalex.org/isis/UploadedFiles/Publications/3D%20Surface%20Reconstruction%20Using%20Polynomial%20Texture%20Mapping.pdf)[crs4.it

Light calibration and quality assessment methods for Reflectance Transformation Imaging applied to artworks' analysis - CRS4](https://www.crs4.it/vic/data/papers/spie2015-rti.pdf)[spiedigitallibrary.org

Enhancing manuscript analysis with reflectance transformation imaging: a user study on interactive visualization options - SPIE Digital Library](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/13569/135690L/Enhancing-manuscript-analysis-with-reflectance-transformation-imaging--a-user/10.1117/12.3062630.full)[mdpi.com

Close-Range Photogrammetry and RTI for 2.5D Documentation of Painted Surfaces: A Tiryns Mural Case Study - MDPI](https://www.mdpi.com/2079-6412/15/4/388)[pmc.ncbi.nlm.nih.gov

Performance of Principal Component Analysis and Independent Component Analysis with Respect to Signal Extraction from Noisy Positron Emission Tomography Data - a Study on Computer Simulated Images - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2703833/)

Mathematical Modeling of Surface Texture

I am examining the mathematical formulations behind surface texture modeling, specifically focusing on how biquadratic polynomial functions capture pixel-level luminance changes under varying light angles. By solving least-squares approximations using singular value decomposition, I am detailing how surface normals and specular enhancements are computed to reveal faint indentations and physical degradation in historical parchment.

Algorithmic Separation of Layered Script

I am synthesizing findings on signal separation techniques used to untangle overlapping ink layers in palimpsests. I am reviewing how statistical methods isolate distinct spectral signatures, allowing undertexts to be clearly distinguished from primary scripts without altering the underlying manuscript material.

Investigating Handwritten Text Recognition Workflows

I am initiating a targeted investigation into modern handwritten text recognition platforms and digital paleography tools. My focus is on determining how automated transcription engines interact with standardized image presentation interfaces to streamline the line-level alignment of diplomatic transcriptions.

[escriptorium.eu

About - eScriptorium](https://escriptorium.eu/about)[help.transkribus.org

1. Uploading - Transkribus Help Center](https://help.transkribus.org/uploading-files-to-transkribus)[transkribus.org

Transkribus for Researchers - The Controllable Pipeline for Historical Documents](https://www.transkribus.org/for-researchers)[transkribus.org

Transkribus for Digital Humanities — AI-Powered Historical Document Analysis](https://www.transkribus.org/digital-humanities)[ub-mannheim.github.io

Training with eScriptorium (a step-by-step guide) - UB Mannheim - GitHub Pages](https://ub-mannheim.github.io/eScriptorium_Dokumentation/Training-with-eScriptorium-EN.html)[iiif.io

Transkribus and IIIF: beneficial possibilities between image sharing and Handwritten Text Recognition frameworks](https://iiif.io/event/2019/goettingen/program/26/)[atrium-research.eu

Workflows - ATRIUM Project](https://atrium-research.eu/workflows/)

Historical Restoration vs Digital Non-Invasive Techniques

I am evaluating the historical trade-offs between destructive chemical restoration methods, such as applying gallic acid or ammonium sulfide, and modern non-invasive optical modalities. While chemical treatments caused permanent darkening and degradation of medieval parchment over time, non-destructive imaging preserves the original physical substrate while digitally recovering hidden text layers.

Methodological Debates and Technical Pitfalls

I am investigating common artifacts and theoretical conflicts in digital manuscript scholarly workflows. Specifically, I am analyzing how statistical separation algorithms like principal component analysis can introduce false readings or palimpsest hallucinations, alongside exploring the architectural friction between canvas-centered spatial data structures and document-centered text encoding models.

Next Targeted Inquiries

I will execute targeted searches on spatial registration algorithms for multi-spectral image stacks, specific plugin extensions for spectral layer blending in web viewers, and formal protocols for linking manuscript annotations across interoperable image and text frameworks.

[archimedespalimpsest.org

Imaging of the Archimedes Palimpsest](https://www.archimedespalimpsest.org/about/imaging/)[scholarsarchive.byu.edu

Multispectral Analysis of a Vatican Library Palimpsest - BYU ScholarsArchive](https://scholarsarchive.byu.edu/cgi/viewcontent.cgi?article=3822&context=jur)[repository.rit.edu

"Multispectral imaging and analysis of the Archimedes Palimpsest" by D. Michael Hansen](https://repository.rit.edu/theses/7957/)[semanticscholar.org

Multispectral imaging of the Archimedes palimpsest - Semantic Scholar](https://www.semanticscholar.org/paper/Multispectral-imaging-of-the-Archimedes-palimpsest-Easton-Knox/fb9460a2110734406508a14de0678c96399487ea)[rdr.ucl.ac.uk

Real and simulated multispectral imaging of a palimpsest - UCL Research Data Repository](https://rdr.ucl.ac.uk/articles/dataset/Real_and_simulated_multispectral_imaging_of_a_palimpsest/28920179)[specialcollections.princeton.edu

Multispectral Imaging of an Aramaic and Greek Palimpsest - Special Collections](https://specialcollections.princeton.edu/2023/07/multispectral-imaging-of-an-aramaic-and-greek-palimpsest/)[repositum.tuwien.at

Restoration of Multispectral Images of Ancient Documents - reposiTUm](https://repositum.tuwien.at/bitstream/20.500.12708/19463/1/Hollaus%20Fabian%20-%202021%20-%20Restoration%20of%20multispectral%20images%20of%20ancient%20documents.pdf)[projects.history.qmul.ac.uk

Multi-Spectral Imaging – Hidden in Plain Sight - QMUL History Projects](https://projects.history.qmul.ac.uk/inplainsight/multi-spectral-imaging/)[researchgate.net

Multispectral imaging for analyzing ancient manuscripts - ResearchGate](https://www.researchgate.net/publication/228983565_Multispectral_imaging_for_analyzing_ancient_manuscripts)[doc.esri.com

Apply transparency and blending modes | ArcGIS Pro documentation - Esri](https://doc.esri.com/en/arcgis-pro/latest/help/mapping/layer-properties/apply-visual-effects.html)

Spectral Unmixing and Artifact Reduction

I am evaluating how statistical decorrelation techniques, such as Principal Component Analysis and Independent Component Analysis, isolate erased undertext while filtering out phantom artifacts caused by ink bleed-through or image misalignments. By analyzing pixel vector distributions across narrow-band spectral datasets, I am observing how orthogonal transformations isolate faint iron-gall signatures onto distinct components, separating the erased historical script from surface degradation and later overwriting.

Supervised Feature Classification for Manuscript Recovery

I am examining supervised classification approaches, such as Linear Discriminant Analysis and Gaussian Mixture Models, that outperform unassisted dimensional reduction during text extraction. Combining spectral response vectors with local spatial context reduces boundary misclassifications along character edges, allowing targeted binarization algorithms to produce clean visual masks suitable for downstream automated transcription pipelines.

Targeted Architectural Queries

I am preparing a final series of precise queries to verify multi-channel visual layer selection constructs within presentation manifests, review text search result highlighting schemas, and confirm the specific X-ray fluorescence iron emission lines used during synchrotron scanning of severe manuscript damage.

[iiif.io

Presentation API 3.0 — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/3.0/)[iiif.io

API Specifications - International Image Interoperability Framework™ — IIIF](https://iiif.io/api/)[github.com

vanda/iiif-features: Code and demos around the use of IIIF - GitHub](https://github.com/vanda/iiif-features)[iiif.io

IIIF Content State API 0.3 - International Image Interoperability Framework](https://iiif.io/api/content-state/0.3/)[iiif.io

IIIF Announces Final Release of 3.0 Specifications](https://iiif.io/news/2020/06/04/IIIF-C-Announces-Final-Release-of-3.0-Specifications/)[iiif.io

Presentation API 3.0 Change Log — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/3.0/change-log/)[iiif.io

Providing Alternative Representations — IIIF | International Image Interoperability Framework](https://iiif.io/api/cookbook/recipe/0046-rendering/)[arxiv.org

[2312.11116] Implementation of the IIIF Presentation API 3.0 based on Software Support: Use Case of an Incremental IIIF Deployment within a Citizen Science Project - arXiv](https://arxiv.org/abs/2312.11116)[stackoverflow.com

How to implement search with hit highlight in Universal Viewer - Stack Overflow](https://stackoverflow.com/questions/62888923/how-to-implement-search-with-hit-highlight-in-universal-viewer)[iiif.io

Content Search API 2.0 Change Log — IIIF | International Image Interoperability Framework](https://iiif.io/api/search/2.0/change-log/)[github.com

Support for IIIF Content Search API · Issue #187 · tify-iiif-viewer/tify - GitHub](https://github.com/tify-iiif-viewer/tify/issues/187)

Protocol Standards and Data Models

I am reviewing the latest interoperability specifications and annotation data models to understand how digital repositories handle multi-layered spectral media and full-text search. My focus is on evaluating how choice constructs and annotation frameworks allow dynamic toggling between multispectral bands and highlighted text search hits within standardized viewers.

Limitations in Statistical Layer Separation

I am identifying critical challenges in automated spectral unmixing and text extraction on historical manuscripts. Specifically, I am examining cases where statistical algorithms struggle with highly correlated ink signatures or low signal-to-noise ratios, leading to potential misinterpretations, and how scholars resolve these ambiguities alongside physical evidence.

Expanding Primary Research Sources

I am formulating targeted inquiries into primary engineering literature and primary research papers. I will search for signal processing studies on palimpsest restoration, historical document conservation debates over chemical versus digital interventions, and schema validation standards for aligning transcriptions with web-based spatial coordinates.

[scispace.com

Multispectral imaging of the Archimedes palimpsest (2003) | Roger L. Easton | 114 Citations](https://scispace.com/papers/multispectral-imaging-of-the-archimedes-palimpsest-4okkk6vs40)[image.ntua.gr

hyperspectral imaging: potential in non-destructive analysis of palimpsests](http://image.ntua.gr/iva/files/Hyperspectral%20imaging%20-%20Potential%20in%20non-destructive%20analysis%20of%20palimpsests%20-%20K.%20Rapantzikos2005.pdf)[specialcollections.princeton.edu

Multispectral Imaging of an Aramaic and Greek Palimpsest - Special Collections](https://specialcollections.princeton.edu/2023/07/multispectral-imaging-of-an-aramaic-and-greek-palimpsest/)[scilit.com

Multispectral imaging of the archimedes palimpsest - Scilit](https://www.scilit.com/publications/bb47f8e0db09bf995945c78ef9873801)[researchgate.net

Palimpsest Research Based on Hyperspectral Information | Request PDF - ResearchGate](https://www.researchgate.net/publication/370616291_Palimpsest_Research_Based_on_Hyperspectral_Information)[rdr.ucl.ac.uk

Real and simulated multispectral imaging of a palimpsest - UCL Research Data Repository](https://rdr.ucl.ac.uk/articles/dataset/Real_and_simulated_multispectral_imaging_of_a_palimpsest/28920179)[semanticscholar.org

Multispectral imaging of the Archimedes palimpsest - Semantic Scholar](https://www.semanticscholar.org/paper/Multispectral-imaging-of-the-Archimedes-palimpsest-Easton-Knox/fb9460a2110734406508a14de0678c96399487ea)[researchgate.net

Digital Transcription of the Archimedes Palimpsest [Applications Corner] - ResearchGate](https://www.researchgate.net/publication/3322061_Digital_Transcription_of_the_Archimedes_Palimpsest_Applications_Corner)[researchgate.net

Multispectral imaging of the Archimedes palimpsest | Request PDF - ResearchGate](https://www.researchgate.net/publication/4067608_Multispectral_imaging_of_the_Archimedes_palimpsest)[iiif-ml-workshop.netlify.app

More about annotations - IIIF for Machine Learning](https://iiif-ml-workshop.netlify.app/docs/annotations-and-iiif/more-about-annotations)

Generative Neural Modeling for Complex Palimpsests

I am reviewing deep generative network architectures designed to decouple severely overlapping text layers where traditional linear decorrelation methods fail. By modeling the physical creation process of palimpsests—coupling a dedicated generative network for undertext reconstruction with a foreground mixing network and background compensation—deep learning models can isolate erased scripts without introducing human-biased visual artifacts.

Multi-Spectral Signal Processing and Registration

I am examining registration and signal processing techniques applied across multi-spectral image stacks spanning ultraviolet to near-infrared wavelengths. Combining log-Gabor spatial filter banks with Markov Random Field models allows spatial stroke dependencies and spectral absorption characteristics to be optimized jointly, drastically improving contrast-to-noise ratios and character segmentation accuracy in heavily degraded manuscripts.

Targeted Technical Inquiries

I am executing targeted searches to gather specific implementation details regarding multi-spectral layer switching patterns in presentation manifests, line-level transcription alignment schemas in automated paleography software, specific synchrotron X-ray fluorescence excitation parameters, and specular enhancement formulations for surface normal modeling.

[iiif.io

Presentation API 3.0 — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/3.0/)[iiif.io

Composition from Multiple Images — IIIF | International Image Interoperability Framework](https://iiif.io/api/cookbook/recipe/0036-composition-from-multiple-images/)[iiif.io

Full recipe list — IIIF | International Image Interoperability Framework](https://iiif.io/api/cookbook/recipe/all/)[iiif.io

Presentation API 3.0 Change Log — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/3.0/change-log/)[iiif.io

API Specifications - International Image Interoperability Framework™ — IIIF](https://iiif.io/api/)[iiif.io

IIIF Content State API 0.3 - International Image Interoperability Framework](https://iiif.io/api/content-state/0.3/)[github.com

IIIF-Commons/presentation-3-types - GitHub](https://github.com/IIIF-Commons/presentation-3-types)[researchgate.net

You Actually Look Twice At it (YALTAi): using an object detection approach instead of region segmentation within the Kraken engine - ResearchGate](https://www.researchgate.net/publication/376848716_You_Actually_Look_Twice_At_it_YALTAi_using_an_object_detection_approach_instead_of_region_segmentation_within_the_Kraken_engine)

Configuring Multi-Spectral Layer Interactions

I am examining how image presentation specifications handle multi-layered media, differentiating between composite renderings and user-driven choice structures. By analyzing layer ordering and canvas painting motivations, I am evaluating how viewers switch between multispectral wavebands or stack overlapping spatial layers, ensuring scholars can alternate between raw spectral captures and processed enhancement overlays.

Resolving Synchronization Friction in Scholarly Workflows

I am addressing the architectural tension between canvas-based spatial representations and document-centric textual schemas. Discrepancies often emerge when aligning machine-generated line segmentations with encoded edition files, requiring robust alignment layers that map bounding coordinates across OCR engine outputs, facsimile surface zones, and web annotation targets without creating competing sources of truth.

Investigating Theoretical Debates and Primary Technical Literature

I am initiating a focused inquiry into the limitations of statistical image separation algorithms, specifically exploring how principal and independent component analysis can generate false visual readings or statistical artifacts in palimpsest analysis. Additionally, I am seeking primary technical source papers covering polynomial texture mapping equations, automated text recognition export pipelines, and interactive layer blending tools for digital paleography.

[mattmcgrattan.github.io

IIIF Presentation API 3.0 (quick introduction) - GitHub Pages](https://mattmcgrattan.github.io/Washington%20Annotation%20Workshop/IIIF%20Presentation%20API%203.0%20(quick%20introduction).html)[iiif.io

Presentation API 3.0 — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/3.0/)[iiif.io

Presentation API 3.0 Change Log — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/3.0/change-log/)[europeana.atlassian.net

IIIF APIs - Europeana Knowledge Base - Confluence](https://europeana.atlassian.net/wiki/spaces/EF/pages/1627914244/IIIF+APIs+Documentation)[iiif.io

Annotate specific images or layers — IIIF](https://iiif.io/api/cookbook/recipe/0326-annotating-image-layer/)[iiif.io

Grouping Annotations into Collections - International Image Interoperability Framework](https://iiif.io/api/cookbook/recipe/0309-annotation-collection/)[iiif.io

Presentation API 2.1.1 — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/2.1/)[digitalcollections.lib.washington.edu

Mirador 3 Viewer - University of Washington Digital Collections](https://digitalcollections.lib.washington.edu/digital/custom/mirador3?manifest=https://digitalcollections.lib.washington.edu//iiif/info/eurasia/5784/manifest.json)

Standardized Presentation Protocols for Multi-Spectral Media

I am examining how presentation data models handle multi-layered spectral media using standardized JSON-LD structures. By organizing images into choices, target canvases allow viewers to seamlessly render overlapping visual layers, such as ultraviolet luminescence, infrared reflectography, and processed false-color composites, within unified digital workspaces.

Architectural Alignment in Automated Paleography

I am analyzing the data flow connecting automated layout analysis engines with encoded diplomatic editions. By converting optical character recognition output formats into structured XML schemas, scholars maintain a clear line of sight between precise manuscript coordinate zones and encoded transcriptions, resolving the tension between spatial image regions and textual hierarchies.

Targeted Engineering and Scientific Verification

I am executing a brief series of targeted inquiries to capture precise mathematical parameters for polynomial surface modeling, verify specific elemental emission channels used during synchrotron scanning, and confirm the JSON-LD context constructs that govern multi-layered image choice selection.

[iiif.io

Multiple Choice of Images in a Single View (Canvas) — IIIF](https://iiif.io/api/cookbook/recipe/0033-choice/)[iiif.io

Presentation API 3.0 — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/3.0/)[iiif.io

The Cookbook of IIIF Recipes - International Image Interoperability Framework](https://iiif.io/get-started/cookbook/)[iiif-prezi.github.io

Composition from Multiple Images - iiif-prezi3 - GitHub Pages](https://iiif-prezi.github.io/iiif-prezi3/recipes/0036-composition-from-multiple-images/)[github.com

awesome-iiif/readme.md at main - GitHub](https://github.com/IIIF/awesome-iiif/blob/main/readme.md)[iiif.io

Code Samples — IIIF | International Image Interoperability Framework](https://iiif.io/api/cookbook/recipe/code/)[iiif.io

Composition from Multiple Images — IIIF | International Image Interoperability Framework](https://iiif.io/api/cookbook/recipe/0036-composition-from-multiple-images/)[github.com

GitHub - Freymat/from_eScriptorium_to_Passim_and_back: Pipeline for ground truth creation to train text recognition models. Extracts OCR results from eScriptorium, prepare them for alignment with passim and import the valid alignments back to eScriptorium.](https://github.com/Freymat/from_eScriptorium_to_Passim_and_back)[tei-c.org

TEI element facsimile - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-facsimile.html)

Configuring Multi-Spectral Layer Interactions

I am reviewing how web presentation frameworks model registered multispectral image stacks using choice constructs. By structuring image resources as ordered options under a single canvas target, viewers can seamlessly switch between distinct wavebands or overlay processed enhancements while maintaining unified spatial coordinates across all spectral layers.

Resolving Synchronization Friction in Scholarly Workflows

I am examining the technical alignment between automated handwritten text recognition platforms and text encoding standards. By mapping layout segmentation formats like PAGE XML and ALTO to facsimile surface zones and web annotation selectors, digital editing pipelines can maintain precise line-level coordinates without creating conflicting sources of truth between transcription schemas and visual canvas representations.

Executing Empirical Research Queries

I am launching a targeted series of searches to gather primary engineering parameters and domain-specific formulations. My focus includes retrieving polynomial texture mapping luminance equations, analyzing statistical limitations and false readings in principal component separation, capturing X-ray fluorescence beamline parameters from historical palimpsest projects, and evaluating interactive layer-blending tools for digital paleography.

[iiif.io

Presentation API 3.0 — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/3.0/)[iiif.io

Composition from Multiple Images — IIIF | International Image Interoperability Framework](https://iiif.io/api/cookbook/recipe/0036-composition-from-multiple-images/)[iiif.io

Full recipe list — IIIF | International Image Interoperability Framework](https://iiif.io/api/cookbook/recipe/all/)[iiif.io

Presentation API 3.0 Change Log — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/3.0/change-log/)[iiif.io

API Specifications - International Image Interoperability Framework™ — IIIF](https://iiif.io/api/)[iiif.io

IIIF Content State API 0.3 - International Image Interoperability Framework](https://iiif.io/api/content-state/0.3/)[github.com

IIIF-Commons/presentation-3-types - GitHub](https://github.com/IIIF-Commons/presentation-3-types)[researchgate.net

You Actually Look Twice At it (YALTAi): using an object detection approach instead of region segmentation within the Kraken engine - ResearchGate](https://www.researchgate.net/publication/376848716_You_Actually_Look_Twice_At_it_YALTAi_using_an_object_detection_approach_instead_of_region_segmentation_within_the_Kraken_engine)

Configuring Multi-Layer Canvas Annotations

I am analyzing how web presentation specifications structure canvas annotations to support interactive layer choice and composite rendering. By examining JSON-LD contexts and painting motivations, I am detailing how client viewers toggle between raw spectral bands, false-color enhancements, and transcriptions while preserving accurate spatial coordinates across different image services.

Addressing Statistical Artifacts in Palimpsest Recovery

I am examining the theoretical and technical limitations of statistical image unmixing, specifically how principal and independent component analyses can introduce false visual readings or spurious ink traces. To mitigate these artifacts, I am evaluating how scholars correlate computational results with physical substrate attributes, elemental spectra, and historical paleographic context to confirm genuine undertext readings.

Formulating Technical and Analytical Synthesis

I am proceeding to execute targeted searches to capture exact mathematical formulations for surface reflectance modeling, verify specific elemental emission channels used during synchrotron scanning, and confirm structural alignment schemas connecting machine-generated layout boundaries with encoded digital editions.

[mattmcgrattan.github.io

IIIF Presentation API 3.0 (quick introduction) - GitHub Pages](https://mattmcgrattan.github.io/Washington%20Annotation%20Workshop/IIIF%20Presentation%20API%203.0%20(quick%20introduction).html)[iiif.io

Presentation API 3.0 — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/3.0/)[iiif.io

Presentation API 3.0 Change Log — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/3.0/change-log/)[europeana.atlassian.net

IIIF APIs - Europeana Knowledge Base - Confluence](https://europeana.atlassian.net/wiki/spaces/EF/pages/1627914244/IIIF+APIs+Documentation)[iiif.io

Annotate specific images or layers — IIIF](https://iiif.io/api/cookbook/recipe/0326-annotating-image-layer/)[iiif.io

Grouping Annotations into Collections - International Image Interoperability Framework](https://iiif.io/api/cookbook/recipe/0309-annotation-collection/)[iiif.io

Presentation API 2.1.1 — IIIF | International Image Interoperability Framework](https://iiif.io/api/presentation/2.1/)

Synthesis of Technical and Methodological Frameworks

I have completed a comprehensive synthesis evaluating how image interoperability standards and multispectral imaging technologies combine to enable deep-zoom access to damaged manuscript witnesses. My analysis bridges spatial image coordinates directly to encoded diplomatic transcriptions, detailing the exact JSON-LD presentation structures, W3C Web Annotation data models, and comparative workspace capabilities that drive modern digital paleography.

Resolution of Algorithmic and Structural Challenges

I have reconciled the architectural tension between canvas-based spatial coordinate systems and document-centric text encoding schemas, establishing robust alignment pipelines between automated layout analysis outputs and facsimile surface zones. Furthermore, I have addressed the critical methodological limitations of statistical signal separation—such as principal and independent component analysis—by incorporating generative neural modeling and targeted false-color composition to prevent statistical visual artifacts.

Transitioning to Report Drafting

Having gathered and verified all necessary technical specifications, mathematical formulations, landmark case studies, and pedagogical frameworks, I am now concluding the research phase and proceeding to write the final comprehensive report.

The initial research has returned a lot of information. I'm sorting through it and organizing it. This will make sure the whole thing flows well and hits all the key points you asked for.

This is it! I’m bringing it all together. Jotting down my final thoughts, polishing everything up, and making sure I give you my very best work.

## References (APA)

1. scholarsarchive.byu.edu. (n.d.). *Multispectral Analysis of a Vatican Library Palimpsest - BYU ScholarsArchive*. https://scholarsarchive.byu.edu/cgi/viewcontent.cgi?article=3822&context=jur
2. image.ntua.gr. (n.d.). *hyperspectral imaging: potential in non-destructive analysis of palimpsests*. http://image.ntua.gr/iva/files/Hyperspectral%20imaging%20-%20Potential%20in%20non-destructive%20analysis%20of%20palimpsests%20-%20K.%20Rapantzikos2005.pdf
3. repositum.tuwien.at. (n.d.). *Restoration of Multispectral Images of Ancient Documents - reposiTUm*. https://repositum.tuwien.at/bitstream/20.500.12708/19463/1/Hollaus%20Fabian%20-%202021%20-%20Restoration%20of%20multispectral%20images%20of%20ancient%20documents.pdf
4. researchgate.net. (n.d.). *Palimpsest Research Based on Hyperspectral Information | Request PDF*. https://www.researchgate.net/publication/370616291_Palimpsest_Research_Based_on_Hyperspectral_Information
5. bibalex.org. (n.d.). *3D Surface Reconstruction Using Polynomial Texture Mapping - Bibliotheca Alexandrina*. https://www.bibalex.org/isis/UploadedFiles/Publications/3D%20Surface%20Reconstruction%20Using%20Polynomial%20Texture%20Mapping.pdf
6. spiedigitallibrary.org. (n.d.). *Enhancing manuscript analysis with reflectance transformation imaging: a user study on interactive visualization options - SPIE Digital Library*. https://www.spiedigitallibrary.org/conference-proceedings-of-spie/13569/135690L/Enhancing-manuscript-analysis-with-reflectance-transformation-imaging--a-user/10.1117/12.3062630.full
7. mdpi.com. (n.d.). *Close-Range Photogrammetry and RTI for 2.5D Documentation of Painted Surfaces: A Tiryns Mural Case Study*. https://www.mdpi.com/2079-6412/15/4/388
8. iiif.io. (n.d.). *IIIF Announces Final Release of 3.0 Specifications*. https://iiif.io/news/2020/06/04/IIIF-C-Announces-Final-Release-of-3.0-Specifications/
9. iiif.io. (n.d.). *API Specifications - International Image Interoperability Framework™*. https://iiif.io/api/
10. iiif.io. (n.d.). *Presentation API 3.0 Change Log — IIIF | International Image Interoperability Framework*. https://iiif.io/api/presentation/3.0/change-log/
11. iiif.io. (n.d.). *Content Search API 2.0 Change Log — IIIF | International Image Interoperability Framework*. https://iiif.io/api/search/2.0/change-log/
12. iiif.io. (n.d.). *Composition from Multiple Images — IIIF | International Image Interoperability Framework*. https://iiif.io/api/cookbook/recipe/0036-composition-from-multiple-images/
13. support.avenza.com. (n.d.). *False-Colour Composite with Multiple Images Tutorial - Avenza Systems*. https://support.avenza.com/hc/en-us/articles/360059420592-False-Colour-Composite-with-Multiple-Images-Tutorial
14. tei-c.org. (n.d.). *Example: - Text Encoding Initiative*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/examples-line.html
15. tei-c.org. (n.d.). *TEI element facsimile - Text Encoding Initiative*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-facsimile.html
16. palimpsest.stmarytx.edu. (n.d.). *Streamlining Text Encoding Initiative (TEI), International Image Interoperability Framework (IIIF), and Mirador: Theoretical and Practical Considerations for Interactive Critical Editions - The Jubilees Palimpsest Project*. https://palimpsest.stmarytx.edu/thanneken/2024/dh/
17. sfu.ca. (n.d.). *TEI element line*. https://www.sfu.ca/~takeda/tei-guidelines/issue_2382_eventName/html/ref-line.html
18. iiif.io. (n.d.). *Represent Canvas Fragment as a Geographic Area in a Web Mapping Client*. https://iiif.io/api/cookbook/recipe/0139-geolocate-canvas-fragment/
19. transkribus.org. (n.d.). *Transkribus for Digital Humanities — AI-Powered Historical Document Analysis*. https://www.transkribus.org/digital-humanities
20. ub-mannheim.github.io. (n.d.). *Training with eScriptorium (a step-by-step guide) - UB Mannheim - GitHub Pages*. https://ub-mannheim.github.io/eScriptorium_Dokumentation/Training-with-eScriptorium-EN.html
21. help.transkribus.org. (n.d.). *1. Uploading - Transkribus Help Center*. https://help.transkribus.org/uploading-files-to-transkribus
22. archimedespalimpsest.org. (n.d.). *Imaging of the Archimedes Palimpsest*. https://www.archimedespalimpsest.org/about/imaging/
23. semanticscholar.org. (n.d.). *Multispectral imaging of the Archimedes palimpsest - Semantic Scholar*. https://www.semanticscholar.org/paper/Multispectral-imaging-of-the-Archimedes-palimpsest-Easton-Knox/fb9460a2110734406508a14de0678c96399487ea
24. researchgate.net. (n.d.). *Digital Transcription of the Archimedes Palimpsest [Applications Corner]*. https://www.researchgate.net/publication/3322061_Digital_Transcription_of_the_Archimedes_Palimpsest_Applications_Corner
25. specialcollections.princeton.edu. (n.d.). *Multispectral Imaging of an Aramaic and Greek Palimpsest - Special Collections*. https://specialcollections.princeton.edu/2023/07/multispectral-imaging-of-an-aramaic-and-greek-palimpsest/
26. iiif.io. (n.d.). *Linking external Annotations targeting a Canvas to a Manifest*. https://iiif.io/api/cookbook/recipe/0306-linking-annotations-to-manifests/
27. rdr.ucl.ac.uk. (n.d.). *Real and simulated multispectral imaging of a palimpsest - UCL Research Data Repository*. https://rdr.ucl.ac.uk/articles/dataset/Real_and_simulated_multispectral_imaging_of_a_palimpsest/28920179
28. github.com. (n.d.). *vanda/iiif-features: Code and demos around the use of IIIF*. https://github.com/vanda/iiif-features
29. projects.history.qmul.ac.uk. (n.d.). *Multi-Spectral Imaging – Hidden in Plain Sight - QMUL History Projects*. https://projects.history.qmul.ac.uk/inplainsight/multi-spectral-imaging/
30. loc.gov. (n.d.). *Image Services | Microservices | APIs at the Library of Congress*. https://www.loc.gov/apis/micro-services/image-services/

_46 citation marker(s) carried no resolvable source in the DOM and were dropped; see the `*_citations.json` sidecar._
