# Lesson 13.2 — The TEI Processing Model, ODD, and TEI Publisher Transformation Pipelines

*RELS 398 / ENGL 398 · Topic 13: Publication · Meeting #35 (Wed Dec 2)*

***Studio and publication assembly week (no three-step cycle).** Today you explore the TEI Processing Model, author an ODD customization (`<model>`, `<modelSequence>`, `<modelGrp>`, `@behaviour`, `@predicate`), and configure TEI Publisher transformation pipelines to automate publication across web and print media.*

---

## **01 Content**

**The Evolution of TEI Publication: From Ad-Hoc XSLT to Declarative Models**

For the first two decades of the Text Encoding Initiative (TEI), publishing a digital scholarly edition required writing thousands of lines of bespoke **XSLT (Extensible Stylesheet Language Transformations)** stylesheets. While XSLT is a powerful, Turing-complete language for transforming XML trees into HTML or PDF layouts, relying on custom XSLT stylesheets introduced severe systemic problems into digital editing projects (Turska et al., 2016; Stadler et al., 2016).

In practice, bespoke XSLT stylesheets became massive, unmaintainable "black boxes." Project programmers wrote custom templates for standard TEI elements—such as `<choice>`, `<app>`, `<persName>`, or `<pb>`—interweaving document parsing logic, complex XPath queries, and hard-coded HTML presentation tags. When the project's TEI schema evolved, or when the editor wanted to add a new publication format (such as an archival print PDF or an EPUB), the XSLT stylesheets had to be rewritten by hand (Turska et al., 2016; Driscoll & Pierazzo, 2016).

| Era | Primary Transformation Mechanism | Architectural Characteristic | Major Vulnerability |
| --- | --- | --- | --- |
| **Legacy Era (1995–2015)** | Monolithic XSLT 1.0/2.0 stylesheets | Procedural, ad-hoc, hard-coded HTML/LaTeX | Brittle; schema and presentation drift apart |
| **Modern Era (2016–Present)** | TEI Processing Model in ODD | Declarative, abstract behaviours in schema | Standardized; one ODD compiles to all media |

The fundamental limitation of legacy XSLT was the total lack of interoperability. Because every digital edition used idiosyncratic XSLT templates, stylesheets could not be shared across institutions or reused by other scholars. An edition was effectively married to the specific software scripts written by its original developer. If that developer left the institution or if the server environment was upgraded, the transformation pipeline broke, leaving the edition unrenderable (Turska et al., 2016; Sahle, 2016).

To solve this crisis, the TEI Consortium developed the **TEI Processing Model**, introducing a declarative standard that formalizes how XML elements should be presented across diverse media directly within the project's schema (TEI Consortium, 2026; Turska et al., 2016).

**Vocabulary.** *XSLT (Extensible Stylesheet Language Transformations)* — an XML-based language used for transforming XML documents into other formats such as HTML or PDF. *Declarative modeling* — specifying *what* should be done abstractly rather than scripting *how* to execute every procedural step. *Transformation brittleness* — the tendency of complex custom stylesheets to break when minor changes are made to the underlying schema.

**Takeaway:** The TEI Processing Model replaces brittle, custom XSLT stylesheets with standardized, declarative rendering rules embedded directly in the schema.

---

## **02 Content**

**The Myth of Presentation in Digital Humanities**

In digital textual scholarship, a foundational dogma has long asserted that **encoding must strictly separate semantic content from visual presentation** (Coombs et al., 1987; Renear, 2004). Editors were taught that XML tags should describe what a text *is* (e.g., `<persName>`, `<title>`, `<foreign>`), never how it *looks* on a page (e.g., `<i>`, `<b>`, `font-size: 12pt`).

While this separation is philosophically sound for content modeling, it created a severe blind spot in digital humanities practice, termed by Magdalena Turska, James Cummings, and Sebastian Rahtz as the **"Myth of Presentation"** (Turska et al., 2016):

1. The belief that an encoded XML text is completely independent of its visual output;
2. The assumption that presentation is a trivial, secondary detail that can be handled arbitrarily by external programmers after the editing is complete.

In reality, scholarly editing and visual presentation are deeply intertwined. When an editor encodes a deleted line (`<del>`), an interlinear addition (`<add>`), or a critical apparatus entry (`<app>`), they make interpretive decisions that directly imply specific visual reading behaviors (Pierazzo, 2016; Turska et al., 2016). For example, a genetic cancellation is not merely an abstract data point; it is a historical stroke that must be presented as a strikethrough in a diplomatic view and suppressed in a reading view.

| Fallacy | Scholarly Reality | Architectural Solution |
| --- | --- | --- |
| "Encoding has nothing to do with presentation." | Editorial markup implies explicit visual reading behaviors. | Declare abstract rendering behaviours in the ODD schema. |
| "Presentation can be outsourced to ad-hoc XSLT." | Custom XSLT obscures editorial intent and creates maintenance debt. | Use standardized `<model>` elements in TEI Processing Model. |
| "A text has only one valid visual display." | Different audiences require diplomatic, reading, and apparatus views. | Use `@predicate` and `@output` to generate multi-modal outputs. |

The TEI Processing Model does not violate the separation of content and presentation; rather, it formalizes presentation as a **first-class scholarly dimension of the text**. By encoding rendering intentions as abstract, machine-readable behaviors within the schema, the editor retains intellectual control over how their scholarship is communicated across every medium (Turska et al., 2016; Pierazzo, 2016).

**Vocabulary.** *Myth of presentation* — the mistaken belief that textual encoding is entirely detached from visual rendering and that presentation can be treated as an arbitrary afterthought. *First-class scholarly dimension* — treating visual layout and interaction as integral to the editorial argument rather than an auxiliary technical detail. *Genetic cancellation* — deleted text in a manuscript witness reflecting an authorial or scribal revision.

**Takeaway:** Visual presentation is an integral dimension of scholarly communication that must be formalized declaratively within the edition's schema.

---

## **03 Content**

**The ODD (One Document Does It All) Philosophy: Unified Specification**

The TEI framework manages schemas, documentation, and transformation pipelines through a literate programming architecture called **ODD (One Document Does It All)** (Burnard & Rahtz, 2004; TEI Consortium, 2026).

Before ODD, digital editing projects were forced to maintain three disconnected files:

1. A prose manual explaining the project's editorial rules to transcribers;
2. A formal XML schema (such as a DTD, XSD, or Relax NG schema) validating the tags;
3. A set of XSLT stylesheets rendering the XML into HTML or PDF.

Inevitably, these three files drifted apart. An editor would update the prose guidelines, forget to modify the Relax NG schema, and the programmer would write XSLT rules that contradicted both (Burnard & Rahtz, 2004).

ODD solves this fragmentation by unifying all three components into a **single XML master file**:

```xml
<teiHeader> ... </teiHeader>
<text>
  <body>
    <div>
      <head>Editorial Guidelines and Specification for RELS 398 Digital Edition</head>
      <p>Human-readable documentation explaining editorial policies...</p>
    </div>
    <schemaSpec ident="rels398-edition" start="TEI">
      <moduleRef key="tei"/>
      <moduleRef key="core"/>
      <moduleRef key="textstructure"/>
      <moduleRef key="textcrit"/>
      <elementSpec ident="choice" mode="change">
        <!-- Schema constraints, Schematron rules, and Processing Models -->
      </elementSpec>
    </schemaSpec>
  </body>
</text>
```

| ODD Component | TEI Element | Functional Output Generated |
| --- | --- | --- |
| **Prose Documentation** | `<body>`, `<div>`, `<p>` | Human-readable HTML/PDF project editing manual |
| **Schema Declarations** | `<schemaSpec>`, `<elementSpec>` | Relax NG (`.rng`), Schematron (`.sch`), and XSD schemas |
| **Processing Model** | `<model>`, `<modelSequence>` | Compiled XSLT 3.0, XQuery, and CSS transformation code |

An ODD file is processed by an ODD compiler (such as Roma, OxGarage, or TEI Publisher). The compiler extracts the formal declarations to generate the validation schemas and executes the processing models to generate the publication stylesheets. Documentation, validation, and rendering remain perpetually in sync (Burnard & Rahtz, 2004; Turska et al., 2016).

**Vocabulary.** *ODD (One Document Does It All)* — a TEI XML format that integrates human-readable prose documentation, formal validation schemas, and output processing models in a single file. *Literate programming* — a programming paradigm where code is interwoven with natural language documentation. *Schema generation* — compiling an ODD specification into formal Relax NG or Schematron schemas.

**Takeaway:** An ODD file serves as the single source of truth, generating human-readable guidelines, validation schemas, and publication transformations from one file.

---

## **04 Content**

**TEI P5 Chapter 22: The Architecture of the TEI Processing Model**

Formalized in Chapter 22 of the TEI P5 Guidelines, the **TEI Processing Model** defines a standardized vocabulary for expressing rendering semantics within an ODD specification (TEI Consortium, 2026; Turska et al., 2016).

The Processing Model rests on a crucial architectural insight: while there are hundreds of distinct XML elements in the TEI vocabulary (e.g., `<p>`, `<head>`, `<persName>`, `<foreign>`, `<app>`, `<lem>`, `<note>`), there are only a small number of **abstract visual and structural behaviours** that a publisher ever applies to a document (Turska et al., 2016).

For example:

- A paragraph (`<p>`) behaves as a block of prose with vertical margins;
- A heading (`<head>`) behaves as a bold block heading;
- An emphasis tag (`<emph>`) or foreign word (`<foreign>`) behaves as inline italicized text;
- An apparatus reading (`<rdg>`) or scholarly gloss (`<note>`) behaves as a footnote, margin note, or interactive popup;
- A physical image reference (`<graphic>`) behaves as an embedded image.

| Processing Model Component | TEI Element | Core Function |
| --- | --- | --- |
| **Behavior Instruction** | `<model>` | Maps a TEI element to an abstract rendering behavior |
| **Execution Sequence** | `<modelSequence>` | Executes multiple `<model>` instructions in strict linear order |
| **Conditional Grouping** | `<modelGrp>` | Groups related `<model>` rules sharing predicates or output targets |
| **Dynamic Parameter** | `<param>` | Passes contextual data (e.g., URLs, alternate readings) to the behavior |
| **Output Rendition** | `<outputRendition>` | Attaches declarative CSS styling rules to the rendered output node |

Instead of writing custom XSLT code to generate specific HTML `<div>` or `<span>` tags, the editor uses `<model>` to declare the element's abstract behavior. The underlying publishing engine (such as TEI Publisher) automatically translates that abstract behavior into the correct target syntax for the web, print, or mobile device (Turska et al., 2016; Stadler et al., 2016).

**Vocabulary.** *TEI Processing Model* — the standardized TEI framework mapping XML elements to abstract rendering behaviors. *Abstract behaviour* — a platform-independent rendering operation (such as `inline`, `block`, or `note`) decoupled from specific HTML or LaTeX syntax. *Rendering semantics* — the formal rules defining how structured data should be visually presented.

**Takeaway:** The TEI Processing Model maps hundreds of diverse TEI elements onto a compact set of abstract, platform-agnostic rendering behaviors.

---

## **05 Content**

**The Anatomy of an ODD File: `<schemaSpec>`, `<elementSpec>`, and `<model>`**

To configure the TEI Processing Model, an editor modifies the element specifications inside the `<schemaSpec>` section of their ODD file (TEI Consortium, 2026; Burnard & Rahtz, 2004).

The hierarchy of an ODD transformation specification follows four nesting tiers:

```xml
<schemaSpec ident="rels398-publication" start="TEI">
  <!-- Module References -->
  <moduleRef key="tei"/>
  <moduleRef key="core"/>
  <moduleRef key="textcrit"/>

  <!-- Element Specification Customization -->
  <elementSpec ident="persName" mode="change">
    <desc>Personal names linked to VIAF / Wikidata authority records.</desc>
    
    <!-- Model Rule 1: Interactive Web View with Tooltip -->
    <model predicate="$mode = 'web'" behaviour="link">
      <param name="uri" value="@ref"/>
      <outputRendition>color: #1a5276; font-weight: bold; text-decoration: underline;</outputRendition>
    </model>
    
    <!-- Model Rule 2: Print PDF View (Plain Inline Text) -->
    <model predicate="$mode = 'print'" behaviour="inline">
      <outputRendition>font-variant: small-caps;</outputRendition>
    </model>
  </elementSpec>
</schemaSpec>
```

| ODD Structural Tier | XML Element | Function in Architecture |
| --- | --- | --- |
| **Tier 1: Schema Root** | `<schemaSpec>` | Defines the edition's schema name, namespace, and active modules |
| **Tier 2: Module Reference** | `<moduleRef>` | Ingests standard TEI chapters (core, textstructure, textcrit, etc.) |
| **Tier 3: Element Customization** | `<elementSpec>` | Customizes a specific TEI tag (`@mode="change"` or `@mode="add"`) |
| **Tier 4: Model Rule** | `<model>` | Declares the conditional behavior, parameters, and CSS styling for that tag |

In the example above, the `<persName>` tag is customized with two distinct `<model>` rules: in web mode, it renders as a clickable hyperlink pointing to the authority URI in `@ref`; in print mode, it renders as clean inline text typeset in small capitals (Turska et al., 2016; Barzaghi et al., 2025).

**Vocabulary.** `<schemaSpec>` — TEI container defining a custom schema and its included modules. `<elementSpec>` — TEI container documenting and modifying the validation and rendering rules for a specific element. `@mode="change"` — ODD attribute indicating that an existing TEI element's default definition is being customized.

**Takeaway:** An ODD transformation pipeline customizes elements inside `<elementSpec>` by attaching conditional `<model>` rules that govern rendering.

---

## **06 Content**

**Understanding Processing Model Behaviors: The Standard Repertoire**

The power of the TEI Processing Model lies in its standardized repertoire of **behaviours**. A behaviour is a predefined, abstract presentation function implemented by the publishing engine (TEI Consortium, 2026; Turska et al., 2016).

The TEI P5 Guidelines define standard behaviors spanning all common document structures:

| Category | Standard Behaviours | Primary Function |
| --- | --- | --- |
| **Basic Layout** | `inline`, `block`, `paragraph`, `heading`, `break` | Formatting text flows, line divisions, and structural headings |
| **Interactive & Annotation** | `alternate`, `note`, `link`, `cit` | Popovers, tooltips, footnotes, margin notes, and hyperlinks |
| **Tabular & Structural** | `table`, `row`, `cell`, `list`, `item` | Data tables, apparatus grids, and ordered/unordered lists |
| **Media & Figures** | `graphic`, `figure` | Digital facsimile images, SVG vector charts, and figures |
| **Document Control** | `document`, `metadata`, `title`, `index`, `omit` | Top-level wrappers, metadata ingestion, and suppressing tags |

Because these behaviors are abstract, they behave appropriately for the target medium:

- In an **HTML5 web environment**, the `note` behaviour generates a floating popover, a drawer, or a clickable superscript footnote;
- In a **PDF/LaTeX environment**, the same `note` behaviour automatically compiles to a bottom-of-the-page footnote (`\footnote{...}`) or a multi-tier critical apparatus note (`\Afootnote{...}`) (Turska et al., 2016; Fischer, 2020).

The editor never writes low-level target code; they simply invoke the appropriate abstract behaviour.

**Vocabulary.** *Behaviour* — an abstract rendering function defined in the TEI Processing Model. `omit` — a behaviour instructing the transformation engine to suppress an element and its contents entirely. *Medium-appropriate rendering* — the automatic adaptation of an abstract behaviour to the physical or digital affordances of the output channel.

**Takeaway:** The TEI Processing Model provides standard behaviours covering layout, annotations, tables, graphics, and document control.

---

## **07 Content**

**The `@behaviour` Vocabulary: `paragraph`, `heading`, `inline`, and `block`**

The most common structural elements in historical and critical editions are mapped using four fundamental behaviours: `paragraph`, `heading`, `inline`, and `block` (TEI Consortium, 2026; Turska et al., 2016).

#### 07.1 The `paragraph` and `heading` Behaviours

- `paragraph`: Formats the element as a distinct block of prose text, typically with top/bottom vertical margins and optional first-line indents. Mapped to `<p>` and `<ab>` (anonymous blocks).
- `heading`: Formats the element as a section title, automatically computing heading levels ($H_1, H_2, H_3$) based on the nesting depth of the enclosing `<div>`. Mapped to `<head>`.

```xml
<elementSpec ident="p" mode="change">
  <model behaviour="paragraph">
    <outputRendition>text-align: justify; line-height: 1.6; margin-bottom: 1em;</outputRendition>
  </model>
</elementSpec>

<elementSpec ident="head" mode="change">
  <model behaviour="heading">
    <param name="level" value="count(ancestor::div)"/>
    <outputRendition>font-family: 'Cinzel', serif; font-weight: bold; color: #2c3e50;</outputRendition>
  </model>
</elementSpec>
```

#### 07.2 The `inline` and `block` Behaviours

- `inline`: Renders the element within the continuous horizontal text flow without introducing line breaks. Used for highlighting, foreign words, scribal hands, and semantic tags (`<foreign>`, `<title>`, `<hi>`, `<persName>`).
- `block`: Formats the element as an isolated vertical container spanning the full width of the parent, but without paragraph-specific indentation. Used for block quotations, poetry stanzas, and apparatus containers (`<quote>`, `<lg>`, `<standOff>`).

| TEI Element | Assigned `@behaviour` | Web HTML Result | PDF / Print Result |
| --- | --- | --- | --- |
| `<p>` | `paragraph` | `<p class="tei-p">` | Paragraph with 1em margin |
| `<head>` | `heading` | `<h1-h6 class="tei-head">` | Bold section title |
| `<foreign>` | `inline` | `<span class="tei-foreign">` | Italicized inline text |
| `<quote>` | `block` | `<blockquote class="tei-quote">` | Indented quotation block |

**Vocabulary.** `paragraph` — behaviour formatting text as a prose paragraph. `heading` — behaviour formatting text as a hierarchical section title. `inline` — behaviour rendering content inside the current text line. `block` — behaviour formatting content as a standalone vertical block.

**Takeaway:** Basic document architecture is established by mapping prose to `paragraph`, titles to `heading`, phrase-level markup to `inline`, and containers to `block`.

---

## **08 Content**

**Modeling Complex Structures: `table`, `row`, `cell`, and `list`**

Digital critical editions frequently present tabular and structured data, including collation alignment matrices, token frequency tables, and list of witnesses. The TEI Processing Model handles these via structural behaviors: `table`, `row`, `cell`, `list`, and `item` (TEI Consortium, 2026; Camps et al., 2019).

When mapping tables:

- `table`: Wraps the entire grid container;
- `row`: Formats each horizontal line of cells;
- `cell`: Formats individual data cells, taking parameters for column spans (`@cols`) and row spans (`@rows`).

