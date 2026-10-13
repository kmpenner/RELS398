# Lesson 7.3 — Rendering with AI: Auditing a Stylesheet You Did Not Write

*RELS 398 / ENGL 398 · Topic 7: Rendering (Publication I) · Meeting #19 (Fri Oct 23)*

***Step 3 of the three-step cycle: AI-assisted.** On Tuesday you rendered a few lines by hand, and on Wednesday you wrote rules that render the whole file. Today you ask an AI model to write those rules for you, and then you audit what it wrote, template by template and word by word, against Tuesday's page, Wednesday's output and your decision table.*

---

## **01 Content**

**Today's Question: Can You Trust a Stylesheet You Did Not Write?**

By now you have two working renderings of your document. Tuesday's page was slow to make, but you know exactly why every word on it looks the way it does. Wednesday's stylesheets were quicker to run, and you know why too, because you wrote every template yourself.

Today a third author joins the project. An AI model can write a complete XSLT stylesheet or a CETEIcean stylesheet in a few seconds. It will look professional. It will have comments, sensible names and neat indentation. It will probably run.

None of that tells you whether it carries out your decisions. A stylesheet can run without errors and still drop gaps, glue words together, show the wrong spelling layer, or quietly display elements you never decided about. You found some of these failures on Wednesday in your own rules. Today you look for them in rules someone else wrote, where you do not already know where the weak points are.

So the question for today is not whether the model can write a stylesheet. It can. The question is whether you can tell, quickly and reliably, when its stylesheet is wrong, and what to do about it.

By the end of today you will have an AI-written stylesheet, a record of every difference between its output and Wednesday's, a decision about each difference, and a final pair of stylesheets you can defend line by line.

**Vocabulary.** *AI-assisted rendering* — Using an AI model to write the rules that render a TEI file, followed by an audit of those rules and their output. *Audit* — A systematic check of work against an independent standard, with every difference recorded and resolved.

**Takeaway:** An AI model can write a stylesheet that looks professional and runs without errors; today's job is to find out whether it carries out your decisions, and to fix it where it does not.

---

## **02 Content**

**Ask for Rules, Not for a Page**

There are two ways to involve an AI model in rendering. You can paste your TEI into a chat and ask for a finished web page. Or you can ask the model to write a stylesheet, and then run that stylesheet yourself with Wednesday's `render.py`.

Always choose the second way. The reason goes back to Wednesday's lesson on determinism.

A model's answers are not deterministic. Ask it the same question twice and you may get two different answers. A team testing models on historical concert programmes ran each model ten times on every image for exactly this reason: the outputs vary from run to run (Eck & Page, 2026). If the model writes your page directly, every page it produces is a new, unchecked piece of work. You would have to audit every word, every time.

A stylesheet is different. Once the model has written it, the stylesheet itself is just rules. It will give the same output every time you run it, like Wednesday's. The uncertainty is all in the writing, and writing happens once. Audit the stylesheet once, carefully, and you can trust its output on every run that follows, including on next month's revised TEI file.

There is a second reason. A stylesheet is short and readable. Your reading stylesheet from Wednesday is about forty lines. You can read forty lines of rules in a few minutes. You cannot easily read an entire generated page against an entire TEI file and be sure you missed nothing.

**Vocabulary.** *Direct rendering* — Asking a model to produce the finished page itself from the TEI text. *Rule generation* — Asking a model to write a stylesheet that you then run and check yourself.

**Takeaway:** Ask the model to write a stylesheet, not a page; a checked stylesheet gives the same output on every run, while every directly generated page needs a fresh audit.

---

## **03 Content**

**What Goes Wrong When a Model Renders Text Directly**

It helps to see clearly why direct rendering is risky, because the temptation is real. It is faster, and the result often looks right.

When a model renders a page directly, it does not copy your text. It writes new text that it predicts should appear there. Most of the time the prediction matches your words. When it does not, the failures are the same ones you met in Week 6 under the name over-normalization: an old spelling is modernized, an odd word is corrected, an abbreviation is expanded in a way your TEI never recorded.

Rendering adds new risks. A model asked to show a gap may fill it with words that seem to fit. A model asked to keep line breaks may join two short lines it judges to be one sentence. A model may leave out your `<sic>` reading entirely, because a mistake looks like something a helpful assistant should fix.

A study of models encoding twentieth-century letters found that one model drifted away from the reference file it had been given and relied on its own information instead, which produced errors where the supplied material should have been followed (De Cristofaro & Zilio, 2025). Rendering a transcription is a task where the supplied material is everything. Any drift away from it is a loss of evidence.

A stylesheet cannot drift in that way. It can only select, wrap and rearrange text that is already in your file. It may select the wrong layer or drop an element, and those are serious errors, but it cannot invent a word that is not in your TEI.

**Vocabulary.** *Drift* — A model's tendency to move away from the material it was given toward what it predicts is likely. *Text-preserving* — Describing a process, such as XSLT, that can rearrange or omit source text but cannot invent new words.

**Takeaway:** A model rendering text directly can modernize, correct or fill in your words, while a stylesheet can only select and wrap text already in your file, so its errors are easier to find.

---

## **04 Content**

**Your Three Points of Comparison**

Today's audit uses three standards, and each catches different problems.

<table>
  <thead>
    <tr><th>Standard</th><th>Made</th><th>What it shows</th><th>What it catches</th></tr>
  </thead>
  <tbody>
    <tr><td><code>RENDERING.md</code></td><td>Tuesday, updated Wednesday</td><td>What you decided each element should look like</td><td>Rules that ignore or contradict a decision</td></tr>
    <tr><td><code>edition.html</code></td><td>Tuesday, by hand</td><td>A few lines rendered exactly as you intended</td><td>Display details: italics, brackets, line numbers</td></tr>
    <tr><td><code>reading-auto.html</code> and <code>diplomatic-auto.html</code></td><td>Wednesday, by your own rules</td><td>The whole document, rendered by checked rules</td><td>Lost or changed words anywhere in the file</td></tr>
  </tbody>
</table>

The decision table is the authority. If the AI stylesheet and Wednesday's stylesheet disagree, the question is never which tool is better. The question is which one carries out the decision in `RENDERING.md`, and whether that decision was clear enough to carry out.

Wednesday's output is the most useful standard for checking words, because it covers the whole document and you have already checked it. If the AI output and Wednesday's output contain different words, at least one of them is wrong, and you can find out which in a minute.

Tuesday's page is the best standard for how things look. Check the AI output against it for the small display decisions: where the italics fall, what a gap looks like, how a line number sits.

**Vocabulary.** *Point of comparison* — An independent, already checked version against which new output is measured. *Authority* — The source that settles a disagreement; for rendering, your recorded decision table.

