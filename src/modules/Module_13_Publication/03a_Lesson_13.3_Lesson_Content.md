# Lesson 13.3 — Multi-Modal Publishing: Compiling Web, Interactive HTML, and Print-Ready PDF Packages

*RELS 398 / ENGL 398 · Topic 13: Publication · Meeting #36 (Fri Dec 4)*

***Studio and publication assembly week (no three-step cycle).** Today you complete the semester-long publication assembly, compiling your TEI XML master into responsive web applications, standalone offline HTML packages, and print-ready PDF volumes via CSS Paged Media, while establishing multi-tiered open access licensing and FAIR archiving.*

---

## **01 Content**

**The Multi-Modal Imperative: Why Digital Scholarly Editions Must Output to Multiple Media**

A fundamental paradox of contemporary digital scholarship is that while researchers create editions using rich, multi-layered XML knowledge graphs, end-users consume scholarship across radically divergent reading environments (Sahle, 2016; Driscoll & Pierazzo, 2016). Some scholars require an interactive, deep-zoom web application to examine high-resolution IIIF manuscript facsimiles alongside diplomatic transcriptions. Others require a standalone, portable HTML package that functions offline during fieldwork without internet access. Still others—including peer reviewers, university libraries, and classroom students—require a beautifully typeset, archival print-ready PDF with running line numbers and traditional critical apparatus footnotes (Sahle, 2016; Pierazzo, 2016).

This reality establishes the **Multi-Modal Imperative**: a true Digital Scholarly Edition (DSE) must not restrict itself to a single medium or proprietary interface. It must compile into multiple optimized presentation formats from a single, authoritative TEI XML source (Sahle, 2016; Turska et al., 2016).

| Publication Modality | Primary Reading Context | Core Technical Medium | Target Scholarly Audience |
| --- | --- | --- | --- |
| **Interactive Web Application** | Online research portal, classroom teaching | Dynamic HTML5, IIIF, Web Components | Digital humanists, general researchers |
| **Standalone Offline Package** | Fieldwork, archival preservation, USB drives | Static HTML5, Lunr.js, embedded assets | Traveling scholars, archival repositories |
| **Print-Ready PDF Codex** | Formal citation, physical reading, library print | CSS Paged Media / LaTeX `reledmac` / PDF/A | Traditional philologists, academic libraries |
| **Linked Open Data / Raw API** | Computational linguistics, automated ingestion | CTS URN endpoints, JSON-LD, TEI XML | Data scientists, machine learning pipelines |

Historically, publishers treated print and digital as competing, mutually exclusive paradigms. In modern computational philology, however, print and web are recognized as complementary modalities of the same underlying semantic model (Sahle, 2016; Pierazzo, 2016). By automating the compilation pipeline from your TEI master file, you achieve total intellectual consistency across every reading surface.

**Vocabulary.** *Multi-modal publishing* — the automated generation of distinct publication formats (web, standalone HTML, print PDF, linked data) from a single master XML source. *Scholarly affordance* — the specific reading, analytical, or annotative capabilities provided by a particular medium. *Single source of truth* — maintaining one canonical dataset from which all derivative deliverables are compiled.

**Takeaway:** A digital scholarly edition must fulfill the multi-modal imperative by compiling into web, standalone offline, and print-ready formats from a single TEI XML master.

---

## **02 Content**

**Deconstructing Medium-Specific Affordances: Screen vs. Page vs. Raw Data**

To publish effectively across multiple formats, an editor must understand the unique **medium-specific affordances** and constraints of each target channel (Pierazzo, 2016; Sahle, 2016).

A digital screen is fluid, boundless, and interactive, but it is ephemeral and prone to distraction. A physical printed page is bounded, fixed, and permanent, but it is static and spatially constrained. Raw data is queryable and machine-actionable, but it is illegible to human readers without a rendering interface (Coombs et al., 1987; Renear, 2004).

| Medium Dimension | The Interactive Web Screen | The Paginated Print Page | The Raw Data / XML Corpus |
| --- | --- | --- | --- |
| **Spatial Model** | Continuous vertical scrolling / dynamic viewports | Fixed two-dimensional page grid ($A_4$, US Letter) | Non-visual tree hierarchy / graph network |
| **Interaction Model** | Clickable popovers, image zooming, layer toggles | Static linear reading, marginal annotations | XPath queries, SPARQL endpoints, NLP pipelines |
| **Apparatus Placement** | Interactive hover popups / collapsible sidebar drawers | Multi-tiered footnotes at page bottom | Parallel segmentation elements inline |
| **Citation Stability** | URI anchors, CTS URNs, Git commit hashes | Fixed page numbers and verse line numbers | Persistent identifiers (PIDs), DOIs, XPath coordinates |
| **Preservation Horizon** | Dependent on server maintenance and web standards | Decades to centuries on acid-free paper / PDF/A | High bit preservation; schema version dependent |

An editor must never attempt to force a print layout onto a smartphone screen, nor should they attempt to paste web hyperlinks onto a printed page. Instead, the transformation pipeline must translate abstract scholarly features into the idiom best suited for each medium:

- On the web, variant readings expand inside smooth interactive popovers (`<pb-popover>`);
- In print, those exact same variants are formatted into compact, Greek-typeset footnote lines at the foot of the page;
- In raw data exports, they are structured as machine-actionable parallel segmentation nodes (`<app><lem>...<rdg>...</app>`) (Turska et al., 2016; Fischer, 2020).

**Vocabulary.** *Medium-specific affordance* — the distinctive functional properties and reading behaviors enabled by a specific physical or digital medium. *Spatial bounding* — the fixed physical dimensions of a printed sheet of paper. *Citation stability* — the guarantee that a reference cited today will resolve to the exact same passage decades later.

**Takeaway:** Effective multi-modal publishing honors the distinct affordances of screens (interactivity), pages (stability), and raw data (computability).

---

## **03 Content**

**Responsive Web Edition Architecture: Client-Side Interaction and Semantic HTML5**

The primary public gateway to your digital edition is the **Responsive Web Application** (Turska et al., 2016; Stadler et al., 2016).

Modern digital edition web design has abandoned heavyweight, proprietary server software in favor of **Semantic HTML5** enhanced with modern CSS grid layouts and lightweight JavaScript Web Components. This architecture guarantees that your edition renders cleanly across desktop workstations, tablets, and smartphones (Turska et al., 2016).

| Interface Region | Sub-Components & Technology | Functional Capability |
| --- | --- | --- |
| **Left Viewport (Facsimile)** | Deep-zoom IIIF canvas, OpenSeadragon, surface overlay | Multi-resolution zooming, surface bounding box highlight |
| **Right Viewport (Critical Text)** | Polytonic Greek text, `<pb-view>`, dynamic popovers | Reading layer toggles, interactive apparatus inspection |
| **Bottom Drawer (Commentary)** | Collapsible `<pb-drawer>`, Leipzig interlinear grid | Synchronized philological notes, four-line morphological glosses |

The core components of a responsive digital edition interface include:

1. **Synchronized Dual Viewport:** A two-column responsive grid pairing high-resolution IIIF manuscript images on the left with transformed TEI reading text on the right;
2. **Dynamic Layer Toggles:** User controls allowing readers to switch seamlessly between diplomatic uncial transcription, normalized reading text, and Leipzig-aligned interlinear glosses;
3. **Interactive Critical Apparatus:** Variants displayed via unobtrusive dotted underlines that open informative popovers upon click or hover;
4. **Contextual Commentary Drawer:** A slide-out sidebar or bottom panel that displays linked philological, historical, and intertextual notes without obscuring the base text (Turska et al., 2016; Berti, 2026).

By building on standard Semantic HTML5 tags (`<article>`, `<section>`, `<nav>`, `<aside>`), you ensure that screen readers, search engine web crawlers, and assistive technologies can parse your scholarship with maximum accessibility (Barzaghi et al., 2025; Wilkinson et al., 2016).

**Vocabulary.** *Responsive web architecture* — a web design approach that dynamically adapts layout and typography to fit any screen size or device. *Dual viewport* — an interface layout that displays manuscript images and transcribed text side by side. *Semantic HTML5* — using standard HTML tags that convey structural meaning rather than generic container divisions.

**Takeaway:** Responsive web editions combine semantic HTML5, CSS grid layouts, and interactive components to deliver synchronized facsimiles, texts, and commentaries.

---

## **04 Content**

**Building Standalone, Serverless HTML Packages (EVT and Static Bundles)**

While dynamic client-server platforms like TEI Publisher offer rich backend querying, they carry a major vulnerability: **server dependency**. If an institution shuts down its XML database server or fails to renew its hosting contract, the digital edition vanishes from the internet (Sahle, 2016; Driscoll & Pierazzo, 2016).

To guarantee unconditional, permanent access, digital editors compile **Standalone Serverless HTML Packages**. A standalone package is a self-contained directory containing pure HTML, CSS, JavaScript, and pre-rendered SVG assets that opens directly in any web browser without requiring an internet connection, a web server, or a backend database (Buzzoni, 2016).

| File / Directory Path | Asset Function | Technical Content |
| --- | --- | --- |
| `index.html` | Entry point | Self-contained offline viewer (double-clickable when data is inlined; otherwise served locally) |
| `assets/css/` | Visual stylesheets | `edition.css` with embedded Cardo & Noto Serif WOFF2 fonts |
| `assets/js/` | Client runtime | `edition.js` viewer logic + pre-compiled Lunr `search-index.js` |
| `assets/images/` | Facsimile storage | High-resolution JPEG/WebP local manuscript page images |
| `data/` | Master XML archives | `1thess_edition.xml` source and `1thess_odd.odd` specification |
| `LICENSE.md` | Legal licensing | Multi-tiered CC BY 4.0, CC0 1.0, and MIT statements |

| Deployment Architecture | Server Required? | Offline Usable? | Archival Durability | Maintenance Cost |
| --- | --- | --- | --- | --- |
| **Server-Dependent Stack** (eXist-db) | Yes (Java/XML Server) | No (Requires network) | Medium (Vulnerable to server decay) | High (Ongoing server administration) |
| **Standalone Static Package** (custom build / EVT) | No (File system) | Yes (100% offline) | Extremely High (Decades in any browser) | Zero (Static hosting on GitHub/Zenodo) |

