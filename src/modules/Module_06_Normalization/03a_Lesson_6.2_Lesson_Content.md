# Lesson 6.2 — Rule-Based Normalization: Regular Expressions in VS Code

*RELS 398 / ENGL 398 · Topic 6: Normalization · Meeting #15 (Wed Oct 7)*

***Step 2 of the three-step cycle: deterministic.** Today you translate yesterday's prose policy and Rule Ledger into formal, automated regular expression patterns. Using the regex engine built directly into Visual Studio Code, you automate spelling regularizations and abbreviation expansions, audit your rules for false positives, and discover where deterministic pattern matching reaches its limits.*

---

## **01 Content**

**From Prose Policy to Deterministic Code**

Yesterday in Lesson 6.1, you performed normalization by hand. You sat with your reconciled diplomatic text in VS Code, examined words one by one, and manually wrapped target spellings and abbreviations in TEI `<choice>` tags. In doing so, you formulated an explicit Editorial Regularization Policy and catalogued your decisions in a Rule Ledger in `NORMALIZATION.md`.

Today, we take the crucial step from manual human execution to automated, deterministic computing. Instead of reading through hundreds of lines and manually typing tags every time an archaic spelling appears, we want a tool to locate every occurrence of our target patterns and apply our transformations systematically.

The transition from a human editorial policy to an automated rule is profound. Prose editorial policies tolerate vagueness. A policy that says "regularize archaic terminal *-ck* on adjectives" seems perfectly clear to a human reader, who instinctively knows that *publick* should become *public*, but *black* should remain *black*. A computer possesses no such historical or linguistic intuition. To a machine, *black* ends in *-ck* just as surely as *publick* does.

Implementing an automated rule therefore acts as an unforgiving audit of your editorial policy. When an automated rule produces a catastrophic mistake—such as turning *black* into *blac* or *track* into *trac*—it exposes an unstated assumption in your human thinking. Deterministic rules force us to state our exact criteria with mathematical precision (Friedl, 2006).

**Vocabulary.** *Deterministic automation* — A computational process that always produces the exact same output when given the same input and rules, without randomness or opacity. *Policy audit* — The process of testing an editorial policy through formal code to uncover unstated ambiguities or edge cases.

**Takeaway:** Translating a human editorial policy into deterministic rules audits your scholarly thinking by exposing unstated assumptions and edge cases.

---

## **02 Content**

**What Is a Regular Expression?**

To automate text normalization deterministically, digital scholars do not need to write thousands of lines of low-level software. Instead, we use one of the most powerful and elegant tools in modern computing: **Regular Expressions** (commonly abbreviated as **regex**).

A regular expression is a formalized pattern-matching language designed to search, match, and transform text based on structural patterns rather than fixed literal words (Jurafsky & Martin, 2024). Instead of searching for the exact literal word *publick*, a regular expression allows you to specify: "find any sequence of letters that begins at a word boundary, ends with the letters *ck*, and is preceded by a specific root."

Regular expressions originated in theoretical computer science and formal language theory in the 1950s, representing finite-state automata that recognize regular languages. Today, regular expression engines are embedded into virtually every programming language, shell utility (like `grep` and `sed`), and modern text editor.

In digital textual editing, regex is the premier tool for deterministic normalization. A single well-crafted regular expression can scan a 500-page historical witness, identify every instance of a 18th-century spelling variant or thorn contraction, and reformat it into valid, multi-element TEI `<choice>` markup in milliseconds.

**Vocabulary.** *Regular expression (regex)* — A specialized formal language consisting of literal characters and metacharacters used to describe search patterns in text. *Pattern matching* — The computational search for sequences of characters that conform to a specified grammatical rule.

**Takeaway:** A regular expression is a concise, formal pattern-matching language that allows digital editors to search and transform text based on structural rules rather than fixed literal strings.

---

## **03 Content**

**The VS Code Regex Engine**

Many novice students assume that running regular expressions requires learning a complex programming language like Python, installing external libraries, and executing command-line scripts. In reality, **Visual Studio Code has a world-class regular expression engine built directly into its editor**.

Whenever you open the Find and Replace widget in VS Code (`Cmd+F` or `Cmd+H` on macOS; `Ctrl+F` or `Ctrl+H` on Windows), you have access to a complete JavaScript/PCRE-compatible regular expression processor. To activate regex mode, you simply click the **Use Regular Expression** icon (which looks like `.*`) in the Find box, or press `Alt+R` (`Option+Cmd+R` on macOS).

Using regex inside VS Code offers a decisive pedagogical advantage over running background scripts: **immediate real-time visual feedback**.

When you write a regex pattern in a Python script and run it over a file, the script executes blindly in memory. If your pattern contains a subtle defect, it will silently corrupt thousands of words before you realize a mistake occurred. In VS Code, as soon as you type a regex pattern into the Find box, the editor instantly highlights every single matching character in yellow across your entire open document. 

You can visually inspect what matches, see what was missed, and immediately detect if your pattern accidentally captures XML tags or milestone markers *before* you execute a single replacement.

**Vocabulary.** *VS Code regex mode* — An interactive editor setting (toggled with `.*` or `Alt+R`) that interprets search strings as regular expressions. *Real-time visual feedback* — The instant editor highlighting of matching text patterns, allowing safe pre-execution inspection.

**Takeaway:** VS Code provides an interactive, full-featured regular expression engine with real-time visual highlighting, making pattern testing visible and safe before execution.

---

## **04 Content**

**Literal Characters vs. Metacharacters**

A regular expression is composed of two distinct types of characters: **literal characters** and **metacharacters** (Friedl, 2006).

A **literal character** is an ordinary alphanumeric symbol that matches only itself. If you type the letter `p`, the regex matches the character `p`. If you type `treaty`, the regex matches the exact sequence `t-r-e-a-t-y`.

A **metacharacter**, by contrast, is a special reserved symbol that carries an operational meaning in the regex grammar. Instead of matching itself literally, a metacharacter instructs the engine to perform a structural test, such as matching any character, repeating a pattern, or anchoring to a boundary.

The fundamental regex metacharacters include:

<ul>
  <li><code>.</code> (Dot): Matches any single character except a newline.</li>
  <li><code>*</code>, <code>+</code>, <code>?</code> (Quantifiers): Control how many times the preceding character or group may repeat.</li>
  <li><code>[</code> and <code>]</code> (Brackets): Define a character class or set.</li>
  <li><code>(</code> and <code>)</code> (Parentheses): Define a capturing group.</li>
  <li><code>^</code> and <code>$</code> (Anchors): Match the beginning and end of a line.</li>
  <li><code>\</code> (Backslash): The escape character, used to neutralize a metacharacter or invoke special escape sequences.</li>
</ul>

If you want to match a literal period (such as the dot in the abbreviation *publ.*), you cannot simply type `.`, because a bare dot matches any letter or space. You must **escape** it with a backslash: `\.`. The backslash tells the regex engine: "treat the following symbol as an ordinary literal character, not as a special command."

