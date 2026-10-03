# Lesson 6.3 — AI-Assisted Normalization and the Risk of Over-Normalization

*RELS 398 / ENGL 398 · Topic 6: Normalization · Meeting #16 (Fri Oct 9)*

***Step 3 of the three-step cycle: AI-assisted.** Today you apply generative artificial intelligence models to historical text normalization and audit their output against your manual ground truth and deterministic regex rules. You will learn to construct rigorous negative prompts, evaluate the serious threat of hypercorrection, and execute the three-way comparative audit that forms the core deliverable of Workshop 6.*

---

## **01 Content**

**Today's Question: Capability vs. Fidelity**

Over the past two sessions, you normalized your 20-line consensus passage twice. On Tuesday (Lesson 6.1), you established your Editorial Regularization Policy by hand, embedding your human scholarly judgment into a Rule Ledger. On Wednesday (Lesson 6.2), you translated that policy into deterministic regular expressions in VS Code, discovering that rules enforce absolute consistency but remain blind to grammatical and semantic context.

Today, we introduce the third and final method of our comparative cycle: **generative artificial intelligence and large language models (LLMs)**.

The central question today is not simply whether an AI model can normalize text faster. The question is: **Is the remarkable contextual capability of generative AI worth the fidelity and accountability it risks?**

This distinction is crucial because normalization fundamentally differs from diplomatic transcription. Transcription is anchored to physical ink: a letter either exists on the parchment or it does not. Normalization, by contrast, is an interpretive act governed by an editorial policy. When an AI model normalizes a word differently from you, it is not necessarily making an image recognition error; it may be applying an unstated modernizing policy of its own (Bollmann, 2019).

Our goal today is to harness the genuine contextual strengths of LLMs while building strict methodological guardrails against their most dangerous failure mode: **over-normalization**.

**Vocabulary.** *Generative normalization* — Using large language models to predict and generate standardized orthographic forms based on contextual linguistic probability. *Model policy drift* — The tendency of an AI model to substitute its own modern commercial training defaults for the editor's explicit scholarly policy.

**Takeaway:** Generative AI brings powerful contextual reasoning to text normalization, but editors must actively prevent the model's fluency from drifting into unwanted modernization.

---

## **02 Content**

**From Sequence-to-Sequence Models to Modern Generative LLMs**

To understand how modern AI approaches historical language, it helps to understand how computational text normalization evolved over the last decade.

In the 2010s, automated historical normalization relied on character-level neural machine translation, using architectures like bidirectional Long Short-Term Memory (LSTM) networks or finite-state transducers (Bollmann, 2019). These earlier models were trained specifically on historical corpora to translate individual character sequences (like *publick* &rarr; *public*). While transparent and bounded, they required massive historical training datasets and frequently failed on rare vocabulary or unusual dialects.

Today, the digital humanities landscape is dominated by large multimodal transformer models, such as Google Gemini, Anthropic Claude, and OpenAI GPT. These models are not character-level transducers; they are vast, billion-parameter neural networks trained on petabytes of multilingual text.

Because modern LLMs have ingested hundreds of thousands of digitized historical books, early modern treatises, and dialect dictionaries, they possess extraordinary latent knowledge of historical orthography. A model like Gemini in VS Code Antigravity recognizes immediately that 18th-century *étoit* corresponds to modern French *était*, that colonial *ye* represents *the*, and that 19th-century *opake* represents *opaque*.

However, because these models were designed primarily to generate fluent, natural contemporary prose, their internal statistical bias is overwhelmingly weighted toward modern standardization. Without strict constraints, they will aggressively rewrite history into contemporary idiom.

**Vocabulary.** *Transformer architecture* — The deep learning neural network design based on self-attention mechanisms that powers modern large language models. *Modernization bias* — The inherent statistical tendency of commercial LLMs to convert historical text into modern standard prose.

**Takeaway:** Modern generative LLMs possess vast latent knowledge of historical spelling, but their commercial training creates a powerful statistical bias toward modern fluency.

---

## **03 Content**

**The Contextual Advantage: Disambiguating Homographs**

Why bother using an AI model for normalization if regular expressions already provide fast, deterministic matching? The answer lies in one word: **context**.

Yesterday in Lesson 6.2, we discovered the absolute limit of regular expressions: regex is semantically blind. A regular expression cannot determine parts of speech, cannot analyze sentence grammar, and cannot understand meaning. When regex encounters an ambiguous homograph, it fails:

<ul>
  <li><strong>The French <em>-oit</em> Homograph:</strong> An 18th-century French regex rule changing <em>-oit</em> to <em>-ait</em> correctly normalizes imperfect verbs like <em>étoit</em> &rarr; <em>était</em>. But it blindly corrupts the invariant noun <em>droit</em> (law/right) into nonsensical <em>drait</em>!</li>
  <li><strong>The English <em>wont</em> Homograph:</strong> A regex rule expanding unpunctuated <em>wont</em> into <em>won't</em> (will not) blindly corrupts historical sentences where <em>wont</em> is a valid noun meaning "custom or habit" (as in "as was his wont").</li>
  <li><strong>The Thorn <em>ye</em> Homograph:</strong> A regex rule expanding <em>ye</em> to <em>the</em> blindly corrupts sentences where <em>ye</em> is the authentic archaic second-person plural pronoun ("ye shall know the truth").</li>
</ul>

This is where large language models excel. Because an LLM attends to all surrounding tokens simultaneously through self-attention layers (Jurafsky & Martin, 2024), it parses sentence syntax with remarkable nuance. 

When Gemini reads "according to his wont", it recognizes *wont* as a noun governed by a possessive pronoun, and leaves it untouched. When it reads "he wont come", it recognizes *wont* as an auxiliary verb contraction and normalizes it to *won't*. Generative AI resolves the semantic and syntactic ambiguities that break deterministic regular expressions.

**Vocabulary.** *Self-attention* — The mathematical mechanism in transformer models that calculates dynamic relationships between all words in a sentence, enabling contextual disambiguation. *Syntactic disambiguation* — Correctly identifying a word's grammatical part of speech by analyzing its syntactic environment.

