# Topic 13 (Topic_13_Publication): Academic Deep Research Report

**Model:** 3.1 Pro (Deep Research)  
**Attachments:** 10 PDF(s)  
**Citations resolved:** 42

## Digital Scholarly Edition Publication Pipelines, Stemmatology, and Declarative Multi-Modal Transformations

# Beyond the Printed Page: Architectural, Epistemological, and Computational Foundations of Digital Scholarly Publishing

## 1. Abstract and Executive Summary

The transition of the critical edition from the static printed codex to the dynamic digital medium represents a foundational epistemological transformation in textual scholarship. For over two centuries, the scholarly edition was defined and constrained by the physical economics of print: a singular reconstructed reading text supported by a dense, compressed, and selective *apparatus criticus* at the foot of the page. Patrick Sahle's foundational criterion establishes that a true Digital Scholarly Edition (DSE) is guided by a digital paradigm, such that it cannot be converted into a printed book without a catastrophic loss of information, functionality, and critical transparency. Rather than functioning as a digital facsimile of a print volume, the digital edition constitutes an integrated information system and programmable knowledge site.

This comprehensive research report investigates the theoretical, methodological, and computational standards governing the final synthesis, contextualization, and multi-modal dissemination of digital critical editions. The central thesis demonstrates that a professional digital scholarly edition demands a transparently argued introduction defining explicit editorial principles and genealogical stemma codicum, coupled with modular, declarative publication pipelines—specifically the TEI Processing Model, ODD (One Document Does it all), and CSS Paged Media—that preserve philological rigor and semantic integrity across web, interactive, and archival print outputs.

We trace the history and mathematics of the *stemma codicum*, from classical Lachmannian stemmatology (*recensio*, *examinatio*, *emendatio*, and *eliminatio codicum descriptorum*) to graph-theoretic models, phylogenetic trees, and the Coherence-Based Genealogical Method (CBGM) designed for contaminated manuscript traditions. We examine how the TEI Processing Model operationalizes the separation of editorial semantics from presentation logic, superseding monolithic, brittle XSLT stylesheets with declarative `<model>` and `@behaviour` rules defined directly within the ODD schema. Furthermore, we analyze publication workflows that compile TEI XML source files into responsive web interfaces, standalone interactive HTML packages with client-side JavaScript, and high-quality, print-ready PDFs utilizing CSS Paged Media (Paged.js, WeasyPrint) and LaTeX (`reledmac`).

Evaluating celebrated digital editions—including the *Jane Austen Fiction Manuscripts*, the *Carl Maria von Weber Gesamtausgabe* (WeGA), the *Shelley-Godwin Archive*, the *Oxford University Electronic Voltaire*, and the *Digital Semantic Edition of Aldo Moro's Writings*—this report delineates best practices for open-access licensing (Creative Commons, Open Source Software), FAIR data stewardship, and long-term digital preservation. Finally, it provides an actionable pedagogical blueprint for assembling the 10-layer undergraduate Digital Edition Portfolio, bridging classical philological erudition with modern computational publishing engineering.

---

## 2. Technical, Methodological & Historical Foundations

### 2.1 The Epistemology of the Digital Scholarly Edition: Sahle's Criteria and Pierazzo's Theories

Textual editing has always been shaped by the physical affordances and economic constraints of the medium through which it is communicated. In the print paradigm, the editor was forced to make definitive, exclusive choices. Because physical paper cannot display multiple divergent readings simultaneously without overwhelming the page, the traditional print critical edition crystallized into a standard tripartite structure: a discursive introduction establishing historical context and manuscript descriptions, an authoritative reconstructed text (*constitutio textus*), and a compressed, negative critical apparatus relegated to footnotes (Buzzoni, 2016; Driscoll & Pierazzo, 2016).

Patrick Sahle formalized the theoretical demarcation between digitized print editions and authentic digital scholarly editions through his rigorous definition:

> "A digital edition is not merely an edition published digitally, but one that is guided by a digital paradigm in its methodology, architecture, and scholarly execution. A digital scholarly edition cannot be converted into a printed book without a significant, critical loss of information, content, and functionality." (Sahle, 2013, 2016).

Sahle's criterion exposes the conceptual limitation of early electronic publishing, which often amounted to little more than "digital facsimiles" or static PDF replicas of printed books. When an edition is constrained by the print paradigm, it remains trapped in a single, linear presentation of text. Conversely, a true Digital Scholarly Edition (DSE) operates as a dynamic, multi-layered data model. In a DSE, the fundamental scholarly asset is not the visual layout on a screen or page, but the underlying machine-actionable domain model—typically expressed as a richly structured Text Encoding Initiative (TEI) XML document (TEI Consortium, 2026; Pierazzo, 2016).

Furthermore, Sahle distinguishes between four fundamental textual concepts that any digital edition must model: the *text as idea* (the abstract work), the *text as language* (the linguistic sequence of signs), the *text as document* (the material carrier and inscription), and the *text as visual sign* (the physical letterforms and layout) (Sahle, 2013). Print editions routinely collapse these four dimensions into a single normalized linguistic string, discarding the material and visual layers. Digital scholarly editions, by contrast, possess the computational capacity to represent all four dimensions simultaneously through multi-layered markup and linked digital facsimiles (Sahle, 2016; Robinson, 2016).

| Feature Dimension | Traditional Print Scholarly Edition | Digital Scholarly Edition (DSE) |
| --- | --- | --- |
| **Primary Medium** | Ink on physical paper (Codex) | Structured XML data & dynamic interfaces |
| **Representational Model** | Single authoritative text + selective apparatus | Multi-perspective, stratified data graph |
| **Apparatus Structure** | Negative, compressed, location-referenced | Positive, exhaustive, parallel segmentation / stand-off |
| **Image Integration** | Rare, monochrome plates in appendix | Deep-zoom IIIF canvas-to-text alignment |
| **Stemmatic Genealogy** | Static 2D line drawing (tree) | Interactive SVG graph / algorithmic variant matrix |
| **Extensibility & Reuse** | Closed, static, non-queryable | Open data (API, SPARQL, JSON-LD, download) |
| **Searchability** | Static printed indices (names, subjects) | Real-time full-text, morphosyntactic, and faceted search |
| **Collaborative Evolution** | Fixed at point of printing (monolithic) | Continuous integration, version-controlled updates |
| **Sahle's Test** | Native to print; no loss when bound | Collapses and loses core functions if printed |

Elena Pierazzo expands upon this foundation by theorizing the digital edition as an explicit, executable model of a historical text (Pierazzo, 2015, 2016). Drawing on Willard McCarty's modeling theory, Pierazzo argues that digital editing is not a passive reproduction of an artifact, but an active, heuristic process of knowledge representation. The editor constructs a formal model that captures specific phenomena of interest: graphemic letterforms, scribal cancellations, interlinear additions, orthographic variation, morphological syntax, intertextual citations, and genealogical affiliations (Pierazzo, 2016; Cugliana et al., 2024).

