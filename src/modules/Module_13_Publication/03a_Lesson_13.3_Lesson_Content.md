# Lesson 13.3 — Multi-Modal Publishing, Minimal Computing, and Long-Term Archiving

*RELS 398 / ENGL 398 · Topic 13: Publication · Meeting #36 (Fri Dec 4)*

***Studio and publication assembly week (no three-step cycle).** Today you complete our capstone publication studio, compiling your TEI XML master into responsive web applications, standalone offline packages, and print-ready PDF volumes, while establishing multi-tiered open access licensing and FAIR archiving with Zenodo DOIs and GitHub Releases.*

---

## **01 Content**

**The Multi-Modal Vision: Publishing Beyond a Single Screen**

Welcome to our final class meeting of the semester. Today we complete our capstone publication studio. Over the past twelve weeks, you built rich TEI XML files. You transcribed handwriting, normalized spellings, linked historical entities, and authored commentary notes.

Now your work must reach the world. A major trap in digital humanities is locking your edition inside a single website. If that website goes offline, your research disappears.

A true digital scholarly edition is **multi-modal**. This means it compiles into several distinct formats from one master XML file. Different readers need different reading environments:

1. An **interactive website** for online research with image zoom and popups;
2. A **standalone offline package** that runs on a laptop without internet access;
3. A **print-ready PDF** for library archiving, physical reading, and formal citation.

Because all these formats compile from the same TEI source, you maintain total consistency. You never copy and paste text between separate files.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Publication Format</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Technical Medium</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Primary Advantage</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Best Audience</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Interactive Web App</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">HTML5, CSS3, JavaScript</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Dynamic facsimiles, search, and popup commentary</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Online scholars and students</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Standalone Offline Zip</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Static HTML and Lunr.js</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Runs anywhere without an internet connection</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Field researchers and museum kiosks</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Print-Ready PDF Codex</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">CSS Paged Media / Typst</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Fixed page numbers and bottom footnotes</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Academic libraries and book readers</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Multi-Modal Publishing* — compiling multiple distinct media formats like web, offline zip, and print PDF from one master XML source. *Single Source of Truth* — maintaining one canonical master dataset to ensure all derived publications remain identical. *Reading Environment* — the physical or digital context in which an audience reads and engages with a text.

**Takeaway:** A digital scholarly edition must compile into interactive web, offline standalone, and print-ready formats from a single master TEI XML file.

---

## **02 Content**

**Medium-Specific Affordances: Screen vs. Page vs. Raw Data**

To publish across multiple media, you must understand **affordances**. An affordance is what a specific medium allows a user to do. Different media have distinct strengths and limitations.

A digital screen is fluid, interactive, and boundless. It allows users to zoom into high-resolution manuscript scans, click on popup notes, and toggle between diplomatic and normalized spelling. However, web pages can be distracting and require battery power or internet access.

A physical printed page is fixed, permanent, and tactile. It has clear page numbers, stable margins, and footnotes at the bottom of the page. It never suffers from dead batteries or broken web links. However, it cannot play audio, show deep-zoom scans, or toggle views.

Raw TEI XML is machine-actionable data. Computers can search it, index it, and analyze it with computational tools. However, human readers cannot read raw XML comfortably without a rendering interface. A skilled editor designs formats that play to the strengths of each medium.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Feature</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Interactive Web Screen</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Printed Book Page (PDF)</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Raw TEI XML Data</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Spatial Layout</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Continuous vertical scroll or split panes</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Fixed two-dimensional page grid</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Hierarchical tree structure</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Commentary Placement</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Interactive popups and sidebar cards</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Numbered footnotes at page bottom</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Standoff note tags with target IDs</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Citation Anchor</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Web URI and HTML element IDs</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Fixed page number and line number</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">XML xml:id and XPath expression</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Affordance* — the unique functional capabilities and reading behaviors provided by a specific medium. *Spatial Layout* — the physical or digital organization of text and images across a display surface. *Citation Anchor* — the fixed reference point used by scholars to cite a specific sentence or passage.

**Takeaway:** Understanding medium-specific affordances allows editors to optimize commentary, layouts, and citations for screens, printed pages, and data streams.

---

## **03 Content**

**What is Minimal Computing in Digital Humanities?**

In recent years, digital humanities scholars have embraced **minimal computing**. Minimal computing is a design philosophy that asks: what is the simplest technology that can accomplish our scholarly goals?

Many early digital humanities projects used complicated technology. They required database servers, custom web applications, and expensive cloud hosting. When project grants ran out after three years, nobody could pay the hosting bills. The servers were shut down, and decades of scholarly research disappeared.

Minimal computing avoids this trap. It emphasizes:

1. **Static files** (plain HTML, CSS, and JS) instead of live database servers;
2. **Open formats** (TEI XML, Markdown, plain text) that any computer can read;
3. **Low infrastructure demands** that work on slow internet connections;
4. **Zero ongoing hosting costs** by using free platforms like GitHub Pages.

A minimal computing edition does not require a full-time system administrator. It runs anywhere and survives for decades.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Dimension</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Complex Database Architecture</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Minimal Computing Architecture</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Server Requirement</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Requires live SQL/NoSQL database and server runtime</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Plain web server serving static files</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Maintenance Cost</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">High; monthly server hosting and regular security patches</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Zero; free hosting on GitHub Pages or institutional storage</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Preservation Risk</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">High; site breaks when server software updates</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Very low; plain HTML files remain readable for decades</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Minimal Computing* — a philosophy favoring simple, sustainable, and durable technologies with low maintenance demands. *Static Files* — web files like HTML and CSS that are delivered to the browser exactly as stored, without server processing. *Infrastructure Fragility* — the vulnerability of complex digital projects to server obsolescence and funding loss.

**Takeaway:** Minimal computing ensures digital editions survive for decades by using simple static files that require zero server maintenance or hosting budgets.

---

## **04 Content**

**The Fragility of the Digital Archive**

Print books are remarkably durable. A printed book from 1752 or 1791 can sit on a library shelf for centuries. As long as the paper stays dry, anyone who speaks the language can open it and read it.

Digital files are far more fragile. Digital humanities projects face several severe preservation hazards:

1. **Link Rot:** Web addresses change over time. Studies show that over half of web links in academic papers break within ten years.
2. **Software Obsolescence:** Software tools and plugins disappear. Flash animations, custom browser extensions, and obsolete server scripts stop functioning.
3. **Format Decay:** Proprietary word processor files from the 1990s often cannot be opened by modern software without data loss.

