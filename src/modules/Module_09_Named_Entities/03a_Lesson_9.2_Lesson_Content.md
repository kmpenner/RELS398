# Lesson 9.2 — Automated Named Entity Recognition (NER) and Gazetteer Lookup

*RELS 398 / ENGL 398 · Topic 9: Named Entities · Meeting #24 (Wed Nov 4)*

***Step 2 of the three-step cycle: Deterministic automation.** Today you write a Python NER pipeline using SpaCy, run gazetteer lookups, export a machine baseline, and audit precision and recall against Tuesday's ground truth.*

---

## **01 Content**

**From Hand Craft to Automated Processing: Scaling Entity Recognition**

Yesterday, you established an authoritative manual baseline for named entities. You read your manuscript witness closely, extracted twenty entity mentions, and linked them to authority files like Wikidata and GeoNames. That manual work is the scientific gold standard of textual scholarship.

However, hand-tagging does not scale to an entire archive. A single colonial treaty or letter is short enough to annotate by hand in one morning. A national archive containing thousands of parliamentary decrees, diplomatic treaties, and personal letters requires computational automation.

Today, we take our second step: automated Named Entity Recognition (NER). You will write and run a Python script using SpaCy sequence models to find and tag entities automatically. You will measure the machine's accuracy directly against yesterday's manual baseline.

**Vocabulary.** *Automated NER* — Using computer software to find and classify proper names in text automatically. *Scalability* — The ability of a digital method to process thousands of pages rapidly.

**Takeaway:** Hand annotation creates gold-standard benchmarks; automated NER provides the speed needed to process large archival collections.

---

## **02 Content**

**How Computers Read Names: Statistical Sequence Models**

A computer cannot understand who a person is or what a town represents. When an automated program reads text, it analyzes statistical patterns across neighboring words.

Modern NER engines are trained on millions of words in curated digital corpora. The software learns grammatical clues that signal a proper name. For example, if a capitalized word follows the title *Governor* or *Major*, statistical probability strongly suggests a personal name (`PER`). If a word follows a spatial preposition like *at* or *near*, the model predicts a location (`LOC`).

These statistical sequence models make decisions in fractions of a second. They process entire paragraphs without human fatigue. But because they rely on probability rather than true understanding, they make systematic mistakes when historical language shifts.

**Vocabulary.** *Sequence Model* — An algorithm that predicts labels for words based on neighboring context. *Training Corpus* — A large body of digitized text used to teach algorithms statistical language patterns.

**Takeaway:** Statistical sequence models predict entity types by calculating the probability of neighboring words in a clause.

---

## **03 Content**

**The IOB2 Tagging Standard: Inside, Outside, Beginning**

To track multi-word entity phrases, natural language processing uses a standard labeling scheme called **IOB2**.

The letters stand for three spatial states:

1. **B (Beginning):** The very first token of an entity span (e.g., `B-PER` for *Major* in *Major Cope*).

2. **I (Inside):** Any subsequent token that continues that same entity span (e.g., `I-PER` for *Cope*).

3. **O (Outside):** Any token that does not belong to any named entity.

Look at how the IOB2 scheme labels a historical sentence:

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 0.5rem; text-align: left;">Token</th>
      <th style="padding: 0.5rem; text-align: left;">IOB2 Tag</th>
      <th style="padding: 0.5rem; text-align: left;">Entity Meaning</th>
      <th style="padding: 0.5rem; text-align: left;">Boundary Role</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Governor</td>
      <td style="padding: 0.5rem;"><code>B-PER</code></td>
      <td style="padding: 0.5rem;">Person</td>
      <td style="padding: 0.5rem;">First word of person name</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Hopson</td>
      <td style="padding: 0.5rem;"><code>I-PER</code></td>
      <td style="padding: 0.5rem;">Person</td>
      <td style="padding: 0.5rem;">Continuation of person name</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">at</td>
      <td style="padding: 0.5rem;"><code>O</code></td>
      <td style="padding: 0.5rem;">None</td>
      <td style="padding: 0.5rem;">Outside any entity</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem;">Halifax</td>
      <td style="padding: 0.5rem;"><code>B-LOC</code></td>
      <td style="padding: 0.5rem;">Location</td>
      <td style="padding: 0.5rem;">Single-word place name</td>
    </tr>
  </tbody>
</table>

This three-letter scheme prevents software from merging two adjacent names into a single person.

