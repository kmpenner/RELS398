# Lesson 13.2 — The TEI Processing Model, ODD Customization, and Presentation Styles

*RELS 398 / ENGL 398 · Topic 13: Publication · Meeting #35 (Wed Dec 2)*

***Studio and publication assembly week (no three-step cycle).** Today you explore the TEI Processing Model, author an ODD customization (`<model>`, `<modelSequence>`, `<modelGrp>`, `@behaviour`, `@predicate`), and configure web layouts with CSS Flexbox and Grid to present your digital edition.*

---

## **01 Content**

**From Raw XML to the Web: The Need for Presentation**

Raw TEI XML is a rich data format. It records textual structure, physical handwriting, and critical commentary with precision. However, raw XML is not designed for everyday reading. Web browsers do not know how to display tags like `<persName>` or `<del>` without clear instructions.

If you open an XML document in a standard browser, you see a raw text tree. You see angle brackets, attribute strings, and unformatted paragraphs. Everyday readers find this view confusing and difficult to navigate. A successful digital edition requires an attractive and readable visual interface.

Visual presentation transforms structured data into an engaging reading experience. It adds readable typography, generous line spacing, and balanced margins. It also creates interactive features such as clickable notes, image viewers, and search panels.

By separating underlying data from visual display, you preserve both functions. Your TEI XML remains an archival record. At the same time, your web presentation delivers an accessible edition to the public.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Layer</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Primary Format</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Core Purpose</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Target Audience</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Data Layer</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">TEI XML</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Archival preservation and semantic structure</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Computers, search engines, and scholars</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Presentation Layer</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">HTML5 and CSS3</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Visual reading layout and interaction</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Students, researchers, and the public</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Data Layer* — the structured XML markup that encodes semantic meaning independently of display. *Presentation Layer* — the visual interface composed of HTML and CSS that displays text to human readers. *Raw XML Tree* — the unformatted hierarchical display of elements, attributes, and tags shown by default in web browsers.

**Takeaway:** Separating semantic data from visual presentation allows digital editions to maintain archival integrity while delivering readable web layouts.

---

## **02 Content**

**The Legacy Trap: Monolithic XSLT Stylesheets**

In the early decades of the digital humanities, publishing a TEI edition required writing complex XSLT stylesheets. XSLT stands for Extensible Stylesheet Language Transformations. It is a programming language designed to convert XML into other formats like HTML or PDF.

While XSLT is very powerful, it created serious maintenance challenges. Projects often accumulated thousands of lines of dense code. Editorial rules, XPath expressions, and HTML tags were mixed together in single files. This created fragile systems that only dedicated programmers could maintain.

When editors changed a tag in their schema, the transformation stylesheet often broke. If the original programmer left the project, nobody knew how to fix the broken templates. Many early digital editions stopped working because their custom scripts could not be updated.

Furthermore, custom stylesheets could rarely be shared between projects. Every university built its own separate publishing software from scratch. The digital humanities community needed a standardized and declarative approach to visual rendering.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Publishing Approach</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">How Rules Are Written</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Maintenance Effort</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Cross-Project Reuse</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Bespoke XSLT (Legacy)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Complex procedural programming templates</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Very high; requires advanced programming staff</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Rare; code is tightly coupled to one project</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Processing Model (Modern)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Declarative rules inside the project ODD schema</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Low; editors configure abstract behaviors directly</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Universal; standard rules run on any modern platform</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *XSLT* — a programming language used to transform XML documents into HTML, PDF, or text formats. *Maintenance Debt* — the accumulated cost and difficulty of maintaining complex or obsolete custom code over time. *Procedural Code* — instructions that detail every programmatic step rather than declaring the desired result.

**Takeaway:** Custom XSLT stylesheets created fragile digital editions that were expensive to maintain and difficult to share across institutions.

---

## **03 Content**

**The TEI Processing Model: Declarative Rendering**

To overcome the fragility of custom scripts, the TEI Consortium created the Processing Model. Introduced in Chapter 22 of the TEI Guidelines, this model offers a declarative system for document publication.

Declarative modeling means stating what you want rather than programming how to build it. Instead of writing fifty lines of procedural code to render a deleted word, you assign a simple behavior rule. You declare that `<del>` has the behavior `inline` with a strikethrough style.

The Processing Model maps hundreds of diverse TEI elements onto a small set of standardized behaviors. These behaviors include familiar concepts like paragraphs, headings, lists, notes, and graphics. Software engines translate these abstract behaviors into valid web layouts automatically.

This design returns control to scholarly editors. You do not need to be a software engineer to publish your edition. By writing clear rendering rules in your schema, you ensure your text displays accurately across all media.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Element</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Abstract Behaviour</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Rendered HTML Output</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Visual Effect</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;p&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">paragraph</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;p&gt;...&lt;/p&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Block text with vertical paragraph spacing</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;head&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">heading</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;h2&gt;...&lt;/h2&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Prominent bold section heading</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;persName&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">inline</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;span class="persName"&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Flowing inline text with optional highlight</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *TEI Processing Model* — a standardized system for expressing publication and rendering rules directly within TEI schemas. *Declarative Rendering* — defining visual intentions through high-level rules rather than low-level procedural code. *Abstract Behaviour* — a platform-neutral rendering instruction such as heading, paragraph, or note.

**Takeaway:** The TEI Processing Model replaces thousands of lines of procedural code with standardized, declarative rendering instructions.

---

## **04 Content**

**The ODD Concept: One Document Does It All**

In TEI scholarship, the acronym ODD stands for **One Document Does It All**. An ODD file is an XML document that contains everything needed to define and document a digital editing project.

Before ODD was created, projects maintained separate files for documentation, validation schemas, and stylesheets. Over time, these files drifted apart. The written guidelines described one set of rules, while the schema enforced another, and the stylesheets expected a third.

ODD solves this problem by creating a single source of truth. An ODD file brings together three critical components:

1. Human-readable prose explaining your editorial principles;
2. Formal schema declarations defining authorized elements and attributes;
3. Processing models specifying how elements should be displayed.