Scholarly editors must guard against these threats. We use open standards like TEI XML because XML is plain text that any operating system can read. We avoid closed, proprietary tools that lock data away behind commercial licenses.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Preservation Hazard</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Cause of Failure</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Digital Humanities Solution</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Link Rot</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Domain changes and site reorganizations break URLs</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Minting persistent DOIs through Zenodo</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Database Rot</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Live databases crash when hosting contracts expire</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Compiling static HTML and storing master XML in git</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Format Obsolescence</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Proprietary software files become unreadable</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Using open plain-text TEI XML and PDF/A standards</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Link Rot* — the gradual process by which web links break and point to missing 404 pages over time. *Format Obsolescence* — the inability of modern computers to read outdated, proprietary file formats. *Plain-Text Preservation* — storing data as unformatted text files to ensure universal readability across all future computer systems.

**Takeaway:** Digital editions protect against link rot and format obsolescence by using open plain-text TEI XML and permanent digital identifiers.

---

## **05 Content**

**Compiling Standalone Offline HTML Packages**

One of the most practical deliverables of a digital edition is a **standalone offline package**. An offline package is a self-contained folder containing everything needed to run your edition without an internet connection.

It bundles together:

1. The compiled `index.html` file containing the document text and paratexts;
2. The `style.css` stylesheet providing typography and layouts;
3. A local `images/` directory containing optimized manuscript facsimiles;
4. Lightweight JavaScript files that provide interactive toggles and note popups.

You can compress this entire directory into a single `.zip` file. A researcher can download the zip, extract it onto their laptop, and double-click `index.html`. The complete edition opens instantly in their web browser.

Offline packages are invaluable for researchers traveling to archives with poor Wi-Fi, for classroom teaching without network lags, and for deposit in university library repositories.

```text
edition_offline_package/
  index.html          # Standalone reading interface
  style.css           # Local typography and layout rules
  app.js              # Lightweight offline interaction scripts
  images/             # Optimized manuscript scans and seals
    page_01.jpg
    seal_01.png
  README.txt          # Quick-start instructions for scholars
```

**Vocabulary.** *Standalone Offline Package* — a self-contained folder of HTML, CSS, JS, and image assets that runs locally without internet connectivity. *Asset Bundling* — gathering all referenced images, styles, and scripts into a local directory structure. *Zero-Dependency Web Page* — an HTML document that requires no external content delivery networks (CDNs) to display properly.

**Takeaway:** Standalone offline packages bundle HTML, CSS, scripts, and images into portable zip files that run anywhere without internet access.

---

## **06 Content**

**Offline Client-Side Search with Lunr.js**

A major advantage of digital editions is full-text search. Readers want to search for names, places, and historical terms across your witness. However, traditional search engines require a live database server running in the cloud.

To maintain minimal computing principles, digital humanists use **client-side search**. A popular tool for this is **Lunr.js**. Lunr.js is a lightweight JavaScript search library that runs entirely inside the reader's browser.

Here is how it works:

1. During the build process, a script parses your TEI XML and extracts all words, sentences, and notes;
2. The script compiles this text into a compact JSON search index;
3. When a reader types a word into your edition's search box, Lunr.js searches the pre-built index in memory;
4. Search results appear in less than ten milliseconds, with sentence excerpts and clickable links.

Because the search runs inside the browser, it works perfectly offline. It requires zero server processing and costs nothing to run.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Search Architecture</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Where Search Executes</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Server Requirement</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Offline Capability</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Server-Side Search (SQL/Elastic)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Remote cloud server database</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Requires live active server process</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Fails completely without internet</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Client-Side Search (Lunr.js)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Inside the user's web browser</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Zero; static JSON index file</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Functions 100% offline anywhere</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Client-Side Search* — executing search queries directly inside the user's browser using JavaScript rather than on a remote server. *Lunr.js* — a lightweight JavaScript search library designed for static websites. *Search Index* — a pre-computed data structure mapping words to their locations in a text to enable instant lookups.

**Takeaway:** Client-side search tools like Lunr.js enable instant full-text search inside the browser without requiring a database server or internet connection.

---

## **07 Content**

**Print-Ready PDF Publishing with CSS Paged Media and Typst**

While web interfaces are dynamic, academic libraries and philologists still require printed codex volumes. A digital scholarly edition must be able to compile into a formal, beautifully typeset PDF.

Historically, converting XML to print required mastering LaTeX, a powerful but difficult typesetting language. Today, modern digital publishing provides streamlined alternatives:

1. **CSS Paged Media:** Uses standard CSS rules with special paged extensions (`@page`, `@top-left`, `marks: crop`). Tools like Weasyprint convert your HTML and CSS into print PDFs.
2. **Typst:** A modern, lightning-fast markup and typesetting system. Typst combines the typographic power of LaTeX with clean, readable syntax.
3. **Pandoc:** An open-source document converter that transforms Markdown and XML into PDF via Typst or LaTeX.

These modern tools automate page layout. They calculate page breaks, generate running headers, create tables of contents, and place numbered footnotes cleanly at the bottom of the page.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Typesetting Tool</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Syntax Style</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Compilation Speed</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Primary Strength</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Typst</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Modern clean markup</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Instantaneous (&lt; 1 second)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Beautiful default typography and fast compilation</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">CSS Paged Media (Weasyprint)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Standard CSS with @page rules</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Fast (2&ndash;5 seconds)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Reuses existing HTML and CSS web styles directly</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">LaTeX (reledmac)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Dense macro commands</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Slow (10&ndash;30 seconds)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Complex multi-tiered classical apparatus layouts</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *CSS Paged Media* — W3C specifications that extend CSS to handle pagination, margins, page numbers, and running headers for print. *Typst* — a modern, fast typesetting system designed as an accessible alternative to LaTeX. *Running Header* — small header text repeated at the top of printed pages showing chapter titles and page numbers.

**Takeaway:** Modern tools like Typst and CSS Paged Media convert TEI XML into elegant, print-ready PDF volumes with automatic page numbering and running headers.

---

## **08 Content**

**Structuring the Print Critical Apparatus**

When preparing a printed edition, commentary notes must be adapted to the physical page. On a website, commentary can hide inside clickable popups. On a printed page, there is no clicking. Every note must be visible on the paper.

In print editions, commentary is presented as a **critical apparatus**. The apparatus is organized into numbered footnotes at the bottom of the page or in endnotes at the end of the text.

