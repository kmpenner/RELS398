# Lesson 8.2 — Deterministic NLP Tagging, Lemmatization, and Universal Dependencies

*RELS 398 / ENGL 398 · Topic 8: Lemmatization · Meeting #21 (Wed Oct 28)*

***Step 2 of the three-step cycle: deterministic.** Today you run automated rule-based and statistical NLP pipelines (TreeTagger and SpaCy) over your manuscript text. You will measure machine accuracy, analyze OOV errors, and benchmark the algorithms against Tuesday's manual ground truth.*

---

## **01 Content**

**From Hand Parsing to Algorithmic Pipelines**

Yesterday, in Lesson 8.1, you parsed and lemmatized a twenty-word passage from your manuscript witness by hand. You looked up each word in a scholarly dictionary, chose the correct part-of-speech tag. Recorded its grammatical features. That manual work gave you an authoritatively verified ground truth.

Today, we take Step 2 of our three-step comparative cycle: deterministic, automated language processing. In modern digital humanities projects, editors cannot parse million-word collections by hand. We need computer programs that can tokenize, tag, and lemmatize text automatically in fractions of a second.

Yet automation comes with a price. Algorithms follow fixed rules and statistical patterns trained on modern newspapers and books. When an algorithm encounters an eighteenth-century legal treaty, a French Revolutionary. A handwritten folk art letter, it often makes surprising mistakes. Today, you will run automated tagging tools over your text and measure their accuracy directly against yesterday's manual baseline.

**Vocabulary.** *Natural Language Processing (NLP)* — Computational methods for analyzing, parsing. Understanding human language in digital texts. *Deterministic Pipeline*. Software that follows fixed algorithms and statistical models, producing the same output for a given input every time.

**Takeaway:** Automated NLP pipelines process large corpora quickly. Their accuracy must be measured against an authoritative manual ground truth.

---

## **02 Content**

**How Rule-Based Lemmatizers Work**

The earliest automated lemmatizers relied entirely on explicit rules written by linguists. These programs are called **rule-based lemmatizers**.

A rule-based program uses two main tools: an internal dictionary of known root words and a set of ending rules. When the program reads an inflected English word like *treaties*, it checks its rules. A rule says: if a word ends in *ies*, replace *ies* with *y* and check if *treaty* is in the dictionary. Since *treaty* is found, the program assigns *treaty* as the lemma.

For regular words, rule systems are fast and predictable. However, natural language is full of irregular exceptions. If a program encounters *was* or *went*, simple suffix rules fail. The program must consult a large table of irregular forms (*went* maps to *go*, *was* maps to *be*). If an old word form is missing from that table, the rule system cannot solve it.

**Vocabulary.** *Rule-Based System* — Software that analyzes language using explicit human-written rules and lookup tables. *Suffix Stripping* — Removing common word endings (like *-ing* or *-ed*) to find a base stem.

**Takeaway:** Rule-based lemmatizers combine ending rules with lookup tables of irregular forms to identify base words.

---

## **03 Content**

**Statistical Sequence Taggers: Parts of Speech in Context**

Identifying parts of speech is harder than simply looking up words in a list. As you saw yesterday, homographs like *will*, *left*, and *est* can belong to multiple grammatical categories. To pick the right tag, an algorithm must look at surrounding words.

Modern deterministic tools use **statistical sequence models**, such as Hidden Markov Models or Decision trees. These models are trained on large collections of hand-tagged sentences called **training corpora**. By reading millions of tagged words, the algorithm learns word chances: how often a determiner like *the* is followed by a noun versus a verb.

When the tagger reads *the will of the people*, it calculates probabilities. It knows that after *the*, the word *will* is far more likely to be a noun than a helping verb. By calculating probabilities across whole sentences, statistical taggers achieve ninety to ninety-five percent accuracy on modern standard texts.

**Vocabulary.** *Sequence Model*. An algorithm that predicts labels for a sequence of tokens based on surrounding context. *Training Corpus* — A large body of human-annotated text used to train statistical language algorithms.

**Takeaway:** Statistical taggers calculate probabilities from surrounding sentence context to predict parts of speech for ambiguous words.

---

## **04 Content**

**TreeTagger: The Probabilistic Decision-Tree Engine**