**Takeaway:** Check the AI stylesheet against all three standards: the decision table for what should happen, Wednesday's output for every word, and Tuesday's page for how each mark looks.

---

## **05 Content**

**Writing the Prompt: What the Model Must Know**

A model writes a better stylesheet when it knows what you know. On Wednesday you learned several things the hard way. Put all of them in the prompt, so the model does not have to guess.

The model needs five pieces of information.

<ol>
  <li><strong>Your decisions.</strong> Paste the whole table from <code>RENDERING.md</code>. This is the specification the stylesheet must carry out.</li>
  <li><strong>A sample of your TEI.</strong> Paste the <code>&lt;teiHeader&gt;</code> and twenty or thirty lines of the body, chosen to include every element in your table. The model needs to see how your file is actually nested.</li>
  <li><strong>The technical setting.</strong> The stylesheet will run in Python's <code>lxml</code>, which supports XSLT 1.0 only. It must declare the TEI namespace with a <code>tei:</code> prefix and use it in every match.</li>
  <li><strong>The class names.</strong> List the class names Tuesday's CSS already uses, such as <code>reg</code>, <code>expan</code>, <code>ex</code>, <code>unclear</code>, <code>gap</code> and <code>lb</code>, so the output works with your existing CSS files.</li>
  <li><strong>The page shell.</strong> Say which CSS file to link, which language code the page needs, and that the page must declare UTF-8.</li>
</ol>

The sample matters more than you might expect. If your file uses `<hi rend="underline">` only once, on line 80, and your sample stops at line 30, the model will not know that element exists. Choose your sample lines by the elements they contain, not by where they fall in the file.

Keep the sample short enough to read. You are asking for rules, so the model does not need your whole document. It needs to see each kind of element at least once.

**Vocabulary.** *Specification* — A precise description of what a program must do, against which the program can be checked. *Representative sample* — A selection of lines chosen so that every element in the file appears at least once.

**Takeaway:** Give the model your whole decision table, a sample containing every element you use, the XSLT 1.0 and namespace requirements, your existing class names, and the page shell settings.

---

## **06 Content**

**Writing the Prompt: What the Model Must Not Do**

In Week 6 you learned that negative constraints matter as much as instructions. The same is true for stylesheets. Each item below is a failure you met on Wednesday or will meet today, so name each one in the prompt.

<ol>
  <li><strong>Do not change, clean up or normalize any text.</strong> In particular, do not apply <code>normalize-space()</code> to every text node.</li>
  <li><strong>Do not choose a layer by position.</strong> Select the layer you want by name, such as <code>tei:reg</code>, never by order, such as the first child.</li>
  <li><strong>Do not let any element vanish.</strong> Every element in the decision table must have its own template, and every <code>&lt;gap/&gt;</code> must produce visible brackets as real text.</li>
  <li><strong>Do not write a catch-all template</strong> that matches every element, such as <code>match="*"</code>.</li>
  <li><strong>Do not put meaningful text in CSS.</strong> Brackets, line numbers and editorial marks must be in the HTML.</li>
  <li><strong>Do not use XSLT 2.0 or 3.0 features</strong>, such as <code>xpath-default-namespace</code> or functions like <code>string-join()</code> and <code>replace()</code>.</li>
  <li><strong>Do not process the header</strong> into the page, except to copy the title.</li>
</ol>

A model may still break one of these rules. The list is not a guarantee. Its value is that it makes the model's choices visible: if the stylesheet you get back contains `normalize-space()` on every text node, you know at once that the model ignored an explicit instruction, and you know where to look.

**Vocabulary.** *Negative constraint* — An explicit instruction about what a model must not do. *Catch-all template* — A template that matches every element without a template of its own, hiding the elements no one decided about.

**Takeaway:** Name every known failure in the prompt as a rule not to break; the model may still break one, but the list tells you exactly what to look for.

---

## **07 Content**

**A Complete Prompt**

Here is a prompt for the reading view, assembled from the last two sections. Adapt the details to your own file, and write a second prompt for the diplomatic view by changing the layer and the line-break rule.

```text
Write an XSLT 1.0 stylesheet that turns a TEI P5 file into the
reading view of a digital edition. It will be run by Python lxml,
which supports XSLT 1.0 only.

Requirements:
1. Declare xmlns:tei for the TEI namespace and use the tei: prefix
   in every match and select. Exclude the prefix from the output.
2. Output HTML with encoding utf-8, html lang=en, a meta charset
   element, the TEI title in the head, and a link to reading.css.
3. Process only tei:body into the page.
4. Carry out every row of the decision table below exactly.
5. For each choice, select tei:reg, tei:expan and tei:corr by name.
6. Use these class names: reg, expan, corr, ex, unclear, gap.
7. Each lb becomes one space; an lb with break=no becomes nothing.
8. Each gap becomes visible brackets, with its reason and extent
   in a title attribute and in a span with class gap-info.

Do not:
- change, clean up or normalize any text
- choose a child of choice by position
- write a template matching every element
- put brackets or other meaningful text in CSS
- use XSLT 2.0 or 3.0 features

Decision table:
[paste the table from RENDERING.md]

Sample of the TEI file:
[paste the header and the sample lines]
```

The prompt is long, and it should be. Every line in it is a decision you made this week, written so that a reader with no context can follow it. If you cannot write a line of the prompt, that is a sign that a decision is still missing from `RENDERING.md`.

**Vocabulary.** *Prompt* — The full set of instructions and material given to a model for one task. *Self-contained instruction* — An instruction that can be followed without knowledge of the conversation or the project behind it.

**Takeaway:** A good stylesheet prompt restates every decision and requirement from this week in plain terms; a line you cannot write points to a decision still missing from `RENDERING.md`.

---

## **08 Content**

**Running the Model and Saving Its Answer**

Use the same setup as in Week 6: open your repository in VS Code and use the AI panel there. Then follow these steps.

<ol>
  <li><strong>Save the prompt first.</strong> Create <code>rendering/prompts/reading-prompt.md</code> and paste your complete prompt into it before you send it. A prompt you did not save cannot be repeated or reported.</li>
  <li><strong>Send the prompt.</strong> Note the name of the model and today's date.</li>
  <li><strong>Save the answer under a new name.</strong> Copy only the stylesheet from the reply into <code>rendering/ai-reading.xsl</code>. Never let it overwrite your own <code>reading.xsl</code>, which is now one of your standards.</li>
  <li><strong>Commit before you change anything.</strong> Commit the prompt and the untouched stylesheet together, with a message such as <em>Add AI-written reading stylesheet, unedited</em>. Your audit will change the file, and this commit keeps a record of what the model actually wrote.</li>
  <li><strong>Repeat for the diplomatic view.</strong> Save <code>diplomatic-prompt.md</code> and <code>ai-diplomatic.xsl</code> the same way.</li>
