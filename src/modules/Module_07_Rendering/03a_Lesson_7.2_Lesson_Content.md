# Lesson 7.2 — Rendering by Rule: XSLT, CETEIcean, and Print Stylesheets

*RELS 398 / ENGL 398 · Topic 7: Rendering (Publication I) · Meeting #18 (Wed Oct 21)*

***Step 2 of the three-step cycle: deterministic software.** Yesterday you rendered a few lines of your document by hand. Today you write rules that render the whole file the same way every time, first with an XSLT stylesheet run by Python and then with CETEIcean in the browser. Tuesday's hand-made page is the standard: wherever a tool's output differs from it, you must decide whether the tool is wrong or your decisions were incomplete.*

---

## **01 Content**

**From Hand to Rule**

On Tuesday you wrote HTML for ten or more lines of your document, one span at a time. It worked, and it taught you exactly what each TEI element should become. But it would not scale. Andromeda's treaty runs to many articles, Ace's decree to many clauses, and Olyvia's letter, though short, will be revised again before December. Every time the TEI file changes, a hand-made page falls out of date.

The answer is the same one you reached in Week 6. On Tuesday of that week you regularized spelling by hand; on Wednesday you wrote `normalize.py`, which applied your rules to the whole text in seconds. Today you do the same for rendering. Each row of your `RENDERING.md` table becomes a rule that a program can apply to every element of its kind, everywhere in the file.

The work changes character. Yesterday the question was how one line should look. Today the question is how every `<choice>`, every `<lb/>` and every `<gap/>` should look, wherever it occurs, including places you have not looked at closely. A rule is a promise about cases you have not seen.

**Vocabulary.** *Rule-based rendering* — Producing a reader's view by applying written rules to every element of a given kind. *Scaling* — Applying a method to a whole document, or many documents, instead of a sample.

**Takeaway:** A hand-made page shows what each element should become; today you turn each of those decisions into a rule that renders the whole file automatically.

---

## **02 Content**

**What Deterministic Means**

A deterministic program gives the same output every time it receives the same input. Run your stylesheet on Monday or in December, on your laptop or on a classmate's, and the page it produces from the same TEI file will be identical, character for character.

That property is what makes a rendering trustworthy. If a reader finds an error in your reading view, you can trace it. Either the TEI file says something wrong, or one rule in the stylesheet does something wrong. There is no third possibility, no mood or randomness in the tool. You fix the file or the rule, run it again, and the error is gone everywhere it occurred.

Compare this with what you will meet on Friday. An AI model asked to render the same file twice may produce two different pages, and neither will come with a list of the rules it followed. Today's tools are less clever but fully accountable: every choice they make is written down in a file you can read.

Determinism does not mean correctness. A deterministic rule that drops every gap will drop every gap, faithfully, every time. That is why the comparison with Tuesday's page matters so much.

**Vocabulary.** *Deterministic* — Always producing the same output from the same input. *Traceable* — Able to be followed back to the exact rule or data that caused it.

**Takeaway:** A deterministic stylesheet gives identical output every run, so every error can be traced to one rule or one line of TEI, but it will repeat a wrong rule just as faithfully as a right one.

---

## **03 Content**

**Rendering in Real Projects**

Rule-based rendering is not a classroom exercise; it is how working editions are published. One recent manuscript repository stores each manuscript as a TEI document and turns it into the HTML page a visitor sees by running an XSLT stylesheet (Clausen et al., 2026).

Its builders note that TEI files and images rendered dynamically through XSLT already give them everything needed to publish critical editions later (Clausen et al., 2026). In other words, the investment in a careful encoding pays off because rules can turn it into new kinds of pages as the project grows.

Rendering also serves the editors themselves, long before any reader arrives. A team that trained cataloguers to edit TEI records directly wrote an XSLT template that produced an HTML preview of each record, and found it very helpful for proofreading on the spot (Faghihi et al., 2022). A page is easier to proofread than raw markup, because errors that hide among the tags stand out in running text.

You will use your stylesheets the same way. Each time you change your TEI file between now and December, run the stylesheet and read the result. It is a quick check that your markup still says what you think it says.

**Vocabulary.** *Repository* — A managed collection of digital objects, such as TEI files and images, with ways to view and retrieve them. *Preview* — A rendering made for the editor's own checking rather than for publication.

**Takeaway:** Working projects render TEI with stylesheets both to publish their editions and to proofread their own encoding, and you can do both with today's tools.

---

## **04 Content**

**Two Routes from TEI to a Web Page**

There are two common ways to turn a TEI file into a web page, and today you will try both.

The first route transforms the file in advance. A program reads your TEI, applies a stylesheet written in XSLT, and writes out a new HTML file. You then publish that HTML file. The reader's browser never sees your TEI at all; it receives an ordinary web page, like the one you wrote by hand on Tuesday.

The second route transforms the file in the reader's browser. You publish the TEI file itself, together with a small JavaScript library called CETEIcean. When a reader opens the page, CETEIcean fetches the TEI file and turns each TEI element into a matching HTML element on the spot. You then style those elements with CSS, much as you did on Tuesday.

<table>
  <thead>
    <tr><th></th><th>XSLT</th><th>CETEIcean</th></tr>
  </thead>
  <tbody>
    <tr><td>When the transformation happens</td><td>Before publication, on your computer</td><td>Each time a reader opens the page</td></tr>
    <tr><td>What you publish</td><td>HTML files</td><td>Your TEI file, a small HTML page, and CSS</td></tr>
    <tr><td>Where your decisions live</td><td>Mostly in the XSLT stylesheet</td><td>Mostly in the CSS</td></tr>
    <tr><td>Language to learn</td><td>XSLT</td><td>CSS, with a little JavaScript</td></tr>
  </tbody>
</table>

Both routes are deterministic, and both can carry out the decisions in your `RENDERING.md`. They differ in where those decisions are written down, and that difference shapes what can go wrong.

**Vocabulary.** *XSLT* — A language for writing rules that transform one XML document into another document, such as an HTML page. *CETEIcean* — A JavaScript library that displays TEI in a web browser by turning TEI elements into custom HTML elements.