```xml
<elementSpec ident="table" mode="change">
  <model behaviour="table">
    <outputRendition>border-collapse: collapse; width: 100%; margin: 1.5em 0;</outputRendition>
  </model>
</elementSpec>

<elementSpec ident="row" mode="change">
  <model predicate="@role = 'label'" behaviour="row">
    <outputRendition>background-color: #f2f4f4; font-weight: bold; border-bottom: 2px solid #333;</outputRendition>
  </model>
  <model behaviour="row"/>
</elementSpec>

<elementSpec ident="cell" mode="change">
  <model behaviour="cell">
    <param name="cols" value="@cols"/>
    <param name="rows" value="@rows"/>
    <outputRendition>padding: 8px 12px; border: 1px solid #ddd;</outputRendition>
  </model>
</elementSpec>
```

| Structured Tag | Target Behaviour | Critical Function in Edition |
| --- | --- | --- |
| `<table>` | `table` | Renders collation alignment matrices and metadata summaries |
| `<row>` | `row` | Distinguishes header rows (`@role="label"`) from data rows |
| `<cell>` | `cell` | Encapsulates witness readings and token values |
| `<list>` | `list` | Renders `<listWit>` catalogues and commentary taxonomies |
| `<item>` | `item` | Formats individual manuscript witness entries |

Mapping these elements through the Processing Model guarantees that tables remain fully responsive on mobile screens while compiling into typographically clean tables in print PDFs (Turska et al., 2016).

**Vocabulary.** `table` — behaviour generating a tabular data grid. `row` — behaviour generating a table row. `cell` — behaviour generating an individual table cell with span support. `list` — behaviour generating an ordered or unordered list container.

**Takeaway:** Structured collation tables and witness lists are mapped using the `table`, `row`, `cell`, and `list` behaviours.

---

## **09 Content**

**Handling Interactive Phenomena: The `alternate` Behaviour for `<choice>`**

One of the greatest achievements of the TEI Processing Model is the **`alternate` behaviour**. In historical editing, texts constantly present alternative versions of the same passage: an original spelling vs. a normalized regularization (`<orig>`/`<reg>`), a scribal error vs. an editorial correction (`<sic>`/`<corr>`), or an abbreviation vs. an expanded reading (`<abbr>`/`<expan>`), all enclosed in a `<choice>` element (Topic 6; TEI Consortium, 2026; Pierazzo, 2016).

In traditional print, an editor was forced to choose one reading and relegate the other to a footnote. In legacy web development, programmers wrote fragile JavaScript tooltips. The Processing Model formalizes this interaction declaratively via `alternate`:

```xml
<elementSpec ident="choice" mode="change">
  <!-- Interactive Web View: Generate Interactive Popover -->
  <model predicate="$mode = 'web'" behaviour="alternate">
    <param name="default" value="reg | corr | expan"/>
    <param name="alternate" value="orig | sic | abbr"/>
  </model>

  <!-- Diplomatic View: Output Historical Original Only -->
  <model predicate="$mode = 'diplomatic'" behaviour="inline">
    <param name="content" value="orig | sic | abbr"/>
    <outputRendition>color: #8b0000; font-family: 'Cardo', serif;</outputRendition>
  </model>

  <!-- Clean Reading View: Output Regularized Form Only -->
  <model predicate="$mode = 'reading'" behaviour="inline">
    <param name="content" value="reg | corr | expan"/>
  </model>
</elementSpec>
```

| Parameter | Meaning in `alternate` Behaviour | Interaction in TEI Publisher |
| --- | --- | --- |
| `default` | The primary reading displayed on the page | Rendered as clickable, highlighted text in the main line |
| `alternate` | The secondary reading revealed on interaction | Displayed inside a floating popup / tooltip upon hover or click |

In TEI Publisher, invoking `alternate` automatically generates an accessible HTML5 `<pb-popover>` Web Component. A reader sees the regularized reading (`<reg>`) in the text, and clicking on it smoothly reveals the exact paleographical spelling (`<orig>`) recorded in the manuscript (Turska et al., 2016; Pierazzo, 2016).

**Vocabulary.** `alternate` — behaviour designed to toggle or pop up alternative readings of the same text span. `<pb-popover>` — a TEI Publisher Web Component that displays interactive floating popups. *Interactive multi-layer reading* — allowing readers to dynamically toggle between diplomatic, regularized, and critical views.

**Takeaway:** The `alternate` behaviour effortlessly transforms TEI `<choice>` elements into interactive web tooltips while supporting clean diplomatic and reading views.

---

## **10 Content**

**Context-Sensitive Styling: The `@predicate` XPath Condition**

In complex scholarly documents, an XML element cannot be rendered using a single static rule. Its visual presentation depends entirely upon its **document context**: where it occurs, what attributes it carries, and what editorial mode is active (TEI Consortium, 2026; Turska et al., 2016).

The TEI Processing Model manages context-sensitive styling through the **`@predicate`** attribute on `<model>`. A predicate is an **XPath 2.0 / 3.0 expression**. When the transformation engine encounters an element, it evaluates the predicates of its `<model>` rules in sequential order. The engine executes the **first model whose predicate evaluates to true** (Turska et al., 2016):

```xml
<elementSpec ident="hi" mode="change">
  <!-- Rule 1: Superscript text -->
  <model predicate="@rend = 'superscript'" behaviour="inline">
    <outputRendition>vertical-align: super; font-size: smaller;</outputRendition>
  </model>

  <!-- Rule 2: Rubricated red text in sacred headings -->
  <model predicate="@rend = 'rubric' or ancestor::head" behaviour="inline">
    <outputRendition>color: #b03a2e; font-weight: bold;</outputRendition>
  </model>

  <!-- Rule 3: Expanded Nomina Sacra -->
  <model predicate="parent::expan" behaviour="inline">
    <outputRendition>border-top: 1px solid #555;</outputRendition>
  </model>

  <!-- Rule 4: Default Fallback -->
  <model behaviour="inline">
    <outputRendition>font-style: italic;</outputRendition>
  </model>
</elementSpec>
```

| Target Context | XPath Predicate Expression | Resulting Presentation |
| --- | --- | --- |
| **Superscript Addition** | `@rend = 'superscript'` | Small, elevated text ($x^2$) |
| **Rubricated Heading** | `@rend = 'rubric' or ancestor::head` | Bold red text |
| **Inside Critical Apparatus** | `ancestor::app` | Relegated to footnote apparatus stream |
| **Global Fallback** | *(No predicate)* | Standard italicized inline text |

Using predicates allows you to author sophisticated, context-aware publishing rules without writing a single line of procedural XSLT branching logic (Turska et al., 2016; Stadler et al., 2016).

**Vocabulary.** `@predicate` — an XPath expression in a `<model>` element that determines whether the rule applies. *Sequential evaluation* — testing model rules in top-to-bottom order until the first matching predicate is found. *Fallback model* — a model rule without a predicate placed at the end of an `<elementSpec>` to handle all default cases.

**Takeaway:** The `@predicate` attribute evaluates XPath expressions to apply context-sensitive rendering rules based on attributes, ancestors, and active modes.

---

## **11 Content**

**Multi-Output Targeting: The `@output` Attribute (web, print, latex, epub)**

A core requirement of modern scholarly publishing is **multi-modal dissemination**: generating web, interactive HTML, print PDF, and eBook packages from the exact same TEI XML master file (Sahle, 2016; Driscoll & Pierazzo, 2016).

The TEI Processing Model accomplishes this through the **`@output`** attribute on `<model>`. The `@output` attribute restricts a model rule to a specific publication channel:

- `@output="web"`: Executed only when compiling responsive HTML5 web applications;
- `@output="print"`: Executed when compiling paginated print layouts via CSS Paged Media;
- `@output="latex"`: Executed when compiling typeset books via LaTeX / `reledmac`;
- `@output="epub"`: Executed when compiling reflowable e-books (Turska et al., 2016).

```xml
<elementSpec ident="ref" mode="change">
  <!-- Web Output: Clickable Anchor -->
  <model output="web" behaviour="link">
    <param name="uri" value="@target"/>
    <outputRendition>color: #2980b9; text-decoration: underline;</outputRendition>
  </model>

  <!-- Print PDF Output: Text followed by Footnote with URL -->
  <modelSequence output="print">
    <model behaviour="inline"/>
    <model behaviour="note">
      <param name="place" value="'foot'"/>
      <param name="content" value="@target"/>
    </model>
  </modelSequence>
</elementSpec>
```

| Publication Channel | `@output` Value | Optimal Behavioural Strategy |
| --- | --- | --- |
| **Responsive Web** | `web` | Interactive tooltips, popovers, deep-zoom IIIF viewers |
| **CSS Paged Media PDF** | `print` | Running headers, bottom footnotes, multi-column layouts |
| **LaTeX Typeset Codex** | `latex` | Multi-tier critical apparatus (`\Afootnote`), line numbering |
| **Universal Default** | *(Omitted)* | Applies across all publication channels simultaneously |

If a `<model>` omits the `@output` attribute, it applies universally across all media. This allows editors to write universal rules for common markup while specializing only where the medium demands distinct affordances (Turska et al., 2016; Fischer, 2020).

**Vocabulary.** `@output` — attribute specifying the target publication format (`web`, `print`, `latex`, `epub`) for a `<model>` rule. *Multi-output targeting* — configuring an ODD specification to generate distinct media outputs from a single XML source. *Universal model* — a model rule without an `@output` restriction that applies to all media.

