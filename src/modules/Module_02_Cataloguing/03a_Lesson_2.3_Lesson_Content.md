# Lesson 2.3 — Auditing AI-Generated Manuscript Metadata

*RELS 398 / ENGL 398 · Topic 2: Cataloguing · Meeting #5 (Fri Sep 11)*

***Step 3 of the three-step cycle: AI-assisted.** On Tuesday you wrote a TEI header by hand. On Wednesday you made a schema check it. Today a machine writes the same header in seconds, and your job is to find what is wrong with it — including the errors that pass every check you own.*

---

## **01 Content**

**What Today Actually Asks of You**

By Monday you owe a workshop submission with three parts: a validated `<msDesc>` for your own witness, authority identifiers that resolve to the right records, and a 300 to 500 word comparison in which you name **at least two subtle hallucinations** in an AI-generated version of the same description.

Read that requirement carefully, because the difficulty is hiding in one word. Not two errors. Two *subtle* errors.

Obvious errors are easy. If a model closes a tag in the wrong place, Wednesday's schema tells you on the spot, and reporting it earns you very little. A subtle error is one that survives every automatic check you have: well-formed XML, valid against `msdesc.rng`, correctly formatted dates, plausible content — and wrong.

So today is not an introduction to AI. You already know from Lesson 1.1 that these systems predict text and invent things. Today is training in a specific skill: looking at a clean, confident, schema-valid TEI header and finding the places where it is lying to you.

That skill is the whole of this lesson, and most of what the module is assessing.

**Takeaway:** The workshop asks you to name at least two subtle hallucinations, meaning errors that pass validation, so today trains you to audit a header that already looks perfect.

---

## **02 Content**

**What the Model Is Doing When It Writes Your Header**

Lesson 1.1 told you that a large language model predicts likely text. It is worth being exact about what that means when the text is TEI.

The model has read enormous amounts of writing, including a great deal of public TEI. It has seen thousands of real `<teiHeader>` elements. So when you hand it a catalogue description, it is not consulting the TEI Guidelines. It is answering one question repeatedly: given everything so far, what usually comes next?

After `<msIdentifier>`, a `<repository>` usually comes next. After a description mentioning animal skin, `material="parchment"` usually comes next. The model is very good at "usually."

Two consequences follow, and they explain nearly everything in this lesson.

First, its output looks right immediately, because it has seen so much TEI that looks right. Second, it has no copy of `msdesc.rng` in its head and no way to check itself against one. It has a strong sense of what TEI tends to look like and no knowledge of what your schema actually permits.

There is a third consequence, and it is the one that matters most for the audit. The model produces the *usual* answer even where your manuscript is unusual — and manuscripts are nothing but unusual.

**Takeaway:** A model writes TEI by predicting what usually comes next, which makes it fluent, unable to check itself, and systematically wrong about whatever is distinctive in your witness.

---

## **03 Content**

**Two Ways of Being Right**

Wednesday and Friday put two very different tools side by side, and they disagree about what "correct" means.

The schema is deterministic. Give it the same file twice and you get the same answer twice. It holds a fixed list of what may appear, in what order, inside what parent. It does not care what your manuscript means. It has one question: does this tree obey the rules?

The model is probabilistic. Give it the same prompt twice and you may get two different headers. It has no fixed rules at all. What it has is a sense of meaning: it can tell that a phrase about a leaf's height belongs near the physical description, even though nobody told it so.

| What you need done | The schema (Wednesday) | The model (Friday) |
| --- | --- | --- |
| Enforce element order and nesting | Reliable; this is its whole job | Approximate; obeys when it happens to |
| Read messy prose and find the meaning | Cannot do this at all | Genuinely good at it |
| Give the same answer every time | Always | Not guaranteed |
| Notice that a date is not really a date | Checks the format, not the fact | Will invent a plausible one |

Neither is the smarter tool. They fail in opposite directions, which is why they belong together: the model proposes, and the schema refuses.

**Takeaway:** Schemas are consistent but indifferent to meaning, models grasp meaning but guarantee nothing, so each covers the other's blind spot.

---

## **04 Content**

**What a Schema Can and Cannot See**

This is the most important idea in the lesson, and everything from section 15 onward depends on it. Take a moment with it.

On Wednesday you drove the Problems panel to zero errors and it felt like proof. It was proof of something quite narrow. A RELAX NG schema answers one question: is this tree built out of permitted elements, in a permitted order, with permitted attribute values?

Notice what is missing from that question. Nothing in it concerns your manuscript.

| The schema checks | The schema cannot check |
| --- | --- |
| Is `msIdentifier` inside `msDesc`? | Is this the right shelfmark? |
| Is `@when` formatted as a date? | Is it the right date? |
| Is `@material` in the permitted list? | Is the leaf actually parchment? |
| Did you close every element? | Did you describe the correct manuscript? |

Every entry in the right column is a fact about a physical object, and a schema has never seen a physical object. It sees a tree.