</ol>

If the reply includes explanations, read them, but do not paste them into the stylesheet. A model's description of what its stylesheet does is not evidence of what it does. Only running it and reading the rules can tell you that.

If you send the same prompt again later, you may receive a different stylesheet. That is expected, and it is why the commit in step 4 matters: your audit applies to one particular stylesheet, the one in that commit.

**Vocabulary.** *Unedited baseline* — The model's output saved and committed exactly as received, before any correction. *Provenance* — The recorded history of where a file came from and how it was changed.

**Takeaway:** Save the prompt, save the stylesheet under a new name, and commit both unedited before you change anything, so the record shows exactly what the model wrote.

---

## **09 Content**

**First Check: Does It Run?**

Run the AI stylesheet exactly as you ran your own on Wednesday:

```bash
python3 rendering/render.py transcription_normalized.xml rendering/ai-reading.xsl rendering/reading-ai.html
```

There are three possible results, and each tells you something different.

**It stops with an error.** Read the last line. One common cause is an XSLT 2.0 function, which `lxml` does not know. A stylesheet that calls `string-join()` or `replace()` stops with the message *XPath evaluation returned no result*, which does not name the function. Search the stylesheet for any function you did not use on Wednesday.

**It runs, but the page is empty or nearly empty.** This is the namespace pitfall again, in a new form. A model may write `version="2.0"` and add `xpath-default-namespace` at the top, so that its matches can leave out the `tei:` prefix. That works in XSLT 2.0. In `lxml` the setting is simply ignored, with no warning, so no template matches your TEI and the body never appears. If the page is empty, look at the first lines of the stylesheet.

**It runs and the page looks full.** This is the most common result and the least informative. A full page proves only that the stylesheet runs. Every check from here on is about whether it is right.

Record the result in a new section of `RENDERING.md` headed *AI stylesheet audit*. If you had to fix an error to make it run, record the error and the fix.

**Vocabulary.** *XSLT 1.0* — The version of XSLT that <code>lxml</code> supports; later versions add features it does not recognize. *`xpath-default-namespace`* — An XSLT 2.0 setting that lets matches omit a namespace prefix, silently ignored by XSLT 1.0 processors.

**Takeaway:** An error usually points to an XSLT 2.0 feature, and an empty page to a missing <code>tei:</code> prefix; a full page proves only that the stylesheet runs, not that it is right.

---

## **10 Content**

**Second Check: Read It Template by Template**

Before you compare any output, read the stylesheet itself. This is the step people skip, and it is the one that finds the most.

Make a two-column inventory in `RENDERING.md`. In the first column, list every row of your decision table. In the second, write the name of the template in the AI stylesheet that carries out that row, or write *none*.

<table>
  <thead>
    <tr><th>Decision table row</th><th>Template in <code>ai-reading.xsl</code></th><th>Carries out the decision?</th></tr>
  </thead>
  <tbody>
    <tr><td><code>&lt;choice&gt;</code>: show <code>reg</code>, <code>expan</code>, <code>corr</code></td><td><code>tei:choice</code></td><td>Check what it selects</td></tr>
    <tr><td><code>&lt;ex&gt;</code>: italics</td><td><code>tei:ex</code></td><td>Check the class or element</td></tr>
    <tr><td><code>&lt;gap/&gt;</code>: brackets with reason</td><td><code>tei:gap</code></td><td>Check that it writes text</td></tr>
    <tr><td><code>&lt;lb/&gt;</code>: a space; <code>break="no"</code>: nothing</td><td><code>tei:lb</code></td><td>Check both cases</td></tr>
  </tbody>
</table>

Then go the other way. List every template in the stylesheet and find the row it belongs to. A template with no row is either something the model added on its own, such as a rule for whitespace, or a sign that your table is missing a decision. Both need a closer look.

For each template, ask one question: given an element of this kind from my file, what exactly will this rule write? Answer it on paper, before you run anything. Then check your answer against the output. Where you were wrong, you have learned something about the stylesheet.

**Vocabulary.** *Template inventory* — A list pairing each decision with the template that carries it out, and each template with its decision. *Orphan template* — A template that corresponds to no recorded decision.

**Takeaway:** Pair every decision with a template and every template with a decision; a decision with no template, or a template with no decision, is where problems hide.

---

## **11 Content**

**A Sample AI Stylesheet**

To practise the audit, here is a short stylesheet of the kind a model might return for the treaty sample you used on Wednesday. It is illustrative: it was written for this lesson to collect several common problems in one place, and it does not come from any particular model. Read it before you read the next sections, and try to find the problems yourself.

```xml
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:tei="http://www.tei-c.org/ns/1.0"
  exclude-result-prefixes="tei">
  <xsl:output method="html" encoding="utf-8"/>

  <xsl:template match="/">
    <html>
      <head>
        <title><xsl:value-of select="//tei:titleStmt/tei:title"/></title>
        <link rel="stylesheet" href="reading.css"/>
      </head>
      <body><xsl:apply-templates select="//tei:body"/></body>
    </html>
  </xsl:template>

  <xsl:template match="tei:div"><section><xsl:apply-templates/></section></xsl:template>
  <xsl:template match="tei:head"><h2><xsl:apply-templates/></h2></xsl:template>
  <xsl:template match="tei:p"><p><xsl:apply-templates/></p></xsl:template>

  <!-- Show the edited form of each choice -->
  <xsl:template match="tei:choice"><xsl:apply-templates select="*[1]"/></xsl:template>

  <xsl:template match="tei:ex"><em><xsl:apply-templates/></em></xsl:template>
  <xsl:template match="tei:unclear"><span class="unclear"><xsl:apply-templates/></span></xsl:template>
  <xsl:template match="tei:gap"><span class="gap"/></xsl:template>
  <xsl:template match="tei:lb"/>

  <!-- Clean up whitespace -->
  <xsl:template match="text()"><xsl:value-of select="normalize-space(.)"/></xsl:template>

  <!-- Anything else: keep the text -->
  <xsl:template match="*"><xsl:apply-templates/></xsl:template>
</xsl:stylesheet>
```

It uses the `tei:` prefix correctly, selects only the body, and copies the title. Its comments are reasonable. Run on Wednesday's treaty sample, it produces this paragraph:

```html
<p>That theGovrandCouncillof the Pro-vinceshall<span class="unclear">meet</span><span class="gap"></span>yearly.</p>
```

Wednesday's stylesheet, run on the same file, produced *That the Governor and Council of the Pro-vince shall meet [… 2 word(s), damage] yearly.* The next six sections take the differences one at a time.