**Vocabulary.** *IOB2 Scheme* — A standard token-level annotation format using Beginning, Inside, and Outside tags. *Entity Span* — The complete sequence of words that forms a single named entity.

**Takeaway:** The IOB2 tagging scheme allows computers to distinguish where multi-word entity spans begin, continue, and end.

---

## **04 Content**

**Two Main Tools: SpaCy and Rule-Based Gazetteers**

In digital humanities workflows, researchers combine two computational approaches: statistical models and rule-based gazetteers.

**SpaCy** is the modern industry standard for Python natural language processing. It provides pre-trained neural sequence pipelines for English (`en_core_web_sm`) and French (`fr_core_news_sm`). SpaCy tokenizes sentences, identifies parts of speech, and extracts entity spans simultaneously.

**Gazetteers** take a different, rule-based approach. A gazetteer is an explicit dictionary list of known places, people, and groups. Instead of guessing based on statistical context, gazetteer matching searches text for exact string matches against verified lists.

Combining both tools gives editors the best of both worlds: statistical flexibility for new names, and gazetteer precision for known historical places.

**Vocabulary.** *SpaCy* — An open-source Python library for advanced natural language processing. *Gazetteer Matching* — Identifying place names by matching text directly against pre-compiled geographic dictionaries.

**Takeaway:** Digital workflows combine statistical models like SpaCy with rule-based gazetteer lookups for maximum accuracy.

---

## **05 Content**

**A 10-Line Python NER Pipeline in VS Code**

Running an automated entity recognition pipeline in Visual Studio Code requires only a few lines of Python.

You import the `spacy` library, load your pre-trained language model, and pass your manuscript text into the pipeline. SpaCy processes the text and stores all detected entities in the `.ents` collection.

Look at the simple script:
```python
import spacy

nlp = spacy.load("en_core_web_sm")  # or fr_core_news_sm
text = "Governor Hopson met Major Cope at Halifax in 1752."
doc = nlp(text)

print(f"{'Entity':20} {'Label':10}")
print("-" * 30)
for ent in doc.ents:
    print(f"{ent.text:20} {ent.label_:10}")
```

Within two seconds, the script prints detected entities alongside standard labels like `PERSON`, `GPE` (geopolitical entity), and `DATE`.

**Vocabulary.** *Pre-Trained Pipeline* — A machine learning model already trained on millions of words, ready for immediate use. *Entity Collection* — The list of detected named entity spans stored in SpaCy's document object.

**Takeaway:** A 10-line Python script using SpaCy can automatically extract people, places, and dates from historical text.

---

## **06 Content**

**SpaCy Entity Labels: PERSON, GPE, LOC, and ORG**

SpaCy uses its own standard set of entity labels, which map closely to TEI elements.

The label `PERSON` corresponds directly to `<persName>`. The label `ORG` maps to `<orgName>`. The label `DATE` maps to `<date>`.

For places, SpaCy divides locations into two categories:

1. **GPE (Geopolitical Entity):** Named administrative territories with a government, such as cities, provinces, and nations (e.g., *Halifax*, *Nova Scotia*, *France*).

2. **LOC (Location):** Natural geographic features without a civic government, such as rivers, mountains, and oceans (e.g., *the Atlantic Ocean*, *the Shubenacadie River*).

Both `GPE` and `LOC` map into TEI `<placeName>`. Understanding this mapping helps you convert SpaCy output into TEI XML.

**Vocabulary.** *GPE* — Geopolitical Entity: a place with an organized government, like a city or country. *LOC* — Non-GPE Location: a physical geographic feature like a mountain or lake.

**Takeaway:** SpaCy tags people, groups, dates, geopolitical entities (GPE), and physical locations (LOC).

---

## **07 Content**

**The Out-of-Vocabulary Problem: Historical Orthography Traps**

Why do modern NER models fail on archival manuscripts? The primary cause is the **Out-of-Vocabulary (OOV)** problem.

Language models are trained on contemporary digital text: modern news articles, Wikipedia, and digitized books. Modern training corpora reflect modern spelling, grammar, and vocabulary.

When an automated model encounters eighteenth-century spelling variations, it gets confused. Scribes write *shew'd*, *promis'd*, *décrétoit*, or *acknowledg'd*. An unrecognized word disrupts the statistical context of the clause. If the model fails to recognize an archaic verb, it often misinterprets surrounding proper names.

