# Lesson 2.3 — AI-Assisted Metadata Enrichment, Entity Extraction, and Validation Auditing

*RELS 398 / ENGL 398 · Topic 2: Cataloguing · Meeting #5 (Fri Sep 11)*

***Step 3 of the three-step cycle: AI-assisted.** On Tuesday you wrote a TEI header by hand. On Wednesday you made a schema check it. Today you ask a machine to write the same header, put its work through the same schema, and score it against yours. The comparison is the lesson.*

---

## **01 Content**

**Why Anyone Would Let a Machine Catalogue a Manuscript**

Start with the size of the problem. Libraries, monasteries, and university archives around the world hold hundreds of thousands of handwritten books and documents that have never been properly catalogued. Many are described only in handwritten registers from the nineteenth century. Some are described nowhere at all.

You now know why this backlog is so hard to clear, because on Tuesday you cleared exactly one page of it. Writing a good `<msDesc>` takes a person who can read the script, recognize the material, count the hands, and encode all of it in TEI. That person works in hours per folio. At that rate, cataloguing the world's manuscripts is not slow. It is impossible (De Cristofaro & Zilio, 2025).

So researchers have started handing the job to AI. Large language models can read a page of catalogue prose and return a tagged TEI header in seconds. That is roughly ten thousand times faster than you were on Tuesday.

The catch is the one you met in Lesson 1.1: these models are prediction engines, not truth engines. They invent scribal hands that never existed, dates that were never recorded, and XML tags that no schema allows (De Cristofaro & Zilio, 2025). Today's question is not "can AI catalogue manuscripts." It plainly can. The question is how you measure what it produced, and how you catch what it made up.

**Takeaway:** AI can generate manuscript metadata thousands of times faster than a human, but because it predicts rather than knows, the real skill is measuring and auditing what it produces.

---

## **02 Content**

**What the Model Is Actually Doing When It Writes TEI**

Lesson 1.1 told you that a large language model predicts likely text. It is worth being precise about what that means when the text is XML.

The model has read enormous amounts of writing, including a great deal of public TEI. It has seen thousands of real `<teiHeader>` elements. So when you give it a manuscript description, it is not consulting a rulebook about TEI. It is answering a much simpler question, over and over: given everything so far, what usually comes next?

After `<msIdentifier>`, a `<repository>` usually comes next. After a description mentioning animal skin, `material="parchment"` usually comes next. The model is very good at "usually."

This explains both its strength and its weakness. Its strength is fluency: it produces TEI that looks right immediately, because it has seen so much TEI that looks right. Its weakness is that "usually correct" and "valid" are different standards. The model has no copy of `msdesc.rng` in its head and no way to check itself against one (De Cristofaro & Zilio, 2025). It has a strong sense of what TEI tends to look like and no knowledge of what this schema actually permits.

Keep that distinction in view all day. Fluency is not knowledge, and the machine has plenty of the first.

**Takeaway:** An LLM writes TEI by predicting what usually comes next, which makes its output fluent and plausible without making it valid.

---

## **03 Content**

**Two Ways of Being Right**

Wednesday and Friday put two very different kinds of tool side by side, and they disagree about what "correct" means.

The schema you used on Wednesday is deterministic. Give it the same file twice and you get the same answer twice. It has a fixed list of what may appear, in what order, inside what parent. It does not care what your manuscript means. It has one question: does this tree obey the rules?

The model you use today is probabilistic. Give it the same prompt twice and you may get two different headers. It has no fixed rules at all. What it has is a sense of meaning: it can tell that a phrase about a leaf's height belongs somewhere near the physical description, even if nobody told it so.

| What you want done | The schema (Wednesday) | The model (Friday) |
| --- | --- | --- |
| Enforce element order and nesting | Reliable; this is its entire job | Approximate; obeys when it happens to |
| Read messy prose and find the meaning | Cannot do this at all | Genuinely good at it |
| Give the same answer every time | Always | Not guaranteed |
| Notice that a date is not really a date | Catches the format, not the fact | Will happily invent a plausible one |

Neither tool is the smarter one. They fail in opposite directions, which is exactly why they work well together: the model proposes, and the schema refuses.

**Takeaway:** Schemas are consistent but meaningless, while models are meaningful but inconsistent, so a serious pipeline uses each to cover the other's blind spot.

---

## **04 Content**

**Asking Well: How to Prompt for TEI**

If you type "convert this into TEI XML," you will get something disappointing. It will be wrapped in chatty preamble, sprinkled with invented tags, and rejected by the schema on the first line. That is not the model failing. That is the prompt failing.

Researchers who do this at scale have converged on a few habits, and you can use all of them today (De Cristofaro & Zilio, 2025).

- **Say who the model is.** "You are cataloguing a manuscript in TEI P5" narrows what "usually comes next" means. It is a cheap way to move the model into the right neighbourhood of everything it has read.
- **Say which tags are allowed.** Paste the element names you expect. The model cannot consult the schema, so the closest substitute is putting part of the schema in front of it.
- **Show a finished example.** One correct header teaches the model your house style faster than three paragraphs of instruction. Two is better.
- **Demand XML and nothing else.** Otherwise you will spend the lab deleting "Certainly! Here is your TEI header:" from the top of the file.
- **Turn down the randomness.** Most interfaces expose a setting called temperature. High temperature makes the model more inventive; low temperature makes it more predictable. For markup you want predictable, so set it low, near zero if you can.