**Takeaway:** XSLT turns TEI into HTML before you publish; CETEIcean turns it into HTML in the reader's browser; both apply your decisions, but they store them in different places.

---

## **05 Content**

**What XSLT Is**

XSLT stands for Extensible Stylesheet Language Transformations. An XSLT stylesheet is itself an XML file, made of **templates**. Each template says: when you meet an element of this kind, write out this instead.

Here is one template:

```xml
<xsl:template match="tei:p">
  <p><xsl:apply-templates/></p>
</xsl:template>
```

The `match` attribute names the element the template applies to, here every TEI `<p>`. The body of the template is what gets written to the output: an HTML `<p>`, and inside it the instruction `<xsl:apply-templates/>`. That instruction means: now process everything inside this element, using whatever templates match it. So the paragraph's words, its `<choice>` elements and its line breaks are each handed to their own templates in turn.

This is the whole idea. The processor walks through your TEI file from the top, finds the template that matches each element, writes what the template says, and moves inward. Your stylesheet is a list of templates, roughly one per row of your decision table.

On Tuesday you read that XSLT can turn one XML file into a web page, a plain-text file, or a file that becomes a PDF. Today you write the stylesheet yourself.

**Vocabulary.** *Template* — An XSLT rule that matches one kind of element and says what to write in its place. *`xsl:apply-templates`* — The XSLT instruction that processes an element's contents with whatever templates match them.

**Takeaway:** An XSLT stylesheet is a list of templates; each matches one kind of TEI element and writes HTML in its place, then hands the element's contents on to other templates.

---

## **06 Content**

**Setting Up: Python, lxml, and a Small Script**

You already have Python from Week 6. To run XSLT you need one more package, `lxml`, which contains a complete XSLT processor. Install it once from the VS Code terminal:

```bash
python3 -m pip install lxml
```

On Windows, type `py` instead of `python3` if that is how you ran `normalize.py`. Then save this short script as `rendering/render.py` in your repository:

```python
import sys
from lxml import etree

xml_file, xsl_file, out_file = sys.argv[1], sys.argv[2], sys.argv[3]
transform = etree.XSLT(etree.parse(xsl_file))
result = transform(etree.parse(xml_file))
with open(out_file, "wb") as f:
    f.write(etree.tostring(result, method="html", encoding="utf-8"))
print("Wrote", out_file)
```

The script takes three names: your TEI file, a stylesheet, and the HTML file to write. It reads the stylesheet, applies it to the TEI file, and saves the result. From the top of your repository you will run it like this:

```bash
python3 rendering/render.py transcription_normalized.xml rendering/reading.xsl rendering/reading-auto.html
```

Write the output into the `rendering/` folder, next to Tuesday's CSS files, so the generated page can find them. Use a new name such as `reading-auto.html`, so the generated page never overwrites your hand-made `edition.html`. You need both for the comparison later today.

**Vocabulary.** *`lxml`* — A Python package for reading, writing and transforming XML, including an XSLT processor. *Command-line argument* — A value typed after a script's name that tells the script what to work on.

**Takeaway:** Install `lxml`, save the short `render.py`, and run it with your TEI file, a stylesheet and an output name; write the output beside Tuesday's CSS under a new name.

---

## **07 Content**

**The Built-in Rules: What Happens to Elements You Forget**

Before you write templates, you need to know what XSLT does with an element that has no template. The answer surprises almost everyone, and it is the source of most rendering errors.

XSLT has a few **built-in rules** that apply when none of your templates match. For an element, the built-in rule writes nothing for the element itself but processes its contents. For text, the built-in rule copies the text to the output. Together they mean that an element without a template simply disappears, and its words fall through into the page as plain text.

Think about what that does to a `<choice>`. Suppose you forgot to write a template for it. The built-in rule processes both children, and both children's text falls through:

```text
That the GovrGovernor and CouncillCouncil of the Pro-vince
```

Both layers appear, glued together. That error is loud and easy to spot. A quieter one follows from the same rule. An empty element, such as `<gap/>` or `<lb/>`, has no contents to fall through. Without a template it vanishes without a trace, and nothing on the page tells you something is missing.

**Vocabulary.** *Built-in rule* — A default behaviour XSLT applies to any element or text that no template matches. *Fall-through* — The way an unmatched element's text passes into the output as plain text.

**Takeaway:** An element with no template disappears and its text falls through as plain words; this glues both layers of a `<choice>` together and silently deletes empty elements such as `<gap/>`.

---

## **08 Content**

**The Namespace Pitfall**

The garbled line in the last section can also appear when you *did* write a `<choice>` template. If it does, the cause is almost always the namespace.

Every element in your TEI file belongs to the TEI namespace, which your root element declares with `xmlns="http://www.tei-c.org/ns/1.0"`. To an XSLT processor, a TEI `<choice>` and a `<choice>` in no namespace are different elements. A template written as `match="choice"` matches the second kind only, so it never fires on your file, and the built-in rules take over.

The fix is to declare the TEI namespace in your stylesheet, give it a short prefix, and use the prefix in every match:

```xml
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="tei">
```

Now `match="tei:choice"` means a TEI `<choice>`, and it matches. The attribute `exclude-result-prefixes="tei"` keeps the prefix declaration out of your HTML.

If your output ever shows both layers of every `<choice>` side by side, check the prefixes first. It is the most common mistake in XSLT for TEI.

**Vocabulary.** *Namespace* — A unique name, written as a web address, that marks which vocabulary an element belongs to. *Prefix* — A short label, such as `tei:`, that stands for a namespace inside a stylesheet.

**Takeaway:** Declare the TEI namespace with a `tei:` prefix and use it in every match; a template without the prefix never fires, and the built-in rules quietly take over.

---

## **09 Content**

**The Page Shell**

Your first template matches the whole document and writes the outer frame of the web page: the same shell you wrote by hand on Tuesday.

```xml
<xsl:output method="html" encoding="utf-8"/>

<xsl:template match="/">
  <html lang="en">
    <head>
      <meta charset="utf-8"/>
      <title><xsl:value-of select="//tei:titleStmt/tei:title[1]"/></title>
      <link rel="stylesheet" href="reading.css"/>
    </head>
    <body>
      <xsl:apply-templates select="//tei:body"/>
    </body>
  </html>
</xsl:template>
```