One of the most famous and durable tools in digital humanities is **TreeTagger**, developed by Helmut Schmid at the University of Stuttgart. TreeTagger is widely used because it supports dozens of languages, including English, French, Latin, and German.

TreeTagger uses decision trees to estimate word chances. A decision tree asks a sequence of yes-or-no questions about neighboring words. For example: Is the previous word a determiner? Is the next word a finite verb? Based on the answers, the tree navigates to a leaf node that assigns the most probable part-of-speech tag and dictionary lemma.

TreeTagger is fast, lightweight, and deterministic. It processes thousands of words per second on an ordinary laptop. Because it has been refined over three decades, its French and English parameter files handle complex syntax with remarkable stability.

**Vocabulary.** *TreeTagger*. A standard statistical software tool that uses decision trees to assign part-of-speech tags and lemmas to text. *Decision Tree* — A branching flowchart algorithm that sorts data by answering a series of categorical questions.

**Takeaway:** TreeTagger uses decision trees to assign parts of speech and lemmas rapidly across many historical and modern languages.

---

## **05 Content**

**SpaCy and Stanza: Modern Industrial NLP in Python**

While TreeTagger remains a classic tool, modern computational linguistics often relies on Python-based libraries like **SpaCy** and **Stanza**.

SpaCy is designed for fast text analysis. It includes pre-trained neural and statistical pipelines for over twenty languages. In Python, you can load a model with a single line of code and pass text to it directly. SpaCy tokenizes the text, tags parts of speech, extracts lemmas, and builds complete sentence trees in memory.

Stanza, developed by the Stanford NLP Group, offers similar capabilities with deep support for historical treebanks. For our work in RELS 398, SpaCy provides a fast and accessible way to test automated parsing in VS Code. Models like `en_core_web_sm` for English and `fr_core_news_sm` for French give you instant access to standard Universal Dependencies pipelines.

**Vocabulary.** *SpaCy* — A popular open-source Python library for advanced language processing. *Pre-Trained Pipeline* — A ready-to-use software package containing statistical models and dictionaries trained on large text datasets.

**Takeaway:** Python libraries like SpaCy provide fast pre-trained language pipelines that tokenize, tag, lemmatiz. Parse sentences with simple code.

---

## **06 Content**

**Setting Up Python for Language Processing in VS Code**

Running an NLP pipeline does not require complicated software. In VS Code, you can write a short Python script that loads your transcript and runs a language pipeline in a few lines.

Here is what a complete ten-line Python script looks like using SpaCy:

```python
import spacy

# Load the standard English language model
nlp = spacy.load("en_core_web_sm")

# Read your 20-word text excerpt
text = "All Treaties shall be renewed by the Governor."

# Process the text
doc = nlp(text)

# Print the automated results
for token in doc:
    print(f"{token.text:12} {token.lemma_:12} {token.pos_:8} {token.dep_:8}")
```

When you run this script, SpaCy processes every token and outputs a clean table showing the surface text, the predicted lemma, the UPOS tag. The grammatical dependency relation.

**Takeaway:** A short Python script using SpaCy can load a pre-trained model and print lemmas, parts of sp. Grammar links in seconds.

---

## **07 Content**

**The Out-of-Vocabulary (OOV) Dilemma**

When an automated tagger reads modern text, it performs with high accuracy. When it reads historical manuscripts, it runs directly into the **Out-of-Vocabulary (OOV)** problem.

An OOV word is any token that does not exist in the software's training dictionary. Modern language models are trained on contemporary sources like Wikipedia, news articles, and modern books. They know modern vocabulary intimately. However, they have never seen eighteenth-century abbreviations, regional dialect spellings, or archaic contractions.

When a tagger encounters an OOV word, its dictionary lookup fails. Most taggers fall back to a simple default: they assume the lemma is identical to the surface string. They guess based on common prefixes and suffixes. In historical documents, this causes frequent errors.

**Vocabulary.** *Out-of-Vocabulary (OOV)*. A word that does not appear in a language model's vocabulary list or dictionary. *Graceful Degradation* — How software behaves when it meets unexpected input without crashing.

**Takeaway:** The missing word problem occurs when historical words or unusual spellings are missing from an automated model's training dictionary.

---

## **08 Content**

**Handling Historical Spelling in Deterministic Models**