**Vocabulary.** *Plausible code* — Code that looks well organized and correct on reading but fails on real input. *Illustrative stylesheet* — A stylesheet written for teaching, to show typical problems; not the output of a particular model.

**Takeaway:** A stylesheet can use the namespace correctly, select only the body and carry tidy comments while still producing a page that changes, glues together and loses your text.

---

## **12 Content**

**The First Child Is Not Always the Right One**

Look at the `<choice>` template. Its comment says it shows the edited form. Its rule says `select="*[1]"`, which means the first child element, whatever it is.

In the treaty sample, every `<choice>` puts the original first: `<abbr>` before `<expan>`, `<orig>` before `<reg>`. So the rule selects the original every time. The reading view shows *Govr* and *Councill*, the diplomatic forms, in the view that promised readers regularized text.

The comment and the rule disagree, and only the rule runs. This is worth remembering as a general lesson about AI-written code: the comments describe what the model intended, or what such code usually does. They are not a description of what this code does.

The error is also fragile in a way that makes it hard to find. The TEI Guidelines do not fix the order of children inside a `<choice>`. If one file puts `<reg>` first and another puts `<orig>` first, the same stylesheet shows the right layer in one and the wrong layer in the other. If your own file happens to be inconsistent, the reading view will mix both layers, line by line, with no pattern a reader could notice.

The fix is the one you wrote on Wednesday: select by name.

```xml
<xsl:template match="tei:choice">
  <xsl:apply-templates select="tei:reg|tei:expan|tei:corr"/>
</xsl:template>
```

This rule gives the same answer whatever order the children are in. That is what makes it a rule about your decision rather than a rule about your file's accidents.

**Vocabulary.** *Positional selection* — Choosing an element by its place among its siblings, such as first or last, rather than by its name. *Order-dependent* — Describing a rule whose result changes when the order of elements changes, though their meaning does not.

**Takeaway:** A rule that picks the first child of <code>&lt;choice&gt;</code> depends on the order of your markup, not on your decision; select each layer by name, whatever its comment says.

---

## **13 Content**

**Cleaning Up Whitespace Glues Words Together**

The most damaging line in the sample is the one labelled *Clean up whitespace*. It applies `normalize-space()` to every piece of text in the file.

On Wednesday you used `normalize-space()` in one narrow place: on text immediately before a `<lb break="no"/>`, to rejoin a split word. Here the same function is applied everywhere. It removes the spaces at the start and end of every text node, and in TEI, the space between two words very often sits at the edge of a text node.

Look at the treaty line `That the <choice>...</choice>`. The space after *the* is the last character of the text node *That the*, just before the `<choice>` begins. Remove it, and the next word attaches directly: *theGovr*. The same happens after the `<choice>`, before *and*, and on both sides of `<unclear>` and `<gap/>`. Every word that sits next to an element loses the space that separated it.

The result is not a small typographic flaw. A search for *Governor* will fail. A screen reader will read nonsense words. A scholar copying a sentence will copy a string that never appeared in the document.

Why would a model write this rule? Because whitespace cleanup is very common in stylesheets for other kinds of XML, where data such as names and numbers sit alone inside elements. Text with mixed content, where words and elements alternate inside a paragraph, is different. The rule is reasonable somewhere else, and harmful here.

The fix is to delete the template. If split words need rejoining, use Wednesday's narrow rule, which touches only the text right before a `break="no"` line break.

**Vocabulary.** *Mixed content* — An element containing both text and child elements, as a TEI paragraph usually does. *Text node* — A continuous run of text between two pieces of markup.

**Takeaway:** Applying <code>normalize-space()</code> to all text deletes the spaces beside every element and glues words together; in mixed content, trim whitespace only where a specific rule requires it.

---

## **14 Content**

**The Silent Gap**

The gap template in the sample is short:

```xml
<xsl:template match="tei:gap"><span class="gap"/></xsl:template>
```

It does write something: an empty span with the class `gap`. On screen, an empty span shows nothing. The reader sees *meet yearly* and has no reason to suspect that two words were lost to damage between them.

This failure is worse than the one you met on Wednesday. There, a missing template meant the gap vanished entirely, and a search of the HTML for `gap` would find nothing. Here the gap has a template, and the HTML contains an element with the right class name. A quick check that looks only for the class will report that everything is in order.

Notice also what the span does not contain: no reason and no extent. Your TEI says the gap is two words, caused by damage. The AI stylesheet discards that information as well as the visible mark.

Could CSS rescue it? A rule such as `.gap::before { content: "[…]"; }` would make brackets appear on screen. But on Tuesday you decided that meaningful text belongs in the HTML. Text added by CSS is not part of the page's text: if a reader selects the sentence and copies it, the brackets do not come with it, and the browser's search cannot find them. The scholar who quotes your line would quote it without the gap.

So the fix is Wednesday's template, which writes the brackets as real text and carries the reason and extent with them.

**Vocabulary.** *Empty element* — An element with no content, which displays nothing unless a rule supplies something. *Generated content* — Text added by CSS rules such as <code>::before</code>, which appears on screen but is not part of the page's text.

**Takeaway:** A gap template that writes an empty span, or brackets added only by CSS, hides the loss from readers and from copied text; brackets and gap details must be real text in the HTML.

---

## **15 Content**

**Line Breaks That Swallow Spaces**

The sample turns every `<lb/>` into nothing:

```xml
<xsl:template match="tei:lb"/>
```

That looks harmless in a reading view, which is supposed to let lines flow. But look at how most transcriptions are typed. Each `<lb/>` starts a new line in your file, and the last word of one line and the first word of the next are separated only by the new line in the XML.

On Wednesday, your reading stylesheet turned each `<lb/>` into a protected space for exactly this reason, and kept the whitespace in your file as well. In the sample, the whitespace rule from Section 13 has already removed the new line, and the `<lb/>` rule adds nothing back. So the end of one line joins the start of the next: *Pro-vinceshall*.

Two rules, each defensible on its own, combine to cause the error. That is common in stylesheets, and it is why the template inventory is not enough by itself. You must also check what the rules do together on real lines.

Also look at what the sample does not have: any rule for `<lb break="no"/>`. Because every line break produces nothing, the split word happens to come out right. If you fix the line-break rule to write a space, without adding Wednesday's separate rule for `break="no"`, you will create a new error, *Pro- vince*, while fixing the old one. Fix both rules together, and test them on a line with a split word.

**Vocabulary.** *Interacting rules* — Two or more templates whose combined effect differs from what either does alone. *Regression* — A new error created while fixing an old one.

**Takeaway:** A line-break rule that writes nothing joins the last word of each line to the first word of the next; write a space for ordinary breaks and nothing for <code>break="no"</code>, and test both together.