Understanding OOV errors is the first lesson of computational auditing. The machine is not broken; its training data simply lacks eighteenth-century language experience.

**Vocabulary.** *Out-of-Vocabulary (OOV)* — A word missing from an algorithm's pre-trained dictionary and training data. *Training Bias* — Systematic model errors caused by training data that reflects only modern digital texts.

**Takeaway:** Modern language models stumble on historical manuscripts because their training data reflects contemporary spelling.

---

## **08 Content**

**Boundary Errors: Where Does a Name Begin and End?**

The most common error in automated entity extraction is a **boundary error**. A boundary error occurs when an algorithm tags part of a name correctly but cuts off or extends the entity span.

Consider the title and name *Governor Hopson*. Did the model tag `Governor Hopson` as a single person, or did it tag only `Hopson`? In Ace's 1791 decree, did the model tag `l'Assemblée nationale` including the elided article `l'`, or did it tag only `Assemblée nationale`?

Boundary errors severely penalize automated scoring. If your manual ground truth tags `Major Jean Baptiste Cope` and the computer tags only `Jean Baptiste`, the algorithm fails both precision and recall tests on that token.

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 0.5rem; text-align: left;">Historical Phrase</th>
      <th style="padding: 0.5rem; text-align: left;">Manual Truth (9.1)</th>
      <th style="padding: 0.5rem; text-align: left;">Machine Span (9.2)</th>
      <th style="padding: 0.5rem; text-align: left;">Error Diagnosis</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Governor Hopson</td>
      <td style="padding: 0.5rem;"><code>Governor Hopson</code></td>
      <td style="padding: 0.5rem;"><code>Hopson</code></td>
      <td style="padding: 0.5rem;">Excluded official role title</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">l'Assemblée nationale</td>
      <td style="padding: 0.5rem;"><code>Assemblée nationale</code></td>
      <td style="padding: 0.5rem;"><code>l'Assemblée nationale</code></td>
      <td style="padding: 0.5rem;">Included French elided article</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem;">Digby County</td>
      <td style="padding: 0.5rem;"><code>Digby County</code></td>
      <td style="padding: 0.5rem;"><code>Digby</code></td>
      <td style="padding: 0.5rem;">Truncated geographic region</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Boundary Error* — When an automated model incorrectly expands or truncates the start or end of an entity span. *Exact Match* — When an automated prediction matches the manual span's start and end tokens perfectly.

**Takeaway:** Boundary errors occur when an automated tool captures part of a name but misses surrounding titles or geographic words.

---

## **09 Content**

**Entity Type Confusion: Mixing Up Places, Groups, and People**

A second frequent failure mode is **entity type confusion**. The algorithm identifies the correct word boundary, but assigns the wrong semantic category.

In Ace's 1791 decree, SpaCy's French model often tags `l'Assemblée nationale` as a `LOC` (location) rather than an `ORG` (organization). The model sees the capital letters and French noun structure and guesses that the Assembly is a physical building rather than a legislative body.