**Takeaway:** The `@output` attribute allows editors to customize rendering rules for specific media while sharing universal baseline rules.

---

## **12 Content**

**Parameterized Transformations: The `<param>` Element**

Behaviors are abstract functions that require specific inputs to generate output. For example, a `link` behaviour needs to know what URL to target; a `graphic` behaviour needs to know the image path; and an `alternate` behaviour needs to know which readings are default versus secondary. These inputs are supplied via the **`<param>` (Parameter)** element (TEI Consortium, 2026; Turska et al., 2016).

Inside a `<model>`, each `<param>` has two core attributes:

- `@name`: The identifier of the parameter expected by the behaviour (e.g., `content`, `uri`, `place`, `default`, `alternate`, `level`);
- `@value`: An **XPath expression** that extracts the required data dynamically from the XML node.

```xml
<elementSpec ident="graphic" mode="change">
  <model behaviour="graphic">
    <param name="url" value="@url"/>
    <param name="width" value="@width"/>
    <param name="height" value="@height"/>
    <param name="scale" value="@scale"/>
    <param name="title" value="desc"/>
    <outputRendition>display: block; margin: 0 auto; max-width: 100%;</outputRendition>
  </model>
</elementSpec>
```

| Behaviour | Standard Parameter `@name` | Expected Value / XPath Query |
| --- | --- | --- |
| `link` | `uri` | `@target` (The URL or internal ID pointer) |
| `graphic` | `url` | `@url` (The image server URL or IIIF manifest) |
| `note` | `place` | `'foot'`, `'margin'`, `'inline'`, or `'popup'` |
| `heading` | `level` | `count(ancestor::div)` (Calculates heading depth) |
| `alternate` | `default` / `alternate` | XPath selecting primary vs secondary readings |

Because `@value` accepts full XPath expressions, you can construct dynamic strings, perform mathematical calculations, or query external nodes directly within parameter definitions (Turska et al., 2016).

**Vocabulary.** `<param>` — TEI element providing a named argument to a processing model behaviour. `@value` — XPath expression evaluated dynamically to supply data to a parameter. *Dynamic string construction* — using XPath functions (such as `concat()`) inside a parameter value to build URLs or labels.

**Takeaway:** The `<param>` element passes dynamic parameters—extracted via XPath—into abstract behaviors to control URLs, image sources, note placements, and content streams.

---

## **13 Content**

**Declarative Styling: `<outputRendition>` and CSS Integration**

While behaviors control document structure and interaction, visual aesthetics (such as typography, colors, margins, and borders) are managed declaratively using the **`<outputRendition>`** element (TEI Consortium, 2026; Turska et al., 2016).

The `<outputRendition>` element encloses standard **CSS3 styling rules**. When the processing model engine compiles the ODD, it attaches these CSS properties directly to the generated HTML or CSS Paged Media nodes:

```xml
<elementSpec ident="supplied" mode="change">
  <model behaviour="inline">
    <outputRendition scope="before">content: '[';</outputRendition>
    <outputRendition scope="after">content: ']';</outputRendition>
    <outputRendition>color: #7f8c8d; font-style: italic;</outputRendition>
  </model>
</elementSpec>
```

| `<outputRendition>` Feature | Attribute / Syntax | Publishing Function |
| --- | --- | --- |
| **Main Element Style** | *(Default content)* | Sets font family, color, margins, padding, line-height |
| **Pseudo-Element Styling** | `@scope="before"` / `@scope="after"` | Injects brackets, quotation marks, or sigla before/after text |
| **Medium Selection** | `@selector` | Attaches CSS rules to custom class names or media queries |

In the example above, the `<supplied>` tag (used for editorial text restorations) is styled with brackets inserted automatically via CSS `content: '['` and `content: ']'`. The editor does not hard-code square brackets into the XML data stream; the presentation engine adds them dynamically at render time (TEI Consortium, 2026; Pierazzo, 2016).

Furthermore, styling rules can reference external CSS stylesheets, allowing designers to update project typography without modifying the ODD specification (Turska et al., 2016).

**Vocabulary.** `<outputRendition>` — TEI element containing declarative CSS styling rules applied to a model behaviour. `@scope="before"` — attribute applying CSS styles to the `::before` pseudo-element. *Presentation decoupling* — generating typographical brackets and punctuation dynamically at render time rather than hard-coding them into the transcription.

**Takeaway:** The `<outputRendition>` element attaches declarative CSS styles and pseudo-element brackets directly to model rules.

---

## **14 Content**

**Sequential Transformations: The `<modelSequence>` Container**

In advanced textual editing, a single XML element often requires **multiple distinct rendering passes**. For example, when displaying a critical apparatus entry (`<app>`), the system must execute two operations in strict succession:

1. Render the accepted reading (`<lem>`) inline in the main reading text stream;
2. Render an apparatus footnote anchored at the bottom of the page containing the lemma and all rejected manuscript variants (`<rdg>`) (Fischer, 2020).

A single `<model>` cannot output to two distinct places simultaneously. To solve this, the Processing Model provides the **`<modelSequence>`** container (TEI Consortium, 2026; Turska et al., 2016).

```xml
<elementSpec ident="app" mode="change">
  <modelSequence>
    <!-- Step 1: Render Lemma Inline in Base Text -->
    <model behaviour="inline">
      <param name="content" value="lem"/>
      <outputRendition>font-weight: normal;</outputRendition>
    </model>
    
    <!-- Step 2: Render Critical Apparatus Entry in Footnote Stream -->
    <model behaviour="note">
      <param name="place" value="'foot'"/>
      <param name="content" value="concat(lem, '] ', string-join(rdg, '; '))"/>
      <outputRendition>font-size: smaller; font-family: 'Cardo', serif;</outputRendition>
    </model>
  </modelSequence>
</elementSpec>
```

| Execution Step | Behaviour | Target Stream | Output Result |
| --- | --- | --- | --- |
| **Step 1** | `inline` | Main Reading Text | Outputs lemma (`<lem>`) seamlessly in the verse |
| **Step 2** | `note` | Apparatus Footnote Stream | Generates footnote containing lemma, bracket, and variants |

When the transformation engine encounters `<modelSequence>`, it executes every enclosed `<model>` in strict linear order. This enables digital editors to construct sophisticated, multi-tiered critical apparatuses and running commentaries without writing custom XSLT recursion (Turska et al., 2016; Fischer, 2020).

**Vocabulary.** `<modelSequence>` — TEI container grouping multiple `<model>` elements that must be executed in sequential order. *Multi-pass rendering* — processing a single XML node into multiple distinct layout locations (e.g., inline text and bottom apparatus). *Footnote stream* — the paginated or digital container where notes and apparatus entries collect.

**Takeaway:** The `<modelSequence>` element executes multiple model rules in sequential order, allowing elements like `<app>` to render simultaneously inline and in the apparatus stream.

---

## **15 Content**

**Conditional Grouping: The `<modelGrp>` Element**

When an ODD specification manages dozens of elements across multiple publication formats, maintaining individual `<model>` rules becomes repetitive. To streamline schema maintenance, the Processing Model provides the **`<modelGrp>` (Model Group)** container (TEI Consortium, 2026; Turska et al., 2016).

The `<modelGrp>` container groups multiple `<model>` elements that share common attributes, such as:

- A shared `@output` format (e.g., grouping all rules intended exclusively for print PDF);
- A shared `@predicate` condition (e.g., grouping all rules active when viewing diplomatic facsimiles) (Turska et al., 2016).

```xml
<elementSpec ident="q" mode="change">
  <!-- Group 1: Rules for Print Output -->
  <modelGrp output="print">
    <model predicate="ancestor::p" behaviour="inline">
      <outputRendition scope="before">content: '“';</outputRendition>
      <outputRendition scope="after">content: '”';</outputRendition>
    </model>
    <model behaviour="block">
      <outputRendition>margin: 1em 2em; font-style: italic;</outputRendition>
    </model>
  </modelGrp>

  <!-- Group 2: Rules for Web Output -->
  <modelGrp output="web">
    <model behaviour="block">
      <outputRendition>border-left: 3px solid #3498db; padding-left: 1em;</outputRendition>
    </model>
  </modelGrp>
</elementSpec>
```

| Optimization Factor | Individual `<model>` Repetition | `<modelGrp>` Centralization |
| --- | --- | --- |
| **Output Specification** | Must write `@output="print"` on every rule | Declared once on parent `<modelGrp output="print">` |
| **Predicate Inheritance** | Predicates repeated across multiple lines | Inherited automatically by child models |
| **Maintenance Burden** | High (risk of conflicting rules) | Low (clean, modular organization) |

Using `<modelGrp>` organizes complex ODD files into clean, modular blocks, dramatically reducing schema errors and simplifying collaborative editing (Turska et al., 2016; Stadler et al., 2016).

**Vocabulary.** `<modelGrp>` — TEI element grouping multiple `<model>` specifications sharing common output targets or predicates. *Attribute inheritance* — child `<model>` elements automatically inheriting properties declared on their parent `<modelGrp>`. *Modular ODD architecture* — structuring schema specifications into clean, isolated logical blocks.

**Takeaway:** The `<modelGrp>` container centralizes shared output formats and predicates, reducing code repetition and simplifying ODD maintenance.

---

## **16 Content**

**Processing the Critical Apparatus: Mapping `<app>`, `<lem>`, and `<rdg>`**