```
A workable system prompt:

"You are cataloguing a manuscript in TEI P5.
Rules:
1. Output only a <TEI> element with the TEI namespace. No commentary.
2. Follow the hierarchy teiHeader > fileDesc > sourceDesc > msDesc.
3. Dates in @when, @notBefore, @notAfter must be YYYY or YYYY-MM-DD.
4. Use only elements from the TEI manuscript description module.
5. Write & as &amp;."
```

**Takeaway:** A good TEI prompt names the role, lists the permitted tags, shows a worked example, forbids commentary, and lowers the temperature.

---

## **05 Content**

**Why Your Own Header Is the Measuring Stick**

A system cannot grade itself. To say anything meaningful about the AI's output, you need an independent reference to compare it against. You built that reference this week without being told that was what you were doing.

Tuesday's hand-authored header is your ground truth: the version made by someone who looked at the actual object. Wednesday's validated header is your structural baseline: the version certified at zero errors. Together they are the standard the machine gets measured against (De Cristofaro & Zilio, 2025).

This matters more than it might sound. Without a baseline, all you can say about an AI header is that it looks impressive, which is worth nothing, because looking impressive is the one thing these models are guaranteed to do. With a baseline you can say something precise: it invented a shelfmark, it missed two hands, it got the material right.

| What you compare | Your header (Tue/Wed) | The AI header (today) |
| --- | --- | --- |
| Well-formed XML | Yes, you fixed it until it was | Usually, but not always |
| Passes the schema | Yes, certified at 0 errors | This is what you are measuring |
| Facts about the object | Checked against the image | Confident, and sometimes fictional |
| Links to VIAF and Pleiades | Chosen by you, verified | Often plausible and dead |

**Takeaway:** Tuesday's header and Wednesday's zero-error file are the independent reference that turns an impression of cleverness into a measurable claim.

---

## **06 Content**

**A Real Experiment: The PubCINET Study**

You are not the first to run today's comparison. In 2025, De Cristofaro and Zilio ran it properly, at scale, and published what happened. Their results are the backbone of this lesson.

Their project, PubCINET, was reconstructing the networks of Italian publishing and cinema from the 1950s to the 1980s. That meant thousands of unpublished letters and manuscripts to catalogue, and a backlog like the one described in section 01 (De Cristofaro & Zilio, 2025).

Their method should look familiar, because it is the method you are following today. They gave each model a careful system prompt, a reference file listing the people and places the project had already verified, and the raw transcribed text. They collected the XML that came back. Then they ran every file through automated schema validation and counted the errors (De Cristofaro & Zilio, 2025).

The one difference worth noting is that they tested two models against each other: OpenAI's ChatGPT-4 and Anthropic's Claude 3.5 Sonnet, the two leading systems at the time of the study. What they found was not that one model was better. It was that the two failed in opposite directions, which turned out to be far more useful to know.

**Takeaway:** The PubCINET study ran this same comparison across two models at scale, and found that different models fail in systematically different ways.

---

## **07 Content**

**The First Profile: Smart About Meaning, Careless About Structure**

ChatGPT-4, in that study, was remarkably good at understanding what the documents were about (De Cristofaro & Zilio, 2025).

When a letter referred to someone by a nickname, a first name only, or an oblique allusion, the model repeatedly worked out who was actually meant, and connected that person to information the prompt had never supplied. That is genuinely hard. It is the kind of inference you would expect from a research assistant who knows the period.

The structure was another story. The same model routinely failed schema validation. It closed containers before their required children were inside them, nested elements where the schema forbids it, and invented tags that TEI does not define (De Cristofaro & Zilio, 2025).

The pattern behind both results is one thing, not two. The model optimizes for meaning. When capturing the sense of a document and obeying the grammar of a schema pull in different directions, meaning wins, because meaning is what it was built to chase.

```
Profile 1 (De Cristofaro & Zilio, 2025):
- Recognizing implied people and places .... strong
- Reading between the lines ............... strong
- Well-formed XML ......................... usually
- Passes the RELAX NG schema .............. often not
- Internal cross-references intact ........ often not
```

**Takeaway:** A model that optimizes for meaning will read a document impressively and break the schema doing it.

---

## **08 Content**

**Structural Hallucination: Confident XML That Cannot Exist**

You already know that models hallucinate facts. There is a second kind, and it is the kind a schema can actually catch.

A structural hallucination is markup that looks entirely reasonable and is illegal in this schema. The model is not confused about the manuscript. It is confused about the rules, because it never had them (De Cristofaro & Zilio, 2025).

Three kinds show up constantly.

- **Closing a container too early.** The model writes `</profileDesc>` and then keeps going with elements that were supposed to be inside it. The children end up orphaned outside their parent.
- **Reaching for HTML.** Models have read far more HTML than TEI. Under pressure they reach for `<p>` or `<br>` in places where TEI allows neither. You saw this exact trap on Wednesday, when `<extent>` refused a `<p>` that `<support>` accepts one line above.
- **Inventing character entities.** `&copy;` and `&nbsp;` are ordinary in HTML and undefined in XML. One of them anywhere in the file is fatal: the parser stops, and you get no validation report at all.

