# Lesson 8.1 — Manual Grammatical Parsing, Lemmatization, and TEI Linguistic Markup

*RELS 398 / ENGL 398 · Topic 8: Lemmatization · Meeting #20 (Tue Oct 27)*

***Step 1 of the three-step cycle: manual.** Today you parse, lemmatize, and record morphological feature bundles for a passage by hand using authoritative lexica. That gold-standard annotation is the reference for Wednesday's rule-based taggers and Friday's AI evaluation.*

---

## **01 Content**

**Words Beyond Strings: Why Editions Need Linguistic Markup**

Over the past seven weeks, you built a real digital edition from scratch. You catalogued your primary witness in a `teiHeader`. You linked high-resolution images with `<facsimile>`. You transcribed every line as written. You reconciled your readings against an AI pass. In Module 6, you regularized historical spelling variations using `<choice>`. Last week, in Module 7, you wrote stylesheets to turn those markup layers into clean reading views.

Throughout all those steps, your computer treated your text as a string of letters. String searches can find exact words. However, a search cannot understand grammar. A computer cannot deduce that *treaties*, *treaty*, and *treaty's* belong to the same word family. It cannot tell whether *left* in Maud Lewis's letter means a direction or the past tense of *leave*. In Ace's 1791 French decree, a search for *décrète* misses *décrété* or *décrétèrent* unless an editor connects them.

Linguistic markup solves this problem. It adds parts of speech, dictionary headwords, and grammatical details to your text. This turns a simple transcript into a powerful research database. Scholars can search for all past-tense verbs or all adjectives that modify a legal title. Today, you will build this grammatical ground truth by hand.

**Vocabulary.** *Linguistic Markup* — Adding grammatical labels and dictionary forms to words in an electronic text. *String Search* — Searching text strictly for matching characters without understanding grammar.

**Takeaway:** String searches only find exact character matches; linguistic markup reveals the grammar and word families beneath the text.

---

## **02 Content**

**Tokens, Surface Forms, and Dictionary Lemmas**

To study text with computers, you must know three basic terms: token, surface form, and lemma.

A **token** is a single instance of a word or punctuation mark in your text. If the word *the* appears fifty times on a manuscript page, it counts as fifty tokens.

A **surface form** is the exact spelling of that token on the historical page. In Andromeda's 1752 Treaty, the surface form might be *promis'd* or *acknowledg'd*. In Ace's 1791 decree, it might be *décrété* or the older spelling *décrétoit*. Surface forms preserve every scribal quirk, ink blot, and historical spelling.

A **lemma** is the base headword you look up in a dictionary. For *promis'd*, *promises*, and *promising*, the English lemma is the base verb *promise*. For *treaties*, the lemma is *treaty*. In French, verbs are listed under their infinitive form (*décréter*). Nouns are listed in the singular (*loi*). Lemmatization means connecting each surface word on the page to its dictionary lemma.

**Vocabulary.** *Token* — An individual word or mark in a text. *Surface Form* — The exact spelling written on the manuscript page. *Lemma* — The base dictionary headword representing a group of related word forms.

**Takeaway:** Lemmatization links inflected surface words from the manuscript to their standard dictionary headwords.

---

## **03 Content**

**The Grammatical Feature List**

Words do more than carry dictionary meanings. In a sentence, words take on different shapes to show their grammatical job. The collection of grammatical traits on a single word is its **feature list**.

Look at the word *writes* in Maud Lewis's letters: *She writes to Mr. Kinnear*. The dictionary lemma is *write*. Its feature list tells us more: Part of Speech = Verb, Person = Third, Number = Singular, and Tense = Present. In English, pronouns change shape for case: *she* is a subject, while *her* is an object or possessive.

French uses rich feature lists for nearly every word. In the 1791 phrase *les assemblées nationales*, the noun *assemblées* is Feminine and Plural. The adjective *nationales* matches those traits through agreement. When you parse a word by hand, you record both its dictionary headword and its full list of grammatical features.

**Vocabulary.** *Word Form* — The specific grammatical shape an inflected word takes in a sentence. *Feature List* — The set of grammatical tags (such as tense, person, number, and gender) that describe a word.

**Takeaway:** A grammatical feature list records all traits—including part of speech, tense, person, gender, and number—for an inflected word.

---

## **04 Content**

**Tokenization in Real Historical Documents**

Before you can tag or lemmatize words, you must separate your text into tokens. In modern English books, software simply splits text at spaces and punctuation. In old documents, tokenization is trickier.

Consider the contractions in Maud Lewis's letters: *can't*, *didn't*, *it's*, and *I'll*. Is *can't* one token or two? Linguistically, it represents two words: the helping verb *can* and the negative word *not*. If you keep them together, software cannot find a dictionary entry for *can't*. If you split them into *can* and *n't*, both parts receive clean tags and lemmas.