---

## **16 Content**

**The Catch-All Template**

The last template in the sample matches every element:

```xml
<!-- Anything else: keep the text -->
<xsl:template match="*"><xsl:apply-templates/></xsl:template>
```

XSLT always prefers a more specific match, so this template only catches elements that have no template of their own. For those, it does exactly what the built-in rules from Wednesday already do: it drops the element and lets its text fall through.

So why does it matter? Because it changes what the stylesheet looks like to a reader. Without it, an element with no template is an obvious omission. With it, the omission looks like a policy, complete with a comment. Anyone reading the stylesheet later will think every remaining element was considered and that keeping its text was the decision.

In the treaty sample, this rule catches `<abbr>`'s child `<hi rend="sup">` whenever the abbreviation is shown, and turns the raised letter into ordinary text. In a larger file, it will catch every `<note>`, every `<hi>` with a value you did not list, every `<persName>` you add in Week 9. Each of these is an undecided decision in the sense of Wednesday's audit, and the catch-all makes all of them invisible.

Delete it. An element with no template should look like what it is: a question you have not yet answered. The next sections show how to make those questions visible on the page.

**Vocabulary.** *Default priority* — The rule by which XSLT prefers a specific match, such as <code>tei:p</code>, over a general one, such as <code>*</code>. *Disguised omission* — A missing decision made to look deliberate by code that handles it generically.

**Takeaway:** A catch-all template behaves like the built-in rules but makes every undecided element look deliberate; remove it, so that elements without a rule stay visible as open questions.

---

## **17 Content**

**What Is Missing from the Page Shell**

Some problems are absences, and a template inventory finds them only if you compare the stylesheet with your requirements line by line.

Compare the sample's page shell with Wednesday's. Two things are missing.

First, there is no `lang` attribute on `<html>`. Without it, a browser and a screen reader must guess the page's language. For an English treaty the guess will often be right. For a French decree read on an English-language computer, a screen reader may pronounce every word as English, and the browser may hyphenate French words by English rules.

Second, there is no `<meta charset="utf-8"/>` in the head. The `xsl:output` element does say `encoding="utf-8"`, so the file itself is written correctly. But when the page is opened from a folder or served without encoding information, the browser has nothing in the page to tell it how to read the bytes. Wednesday's lesson asked you to keep both, and the reason is that either can be lost in a different way.

Also notice that the sample uses `<em>` for supplied letters instead of Tuesday's class `ex`. The italics will look the same, so a visual check will pass. But your `reading.css` and your print stylesheet both expect `.ex`. Any rule you wrote for that class, such as a different colour for supplied letters, will silently stop applying.

None of these produce an error. You find them by reading the stylesheet against the requirements in your prompt, one requirement at a time.

**Vocabulary.** *Page shell* — The outer HTML of a page, including the language, character encoding, title and stylesheet links. *Class contract* — The agreement between HTML and CSS that a given class name marks a given kind of content.

**Takeaway:** Check the AI page shell for <code>lang</code> and <code>meta charset</code>, and check that it uses your existing class names; their absence causes no errors, only quiet failures.

---

## **18 Content**

**Third Check: Compare the Output Word by Word**

Reading the stylesheet finds problems in the rules. Comparing the output finds problems you missed in the rules. Because Wednesday's output is already checked, the fastest way to compare is with a short script.

Save this as `rendering/compare.py`:

```python
import sys
import difflib
from lxml import html

def words(path):
    body = html.parse(path).find("body")
    return body.text_content().split()

old, new = words(sys.argv[1]), words(sys.argv[2])
matcher = difflib.SequenceMatcher(None, old, new, autojunk=False)
for op, i1, i2, j1, j2 in matcher.get_opcodes():
    if op != "equal":
        print(op.upper(), "|", " ".join(old[i1:i2]), "|", " ".join(new[j1:j2]))
print("Words:", len(old), "and", len(new))
```

The script reads the visible text of each page, splits it into words, and prints every place where the two lists differ. Run it with Wednesday's page first and the AI page second:

```bash
python3 rendering/compare.py rendering/reading-auto.html rendering/reading-ai.html
```

On the treaty sample, the last line reads *Words: 17 and 5*. Wednesday's page has seventeen words; the AI page has five, because the missing spaces have glued the rest into long strings. The lines above it show each place where the texts part company.

On your own file, a clean result is a single line with two equal numbers. Anything else needs an explanation. Each difference is either an error in the AI stylesheet, an error in yours that Wednesday's checks missed, or a difference in display that does not affect the words. Decide which, and record it.

**Vocabulary.** *Word-level comparison* — Comparing two texts as sequences of words, so that each insertion, deletion or change can be located. *`difflib`* — The Python library that finds the differences between two sequences.

**Takeaway:** Compare the visible words of the AI page with Wednesday's checked page; equal word counts and no differences mean no words were lost, changed or glued together.

---

## **19 Content**

**Fourth Check: Count What the Reader Sees**

A word comparison catches lost and changed words. It does not catch a wrong layer if both stylesheets made the same mistake, and it does not tell you whether every editorial mark survived. For that, count.

Save this as `rendering/count.py`:

```python
import sys
from lxml import etree, html

TEI = {"tei": "http://www.tei-c.org/ns/1.0"}
source = etree.parse(sys.argv[1])
page = html.parse(sys.argv[2])

print("In the TEI body:")
for name in ["choice", "unclear", "gap", "lb"]:
    found = source.xpath("//tei:body//tei:" + name, namespaces=TEI)
    print("  ", name, len(found))

print("In the page:")
for name in ["reg", "expan", "corr", "orig", "abbr", "sic", "unclear", "gap", "lb"]:
    found = [e for e in page.iter("*") if name in e.get("class", "").split()]
    print("  ", name, len(found))
print("   brackets", page.find("body").text_content().count("[…"))
```

Run it with your TEI file and a page. For a reading view, the number of `<choice>` elements should equal the total of `reg`, `expan` and `corr` on the page, with no `orig`, `abbr` or `sic`. For a diplomatic view, it should be the other way round, and the number of `lb` spans should equal the number of `<lb/>` elements.

The last line is the one that matters most. Run on the AI treaty page, the script reports one `gap` class and zero brackets. The class is there; the mark the reader needs is not. This is why you count what the reader sees, not only what the HTML contains.

**Vocabulary.** *Count check* — Comparing the number of occurrences of each element in the source with the number of corresponding marks in the output. *Visible mark* — The text a reader actually sees for an editorial element, such as the brackets of a gap.

**Takeaway:** Count each element in the TEI and each class and bracket on the page; a matching class with a missing bracket shows a mark that exists in the code but not for the reader.

