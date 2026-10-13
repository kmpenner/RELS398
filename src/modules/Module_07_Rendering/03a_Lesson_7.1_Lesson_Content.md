# Lesson 7.1 — Rendering by Hand: Display Decisions, HTML, and CSS

*RELS 398 / ENGL 398 · Topic 7: Rendering (Publication I) · Meeting #17 (Tue Oct 20)*

***Step 1 of the three-step cycle: manual.** Today you decide how every element in your TEI file should look to a reader, write those decisions down, and then build a small web page by hand that carries them out. That hand-made page is the ground truth that Wednesday's XSLT stylesheet and Friday's AI-generated stylesheet will be measured against.*

---

## **01 Content**

**Your Edition So Far, and Why Nobody Can Read It Yet**

Over six weeks you have built something real. You catalogued your document in a `teiHeader`, linked it to its image, transcribed it line by line, reconciled your transcription against an AI pass, and recorded your normalization decisions inside `<choice>` elements. Your file `transcription_normalized.xml` now holds two layers of your document at once: what the page says, letter for letter, and what a modern reader needs it to say.

Now try a simple test. Send that file to a friend who has never taken this course and ask them to read your document. They will open a screen full of angle brackets, attributes and nested tags. The words of the 1752 Treaty, the 1791 decree, or Maud Lewis's letter are all in there, but they are buried in markup. Your friend sees code, not a document.

This is not a flaw in your work. A TEI file is designed to be precise for machines and for editors, not pleasant for readers. Turning that file into something a person can read is a separate step, and this week is about that step. It is the first stage of publication: making your edition visible.

**Vocabulary.** *Rendering* — Turning an encoded file into a form a person can read, such as a web page or a printed page. *Publication* — Making an edition available to readers outside the project, in a form they can use.

**Takeaway:** A valid TEI file is a complete record of your document but not yet a publication; rendering is the step that turns it into something a reader can use.

---

## **02 Content**

**Content and Presentation Are Two Different Things**

Everything this week rests on one idea: what a text *is* and how it *looks* are separate questions. Your TEI file answers the first question. It says that a word was abbreviated, that a line ended here, that a letter was hard to read. It does not say that the abbreviation should be shown in italics, or that the unclear letter should have a dotted line under it. Those are presentation choices, and they belong somewhere else.

Layout belongs to the rendering of an edition's data, not to the data themselves, which is why some digital projects treat display as a separate scholarly task (Huskey, 2024).

Keeping the two apart has a practical payoff. If you decide next month that abbreviations look better in grey than in italics, you change one display rule and every abbreviation in the edition changes with it. You never touch the transcription. The evidence stays fixed while the presentation is free to improve.

The same idea drives the web itself. HTML records the structure of a page (this is a heading, this is a paragraph), and a separate language, CSS, records how that structure should look. You will write both today.

**Vocabulary.** *Content* — What a text is and says, recorded in the markup. *Presentation* — How the text is displayed: fonts, spacing, colour, what is shown and what is hidden.

**Takeaway:** Keep what your document says (the TEI file) separate from how it looks (the display rules), so you can change the look without ever touching the evidence.

---

## **03 Content**

**One File, Many Views**

Because the content is separate from the presentation, one TEI file can be shown in more than one way. This is the most powerful thing a digital edition can do that a printed book cannot.

Because an encoded text can be run through different sets of rules held in stylesheets, the same file can be shown as a diplomatic text, a critical text, or a reading text (Pierazzo, 2016).

For your project, two views matter most. A **diplomatic view** shows the document as it is: original spellings, abbreviations as written, the original line breaks. A **reading view** shows the document as a modern reader needs it: regularized spelling, expanded abbreviations, lines flowing into paragraphs. Both views come from the same file. Neither one is the "real" text; they are two honest windows onto it.

You already built both layers in Week 6. Every `<choice>` holds an `<orig>` for the diplomatic view and a `<reg>` for the reading view. Rendering is simply the act of choosing, for each view, which child of each `<choice>` to show.

**Vocabulary.** *View* — One particular way of displaying an edition, such as diplomatic or reading. *Stylesheet* — A set of rules that tells software how to display or transform marked-up text.

**Takeaway:** One encoded file can produce several views; your diplomatic and reading views both come from the `<choice>` layers you built in Week 6.

---

## **04 Content**

**The Diplomatic View**

The diplomatic view is for readers who care about the document as an object. A historian of the French Revolution may want to see exactly how a clerk in 1791 spelled and abbreviated official titles. A scholar of Maritime folk art may want to see where Maud Lewis broke her lines and how she spelled words in her own hand. A legal historian may want to see the 1752 Treaty's capitalization and punctuation exactly as the printer set them.

So the diplomatic view shows what you put inside `<orig>`, `<abbr>`, and `<sic>`. It keeps every line break where the page put it, usually with a line number in the margin so a reader can cite "line 14" and be understood. It marks unclear letters and gaps so the reader knows exactly where your reading is uncertain.

A diplomatic view is not a photograph. It is still your interpretation, because you decided what each letter was. But it is the interpretation that stays as close to the page as type allows. It is the view you check against the image when a reading is in doubt.

**Vocabulary.** *Diplomatic view* — A display that follows the document's own spelling, abbreviation and line breaks as closely as possible. *Line number* — A number shown beside each line so readers can cite a precise location.

**Takeaway:** The diplomatic view shows the original layer of your file, line by line, for readers who need the document as it actually appears.