The layout above is the one this course's own build script produces (Section 14 onward). **Edition Visualization Technology (EVT)** takes a different route to the same goal: rather than compiling a bespoke bundle, you drop your TEI XML and facsimiles into EVT's prebuilt client-side viewer and configure it through a settings file. Either way, the output is a static bundle. The entire edition can be distributed on USB flash drives, attached to archival journal submissions, or hosted for free on GitHub Pages indefinitely (Buzzoni, 2016; Driscoll & Pierazzo, 2016).

**Current status (September 2026).** EVT 3 v2.0.0-beta ("Beta 2") was released on 28 September 2026 ([release announcement](https://visualizationtechnology.wordpress.com/2026/09/28/evt-3-beta-2-evt-3-v2-0-0-beta-available-for-download-and-testing/)). It consolidates configuration into a single YAML file, supports double-end-point attachment for the critical apparatus (compare Module 15), refines line-level image–text highlighting (compare Module 3), and adds an *Errors* button that surfaces encoding mistakes. Running it requires a local web server (VS Code Live Server, or Git/npm), not a double-click. The developers state plainly that the beta is not yet ready for publishing editions; a stable release is planned for 2027. Treat EVT 3 as a tool to explore and test your encoding against, not as the delivery platform for your final package.

**Vocabulary.** *Serverless edition bundle* — a digital edition compiled into static HTML/JS/CSS files requiring no server-side database. *Edition Visualization Technology (EVT)* — an open-source static client tool for rendering TEI critical and diplomatic editions. *Server decay* — the eventual failure and abandonment of digital projects due to unmaintained server infrastructure.

**Takeaway:** Standalone, serverless HTML packages eliminate database dependencies, allowing editions to run offline and survive indefinitely as static files.

---

## **05 Content**

**Client-Side Full-Text Search with Lunr.js and Standoff Indices**

A common objection to static, serverless editions is the perceived loss of search functionality. Without a backend database like eXist-db or Elasticsearch, how can users perform full-text and entity queries? (Stadler et al., 2016).

The solution in modern web engineering is **Client-Side Indexing with Lunr.js**. Lunr.js is a lightweight, full-text search engine written entirely in JavaScript that runs locally inside the user's browser (Barzaghi et al., 2025).

The build pipeline compiles a pre-computed JSON search index at build time:

```javascript
// Sample Pre-Compiled Lunr.js Search Index: search-index.js
const searchIndex = lunr(function () {
  this.ref('id');
  this.field('passage');
  this.field('greek_surface');
  this.field('lemma');
  this.field('pos');
  this.field('english_gloss');
  this.field('commentary');

  // Ingest Pre-Extracted Tokens from TEI XML
  editionTokens.forEach(function (token) {
    this.add(token);
  }, this);
});
```

| Search Modality | Query Syntax | In-Browser Client Execution |
| --- | --- | --- |
| **Surface Greek Match** | `νηπιοι` | Scans surface forms across all transcribed witnesses |
| **Morphological Lemma Search** | `lemma:λόγος` | Returns all inflected tokens linked to lemma *λόγος* |
| **Part-of-Speech Filter** | `pos:N-NSM` | Filters for nominative singular masculine nouns |
| **Commentary Full-Text** | `commentary:Thessalonica` | Searches all stand-off commentary notes and glosses |

Because the entire index is pre-computed during the build step and stored as a compact JSON file (~100 KB), search queries execute instantly in the browser without sending network requests to a server (Barzaghi et al., 2025).

**Vocabulary.** *Lunr.js* — a client-side JavaScript full-text search engine designed for static web applications. *Pre-computed index* — a search index generated during build time and serialized into JSON for instant browser querying. *Zero-latency search* — search queries evaluated in local memory without network round-trips.

**Takeaway:** Pre-compiling search indices with Lunr.js enables instant full-text, lemma, and commentary searching directly inside static, serverless web editions.

---

## **06 Content**

**The CSS Paged Media Standard: W3C Paged Media Modules for Print Layout**

While web browsers excel at fluid screens, producing an archival print edition requires dividing continuous text into discrete, physical pages with running headers, page numbers, footnotes, and margins. For decades, this was accomplished using proprietary desktop publishing tools (such as Adobe InDesign) or complex XML formatting objects (XSL-FO) (Turska et al., 2016).

Today, the modern standard for print generation from XML is **CSS Paged Media**, standardized by the W3C (World Wide Web Consortium, 2026; Turska et al., 2016).

**CSS Paged Media** extends standard CSS with page-specific rules:

```css
/* Page Geometry and Running Margin Boxes */
@page {
  size: 7in 10in; /* Standard Academic Monograph Royal Octavo */
  margin: 20mm 15mm 25mm 15mm;

  @top-left {
    content: "RELS 398 / ENGL 398 Digital Critical Edition";
    font-family: 'Cardo', serif;
    font-size: 8pt;
    font-variant: small-caps;
  }
  @top-right {
    content: string(heading-text);
    font-family: 'Cardo', serif;
    font-size: 8pt;
    font-style: italic;
  }
  @bottom-center {
    content: counter(page);
    font-family: 'Cardo', serif;
    font-size: 9pt;
  }
}
```

| CSS Paged Media Rule | Primary Function | Output Result |
| --- | --- | --- |
| `@page` | Defines physical trim size, bleed, and margins | 7x10 inch monograph page with 20mm margins |
| `@top-left / @top-right` | Defines running headers | Injects book title and current chapter heading |
| `@bottom-center` | Defines running footer | Injects dynamic page counter (`counter(page)`) |
| `break-before: page` | Enforces structural page breaks | Forces chapters to begin on fresh pages |
| `float: footnote` | Relegates elements to page bottom | Generates paginated critical apparatus footnotes |

By defining print layouts with standard CSS, you reuse your existing web styling rules, eliminating the need to learn complex auxiliary typesetting languages (Turska et al., 2016).

**Vocabulary.** *CSS Paged Media* — W3C CSS specifications governing the pagination and printing of web documents. `@page` — CSS at-rule used to define the dimensions, orientation, and margins of a printed page. *Running header* — repetitive text printed at the top of successive pages indicating title or chapter.

**Takeaway:** The CSS Paged Media standard enables scholars to design beautiful, paginated print layouts using familiar CSS syntax.

---

## **07 Content**

**Typesetting Pages with CSS: `@page` Selectors, Bleeds, and Running Headers**

Professional book design requires distinct layouts for different parts of a book: left-hand (verso) and right-hand (recto) pages have mirror margins to accommodate the binding gutter; title pages suppress running headers; and chapter beginnings require extra top spacing (Turska et al., 2016).

CSS Paged Media accommodates these requirements through specialized **page pseudo-class selectors**:

```css
/* Recto (Right-Hand Page): Wider Inner Left Gutter */
@page :right {
  margin-left: 25mm;  /* Binding Gutter */
  margin-right: 15mm;
  @top-right {
    content: counter(page);
  }
  @top-left {
    content: string(chapter-title);
  }
}

/* Verso (Left-Hand Page): Wider Inner Right Gutter */
@page :left {
  margin-left: 15mm;
  margin-right: 25mm;  /* Binding Gutter */
  @top-left {
    content: counter(page);
  }
  @top-right {
    content: "1 Thessalonians 2: A Digital Critical Edition";
  }
}

/* First Page of Chapter: Suppress Running Headers */
@page :first {
  @top-left { content: none; }
  @top-right { content: none; }
  margin-top: 40mm;
}
```

| Page Selector | Target Surface | Design Requirement Addressed |
| --- | --- | --- |
| `@page :right` | Recto (Odd Pages) | Wider left margin for book spine gutter; chapter title header |
| `@page :left` | Verso (Even Pages) | Wider right margin for book spine gutter; edition title header |
| `@page :first` | Chapter Opening Pages | Clears running header; increases top margin for chapter title |
| `@page :blank` | Empty Verso Buffer Pages | Suppresses all headers and footers on blank buffer pages |

Using pseudo-class selectors guarantees that your compiled PDF exhibits the exact typographic polish of an academic university press monograph (Turska et al., 2016; Fischer, 2020).

**Vocabulary.** *Recto* — the front or right-hand page of a bound book (always odd-numbered). *Verso* — the back or left-hand page of a bound book (always even-numbered). *Binding gutter* — the extra margin space added to the inner edge of a page to ensure text is not obscured by book binding.

**Takeaway:** Using `@page :left`, `@page :right`, and `@page :first` selectors establishes mirror binding gutters and professional academic running headers.

---

## **08 Content**

**Margin Boxes and Page Numbering in CSS Paged Media**

In the CSS Paged Media model, the page margin is not merely empty white space; it is divided into sixteen distinct **margin boxes** surrounding the central content area (World Wide Web Consortium, 2026; Turska et al., 2016).

| Margin Box Position | Margin Box Identifier | Standard Scholarly Function |
| --- | --- | --- |
| **Top Left / Right Corners** | `@top-left-corner`, `@top-right-corner` | Volume numbers, edition brand stamps |
| **Top Margin (Running Headers)** | `@top-left`, `@top-center`, `@top-right` | Book titles, chapter headings, section markers |
| **Left / Right Outer Margins** | `@left-middle`, `@right-middle` | Line numbers, marginal glosses, folio indicators |
| **Bottom Margin (Running Footers)** | `@bottom-left`, `@bottom-center`, `@bottom-right` | Page numbering, archival DOI / Zenodo stamps |

These margin boxes allow editors to position complex metadata with absolute precision:

- **String Sets for Dynamic Headers:** When a chapter title (`<head>`) appears on a page, CSS captures its text using `string-set: chapter-title content()`. The margin box retrieves it dynamically using `content: string(chapter-title);`
- **Page Counters:** CSS maintains page counters that can be formatted as Arabic numerals (`counter(page)`), Roman numerals for front matter (`counter(page, lower-roman)`), or total page counts (`counter(pages)`).

```css
/* Front Matter Page Numbering (Roman Numerals) */
.front-matter {
  page: front;
}
@page front {
  @bottom-center {
    content: counter(page, lower-roman);
  }
}

/* Main Text Page Numbering (Arabic Numerals) */
.main-text {
  page: main;
  counter-reset: page 1;
}
@page main {
  @bottom-center {
    content: counter(page, decimal);
  }
}
```

| Margin Box Name | Position on Page | Standard Critical Edition Usage |
| --- | --- | --- |
| `@top-center` | Centered top margin | Running biblical book and chapter citation (e.g., *1 Thess 2:1–12*) |
| `@left-middle` | Outer left vertical margin | Line numbering milestones (e.g., line 5, 10, 15, 20) |
| `@bottom-center` | Centered bottom margin | Page number (Arabic or Roman numeral) |
| `@bottom-right` | Bottom right corner | Archival volume DOI or Zenodo PID stamp |

**Vocabulary.** *Margin box* — one of sixteen predefined layout areas in the page margin defined by CSS Paged Media. `string-set` — CSS property that copies text content from a document node into a named string variable. `counter-reset` — CSS property initializing or restarting a counter (such as resetting page numbers to 1).

**Takeaway:** CSS margin boxes provide sixteen dedicated layout containers for dynamic running headers, folio markers, and multi-scheme page counters.

---

## **09 Content**

**Evaluating CSS Paged Media Rendering Engines: Paged.js vs. WeasyPrint vs. Vivliostyle**

To compile HTML and CSS Paged Media stylesheets into physical PDF files, developers use specialized **Paged Media rendering engines** (Turska et al., 2016).

Three primary open-source engines lead the digital humanities field:

| Rendering Engine | Architecture & Core Technology | Primary Strengths | Primary Liabilities | Optimal Use Case |
| --- | --- | --- | --- | --- |
| **Paged.js** | Client-side JavaScript polyfill running inside Chromium headless | Direct browser preview; interactive debugging in DevTools; 100% standard CSS support | Requires Node.js / headless browser runner for PDF compilation | Interactive development, browser preview, classroom lab |
| **WeasyPrint** | Standalone Python / Cairo / Pango rendering engine | Zero browser dependencies; clean CLI automation; native PDF/A and bookmark support | Slightly slower on complex multi-tier footnote layouts | Automated Python build pipelines, CI/CD runners, server batch jobs |
| **Vivliostyle** | TypeScript rendering engine based on Chromium | Excellent East Asian typography; advanced page float control; CLI & GUI apps | Heavier dependency tree | Complex multilingual layouts, e-book conversions |

In a typical publishing workflow:

1. **Development & Design Phase:** Use **Paged.js** inside the browser to visually inspect and refine your layout in real time using Chrome DevTools;
2. **Automated Production Build:** Execute **WeasyPrint** or **Paged.js CLI** inside a Python script or GitHub Actions workflow to compile the final publication PDF automatically (Turska et al., 2016; Barzaghi et al., 2025).

**Vocabulary.** *Paged.js* — an open-source JavaScript polyfill that renders CSS Paged Media layouts inside any web browser. *WeasyPrint* — an open-source Python library that transforms HTML and CSS into print-ready PDF documents. *Headless browser* — a web browser running without a graphical user interface, controlled programmatically via command line.

**Takeaway:** Paged.js enables interactive in-browser layout design, while WeasyPrint provides automated Python-based PDF compilation.

---

## **10 Content**

**The Classical Print Tradition: LaTeX, `reledmac`, and Typst Comparison**

While CSS Paged Media represents the cutting edge of web-to-print compilation, textual editing has a rich history of typesetting systems designed specifically for philology. An editor should understand how CSS Paged Media compares to traditional systems like **LaTeX (`reledmac`)** and modern alternatives like **Typst** (Fischer, 2020; Sahle, 2016).

| Typesetting System | Core Architecture | Apparatus Strategy | Primary Strengths | Primary Liabilities |
| --- | --- | --- | --- | --- |
| **Classical LaTeX (`reledmac`)** | TeX macro engine (~5GB TeX Live) | Multi-tier `\Afootnote`, sub-line lemmas | Unmatched micro-typography and line-breaking algorithms | Steep learning curve; disconnected from web CSS |
| **Modern CSS Paged Media** | Paged.js / WeasyPrint | `float: footnote`, CSS flexbox | Unified web/print styling; native HTML5/TEI processing model | Requires tuning for deep multi-tier apparatus pages |
| **Next-Generation Typst** | Standalone Rust engine (<100ms) | Footnote stream / custom functions | Blazing fast compilation; clean syntax | Developing critical apparatus package ecosystem |

| Feature Dimension | LaTeX (`reledmac`) | CSS Paged Media (Paged.js / WeasyPrint) | Typst |
| --- | --- | --- | --- |
| **Apparatus Capability** | Multi-tier footnotes, sub-line lemmas, line numbering | Multi-tier footnotes, CSS float footnotes | Developing footnote apparatus libraries |
| **Pipeline Integration** | Requires TEI-to-LaTeX XSLT stylesheets | Direct compilation from TEI ODD Processing Model | Requires TEI-to-Typst conversion scripts |
| **Installation Footprint** | Massive TeX Live distribution (~5 GB) | Lightweight npm / Python package (~50 MB) | Single standalone binary (~20 MB) |
| **Styling Language** | Low-level TeX macros | Standard W3C CSS3 | Custom Rust-like syntax |

For traditional book publication with massive, four-tier apparatuses spanning hundreds of variants per page, LaTeX `reledmac` remains an industry standard. However, for modern digital humanities projects seeking a single, maintainable pipeline bridging web and print from ODD, **CSS Paged Media** is the recommended standard (Turska et al., 2016; Fischer, 2020).

**Vocabulary.** *`reledmac`* — a comprehensive LaTeX package designed for typesetting critical editions with multiple apparatus streams and line numbers. *Typst* — a modern, Rust-based markup-based typesetting system designed as an alternative to LaTeX. *Micro-typography* — fine adjustments to kerning, tracking, and line breaking to produce optimal visual harmony.

**Takeaway:** CSS Paged Media unifies web and print workflows, while LaTeX `reledmac` and Typst offer specialized micro-typographic alternatives.

---

## **11 Content**

**Compiling Multi-Tiered Critical Apparatuses for Paginated Print Output**

A hallmark of scholarly critical editions is the **multi-tiered apparatus**: dividing the bottom of the page into distinct horizontal bands dedicated to different categories of textual evidence (Fischer, 2020; Maas, 1958).

In our digital edition of 1 Thessalonians 2, we establish a **two-tier apparatus layout**:

- **Tier 1 (Significant Textual Variants):** Significant variants affecting the stemma, translation, or theological interpretation;
- **Tier 2 (Orthographic & Scribal Variants):** Trivial spelling variations, iotacisms, movable nus, and scribal slips (Topic 15; Topic 13.1).

```css
/* Footnote Stream Base Styling */
@page {
  @footnotes {
    border-top: 1px solid #333;
    padding-top: 8pt;
    margin-top: 15pt;
  }
}

/* Tier 1: Significant Textual Variants (Bold Lemma, Bracket, Sigla) */
.app-tier1 {
  float: footnote;
  font-family: 'Cardo', serif;
  font-size: 8.5pt;
  line-height: 1.25;
  margin-bottom: 2pt;
}
.app-tier1 .lemma {
  font-weight: bold;
}
.app-tier1 .bracket::after {
  content: '] ';
}

/* Tier 2: Orthographic / Trivial Variants (Smaller Monospace / Italic) */
.app-tier2 {
  float: footnote;
  font-family: 'Cardo', serif;
  font-size: 7.5pt;
  color: #444;
  line-height: 1.15;
}
```

| Apparatus Tier | Content Categorization | Print Typography | Sample Rendered Footnote Line |
| --- | --- | --- | --- |
| **Tier 1: Substantive** | Major variants, transpositions, omissions | 8.5pt Cardo, bold lemma, standard sigla | `7 νήπιοι] א B C*; ἤπιοι A C2 D Ψ 33 1739 𝔐` |
| **Tier 2: Orthographic** | Iotacisms, movable nus, spelling slips | 7.5pt Cardo, muted gray, compact | `7 εγενηθημεν] εγενηθημεθα D* · 8 ομειρομενοι] ιμειρομενοι B` |

By using CSS `float: footnote`, the rendering engine automatically calculates page breaks, ensuring that footnotes always appear at the bottom of the exact page where their corresponding text occurs (Turska et al., 2016; Fischer, 2020).

**Vocabulary.** *Multi-tiered apparatus* — a critical apparatus divided into separate horizontal bands for substantive vs. orthographic variants. `float: footnote` — CSS Paged Media property that moves an element from the text stream to the bottom footnote area. *Substantive variant* — a textual variation that affects meaning or syntax.

**Takeaway:** Using CSS `float: footnote` and distinct classes formats multi-tiered critical apparatuses at the foot of each page automatically.

---

## **12 Content**

**Managing Polytonic Greek Fonts and Typography (Cardo, New Athena Unicode, Noto Serif)**

Typesetting ancient Greek texts requires specialized **polytonic Unicode fonts** that support the full range of Greek diacritics: acute, grave, and circumflex accents; rough and smooth breathings; iota subscripts ($\alpha, \eta, \omega$ with $\iota$); and uncial manuscript glyphs (TEI Consortium, 2026).

If a publication uses system fonts that lack proper Greek glyph coverage, the system will fall back to mismatched fonts, resulting in jarring typographical errors termed "tofu" (missing character boxes) or misaligned diacritics.

Three premier open-source font families are standard for academic Greek publication:

| Font Family | Designer / Institution | Primary Typographic Style | Best Use Case |
| --- | --- | --- | --- |
| **Cardo** | David Perry (Scholars Press) | Classical Renaissance humanist typeface based on Aldus Manutius | Critical texts, scholarly apparatuses, formal academic monographs |
| **New Athena Unicode** | American Philological Association (SCS) | Specialized epigraphical and papyrological font with extensive symbols | Diplomatic transcriptions, papyrus editions, epigraphy |
| **Noto Serif / Noto Sans** | Google Fonts Internationalization Project | Clean, modern, highly legible universal multilingual typeface | Screen reading, mobile interfaces, clean commentary text |

```css
/* Embedding Web Open Font Format (WOFF2) for Universal Rendering */
@font-face {
  font-family: 'Cardo';
  src: url('../fonts/Cardo-Regular.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Cardo';
  src: url('../fonts/Cardo-Bold.woff2') format('woff2');
  font-weight: bold;
  font-style: normal;
  font-display: swap;
}

.greek-text {
  font-family: 'Cardo', 'New Athena Unicode', serif;
  font-feature-settings: "kern" 1, "liga" 1;
  text-rendering: optimizeLegibility;
}
```

Embedding `@font-face` definitions directly inside your CSS and packaging the `.woff2` font files with your edition guarantees that polytonic Greek characters render with flawless typographic accuracy on every device and in every compiled PDF (Turska et al., 2016).

**Vocabulary.** *Polytonic Greek* — the Greek writing system featuring the full traditional system of accents, breathings, and iota subscripts. *WOFF2 (Web Open Font Format 2.0)* — a highly compressed font format optimized for web and digital publishing. *Glyph fallback* — the undesirable visual glitch occurring when a system substitutes missing characters with default system fonts.

**Takeaway:** Packaging dedicated polytonic Greek fonts (Cardo, New Athena Unicode) ensures flawless diacritic rendering across web and print media.

---

## **13 Content**

**Archival PDF Standards: PDF/A Compliance and Long-Term Preservation**

A standard PDF file generated by a typical desktop application is not suitable for long-term archival preservation. Standard PDFs often depend on external fonts installed on the host operating system, contain active JavaScript scripts, reference external URLs, and use non-standard color profiles that can degrade over time (International Organization for Standardization, 2020).

For scholarly publication, academic libraries and digital repositories mandate **PDF/A (PDF for Archiving)** compliance (ISO 19005 standard) (International Organization for Standardization, 2020).

**PDF/A** enforces strict preservation constraints:

1. **100% Font Embedding:** Every glyph used in the text must be fully embedded within the PDF binary;
2. **Device-Independent Color:** Colors must be defined using standard sRGB or CMYK ICC profiles;
3. **No Dynamic Content:** Interactive JavaScript, external audio/video streams, and proprietary encryption are strictly prohibited;
4. **Embedded XMP Metadata:** Bibliographical metadata (title, author, DOI, license) must be embedded in machine-readable Extensible Metadata Platform (XMP) XML (International Organization for Standardization, 2020; Wilkinson et al., 2016).

```
   WeasyPrint PDF/A Compilation Command:
   weasyprint --pdf-variant pdf/a-3b \
              --pdf-metadata-title "1 Thessalonians 2 Digital Critical Edition" \
              --pdf-metadata-author "RELS 398 Editing Team" \
              build/print.html build/1thess_edition_v1.0.0_archival.pdf
```

| PDF Standard | Target Use Case | Preserved Capabilities |
| --- | --- | --- |
| **PDF/A-1b** | Basic visual preservation | Guarantees exact visual reproduction over decades |
| **PDF/A-2u** | Unicode semantic preservation | Preserves exact Unicode text extraction and searchability |
| **PDF/A-3b** | Compound data archiving | Allows embedding the raw TEI XML source file *inside* the PDF binary |

Compiling to **PDF/A-3b** represents the gold standard of digital preservation: the PDF serves as a human-readable printed book, while simultaneously carrying the raw TEI XML master file embedded inside itself as an attachment (Wilkinson et al., 2016).

**Vocabulary.** *PDF/A* — an ISO-standardized version of the Portable Document Format specialized for long-term digital preservation. *Font embedding* — including the complete binary font data within a document file. *Compound archiving (PDF/A-3)* — embedding raw data files (such as XML) directly inside an archival PDF container.

**Takeaway:** Compiling print editions to PDF/A-3b guarantees long-term visual preservation while embedding the raw TEI XML source directly inside the PDF.

---

## **14 Content**

**Automated Multi-Modal Compilation Pipelines via Python and Shell Automation**

To eliminate manual errors and ensure 100% reproducibility, multi-modal publishing must be orchestrated by an **automated build pipeline** (Barzaghi et al., 2025; Topic 1).

A master build script (such as `build_edition.py` or a `Makefile`) automates the entire sequence from source TEI XML to finished web and PDF deliverables:

```python
# build_edition.py: Master Publication Pipeline Script
import subprocess
import shutil
from pathlib import Path

def build_all():
    print("=== Step 1: Running Quality Assurance Linter ===")
    subprocess.run(["python3", "scripts/lint_lesson_content.py", "--course-dir", "."], check=True)

    print("=== Step 2: Compiling ODD to Relax NG and Schematron ===")
    subprocess.run([
        "java", "-jar", "bin/saxon-he.jar",
        "-s:odds/edition.odd", "-xsl:scripts/odd2relaxng.xsl", "-o:build/edition.rng"
    ], check=True)

    print("=== Step 3: Validating Master TEI XML against Generated Schema ===")
    subprocess.run(["xmllint", "--noout", "--relaxng", "build/edition.rng", "data/edition.xml"], check=True)

    print("=== Step 4: Compiling Interactive Web Application ===")
    subprocess.run([
        "java", "-jar", "bin/saxon-he.jar",
        "-s:data/edition.xml", "-xsl:scripts/tei2html-web.xsl", "-o:dist/web/index.html"
    ], check=True)

    print("=== Step 5: Compiling Standalone Lunr.js Search Index ===")
    subprocess.run(["python3", "scripts/generate_search_index.py", "data/edition.xml", "dist/web/assets/js/search-index.js"], check=True)

    print("=== Step 6: Compiling Print-Ready PDF via WeasyPrint ===")
    subprocess.run([
        "weasyprint", "--pdf-variant", "pdf/a-3b",
        "dist/web/index.html", "dist/pdf/1thess_edition_archival.pdf"
    ], check=True)

    print("=== Multi-Modal Build Successfully Completed! ===")

if __name__ == "__main__":
    build_all()
```

| Pipeline Step | Tool Invoked | Deliverable Generated |
| --- | --- | --- |
| **1. Lint Gate** | Python linter | Validates takeaways, tables, and markup rules |
| **2. ODD Compilation** | Saxon XSLT | `build/edition.rng` schema |
| **3. Validation** | `xmllint` | Validates `data/edition.xml` |
| **4. Web Compilation** | Saxon XSLT | `dist/web/index.html` interactive portal |
| **5. Search Index** | Python extraction | `dist/web/assets/js/search-index.js` |
| **6. Archival PDF** | WeasyPrint | `dist/pdf/1thess_edition_archival.pdf` (PDF/A-3b) |

Running a single command (`python3 build_edition.py`) regenerates every publication artifact in seconds, guaranteeing that your deliverables never drift out of sync (Barzaghi et al., 2025; Wilkinson et al., 2016).

**Vocabulary.** *Automated build pipeline* — a scripted workflow that executes compilation, validation, and packaging tasks in sequence. *Lint gate* — a strict validation checkpoint that halts the build pipeline if formatting or schema errors are detected. *Reproducible research* — the principle that any scholar can re-run the build pipeline to generate identical deliverables.

**Takeaway:** An automated Python build pipeline orchestrates validation, ODD compilation, search indexing, and PDF generation with a single command.

---

## **15 Content**

**Multi-Tiered Open Access Licensing Architecture for Digital Editions**

A digital critical edition is a complex intellectual artifact composed of heterogeneous assets: historical manuscript texts, editorial introductions, conjectural emendations, critical translations, morphological taggings, RDF knowledge graphs, and transformation software code (Sahle, 2016; Barzaghi et al., 2025).

Because these assets serve different scholarly functions, applying a single blanket license (such as standard "All Rights Reserved" copyright) cripples the edition's utility. A digital scholarly edition requires a **Multi-Tiered Open Access Licensing Architecture** (Barzaghi et al., 2025; Driscoll & Pierazzo, 2016).

| Licensing Tier | Governing Legal Instrument | Project Assets Governed | Scholarly Objective |
| --- | --- | --- | --- |
| **Tier 1: Creative Prose** | Creative Commons Attribution (CC BY 4.0) | Critical text, translation, historical introduction, commentary | Protects scholarly credit and attribution for authors |
| **Tier 2: Structured Data** | Creative Commons Zero (CC0 1.0 Universal) | Raw tokens, collation matrices, POS tags, RDF knowledge graphs | Eliminates attribution stacking for data aggregators |
| **Tier 3: Software & Tools**| Open Source License (MIT / GPL-3.0) | ODD schemas, XSLT/XQuery pipelines, Python scripts, Web Components | Maximizes computational reproducibility and software reuse |

This multi-tiered architecture achieves three vital objectives:

1. **Academic Recognition:** CC BY 4.0 ensures that human authors receive proper academic citation for their prose, translation, and editorial analysis;
2. **Computational Reusability:** CC0 ensures that algorithms, data aggregators, and Linked Open Data graphs can ingest raw tokens without legal friction;
3. **Software Freedom:** MIT licensing allows other digital humanists to fork and reuse your build scripts and ODD stylesheets (Barzaghi et al., 2025; Wilkinson et al., 2016).

**Vocabulary.** *Multi-tiered licensing* — applying different, specialized open access licenses to distinct layers of a digital project. *Legal friction* — contractual or copyright barriers that prevent computational reuse of research data. *Open access* — the free, unrestricted online availability of scholarly research.

**Takeaway:** Multi-tiered licensing pairs CC BY 4.0 for prose, CC0 for structured data, and MIT for software to maximize scholarly impact and legal reusability.

---

## **16 Content**

**The Creative Commons Suite: Applying CC BY 4.0 to Critical Texts and Translations**

For human-authored scholarly prose, critical translations, and commentary notes, the international gold standard is the **Creative Commons Attribution 4.0 International License (CC BY 4.0)** (Creative Commons, 2026; Barzaghi et al., 2025).

Under CC BY 4.0:

- **Share:** Anyone is free to copy, distribute, and transmit the work in any medium or format;
- **Adapt:** Anyone is free to remix, transform, and build upon the material for any purpose, including commercial applications;
- **Attribution Condition:** The user must give appropriate credit, provide a link to the license, and indicate if changes were made (Creative Commons, 2026).

| Creative Commons License | Permitted Uses | Commercial Use? | Adaptations Allowed? | Recommended for DSE? |
| --- | --- | --- | --- | --- |
| **CC BY 4.0** | Share, adapt, remix | Yes (with attribution) | Yes (with attribution) | **Yes (Gold Standard)** |
| **CC BY-SA 4.0** | Share, adapt | Yes (with attribution) | Yes (Share-Alike copyleft) | Acceptable |
| **CC BY-NC 4.0** | Share, adapt | No (Non-commercial only) | Yes (Non-commercial) | Discouraged (Restricts repositories) |
| **CC BY-ND 4.0** | Share only | Yes (with attribution) | No (No derivatives) | Strongly Discouraged (Blocks NLP) |

Why is **CC BY-NC (Non-Commercial)** discouraged in digital humanities?

1. Defining "commercial" is legally ambiguous—it often inadvertently blocks university libraries, non-profit academic publishers, and open-access repositories from mirroring your data;
2. It prevents commercial search engines and open-source AI models from indexing your scholarship (Creative Commons, 2026; Wilkinson et al., 2016).

Applying standard **CC BY 4.0** guarantees maximum dissemination while securing your legal right to scholarly attribution (Barzaghi et al., 2025).

**Vocabulary.** *CC BY 4.0* — Creative Commons Attribution 4.0 International license permitting free sharing and adaptation with credit. *Attribution requirement* — the legal obligation to cite the original authors and provide a link to the source edition. *Copyleft* — a licensing principle requiring derivative works to be released under the same license.

**Takeaway:** CC BY 4.0 is the gold standard for critical editions, maximizing global dissemination while guaranteeing proper scholarly citation.

---

## **17 Content**

**The CC0 1.0 Public Domain Dedication: Liberating Data, Tokens, and RDF Triples**

While creative prose requires attribution via CC BY, raw structured data—such as token lists, lemma mappings, collation matrices, and RDF knowledge triples—should be dedicated to the public domain under **Creative Commons Zero (CC0 1.0 Universal)** (Creative Commons, 2026; Wilkinson et al., 2016).

Under copyright law across most international jurisdictions (including Canada, the United States, and the European Union), **facts, data points, and mechanical historical observations are not copyrightable** (Feist Publications v. Rural Telephone Service Co., 1991). A 4th-century Greek manuscript reading is a historical fact, not modern creative intellectual property.

```xml
<!-- CC0 Declaration for Structured Datasets inside TEI Header -->
<availability status="free">
  <licence target="https://creativecommons.org/publicdomain/zero/1.0/">
    <p>To the extent possible under law, the editors have waived all copyright and
    related or neighboring rights to the raw token lists, morphosyntactic tags,
    collation matrices, and RDF graphs in this edition under CC0 1.0 Universal.</p>
  </licence>
</availability>
```

| Data Asset | Legal Status under CC0 | Reusability Benefit |
| --- | --- | --- |
| **Morphological Tags** | Public Domain Dedication | Can be ingested by CLTK or TreeTagger training sets |
| **Collation Matrices** | Public Domain Dedication | Can be fed into phylogenetic tree algorithms |
| **CIDOC-CRM Triples** | Public Domain Dedication | Can be merged into global LOD knowledge graphs (Wikidata) |
| **Coordinate Boxes** | Public Domain Dedication | Can be used to train computer vision OCR pipelines |

Dedicating data to CC0 eliminates "attribution stacking"—a catastrophic legal scenario where an algorithm combining datasets from 500 digital editions would be legally forced to print 500 separate attribution notices for every automated query (Wilkinson et al., 2016; Barzaghi et al., 2025).

**Vocabulary.** *CC0 1.0 Universal* — a legal tool that allows copyright owners to waive all copyright and dedicate their data to the worldwide public domain. *Attribution stacking* — the accumulation of burdensome legal attribution requirements when combining hundreds of independent datasets. *Non-copyrightability of facts* — the legal principle that factual and historical data cannot be copyrighted.

**Takeaway:** Dedicating structured tokens and RDF graphs to CC0 eliminates legal attribution stacking and maximizes Linked Open Data reusability.

---

## **18 Content**

**Open Source Software Licensing: MIT and GNU GPL-3.0 for Build Scripts and ODDs**

A digital scholarly edition is not merely a publication; it is also a software system. The Python collation scripts, ODD transformation pipelines, XSLT stylesheets, and Web Component interfaces that power your edition are software code (Sahle, 2016; Barzaghi et al., 2025).

To ensure that your technical labor benefits future scholars, code assets must be released under standard **Open Source Software (OSS) Licenses** (Open Source Initiative, 2026).

Two primary open-source licenses dominate digital humanities:

| Open Source License | License Philosophy | Permissions Granted | Requirements & Restrictions |
| --- | --- | --- | --- |
| **MIT License** | Permissive, minimalist | Free use, modification, distribution, sublicensing, commercial use | Requires preserving original copyright notice; zero warranties |
| **GNU GPL-3.0** | Strong copyleft | Free use, modification, distribution | Mandates that any derivative software must also be open source under GPL-3.0 |

```
// Standard MIT License Header for Python / ODD / XSLT Files
/*
 * Copyright (c) 2026 RELS 398 Digital Editing Studio
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction...
 */
```

For digital humanities build pipelines, the **MIT License** is strongly recommended because its simplicity allows other researchers to freely copy, adapt, and integrate your transformation scripts into their own university repositories without complex legal restrictions (Barzaghi et al., 2025).

**Vocabulary.** *MIT License* — a permissive open-source software license granting unrestricted rights to use, copy, modify, and distribute code. *GNU GPL-3.0* — a strong copyleft software license requiring all modified versions to remain open source. *Open Source Initiative (OSI)* — the international organization maintaining the formal open source definition.

**Takeaway:** Releasing build scripts and ODD stylesheets under the MIT Open Source License enables other scholars to freely adapt and reuse your computational pipelines.

---

## **19 Content**

**Formalizing Licensing Declarations in the TEI Header `<publicationStmt>`**

In Lesson 13.1, you introduced the basic `<publicationStmt>`. Today, we formalize the complete **multi-tiered licensing statement** using machine-actionable TEI P5 elements (TEI Consortium, 2026; Barzaghi et al., 2025).

Within `<publicationStmt>`, multiple `<licence>` elements are nested inside `<availability>`, each carrying a `@target` URI pointing to the formal legal deed:

```xml
<publicationStmt>
  <publisher>St. Francis Xavier University Digital Humanities Press</publisher>
  <pubPlace>Antigonish, Nova Scotia, Canada</pubPlace>
  <date when="2026-12-04">December 4, 2026</date>
  <idno type="DOI">10.5281/zenodo.1234567</idno>
  <idno type="CTS-URN">urn:cts:greekLit:tlg0031.tlg052.rels398-crit:2.1-2.12</idno>
  
  <availability status="restricted">
    <!-- Tier 1: Editorial Text, Translation, Commentary (CC BY 4.0) -->
    <licence target="https://creativecommons.org/licenses/by/4.0/">
      <p>The scholarly introduction, critical edition text, English translation,
      and commentary notes are licensed under a Creative Commons Attribution 4.0
      International License (CC BY 4.0).</p>
    </licence>

    <!-- Tier 2: Raw Tokens, Lemmas, Collation Data (CC0 1.0) -->
    <licence target="https://creativecommons.org/publicdomain/zero/1.0/">
      <p>All underlying structured data, token lists, alignment tables, and
      RDF assertions are dedicated to the public domain under CC0 1.0 Universal.</p>
    </licence>

    <!-- Tier 3: ODD Stylesheets and Build Code (MIT License) -->
    <licence target="https://opensource.org/licenses/MIT">
      <p>All transformation stylesheets (ODD/XSLT), Python collation scripts, and
      automated build pipelines are released under the MIT Open Source License.</p>
    </licence>
  </availability>
</publicationStmt>
```

| TEI Element | Attribute | Semantic Function |
| --- | --- | --- |
| `<availability>` | `@status="restricted"` | Indicates that use is governed by explicit license conditions |
| `<licence>` | `@target="https://..."` | Machine-actionable URI pointing to the authoritative legal license |
| `<p>` | Prose description | Human-readable explanation of which specific asset layer is governed |

Embedding machine-actionable license URIs enables automated search engines and data harvesters to verify the legal reusability of your edition without human intervention (Wilkinson et al., 2016; Barzaghi et al., 2025).

**Vocabulary.** `<licence>` — TEI element within `<availability>` documenting the legal terms under which a text is published. `@target` — attribute containing the canonical URL of the license deed. *Machine-actionable licensing* — expressing copyright terms in structured XML that software crawlers can parse automatically.

**Takeaway:** Embedding explicit `<licence>` elements with canonical URLs inside `<publicationStmt>` formalizes the multi-tiered licensing structure in machine-readable XML.

---

## **20 Content**

**The FAIR Guiding Principles for Textual Data: Findable, Accessible, Interoperable, Reusable**

In 2016, an international consortium of research institutions established the **FAIR Guiding Principles** for scientific and humanities data management (Wilkinson et al., 2016).

To achieve true scholarly impact, a digital edition must satisfy all four FAIR pillars:

| FAIR Pillar | Meaning in Textual Scholarship | Implementation in RELS 398 Edition |
| --- | --- | --- |
| **F — Findable** | Data must be assigned persistent identifiers and indexed in searchable repositories | Minting Zenodo DOIs and Canonical Text Service (CTS) URNs |
| **A — Accessible** | Data must be retrievable via open, standardized communication protocols | Hosting on public GitHub repositories, Zenodo, and open HTTP/HTTPS |
| **I — Interoperable** | Data must use formal, shared vocabularies and standard schemas | Encoding in standard TEI P5 XML, CIDOC-CRM RDF, and IIIF |
| **R — Reusable** | Data must possess rich provenance and unambiguous open licensing | Documenting `<revisionDesc>`, `<editorialDecl>`, and CC BY/CC0 licenses |

A digital edition that exists only on an obscure, private server behind a login screen violates every FAIR principle. By engineering your edition to be FAIR-compliant, you ensure that your philological scholarship remains discoverable and reusable by global research networks for generations (Wilkinson et al., 2016; Barzaghi et al., 2025).

**Vocabulary.** *FAIR Principles* — a set of international guidelines ensuring that digital research data is Findable, Accessible, Interoperable, and Reusable. *Data stewardship* — the long-term ethical and technical preservation of scholarly research outputs. *Open protocol* — a publicly available, non-proprietary communication standard (such as HTTP or REST).

**Takeaway:** The FAIR principles guarantee that digital editions are Findable via persistent IDs, Accessible via open protocols, Interoperable via TEI XML, and Reusable via open licensing.

---

## **21 Content**

**Persistent Identifiers (PIDs): DOIs, Handle.Net, and CTS URN Resolution**

In the digital world, web URLs are notoriously fragile. Academic studies show that over 50% of web links cited in scholarly literature break within ten years—a crisis known as **link rot** or **reference rot** (Klein et al., 2014).

To guarantee that your digital edition can be cited permanently, you must assign **Persistent Identifiers (PIDs)** (Klein et al., 2014; Wilkinson et al., 2016).

Two primary persistent identifier systems are employed in computational philology:

1. **Digital Object Identifiers (DOIs):** Managed by DataCite and Crossref, a DOI (e.g., `10.5281/zenodo.1234567`) provides a persistent, globally unique handle that resolves to the current web address of the publication package (Wilkinson et al., 2016).
2. **Canonical Text Service (CTS) URNs:** Developed by the Homer Multitext project, CTS URNs provide permanent, citation-based identifiers that reference specific texts, versions, and passage passages regardless of where the file is hosted (Smith & Blackwell, 2012; Topic 8).

| CTS URN Component | Segment Value in 1 Thess 2:7 | Ontological Level | Resolving Target |
| --- | --- | --- | --- |
| **Scheme Prefix** | `urn:cts` | Protocol standard | Canonical Text Service protocol |
| **Textgroup Namespace**| `greekLit` | Namespace | Ancient Greek literary corpus |
| **Author Identifier** | `tlg0031` | Author authority | Pauline Corpus / New Testament |
| **Work Identifier** | `tlg052` | Work authority | First Epistle to the Thessalonians |
| **Edition Identifier** | `rels398-crit` | Edition version | RELS 398 Digital Critical Edition |
| **Passage Pointer** | `2.7` | Passage node | Chapter 2, Verse 7 |

| Identifier System | Scope of Resolution | Example Identifier | Scholarly Function |
| --- | --- | --- | --- |
| **DOI (DataCite)** | Whole Edition Package | `10.5281/zenodo.1234567` | Permanent bibliographical citation of the released edition archive |
| **CTS URN** | Exact Verse / Passage | `urn:cts:greekLit:tlg0031.tlg052.rels398-crit:2.7` | Machine-actionable pointer resolving to an exact textual verse |
| **Pleiades URI** | Historical Place Entity | `https://pleiades.stoa.org/places/491741` | Permanent linked data identifier for *Thessalonica* |
| **VIAF Identifier** | Historical Person Entity | `http://viaf.org/viaf/100178828` | Permanent authority identifier for *Apostle Paul* |

**Vocabulary.** *Persistent Identifier (PID)* — a long-lasting digital reference that reliably points to a unique digital object even if its underlying web URL changes. *Link rot* — the phenomenon where hyperlinks cease to function because target web pages move or disappear. *Canonical Text Service (CTS) URN* — a URN syntax providing citation-based identification of textual passages.

**Takeaway:** Assigning DOIs and CTS URNs guarantees persistent, unalterable citation resolution, insulating your scholarship against link rot.

---

## **22 Content**

**Long-Term Data Preservation: Archiving Master Packages on Zenodo and Dataverse**

Publishing code on a GitHub repository is essential for collaboration, but **GitHub is not an archival repository**. Commercial platforms can change their terms of service, delete inactive repositories, or shut down entirely (Barzaghi et al., 2025; Wilkinson et al., 2016).

To guarantee long-term preservation for decades, academic institutions use **trusted digital repositories**, such as **Zenodo** (hosted by CERN) and **Harvard Dataverse** (Wilkinson et al., 2016).

When preparing an archival release package for Zenodo:

1. **Tag a Semantic Release in Git:** Tag your milestone commit with a formal version number (e.g., `git tag -a v1.0.0 -m "Release v1.0.0"`);
2. **Compile the Complete Multi-Modal Bundle:** Assemble the ZIP archive containing TEI XML, ODD, standalone HTML, PDF/A-3b, fonts, and licenses;
3. **Automated Zenodo Deposit:** Connect GitHub to Zenodo via OAuth webhooks. When a GitHub Release is published, Zenodo automatically archives a permanent snapshot of the repository, mints a citable DOI, and stores the data across redundant European server nodes (Wilkinson et al., 2016; Barzaghi et al., 2025).

| Zenodo Deposit Requirement | Included Package File | Verification Status |
| --- | --- | --- |
| **1. Master XML Source** | `data/edition.xml` | Fully validated against compiled Relax NG |
| **2. Compiled Schemas** | `build/edition.rng` + Schematron | Standalone schemas for independent validation |
| **3. Literate ODD Spec** | `odds/edition.odd` | Complete encoding model and behaviour rules |
| **4. Standalone HTML Bundle**| `dist/web/` | Double-clickable offline edition with Lunr search |
| **5. Archival Print Volume** | `dist/pdf/edition_archival.pdf` | ISO 19005-3 compliant PDF/A-3b volume |
| **6. Machine Metadata** | `CITATION.cff` & `LICENSE.md` | Automated citation format and license deeds |

Archiving on Zenodo guarantees that even if your university server goes offline tomorrow, your complete edition will remain permanently accessible to the global research community (Wilkinson et al., 2016).

**Vocabulary.** *Trusted digital repository* — an archival data storage institution committed to long-term data preservation, persistent indexing, and open access. *Zenodo* — an open-access general-purpose repository developed by CERN under the European Open Science Cloud (EOSC). *Semantic release snapshot* — an immutable, point-in-time archival copy of a software or data release.

**Takeaway:** Depositing versioned release bundles into trusted repositories like Zenodo mints citable DOIs and guarantees redundant, multi-decade preservation.

---

## **23 Content**

**Mitigating Software Obsolescence and Link Rot in Digital Humanities**

In digital humanities, the greatest threat to scholarship is not physical degradation (like rotting paper); it is **software obsolescence** and **technical dependency rot** (Sahle, 2016; Driscoll & Pierazzo, 2016).

Projects created in 2005 using Macromedia Flash, proprietary Java applets, or custom PHP 4 scripts are today completely dead and unopenable on modern computers. To ensure your digital edition survives fifty years from now, you must design for **graceful degradation** and **format durability** (Sahle, 2016; Turska et al., 2016).

| Fragile / Ephemeral Practice | Resilient / Archival Strategy | Preservation Rationale |
| --- | --- | --- |
| Storing text in MySQL / relational tables | Storing text in pure TEI P5 XML | XML is plain-text UTF-8; readable without database software |
| Complex server-side web frameworks | Standalone, static HTML5 + Web Components | Static HTML opens in any browser without server dependencies |
| Dynamic vector graphics rendered via Flash | Scalable Vector Graphics (SVG) | SVG is an open W3C XML standard supported natively |
| Proprietary binary image formats | IIIF + standard uncompressed TIFF / WebP | Open international standard backed by global libraries |
| Unversioned local scripts | Git version control + Docker container | Docker preserves the exact execution environment |

By isolating your scholarship in human-readable plain text (TEI XML) and compiling to open web standards (HTML5/SVG/PDF/A), you ensure that future scholars can read your edition even if every software tool used today becomes obsolete (Sahle, 2016; Wilkinson et al., 2016).

**Vocabulary.** *Software obsolescence* — the process whereby software tools, formats, or operating systems become unsupported and unusable. *Graceful degradation* — the ability of a system to maintain core functionality even when advanced features fail. *Plain-text durability* — the indefinite readability of ASCII and UTF-8 encoded text without specialized decoding software.

**Takeaway:** Grounding your edition in plain-text TEI XML, static HTML5, and open standards protects your scholarship against software obsolescence.

---

## **24 Content**

**Assembling the 10-Layer Digital Edition Portfolio Architecture**

Over the past fourteen weeks, you have methodically constructed all ten intellectual and technical layers of a professional Digital Scholarly Edition (Sahle, 2016; Pierazzo, 2016).

Today, we assemble these ten layers into a unified **Digital Edition Portfolio**:

| Portfolio Layer Number | Editorial & Computational Layer | Primary Technologies & Standards | Core Scholarly Contribution |
| --- | --- | --- | --- |
| **Layer 10** | Multi-Modal Publishing Packages | TEI Processing Model, CSS Paged Media, WeasyPrint | Web, standalone HTML, and PDF/A-3b print volumes |
| **Layer 9** | Commentary Knowledge Graphs | `<standOff>`, CTS URNs, Pleiades, VIAF, CiTO | Multi-tier historical, intertextual notes in LOD |
| **Layer 8** | Stratified Translation Models | Leipzig Glossing Rules, CTS passage alignment | Aligned morphological glosses and critical English text |
| **Layer 7** | Morphosyntactic Annotation | `<w>`, `@lemma`, `@pos`, CLTK parsing | Lemmatized tokens and morphosyntactic tagging |
| **Layer 6** | Critical Apparatus Modeling | Parallel Segmentation (`<app>`, `<lem>`, `<rdg>`) | Critical text constitution and variant apparatus |
| **Layer 5** | Algorithmic Collation | CollateX, dynamic programming, variant graphs | Automated alignment matrix across all four witnesses |
| **Layer 4** | Historical Normalization | `<choice>`, `<orig>`, `<reg>` | Dual diplomatic and regularized lexical views |
| **Layer 3** | Ground-Truth Transcription | `<lb>`, `<del>`, `<add>`, `<abbr>`, *nomina sacra* | Paleographical fidelity to manuscript ink |
| **Layer 2** | Digital Facsimile Integration | IIIF Image API, OpenSeadragon, `@facs` | High-resolution deep-zoom manuscript folios |
| **Layer 1** | Codicological Metadata | `<msDesc>`, `<physDesc>`, repository shelfmarks | Physical support, quire structure, hand analysis |

Each layer builds upon the foundation beneath it: codicological metadata grounds the physical manuscript images; diplomatic markup transcribes the ink; normalization aligns spelling; collation reveals variants; the apparatus formalizes editorial decisions; morphological tagging parses syntax; commentary enriches context; and the processing model publishes the whole into multi-modal packages (Sahle, 2016; Pierazzo, 2016).

In the remaining sections, we review the synthesis of these layers and execute the final Quality Assurance audit.

**Vocabulary.** *10-layer portfolio architecture* — the complete, integrated hierarchy of philological, linguistic, codicological, and computational data forming a digital scholarly edition. *Vertical integration* — the seamless flow of data from base codicology up through the published interface.

**Takeaway:** The 10-layer portfolio architecture integrates codicology, facsimiles, transcriptions, normalizations, collations, apparatuses, morphology, translations, commentaries, and publication pipelines into an inseparable whole.

---

## **25 Content**

**Layer 1–4 Integration: Codicology, Facsimiles, Transcriptions, and Normalizations**

The foundation of your digital edition connects the material reality of ancient manuscripts to digital transcriptions:

#### 25.1 Layer 1: Codicological Metadata (`<msDesc>`)

- Formulate complete descriptions of all four witnesses (Codex Sinaiticus $\aleph$, Codex Vaticanus $B$, Codex Alexandrinus $A$, Codex Ephraemi Rescriptus $C$);
- Document shelfmarks, holding repositories, quire structures, dimensions, scribal hands, and historical provenance in `<msDesc>` (Topic 2; Topic 13.1).

#### 25.2 Layer 2: IIIF Digital Facsimiles (`@facs`)

- Bind page milestones (`<pb>`) and surface coordinates (`<surface>`) to high-resolution IIIF image manifests;
- Ensure deep-zoom panning and canvas navigation synchronize with text scrolling (Topic 3; Topic 13.2).

#### 25.3 Layer 3: Diplomatic Ground-Truth Transcription

- Record the exact paleographical realities of the manuscripts: line breaks (`<lb>`), scribal deletions (`<del>`), additions (`<add>`), abbreviations, and *nomina sacra* (Topic 4; Topic 5).

#### 25.4 Layer 4: Orthographic Normalization (`<choice>`)

- Wrap phonetic iotacisms, movable nus, and non-standard uncial spellings in `<choice><orig>...</orig><reg>...</reg></choice>`, enabling dual diplomatic and regularized views (Topic 6).

| Foundation Layer | Key TEI Elements | Primary Verification Milestone |
| --- | --- | --- |
| **Layer 1: Codicology** | `<msDesc>`, `<physDesc>`, `<handDesc>` | Complete repository shelfmarks and physical quire structures |
| **Layer 2: Facsimiles** | `<pb facs="...">`, `<surface>` | IIIF canvas URIs resolve to high-resolution images |
| **Layer 3: Diplomatic** | `<lb>`, `<del>`, `<add>`, `<abbr>` | Verbatim character-for-character reproduction of manuscript ink |
| **Layer 4: Normalization**| `<choice>`, `<orig>`, `<reg>` | Clean separation of historical spelling from dictionary headwords |

**Vocabulary.** *Diplomatic fidelity* — the precise, unregularized recording of physical manuscript text. *Surface coordinate binding* — linking XML text elements directly to $(x, y, w, h)$ bounding boxes on a digital facsimile image.

**Takeaway:** Layers 1–4 establish the material and paleographical foundation, connecting codicological metadata, IIIF facsimiles, diplomatic transcriptions, and normalized spellings.

---

## **26 Content**

**Layer 5–8 Integration: Collations, Apparatuses, Morphosyntax, and Translations**

The analytical engine of your digital edition performs computational collation, critical apparatus modeling, linguistic parsing, and translation:

#### 26.1 Layer 5: Algorithmic Collation (CollateX)

- Execute Python collation scripts using CollateX to align the four witnesses into a mathematical variant graph and alignment table (Topic 14).

#### 26.2 Layer 6: Parallel Segmentation Critical Apparatus (`<app>`)

- Encode variation units using parallel segmentation (`<app><lem wit="...">...<rdg wit="...">...</app>`);
- Adjudicate disputed variants using stemmatic authority, *lectio difficilior potior*, and *lectio brevior* (Topic 15; Topic 13.1).

#### 26.3 Layer 7: Morphosyntactic Parsing and Lemmatization

- Tokenize words into `<w>` elements carrying `@lemma`, `@pos`, and Leipzig grammatical tags, processed via the Classical Language Toolkit (CLTK) (Topic 8; Topic 10).

#### 26.4 Layer 8: Stratified Translation and Interlinear Glossing

- Construct the four-line interlinear gloss (surface, lemma, POS, English gloss) and author a formal-equivalent scholarly translation linked via CTS URNs (Topic 11).

| Analytical Layer | Key TEI Markup | Primary Verification Milestone |
| --- | --- | --- |
| **Layer 5: Collation** | CollateX JSON / Alignment Tables | Mathematical identification of all variation points |
| **Layer 6: Apparatus** | `<app>`, `<lem>`, `<rdg>`, `<listWit>` | Explicit editorial constitution of the critical text |
| **Layer 7: Morphology** | `<w lemma="..." pos="...">` | 100% token lemmatization and morphosyntactic tagging |
| **Layer 8: Translation** | `<interlinear>`, `<translation>` | Four-line aligned Leipzig gloss and critical English translation |

**Vocabulary.** *Algorithmic alignment* — using dynamic programming algorithms (Needleman-Wunsch) to align divergent manuscript streams. *Morphosyntactic tagging* — assigning grammatical part-of-speech and inflectional codes to individual words.

**Takeaway:** Layers 5–8 execute the philological analysis, generating automated collations, critical apparatuses, linguistic parses, and stratified translations.

---

## **27 Content**

**Layer 9–10 Integration: Commentary Knowledge Graphs and Multi-Modal Publishing Packages**

The final layers of the edition enrich the text with Linked Open Data commentary and compile all assets into multi-modal publication deliverables:

#### 27.1 Layer 9: Interactive Stand-Off Commentary Knowledge Graphs

- Author scholarly notes inside `<standOff>` categorized into philological, historical, intertextual, and structural tiers;
- Anchor notes to base text tokens using CTS URNs and target Pleiades, VIAF, and CiTO ontological URIs (Topic 12).

#### 27.2 Layer 10: Multi-Modal Publication Packages

- Configure ODD Processing Models (`<model>`, `@behaviour`, `@predicate`) to automate rendering across web popovers and print footnotes (Topic 13.2);
- Compile the interactive web portal, standalone offline HTML bundle (EVT), and archival print-ready PDF (PDF/A-3b) (Topic 13.3).

| Enrichment & Output Layer | Technical Mechanism | Primary Deliverable |
| --- | --- | --- |
| **Layer 9: Commentary** | `<standOff>`, CTS URNs, Linked Open Data | Semantic knowledge graph linking text to Pleiades / VIAF / CiTO |
| **Layer 10: Publication** | ODD Processing Model, CSS Paged Media | Interactive Web Portal, Static HTML Bundle, Archival PDF/A-3b |

Integrating these final layers transforms your structured XML repository into a globally connected, fully published digital critical edition (Sahle, 2016; Barzaghi et al., 2025).

**Vocabulary.** *Linked Open Data (LOD)* — publishing structured data using URIs and RDF to connect information across global research databases. *Multi-modal deliverable suite* — the complete set of generated web, standalone HTML, and print PDF artifacts.

**Takeaway:** Layers 9–10 complete the edition, integrating Linked Open Data commentary graphs and compiling multi-modal publishing packages.

---

## **28 Content**

**The Final Quality Assurance (QA) Checklist: 12 Gates to Publication**

Before publishing your digital critical edition to Zenodo and GitHub, you must execute the **12-Gate Quality Assurance Checklist**. A defect at any gate halts publication until corrected (Driscoll & Pierazzo, 2016; Barzaghi et al., 2025).

| Gate # | Quality Assurance Gate | Verification Action | Pass / Fail Criterion |
| --- | --- | --- | --- |
| **Gate 1** | **XML Well-Formedness** | Run `xmllint --noout data/*.xml` | Zero XML syntax or unclosed tag errors |
| **Gate 2** | **ODD Schema Validation** | Validate XML against compiled Relax NG (`.rng`) | Zero schema invalidity errors in VS Code and validation pipelines |
| **Gate 3** | **Content Linter** | Run `python3 scripts/lint_lesson_content.py` | Exactly 0 lint issues across all course lessons |
| **Gate 4** | **Pointer Integrity** | Verify all `@wit` values match `<listWit>` IDs | Zero broken or unresolved `#wit-` pointers |
| **Gate 5** | **Apparatus Alignment** | Check `<lem>` text matches base reading text verbatim | Zero discrepancies between lemma and reading view |
| **Gate 6** | **Stemma Consistency** | Check shared errors against stemma branches | Sibling manuscripts share confirmed conjunctive errors |
| **Gate 7** | **Commentary Anchors** | Check all stand-off note CTS URN target pointers | Zero dangling or invalid token ID references |
| **Gate 8** | **LOD Link Health** | Verify all Pleiades / VIAF / DOI URIs resolve | Zero 404 broken links in `<publicationStmt>` or notes |
| **Gate 9** | **Font Embedding** | Check Cardo and Noto Serif WOFF2 fonts load | Polytonic Greek renders with zero missing glyphs |
| **Gate 10**| **Offline Package** | Open `dist/web/index.html` locally in browser | Web edition and Lunr search function 100% offline |
| **Gate 11**| **PDF/A Compliance** | Validate PDF with VeraPDF / WeasyPrint validator | 100% compliance with ISO 19005-3 (PDF/A-3b) |
| **Gate 12**| **Licensing Complete** | Verify CC BY 4.0, CC0, and MIT statements | Multi-tiered licensing explicitly declared in header |

Document the results of your audit in `FINAL_QA_AUDIT.md`. Once all 12 gates are certified green, your edition is cleared for release (Barzaghi et al., 2025).

**Vocabulary.** *Quality Assurance (QA) gate* — a mandatory verification checkpoint that must pass before software or research data is published. *Pointer integrity* — the programmatic verification that all internal XML ID references resolve successfully. *VeraPDF* — an industry-standard open-source validator for PDF/A compliance.

**Takeaway:** The 12-Gate QA Checklist verifies XML validity, schema compliance, pointer integrity, font embedding, offline functionality, and PDF/A standards prior to release.

---

## **29 Content**

**Post-Publication Life Cycle: Community Feedback, Errata, and Versioned Releases**

In the traditional print world, publishing a book was a final, immutable event. In digital scholarship, publication marks the beginning of an ongoing **scholarly life cycle** (Sahle, 2016; Pierazzo, 2016).

As other scholars and students read your edition, they will discover new evidence: an overlooked scribal correction in Codex Ephraemi, a new papyrus fragment published in *Oxyrhynchus Papyri*, or an improved syntactical parse for a difficult verse. A digital scholarly edition must maintain a formal mechanism for incorporating community feedback and publishing **versioned releases** (Barzaghi et al., 2025; Topic 1).

| Life Cycle Stage | Operational Action | Computational Mechanism |
| --- | --- | --- |
| **1. Reader Feedback** | Reader submits issue on GitHub | GitHub Issues (e.g., `#42: Typo in 1 Thess 2:8 lem`) |
| **2. Editorial Triage** | Editorial board reviews and opens branch | `git checkout -b fix/issue-42-lemma-typo` |
| **3. XML Revision & QA**| Edits XML, updates `<revisionDesc>`, runs QA | `xmllint` + Relax NG + `lint_lesson_content.py` |
| **4. Versioned Release**| Merges PR, bumps semantic version tag | `git tag -a v1.0.1 -m "Patch release v1.0.1"` |
| **5. Automated Archive**| Zenodo webhook archives snapshot | Mints versioned sub-DOI linked to master concept DOI |

| Semantic Version | Change Category | Example Trigger in Digital Edition |
| --- | --- | --- |
| **Patch Release (v1.0.1)** | Minor errata, typographical fixes | Correcting a misspelled English gloss or fixing a broken Pleiades link |
| **Minor Release (v1.1.0)** | New scholarly content, added witnesses | Collating an additional minuscules witness or adding a new commentary tier |
| **Major Release (v2.0.0)** | Major structural or theoretical revision | Changing the editorial constitution from eclectic to documentary Bédierism |

Maintaining an active, version-controlled repository ensures that your scholarship remains an enduring, reliable foundation for future philological research (Barzaghi et al., 2025; Wilkinson et al., 2016).

**Vocabulary.** *Scholarly life cycle* — the ongoing process of maintaining, correcting, and updating a digital edition post-publication. *Semantic versioning* — standard version numbering scheme (`MAJOR.MINOR.PATCH`). *Zenodo versioning* — Zenodo's capability to maintain a master DOI representing all versions while assigning individual DOIs to each specific release snapshot.

**Takeaway:** Post-publication maintenance uses GitHub Issues, semantic versioning, and automated Zenodo archiving to integrate scholarly feedback and publish versioned releases.

---

## **30 Content**

**Synthesis & Epilogue: The Transformed Philologist and the Future of Digital Scholarly Editing**

Over the course of this semester in RELS 398 / ENGL 398, you have accomplished a profound transformation: you have evolved from a reader of static printed texts into a **computational philologist and digital editor** (Sahle, 2016; Pierazzo, 2016).

You have mastered the complete arc of textual scholarship:

1. **Codicology & Facsimiles:** Grounding texts in physical manuscript materiality and high-resolution IIIF canvases (Topics 2–3);
2. **Diplomatic & Normalized Markup:** Mastering the delicate boundary between historical manuscript reality and standardized lexical forms (Topics 4–6);
3. **Computational Collation & Stemmatology:** Aligning witnesses via CollateX, constructing stemmata codicum, and applying the CBGM to open traditions (Topics 7–8; Topic 13.1);
4. **Linguistic Parsing & Translation:** Tokenizing syntax via CLTK and authoring Leipzig-aligned interlinear glosses (Topics 9–11);
5. **Commentary Knowledge Graphs:** Structuring stand-off annotations with Linked Open Data ontologies (Topic 12);
6. **Multi-Modal Publishing & Stewardship:** Configuring the TEI Processing Model in ODD, compiling web/PDF packages, and releasing under CC BY/CC0/MIT open access standards (Topic 13).

As Patrick Sahle and Elena Pierazzo have shown, a digital scholarly edition is not merely a computerized version of a paper book. It is a new paradigm of knowledge representation: an open, transparent, reproducible, and multi-modal research environment that honors the historical complexity of our shared textual heritage (Sahle, 2016; Pierazzo, 2016).

Congratulations on completing your digital scholarly edition!

**Takeaway:** Digital scholarly editing transforms philology by uniting deep manuscript knowledge, rigorous computational modeling, and multi-modal open stewardship into an enduring digital edition.

---

## References

Barzaghi, S., Palmero Aprosio, A., Paolucci, F., & Peroni, S. (2025). The semantic digital edition of Aldo Moro's writings: A workflow supporting data sharing and replicability. *ACM Journal on Computing and Cultural Heritage, 18*(2), Article 24. https://doi.org/10.1145/3725534

Berti, M. (2026). Annotating the ancient world: Critical annotations and digital editions. In *Charting the Future of Historical Humanities* (pp. 45–68). Brepols. https://doi.org/10.1484/M.LECTIO-EB.5.151800

Buzzoni, M. (2016). A protocol for scholarly digital editions? The Italian point of view. In M. J. Driscoll & E. Pierazzo (Eds.), *Digital Scholarly Editing: Theories and Practices* (pp. 89–108). Open Book Publishers. https://doi.org/10.11647/OBP.0095.05

Coombs, J. H., Renear, A. H., & DeRose, S. J. (1987). Markup systems and the future of scholarly text processing. *Communications of the ACM, 30*(11), 933–947. https://doi.org/10.1145/32206.32209

Creative Commons. (2026). *About the CC licenses*. Creative Commons. https://creativecommons.org/about/cclicenses/

Driscoll, M. J., & Pierazzo, E. (Eds.). (2016). *Digital scholarly editing: Theories and practices*. Open Book Publishers. https://doi.org/10.11647/OBP.0095

Feist Publications, Inc., v. Rural Telephone Service Co., 499 U.S. 340 (1991). https://supreme.justia.com/cases/federal/us/499/340/

Fischer, F. (2020). 6.3 Representing the critical text. In P. Roelli (Ed.), *Handbook of Stemmatology: History, Methodology, Digital Approaches* (pp. 405–424). De Gruyter. https://doi.org/10.1515/9783110684384-006

International Organization for Standardization. (2020). *Document management — Electronic document file format for long-term preservation — Part 3: Use of ISO 32000-1 with support for embedded files (PDF/A-3)* (ISO Standard No. 19005-3:2012/Amd 1:2020). ISO. https://www.iso.org/standard/76508.html

Klein, M., Van de Sompel, H., Sanderson, R., Shankar, H., Balakireva, L., Zhou, K., & Tobin, R. (2014). Scholarly context not found: One in five articles suffers from reference rot. *PLOS ONE, 9*(12), Article e115253. https://doi.org/10.1371/journal.pone.0115253

Maas, P. (1958). *Textual criticism* (B. Flower, Trans.). Oxford University Press.

Open Source Initiative. (2026). *The Open Source Definition*. Open Source Initiative. https://opensource.org/osd

Pierazzo, E. (2015). *Digital scholarly editing: Theories, models and methods*. Ashgate Publishing / Routledge. https://doi.org/10.4324/9781315577227

Pierazzo, E. (2016). Modelling digital scholarly editions: 'In the making'. In M. J. Driscoll & E. Pierazzo (Eds.), *Digital Scholarly Editing: Theories and Practices* (pp. 61–77). Open Book Publishers. https://doi.org/10.11647/OBP.0095.04

Renear, A. H. (2004). Text encoding. In S. Schreibman, R. Siemens, & J. Unsworth (Eds.), *A Companion to Digital Humanities* (pp. 218–239). Blackwell. https://doi.org/10.1002/9780470999875.ch17

Sahle, P. (2016). What is a scholarly digital edition? In M. J. Driscoll & E. Pierazzo (Eds.), *Digital Scholarly Editing: Theories and Practices* (pp. 19–39). Open Book Publishers. https://doi.org/10.11647/OBP.0095.02

Smith, N., & Blackwell, C. (2012). *The CITE architecture: Canonical Text Services*. Center for Hellenic Studies, Harvard University. http://www.homermultitext.org/hmt-doc/cite/texts/ctsom2.html

Stadler, P., Illetschko, M., & Veit, J. (2016). Towards a digital edition of the Carl Maria von Weber complete works. *International Journal of Humanities and Arts Computing, 10*(1), 67–85. https://doi.org/10.3366/ijhac.2016.0160

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and interchange* (Version 4.8.1). TEI Consortium. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/

Turska, M., Cummings, J., & Rahtz, S. (2016). Challenging the myth of presentation in digital editions: The TEI Processing Model. *Journal of the Text Encoding Initiative, 9*, 1–22. https://doi.org/10.4000/jtei.1467

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., ... & Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data, 3*, Article 160018. https://doi.org/10.1038/sdata.2016.18

World Wide Web Consortium. (2026). *CSS Paged Media Module Level 3* (W3C Working Draft). World Wide Web Consortium. https://www.w3.org/TR/css-page-3/