| What the model wrote | Why the schema refuses it |
| --- | --- |
| `</profileDesc><langUsage>...</langUsage>` | `langUsage` belongs inside `profileDesc`, not after it |
| `<closer><p>Yours faithfully,</p></closer>` | `closer` takes phrases, not paragraphs |
| `<p>Copyright &copy; 2026</p>` | `copy` is an HTML entity; XML has never heard of it |
| `<supportDesc support="parchment">` | The attribute is `material`, not `support` |

Every one of these is caught by the check you already know how to run.

**Takeaway:** Structural hallucinations are plausible, illegal markup — early closures, stray HTML, undefined entities — and Wednesday's schema catches all of them.

---

## **09 Content**

**The Second Profile: Obedient About Structure, Silent About the Rest**

Claude 3.5 Sonnet, in the same study, behaved almost as the mirror image (De Cristofaro & Zilio, 2025).

Its XML was clean. Given the system prompt and the schema constraints, it produced valid TEI on the first attempt, with correct nesting and correctly formatted dates, and without reaching for HTML. Where the other model needed repeated correction, this one usually needed none (De Cristofaro & Zilio, 2025).

The cost appeared elsewhere. It stayed strictly inside what it had been given. If a letter mentioned a person who was not in the project's reference list, the model tended to leave them untagged rather than work out who they were. The markup was flawless and the record was incomplete (De Cristofaro & Zilio, 2025).

That failure is harder to catch than the first one, and worth pausing on. A missing entity produces no error. The schema is satisfied, the file is green, and the omission is invisible unless a human notices something absent. Broken structure announces itself. Silence does not.

```
Profile 2 (De Cristofaro & Zilio, 2025):
- Recognizing implied people and places .... cautious; skips the unlisted
- Reading between the lines ............... rarely attempts it
- Well-formed XML ......................... clean
- Passes the RELAX NG schema .............. clean
- Internal cross-references intact ........ reliable
```

**Takeaway:** A model that obeys the schema perfectly can still omit entities silently, and omissions produce no error to catch them.

---

## **10 Content**

**The Trade-Off, and What to Do About It**

Put the two profiles together and a pattern appears that has held up well beyond this one study (De Cristofaro & Zilio, 2025).

| | Strong at | Weak at | Sensible use |
| --- | --- | --- | --- |
| Meaning-first model | Finding entities nobody listed | Obeying the schema | First-pass discovery of what is in the document |
| Structure-first model | Producing valid TEI directly | Noticing the unlisted | Turning verified facts into correct markup |

The practical conclusion is that a single model working unsupervised is the wrong design, whichever model you choose. One will hand you rich content in broken markup; the other will hand you clean markup missing content. Neither is finished work.

What functions is a pipeline: one pass to find what is there, a second to encode it properly, and the schema gate standing between them and publication (De Cristofaro & Zilio, 2025).

Notice that this is your three-step cycle with the labels changed. Discovery, then structure, then verification. You have been practising the shape of a professional pipeline all week.

**Takeaway:** No single model is both semantically thorough and structurally obedient, so real pipelines combine models and put a schema gate between them and publication.

---

## **11 Content**

**Giving the Model a List Instead of Letting It Guess**

Ask a model to add VIAF identifiers and it will produce VIAF identifiers. They will be correctly formatted. Some of them will lead nowhere, and some will lead confidently to the wrong person (De Cristofaro & Zilio, 2025; Koho et al., 2021).

This is worth sitting with, because it is the single most dangerous behaviour in the whole lesson. On Wednesday you looked up your repository's VIAF record yourself and pasted the identifier you found. A model does not look anything up. It produces a string of the right shape, which is what it was asked for.

The fix is disarmingly simple. Stop asking the model to supply identifiers and start asking it to choose from ones you have already verified. Compile a small reference file of the people and places your project has confirmed, each with its checked URI, and put that file in the prompt (De Cristofaro & Zilio, 2025).

```xml
<!-- A project's verified reference list, supplied with the prompt -->
<authorityList>
  <personList>
    <person xml:id="pers_origen" ref="https://viaf.org/viaf/34454471">
      <persName>Origen of Alexandria</persName>
    </person>
  </personList>
  <placeList>
    <place xml:id="place_alexandria" ref="https://pleiades.stoa.org/places/727070">
      <placeName>Alexandria</placeName>
    </place>
  </placeList>
</authorityList>
```

Now the instruction is "use only identifiers from this list." An open-ended invention problem has become a matching problem, and matching is something these models do well.

**Takeaway:** Models fabricate authority URIs when asked to supply them, so give them a verified list and let them match instead of invent.

---

## **12 Content**

**Finding Names in Text That Was Not Written for You**

Recognizing a name in a historical document and working out which person it refers to is harder than it sounds, and it is where a model's semantic strength genuinely earns its place (Koho et al., 2021; Koho et al., 2023).

Three difficulties defeat simple search-and-match.

- **Spelling was not standardized.** The same person appears as *Marchalianus*, *Marchal*, and *Marcialis*, depending on the scribe and the century.
- **Names repeat endlessly.** Dozens of medieval bishops are named Johannes. The name alone identifies nobody.
- **Scribes often do not use names at all.** A figure may appear only as "the blessed bishop," with the identification assumed to be obvious.