---

## **20 Content**

**Making Undecided Elements Visible**

The catch-all template hid undecided elements. You can turn the same idea around and make them stand out instead. Add this template, for the audit only, at the end of a copy of the AI stylesheet or of your own:

```xml
<xsl:template match="tei:body//tei:*" priority="-1">
  <span class="undecided" title="{local-name()}"><xsl:apply-templates/></span>
</xsl:template>
```

It matches any element inside the body that has no template of its own. The `priority="-1"` makes sure every one of your real templates still wins. Instead of letting the element's text fall through silently, it wraps the text in a span whose tooltip names the element.

Then add one line to the CSS you link while auditing:

```css
.undecided { outline: 2px solid red; }
```

Run the stylesheet and open the page. Every red box is text from an element that no rule handles. Hover over it to see which element it is. Tested with Wednesday's reading stylesheet on a treaty line with a `<note>` and an underlined word added, the page shows both, each in a red box, with tooltips reading *note* and *hi*.

Each red box goes into the audit as an undecided decision. Decide it in `RENDERING.md`, write the rule, and run again until there are no red boxes. Then remove the audit template, or keep it in a separate `audit.xsl`, so it never reaches your published pages.

**Vocabulary.** *Audit template* — A temporary rule that makes problems visible during checking and is removed before publication. *Template priority* — A number that decides which template applies when more than one matches; higher wins.

**Takeaway:** A low-priority audit template that outlines every unhandled element in red turns silent omissions into visible questions; resolve each one in <code>RENDERING.md</code>, then remove the template.

---

## **21 Content**

**Auditing AI-Written CSS for CETEIcean**

If you chose CETEIcean on Wednesday, ask the model for the CSS and the behaviors instead of a stylesheet, using the same prompt structure. Give it your decision table, a sample of the TEI, the names of the `tei-` elements, and the list of things it must not do. Then audit the result with the same care.

Four problems are especially likely in AI-written CETEIcean CSS.

<ol>
  <li><strong>Brackets in CSS.</strong> A rule such as <code>tei-gap::before { content: "[…]"; }</code> puts the brackets on screen but not in the page's text. Tested in a browser, a copied sentence came out as <em>shall meet  yearly.</em>, with the brackets gone, and the browser's search could not find them. Wednesday's behavior puts real brackets in the page; use it.</li>
  <li><strong>Layers by position.</strong> A rule such as <code>tei-choice &gt; :first-child</code> has the same flaw as <code>*[1]</code> in XSLT. Hide and show layers by element name: <code>tei-orig</code>, <code>tei-reg</code>.</li>
  <li><strong>Line numbers on their own line.</strong> A rule that gives <code>tei-lb</code> <code>display: block</code> and puts the number in <code>::before</code> places each number on a line by itself, above its text. Tuesday's lesson explains the fix.</li>
  <li><strong>Hidden elements by accident.</strong> A model may hide <code>tei-teiheader</code> and, in the same rule, other elements whose names it guessed, such as <code>tei-note</code>. Check every <code>display: none</code> against your table.</li>
</ol>

The line numbers raise an awkward point. On Tuesday you also chose to put line numbers in CSS, with `attr(data-n)`. That was a deliberate decision, recorded in `RENDERING.md`, for a view where numbers are a reading aid rather than part of the text. The rule is not that CSS may never add anything. The rule is that every such choice must be one you made and recorded, not one you inherited.

**Vocabulary.** *Behavior* — A CETEIcean function that changes an element's content when the page loads, such as adding real brackets to <code>tei-gap</code>. *Inherited decision* — A display choice that entered your edition through someone else's code without being examined.

**Takeaway:** Audit AI-written CETEIcean CSS for brackets made in CSS, layers chosen by position, misplaced line numbers and accidental <code>display: none</code>; every display choice must be one you recorded.

---

## **22 Content**

**Sorting What You Find: Three Kinds of Difference**

On Wednesday you sorted differences into two kinds: tool errors and undecided decisions. Today there is a third kind, and it is the one that makes AI assistance worth the trouble.

<table>
  <thead>
    <tr><th>Kind</th><th>What it means</th><th>Example</th><th>What to do</th></tr>
  </thead>
  <tbody>
    <tr><td>AI error</td><td>Your decision was clear and the AI rule fails it</td><td><code>*[1]</code> selects the original in the reading view</td><td>Fix the AI rule, or use yours</td></tr>
    <tr><td>Undecided decision</td><td>Your table never covered the case</td><td>A <code>&lt;note&gt;</code> outlined in red</td><td>Decide in <code>RENDERING.md</code>, then write the rule</td></tr>
    <tr><td>Improvement</td><td>The AI rule does something better than yours</td><td>A rule you lacked for <code>&lt;hi rend="underline"&gt;</code></td><td>Adopt it deliberately, and record why</td></tr>
  </tbody>
</table>

Be strict about the third kind. An improvement is not something that merely looks nicer. It is a rule that carries out one of your decisions more faithfully than your own rule did, or that handles a case you had genuinely overlooked in a way you would have chosen. If the AI rule makes a choice you would not have made, it is not an improvement, however polished it looks.

Every difference also has a fourth possibility: the error is in your own stylesheet, and the AI rule is right. Do not assume Wednesday's output is perfect because you wrote it. If the AI output keeps a word that yours drops, check the TEI. Wednesday's stylesheet was checked, but it was checked by you, on a schedule.

Record each difference in the audit section of `RENDERING.md` with its kind and what you did.

**Vocabulary.** *Improvement* — A difference in which the AI rule carries out a recorded decision, or covers an overlooked case, better than your own rule. *Audit log* — The record of every difference found, how it was classified, and how it was resolved.

**Takeaway:** Sort each difference into an AI error, an undecided decision, or a genuine improvement, and remember that some differences will reveal errors in your own stylesheet.

---

## **23 Content**

**When the Model Is Right and You Were Wrong**

It will happen. A model will sometimes write a rule that handles a case you missed, or handle a familiar case more cleanly than you did. That is not a failure of your work. It is one of the reasons to include an AI step at all.

Suppose your file contains `<hi rend="underline">` on one line, which you overlooked on Tuesday, and the AI stylesheet includes a rule that writes it as `<span class="underline">` with CSS to underline it. Your stylesheet let the word fall through as plain text. The AI rule is closer to the evidence: the writer underlined that word, and now the reader can see it.

Adopting the rule is reasonable. But adopt it in the right order.