Footnotes must be formatted with scholarly rigor:

1. Each note begins with a superscript number matching the anchor in the text;
2. The note quotes the referenced word or lemma in bold or italics;
3. A closing square bracket (`]`) separates the lemma from the critical commentary;
4. Concise philological definitions, historical facts, and bibliographic citations follow.

This standard layout allows scholars to consult commentary instantly while reading without flipping pages.

```
---------------------------------------------------------------------
1 truckhouse] A British colonial trading post established by Governor
Hopson in 1752, where Mi'kmaq exchanged furs for British goods at
fixed government rates. See Nova Scotia Archives RG 1 vol 430.
```

**Vocabulary.** *Critical Apparatus* — the organized system of notes and references explaining textual variants, historical context, and emendations. *Lemma* — the specific word or phrase quoted at the start of a critical note to identify the passage being explained. *Lemma Separator* — the square bracket (]) used in traditional philology to separate the lemma from the note.

**Takeaway:** Print editions structure commentary as a critical apparatus at the bottom of the page, citing the lemma with a closing square bracket and clear historical notes.

---

## **09 Content**

**PDF/A: The Archival Standard for Digital Documents**

When generating a PDF for long-term preservation, not all PDFs are equal. Standard PDFs can contain active JavaScript, external font links, and embedded audio. Over time, these dependencies break, causing the document to render incorrectly.

To solve this problem, the International Organization for Standardization created **PDF/A**. PDF/A is a specialized subset of PDF designed specifically for digital preservation.

PDF/A enforces strict preservation rules:

1. **100% Font Embedding:** Every font used in the document must be embedded directly inside the PDF file. The document will display correctly even if the original font is deleted from the computer.
2. **Device-Independent Color:** Colors are defined using standard color profiles so pages look identical on all screens and printers.
3. **No External Dependencies:** External hyperlinks to outside scripts or dynamic media are prohibited.
4. **Structured Metadata:** Rich XML metadata (XMP) is embedded inside the PDF header, detailing author, title, date, and license.

When submitting your final digital edition PDF, compiling to PDF/A guarantees your work remains readable for decades.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Preservation Rule</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Standard PDF Behavior</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Archival PDF/A Requirement</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Font Handling</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Often links to system fonts; breaks if font missing</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Mandatory 100% embedded fonts inside the file</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Embedded Code</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Permits active JavaScript and executable macros</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Strictly prohibited; only static content allowed</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Preservation Horizon</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Uncertain; dependent on proprietary viewers</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Guaranteed 50+ year visual fidelity under ISO 19005</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *PDF/A* — an ISO-standardized version of PDF specialized for digital preservation and archiving. *Font Embedding* — storing the full outline data of every typeface inside the document file. *XMP Metadata* — Extensible Metadata Platform, an XML format for embedding bibliographic metadata inside digital files.

**Takeaway:** Compiling to the PDF/A archival standard embeds all fonts and metadata directly inside the file, guaranteeing permanent visual preservation.

---

## **10 Content**

**The FAIR Data Principles: Findable and Accessible**

Publishing a digital edition is not just about making a website; it is about contributing to global scholarly knowledge. Today, research funding agencies and universities require research data to follow the **FAIR Data Principles**.

FAIR stands for:

- **F**indable
- **A**ccessible
- **I**nteroperable
- **R**eusable

Let us examine the first two principles:

1. **Findable:** Your edition must have rich metadata and a unique, persistent identifier (such as a DOI). Search engines and library catalogues must be able to discover your project easily.
2. **Accessible:** Your edition must be stored in a trusted repository where anyone can download it using standard, open communication protocols (like HTTP). There should be no paywalls or proprietary barriers preventing scholars from accessing the text.

Following these principles ensures your scholarship reaches a worldwide audience and remains discoverable for generations.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Principle</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Core Requirement</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Implementation in RELS 398</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Findable (F)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Persistent identifier (DOI) and rich searchable metadata</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Depositing edition on Zenodo and minting an official DOI</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Accessible (A)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Open, free retrieval via standard protocols without barriers</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Public repository on GitHub and open access download on Zenodo</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *FAIR Data Principles* — international guidelines establishing that research data must be Findable, Accessible, Interoperable, and Reusable. *Persistent Identifier (PID)* — a permanent digital handle that remains valid even if web server addresses change. *Open Access* — the free, unrestricted online availability of research scholarship and data.

**Takeaway:** The Findable and Accessible principles ensure your digital edition can be discovered through persistent DOIs and downloaded freely by scholars worldwide.

---

## **11 Content**

**The FAIR Data Principles: Interoperable and Reusable**

The second half of the FAIR framework addresses how other scholars and computers can work with your data: **Interoperable** and **Reusable**.

1. **Interoperable:** Data should use formal, standardized vocabularies so computers can integrate it with other datasets. By encoding your document in standard TEI XML and linking people and places to Wikidata and GeoNames, your edition is fully interoperable. Other digital humanists can combine your text with maps, timelines, and linguistic corpora without manual reformatting.

2. **Reusable:** Data must have clear, unambiguous licensing and detailed provenance. Other scholars must know legally how they are permitted to reuse your work. Your project must clearly declare author credits, historical sources, and computational tools.

When your edition is interoperable and reusable, other researchers can build upon your research, cite your findings, and incorporate your primary witness into larger global archives.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Principle</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Core Requirement</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Implementation in RELS 398</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Interoperable (I)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Standard formats and shared vocabularies for data exchange</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Valid TEI P5 XML schema and Linked Open Data URIs</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Reusable (R)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Clear licenses, detailed provenance, and documentation</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Creative Commons licenses, README.md, and LEDGER.md</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Interoperability* — the ability of computer systems and software to exchange and interpret shared data without friction. *Reusability* — providing clear licensing and documentation so future researchers can legally and practically reuse data. *Data Provenance* — the documented history of data creation, revision, and computational processing.

**Takeaway:** Encoding in TEI XML and declaring explicit open licenses satisfies the Interoperable and Reusable principles, empowering global scholars to build upon your work.

---

## **12 Content**

**Persistent Identifiers: Why URLs Break and DOIs Endure**

When a scholar cites a book, they cite the author, title, publisher, and year. That citation remains valid forever because library catalogues index books by stable metadata.

On the internet, citations are notoriously fragile. If you cite a plain web address like `http://myproject.org/edition.html`, that link will probably break within a few years. When the domain name expires or the university redesigns its website, your URL leads to a broken 404 page.