So "zero errors" means the file is *well built*. It says nothing about whether the file is *true*. A completely fabricated description of a manuscript that does not exist can pass at zero errors, and later in this lesson you will watch one do exactly that.

Hold on to the distinction. Once a machine is generating the markup, the gap between well built and true is where all your work lives.

**Takeaway:** A schema certifies that a file is well built, never that it is true, and every fact about the physical manuscript falls outside what it can see.

---

## **05 Content**

**Why Your Own Header Is the Measuring Stick**

A system cannot grade itself. To say anything precise about an AI header, you need an independent reference — and you built one this week without being told that was the point.

Tuesday's hand-authored header is your ground truth: made by someone who looked at the actual object. Wednesday's validated file is your structural baseline: certified at zero errors. Together they are the standard the machine gets measured against.

This matters more than it sounds. Without a baseline, all you can say about an AI header is that it looks impressive — worth nothing, because looking impressive is the one thing these systems are guaranteed to do. With a baseline you can say something a marker can check: it invented a shelfmark, it missed two hands, it got the material right.

Your workshop grade turns on this. "The AI made some mistakes" is not an audit. "The AI gave the treaty the reference number of a different volume in the same series, and that number resolves to a document signed three years later" is an audit. The second sentence is only available to someone holding a verified reference.

Keep your Tuesday file open beside the AI output all through today's lab. The comparison is not a step at the end. It is the work.

**Takeaway:** Your verified header is what converts an impression of the AI's cleverness into a specific, checkable claim about what it got wrong.

---

## **06 Content**

**Finding the Information: Where Your Facts Come From**

An AI header can only be as good as the facts you feed it, and you cannot check its output against facts you never established yourself. So before you generate anything, you need a verified dossier on your own document.

**In practice, four things have to be pinned down:**

| What you need | Where it comes from |
| :--- | :--- |
| **Identity of the object** | Holding institution + reference number or call number, copied exactly as the institution writes it |
| **What it physically is** | The catalogue record: support and material, dimensions, extent, script or type, condition, seals or watermarks |
| **Who and where** | Authority records for the responsible person/institution and the place of origin or issue |
| **What it contains** | The work or text it carries, and its status — original, contemporary copy, later transcript, or printed edition |

**Two rules carry most of the weight.**

**First: the register depends on the tradition.** Authority control has a general layer — VIAF, Wikidata, Library of Congress, Getty — that works for almost any document. It also has a tradition-specific layer that does not transfer. Two of you are working on documents whose registers are named for other traditions' materials (Greek literary texts), and those will not describe your objects. Finding *which* register governs your document is part of the work, and saying "I checked this register and it has no record for my object" is a legitimate finding, provided you show the search.

**Second: verify by reading the record, not by checking the link.** Some registers return a page even for identifiers that do not exist. A link that loads proves nothing. Open the record, read the fields, and compare them against an independent source.

**Takeaway:** Build a verified dossier — object identity, physical description, responsible agents and places, and textual content — before generating anything, because you cannot audit the machine against facts you never established.

---

## **07 Content**

**Recording What You Found in the Header**

Now the facts become markup. Wednesday taught you the elements; today the question is which element carries which kind of fact, and how to be honest about uncertainty.

Here is a worked header for a printed proclamation, with the identifications that matter marked:

```xml
<msIdentifier>
    <settlement ref="https://www.wikidata.org/wiki/Q3350">Antigonish</settlement>
    <repository ref="http://viaf.org/viaf/...">Nova Scotia Archives</repository>
    <idno type="reference">RG 1 volume 430 number 2</idno>
</msIdentifier>
<physDesc>
    <objectDesc form="broadside">
        <supportDesc material="chart">
            <support><p>Single printed sheet.</p></support>
            <extent>1 sheet.</extent>
        </supportDesc>
    </objectDesc>
</physDesc>
<note type="status">Printed proclamation issued at signing; no original signed copy is known to survive.</note>
```

**Four decisions to notice, because each is one a model gets wrong:**

1. **`<idno>` carries a `type`.** A reference number, an ARK, and a call number are different kinds of identifier. Untyped, a reader cannot tell which they are looking at.
2. **`ref` goes on the element it identifies**, and holds an authority URI — not on the header as a whole.
3. **The form attribute describes what the object is.** `broadside` is not `codex`. Choosing the wrong one asserts something false about the physical object, and no schema will stop you.
4. **Status goes in a `<note>`.** The reference number does not tell you whether you hold an original, a copy, or a print. If that is unrecorded, a reader will assume original — which is precisely the error to avoid.

**On uncertainty.** Some dates are editorial attributions rather than statements by the document; some registries have no record for an object; some objects have no surviving original. When a fact is uncertain, say so in the header rather than rounding it to a confident value. Recording uncertainty accurately is scholarship. Flattening it is the failure this whole lesson exists to catch.

**Takeaway:** Put each fact in the element whose meaning actually fits it — typed `<idno>`, `ref` on the identified element, an accurate `@form`, status in a `<note>` — and record uncertainty rather than concealing it.

---

## **08 Content**

**Choosing the Right Element for the Right Fact**