---

## **05 Content**

**The Reading View, and What It Hides**

The reading view is for readers who care about what the document says. A student reading the 1752 Treaty for its terms should not have to decode eighteenth-century spellings in every clause. A reader of Maud Lewis's letter wants to follow her news, not stumble over missing apostrophes. So the reading view shows `<reg>`, `<expan>` and `<corr>`, and lets the lines flow together into ordinary paragraphs.

That convenience has a cost. A smooth reading view hides the editor's work, and it can hide it so well that readers forget anyone made a choice at all.

A clean reading text, with almost no visible trace of the editing behind it, can give readers the false impression that the text is stable and finished (Pierazzo, 2016).

Your job is to make the reading view easy without making it dishonest. A short note at the top of the page saying what was regularized, and a clear way to reach the diplomatic view, cost almost nothing. Later sections show you how to build both.

**Vocabulary.** *Reading view* — A display that shows regularized spelling and expanded abbreviations, with lines joined into paragraphs. *Silent intervention* — An editorial change that the reader cannot see or detect.

**Takeaway:** The reading view makes the document easy to read but hides your interventions; always tell readers what was changed and how to see the original.

---

## **06 Content**

**Who Is Your Reader?**

Before you decide how anything should look, decide who will read your edition and why. This is not a formality. Your answers will settle dozens of small display questions later.

Print editions tried to serve every kind of reader with one product because of cost, but a digital edition can offer different outputs for different readers (Pierazzo, 2016).

Think about your own document. Andromeda's 1752 Treaty will be read by people studying Mi'kmaw–British relations, and some of them will read the treaty for its legal promises, word by word. They need accurate article numbers and visible line references. Olyvia's Maud Lewis letter may reach readers who love her paintings and have never seen her handwriting; they need a warm, readable page and perhaps a link to the image. Ace's 1791 decree will interest historians of the Revolution who want to cite the exact wording, and students who need the French to be readable on a screen.

Write down two or three real readers for your edition before you go on. Name what each one needs to do with it: read it through, check a word, quote a line, compare it with the image.

**Vocabulary.** *Audience* — The specific readers an edition is built for. *Use case* — A concrete task a reader wants to perform with the edition, such as quoting a line.

**Takeaway:** Decide who your readers are and what they need to do before you make any display decision; the right look depends on the reader.

---

## **07 Content**

**Screens, Phones, and Paper**

Your readers will not all see your page the same way. Some will open it on a laptop, some on a phone on the bus, and some will print it to read with a pencil.

The same text read on a phone, a tablet, a laptop, or a sheet of printed paper can give a quite different reading experience (Pierazzo, 2016).

This matters for display decisions. A diplomatic view with long lines and line numbers in a wide margin works on a laptop but may break badly on a narrow phone screen. Colour that marks an unclear reading on screen may vanish on a black-and-white printer. Hover tooltips that explain a gap do not exist on paper at all.

Today you will build for the laptop screen first, because that is where you will check your work. But keep the other two in mind as you make each decision. Ask of every choice: will this still make sense on a phone? Will it still make sense on paper? On Wednesday you will add a print stylesheet that answers the paper question directly.

**Vocabulary.** *Device* — The screen or medium on which a reader encounters the edition. *Responsive layout* — A page design that adapts to different screen widths.

**Takeaway:** Every display decision should survive a phone screen and a printed page, not just your laptop.

---

## **08 Content**

**The Rendering Decision Table**

Now comes the core manual work of the day. Open your `transcription_normalized.xml` and list every element that appears inside your `<body>`. Then, for each one, decide how it should look in each view. Write the decisions in a new file called `RENDERING.md`, just as you wrote `NORMALIZATION.md` in Week 6.

Here is the shape of the table. Your rows will depend on which elements your file actually uses.

<table>
  <thead>
    <tr><th>TEI element</th><th>What it records</th><th>Diplomatic view</th><th>Reading view</th></tr>
  </thead>
  <tbody>
    <tr><td><code>&lt;lb/&gt;</code></td><td>A line break on the page</td><td>New line, with a line number</td><td>No break; text flows on</td></tr>
    <tr><td><code>&lt;orig&gt;</code> / <code>&lt;reg&gt;</code></td><td>Original and regularized spelling</td><td>Show <code>orig</code></td><td>Show <code>reg</code></td></tr>
    <tr><td><code>&lt;abbr&gt;</code> / <code>&lt;expan&gt;</code></td><td>Abbreviation and its expansion</td><td>Show <code>abbr</code></td><td>Show <code>expan</code>, supplied letters in italics</td></tr>
    <tr><td><code>&lt;sic&gt;</code> / <code>&lt;corr&gt;</code></td><td>An error and its correction</td><td>Show <code>sic</code></td><td>Show <code>corr</code></td></tr>
    <tr><td><code>&lt;unclear&gt;</code></td><td>Letters that are hard to read</td><td>Dotted underline</td><td>Dotted underline</td></tr>
    <tr><td><code>&lt;gap/&gt;</code></td><td>Text that could not be read at all</td><td>[…] with reason on hover</td><td>[…] with reason on hover</td></tr>
  </tbody>
</table>

Every row is a decision you can defend, and every row will become a rule in code.

**Vocabulary.** *Rendering decision* — A recorded rule for how one TEI element appears in one view. *`RENDERING.md`* — The file in your repository where you record every rendering decision.