<ol>
  <li><strong>Decide first.</strong> Add a row for <code>&lt;hi rend="underline"&gt;</code> to <code>RENDERING.md</code>, stating how it appears in each view and why.</li>
  <li><strong>Then take the rule.</strong> Copy the template into your own stylesheet, and read it as carefully as you would any template you wrote.</li>
  <li><strong>Then test it.</strong> Run both views, compare, and count again.</li>
  <li><strong>Then credit it.</strong> Note in the audit log that the rule came from the AI stylesheet.</li>
</ol>

The order matters because the decision is yours even when the idea is not. If the rule enters your stylesheet without a row in the table, you have accepted an inherited decision. If the row comes first, you have made a decision the model happened to suggest.

This is the same principle that ran through Week 6. The model's output is a suggestion for an editor to accept or reject. It is never the editor.

**Vocabulary.** *Adoption* — Taking an AI-written rule into your own stylesheet after deciding, in writing, that it carries out your policy. *Editorial responsibility* — The principle that every choice in an edition belongs to a named editor who can explain it.

**Takeaway:** When the model handles a case better than you did, record the decision in <code>RENDERING.md</code> first, then adopt, test and credit the rule; the idea may be the model's, but the decision is yours.

---

## **24 Content**

**Fix, Adopt, or Discard**

When the audit is complete, you have three options for the AI stylesheet as a whole.

**Fix it.** If the AI stylesheet is well organized and most of its rules are right, correct the errors you found, rerun every check, and make it your stylesheet. This is sensible when it covers more of your file than Wednesday's did.

**Adopt parts of it.** If your own stylesheet is sound, keep it, and copy in only the rules you classified as improvements. This is the most common outcome, and usually the safest.

**Discard it.** If the AI stylesheet has errors in most of its rules, fixing it will take longer than keeping your own. Record what you found, keep the unedited copy in your commit history, and move on. The audit still did its job: it tested your decisions against a second, independent reading of them.

Whichever you choose, finish with exactly one reading stylesheet and one diplomatic stylesheet, named `reading.xsl` and `diplomatic.xsl`, or one set of CETEIcean files. Do not keep two competing versions of the same view. A reader who finds `reading.xsl` and `ai-reading.xsl` side by side cannot tell which one made your published page.

After the final stylesheets are in place, run the full set of checks once more: the word comparison, the count, the audit template, and Tuesday's read-back on ten lines. Record the final results in `RENDERING.md`.

**Vocabulary.** *Final stylesheet* — The single checked set of rules for each view, from which the published pages are made. *Rerun* — Running every check again after any change to the rules.

**Takeaway:** Fix the AI stylesheet, adopt only its improvements, or discard it; then finish with one checked stylesheet per view and rerun every check on the final version.

---

## **25 Content**

**Worked Example: Auditing an AI Stylesheet for Maud Lewis's Letter**

Olyvia's letter shows what happens when a model does not know the shape of the document. Suppose her prompt pasted the decision table and a sample of the letter's body, but her table did not yet have rows for the parts of a letter. Her TEI uses `<opener>`, `<salute>`, `<closer>` and `<signed>`, as many TEI letters do.

The AI stylesheet has good templates for `<choice>`, `<unclear>` and `<lb/>`. It has none for the four letter parts. Run with the audit template, Olyvia's page shows four red boxes: the greeting, the closing formula and the signature are all running into the body text, with nothing to set them apart.

The word comparison with Wednesday's page shows no differences at all. Every word is present and in order. Only the audit template and Tuesday's page reveal the problem, because the problem is not in the words but in the structure. This is why no single check is enough.

These are undecided decisions, not AI errors. Olyvia decided how a letter should look on Tuesday, in her hand-made page, but never wrote those decisions into `RENDERING.md`. She adds four rows, then writes four short templates, mapping each part to a paragraph or span with a class and matching Tuesday's CSS.

There is one more check for a letter written in a vernacular voice. Her Week 6 policy keeps Maud Lewis's grammar and most of her spelling unchanged. A stylesheet cannot invent new words, but Olyvia confirms with the word comparison that every word from her TEI reached the page, in its original form.

**Vocabulary.** *Document structure* — The conventional parts of a kind of document, such as a letter's greeting, body and signature. *Structural omission* — An error in which every word survives but the parts of a document are no longer distinguished.

**Takeaway:** A word comparison can show no differences while a letter's greeting and signature run into the body; use the audit template and Tuesday's page to catch structural omissions.

---

## **26 Content**

**Worked Example: The 1752 Treaty and an Inconsistent File**

Andromeda's treaty shows why the first-child error is so hard to see. The numbers below are illustrative.

Suppose her AI stylesheet selects `*[1]` in the `<choice>` template, as in the sample. But most of her file was encoded in Week 6 with `<reg>` first, so for most lines the rule shows the regularized form, as it should. A glance at the reading view looks right.

The count check tells a different story. Her TEI has 42 `<choice>` elements, but the reading page has only 36 `reg` spans. Six times, the reading view shows something other than the regularized form.

She searches her TEI and finds the reason. Six of her `<choice>` elements were added later, by copying a pattern from the TEI Guidelines, which happened to put `<orig>` first. Both orders are valid TEI. Her file is correct. The stylesheet's rule depended on something that carries no meaning.

This is an AI error, and the fix is to select by name. But the audit also teaches Andromeda something about her own file. She decides to make the order consistent anyway, so that anyone reading the source sees the same pattern throughout, and records that choice in her Week 6 notes as a tidying change with no effect on meaning.

Notice what found the problem. The word comparison with Wednesday's page did find six differences, but they looked like ordinary spelling variants and were easy to skim past. The count gave an exact number: six layers missing from the reading view.

**Vocabulary.** *Inconsistent encoding* — Valid markup that expresses the same thing in more than one way across a file. *Meaningless dependency* — A rule whose output depends on a feature of the source, such as element order, that carries no editorial meaning.

**Takeaway:** A first-child rule can look right on most lines and fail on a few; counting layer classes on the page against <code>&lt;choice&gt;</code> elements in the TEI finds the exact number of failures.

---

## **27 Content**

**Recording the AI's Contribution**

In Week 6 you recorded AI involvement in your TEI header, because the model had suggested changes to your encoded text. Today the model wrote software that displays your text, not the text itself, so the record belongs with the software.

Record it in three places.

<ol>
  <li><strong>In the stylesheet.</strong> Add a comment at the top of any stylesheet that contains AI-written rules, naming the model, the date, the prompt file, and which rules you adopted.</li>
  <li><strong>In <code>RENDERING.md</code>.</strong> The audit section already lists every difference and how you resolved it. Add a short summary: the model used, whether you fixed, adopted from or discarded its stylesheet, and how many errors, undecided decisions and improvements you found.</li>
  <li><strong>In your commits.</strong> Commit the corrected stylesheet separately from the unedited one, with a message that says what you changed, such as <em>Fix AI reading stylesheet: select choice layers by name, remove whitespace rule</em>.</li>