Because no single visual layout can simultaneously represent all these interpretive dimensions without visual chaos, the digital paradigm demands a strict separation between **content modeling** and **presentation rendering**. The TEI source serves as the single source of truth, while automated transformation engines generate multiple dynamic views tailored to diverse scholarly audiences: a diplomatic transcription aligned pixel-by-pixel with IIIF digital facsimiles for paleographers; a regularized reading text with modern punctuation for students; and an interactive variant graph with complete stemmatic apparatus for textual critics (Driscoll & Pierazzo, 2016; Fischer, 2020).

---

### 2.2 Stemma Codicum Construction, Stemmatology, and Graph Theory

The genealogical classification of manuscript witnesses constitutes the historic core of textual criticism. When multiple handwritten copies of an ancient or medieval work survive, they inevitably diverge due to scribal errors, deliberate revisions, harmonizations, and omissions. The objective of stemmatology is to reconstruct the history of this transmission, establishing a *stemma codicum* (family tree of manuscripts) that illustrates how surviving witnesses descend from lost intermediaries (*hyparchetypes*) and ultimately from the original text or archetype (Andrews, 2020; Guillaumin, 2020).

#### 2.2.1 Classical Lachmannian Stemmatology

Formulated in the nineteenth century by Karl Lachmann and systematized by Paul Maas (1958), classical stemmatology divides the editorial task into three strictly sequenced operations:

1. ***Recensio* (Survey and Collation):** The comprehensive identification, transcription, and collation of all surviving manuscript witnesses. The editor compares every word and sentence, compiling an exhaustive table of variation units (Andrews, 2020).
2. ***Examinatio* (Critical Examination):** The evaluation of variant readings to distinguish between genuine authorial readings, indifferent variants, and identifiable errors. Lachmannian stemmatology is predicated upon the diagnostic value of **shared errors** (*conjunctive errors* / *errores conjunctivi*). If two manuscripts share an identical, non-trivial error that two independent scribes could not have produced by coincidence, they must share a common ancestor that introduced that error. Conversely, a **separative error** (*error separativus*) proves that manuscript A cannot have been copied from manuscript B if B contains an error from which A is free (Maas, 1958; Fischer, 2020).
3. ***Emendatio* (Correction and Reconstruction):** Using the genealogical tree established during *recensio*, the editor reconstructs the readings of lost archetypes and hyparchetypes. Where the archetype itself was corrupted, the editor applies conjectural emendation (*divinatio*) to restore the authorial reading (Maas, 1958; Lazzerini & Di Franco, 2026).

A crucial operational outcome of stemmatic analysis is ***eliminatio codicum descriptorum*** (the elimination of derived copies). If a manuscript $C$ can be proven through conjunctive and separative errors to be a direct copy of an existing, surviving manuscript $P$ (*codex descriptus*), manuscript $C$ possesses zero independent stemmatic value for reconstructing the archetype and must be excluded from the critical apparatus to eliminate noise (Guillaumin, 2020; Lazzerini & Di Franco, 2026). For example, if Manuscript B contains a massive saut du même au même omission spanning twelve lines that is completely absent in Manuscript A, Manuscript A cannot be a copy of Manuscript B (separative error for B against A). If Manuscript C contains that exact same twelve-line omission plus all of B's unique spelling errors, Manuscript C is identified as a *codex descriptus* copied directly from B and is eliminated from the apparatus (Maas, 1958; Fischer, 2020).

| Stemmatic Relationship | Defining Criterion | Philological Impact | Methodological Action |
| --- | --- | --- | --- |
| **Conjunctive Error** (*error conjunctivus*) | Shared peculiar error improbable by coincidence | Identifies common ancestral hyparchetype | Connects witnesses under a common ancestor node |
| **Separative Error** (*error separativus*) | Error in Witness B not present in Witness A | Proves A is not a descendant of B | Blocks genealogical descent along that vector |
| **Eliminatio Codicum Descriptorum** | Witness is proven to be a direct copy of an extant witness | Removes redundant witness readings | Excluded from the critical apparatus |
| **Hyparchetype** (Greek letter $\alpha, \beta$) | Reconstructed lost common ancestor of a branch | Explains shared branch-level innovations | Posited as an intermediate node in the stemma graph |
| **Archetype** (Greek letter $\Omega$) | Most recent common ancestor of all surviving witnesses | Reconstructs the root of surviving transmission | Target text for editorial reconstruction |
| **Contamination** (Horizontal Transmission) | Scribe copies from or collates multiple exemplars | Creates non-treelike cross-branch networks | Requires DAGs or network graphs instead of trees |

#### 2.2.2 Computational Stemmatology, Phylogenetics, and Directed Acyclic Graphs (DAGs)

While classical Lachmannian stemmatology works well for simple traditions with clean, vertical copying, it struggles when applied to large, complex traditions. Manual stemmatic analysis is vulnerable to cognitive bias: editors often select a handful of favorite variants to draw a tree, ignoring hundreds of conflicting readings (Bordalejo & Vázquez, 2021).

Computational stemmatology treats manuscript collation data as character-state matrices analogous to evolutionary biology. Algorithms adapted from phylogenetics (such as Maximum Parsimony, Neighbor-Joining, and Bayesian inference) process thousands of collated variation units simultaneously, calculating optimal bifurcating tree topologies that minimize the total number of independent mutations required to explain the observed distribution of readings (Andrews, 2020; Shahnazaryan, 2026).

However, historical manuscript transmission frequently violates the strict assumption of bifurcating trees. Scribes did not always copy from a single exemplar; they engaged in **contamination** (horizontal transmission), consulting multiple exemplars in a scriptorium, copying corrections from marginal notes, or memorizing alternative readings. When contamination occurs, the transmission history cannot be modeled as a tree; it forms a **Directed Acyclic Graph (DAG)** or a **reticulate network** with intersecting branches (Andrews, 2020; Guillaumin, 2020).

To address heavily contaminated traditions (such as the Greek New Testament), Gerd Mink developed the **Coherence-Based Genealogical Method (CBGM)** (Mink, 2004; Wachtel, 2015). Rather than forcing manuscripts into a rigid global tree, the CBGM calculates **pre-genealogical coherence**—the statistical percentage of agreement between every pair of witnesses across all variation units. It evaluates local stemmata (the logical direction of variation for individual passages) against global coherence, allowing scholars to trace the fluid "textual flow" across contaminated networks without relying on unproven archetypal assumptions (Fischer, 2020; Lazzerini & Di Franco, 2026).