Historical spelling variations present a severe obstacle for deterministic taggers. In Module 6, you saw how eighteenth-century scribes used spellings that look unfamiliar today.

In Andromeda's 1752 Treaty, words like *shew'd* (for *showed*) or *promis'd* (for *promised*) confuse modern models. Because *shew'd* is not in the modern dictionary, the tagger cannot find the lemma *show*. It may tag *shew'd* as a noun or invent a fictitious lemma *shew'd*.

In Ace's 1791 French decree, eighteenth-century scribes wrote imperfect verb endings with *-oit* instead of modern *-ait* (*faisoit*, *décrétoit*). A modern French model expects *faisait* or *décrétait*. When it sees *faisoit*, it fails to recognize the verb *faire*. As an editor, understanding this limitation helps you diagnose why taggers stumble on archival sources.

**Takeaway:** Historical spelling variations like French *-oit* or English *shew'd* confuse automated taggers because they deviate from modern training lexica.

---

## **09 Content**

**Universal Dependencies in Automated NLP**

A major benefit of modern NLP pipelines like SpaCy and Stanza is that they output standard **Universal Dependencies (UD)** tags by default.

When SpaCy processes a sentence, its `token.pos_` attribute returns the exact 17 UPOS tags you learned yesterday (`NOUN`, `VERB`, `ADJ`, `DET`, `PUNCT`). Its `token.morph` attribute provides standard FEATS pairs, such as `Number=Plur` or `Tense=Past`.

This standardization is crucial for our comparative workflow. Because the automated program outputs the same tag names as your manual ground truth from Lesson 8.1, you can compare human and computer decisions directly in code. You do not need to translate between different labeling systems.

**Takeaway:** Modern NLP libraries output Universal Dependencies tags by default, allowing direct side-by-side comparison with your manual ground truth.

---

## **10 Content**

**Tokenization Pitfalls in French: Clitics and Apostrophes**

Before a computer can tag parts of speech, it must tokenize the text. In French, apostrophes create frequent tokenization traps for automated tools.

In Ace's 1791 decree, phrases like *l'assemblée* or *d'état* require splitting the clitic from the noun. Modern French SpaCy models usually handle standard clitics like *l'* and *d'* correctly. However, if a historical document contains irregular spacing (such as *l ' assemblée* or *d' accord* with extra space), the tokenizer can split in the wrong place.

Worse, archaic contractions like *qu'il* or *lorsqu'il* are sometimes kept as a single token by older taggers. When this happens, the entire multi-word unit receives an inaccurate tag. The second word loses its lemma. Checking token boundaries is always the first diagnostic step when evaluating tagger output.

**Takeaway:** In French text, verify that automated tokenizers split apostrophe clitics cleanly so that articles and nouns receive separate tags.

---

## **11 Content**

**Tokenization Pitfalls in English: Contractions and Hyphens**

Historical English documents present their own tokenization challenges. In Maud Lewis's informal correspondence, contractions like *can't*, *it's*, and *I'll* appear frequently.

Modern English SpaCy tokenizers are programmed to split contractions into syntactic components: *ca* + *n't*. *i* + *'ll*. However, if the scribe wrote with non-standard punctuation (such as a grave accent instead of an apostrop. Missing spaces), the tokenizer treats the contraction as a single unknown word.

In Andromeda's 1752 Treaty, legal compounds like *hereinafter*, *whereof*, and *thereunto* pose the opposite problem. Are they single tokens or multiple words? Most modern tokenizers treat *whereof* as a single token with UPOS `ADV`. If your project policy in `LEMMATIZATION_POLICIES.md` specifies a different split, an editorial disagreement occurs.

**Takeaway:** Verify how automated tokenizers handle informal contractions and historical compound adverbs against your project policies.

---

## **12 Content**

**Homograph Meaning choice Under the Microscope**

Yesterday, you learned that homographs like *will* and *est* require sentence context to resolve. Today, you can test how well statistical algorithms handle those same ambiguous words.

In Andromeda's 1752 Treaty, consider the sentence: *The Chief will observe this Treaty of his own free will*. The word *will* appears twice. The first *will* is an auxiliary verb (`AUX`). The second *will* is a common noun (`NOUN`).