**Takeaway:** List every element your file uses and decide, in writing, how each one appears in each view; the table in `RENDERING.md` is today's main deliverable.

---

## **09 Content**

**Deciding About Line Breaks**

Line breaks are the first decision, and they are less simple than they look. In Week 4 you recorded every line break on the page with `<lb/>`, often with a number: `<lb n="7"/>`.

In the diplomatic view, the answer is clear: each `<lb/>` starts a new line, and its number appears in the margin. In the reading view, the usual answer is that line breaks disappear and the text runs on as a paragraph. But watch what happens to the words on either side.

Suppose an illustrative line from a letter reads `the paintings<lb n="4"/>were sent`. If the reading view simply deletes the break, the words may run together as *paintingswere*. Whether that happens depends on whether there is a space or a new line in your file next to the `<lb/>`. Check your own file now and see how you typed your line breaks.

Then there are words split across two lines. If a printer broke *Governor* as *Gover-* at the end of one line and *nor* at the start of the next, the reading view should rejoin it as *Governor*, with no hyphen and no space. TEI marks this with `<lb break="no"/>`. Write down what your reading view does with that hyphen: keep it, or remove it.

**Vocabulary.** *`<lb/>`* — An empty TEI element marking the start of a new line on the page. *`break="no"`* — An attribute on `<lb/>` saying the line break falls inside a word.

**Takeaway:** Decide what each view does with line breaks, and check that removing a break in the reading view never glues two words together or leaves a stray hyphen.

---

## **10 Content**

**Deciding About `<choice>`: Original and Regularized Spelling**

Your Week 6 work produced many `<choice>` elements like this one:

```xml
<choice>
  <orig>publick</orig>
  <reg resp="#editor">public</reg>
</choice>
```

The basic rule is simple. The diplomatic view shows the `<orig>`; the reading view shows the `<reg>`. But there are two further decisions to make, and you should record both.

First, should the reading view show any sign that a word was regularized? Some editions show nothing. Others put a faint mark under the word, or let the reader hover over it to see the original. A light signal respects the reader who wants a smooth text while keeping the editing visible to the reader who wants to check.

Second, what happens to Maud Lewis's grammar? In Week 6 you decided to regularize her spelling (*dont* to *don't*) but never her grammar (*we was* stays *we was*). Your rendering must keep that promise. If *we was* has no `<choice>` around it, it will appear the same in both views, which is exactly right. The rendering never makes an editorial decision that the encoding did not make first.

**Vocabulary.** *`<choice>`* — A TEI element grouping alternative encodings of the same passage. *Regularization signal* — A visual hint in the reading view that a word's spelling was standardized.

**Takeaway:** Show `<orig>` in the diplomatic view and `<reg>` in the reading view, decide whether regularized words carry a visible hint, and never let the display change anything the encoding did not.

---

## **11 Content**

**Deciding About Abbreviations**

Abbreviations follow the same pattern as spelling. The diplomatic view shows `<abbr>`, and the reading view shows `<expan>`. The extra decision here is how to show the letters you supplied.

Suppose the 1752 Treaty abbreviates *Governor* as *Gov^r*, with a raised *r*. Your encoding might be:

```xml
<choice>
  <abbr>Gov<hi rend="sup">r</hi></abbr>
  <expan>Gov<ex>erno</ex>r</expan>
</choice>
```

The `<ex>` element marks the letters that are not on the page. A common print convention puts supplied letters in italics or round brackets, so the reader sees *Gov(erno)r* and knows which letters the editor added. Another choice is to show the expansion plainly and let the diplomatic view carry the evidence.

Decide which convention you will use, and use it everywhere. The worst outcome is a page where some expansions are marked and others are not, because the reader can no longer tell which letters came from the page. If your file does not use `<ex>`, you can only show whole expansions; note that limit in `RENDERING.md`.

**Vocabulary.** *`<expan>`* — A TEI element holding the full form of an abbreviated word. *`<ex>`* — A TEI element marking letters an editor supplied when expanding an abbreviation.

**Takeaway:** Show abbreviations in the diplomatic view and expansions in the reading view, and choose one consistent way to mark the letters you supplied.

---

## **12 Content**

**Deciding About Errors and Corrections**

Some of you used `<sic>` and `<corr>` in Week 6 to record a real mistake on the page and your correction of it. This pair needs more care than spelling, because it involves a judgment that the writer got something wrong.

The diplomatic view shows `<sic>`, the text as written. The reading view shows `<corr>`, your correction. But should the reading view also say that a correction was made? A common print convention adds *[sic]* after an error that is kept, or puts the corrected letters in square brackets.

Think about what your readers need. If Ace finds that a printer set the same word twice in the 1791 decree, a reader of the French text will be grateful for the correction and will probably want a small signal that it was made. If you are not sure whether something is really an error, you should not have used `<sic>` at all; go back and check your Week 6 rule ledger.

Remember the Week 6 warning about Maud Lewis: her vernacular grammar is not an error and must never carry `<sic>`. If your rendering shows a *[sic]* anywhere in her letter, check that the encoding underneath it is correct.

**Vocabulary.** *`<sic>`* — A TEI element marking text that is apparently wrong but reproduced as written. *`<corr>`* — A TEI element holding the editor's correction of an error.

**Takeaway:** Show the error in the diplomatic view and the correction in the reading view, and give readers a visible signal whenever you have corrected the writer.