The hardest part of writing a header is not syntax. It is deciding which element carries a given fact — and getting it wrong asserts something false without any tool complaining.

**Work through the decisions your own document forces:**

| Fact about your object | Element | The trap |
| :--- | :--- | :--- |
| Who holds it | `<repository>` | Putting a person here instead of an institution |
| Where it was made or issued | `<origPlace>` | Confusing place of origin with place of current holding |
| What it is physically | `<objectDesc @form>` | `codex` for something that is not a codex |
| What it is made of | `<supportDesc @material>` | Copying a term the schema does not enumerate |
| How much of it there is | `<extent>` | Counting leaves when you mean sheets, or vice versa |
| Who wrote or printed it | `<handNote>` / `<typeDesc>` | Asserting scribal hands on a printed document |
| When | `<origin><date>` | Stating an editorial attribution as if the document said it |

**Three of these traps are specific to documents outside the codex tradition**, which is where all three of you are working:

- A **printed broadside** has no quires and no scribal hand. Describe the type and the impression, not hands.
- A **single-sheet document** is not measured in folios. Use the extent vocabulary that fits.
- A **document with no surviving original** cannot be described as an original. Its status is a fact about it, and it belongs in the record.

**When nothing fits, say so in a note rather than forcing an element.** A `<note>` explaining that the standard category does not apply is better scholarship than an empty element that implies it does.

**Takeaway:** Choose the element whose meaning actually matches your object, use the categories that honestly apply, and record the misfit in a note rather than forcing a category that asserts something untrue.

---

## **09 Content**

**What Your Dossier Must Cover Before You Generate**

You cannot audit what you did not establish. Here is the checklist, and you should be able to point to a source for every line.

**About the object:**

- Holding institution, with its authority URI if one exists
- Reference number, call number, or ARK — copied exactly, with brackets and punctuation intact
- Status: original, contemporary copy, later transcript, or printed edition

**About its physical form:**

- Support and material, in the schema's vocabulary
- Extent, in the right unit for the object
- Script and hand, or type and impression
- Condition, damage, and any seals or watermarks
- Dimensions, if the catalogue records them

**About its content and people:**

- The work or text it carries
- The person or body responsible, with an authority URI
- The place of origin or issue, with an authority URI
- The date, marked as authorial or editorial

**The test of a good dossier:** every field is something you could show someone else, and every field you could not verify is marked as unverified rather than omitted. An omission you know about is safe. An omission you have forgotten about is where the machine's invention will go unnoticed.

**Takeaway:** Assemble a sourced dossier covering object, physical form, content, agents, places, and date before generating — marking what you could not verify, because unmarked gaps are where fabrication hides.

---

## **10 Content**

**Working With a Model That Cannot See Your Document**

A language model has never handled a manuscript. It has read descriptions of them. That single fact predicts where it will succeed and where it will fail, and it is worth stating plainly before you start.

**Where it will do well:** prose that sounds like a catalogue record. Recurring structures. Standard formulas and boilerplate. Anything well represented in the writing it has read.

**Where it will fail:** anything requiring the physical object — the number of hands, the exact dimensions, the condition of a leaf, the reading of a damaged word. Anything requiring a register it cannot query — a shelfmark, a cote, an ARK, a treaty reference number. Anything where your document is unusual, because unusual things are rare in its training data.

**Notice that the failures cluster.** They are not randomly distributed. The model will be confident precisely where it cannot be right, because confidence is a property of its prose rather than of its knowledge.

This is also why a low schema error count tells you almost nothing. Structural markup is the part it has read most about. The part it cannot do is the part a schema cannot check.

**Takeaway:** A model's knowledge comes from descriptions rather than objects, so its failures cluster on facts requiring physical access or a queryable register — which is exactly the ground your dossier covers.

---

## **11 Content**

**Asking the Model for a Header**

Now you generate the machine's version.

**Give it your raw material and ask for a header.** The prompt below is deliberately plain. Note what it does and does not do.

```text
Generate a TEI P5 teiHeader for the document described below,
valid against the msdesc RELAX NG schema.
Include msIdentifier, physDesc with material and extent, and handDesc
or typeDesc as appropriate. Output only XML.

Description: [paste your own catalogue notes here]
```

**What the prompt does:** it names the schema, names the elements, and supplies real source material.

**What it deliberately leaves out:** the correct answers. Do not paste your finished header in and ask the model to reproduce it — that measures nothing. Do not tell it the shelfmark is right or wrong. The point is to see what it does with the same raw material you had.

**Four failure modes to watch for, all of them common:**

- **Invented elements.** Tags that no schema permits, because they sound plausible. These the validator catches.
- **Confident invented specifics.** A shelfmark, hand count, or date the model could not possibly know from your description. These validate cleanly and are the real danger.
- **Wrong structural form.** Describing a printed broadside as a codex, or supplying quires for a document that has none.
- **Silent omission.** Fields your dossier establishes that the model simply leaves out.

**Save the output unchanged** as a separate file — for example `witness_ai.xml`. Do not fix it before you have counted what is wrong with it.