---

### 2.3 The TEI Processing Model and ODD Architecture

For decades, the standard mechanism for publishing TEI XML documents was the application of custom **XSLT (Extensible Stylesheet Language Transformations)** stylesheets. While XSLT is a Turing-complete, expressive transformation language, relying on ad-hoc XSLT stylesheets introduced severe structural liabilities into digital humanities projects:

1. **Monolithic Brittleness:** A typical XSLT stylesheet intertwines deep XPath queries, document manipulation logic, and hard-coded HTML layout markup. Modifying a visual style or adding an output format frequently breaks complex template matches (Turska et al., 2016; Stadler et al., 2016).
2. **Schema-Presentation Divergence:** As the project's TEI schema evolves, the XSLT stylesheets must be manually updated in parallel. In practice, documentation, schema constraints, and transformation rules drift apart, leading to silent rendering bugs.
3. **Lack of Interoperability:** Because every digital edition project authored its own idiosyncratic XSLT templates for standard TEI elements (such as `<choice>`, `<app>`, or `<persName>`), stylesheets could not be shared or reused across institutions (Turska et al., 2016).

To solve these systemic problems, the TEI Consortium developed the **TEI Processing Model**, formalized in Chapter 22 of the TEI P5 Guidelines (*Documentation Elements: The TEI Processing Model*) (TEI Consortium, 2026; Turska et al., 2016).

#### 2.3.1 ODD ("One Document Does It All") as a Unified Specification

The TEI Processing Model is embedded directly within an **ODD (One Document Does it all)** file. An ODD file is a literate programming document that integrates:
- Human-readable prose documentation explaining the editorial rationale;
- Formal schema declarations (specifying which TEI modules, elements, and attributes are valid);
- Semantic constraint rules expressed in ISO Schematron;
- **Declarative output specifications** mapping TEI elements to standardized rendering behaviors (Turska et al., 2016).

#### 2.3.2 Mechanics of `<model>`, `@behaviour`, and `@predicate`

Within an ODD element specification (`<elementSpec>`), the processing model defines how that element should be rendered using the `<model>` element. A `<model>` instruction does not generate raw HTML or LaTeX syntax; instead, it invokes an abstract, platform-agnostic **behaviour** (Turska et al., 2016; Stadler et al., 2016).

The fundamental attributes of `<model>` include:
- `@behaviour`: The abstract rendering operation to execute. Standard behaviors defined by the TEI Guidelines include `paragraph`, `heading`, `inline`, `block`, `alternate`, `note`, `link`, `graphic`, `table`, `cell`, `row`, `cit`, `index`, and `omit`.
- `@predicate`: An XPath expression that evaluates the document context. If the predicate evaluates to true, the model rule is applied. This allows editors to apply different behaviors to the same element depending on its parent, attributes, or position.
- `@output`: The target publication format (e.g., `web`, `print`, `latex`, `epub`).
- `<param>`: Named parameters passed to the behaviour (such as `content`, `alternate`, `uri`, or `place`).
- `<outputRendition>`: Declarative CSS styling rules attached directly to the output node.

```xml
<elementSpec ident="choice" mode="change">
  <model predicate="$mode = 'diplomatic'" behaviour="inline">
    <param name="content" value="orig | sic | abbr"/>
    <outputRendition>color: #8b0000; font-family: 'Cardo', serif;</outputRendition>
  </model>
  <model predicate="$mode = 'reading'" behaviour="inline">
    <param name="content" value="reg | corr | expan"/>
    <outputRendition>color: #000000;</outputRendition>
  </model>
  <model behaviour="alternate">
    <param name="default" value="reg | corr | expan"/>
    <param name="alternate" value="orig | sic | abbr"/>
  </model>
</elementSpec>
```

In the example above, the `<choice>` element is mapped declaratively. In "diplomatic" mode, the system outputs the historical original forms (`<orig>`, `<sic>`, `<abbr>`) styled in dark red. In "reading" mode, it outputs normalized regularizations (`<reg>`, `<corr>`, `<expan>`). In default interactive web mode, it invokes the abstract `alternate` behaviour, which TEI Publisher automatically converts into an interactive popover or tooltip (Turska et al., 2016).

#### 2.3.3 Advanced Model Orchestration: `<modelSequence>` and `<modelGrp>`

When complex editorial elements require multiple rendering passes or conditional groupings, the Processing Model provides structural grouping containers:
- `<modelSequence>`: Executes a series of `<model>` instructions in strict linear order. For example, rendering a critical apparatus entry may require outputting the lemma inline, followed immediately by an apparatus note anchored at the bottom of the page (Turska et al., 2016).
- `<modelGrp>`: Groups multiple `<model>` rules that share a common condition, output target, or predicate, simplifying schema maintenance.

```xml
<elementSpec ident="app" mode="change">
  <modelSequence>
    <model behaviour="inline">
      <param name="content" value="lem"/>
    </model>
    <model behaviour="note">
      <param name="place" value="'margin'"/>
      <param name="content" value="rdg"/>
    </model>
  </modelSequence>
</elementSpec>
```

#### 2.3.4 TEI Publisher Architecture

**TEI Publisher**, developed by e-editiones, is the flagship open-source reference implementation of the TEI Processing Model (Turska et al., 2016; Stadler et al., 2016). Built upon the Native XML database **eXist-db**, TEI Publisher eliminates the need for developers to write thousands of lines of bespoke XSLT.

The TEI Publisher transformation engine ingests the ODD specification and compiles its declarative `<model>` rules into highly optimized XQuery or XSLT 3.0 transformation libraries. When a user requests a document, the engine dynamically executes the compiled pipeline, injecting the rendered content into lightweight HTML5 Web Components (such as `<pb-view>`, `<pb-facsimile>`, and `<pb-popover>`) (Turska et al., 2016). This architecture guarantees that the same ODD file that validates the transcription simultaneously powers the live web edition and the print PDF pipeline.

---

## 3. Applied Implementation & Multi-Modal Publishing Dimensions

### 3.1 Multi-Modal Publishing Pipelines: Web, Interactive HTML, and Print-Ready PDF

A digital scholarly project should not lock its data into a single output channel. The modern standard for scholarly publishing is **multi-modal dissemination**: delivering content across responsive web applications, self-contained interactive packages, and typographically flawless archival PDFs from the identical TEI XML master source.

#### 3.1.1 Responsive Web Publication