---

## **13 Content**

**Deciding About Uncertainty: `<unclear>` and `<gap/>`**

Uncertainty must be visible in every view. A reader who quotes your edition needs to know which words you read with confidence and which you could only guess.

The `<unclear>` element marks letters you read but are not sure of. A widely used convention places a dot under each uncertain letter, but that is hard to do in a web page. A dotted underline is a practical substitute on screen. Whatever you choose, do not use colour alone, because colour disappears on a black-and-white printout and some readers cannot distinguish it.

The `<gap/>` element marks text you could not read at all, such as a hole, a stain, or a torn edge. It is empty, so there is no text to show. You must decide what stands in for it. A common choice is `[…]`, with the reason (`reason="illegible"`, `reason="damage"`) and the extent (`quantity="2" unit="word"`) available to the reader, perhaps in a tooltip.

Unlike spelling, uncertainty usually looks the same in both views. A word you could not read in the diplomatic view is just as unreadable in the reading view. Hiding it would make the reading view claim a certainty you do not have.

**Vocabulary.** *`<unclear>`* — A TEI element marking text that is present but difficult to read with certainty. *`<gap/>`* — An empty TEI element marking text that has been left out because it cannot be read.

**Takeaway:** Show uncertain readings and gaps in both views, with a mark that does not depend on colour alone.

---

## **14 Content**

**Deciding About Structure: Headings, Paragraphs, Signatures**

So far you have decided about words. Now decide about the larger shape of the document. Your `<body>` probably contains structural elements such as `<div>`, `<head>`, `<p>`, `<closer>`, `<signed>`, or `<pb/>`.

The 1752 Treaty is organized in numbered articles. If you encoded each one as `<div type="article" n="3">` with a `<head>`, the reader will expect each article to start on its own line with a visible heading. The 1791 decree likely opens with a formal preamble and then numbered articles of its own. Maud Lewis's letter has an opening greeting, a body, and a closing with her signature, which a reader expects to see set apart at the end.

Write down how each structural element should look. Headings should look like headings. Paragraphs should look like paragraphs, with space between them. A signature usually sits on its own line, often set to the right. A page break, `<pb/>`, may appear in the diplomatic view as a small marker such as "[page 2]" and may vanish in the reading view.

These choices seem obvious, but they still have to be made, and an automated tool on Wednesday will make them for you unless you have decided first.

**Vocabulary.** *Structural element* — A TEI element that records the organization of a text, such as a division, heading, or paragraph. *`<pb/>`* — An empty TEI element marking the start of a new page.

**Takeaway:** Decide how headings, paragraphs, closings and page breaks should look, so that the shape of the original document is visible to the reader.

---

## **15 Content**

**What HTML Is**

With your decisions recorded, you can now build the page. Web pages are written in HTML, the HyperText Markup Language. You will find it familiar, because it is a markup language like TEI: it uses tags in angle brackets, opening and closing pairs, and attributes.

Here is a complete, minimal HTML page:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Letter of Maud Lewis, 13 February 1967</title>
    <link rel="stylesheet" href="reading.css">
  </head>
  <body>
    <h1>Letter of Maud Lewis, 13 February 1967</h1>
    <p>The text of the letter goes here.</p>
  </body>