**Takeaway:** Prompt with real source material and the schema, withhold the answers, and save the model's output unedited so the comparison measures the machine rather than your corrections.

---

## **12 Content**

**Holding Both to the Same Gate**

Both headers now go through the same validator. That symmetry is what makes the comparison an experiment.

**Run the schema against the AI output first, before fixing anything, and write down the raw error count.** That number is a datum. An error count of zero is a perfectly interesting result — it means the model produced well-built markup, which is the one thing it is reliably good at, and it tells you the audit has to happen somewhere other than the Problems panel.

Then work the errors the way you did on Wednesday: one at a time, re-saving and watching the count fall.

**Two traps in this step:**

- **A low error count is not a good header.** A tiny, vague header can validate perfectly while omitting most of what your dossier establishes. Validity measures construction, not completeness.
- **Do not let the model fix its own errors without recording the original count.** If you hand the errors back and paste the corrected version, you have measured the model *plus* your supervision and lost the baseline. Record first, repair second.

**Takeaway:** Validate the AI header unedited and record its raw error count before any repair, because that first number is the measurement and everything after it is remediation.

---

## **13 Content**

**The Audit: Comparing Content, Not Just Structure**

Now the part the workshop actually grades.

Go field by field through your dossier and mark what the machine produced:

| Field | Mark it |
| :--- | :--- |
| Repository / holding institution | correct / wrong / invented / missing |
| Reference number or call number | correct / wrong / invented / missing |
| Material and support | correct / wrong / invented / missing |
| Extent (folios, sheets, volumes) | correct / wrong / invented / missing |
| Number of hands, or type and impression | correct / wrong / invented / missing |
| Date | correct / wrong / invented / missing |

**"Invented" is the category that matters most.** A shelfmark that is well-formed, correctly formatted, and simply false counts as invented — and it will have passed the schema. So will a reference number that belongs to a different volume, or a repository URI that resolves to a different institution. Make sure you can point to the specific thing that is false, not merely that something feels off.

**Record two numbers:** the raw schema error count from section 09, and how many of the six fields were wrong or invented.

**Then ask the question the numbers raise.** Where did the machine beat you? Where did it lie to you? The failures tend to cluster on facts requiring access to the physical object or to a trustworthy register — the things a language model has no way to consult and every incentive to produce fluently anyway.

**Takeaway:** Audit the machine field by field against your verified dossier, count both the schema errors and the wrong-or-invented fields, and be able to name the specific falsehood rather than a general impression of error.

---

## **14 Content**

**Four Kinds of Wrong**

You are now at the centre of the lesson. Everything so far was preparation for a single question: when an AI header is wrong, in what way is it wrong?

Sorting errors into these four kinds is the skill the workshop grades, because the categories differ in who can catch them.

| Kind of error | Example | What catches it |
| --- | --- | --- |
| Structural | `<p>` inside `<closer>` | The schema, instantly |
| Factual, obvious | Says paper; your image plainly shows parchment | You, in seconds, from the image |
| Factual, subtle | A complete provenance narrative, invented | Only a specialist who knows the manuscript |
| Authority and citation | A well-formed identifier pointing at the wrong record | Only someone who follows the link |

Read the third column downward. It is a description of how much of you each error requires.

The top row is free. The second is cheap. The bottom two are the reason a human editor still holds this job, and they are where your two subtle hallucinations will come from. A submission reporting two structural errors has reported the two things the machine already told you.

Sections 16 through 22 work through the four kinds in order, spending most of their time on the bottom half.

**Takeaway:** AI errors are structural, obviously factual, subtly factual, or citational, and the categories differ by who is capable of catching them.

---

## **15 Content**

**Structural Errors: The Ones the Schema Hands You**

Start with the easy kind, so you can stop spending attention on it.

A structural hallucination is markup that looks reasonable and is illegal in this schema. The model is not confused about your manuscript. It is confused about rules it never had (De Cristofaro & Zilio, 2025).

Three patterns recur.

- **Closing a container too early.** It writes `</profileDesc>` and keeps going with elements that belonged inside, leaving them orphaned.
- **Reaching for HTML.** Models have read far more HTML than TEI, so under pressure they reach for `<p>` or `<br>` where TEI allows neither. You watched this exact trap on Wednesday, when `<extent>` refused a `<p>` that `<support>` accepts one line above.
- **Inventing character entities.** `&copy;` and `&nbsp;` are ordinary in HTML and undefined in XML. One of them anywhere is fatal: the parser stops and you get no report at all.

| What the model wrote | Why the schema refuses it |
| --- | --- |
| `</profileDesc><langUsage>...</langUsage>` | `langUsage` belongs inside `profileDesc` |
| `<closer><p>Yours faithfully,</p></closer>` | `closer` takes phrases, not paragraphs |
| `<p>Copyright &copy; 2026</p>` | `copy` is an HTML entity; XML has never heard of it |
| `<supportDesc support="parchment">` | The attribute is `material`, not `support` |

Count these, report the number, and move on. They are the cheapest finding in your audit, and everyone else will report them too.