When you run SpaCy over this sentence, the statistical model uses surrounding words to make its choices. Because the first *will* precedes the infinitive *observe*, SpaCy predicts `AUX`. Because the second *will* follows the adjectives *own free*, SpaCy predicts `NOUN`. In this test, the statistical model succeeds! However, if sentence syntax is distorted by archaic word order, the model's predictions often collapse.

**Takeaway:** Statistical models use neighboring words to resolve double meanings, succeeding on standard syntax but stumbling on unusual historical phrasing.

---

## **13 Content**

**Universal Dependencies Syntactic Relations (DEPREL)**

In addition to tagging parts of speech, modern pipelines analyze sentence grammar by predicting **dependency relations (DEPREL)**.

In Universal Dependencies, every word in a clause connects to a governing head word through a labeled relation. Here is a summary of the most common dependency tags used by automated tools:

<table>
  <thead>
    <tr>
      <th>Relation</th>
      <th>Description</th>
      <th>Example (Head → Dependent)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>root</code></td>
      <td>Main clause verb</td>
      <td>[Sentence] → renewed</td>
    </tr>
    <tr>
      <td><code>nsubj</code></td>
      <td>Nominal subject</td>
      <td>renewed → Treaties</td>
    </tr>
    <tr>
      <td><code>obj</code></td>
      <td>Direct object</td>
      <td>signed → Treaty</td>
    </tr>
    <tr>
      <td><code>iobj</code></td>
      <td>Indirect object</td>
      <td>gave → Chief</td>
    </tr>
    <tr>
      <td><code>amod</code></td>
      <td>Adjectival modifier</td>
      <td>Treaty → peaceable</td>
    </tr>
    <tr>
      <td><code>det</code></td>
      <td>Determiner</td>
      <td>Treaty → the</td>
    </tr>
    <tr>
      <td><code>case</code></td>
      <td>Preposition marker</td>
      <td>Governor → by</td>
    </tr>
    <tr>
      <td><code>punct</code></td>
      <td>Punctuation mark</td>
      <td>renewed → .</td>
    </tr>
  </tbody>
</table>

These tags show how words work together to build meaning.

**Takeaway:** Relation tags like `nsubj`, `obj`. `case` describe the specific grammatical jobs that words perform in clauses.

---

## **14 Content**

**Heads and Dependents in Automated Trees**

How do automated parsers connect words into syntactic trees? In dependency grammar, every word has exactly one governing **head**, except for the main verb. This is the **root** of the sentence.

Consider the passive clause: *All Treaties shall be renewed by the Governor*. In this sentence, the main past participle *renewed* is the structural root (Head = 0). The subject noun *Treaties* points to *renewed* as its head with relation `nsubj:pass`. The helping verb *shall* points to *renewed* with relation `aux`. The infinitive *be* points to *renewed* with relation `aux:pass`.

Prepositional phrases also attach to their heads. In *by the Governor*, the noun *Governor* attaches to *renewed* as an oblique agent (`obl`). The preposition *by* attaches to *Governor* with relation `case`. The parser builds a complete tree linking every word back to the central verb.

**Vocabulary.** *Root* — The main governing verb of an independent clause. This has no syntactic head in the sentence. *Oblique (obl)* — A noun phrase functioning as an adverbial modifier, usually introduced by a preposition.

**Takeaway:** Dependency parsers link every word to a governing head word, creating a rooted tree centered on the main finite verb.

---

## **15 Content**

**Visualizing Dependency Trees with displaCy**

Looking at text tables of heads and relation tags can feel abstract. SpaCy provides a built-in visualization tool called **displaCy** that renders syntactic trees into beautiful graphical diagrams.

With a single Python command, you can launch a local web server or generate an SVG image showing arrows connecting heads to dependents:

```python
from spacy import displacy

# Generate an SVG visualization of the syntax tree
svg = displacy.render(doc, style="dep", jupyter=False)

# Save the SVG image to disk
with open("syntax_tree.svg", "w", encoding="utf-8") as f:
    f.write(svg)
```

Opening `syntax_tree.svg` in your browser reveals the sentence structure visually. Curved arrows arc from *renewed* to *Treaties*, labeled with `nsubj`. Seeing the visual tree makes grammatical hierarchies immediately intuitive.

**Vocabulary.** *displaCy*. A visual rendering tool in spacy that turns dependency trees and entity markup into interactive diagrams. *SVG* — Vector graphics, an open image format for rendering clean vector lines in web browsers.