A model handles this kind of ambiguity far better than a keyword search, because resolving it requires context rather than matching (De Cristofaro & Zilio, 2025).

It also gets it wrong in ways a keyword search never could. Faced with a marginal note crediting a reading to "Theodotion," a model must decide whether that means the second-century translator or a later copyist of the same name. It will decide. It will not tell you it was a decision, and it will sound equally confident either way.

**Takeaway:** Models resolve ambiguous historical names better than keyword matching, and state their guesses with the same confidence as their certainties.

---

## **13 Content**

**The Failure the Schema Cannot See**

Everything so far has been catchable. This section is the one that is not, and it is the most important idea in the lesson.

Suppose a model is given a thin description: *Vat. gr. 2125: 6th-century prophetic codex, uncial script, damaged at the beginning, provenance Egypt.* You ask it for a full `<history>`. It returns this.

```xml
<!-- Generated by a model. Every fact in it is invented. -->
<provenance notBefore="0700" notAfter="0750">
  <p>Transferred in 722 CE to the Monastery of Saint Catherine at Mount Sinai
     by the monk Dorotheus, and recorded in the 8th-century library inventory.</p>
</provenance>
```

Look at what this passes. The XML is well-formed. The elements are real TEI. The dates are correctly formatted ISO 8601 and consistent with each other. Run it through Wednesday's schema and it reports zero errors.

Mount Sinai is invented. Dorotheus is invented. The year 722 is invented. The inventory is invented. The model assembled a plausible provenance out of general knowledge about how manuscripts moved, and the result is fiction in perfect TEI.

Nothing in your toolchain will flag this. A schema checks shape, not truth. The only instrument that catches a fabricated provenance is an editor who knows the manuscript — which is the answer to the question of what you are for, once machines can write markup faster than you can.

**Takeaway:** A schema validates structure and cannot validate facts, so schema-valid output can be entirely fabricated and only a human editor will notice.

---

## **14 Content**

**Metadata That Lives in the Image, Not the Text**

Everything so far has assumed the AI is reading text. But a good deal of what you recorded on Tuesday was never written down anywhere. You got it by looking.

Column counts, ruled lines, margin widths, the size and colour of initials, ownership stamps, wormholes and water damage: none of this appears in a catalogue description. It exists in the object, and in the digital image of the object (Ignatowicz et al., 2025).

So a second family of AI works on pixels rather than prose. Computer vision models examine a high-resolution facsimile and try to find and classify physical features directly (Ignatowicz et al., 2025).

| Stage | What happens |
| --- | --- |
| Detection | Scan the page image and mark regions that look like stamps, initials, or text columns |
| Cropping | Cut each marked region out as its own small image |
| Interpretation | Read or identify what is in each crop |
| Encoding | Emit the results as TEI, mostly into `<physDesc>` |

The appeal is obvious. Measuring margins by hand across ten thousand folios is not work anyone will fund. Measuring them automatically is a script that runs overnight.

**Takeaway:** Computer vision targets the codicological evidence that exists only in the image — layout, decoration, damage — and never appears in catalogue prose.

---

## **15 Content**

**Looking at a Page in Layers**

A page does not decompose into a flat list of things. It nests, the same way your TEI nests, and vision systems that ignore that nesting perform badly (Ignatowicz et al., 2025).

Consider what your own witness looks like. The page contains a text block. The text block contains a decorated initial. The initial contains a small figure. Beside all of it sits an owner's stamp, and inside the stamp is an inscription. Ask a detector for "the objects on this page" and it will return some of these and miss the rest, because several of them are inside each other.

The Metadata Enrichment Model, built by Ignatowicz, Kutt, and Nalepa (2025) for the Jagiellonian Digital Library, addresses this by looking more than once, at different scales.

1. **The wide pass** finds the big architectural pieces: columns, margins, major decorated areas, the block of writing.
2. **The close pass** crops each of those regions and examines it on its own terms, where a small initial is no longer a speck in a corner but the whole picture.
3. **The interpretation pass** takes each crop and asks what it actually is — reading an inscription, identifying a motif, matching a coat of arms to a known family (Ignatowicz et al., 2025).

The structure is the same one you use when you catalogue by eye. You take in the page, then look closely at one feature, then decide what that feature means. The system is imitating an order of operations you already perform.

**Takeaway:** Manuscript features nest inside one another, so vision systems examine a page in layers — wide, close, then interpretive — much as a cataloguer does.

---

## **16 Content**

**From Pixel Coordinates to TEI Elements**

The point of detecting a region is not the box around it. The point is that each kind of region maps onto a TEI element you already know how to write (Ignatowicz et al., 2025).

- **Ownership stamps** are found by shape, then read, and become part of `<provenance>` — the custodial chain you encoded on Tuesday.
- **Decorated initials** are outlined, measured in lines of height, and described in `<decoDesc>`.
- **Ruling and column edges** are traced as lines, which yields the column count and written-line count for `<layoutDesc>`.
- **Damage** — ink corrosion, wormholes, staining, cropped margins — is detected as a category of its own and becomes `<condition>`.

| Feature on the page | How it is found | Where it lands in TEI |
| --- | --- | --- |
| Library ownership stamp | Shape detection, then text reading | `<provenance>` |
| Decorated initial | Outline and measure in lines | `<decoDesc>` |
| Column boundaries | Line detection across the page | `<layout columns="1" writtenLines="29">` |
| Leaf dimensions | Pixel measurement against a known scale | `<extent><dimensions unit="mm">` |
| Marginal annotation | Region outline beside the text block | `<additions>` |