The `match="/"` means the whole document. The `xsl:value-of` instruction copies text from your file into the page, here the first title in your `teiHeader`, so the browser tab shows your document's title. The `select` attribute on `xsl:apply-templates` restricts processing to your `<body>`. Without it, every word of your `teiHeader` would fall through into the top of the page.

Notice that the shell carries over two decisions from Tuesday: the `charset` that keeps accents intact and the `lang` that tells software which language it is reading. The link points to Tuesday's `reading.css`, which is why you write the output into the same folder.

**Vocabulary.** *`xsl:value-of`* — The XSLT instruction that writes the text of a selected element into the output. *`select`* — An attribute giving an XPath expression that picks out which part of the document to use.

**Takeaway:** The root template writes the HTML shell, copies your title from the header, keeps `charset` and `lang`, and processes only the `<body>` so the header does not spill onto the page.

---

## **10 Content**

**Structure: Divisions, Headings, and Paragraphs**

Next come the structural elements. These are the easiest templates, because HTML has close equivalents.

```xml
<xsl:template match="tei:div">
  <section class="{@type}"><xsl:apply-templates/></section>
</xsl:template>

<xsl:template match="tei:head"><h2><xsl:apply-templates/></h2></xsl:template>

<xsl:template match="tei:p"><p><xsl:apply-templates/></p></xsl:template>
```

The curly braces in `class="{@type}"` are new. They are called an **attribute value template**: XSLT replaces the expression inside the braces with its value. `@type` means the `type` attribute of the current element. So `<div type="article">` becomes `<section class="article">`, and a `<div type="clause">` in Ace's decree becomes `<section class="clause">`. One template handles every kind of division.

A letter has its own structure. If Olyvia's file uses `<opener>`, `<salute>`, `<closer>` and `<signed>`, each needs a template, or each will fall through as plain text and lose the separation from the body that she decided on yesterday. A template such as `<xsl:template match="tei:closer"><p class="closer"><xsl:apply-templates/></p></xsl:template>` brings back the class her `reading.css` already styles.

**Vocabulary.** *Attribute value template* — Curly braces inside an output attribute, telling XSLT to insert a computed value. *`@`* — In XPath, the sign that names an attribute rather than an element.

**Takeaway:** Map divisions, headings and paragraphs to HTML equivalents, use `{@type}` to carry attribute values into classes, and give every structural element in your file its own template.

---

## **11 Content**

**Choosing a Layer: The `<choice>` Template**

Here is where today's method parts ways with Tuesday's. On Tuesday your HTML held both layers of every `<choice>`, and the CSS hid one of them. An XSLT stylesheet can do something more decisive: it can write only one layer into the page.

```xml
<xsl:template match="tei:choice">
  <xsl:apply-templates select="tei:reg|tei:expan|tei:corr"/>
</xsl:template>
```

The vertical bar means or; spaces around it are allowed but not needed. This template says: when you meet a `<choice>`, process only its `<reg>`, `<expan>` or `<corr>` child, and ignore the rest. The `<orig>`, `<abbr>` and `<sic>` are never processed, so their text never reaches the page.

Then give the chosen children the same class names you used by hand on Tuesday, so that Tuesday's CSS still applies:

```xml
<xsl:template match="tei:reg|tei:expan|tei:corr|tei:ex|tei:unclear">
  <span class="{local-name()}"><xsl:apply-templates/></span>
</xsl:template>
```

The function `local-name()` gives the element's name without its prefix, so a `<reg>` becomes `<span class="reg">` and an `<unclear>` becomes `<span class="unclear">`. One template covers five elements and repeats exactly the naming convention from Tuesday's section 17.

**Vocabulary.** *`|` (union)* — In XPath, joins two selections, meaning this one or that one. *`local-name()`* — An XPath function returning an element's name without any namespace prefix.

**Takeaway:** A `<choice>` template that selects only one child writes one layer into the page; giving the output Tuesday's class names lets Tuesday's CSS style it unchanged.

---

## **12 Content**

**Abbreviations and Supplied Letters**

Abbreviations deserve a closer look, because they combine two of your decisions. In the diplomatic view the reader sees the abbreviation as written, perhaps with a raised letter. In the reading view the reader sees the expansion, with the letters you supplied in italics.

Take the illustrative line from Tuesday's worked example:

```xml
<choice><abbr>Gov<hi rend="sup">r</hi></abbr><expan>Gov<ex>erno</ex>r</expan></choice>
```

In the reading stylesheet, the `<choice>` template chooses `<expan>`. The shared template from section 11 writes `<span class="expan">`, and inside it, the `<ex>` becomes `<span class="ex">`. Tuesday's rule `.expan .ex { font-style: italic; }` then sets *erno* in italics. The result reads Gov*erno*r, with the editor's contribution visible.

In the diplomatic stylesheet, the `<choice>` template chooses `<abbr>` instead, and the raised letter needs one more template:

```xml
<xsl:template match="tei:hi[@rend='sup']"><sup><xsl:apply-templates/></sup></xsl:template>
```

The square brackets in the match are a **predicate**: a condition the element must meet. This template matches only a `<hi>` whose `rend` attribute is `sup`. If your file uses `<hi>` with other values, such as underlining, each needs its own template, or its text will fall through without any mark.

**Vocabulary.** *Predicate* — A condition in square brackets that narrows which elements a match or selection applies to. *Supplied letters* — Letters added by the editor to complete an abbreviation, recorded in TEI with `<ex>`.

**Takeaway:** The reading stylesheet chooses `<expan>` and marks `<ex>` for italics; the diplomatic one chooses `<abbr>` and needs a predicate template for raised letters and every other `<hi>` your file uses.

---

## **13 Content**

**Line Breaks by Rule**

Line breaks are where the two views differ most, and they are empty elements, so a missing template would delete them silently. Write them carefully.

In the diplomatic stylesheet, reproduce Tuesday's markup exactly:

```xml
<xsl:template match="tei:lb">
  <span class="lb" data-n="{@n}"></span>
</xsl:template>
```

Every `<lb n="12"/>` becomes `<span class="lb" data-n="12"></span>`, the same empty span you typed by hand, and Tuesday's `diplomatic.css` turns it into a new numbered line.

In the reading stylesheet, a line break should become a space, so that the last word of one line does not glue onto the first word of the next:

```xml
<xsl:template match="tei:lb"><xsl:text> </xsl:text></xsl:template>
<xsl:template match="tei:lb[@break='no']"/>
```

The `xsl:text` element writes exactly what it contains, here a single space. XSLT normally throws away whitespace inside a stylesheet, so a bare space would be lost; `xsl:text` protects it. The second template, which is empty, handles a word split across two lines. A break marked `break="no"` produces nothing at all, so the two halves can rejoin. When two templates match the same element, the more specific one, with the predicate, wins.

**Vocabulary.** *`xsl:text`* — The XSLT element that writes its exact contents, including spaces, to the output. *Template priority* — The rule that a more specific match, such as one with a predicate, wins over a general one.

**Takeaway:** In the diplomatic view each `<lb/>` becomes Tuesday's numbered span; in the reading view it becomes a protected space, except a `break="no"` break, which becomes nothing.

---

## **14 Content**

**Words Split Across Lines**

The empty template for `break="no"` is not quite enough. Many TEI files put each `<lb/>` at the start of a new line in the XML, like this:

```xml
of the Pro-
<lb n="13" break="no"/>vince
```

The new line and indentation between *Pro-* and the `<lb/>` are ordinary text in the file. The `<lb/>` produces nothing, but that whitespace survives, and the browser shows *Pro- vince* with a space in the middle of the word.

A template for text can remove it. This one matches any piece of text that sits directly before a `break="no"` line break, squeezes out its extra whitespace, and keeps one space at the front only if there was one:

```xml
<xsl:template match="text()[following-sibling::node()[1][self::tei:lb[@break='no']]]">
  <xsl:if test="normalize-space(substring(.,1,1))='' and normalize-space(.)!=''">
    <xsl:text> </xsl:text>
  </xsl:if>
  <xsl:value-of select="normalize-space(.)"/>
</xsl:template>
```

You do not need to master every part of this. Read it as a recipe: copy it into your reading stylesheet, run it, and search the output for the split words in your file. Notice what it does not do. The hyphen in *Pro-vince* stays, because it is written in your transcription. If your Week 6 policy removed such hyphens in the reading text, that decision belongs in a `<choice>` in your TEI, not in a hidden trick in the stylesheet.

**Vocabulary.** *`normalize-space()`* — An XPath function that trims leading and trailing whitespace and reduces internal runs of whitespace to single spaces. *Recipe* — A tested piece of code you reuse without needing to rebuild it from first principles.

**Takeaway:** Whitespace before a `break="no"` line break survives as a stray space; a text template removes it, while the hyphen stays because it belongs to your transcription.

---

## **15 Content**

**Uncertainty by Rule: `<unclear>` and `<gap/>`**

Your decision table says that uncertainty shows in both views. The `<unclear>` element is already handled: the shared template from section 11 writes `<span class="unclear">`, and Tuesday's dotted underline applies.

The `<gap/>` element needs its own template, because it is empty. Without one, it vanishes. With one, you can do better than Tuesday's hand-typed brackets, because attribute value templates can copy the reason and extent straight from your TEI:

```xml
<xsl:template match="tei:gap">
  <span class="gap" title="{@reason}, {@quantity} {@unit}(s)">[…<span class="gap-info"><xsl:value-of select="concat(' ',@quantity,' ',@unit,'(s), ',@reason)"/></span>]</span>
</xsl:template>
```

For `<gap reason="damage" quantity="2" unit="word"/>`, this writes brackets with a tooltip reading *damage, 2 word(s)*. It also writes the same information as real text inside a `gap-info` span. For now, add `.gap-info { display: none; }` to both CSS files; in section 24 you will make that text appear on paper, where tooltips do not exist.

Two details are worth noticing. The `concat()` function joins pieces of text, and the space at its start is inside quotation marks so it survives. And the stylesheet copies attribute values exactly as they are, which is why the output says *word(s)*: XSLT does not know English plurals. A rule can only be as smart as you make it.

**Vocabulary.** *`concat()`* — An XPath function that joins several pieces of text into one. *Tooltip* — A short explanation that appears when the pointer rests on an element, set by the HTML `title` attribute.

**Takeaway:** Give `<gap/>` a template or it vanishes; attribute value templates can copy its reason and extent into both a tooltip and real text, exactly as written in your TEI.

---

## **16 Content**

**Two Stylesheets, One Source**

You now have every template for the reading view. Save them together, inside the `xsl:stylesheet` element from section 08, as `rendering/reading.xsl`. Then copy the file to `rendering/diplomatic.xsl` and change four things:

<table>
  <thead>
    <tr><th>Template</th><th><code>reading.xsl</code></th><th><code>diplomatic.xsl</code></th></tr>
  </thead>
  <tbody>
    <tr><td>Page shell</td><td>Links <code>reading.css</code></td><td>Links <code>diplomatic.css</code></td></tr>
    <tr><td><code>&lt;choice&gt;</code></td><td>Selects <code>reg | expan | corr</code></td><td>Selects <code>orig | abbr | sic</code></td></tr>
    <tr><td>Shared span template</td><td><code>reg | expan | corr | ex | unclear</code></td><td><code>orig | abbr | sic | unclear</code></td></tr>
    <tr><td><code>&lt;lb/&gt;</code></td><td>A space, or nothing for <code>break="no"</code></td><td>Tuesday's numbered span</td></tr>
  </tbody>
</table>

The diplomatic stylesheet also needs the raised-letter template from section 12, and it does not need the split-word recipe, since each line keeps its own break. Run both:

```bash
python3 rendering/render.py transcription_normalized.xml rendering/reading.xsl rendering/reading-auto.html
python3 rendering/render.py transcription_normalized.xml rendering/diplomatic.xsl rendering/diplomatic-auto.html
```