**Takeaway:** Visualizing syntax trees with displaCy turns abstract grammar links into clear graphical diagrams of sentence structure.

---

## **16 Content**

**The CoNLL-U Data Pipeline in Python**

Yesterday, you learned that CoNLL-U is the global ten-column plain-text exchange format for Universal Dependencies. In Python, you can easily read, modify, and write CoNLL-U files.

When you run an automated pipeline like SpaCy or Stanza, you can export the results directly into CoNLL-U format using the open-source `spacy-conll` package or a simple Python loop:

```python
for i, token in enumerate(doc, 1):
    head_id = token.head.i + 1 if token.head != token else 0
    print(f"{i}\t{token.text}\t{token.lemma_}\t{token.pos_}\t_\t{token.morph}\t{head_id}\t{token.dep_}\t_\t_")
```

This short script produces standard ten-column CoNLL-U output. Because CoNLL-U is plain text, you can save it to `nlp_baseline.conllu` in your repository and diff it directly against your manual ground truth.

**Takeaway:** Python scripts can format automated NLP predictions directly into standard ten-column CoNLL-U exchange files.

---

## **17 Content**

**Running an NLP Pipeline on the 1752 Treaty**

Let us look at what happens when we run an automated English SpaCy pipeline on the opening clause from Andromeda's project: *All Treaties shall be renewed*.

Here are the automated predictions:

<table>
  <thead>
    <tr>
      <th>Token</th>
      <th>Predicted Lemma</th>
      <th>Predicted UPOS</th>
      <th>Predicted Deprel</th>
      <th>Manual Truth Match?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>All</td>
      <td>all</td>
      <td><code>DET</code></td>
      <td><code>det</code></td>
      <td>Match</td>
    </tr>
    <tr>
      <td>Treaties</td>
      <td>treaty</td>
      <td><code>NOUN</code></td>
      <td><code>nsubj:pass</code></td>
      <td>Match</td>
    </tr>
    <tr>
      <td>shall</td>
      <td>shall</td>
      <td><code>AUX</code></td>
      <td><code>aux</code></td>
      <td>Match</td>
    </tr>
    <tr>
      <td>be</td>
      <td>be</td>
      <td><code>AUX</code></td>
      <td><code>aux:pass</code></td>
      <td>Match</td>
    </tr>
    <tr>
      <td>renewed</td>
      <td>renew</td>
      <td><code>VERB</code></td>
      <td><code>ROOT</code></td>
      <td>Match</td>
    </tr>
  </tbody>
</table>

On this straightforward legal sentence, the modern model achieves a perfect score! Every lemma matches the OED baseline, every part of sp. The passive dependency structure is correctly analyzed.

**Takeaway:** On formal clauses with standard grammar, modern automated pipelines can achieve high accuracy matching human ground truth.

---

## **18 Content**

**Running an NLP Pipeline on the 1791 French Decree**

Now let us test our automated pipeline on Ace's project: a 1791 French Revolutionary decree.

When we run French SpaCy (`fr_core_news_sm`) on *L'Assemblée nationale décrète les lois suivantes*, here is what the program outputs:

<table>
  <thead>
    <tr>
      <th>Token</th>
      <th>Predicted Lemma</th>
      <th>Predicted UPOS</th>
      <th>Predicted Deprel</th>
      <th>Manual Truth Match?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>L'</td>
      <td>le</td>
      <td><code>DET</code></td>
      <td><code>det</code></td>
      <td>Match</td>
    </tr>
    <tr>
      <td>Assemblée</td>
      <td>assemblée</td>
      <td><code>NOUN</code></td>
      <td><code>nsubj</code></td>
      <td>Match</td>
    </tr>
    <tr>
      <td>nationale</td>
      <td>national</td>
      <td><code>ADJ</code></td>
      <td><code>amod</code></td>
      <td>Match</td>
    </tr>
    <tr>
      <td>décrète</td>
      <td>décréter</td>
      <td><code>VERB</code></td>
      <td><code>ROOT</code></td>
      <td>Match</td>
    </tr>
    <tr>
      <td>les</td>
      <td>le</td>
      <td><code>DET</code></td>
      <td><code>det</code></td>
      <td>Match</td>
    </tr>
    <tr>
      <td>lois</td>
      <td>loi</td>
      <td><code>NOUN</code></td>
      <td><code>obj</code></td>
      <td>Match</td>
    </tr>
    <tr>
      <td>suivantes</td>
      <td>suivant</td>
      <td><code>ADJ</code></td>
      <td><code>amod</code></td>
      <td>Match</td>
    </tr>
  </tbody>