In Andromeda's treaty, the model often mistakes `His Majesty's Council` for a person (`PER`) because it associates *Majesty* with royalty. Diagnosing type confusion helps editors decide when rule-based filters must override statistical guesses.

**Vocabulary.** *Type Confusion* — When an algorithm correctly identifies an entity span but assigns the wrong category label. *Semantic Ambiguity* — Words that can represent both physical places and governing organizations.

**Takeaway:** Automated taggers frequently confuse governing organizations with physical buildings or personal titles.

---

## **10 Content**

**Cohort Corpus A Tests: Ace and the 1791 French Decree**

When Ace runs SpaCy's French pipeline (`fr_core_news_sm`) over the 1791 French Revolutionary decree, several predictable errors emerge.

First, elided clitics create tokenization traps. In French, the definite article *le* or *la* contracts before a vowel into `l'`. When SpaCy encounters `l'Assemblée nationale`, does it split `l'` from `Assemblée`? If the tokenizer treats `l'Assemblée` as a single word, the entity boundary becomes corrupted.

Second, royal and revolutionary dates challenge modern parsers. The phrase *ce 25 Août 1791* contains historical capitalization and month naming. SpaCy often misses the full date expression, capturing only the year `1791` while ignoring the day and month.

**Vocabulary.** *Clitic Contraction* — A contracted word like French l' attached directly to a neighboring noun. *Date Truncation* — Capturing only a single year number while missing the surrounding calendar phrase.

**Takeaway:** French historical decrees challenge automated parsers with elided articles and complex formal date phrasing.

---

## **11 Content**

**Cohort Corpus B Tests: Olyvia and Maud Lewis's Letters**

When Olyvia runs SpaCy's English pipeline (`en_core_web_sm`) over Maud Lewis's 1967 letter, a different set of challenges arises.

Informal personal correspondence lacks formal official titles. Maud Lewis writes in casual prose, referring to her husband simply as *Everett*. Because *Everett* appears without an honorific title like *Mr.* or *Dr.*, SpaCy's statistical model assigns lower confidence to the word.

Furthermore, rural Maritime place names test modern training corpora. SpaCy easily recognizes *Halifax* and *Nova Scotia*. But it often completely ignores *Marshalltown*, treating it as an ordinary common noun. Automated tools trained on global news know world capitals, but they are blind to rural Nova Scotia hamlets.

**Vocabulary.** *Low-Resource Toponym* — A small village or rural location rarely mentioned in global digital training text. *Confidence Score* — A mathematical probability value generated by an algorithm indicating its certainty.

**Takeaway:** Modern NER models easily recognize global cities like Halifax but frequently miss rural hamlets like Marshalltown.

---

## **12 Content**

**Cohort Corpus C Tests: Andromeda and the 1752 Treaty**

When Andromeda runs SpaCy over the 1752 Peace and Friendship Treaty, the model encounters eighteenth-century legal rhetoric.

The treaty features long, complex sentences with multiple embedded clauses. In the phrase *Major Jean Baptiste Cope, Chief Sachem of the Tribe of Mickmack Indians*, SpaCy struggles to separate personal names from sovereign titles.

The model frequently tags *Major Jean Baptiste Cope* as a person, but truncates *Tribe of Mickmack Indians* or misclassifies it as a location. Crucially, SpaCy completely overlooks the Indigenous toponym *Chigabenakady*, guessing that the archaic word is a foreign term or common noun.

**Vocabulary.** *Legal Preamble* — The introductory formal declaration of a treaty or law setting out parties and dates. *Toponym Blindness* — The total failure of an algorithm to recognize an Indigenous or historical place name.

**Takeaway:** Complex 18th-century treaty rhetoric and Indigenous place names cause severe omissions in standard NER pipelines.

---

## **13 Content**

**Measuring Machine Accuracy: Precision, Recall, and F1-Score**

To evaluate automated tools scientifically, computational humanists use three standard mathematical metrics: **Precision**, **Recall**, and **F1-Score**.

**Precision** measures correctness: out of all the entities the computer predicted, how many were actually right?
$$\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}$$

**Recall** measures completeness: out of all the true entities in your document, how many did the computer find?
$$\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}$$

**F1-Score** is the harmonic balance between Precision and Recall. A model that guesses rarely might have high precision, but terrible recall. F1 measures overall reliability.

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 0.5rem; text-align: left;">Metric</th>
      <th style="padding: 0.5rem; text-align: left;">Core Question</th>
      <th style="padding: 0.5rem; text-align: left;">Formula</th>
      <th style="padding: 0.5rem; text-align: left;">What It Penalizes</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Precision</td>
      <td style="padding: 0.5rem;">Were the computer's guesses correct?</td>
      <td style="padding: 0.5rem;">TP / (TP + FP)</td>
      <td style="padding: 0.5rem;">False alarms (hallucinated entities)</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Recall</td>
      <td style="padding: 0.5rem;">Did the computer find all true entities?</td>
      <td style="padding: 0.5rem;">TP / (TP + FN)</td>
      <td style="padding: 0.5rem;">Missed entities (silent omissions)</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem;">F1-Score</td>
      <td style="padding: 0.5rem;">What is the overall balanced score?</td>
      <td style="padding: 0.5rem;">2 * (P * R) / (P + R)</td>
      <td style="padding: 0.5rem;">Unbalanced performance</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Precision* — The fraction of retrieved entities that are relevant and accurate. *Recall* — The fraction of true historical entities that the model successfully retrieved. *F1-Score* — The balanced harmonic mean of precision and recall.

**Takeaway:** Precision measures accuracy, recall measures completeness, and F1-Score balances both metrics into a single score.

---

## **14 Content**

**Understanding Error Types: False Positives vs. False Negatives**

To calculate precision and recall, you must classify every machine decision into one of four bins:


1. **True Positive (TP):** The machine predicted an entity, and your manual ground truth confirms it is correct.

2. **False Positive (FP):** The machine predicted an entity that is not in your ground truth (a false alarm).

3. **False Negative (FN):** Your ground truth contains an entity that the machine completely missed (an omission).

4. **True Negative (TN):** Ordinary words that both you and the machine correctly ignored.

If your 20-entity passage produced 14 True Positives, 3 False Positives, and 6 False Negatives, your Precision is $14 / 17 = 82.4\%$. Your Recall is $14 / 20 = 70.0\%$.

**Vocabulary.** *True Positive* — A correctly identified named entity. *False Positive* — An incorrect prediction where ordinary text was falsely tagged as an entity. *False Negative* — A true entity that the machine completely overlooked.

**Takeaway:** Classifying machine decisions into True Positives, False Positives, and False Negatives allows exact mathematical scoring.

---

## **15 Content**

**Automated Gazetteers: Matching Names Against Pre-Compiled Lists**

Statistical sequence models are not the only way to find entities. A **gazetteer pipeline** uses exact dictionary lookup.

A gazetteer is a simple text file containing known historical names, places, and organizations. When your Python script reads a historical document, it searches every token against the gazetteer list.

Look at how a simple Python gazetteer operates:
```python
places = {"Halifax", "Marshalltown", "Digby", "Paris", "Chigabenakady"}
words = text.split()
found_places = [w for w in words if w in places]
```

Gazetteer lookups are lightning fast and 100% predictable. If *Chigabenakady* is in your list, the computer finds it every time. However, gazetteers cannot identify new, unexpected names that are missing from the list.

**Vocabulary.** *Gazetteer Lookup* — Finding entities by matching words directly against a pre-compiled list. *Dictionary Coverage* — The percentage of true entities contained within a gazetteer list.

**Takeaway:** Gazetteer lookups provide fast, reliable matching for known historical names but cannot discover new entities.

---

## **16 Content**

**SpaCy EntityRuler: Combining Rules with Statistical Models**

SpaCy provides a powerful built-in component that bridges rules and statistics: the **EntityRuler**.

The EntityRuler lets you define custom pattern-matching rules using Python dictionaries. You can specify exact word strings, capitalization patterns, or regular expressions.

Look at how you teach SpaCy an Indigenous place name that its statistical model missed:
```python
ruler = nlp.add_pipe("entity_ruler", before="ner")
patterns = [
    {"label": "GPE", "pattern": "Chigabenakady"},
    {"label": "PERSON", "pattern": "Major Jean Baptiste Cope"}
]
ruler.add_patterns(patterns)
```

By placing the EntityRuler *before* the statistical NER model, your verified historical rules take priority. The computer checks your rules first, and uses statistical predictions only for remaining words.

**Vocabulary.** *EntityRuler* — A SpaCy component that applies custom pattern-matching rules before statistical models. *Rule Precedence* — The principle that verified editorial rules override machine statistical guesses.

**Takeaway:** The SpaCy EntityRuler lets you add verified historical names to the pipeline so custom rules override statistical errors.

---

## **17 Content**

**Exporting Automated NER to TEI XML: Building ner_baseline.xml**

To compare automated predictions directly against yesterday's manual ground truth, the computer's output must be exported in the same file format: TEI XML.

Your Python script processes your manuscript text, extracts detected entity spans, and wraps them in TEI elements: `<persName>`, `<placeName>`, `<orgName>`, and `<date>`.

The script saves the result to `ner_baseline.xml`. Every automatically detected entity receives an automated ID, such as `xml:id="ner-01"`. By converting raw SpaCy predictions into structured XML, you prepare the file for direct side-by-side diffing in VS Code.

**Vocabulary.** *XML Serialization* — Converting computer data structures into formatted, valid XML text. *Baseline XML* — The unedited automated output file used to benchmark machine accuracy.

**Takeaway:** Exporting automated predictions into ner_baseline.xml creates a standardized XML file ready for direct comparison with ground truth.

---

## **18 Content**

**The VS Code Side-by-Side Diff Audit**

Now comes your primary scientific task for today: auditing machine predictions against human ground truth using the VS Code diff viewer.

Open your project terminal in VS Code and launch the diff viewer:
```bash
code --diff ground_truth_entities_manual.xml ner_baseline.xml
```

VS Code opens both files in a split-screen view. Differences appear highlighted in red and green:

* **Green on the Left:** Entities from your manual baseline that the computer missed (False Negatives).

* **Red on the Right:** Entities that the computer hallucinated or tagged incorrectly (False Positives).

* **Aligned Blocks:** Entities where both human and computer agreed perfectly (True Positives).

**Vocabulary.** *Diff Viewer* — A software tool that visually highlights textual differences between two files side by side. *Visual Auditing* — Inspecting colored diff lines to locate machine errors rapidly.

**Takeaway:** The VS Code diff viewer highlights discrepancies between manual truth and automated predictions in clear color codes.

---

## **19 Content**

**Building the Discrepancy Table in NER_BENCHMARK.md**

As you inspect the diff, you will record every disagreement in your benchmark report: `NER_BENCHMARK.md`.

You will compile a structured discrepancy table with four columns:

1. **Mention:** The historical word string on the manuscript page.

2. **Manual Truth (9.1):** Your verified human tag and category.

3. **Machine Guess (9.2):** What the automated tool predicted.

4. **Error Diagnosis:** Why the machine failed (e.g., OOV spelling, boundary error, type confusion).

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 0.5rem; text-align: left;">Mention</th>
      <th style="padding: 0.5rem; text-align: left;">Manual Truth (9.1)</th>
      <th style="padding: 0.5rem; text-align: left;">Machine Guess (9.2)</th>
      <th style="padding: 0.5rem; text-align: left;">Error Diagnosis</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Major Cope</td>
      <td style="padding: 0.5rem;"><code>&lt;persName&gt;</code></td>
      <td style="padding: 0.5rem;"><code>Cope (PER)</code></td>
      <td style="padding: 0.5rem;">Boundary error: dropped title</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Chigabenakady</td>
      <td style="padding: 0.5rem;"><code>&lt;placeName&gt;</code></td>
      <td style="padding: 0.5rem;">[None]</td>
      <td style="padding: 0.5rem;">False negative: OOV Indigenous name</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem;">Assemblée</td>
      <td style="padding: 0.5rem;"><code>&lt;orgName&gt;</code></td>
      <td style="padding: 0.5rem;"><code>LOC</code></td>
      <td style="padding: 0.5rem;">Type confusion: tagged org as place</td>
    </tr>
  </tbody>
</table>

Documenting these errors transforms raw numbers into scholarly insight.

**Vocabulary.** *Discrepancy Table* — A structured log listing every point of disagreement between two annotation passes. *Error Diagnosis* — Explaining the linguistic or technical reason behind a machine failure.

**Takeaway:** The discrepancy table in NER_BENCHMARK.md records and diagnoses every machine error against manual ground truth.

---

## **20 Content**

**Preprocessing with Module 6 Normalization**

How can an editor improve automated NER accuracy on historical documents? The most effective strategy is **text preprocessing** using our work from Module 6.

In Module 6, you created normalized reading forms inside `<choice>` tags. Scribes wrote *décrétoit* and *shew'd*; you added normalized forms like *décrétait* and *showed*.

If you feed raw historical ink into SpaCy, OOV errors spike. But if you feed your normalized reading text into the pipeline, dictionary lookups succeed. The model recognizes the modern spelling, predicts the correct entity tags, and transfers those tags back to your diplomatic edition. Preprocessing bridges premodern spelling with modern training models.

**Vocabulary.** *Text Preprocessing* — Cleaning or regularizing text before passing it to machine learning tools. *Normalization Bridge* — Using standardized spellings from choice tags to rescue modern NLP tools.

**Takeaway:** Preprocessing text with Module 6 regularized spellings dramatically increases automated NER accuracy on historical documents.

---

## **21 Content**

**Token Alignment and Overlapping Spans**

When evaluating automated models, you must verify that token counts remain aligned.

If SpaCy splits contractions differently than your manual file, token counts diverge. For example, if your manual ground truth treated *can't* as two tokens (`can` and `n't`) and SpaCy treats it as one token (`can't`), scoring scripts will throw alignment errors.

Always run a token alignment check before calculating final precision and recall. If token counts differ, adjust your tokenization settings in Python before computing performance scores.

**Vocabulary.** *Token Alignment* — Ensuring that two different annotation passes share identical word boundaries and token counts. *Alignment Error* — A mismatch in token splitting that prevents automated scoring scripts from running.

**Takeaway:** Verifying token alignment between manual and machine files is required before calculating precision and recall.

---

## **22 Content**

**Entity Linking: From Tagged Spans to External Records**

Extracting an entity span is only the first half of the task. The second half is **Entity Linking** (also called entity disambiguation or Wikification).

Entity linking matches an extracted string (like *Halifax*) to a specific authority record in Wikidata, VIAF, or GeoNames.

Automated sequence models like SpaCy find the boundaries of names, but standard models do not link them to external URLs by default. To automate entity linking, digital scholars use specialized linking libraries like SpaCy-Entity-Linker or direct API queries against Wikidata.

**Vocabulary.** *Entity Linking* — Connecting a detected entity span to its specific entry in an external knowledge base. *Wikification* — Automatically linking text mentions to relevant Wikipedia or Wikidata articles.

**Takeaway:** Entity linking connects raw detected name strings to specific external authority records in public knowledge graphs.

---

## **23 Content**

**Wikidata API Queries in Python**

You can automate entity linking in Python by sending search requests directly to the Wikidata Web API.

When your script detects an entity span like *Maud Lewis*, it formats a search URL and retrieves matching Wikidata entities in JSON format:
```python
import urllib.request, json, urllib.parse