When you compile an ODD file, automated tools generate your validation schemas and publication code from the same source. If you update a rule in your ODD, your documentation, schemas, and web layouts update together.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">ODD Section</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">XML Elements</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Compiled Product</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Primary Beneficiary</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Prose Manual</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;body&gt;, &lt;div&gt;, &lt;p&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Editorial handbook in HTML or PDF</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Editors and students</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Schema Specification</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;schemaSpec&gt;, &lt;elementSpec&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Relax NG (.rng) and Schematron (.sch) schemas</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">XML validators in VS Code</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Processing Models</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;model&gt;, &lt;modelSequence&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Web stylesheets and transformation scripts</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Web browsers and publishing engines</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *ODD (One Document Does It All)* — a TEI XML format that integrates prose documentation, schema declarations, and rendering models into a single file. *Single Source of Truth* — a design principle where data and rules are defined in one authoritative location to avoid drift. *Schema Compilation* — the automated process of converting an ODD file into formal validation schemas like Relax NG.

**Takeaway:** An ODD file acts as the single source of truth for an edition, generating guidelines, validation schemas, and web stylesheets from one master file.

---

## **05 Content**

**The Structure of an ODD File: schemaSpec and elementSpec**

An ODD file is written using standard TEI XML markup. Its root element is `<TEI>`, and its metadata lives inside `<teiHeader>`. The core technical work occurs inside `<text><body>` within the `<schemaSpec>` element.

The `<schemaSpec>` tag establishes the name, prefix, and identity of your custom schema. Inside this container, you select the TEI modules your project needs using `<moduleRef>` tags. For example, loading `moduleRef key="core"` imports fundamental tags like paragraphs and titles.

To customize a specific tag, you add an `<elementSpec>` block. You set `@ident` to the name of the tag and `@mode="change"` to modify its behavior. This tells the processor that you are refining an existing TEI element rather than inventing a new one.

Inside `<elementSpec>`, you nest `<model>` tags. Each `<model>` defines a specific rendering behavior for that element. This clean structure keeps all rules for an element organized in one clear location.

```xml
<elementSpec ident="persName" mode="change">
  <desc>Encodes personal names with popups linking to Wikidata</desc>
  <model behaviour="inline" cssClass="tei-persName">
    <param name="ref" value="@ref"/>
  </model>
</elementSpec>
```

**Vocabulary.** *schemaSpec* — the root container in an ODD file defining the project schema and module imports. *elementSpec* — an ODD block that customizes the rules, attributes, and models for a specific TEI element. *moduleRef* — a declaration that imports a standard module of elements from the TEI Guidelines.

**Takeaway:** An ODD file organizes customizations inside elementSpec containers, where each tag receives its description, rules, and rendering models.

---

## **06 Content**

**Core Processing Model Behaviours: Inlines and Blocks**

At the heart of the Processing Model are predefined **behaviours**. A behaviour tells the publishing software how to treat an element in the final output. The two most fundamental layout behaviours are `inline` and `block`.

An `inline` behaviour renders an element within the natural flow of surrounding text. Words continue across the line without creating line breaks. You use `inline` for personal names (`<persName>`), place names (`<placeName>`), dates (`<date>`), and highlighted phrases (`<hi>`).

A `block` behaviour creates a distinct rectangular area that starts on a new line and pushes subsequent content below it. In web browsers, blocks are rendered as `<div>` or `<section>` elements. You use `block` for divisions, author statements, and editorial notes.

A closely related behaviour is `paragraph`. It formats text with standard paragraph margins and indentation, rendering as an HTML `<p>` tag. Distinguishing between inline and block flows forms the basis of all clean web typography.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Behaviour</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Typical TEI Tags</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">HTML Rendering</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Layout Effect</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">inline</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">&lt;persName&gt;, &lt;placeName&gt;, &lt;date&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">&lt;span class="..."&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Flows seamlessly within the current text line</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">block</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">&lt;div&gt;, &lt;byline&gt;, &lt;docDate&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">&lt;div class="..."&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Starts on a new line; occupies full available width</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">paragraph</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">&lt;p&gt;, &lt;ab&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">&lt;p&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Block text with vertical margin spacing</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Inline Behaviour* — a rendering mode where content flows inside the existing line without creating vertical breaks. *Block Behaviour* — a rendering mode where content starts on a new line and occupies the full horizontal space. *Predefined Behaviour* — a standard keyword in the TEI Processing Model specifying a layout function.

**Takeaway:** The inline and block behaviours establish the core structure of web layouts, determining whether text flows horizontally or breaks into distinct vertical blocks.

---

## **07 Content**

**Document Structure Behaviours: Sections and Breaks**

Historical documents possess physical boundaries that do not always match modern reading units. A letter may cross two physical pages. A legal decree may contain formal margin notes and line breaks. The Processing Model provides special behaviours to handle physical divisions.

The `heading` behaviour formats titles and section banners. When applied to `<head>`, it generates appropriate HTML header tags (`<h2>`, `<h3>`) based on the nesting level of the parent `<div>`. This creates a clear visual hierarchy for readers.

The `break` behaviour handles milestone markers like page breaks (`<pb/>`) and line breaks (`<lb/>`). Instead of enclosing text, milestone tags mark specific physical points in the document.

In a diplomatic edition, you might render `<lb/>` as a visible line break (`<br>`) to preserve handwritten lineation. In a normalized reading view, you might suppress `<lb/>` or replace it with a space so sentences flow continuously. The Processing Model makes this distinction easy to configure.

```xml
<elementSpec ident="pb" mode="change">
  <model behaviour="break" type="page">
    <param name="label" value="concat('[Page ', @n, ']')"/>
  </model>
</elementSpec>
```

**Vocabulary.** *Heading Behaviour* — a rendering instruction that formats title text with prominent size and weight based on section level. *Break Behaviour* — a rendering rule for milestone elements that inserts page or line breaks into the output stream. *Milestone Element* — an empty XML tag like pb or lb marking a physical transition point rather than enclosing content.

**Takeaway:** The heading and break behaviours allow editors to represent document divisions and physical manuscript milestones without disrupting reading flow.

---

## **08 Content**

**Critical Editing Behaviours: Notes and Popups**

Commentary notes are essential for historical understanding, but long notes can clutter the primary text. If every historical explanation appeared inline, readers would lose the thread of the original author's voice.