</html>
```

The `<head>` holds information about the page: its character encoding, its title (shown in the browser tab), and a link to the stylesheet. The `<body>` holds what the reader sees. `<h1>` is a top-level heading and `<p>` is a paragraph.

Save this as `edition.html` in a new folder called `rendering/`, then double-click it. It opens in your web browser. Every time you change the file, save it and refresh the browser to see the result.

**Vocabulary.** *HTML* — The markup language used to structure web pages. *`<head>` and `<body>`* — The two parts of an HTML page: information about the page, and the content the reader sees.

**Takeaway:** HTML is a markup language like TEI, with a `<head>` for information about the page and a `<body>` for what the reader sees.

---

## **16 Content**

**HTML Is Forgiving, and That Is Dangerous**

There is one big difference between HTML and the XML you have written all term. XML is strict. If you leave a tag unclosed in your TEI file, VS Code reports an error and the file is invalid. HTML is forgiving. If you leave a tag unclosed in a web page, the browser quietly guesses what you meant and shows something anyway.

That sounds friendly, but for an editor it is a trap. A browser's guess can hide words, swallow a closing note into a heading, or apply italics to the rest of the page. Nothing warns you. The page simply looks a little wrong, or worse, looks fine while the structure underneath is broken.

So you will check your HTML deliberately. Free tools such as the W3C Markup Validation Service (validator.w3.org) will read your file and list every unclosed tag and misplaced element. Run your page through it before you commit. Treat any error it reports the same way you treated a TEI schema error: fix it before you go on.

Two characters need special care in both XML and HTML. A literal ampersand must be written `&amp;`, and a literal less-than sign must be written `&lt;`. If the 1752 Treaty uses an ampersand for *and*, check how it appears in your page.

**Vocabulary.** *Well-formed* — Following the basic rules of a markup language, such as closing every tag. *HTML validator* — A tool that checks a web page for structural errors the browser would silently accept.

**Takeaway:** Browsers silently repair broken HTML, so check your page with a validator rather than trusting how it looks.

---

## **17 Content**

**Mapping TEI Elements to HTML**

HTML has a small, fixed set of elements. It has no `<choice>`, no `<orig>`, no `<unclear>`. So how do you carry TEI's rich vocabulary into a web page? The usual answer is to use two general-purpose HTML elements and label them with a `class` attribute.

The `<span>` element wraps a piece of text inside a line, with no effect of its own. The `<div>` element wraps a larger block. The `class` attribute gives each one a name that a stylesheet can find. So the TEI on the left becomes the HTML on the right:

<table>
  <thead>
    <tr><th>TEI</th><th>Hand-written HTML</th></tr>
  </thead>
  <tbody>
    <tr><td><code>&lt;choice&gt;</code></td><td><code>&lt;span class="choice"&gt;</code></td></tr>
    <tr><td><code>&lt;orig&gt;publick&lt;/orig&gt;</code></td><td><code>&lt;span class="orig"&gt;publick&lt;/span&gt;</code></td></tr>
    <tr><td><code>&lt;reg&gt;public&lt;/reg&gt;</code></td><td><code>&lt;span class="reg"&gt;public&lt;/span&gt;</code></td></tr>
    <tr><td><code>&lt;unclear&gt;Kinn&lt;/unclear&gt;</code></td><td><code>&lt;span class="unclear"&gt;Kinn&lt;/span&gt;</code></td></tr>
    <tr><td><code>&lt;div type="article" n="3"&gt;</code></td><td><code>&lt;section class="article" id="art3"&gt;</code></td></tr>
    <tr><td><code>&lt;head&gt;</code> inside an article</td><td><code>&lt;h2&gt;</code></td></tr>
  </tbody>
</table>

Notice the pattern: you keep the TEI name as the class name. That makes the HTML easy to check against your XML, line by line. Where HTML has a real equivalent, such as `<p>` for a paragraph or `<h2>` for a heading, use it.

**Vocabulary.** *`<span>`* — A general HTML element that wraps inline text without changing its appearance. *`class`* — An HTML attribute that names an element so a stylesheet can find and style it.

**Takeaway:** Carry each TEI element into HTML as a `<span>` or `<div>` whose `class` repeats the TEI name, using real HTML elements where they exist.

---

## **18 Content**

**Line Breaks in HTML**

HTML ignores the line breaks in your source file. If you type three lines of text inside a `<p>`, the browser runs them together into one paragraph. To make a new line appear, you need an element that creates one.

For your edition, mark each TEI `<lb/>` with an empty `<span>` that carries the line number:

```html
<p>
  <span class="lb" data-n="1"></span>We the Subscribers
  <span class="lb" data-n="2"></span>Delegates from the Tribe
</p>
```

The `data-n` attribute is HTML's way of holding a custom value, here the line number from `<lb n="2"/>`. On its own, this empty span does nothing. In the next sections, your diplomatic stylesheet will turn each `lb` span into a new line with its number in the margin, and your reading stylesheet will leave it as nothing at all.

Notice the space or new line before each span in the example. That whitespace is what stops two words from gluing together in the reading view when the break disappears. For a word split across lines, where TEI has `<lb break="no"/>`, write the span with no space on either side, so the two halves rejoin into one word.

These lines are illustrative. Use the real words and line numbers from your own file.

**Vocabulary.** *`data-` attribute* — An HTML attribute for storing a custom value, such as a line number. *Whitespace* — Spaces, tabs and new lines; in HTML they decide whether words stay apart.

**Takeaway:** Mark each line break with an empty `<span class="lb">` carrying its number, and watch the whitespace around it so words neither merge nor split wrongly.

---

## **19 Content**

**What CSS Is**

CSS, Cascading Style Sheets, is the language that decides how HTML looks. A CSS file is a list of rules. Each rule has a **selector**, which says which elements it applies to, and a set of **declarations**, which say what to do to them.

```css
p {
  font-family: Georgia, serif;
  line-height: 1.6;
}

.unclear {
  text-decoration: underline dotted;
}
```

The first rule says: every `<p>` should use a serif font with comfortable spacing between lines. The second rule starts with a full stop, which makes it apply to every element whose class is `unclear`. It gives those elements a dotted underline.

The property you will use most this week is `display`. Setting `display: none;` on an element hides it completely, as if it were not there. Setting `display: block;` makes an element start on a new line. These two settings, with one extra rule for line breaks in the next section, are enough to build both your views.

Save your rules in a separate file, such as `reading.css`, in the same `rendering/` folder, and connect it with the `<link>` line in your page's `<head>`. Change a rule, save, refresh, and see what happens.

**Vocabulary.** *CSS* — The language that controls how HTML elements look. *Selector* — The part of a CSS rule that says which elements the rule applies to.

**Takeaway:** CSS is a list of rules, each pairing a selector with declarations; `display: none` hides an element and `display: block` puts it on its own line.

---

## **20 Content**

**Two Stylesheets, One Page**

Here is the central move of the day. You will write one HTML page that contains both layers of every `<choice>`, and two stylesheets that each show one layer. This is the content–presentation split from section 02, built with your own hands.

Your `diplomatic.css` hides the reading layer and shows each line on its own, numbered:

```css
.reg, .expan, .corr { display: none; }

.lb::before {
  content: "\A" attr(data-n) "  ";
  white-space: pre;
  color: #666;
}
```

The line-break rule needs a word of explanation. The `::before` part adds generated text just before each `lb` span. In that text, `\A` is CSS's code for a new line, `attr(data-n)` is the line number, and the two spaces separate the number from the words. The setting `white-space: pre;` tells the browser to obey that new line instead of collapsing it. You might expect `display: block;` on the span to do the job, but try it: the number lands on a line by itself and the words drop to the line below, because the empty block holds only the number.

Your `reading.css` hides the original layer and lets the lines flow:

```css
.orig, .abbr, .sic { display: none; }