When an edition encodes multi-witness textual variation using the TEI Parallel Segmentation method (`<app>`, `<lem>`, `<rdg>`, `<listWit>`), we configure the ODD processing model to transform these apparatus structures into an automated, interactive critical edition (Buzzoni, 2016; Fischer, 2020).

A complete apparatus processing model must accommodate three distinct publication modes:

```xml
<elementSpec ident="app" mode="change">
  <!-- Mode 1: Interactive Web View with Dynamic Variant Popover -->
  <model predicate="$mode = 'web'" behaviour="alternate">
    <param name="default" value="lem"/>
    <param name="alternate" value="rdg"/>
    <outputRendition>border-bottom: 1px dotted #2980b9; cursor: pointer;</outputRendition>
  </model>

  <!-- Mode 2: Multi-Modal Print PDF with Two-Tier Footnote Apparatus -->
  <modelSequence output="print">
    <model behaviour="inline">
      <param name="content" value="lem"/>
    </model>
    <model behaviour="note">
      <param name="place" value="'foot'"/>
      <param name="content" value="concat(lem, '] ', string-join(rdg/@wit, ' '), ' (', rdg, ')')"/>
      <outputRendition>font-size: 8.5pt; line-height: 1.2;</outputRendition>
    </model>
  </modelSequence>
</elementSpec>

<elementSpec ident="rdg" mode="change">
  <model behaviour="inline">
    <param name="content" value="concat(., ' ', @wit)"/>
  </model>
</elementSpec>
```

| Output Channel | Visual Presentation of Apparatus | User Interaction |
| --- | --- | --- |
| **Interactive Web** | Lemma displayed with dotted blue underline | Clicking lemma opens popover showing witness readings and sigla |
| **Paginated PDF** | Lemma inline in text; full entry at foot of page | Standard critical apparatus line: `7 νήπιοι] א B C*; ἤπιοι A C2 D Ψ` |
| **Diplomatic View** | Displays reading of the currently selected witness | Selecting "Codex Sinaiticus" renders only Sinaiticus readings |

By mapping the apparatus through the Processing Model, you eliminate the need to maintain separate print and web transcription files. The same XML source powers both seamlessly (Buzzoni, 2016; Fischer, 2020).

**Vocabulary.** *Parallel segmentation transformation* — extracting the `<lem>` for reading flows while converting `<rdg>` variants into apparatus notes. *Variant popover* — an interactive web component displaying manuscript sigla upon user click. *Siglum formatting* — programmatically appending witness sigla (`@wit`) to variant strings at render time.

**Takeaway:** Mapping `<app>`, `<lem>`, and `<rdg>` through the Processing Model automates interactive web popovers and multi-tier print apparatus footnotes from a single XML source.

---

## **17 Content**

**Processing Stand-off Commentary: Mapping `<standOff>`, `<interpGrp>`, and `<note>`**

In Topic 12, you authored scholarly commentary notes inside a dedicated `<standOff>` container, categorizing notes into philological, historical, intertextual, and structural types (Berti, 2026; Tafdrup et al., 2026).

Transforming stand-off commentary requires mapping the relationship between the external `<note>` elements and their target anchors in the base text:

```xml
<elementSpec ident="standOff" mode="change">
  <!-- In Web Mode: Ingest into Sidebar Commentary Drawer -->
  <model predicate="$mode = 'web'" behaviour="block">
    <outputRendition>display: none;</outputRendition> <!-- Handled dynamically via JS / Web Components -->
  </model>
  <!-- In Print Mode: Output as Endnotes Section -->
  <model output="print" behaviour="block">
    <outputRendition>page-break-before: always; margin-top: 2em;</outputRendition>
  </model>
</elementSpec>

<elementSpec ident="interpGrp" mode="change">
  <model behaviour="block">
    <param name="content" value="note"/>
    <outputRendition>margin-bottom: 1.5em;</outputRendition>
  </model>
</elementSpec>

<elementSpec ident="note" mode="change">
  <model predicate="parent::interpGrp[@type='philological']" behaviour="paragraph">
    <outputRendition>border-left: 3px solid #27ae60; padding-left: 8px;</outputRendition>
  </model>
  <model predicate="parent::interpGrp[@type='historical']" behaviour="paragraph">
    <outputRendition>border-left: 3px solid #e67e22; padding-left: 8px;</outputRendition>
  </model>
  <model predicate="parent::interpGrp[@type='intertextual']" behaviour="paragraph">
    <outputRendition>border-left: 3px solid #8e44ad; padding-left: 8px;</outputRendition>
  </model>
</elementSpec>
```

| Commentary Category | Web Sidebar Styling | Print PDF Presentation |
| --- | --- | --- |
| **Philological** | Green border indicator (`#27ae60`) | Endnote labeled `[Philological Note]` |
| **Historical** | Orange border indicator (`#e67e22`) | Endnote with active Pleiades LOD link |
| **Intertextual** | Purple border indicator (`#8e44ad`) | Endnote with citation formula and Tesserae score |
| **Structural** | Blue border indicator (`#2980b9`) | Section divider note preceding pericope |

In TEI Publisher, stand-off notes are dynamically linked to inline text spans via the `<pb-popover>` or `<pb-drawer>` web components, allowing readers to toggle commentary layers on and off at will (Turska et al., 2016; Berti, 2026).

**Vocabulary.** `<standOff>` — TEI container for annotations and commentary decoupled from the primary text. *Commentary drawer* — a collapsible web panel that displays context-sensitive scholarly notes. *Categorical color-coding* — using distinct border colors to visually distinguish philological, historical, and intertextual notes.

**Takeaway:** Stand-off commentary is mapped to interactive sidebar drawers on the web and structured endnote sections in print PDFs.

---

## **18 Content**

**Processing Interlinear Glosses: Mapping `<w>`, `<m>`, and `<linkGrp>`**

In Topic 11, you constructed four-line interlinear glossed transcriptions following the Leipzig Glossing Rules, mapping Greek surface forms, normalized lemmas, grammatical morphemes, and English translation tokens (Camps et al., 2019; Topic 11).

Rendering interlinear glosses requires maintaining strict vertical alignment across all four linguistic tiers:

```xml
<elementSpec ident="w" mode="change">
  <!-- Mode 1: Interlinear Gloss Grid -->
  <model predicate="$mode = 'interlinear'" behaviour="block">
    <param name="content" value="concat(
      '&lt;span class=&quot;surface&quot;&gt;', text(), '&lt;/span&gt;',
      '&lt;span class=&quot;lemma&quot;&gt;', @lemma, '&lt;/span&gt;',
      '&lt;span class=&quot;pos&quot;&gt;', @pos, '&lt;/span&gt;',
      '&lt;span class=&quot;gloss&quot;&gt;', @gloss, '&lt;/span&gt;'
    )"/>
    <outputRendition>display: inline-flex; flex-direction: column; margin: 0 4px; text-align: center;</outputRendition>
  </model>

  <!-- Mode 2: Standard Reading View -->
  <model behaviour="inline">
    <outputRendition>font-family: 'Cardo', serif;</outputRendition>
  </model>
</elementSpec>
```

| Interlinear Tier | Source Attribute / Node | Rendered CSS Class | Visual Alignment |
| --- | --- | --- | --- |
| **Tier 1: Surface Form** | Text node (`text()`) | `.surface` (Greek Uncial / Polytonic) | Top line in bold Cardo serif |
| **Tier 2: Lemma** | `@lemma` | `.lemma` (Dictionary Headword) | Second line in small italics |
| **Tier 3: Morphosyntax** | `@pos` | `.pos` (Leipzig Glossing Codes) | Third line in monospace small caps |
| **Tier 4: English Token** | `@gloss` | `.gloss` (Literal Translation) | Bottom line in sans-serif |

By applying CSS Flexbox (`display: inline-flex; flex-direction: column;`), the four tiers remain perfectly stacked vertically while allowing words to wrap naturally across lines in responsive web and print layouts (Turska et al., 2016; Camps et al., 2019).

**Vocabulary.** *Interlinear stacking* — arranging multiple linguistic tiers vertically above or below a word. *CSS Flexbox alignment* — using flexible box layout modules to keep multi-line glosses aligned. *Leipzig glossing presentation* — formatting grammatical tags in standardized small-cap abbreviations.

**Takeaway:** Mapping `<w>` with CSS Flexbox maintains perfect vertical alignment across all four interlinear gloss tiers while supporting responsive line wrapping.

---

## **19 Content**

**Processing Manuscript Facsimiles: Mapping `<pb>`, `<surface>`, and IIIF Canvases**

In Topic 3, you bound your digital edition to high-resolution manuscript images using the **International Image Interoperability Framework (IIIF)** (Sanderson et al., 2017; Topic 3).

The TEI Processing Model bridges textual transcriptions and IIIF images via the **`<pb>` (Page Break)** and **`<surface>`** elements:

```xml
<elementSpec ident="pb" mode="change">
  <!-- Mode 1: Interactive Web View with Deep-Zoom IIIF Binding -->
  <model predicate="$mode = 'web'" behaviour="webcomponent">
    <param name="name" value="'pb-facsimile'"/>
    <param name="facs" value="@facs"/>
    <outputRendition>display: block; margin: 1em 0; border-top: 1px solid #ccc;</outputRendition>
  </model>

  <!-- Mode 2: Print PDF Layout with Folio Indicator -->
  <model output="print" behaviour="break">
    <param name="type" value="'page'"/>
    <param name="label" value="concat('[Fol. ', @n, ']')"/>
    <outputRendition>color: #7f8c8d; font-size: 8pt; text-align: right;</outputRendition>
  </model>
</elementSpec>
```