For online scholarly access, TEI XML is transformed into semantic HTML5 structured with modern Web Components. Standard features of modern digital editions include:
- **Synchronized Dual Views:** Presenting high-resolution IIIF facsimiles side-by-side with diplomatic and normalized transcriptions using OpenSeadragon or Mirador viewers (Topic 3).
- **Faceted Search and Entity Filtering:** Interrogating indexed XML nodes using Lucene or XPath in eXist-db, enabling users to filter by prosopographical entities, date ranges, scribal hands, or lemma forms (Barzaghi et al., 2025; Stadler et al., 2016).
- **Interactive Variant Graphs:** Rendering CollateX alignment graphs dynamically in SVG via D3.js, allowing users to trace textual divergence across witnesses visually (Shahnazaryan, 2026).

#### 3.1.2 Standalone Interactive HTML Packages

While server-side architectures like eXist-db offer powerful querying, they require server maintenance, database administration, and ongoing institutional support. If the server goes offline, the edition disappears.

To ensure portable, zero-dependency dissemination, editors compile **standalone interactive HTML packages**. In this workflow, the TEI XML is compiled into a single, self-contained HTML file with embedded JavaScript and CSS. Tools like **Edition Visualization Technology (EVT)** and lightweight static site generators package complete interactive critical apparatuses, collapsible commentary drawers, and client-side search engines (using WebAssembly or Lunr.js) into a file that can be distributed on a USB drive, hosted on GitHub Pages, or viewed offline in any standard web browser (Driscoll & Pierazzo, 2016; Buzzoni, 2016).

#### 3.1.3 Print-Ready PDF Pipelines: Comparative Evaluation

Despite the primacy of the digital paradigm, physical codices and paginated PDFs remain essential for archival durability, classroom adoption, and long-form linear reading. Generating a critical edition PDF from TEI XML requires sophisticated typesetting engines capable of handling running line numbers, multi-column layouts, footnotes, and multi-tiered critical apparatuses (Fischer, 2020; Lazzerini & Di Franco, 2026).

| Typesetting Pipeline | Input Standard | Strengths | Weaknesses & Trade-offs |
| --- | --- | --- | --- |
| **CSS Paged Media**<br>*(Paged.js, WeasyPrint, Vivliostyle)* | HTML5 / CSS3 Paged Media Module (`@page`, `@bottom-center`, `marks`) | Web-standard syntax; shares styling directly with web edition; rapid prototyping. | Limited support for complex multi-tier synchronized apparatus footnotes; footnotes on two-column layouts can be fragile. |
| **XSL-FO**<br>*(Apache FOP, Antenna House)* | Formatting Objects XML (`fo:root`, `fo:block`) | Highly stable, mature enterprise standard; robust page numbering and running headers. | Extremely verbose XML syntax; complex setup; Apache FOP lacks advanced micro-typography. |
| **LaTeX (`reledmac`)**<br>*(TeXLive Engine)* | LaTeX markup (`\begin{numberpstart}`, `\edtext{...}{\Afootnote{...}}`) | Gold standard for classical philology; multi-tiered apparatus (`\Afootnote`, `\Bfootnote`), synchronized parallel columns (`reledpar`), automated line numbering. | Steep learning curve; requires compiling TEI XML to LaTeX markup; fragile macro expansions on non-standard Unicode. |
| **Typst**<br>*(Modern Rust Engine)* | Typst scripting language (`#table()`, `#show`, `#locate()`) | Ultra-fast compilation; clean modern syntax; powerful programmable layouts; robust PDF/A export. | Nascent ecosystem; specialized multi-tiered critical apparatus packages are still in active development. |

For classical philological workflows requiring multi-tiered apparatuses (e.g., Tier A for text-critical variants, Tier B for biblical/classical fontes, and Tier C for linguistic commentary), the LaTeX `reledmac` package remains the most typographically rigorous engine (Fischer, 2020). However, for modern, accessible multi-modal workflows, CSS Paged Media (via Paged.js or WeasyPrint) has emerged as the premier standard because it allows web developers to leverage their existing CSS skills to format printed books directly from the HTML generated by the TEI Processing Model (Turska et al., 2016).

---

### 3.2 Licensing, Open Access, and Intellectual Property

A digital scholarly edition is a complex intellectual assembly comprising historical primary sources, high-resolution digital images, editorial transcriptions, critical annotations, computational schemas, and software code. Ensuring that this asset can be legally accessed, cited, and computationally reused requires a sophisticated, multi-tiered licensing strategy (Barzaghi et al., 2025; Driscoll & Pierazzo, 2016).

#### 3.2.1 Textual Content vs. Raw Data vs. Code Licensing

1. **Editorial Prose and Interpretive Annotations:** The critical introduction, scholarly commentary, translation, and semantic markup represent original scholarly contributions. These components should be licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**, or **CC BY-SA 4.0** (ShareAlike). This ensures that other scholars may freely quote, distribute, and build upon the edition, provided proper attribution is given to the editors (Barzaghi et al., 2025).
2. **Raw Metadata and Collation Data:** Concordances, token frequency lists, CTS URN registries, and RDF linked data triples are factual data. In many legal jurisdictions (including the United States and the European Union), purely factual datasets cannot be copyrighted. Applying a **Creative Commons Zero (CC0 1.0 Universal) Public Domain Dedication** to raw data files and TEI Header metadata eliminates legal ambiguity and maximizes computational reuse across the global semantic web.
3. **Software Code and Processing Scripts:** Python normalization scripts, CollateX pipeline runners, ODD transformation stylesheets, and web frontend code must be protected with standard Open Source Software (OSS) licenses, such as the **MIT License** (permissive) or the **GNU General Public License v3.0 (GPL-3.0)** (copyleft).
4. **Digital Facsimiles:** High-resolution manuscript images are often governed by holding library policies. While digital humanities best practices encourage institutions to release faithful photographic reproductions of public-domain cultural artifacts under CC0 or Public Domain Marks, editors must explicitly document institutional image rights and IIIF terms of use within the `<teiHeader>` `<publicationStmt>` (TEI Consortium, 2026).

```xml
<publicationStmt>
  <publisher>St. Francis Xavier University Digital Humanities Press</publisher>
  <pubPlace>Antigonish, Nova Scotia</pubPlace>
  <date when="2026-12-04">December 4, 2026</date>
  <availability status="restricted">
    <licence target="https://creativecommons.org/licenses/by/4.0/">
      The editorial text, critical apparatus, translation, and commentary are licensed
      under a Creative Commons Attribution 4.0 International License (CC BY 4.0).
    </licence>
    <licence target="https://creativecommons.org/publicdomain/zero/1.0/">
      All underlying structured metadata, token lists, and RDF assertions are
      dedicated to the public domain under CC0 1.0 Universal.
    </licence>
  </availability>
</publicationStmt>
```

---

### 3.3 Archival Sustainability, Digital Preservation, and FAIR Data Principles