That right-hand column is the useful part of this section. These are the same elements you filled in by hand on Tuesday. The pipeline is not doing something exotic; it is doing your job, from the image, at speed.

**Takeaway:** Each detected visual region maps onto a TEI element you already write by hand, so vision pipelines populate `physDesc` rather than inventing a new vocabulary.

---

## **17 Content**

**Turning a Picture into a Statement**

On Wednesday you learned that linked data is built from three-part statements: something, a relationship, something else. Vision pipelines produce exactly that shape, from images (Ignatowicz et al., 2025; Koho et al., 2023).

The sequence runs like this. The detector finds an oval stamp on the first folio. The interpretation pass reads it and matches the design against known institutional marks. The result is written as a statement in a standard format that any linked-data system can read.

```turtle
# The stamp on folio 1r, expressed as linked data
<http://example.org/manuscript/vat_gr_2125>
    bears_feature  <http://example.org/feature/stamp_001> .

<http://example.org/feature/stamp_001>
    is_a           <http://vocab.getty.edu/aat/300028744> ;   # "library stamps"
    identifies     <http://www.wikidata.org/entity/Q213878> ; # the Vatican Library
    has_note       "Oval ink stamp on fol. 1r" .
```

Read it as sentences and it is unremarkable. This manuscript bears this feature. This feature is a library stamp. This stamp identifies the Vatican Library.

What has happened is that a mark in a photograph became a claim other systems can find. Someone searching for every manuscript that passed through the Vatican Library can now find this one, without ever opening the image. That is the whole promise of linked data from Wednesday, arriving from an unexpected direction.

**Takeaway:** Vision pipelines convert visual features into the same three-part linked-data statements you met on Wednesday, making a mark in a photograph searchable worldwide.

---

## **18 Content**

**Where Vision Models Fail, and Who Pays for It**

Vision models were trained mostly on clean modern documents. Your manuscript is neither (Ignatowicz et al., 2025).

Centuries of handling leave a page full of things that look like features and are not: faded ink, writing showing through from the other side, water stains, mould, insect damage. Three failures follow predictably.

- **Stains read as decoration.** A dark water stain or a grease spot has roughly the shape and contrast of a small illumination, and gets confidently labelled as one.
- **Damage splits a column.** A tear or a mould patch running down a page can make one continuous text column register as two or three separate fragments.
- **The training data was European.** Most open image collections come from Western European libraries. Models built on them handle Latin codices well and misread or entirely miss Syriac flourishes, Coptic initials, and Ethiopic decorative headpieces (Ignatowicz et al., 2025).

That third failure deserves more than a technical note. It means these tools work least well on exactly the traditions that are already least well catalogued. Run an unaudited pipeline across a mixed collection and you will widen the gap between the well-described and the neglected, using a tool that appears neutral. That is a scholarly and ethical problem, not a bug report.

**Takeaway:** Vision models misread damage as decoration and perform worst on non-Western material, so unaudited automation deepens exactly the cataloguing inequities it claims to fix.

---

## **19 Content**

**Two Numbers That Describe Any Extraction**

You need a way to say how good an AI header was that survives contact with someone who disagrees with you. Two numbers do most of the work, and you can calculate both by hand today (De Cristofaro & Zilio, 2025).

Go field by field — repository, shelfmark, material, extent, number of hands, date — and sort every field into three piles.

- **Right:** the AI supplied it and it matches your verified header.
- **Wrong or invented:** the AI supplied it and it does not match, or it supplied something that is not true at all.
- **Missing:** it is in your header, and the AI left it out.

Now the two numbers.

**Precision** asks: of everything the AI claimed, how much was right? Divide the right answers by everything it supplied. Low precision means it makes things up.

**Recall** asks: of everything that should have been found, how much did it find? Divide the right answers by everything in your header. Low recall means it leaves things out.

These measure different failures, and a model can be excellent at one while poor at the other. The structure-first model from section 09 has high precision and lower recall: what it says is right, and it says too little. The meaning-first model from section 07 is the reverse. Report only one number and you have hidden half of what happened (De Cristofaro & Zilio, 2025).

Combine them into a single score if you like — that combined figure is called F1 — but the pair is more informative than the average.

**Takeaway:** Precision measures how much of what the AI said was true, recall measures how much of the truth it found, and the two fail independently.

---

## **20 Content**

**Counting Errors Without Reading Them**

Today you will open the AI's file and look at the error count yourself. At a hundred files that stops being possible, so the count gets automated (De Cristofaro & Zilio, 2025).

The idea needs no new concepts. You learned in Lesson 1.1 that Python can do a mechanical job in milliseconds that would take you an afternoon. Checking whether a file is well-formed and whether it satisfies a schema is exactly that kind of job.

```python
# Score one AI-generated TEI file: is it parseable, and does it satisfy the schema?
import subprocess
from lxml import etree

def score(xml_path, schema_path):
    result = {"well_formed": False, "valid": False, "errors": []}

    try:
        etree.parse(xml_path)
        result["well_formed"] = True
    except etree.XMLSyntaxError as e:
        result["errors"].append(f"Not well-formed: {e}")
        return result          # a broken file cannot be schema-checked at all

    check = subprocess.run(["jing", schema_path, xml_path],
                           capture_output=True, text=True)
    result["valid"] = (check.returncode == 0)
    result["errors"] = check.stdout.strip().splitlines()
    return result
```