.lb { display: inline; }
.expan .ex { font-style: italic; }
```

To switch views, change one word in the `<link>` line of your page, from `diplomatic.css` to `reading.css`, and refresh. The words on the page never change. Only the rules change, and the page transforms. When you see it happen with your own document, the idea behind the whole week becomes concrete.

**Vocabulary.** *Diplomatic stylesheet* — A CSS file that shows the original layer and the page's line breaks. *Reading stylesheet* — A CSS file that shows the regularized layer as flowing text.

**Takeaway:** Put both layers into one HTML page and write two stylesheets that each hide one layer; switching the stylesheet switches the view without touching the text.

---

## **21 Content**

**Worked Example: A Line of the 1752 Treaty**

Let us put the pieces together for one illustrative line. Suppose your TEI for one line of the 1752 Treaty reads:

```xml
<lb n="12"/>the <choice><abbr>Gov<hi rend="sup">r</hi></abbr><expan>Gov<ex>erno</ex>r</expan></choice>
and <choice><orig>Councill</orig><reg>Council</reg></choice> of
```

Your hand-written HTML for the same line is:

```html
<span class="lb" data-n="12"></span>the <span class="choice"><span class="abbr">Gov<sup>r</sup></span><span class="expan">Gov<span class="ex">erno</span>r</span></span>
and <span class="choice"><span class="orig">Councill</span><span class="reg">Council</span></span> of
```

With `diplomatic.css`, the reader sees a new line numbered 12 reading *the Gov^r and Councill of*. With `reading.css`, the reader sees *the Gov*erno*r and Council of* running on from the line before, with the supplied letters in italics.

Check three things. Is every TEI element present in the HTML? Is every word present, in the same order? Is there a space between every pair of words in both views? These checks are what you will repeat for every line you render today.

**Vocabulary.** *Worked example* — A fully solved instance of a task, shown step by step. *Line-by-line check* — Comparing the source and the rendering one line at a time for missing elements or words.

**Takeaway:** For each line, check that every element and every word of the TEI appears in the HTML, in order, with correct spacing in both views.

---

## **22 Content**

**Worked Example: Maud Lewis's Letter**

A personal letter raises different questions from a treaty. Olyvia's page is handwritten, informal and short. The reader is likely to care about Maud Lewis's voice and her news more than about line numbers.

So the reading view of a letter may look like a letter. The greeting sits on its own line. The body runs as paragraphs. The closing and signature sit at the end, set to the right. Your HTML can use real elements for these parts:

```html
<p class="salute">Dear Mr. Kinnear</p>
<p>…the body of the letter…</p>
<p class="closer">Yours truly<br>
  <span class="signed">Maud Lewis</span></p>