**Vocabulary.** *Literal character* — A character that matches only itself in a regex search. *Metacharacter* — A reserved character with special syntactic meaning that controls pattern matching. *Escaping* — Prefixing a metacharacter with a backslash (`\`) to force the engine to match it as a literal symbol.

**Takeaway:** Regular expressions combine literal characters that match themselves with metacharacters that control pattern structure; reserved symbols must be escaped with a backslash to match literally.

---

## **05 Content**

**Character Classes and Sets: `[...]`**

In historical documents, writers frequently substitute vowels or interchangeable consonants. For example, an 18th-century French writer might spell a word with an acute accent, a grave accent, or no accent at all. To match any one of several alternative characters at a specific position, regular expressions provide **character classes**, enclosed in square brackets: `[...]`.

A character class matches **exactly one character** from the set of characters listed inside the brackets:

<ul>
  <li><code>[aeiou]</code>: Matches any single lowercase English vowel.</li>
  <li><code>[ſs]</code>: Matches either a historical long <em>s</em> (<em>ſ</em>) or a standard short <em>s</em>.</li>
  <li><code>[0-9]</code>: Matches any single decimal digit from 0 to 9. (The hyphen indicates an inclusive range).</li>
  <li><code>[a-zA-Z]</code>: Matches any single uppercase or lowercase English letter.</li>
</ul>

Inside a character class, most normal metacharacters lose their special meaning. For example, `[.]` matches a literal period without needing a backslash.

Furthermore, placing a caret (`^`) as the **first character** inside the brackets negates the class, matching any character that is *not* in the set. For digital humanities text editors working in XML, the negated character class `[^<>]` is one of the most vital patterns in existence: it matches any character that is not an opening or closing angle bracket, preventing search patterns from accidentally spilling into XML tags.

**Vocabulary.** *Character class* — A regex pattern enclosed in square brackets `[...]` that matches any single character contained within the set. *Negated character class* — A character class starting with `[^...]` that matches any character *except* those listed.

**Takeaway:** Use character classes `[...]` to match alternative single characters (such as `[ſs]`), and negated classes like `[^<>]` to safely exclude XML markup.

---

## **06 Content**

**Quantifiers: Matching Repetitions (`+`, `*`, `?`)**

Historical words vary not only in which letters appear, but in how many times a letter is repeated. In Maud Lewis's letters, consonants are often doubled phonetically (e.g., *allways*), while scribal flourishes can introduce variable spaces. To control how many times a character or group repeats, regular expressions use **quantifiers**:

<ul>
  <li><code>+</code> (Plus): Matches the preceding element <strong>one or more times</strong>. For example, <code>l+</code> matches <em>l</em>, <em>ll</em>, or <em>lll</em>.</li>
  <li><code>*</code> (Asterisk): Matches the preceding element <strong>zero or more times</strong>. For example, <code>e*</code> matches nothing, or <em>e</em>, or <em>ee</em>.</li>
  <li><code>?</code> (Question Mark): Matches the preceding element <strong>zero or one time</strong> (making it optional). For example, <code>colou?r</code> matches both British <em>colour</em> and American <em>color</em>.</li>
</ul>

A critical concept every digital editor must understand is **greediness**. By default, quantifiers in regular expressions are greedy: they consume as much text as possible.

Consider what happens if you have the XML line `<orig>publick</orig> and <orig>traffick</orig>` and you search with the pattern `<orig>.*</orig>`. You might expect the engine to match the first tag. Instead, because `.*` is greedy, it starts at the first `<orig>`, consumes all the text across the middle of the line, and stops only at the *final* `</orig>`! It swallows both words and the word *and* between them.

To prevent greedy over-matching, you can make a quantifier lazy by appending a question mark (e.g., `.*?`), or even better, use a negated character class: `<orig>[^<]*</orig>`.

**Vocabulary.** *Quantifier* — A regex symbol (`+`, `*`, `?`) specifying how many instances of the preceding character or group must occur. *Greedy matching* — The default regex behavior of consuming the longest possible matching string. *Lazy matching* — A quantifier modified with `?` that consumes the shortest possible matching string.

**Takeaway:** Quantifiers control repetition, but default to greedy matching; use negated classes like `[^<]*` to prevent patterns from swallowing multiple tags across a line.

---

## **07 Content**

**The Inviolable Rule: Word Boundaries (``)**

If there is one metacharacter that every digital humanities editor must memorize, revere, and never forget, it is the **word boundary anchor**: ``.

A word boundary is an anchor: it does not consume any physical characters. Instead, `` asserts a physical position: the boundary between a word character (letters, numbers, underscores) and a non-word character (spaces, punctuation, quotes, or tag brackets) (Friedl, 2006).

Consider what happens if you neglect to use ``. Suppose you want to find the archaic contraction *ye* in an 18th-century document and replace it with *the*. If you search for the bare letters `ye` without word boundaries, look at what gets matched:

<ul>
  <li><em>ye</em> in <em>ye Governor</em> (Correct match)</li>
  <li><em>ye</em> inside <em>yesterday</em> $	o$ becomes <em>thesturday</em>!</li>
  <li><em>ye</em> inside <em>eye</em> $	o$ becomes <em>ethe</em>!</li>
  <li><em>ye</em> inside <em>lawyer</em> $	o$ becomes <em>lawther</em>!</li>
  <li><em>ye</em> inside <em>bye</em> $	o$ becomes <em>bthe</em>!</li>
</ul>

Searching for unanchored strings will violently dismantle your text. If you search for *in*, you will replace the middle of *point*, *prince*, and *administrative*. 

By wrapping your target in word boundaries—`ye`—you instruct the regex engine to match the letters *y* and *e* **only when they exist as a standalone, isolated word**, surrounded by spaces or punctuation. In textual normalization, **never search for a word without `` anchors**.

**Vocabulary.** *Word boundary (``)* — A zero-width anchor that matches the boundary between a word character and a non-word character (such as whitespace or punctuation). *Substring corruption* — The disastrous accidental replacement of letters inside unrelated longer words caused by omitting word boundaries.

**Takeaway:** Always enclose word patterns in word boundary anchors (`pattern`) to prevent catastrophic accidental replacements inside longer words.

---

## **08 Content**

**Capturing Groups: The Power of Parentheses `(...)`**

Searching for text is only half the battle. In digital editing, we do not merely want to find words; we want to restructure them. We want to take an original word, capture its root stem, and wrap it inside TEI tags. To achieve this, regular expressions use **capturing groups**, defined by parentheses: `(...)`.

When you enclose part of a regex pattern in parentheses, the regex engine performs two actions:
<ol>
  <li>It groups the enclosed characters into a single logical unit.</li>
  <li>It saves whichever specific text matched inside those parentheses into an internal memory slot (a register).</li>
</ol>

Capturing groups are numbered automatically from left to right based on the order of their opening parentheses: Group 1, Group 2, Group 3, and so on (Jurafsky & Martin, 2024).

For example, consider the pattern:

```regex
(\w+)ck
```

Here, `\w+` matches one or more word characters (letters). Because `\w+` is enclosed in parentheses, it forms **Group 1**. The trailing letters `ck` sit outside the parentheses.

When this pattern encounters the word *publick*, the entire pattern matches the full word *publick*. But inside memory, **Group 1 captures solely the root stem: *public***. When the pattern encounters *authentick*, Group 1 captures *authenti*. 

Capturing groups allow you to isolate the variable parts of a word so you can reuse them dynamically during replacement.

**Vocabulary.** *Capturing group* — A sub-pattern enclosed in parentheses `(...)` whose matched content is stored in memory for retrieval during replacement. *Group numbering* — The sequential assignment of matched groups (`$1`, `$2`) ordered by their opening parentheses from left to right.

**Takeaway:** Enclose sub-patterns in parentheses to create capturing groups that store matched word stems in memory for dynamic reuse.

---

## **09 Content**

**Backreferences in the Replace Box: `$1` and `$2`**

Once a regular expression captures text into a group, how do you insert that captured text into your replacement string? In VS Code, you retrieve captured groups using **backreferences**: `$1`, `$2`, `$3`, and so on.

When you type `$1` in the VS Code Replace box, the editor replaces that token with whichever characters were matched by the first capturing group. If your pattern has a second group, `$2` retrieves the second group. The special token `$0` represents the *entire* matched string.

Let us see how capturing groups and backreferences work together in a simple example:

```text
Find:    (\w+)ck
Replace: $1c
```

Let us trace how the engine processes this command on the word *publick*:
<ol>
  <li>The search pattern matches the full word <code>publick</code>.</li>
  <li>Group 1 captures the stem: <code>public</code>.</li>
  <li>The Replace field instructs the editor: insert the text of Group 1 (<code>public</code>), followed by the literal letter <code>c</code>.</li>
  <li>Result: <code>publicc</code> (Notice the spelling error! If the stem was <em>public</em>, adding <em>c</em> produced two <em>c</em>'s!).</li>
</ol>

This simple trace illustrates why precision is vital. If our root stem already ends in *c*, we do not want to add *c*; we simply want to drop the *k*! The correct pattern would be:

```text
Find:    (\w+c)k
Replace: $1
```

Here, Group 1 captures *public* (including the *c*). The replace token `$1` outputs *public*, cleanly dropping the terminal *k*.

**Vocabulary.** *Backreference* — A special replacement syntax (such as `$1` or `$2`) that outputs the text stored by a specific capturing group. *Replacement token* — A placeholder in the replacement field that dynamically references captured search data.

**Takeaway:** In the VS Code Replace box, use `$1`, `$2`, etc., to output the exact text captured by your search parentheses, dynamically reconstructing your words.

---

## **10 Content**

**Generating TEI `<choice>` Dynamically in VS Code**

Now we arrive at the central technique of automated digital normalization. By combining capturing groups with literal XML tags in the VS Code Replace box, we can **generate complete, validated TEI `<choice>` structures automatically**.

Recall our manual encoding goal from yesterday: we want to transform historical *publick* into:

```xml
<choice><orig>publick</orig><reg resp="#editor">public</reg></choice>
```

Typing that entire block by hand took thirty seconds. With regular expressions in VS Code, we can generate it in one keystroke across all occurrences:

```text
Find:    (\w+c)k
Replace: <choice><orig>$1k</orig><reg resp="#editor">$1</reg></choice>
```

Let us trace what VS Code does when it executes this command on *publick*:
<ol>
  <li>The Find pattern matches <code>publick</code>.</li>
  <li>Group 1 captures the stem <code>public</code> into <code>$1</code>.</li>
  <li>The Replace box outputs:
    <ul>
      <li>Literal XML: <code>&lt;choice&gt;&lt;orig&gt;</code></li>
      <li><code>$1k</code> $	o$ inserts <code>public</code> followed by literal <code>k</code> (reproducing the original word <code>publick</code>!).</li>
      <li>Literal XML: <code>&lt;/orig&gt;&lt;reg resp="#editor"&gt;</code></li>
      <li><code>$1</code> $	o$ inserts the regularized stem <code>public</code>.</li>
      <li>Literal XML: <code>&lt;/reg&gt;&lt;/choice&gt;</code></li>
    </ul>
  </li>
</ol>

The resulting text is perfect, fully formed, valid TEI markup. The editor did not need to write a Python script; the regex engine in VS Code constructed the entire multi-element parallel XML structure dynamically.

**Vocabulary.** *Dynamic XML generation* — Using regex replacement backreferences to construct complex structural markup around captured text strings. *Markup automation* — Automating the insertion of repetitive tagging structures while preserving original witness readings.

**Takeaway:** Combine captured stems with literal XML tags in the VS Code Replace box to generate complete, validated TEI `<choice>` blocks instantly.

---

## **11 Content**

**Case Sensitivity and Case Preservation in VS Code**

Historical documents constantly alternate between uppercase and lowercase letters. An 18th-century text might print *Publick* with a capital *P* at the start of a sentence and *publick* with a lowercase *p* in the middle of a line.

How does regular expression matching handle capitalization? In VS Code, case sensitivity is controlled by two dedicated toggles in the Find and Replace widget:

<ol>
  <li><strong>Match Case (`Alt+C`):</strong> When this toggle is active, the search is strictly case-sensitive. Searching for <code>publick</code> will ignore <code>Publick</code>. When inactive, the search matches both.</li>
  <li><strong>Preserve Case:</strong> In the Replace box, VS Code features an extraordinary built-in button labeled <strong>Preserve Case</strong> (an icon showing uppercase and lowercase <code>AB</code>). When active, VS Code automatically matches the capitalization style of the replacement string to the matched text! If the search matches lowercase <code>publick</code>, it outputs lowercase <code>public</code>; if it matches capitalized <code>Publick</code>, it outputs capitalized <code>Public</code>!</li>
</ol>

Alternatively, you can handle casing explicitly within your regex pattern using character classes:

```regex
([Pp]ublic)k
```

Here, Group 1 captures either *Public* or *public*, preserving the exact initial casing inside `$1` when output into `<orig>` and `<reg>`.

Understanding casing prevents duplicate rules. Rather than writing one rule for lowercase words and a second rule for capitalized words, a single case-aware pattern handles both cleanly.

**Vocabulary.** *Match Case* — A toggle (`Alt+C`) enforcing strict character casing during regex search. *Preserve Case* — A VS Code feature that automatically adapts replacement text capitalization to match the original source word.

**Takeaway:** Use the Match Case and Preserve Case toggles in VS Code, or case-insensitive character classes like `[Pp]`, to handle capitalized and lowercase variants within a single rule.

---

## **12 Content**

**Rule 1 in Practice: 18th-Century Terminal `-ck`**

Now let us apply these principles to our first real historical case study: 18th-century adjectives ending in *-ck* (from the 1752 Treaty and colonial legal records).

Suppose we begin with a simple pattern:

```text
Find:    (\w+)ck
Replace: <choice><orig>$1ck</orig><reg resp="#editor">$1c</reg></choice>
```

Let us test this rule against a realistic sample sentence from an 18th-century colonial document:

```text
"The publick traffick of black cattle shall be conducted by a politick truck."
```

If you click "Replace All" in VS Code with that simple pattern, look at the disaster that occurs:
<ul>
  <li><em>publick</em> $	o$ correctly regularized to <em>public</em>.</li>
  <li><em>traffick</em> $	o$ correctly regularized to <em>traffic</em>.</li>
  <li><em>black</em> $	o$ transformed to <em>blac</em>! (Fatal error: <em>black</em> is a modern standard word!).</li>
  <li><em>politick</em> $	o$ correctly regularized to <em>politic</em>.</li>
  <li><em>truck</em> $	o$ transformed to <em>truc</em>! (Fatal error: <em>truck</em> is a modern standard word!).</li>
</ul>

This test demonstrates the fundamental danger of naive regular expressions: **over-matching**. Our rule was too broad. It assumed that *every* word ending in *-ck* was an archaic 18th-century variant, forgetting that English has dozens of native Germanic words (*back*, *black*, *thick*, *quick*, *truck*, *lock*, *duck*) where *-ck* is standard orthography!

A rule that fixes three words while corrupting two others is unacceptable in scholarship. We must refine our rule.

**Vocabulary.** *Over-matching* — When a regex pattern is too general, capturing unintended words and producing erroneous replacements. *Naive pattern* — A simplistic pattern that fails to account for linguistic exceptions or homographs.

**Takeaway:** Naive regular expressions over-match; always test patterns against diverse sentences to ensure they do not corrupt standard modern vocabulary like *black* or *truck*.

---

## **13 Content**

**Refining Regex Rules: Stems and Root Whitelists**

How do we refine Rule 1 so that it regularizes *publick* and *traffick* without touching *black* or *truck*?

In regular expressions, when a broad phonetic or morphological pattern has numerous common exceptions, the solution is to use **alternation** (`|`) to restrict the pattern to an explicit list of known historical roots (Friedl, 2006).

Instead of matching any arbitrary word characters with `\w+`, we specify the exact root stems that historically underwent the *-ck* to *-c* spelling reform:

```text
Find:    (authenti|criti|fantasti|musick|politi|publi|traffi)ck
```

Notice what this refined pattern does:
<ol>
  <li>The parentheses group an explicit whitelist of historical Latin and Greek stems that ended in <em>-ck</em> in 18th-century English.</li>
  <li>The pipe symbol (<code>|</code>) functions as a logical OR. The engine matches <em>authenti</em> OR <em>criti</em> OR <em>publi</em>, etc.</li>
  <li>It requires the matched root to be immediately followed by literal <code>ck</code> and a word boundary.</li>
</ol>

Now let us write the replacement pattern:

```text
Replace: <choice><orig>$1ck</orig><reg resp="#editor">$1c</reg></choice>
```

When this refined rule scans our test sentence:
<ul>
  <li><em>publick</em> matches $	o$ regularized to <em>public</em>.</li>
  <li><em>traffick</em> matches $	o$ regularized to <em>traffic</em>.</li>
  <li><em>black</em>: the stem <em>bla</em> is not in our whitelist $	o$ ignored completely!</li>
  <li><em>truck</em>: the stem <em>tru</em> is not in our whitelist $	o$ ignored completely!</li>
</ul>

By constraining the search with root alternation, our rule achieves **100% precision**. It transforms every legitimate target and touches zero innocent words.

**Vocabulary.** *Alternation (`|`)* — A regex operator functioning as a logical OR, matching either the pattern on its left or its right. *Root whitelisting* — Restricting a regex pattern to an explicit enumeration of validated historical stems to prevent false positives.

**Takeaway:** Use alternation `(stem1|stem2|stem3)` to restrict normalization rules to validated historical roots, eliminating false positive errors.

---

## **14 Content**

**Rule 2 in Practice: The Long s (`ſ`)**

Our second historical rule addresses the typographical **long s** (Unicode `ſ` / `U+017F`), ubiquitous in printed books and broadsides prior to roughly 1800.

In the 1752 Treaty, the long *s* is used for lowercase *s* at the beginning and in the middle of words, while the round *s* is used at the end (e.g., *ſaid*, *firſt*, *witneſses*).

How should an editor handle the long *s* with regular expressions?

First, you must consult your **Editorial Policy**:
<ul>
  <li><strong>Policy Option A (Global Graphemic Modernization):</strong> Many modern digital editions consider the long <em>s</em> to be a purely typographical font feature (like a ligature or font variant) rather than a spelling variation. Under this policy, you simply replace all instances of <code>ſ</code> with modern <code>s</code> globally across the text.
    <pre><code>Find:    ſ
Replace: s</code></pre>
  </li>
  <li><strong>Policy Option B (Full TEI Parallel Tracking):</strong> If your edition is a strict paleographical study documenting 18th-century typographical habits, you may choose to record every long <em>s</em> inside a <code>&lt;choice&gt;</code> block:
    <pre><code>Find:    (\w*)ſ(\w*)
Replace: &lt;choice&gt;&lt;orig&gt;$1ſ$2&lt;/orig&gt;&lt;reg resp="#editor"&gt;$1s$2&lt;/reg&gt;&lt;/choice&gt;</code></pre>
  </li>
</ul>

Notice that Option B wraps the entire word containing the long *s* into `<choice>`. If a word contains two long *s*'s (like *witneſses*), running a single-letter regex requires care so you do not nest `<choice>` tags inside `<choice>` tags. For most undergraduate projects, Option A (or replacing `ſ` before line-level normalization) is standard practice.

**Vocabulary.** *Typographical regularization* — Standardizing archaic letterforms (such as long *s*) that represent font conventions rather than distinct lexical spellings. *Character-level vs. word-level* — Choosing whether to tag individual letters or wrap the entire containing word in TEI markup.

**Takeaway:** The long *s* (`ſ`) can be regularized globally as a typographical feature or wrapped at word level in `<choice>`, depending on your stated editorial policy.

---

## **15 Content**

**Rule 3 in Practice: Thorn Contractions (`ye` and `yt`)**

Our third rule automates the expansion of early modern scribal contractions in colonial documents, specifically the thorn abbreviations *y<hi rend="superscript">e</hi>* (*the*) and *y<hi rend="superscript">t</hi>* (*that*).

In your diplomatic transcription from Week 4, you may have transcribed these words either as plain text (*ye*, *yt*) or with superscript tags (*y<sup>e</sup>* or `y<hi rend="superscript">e</hi>`).

Let us build a regex rule to handle plain text *ye* first:

```text
Find:    ([Yy])e
Replace: <choice><abbr>$1e</abbr><expan resp="#editor">$1he</expan></choice>
```

Let us trace this rule:
<ol>
  <li><code>([Yy])e</code> matches standalone <em>ye</em> or <em>Ye</em>. Group 1 captures the initial casing.</li>
  <li>If the document had capitalized <em>Ye</em>, Group 1 captures <em>Y</em>, and the replacement outputs <code>&lt;abbr&gt;Ye&lt;/abbr&gt;&lt;expan resp="#editor"&gt;The&lt;/expan&gt;</code>! (Notice that <code>$1he</code> capitalizes the <em>T</em> automatically!).</li>
</ol>

Now, what if your transcription already contains superscript tags, such as `y<hi rend="superscript">e</hi>`?

```text
Find:    ([Yy])<hi rend="superscript">e</hi>
Replace: <choice><abbr>$1<hi rend="superscript">e</hi></abbr><expan resp="#editor">$1he</expan></choice>
```

Because the tag `<hi rend="superscript">e</hi>` is literal XML, we include it directly in our search pattern. The regex matches the letter *y* followed immediately by the superscript tag, wrapping the entire historical graphic unit into `<abbr>` and supplying the expanded modern word in `<expan>`.

**Vocabulary.** *Thorn pattern* — A regex designed to identify pseudo-archaic *y*-abbreviations and map them to standard *th*-words. *Superscript matching* — Matching embedded XML formatting tags as part of an abbreviation search string.

**Takeaway:** Use capturing groups on initial letters (`[Yy]`) to preserve capitalization when expanding historical thorn contractions like *ye* into *the*.

---

## **16 Content**

**Rule 4 in Practice: Early French Verb Endings (`-oit` and `-oient`)**

Now let us turn to our French Revolutionary decree (Ace's project). In 1791 French official printing, the imperfect indicative and conditional verb endings are systematically printed with *oi* instead of modern *ai*:

<ul>
  <li>3rd-person singular: <em>-oit</em> (modern <em>-ait</em>), as in <em>étoit</em> $	o$ <em>était</em>, <em>dérogeoit</em> $	o$ <em>dérogeait</em>.</li>
  <li>3rd-person plural: <em>-oient</em> (modern <em>-aient</em>), as in <em>étoient</em> $	o$ <em>étaient</em>, <em>faisoient</em> $	o$ <em>faisaient</em>.</li>
</ul>

Can we automate this transformation in VS Code? Yes! We write two clean, targeted rules:

```text
Rule 4a (Singular Imperfect):
Find:    (\w+)oit
Replace: <choice><orig>$1oit</orig><reg resp="#editor">$1ait</reg></choice>

Rule 4b (Plural Imperfect):
Find:    (\w+)oient
Replace: <choice><orig>$1oient</orig><reg resp="#editor">$1aient</reg></choice>
```

Notice what happens during execution:
<ol>
  <li>Rule 4a matches <em>étoit</em>. Group 1 captures the verbal root <code>ét</code>.</li>
  <li>The Replace field reconstructs the original word in <code>&lt;orig&gt;$1oit&lt;/orig&gt;</code> and supplies the modern spelling in <code>&lt;reg resp="#editor"&gt;$1ait&lt;/reg&gt;</code>.</li>
  <li>Result: <code>&lt;choice&gt;&lt;orig&gt;étoit&lt;/orig&gt;&lt;reg resp="#editor"&gt;était&lt;/reg&gt;&lt;/choice&gt;</code>.</li>
</ol>

What about nouns or adjectives ending in *-oit*, such as *droit* (law/right) or *étroit* (narrow)?
If we ran a naive `(\w+)oit`, would *droit* become *drait*? 
**YES!** In modern French, *droit* is still spelled *droit*!

This demonstrates why Rule Ordering and Whitelisting matter. In French, nouns like *droit* must either be excluded using negative lookaheads or verb stems must be explicitly whitelisted. Testing in VS Code reveals this immediately!

**Vocabulary.** *Voltairean verb rule* — A regex automating the historical French orthographic shift from *oi* to *ai* in verb conjugations. *Grammatical homograph* — Words sharing a terminal spelling where some are verbs requiring regularization and others are invariant nouns (like *droit*).

**Takeaway:** Automating French *-oit* to *-ait* regularizes imperfect verbs, but editors must protect invariant nouns like *droit* from accidental corruption.

---

## **17 Content**

**Rule 5 in Practice: Maud Lewis Phonetic Doubling**

Now let us examine vernacular English correspondence (Olyvia's Maud Lewis project). In personal letters, writers frequently double consonants phonetically, writing *allways* for *always*, *untill* for *until*, or *truely* for *truly*.

Unlike colonial treaties, vernacular personal letters do not follow an official government printing style. Their spelling reflects individual acoustic habits. Therefore, building broad morphological rules (like "reduce all double *l*'s") is completely impossible, because words like *ball*, *call*, and *yellow* require double *l*'s!

For vernacular writing, the correct deterministic strategy is **explicit vocabulary alternation**:

```text
Find:    ([Aa])llways
Replace: <choice><orig>$1llways</orig><reg resp="#editor">$1lways</reg></choice>
```

```text
Find:    ([Uu])ntill
Replace: <choice><orig>$1ntill</orig><reg resp="#editor">$1ntil</reg></choice>
```

```text
Find:    ([Tt])ruely
Replace: <choice><orig>$1ruely</orig><reg resp="#editor">$1ruly</reg></choice>
```

Notice how clean and safe these rules are:
<ul>
  <li>Each rule targets an exact, known phonetic quirk identified during your close reading in Step 1.</li>
  <li>Word boundaries (<code></code>) ensure that the rule matches only the complete standalone word.</li>
  <li>Initial character classes (<code>[Aa]</code>, <code>[Uu]</code>) preserve capitalization whether the word opens a sentence or sits mid-line.</li>
  <li>The rule cannot possibly produce false positives on unrelated words.</li>
</ul>

In digital editing, a set of five precise, explicit rules is infinitely superior to one clever, complex rule that corrupts words you never intended to touch.

**Vocabulary.** *Explicit vocabulary rule* — A regex targeting specific, pre-identified variant words rather than broad grammatical patterns. *Vernacular targeting* — Adapting regex precision to the individualized phonetic habits of personal correspondence.

**Takeaway:** For vernacular correspondence, use targeted explicit word rules rather than broad morphological patterns to eliminate false positives.

---

## **18 Content**

**Rule 6 in Practice: Unpunctuated Contractions**

In vernacular writing and informal manuscripts, authors frequently omit the apostrophe in common negative contractions, writing *dont*, *cant*, *wont*, and *didnt*.

Can we write a regular expression to add the missing apostrophe inside a TEI `<choice>` block?

Let us test a pattern in VS Code:

```text
Find:    ([Dd])ont
Replace: <choice><orig>$1ont</orig><reg resp="#editor">$1on't</reg></choice>
```

```text
Find:    ([Cc])ant
Replace: <choice><orig>$1ant</orig><reg resp="#editor">$1an't</reg></choice>
```

These rules work beautifully for *dont* and *cant*. But now consider the word **wont**:

```text
Find:    ([Ww])ont
Replace: <choice><orig>$1ont</orig><reg resp="#editor">$1on't</reg></choice>
```

In English, **wont** is an authentic dictionary word! It is an archaic noun and adjective meaning "accustomed, habit, or custom" (as in "as was his wont", or "he was wont to rise early").

If a 19th-century author or colonial writer writes "according to his wont", and your regex blindly replaces it with *won't* (will not), you have introduced a catastrophic semantic blunder into your text!

This is why regular expressions cannot be trusted blindly. An automated tool matches character strings, not meaning. In Section 21, we will see how VS Code's "Find Next" stepping protects you from this exact homograph trap.

**Vocabulary.** *Lexical homograph trap* — When an unpunctuated contraction (like *wont*) is identical in spelling to a valid, unrelated word (like *wont* = custom), risking false-positive replacement.

**Takeaway:** Unpunctuated contractions like *dont* can be regularized with regex, but homographs like *wont* require human contextual verification.

---

## **19 Content**

**The Golden Rule of XML-Safe Regex**

When working in TEI, you are not editing raw plain text. You are editing text **already embedded inside an XML markup tree**.

This structural reality introduces a severe hazard that destroys hundreds of student files every semester: **regex patterns that accidentally match XML tags**.

Consider what happens if you write a search pattern using a bare dot: `.*`. Remember that a dot matches *any* character, including `<` and `>`. If you search for:

```regex
(in).*
```

The dot can match directly across an XML tag! It might match the *in* in `<div type="section">`, swallow the attribute, cross the closing bracket, and match into the text! If you hit replace, you will tear open the XML tag, corrupting the document hierarchy and causing immediate schema validation failure.

To prevent this catastrophe, memorize and follow **The Golden Rule of XML-Safe Regex**:

<table style="width: 100%; border-collapse: collapse; margin-top: 1rem; margin-bottom: 1rem;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1; text-align: left;">
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Rule</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Dangerous Pattern</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">XML-Safe Pattern</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Why It Protects You</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><strong>1. Restrict Wildcards</strong></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>.*</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>[^&lt;&gt;]*</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Refuses to match angle brackets; stays strictly inside text nodes.</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><strong>2. Use Word Characters</strong></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>.+</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>\w+</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Matches only letters and digits; stops instantly at punctuation and tags.</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><strong>3. Anchor Boundaries</strong></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>ye</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>ye</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Prevents matching attributes like <code>type="poem"</code>.</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *XML-safe regex* — A regular expression specifically constrained to prevent matching or corrupting XML element tags, attribute quotes, or bracket delimiters. *Tag corruption* — The accidental mutilation of XML syntax caused by unconstrained regex wildcards.

**Takeaway:** Never use unconstrained wildcards (`.*`) in XML; use `\w+` or `[^<>]*` to ensure your search patterns stay strictly confined within text nodes.

---

## **20 Content**

**Milestones and Line Breaks: Protecting `<lb/>`**

In Lesson 6.1, we established that when a word is divided across a line break, the physical milestone `<lb/>` must reside inside the `<orig>` element:

```xml
<choice>
  <orig>Gov-<lb n="13"/>ernor</orig>
  <reg resp="#editor">Governor</reg>
</choice>
```

Now ask yourself: what happens if you run an automated regular expression search for the word *Governor* across that line?

```regex
Governor
```

Will it match? **NO!** 

To the regular expression engine, the characters on the page are `Gov-<lb n="13"/>ernor`. The letters *G-o-v* are immediately followed by a hyphen and an angle bracket `<`. Because an angle bracket is a non-word character, `` asserts a boundary, and the search fails to find *Governor*.

Furthermore, what if you write a regex to regularize hyphenated words:

```regex
(\w+)-<lb n="\d+"/>(\w+)
```

This pattern will successfully match the hyphenated split! And you can write a replacement that wraps it cleanly into TEI:

```text
Replace: <choice><orig>$1-<lb n="13"/>$2</orig><reg resp="#editor">$1$2</reg></choice>
```

However, because line numbers vary on every line, hardcoding line numbers in regex replacement is complex. For hyphenated words split across line breaks, **it is almost always safer and faster to regularize them by hand** during Step 1, using automated regex only for words that sit completely within a single typographic line.

**Vocabulary.** *Milestone collision* — The failure of a regex pattern to match a word because an empty XML milestone (like `<lb/>`) interrupts the character sequence. *Hyphenated split* — A word broken across two lines by a hyphen and an `<lb/>` element.

**Takeaway:** Words split across lines by `<lb/>` tags will not match standard single-word regex patterns; handle split words manually in Step 1.

---

## **21 Content**

**Interactive Step-and-Replace vs. Blind "Replace All"**

In the VS Code Replace widget, there are two replacement buttons:
<ol>
  <li><strong>Replace (`Enter` or `Cmd+Alt+Enter`):</strong> Replaces the single currently highlighted match and advances the cursor to the next match.</li>
  <li><strong>Replace All (`Cmd+Option+Enter` or `Ctrl+Alt+Enter`):</strong> Replaces every match in the entire document instantly in a single unmonitored pass.</li>
</ol>

To novice editors, "Replace All" feels like magic. You press one button, and fifty words are instantly regularized.

In professional textual editing, **blind "Replace All" is the single greatest cause of corrupted editions**.

When you click "Replace All", you surrender your human eyes. You assume that your regex pattern is mathematically perfect, that it has zero false positives, that no homographs exist in the document, and that no XML attributes happen to share the same letters. If your rule contains a subtle flaw, "Replace All" multiplies that flaw across fifty lines in a microsecond.

Instead, professional digital editors practice **Interactive Step-and-Replace**:

<ul>
  <li>Press <code>Enter</code> to jump to Match 1. Look at it. Confirm that it is a genuine target word, not a homograph or tag.</li>
  <li>Click <code>Replace</code>. Watch the replacement happen. Verify that the newly inserted <code>&lt;choice&gt;</code> block looks syntactically valid.</li>
  <li>Press <code>Enter</code> to advance to Match 2. Repeat.</li>
  <li>Only after you have stepped through 5 or 6 matches and verified with 100% certainty that your rule is performing flawlessly should you ever consider clicking "Replace All" for the remainder of that specific rule.</li>
</ul>

**Vocabulary.** *Interactive Step-and-Replace* — The disciplined editorial practice of visually inspecting each regex match before confirming replacement. *Blind replacement* — Executing a global "Replace All" command without inspecting individual matches, risking silent textual corruption.

**Takeaway:** Always use Interactive Step-and-Replace to inspect matches individually; never execute blind "Replace All" without prior visual verification.

---

## **22 Content**

**Measuring Rule Quality: True Positives vs. False Positives**

In computational linguistics and information retrieval, the quality of an automated rule is measured using four fundamental diagnostic categories (Jurafsky & Martin, 2024):

<ol>
  <li><strong>True Positive (TP):</strong> The rule matches a word that legitimately required normalization, and transforms it correctly (e.g., matching <em>publick</em> and regularizing it to <em>public</em>).</li>
  <li><strong>False Positive (FP):</strong> The rule matches a word that should NOT have been touched, and corrupts it (e.g., matching <em>black</em> and changing it to <em>blac</em>, or matching <em>wont</em> and changing it to <em>won't</em>). In digital editing, a False Positive is an editorial disaster.</li>
  <li><strong>False Negative (FN):</strong> The rule misses a word that legitimately required normalization, leaving it unregularized (e.g., failing to match <em>politick</em> because of an unexpected capital letter).</li>
  <li><strong>True Negative (TN):</strong> The rule correctly ignores words that did not require normalization (e.g., correctly skipping words like <em>peace</em>, <em>governor</em>, and <em>the</em>).</li>
</ol>

Every time you test a regular expression on your 20-line workshop passage, you must count these outcomes:

```text
TP = Legitimate targets correctly regularized
FP = Innocent words corrupted by the rule
FN = Legitimate targets missed by the rule
```

If your rule produces even a single False Positive ($FP > 0$), the rule is broken. You must stop, analyze the match, and refine your regex pattern before proceeding.

**Vocabulary.** *True Positive (TP)* — A legitimate target correctly identified and transformed by a rule. *False Positive (FP)* — An innocent word wrongly matched and transformed by a rule (a commission error). *False Negative (FN)* — A legitimate target overlooked by a rule (an omission error).

**Takeaway:** Evaluate every regex rule by tracking True Positives (successes), False Positives (disastrous over-matches), and False Negatives (missed targets).

---

## **23 Content**

**Precision and Recall in Digital Editing**

To quantify the performance of your regular expressions mathematically, digital textual scholarship borrows two core metrics from data science: **Precision** and **Recall** (Bollmann, 2019).

**Precision** measures how accurate your rule is when it takes an action. It answers the question: *Of all the words this rule matched and transformed, what percentage was actually correct?*

$$	ext{Precision} = rac{	ext{True Positives}}{	ext{True Positives} + 	ext{False Positives}}$$

If your rule transforms 10 words, and 9 were genuine archaic spellings while 1 was a modern word corrupted by accident, your precision is:

$$	ext{Precision} = rac{9}{9 + 1} = 0.90 	ext{ (90\%)}$$

**Recall** measures the completeness of your rule. It answers the question: *Of all the archaic words that existed in the text, what percentage did your rule successfully find?*

$$	ext{Recall} = rac{	ext{True Positives}}{	ext{True Positives} + 	ext{False Negatives}}$$

If there were 12 archaic words in your document, and your rule found 9 of them while missing 3, your recall is:

$$	ext{Recall} = rac{9}{9 + 3} = 0.75 	ext{ (75\%)}$$

In scholarly editing, **Precision always outranks Recall**. A rule with 100% precision and 75% recall is completely acceptable: it safely normalizes 9 words and leaves 3 for manual review. But a rule with 100% recall and 70% precision corrupts your text with false positives! Strive for 100% precision in every rule you write.

**Vocabulary.** *Precision* — The proportion of matched instances that were genuine, correct targets ($TP / [TP + FP]$). *Recall* — The proportion of all actual targets in the text that were successfully retrieved by the rule ($TP / [TP + FN]$). *Scholarly precision priority* — The editorial principle that avoiding false positives is far more important than achieving total recall.

**Takeaway:** In digital editing, precision must always outrank recall: it is far better to miss a variant for manual review than to corrupt a single word with a false positive.

---

## **24 Content**

**Auditing Rules against Yesterday's Manual Ground Truth**

How do you know what your True Positives, False Positives, and False Negatives actually are? You discover them by **auditing your automated regex output against yesterday's manual ground truth**.

Yesterday in Step 1, you hand-encoded your 20-line passage into `transcription_reconciled_manual.xml`. Every tag in that file was placed with verified human scholarly judgment.

Today in Step 2, you create a duplicate file: `transcription_reconciled_regex.xml`. You run your VS Code regular expressions across this second file.

Now, open both files side by side in Visual Studio Code:
<ol>
  <li>Right-click on `transcription_reconciled_manual.xml` in the Explorer panel and select <strong>Select for Compare</strong>.</li>
  <li>Right-click on `transcription_reconciled_regex.xml` and select <strong>Compare with Selected</strong>.</li>
</ol>

VS Code opens a side-by-side **Diff Editor**:
<ul>
  <li>Where the two files match identically in green: your regex rule matched your manual ground truth perfectly (<strong>True Positive</strong>).</li>
  <li>Where your regex file changed a word that your manual ground truth left alone: you have caught a <strong>False Positive</strong>!</li>
  <li>Where your manual ground truth has a <code>&lt;choice&gt;</code> block that your regex file missed: you have caught a <strong>False Negative</strong>!</li>
</ul>

This visual diff transforms proofreading into an exact science. You do not have to guess whether your regex worked; the diff highlights every discrepancy with surgical precision.

**Vocabulary.** *Side-by-side diff* — A comparative editor interface displaying two versions of a file side by side, highlighting additions, deletions, and character discrepancies in color. *Ground truth audit* — Evaluating automated script or regex outputs by measuring their exact divergence from a hand-verified baseline.

**Takeaway:** Use VS Code's side-by-side diff editor to compare your regex output against your manual ground truth, visually exposing every false positive and false negative.

---

## **25 Content**

**Documenting Regex Patterns in the Rule Ledger**

In Workshop 6, your regular expression rules must be documented with complete scholarly transparency. A rule that lives only in your personal editor history is not reproducible research.

Open your `NORMALIZATION.md` file from yesterday. You will now expand your Editorial Rule Ledger by adding two new technical columns: **Regex Search Pattern** and **Regex Replacement String**:

<table style="width: 100%; border-collapse: collapse; margin-top: 1rem; margin-bottom: 1rem;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1; text-align: left;">
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Rule ID</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Description</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Regex Search Pattern</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Regex Replacement String</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Observed FP / Limitations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>R-01</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Archaic terminal <em>-ck</em></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>(publi|traffi)ck</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>&lt;choice&gt;&lt;orig&gt;$1ck&lt;/orig&gt;&lt;reg resp="#editor"&gt;$1c&lt;/reg&gt;&lt;/choice&gt;</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">0 FP; restricted to root whitelist to avoid <em>black</em>.</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>R-02</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Thorn contraction <em>ye</em></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>([Yy])e</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>&lt;choice&gt;&lt;abbr&gt;$1e&lt;/abbr&gt;&lt;expan resp="#editor"&gt;$1he&lt;/expan&gt;&lt;/choice&gt;</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">0 FP; inspected manually to ensure not modern pronoun.</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>R-03</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Maud Lewis <em>allways</em></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>([Aa])llways</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>&lt;choice&gt;&lt;orig&gt;$1llways&lt;/orig&gt;&lt;reg resp="#editor"&gt;$1lways&lt;/reg&gt;&lt;/choice&gt;</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">0 FP; 100% precision on target personal hand.</td>
    </tr>
  </tbody>
</table>

Documenting your exact search and replacement strings guarantees that any external evaluator can verify your rules, replicate your results, and test your code against new folios.

**Vocabulary.** *Reproducible research* — The scientific standard requiring scholars to publish the exact data, rules, and computational parameters used to generate their findings. *Documented ledger* — A formal record pairing scholarly rationales with executable technical code.

**Takeaway:** Record your exact regex search and replacement patterns in `NORMALIZATION.md`, documenting their observed precision and edge cases.

---

## **26 Content**

**The Scaffolded Bridge: What Is Python `re`?**

Now that you have mastered regular expressions inside VS Code, you possess an invaluable secret: **you already understand the core engine behind automated text processing in Python**.

Students often fear programming because they imagine that writing Python requires learning an entirely alien way of thinking. But in Python, regular expressions are handled by a standard library module named `re`. 

And here is the crucial realization: **the syntax of regular expressions in Python is identical to the syntax in VS Code**.

The character classes `[...]`, the quantifiers `+` and `*`, the word boundaries ``, the capturing groups `()`, and the root alternations `(a|b)` that you tested in VS Code operate with the exact same mathematical logic in Python!

The only difference is how the engine is invoked. In VS Code, you press `Cmd+F` and click `Replace`. In Python, you write a single function call:

```python
import re

new_text = re.sub(pattern, replacement, original_text)
```

The function `re.sub()` stands for "substitute". It takes your regex pattern, takes your replacement string, scans the text, and returns the transformed document. Python is simply an automated container for the exact regular expressions you have already mastered.

**Vocabulary.** *Python `re` module* — The built-in Python library providing regular expression pattern matching and string substitution functions. *`re.sub()`* — The Python function that searches a string for a regex pattern and replaces matches with a specified replacement string.

**Takeaway:** Python's `re.sub()` uses the exact same regular expression syntax as VS Code; Python merely acts as an automated wrapper for your existing regex rules.

---

## **27 Content**

**A 10-Line Python Script Recipe (`normalize.py`)**

For students who want to take their digital skills to the next level, you can translate your VS Code rules into an executable Python script (`normalize.py`) in less than ten lines of code.

Here is the complete, canonical Python script recipe:

```python
import re
from pathlib import Path

# 1. Read the input XML file
text = Path("transcription_reconciled.xml").read_text(encoding="utf-8")

# 2. Apply your regex rules sequentially
text = re.sub(r"(publi|traffi)ck", r'<choice><orig>ck</orig><reg resp="#editor">c</reg></choice>', text)
text = re.sub(r"([Yy])e", r'<choice><abbr>e</abbr><expan resp="#editor">he</expan></choice>', text)
text = re.sub(r"([Aa])llways", r'<choice><orig>llways</orig><reg resp="#editor">lways</reg></choice>', text)

# 3. Write the transformed output file
Path("transcription_reconciled_regex.xml").write_text(text, encoding="utf-8")
print("Normalization complete! Saved to transcription_reconciled_regex.xml")
```

Notice two critical details:
<ol>
  <li><strong>Raw Strings (<code>r"..."</code>):</strong> Always prefix your regex patterns and replacement strings in Python with the letter <code>r</code> (e.g., <code>r"..."</code>). The <code>r</code> stands for "raw string", which prevents Python from misinterpreting backslashes like <code></code> as special escape characters.</li>
  <li><strong>Backreference Syntax:</strong> In Python replacement strings, backreferences are written with backslashes (<code></code>, <code></code>) rather than dollar signs (<code>$1</code>, <code>$2</code>).</li>
</ol>

Running this script (`python3 normalize.py`) executes all your rules simultaneously in a fraction of a second.

**Vocabulary.** *Raw string (`r"..."`)* — A Python string literal that treats backslashes as literal characters, essential for writing regular expression patterns. *Sequential pipeline* — Applying multiple transformation rules one after another, passing the output of each rule as the input to the next.

**Takeaway:** A 10-line Python script using `re.sub()` chains your tested regular expressions into an automated, one-click normalization pipeline.

---

## **28 Content**

**Batching Rules: The Sequential Execution Pipeline**

When you run multiple regular expressions—whether sequentially in VS Code or in a Python script—you are executing a **sequential transformation pipeline**.

In a pipeline, the order in which rules execute is load-bearing. Rule 1 runs on the original text and produces an intermediate text. Rule 2 runs on that intermediate text and produces a second intermediate text. If your rules interact with the same words, the order of execution can produce unexpected side effects.

Consider this rule-ordering dilemma:

```text
Rule A (Capitalization): Regularize common-noun capitals: Treaty -> treaty
Rule B (Thorn Expansion): Expand Ye -> The
```

If Rule A runs first with an unconstrained casing pattern, it might turn *Ye* into *ye*. When Rule B runs second, its capitalized pattern `Ye` will fail to find anything, because Rule A already lowercased it!

To prevent pipeline collisions:
<ol>
  <li><strong>Run specific rules before general rules:</strong> Always execute narrow, exact rules (like expanding unique abbreviations) before applying broad spelling or casing regularizations.</li>
  <li><strong>Never run a rule on already-tagged markup:</strong> Ensure that your patterns do not match text that is already inside a <code>&lt;choice&gt;</code> block. For example, if you replace <em>publick</em> with <code>&lt;choice&gt;...&lt;/choice&gt;</code>, make sure a subsequent rule does not match the word <em>publick</em> inside your newly generated <code>&lt;orig&gt;</code> tag!</li>
</ol>

Testing your pipeline sequentially in VS Code reveals these ordering traps before they cause damage.

**Vocabulary.** *Rule ordering* — The deliberate sequence in which automated transformations are applied to prevent adverse interactions between rules. *Pipeline collision* — An error where an earlier rule alters text in a way that breaks a subsequent rule or re-matches already-tagged markup.

**Takeaway:** Order your rules carefully—executing narrow specific abbreviations before general casing rules—to prevent pipeline collisions.

---

## **29 Content**

**When Deterministic Regex Fails: Context-Dependency**

As powerful as regular expressions are, every digital editor must recognize their absolute theoretical and practical limits: **regular expressions have no access to semantic context**.

A regular expression matches formal character strings. It does not know who wrote the document, what century it was composed in, what the grammatical syntax of the sentence is, or what the author intended.

Regex fails whenever normalization is **context-dependent**:

<ul>
  <li><strong>Syntactic Ambiguity:</strong> In 18th-century French, deciding whether a word ending in <em>-oit</em> is an imperfect verb (needing regularization to <em>-ait</em>) or an invariant noun (like <em>droit</em>) requires understanding grammatical parts of speech. Regex cannot parse parts of speech.</li>
  <li><strong>Semantic Homographs:</strong> In English, deciding whether <em>wont</em> means <em>won't</em> (will not) or <em>wont</em> (custom) requires understanding the sentence's meaning.</li>
  <li><strong>Poetic Restraint:</strong> In Emily Dickinson's poetry, deciding whether a capitalized word like <em>Door</em> is an accidental 18th-century habit or a deliberate metaphysical personification requires literary sensitivity that no mathematical regex can ever possess.</li>
</ul>

This boundary marks the transition to Friday's session. Where deterministic regex stops, artificial intelligence models and large language models step in with the ability to perform contextual semantic disambiguation.

**Vocabulary.** *Context-dependency* — A linguistic situation where the correct interpretation or normalization of a word depends on surrounding sentence semantics rather than raw spelling. *Semantic blindness* — The inability of regular expressions to comprehend meaning, syntax, or authorial intent.

**Takeaway:** Regular expressions excel at mechanical, unambiguous pattern matching, but fail on context-dependent words, syntactic homographs, and poetic nuance.

---

## **30 Content**

**Review and Workshop 6 Step 2 Deliverables**

Today you bridged the gap between human editorial policy and automated computational execution. You mastered regular expressions directly inside the VS Code editor, demonstrated the power of word boundaries and capturing groups, generated TEI `<choice>` markup dynamically, and audited your rules against your manual ground truth.

Before concluding today's session, review the **Workshop 6 Step 2 Checklist**:

<ol>
  <li><strong>Regex Rules Formulated:</strong> Have you created at least 3 to 5 distinct regular expressions corresponding to the active rules in your Rule Ledger?</li>
  <li><strong>Word Boundaries Enforced:</strong> Are all your word search patterns strictly anchored with <code></code> to prevent accidental substring corruption?</li>
  <li><strong>XML-Safe Patterns Used:</strong> Have you ensured that no unconstrained wildcards (<code>.*</code>) match across XML tags or milestone markers?</li>
  <li><strong>Dynamic `<choice>` Generated:</strong> Did your replacement patterns successfully construct complete, valid TEI <code>&lt;choice&gt;</code> blocks with <code>&lt;orig&gt;</code>/<code>&lt;reg&gt;</code> or <code>&lt;abbr&gt;</code>/<code>&lt;expan&gt;</code>?</li>
  <li><strong>Audited via Side-by-Side Diff:</strong> Have you compared your regex-transformed file against yesterday's manual ground truth in VS Code, calculating your True Positives and eliminating False Positives?</li>
  <li><strong>Rule Ledger Updated in `NORMALIZATION.md`:</strong> Have you recorded your exact regex patterns, replacement strings, and observed precision metrics in your project ledger?</li>
  <li><strong>Schema Validated:</strong> Does your transformed XML document validate with <strong>0 errors</strong> in VS Code?</li>
</ol>

With Step 2 complete, you have an audited deterministic baseline ready for Friday, where we will unleash generative AI models on the same text and test whether they enhance or over-normalize our historical documents.

**Vocabulary.** *Step 2 milestone* — The completion of the deterministic regular expression pass, documented in the Rule Ledger and verified against the manual ground truth baseline.

**Takeaway:** Step 2 automates your normalization policy using validated, XML-safe regular expressions, establishing an audited baseline for Friday's AI comparison.

---

## References

Bollmann, M. (2019). A large-scale comparison of historical text normalization systems. In *Proceedings of the 2019 conference of the North American chapter of the Association for Computational Linguistics: Human language technologies* (Vol. 1, pp. 3887–3898). Association for Computational Linguistics. https://doi.org/10.18653/v1/N19-1389

Burnard, L. (2014). *What is the Text Encoding Initiative? How to add intelligent markup to digital resources*. OpenEdition Press. https://doi.org/10.4000/books.oep.426

Friedl, J. E. (2006). *Mastering regular expressions* (3rd ed.). O'Reilly Media.

Jurafsky, D., & Martin, J. H. (2024). *Speech and language processing: An introduction to natural language processing, computational linguistics, and speech recognition* (3rd ed. draft). Stanford University. https://web.stanford.edu/~jurafsky/slp3/

TEI Consortium. (2024). *TEI P5: Guidelines for electronic text encoding and interchange* (version 4.8.0). TEI Consortium. https://tei-c.org/guidelines/p5/