**Takeaway:** Structural hallucinations are plausible, illegal markup that the schema catches instantly, which makes them the least valuable finding in your audit.

---

## **16 Content**

**Obvious Factual Errors: Check These First**

Now errors the schema cannot see but you can, quickly, by looking at your own file and your image.

Five fields carry most of them.

- **Support.** The model says paper; your image plainly shows parchment. It guessed from a period, or from nothing.
- **Extent.** A folio count that does not match what you counted.
- **Hands.** A single hand asserted where you recorded three.
- **Date.** A century that contradicts your own dating.
- **Repository.** The wrong library, sometimes a famous one substituted for an obscure one.

That last pattern is worth naming, because it is systematic rather than random. Asked about an unfamiliar document, a model drifts toward the famous: the Bibliothèque nationale rather than a departmental archive, a celebrated author rather than an anonymous clerk. Its training data contains far more text about famous things, so "what usually comes next" is biased toward them.

This gives you a place to look first. **Check the parts of your description that are unusual.** A witness that is ordinary in every respect will be described well. Whatever makes yours distinctive is exactly where the model will have replaced your manuscript with the average one.

**Takeaway:** Obvious factual errors cluster in support, extent, hands, date, and repository, and models drift toward the famous, so check whatever is distinctive about your witness first.

---

## **17 Content**

**The Subtle One: The Provenance That Never Happened**

Here is the failure that gives this lesson its shape. Read it slowly.

You give a model a thin description: *Halifax, 1752: printed proclamation in English and French, single sheet, damaged along one fold, issued by the governor.* You ask for a full `<history>`. It returns this.

```xml
<!-- Generated by a model. Every fact in it is invented. -->
<provenance notBefore="0700" notAfter="0750">
  <p>Transferred in 722 CE to the Monastery of Saint Catherine at Mount Sinai
     and entered in the Council register for that year.</p>
</provenance>
```

Now audit it with everything you own. The XML is well-formed. The elements are real TEI. The dates are correct ISO 8601 and consistent with each other. Run it through Wednesday's schema and it reports zero errors.

Mount Sinai is invented. Dorotheus is invented. The year 722 is invented. The inventory is invented. The model assembled a plausible provenance from general knowledge of how manuscripts moved, and produced fiction in perfect TEI.

Notice what makes it convincing: it is *specific*. Vague output reads as uncertain, and specific output reads as researched. The model has no way to be vague — it produces the most probable continuation, and a probable provenance narrative contains names and dates.

**Specificity is not evidence.** In AI output, it is the opposite: an unexpectedly precise claim about a poorly documented object is the thing to distrust first.

**Takeaway:** A model produces fabricated provenance in flawless TEI that passes the schema at zero errors, and its specificity is a warning sign rather than a mark of research.

---

## **18 Content**

**The Subtle One: Confidence the Source Never Had**

This one is quieter than section 18, and better suited to your workshop, because you can demonstrate it from your own source.

Your evidence is uncertain in ordinary, honest ways. A script is *probably* sixth century. A hand *may* be a later corrector. Damage makes a line count *approximate*. On Tuesday you had to decide how to encode that uncertainty, and TEI has vocabulary for it: `@notBefore` and `@notAfter` for a range, `<certainty>`, a plain "possibly" in a note.

A model tends to erase all of it.

| Your source says | The model writes | What has happened |
| --- | --- | --- |
| "ca. 550" | `when="0550"` | A range became a single year |
| "uncial, possibly two hands" | Two `handNote` elements, no qualification | A maybe became a count |
| "approximately 29 lines" | `writtenLines="29"` | An estimate became a measurement |
| "provenance Egypt" | `<origPlace>Alexandria</origPlace>` | A region became a city |

Every row validates. Every row is more confident than the evidence supports.

This matters beyond tidiness. Someone downstream will query these fields as data — Module 07 will collate on them — and a false precision is worse than a recorded uncertainty, because it cannot be seen and cannot be undone.

This is an excellent candidate for one of your two subtle hallucinations. It is easy to demonstrate: put your source description and the AI output side by side and point to a hedge that vanished.

**Takeaway:** Models convert hedged evidence into precise assertions — ranges into years, maybes into counts — producing valid markup that claims more than the source ever did.

---

## **19 Content**

**The Subtle One: What Is Not There**

Every error so far was something written down. This one is the absence of something, and it is the hardest kind to see.

The behaviour was documented at scale. In the PubCINET study, one model produced near-flawless valid TEI and, when a document mentioned a person outside the supplied reference list, simply left them untagged rather than work out who they were (De Cristofaro & Zilio, 2025). The markup was perfect and the record was incomplete.

Think about how invisible that is. A missing hand produces no error. A missing `<msItem>` produces no error. The file is green, the structure is clean, and nothing anywhere signals that something is absent. **A schema can only judge what you gave it.** It has no view of what should have been there.

This is why comparison, not inspection, is the method. Reading the AI file on its own, you will never find an omission — there is nothing to see. Reading it beside your own header, an omission is obvious immediately, because your file has an element theirs does not.