Open each result in your browser. Your whole document, not just ten lines, now appears in both views. The two stylesheets are a precise, runnable copy of your `RENDERING.md` table, and the differences between them are exactly the differences between the two columns of that table.

It is possible to write a single stylesheet that takes the view as a setting, but two short files are easier to read and to compare.

**Vocabulary.** *Source file* — The one authoritative file, here your TEI, from which every view is generated. *Stylesheet pair* — Two stylesheets applied to the same source to produce two views.

**Takeaway:** Save `reading.xsl`, copy it to `diplomatic.xsl` with four changes and one extra template, and run both to produce full-length versions of both views.

---

## **17 Content**

**Comparing the Generated Pages with Tuesday's**

Now open Tuesday's hand-made `edition.html` and today's generated pages side by side, on the same lines, in the same view.

First look at the screen. The words should match, the italics should match, and gaps and unclear readings should carry the same marks. Then look underneath. In your browser, right-click and choose View Page Source for each page. Tuesday's page contains both layers of every `<choice>`, one hidden by CSS. Today's reading page contains only the reading layer. The original spellings are not hidden; they are simply not there.

This difference matters for what readers can do. A reader of Tuesday's page could, with a little effort, recover the original spelling from the source. A reader of today's reading page cannot; for that, they need the diplomatic page. Neither approach is wrong, but your rendering statement should now tell readers where to find the other view, and both pages should link to each other.

Record each difference you find in `RENDERING.md`, under a new heading such as Step 2 comparison. Some differences will be improvements: the generated gap carries its reason, and the whole document is present. Others will be problems. Section 28 shows how to sort them.

**Vocabulary.** *Page source* — The HTML file as the browser received it, before CSS hides or shows anything. *Side-by-side comparison* — Viewing two renderings of the same lines together to find every difference.

**Takeaway:** Compare the generated pages with Tuesday's both on screen and in the page source; the XSLT pages drop one layer entirely, so each view must link to the other.

---

## **18 Content**

**Generic Stylesheets Make Generic Decisions**

You may wonder why you are writing a stylesheet at all, when ready-made stylesheets for TEI exist. The TEI Consortium itself maintains a large set that can turn almost any TEI file into HTML.

Ready-made stylesheets are valuable, but they must make decisions without knowing your document. A generic stylesheet has to pick some way to display `<choice>` for every project at once. It might show both layers, or one, or put one in a tooltip. Whatever it picks, it picks for a parliamentary decree and a painter's letter alike. It does not know that Olyvia's policy forbids regularizing Maud Lewis's grammar, or that Andromeda's readers need the treaty's article numbers.

So a generic stylesheet does not remove the need for your decision table. It moves the work: instead of writing templates, you must check every one of its decisions against yours and override those that disagree. For a large project that is often worth it. For a single document with a short decision table, a stylesheet of your own is shorter than the list of overrides.

The same reasoning applies on Friday. An AI model asked to write you a stylesheet will produce something generic unless you give it your table, and even then you must check every rule.

**Vocabulary.** *Generic stylesheet* — A stylesheet written to render many projects' files, with display decisions made in advance. *Override* — A rule you add to replace a decision someone else's stylesheet made.

**Takeaway:** Ready-made stylesheets make display decisions without knowing your document, so using one means checking and overriding its choices rather than skipping your own.

---

## **19 Content**

**What CETEIcean Does**

Now for the second route. CETEIcean is a JavaScript library that runs in the reader's browser. It does not convert TEI into ordinary HTML elements such as `<p>` and `<span>`. Instead, it keeps your TEI structure and renames each element.

Every TEI element becomes a **custom element** whose name is `tei-` followed by the TEI name in lower case. Your `<choice>` becomes `<tei-choice>`, your `<lb/>` becomes `<tei-lb>`, and your `teiHeader` becomes `<tei-teiheader>`. Attributes are kept, so `<lb n="12"/>` becomes `<tei-lb n="12">`. The structure of the page in the browser is a one-for-one copy of your TEI file.

That has a striking consequence: nothing is chosen in advance. Both layers of every `<choice>` arrive in the page, just as they did in Tuesday's hand-made HTML. Every display decision, including which layer to show, is left to your CSS.

In that sense CETEIcean is closer to Tuesday's method than XSLT is. On Tuesday you hand-wrote spans named after TEI elements; CETEIcean writes the same kind of named elements for you, automatically, for the whole file.

**Vocabulary.** *Custom element* — An HTML element with a made-up name containing a hyphen, which browsers accept and display without built-in styling. *`tei-` element* — The custom element CETEIcean creates for each TEI element, such as `<tei-choice>`.

**Takeaway:** CETEIcean renames every TEI element as a `tei-` custom element and keeps both layers of every `<choice>`, leaving every display decision to your CSS.

---

## **20 Content**

**Setting Up CETEIcean**

A CETEIcean page is a small HTML file that loads the library and tells it which TEI file to fetch. Save this as `rendering/ceteicean.html`:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>My edition</title>
    <link rel="stylesheet" href="cetei-reading.css">
    <script src="https://cdn.jsdelivr.net/npm/CETEIcean@1.9.5/dist/CETEI.js"></script>
  </head>
  <body>
    <div id="TEI"></div>
    <script>
      const c = new CETEI();
      c.getHTML5("../transcription_normalized.xml", function (data) {
        document.getElementById("TEI").appendChild(data);
      });
    </script>
  </body>
</html>
```

The `<script src>` line loads CETEIcean version 1.9.5 from a public server. The second script creates a CETEIcean object, asks it to fetch your TEI file from the folder above, and places the result inside the empty `<div>`.

If you double-click this file, you will see a blank page. Browsers refuse to let a page fetch other files from your disk, for security. You need a small local web server. From the top of your repository, run:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/rendering/ceteicean.html` in your browser. Press Ctrl+C in the terminal when you are finished to stop the server.

**Vocabulary.** *Local web server* — A program on your own computer that serves files to your browser as a website would. *CDN* — A content delivery network, a public server that hosts libraries such as CETEIcean for pages to load.

**Takeaway:** A CETEIcean page loads the library and fetches your TEI file; it must be opened through a local web server, such as Python's `http.server`, not by double-clicking.