To solve this, the scholarly community uses **Persistent Identifiers (PIDs)**. The most famous persistent identifier is the **DOI (Digital Object Identifier)**.

A DOI looks like `10.5281/zenodo.1234567`. It does not point to a specific server. Instead, it points to a central global directory managed by the International DOI Foundation. When someone clicks `https://doi.org/10.5281/zenodo.1234567`, the registry automatically redirects them to the current live location of your files. If you move your files to a new server, you update the redirect target once in the registry, and every printed citation remains valid.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Identifier Type</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Example Format</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">What Happens When Server Moves</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Scholarly Reliability</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Standard URL</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">http://university.edu/~user/text.html</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Link breaks completely; 404 Not Found error</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Very low; high risk of link rot within 3&ndash;5 years</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Persistent DOI</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">https://doi.org/10.5281/zenodo.1234567</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Registry updates redirect target; citation never breaks</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Permanent; international ISO standard guarantee</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *DOI (Digital Object Identifier)* — a permanent alphanumeric string assigned by an authorized agency to identify digital content permanently. *Central DOI Directory* — the global registry that resolves DOIs to their current web addresses. *Citation Stability* — the guarantee that a scholarly reference will remain discoverable across decades.

**Takeaway:** Persistent DOIs protect your edition against link rot by providing permanent redirection through the international DOI registry.

---

## **13 Content**

**Depositing Research Data with Zenodo**

To mint an official DOI for your digital edition, you need to deposit your files in a certified research repository. The leading platform for open humanities data is **Zenodo**.

Zenodo is a free, open-access research repository operated by **CERN** (the European Organization for Nuclear Research) and supported by the European Commission. CERN is committed to maintaining Zenodo permanently, guaranteeing long-term data preservation.

When you upload your digital edition package to Zenodo:

1. Zenodo stores multiple redundant copies of your files in secure archival data centers;
2. Zenodo mints an official, internationally recognized DOI for your deposit;
3. Zenodo generates a permanent citation page with structured metadata;
4. Your edition is indexed by Google Scholar, OpenAIRE, and international university library catalogues.

Depositing your project on Zenodo elevates your work from a student class project to a formal, citable contribution to digital textual scholarship.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Repository Feature</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Zenodo Implementation</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Benefit to Your Edition</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Operating Institution</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">CERN (European Organization for Nuclear Research)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Permanent institutional backing and secure infrastructure</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">DOI Assignment</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Automatic minting via DataCite registration agency</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Official, citable DOI for CVs and academic papers</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Cost to Researchers</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">100% free for open-access datasets up to 50 GB</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Zero hosting fees or recurring financial maintenance</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Zenodo* — a trusted, open-access digital research repository operated by CERN that provides free long-term data storage and DOIs. *CERN* — the European Organization for Nuclear Research, providing global scientific infrastructure. *DataCite* — the leading global registration agency that mints DOIs for research datasets.

**Takeaway:** Zenodo provides free, permanent archival storage and mints an official citable DOI for your capstone digital edition.

---

## **14 Content**

**Linking GitHub to Zenodo for Automated Releases**

One of the most powerful workflows in modern digital scholarship is linking your **GitHub code repository** directly to **Zenodo**.

When you link GitHub to Zenodo, you automate the archiving process:

1. In your Zenodo account settings, you authorize GitHub and flip the switch for your edition repository;
2. In GitHub, whenever you are ready to publish a new milestone, you create a formal **Release** and assign a version tag (like `v1.0.0`);
3. GitHub automatically sends a snapshot of your repository to Zenodo;
4. Zenodo archives the code, extracts metadata from your repository, and mints a brand-new DOI in seconds.

Zenodo also manages versioning automatically. It provides a "Concept DOI" that always points to your newest release, as well as distinct "Version DOIs" for specific milestones. Scholars can cite the exact version of your edition they used in their research.

```text
1. GitHub Repository (Active Editing)
   -> Create Tagged Release (v1.0.0)
2. Zenodo Automated Ingestion
   -> Archive Snapshot and Mint DOI
3. Permanent Citable DOI: 10.5281/zenodo.1234567
```

**Vocabulary.** *GitHub-Zenodo Integration* — an automated bridge that archives GitHub repository releases directly into Zenodo. *Concept DOI* — a master DOI that resolves to the latest version of a project across all its releases. *Version DOI* — a persistent identifier pointing specifically to an individual release snapshot of a project.

**Takeaway:** The GitHub-Zenodo integration automatically archives tagged releases, minting permanent DOIs without manual file uploads.

---

## **15 Content**

**Structuring the Capstone Edition Portfolio**

For your final RELS 398 / ENGL 398 course deliverable, you will assemble a comprehensive **Digital Edition Portfolio**. This portfolio represents the culmination of your entire semester's research and technical work.

A complete portfolio contains five core components organized cleanly in your repository:

1. **Master TEI XML File (`edition_master.xml`):** The fully validated master document integrating `<teiHeader>`, `<editorialDecl>`, `<facsimile>`, diplomatic/normalized text, and `<standOff>` commentary notes.
2. **Archival Facsimiles (`images/`):** High-resolution scans of the primary document with transparent zone coordinates.
3. **Standalone Web Package (`dist/web/`):** Responsive HTML and CSS files ready for web hosting or offline browsing.
4. **Print-Ready PDF Codex (`dist/pdf/`):** A beautifully typeset PDF/A document with running headers, line numbers, and bottom apparatus footnotes.
5. **Project Introduction & Ledger (`README.md` and `LEDGER.md`):** Complete documentation of provenance, editorial principles, AI disclosures, and settled decisions.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Portfolio Component</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">File Path</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Primary Quality Gate</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Master TEI XML</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">edition_master.xml</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Zero schema validation errors; valid internal pointer IDs</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Web Application</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">dist/web/index.html</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Responsive layout; functional commentary popups; 0 broken links</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Print PDF Codex</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">dist/pdf/edition.pdf</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">PDF/A compliant; embedded fonts; clean footnote apparatus</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Editorial Ledger</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">LEDGER.md</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Documented decisions, settled policies, and AI provenance</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Digital Edition Portfolio* — the complete bundle of master XML data, facsimile images, web layouts, print PDFs, and documentation representing a completed editing project. *Quality Gate* — a strict verification check that must pass before a milestone is accepted. *Portfolio Assembly* — gathering and testing all semester components into a unified directory structure.