One of the most pressing crises facing digital humanities is "digital rot" or obsolescence. Dozens of pioneering digital editions created in the 1990s and 2000s are now completely inaccessible because they relied on proprietary software, unmaintained database servers, deprecated browser plugins (such as Adobe Flash or Java applets), or broken server-side scripts (Sahle, 2016; Driscoll & Pierazzo, 2016).

To ensure that a digital scholarly edition survives for decades, project architects must decouple **data preservation** from **software preservation**, adhering to the internationally recognized **FAIR Data Principles** (Wilkinson et al., 2016):

- **Findable:** The edition must be assigned a persistent identifier, such as a **Digital Object Identifier (DOI)** minted through Zenodo or Crossref. Metadata must be indexed in public registries and structured using standard schemas (schema.org, Dublin Core, TEI Header).
- **Accessible:** The primary data (TEI XML source files, schemas, and media assets) must be retrievable via open, standardized protocols (HTTPS, Git) without paywalls or proprietary client software.
- **Interoperable:** Data must utilize open, machine-readable formats. TEI XML, W3C Web Annotation JSON-LD, RDF Turtle, and IIIF Presentation manifests ensure semantic interoperability across international repositories.
- **Reusable:** Data must be released with clear, machine-readable licenses (CC BY, CC0) and detailed provenance documentation detailing exactly how the transcriptions, collations, and corrections were produced.

#### 3.3.1 Best Practices for Archival Ingestion

To achieve permanent preservation, the final digital edition repository should follow a three-tiered archiving protocol:
1. **Version-Controlled Source Code (GitHub / GitLab):** Maintain the active codebase, commit history, and issue tracking in a public Git repository, providing an immutable audit trail of editorial decisions (Topic 1).
2. **Permanent Trusted Repository (Zenodo / Dataverse):** On project completion or major release, archive a frozen snapshot of the repository in a certified long-term data repository (e.g., Zenodo, backed by CERN). Zenodo automatically issues a citable DOI and guarantees bit-level preservation for decades.
3. **Static Self-Contained Deliverables:** Generate static HTML and PDF archives that do not rely on dynamic databases. Storing static files alongside the raw TEI XML ensures that future readers can access the scholarship even if the underlying database software becomes obsolete.

---

## 4. Real-World Digital Edition Case Studies

The practical viability of digital publication pipelines is demonstrated through their successful implementation in major digital editing initiatives. The following case studies showcase diverse strategies for managing genetic variation, musicological data, multi-hand manuscripts, and semantic Linked Open Data.

### 4.1 The Jane Austen Fiction Manuscripts Digital Edition

The *Jane Austen Fiction Manuscripts Digital Edition*, directed by Kathryn Sutherland and technical director Elena Pierazzo, is a landmark achievement in genetic editing and TEI encoding (Pierazzo, 2015, 2016). The project reunited approximately 4,500 pages of Austen's surviving unpublished fiction manuscripts, held across multiple international libraries, into a single virtual workspace.

Austen's working manuscripts are heavily revised, featuring intricate layers of interlinear insertions, marginal additions, deletions, paste-overs (patches of paper pinned over discarded text), and idiosyncratic punctuation. A traditional print edition could not represent this physical and genetic complexity without forcing an artificial editorial choice between an unreadable diplomatic rendering and a smoothed, modernized text (Pierazzo, 2016).

Pierazzo and Sutherland solved this by authoring a single, deeply encoded TEI P5 source file utilizing the Primary Sources module (`<subst>`, `<add>`, `<del>`, `<handShift>`). Through automated XSLT pipelines, the web application generates two synchronized, interactive views alongside the facsimile:
1. A **diplomatic view** that maps every strike-through, superscript correction, and physical layout feature exactly as inscribed on the paper;
2. A **linear reading view** that resolves all cancellations and incorporates Austen's final authorial corrections, providing a clean, accessible reading text.

By proving that a single TEI XML model could satisfy both the rigorous paleographer and the literary reader, the Jane Austen project established the foundational methodology for modern genetic digital editing (Pierazzo, 2015, 2016).

---

### 4.2 The Carl Maria von Weber Gesamtausgabe (WeGA)

The *Carl Maria von Weber Gesamtausgabe* (WeGA), based at the Detmold/Paderborn Digital Humanities center and directed by Peter Stadler and Joachim Veit, is the international pioneer of the TEI Processing Model and TEI Publisher (Stadler et al., 2016; Turska et al., 2016).

WeGA is a massive, multi-disciplinary edition encompassing Weber's musical works, letters, diaries, writings, and historical documents. Managing this heterogeneous corpus presented immense technical challenges: musicological critical apparatuses had to be integrated with textual critical editions, complex biographical registries, and music encodings (Music Encoding Initiative, MEI).

Frustrated by the unmaintainability of tens of thousands of lines of bespoke XSLT, the WeGA team co-developed the TEI Processing Model. They authored a comprehensive ODD specification that formalizes how every TEI and MEI element behaves across publication media. Using eXist-db and the compiled Processing Model pipeline, WeGA dynamically serves:
- A responsive, faceted public web portal with instant cross-linking between persons, places, musical compositions, and diary entries;
- Automated print-ready PDF volumes for traditional musicological publication;
- Open API endpoints delivering raw TEI XML and RDF linked data to external research libraries.

WeGA stands as the definitive real-world proof of concept that the TEI Processing Model dramatically reduces software maintenance costs while accelerating multi-modal scholarly publication (Stadler et al., 2016).

---

### 4.3 The Shelley-Godwin Archive

The *Shelley-Godwin Archive* (S-GA), developed by the Maryland Institute for Technology in the Humanities (MITH) in partnership with the Bodleian Library, the New York Public Library, and the Huntington Library, provides digital critical editions of the manuscripts of Mary Wollstonecraft Shelley, Percy Bysshe Shelley, William Godwin, and Mary Wollstonecraft (Fraistat et al., 2013).

The centerpiece of the archive is the manuscript of Mary Shelley's *Frankenstein* (1818). The draft notebook contains a deeply collaborative textual dialogue: Mary Shelley composed the primary narrative, while Percy Bysshe Shelley made extensive marginal and interlinear interventions, modifying vocabulary, adjusting tone, and rewriting sentences.

The S-GA team utilized TEI P5's genetic edition module (`<sourceDoc>`, `<surface>`, `<zone>`, `<line>`) to encode the exact spatial and temporal coordinates of every stroke on the manuscript page. The publication interface provides an interactive hand-attribution toggle: users can highlight Percy Shelley's edits in orange and Mary Shelley's text in blue, or use an interactive slider to watch the manuscript evolve from its earliest rough draft to the final fair copy (Fraistat et al., 2013). The S-GA architecture demonstrates how digital publication can make visible the collaborative, social nature of literary composition.

---

### 4.4 The Semantic Digital Edition of Aldo Moro's Writings