| Publication Channel | XML Attribute `@facs` | Rendered Result |
| --- | --- | --- |
| **Interactive Web Edition** | IIIF Canvas URI (`https://.../canvas/f23r`) | Triggers OpenSeadragon / Mirador deep-zoom viewer to display high-resolution folio image |
| **Archival Print PDF** | Folio Number (`@n="23r"`) | Injects running margin indicator: `[Fol. 23r]` and triggers page break |

In TEI Publisher, scrolling past a `<pb>` tag in the text view automatically sends an event to the `<pb-facsimile>` component, causing the IIIF viewer to smoothly pan and zoom to the corresponding manuscript page in real time (Turska et al., 2016; Stadler et al., 2016).

**Vocabulary.** `<pb>` — TEI milestone element marking the boundary between one page of a text and the next. `<pb-facsimile>` — TEI Publisher Web Component that embeds and controls a IIIF image viewer. *Synchronized scrolling* — automatically updating the image viewer as the reader scrolls through the transcription.

**Takeaway:** The `<pb>` element is mapped to `<pb-facsimile>` for real-time IIIF deep-zoom synchronization on the web and folio markers in print PDFs.

---

## **20 Content**

**The TEI Publisher Architecture: eXist-db, XQuery, and Web Components**

**TEI Publisher**, maintained by e-editiones, is the premier open-source reference platform implementing the TEI Processing Model (Turska et al., 2016; Stadler et al., 2016).

The technical architecture of TEI Publisher comprises three integrated tiers:

| Architecture Tier | Primary Technologies | System Responsibility |
| --- | --- | --- |
| **1. Client / Frontend Tier** | HTML5 + Web Components (`<pb-view>`, `<pb-facsimile>`, `<pb-popover>`) | Native browser interface, IIIF viewport, interactive popovers |
| **2. Processing & Transformation Tier** | Compiled ODD Processing Model Libraries (XQuery 3.1 / XSLT 3.0) | High-speed server-side translation from TEI XML into HTML fragments |
| **3. Database & Storage Tier** | eXist-db Native XML Database (Lucene Indexing, XPath 3.1) | Native XML storage, CTS URN resolution, full-text and entity search |

The three tiers interact seamlessly:

1. **Storage Tier (eXist-db):** A high-performance Native XML database that stores master TEI XML documents, ODD specifications, and authority registries. Documents are queried using XPath 3.1 and indexed via Apache Lucene for instantaneous full-text and morphosyntactic searching (Stadler et al., 2016).
2. **Transformation Tier (Processing Model Engine):** When an ODD file is saved, TEI Publisher compiles its `<model>` rules into native XQuery functions. When a user requests a document, the engine executes these compiled functions server-side, transforming raw TEI XML into semantic HTML fragments in milliseconds.
3. **Frontend Tier (Web Components):** Lightweight, modular Custom Elements (such as `<pb-view>`, `<pb-load>`, `<pb-facsimile>`) receive the transformed HTML and render the user interface in the browser (Turska et al., 2016).

This three-tier architecture eliminates the need for heavyweight server-side web frameworks, enabling scholars to publish enterprise-grade digital editions simply by configuring XML and ODD files (Turska et al., 2016; Stadler et al., 2016).

**Vocabulary.** *eXist-db* — an open-source native XML database engine. *XQuery* — a functional programming language designed for querying and transforming XML data collections. *Web Components* — a suite of W3C standard web platform APIs allowing developers to create reusable custom HTML tags.

**Takeaway:** TEI Publisher integrates eXist-db, compiled XQuery Processing Model engines, and frontend Web Components into a complete publication stack.

---

## **21 Content**

**Compiling ODD to Executable Code: Saxon XSLT 3.0 and XQuery Modules**

How does an abstract ODD file become an executable transformation pipeline? The compilation process is handled by dedicated ODD processing libraries (such as `tei-publisher-lib` or Saxon-HE) (Turska et al., 2016).

The compilation workflow proceeds in three automated stages:

| Stage | Input File | Compiler Action | Generated Output File |
| --- | --- | --- | --- |
| **1. ODD Ingestion** | `custom_odd.odd` | Ingests ODD, resolves module references (`<moduleRef>`), and validates Schematron | Expanded ODD XML |
| **2. Behavior Translation** | Expanded ODD XML | Maps every `<model>` instruction into corresponding XSLT 3.0 templates or XQuery functions | `transform-web.xql` / `transform-print.xsl` |
| **3. Execution** | Master `edition.xml` | Executes compiled transformation library against the source TEI document | HTML5 / CSS Paged Media PDF |

| Command-Line Operation | Standard Saxon Execution Command | Operational Goal |
| --- | --- | --- |
| **1. Compile ODD Pipeline** | `java -jar saxon-he.jar -s:edition.odd -xsl:odd2processingmodel.xsl -o:pipeline.xsl` | Generates executable XSLT 3.0 transformation code from ODD rules |
| **2. Execute Transformation** | `java -jar saxon-he.jar -s:edition.xml -xsl:pipeline.xsl -o:index.html` | Applies compiled pipeline to master XML, generating publishable HTML5 |

Because the compilation step is fully automated, editors never write low-level transformation code by hand. If you decide to change a font, add a footnote bracket, or alter a variant popover, you modify a single line in your ODD file and re-run the compiler (Turska et al., 2016; Stadler et al., 2016).

**Vocabulary.** *ODD compilation* — the automated generation of XSLT or XQuery transformation libraries from an ODD specification. *Saxon* — an industry-standard XSLT and XQuery processing engine. `tei-publisher-lib` — the open-source XQuery library powering the TEI Publisher processing model.

**Takeaway:** ODD compilers automatically generate optimized XSLT 3.0 or XQuery transformation code from abstract model rules.

---

## **22 Content**

**The TEI Publisher Web Component Library: `<pb-view>`, `<pb-facsimile>`, `<pb-popover>`**

On the client side, TEI Publisher provides a modular library of **Web Components** that handle all user interactions (Turska et al., 2016).

Unlike monolithic web frameworks (such as React or Angular) that require massive build tools and npm dependency trees, TEI Publisher Web Components are native browser Custom Elements. They are embedded directly into standard HTML pages:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Digital Critical Edition of 1 Thessalonians 2</title>
  <script type="module" src="components/pb-view.js"></script>
  <script type="module" src="components/pb-facsimile.js"></script>
  <script type="module" src="components/pb-popover.js"></script>
  <link rel="stylesheet" href="styles/edition.css">
</head>
<body>
  <div class="edition-layout">
    <!-- Left Column: Synchronized IIIF Digital Facsimile -->
    <pb-facsimile id="facsimile-viewer" default-zoom="1.5"></pb-facsimile>

    <!-- Right Column: Interactive Transformed TEI Text View -->
    <pb-view src="data/1thess_edition.xml" odd="odds/1thess.odd" view="reading"
             subscribe="facsimile-viewer"></pb-view>
  </div>
</body>
</html>
```

| Web Component | HTML Tag | Primary Function in Digital Edition |
| --- | --- | --- |
| **Document View** | `<pb-view>` | Requests TEI XML, applies ODD transformation, and renders HTML |
| **Facsimile Viewer** | `<pb-facsimile>` | Renders deep-zoom IIIF images using OpenSeadragon |
| **Interactive Popover** | `<pb-popover>` | Displays variant readings, morphological analyses, and commentary tooltips |
| **Document Loader** | `<pb-load>` | Dynamically loads external commentary notes or collation tables |

The `subscribe` attribute allows web components to communicate asynchronously: when a user clicks a line in `<pb-view>`, it broadcasts a signal that causes `<pb-facsimile>` to automatically highlight the corresponding region on the manuscript image (Turska et al., 2016).

**Vocabulary.** `<pb-view>` — the core Web Component responsible for displaying transformed TEI content. *Custom Elements* — the HTML5 standard allowing developers to define new HTML tags with encapsulated functionality. *Asynchronous event broadcasting* — components communicating across an interface via event signals.

**Takeaway:** TEI Publisher Web Components provide lightweight, native browser tags for rendering text, IIIF images, and interactive popovers.

---

## **23 Content**

**Configuring eXist-db Native XML Database for Digital Editions**

For institutional digital humanities projects, **eXist-db** serves as the standard backend database. Unlike relational databases (such as MySQL or PostgreSQL) that force hierarchical XML documents into flat SQL tables, eXist-db stores XML documents natively as DOM trees (Stadler et al., 2016; Barzaghi et al., 2025).

Configuring eXist-db for a digital critical edition involves three primary administrative tasks:

1. **Collection Management:** Organizing project files into hierarchical collections:
   - `/db/apps/edition/data/`: Master TEI XML source files;
   - `/db/apps/edition/odds/`: ODD specification files;
   - `/db/apps/edition/resources/`: CSS, fonts, and client-side JavaScript.
2. **Security & Permissions:** Setting read/write permissions via Unix-style chmod flags, ensuring public read-only access while restricting write privileges to authenticated editors.
3. **MIME-Type Configuration:** Mapping `.odd`, `.xml`, and `.rng` extensions to `application/xml` (Stadler et al., 2016).

```xquery
(: Sample eXist-db XQuery Script: query_apparatus.xql :)
xquery version "3.1";
declare namespace tei="http://www.tei-c.org/ns/1.0";