---

## **21 Content**

**Styling `tei-` Elements: The Reading View**

When the page first loads, it will look like an unbroken stream of words. That is because browsers know nothing about custom elements, so they display every one of them inline, like a `<span>`. Your headings and paragraphs run together. CSS must give each structural element its display.

Save this as `rendering/cetei-reading.css`:

```css
tei-head { display: block; font-size: 1.4em; font-weight: bold; margin: 1em 0 0.5em; }
tei-p    { display: block; margin-bottom: 1em; }

tei-orig, tei-abbr, tei-sic { display: none; }
tei-expan tei-ex { font-style: italic; }
tei-unclear { text-decoration: underline dotted; }
```

Compare these rules with Tuesday's `reading.css`. They are almost identical. Where Tuesday's selector was `.orig`, a class you wrote by hand, today's is `tei-orig`, an element CETEIcean wrote. The selector `tei-expan tei-ex` means an `<ex>` anywhere inside an `<expan>`, just like Tuesday's `.expan .ex`.

Notice the first two rules. On Tuesday and in your XSLT, a TEI `<p>` became an HTML `<p>`, which browsers already display as a block. Here nothing is automatic. If your file uses `<closer>`, `<salute>`, list items or table rows, each needs a `display` rule too, or it will run into its neighbours.

**Vocabulary.** *Inline element* — An element that flows within a line of text, like a word, rather than starting a new line. *Descendant selector* — A CSS selector with a space, such as `tei-expan tei-ex`, matching one element inside another.

**Takeaway:** Browsers display custom elements inline, so your CSS must make every structural `tei-` element a block, and the layer rules are Tuesday's rules with `tei-` names.

---

## **22 Content**

**The Diplomatic View and the Empty Gap**

The diplomatic view in CETEIcean follows the same pattern. Save this as `rendering/cetei-diplomatic.css`, and change the `<link>` in a copy of your page, `ceteicean-diplomatic.html`, to point to it:

```css
tei-head { display: block; font-size: 1.4em; font-weight: bold; }
tei-p    { display: block; }

tei-reg, tei-expan, tei-corr { display: none; }
tei-lb::before { content: "\A" attr(n) "  "; white-space: pre; color: #666; }
tei-hi[rend="sup"] { vertical-align: super; font-size: 0.75em; }
tei-unclear { text-decoration: underline dotted; }
```

The line-break rule is Tuesday's rule with one change: the line number now comes from the `n` attribute, which CETEIcean kept, rather than from a `data-n` you typed.

Now find a gap in your document. It is not there. Your `<gap/>` became an empty `<tei-gap>`, and an empty element shows nothing. This is the CETEIcean version of the problem from section 07, and you must fix it with a **behavior**: a rule, written in JavaScript, that CETEIcean applies to every element of a kind. Add one line before `getHTML5` in both pages:

```javascript
c.addBehaviors({ tei: { gap: ["[…]"] } });
```

This puts real brackets inside every `<tei-gap>`, as text that can be copied and read aloud. To show the reason and extent as well, a longer behavior can read the attributes; for today, record in `RENDERING.md` that CETEIcean's gaps carry brackets only.

**Vocabulary.** *Behavior* — In CETEIcean, a JavaScript rule that changes how every element of one kind is displayed. *Empty element* — An element with no content, such as `<gap/>` or `<lb/>`, which displays nothing unless a rule supplies something.

**Takeaway:** The diplomatic CSS reuses Tuesday's rules with `tei-` names and the kept `n` attribute; an empty `<gap/>` shows nothing until a behavior puts real brackets inside it.

---

## **23 Content**

**XSLT or CETEIcean?**

You have now rendered your file both ways. Which should your edition use in December? The answer depends on your readers and on what you want to maintain.

<table>
  <thead>
    <tr><th>Question</th><th>XSLT</th><th>CETEIcean</th></tr>
  </thead>
  <tbody>
    <tr><td>Does the page work without JavaScript?</td><td>Yes, it is plain HTML</td><td>No</td></tr>
    <tr><td>Can readers download your TEI?</td><td>Only if you publish it separately</td><td>Yes, the page is built from it</td></tr>
    <tr><td>Where do I change a decision?</td><td>The stylesheet, then run it again</td><td>The CSS, then refresh</td></tr>
    <tr><td>What happens to an element I forgot?</td><td>Its text falls through; empty ones vanish</td><td>It shows inline as plain text; empty ones vanish</td></tr>
    <tr><td>Can it pick one layer at build time?</td><td>Yes</td><td>No; both layers are always in the page</td></tr>
  </tbody>
</table>

There is also a third route you will meet in December: ready-made edition viewers. One Italian research project built its digital editions, including two texts surviving in a single manuscript, with a ready-made viewer called EVT, Edition Visualization Technology (Lazzerini & Di Franco, 2026). Viewers like EVT offer facsimile and text side by side with little coding, but, like generic stylesheets, they bring their own decisions.

For a single document in this course, either of today's routes is sound. Choose the one whose rules you can read and maintain, and record your choice and its reason in `RENDERING.md`.

**Vocabulary.** *Maintenance* — The ongoing work of keeping an edition correct and working as files and tools change. *Edition viewer* — Ready-made software that displays TEI editions, often with images, through a fixed interface.

**Takeaway:** XSLT gives plain HTML with one layer chosen in advance; CETEIcean keeps your TEI in the page with every decision in CSS; choose the one you can maintain and record why.

---

## **24 Content**

**Print Stylesheets**

Some readers will print your edition, and many will save it as a PDF. A page designed for a screen does not always survive the trip to paper. Tooltips disappear, links cannot be clicked, and a heading can be stranded at the bottom of a page with its text on the next.

CSS lets you write rules that apply only when printing, inside an `@media print` block. Add this to the end of your `reading.css`:

```css
@media print {
  .gap-info { display: inline; }
  h2 { break-after: avoid; }
  @page { margin: 2cm; }
}
```

The first rule is the payoff from section 15. On screen, the `gap-info` text stays hidden behind the tooltip; on paper, the same real text appears inside the brackets, so a printed gap reads *[… 2 word(s), damage]*. Nothing was added by CSS; the words were in the HTML all along, and the print rule merely shows them. That keeps faith with Tuesday's section 24.