The *Edizione Nazionale delle Opere di Aldo Moro*, published in 2025, represents state-of-the-art integration of traditional philology with Semantic Web and Linked Open Data technologies (Barzaghi et al., 2025). Aldo Moro was one of twentieth-century Italy's foremost political leaders, and his vast corpus of speeches, letters, and governmental writings spans decades of turbulent history.

The project team developed a multi-layered publication workflow:
1. **Philological Ground Truth:** All historical writings were transcribed and collated in TEI XML, complete with comprehensive historical introductions and critical apparatuses.
2. **Semantic Knowledge Graph:** Named entities (politicians, political parties, historical events, legislative bills) were extracted and mapped to an OWL/RDF ontology, linking occurrences to DBpedia, Wikidata, and Italian parliamentary authority records (Barzaghi et al., 2025).
3. **Multi-Format Dissemination:** The platform provides dual publication: users can explore the rich semantic web interface with network graph visualizations of political relationships, or download archival TEI XML files and high-quality, print-ready PDF volumes typeset automatically from the TEI source.

This edition exemplifies the contemporary convergence of philological rigor, machine-actionable linked data, and multi-modal distribution (Barzaghi et al., 2025).

---

## 5. Pedagogical Takeaways & Synthesis for Digital Editors

### 5.1 The 10-Layer Digital Critical Edition Architecture

For students and emerging scholars in digital humanities, constructing a digital scholarly edition is an integrative, cumulative discipline. Across the thirteen modules of this curriculum, each student constructs a complete, TEI-conformant digital critical edition of an ancient or medieval manuscript passage.

The completed **Digital Edition Portfolio** brings together ten distinct methodological layers into a unified, publication-ready package:

| Layer Number | Curriculum Module | Core Methodological Artifact | Primary Standards & Tools |
| --- | --- | --- | --- |
| **Layer 01** | Topic 2 (Cataloguing & Metadata) | `<teiHeader>`, `<msDesc>`, CTS URNs | TEI P5, RDF Triples, Oxygen XML |
| **Layer 02** | Topic 3 (IIIF Imaging) | IIIF Presentation Manifest, Canvas IDs | IIIF API 3.0, Mirador, OpenSeadragon |
| **Layer 03** | Topics 4–5 (Transcription & Reconciliation) | Character-accurate diplomatic transcription | Plain text, Transkribus HTR, CER scoring |
| **Layer 04** | Topic 6 (Orthographic Normalization) | Orthographic decision log, regularized text | TEI `<choice>`, `<orig>`, `<reg>`, Python |
| **Layer 05** | Topic 7 (Collation & Alignment) | Multi-witness alignment matrix | CollateX, Gotoh Algorithm, Variant Graph |
| **Layer 06** | Topic 8 (Critical Apparatus) | TEI Parallel Segmentation Apparatus | TEI `<app>`, `<lem>`, `<rdg>`, `<listWit>` |
| **Layer 07** | Topic 9 (Lemmatization & POS) | Morphosyntactic tokens & part-of-speech | CLTK, TreeTagger, TEI `<w lemma="" pos="">` |
| **Layer 08** | Topic 11 (Interlinear Translation) | 4-line interlinear glossed translation | Leipzig Glossing Rules, TEI `<linkGrp>` |
| **Layer 09** | Topic 12 (Scholarly Commentary) | Categorized stand-off commentary notes | TEI `<standOff>`, `<interpGrp>`, W3C WADM |
| **Layer 10** | Topic 13 (Studio & Publication) | Final Introduction, Stemma, Multi-Modal Output | ODD Processing Model, CSS Paged Media, PDF |

---

### 5.2 Formulating the Editorial Introduction (`<editorialDecl>`)

The **Editorial Introduction** is the intellectual anchor of the entire digital edition. It is the forum where the editor explains their scholarly rationale, justifies emendations, details manuscript witnesses, and articulates explicit encoding policies (Driscoll & Pierazzo, 2016; Fischer, 2020).

Within the TEI Header, these policies are formally recorded inside the `<encodingDesc>` element, structured under dedicated sub-elements:

```xml
<teiHeader>
  <fileDesc>
    <titleStmt>
      <title>A Digital Critical Edition of 1 Thessalonians 2:1–12</title>
      <author>Paul the Apostle</author>
      <editor>Student Philologist</editor>
    </titleStmt>
    <publicationStmt>
      <publisher>St. Francis Xavier University Digital Humanities Press</publisher>
      <date>2026-12-04</date>
      <availability status="restricted">
        <licence target="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</licence>
      </availability>
    </publicationStmt>
    <sourceDesc>
      <listWit>
        <witness xml:id="wit-aleph"><msDesc><msIdentifier><settlement>London</settlement><repository>British Library</repository><idno>Add. 43725</idno><msName>Codex Sinaiticus</msName></msIdentifier></msDesc></witness>
        <witness xml:id="wit-B"><msDesc><msIdentifier><settlement>Vatican City</settlement><repository>Biblioteca Apostolica Vaticana</repository><idno>Vat.gr.1209</idno><msName>Codex Vaticanus</msName></msIdentifier></msDesc></witness>
      </listWit>
    </sourceDesc>
  </fileDesc>
  <encodingDesc>
    <editorialDecl>
      <correction status="high" method="silent">
        <p>Obvious scribal slips (such as dittographies) have been corrected and flagged in the critical apparatus via &lt;choice&gt;/&lt;corr&gt;.</p>
      </correction>
      <normalization method="markup">
        <p>Iotacisms and vowel substitutions (such as ει for ι) are regularized in reading mode via &lt;orig&gt; and &lt;reg&gt; while preserving paleographical forms in diplomatic mode.</p>
      </normalization>
      <segmentation>
        <p>Text is tokenized at the word level, with punctuation marks isolated as independent tokens. Sentences are delimited via &lt;s&gt; and numbered sequentially.</p>
      </segmentation>
      <interpretation>
        <p>Commentary notes are classified into four distinct categories: philological, historical, intertextual, and structural, encoded in &lt;standOff&gt; with CTS URN targets.</p>
      </interpretation>
    </editorialDecl>
    <variantEncoding method="parallel-segmentation" location="internal"/>
  </encodingDesc>
</teiHeader>
```

#### 5.2.1 Core Sections of the Narrative Editorial Introduction

Alongside the structured TEI Header, the editor authors an introductory essay containing six mandatory scholarly sections:

1. **Codicological Overview and Witness Descriptions:** Detailed material descriptions of all collated manuscripts (date, script, provenance, physical condition, foliation, and digital IIIF manifest URIs).
2. **Stemmatic Analysis and Genealogical Stemma:** The formal argument for the relationship among witnesses, citing shared conjunctive errors, establishing hyparchetypes, and presenting the graphical stemma codicum alongside the justification for any *eliminatio codicum descriptorum* (Andrews, 2020; Guillaumin, 2020).
3. **Principles of Textual Constitution:** The explicit criteria governing editorial choice (e.g., preference for *lectio difficilior potior*, *lectio brevior*, genealogical weighting via CBGM, or adherence to a specific base text) (Maas, 1958; Fischer, 2020).
4. **Orthographic and Normalization Policy:** Clear guidelines regarding how spelling fluctuations, word division, accentuation, and breathings are handled between diplomatic and reading views.
5. **Apparatus and Commentary Conventions:** Definitions of all witness sigla, Latin abbreviations (*om.*, *add.*, *transp.*, *in marg.*, *a.c.*, *p.c.*), and commentary categorization schemes.
6. **Licensing and Reusability Statement:** Explicit declarations of Creative Commons terms for text and commentary, Open Source licenses for software scripts, and archival repository DOI citations.

---

### 5.3 Final Assembly and Quality Assurance Checklist

Prior to compiling the final multi-modal release packages, digital editors must execute a rigorous quality assurance protocol. The following checklist ensures structural validity, philological integrity, and technical reusability:

| Verification Domain | Quality Assurance Check | Verification Tool / Command | Pass Criteria |
| --- | --- | --- | --- |
| **Schema Validation** | Full TEI P5 Relax NG validation | Oxygen XML / `xmllint --relaxng` | Zero schema violations across all files |
| **Schematron Constraints** | Internal ID/IDREF consistency | `schxslt` / Schematron Validator | All `@wit`, `@target`, and `@corresp` resolve to valid `xml:id` |
| **IIIF Image Binding** | Canvas and manifest URL check | Python `requests` / Mirador | All `@facs` URIs return HTTP 200 and render deep-zoom tiles |
| **Stemmatic Coherence** | Stemma codicum node verification | Graphviz `dot` / Mermaid | Every node corresponds to a declared witness siglum in `<listWit>` |
| **Apparatus Integrity** | Variation unit syntax | `lint_lesson_content.py` / Python | Every `<app>` contains exactly one `<lem>` and valid `<rdg>` elements |
| **Linguistic Layers** | Lemmatization and Leipzig glossing | CLTK validator / Python script | 100% of tokens lemmatized; morpheme boundaries match glosses |
| **Stand-off Anchors** | Commentary target verification | CTS URN resolver / XPath | All `<note>` elements anchor to existing CTS passage coordinates |
| **Processing Model** | ODD behaviour mapping | TEI Publisher / Saxon-HE | All TEI elements map to valid `@behaviour` rules without fallbacks |
| **Multi-Modal Export** | Dual Web, HTML, and PDF build | Webpack / Paged.js / `reledmac` | Visual layouts compile cleanly with 0 formatting errors |
| **Open Access & FAIR** | Metadata and licensing metadata | Zenodo / GitHub Release tag | CC BY 4.0 / CC0 declared; repository tagged with frozen version |

---

## 6. Comprehensive Academic & Technical References