In Ace's 1791 French decree, short words often cling to nouns: *l'assemblée*, *d'état*, *qu'un*. The letter *l'* is the definite article *le*. The word *assemblée* is a noun. Standard French tools split *l'assemblée* into two tokens: *l'* (lemma *le*) and *assemblée*. In old English treaties, phrases like *whereof* and *thereunto* fuse words together. Your tokenization rules decide where each token begins and ends.

**Vocabulary.** *Tokenization* — Splitting running text into distinct words, symbols, and punctuation marks. *Clitic* — A short word that attaches phonetically to a neighbor, like French *l'* or English *'ve*.

**Takeaway:** Tokenization must split contracted words so that each underlying word receives its own lemma and grammatical tag.

---

## **05 Content**

**Words with Multiple Meanings: Homographs**

A major hurdle in grammar tagging is double meanings. In natural human language, one written spelling can represent two completely different words. Words that share an identical spelling but differ in meaning or origin are called **homographs**.

English has thousands of homographs. In the 1752 Treaty, the word *will* appears in two ways. It can be a helping verb (*the Tribe will observe this Treaty*). It can also be a noun (*of their own free will*). The spelling is identical, but the lemmas and parts of speech are totally different. If a computer guesses without reading the sentence, it often makes a mistake.

French has the same double meanings. The token *est* can be a form of the verb *être* ("is"). It can also be the noun *est* meaning the East. The word *son* can mean "his" or "sound". Human readers resolve these puzzles easily by looking at the sentence context. Automated programs often trip over them.

**Vocabulary.** *Homograph* — A word spelled the same as another word but with a different meaning or part of speech. *Disambiguation* — Picking the correct meaning or grammatical tag for an ambiguous word in context.

**Takeaway:** Human readers use sentence context to pick the right lemma when two different words share the same spelling.

---

## **06 Content**

**Verbs: Tense, Person, and Agreement**

Verbs form the backbone of sentences in English and French. In historical texts, verb endings reveal who acted, when they acted, and whether the action was finished.

In English, verbs change shape to match third-person subjects (*she paints*, *he writes*). Older English used distinct verb endings (*thou dost*, *he hath*, *she speaketh*). The 1752 Treaty uses formal legal style: *doth hereby promise and grant*. The lemma for *doth* is *do*. Its features are Verb, Present Tense, Third Person, Singular.

French verbs have rich sets of endings. In Ace's 1791 decree, you find past-tense forms like *décréta* (past definite), *décrétoit* (older spelling of the imperfect), and *a décrété* (compound past). In all three cases, the base dictionary lemma is *décréter*. When tagging verbs, editors separate main verbs that take subjects from infinitives and participles.

**Vocabulary.** *Finite Verb* — A verb that has a person and tense and serves as the main predicate of a clause. *Infinitive* — The uninflected base form of a verb, such as *to write* or *décréter*.

**Takeaway:** Verb endings show tense, person, and number; manual parsing identifies both the inflected form and its base dictionary infinitive.

---

## **07 Content**

**Nouns and Adjectives: Gender and Number**