So work through your own header element by element and ask of each: is this present in the AI version? That is a mechanical procedure, it takes a few minutes, and it will find things no validator can.

**Takeaway:** Omissions produce no error and cannot be found by reading the AI file alone, so audit by walking your own header element by element.

---

## **20 Content**

**The Subtle One: The Link That Goes Somewhere Else**

Section 12 warned that models fabricate identifiers. Now look at what that produces in a finished file, because it is a strong candidate for your second subtle hallucination.

A fabricated identifier fails in three different ways, and only one is easy to spot.

- **It resolves to nothing.** The URL is dead. Annoying, but honest: anyone who clicks discovers the problem.
- **It is correctly formatted and wrong.** The number belongs to a real record for a different manuscript. Nothing looks broken. A reader who trusts it now believes something false about your witness.
- **It is nearly right.** An ARK one character off, landing on a real but different item; a VIAF number for the right institution but the wrong branch.

The second and third are what to hunt for. They pass every check in your toolchain: valid XML, valid schema, resolvable URL, plausible record. The only test is to follow the link and read what is on the other end.

That is your method, and it takes about a minute per identifier. **Click every one.** If the record that opens is not your manuscript, your work, or your library, you have found a subtle hallucination worth writing up — one your marker can verify by clicking too.

**Takeaway:** Fabricated identifiers most often resolve to a real but wrong record, passing every automatic check, so the only test is following each link and reading what opens.

---

## **21 Content**

**The Subtle One: The Citation That Does Not Resolve**

On Wednesday you recorded a persistent identifier for your object — an ARK, a call number, or an archival reference. Each has a strict internal syntax, and every part must be right.

Ask a model for one and it will produce the right shape. Shape is never the problem. Three things go wrong inside it.

- **Right shape, wrong authority.** A plausible-looking ARK whose NAAN belongs to a different institution, or a call number in a series that does not exist.
- **Wrong work numbers.** The model half-remembers a TLG number and assigns Homer's identifier to Isaiah. The URN is perfectly formed and points at the wrong text.
- **An identifier that resolves to something else.** The syntax is correct and the link works — but it opens a different document, which is worse than a dead link because it looks like verification.

Each produces a citation that looks correct in your file and fails when somebody tries to follow it. Since the entire purpose of a canonical URN is to still resolve in fifty years, a fabricated one is worse than none: a broken promise that looks like a kept one.

The rule from section 06 applies unchanged. Do not accept an identifier from a model. Resolve it against the real service before it enters your file.

**Takeaway:** Generated identifiers are correctly shaped and frequently point at the wrong object, so every one must be resolved and read before you commit it.

---

## **22 Content**

**Sorting the Differences, and What the Pattern Shows**

You now have two headers and two numbers. Put them side by side — `git diff` will line them up, using the tool from Lesson 1.1 — and classify every difference. Choosing the category *is* the analysis, and there are four:

1. **Structural error.** The schema found it for you. Cheap to fix, and the least interesting result.
2. **Factual error.** A fabricated date, a hand count that does not match the object, a shelfmark belonging to a different volume. Only you can find these.
3. **The machine was right and you were not.** It caught something you missed. Say so — an audit that never credits the model is not an audit.
4. **Legitimate disagreement.** Both descriptions are defensible, usually because your sources differ or an attribution is genuinely contested. Name the disagreement rather than resolving it by fiat.

**Two standard measures sharpen the write-up.** *Precision* asks: of everything the AI claimed, how much was right? *Recall* asks: of everything your dossier establishes, how much did it find? Low precision means it invents; low recall means it omits. You do not need to compute them formally — the scorecard's counts already give you both, and naming them correctly makes your comparison precise.

**Then state the pattern, because the pattern is the finding.** The errors will not be randomly distributed. Structural errors cluster where the schema could reach them. Invented specifics cluster on exactly the facts that require access to the physical object or a trustworthy register: shelfmarks, hand counts, exact dimensions, dates. Coverage will be better for well-documented, heavily catalogued material and worse for anything scarce — which means the model's reliability is unevenly distributed across the very documents scholarship has neglected.

That last point is worth one sentence in your comparison, and it is a scholarly observation rather than a technical one. Do not let it grow into an essay: the workshop grades your audit, not your position on the ethics of machine cataloguing.

**Takeaway:** Classify every difference, name precision and recall from your own counts, and state the pattern — structural errors where the schema could reach, invented specifics where only the object could answer.

---

## **23 Content**

**From Counts to a Defensible Claim**

You have two numbers: the raw schema error count, and how many of the six fields were wrong or invented. Neither is a finding on its own. A finding is a claim the numbers support.

**Weak:** "The AI made several errors." Unfalsifiable, and it describes every AI output ever produced.

**Strong:** "The AI produced valid markup at zero errors, but invented the reference number and gave the wrong extent; both errors passed validation, and both concern facts that only the object could supply."

The second sentence does three things the first does not. It separates structural from factual performance. It names the specific falsehoods. And it draws a conclusion about *why* those particular fields failed — which is the analysis your comparison is graded on.