Note the early return. If the XML is not well-formed, the schema check never runs, because there is no tree to check. That is the same order of operations VS Code follows for you: syntax first, then schema.

Run this across a batch and you get one honest number — how many files passed — instead of an impression.

**Takeaway:** A short Python script checks well-formedness and then schema validity, turning a pile of AI files into a countable pass rate.

---

## **21 Content**

**Handing the Errors Back**

When the AI's file fails validation, you do not have to repair it yourself. You can show the model its own error messages and ask again (De Cristofaro & Zilio, 2025).

This works better than it has any right to. The reason is section 02: the model never had the schema. An error message is a small, precise piece of the schema, delivered exactly where it is needed. You are supplying the missing rulebook one line at a time.

| Step | What happens |
| --- | --- |
| 1 | The model produces a first draft header |
| 2 | The validator checks it against `msdesc.rng` |
| 3 | Zero errors, and you are done; otherwise capture the messages |
| 4 | Paste the messages back to the model and ask for a repair |
| 5 | The model returns a new file, which goes back through step 2 |

```
What you paste back:

"Your TEI failed validation with these 2 errors:
 1. line 14: element 'supportDesc' not allowed here; expected inside 'objectDesc'
 2. line 28: value 'ca. 550' is not a valid date
Return only the corrected XML."
```

Try this today on whatever your model got wrong. It is the fastest way to feel the difference between a system that cannot follow rules and one that was simply never given them.

**Takeaway:** Feeding validation errors back to the model supplies the schema knowledge it never had, and repairs most structural failures without your editing a tag.

---

## **22 Content**

**How Many Rounds Before It Gives Up**

The correction loop is not magic, and it does not always converge. De Cristofaro and Zilio (2025) measured how many rounds different models needed.

| Model | Valid on first try | After one correction | After two | Never converges |
| --- | --- | --- | --- | --- |
| Meaning-first (ChatGPT-4) | 35% | 78% | 91% | 9% |
| Structure-first (Claude 3.5 Sonnet) | 88% | 98% | 100% | 0% |
| Small open-source model | 5% | 22% | 41% | 59% |

Three things in this table are worth your attention.

The structure-first model was nearly always right immediately and always right by the second round. The meaning-first model improved sharply when corrected but kept a stubborn remainder, where repairing one error introduced another and the loop went in circles.

The small open-source model is the interesting row. It did not merely start badly; it failed to improve. Reading a compiler message and working out what it implies about a tree structure is itself a hard reasoning task, and a model that cannot do it will resubmit the same mistake indefinitely (De Cristofaro & Zilio, 2025).

The practical lesson: put a limit on your loop. Two or three attempts, then it goes to a human. Without a cap you can burn an afternoon watching a model retype the same error.

**Takeaway:** Correction loops converge in one or two rounds for capable models and never converge for weak ones, so always cap the number of attempts.

---

## **23 Content**

**Citations the Model Cannot Check**

On Wednesday you built a CTS URN for your passage. It is a strict, multi-part identifier, and every part must be right for it to resolve (Blackwell & Smith, 2019; Tiepmar & Heyer, 2014).

Ask a model to build one and you will get something with the right shape. Shape is not the problem. Three specific things go wrong.

- **Invented namespaces.** `urn:cts:bible:` looks reasonable and does not exist; the real one is `urn:cts:greekLit:`.
- **Wrong work numbers.** The model half-remembers a TLG number and assigns Homer's identifier to Isaiah. The URN is perfectly formed and points at the wrong text.
- **Invented word positions.** A sub-reference may point to the fifth occurrence of a word that appears three times (Blackwell & Smith, 2019).

Every one of these produces a citation that looks correct in your file and fails when someone tries to follow it. Since the entire purpose of a canonical URN is to still resolve in fifty years, a fabricated one is worse than none: it is a broken promise that looks like a kept one.

The rule is the same as section 11. Do not accept an identifier from a model. Check it against the actual CTS service before it goes in the file (Tiepmar & Heyer, 2014).

**Takeaway:** Models produce correctly shaped CTS URNs that point nowhere, so every generated identifier must be resolved against a real service before it is committed.

---

## **24 Content**

**Sorting the Differences**

Now the core exercise. Put your validated header beside the AI's and go through the differences one at a time. `git diff` will line them up for you, using the same tool you learned in Lesson 1.1.

Every difference goes into one of four categories, and choosing the category is the analytical work.

1. **Structural error.** Illegal nesting, a bad attribute, a date in the wrong format. The schema found this one for you.
2. **Factual error.** A fabricated date, a scribal hand that does not exist, a wrong shelfmark. Only you can find this one.
3. **The AI was right and you were not.** It caught a detail you missed. This happens, it is not embarrassing, and recording it honestly is what makes the exercise research rather than a defence of your own work.
4. **Legitimate disagreement.** Both descriptions are defensible. A broader date range is not an error just because you chose a narrower one.