</ol>

A comment at the top of a stylesheet might read:

```xml
<!-- Reading view stylesheet.
     Template for hi with rend=underline adapted from a stylesheet
     written by [model name] on 2026-10-23 (prompt in
     rendering/prompts/reading-prompt.md). All other templates are
     the editor's own. Audit recorded in RENDERING.md. -->
```

Together these records answer the questions a reviewer will ask: which rules came from a model, which were checked, and who is responsible for each choice.

**Vocabulary.** *Attribution* — A record of who or what contributed each part of a piece of work. *Audit trail* — The connected record, here in comments, notes and commits, that lets someone retrace how a result was produced.

**Takeaway:** Record AI involvement in a comment in the stylesheet, a summary in <code>RENDERING.md</code>, and separate commits for the unedited and corrected versions.

---

## **28 Content**

**What This Week Has Built**

Look at what is now in your `rendering/` folder: a decision table, a hand-made page, two checked stylesheets or a set of CETEIcean files, a print stylesheet, full-length reading and diplomatic views, an audit of an AI-written alternative, and a set of short scripts that check any rendering against your source.

The scripts are worth keeping. `compare.py` and `count.py` will work on any future version of your rendering. When your TEI changes in the coming weeks, as it will when you add lemmas in Week 8 and named entities in Week 9, rerun the stylesheets and then rerun the checks. Each new element will need a row in `RENDERING.md`, and the audit template will tell you which ones are still missing.

This week's work also feeds directly into the Print-Ready Publication. The views you made this week are the start of that publication. The print stylesheet from Wednesday is the start of its PDF. The decision table is the start of the editorial statement that explains to readers what they are looking at.

Finally, notice the shape of the week. On Tuesday you made the decisions. On Wednesday you made rules that carry them out. Today you tested those decisions against a second author who did not know them, and the gaps in your table showed up as the places where the model had to guess. That is the same cycle you have used since Week 4, and it will continue next week.

**Vocabulary.** *Regression check* — Rerunning comparison and count checks after a change, to confirm that nothing that worked before has broken. *Editorial statement* — The part of an edition that explains its editorial policies and display conventions to readers.

**Takeaway:** This week has produced checked views, rules and reusable checks; rerun them whenever your TEI changes, and treat the decision table as the start of your edition's editorial statement.

---

## **29 Content**

**Hypothetical Scenario: The Gap That Filled Itself**

*This scenario is invented to illustrate the risk; it describes no real person or edition.*

An editor is short of time before a conference. Rather than run a stylesheet, they paste the TEI of a damaged eighteenth-century letter into a chat and ask for a clean web page of the reading text. The page comes back in seconds. It looks excellent, and they put it online.

The TEI contains `<gap reason="damage" quantity="3" unit="word"/>` in the middle of a sentence about a debt. The generated page shows no gap. In its place are three words that complete the sentence smoothly. The words make sense. They are the kind of words that often appear in such letters. They are not in the document.

A year later, a student working on the same family's papers quotes the sentence in a thesis. Nobody notices the problem until a reviewer compares the quotation with the manuscript and finds a hole in the paper where the three words should be.

No one tampered with the evidence on purpose. The transcription was correct, and the encoding was correct. The failure happened in one step: the editor asked a model for text instead of rules, and published its text without checking it against the source.

Ask yourself which of this week's checks would have caught it. A count check would have found one gap in the TEI and no brackets on the page. A word comparison with a stylesheet's output would have found three extra words. And the simplest protection of all would have prevented it: a stylesheet can select and wrap your text, but it cannot write words that are not there.

**Vocabulary.** *Confabulated text* — Plausible words produced by a model in place of missing or damaged text. *Source fidelity* — The principle that every word presented as the document's text must be in the document.

**Takeaway:** A model rendering text directly can fill a gap with plausible words; asking for rules instead of text, and counting gaps against brackets, protects readers from text that was never there.

---

## **30 Content**

**Review and Step 3 Checklist**

Today you asked a model to write your rendering rules, and then audited what it wrote against your decision table, Tuesday's page and Wednesday's output. You also built checks you can rerun on any future version of your edition.

Before you leave, confirm each item below:

<ol>
  <li><strong>Prompts saved:</strong> Are <code>reading-prompt.md</code> and <code>diplomatic-prompt.md</code> in <code>rendering/prompts/</code>, each with the model name and date?</li>
  <li><strong>Unedited baseline:</strong> Are the AI stylesheets or CSS committed exactly as the model wrote them, in a commit of their own?</li>
  <li><strong>Template inventory:</strong> Does <code>RENDERING.md</code> pair every decision with a template, and every template with a decision?</li>
  <li><strong>Word comparison:</strong> Does <code>compare.py</code> report equal word counts and no unexplained differences between the final pages and Wednesday's?</li>
  <li><strong>Count check:</strong> Do the counts of layers, unclear readings, line breaks and brackets on each final page match the elements in your TEI?</li>
  <li><strong>No red boxes:</strong> Does the audit template find no unhandled elements in your final stylesheets?</li>
  <li><strong>Audit log:</strong> Is every difference recorded as an AI error, an undecided decision or an improvement, with what you did about it?</li>
  <li><strong>One stylesheet per view:</strong> Do you have exactly one final stylesheet for each view, with AI-written rules credited in a comment?</li>
  <li><strong>Committed:</strong> Are the corrected stylesheets, the scripts and the updated <code>RENDERING.md</code> committed with clear messages?</li>
</ol>

Next week begins Module 8, Lemmatization. You will add a new layer of information to your TEI, the dictionary form of each word, and the rendering rules you built this week will need new rows for it.

**Vocabulary.** *Step 3 milestone* — The completed AI-assisted rendering and its audit, closing the three-step cycle for rendering. *Reusable check* — A script, such as <code>compare.py</code> or <code>count.py</code>, that can be rerun on any later version of the edition.

**Takeaway:** Completing Step 3 gives you final stylesheets you can defend rule by rule, an audit log of everything the model got wrong or right, and checks you can rerun as your edition grows.

---

## References

De Cristofaro, M., & Zilio, D. (2025). Automating XML-TEI encoding of unpublished correspondence: A comparative analysis of two LLM approaches. *AIUCD 2025 Proceedings: Diversity, Equity, and Inclusion: Challenges and Opportunities for Digital Humanities in the Age of Artificial Intelligence*.

Eck, S. O., & Page, K. R. (2026). Multimodal large language model-assisted metadata extraction from historical concert programmes (1872–1928). In *Proceedings of the 13th Annual Conference on Digital Libraries for Musicology (DLfM 2026)*. ACM. https://doi.org/10.1145/3815723.3815726