let $edition := doc("/db/apps/edition/data/1thess_edition.xml")
for $app in $edition//tei:app
return
  <variant_unit id="{$app/@xml:id}">
    <lemma>{$app/tei:lem/text()}</lemma>
    <divergent_witnesses>{string-join($app/tei:rdg/@wit, ", ")}</divergent_witnesses>
  </variant_unit>
```

Storing documents natively in eXist-db allows scholars to execute powerful XQuery scripts across thousands of files simultaneously (Stadler et al., 2016; Barzaghi et al., 2025).

**Vocabulary.** *Native XML database* — a database engine designed specifically to store, query, and manipulate XML documents natively without relational decomposition. *XQuery collection* — a logical directory inside an XML database containing documents. *DOM tree* — Document Object Model tree structure representing an XML file in memory.

**Takeaway:** eXist-db stores TEI XML documents natively, allowing rapid querying, collection management, and transformation.

---

## **24 Content**

**Full-Text Indexing and Lucene Querying in TEI Publisher**

A major advantage of native XML databases is their integration with high-performance search engines. eXist-db embeds **Apache Lucene**, enabling instant full-text searching, fuzzy matching, and faceted entity filtering across large manuscript corpora (Stadler et al., 2016; Barzaghi et al., 2025).

To enable Lucene indexing, the editor creates an index configuration file (`collection.xconf`):

```xml
<collection xmlns="http://exist-db.org/collection-config/1.0">
  <index xmlns:tei="http://www.tei-c.org/ns/1.0">
    <lucene>
      <text qname="tei:body"/>
      <text qname="tei:w"/>
      <text qname="tei:persName"/>
      <text qname="tei:placeName"/>
      <text qname="tei:note"/>
    </lucene>
  </index>
</collection>
```

| Index Query Type | Target XML Node | Example Search Capability |
| --- | --- | --- |
| **Morphological Search** | `tei:w/@lemma` | Find all occurrences of the lemma *λόγος* across all inflected forms |
| **Prosopographical Search** | `tei:persName/@ref` | Find all mentions of *Paul* or *Silvanus* across the corpus |
| **Apparatus Search** | `tei:rdg/@wit` | Find all passages where *Codex Sinaiticus* diverges from the lemma |
| **Commentary Search** | `tei:note[@type='intertextual']` | Search all notes documenting citations of the Septuagint (LXX) |

Configuring specialized Lucene indices transforms your digital edition from a passive reading document into a queryable research corpus (Stadler et al., 2016; Barzaghi et al., 2025).

**Vocabulary.** *Apache Lucene* — an open-source full-text search engine library. `collection.xconf` — configuration file defining index rules in eXist-db. *Faceted search* — searching across multiple orthogonal dimensions (e.g., author, date, manuscript witness, lemma).

**Takeaway:** Configuring Lucene indexing in eXist-db enables real-time full-text, morphosyntactic, and faceted entity search across the edition.

---

## **25 Content**

**Developing Custom Behaviors and Extension Modules**

While the standard repertoire of TEI Processing Model behaviors covers 95% of editorial needs, highly specialized projects (such as musical editions, epigraphic 3D models, or complex stemmata) occasionally require **custom behaviours** (Turska et al., 2016; Stadler et al., 2016).

In the *Carl Maria von Weber Gesamtausgabe* (WeGA), researchers required a custom behavior to render musical scores encoded in MEI (Music Encoding Initiative) directly alongside historical letters (Stadler et al., 2016).

To implement a custom behavior in TEI Publisher:

1. Define the custom behavior function in an XQuery extension module (`custom-behaviours.xql`);
2. Register the behavior name in your project's ODD configuration;
3. Invoke the behavior inside your `<model>` specification:

```xml
<elementSpec ident="stemma" mode="add">
  <model behaviour="render-stemma">
    <param name="source" value="@corresp"/>
    <param name="layout" value="'hierarchical'"/>
  </model>