```
Discrepancy log — worked example:
  origDate     you "0550-0599"  | AI "0500-0600"      -> legitimate disagreement
  supportDesc  you "parchment"  | AI "parchment"      -> match
  handNote     you "h1, h2, h3" | AI "h1"             -> factual error: two hands missed
  decoNote     you none         | AI "marginal signs" -> AI was right; verify, then adopt
```

Keep the log as you go. It is the evidence for tonight's Comparison Post, and reconstructing it from memory afterwards does not work.

**Takeaway:** Every difference between your header and the AI's is a structural error, a factual error, a genuine AI catch, or a legitimate disagreement — and the sorting is the analysis.

---

## **25 Content**

**What It Costs**

The case for AI cataloguing is economic before it is intellectual, so the numbers deserve to be stated plainly (De Cristofaro & Zilio, 2025).

| | Manual (Tue) | Deterministic (Wed) | AI-assisted (Fri) |
| --- | --- | --- | --- |
| Time per manuscript | 8 to 15 hours | 1 to 2 hours | under a minute |
| Who has to do it | A trained specialist | A technical editor | Anyone, then a reviewer |
| Cost per record | Their salary | Nothing; the tools are free | A few cents |
| Across 10,000 manuscripts | Not fundable | Feasible if structured | Runs overnight |
| Structural error rate | Some typing errors | Zero; the schema forbids them | 5% to 20% before repair |
| Factual error rate | Very low | Very low | High; must be audited |

Read the last two rows together, because they carry the argument. AI removes the structural errors cheaply and multiplies the factual ones. The work does not disappear. It changes shape, from writing records to checking them (De Cristofaro & Zilio, 2025).

Whether that is a good trade depends on something the table cannot show: whether the checking actually happens. An audited pipeline is a genuine advance. The same pipeline unaudited is a fast way to fill a catalogue with confident fiction.

**Takeaway:** AI cuts cataloguing from hours to seconds and shifts the human effort from authoring to auditing, which is only an improvement if the auditing is real.

---

## **26 Content**

**Saying So in the File**

If a model drafted part of your description, the edition must say so. This is not a disclaimer. It is provenance, which you already accept as a scholarly obligation for manuscripts and which applies equally to your own work (De Cristofaro & Zilio, 2025; TEI Consortium, 2025).

The argument is straightforward. A future reader needs to know which claims came from an editor who examined the object and which came from a system that predicted plausible text. Those deserve different levels of trust, and the difference is invisible in the finished markup unless you record it.

TEI already has the elements, and you met both on Tuesday.

```xml
<titleStmt>
  <title>Diplomatic Edition of Codex Marchalianus (Vat. gr. 2125)</title>
  <respStmt>
    <resp>Codicological description and editorial audit</resp>
    <name xml:id="JD">Jane Doe</name>
  </respStmt>
  <respStmt>
    <resp>AI-assisted metadata extraction</resp>
    <orgName xml:id="AI_model">Claude 3.5 Sonnet (version 2024-10-22)</orgName>
  </respStmt>
</titleStmt>

<revisionDesc>
  <change when="2026-09-11" who="#AI_model">Initial automated draft of msDesc.</change>
  <change when="2026-09-11" who="#JD">Audited, corrected, and validated against msdesc.rng.</change>
</revisionDesc>
```

Record the model version too. "An AI wrote this" will mean very little in ten years; a version and a date can be checked.

**Takeaway:** Record AI contributions in `<respStmt>` and `<revisionDesc>` with model versions and dates, because algorithmic provenance is provenance.

---

## **27 Content**

**Making the Check Run Itself**

One last step turns all of this into something that holds up over a long project. The schema check can run automatically, every time anything changes.

You already know the pieces. Git records a commit; a service watches the repository; when a commit arrives, it runs the validator. If the file fails, the change is rejected and the editor is told. Nobody has to remember to check.

```yaml
# Runs on every commit: validate all TEI files against the schema
name: TEI Validation Gate
on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install the RELAX NG validator
        run: sudo apt-get install -y jing
      - name: Check every TEI file
        run: jing schemas/msdesc.rng src/**/*.xml
```

You do not need to write one of these for this course. You do need to see what it implies (Cummings, 2018).

The gate treats human and machine contributions identically. Neither an AI draft nor a tired editor at midnight can put an invalid file into the published edition, because the rule is enforced by the repository rather than by anyone's vigilance. That is the structural answer to a problem that discipline alone does not solve.

**Takeaway:** An automated validation gate on every commit enforces the schema on human and AI contributions alike, without relying on anyone remembering to check.

---

## **28 Content**

**Today's Lab: Your Passage, Your Comparison**

Now run the experiment on your own witness. Work through this in order.

1. **Gather your input.** Put your raw notes and description of the manuscript into a plain text file. Use what you had before you encoded anything — the object, not your header.
2. **Prompt the model.** Use the structure from section 04: state the role, name the permitted elements, demand XML only, keep the temperature low. Paste your notes at the end.
3. **Save the output untouched.** Call it `witness_ai.xml`. Do not tidy it. The unedited version is your evidence.
4. **Validate it and write down the number.** Add the same `xml-model` line you used on Wednesday, open the Problems panel, and record the error count **before fixing anything.** That number is your first result and it cannot be recovered later.
5. **Try one correction round.** Paste the errors back and ask for a repair, as in section 21. Record the new count.
6. **Score the six fields.** Repository, shelfmark, material, extent, number of hands, date. Mark each right, wrong or invented, or missing, against your own validated header.