The second rule asks the browser not to break a page directly after a heading. The `@page` rule sets the paper margins.

To test, open your generated reading page and choose Print in your browser. The preview shows exactly what the print rules do. Check every gap, every unclear reading and every italic expansion. If any editorial mark depends on colour, it will now be grey or invisible, and your print rules should give it another form.

**Vocabulary.** *`@media print`* — A CSS block whose rules apply only when a page is printed or saved as a PDF. *Print preview* — The browser's display of how a page will look on paper, before printing.

**Takeaway:** Put print-only rules inside `@media print`, reveal on paper the gap details that tooltips carry on screen, and check every editorial mark in the print preview.

---

## **25 Content**

**From Page to PDF**

The quickest PDF of your edition comes from the browser itself. Open a generated view, choose Print, and select Save as PDF as the destination. Your print stylesheet controls the result. For a short document with clean print rules, this is a respectable PDF.

XSLT can also produce formatting objects, an intermediate format that other software turns into PDF (Bausi et al., 2015). That route gives fine control over page layout, footnotes and running heads, and large print-oriented projects use it. It is also a substantial skill of its own, and you will not need it for this course.

The deeper point is that the PDF is one more view generated from the same source. Different views of the same encoded text can be generated on demand by the reader (Pierazzo, 2016). A reading view on screen, a diplomatic view on screen, and a printed reading view are three outputs of one TEI file and a handful of rules. None of them is the edition; the edition is the encoded file and the decisions that render it.

This matters for the Print-Ready Publication you will submit in December. Your PDF will be judged on whether it carries out documented decisions faithfully, not on whether it was made with expensive software. Today's stylesheets, print rules and `RENDERING.md` are the start of that submission.

**Vocabulary.** *XSL-FO* — Extensible Stylesheet Language Formatting Objects, an XML format describing printed pages, which software converts to PDF. *Output* — One generated form of an edition, such as a web page or a PDF.

**Takeaway:** The browser's Save as PDF with a good print stylesheet makes a sound PDF; it is one more view of the same source, and this week's work feeds directly into the Print-Ready Publication.

---

## **26 Content**

**Worked Example: The 1791 Decree by XSLT**

Ace's decree shows how the stylesheets handle a French text. Suppose one illustrative line of the TEI reads:

```xml
<lb n="4"/>qui <choice><orig>étoient</orig><reg>étaient</reg></choice> réunis
```

The reading stylesheet chooses `<reg>` and writes:

```html
qui <span class="reg">étaient</span> réunis
```

The diplomatic stylesheet chooses `<orig>` and writes a numbered line reading *qui étoient réunis*.

Three adjustments make the stylesheets right for Ace's file. First, change `<html lang="en">` in the page shell to `<html lang="fr">`, because the page is French. Second, keep `encoding="utf-8"` in `xsl:output` and `<meta charset="utf-8"/>` in the head. Open the result and check every accented letter: *é*, *è*, *à*, *ç*. If any appears as a pair of strange symbols, one of those two settings is missing. Third, if the decree's divisions are articles or clauses, check that `class="{@type}"` produced the class names your CSS expects.

Then do the line-by-line check from Tuesday on ten lines. Every regularized form should appear in the reading view and every original form in the diplomatic view, with nothing glued together and nothing missing.

**Vocabulary.** *`xsl:output`* — The XSLT element that sets the kind of output, such as HTML, and its character encoding. *Mojibake* — Garbled characters that appear when text is read with the wrong encoding.

**Takeaway:** For a French text, set `lang="fr"`, keep UTF-8 in both the output setting and the page head, and check every accented letter and every `<choice>` in both views.

---

## **27 Content**

**Worked Example: The 1752 Treaty in CETEIcean**

Andromeda's treaty shows the CETEIcean route. Take the illustrative lines from Tuesday, now with a damaged word:

```xml
<lb n="11"/>That the <choice><abbr>Gov<hi rend="sup">r</hi></abbr><expan>Gov<ex>erno</ex>r</expan></choice>
<lb n="12"/>and <choice><orig>Councill</orig><reg>Council</reg></choice> of the Pro-<lb n="13" break="no"/>vince
<lb n="14"/>shall <unclear>meet</unclear> <gap reason="damage" quantity="2" unit="word"/> yearly.
```

With `cetei-reading.css` and the gap behavior, the reading view runs the lines together as one sentence: That the Gov*erno*r and Council of the Pro-vince shall meet […] yearly. The word *meet* carries a dotted underline. With `cetei-diplomatic.css`, the same file shows four numbered lines: *Gov* with a raised *r*, *Councill* with its double *l*, and *Pro-* ending line 12.

Now look closely at what CETEIcean did not do. The gap shows brackets, but its reason and extent are only in the attributes, invisible on screen and on paper. And if the `<lb break="no"/>` in your file sits on a new line of the XML, the reading view shows *Pro- vince*, because CSS cannot remove whitespace the way the XSLT recipe in section 14 did. Each of these is a difference from your decision table, and each goes into `RENDERING.md`.

These lines are illustrative. Use the real lines from your own file, and choose at least one that contains a gap or an unclear reading.

**Vocabulary.** *Attribute-only information* — Data recorded in an element's attributes that no reader sees unless a rule displays it. *Fidelity gap* — A place where a rendering shows less than the source records.

**Takeaway:** CETEIcean renders the treaty lines in both views with Tuesday's rules, but gap details stay hidden in attributes and split-word whitespace survives; record both against your table.

---

## **28 Content**

**The Fidelity Audit: Tool Error or Undecided Decision?**

Every difference between a generated page and Tuesday's page has one of two causes, and sorting them is today's most important task.

A **tool error** is a place where your decision was clear but the rule failed to carry it out. The namespace prefix was missing; a template selected the wrong child; a gap had no template and vanished. The fix is in the stylesheet or the CSS.