</table>

The model correctly handles the elided article *L'*, matches the feminine agreement on *nationale*. Maps the conjugated verb *décrète* to its infinitive *décréter*. However, on older passages with eighteenth-century spelling (*décrétoit*), the model stumbles.

**Takeaway:** French pre-trained models handle standard vocabulary accurately, but require normalized spelling to parse older texts correctly.

---

## **19 Content**

**Running an NLP Pipeline on Maud Lewis's Letter**

Next, we test our automated pipeline on Olyvia's project: Maud Lewis's informal 1967 letter: *I received your letter today*.

Here are the automated predictions:

<table>
  <thead>
    <tr>
      <th>Token</th>
      <th>Predicted Lemma</th>
      <th>Predicted UPOS</th>
      <th>Predicted Deprel</th>
      <th>Manual Truth Match?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>I</td>
      <td>I</td>
      <td><code>PRON</code></td>
      <td><code>nsubj</code></td>
      <td>Match</td>
    </tr>
    <tr>
      <td>received</td>
      <td>receive</td>
      <td><code>VERB</code></td>
      <td><code>ROOT</code></td>
      <td>Match</td>
    </tr>
    <tr>
      <td>your</td>
      <td>your</td>
      <td><code>PRON</code></td>
      <td><code>nmod:poss</code></td>
      <td>Disagreement</td>
    </tr>
    <tr>
      <td>letter</td>
      <td>letter</td>
      <td><code>NOUN</code></td>
      <td><code>obj</code></td>
      <td>Match</td>
    </tr>
    <tr>
      <td>today</td>
      <td>today</td>
      <td><code>NOUN</code></td>
      <td><code>obl:tmod</code></td>
      <td>Match</td>
    </tr>
  </tbody>
</table>

Look closely at row three! In our manual ground truth from yesterday, we assigned the canonical lemma *you* for the possessive pronoun *your* (following standard dictionary policy). SpaCy predicted *your* as its own lemma. This is an editorial policy disagreement: does a possessive pronoun map to its base personal p. Does it keep its own lemma?

**Takeaway:** Automated tools may follow different dictionary conventions for pronouns, creating disagreements with your project policies.

---

## **20 Content**

**Measuring Machine Accuracy Against Human Ground Truth**

Now that you have run your automated pipeline, how do you evaluate its performance? In computational scholarship, we calculate **token-level accuracy**.

Token accuracy is the percentage of tokens where the computer's prediction exactly matches your manual ground truth. To calculate accuracy, use this simple formula:

```text
Accuracy = (Number of Correct Tokens) / (Total Number of Tokens) * 100
```

If your 20-word excerpt contains 18 tokens where both the lemma and the part-of-speech tag match your manual ground truth, your pipeline's accuracy is 90%.

When evaluating, calculate two separate scores: **POS Accuracy** (did the tagger get the part of speech right?) and **Lemma Accuracy** (did the tagger assign the right dictionary headword?). Often, a tagger identifies that a word is a v. Fails to find the right historical lemma.

**Vocabulary.** *Accuracy*. The proportion of correct predictions made by a model out of the total number of items tested.

**Takeaway:** Calculate separate accuracy scores for parts of speech and lemmas by comparing automated output directly to your manual ground truth.

---

## **21 Content**

**Calculating Precision, Recall, and F1 Score**

Overall accuracy gives a broad overview. However, it can hide critical flaws. If an edition contains ninety common nouns and ten rare verbs, a model that guesses `NOUN` for everything might score ninety percent accuracy while being completely useless for verbs!

To evaluate specific grammatical categories, computational linguists use **Precision** and **Recall**:

<ul>
  <li><strong>Precision:</strong> When the model predicts a specific tag (like <code>VERB</code>), how often is it actually right?</li>
  <li><strong>Recall:</strong> Out of all real verbs in your text, how many did the model successfully find?</li>
</ul>