query = urllib.parse.quote("Maud Lewis")
url = f"https://www.wikidata.org/w/api.php?action=wbsearchentities&search={query}&language=en&format=json"
req = urllib.request.urlopen(url)
data = json.loads(req.read().decode())

top_result = data["search"][0]
print(top_result["id"], top_result["label"], top_result["description"])
```

Within half a second, the API returns `Q1479154`: "Canadian folk artist (1903–1970)." Your script captures this ID and writes it into the `@ref` attribute.

**Vocabulary.** *Web API* — An online interface that allows software programs to request and receive structured data automatically. *JSON* — JavaScript Object Notation, the standard data format for web API responses.

**Takeaway:** Python scripts can query the Wikidata API automatically to retrieve Q-identifiers for detected entities.

---

## **24 Content**

**The Ambiguity Trap in Automated Linking**

Automated entity linking works well for famous, unique names. But it falls into catastrophic traps when a name is common or ambiguous.

Suppose your script searches the Wikidata API for the surname *Cope* from the 1752 Treaty. The API returns dozens of results: Edward Drinker Cope (the American paleontologist), Arthur Cope (the British portrait painter), and Julian Cope (the rock musician).

An automated script without historical context often defaults to the most famous modern result. It might link an eighteenth-century Mi'kmaw leader to a twentieth-century rock singer. Human supervision is required to prevent absurd automated linking errors.

**Vocabulary.** *Linking Ambiguity* — When a search query matches multiple plausible authority records in a knowledge base. *Default Bias* — An automated algorithm's tendency to select the most popular modern record when multiple matches exist.

**Takeaway:** Automated linking frequently confuses historical figures with famous modern names; human supervision prevents absurd errors.

---

## **25 Content**

**Handling Verified Absences in Automated Pipelines**

What happens when an automated linking script searches Wikidata for a historical person who has no record?

Standard API scripts are programmed to return the closest fuzzy match. If a minor French clerk or rural correspondent has no entry, the algorithm picks the nearest similar name.

A scholarly pipeline must include a **similarity threshold gate**. If the API's top match score falls below an editorial confidence threshold (such as 85%), the script must record a null result rather than attaching a false match. The mention remains tagged in TEI XML, but the `@ref` attribute points to your local `<particDesc>` in the header.

**Vocabulary.** *Confidence Threshold* — A minimum mathematical score required before an automated tool accepts an API match. *Fuzzy Matching* — Searching for strings that are approximately similar rather than exact matches.

**Takeaway:** Setting a strict confidence threshold prevents automated linking scripts from attaching false matches to unindexed people.

---

## **26 Content**

**Synthesizing Results: Writing NER_BENCHMARK.md**

Today's lab culminates in the creation of your formal benchmark report: `NER_BENCHMARK.md`. This file documents your empirical findings in your project repository.

Your report must contain four core sections:

1. **Pipeline Configuration:** Detail the model used (`en_core_web_sm` or `fr_core_news_sm`), Python version, and parameters.

2. **Quantitative Scores:** Report your exact Precision, Recall, and F1-Scores against Tuesday's manual table.

3. **Discrepancy Analysis:** Include your four-column discrepancy table diagnosing every machine error.

4. **Scholarly Reflection:** A 200–300 word discussion explaining why the automated model struggled with your specific historical witness.

**Vocabulary.** *Benchmark Report* — A formal document reporting the quantitative accuracy and error analysis of a computational tool. *Empirical Findings* — Results derived from actual experimental data and mathematical measurement.

**Takeaway:** NER_BENCHMARK.md documents your model setup, accuracy scores, error diagnoses, and methodological reflection.

---

## **27 Content**

**The Error Taxonomy: Four Reasons Machines Fail**

In your benchmark report, classify every error according to our four-part course taxonomy:


1. **Historical Orthography (OOV):** Archaic spellings, contractions, or suffixes confused the model.

2. **Boundary Truncation:** The model dropped honorific titles, prepositions, or surrounding words.

3. **Type Confusion:** The model assigned the wrong category (e.g., tagging an organization as a place).

4. **Toponym Blindness:** The model completely overlooked a regional or Indigenous place name missing from global training data.

This taxonomy proves that you understand *why* the tool failed, not just that it produced a wrong answer.

**Vocabulary.** *Error Taxonomy* — A structured classification system that groups mistakes by their underlying technical causes. *Toponym Blindness* — The total failure of an algorithm to recognize a geographic name.

**Takeaway:** Grouping errors into our four-part taxonomy explains the technical and linguistic causes behind machine failures.

---

## **28 Content**

**Refining the Pipeline: Adding Custom Rules to Boost Recall**

Before finalizing your benchmark, you can test how much custom rules improve performance.

In your Python script, add an `EntityRuler` containing three or four project-specific patterns. Add patterns for your document's primary historical figures and Indigenous place names.

Rerun your pipeline and recompute your scores. You will watch your Recall jump from 70% to 90% or higher. Documenting this performance boost shows how human editorial rules rescue general-purpose computer models.

**Vocabulary.** *Performance Boost* — A measurable increase in accuracy achieved by tuning an algorithm or adding custom rules. *Hybrid Pipeline* — A computational pipeline that combines human-authored rules with machine-learned statistical models.

**Takeaway:** Adding custom patterns via EntityRuler rescues missing entities and demonstrates the power of hybrid workflows.

---

## **29 Content**

**Preparing for Friday's AI Synthesis Test**

Today's deterministic experiments provide the essential middle tier of our three-step comparative cycle.

On Tuesday, you established manual ground truth. Today, you tested deterministic natural language processing models, observing their speed, rigidity, and predictable blind spots.

On Friday, in Lesson 9.3, you will test large language model artificial intelligence prompts on this exact same passage. You will compare human close reading, statistical sequence taggers, and generative AI in a comprehensive three-way audit.

**Vocabulary.** *Three-Step Cycle* — The course's core method: comparing manual baseline, deterministic automation, and AI models on the same text. *Three-Way Audit* — A comprehensive comparison evaluating the strengths and weaknesses of three distinct editorial methods.

**Takeaway:** Today's deterministic benchmark establishes the middle comparison tier for Friday's three-way audit with generative AI.

---

## **30 Content**

**The Stage Gate: Committing Your Benchmark and Pipeline**

You have reached the stage gate for Step 2 of Module 9. Today, you moved from manual cataloguing to automated algorithmic processing.

You authored a Python NER script, processed your 20-entity excerpt, exported `ner_baseline.xml`, and conducted a side-by-side diff in VS Code. You computed exact precision and recall scores and diagnosed every error in `NER_BENCHMARK.md`.

Stage and commit all four files to your git repository:
```bash
git add ner_pipeline.py ner_baseline.xml NER_BENCHMARK.md
git commit -m "Week 9 Step 2: deterministic NER pipeline and benchmark audit"
```

Verify that your working tree on `main` is clean. On Friday, we bring generative artificial intelligence into our workflow to complete our three-way synthesis.

**Vocabulary.** *Stage Gate Commit* — A verified git commit that locks in project deliverables before beginning the next phase. *Clean Working Tree* — A git status showing that all changes are committed and no untracked files remain.

**Takeaway:** Committing your pipeline script, baseline XML, and benchmark report completes Step 2 and prepares your repository for Friday's AI audit.

---