**Takeaway:** The final capstone portfolio unifies your master TEI XML, archival facsimiles, responsive web edition, print PDF, and documentation into a single citable release.

---

## **16 Content**

**The Project Ledger (LEDGER.md): Documenting Decisions**

Throughout this course, you have maintained a project ledger called `LEDGER.md`. In professional digital textual scholarship, keeping an active ledger is essential for governance and reproducibility.

An editorial project involves hundreds of micro-decisions. How did you decide to regularize a misspelled word? Why did you link a person to one specific Wikidata record instead of another? What criteria did you use to date an undated letter?

If you do not write these decisions down, you will forget your own reasoning within three months. Furthermore, external peer reviewers will not be able to evaluate the integrity of your scholarship.

Your `LEDGER.md` documents:

1. **Settled Decisions:** Editorial choices that are locked and finalized;
2. **Methodological Provenance:** Dictionaries and archival records consulted;
3. **Computational Logs:** Software versions, prompts, and verification audits.

Keeping a clear ledger establishes an unbroken chain of custody for your scholarly findings.

```markdown
## Settled Decisions
1. Orthography: Regularized 18th-century verb endings (-oit to -ait)
   using Dictionnaire de l'Académie française (5e éd., 1798).
2. Entity Resolution: Linked Shubenacadie Chief Jean-Baptiste Cope
   to Wikidata Q104853241 based on 1752 treaty council minutes.
3. AI Assistance: Drafted philological notes with LLM assistance;
   verified 100% against the Oxford English Dictionary.
```

**Vocabulary.** *Project Ledger* — a markdown file tracking editorial decisions, settled policies, and methodological provenance across an editing project. *Methodological Provenance* — the documented reasoning and evidence supporting scholarly choices. *Settled Decision* — a locked editorial baseline that prevents endless revisiting of resolved questions.

**Takeaway:** The project ledger records your editorial decisions and methodological reasoning, ensuring scholarly transparency and reproducibility.

---

## **17 Content**

**Open Access Licensing in Practice: CC BY, CC0, and MIT**

A digital edition contains different kinds of intellectual property. It contains original prose, structured data, and computer code. Applying a single generic license to the whole project is often legally ineffective.

Professional digital humanities projects use **multi-tiered licensing**:

1. **Creative Commons Attribution 4.0 (CC BY 4.0):** Applied to your original prose, historical introductions, and commentary notes. Anyone may share and adapt your writing, as long as they give you proper scholarly credit.
2. **Creative Commons CC0 1.0 Universal (Public Domain Dedication):** Applied to your TEI XML markup, entity registries, and metadata. Dedicating metadata to the public domain allows libraries and search engines to ingest your records freely without legal friction.
3. **The MIT License:** Applied to your build scripts, Python tools, and CSS stylesheets. The MIT license is a standard open-source software license permitting free code reuse.

Declaring these licenses explicitly in your `README.md` and TEI header eliminates legal ambiguity for future researchers.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Edition Asset Layer</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Recommended License</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Legal Effect</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Scholarly Benefit</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Prose &amp; Commentary</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">CC BY 4.0 International</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Free sharing and adaptation with attribution</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Protects academic credit while maximizing impact</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">TEI XML &amp; Metadata</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">CC0 1.0 Universal</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Public domain dedication without restrictions</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Enables automated library and database indexing</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Software &amp; Scripts</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">MIT License</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Permissive open-source software license</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Allows other digital editors to reuse build tools</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Multi-Tiered Licensing* — applying distinct open licenses to different asset types like prose, metadata, and code within a single project. *CC BY 4.0* — an open license requiring users to give attribution to the original author. *CC0 1.0 Universal* — dedicating data to the public domain by waiving all copyright rights.

**Takeaway:** Multi-tiered open access licensing protects your scholarly authorship while permitting global research reuse and library indexing.

---

## **18 Content**

**Cohort Archiving: Ace's French Revolutionary Decree**

Let us examine how our three cohort students will archive their completed editions on Zenodo and GitHub.

Ace is archiving the 1791 French decree *Loi relative à la fabrication des assignats*. When Ace deposits the project on Zenodo, the metadata must accurately capture the document's historical coordinates:

- **Title:** *A Digital Scholarly Edition of the French Revolutionary Decree on Assignats (June 19, 1791)*
- **Creators:** Ace (Editor), Kenneth Penner (Instructor)
- **Description:** A digital documentary edition of the National Assembly decree authorizing small 5-livre paper currency notes, featuring diplomatic transcription of Imprimerie Royale printings and modernized French.
- **Keywords:** French Revolution, assignats, paper money, Imprimerie Royale, monetary policy, TEI XML, 1791.
- **Archival Custody:** Archives nationales de France (Paris), Série C (Procès-verbaux de l'Assemblée nationale).

Ace uploads the master TEI XML, high-resolution scans of the decree, the dual-column HTML package, and the print PDF codex. Zenodo mints an official DOI, giving Ace a permanent academic citation for graduate school applications.

**Vocabulary.** *Archival Coordinates* — the official title, series, box, and shelfmark identifying a document's physical location in an archive. *Monetary Policy* — government actions regulating the money supply, currency printing, and financial stability. *Assignat* — paper money issued by the French National Assembly during the French Revolution backed by nationalized church property.

**Takeaway:** Ace's Zenodo deposit preserves the 1791 French Revolutionary currency decree with complete archival coordinates, bilingual XML, and a citable DOI.

---

## **19 Content**

**Cohort Archiving: Olyvia's Maud Lewis Letter**

Olyvia is archiving the 1967 personal letter written by celebrated Nova Scotia folk artist Maud Lewis to collector Leonard Kinnear.

Olyvia's Zenodo deposit captures the unique cultural and epistolary value of the artifact:

- **Title:** *An Epistolary Digital Edition of Maud Lewis's Letter to Leonard Kinnear, October 25, 1967*
- **Creators:** Olyvia (Editor), Kenneth Penner (Instructor)
- **Description:** A single-witness digital documentary edition of a handwritten letter by folk artist Maud Lewis, documenting her cottage life in Marshalltown, roadside painting sales, and correspondence with collector Leonard Kinnear.
- **Keywords:** Maud Lewis, Nova Scotia folk art, Digby County, Marshalltown, epistolary edition, Canadian art history, TEI XML.
- **Archival Context:** Kinnear Family Papers; related folk art holdings in the Art Gallery of Nova Scotia (Halifax).

Olyvia bundles the postal envelope facsimiles, letter page scans, diplomatic transcription with preserved line breaks, and interactive popups of Maud's painted oxen. The resulting Zenodo DOI creates a permanent scholarly resource for Canadian art historians.

**Vocabulary.** *Folk Art* — art created by self-taught artists that reflects traditional community life and personal aesthetic expression. *Epistolary Edition* — a scholarly edition focused on letters and personal correspondence. *Single-Witness Fidelity* — preserving the authentic physical and linguistic features of a unique surviving artifact.

**Takeaway:** Olyvia's Zenodo deposit preserves Maud Lewis's 1967 handwritten letter, providing art historians with high-resolution facsimiles, diplomatic text, and a permanent DOI.

---

## **20 Content**

**Cohort Archiving: Andromeda's 1752 Peace and Friendship Treaty**

Andromeda is archiving the foundational 1752 Peace and Friendship Treaty negotiated at Halifax between Mi'kmaw Chief Jean-Baptiste Cope and Nova Scotia Governor Peregrine Hopson.

Andromeda's deposit addresses sensitive and critical legal history:

- **Title:** *A Digital Documentary Edition of the 1752 Peace and Friendship Treaty between the Mi'kmaq and the British Crown*
- **Creators:** Andromeda (Editor), Kenneth Penner (Instructor)
- **Description:** A digital edition of the November 22, 1752 treaty, featuring clause-by-clause legal transcription, scanned Mi'kmaw totem marks and wax seals, and extensive commentary on treaty rights jurisprudence.
- **Keywords:** Peace and Friendship Treaties, Mi'kma'ki, Jean-Baptiste Cope, Peregrine Hopson, Halifax, Indigenous treaties, Canadian legal history, TEI XML.
- **Archival Custody:** Nova Scotia Archives (Halifax), Record Group 1, volume 430, number 2.

Andromeda's deposit provides a dignified legal presentation, clean PDF codex, and complete historical commentary. The persistent DOI ensures this foundational treaty text is accessible to legal scholars, Indigenous communities, and historians worldwide.

**Vocabulary.** *Treaty Rights Jurisprudence* — the body of legal precedents and court decisions interpreting the rights guaranteed by historical treaties. *Nation-to-Nation Agreement* — a formal diplomatic treaty negotiated between sovereign political entities. *Archival Record Group (RG)* — a major classification unit in an archive grouping records from an official government body.

**Takeaway:** Andromeda's Zenodo deposit establishes a permanent, open-access digital edition of the 1752 treaty with legal commentary and high-resolution totem facsimiles.

---

## **21 Content**

**Creating a GitHub Release for Your Edition**

Once your files are tested and organized in your local Git repository, you are ready to publish an official **GitHub Release**. A release marks a frozen, tagged milestone in the history of your project.

To create a release in GitHub:

1. Ensure all your latest changes are committed to the `main` branch;
2. Navigate to the **Releases** tab in your GitHub repository and click **Draft a new release**;
3. Assign a semantic version tag like `v1.0.0`;
4. Give your release a descriptive title, such as *RELS 398 Capstone Digital Edition (v1.0.0)*;
5. Write detailed release notes summarizing your project scope, historical witness, and editorial principles;
6. Attach compiled binary assets, such as your standalone offline `.zip` package and print-ready `.pdf` codex.

Clicking **Publish release** freezes this snapshot permanently in Git history and triggers the automated transfer to Zenodo.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Release Field</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Recommended Value</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Tag Version</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">v1.0.0</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Semantic versioning tag marking the first full production release</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Release Title</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Capstone Digital Scholarly Edition (v1.0.0)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Clear, human-readable title for visitors and catalogues</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Attached Binaries</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">edition_offline.zip, edition_codex.pdf</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Direct download links for offline readers and library archivists</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *GitHub Release* — a formal, tagged snapshot of a repository accompanied by release notes and downloadable binary files. *Semantic Versioning* — a version numbering system (Major.Minor.Patch, like 1.0.0) reflecting the nature of project updates. *Release Notes* — a written summary describing features, fixes, and files included in a publication release.

**Takeaway:** Publishing a GitHub Release freezes an official versioned snapshot of your edition and attaches downloadable offline zip and PDF files.

---

## **22 Content**

**Preparing Your Web Edition for GitHub Pages**

In addition to depositing your source files on Zenodo, you want your interactive web edition to be live and readable online. The simplest, most durable way to host a static digital edition is **GitHub Pages**.

GitHub Pages is a free hosting service that serves web pages directly from your GitHub repository. It does not require setting up a database or managing a web server.

To launch GitHub Pages:

1. Place your compiled `index.html`, `style.css`, and `images/` directory in a folder named `docs/` or directly at the root of your repository;
2. Navigate to your repository **Settings** and select **Pages**;
3. Under **Source**, choose the `main` branch and specify the `/docs` folder;
4. Click **Save**.

Within sixty seconds, GitHub gives you a secure live public web address, such as `https://username.github.io/edition/`. Anyone with an internet browser can now explore your digital edition worldwide.

```
Repository Settings -> Pages
  Source: Deploy from a branch
  Branch: main /docs
  Status: Live at https://username.github.io/my-edition/
```

**Vocabulary.** *GitHub Pages* — a free static web hosting service provided by GitHub that turns a repository into a live public website. *Docs Folder Workflow* — storing compiled public website files in a dedicated /docs directory inside a repository. *Live Public URL* — an active web address accessible by any user on the internet over standard HTTPS.

**Takeaway:** GitHub Pages provides free, permanent static web hosting directly from your repository, making your edition instantly accessible to the public.

---

## **23 Content**

**Documenting AI Provenance and Human-in-the-Loop Audit**

Throughout this semester, you explored how computational tools and Large Language Models (LLMs) can assist digital editing. You used language models to assist with translation drafting and initial commentary suggestions.

In academic scholarship, using AI tools is entirely acceptable provided that it is accompanied by **transparent methodological provenance**. You must never hide the tools you used.

In your `README.md` and edition paratexts, you must include a formal **AI Disclosure Statement**:

1. Name the specific models, versions, and platforms consulted (e.g. Claude 3.5 Sonnet, Gemini 1.5 Pro, local Gemma);
2. Document the prompt templates used to generate initial drafts;
3. State the dates when queries were run;
4. Detail your **Human-in-the-Loop verification protocol**: how human editors audited every suggested date, name, and definition against primary facsimiles and peer-reviewed reference works.

Scholarly authority does not come from doing everything by hand; it comes from rigorous verification and complete methodological transparency.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Disclosure Area</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Required Information</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Ethical Standard</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Model Specification</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Exact model name, version number, and provider API</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Reproducibility and computational transparency</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Human Verification</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Reference works consulted to verify AI drafts (OED, SEDRA)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Scholarly accuracy and human accountability</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *AI Disclosure Statement* — a formal declaration in an edition documenting all artificial intelligence tools used during research. *Human-in-the-Loop (HITL)* — a workflow where human experts review, verify, and correct automated or AI-generated outputs. *Computational Transparency* — full disclosure of all software tools and algorithms used in research.

**Takeaway:** Full disclosure of AI models and human-in-the-loop verification protocols establishes scholarly trust and upholds academic integrity.

---

## **24 Content**

**Archival Checksums: Verifying Data Integrity with SHA-256**

When archiving digital files for decades, how do you know a file has not been corrupted or altered? Digital files can experience "bit rot," where physical storage degradation flips bits on a hard drive.

To guarantee file integrity, archivists use **cryptographic checksums**. A checksum is a unique mathematical fingerprint generated from the exact bytes of a file. The international standard for data integrity is **SHA-256**.

If a file changes by even a single comma or space, its SHA-256 checksum changes completely. When you publish your release, you generate a checksum for each file and record them in a file named `CHECKSUMS.txt`.

Anyone who downloads your edition can run `sha256sum -c CHECKSUMS.txt` in their terminal. If the check returns "OK", they have mathematical proof that their copy is 100% identical to your original archive.

```bash
# Generating SHA-256 checksums in terminal
sha256sum edition_master.xml dist/pdf/edition.pdf > CHECKSUMS.txt
```

```
CHECKSUMS.txt content:
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  edition_master.xml
5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8  edition.pdf
```

**Vocabulary.** *Cryptographic Checksum* — a fixed-length string generated by an algorithm representing the unique byte contents of a file. *SHA-256* — a secure cryptographic hashing algorithm that produces a 256-bit mathematical fingerprint. *Bit Rot* — the gradual physical decay of storage media resulting in silent file corruption.

**Takeaway:** SHA-256 checksums provide cryptographic proof of data integrity, allowing scholars to verify that downloaded files are authentic and uncorrupted.

---

## **25 Content**

**Writing a Professional Citation for Your Digital Edition**

If you want other scholars to cite your work, you must provide them with a clear, standardized citation. Do not force readers to guess how to cite your digital edition.

Include a dedicated **"How to Cite This Edition"** section at the bottom of your `README.md` and in your TEI header. Provide citations in standard academic styles, such as Chicago, MLA, and APA.

A professional digital edition citation includes:

1. **Editor Name(s):** The scholar(s) who transcribed, edited, and annotated the text;
2. **Edition Title:** In italics, followed by the descriptor *[Digital Scholarly Edition]*;
3. **Institutional Context:** St. Francis Xavier University;
4. **Publication Year:** The year of release (2026);
5. **Persistent Identifier:** The permanent DOI link pointing to Zenodo.

```markdown
### How to Cite This Edition (Chicago Style)
Penner, Andromeda, ed. *The 1752 Peace and Friendship Treaty: A Digital
Documentary Edition*. Antigonish, NS: St. Francis Xavier University, 2026.
https://doi.org/10.5281/zenodo.1234567.
```

**Vocabulary.** *Scholarly Citation* — a formal reference providing bibliographic details necessary to locate and verify an academic source. *Chicago Manual of Style* — the standard citation guideline used in history and humanities disciplines. *Citation Descriptor* — a bracketed note like [Digital Scholarly Edition] indicating the medium of a published source.

**Takeaway:** Providing formal Chicago, MLA, and APA citations with persistent DOIs enables future researchers to cite your digital scholarship accurately.

---

## **26 Content**

**Peer Review and Scholarly Evaluation of Digital Editions**

How is a digital edition evaluated by the academic community? In traditional publishing, a monograph is reviewed based on prose arguments and press reputation. In digital textual scholarship, peer review evaluates both philological quality and computational architecture.

Organizations like the **Institute for Documentology and Scholarly Editing (IDE)** have published formal criteria for reviewing digital scholarly editions:

1. **Methodological Transparency:** Are transcription, normalization, and emendation policies clearly explained in the introduction?
2. **Markup Quality:** Does the TEI XML conform to valid schemas? Are entities linked to verified Linked Open Data records?
3. **Material Witness Fidelity:** Does the edition provide high-resolution facsimiles and respect the physical artifact?
4. **Technical Sustainability:** Is the edition built with open formats and minimal computing principles, free from server fragility?

When your capstone portfolio satisfies these criteria, your work achieves the status of peer-reviewed digital scholarship.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Evaluation Dimension</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Key Scholarly Question</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Passing Evidence</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Editorial Transparency</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Are all regularizations and emendations fully documented?</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Detailed &lt;editorialDecl&gt; and project LEDGER.md</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Data Integrity</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Is the master XML valid and free from broken pointers?</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">100% schema validation pass in VS Code</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Long-Term Survival</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Will the edition remain functional in twenty years?</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Static HTML, PDF/A, and Zenodo DOI archive</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Digital Edition Peer Review* — the systematic academic evaluation of an electronic scholarly edition based on textual, technical, and interface standards. *IDE (Institut für Dokumentologie und Editorik)* — a leading international organization that establishes peer review standards for digital editions.

**Takeaway:** Peer review of digital editions evaluates both philological rigor and computational sustainability, requiring valid XML, clear policies, and durable archiving.

---

## **27 Content**

**Final Quality Gate: Pre-Deposit Verification Checklist**

Before tagging your release and depositing files on Zenodo, you must pass the final **Pre-Deposit Verification Checklist**. This checklist ensures that your project contains zero embarrassing defects.

The checklist covers five critical verification gates:

1. **Schema Gate:** Run XML validation on `edition_master.xml`. Verify zero syntax errors and zero orphaned note targets.
2. **HTML Gate:** Test `index.html` in your browser. Verify that all five commentary popups open properly and that image paths load cleanly.
3. **PDF Gate:** Inspect `dist/pdf/edition.pdf`. Confirm that fonts are embedded, margins are balanced, and footnotes appear on correct pages.
4. **Metadata Gate:** Confirm that `README.md` includes complete archival coordinates, AI disclosures, and citation text.
5. **Checksum Gate:** Run `sha256sum` to generate `CHECKSUMS.txt`.

Taking thirty minutes to complete this checklist protects your academic reputation and ensures your edition is ready for permanent deposit.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Checklist Item</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Verification Tool</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Required Output</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">TEI Schema Validation</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Red Hat XML extension in VS Code</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Green checkmark; 0 errors, 0 warnings</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Link and Pointer Audit</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Browser DevTools (F12) Network Tab</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Zero 404 errors; all 5 note targets resolve</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Archival Checksums</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">sha256sum command in terminal</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">CHECKSUMS.txt generated with accurate hashes</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Pre-Deposit Checklist* — a systematic verification protocol executed immediately before freezing a release and archiving files. *Orphaned Target* — an internal note pointer referencing an anchor ID that does not exist in the document text. *Zero-Error Standard* — requiring that all schemas and links validate completely before publication.

**Takeaway:** The pre-deposit verification checklist guarantees that your master XML, web layouts, print PDF, and metadata are 100% verified before permanent release.

---

## **28 Content**

**Today's Studio Lab: Building the Release Package**

In today's final classroom studio lab in Mulroney Hall 3032, you will assemble and test your complete release package.

Your lab workflow follows three structured stages:

1. **Compile Offline Deliverables:** Build your standalone offline HTML package and print-ready PDF codex. Test that the offline package opens and searches properly without internet access.
2. **Assemble Repository Structure:** Organize your project files into standard directories (`src/`, `dist/web/`, `dist/pdf/`, `images/`). Run `sha256sum` to generate your `CHECKSUMS.txt` manifest.
3. **Draft Release Notes:** In your repository, draft the release notes for version `v1.0.0`. Document your project scope, historical artifact details, and open licensing terms.

I will circulate throughout the lab to inspect your directory trees, test offline packages, and verify checksum outputs.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Lab Stage</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Student Action in VS Code</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Target Deliverable</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Stage 1: Compilation</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Generate offline web bundle and print-ready PDF</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">dist/web/ and dist/pdf/ populated</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Stage 2: Checksums</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Run sha256sum across master files and binaries</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Verified CHECKSUMS.txt manifest</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Stage 3: Release Draft</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Draft release notes and verify Zenodo metadata fields</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">v1.0.0 release notes prepared in README.md</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Release Package* — the structured bundle of validated XML, compiled web pages, PDFs, and checksums prepared for public archiving. *Checksum Manifest* — a plain-text file listing cryptographic hashes for every file in a dataset. *Verification Stage* — a distinct checkpoint during project assembly confirming quality before release.

**Takeaway:** Today's studio lab guides you to compile offline packages, generate cryptographic checksums, and draft your official release notes in VS Code.

---

## **29 Content**

**The December Exam Period Deliverable and Timeline**

As our semester concludes, let us review the final course evaluation timeline and requirements.

First, remember that **Assignment 12 (Scholarly Commentary)** is due tonight, **Friday, December 4 at 11:00 PM**. Assignment 12 evaluates your five hand-authored commentary notes and your `COMMENTARY.md` reflection ledger (80 points total).

Second, your final course deliverable is the **Comprehensive Digital Edition Portfolio**. This is your capstone submission for the course.

- **Submission Window:** December Exam Period, December 10 to 19, 2026;
- **Total Value:** 100 points (the capstone culmination of your semester);
- **Grading Rubric:** Evaluates single-witness transcription accuracy (20 pts), TEI XML schema validity (20 pts), named entity linking and LOD (20 pts), critical commentary depth (20 pts), and multi-modal publishing with Zenodo DOI (20 pts).

You have plenty of time during the exam period to polish your layout, double-check your shelfmarks, and finalize your Zenodo deposit.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Deliverable</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Due Date &amp; Time</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Points</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Submission Location</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Assignment 12: Commentary</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Tonight, Fri Dec 4 &middot; 11:00 PM</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">80 pts</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Moodle Workshop Section 12</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Capstone Edition Portfolio</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Exam Period: Dec 10&ndash;19, 2026</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">100 pts</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Moodle Section 13 &amp; GitHub Repository</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Capstone Portfolio* — the comprehensive final project deliverable synthesizing all semester learning into a finished publication. *Exam Period Submission Window* — the designated university schedule window (Dec 10–19) for submitting final projects and portfolios. *Holistic Evaluation* — grading that assesses the overall integration, rigor, and craft of a complete digital project.

**Takeaway:** Assignment 12 is due tonight at 11:00 PM, and your final Capstone Digital Edition Portfolio is submitted during the December Exam Period (Dec 10–19).

---

## **30 Content**

**Course Synthesis: The Journey from Novice to Digital Editor**

Take a moment to reflect on how far you have traveled since September. When you entered Mulroney Hall 3032 in early September, you had never opened VS Code. You had never typed a command into a terminal. You had never written an XML tag.

Over thirteen weeks, you conquered the fundamental crafts of digital textual scholarship:

- You learned to navigate the file system and control code with Git;
- You bound digital facsimiles and encoded diplomatic transcriptions in TEI XML;
- You resolved orthographic variations and parsed linguistic features;
- You connected historical people and places to global Linked Open Data registries;
- You authored scholarly commentary notes and designed responsive web layouts;
- Today, you published multi-modal editions with persistent DOIs and open licenses.

You have preserved three remarkable historical voices: an 18th-century French Revolutionary decree, an intimate handwritten letter by Maud Lewis, and a foundational 1752 Peace and Friendship Treaty.

Your editions are rigorous, accessible, and durable. You are no longer novices; you are published digital scholarly editors. Congratulations on an extraordinary semester of scholarship.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Phase</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Skills Acquired</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Scholarly Transformation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Weeks 1&ndash;4</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">VS Code, Terminal, Git, Cataloguing, Facsimiles</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">From computer novices to confident codicologists</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Weeks 5&ndash;9</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">TEI XML, Normalization, Lemmatization, NER, LOD</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">From transcribers to computational linguists</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Weeks 10&ndash;13</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Alignment, Commentary, Processing Model, Zenodo</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">From students to published digital textual editors</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Scholarly Transformation* — the developmental growth of students from initial beginners to confident, independent digital editors. *Textual Stewardship* — the ethical and academic responsibility of preserving and publishing historical voices faithfully. *Digital Textual Editor* — a scholar capable of transcribing, encoding, annotating, and publishing historical primary documents.

**Takeaway:** Over thirteen weeks, you evolved from terminal novices into published digital scholarly editors, preserving vital historical witnesses for the global community.