```

These lines are illustrative; copy the real wording from your own transcription. In your `reading.css`, a rule such as `.closer { text-align: right; }` sets the closing apart.

The diplomatic view of a letter keeps every one of her line breaks, because how she filled the page is part of the evidence. Readers who compare your diplomatic view with the photograph should be able to find each line in both. Check also that her vernacular grammar is identical in both views, as your Week 6 policy requires.

**Vocabulary.** *Salutation* — The greeting that opens a letter. *Closer* — The closing formula and signature that end a letter; TEI records it with `<closer>`.

**Takeaway:** A letter's reading view should look like a letter, with its greeting and signature set apart, while its diplomatic view keeps every original line break.

---

## **23 Content**

**Worked Example: The 1791 Decree and French Text**

Ace's decree is in French, and that adds two technical requirements that are easy to forget.

First, the page must declare its character encoding. The line `<meta charset="utf-8">` in the `<head>` tells the browser to read the file as UTF-8, the same encoding your TEI file uses. Without it, accented letters such as *é*, *è*, *à* and *ç* can appear as strings of nonsense symbols on some computers.

Second, the page must declare its language. Write `<html lang="fr">` at the top, instead of `lang="en"`. This tells browsers, search engines and screen readers that the text is French. A screen reader will then pronounce *Assemblée nationale* as French words rather than mangling them with English sounds. If your page mixes languages, such as an English introduction above a French text, you can put `lang="fr"` on the element that holds the French and leave the rest in English.

The same applies to any project with more than one language. If Andromeda's treaty contains any Mi'kmaw words or names, the right language code on those words helps readers and their software treat them properly.

**Vocabulary.** *Character encoding* — The system that maps stored bytes to letters; UTF-8 covers all the world's scripts. *`lang` attribute* — An HTML attribute declaring the language of an element's text.

**Takeaway:** Declare `<meta charset="utf-8">` and the correct `lang` on every page, so accented letters display correctly and software knows what language it is reading.

---

## **24 Content**

**Text That Matters Belongs in the HTML, Not the CSS**

CSS can add text to a page. A rule such as `.gap::before { content: "[…]"; }` makes the brackets appear wherever there is a gap. It is tempting to use this trick for every editorial mark: brackets, *[sic]*, line numbers, and so on.

Be careful. Text added by CSS is decoration, not content. In many browsers it cannot be selected, copied or searched, and some screen readers skip it. A reader who copies a sentence of your reading view into their own notes may lose every bracket that told them where the gaps were. Their quotation will then claim more certainty than your edition does.

So follow a simple rule. If a mark carries editorial meaning (a gap, a correction, an uncertain reading), put it in the HTML as real text, for example `<span class="gap" title="2 words, ink stain">[…]</span>`. Use CSS only for appearance: colour, spacing, fonts, underlines, and hiding one layer or the other. Line numbers in the diplomatic margin are a fair exception, because they label the text rather than form part of it.

The `title` attribute in that example gives a small pop-up explanation when the reader hovers over the gap. It works on a laptop, but not on a phone or on paper, so the brackets themselves must still be clear without it.

**Vocabulary.** *Generated content* — Text inserted by a CSS rule rather than written in the HTML. *`title` attribute* — An HTML attribute whose text appears as a tooltip when the pointer rests on an element.

**Takeaway:** Put every editorial mark that carries meaning into the HTML as real text; use CSS only to change how things look.

---

## **25 Content**

**Making the Page Readable for Everyone**

A scholarly edition is published for readers, and some of your readers will use screen magnifiers, screen readers, or high-contrast settings. Building with them in mind costs little if you do it from the start.

Use real headings (`<h1>`, `<h2>`) for real headings, in order, because screen-reader users jump from heading to heading to find their place. Keep enough contrast between text and background; grey text on a white page may look elegant but can be hard to read. Never use colour as the only signal of an editorial state. An unclear reading marked only in red is invisible to a reader who cannot tell red from black, and to anyone with a black-and-white printer.

Set a comfortable line length and line spacing for the reading view. Very long lines are tiring to read on a wide screen. A rule such as `body { max-width: 40em; margin: auto; }` keeps the text in a readable column.

Finally, add a short statement at the top of each view, in plain words. For a reading view it might say that this is the reading view, that spelling has been regularized and abbreviations expanded, that supplied letters are in italics, and that the diplomatic view shows the original spelling. This one statement answers the warning in section 05. It tells every reader what kind of text they are looking at.

**Vocabulary.** *Accessibility* — Designing so that readers with different abilities and tools can use the page. *Contrast* — The difference in brightness between text and its background.

**Takeaway:** Use real headings, strong contrast, more than colour to mark editorial states, and a plain statement at the top of each view saying what the reader is seeing.

---

## **26 Content**

**Checking That Nothing Was Lost**

When you have rendered your passage, check it as carefully as you checked your transcription. Rendering by hand is a new chance to make mistakes: a word left out while copying, two spans in the wrong order, a gap that turned into nothing.

Use three checks. First, read the diplomatic view aloud while following the image of your document with your finger. Every word on the page should be on the screen, in the same line. Second, read the reading view aloud while following your TEI file. Every `<reg>`, `<expan>` and `<corr>` should appear, and every word outside a `<choice>` should appear in both views. Third, count. Pick ten lines and count the words in your TEI and in each view. If the numbers differ, find out why before you go on.

Record what you find in `RENDERING.md`, under a heading such as "Checks". If you found and fixed a problem, say what it was. That record is part of the work, just as your reconciliation notes were in Week 5.

**Vocabulary.** *Fidelity check* — A deliberate comparison confirming that a rendering preserves every word and mark of its source. *Read-back* — Reading a rendering aloud against its source to catch omissions.

**Takeaway:** Check your rendering against both the image and the TEI file, word by word and line by line, and record every problem you find and fix.

---

## **27 Content**

**Why Do This by Hand?**

On Wednesday you will render the same file automatically, and in seconds. So why spend a class building a page by hand? Because the automatic version is only as good as the decisions behind it, and you cannot judge a tool's decisions until you have made your own.

The idea of generating editions automatically from one encoded file is not new. Manuscript scholars note that a carefully annotated file can produce both diplomatic and critical editions, in print and online, automatically (Bausi et al., 2015). The usual tool is XSLT, a language that can transform an XML document into an HTML web page, a plain-text file, or a formatting-object file that is then turned into a PDF (Bausi et al., 2015). Working projects build this into their routine: in one recent music-and-text edition project, the encoders tested their transcription and edition versions with XSLT stylesheets before storing the files in Git (Weigl et al., 2025).

Your hand-made page is your ground truth, just as your manual transcription was in Week 4. On Wednesday you will hold the XSLT output up against it. On Friday you will hold an AI-written stylesheet up against it. Every difference will be either a mistake by the tool or a decision you had not thought to make. Either way, you will only see it because you did this first.

**Vocabulary.** *XSLT* — A language for transforming XML documents into other forms, such as HTML. *Ground truth* — A carefully checked result used as the standard for judging automated results.

**Takeaway:** Your hand-made page is the ground truth for this week; without it, you cannot tell whether Wednesday's and Friday's automatic renderings are right.

---

## **28 Content**

**Hypothetical Scenario: The Quotation That Went Wrong**

*This scenario is invented to illustrate the risk; it describes no real person or edition.*

A student writing a paper on colonial treaty language finds an online edition of a mid-eighteenth-century treaty. The page is clean and pleasant to read. The student quotes a clause in the paper, word for word, and comments on how "modern" the treaty's spelling seems for its date.

The professor checks the clause against a photograph of the original. The original spellings are quite different. The edition had regularized every word, which was a reasonable choice for a reading view. But the page gave no sign of it: no statement at the top, no hint on changed words, and no link to a diplomatic view. The student had no way to know.

Who made the mistake? The student should have checked the edition's introduction. But the edition made the mistake easy. Its encoding may have been flawless, with every `<orig>` and `<reg>` in place, and its rendering still misled a careful reader.

Ask yourself which of today's decisions would have prevented this. A one-sentence statement at the top of the page. A light mark on regularized words. A link to the diplomatic view. Each is cheap, and each belongs in your `RENDERING.md`.

**Vocabulary.** *Hypothetical scenario* — An invented situation used to show a real risk. *Rendering statement* — A short note on a page telling readers which view they are seeing and what was changed.

**Takeaway:** A perfect encoding can still mislead readers if the rendering hides its interventions; a rendering statement and a link to the diplomatic view prevent it.

---

## **29 Content**

**Saving Your Work in Git**

Your rendering is part of your edition, so it belongs in your repository with everything else. Organize it so that anyone, including you in December, can see how the parts fit together.

A simple layout is:

<table>
  <thead>
    <tr><th>File</th><th>What it holds</th></tr>
  </thead>
  <tbody>
    <tr><td><code>RENDERING.md</code></td><td>Your decision table, your readers, and your checks</td></tr>
    <tr><td><code>rendering/edition.html</code></td><td>The hand-written page with both layers</td></tr>
    <tr><td><code>rendering/diplomatic.css</code></td><td>Rules for the diplomatic view</td></tr>
    <tr><td><code>rendering/reading.css</code></td><td>Rules for the reading view</td></tr>
  </tbody>
</table>

Commit in small steps, as you learned in Week 1. Commit `RENDERING.md` once your decisions are written, before you write any code, with a message such as `docs: record rendering decisions for diplomatic and reading views`. Commit the HTML and each stylesheet separately once they work. If a later change breaks the page, these small commits let you see exactly what changed and step back.

The order of those commits also tells a story. It shows that you decided first and coded second, which is the method of the whole course.

**Vocabulary.** *Repository layout* — The arrangement of folders and files in a project, chosen so others can find their way. *Atomic commit* — A commit that records one complete, self-contained change.

**Takeaway:** Keep `RENDERING.md`, your HTML page and both stylesheets in your repository, and commit your decisions before your code.

---

## **30 Content**

**Review and Step 1 Checklist**

Today you moved your edition from a file that only machines and editors can read to a page that anyone can open in a browser. More importantly, you made every display decision yourself, in writing, before any tool could make it for you.

Before you leave, confirm each item below:

<ol>
  <li><strong>Readers named:</strong> Does <code>RENDERING.md</code> name two or three real readers of your edition and what each needs to do with it?</li>
  <li><strong>Decision table complete:</strong> Does it give a diplomatic and a reading decision for every element in your <code>&lt;body&gt;</code>, including line breaks, every <code>&lt;choice&gt;</code> pair, <code>&lt;unclear&gt;</code>, <code>&lt;gap/&gt;</code>, and structural elements?</li>
  <li><strong>Page built:</strong> Does <code>rendering/edition.html</code> hold at least ten lines of your document, with both layers of every <code>&lt;choice&gt;</code>, and the correct <code>charset</code> and <code>lang</code>?</li>
  <li><strong>Two views working:</strong> Do <code>diplomatic.css</code> and <code>reading.css</code> each produce the right view when linked?</li>
  <li><strong>Honest marks:</strong> Are gaps and uncertain readings visible in both views without relying on colour, and does each view carry a rendering statement?</li>
  <li><strong>Checked and valid:</strong> Have you done the read-back and word-count checks, and does the page pass the HTML validator?</li>
  <li><strong>Committed:</strong> Are your decisions and your code committed in separate, clearly described commits?</li>
</ol>

On Wednesday you will render the same file automatically with XSLT and with CETEIcean, and compare the results with the page you made today.

**Vocabulary.** *Step 1 milestone* — The completed manual rendering and decision record, fixed as the standard for the rest of the week.

**Takeaway:** Completing Step 1 gives you a written set of display decisions and a hand-made page that carries them out, the standard against which every automatic rendering this week will be judged.

---

## References

Bausi, A., Borbone, P. G., Briquel-Chatonnet, F., Buzi, P., Gippert, J., Macé, C., Maniaci, M., Melissakis, Z., Parodi, L. E., & Witakowski, W. (Eds.). (2015). *Comparative oriental manuscript studies: An introduction*. COMSt.

Huskey, S. J. (2024). Committing to reproducibility and explainability: Using Git as a research journal. *International Journal of Digital Humanities, 6*, 9–21. https://doi.org/10.1007/s42803-023-00076-9

Pierazzo, E. (2016). Modelling digital scholarly editing: From Plato to Heraclitus. In M. J. Driscoll & E. Pierazzo (Eds.), *Digital scholarly editing: Theories and practices* (pp. 41–58). Open Book Publishers. https://doi.org/10.11647/OBP.0095.03

Weigl, D. M., Janjuš, O., Rosmer, S., de Valk, R., Burghoff, H., Schöning, K., Kyriazis, I., Jaklin, J., Rauber, A., Bürgermeister, M., Steindl, C., & Bischoff, S. (2025). Collaborative workflows for encoding, validating, and publishing a multimodal digital edition. In *Proceedings of the 12th International Conference on Digital Libraries for Musicology (DLfM 2025)*. ACM. https://doi.org/10.1145/3748336.3748349