The **F1 Score** is the harmonic mean of precision and recall, balancing false alarms against missed words. In historical editing, high precision means you can trust the tags the computer assigns. In contrast, high recall means the computer did not overlook rare grammatical constructions.

**Vocabulary.** *Precision* — The proportion of predicted instances for a category that are correct. *Recall* — The proportion of actual instances of a category in the text that were successfully retrieved. *F1 Score* — A balanced score combining precision and recall into a single metric.

**Takeaway:** Precision and recall reveal how well a pipeline performs on specific grammatical classes, balancing false alarms against missed words.

---

## **22 Content**

**The Confusion Matrix: Where Models Stumble**

When a model makes mistakes, where do those errors happen? To diagnose error patterns, linguists use a tool called a **confusion matrix**.

A confusion matrix is a table that plots human ground-truth tags against machine predictions. Rows represent the actual human tags, and columns represent what the computer predicted.

In historical English, taggers frequently confuse nouns and adjectives. In the phrase *Peace and Friendship Treaty*, the word *Peace* is a noun functioning as a modifier. A tagger might predict `ADJ` instead of `NOUN`. In French, taggers sometimes confuse past participles (`VERB`) with predicate adjectives (`ADJ`). Looking at a confusion matrix reveals which grammatical boundaries are most fragile in your document.

**Vocabulary.** *Confusion Matrix*. A diagnostic table that records how often each actual category is confused with another category by an automated model.

**Takeaway:** A confusion matrix highlights systematic error patterns, showing which parts of speech are most frequently confused by automated models.

---

## **23 Content**

**Diagnosing Out-of-Vocabulary (OOV) Failures**

The most common error in historical NLP is the Out-of-Vocabulary failure. When an algorithm encounters an unfamiliar word, how does it fail?