1. Andrews, T. (2020). 3.3 Transcription and collation. In P. Roelli (Ed.), *Handbook of Stemmatology: History, Methodology, Digital Approaches* (pp. 167–180). De Gruyter. https://doi.org/10.1515/9783110684384-003
2. Apollon, D., Bélisle, C., & Régnier, P. (Eds.). (2014). *Digital critical editions*. University of Illinois Press. https://doi.org/10.5406/illinois/9780252038402.001.0001
3. Barker, D., Cronk, N., & Roe, G. (2026). *Digital scholarly editing in practice: Making Oxford University Voltaire*. Cambridge University Press. https://doi.org/10.1017/9781009384582
4. Bartalesi, V., Meghini, C., & Metilli, D. (2018). A web application for exploring primary sources: The DanteSources case study. *Digital Scholarship in the Humanities, 33*(4), 705–719. https://doi.org/10.1093/llc/fqx050
5. Barzaghi, S., Palmero Aprosio, A., Paolucci, F., & Peroni, S. (2025). The semantic digital edition of Aldo Moro's writings: A workflow supporting data sharing and replicability. *ACM Journal on Computing and Cultural Heritage, 18*(2), Article 24. https://doi.org/10.1145/3725534
6. Berti, M. (2026). Annotating the ancient world: Critical annotations and digital editions. In *Charting the Future of Historical Humanities* (pp. 45–68). Brepols. https://doi.org/10.1484/M.LECTIO-EB.5.151800
7. Blackwell, C. W., & Smith, N. (2014). *The Canonical Text Services URN specification, version 2.0.rc.1*. Center for Hellenic Studies, Harvard University. https://cite-architecture.github.io/ctsurn_spec/
8. Bollmann, M. (2019). A large-scale comparison of historical text normalization systems. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies* (pp. 3885–3898). Association for Computational Linguistics. https://doi.org/10.18653/v1/N19-1389
9. Bordalejo, B., & Vázquez, A. (2021). You're collating just fine and other lies you've been telling yourself. *Digital Medievalist, 14*(1), 1–28. https://doi.org/10.16995/dm.8066
10. Buzzoni, M. (2016). A protocol for scholarly digital editions? The Italian point of view. In M. J. Driscoll & E. Pierazzo (Eds.), *Digital Scholarly Editing: Theories and Practices* (pp. 89–108). Open Book Publishers. https://doi.org/10.11647/OBP.0095.05
11. Camps, J.-B., Spadini, E., & Ing, L. (2019). Collating medieval vernacular texts: Aligning witnesses, classifying variants. In *Digital Humanities 2019: Conference Abstracts* (pp. 1–6). Utrecht University. https://hal.science/hal-02268348
12. Coffee, N., Koenig, J.-P., Poornima, S., Forstall, C. W., Ossewaarde, R., & Jacobson, S. L. (2012). The Tesserae Project: Intertextual analysis of Latin poetry. *Literary and Linguistic Computing, 28*(2), 221–228. https://doi.org/10.1093/llc/fqs033
13. Cugliana, E., Ward, A., van Zundert, J., & Andrews, T. (2024). Computational approaches and the epistemology of scholarly editing. *International Journal of Digital Humanities, 6*, 115–138. https://doi.org/10.1007/s42803-024-00082-7
14. Driscoll, M. J., & Pierazzo, E. (Eds.). (2016). *Digital scholarly editing: Theories and practices*. Open Book Publishers. https://doi.org/10.11647/OBP.0095
15. Fischer, F. (2020). 6.3 Representing the critical text. In P. Roelli (Ed.), *Handbook of Stemmatology: History, Methodology, Digital Approaches* (pp. 405–424). De Gruyter. https://doi.org/10.1515/9783110684384-006
16. Fraistat, N., Denlinger, E., & Stauffer, A. (2013). *The Shelley-Godwin Archive*. Maryland Institute for Technology in the Humanities. https://shelleygodwinarchive.org/
17. Francese, C. (2014). *About DCC: Overview and pedagogical principles*. Dickinson College Commentaries. https://dcc.dickinson.edu/about-dcc
18. Guillaumin, J.-B. (2020). 5.5 Criticisms of digital methods. In P. Roelli (Ed.), *Handbook of Stemmatology: History, Methodology, Digital Approaches* (pp. 341–352). De Gruyter. https://doi.org/10.1515/9783110684384-005
19. Haaf, S., Wiegand, F., & Geyken, A. (2013). Measuring the correctness of double-keying: An error analysis. *Literary and Linguistic Computing, 28*(2), 242–258. https://doi.org/10.1093/llc/fqs054
20. Haentjens Dekker, R., & Middell, G. (2011). Computer-supported collation with CollateX: Managing textual variance in an environment with varying requirements. In *Supporting Digital Humanities 2011 Conference Proceedings* (pp. 1–18). University of Copenhagen. https://pure.knaw.nl/portal/files/799786159/Computer_supported_collation_with_CollateX_haentjens_dekker_middell.pdf
21. Haentjens Dekker, R., van Hulle, D., Middell, G., Neyt, V., & van Zundert, J. (2015). Computer-supported collation of modern manuscripts. *Literary and Linguistic Computing, 30*(3), 452–470. https://doi.org/10.1093/llc/fqu007
22. Lazzerini, F., & Di Franco, M. (2026). Creating a digital critical edition of a classical text with XML/TEI. *Umanistica Digitale, 18*, 45–72. https://doi.org/10.60923/issn.2532-8816/23486
23. Maas, P. (1958). *Textual criticism* (B. Flower, Trans.). Oxford University Press.
24. Mink, G. (2004). Problems of a highly contaminated tradition: The New Testament. Stemmatics of variants: A genealogical approach based on genealogical coherence. In P. van Reenen, M. van Mulken, & J. Dworkin (Eds.), *Studies in Stemmatology II* (pp. 13–85). John Benjamins. https://doi.org/10.1075/z.125.04min
25. Nury, E. (2018). *Automated collation and digital editions: From theory to practice* (Doctoral dissertation, Université de Lausanne). HAL. https://hal.science/tel-02493805
26. Pierazzo, E. (2015). *Digital scholarly editing: Theories, models and methods*. Ashgate Publishing / Routledge. https://doi.org/10.4324/9781315577227
27. Pierazzo, E. (2016). Modelling digital scholarly editions: 'In the making'. In M. J. Driscoll & E. Pierazzo (Eds.), *Digital Scholarly Editing: Theories and Practices* (pp. 61–77). Open Book Publishers. https://doi.org/10.11647/OBP.0095.04
28. Robinson, P. (2016). The digital revolution in scholarly editing. In B. Crostini, G. Iversen, & B. M. Jensen (Eds.), *Ars Edendi Lecture Series, vol. IV* (pp. 181–207). Stockholm University Press. https://doi.org/10.16993/baj.h
29. Sahle, P. (2013). *Digitale Editionsformen: Zum textuellen Quellenbegriff und zu den theoretischen Grundlagen digitaler Editionen* (3 vols.). Books on Demand / Universität zu Köln. https://kups.ub.uni-koeln.de/5018/
30. Sahle, P. (2016). What is a scholarly digital edition? In M. J. Driscoll & E. Pierazzo (Eds.), *Digital Scholarly Editing: Theories and Practices* (pp. 19–39). Open Book Publishers. https://doi.org/10.11647/OBP.0095.02
31. Sanderson, R., Ciccarese, P., & Young, B. (Eds.). (2017). *Web Annotation Data Model* (W3C Recommendation 23 February 2017). World Wide Web Consortium. https://www.w3.org/TR/annotation-model/
32. Schmidt, D. (2010). The inadequacy of embedded markup for cultural heritage texts. *Literary and Linguistic Computing, 25*(3), 337–356. https://doi.org/10.1093/llc/fqq007
33. Shahnazaryan, A. (2026). From manuscript to stemma: A phylogenetic approach to medieval Armenian fables. *Connections: A Journal for Historians and Area Specialists, 12*(1), 88–104. https://www.connections.clio-online.net/article/id/fda-161612
34. Simon, R., Barker, E., Desoto, P., & Isaksen, L. (2017). *Linked data annotation without the pointy brackets: Introducing Recogito 2*. Pelagios Network. https://www.researchgate.net/publication/316865029_Linked_Data_Annotation_Without_the_Pointy_Brackets_Introducing_Recogito_2
35. Spadini, E. (2017). The role of the base manuscript in the collation of medieval texts. In P. Boot, A. Cappellotto, W. R. Dobreva, M. J. Driscoll, F. Fischer, F. Hermans, J. Flores, L. Martinez, E. Pierazzo, & D. Sichani (Eds.), *Advances in Digital Scholarly Editing* (pp. 345–350). Sidestone Press. https://pure.knaw.nl/ws/portalfiles/portal/5794483/9789088904837_Boot_et_al._2017_Advances_in_Digital_Scholary_Editing_e_book.pdf
36. Sperberg-McQueen, C. M., & Burnard, L. (Eds.). (1994). *Guidelines for electronic text encoding and interchange (TEI P2)*. Association for Computers and the Humanities, Association for Computational Linguistics, Association for Literary and Linguistic Computing.
37. Stadler, P., Illetschko, M., & Veit, J. (2016). Towards a digital edition of the Carl Maria von Weber complete works. *International Journal of Humanities and Arts Computing, 10*(1), 67–85. https://doi.org/10.3366/ijhac.2016.0160
38. Sutherland, K. (2015). *Jane Austen's fiction manuscripts: A digital edition*. University of Oxford. https://janeausten.ac.uk/
39. Tafdrup, J., Bjerring-Hansen, J., & Hansen, J. N. (2026). Convergences: AI, editorial practice, and the Danish Digital Scholarly Edition of Grundtvig’s Works. *International Journal of Digital Humanities, 8*, 191–211. https://doi.org/10.1007/s42803-026-00125-z
40. TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and interchange* (Version 4.8.1). TEI Consortium. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/
41. Turska, M., Cummings, J., & Rahtz, S. (2016). Challenging the myth of presentation in digital editions: The TEI Processing Model. *Journal of the Text Encoding Initiative, 9*, 1–22. https://doi.org/10.4000/jtei.1467
42. Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., ... & Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data, 3*, Article 160018. https://doi.org/10.1038/sdata.2016.18