Commit both files when you are done. If time runs short, steps 1 through 4 are the ones that matter — an unfixed AI file with its error count written down is a complete result on its own.

**Takeaway:** Generate a header for your own witness, record its error count before touching it, then score six fields against your validated file.

---

## **29 Content**

**Writing It Up**

Your Comparison Post is due tonight, and you now have everything it needs. It draws on all three days, so present them together.

| | Manual (Tue) | Deterministic (Wed) | AI-assisted (Fri) |
| --- | --- | --- | --- |
| Time taken | hours | under an hour | seconds |
| Schema errors, first check | not checked | your Wednesday count | your AI count today |
| Schema errors after correction | 0 | 0 | your second count |
| Fields right out of six | reference | reference | your score |
| Facts that had to be verified by hand | all | all | all |

Then four short sections.

- **What you did.** Your witness, the model you used, the prompt you gave it.
- **The numbers.** Error counts before and after correction, and your six-field score. Give the actual figures, not impressions.
- **What went wrong, specifically.** Name the errors. "It invented a shelfmark" is an argument; "the output had problems" is not.
- **What you would do next time.** Where in your own project would you let a model draft, and what would you refuse to let it touch? Base the answer on your numbers.

The last row of the table is the one to think hardest about. Every method required a human to check the facts. Nothing today changed that.

**Takeaway:** The report presents actual error counts and named failures across all three days, and concludes with a recommendation grounded in your own numbers.

---

## **30 Content**

**What the Week Was For**

Step back and look at what you built in three days.

- **Tuesday, by hand.** You wrote a TEI header yourself and found out how much a manuscript demands before it can be described at all (TEI Consortium, 2025).
- **Wednesday, by rule.** You handed your file to a schema and let it find what you could not see in your own work (Cummings, 2018; Blackwell & Smith, 2019).
- **Friday, by machine.** You had a model do the same job in seconds, and then you measured it, which is a thing you could only do because of Tuesday and Wednesday (De Cristofaro & Zilio, 2025; Ignatowicz et al., 2025).

```
Topic 02, complete:
  Tue  manual        hand-authored TEI header          -> your ground truth
  Wed  deterministic schema validation to 0 errors     -> your structural baseline
  Fri  AI-assisted   generated header, scored          -> measured against both
```

Here is the conclusion the week has been building toward, and it is not the one people expect. AI does not make schemas less important. It makes them essential.

When markup was slow and expensive, structural mistakes were rare because so little got produced. A system that generates plausible TEI in seconds can produce wrong markup faster than any human can read it. The formal schema is what stands between that output and the published record — together with an editor who knows the difference between a valid file and a true one.

That editor is what this course is training you to be. The machine got faster this week. The judgement did not become less necessary; it became the only part that was ever scarce.

**Takeaway:** Generative AI makes deterministic schemas and human editorial judgement more necessary, not less, because it can produce plausible errors faster than anyone can read them.

---

## References

Blackwell, C., & Smith, N. (2019). The CITE Architecture: A conceptual and practical overview. In M. Berti (Ed.), *Digital Classical Philology: Ancient Greek and Latin in the Digital Revolution* (pp. 73–94). De Gruyter Saur.

Cummings, J. (2018). The Text Encoding Initiative and the study of literature. In R. Siemens & S. Schreibman (Eds.), *A Companion to Digital Literary Studies* (pp. 451–476). Blackwell.

De Cristofaro, M., & Zilio, D. (2025). Automating XML-TEI encoding of unpublished correspondence: A comparative analysis of two LLM approaches. *AIUCD 2025 Proceedings: Diversity, Equity, and Inclusion: Challenges and Opportunities for Digital Humanities in the Age of Artificial Intelligence*.

Ignatowicz, J., Kutt, K., & Nalepa, G. J. (2025). Metadata Enrichment Model: Integrating neural networks and semantic knowledge graphs for cultural heritage applications. *arXiv preprint*. https://arxiv.org/abs/2505.23543

Koho, M., Burrows, T., Hyvönen, E., Ikkala, E., Page, K., Ransom, L., ... & Wijsman, H. (2021). Harmonizing and publishing heterogeneous premodern manuscript metadata as Linked Open Data. *Journal of the Association for Information Science and Technology*, 73(2), 240–257. https://doi.org/10.1002/asi.24499

Koho, M., Coladangelo, L. P., Ransom, L., & Emery, D. (2023). Wikibase model for premodern manuscript metadata harmonization, linked data integration, and discovery. *ACM Journal on Computing and Cultural Heritage*, 16(3), Article 56. https://doi.org/10.1145/3594723

Le Bœuf, P. (2012). Modeling rare and unique documents: Using FRBRoo/CIDOC CRM. *Journal of Archival Organization*, 10(2), 96–106.

TEI Consortium. (2025). *TEI P5: Guidelines for Electronic Text Encoding and Interchange*. Version 4.8.0. https://tei-c.org/release/doc/tei-p5-doc/en/html/

Tiepmar, J., & Heyer, G. (2014). A new implementation for Canonical Text Services. In *Proceedings of the Workshop on Human-Computer Tractable Data for the Digital Humanities* (pp. 1–8).