</elementSpec>
```

```xquery
(: Custom Behavior Implementation in XQuery :)
declare function custom:render-stemma($config as map(*), $node as element(), $class as xs:string, $params as map(*)) {
  let $dotCode := $params?source
  return
    <div class="stemma-container {$class}">
      <svg-interactive-graph src="{$dotCode}" layout="{$params?layout}"/>
    </div>
};
```

This modular extension mechanism guarantees that even the most complex digital editing features can be integrated cleanly into the declarative Processing Model pipeline without breaking standard TEI compliance (Turska et al., 2016; Stadler et al., 2016).

**Vocabulary.** *Custom behaviour* — a project-specific extension function added to the TEI Processing Model engine. *MEI (Music Encoding Initiative)* — an XML standard for encoding musical scores. *Modular extensibility* — the ability to add new computational features without modifying core system libraries.

**Takeaway:** Custom behaviors allow editors to extend the Processing Model with project-specific features—such as interactive stemmata or music scores—while preserving clean ODD architecture.

---

## **26 Content**

**Testing and Debugging ODD Transformations**

Authoring ODD transformation pipelines requires rigorous **iterative testing and debugging**. When a `<model>` rule fails to render as expected, the issue typically traces to one of four common defects (Turska et al., 2016):

| Defect Type | Root Cause | Diagnostic Strategy |
| --- | --- | --- |
| **Predicate Failure** | The XPath expression in `@predicate` evaluated to `false()` | Test XPath expression in VS Code XPath tools or Python `lxml` against the source XML |
| **Parameter Typo** | Parameter `@name` misspelled or unrecognized by the behavior | Check TEI P5 Chapter 22 documentation for valid parameter names |
| **Model Precedence Collision** | A generic fallback model was placed *above* a specific model rule | Reorder `<model>` elements so most specific predicates appear first |
| **Output Target Mismatch** | The `@output` attribute was set to `print` when testing in `web` mode | Verify active transformation mode in TEI Publisher |

To debug transformations systematically:

1. **Inspect Compiled XSLT / XQuery:** Use TEI Publisher’s "Show Generated Code" feature to inspect the raw XQuery or XSLT generated by your ODD;
2. **Browser Developer Tools:** Use the browser DOM inspector to verify whether the expected HTML classes and CSS styles were attached to the rendered elements;
3. **Isolation Testing:** Test isolated XML snippets in VS Code before compiling the full manuscript corpus (Turska et al., 2016; Fischer, 2020).

**Vocabulary.** *Model precedence* — the rule that the first `<model>` whose predicate evaluates to true is executed, while subsequent models are ignored. *XPath builder* — an interactive development tool used to test and validate XPath queries against an XML document. *Isolation testing* — verifying a small fragment of code independently to locate errors quickly.

**Takeaway:** Systematic debugging requires testing XPath predicates, checking parameter names, enforcing model precedence, and inspecting compiled transformation code.

---

## **27 Content**

**Version Controlling ODD Specifications in Git**

Because an ODD file controls both schema validation and publication rendering, it must be rigorously tracked in **Git version control** (Topic 1; Barzaghi et al., 2025).

In collaborative editing projects, changes to an ODD file directly impact all team members. A poorly tested modification to an `<elementSpec>` can immediately cause other transcribers' files to fail schema validation or break live web interfaces.

Best practices for ODD version control include:

| Version Control Stage | Command-Line Action | Best Practice Objective |
| --- | --- | --- |
| **1. Feature Branching** | `git checkout -b feature/odd-apparatus` | Isolates schema modifications from production branch |
| **2. Local Verification** | `java -jar saxon.jar ... && pytest` | Validates compiled schemas and runs unit tests locally |
| **3. Atomic Commit** | `git commit -m "feat(odd): add alternate model"` | Uses structured semantic message documenting changes |
| **4. Pull Request Review** | `gh pr create --title "ODD Update"` | Enforces peer review and automated CI validation |

| Git Discipline | Methodological Reason in ODD Development |
| --- | --- |
| **Atomic Commits** | Isolate schema rule changes from documentation edits for clean bisecting |
| **Semantic Commit Messages** | Clearly state which element (`<app>`, `<choice>`, `<w>`) was modified |
| **Branch Protection** | Require pull request reviews before merging changes to `main` branch |
| **Release Tagging** | Tag stable ODD milestones with semantic versions (e.g., `v1.0.0-odd`) |

Maintaining strict version control discipline ensures that the history of your schema and transformation pipeline is as transparent and reproducible as your textual scholarship (Barzaghi et al., 2025; Wilkinson et al., 2016).

**Vocabulary.** *Semantic commit message* — a structured commit message format (e.g., `feat:`, `fix:`, `docs:`) indicating the precise nature of an edit. *Branch protection* — repository rules preventing direct commits to the production branch without peer review. *Semantic versioning* — standard version numbering scheme (`MAJOR.MINOR.PATCH`).

**Takeaway:** ODD specifications must be managed with atomic Git commits, branch protection, and semantic release tagging to maintain reproducible build history.

---

## **28 Content**

**Integrating ODD Validation into Continuous Integration (CI) Pipelines**

In professional digital humanities engineering, software testing is automated using **Continuous Integration (CI)** services, such as **GitHub Actions** (Barzaghi et al., 2025).

A Continuous Integration pipeline automatically executes every time an editor pushes a commit or opens a pull request. The CI runner spins up a clean Linux virtual environment, downloads validation tools, compiles the ODD specification, and tests all TEI XML documents in the repository:

```yaml
# .github/workflows/validate-edition.yml
name: Validate TEI Digital Edition

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Java Runtime
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Compile ODD to Relax NG Schema
        run: |
          java -jar bin/saxon-he.jar -s:odds/edition.odd \
               -xsl:scripts/odd2relaxng.xsl -o:build/edition.rng

      - name: Validate All TEI XML Files
        run: |
          python3 scripts/lint_lesson_content.py --course-dir .
          xmllint --noout --relaxng build/edition.rng data/*.xml
```

| CI Stage | Automated Verification Action | Pass / Fail Condition |
| --- | --- | --- |
| **1. ODD Compilation** | Compiles `edition.odd` into `edition.rng` | Passes if ODD is structurally well-formed |
| **2. XML Schema Validation** | Validates all XML files against generated `.rng` | Fails if any transcriber introduces an invalid tag |
| **3. Content Linter** | Runs Python linter checking apparatus integrity | Fails if absorbed lists, bad tables, or broken IDs exist |
| **4. Multi-Modal Build** | Compiles Web HTML and Print PDF deliverables | Fails if transformation pipeline throws runtime errors |

Automating validation via GitHub Actions ensures that defects are caught immediately before they reach production servers or published deliverables (Barzaghi et al., 2025).

**Vocabulary.** *Continuous Integration (CI)* — the automated practice of building and testing code on every repository commit. *GitHub Actions* — a CI/CD platform that automates software workflows directly within GitHub repositories. *Virtual test environment* — an isolated cloud container used to execute automated build and test scripts.

**Takeaway:** Continuous Integration pipelines automatically compile ODD specifications and validate all TEI XML documents on every Git push.

---

## **29 Content**

**Comparing TEI Publisher with Static Site Generators (EVT, Wax, Jekyll)**

While TEI Publisher provides an enterprise-grade stack backed by eXist-db, digital editors can choose among several publication platforms, each offering distinct trade-offs between dynamic querying power and long-term archival simplicity (Driscoll & Pierazzo, 2016; Buzzoni, 2016).

| Publishing Platform | Architecture Type | Database Required? | Primary Strengths | Primary Liabilities |
| --- | --- | --- | --- | --- |
| **TEI Publisher** | Client/Server (eXist-db + Web Components) | Yes (eXist-db Native XML) | Full TEI Processing Model support; native IIIF integration; powerful XQuery search | Requires server administration and database maintenance |
| **Edition Visualization Technology (EVT)** | Standalone Static Client (HTML5 + Angular/Vue) | No (Pure Client-Side) | Zero server dependencies; beautiful dual facsimile/text display; portable on USB | Limited customization of complex non-standard TEI structures |
| **Wax / Jekyll** | Static Site Generator (Ruby + Markdown/IIIF) | No (Flat HTML/CSS) | Ultra-lightweight; free hosting on GitHub Pages; permanent bit preservation | Requires flattening rich TEI XML into Markdown / JSON metadata |
| **Custom XSLT Pipeline** | Bespoke Build Script (Saxon + Webpack) | No (Build-time generation) | Total design freedom; tailored to unique project needs | High initial programming cost; maintenance debt |

For classroom and long-term archival projects where server maintenance cannot be guaranteed for decades, **EVT** and **static HTML generators** provide robust solutions because their output consists of static files that will open in any browser indefinitely without a database (Driscoll & Pierazzo, 2016; Sahle, 2016).

However, for advanced multi-modal editions requiring dynamic full-text search, faceted entity filtering, and simultaneous web/print compilation from ODD, **TEI Publisher** remains the gold standard (Turska et al., 2016; Stadler et al., 2016).

**Vocabulary.** *Static site generator* — a software tool that compiles raw source files into static HTML pages at build time. *Edition Visualization Technology (EVT)* — an open-source tool for creating digital editions from TEI XML without a backend database. *Maintenance debt* — the ongoing labor and financial cost required to keep software servers operating over time.

**Takeaway:** Choosing between TEI Publisher, EVT, and static site generators involves balancing dynamic querying power against long-term serverless sustainability.

---

## **30 Content**

**Synthesis: Declarative Transformation as the Bridge from Markup to Interface**

Today, we have explored the computational engine that connects raw philological markup to finished, multi-modal editions.

We have demonstrated that:

1. **The Processing Model Revolution:** The TEI Processing Model supersedes brittle, unmaintainable XSLT stylesheets by formalizing rendering behaviors directly inside the ODD schema (Turska et al., 2016; Stadler et al., 2016).
2. **Literate Specification in ODD:** ODD serves as the unified single source of truth, compiling simultaneously into prose documentation, Relax NG schemas, and transformation pipelines (Burnard & Rahtz, 2004).
3. **Abstract Behaviours:** Mapping tags to standardized behaviours (`inline`, `block`, `paragraph`, `heading`, `alternate`, `note`, `table`) decouples editorial semantics from low-level HTML layout (TEI Consortium, 2026).
4. **Context & Modality Control:** Using `@predicate`, `@output`, `<param>`, and `<modelSequence>` enables complex, context-sensitive styling across web popovers and print footnotes.
5. **Modern Architecture:** TEI Publisher combines eXist-db storage, compiled XQuery transformations, and client-side Web Components to deliver responsive web portals and automated print-ready volumes (Turska et al., 2016).

On Friday, in Lesson 13.3, you will complete the publication assembly, compiling your edition into responsive web applications, standalone interactive HTML packages, and typographically flawless print-ready PDFs.

**Takeaway:** The TEI Processing Model and ODD architecture provide the declarative bridge that transforms structured TEI XML markup into multi-modal scholarly editions.

---

## References

Barzaghi, S., Palmero Aprosio, A., Paolucci, F., & Peroni, S. (2025). The semantic digital edition of Aldo Moro's writings: A workflow supporting data sharing and replicability. *ACM Journal on Computing and Cultural Heritage, 18*(2), Article 24. https://doi.org/10.1145/3725534

Berti, M. (2026). Annotating the ancient world: Critical annotations and digital editions. In *Charting the Future of Historical Humanities* (pp. 45–68). Brepols. https://doi.org/10.1484/M.LECTIO-EB.5.151800

Burnard, L., & Rahtz, S. (2004). RelaxNG with son of ODD. In *Proceedings of Extreme Markup Languages 2004*. Montreal, Canada. https://ora.ox.ac.uk/objects/uuid:b337cb6d-9e7b-4bbc-aa71-f0b9d12bb8de

Buzzoni, M. (2016). A protocol for scholarly digital editions? The Italian point of view. In M. J. Driscoll & E. Pierazzo (Eds.), *Digital Scholarly Editing: Theories and Practices* (pp. 89–108). Open Book Publishers. https://doi.org/10.11647/OBP.0095.05

Camps, J.-B., Spadini, E., & Ing, L. (2019). Collating medieval vernacular texts: Aligning witnesses, classifying variants. In *Digital Humanities 2019: Conference Abstracts* (pp. 1–6). Utrecht University. https://hal.science/hal-02268348

Coombs, J. H., Renear, A. H., & DeRose, S. J. (1987). Markup systems and the future of scholarly text processing. *Communications of the ACM, 30*(11), 933–947. https://doi.org/10.1145/32206.32209

Driscoll, M. J., & Pierazzo, E. (Eds.). (2016). *Digital scholarly editing: Theories and practices*. Open Book Publishers. https://doi.org/10.11647/OBP.0095

Fischer, F. (2020). 6.3 Representing the critical text. In P. Roelli (Ed.), *Handbook of Stemmatology: History, Methodology, Digital Approaches* (pp. 405–424). De Gruyter. https://doi.org/10.1515/9783110684384-006

Pierazzo, E. (2015). *Digital scholarly editing: Theories, models and methods*. Ashgate Publishing / Routledge. https://doi.org/10.4324/9781315577227

Pierazzo, E. (2016). Modelling digital scholarly editions: 'In the making'. In M. J. Driscoll & E. Pierazzo (Eds.), *Digital Scholarly Editing: Theories and Practices* (pp. 61–77). Open Book Publishers. https://doi.org/10.11647/OBP.0095.04

Renear, A. H. (2004). Text encoding. In S. Schreibman, R. Siemens, & J. Unsworth (Eds.), *A Companion to Digital Humanities* (pp. 218–239). Blackwell. https://doi.org/10.1002/9780470999875.ch17

Sahle, P. (2016). What is a scholarly digital edition? In M. J. Driscoll & E. Pierazzo (Eds.), *Digital Scholarly Editing: Theories and Practices* (pp. 19–39). Open Book Publishers. https://doi.org/10.11647/OBP.0095.02

Sanderson, R., Ciccarese, P., & Young, B. (Eds.). (2017). *Web Annotation Data Model* (W3C Recommendation 23 February 2017). World Wide Web Consortium. https://www.w3.org/TR/annotation-model/

Stadler, P., Illetschko, M., & Veit, J. (2016). Towards a digital edition of the Carl Maria von Weber complete works. *International Journal of Humanities and Arts Computing, 10*(1), 67–85. https://doi.org/10.3366/ijhac.2016.0160

Tafdrup, J., Bjerring-Hansen, J., & Hansen, J. N. (2026). Convergences: AI, editorial practice, and the Danish Digital Scholarly Edition of Grundtvig’s Works. *International Journal of Digital Humanities, 8*, 191–211. https://doi.org/10.1007/s42803-026-00125-z

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and interchange* (Version 4.8.1). TEI Consortium. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/

Turska, M., Cummings, J., & Rahtz, S. (2016). Challenging the myth of presentation in digital editions: The TEI Processing Model. *Journal of the Text Encoding Initiative, 9*, 1–22. https://doi.org/10.4000/jtei.1467

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., ... & Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data, 3*, Article 160018. https://doi.org/10.1038/sdata.2016.18