The Processing Model provides the `note` behaviour to manage annotations cleanly. The `note` behaviour instructs the publishing engine to separate the commentary from the text flow. The note can be displayed in three main ways:

1. In a side margin alongside the referenced sentence;
2. As a traditional footnote at the bottom of the reading pane;
3. Inside an interactive popup modal triggered by clicking an anchor.

In web editions, popup notes and margin sidebars are very popular. Readers can click on an annotated phrase to inspect historical context, dictionary definitions, or authority links. When finished, they close the popup and continue reading smoothly.

```xml
<elementSpec ident="note" mode="change">
  <model behaviour="note">
    <param name="place" value="'margin'"/>
  </model>
</elementSpec>
```

**Vocabulary.** *Note Behaviour* — a rendering rule that decouples annotations from main text and places them in margins, footnotes, or popups. *Interactive Popup* — a lightweight web modal that displays commentary upon clicking an anchor without navigating away. *Margin Sidebar* — a vertical reading column alongside the text used for displaying glosses and commentary.

**Takeaway:** The note behaviour separates commentary from the main text flow, presenting critical explanations in sidebars, footnotes, or interactive popups.

---

## **09 Content**

**Alternate Text Behaviours: Choice and Variations**

Documentary editing frequently requires presenting two views of the same word. Scribes make spelling errors that editors regularize. Historical texts contain archaic abbreviations that editors expand. In TEI XML, these pairings are captured inside the `<choice>` element.

The Processing Model offers the `alternate` behaviour specifically for `<choice>`. The `alternate` behaviour instructs the publishing engine to display one reading as default while making the second reading accessible on demand.

For example, when displaying `<choice><orig>publiq</orig><reg>public</reg></choice>`, you can configure the web edition to show the normalized word "public" in reading view. Readers who hover or click on the word see a small badge displaying the original scribal spelling "publiq".

Alternatively, you can provide an interface toggle that switches the entire document between diplomatic and normalized views. The `alternate` behaviour makes this multi-view publication straightforward without duplicating the underlying text.

```xml
<elementSpec ident="choice" mode="change">
  <model behaviour="alternate">
    <param name="default" value="reg"/>
    <param name="alternate" value="orig"/>
  </model>
</elementSpec>
```

**Vocabulary.** *Alternate Behaviour* — a rendering model that pairs primary and secondary readings, allowing readers to toggle between them. *Interactive Hover Badge* — a visual indicator displaying regularized spellings or expansions when the cursor moves over a word. *Diplomatic View* — a presentation that displays exact physical manuscript spellings and line breaks.

**Takeaway:** The alternate behaviour enables multi-view reading, allowing users to inspect diplomatic spellings and normalized readings from a single encoded text.

---

## **10 Content**

**Tabular and Graphic Behaviours: Tables and Figures**

Historical documents frequently contain non-textual or semi-structured data. Financial records include accounting ledgers. Decrees and letters include official stamps, wax seals, and illustrations. The Processing Model provides dedicated behaviours for these elements.

For structured information encoded in `<table>`, `<row>`, and `<cell>`, the Processing Model supplies matching `table`, `row`, and `cell` behaviours. These compile directly into semantic HTML `<table>` elements with responsive borders and padding.

For facsimiles and illustrations, the `graphic` and `figure` behaviours embed digital images into the reading pane. You pass the image file path or URL to the `url` parameter. The publishing engine generates an HTML `<img>` tag with appropriate dimensions.

You can also pair transcribed text directly with its corresponding facsimile zone. Clicking on a transcribed paragraph highlights the exact region on the high-resolution page image, demonstrating rigorous documentary evidence.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Element</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Behaviour</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Required Parameters</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">HTML Output</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;graphic&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">graphic</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">url, title, width</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;img src="..." alt="..."&gt;</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;table&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">table</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">columns, border</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;table class="..."&gt;</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Graphic Behaviour* — a rendering instruction that embeds digital images and facsimile zones into the document flow. *Table Behaviour* — a rendering rule that formats rows and cells into structured tabular displays. *Facsimile Zone Pairing* — linking a transcribed section directly to coordinates on a manuscript image.

**Takeaway:** The graphic and table behaviours integrate manuscript images, wax seals, and structured accounting ledgers directly alongside transcribed text.

---

## **11 Content**

**Conditional Behaviours: The @predicate Attribute**

An element should not always be rendered in the exact same way. Its visual appearance often depends on its context, its type, or the surrounding elements. The Processing Model handles this flexibility using the `@predicate` attribute.

The `@predicate` attribute contains an XPath expression that tests a condition. If the condition evaluates to true, the model rule applies. If it evaluates to false, the publishing engine skips that rule and checks the next model.

For example, consider the `<note>` element. A brief marginal gloss requires different styling than a lengthy historical commentary note. By testing `@place='margin'` in a predicate, you route marginal notes to a sidebar while routing unassigned notes to footnotes.

You can also use predicates to differentiate categories of commentary. You can apply distinctive color badges to philological notes, historical biographies, and legal intertextual references across your edition.

```xml
<elementSpec ident="note" mode="change">
  <model predicate="@type='philological'" behaviour="note" cssClass="note-lexical"/>
  <model predicate="@type='historical'" behaviour="note" cssClass="note-history"/>
  <model behaviour="note" cssClass="note-default"/>
</elementSpec>
```

**Vocabulary.** *Predicate* — an XPath expression inside a model tag that tests conditions before applying a rendering rule. *Conditional Rendering* — displaying an element differently based on its attributes or document context. *Fallback Model* — the default model without a predicate placed at the end of an element specification to catch remaining cases.

**Takeaway:** The predicate attribute uses XPath expressions to apply different rendering behaviors and styles based on element context and attributes.

---

## **12 Content**

**Multi-Channel Publishing: The @output Attribute**

A major strength of the TEI Processing Model is its support for multi-channel publishing. A digital scholarly edition should not be restricted to a single medium. Scholars need responsive web pages, downloadable PDF facsimiles, and print-ready proofs.

The `@output` attribute allows you to tailor rendering rules to specific publication media. You can assign different models for `@output="web"`, `@output="print"`, or `@output="epub"`.