**Takeaway:** LLMs use contextual self-attention to successfully disambiguate syntactic homographs (like *droit* vs. *étoit* or *wont* vs. *won't*) that cause regex to fail.

---

## **04 Content**

**The Critical Risk: Over-Normalization**

While contextual awareness is the greatest asset of generative AI, it gives birth to the greatest hazard in digital textual scholarship: **over-normalization**.

Over-normalization occurs when an artificial intelligence model expands its editorial intervention beyond surface orthography into morphology, vocabulary, syntax, or tone (Bollmann, 2019). Instead of simply modernizing spelling within `<orig>` and `<reg>` tags, the model silently rewrites the author's prose to sound like a 21st-century essay.

Commercial language models are fine-tuned with reinforcement learning from human feedback (RLHF) to prioritize helpfulness, clarity, and grammatical correctness. In customer service or business writing, smoothing out awkward phrasing is a virtue. In digital textual scholarship, smoothing out historical phrasing is an act of **editorial vandalism**.

Consider what an unconstrained AI model does to historical text:
<ul>
  <li><strong>Syntactic Flattening:</strong> In an 18th-century treaty, an unconstrained model might alter inverted word order (e.g., changing "Articles herein agreed upon" to "Articles agreed upon here").</li>
  <li><strong>Grammatical Modernization:</strong> In personal letters, a model might "correct" non-standard dialectal verb agreement (e.g., changing Maud Lewis's "we was" to "we were").</li>
  <li><strong>Lexical Substitution:</strong> An unconstrained model might replace unfamiliar archaic vocabulary with contemporary synonyms (e.g., replacing *betwixt* with *between*, or *vouchsafe* with *grant*).</li>
</ul>

In scholarly editing, our job is to regularize spelling, not to ghostwrite history. The editor must maintain an aggressive, skeptical guard against over-normalization.

**Vocabulary.** *Over-normalization* — The destructive editorial error where an automated tool alters grammar, vocabulary, or word order under the guise of regularizing spelling. *Syntactic flattening* — Eliminating historical sentence structures to produce generic modern prose.

**Takeaway:** Over-normalization occurs when an AI model exceeds spelling regularization to silently alter historical vocabulary, grammar, or word order.

---

## **05 Content**

**The Hypercorrection Taxonomy in Normalization**

To audit an AI model's performance rigorously, a digital editor must be able to classify its mistakes. We do not simply say "the AI made an error"; we diagnose the exact type of failure using an established **Hypercorrection Taxonomy**:

<table style="width: 100%; border-collapse: collapse; margin-top: 1rem; margin-bottom: 1rem;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1; text-align: left;">
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Error Category</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Mechanism</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Historical Example</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">AI Hypercorrection</th>
      <th style="padding: 0.5rem; border: 1px solid #cbd5e1;">Scholarly Verdict</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><strong>1. Lexical Substitution</strong></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Replaces an archaic word with a modern synonym.</td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><em>betwixt</em></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>&lt;reg&gt;between&lt;/reg&gt;</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><strong>Severe Error:</strong> Destroys historical vocabulary; <em>betwixt</em> is a valid word, not a misspelling.</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><strong>2. Morphological Modernization</strong></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Modernizes archaic grammatical inflections.</td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><em>doth</em>, <em>hath</em></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>&lt;reg&gt;does&lt;/reg&gt;</code>, <code>&lt;reg&gt;has&lt;/reg&gt;</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><strong>Severe Error:</strong> Modernizes early modern third-person singular verb morphology.</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><strong>3. Dialect Erasure</strong></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Standardizes vernacular dialectal grammar.</td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><em>we was</em></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>&lt;reg&gt;we were&lt;/reg&gt;</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><strong>Severe Error:</strong> Erases working-class Maritime dialectal voice.</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><strong>4. Hallucinated Expansion</strong></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;">Invents an unwritten expansion without evidence.</td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><em>Capt.</em></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><code>&lt;expan&gt;Captain of the Guard&lt;/expan&gt;</code></td>
      <td style="padding: 0.5rem; border: 1px solid #cbd5e1;"><strong>Hallucination:</strong> Expands beyond what was physically abbreviated.</td>
    </tr>
  </tbody>
</table>

When auditing your AI pass on Friday, test every single `<choice>` tag against this taxonomy. If the AI committed any of these four errors, flag it immediately.

**Vocabulary.** *Hypercorrection taxonomy* — A formal classification system categorizing automated editorial errors into lexical substitution, morphological modernization, dialect erasure, and hallucinated expansion. *Dialect erasure* — The unauthorized alteration of regional grammar to conform to prestige standard language.

**Takeaway:** Classify AI normalization errors using the four-part taxonomy: lexical substitution, morphological modernization, dialect erasure, and hallucinated expansion.

---

## **06 Content**

**Hallucinated Abbreviation Expansions**

Among the errors catalogued in our taxonomy, **hallucinated abbreviation expansion** represents a unique danger in digital scholarship.

Because generative language models are trained to predict the most statistically probable sequence of tokens, they abhor ambiguity. When an LLM encounters a truncated historical abbreviation, it does not like to admit that it does not know the full word. Instead, it generates an elaborate, plausible-sounding expansion based on its statistical training, whether or not that expansion is historically true.

Consider an 18th-century military commission or treaty that refers to an officer as:

```text
"Lieut. Col. John Gorham"
```

A careful human editor expands the abbreviations to:

```xml
<choice><abbr>Lieut.</abbr><expan resp="#editor">Lieutenant</expan></choice>
<choice><abbr>Col.</abbr><expan resp="#editor">Colonel</expan></choice>
```

An unconstrained AI model, however, frequently hallucinates additional historical context into the expansion tag. It might generate:

```xml
<choice><abbr>Col.</abbr><expan resp="#gemini">Colonel of the Independent Company of Rangers</expan></choice>
```

While John Gorham may indeed have commanded the Gorham's Rangers historically, the letters *C-o-l* on that physical parchment page stand strictly for the word *Colonel*, not for his entire military resume! 

An expansion inside `<expan>` must supply **only the letters that were omitted from the abbreviated word itself**. It must never become an encyclopedia article or historical commentary. When checking AI expansions, verify that every expansion corresponds strictly to the lexical word being abbreviated.

**Vocabulary.** *Hallucinated expansion* — An expansion that invents unwritten historical titles, offices, or words beyond the lexical scope of the abbreviated letters. *Lexical boundary* — The strict rule that an `<expan>` tag must supply only the omitted letters of the target word.

**Takeaway:** An `<expan>` tag must contain only the omitted letters of the abbreviated word; verify that AI models never inject historical commentary or unwritten titles into expansions.

---

## **07 Content**

**Negative Prompting: The Essential Defense**

How do we prevent generative AI models from committing lexical substitution, morphological modernization, dialect erasure, and hallucinated expansions? The answer lies in **Negative Prompting** (Jurafsky & Martin, 2024).

In prompt engineering, a positive instruction tells the model what to do (e.g., "Regularize historical spelling using TEI choice markup"). A **negative constraint** tells the model what it is strictly forbidden to do.

LLMs are prone to "helpful drift"—they assume that your request to "normalize" means you want the text to look clean, polished, and contemporary. To counteract this, an editor must construct rigid, unambiguous negative guardrails.

Effective negative prompting requires three rules:
<ol>
  <li><strong>Be Explicit, Not Vague:</strong> Do not say "do not change too much." Say: "DO NOT alter vocabulary, DO NOT modernize grammatical verb inflections (such as -eth or -st), and DO NOT alter word order."</li>
  <li><strong>State the Forbidden Actions in All-Caps:</strong> Capitalized constraint headers draw heavy attention weights across the model's self-attention matrix during token generation.</li>
  <li><strong>Define the Boundary Between Spelling and Grammar:</strong> Explicitly state: "You are an orthographic regularizer, NOT a stylistic editor. If an author writes non-standard grammar, PRESERVE THE GRAMMAR EXACTLY."</li>
</ol>

By establishing explicit negative boundaries, you constrain the model's generative capacity, forcing it to act as a disciplined paleographical assistant rather than an unauthorized co-author.

**Vocabulary.** *Negative prompting* — The deliberate technique of specifying explicit prohibitions and boundaries in a prompt to suppress model hallucination and unwanted behaviors. *Constraint weighting* — Structuring prompt instructions to ensure negative prohibitions dominate generative token selection.

**Takeaway:** Negative prompting is the digital editor's primary defense: explicitly forbid lexical substitution, grammatical modernization, and syntactic reordering.

---

## **08 Content**

**Crafting the Normalization System Prompt**

Now let us construct the master **Normalization System Prompt** that you will use in Visual Studio Code Antigravity.

A production-grade scholarly system prompt consists of five modular components:

<ol>
  <li><strong>Persona & Role:</strong> Establishes the model's professional identity as a conservative academic digital editor.</li>
  <li><strong>Primary Task:</strong> Defines the exact objective—inserting TEI <code>&lt;choice&gt;</code> tags around spelling variants and abbreviations.</li>
  <li><strong>Target Authority:</strong> Declares the normative reference standard (e.g., standard modern Canadian/American English or Académie française French).</li>
  <li><strong>Inviolable Negative Constraints:</strong> Forbids lexical substitution, grammatical modernization, and tag deletion.</li>
  <li><strong>Output Format Requirements:</strong> Demands strictly well-formed TEI XML with zero markdown commentary.</li>
</ol>

Here is the foundational prompt structure for our course:

```text
You are an expert digital textual scholar specializing in TEI P5 XML encoding.
Your task is to perform conservative orthographic normalization and abbreviation expansion on a historical document excerpt.

RULES AND CONSTRAINTS:
1. OUTPUT: Return ONLY the updated TEI XML fragment. Do not include markdown conversational filler, explanations, or notes.
2. PRESERVATION: Wrap target words in <choice>. Preserve the exact historical reading in <orig> or <abbr>. Supply the standardized modern reading in <reg resp="#gemini"> or <expan resp="#gemini">.
3. NEGATIVE CONSTRAINT - NO LEXICAL SUBSTITUTION: Do NOT replace archaic words with modern synonyms (e.g., keep "betwixt", do not change to "between").
4. NEGATIVE CONSTRAINT - NO GRAMMATICAL MODERNIZATION: Do NOT modernize verb endings (keep "hath", "doth", "sheweth") or dialectal syntax (keep "we was").
5. NEGATIVE CONSTRAINT - NO TAG MUTILATION: NEVER delete, move, or rename existing milestone tags (<lb/>, <pb/>). Line breaks must remain inside <orig>.
6. ATTRIBUTION: Every newly created <reg> and <expan> tag MUST include the attribute resp="#gemini".
```

Notice how every instruction addresses a specific failure mode we identified in our taxonomy. This prompt transforms a commercial chatbot into a focused scholarly tool.

**Vocabulary.** *System prompt* — The top-level foundational instruction provided to an AI model that sets its persistent persona, constraints, and operational boundaries. *Attribution tagging* — Attaching `resp="#gemini"` to automated markup to distinguish machine intervention from human judgment.

**Takeaway:** A scholarly system prompt combines persona, task, target authority, strict negative constraints, and output formatting rules into an auditable protocol.

---

## **09 Content**

**Prompt Engineering for Historical English (1752 Treaty)**

Now let us customize our system prompt for the specific document projects in our cohort. We begin with Andromeda's project: the **1752 Peace and Friendship Treaty**.

Eighteenth-century colonial legal documents present two unique challenges for AI models: **substantive common-noun capitalization** and **archaic legal diction**.

If you feed the 1752 Treaty to a generic AI model, it will often try to rewrite the formal preamble, modernizing legal formulas like "In Witness whereof" or "Know ye that". Furthermore, it may become confused by the heavy capitalization, lowercasing words that are proper names or titles.

To tailor your prompt for the 1752 Treaty, add these document-specific instructions to your system prompt:

```text
DOCUMENT SPECIFICATION - 18th-CENTURY COLONIAL TREATY (1752):
- TARGET 1 (Terminal -ck): Regularize 18th-century adjectives ending in -ck (e.g., "publick" -> "public", "traffick" -> "traffic"). Do NOT regularize native standard Germanic words (e.g., "black", "truck").
- TARGET 2 (Thorn Contractions): Expand thorn contractions: "ye" -> <choice><abbr>ye</abbr><expan resp="#gemini">the</expan></choice>; "yt" -> <choice><abbr>yt</abbr><expan resp="#gemini">that</expan></choice>.
- TARGET 3 (Common Nouns): Regularize substantive capitalized common nouns to lowercase in <reg> ONLY when they are ordinary nouns (e.g., "Treaty" -> "treaty", "Articles" -> "articles"). PRESERVE capital letters on official titles and sovereign names (e.g., "His Majesty", "Governor", "King").
- STRICT PROHIBITION: Do NOT alter archaic legal phrasing, prepositional idioms, or punctuation.
```

By explicitly naming the targets (*-ck*, thorn contractions, common nouns) and naming the exceptions (titles, legal phrasing), you provide the AI with the exact scholarly policy you established in Lesson 6.1.

**Vocabulary.** *Document-specific tailoring* — Modifying a general system prompt with specialized rules and exceptions reflecting the paleographical realities of a specific historical witness.

**Takeaway:** Tailor prompts for 18th-century legal texts by explicitly defining rules for terminal *-ck*, thorn abbreviations, and title versus common-noun capitalization.

---

## **10 Content**

**Prompt Engineering for Autograph Poetry (Emily Dickinson)**

Next, let us examine prompt engineering for Jay's project: **Emily Dickinson's autograph poetry** (`MS Am 1118.3 [338]`).

Dickinson represents the ultimate test of prompt discipline. Large language models are trained heavily on modern edited editions of 19th-century literature. When an LLM sees a Dickinson poem, its internal weights scream to "fix" her: to replace her dashes with commas, to lowercase her idiosyncratic capitals (*Soul*, *Society*, *Door*), and to normalize her slant rhymes.

If you give a Dickinson poem to an untuned AI model, it will completely obliterate her poetic genius in a single pass.

To protect Dickinson's text, your system prompt must erect an absolute firewall around her poetic orthography:

```text
DOCUMENT SPECIFICATION - AUTOGRAPH 19th-CENTURY POETRY (EMILY DICKINSON):
- STRICT PROHIBITION - CAPITALIZATION: NEVER normalize, lowercase, or tag Dickinson's capitalized common nouns (e.g., "Soul", "Society", "Door", "Valves", "Stone"). Her capitalization represents intentional poetic personification and MUST remain unaltered plain text.
- STRICT PROHIBITION - DASHES AND PUNCTUATION: NEVER replace, alter, or standardize her dashes. Do NOT insert commas, semicolons, or periods.
- STRICT PROHIBITION - RHYME WORDS: NEVER normalize spelling on terminal line words that participate in authorial slant rhyme.
- ALLOWED TARGETS: You may ONLY regularize genuine archaic or variant spellings where standard lexicography has shifted (e.g., "opake" -> <choice><orig>opake</orig><reg resp="#gemini">opaque</reg></choice>; "etherial" -> <choice><orig>etherial</orig><reg resp="#gemini">ethereal</reg></choice>).
```

Notice the tone of this prompt. It is fiercely protective. It forbids the model from touching 95% of the text, confining its authority strictly to undisputed lexical variants. This is how digital editors use AI responsibly in literary scholarship.

**Vocabulary.** *Poetic firewall* — Prompt constraints designed to completely protect authorial punctuation, capitalization, and rhyme from automated normalization.

**Takeaway:** For Emily Dickinson's poetry, construct an aggressive poetic firewall in your prompt, strictly forbidding the model from altering her capitalization, dashes, or rhyme words.

---

## **11 Content**

**Prompt Engineering for Vernacular Correspondence (Maud Lewis)**

Now let us examine Olyvia's project: personal handwritten letters by celebrated folk artist **Maud Lewis**.

When editing vernacular personal correspondence, the primary danger is that the AI model will act as an arrogant schoolmaster, "correcting" Lewis's working-class dialect, informal spelling, and conversational syntax to sound like an academic textbook.

If Maud Lewis writes "we was pleased to get your letter and we dont have no more paintings", an unconstrained model will aggressively change *was* to *were*, delete the double negative, and rewrite her voice completely.

Your system prompt must explicitly defend the integrity of her vernacular voice:

```text
DOCUMENT SPECIFICATION - 20th-CENTURY VERNACULAR CORRESPONDENCE (MAUD LEWIS):
- TARGET 1 (Phonetic Doubling): Regularize obvious phonetic spelling variants using <choice><orig>...</orig><reg resp="#gemini">...</reg></choice> (e.g., "allways" -> "always", "untill" -> "until", "truely" -> "truly").
- TARGET 2 (Unpunctuated Contractions): Supply missing apostrophes in negative contractions (e.g., "dont" -> "don't", "cant" -> "can't", "wont" -> "won't").
- STRICT PROHIBITION - VERNACULAR GRAMMAR: Do NOT touch or regularize non-standard verb agreement, colloquial idioms, or conversational syntax (e.g., PRESERVE "we was").
- STRICT PROHIBITION - NO <sic> TAGS: Do NOT use <sic> or <corr> tags. All vernacular variations must be treated respectfully as valid historical variants using <orig> and <reg>.
```

Notice the explicit ban on `<sic>` tags. This constraint ensures that the AI model does not brand working-class Maritime dialect as an error, fulfilling the ethical principles of respectful editing we established in Lesson 6.1.

**Vocabulary.** *Voice preservation* — Prompt constraints ensuring that regional, working-class, and informal conversational idioms are protected from automated standardizing bias.

**Takeaway:** For Maud Lewis's personal letters, instruct the AI to regularize phonetic spelling and omitted apostrophes while strictly forbidding it from altering vernacular grammar or using `<sic>` tags.

---

## **12 Content**

**Prompt Engineering for Revolutionary French (1791 Decree)**

Finally, let us customize our prompt for Ace's project: the **1791 French Revolutionary Decree** from the National Assembly.

Eighteenth-century French presents two challenges that confuse generic AI models: the **Voltairean *oi*/*ai* imperfect verb shift** and **omitted accents on capital letters**.

An untuned model will often try to translate the entire decree into modern French legal vocabulary, modernizing phrases like *Comité des décrets* or replacing 18th-century juridical terms. Furthermore, it may fail to distinguish between imperfect verbs (which changed from *-oit* to *-ait*) and invariant nouns (like *droit*).

Here is the tailored prompt for the 1791 French Decree:

```text
DOCUMENT SPECIFICATION - 18th-CENTURY FRENCH REVOLUTIONARY DECREE (1791):
- TARGET 1 (Voltairean Imperfect Verbs): Regularize historical imperfect indicative and conditional verb endings from -oit to -ait (e.g., "étoit" -> "était", "dérogeoit" -> "dérogeait", "faisoient" -> "faisaient").
- TARGET 2 (Historical Nationality / Adjectives): Regularize historical -ois endings on nationality adjectives to -ais (e.g., "françois" -> "français").
- TARGET 3 (Accented Capitals): Supply missing acute and grave accents on capitalized words in <reg> (e.g., "DECRET" -> "DÉCRET", "ASSEMBLEE" -> "ASSEMBLÉE").
- EXCLUSION - INVARIANT NOUNS: Do NOT alter invariant nouns ending in -oit (e.g., PRESERVE "droit", "étroit").
- STRICT PROHIBITION: Do NOT alter French revolutionary legal formulas, syntax, or Latin terms (e.g., PRESERVE "L.S.").
```

Notice how this prompt gives the model the historical linguistic rule (the 1835 Académie reform) and explicitly names the invariant nouns (*droit*) that must be protected. The AI now possesses the precise historical boundaries needed to succeed.

**Vocabulary.** *Voltairean prompt specification* — Guiding the model to regularize 18th-century French *oi* endings to *ai* while protecting invariant nouns and legal Latin shorthand.

**Takeaway:** For 18th-century French decrees, direct the model to normalize *-oit* imperfect verbs and accented capitals while strictly preserving legal formulas and invariant nouns like *droit*.

---

## **13 Content**

**Few-Shot Prompting: Providing Examples**

Even with explicit instructions and negative constraints, generative models sometimes misinterpret XML tag syntax. A model might generate `<reg value="public"/>` instead of `<reg>public</reg>`, or forget to include the `@resp` attribute.

The most powerful technique in prompt engineering for enforcing exact formatting is **Few-Shot Prompting** (Jurafsky & Martin, 2024).

Few-shot prompting means providing the model with **two or three concrete, perfectly formatted input/output examples** directly inside the prompt. When an LLM processes few-shot examples, its self-attention layers lock onto the structural template of your examples, replicating the exact tagging syntax with extraordinary fidelity.

Add this few-shot demonstration block to your system prompt:

```text
FEW-SHOT EXAMPLES (Follow this exact TEI syntax):

Input:
The publick good of this Province requires firm Articles.

Output:
The <choice><orig>publick</orig><reg resp="#gemini">public</reg></choice> good of this Province requires firm <choice><orig>Articles</orig><reg resp="#gemini">articles</reg></choice>.

Input:
yt was agreed by ye Govr at Halifax.

Output:
<choice><abbr>yt</abbr><expan resp="#gemini">that</expan></choice> was agreed by <choice><abbr>ye</abbr><expan resp="#gemini">the</expan></choice> <choice><abbr>Govr</abbr><expan resp="#gemini">Governor</expan></choice> at Halifax.
```

By providing these examples, you eliminate ambiguity. The model sees exactly how `<orig>` and `<reg>` pair together, how `<abbr>` and `<expan>` pair together, and where the `resp="#gemini"` attribute belongs. Few-shot prompting increases XML formatting compliance from roughly 75% to over 98%.

**Vocabulary.** *Few-shot prompting* — Providing an AI model with several concrete input-output demonstration pairs within the prompt to enforce exact formatting and behavior. *Zero-shot prompting* — Prompting a model with instructions only, without demonstration examples.

**Takeaway:** Include two or three few-shot examples in your prompt to anchor the model to your exact TEI `<choice>` syntax and attribute conventions.

---

## **14 Content**

**Running Normalization in VS Code Antigravity**

Now that your system prompt, document constraints, and few-shot examples are assembled, you are ready to execute the AI normalization pass directly inside your development environment: **Visual Studio Code with the Antigravity extension**.

Follow this step-by-step workflow:

<ol>
  <li><strong>Create your target file:</strong> In your course repository, duplicate your consensus file: create <code>transcription_reconciled_ai.xml</code>. This ensures that your manual ground truth and regex files remain untouched.</li>
  <li><strong>Open the Antigravity Chat Panel:</strong> In VS Code, open the Antigravity agent panel (in the left sidebar or via the Command Palette). Select your course model (Gemini 2.5 Pro / Flash).</li>
  <li><strong>Paste your System Prompt:</strong> Paste your master prompt, including your document-specific negative constraints and few-shot examples, into the chat interface.</li>
  <li><strong>Provide your 20-line passage:</strong> Copy your 20-line consensus excerpt from <code>transcription_reconciled.xml</code> and submit it with the instruction: <em>"Normalize the following TEI excerpt according to the prompt instructions."</em></li>
  <li><strong>Inspect the generated code:</strong> When Antigravity completes the generation, review the code block in the chat. Verify that it output valid TEI XML without conversational chit-chat.</li>
  <li><strong>Apply to your file:</strong> Click <strong>Apply</strong> or copy the generated XML into <code>transcription_reconciled_ai.xml</code>.</li>
</ol>

By running this process inside VS Code, you keep your entire edition within a single unified workspace.

**Vocabulary.** *Antigravity extension* — The Google AI pair-programming extension in VS Code providing direct access to Gemini models within the editor. *Workspace integration* — Executing AI generation and code application directly inside the development environment without copying between external web browsers.

**Takeaway:** Execute your AI normalization pass in VS Code Antigravity by submitting your tailored prompt and consensus text to generate `transcription_reconciled_ai.xml`.

---

## **15 Content**

**Formatting Output as Valid TEI `<choice>`**

Once the AI model returns its generated XML, your first technical duty is to verify that the markup conforms strictly to the TEI P5 schema (TEI Consortium, 2024).

Check for these three critical structural criteria:

<ol>
  <li><strong>Valid Pairing:</strong> Every <code>&lt;choice&gt;</code> element must enclose exactly one valid pair of child elements:
    <ul>
      <li><code>&lt;orig&gt;</code> and <code>&lt;reg&gt;</code> (for spelling regularization)</li>
      <li><code>&lt;abbr&gt;</code> and <code>&lt;expan&gt;</code> (for abbreviation expansion)</li>
    </ul>
    Confirm that the model did not invent non-standard tags like <code>&lt;modern&gt;</code>, <code>&lt;normalized&gt;</code>, or <code>&lt;expanded&gt;</code>.</li>
  <li><strong>Attribution Attribute:</strong> Verify that every <code>&lt;reg&gt;</code> and <code>&lt;expan&gt;</code> tag carries the attribution attribute: <code>resp="#gemini"</code>, which must match the <code>xml:id</code> you declare in the header.</li>
  <li><strong>Whitespace Containment:</strong> Verify that spaces between words remain outside the <code>&lt;choice&gt;</code> tags. If the model generated <code>&lt;choice&gt;&lt;orig&gt;publick &lt;/orig&gt;...&lt;/choice&gt;</code> with a space inside <code>&lt;orig&gt;</code>, remove the trailing space so words do not collapse or space erratically in downstream HTML viewers.</li>
</ol>

Open the Problems panel in VS Code (`Cmd+Shift+M`). Confirm that the newly pasted AI markup displays **0 schema errors**.

**Vocabulary.** *Valid pairing* — The strict TEI rule that `<choice>` must contain authorized child combinations (such as `<orig>`/`<reg>`). *Whitespace containment* — Ensuring inter-word spaces sit outside XML tagging structures to prevent display anomalies.

**Takeaway:** Inspect the AI output immediately to ensure it uses valid TEI `<choice>` element pairs, carries `@resp="#gemini"`, and passes schema validation with zero errors.

---

## **16 Content**

**Milestone Tag Preservation in AI Normalization**

In Lesson 6.1 and 6.2, we emphasized that physical milestone tags—specifically line breaks (`<lb/>`) and page breaks (`<pb/>`)—are sacred codicological data. They record where lines physically ended on the historical manuscript page.

Large language models have a notorious, well-documented bad habit: **they love to delete or move milestone tags** (Bollmann, 2019).

Because an LLM views text as a continuous semantic stream, empty milestone tags like `<lb n="14"/>` look like meaningless typographical clutter. If a model encounters a word divided across a line break (`Gov-<lb n="14"/>ernor`), an untuned model will often delete the `<lb/>` tag entirely, regularizing the word as a single continuous line:

```xml
<!-- FATAL AI ERROR: The physical line break was deleted! -->
<choice><orig>Governor</orig><reg resp="#gemini">Governor</reg></choice>
```

When this happens, your digital edition loses its physical alignment to the page image! The coordinate zones you built in Week 3 and the line numbers you verified in Week 4 are permanently severed.

Check your AI-generated text immediately:
<ul>
  <li>Did the model keep every <code>&lt;lb/&gt;</code> tag?</li>
  <li>Did the model preserve the line numbers (e.g., <code>n="14"</code>)?</li>
  <li>Did the model keep the milestone <em>inside</em> the <code>&lt;orig&gt;</code> element where it belongs?</li>
</ul>

If the model dropped even a single line break, reject that section and re-prompt with an intensified negative constraint: *"DO NOT DELETE OR MOVE ANY `<lb/>` TAGS."*

**Vocabulary.** *Milestone dropping* — The automated error where an AI model silently deletes empty milestone tags like `<lb/>` or `<pb/>` during text generation. *Codicological alignment* — The structural synchronization between digital transcription lines and physical manuscript page coordinates.

**Takeaway:** Carefully audit the AI output to verify that every `<lb/>` milestone tag and line number was preserved inside `<orig>` without being dropped or relocated.

---

## **17 Content**

**Conducting the Three-Way Audit (Workshop 6 Deliverable)**

Now arrives the intellectual climax of Week 6 and the primary deliverable of Workshop 6: **The Three-Way Comparative Audit**.

You now possess three distinct digital files in your repository, all derived from the exact same 20-line consensus passage:

<ol>
  <li><strong>File 1 (Manual Ground Truth):</strong> <code>transcription_reconciled_manual.xml</code> — Hand-encoded by you on Tuesday in Lesson 6.1. Reflects careful scholarly judgment and your explicit Rule Ledger.</li>
  <li><strong>File 2 (Deterministic Regex):</strong> <code>transcription_reconciled_regex.xml</code> — Automated by your regular expression rules on Wednesday in Lesson 6.2. Reflects absolute consistency, but semantic blindness.</li>
  <li><strong>File 3 (Generative AI):</strong> <code>transcription_reconciled_ai.xml</code> — Automated by Gemini in VS Code Antigravity today in Lesson 6.3. Reflects contextual reasoning, but risks over-normalization.</li>
</ol>

Your task is to conduct a systematic, word-by-word comparison across all three files.

You will not simply choose which file looks prettiest. You will conduct a scientific audit: comparing where the three methods agreed, where they diverged, and what each divergence teaches us about the strengths and limits of human, deterministic, and generative digital scholarship.

**Vocabulary.** *Three-way audit* — A comparative evaluation methodology comparing manual human baseline data, deterministic algorithmic outputs, and generative AI predictions on the same textual passage. *Triangulation* — Cross-verifying textual data across three independent methodologies to establish reliable findings.

**Takeaway:** The three-way audit compares your manual ground truth, deterministic regex output, and generative AI predictions to evaluate the strengths and limits of each method.

---

## **18 Content**

**The Side-by-Side Three-Way Diff in VS Code**

To conduct the audit efficiently, you must use Visual Studio Code's multi-editor layout to inspect all three files simultaneously.

Follow these steps in VS Code:

<ol>
  <li>Open <code>transcription_reconciled_manual.xml</code> in your main editor window.</li>
  <li>Split your editor into three columns: go to <em>View &rarr; Editor Layout &rarr; Three Columns</em> (or drag the tabs side by side).</li>
  <li>Place <code>transcription_reconciled_manual.xml</code> in the left column. Place <code>transcription_reconciled_regex.xml</code> in the middle column. Place <code>transcription_reconciled_ai.xml</code> in the right column.</li>
  <li>Scroll down line by line, comparing the three files at each line break.</li>
</ol>

Alternatively, you can run two pairwise diffs:
<ul>
  <li>Diff 1: <em>Manual vs. Regex</em> (highlights where deterministic rules over-matched or missed variants).</li>
  <li>Diff 2: <em>Manual vs. AI</em> (highlights where the AI model hypercorrected, hallucinated, or discovered new variants).</li>
</ul>

As you examine each line across the three columns, record every point of divergence in your notes. Every disagreement will fall into one of three primary discrepancy categories.

**Vocabulary.** *Three-column layout* — An editor arrangement displaying three files side by side simultaneously for line-by-line comparative auditing. *Pairwise diff* — Comparing two specific versions of a document to isolate exact character differences.

**Takeaway:** Configure a three-column layout or run pairwise diffs in VS Code to compare your manual, regex, and AI files line by line.

---

## **19 Content**

**Discrepancy Category A: Regex Missed, AI Caught**

The first category of divergence you will encounter is **Category A: Regex Missed, AI Caught** (a win for the AI model).

Recall the limitations of regular expressions. Regex matches only the exact characters and stems you anticipated in your pattern. If an author used an unexpected variant, an inflected grammatical form, or an irregular spelling that was not in your root whitelist, your regex rule missed it (a False Negative).

Consider an example from our cohort documents:
<ul>
  <li>Your regex rule looked for <code>\b(publi|traffi)ck\b</code>.</li>
  <li>On line 14, the manuscript contained the inflected adverb: <em>publickly</em>.</li>
  <li>Because of the trailing <em>-ly</em>, your regex word boundary <code>ck\b</code> failed to match, leaving <em>publickly</em> completely unregularized!</li>
</ul>

When you inspect Column 3 (the AI file), look at what Gemini did:
Gemini recognized that *publickly* is the adverbial form of *publick*. It successfully wrapped the word in:

```xml
<choice><orig>publickly</orig><reg resp="#gemini">publicly</reg></choice>
```

In Category A discrepancies, the AI model's deep linguistic knowledge and morphological generalization outperform the rigid, literal matching of regular expressions. When you verify that the AI's regularization is historically sound and conforms to your stated policy, record it in your report as a confirmed True Positive for the AI.

**Vocabulary.** *Morphological generalization* — The ability of an AI model to recognize inflected, derived, or unexpected forms of a word that rigid regex patterns overlook. *Category A discrepancy* — A divergence where generative AI successfully identifies a legitimate variant that deterministic rules missed.

**Takeaway:** Category A discrepancies demonstrate the power of AI: models generalize across inflected endings (like *publickly*) that rigid regular expressions overlook.

---

## **20 Content**

**Discrepancy Category B: Regex Safe, AI Hypercorrected**

The second category of divergence is the exact inverse: **Category B: Regex Safe, AI Hypercorrected** (a win for deterministic rules).

In Category B, your deterministic regular expression performed flawlessly: it adhered strictly to your root whitelist, regularized the target word, and left surrounding vocabulary completely alone.

The generative AI model, by contrast, fell victim to its commercial training bias and committed an act of **hypercorrection**.

Consider this real example from our student projects:
<ul>
  <li>On line 8 of the 1752 Treaty, the text reads: <em>"betwixt the Governor and the Chief"</em>.</li>
  <li>In Column 2 (Regex), your rule safely skipped <em>betwixt</em>, because your regex rules were confined strictly to terminal <em>-ck</em> and thorn abbreviations.</li>
  <li>In Column 3 (AI), Gemini decided that <em>betwixt</em> was "outdated", and generated:
    <pre><code>&lt;choice&gt;&lt;orig&gt;betwixt&lt;/orig&gt;&lt;reg resp="#gemini"&gt;between&lt;/reg&gt;&lt;/choice&gt;</code></pre>
  </li>
</ul>

This is a classic **Lexical Substitution Hypercorrection**. The word *betwixt* is an authentic, legitimate English preposition. It is not an unstandardized spelling; it is a distinct historical lexeme! Regularizing *betwixt* to *between* destroys the author's vocabulary.

In Category B discrepancies, the deterministic rigidity of regular expressions protects the document from the unauthorized over-reach of artificial intelligence. Record this in your report as an AI False Positive.

**Vocabulary.** *Category B discrepancy* — A divergence where deterministic regex correctly protected a historical word, but generative AI hypercorrected it. *Lexical over-reach* — The AI error of altering an author's authentic vocabulary under the pretext of spelling regularization.

**Takeaway:** Category B discrepancies demonstrate the strength of deterministic rules: regex strictly respects boundaries that generative AI crosses through hypercorrection.

---

## **21 Content**

**Discrepancy Category C: Mutual Failure and Complex Paleography**

The third category of divergence occurs when **both automated passes failed**: **Category C: Mutual Failure**.

Category C discrepancies occur at points of deep physical, paleographical, or linguistic ambiguity where neither mathematical pattern matching nor statistical token prediction can substitute for human scholarly immersion.

Examples of Category C failures across our cohort documents include:
<ul>
  <li><strong>Faded or Damaged Writing:</strong> A word where several letters are obscured by an ink blot or water stain. The regex pattern failed because the letters did not match standard characters. The AI model hallucinated a completely fabricated word because it predicted what ought to be there based on context, rather than reporting physical damage! Only your manual pass correctly used <code>&lt;unclear&gt;</code> and <code>&lt;gap/&gt;</code>.</li>
  <li><strong>Hyphenated Line Breaks across Folios:</strong> A word split across a folio boundary. Both automated tools failed to link the two halves.</li>
  <li><strong>Private Poetic Punctuation:</strong> Dickinson's variable dashes. Regex had no way to interpret the pen stroke, while the AI model aggressively converted the dashes into standard commas and semicolons, violating your explicit negative prompt!</li>
</ul>

Category C discrepancies are the most intellectually rewarding sections of your workshop report. They highlight the precise boundaries where automated digital tools break down and where the indispensable expertise of the human scholar remains sovereign.

**Vocabulary.** *Category C discrepancy* — A divergence where both deterministic regex and generative AI failed, proving that human paleographical judgment was strictly required. *Sovereignty of scholarship* — The principle that automated tools assist, but can never replace, human critical expertise.

**Takeaway:** Category C discrepancies expose points of complex physical damage or poetic nuance where both regex and AI fail, proving the irreplaceable necessity of human judgment.

---

## **22 Content**

**Calculating the Hypercorrection Rate**

To make your comparative audit empirical and scientific, you will calculate a formal quantitative metric for your AI pass: the **Hypercorrection Rate (HR)**.

The Hypercorrection Rate measures the proportion of an AI model's proposed editorial interventions that were unauthorized, excessive, or linguistically destructive:

$$\text{Hypercorrection Rate} = \frac{\text{Total AI Hypercorrections}}{\text{Total AI Editorial Interventions}}$$

Let us trace a concrete calculation on a 20-line passage:
<ol>
  <li>Suppose Gemini generated a total of <strong>16</strong> <code>&lt;choice&gt;</code> blocks across your passage (Total Interventions = 16).</li>
  <li>You audit each of the 16 blocks against your manual ground truth.</li>
  <li>You discover:
    <ul>
      <li>12 blocks were legitimate orthographic regularizations (True Positives).</li>
      <li>2 blocks replaced valid archaic words with modern synonyms (Lexical Substitutions: <em>betwixt</em> &rarr; <em>between</em>).</li>
      <li>1 block modernized a dialect verb inflection (Morphological Modernization: <em>we was</em> &rarr; <em>we were</em>).</li>
      <li>1 block invented an unwritten military title in an expansion (Hallucinated Expansion).</li>
    </ul>
  </li>
  <li>Total Hypercorrections = $2 + 1 + 1 = 4$.</li>
</ol>

Now calculate the Hypercorrection Rate:

$$\text{Hypercorrection Rate} = \frac{4}{16} = 0.25 \text{ (25\%)}$$

A Hypercorrection Rate of 25% means that **one out of every four edits proposed by the AI model was linguistically destructive**. Publishing this metric in your edition's documentation provides critical transparency for future researchers evaluating your dataset.

**Vocabulary.** *Hypercorrection Rate (HR)* — The mathematical proportion of an automated tool's proposed edits that represent unauthorized modernizations or hallucinations ($H / \text{Total Edits}$). *Quantitative audit* — Supporting qualitative textual observations with exact mathematical error frequencies.

**Takeaway:** Calculate the Hypercorrection Rate ($H / \text{Total Edits}$) to quantify the exact frequency with which an AI model over-stepped its scholarly boundaries.

---

## **23 Content**

**Evaluating Precision and Recall for the AI Pass**

Just as you evaluated your deterministic regex rules on Wednesday using Precision and Recall, you must now calculate the identical metrics for your generative AI pass.

Recall the core definitions:

$$\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}$$

$$\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}$$

Let us evaluate the AI pass from our previous section:
<ul>
  <li><strong>True Positives (TP):</strong> The AI correctly identified and regularized 12 legitimate historical variants that matched your manual ground truth policy.</li>
  <li><strong>False Positives (FP):</strong> The AI committed 4 hypercorrections on words that should have been left alone ($FP = 4$).</li>
  <li><strong>False Negatives (FN):</strong> Suppose your manual ground truth contained 14 legitimate target words, meaning the AI overlooked 2 archaic spellings ($FN = 2$).</li>
</ul>

Now calculate Precision and Recall:

$$\text{Precision} = \frac{12}{12 + 4} = \frac{12}{16} = 0.75 \text{ (75\%)}$$

$$\text{Recall} = \frac{12}{12 + 2} = \frac{12}{14} = 0.857 \text{ (85.7\%)}$$

Now compare this with Wednesday's deterministic regex!
Often, you will find a fascinating comparative trade-off:
<ul>
  <li><strong>Regex:</strong> Precision = 100%, Recall = 71% (Regex made zero mistakes, but missed irregular inflections).</li>
  <li><strong>Generative AI:</strong> Precision = 75%, Recall = 85.7% (AI caught more variations, but introduced destructive hypercorrections!).</li>
</ul>

This mathematical comparison is the heart of digital humanities. It proves empirically why neither tool can be trusted in isolation.

**Vocabulary.** *Comparative metrics* — Measuring Precision and Recall across multiple distinct methodologies applied to the identical textual benchmark. *Methodological trade-off* — The common phenomenon where deterministic rules maximize precision while generative models maximize recall at the expense of accuracy.

**Takeaway:** Comparing Precision and Recall reveals the fundamental trade-off: deterministic regex maximizes precision, while generative AI maximizes recall at the risk of false positives.

---

## **24 Content**

**Synthesizing the Final Normalized Text**

Now that your three-way audit is complete, you must assemble the final production artifact of Week 6: `transcription_normalized.xml`.

The final normalized file is not simply a copy of File 1, File 2, or File 3. It is a **scholarly synthesis** that brings together the best elements of all three passes:

<ol>
  <li><strong>Start with your Manual Ground Truth:</strong> Use <code>transcription_reconciled_manual.xml</code> as your master foundation. It contains your verified line breaks, your careful policy choices, and your human restraint.</li>
  <li><strong>Incorporate Valid AI Discoveries (Category A):</strong> Where the AI model successfully caught legitimate inflections or variants that you and your regex rules overlooked, adopt those specific <code>&lt;choice&gt;</code> blocks into your master file. Attribute them with <code>resp="#gemini"</code>.</li>
  <li><strong>Reject All AI Hypercorrections (Category B):</strong> Where the AI model committed lexical substitution or dialect erasure, ensure that the original witness reading remains clean and unaltered.</li>
  <li><strong>Resolve Complex Ambiguities (Category C):</strong> Where automated tools failed on damaged text or poetic punctuation, verify that your manual paleographical encoding correctly uses <code>&lt;unclear&gt;</code> or preserved dashes.</li>
</ol>

The resulting document represents the gold standard of digital scholarship: a human-curated text enhanced by computational speed and artificial intelligence, where every single character has been verified by a responsible scholar.

**Vocabulary.** *Scholarly synthesis* — Constructing a final authoritative text by critically selecting the strongest verified readings across manual, algorithmic, and AI passes. *Curated edition* — A digital text where automated suggestions have been vetted and authorized by human editorial judgment.

**Takeaway:** The final normalized file synthesizes the best of all three passes, adopting valid AI discoveries while rejecting automated hypercorrections under human oversight.

---

## **25 Content**

**Documenting AI Attribution in the TEI Header**

In academic digital scholarship, using artificial intelligence is completely acceptable—provided that it is **transparently acknowledged and attributed**. Secretly using AI to generate markup and presenting it as your own manual work is a grave breach of academic integrity.

The TEI Header provides built-in mechanisms for attributing automated and artificial intelligence contributions (TEI Consortium, 2024).

In your `transcription_normalized.xml` file, update your TEI Header in two specific places:

<ol>
  <li><strong>In `<titleStmt>`:</strong> Add a formal statement of responsibility recording the AI model used in the workflow:
    <pre><code>&lt;titleStmt&gt;
  &lt;title&gt;Normalized Edition of Witness RG 1 Vol 430 No 2&lt;/title&gt;
  &lt;author&gt;Ken Penner&lt;/author&gt;
  &lt;respStmt&gt;
    &lt;resp&gt;Manual normalization, policy design, and editorial audit&lt;/resp&gt;
    &lt;name xml:id="editor"&gt;Ken Penner&lt;/name&gt;
  &lt;/respStmt&gt;
  &lt;respStmt&gt;
    &lt;resp&gt;Automated normalization suggestions generated by Gemini 2.5 Pro via VS Code Antigravity&lt;/resp&gt;
    &lt;name xml:id="gemini"&gt;Google Gemini 2.5 Pro&lt;/name&gt;
  &lt;/respStmt&gt;
&lt;/titleStmt&gt;</code></pre>
  </li>
  <li><strong>In `<revisionDesc>`:</strong> Log the date, model, and nature of the automated pass:
    <pre><code>&lt;revisionDesc&gt;
  &lt;change when="2026-10-09" who="#editor"&gt;Synthesized final normalized edition; audited AI suggestions from #gemini and rejected 4 hypercorrections.&lt;/change&gt;
&lt;/revisionDesc&gt;</code></pre>
  </li>
</ol>

Notice how this transparently records the collaboration: the human editor is named as the primary authority, the AI model is acknowledged as an automated contributor, and every tag carrying `resp="#editor"` or `resp="#gemini"` resolves to a valid identifier in the header.

**Vocabulary.** *AI attribution* — Transparently documenting the specific AI models, versions, and prompting workflows used to generate digital edition markup. *`<respStmt>`* — The TEI Header element defining roles and responsibilities of all human and automated project contributors.

**Takeaway:** Transparently attribute AI assistance in your TEI Header using `<respStmt>` and `<change>` tags, linking `resp="#gemini"` to an explicit model identifier.

---

## **26 Content**

**Writing the Comparative Reflection Report**

The final component of Workshop 6 is composing your **Comparative Reflection Report**, recorded in `NORMALIZATION.md`.

Your report should be between **300 and 500 words**, written in clear academic prose. It synthesizes your findings from the three-way audit and evaluates what the exercise revealed about your document.

Structure your report into four distinct sections:

<ol>
  <li><strong>Methodological Overview (approx. 75 words):</strong> Briefly describe your 20-line passage and state the core principles of your Editorial Regularization Policy.</li>
  <li><strong>Quantitative Results (approx. 100 words):</strong> Report your empirical metrics in a clean markdown table:
    <ul>
      <li>Deterministic Regex: True Positives, False Positives, Precision, Recall.</li>
      <li>Generative AI: True Positives, False Positives, Hypercorrection Rate, Precision, Recall.</li>
    </ul>
  </li>
  <li><strong>Discrepancy Analysis (approx. 200 words):</strong> Discuss at least one concrete example from each discrepancy category:
    <ul>
      <li>One Category A instance where AI succeeded over regex.</li>
      <li>One Category B instance where regex protected text from an AI hypercorrection.</li>
      <li>One Category C instance where both automated tools struggled.</li>
    </ul>
  </li>
  <li><strong>Scholarly Conclusion (approx. 75 words):</strong> Conclude with a reflection on how automated tools impact the preservation of historical language and dialect in your specific witness.</li>
</ol>

This report is where you earn your grade. It demonstrates that you are not merely a technician running software, but a critical humanist capable of evaluating computational tools with scholarly rigor.

**Vocabulary.** *Comparative reflection report* — A structured academic synthesis evaluating the empirical performance and qualitative trade-offs of manual, regex, and AI text processing.

**Takeaway:** Structure your 300–500 word reflection report around your policy overview, quantitative metrics table, discrepancy analysis, and scholarly conclusions.

---

## **27 Content**

**Ethical Dimensions of AI in Cultural Heritage**

Before completing our study of automated normalization, we must pause to consider the broader **ethical and political dimensions of artificial intelligence in digital humanities**.

Artificial intelligence models are not neutral, objective mathematical conduits. They are commercial technologies built by multinational corporations, trained on contemporary internet data that overwhelmingly reflects standard, wealthy, modern Anglo-American cultural norms (Pierazzo, 2015).

When an AI model encounters historical documents, it instinctively attempts to discipline those documents:
<ul>
  <li>It flattens working-class vernacular voices (like Maud Lewis) into corporate business English.</li>
  <li>It smooths over the idiosyncratic, resistant rhythms of female poets (like Emily Dickinson) into standard Victorian metrics.</li>
  <li>It homogenizes non-standard regional spellings, erasing the rich diversity of historical dialects.</li>
</ul>

If digital scholars blindly accept AI-generated text without rigorous manual auditing, we risk creating a homogenized, algorithmic digital archive where the authentic linguistic friction of the past has been quietly scrubbed away.

The role of the digital humanist is to stand as a guardian of historical alterity. We use artificial intelligence to accelerate indexing and accessibility, but we never allow an algorithm to decide what the past sounded like. The scholar's critical eye remains the ultimate ethical defense of human memory.

**Vocabulary.** *Linguistic homogenization* — The erasure of regional, dialectal, and historical linguistic diversity by automated AI language models. *Historical alterity* — The fundamental, authentic difference of past languages, cultures, and mindsets from modern contemporary norms.

**Takeaway:** Digital humanists must ethically guard against AI linguistic homogenization, ensuring that automated tools never erase the authentic, non-standard voices of historical writers.

---

## **28 Content**

**Validating the Final Normalized Edition**

Before committing your files to Git and submitting Workshop 6, you must conduct a comprehensive **validation sweep** across your entire project repository.

In digital editing, an unvalidated XML file is considered broken. A single syntax error prevents TEI Publisher, web browsers, or search engines from reading your document.

Complete this pre-submission validation checklist in VS Code:

<ol>
  <li><strong>Verify XML Schema Compliance:</strong> Open <code>transcription_normalized.xml</code>. Open the Problems panel (<code>Cmd+Shift+M</code>). Confirm that the document displays <strong>0 errors</strong> against your project's RELAX NG schema.</li>
  <li><strong>Check Milestone Integrity:</strong> Search for <code>&lt;lb/&gt;</code> tags. Verify that every single line break from your consensus diplomatic text is present, in order, with its original line number intact.</li>
  <li><strong>Audit Attribution Tags:</strong> Ensure that every `<reg>` and `<expan>` element carries an authorized `@resp` attribute pointing to a valid identifier in the TEI Header (`#editor` or `#gemini`).</li>
  <li><strong>Confirm Non-Destructive Markup:</strong> Verify that no raw text was deleted; every normalization must exist as a parallel pairing inside a valid <code>&lt;choice&gt;</code> block.</li>
</ol>

When your Problems panel displays a clean green checkmark with zero errors, your digital edition satisfies the highest technical standards of professional scholarship.

**Vocabulary.** *Validation sweep* — An exhaustive pre-publication review verifying schema conformance, milestone preservation, and attribution accuracy across all project files. *Zero-error baseline* — The mandatory technical standard requiring digital edition files to pass schema validation without syntax violations.

**Takeaway:** Conduct an exhaustive validation sweep before submission, ensuring your final normalized XML passes schema validation with zero errors and preserves all milestones.

---

## **29 Content**

**Preparing for Week 7: Collation**

Congratulations! By completing Week 6, you have mastered the first four foundational stages of the scholarly editing pipeline:
<ol>
  <li><strong>Cataloguing & Metadata (Module 2):</strong> Creating the TEI Header and authority files.</li>
  <li><strong>Imaging & IIIF (Module 3):</strong> Binding facsimile images to structural canvas zones.</li>
  <li><strong>Diplomatic Transcription (Module 4):</strong> Keying the physical witness line by line.</li>
  <li><strong>Reconciliation & Normalization (Modules 5 & 6):</strong> Building a consensus text and encoding parallel standardizations and abbreviation expansions.</li>
</ol>

Your document is now in pristine condition. It preserves the exact historical handwriting of the witness, while simultaneously providing modern standard lemmas and expanded abbreviations for automated computational tools.

Where do we go next?

After next week's **Fall Study Break (Oct 12–16)**, we return in **Week 7 (Module 07: Collation)** to confront the fundamental challenge of textual criticism: **comparing multiple witnesses of the same work**.

In Week 7, you will take your normalized text and compare it against alternative manuscript witnesses or printed editions of the same text. You will learn to perform manual collation on paper, run automated multi-witness alignment algorithms using the **CollateX** engine, and deploy AI models to classify textual variants into substitutions, additions, omissions, and transpositions.

Your normalized text is the essential engine that makes automated collation possible: because you regularized spelling, CollateX will align the words correctly rather than stumbling over superficial orthographic noise!

**Vocabulary.** *Textual collation* — The systematic comparison of multiple physical witnesses of the same work to identify, record, and analyze textual variations. *CollateX* — The premier open-source algorithmic engine used by digital humanists to align and collate multi-witness texts.

**Takeaway:** Your normalized text provides the clean baseline needed for Week 7, where you will use CollateX to align and collate multiple historical witnesses.

---

## **30 Content**

**Review and Workshop 6 Master Checklist**

Today you brought Week 6 to its triumphant scholarly conclusion. You explored the capabilities of generative artificial intelligence, constructed negative prompts, diagnosed hypercorrections, executed a three-way comparative audit, and synthesized a final normalized digital edition.

Before submitting Workshop 6, review the **Master Deliverables Checklist**:

<ol>
  <li><strong>Consensus Excerpt Base:</strong> A clean 20-line passage from <code>transcription_reconciled.xml</code>.</li>
  <li><strong>File 1 (Manual Pass):</strong> <code>transcription_reconciled_manual.xml</code> hand-encoded with validated TEI <code>&lt;choice&gt;</code> markup in Lesson 6.1.</li>
  <li><strong>File 2 (Regex Pass):</strong> <code>transcription_reconciled_regex.xml</code> automated using XML-safe regular expressions in Lesson 6.2.</li>
  <li><strong>File 3 (AI Pass):</strong> <code>transcription_reconciled_ai.xml</code> generated by Gemini in VS Code Antigravity with strict negative prompts in Lesson 6.3.</li>
  <li><strong>File 4 (Final Synthesis):</strong> <code>transcription_normalized.xml</code> synthesizing the best verified readings across all passes, validated with 0 schema errors.</li>
  <li><strong>Documentation in `NORMALIZATION.md`:</strong>
    <ul>
      <li>Your explicit Editorial Regularization Policy statement.</li>
      <li>Your completed Rule Ledger cataloguing Rule IDs, descriptions, regex patterns, and replacements.</li>
      <li>Your 300–500 word Comparative Reflection Report containing your metrics table and Category A, B, and C discrepancy analysis.</li>
    </ul>
  </li>
  <li><strong>TEI Header Updated:</strong> Transparent attribution recorded in <code>&lt;editorialDecl&gt;</code> and <code>&lt;respStmt&gt;</code> with <code>resp="#gemini"</code>.</li>
</ol>

Commit your files to your local repository. Enjoy your well-earned Fall Study Break next week, and return ready to conquer multi-witness collation in Week 7!

**Vocabulary.** *Master checklist* — The comprehensive verification inventory ensuring all code, XML data, and analytical documentation are complete and validated before submission.

**Takeaway:** Completing the Master Checklist guarantees that your workshop submission contains all four XML passes, a documented Rule Ledger, and an audited reflection report.

---

## References

Bollmann, M. (2019). A large-scale comparison of historical text normalization systems. In *Proceedings of the 2019 conference of the North American chapter of the Association for Computational Linguistics: Human language technologies* (Vol. 1, pp. 3887–3898). Association for Computational Linguistics. https://doi.org/10.18653/v1/N19-1389

Burnard, L. (2014). *What is the Text Encoding Initiative? How to add intelligent markup to digital resources*. OpenEdition Press. https://doi.org/10.4000/books.oep.426

Jurafsky, D., & Martin, J. H. (2024). *Speech and language processing: An introduction to natural language processing, computational linguistics, and speech recognition* (3rd ed. draft). Stanford University. https://web.stanford.edu/~jurafsky/slp3/

Pierazzo, E. (2015). *Digital scholarly editing: Theories, models and methods*. Ashgate Publishing.

TEI Consortium. (2024). *TEI P5: Guidelines for electronic text encoding and interchange* (version 4.8.0). TEI Consortium. https://tei-c.org/guidelines/p5/