An **undecided decision** is a place where the tool met something your table never addressed. Perhaps your file contains a `<hi rend="underline">` you never mentioned, or a `<note>` that appears on line 30, beyond the ten lines you rendered by hand. The rule had to do something, and whatever it did was not your choice. The fix is in `RENDERING.md` first: make the decision, then write the rule.

<table>
  <thead>
    <tr><th>What you see</th><th>Likely cause</th><th>Where to fix it</th></tr>
  </thead>
  <tbody>
    <tr><td>Both layers glued together</td><td>Tool error: missing prefix or template</td><td>Stylesheet</td></tr>
    <tr><td>A gap or line break missing</td><td>Tool error: no template or behavior for an empty element</td><td>Stylesheet or behavior</td></tr>
    <tr><td>Words from an element you never listed</td><td>Undecided decision</td><td><code>RENDERING.md</code>, then the rule</td></tr>
    <tr><td>Header text at the top of the page</td><td>Tool error: body not selected</td><td>Page shell</td></tr>
  </tbody>
</table>

Run a quick search to catch undecided elements. Open your TEI file in VS Code, list every element name inside `<body>`, and tick each one off against your table. Any element without a row is undecided, however the tool happened to display it.

**Vocabulary.** *Tool error* — A failure of a rule to carry out a clear, recorded decision. *Undecided decision* — A case the decision table never addressed, so that a tool's default chose instead of the editor.

**Takeaway:** Sort every difference into a tool error, fixed in the rule, or an undecided decision, fixed first in `RENDERING.md`; a tool's default is never an editorial decision.

---

## **29 Content**

**Hypothetical Scenario: The Vanishing Gap**

*This scenario is invented to illustrate the risk; it describes no real person or edition.*

An editor publishes an online reading text of a damaged eighteenth-century letter. The stylesheet was adapted from a colleague's project, which had no damaged documents and so no template for `<gap/>`. The page looks clean and complete.

A historian quotes a sentence from it in an article, arguing that the writer made a promise without conditions. A reviewer later checks the manuscript and finds a hole in the paper exactly where a condition might have stood. The TEI file recorded it correctly, with a `<gap reason="damage" quantity="3" unit="word"/>`. The rendering dropped it silently, because an empty element with no template produces nothing.

No one was careless with the evidence. The transcription was right, and the encoding was right. The failure was a missing rule, and it went unnoticed because nobody compared the rendered page against the source, element by element.

Ask yourself how this week's steps would have caught it. Tuesday's decision table would have listed `<gap/>` as an element that must show in both views. Today's audit would have found that the generated page had fewer brackets than the TEI had gaps. A simple count, gaps in the file against brackets on the page, takes a minute.

**Vocabulary.** *Silent failure* — An error that produces no warning and leaves output that looks correct. *Count check* — Comparing the number of occurrences of an element in the source with the number of marks in the rendering.

**Takeaway:** An empty element with no rule disappears without warning; counting each element in the TEI against its marks on the page catches the loss.

---

## **30 Content**

**Review and Step 2 Checklist**

Today you turned your decision table into rules and rendered your whole document twice, once by XSLT and once by CETEIcean. You also learned where each route fails silently, and you compared both against the page you made by hand.

Before you leave, confirm each item below:

<ol>
  <li><strong>XSLT stylesheets:</strong> Do <code>rendering/reading.xsl</code> and <code>rendering/diplomatic.xsl</code> use the <code>tei:</code> prefix, select only the <code>&lt;body&gt;</code>, and have a template for every element in your decision table?</li>
  <li><strong>Generated pages:</strong> Do <code>reading-auto.html</code> and <code>diplomatic-auto.html</code> show your whole document, with the correct <code>charset</code> and <code>lang</code>, and link to each other?</li>
  <li><strong>CETEIcean pages:</strong> Do both CETEIcean views load through a local server, with every structural element displayed as a block and every gap showing brackets?</li>
  <li><strong>Print rules:</strong> Does the print preview of your reading view show gap details as text and keep every editorial mark visible without colour?</li>
  <li><strong>Audit recorded:</strong> Does <code>RENDERING.md</code> list each difference from Tuesday's page as a tool error or an undecided decision, with what you did about it?</li>
  <li><strong>Count check:</strong> Do the numbers of gaps, unclear readings and <code>&lt;choice&gt;</code> elements in your TEI match the marks in each generated view?</li>
  <li><strong>Committed:</strong> Are <code>render.py</code>, the stylesheets, the CETEIcean pages and the updated <code>RENDERING.md</code> committed in clearly described commits?</li>
</ol>

On Friday you will ask an AI model to write a stylesheet for the same file, and audit its output against Tuesday's page and today's rules, element by element.

**Vocabulary.** *Step 2 milestone* — The completed rule-based rendering and audit, fixed as the second point of comparison for Friday.

**Takeaway:** Completing Step 2 gives you runnable rules that render your whole document in both views, and an audit that separates tool errors from decisions you had not yet made.

---

## References

Bausi, A., Borbone, P. G., Briquel-Chatonnet, F., Buzi, P., Gippert, J., Macé, C., Maniaci, M., Melissakis, Z., Parodi, L. E., & Witakowski, W. (Eds.). (2015). *Comparative oriental manuscript studies: An introduction*. COMSt.

Clausen, H., Brenner, S., Schreiner, M., & Vetter, W. (2026). Multimodal manuscript representation: Toward an open repository for manuscript research data. *The European Physical Journal Plus, 141*, 445. https://doi.org/10.1140/epjp/s13360-025-07133-y

Faghihi, Y., Holford, M., & Jones, H. (2022). Teaching the Text Encoding Initiative: Context, community and collaboration. *Journal of Open Humanities Data, 8*, 15. https://doi.org/10.5334/johd.72

Lazzerini, F., & Di Franco, M. (2026). Creating a digital critical edition of a classical text with XML/TEI. *Umanistica Digitale, 23*. https://doi.org/10.60923/issn.2532-8816/23486

Pierazzo, E. (2016). Modelling digital scholarly editing: From Plato to Heraclitus. In M. J. Driscoll & E. Pierazzo (Eds.), *Digital scholarly editing: Theories and practices* (pp. 41–58). Open Book Publishers. https://doi.org/10.11647/OBP.0095.03