When compiling for the web, you might render `<ref>` as a clickable hyperlink leading to Wikidata. When compiling for print PDF, you might render that same `<ref>` with a formal printed citation or URL in parentheses.

Because all these rules live inside the same ODD file, you never duplicate your editorial work. A single master TEI file generates both an interactive web edition and an elegant print book.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Output Target</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">@output Value</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Rendering Strategy</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Typical Use Case</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Interactive Web</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">web</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Clickable popups, image zoom, responsive sidebars</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Online public reading interface</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Archival Print PDF</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">print</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Fixed page numbers, bottom footnotes, running headers</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Formal library preservation and print publishing</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Multi-Channel Publishing* — generating multiple distinct media outputs like web, print, and ebook from a single master XML source. *Output Attribute* — an attribute on model tags specifying which media channel a rule targets. *Preservation PDF* — a fixed-layout document optimized for long-term archiving and physical printing.

**Takeaway:** The output attribute targets rendering rules to specific media, allowing one ODD file to generate both interactive websites and archival print PDFs.

---

## **13 Content**

**Formatting with CSS: Linking ODD to Web Styles**

While behaviours define structure, **Cascading Style Sheets (CSS)** control visual aesthetics. CSS dictates fonts, colors, borders, line spacing, and layout positions. The Processing Model connects abstract behaviors to CSS using the `@cssClass` attribute.

When an engine transforms a TEI element, it adds the class specified in `@cssClass` to the resulting HTML tag. For example, `<model behaviour="inline" cssClass="tei-persName">` produces `<span class="tei-persName">`.

You then write clean CSS rules in an external stylesheet. You can define subtle background tints, small-caps fonts, or borders for specific classes. Keeping styling rules in external CSS keeps your ODD schema focused on structural meaning.

This separation makes redesigning your edition simple. If you decide to change your site font or color palette, you edit a single CSS file. You never need to touch your underlying TEI XML or recompile your schemas.

```css
/* External edition stylesheet */
.tei-persName {
  font-weight: 500;
  color: #002d62;
  border-bottom: 1px dotted #c59b27;
}

.tei-placeName {
  font-style: italic;
  color: #0f172a;
}
```

**Vocabulary.** *CSS (Cascading Style Sheets)* — the standard language used to style the visual presentation of HTML web pages. *cssClass Attribute* — an attribute on model tags that assigns CSS class names to generated HTML elements. *External Stylesheet* — a separate .css file containing style rules that apply across an entire website.

**Takeaway:** The cssClass attribute binds ODD model rules to external CSS stylesheets, keeping visual styling modular and easy to update.

---

## **14 Content**

**Modern Web Layouts: CSS Flexbox for Editions**

Historical editions frequently require displaying related content side by side. Editors often want to display a page image directly next to its transcription, or a French primary text next to its English translation.

**CSS Flexbox** is a modern layout system designed for aligning items in rows or columns. By applying `display: flex` to a container, you create a flexible layout that adjusts automatically to different screen widths.

In a bilingual or dual-view edition, Flexbox makes aligning sentences straightforward. You create a container `<div>` with two child columns: one for the primary witness and one for the translation. Flexbox keeps the columns equal in height and cleanly aligned.

Flexbox also handles responsive wrapping. On wide desktop screens, the two texts sit comfortably side by side. On narrow smartphone screens, Flexbox wraps the second column below the first, preserving readability without horizontal scrolling.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Flexbox Property</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Standard Value</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Visual Effect in Edition</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">display</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">flex</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Activates flexible box layout on the parent container</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">flex-direction</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">row / column</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Arranges child panes horizontally in a row or vertically in a column</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">gap</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">24px</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Creates consistent spacing between the side-by-side reading panes</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *CSS Flexbox* — a flexible CSS layout model that arranges child elements along horizontal or vertical axes. *Side-by-Side Reading Pane* — a split-screen display showing image and text or source and translation together. *Responsive Wrapping* — the automatic stacking of side-by-side columns into vertical rows on smaller screens.

**Takeaway:** CSS Flexbox provides an adaptable layout system for presenting manuscript images, transcriptions, and translations in side-by-side reading panes.

---

## **15 Content**

**Grid Layouts: CSS Grid for Edition Headers and Metadata**

While Flexbox is ideal for one-dimensional rows or columns, **CSS Grid** is designed for two-dimensional layouts with rows and columns. In a digital edition, CSS Grid is the best tool for structuring edition headers and metadata panels.

A historical edition header displays diverse information. It presents archival shelfmarks, document dates, repository names, licensing badges, and editorial credits. Displaying this data as a plain bulleted list looks unpolished.

With CSS Grid, you define a structured grid template. You can allocate specific areas for repository details, thumbnail images, and legal badges. Each item snaps into its designated cell, creating a clean card layout.

CSS Grid also makes responsive adjustment easy. On desktop displays, metadata can span three balanced columns. On mobile screens, the grid collapses into a neat single column with one CSS rule.

```css
/* Responsive metadata header grid */
.edition-header-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
  background-color: #f8fafc;
  padding: 20px;
  border: 1px solid #cbd5e1;
}
```

**Vocabulary.** *CSS Grid* — a two-dimensional CSS layout engine that positions elements across defined rows and columns. *Grid Template* — a CSS rule that defines the number, sizes, and names of grid columns and rows. *Metadata Panel* — a structured card display presenting archival and bibliographic details at the top of an edition.

**Takeaway:** CSS Grid structures complex archival metadata and edition headers into polished, multi-column card layouts that adapt across screen sizes.

---

## **16 Content**

**Styling Inline Entities: People, Places, and Dates**

In Modules 8 and 9, you encoded named entities like `<persName>`, `<placeName>`, and `<date>`. You also linked these entities to external Linked Open Data authorities like Wikidata and GeoNames. When publishing, you must decide how to style these elements.

Novice web designers often make the mistake of using garish neon colors for entities. Highlighting every name in bright yellow or purple creates visual noise that distracts readers from the historical text.

Professional editions use subtle typographic styling. You might apply a gentle slate blue color to people, a quiet italic font to places, or a thin dotted underline. The text remains comfortable to read as continuous prose.