Nouns name people, places, things, and ideas. Adjectives describe nouns. In modern English, nouns change for number (singular *letter*, plural *letters*) and possession (*Maud's*). English adjectives never change shape for gender or number. The word *red* stays the same whether describing one apple or ten.

French works differently. Every French noun has a grammatical gender: masculine or feminine. French nouns also show singular or plural number. Adjectives must match their noun in both gender and number. In the phrase *décrets nationaux* (national decrees), *décrets* is masculine plural. The adjective *nationaux* changes its ending to agree with it. Its base lemma is *national*.

In English historical documents, pronouns still show case (*they*, *them*, *their*). Knowing whether a word is a subject, an object, or a modifier helps you understand the legal force of an old document.

**Vocabulary.** *Agreement* — When modifying words match their head noun in gender, number, or case. *Grammatical Gender* — A noun class system (masculine or feminine) that controls how modifiers change.

**Takeaway:** French adjectives change their endings to agree with nouns, while English words mainly show number and possession.

---

## **08 Content**

**Function Words: Determiners, Prepositions, and Conjunctions**

Linguists divide words into two big groups: content words and function words. **Content words**—nouns, main verbs, adjectives, and adverbs—carry specific real-world meaning. Languages invent new content words all the time.

**Function words**, on the other hand, act as grammatical glue. They include determiners (*the*, *a*, *le*, *ces*), prepositions (*in*, *by*, *sur*, *dans*), and conjunctions (*and*, *but*, *et*, *ou*). Languages rarely add new function words. While they do not change shape often, function words show how clauses fit together.

In the 1752 Treaty, prepositions and conjunctions link long legal clauses: *between His Excellency Peregrine Thomas Hopson... and Major Jean Baptiste Cope*. Here, *between* and *and* link names and titles into a clear legal partnership. In your parsing, pay careful attention to function words.

**Vocabulary.** *Content Words* — Words like nouns and verbs that carry real-world meaning. *Function Words* — Words like prepositions and conjunctions that connect phrases and show grammar.

**Takeaway:** Function words link nouns and verbs together into complete, well-structured sentences.

---

## **09 Content**

**The Universal Dependencies Part-of-Speech Tagset**

To help projects share linguistic data across languages, linguists built the **Universal Dependencies (UD)** project. UD created a standard list of 17 Universal Part-of-Speech (UPOS) tags.

Instead of making up private tags, everyone uses the same labels. Here are the core tags you will use for our course documents:

<table>
  <thead>
    <tr>
      <th>Tag</th>
      <th>Meaning</th>
      <th>Examples in English and French</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>NOUN</code></td>
      <td>Common noun</td>
      <td>treaty, letter, assemblée, décrets</td>
    </tr>
    <tr>
      <td><code>PROPN</code></td>
      <td>Proper name</td>
      <td>Hopson, Cope, France, Paris</td>
    </tr>
    <tr>
      <td><code>VERB</code></td>
      <td>Main verb</td>
      <td>promise, write, décrète, signer</td>
    </tr>
    <tr>
      <td><code>AUX</code></td>
      <td>Helping verb</td>
      <td>shall, will, have, est, ont</td>
    </tr>
    <tr>
      <td><code>ADJ</code></td>
      <td>Adjective</td>
      <td>peaceable, good, national, royal</td>
    </tr>
    <tr>
      <td><code>DET</code></td>
      <td>Determiner</td>
      <td>the, this, le, la, ces</td>
    </tr>
    <tr>
      <td><code>ADP</code></td>
      <td>Preposition</td>
      <td>in, between, par, dans</td>
    </tr>
    <tr>
      <td><code>CCONJ</code></td>
      <td>Coordinating conjunction</td>
      <td>and, but, et, ou</td>
    </tr>
    <tr>
      <td><code>PUNCT</code></td>
      <td>Punctuation</td>
      <td>., ,, ;, :</td>
    </tr>
  </tbody>
</table>

Using standard UPOS tags means tools can compare Ace's 1791 French decree directly with Andromeda's 1752 English treaty.

**Vocabulary.** *Universal Dependencies (UD)* — An open global standard for grammar annotation across languages. *UPOS* — Universal Part-of-Speech tags, a set of 17 standard labels.

**Takeaway:** The 17 Universal Dependencies UPOS tags give researchers a shared vocabulary for tagging parts of speech across languages.

---

## **10 Content**

**Standard Grammatical Features (FEATS)**

A UPOS tag tells you a word's broad class (like `NOUN` or `VERB`). It does not record details like past tense or plural number. In Universal Dependencies, those details live in a field called **FEATS** (Features).

FEATS uses simple pairs separated by vertical bars. For example, the French noun *décrets* in Ace's text gets: `Gender=Masc|Number=Plur`. The English verb *promised* gets: `Tense=Past|VerbForm=Fin`.

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Common Values</th>
      <th>Simple Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>Number</code></td>
      <td><code>Sing</code>, <code>Plur</code></td>
      <td>treaty (Sing), treaties (Plur)</td>
    </tr>
    <tr>
      <td><code>Gender</code></td>
      <td><code>Masc</code>, <code>Fem</code></td>
      <td>roi (Masc), reine (Fem)</td>
    </tr>
    <tr>
      <td><code>Tense</code></td>
      <td><code>Past</code>, <code>Pres</code></td>
      <td>wrote (Past), writes (Pres)</td>
    </tr>
    <tr>
      <td><code>Person</code></td>
      <td><code>1</code>, <code>2</code>, <code>3</code></td>
      <td>am (1), is (3)</td>
    </tr>
    <tr>
      <td><code>VerbForm</code></td>
      <td><code>Fin</code>, <code>Inf</code>, <code>Part</code></td>
      <td>writes (Fin), write (Inf), written (Part)</td>
    </tr>
  </tbody>
</table>

Standard feature names let researchers search across many files for exact grammar forms, such as all feminine plural adjectives.

**Vocabulary.** *FEATS* — The field in Universal Dependencies that holds specific grammatical traits like tense and number.

**Takeaway:** The FEATS field records specific grammatical details using simple pairs like `Gender=Masc` and `Number=Plur`.

---

## **11 Content**

**Authoritative Dictionaries as Citation Baselines**

How do you decide on the official lemma for an old word? In everyday life, people guess word origins. In scholarly editing, every lemma must come from an authoritative dictionary.

For historical English texts—including the 1752 Treaty and Maud Lewis's letters—our primary authority is the **Oxford English Dictionary (OED)**. The OED tracks spelling history and gives standard modern headwords. If a word is archaic, like *whereunto*, the OED confirms its canonical dictionary entry.

For French texts, the primary baseline is the **Trésor de la Langue Française informatisé (TLFi)** and the historical dictionaries of the Académie française. When lemmatizing words in Ace's 1791 decree, checking the TLFi ensures that 18th-century government words map to the headwords recognized by scholars.

**Vocabulary.** *Citation Baseline* — The standard scholarly dictionary chosen to govern lemma spellings in an edition. *OED* — Oxford English Dictionary, the historical authority for English. *TLFi* — Trésor de la Langue Française informatisé, the primary digital lexicon for French.

**Takeaway:** Every lemma should be checked against an authoritative dictionary, such as the OED for English or the TLFi for French.

---

## **12 Content**

**TEI XML Word Elements: `<w>` and `<pc>`**

The Text Encoding Initiative provides clean tags to mark words and punctuation directly in XML. The two most important tags are `<w>` (word) and `<pc>` (punctuation character).

The `<w>` tag wraps a single word. Punctuation marks go inside `<pc>`. Here is how a short clause from the 1752 Treaty looks when segmented into TEI elements:

```xml
<w>The</w>
<w>said</w>
<w>Chief</w>
<w>doth</w>
<w>promise</w>
<pc>,</pc>
```

Wrapping words in `<w>` makes token boundaries unmistakable for software. Normal spaces between words remain in the file, but programs process each `<w>` tag as one unit. The `<pc>` tag marks punctuation clearly, preventing search tools from treating a comma as part of a word.

**Vocabulary.** *`<w>`* — The TEI tag that encloses a single grammatical word token. *`<pc>`* — The TEI tag that encloses a punctuation mark or symbol.

**Takeaway:** Use the TEI `<w>` element to enclose words and the `<pc>` element to enclose punctuation marks.

---

## **13 Content**

**Adding Attributes: `@lemma` and `@pos`**

Wrapping words in `<w>` is only the first step. To add grammatical information, you include attributes. The two main attributes are `@lemma` and `@pos`.

The `@lemma` attribute holds the dictionary headword. The `@pos` attribute holds the part-of-speech tag. Here is the same 1752 clause enriched with linguistic attributes:

```xml
<w lemma="the" pos="DET">The</w>
<w lemma="say" pos="VERB">said</w>
<w lemma="chief" pos="NOUN">Chief</w>
<w lemma="do" pos="AUX">doth</w>
<w lemma="promise" pos="VERB">promise</w>
<pc pos="PUNCT">,</pc>
```

Look at what this achieves. The surface form *said* connects to its dictionary headword *say*. The old auxiliary *doth* connects to *do*. A reader sees the original historical words on screen, while a search engine can find *do* and *promise* across the whole collection.

**Vocabulary.** *`@lemma`* — The TEI attribute holding the dictionary headword. *`@pos`* — The TEI attribute holding the part-of-speech tag.

**Takeaway:** Adding `@lemma` and `@pos` to `<w>` tags attaches dictionary headwords and grammar tags without altering the original text.

---

## **14 Content**

**Grammar Tags vs. Spelling Normalization**

In Module 6, you learned how to clean up historical spellings using `<choice>`, `<orig>`, and `<reg>`. Students often ask: is lemmatization just another kind of spelling normalization?

They are two distinct tasks. Spelling normalization updates historical spelling; lemmatization identifies the base grammatical word. In the 1752 Treaty, the scribe wrote *acknowledg'd*. In Module 6, you normalized that spelling to *acknowledged*:

```xml
<choice>
  <orig>acknowledg'd</orig>
  <reg>acknowledged</reg>
</choice>
```

Notice that *acknowledged* is still an inflected past-tense verb! It is not the dictionary headword; the headword is the infinitive *acknowledge*. When combining both layers, TEI nests the regularized `<choice>` tag inside the linguistic `<w>` tag:

```xml
<w lemma="acknowledge" pos="VERB">
  <choice>
    <orig>acknowledg'd</orig>
    <reg>acknowledged</reg>
  </choice>
</w>
```

This nesting keeps both editorial choices clear: you standardized the spelling to *acknowledged*, and you mapped the word to the lemma *acknowledge*.

**Takeaway:** Normalization updates spelling, while lemmatization identifies the base word; in TEI XML, `<choice>` nests inside `<w>`.

---

## **15 Content**

**External Feature Links with `@ana`**

When grammatical annotations grow complex, writing long lists of traits inside tag attributes can make XML hard to read. TEI provides the `@ana` (analysis) attribute to link a word to an external definition.

Instead of writing long strings of features, an editor defines grammatical categories in a feature list inside the `teiHeader`. Then, the `<w>` tag points to that definition using a link:

```xml
<w lemma="assemblée" pos="NOUN" ana="#fem_sing">assemblée</w>
```

In the header, `#fem_sing` points to an entry that defines the word as Feminine and Singular. This method, called **stand-off annotation**, keeps your main transcription neat while storing rich linguistic data. For class labs, inline `@lemma` and `@pos` attributes are plenty, but large projects use `@ana` often.

**Vocabulary.** *`@ana`* — A TEI attribute that points to an external analysis definition. *Stand-Off Annotation* — Storing notes and linguistic data in a separate place from the main text.

**Takeaway:** The `@ana` attribute links words to external feature lists, keeping transcripts clean while supporting deep grammatical notes.

---

## **16 Content**

**Marking Sentences with `<s>`**

Grammar does not end with single words; it also shapes sentences. In TEI P5, complete sentences are wrapped in the `<s>` (sentence) tag.

Grouping words into `<s>` elements is essential for studying syntax. Grammar rules—such as a subject matching its verb—work within sentence boundaries. Here is an example using `<s>`, `<w>`, and `<pc>` together:

```xml
<s>
  <w lemma="the" pos="DET">The</w>
  <w lemma="treaty" pos="NOUN">Treaty</w>
  <w lemma="be" pos="AUX">was</w>
  <w lemma="sign" pos="VERB">signed</w>
  <pc pos="PUNCT">.</pc>
</s>
```

Notice how punctuation marks sit in `<pc>` tags. This cleanly separates words from sentence endings. In historical texts, punctuation is often irregular. Marking sentence boundaries by hand helps grammar tools parse clauses correctly.

**Vocabulary.** *`<s>`* — The TEI element that marks a grammatical sentence.

**Takeaway:** Wrapping clauses in `<s>` elements marks sentence boundaries that guide grammatical analysis.

---

## **17 Content**

**Parsing Walkthrough 1: The 1752 Peace and Friendship Treaty**

Let us look at a hands-on manual parse from Andromeda's project: the 1752 Peace and Friendship Treaty.

Consider this opening clause: *All Treaties shall be renewed*. Here is the grammatical breakdown in a clear table:

<table>
  <thead>
    <tr>
      <th>Surface Word</th>
      <th>Lemma</th>
      <th>UPOS</th>
      <th>Features (FEATS)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>All</td>
      <td>all</td>
      <td><code>DET</code></td>
      <td>PronType=Tot</td>
    </tr>
    <tr>
      <td>Treaties</td>
      <td>treaty</td>
      <td><code>NOUN</code></td>
      <td>Number=Plur</td>
    </tr>
    <tr>
      <td>shall</td>
      <td>shall</td>
      <td><code>AUX</code></td>
      <td>VerbForm=Fin</td>
    </tr>
    <tr>
      <td>be</td>
      <td>be</td>
      <td><code>AUX</code></td>
      <td>VerbForm=Inf</td>
    </tr>
    <tr>
      <td>renewed</td>
      <td>renew</td>
      <td><code>VERB</code></td>
      <td>Tense=Past|VerbForm=Part</td>
    </tr>
  </tbody>
</table>

Notice how each token receives an exact analysis. *Treaties* maps to the singular lemma *treaty*. The verb group *shall be renewed* breaks down into a helping verb (`shall`), a helping infinitive (`be`), and a main past participle (`renewed`, lemma *renew*).

**Takeaway:** Breaking old legal clauses into tables makes lemmas, parts of speech, and grammatical features clear and simple.

---

## **18 Content**

**Parsing Walkthrough 2: The 1791 French Revolutionary Decree**

Now let us examine a government clause from Ace's project: a 1791 decree from the National Assembly of Revolutionary France.

Consider this line: *L'Assemblée nationale décrète les lois suivantes* ("The National Assembly decrees the following laws"). Because French features rich agreement and clitics, we look closely at each ending:

<table>
  <thead>
    <tr>
      <th>Surface Word</th>
      <th>Lemma</th>
      <th>UPOS</th>
      <th>Features (FEATS)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>L'</td>
      <td>le</td>
      <td><code>DET</code></td>
      <td>Gender=Fem|Number=Sing|PronType=Art</td>
    </tr>
    <tr>
      <td>Assemblée</td>
      <td>assemblée</td>
      <td><code>NOUN</code></td>
      <td>Gender=Fem|Number=Sing</td>
    </tr>
    <tr>
      <td>nationale</td>
      <td>national</td>
      <td><code>ADJ</code></td>
      <td>Gender=Fem|Number=Sing</td>
    </tr>
    <tr>
      <td>décrète</td>
      <td>décréter</td>
      <td><code>VERB</code></td>
      <td>Number=Sing|Person=3|Tense=Pres|VerbForm=Fin</td>
    </tr>
    <tr>
      <td>les</td>
      <td>le</td>
      <td><code>DET</code></td>
      <td>Number=Plur|PronType=Art</td>
    </tr>
    <tr>
      <td>lois</td>
      <td>loi</td>
      <td><code>NOUN</code></td>
      <td>Gender=Fem|Number=Plur</td>
    </tr>
    <tr>
      <td>suivantes</td>
      <td>suivant</td>
      <td><code>ADJ</code></td>
      <td>Gender=Fem|Number=Plur</td>
    </tr>
  </tbody>
</table>

Look at the matching pairs. *Assemblée* is feminine singular, so *L'* and *nationale* match it. Next, *lois* is feminine plural, and *suivantes* agrees with it. The verb *décrète* maps to its base infinitive *décréter*.

**Takeaway:** French manual parsing requires tracking gender and number agreement across phrases and mapping verbs to infinitives.

---

## **19 Content**

**Parsing Walkthrough 3: Maud Lewis's Folk Correspondence**

For our third walkthrough, we examine a line from Olyvia's project: a handwritten 1967 letter by Maud Lewis to Mr. Kinnear.

Maud Lewis's writing is warm, personal, and informal: *I received your letter today*. Here is the grammatical breakdown:

<table>
  <thead>
    <tr>
      <th>Surface Word</th>
      <th>Lemma</th>
      <th>UPOS</th>
      <th>Features (FEATS)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>I</td>
      <td>I</td>
      <td><code>PRON</code></td>
      <td>Case=Nom|Number=Sing|Person=1|PronType=Prs</td>
    </tr>
    <tr>
      <td>received</td>
      <td>receive</td>
      <td><code>VERB</code></td>
      <td>Tense=Past|VerbForm=Fin</td>
    </tr>
    <tr>
      <td>your</td>
      <td>you</td>
      <td><code>PRON</code></td>
      <td>Person=2|Poss=Yes|PronType=Prs</td>
    </tr>
    <tr>
      <td>letter</td>
      <td>letter</td>
      <td><code>NOUN</code></td>
      <td>Number=Sing</td>
    </tr>
    <tr>
      <td>today</td>
      <td>today</td>
      <td><code>NOUN</code></td>
      <td>Number=Sing</td>
    </tr>
  </tbody>
</table>

Even personal letters benefit from linguistic tags. The possessive pronoun *your* links to its base lemma *you*. The past-tense verb *received* maps to *receive*. Tagging Maud Lewis's letters helps researchers trace her vocabulary and informal writing style across her letters.

**Takeaway:** Personal letters follow standard Universal Dependencies tags, recording informal phrasing and everyday vocabulary clearly.

---

## **20 Content**

**Handling Old Spellings During Lemmatization**

In historical manuscripts, you will often find words with non-standard spellings. Scribes made spelling slips, used local spellings, or followed conventions that changed over time. How should you lemmatize a word with an unusual spelling?

The main rule of lemmatization is simple: **the lemma is always modern and canonical, even when the manuscript spelling is unusual.**

In 18th-century English, words like *publick* or *musick* ended in *ck*. The surface form on the page is *publick*, but the lemma is modern *public*. In 18th-century French, imperfect verbs ended in *-oit* (*faisoit*, *étoit*). The surface spelling is *faisoit*, but its lemma is the standard infinitive *faire*.

If an editor invented an archaic lemma like *faisoir* or *publick*, they would break the dictionary index. A digital edition connects old spellings to modern dictionaries so that readers can search the text using familiar words.

**Vocabulary.** *Canonical Lemma* — The modern standard headword used to index historical spelling variations in a lexicon.

**Takeaway:** Always assign a modern standard dictionary headword as the lemma, no matter how unusual the spelling is on the page.

---

## **21 Content**

**Multi-Word Phrases and Titles**

In many documents, several words work together as a single unit. These are called **multi-word expressions** or compound terms.

In English legal texts, you often find fixed formulas like *in witness whereof*, *peace and friendship*, or *His Excellency*. In French government papers, titles like *procès-verbal* or *assemblée nationale* represent single official ideas.

How do you encode them in TEI? In standard tokenization, each written word gets its own `<w>` tag. However, TEI provides the `<phr>` (phrase) tag to group multi-word expressions together:

```xml
<phr type="legal_formula">
  <w lemma="in" pos="ADP">in</w>
  <w lemma="witness" pos="NOUN">witness</w>
  <w lemma="whereof" pos="ADV">whereof</w>
</phr>
```

This lets search engines analyze each word on its own while still knowing that the three words form a single fixed phrase.

**Vocabulary.** *Multi-Word Expression* — A group of words that functions together as a single phrase or meaning. *`<phr>`* — The TEI element used to group words into grammatical phrases.

**Takeaway:** Group multi-word legal formulas with `<phr>` while keeping individual `<w>` elements for each token.

---

## **22 Content**

**Splitting Contractions for Tagging**

As noted earlier, contractions join two words into one printed unit. When preparing text for tagging, you must decide how to handle these words.

In French, words join with an apostrophe: *d'accord*, *l'homme*, *qu'il*. If you keep *d'accord* as a single word, it has no single part of speech. It is a preposition plus a noun. In TEI XML, you can tag both words while keeping the apostrophe:

```xml
<w lemma="de" pos="ADP">d'</w>
<w lemma="accord" pos="NOUN">accord</w>
```

In English, informal words like *don't* or *they'll* follow the same pattern:

```xml
<w lemma="do" pos="AUX">do</w>
<w lemma="not" pos="ADV">n't</w>
```

Notice how the surface letters are shared between the two `<w>` elements. This preserves the original letters on the page while giving accurate tags to each underlying word.

**Takeaway:** Splitting contracted words across separate `<w>` tags lets each word receive its own lemma and part of speech.

---

## **23 Content**

**Heads and Modifiers: The Heart of Syntax**

Linguistic annotation goes beyond sorting single words; it also shows how words connect in sentences. The central idea of **dependency grammar** is that words connect through links between **heads** and **modifiers**.

In every word pair, one word acts as the head, and the other acts as its dependent modifier. In the phrase *national decree*, the noun *decree* is the head, and the adjective *national* is the modifier. If you drop the adjective, the sentence still makes sense (*The decree was read*). If you drop the noun, the phrase breaks down.

In a full clause, the main verb serves as the root of the sentence. The subject noun depends on the verb, and the direct object depends on the verb. Seeing this structure is the first step toward syntactic treebanking.

**Vocabulary.** *Dependency Grammar* — A grammar model based on links between governing heads and dependent modifiers. *Head* — The main word that governs a grammatical phrase. *Modifier* — A word that depends on a governing head word.

**Takeaway:** Sentences are organized into trees where dependent words connect directly to governing head words.

---

## **24 Content**

**A First Look at Dependency Relations**

Just as Universal Dependencies uses UPOS tags for parts of speech, it uses **relation tags** to label how words connect.

Here are the six most common relation tags you will see in our historical English and French documents:

<table>
  <thead>
    <tr>
      <th>Tag</th>
      <th>Job</th>
      <th>Example (Head → Modifier)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>root</code></td>
      <td>Main sentence verb</td>
      <td>[Sentence] → signed</td>
    </tr>
    <tr>
      <td><code>nsubj</code></td>
      <td>Subject noun</td>
      <td>signed → Chief</td>
    </tr>
    <tr>
      <td><code>obj</code></td>
      <td>Direct object</td>
      <td>signed → Treaty</td>
    </tr>
    <tr>
      <td><code>amod</code></td>
      <td>Adjective modifier</td>
      <td>decree → national</td>
    </tr>
    <tr>
      <td><code>det</code></td>
      <td>Determiner</td>
      <td>decree → the</td>
    </tr>
    <tr>
      <td><code>punct</code></td>
      <td>Punctuation</td>
      <td>signed → .</td>
    </tr>
  </tbody>
</table>

In a sentence like *The Chief signed the Treaty*, the verb *signed* is the `root`. *Chief* is the `nsubj` of *signed*, and *Treaty* is the `obj`. Each noun connects to *the* with a `det` tag. This gives you the basic grammatical skeleton of the sentence.

**Vocabulary.** *Relation Tag* — A label that describes the grammatical link between a head word and a modifier. *`root`* — The central verb that anchors an entire sentence.

**Takeaway:** Standard relation tags like `nsubj`, `obj`, and `amod` label how words connect to their governing heads.

---

## **25 Content**

**The CoNLL-U Plain-Text Format**

In computational linguistics, syntax trees are stored in an open plain-text format called **CoNLL-U**. Every sentence is written as a simple 10-column table.

Each line in a CoNLL-U file represents one token. Here are the ten columns:

<ol>
  <li><strong>ID:</strong> Word number in the sentence (starting at 1).</li>
  <li><strong>FORM:</strong> Word spelling on the page.</li>
  <li><strong>LEMMA:</strong> Dictionary headword.</li>
  <li><strong>UPOS:</strong> Universal part-of-speech tag.</li>
  <li><strong>XPOS:</strong> Local language tag (often <code>_</code>).</li>
  <li><strong>FEATS:</strong> Grammatical features list (or <code>_</code>).</li>
  <li><strong>HEAD:</strong> The ID number of the governing head word (or <code>0</code> for root).</li>
  <li><strong>DEPREL:</strong> Grammatical relation to the head word.</li>
  <li><strong>DEPS:</strong> Extra dependency links (often <code>_</code>).</li>
  <li><strong>MISC:</strong> Extra notes (like <code>SpaceAfter=No</code>).</li>
</ol>

Because CoNLL-U is plain text, any text editor or script can read it easily. On Wednesday, you will see how automated tools output CoNLL-U tables directly.

**Vocabulary.** *CoNLL-U* — The standard 10-column plain-text file format used to store Universal Dependencies sentences.

**Takeaway:** CoNLL-U is the global 10-column text format used to store tokens, lemmas, tags, and syntax trees.

---

## **26 Content**

**Building Your Manual Ground-Truth Table**

Your main task for this week is to build a **manual ground-truth table** for a 20-word excerpt from your project document. This table serves as the benchmark against which automated tools will be tested.

To build your table, follow these four simple steps:
<ol>
  <li><strong>Pick an Excerpt:</strong> Select 20 words in a row from your transcript that form complete clauses.</li>
  <li><strong>Tokenize:</strong> Put each word on its own line, separating punctuation and splitting contractions.</li>
  <li><strong>Look Up Lemmas:</strong> Check each word in your chosen dictionary (OED for English, TLFi for French) to find its canonical headword.</li>
  <li><strong>Tag Grammar:</strong> Assign the right UPOS tag and record features like number, tense, and gender.</li>
</ol>

Do not guess from memory. Check your dictionary and write down your reasons in your notes.

**Vocabulary.** *Ground Truth* — An authoritatively verified dataset built by hand to test automated programs.

**Takeaway:** Your 20-word manual ground-truth table provides the trusted benchmark for testing automated software.

---

## **27 Content**

**Writing Rules in `LEMMATIZATION_POLICIES.md`**

When annotating historical texts, you will run into questions that need consistent answers. Should proper names stay capitalized in lemmas? How should archaic contractions be split? Which dictionary edition sets the rules?

To keep your work consistent, record these decisions in a file called `LEMMATIZATION_POLICIES.md`.

Your policy file should answer three simple questions:
<ol>
  <li><strong>Dictionary Authority:</strong> Which dictionary governs headwords (e.g., OED, TLFi)?</li>
  <li><strong>Capitalization Rules:</strong> Are proper names capitalized in lemmas (e.g., *France*, *Hopson*) while common nouns stay lower-case?</li>
  <li><strong>Contraction Rules:</strong> Exactly where are contractions split, and how are missing letters recorded?</li>
</ol>

Writing these choices down ensures that your edition remains consistent across every page.

**Vocabulary.** *Policy Ledger* — A document recording your project's rules to keep annotations consistent.

**Takeaway:** Document your dictionary sources, capitalization rules, and contraction splits in `LEMMATIZATION_POLICIES.md`.

---

## **28 Content**

**Recording Difficult Readings and Editorial Doubts**

Even skilled editors sometimes disagree on how to parse an old word. A word might fit two parts of speech, or an old sentence might allow two different readings.

When two people tag the same text separately, the percentage of words where they agree is called **editor agreement**. In digital humanities research, high agreement (often 90% or higher) shows that the project rules are clear.

When you find a word that has two reasonable readings, do not hide the problem. Put your preferred reading in your table, but add a brief note explaining the alternative. Recording these questions shows scholarly honesty and helps future readers understand difficult spots.

**Vocabulary.** *Editor Agreement* — The percentage of words where two independent scholars assign matching tags. *Textual Crux* — A puzzling or ambiguous passage that has more than one valid reading.

**Takeaway:** When an old word allows two different readings, record your top choice and note the alternative reading clearly.

---

## **29 Content**

**Getting Ready for Wednesday's Automated NLP Test**

Today's manual parsing is not a standalone drill. It sets up the rest of the week's experiments. Over the next two meetings, you will run computer tools over this exact same passage.

On Wednesday, in Lesson 8.2, you will run an automated rule-based tagger (like TreeTagger or SpaCy) on your 20-word excerpt. You will compare the computer's results directly against today's manual table. Every place where the computer disagrees with your work will be examined. Did the tool choke on an old spelling, or did it pick the wrong homograph?

On Friday, in Lesson 8.3, you will test an AI model on the same text. Having a trusted manual ground truth is the only way to measure how well these automated tools perform.

**Takeaway:** Today's manual ground truth is the benchmark you will use to evaluate automated tools on Wednesday and Friday.

---

## **30 Content**

**The Scholar as the Ground Truth**

Computers make linguistic tagging fast. Modern programs can process thousands of words in a few seconds. Yet all of that automation depends on human scholarship.

A computer does not understand the meaning of a 1791 French Revolutionary decree. It does not feel the personal warmth in Maud Lewis's letters, nor the legal weight of the 1752 Treaty. It simply follows statistical patterns learned from modern text. When an algorithm runs into old spelling or unusual grammar, it often breaks down.

The human editor remains the essential foundation of the digital edition. By looking up lemmas, tagging parts of speech, and encoding them in TEI XML, you create the trusted ground truth that computers cannot produce alone. Today you laid that foundation; tomorrow you will put automated tools to the test against it.

**Takeaway:** Computers process text quickly, but only human editors possess the historical knowledge to create true ground-truth data.

---