**Test your own sentence against three questions:**

1. Could a marker check it against your files? If not, it is an impression.
2. Does it name the specific field and the specific error? If not, it is too general.
3. Does it say something about the machine rather than about your own effort? If not, it is a diary entry.

**One more thing worth doing:** note where the model was *right* and you had been wrong. Audits that only catalogue failures are incomplete, and finding a case where the machine corrected you is a genuinely interesting result.

**Takeaway:** Convert your counts into a specific, checkable claim that separates structural from factual performance and explains why those fields in particular failed.

---

## **24 Content**

**Recording the Machine's Part in the File**

If a model drafted part of your description, the edition must say so. This is not a disclaimer. It is provenance — which you already accept as an obligation for manuscripts, and which applies just as much to your own work.

The argument is simple. A future reader needs to know which claims came from an editor who examined the object and which from a system predicting plausible text. Those deserve different trust, and the difference is invisible in finished markup unless recorded.

TEI has the elements, and you met both on Tuesday.

```xml
<titleStmt>
  <title>Diplomatic Edition of the 1752 Peace and Friendship Treaty</title>
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

Record the model version. "An AI wrote this" will mean little in ten years; a version and a date can be checked.

This also protects you. A documented AI draft that you audited is methodologically respectable. An undocumented one that a reader later detects is not.

**Takeaway:** Record AI contributions in `respStmt` and `revisionDesc` with model versions and dates, because algorithmic provenance is provenance.

---

## **25 Content**

**Friday's Lab, Step by Step**

Now run the experiment on your own witness.

1. **Look up your identifiers first.** The registers that govern your own document, from section 06. Do this before any prompting, so you hold verified values the model cannot influence.
2. **Gather your input.** Put your raw notes and catalogue description into a plain text file — the object as you found it, not your finished header.
3. **Prompt the model** using section 08. Save the prompt itself; you will quote it.
4. **Save the output untouched** as `witness_ai.xml`. Do not tidy it. The unedited version is your evidence.
5. **Validate and record the count** before fixing anything. This is section 13, and it is the step most often lost to enthusiasm.
6. **Run one correction round** as in section 14, and record the new count.
7. **Score the six fields** from section 24 against your validated header.
8. **Click every identifier** the model produced. This is where your subtle hallucinations are most likely to be, and it takes about a minute each.

Commit both files when you are done.

If time runs short, steps 1, 4, 5, and 8 are the ones that matter. An unfixed AI file, its first error count, and one identifier proven wrong is a complete finding.

**Takeaway:** Verify identifiers before prompting, record the untouched output and its first error count, then score six fields and follow every link the model produced.

---

## **26 Content**

**Writing the Comparison**

Your comparison is 300 to 500 words and carries three of the ten workshop points. The rubric asks it to *precisely diagnose model hallucinations* and *explain the methodological necessity of deterministic validation*. Both halves are graded, and the second is the one people forget.

A structure that fits the word count.

- **Method, about 60 words.** Your witness, the model, the prompt, the schema. Enough that someone could repeat it.
- **Numbers, about 60 words.** First-pass error count, count after correction, six-field score. Actual figures.
- **Your two subtle hallucinations, about 250 words.** This is the substance. For each: quote the AI's markup, state what is actually true and how you verified it, and name why it survived validation.
- **Why the schema is necessary anyway, about 80 words.** Answer the second half of the rubric.

That last part deserves care, because the obvious answer is wrong. Your own evidence shows the schema catching structural errors and missing every subtle one you reported. So why keep it?

Because it removes an entire class of failure at zero cost, leaving your attention free for the errors only you can catch. A validator that eliminates the cheap errors is what makes it possible to spend your limited attention on the expensive ones. Argue it from your own numbers rather than from conviction.

**Takeaway:** The comparison reports method and figures briefly, spends its length on two verified subtle hallucinations, and argues the schema's necessity from your own numbers.

---

## **27 Content**

**Where This Method Transfers**

The audit you are learning is not specific to TEI headers, and it is worth naming what it actually is, because it is the most durable thing in this module.

**The pattern is: establish ground truth independently, generate with a machine, compare against the ground truth rather than against plausibility, and classify the differences by kind.**

That sequence works anywhere a language model produces structured output that must correspond to something real:

- Extracting metadata from a digitised collection at scale — where no human can check every record, so you sample and audit.
- Converting legacy finding aids into structured data — where the model's fluency makes errors hard to spot.
- Generating catalogue records for uncatalogued material — the case where its confident inventions are most dangerous, because no existing record contradicts them.
- Any downstream pipeline where a wrong identifier silently attaches to the wrong object.

**What does not transfer is the shortcut.** There is no version of this where you accept the output because it looks right, and there is no version where the schema checking it is sufficient. The schema checks construction. You check truth. That division of labour is the lesson.

**Takeaway:** The method — independent ground truth, generation, comparison against truth rather than plausibility, classification of differences — transfers to any structured output a model produces about real objects.

---

## **28 Content**

**The Three-Step Cycle, Completed**

Step back and look at what the three meetings of this cycle built.

**Tuesday — the manual baseline.** You read a document and wrote a header by hand. Slow, and the only step where a human looked at the object and decided what was true.

**Wednesday — the deterministic gate.** You linked a schema and drove the errors to zero. This did not make your header true; it made it well built, and it gave you a machine-checkable standard.

**Friday — the measured audit.** A model wrote the same header in seconds. You put it through the same gate, then through the comparison the gate cannot perform, and you came out with numbers and a claim about where machine description fails and why.

Each step exists because the previous one is insufficient. Hand-authoring does not scale and cannot self-check. Schema validation checks form and is blind to fact. Machine generation is fast and fluent and cannot be trusted. **Only the combination produces a record you can defend**, and the part that makes it defensible is the human comparison at the end.

That is the argument this course is making, and this week is the first place you have made it with evidence of your own rather than taking it on faith.

**Takeaway:** Manual authorship gives truth without scale, schema validation gives structure without truth, and machine generation gives scale without either — the audit is what makes the combination defensible.

---

## **29 Content**

**Writing It Up: What Your Marker Is Looking For**

Your comparison is 300 to 500 words, and it is worth being explicit about how it is read.

**What earns credit:**

- Two *subtle* hallucinations, named specifically, with the field and the false value
- Evidence that they passed validation — this is what makes them subtle
- Your two counts, used with their correct names
- A claim about why those fields failed, not just that they did
- Correct attribution of authority identifiers to the sources you actually used

**What does not:**

- A general account of AI limitations. The lesson already gave you that; reproducing it shows nothing.
- Errors the schema caught. These are cheap and every student will have them.
- Claims you cannot point to a file for.
- Padding toward the word count. Five hundred words of specificity beats five hundred words of reflection.

**The one-sentence summary of the assignment:** show that a schema-valid description can be false, name the specific ways yours was, and explain what that implies about relying on structure as a guarantee.

**Takeaway:** Name two specific schema-valid falsehoods, supply your counts, and explain why those fields failed — specificity about your own files is what the mark rewards.

---

## **30 Content**

**What the Week Was For**

Three days, three ways of producing the same description.

- **Tuesday, by hand.** You wrote a TEI header yourself and found out how much a manuscript demands before it can be described at all (TEI Consortium, 2025).
- **Wednesday, by rule.** You gave your file to a schema, which found what you could not see in your own work (Cummings, 2018).
- **Friday, by machine.** A model did the job in seconds, and you measured it — which you could only do because of Tuesday and Wednesday.

```
Topic 02, complete:
  Tue  manual        hand-authored TEI header       -> your ground truth
  Wed  deterministic validated to 0 errors          -> your structural baseline
  Fri  AI-assisted   generated header, audited      -> measured against both