Look for these three common OOV symptoms in your output:
<ol>
  <li><strong>Identity Fallback:</strong> The model simply copies the surface spelling into the lemma field (e.g., surface *promis'd* receives lemma *promis'd* instead of *promise*).</li>
  <li><strong>Fictitious Headwords:</strong> The model applies a modern rule inappropriately, inventing a non-existent word (e.g., predicting *shew* for *shew'd*).</li>
  <li><strong>Unknown Tags:</strong> The model assigns an `X` (unknown) or default `NOUN` tag to any word it cannot parse.</li>
</ol>

Whenever you spot an OOV error, record it in your work notes. This provides the evidence you will use to refine your workflow.

**Takeaway:** OOV failures typically show up as copied surface spellings, invented headwords, or default noun tags.

---

## **24 Content**

**Archaic Inflection Errors: Suffix Errors**

Another major failure mode stems from historical grammar endings that have vanished from modern speech.

In 18th-century French, imperfect verbs ended in *-oit* (*décrétoit*, *faisoit*). Modern French models are trained on texts using *-ait* (*décrétait*, *faisait*). Because the suffix *-oit* does not match any regular modern verb paradigm, the model fails to recognize the verb. It may guess that *décrétoit* is an obscure noun or foreign word.

In 18th-century English, formal verbs took archaic suffixes (*doth*, *hath*, *speaketh*). While modern English models usually recognize *doth* as an archaic auxiliary, rarer forms like *witnesseth* are often misclassified as adjectives or common nouns. Documenting these suffix errors proves why historical texts require specialized domain handling.

**Takeaway:** Historical grammar endings like French *-oit* or English *-eth* trigger errors because modern statistical models do not recognize them as active verb suffixes.

---

## **25 Content**

**Exporting Automated Output to TEI XML**

Once your Python script processes your text, you can automatically convert the output into valid TEI XML.

Here is a simple Python function that writes TEI `<w>` elements from SpaCy tokens:

```python
def export_tei(doc, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("<s>\n")
        for token in doc:
            if token.is_punct:
                f.write(f'  <pc pos="PUNCT">{token.text}</pc>\n')
            else:
                f.write(f'  <w lemma="{token.lemma_}" pos="{token.pos_}">{token.text}</w>\n')
        f.write("</s>\n")
```

Running this function produces `nlp_baseline.xml`. Now you have two comparable XML files in your repository: the manual ground truth you hand-crafted yesterday. The automated version produced by the python pipeline today.

**Takeaway:** A short Python loop can convert automated NLP output directly into valid TEI `<w>` and `<pc>` XML tags.

---

## **26 Content**

**Auditing the Machine TEI Against the Manual Baseline**

Now comes the crucial scientific step: comparing the two XML files side by side.

In VS Code, open both files and use the built-in diff viewer:
```bash
code --diff ground_truth_manual.xml nlp_baseline.xml
```

The diff viewer highlights every discrepancy in red and green. Read through the differences line by line:
<ul>
  <li>Did the automated tool split contractions in the same places you did?</li>
  <li>Did it predict the same dictionary lemma as your OED or TLFi authority?</li>
  <li>Did it assign the same UPOS tag?</li>
</ul>

This side-by-side audit reveals the exact error rate of the automated pipeline on historical prose.

**Takeaway:** Diffing your manual XML against the machine-generated XML in VS Code exposes every automated discrepancy instantly.

---

## **27 Content**

**Documenting Algorithm Quirks in `NLP_BENCHMARK.md`**

To preserve your findings, record your results in a project report called `NLP_BENCHMARK.md`.

Your benchmark report should include four sections:
<ol>
  <li><strong>Pipeline Specifications:</strong> Which tool and model were used (e.g., SpaCy 3.7 with <code>en_core_web_sm</code>)?</li>
  <li><strong>Accuracy Scores:</strong> Overall token accuracy, POS accuracy, and lemma accuracy percentages.</li>
  <li><strong>Discrepancy Log:</strong> A table listing every token where the computer disagreed with your manual ground truth.</li>
  <li><strong>Error Diagnosis:</strong> An analysis explaining why the machine failed (e.g., OOV archaic spelling, homograph ambiguity, tokenization split).</li>
</ol>

Writing this report ensures that your digital edition maintains full methodological transparency.

**Takeaway:** Record pipeline versions, accuracy scores, discrepancy tables, and error causes in `NLP_BENCHMARK.md`.

---

## **28 Content**

**Preprocessing Strategies: Can Normalization Rescue the Tagger?**

After seeing how historical spellings trip up automated taggers, a natural question arises: can we fix these errors before the tagger runs?

Yes! This is where your work from Module 6 pays off. In Module 6, you built regularized readings using `<reg>` tags (*acknowledged* for *acknowledg'd*, *décrétait* for *décrétoit*).

If you feed the **regularized reading text** into SpaCy instead of the raw diplomatic transcript, accuracy jumps dramatically! Because the normalized text uses modern spelling, the tagger's dictionary lookups succeed. The model correctly identifies *décréter* and *acknowledge*. You can then transfer those accurate lemmas back onto your diplomatic `<w>` elements.

**Takeaway:** Preprocessing text with Module 6 regularizations dramatically reduces OOV errors and boosts automated tagging accuracy.

---

## **29 Content**

**Preparing for Friday's AI-Assisted Parsing Test**

Today you evaluated a deterministic natural language processing tool. You saw its speed, its consistency, and its vulnerabilities when facing historical language shifts.

On Friday, in Lesson 8.3, you will test a completely different technology: large language model AI in VS Code Antigravity. Unlike deterministic taggers, modern AI models have seen vast amounts of historical literature during training. They can often recognize eighteenth-century French and archaic English with remarkable intuition.

However, AI models bring their own risks, including hallucinated lemmas and unpredictable outputs. Today's deterministic baseline and Tuesday's manual ground truth provide the twin reference points you will use to audit Friday's AI output.

**Takeaway:** Today's deterministic NLP benchmark provides the essential comparison point for evaluating Friday's AI language models.

---

## **30 Content**

**The Limits and Power of Deterministic Algorithms**

Deterministic NLP pipelines are among the most powerful tools in computational textual scholarship. They allow a single researcher to analyze millions of words in minutes, revealing large-scale stylistic patterns and grammatical shifts across centuries.

Yet algorithms are not infallible authorities. They are statistical mirrors of the data on which they were trained. When turned loose on the rich, irreg. Beautiful prose of historical documents, they require human guidance, careful preprocessing, and rigorous validation.

By establishing a manual ground truth, measuring machine accuracy. Diagnosing error patterns, you have learned how to use automated tools critically and responsibly. You are no longer just running software; you are conducting rigorous computational scholarship.

**Takeaway:** Deterministic tools offer incredible sp. Scholarly rigor requires measuring their limits against human ground truth.

---