You can then add interactive tooltips. When a reader moves their cursor over a person's name, a small popup displays the person's birth dates and a link to their Wikidata profile. This provides immediate scholarly enrichment without visual clutter.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Entity Type</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Recommended CSS Styling</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Interactive Hover Behavior</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Personal Name (&lt;persName&gt;)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Deep navy text (#002d62), subtle dotted underline</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Tooltip with biographical dates and Wikidata URI link</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Place Name (&lt;placeName&gt;)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Soft slate color (#0f172a), italic font style</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Tooltip with geographic coordinates and GeoNames link</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Date (&lt;date&gt;)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Neutral dark text, subtle gray border-bottom</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Tooltip showing normalized ISO date (YYYY-MM-DD)</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Visual Noise* — excessive colors, lines, and highlights that overwhelm the eye and distract from reading. *Interactive Tooltip* — a small information box that appears when hovering over an annotated word. *Subtle Typographic Styling* — using muted colors and gentle underlines rather than garish highlights to indicate markup.

**Takeaway:** Muted typographic styling and interactive tooltips enrich named entities with Linked Open Data without cluttering the reading experience.

---

## **17 Content**

**Styling Documentary Features: Deletions and Additions**

Documentary editing honors the physical reality of the manuscript. Historical authors cross out words, insert phrases above lines, and write in margins. Representing these interventions clearly is a vital test of edition design.

The `<del>` element records deleted text. In CSS, you should render deletions using `text-decoration: line-through`. You can also soften the text color to a muted gray (`#64748b`). This visually signals that the words were cancelled while leaving them legible to scholars.

The `<add>` element records additions. You can format additions using `vertical-align: super` with a slightly smaller font size, imitating handwritten interlinear text. Alternatively, you can surround additions with caret symbols or a soft green border.

Providing an editorial toggle for documentary layers is best practice. Readers who want a clean reading experience can hide cancelled text with one click. Readers conducting genetic textual analysis can view every strikeout in full detail.

```css
/* Documentary editing styles */
.tei-del {
  text-decoration: line-through;
  color: #64748b;
  opacity: 0.85;
}

.tei-add {
  vertical-align: super;
  font-size: 0.85em;
  color: #0f766e;
}
```

**Vocabulary.** *Genetic Textual Analysis* — the study of authorial revisions, drafts, and cancellations to understand how a text evolved. *Strikethrough Rendering* — styling deleted words with a horizontal line across them using text-decoration: line-through. *Interlinear Text* — handwritten words inserted between normal lines of writing.

**Takeaway:** Clear CSS styling for deletions and additions visualizes physical revisions while allowing readers to inspect scribal corrections effortlessly.

---

## **18 Content**

**Cohort Presentation: Ace's French Revolutionary Decree**

Let us examine how these presentation principles apply to the three cohort editions. Ace is editing the 1791 French decree *Loi relative à la fabrication des assignats*. This document was printed by the Imprimerie Royale during the French Revolution.

Ace's edition requires formal legislative presentation. The decree opens with a royal proclamation and legal promulgation formula. Ace should format the royal banner using a centered, high-contrast serif font that evokes 18th-century French typography.

The decree contains numbered articles specifying small denomination currency notes of 5 livres. Ace can style each article with prominent bold headings and numbered bullet badges. This helps modern legal historians compare specific clauses.

Finally, Ace's edition benefits from a dual-column layout. The left column displays the diplomatic transcription, preserving historical long-s characters and 18th-century spelling. The right column displays regularized modern French, allowing instant comparison.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Document Feature</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">TEI Encoding</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Recommended Web Presentation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Royal Title Banner</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;head type="main"&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Centered, uppercase serif header with royal fleur-de-lis separator</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Numbered Decree Articles</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;div type="article" n="1"&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Indented card blocks with bold Roman numeral badges (Article I)</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Bilingual Text Alignment</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;linkGrp type="translation"&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Synchronized two-column Flexbox layout with sentence highlighting</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Promulgation Formula* — formal legal language opening an official decree that declares the law active and binding. *Dual-Column Layout* — a split display presenting diplomatic historical text side by side with modern regularized prose. *Legislative Typography* — formal serif fonts and structural numbering appropriate for official government decrees.

**Takeaway:** Ace's French decree requires formal legislative typography, numbered article cards, and a dual-column display comparing diplomatic and modernized text.

---

## **19 Content**

**Cohort Presentation: Olyvia's Maud Lewis Letter**

Olyvia is editing the 1967 personal letter written by Nova Scotia folk artist Maud Lewis to collector Leonard Kinnear. This document has completely different presentation needs than a royal decree. It is an intimate, handwritten epistolary artifact.

Maud wrote from her tiny house in Marshalltown, Digby County. Her letter was written on personal stationery with irregular line spacing and informal phrasing. Preserving this intimate feel requires warm and informal styling choices.

Olyvia should preserve physical line breaks (`<lb/>`) in her default layout. This retains the rhythm of Maud's handwritten sentences. Maud's phonetic spellings and corrections should be displayed with gentle strikeout styling rather than erased.

Olyvia's web layout should feature a side-by-side view. The left pane displays high-resolution scans of the postal envelope and handwritten pages. The right pane displays the transcription. Olyvia can also embed thumbnail images of Maud's paintings referenced in the letter.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Letter Component</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">TEI Encoding</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Recommended Web Presentation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Postal Stationery Header</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;opener&gt;&lt;dateline&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Right-aligned dateline with vintage postmark badge styling</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Handwritten Lineation</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;lb/&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Preserved line breaks with comfortable, handwritten line spacing</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Artistic References</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;rs type="artwork"&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Clickable links opening thumbnail popups of Maud's painted oxen</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Epistolary Artifact* — a primary historical document consisting of a personal or official written letter. *Postal Stationery* — the physical writing paper, cards, or envelopes used for historical correspondence. *Facsimile-First Layout* — an edition interface that emphasizes direct comparison between manuscript scans and transcription.

**Takeaway:** Olyvia's Maud Lewis edition emphasizes the intimate epistolary artifact, pairing handwritten lineation and physical stationery with folk art popups.

---

## **20 Content**

**Cohort Presentation: Andromeda's 1752 Peace and Friendship Treaty**

Andromeda is editing the 1752 Peace and Friendship Treaty negotiated at Halifax between Mi'kmaw Chief Jean-Baptiste Cope and Nova Scotia Governor Peregrine Hopson. This foundational diplomatic document requires dignified and legally precise presentation.

The treaty consists of eight formal articles establishing peace, hunting rights, and British trade truckhouses. Andromeda should format the articles with clear visual divisions. Each clause should feature its Roman numeral heading and full legal text.

A crucial feature of the treaty is the witness and signature section. Mi'kmaw delegates signed using totem marks, while colonial council members signed their names beside red wax seals. Andromeda's web layout must present these signatures and seal marks clearly.

Andromeda should also implement interactive popup commentary notes. When readers click on historical terms like "truckhouse" or "liberty of hunting," a popup explains eighteenth-century legal definitions and treaty rights jurisprudence.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Treaty Section</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">TEI Encoding</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Recommended Web Presentation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Numbered Treaty Articles</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;div type="article" n="4"&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Spacious numbered legal blocks with gold Roman numeral headings</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Totem Marks &amp; Seals</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;figure&gt;&lt;graphic&gt;&lt;/figure&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Inline graphics displaying scanned totem marks and wax seals</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Legal Commentary</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;note type="legal"&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Interactive side popups explaining treaty rights jurisprudence</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Treaty Clause* — an individual numbered legal article within a formal international or diplomatic agreement. *Totem Mark* — a personal pictographic signature drawn by Indigenous leaders representing their clan or identity. *Wax Seal* — an impression stamped in heated wax on an official document to authenticate legal authority.

**Takeaway:** Andromeda's treaty edition requires dignified legal typography, visual representations of totem marks and seals, and interactive commentary popups.

---

## **21 Content**

**Building Interactive Toggles with HTML and CSS**

A hallmark of modern digital editions is user choice. Different readers visit your site with different goals. A paleographer wants to inspect exact abbreviations. A high school teacher wants modern spelling. A legal researcher wants to highlight commentary notes.

Instead of building three separate websites, you can provide **interactive toggles**. A toggle allows readers to switch visual layers on and off in real time without reloading the page.

You can build lightweight toggles using pure HTML and CSS. By using hidden `<input type="checkbox">` elements, you can change display properties based on whether the checkbox is checked. For example, checking "Show Normalized Spelling" hides `<orig>` and displays `<reg>`.

Alternatively, a few lines of clean JavaScript can toggle CSS classes on the main document container. This provides an intuitive interface with clickable buttons at the top of your reading pane.

```html
<!-- View control toolbar -->
<div class="edition-toolbar">
  <button onclick="toggleView('diplomatic')">Diplomatic View</button>
  <button onclick="toggleView('normalized')">Normalized View</button>
  <button onclick="toggleNotes()">Toggle Commentary</button>
</div>
```

**Vocabulary.** *View Toggle* — an interactive user control that switches between different visual rendering modes of a text. *Layered Presentation* — designing an interface where distinct editorial layers can be displayed or hidden on demand. *Zero-Reload Interface* — updating visual layouts instantly in the browser without making a new request to a server.

**Takeaway:** Interactive toggles give readers control over their reading experience, allowing them to switch between diplomatic and normalized views effortlessly.

---

## **22 Content**

**Typography for Historical Texts: Hierarchy and Readability**

Web typography directly impacts how long people will engage with your scholarship. Reading 18th-century prose or handwritten letters requires concentration. Poor typographic choices make historical texts exhausting to read.

Good typography begins with choosing appropriate typefaces. For historical editions, high-quality serif fonts like Georgia, Garamond, or EB Garamond are ideal. Serif fonts have distinctive letter strokes that guide the human eye smoothly across lines of text.

Spacing is equally critical. You should maintain a generous line height of approximately `1.6` to `1.8`. Lines that are packed too tightly cause readers to lose their place. Paragraph margins should provide clear breathing room between thoughts.

Finally, ensure sufficient color contrast. Avoid harsh pure black text on pure white backgrounds, which causes glare. A deep charcoal (`#0f172a`) on an off-white or soft cream background (`#f8fafc`) creates an elegant reading environment that satisfies WCAG accessibility standards.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Typographic Property</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Recommended Value</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Pedagogical Rationale</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Font Family</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">EB Garamond, Georgia, serif</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Evokes historical print culture while maintaining high digital clarity</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Line Height</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">1.65 (165% of font size)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Prevents line collision and supports sustained reading comfort</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Measure (Line Length)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">65 to 75 characters per line</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Optimal reading width; prevents eye fatigue across widescreen monitors</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Measure* — the horizontal length of a line of text, ideally between 65 and 75 characters for optimal reading comfort. *Line Height* — the vertical space between baseline lines of text. *WCAG Contrast Standards* — international accessibility guidelines requiring sufficient contrast between text and background colors.

**Takeaway:** Thoughtful typography with serif typefaces, generous line height, and balanced contrast ensures sustained reading comfort for historical editions.

---

## **23 Content**

**Responsive Design: Supporting Mobile and Desktop**

Today, more than half of all web traffic occurs on mobile devices. Students, researchers, and museum visitors frequently access digital editions from smartphones and tablets. If your edition only works on a giant desktop monitor, half your audience cannot use it.

**Responsive web design** means designing layouts that adapt gracefully to any screen size. You implement responsive design using CSS **media queries** (`@media`). Media queries detect the screen width and apply tailored style rules.

On a wide desktop monitor, a split-screen view works wonderfully. The manuscript facsimile sits on the left, and the transcription sits on the right. Both panes have plenty of room to breathe.

On a smartphone screen, a split view becomes unusable because each column would be only a few inches wide. Using a media query, you instruct the layout to stack the facsimile above the text. Readers scroll down naturally, enjoying both images and text without pinching and zooming.

```css
/* Responsive media query for mobile screens */
@media (max-width: 768px) {
  .edition-container {
    flex-direction: column;
  }
  .facsimile-pane, .text-pane {
    width: 100%;
  }
}
```

**Vocabulary.** *Responsive Design* — the practice of designing web layouts that adapt seamlessly to smartphones, tablets, and desktop computers. *Media Query* — a CSS technique that applies style rules only when specific device conditions like screen width are met. *Horizontal Pinch-Zoom* — an awkward mobile user experience where users must zoom in to read tiny side-by-side text columns.

**Takeaway:** Responsive design uses CSS media queries to stack side-by-side reading panes vertically on mobile screens, ensuring universal accessibility.

---

## **24 Content**

**Accessibility (a11y) in Digital Textual Editions**

Accessibility in web design means ensuring that everyone, including people with visual, auditory, or motor disabilities, can read and navigate your website. In digital humanities, accessibility is an ethical commitment to open scholarship.

The first step in accessibility is using **semantic HTML**. Instead of building your entire page out of generic `<div>` tags, use meaningful elements like `<header>`, `<main>`, `<article>`, `<aside>`, and `<footer>`. Screen readers use these tags to help blind users navigate between sections.

Second, provide descriptive **alt text** for all images. An image tag like `<img src="treaty.jpg" alt="1752 Peace and Friendship Treaty manuscript page showing wax seals">` allows screen readers to describe the artifact to visually impaired scholars.

Third, ensure full **keyboard navigation**. Every interactive button, popup note, and view toggle must be reachable using the Tab key and activatable with the Enter or Space key. Never rely solely on mouse clicks for essential scholarship.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Accessibility Feature</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Technical Implementation</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Beneficiary</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Semantic Structure</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">&lt;main&gt;, &lt;article&gt;, &lt;aside&gt;, &lt;nav&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Screen reader users navigating page landmarks</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Descriptive Alt Text</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">alt="Physical description of manuscript scan"</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Users with visual impairments or slow connections</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Keyboard Navigability</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">tabindex="0", :focus outline styles</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Users navigating via keyboard without a mouse</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Accessibility (a11y)* — the design of software and web interfaces to be usable by people of all abilities and disabilities. *Screen Reader* — assistive software that reads aloud web content and navigation landmarks for visually impaired users. *Semantic HTML* — HTML elements that convey their structural role and meaning rather than just visual styling.

**Takeaway:** Accessible editions use semantic HTML landmarks, descriptive alt text, and full keyboard navigation to ensure all scholars can explore historical documents.

---

## **25 Content**

**Web Components and TEI Publisher**

In modern digital publishing platforms, such as **TEI Publisher**, developers use **Web Components**. Web Components are reusable custom HTML tags that encapsulate complex interactive behaviors into single elements.

Instead of writing hundreds of lines of custom JavaScript to build a facsimile image viewer, you insert a custom tag like `<pb-facsimile>`. The component automatically handles deep zooming, coordinate panning, and image tile loading.

Similarly, a tag like `<pb-view>` connects directly to an ODD file. It takes a TEI document, sends it to the processing engine, and renders the styled output inside the web page.

Web Components make digital edition design modular. You assemble your reading interface using pre-built, robust components. This approach saves hundreds of hours of coding while delivering professional features.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Web Component</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Built-In Function</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Underlying Technology</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;pb-view&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Renders styled TEI XML using ODD processing models</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">TEI Processing Model and XQuery engine</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;pb-facsimile&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Interactive deep-zoom pan and zoom image viewer</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">OpenSeadragon and IIIF Image API</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-family: monospace;">&lt;pb-timeline&gt;</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Interactive historical timeline showing document dates</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">SVG graphics and structured TEI date events</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Web Components* — a suite of standard web platform technologies allowing creation of reusable custom HTML elements. *TEI Publisher* — an open-source publishing framework that transforms TEI documents using the Processing Model. *IIIF (International Image Interoperability Framework)* — an open standard for delivering high-resolution manuscript images over the web.

**Takeaway:** Web Components package complex interactive features like deep-zoom image viewers and ODD renderers into reusable custom HTML tags.

---

## **26 Content**

**Static Site Generation: Minimal Computing for Editions**

When publishing a digital project, scholars must consider its long-term survival. Complex websites that rely on active databases and server-side software often break after a few years. When server security updates occur or hosting budgets expire, database-driven sites go offline.

To prevent this decay, digital humanists embrace **minimal computing**. A primary minimal computing strategy is **static site generation**. Instead of running a live database server, you pre-compile your entire edition into plain HTML, CSS, and JavaScript files.

Static files do not require an active database or server runtime. They can be hosted on simple, free platforms like **GitHub Pages** or institutional web servers. A static website is virtually immune to database security vulnerabilities.

Most importantly, static editions last for decades. A folder of well-written HTML, CSS, and images will render just as cleanly in thirty years as it does today. Minimal computing ensures your scholarship endures.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Architecture</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Hosting Infrastructure</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Security Risk</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Long-Term Durability</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Dynamic Database Edition</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">PHP/MySQL server or eXist-db database</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">High; requires regular security patches and server upkeep</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Low; breaks when server versions or databases drift</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Static Minimal Edition</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Plain files on GitHub Pages or static web storage</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">None; no database or server-side execution</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Decades; plain HTML and CSS remain universally supported</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Minimal Computing* — a digital humanities philosophy emphasizing simple, durable, and sustainable technologies with low infrastructure demands. *Static Site Generation* — pre-compiling web pages into plain HTML, CSS, and JS files that run without an active server database. *GitHub Pages* — a free hosting service that serves static websites directly from a GitHub code repository.

**Takeaway:** Static site generation embodies minimal computing, producing durable HTML files that survive for decades without server maintenance or database costs.

---

## **27 Content**

**Previewing Your Edition Locally in VS Code**

Before publishing your edition to the global web, you must test its visual presentation locally. You need an environment where you can edit styles and see the results instantly without uploading files to a remote server.

In **VS Code**, the most useful tool for local testing is the **Live Server** extension. Live Server starts a lightweight local web server on your machine with one click. When you open your edition HTML file in Live Server, it opens in your web browser at a local address like `http://127.0.0.1:5500`.

Whenever you save a change to your HTML or CSS file in VS Code, Live Server automatically refreshes the browser page. This live reload feature allows you to fine-tune margins, fonts, and colors rapidly.

Inside your browser, you can press `F12` to open the **Developer Tools**. The browser inspector allows you to inspect specific HTML elements, test CSS changes in real time, and diagnose why a layout rule is not behaving as expected.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Tool</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Environment</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Primary Function</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Live Server Extension</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">VS Code</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Launches local server with automatic browser refresh on file save</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Browser DevTools (F12)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Chrome / Firefox</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Inspects DOM elements, debugs CSS rules, and simulates mobile screens</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Live Server* — a development tool that hosts files locally and automatically refreshes connected browsers upon saving edits. *Browser DevTools (F12)* — built-in diagnostic tools inside web browsers used to inspect HTML elements and test CSS styles live. *Local Development Loop* — the rapid cycle of editing code, saving, and observing instant updates on a local test server.

**Takeaway:** Using VS Code Live Server and browser developer tools enables rapid local testing and fine-tuning of your digital edition layouts.

---

## **28 Content**

**Quality Gate: Validating HTML and CSS Outputs**

Before your digital edition is ready for publication, you must pass a final quality audit. Just as you validated your TEI XML against schemas, you must validate your compiled web presentation.

A robust quality audit checks four essential dimensions:

1. **HTML Well-Formedness:** Verify that all HTML tags close correctly and that nesting rules are obeyed.
2. **CSS Linkage:** Confirm that all external stylesheets load without 404 errors and that class names match your ODD declarations.
3. **Asset Paths:** Test every image URL to verify that facsimile scans and seal graphics display properly.
4. **Interactive Pointers:** Click every commentary note and entity link to verify that anchor IDs resolve without broken references.

Running these checks prevents embarrassing glitches when users visit your site. Catching broken paths or overlapping text early ensures your edition reflects rigorous scholarly craftsmanship.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Audit Area</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Common Novice Defect</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Verification Method</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Image Assets</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Broken relative path (e.g. missing images/ folder prefix)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Inspect browser network tab (F12) for 404 HTTP errors</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Commentary Popups</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Clicking note does nothing because target ID has a typo</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Manual click test on all 5 commentary anchors</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Mobile Layout</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Horizontal scrolling required on narrow phone screens</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Test using browser responsive device toolbar (Ctrl+Shift+M)</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Quality Audit* — a systematic pre-publication review verifying markup validity, link integrity, and visual presentation. *Asset Resolution* — the successful loading of linked external files like images and stylesheets without 404 errors. *Broken Pointer* — an interactive link or reference pointing to an anchor ID that does not exist in the document.

**Takeaway:** A pre-publication quality audit verifies HTML validity, image asset paths, commentary pointers, and mobile responsiveness across your entire edition.

---

## **29 Content**

**Today's Studio Lab: Designing Your Edition Styles**

In today's studio lab in Mulroney Hall 3032, you will transition from abstract markup to visual presentation. You will create the styling rules that govern your project's web appearance.

Your lab workflow follows three focused steps:

1. **Define Your Style Rules:** In your project stylesheet (`style.css`), establish your typographic palette. Choose a clean serif body font, set line height to 1.65, and define subtle styles for personal names, place names, and dates.
2. **Implement Feature Styling:** Configure styles tailored to your document. Ace creates dual-column bilingual alignment. Olyvia styles handwritten line breaks and strikeout deletions. Andromeda formats treaty clauses with Roman numerals and seal graphics.
3. **Test in Browser:** Launch Live Server in VS Code. Inspect your styled edition in your browser and test your interactive note popups.

I will circulate during the lab to help you fine-tune CSS selectors and test responsive layouts.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Step</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Student Action in VS Code</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Deliverable Target</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Step 1: Typography</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Configure body font, line height, and entity classes in style.css</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Base typography stylesheet established</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Step 2: Document Layout</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Build Flexbox columns, note popups, and documentary styles</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Document-specific presentation rules active</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Step 3: Verification</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Launch Live Server and audit layout across desktop and mobile views</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Zero layout glitches; verified local preview</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Styling Rules* — CSS declarations specifying color, typography, spacing, and borders for specific element classes. *Local Preview* — viewing and interacting with a website hosted temporarily on your own computer before uploading it. *Feature Styling* — designing custom visual rules for unique documentary traits like seals, deletions, or parallel columns.

**Takeaway:** Today's lab guides you to define typographic rules, implement document-specific layouts, and verify your presentation locally in VS Code.

---

## **30 Content**

**Summary and Looking Ahead to Friday's Milestone**

Today, you crossed a major milestone in digital textual scholarship. You explored how the TEI Processing Model replaces thousands of lines of fragile procedural code with standardized, declarative rendering rules.

You discovered how ODD files serve as single sources of truth, uniting human guidelines, validation schemas, and presentation stylesheets. You also learned how modern web standards like CSS Flexbox and Grid structure primary facsimiles, transcriptions, and commentary into elegant reading interfaces.

Remember the university schedule notice for this week: Thursday is the StFX Patronal Feast Day, so classes do not meet. On Friday, December 4, StFX runs on a Wednesday timetable. Our final class meeting of the semester will take place at **10:30 AM in Mulroney Hall 3032**.

On Friday, we complete our capstone publication studio. We will explore multi-modal publishing, minimal computing, FAIR open data principles, and long-term archiving with Zenodo DOIs and GitHub Releases. Bring your styled edition, and let us prepare for public release.

<table style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;">
  <thead>
    <tr style="background-color: #002d62; color: #ffffff;">
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Meeting</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Date &amp; Time</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Focus Topic</th>
      <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Capstone Deliverable</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Meeting #35 (Today)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Wed Dec 2 &middot; 10:30 AM</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">TEI Processing Model, ODD, and CSS presentation</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Styled edition preview in Live Server</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Meeting #36 (Friday)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Fri Dec 4 &middot; 10:30 AM (Wed schedule)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Multi-modal publishing, FAIR data, Zenodo archiving</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Zenodo deposit &amp; GitHub release portfolio</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Patronal Feast Day* — an official university holiday celebrating St. Francis Xavier on December 3, during which classes are suspended. *Wednesday Timetable* — an academic scheduling practice where Friday classes follow Wednesday meeting times to balance course contact hours. *Long-Term Archiving* — depositing research datasets into trusted repositories with permanent digital identifiers.

**Takeaway:** Today you styled your digital edition with modern web layouts; on Friday at 10:30 AM, we conclude our capstone studio with multi-modal archiving and public release.