```

Here is the conclusion the week was built toward, and it is not the expected one. AI does not make schemas less important. It makes them essential.

When markup was slow and expensive, errors were rare because so little got produced. A system generating plausible TEI in seconds can produce wrong markup faster than anyone can read it. The schema is what removes the cheap errors automatically — and that is precisely what frees a human editor to spend attention on the expensive ones, the fabricated provenance and the identifier pointing at the wrong codex.

Notice what changed this week and what did not. The typing got faster. The judgement did not get easier, and it did not get less necessary. It became the only part that was ever scarce.

**Takeaway:** Generative AI makes deterministic schemas and human editorial judgement more necessary, because automating the cheap errors is what frees attention for the ones only a person can catch.

---

## References



Cummings, J. (2018). The Text Encoding Initiative and the study of literature. In R. Siemens & S. Schreibman (Eds.), *A Companion to Digital Literary Studies* (pp. 451–476). Blackwell.

De Cristofaro, M., & Zilio, D. (2025). Automating XML-TEI encoding of unpublished correspondence: A comparative analysis of two LLM approaches. *AIUCD 2025 Proceedings: Diversity, Equity, and Inclusion: Challenges and Opportunities for Digital Humanities in the Age of Artificial Intelligence*.

Ignatowicz, J., Kutt, K., & Nalepa, G. J. (2025). Metadata Enrichment Model: Integrating neural networks and semantic knowledge graphs for cultural heritage applications. *arXiv preprint*. https://arxiv.org/abs/2505.23543

Koho, M., Burrows, T., Hyvönen, E., Ikkala, E., Page, K., Ransom, L., ... & Wijsman, H. (2021). Harmonizing and publishing heterogeneous premodern manuscript metadata as Linked Open Data. *Journal of the Association for Information Science and Technology*, 73(2), 240–257. https://doi.org/10.1002/asi.24499

Romanello, M., & Gautier, A. (2024). Automatic metadata extraction: Leveraging large language models in digital humanities. *Journal of Open Humanities Data*.

TEI Consortium. (2025). *TEI P5: Guidelines for Electronic Text Encoding and Interchange*. Version 4.8.0. https://tei-c.org/release/doc/tei-p5-doc/en/html/

