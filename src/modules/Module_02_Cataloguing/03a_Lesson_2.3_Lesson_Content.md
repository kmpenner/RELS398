# Lesson 2.3 — Auditing AI-Generated Manuscript Metadata

*RELS 398 / ENGL 398 · Topic 2: Cataloguing · Meeting #5 (Fri Sep 11)*

***Step 3 of the three-step cycle: AI-assisted.** On Tuesday you wrote a TEI header by hand. On Wednesday you made a schema check it. Today a machine writes the same header in seconds, and your job is to find what is wrong with it — including the errors that pass every check you own.*

---

## **01 Content**

**What Today Actually Asks of You**

By Monday you owe a workshop submission with three parts: a validated `<msDesc>` for your assigned Greek witness, authority identifiers that resolve to the right records, and a 300 to 500 word comparison in which you name **at least two subtle hallucinations** in an AI-generated version of the same description.

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

Your workshop grade turns on this. "The AI made some mistakes" is not an audit. "The AI assigned Diktyon 12345 to a manuscript whose actual Diktyon number is different, and the wrong number resolves to a different codex entirely" is an audit. The second sentence is only available to someone holding a verified reference.

Keep your Tuesday file open beside the AI output all through today's lab. The comparison is not a step at the end. It is the work.

**Takeaway:** Your verified header is what converts an impression of the AI's cleverness into a specific, checkable claim about what it got wrong.

---

## **06 Content**

**Why VIAF and Pleiades Are Not Enough Here**

On Wednesday you linked your repository to VIAF and your place of origin to Pleiades. Both are excellent, and neither will carry your workshop submission.

VIAF identifies *people and institutions*. Pleiades identifies *ancient places*. Your witness is neither. It is a specific physical codex, holding specific texts, sitting in a specific library — and none of those three facts has an identifier in either system.

This is a real gap, and Greek manuscript scholarship built its own tools to fill it. Three of them appear in your workshop instructions, and you are graded on using them accurately.

| Question about your witness | The register that answers it |
| --- | --- |
| Which ancient text is this, as a text? | Trismegistos |
| Which work is this, and which manuscripts carry it? | Pinakes |
| Which physical Greek codex is this? | Diktyon |

The next three sections take these one at a time. Learn them for a practical reason as well as a scholarly one: they are worth three of the ten points on your workshop, and they are the identifiers a model is most likely to fabricate, because they are far rarer in its training data than VIAF numbers.

**Takeaway:** VIAF identifies people and Pleiades identifies places, so Greek manuscripts need their own registers — Trismegistos, Pinakes, and Diktyon.

---

## **07 Content**

**Trismegistos: An Identifier for the Text Itself**

Trismegistos began as a database of texts from Greco-Roman Egypt and grew into a much wider register of ancient texts and the material that carries them (Clarysse, 2010).

Its core idea is one you have already met in a different form. A CTS URN identifies a *work* as an abstract literary thing. A Trismegistos number identifies a *text* as a documented object of study — this inscription, this papyrus, this document, with its own record, bibliography, and links.

A TM number looks unglamorous: a bare number attached to a record at `trismegistos.org`. Its value is that it is stable and shared. Two scholars who have never met can be certain they are discussing the same text.

Trismegistos also maintains connected registers of places and of ancient persons and their name variants. That second one solves a problem you will recognize from any manuscript: the same person spelled six ways across four centuries.

Look yours up by shelfmark or by text before Friday, and record what you find. If your witness has no TM record, that is a finding worth reporting too, not a failure.

**Takeaway:** A Trismegistos number is a stable public identifier for an ancient text as a documented object, alongside its registers of ancient places and persons.

---

## **08 Content**

**Pinakes: Which Work, and Which Manuscripts Carry It**

Pinakes, maintained by the Institut de recherche et d'histoire des textes, is the reference catalogue for Greek literary works and the manuscripts that transmit them.

Its structure maps neatly onto TEI you already know, which makes it easier to learn than it first appears.

- **Authors** are entries for the writer, real or attributed, gathering everything credited to them.
- **Works** are entries for the text itself, independent of any one copy. This is the level your `<msItem>` describes.
- **Witnesses** are the manuscripts carrying that work. Your codex is one of them.

That three-part shape is the same distinction you drew on Tuesday between the work your page transmits and the physical object in front of you. Pinakes simply gives both an identifier.

The practical use for your workshop: find your work in Pinakes, and the record will list the other manuscripts that carry it. You will see immediately that your witness is one member of a family, which is the entire premise of Module 07's collation work.

Pinakes is in French. This is not an obstacle worth worrying about — the field names repeat, and you are reading a database, not an essay.

**Takeaway:** Pinakes catalogues Greek authors, works, and the manuscripts that transmit them, giving identifiers to the same work-versus-object distinction you drew on Tuesday.

---

## **09 Content**

**Diktyon: A Number That Survives a Change of Shelfmark**

Shelfmarks move. Collections are renumbered, libraries reorganize, and a manuscript cited by shelfmark in 1890 may sit under a different call number today. You met this problem on Tuesday and answered it with a permanent identifier.

Diktyon is that answer for Greek manuscripts. It assigns each known Greek codex a stable number that stays fixed regardless of what the holding library later calls it, and it lets catalogues that describe the same manuscript recognize one another.

The reasoning should feel familiar. It is the argument you accepted on Wednesday for CTS URNs, applied to physical objects instead of texts: a citation is only durable if it survives the administrative decisions of institutions.

Here is where this lesson gets an opportunity, so notice what is happening. **This lesson does not print the Diktyon number for the Codex Marchalianus, or for your witness.** Not because it is hard to find, but because a number you have not verified is exactly the failure mode you are being trained to catch. A confident, correctly formatted, unverified identifier is precisely what a model will hand you on Friday.

Look yours up. Then you will know it, rather than having been told it.

**Takeaway:** A Diktyon number identifies a Greek manuscript stably across changes of shelfmark, and this lesson deliberately makes you look yours up rather than supplying it.

---

## **10 Content**

**Putting Authority Identifiers into Your msDesc**

You already know the mechanism, because Wednesday taught it. An identifier goes into your markup as an attribute pointing outward, turning a string into a reference.

```xml
<msIdentifier>
  <settlement>Vatican City</settlement>
  <repository ref="http://viaf.org/viaf/141312782">Biblioteca Apostolica Vaticana</repository>
  <idno>Vat. gr. 2125</idno>
  <altIdentifier type="Diktyon">
    <idno>[the number you looked up]</idno>
  </altIdentifier>
</msIdentifier>

<msContents>
  <msItem n="1" corresp="[your CTS URN]">
    <title ref="[your Pinakes work record]">Isaiah</title>
  </msItem>
</msContents>
```

Two things to notice.

`<altIdentifier>` is how TEI records a second identifier for the same object alongside the shelfmark. That is precisely what a Diktyon number is, so it belongs there rather than jammed into `<idno>`.

And every bracketed placeholder above is something you must look up. That is not an accident of writing. It is the rule the rest of this lesson defends: an identifier you did not verify is not an identifier, whether a machine supplied it or a lesson did.

**Takeaway:** Authority identifiers attach to your markup through `@ref`, `@corresp`, and `altIdentifier`, and every one of them has to be looked up rather than assumed.

---

## **11 Content**

**Asking Well: How to Prompt for TEI**

Type "convert this into TEI XML" and you will get something poor: chatty preamble, invented tags, rejected on the first line. That is the prompt failing, not the model.

Researchers doing this at scale have converged on a few habits, and you can use all of them on Friday (De Cristofaro & Zilio, 2025).

- **Say who the model is.** "You are cataloguing a Greek manuscript in TEI P5" narrows what "usually comes next" means.
- **Say which tags are allowed.** Paste the element names you expect. The model cannot consult the schema, so putting part of it in the prompt is the closest available substitute.
- **Show a finished example.** One correct header teaches your house style faster than three paragraphs of instruction.
- **Demand XML and nothing else.** Otherwise you will spend the lab deleting "Certainly! Here is your TEI header:" from the top of the file.
- **Turn down the randomness.** Most interfaces expose a setting called temperature. Higher means more inventive; lower means more predictable. For markup you want predictable.

```
A workable system prompt:

"You are cataloguing a Greek manuscript in TEI P5.
Rules:
1. Output only a <TEI> element with the TEI namespace. No commentary.
2. Follow the hierarchy teiHeader > fileDesc > sourceDesc > msDesc.
3. Dates in @when, @notBefore, @notAfter must be YYYY or YYYY-MM-DD.
4. Use only elements from the TEI manuscript description module.
5. Write & as &amp;."
```

Keep the prompt you use. Your workshop comparison should quote it, because a result nobody can reproduce is not evidence.

**Takeaway:** A good TEI prompt names the role, lists permitted tags, shows an example, forbids commentary, and lowers the temperature — and you record it as part of your method.

---

## **12 Content**

**Give It a List Instead of Letting It Guess**

Ask a model for authority identifiers and it will produce authority identifiers. They will be correctly formatted. Some will lead nowhere, and some will lead confidently to the wrong record.

This is the single most dangerous behaviour in the lesson, and section 06 explained why it is worse for you than for most people. TM, Pinakes, and Diktyon numbers are far rarer in training data than VIAF numbers. The model has seen the *shape* of them and comparatively few real examples, which is the exact recipe for confident invention.

The fix is unglamorous. Stop asking the model to supply identifiers. Look them up yourself, put the verified ones in the prompt, and instruct the model to use only those (De Cristofaro & Zilio, 2025).

```xml
<!-- Verified by you, supplied with the prompt -->
<authorityList>
  <place ref="https://pleiades.stoa.org/places/727070">Alexandria</place>
  <org   ref="http://viaf.org/viaf/141312782">Biblioteca Apostolica Vaticana</org>
</authorityList>
```

An open-ended invention problem has become a matching problem, and matching is something these systems do well.

Note what this implies about the division of labour. The model is useful for structure and phrasing. The identifiers — the part your grade depends on — remain yours.

**Takeaway:** Models fabricate rare identifiers most confidently, so verify them yourself and give the model a list to match against instead of a gap to fill.

---

## **13 Content**

**The First Validation Pass**

Now the mechanical part, which you can already do. The AI hands you a file. You check it exactly as you checked your own on Wednesday.

Add the same `xml-model` line under the XML declaration, save, and open the Problems panel. Nothing here is new except whose work is being judged.

One instruction matters more than any other, and it is easy to get wrong in the moment. **Write down the error count before you fix anything.**

That first number is a measurement, and it is destroyed the moment you start editing. It is also the only number in your workshop that describes the model's unassisted performance. Everything after your first correction describes a collaboration between you and the machine, which is a different and less interesting claim.

So the order is: validate, record, *then* improve.

While you are reading the errors, sort them as you go. Some tell you the file is broken. Some tell you the file is odd. An `@material` value outside the permitted list is a structural error, but it is also a hint that the model guessed at the physical support — which is a factual question the schema cannot ask. The errors are evidence about the model's reasoning, not just a list of repairs.

**Takeaway:** Validate the AI file exactly as you validated your own, and record the first-pass error count before touching anything, because correcting destroys the measurement.

---

## **14 Content**

**Handing the Errors Back**

When the AI's file fails validation, you do not have to repair it by hand. You can show the model its own error messages and ask again (De Cristofaro & Zilio, 2025).

This works better than it has any right to, and section 02 explains why. The model never had the schema. An error message is a small, precise piece of that schema, delivered exactly where it is needed. You are supplying the missing rulebook one line at a time.

```
What you paste back:

"Your TEI failed validation with these 2 errors:
 1. line 14: element 'supportDesc' not allowed here; expected inside 'objectDesc'
 2. line 28: value 'ca. 550' is not a valid date
Return only the corrected XML."
```

Two cautions.

**Cap the loop.** Two or three attempts, then finish by hand. Capable models converge in one or two rounds; weaker ones resubmit the same mistake indefinitely, because interpreting a compiler message is itself a reasoning task (De Cristofaro & Zilio, 2025). Without a cap you can lose an afternoon.

**Watch what the repairs cost.** Look closely at the second error above. Asked to fix `ca. 550`, a model will often return `when="0550"` — a precise date replacing an explicitly approximate one. The file now validates. It also now asserts something the source never said. Structural repair can quietly manufacture false precision, which is the subject of section 19.

**Takeaway:** Feeding validation errors back repairs most structural faults, but cap the loop and check whether a repair invented certainty the source never had.

---

## **15 Content**

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

## **16 Content**

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

## **17 Content**

**Obvious Factual Errors: Check These First**

Now errors the schema cannot see but you can, quickly, by looking at your own file and your image.

Five fields carry most of them.

- **Support.** The model says paper; your image plainly shows parchment. It guessed from a period, or from nothing.
- **Extent.** A folio count that does not match what you counted.
- **Hands.** A single hand asserted where you recorded three.
- **Date.** A century that contradicts your own dating.
- **Repository.** The wrong library, sometimes a famous one substituted for an obscure one.

That last pattern is worth naming, because it is systematic rather than random. Asked about an unfamiliar manuscript, a model drifts toward the famous: the Vatican rather than the small diocesan collection, the well-known scribe rather than the anonymous one. Its training data contains far more text about famous things, so "what usually comes next" is biased toward them.

This gives you a place to look first. **Check the parts of your description that are unusual.** A witness that is ordinary in every respect will be described well. Whatever makes yours distinctive is exactly where the model will have replaced your manuscript with the average one.

**Takeaway:** Obvious factual errors cluster in support, extent, hands, date, and repository, and models drift toward the famous, so check whatever is distinctive about your witness first.

---

## **18 Content**

**The Subtle One: The Provenance That Never Happened**

Here is the failure that gives this lesson its shape. Read it slowly.

You give a model a thin description: *Vat. gr. 2125: 6th-century prophetic codex, uncial script, damaged at the beginning, provenance Egypt.* You ask for a full `<history>`. It returns this.

```xml
<!-- Generated by a model. Every fact in it is invented. -->
<provenance notBefore="0700" notAfter="0750">
  <p>Transferred in 722 CE to the Monastery of Saint Catherine at Mount Sinai
     by the monk Dorotheus, and recorded in the 8th-century library inventory.</p>
</provenance>
```

Now audit it with everything you own. The XML is well-formed. The elements are real TEI. The dates are correct ISO 8601 and consistent with each other. Run it through Wednesday's schema and it reports zero errors.

Mount Sinai is invented. Dorotheus is invented. The year 722 is invented. The inventory is invented. The model assembled a plausible provenance from general knowledge of how manuscripts moved, and produced fiction in perfect TEI.

Notice what makes it convincing: it is *specific*. Vague output reads as uncertain, and specific output reads as researched. The model has no way to be vague — it produces the most probable continuation, and a probable provenance narrative contains names and dates.

**Specificity is not evidence.** In AI output, it is the opposite: an unexpectedly precise claim about a poorly documented object is the thing to distrust first.

**Takeaway:** A model produces fabricated provenance in flawless TEI that passes the schema at zero errors, and its specificity is a warning sign rather than a mark of research.

---

## **19 Content**

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

## **20 Content**

**The Subtle One: What Is Not There**

Every error so far was something written down. This one is the absence of something, and it is the hardest kind to see.

The behaviour was documented at scale. In the PubCINET study, one model produced near-flawless valid TEI and, when a document mentioned a person outside the supplied reference list, simply left them untagged rather than work out who they were (De Cristofaro & Zilio, 2025). The markup was perfect and the record was incomplete.

Think about how invisible that is. A missing hand produces no error. A missing `<msItem>` produces no error. The file is green, the structure is clean, and nothing anywhere signals that something is absent. **A schema can only judge what you gave it.** It has no view of what should have been there.

This is why comparison, not inspection, is the method. Reading the AI file on its own, you will never find an omission — there is nothing to see. Reading it beside your own header, an omission is obvious immediately, because your file has an element theirs does not.

So work through your own header element by element and ask of each: is this present in the AI version? That is a mechanical procedure, it takes a few minutes, and it will find things no validator can.

**Takeaway:** Omissions produce no error and cannot be found by reading the AI file alone, so audit by walking your own header element by element.

---

## **21 Content**

**The Subtle One: The Link That Goes Somewhere Else**

Section 12 warned that models fabricate identifiers. Now look at what that produces in a finished file, because it is a strong candidate for your second subtle hallucination.

A fabricated identifier fails in three different ways, and only one is easy to spot.

- **It resolves to nothing.** The URL is dead. Annoying, but honest: anyone who clicks discovers the problem.
- **It is correctly formatted and wrong.** The number belongs to a real record for a different manuscript. Nothing looks broken. A reader who trusts it now believes something false about your witness.
- **It is nearly right.** A Pinakes work identifier for the correct author but the wrong work; a Diktyon number one digit off, landing on a real codex.

The second and third are what to hunt for. They pass every check in your toolchain: valid XML, valid schema, resolvable URL, plausible record. The only test is to follow the link and read what is on the other end.

That is your method, and it takes about a minute per identifier. **Click every one.** If the record that opens is not your manuscript, your work, or your library, you have found a subtle hallucination worth writing up — one your marker can verify by clicking too.

**Takeaway:** Fabricated identifiers most often resolve to a real but wrong record, passing every automatic check, so the only test is following each link and reading what opens.

---

## **22 Content**

**The Subtle One: The Citation That Does Not Resolve**

On Wednesday you built a CTS URN for your passage. It is strict and multi-part, and every part must be right (Blackwell & Smith, 2019; Tiepmar & Heyer, 2014).

Ask a model for one and it will produce the right shape. Shape is never the problem. Three things go wrong inside it.

- **Invented namespaces.** `urn:cts:bible:` looks reasonable and does not exist; the real one is `urn:cts:greekLit:`.
- **Wrong work numbers.** The model half-remembers a TLG number and assigns Homer's identifier to Isaiah. The URN is perfectly formed and points at the wrong text.
- **Invented word positions.** A sub-reference points to the fifth occurrence of a word that appears three times (Blackwell & Smith, 2019).

Each produces a citation that looks correct in your file and fails when somebody tries to follow it. Since the entire purpose of a canonical URN is to still resolve in fifty years, a fabricated one is worse than none: a broken promise that looks like a kept one.

The rule from section 12 applies unchanged. Do not accept an identifier from a model. Resolve it against the real service before it enters your file.

**Takeaway:** Generated CTS URNs are correctly shaped and frequently point at the wrong text, so every one must be resolved against a real service before you commit it.

---

## **23 Content**

**Where Models Are Weakest, and Who That Harms**

One pattern runs underneath sections 17 through 22, and it is worth stating on its own, because it is a scholarly problem rather than a technical one.

A model is accurate in proportion to how much it has read about something. That is not a flaw to be fixed; it is what the method is. And it means performance is unevenly distributed in a way that follows existing scholarly attention.

Well-catalogued, frequently-edited, much-discussed material gets described well. Latin and Greek codices in major European collections have been written about for centuries, and models handle them competently. Material outside that centre — Syriac, Coptic, Ethiopic, Armenian, and archival documents in minority languages — is thinly represented, and there the model does not fall silent. It produces the same confident, fluent, plausible output, with far more of it invented.

Sit with the consequence. **The tool performs worst exactly where the cataloguing backlog is largest.** The collections most in need of the speed are the ones where the output is least trustworthy, and the failure is invisible, because the prose is equally polished either way.

An unaudited pipeline run across a mixed collection will widen the gap between well-described and neglected traditions, while appearing neutral and efficient. If you work on material outside the well-trodden centre, budget more auditing, not less.

**Takeaway:** Models are least reliable on the least-studied traditions, so unaudited automation widens existing cataloguing inequities while appearing neutral.

---

## **24 Content**

**The Six-Field Scorecard**

Time in Friday's lab is short, so the scoring has to be something you can finish. Six fields, three verdicts.

| Field | Right | Wrong or invented | Missing |
| --- | --- | --- | --- |
| Repository | | | |
| Shelfmark or idno | | | |
| Support material | | | |
| Extent | | | |
| Number of hands | | | |
| Date of origin | | | |

Mark each against your own validated header, not against your impression. Three minutes, and you leave with a result rather than a feeling.

Two rules keep the scorecard honest.

**A confident, valid, false value counts as wrong**, not as partial credit. If the model asserts a shelfmark that is not yours, the fact that it is well formed is irrelevant.

**Missing is its own column**, kept separate from wrong. Section 20 explained why: omission and invention are different failures with different causes, and averaging them together hides both.

Record two numbers alongside the grid: the AI file's first-pass error count from section 13, and its count after one correction round. Those three items — grid, first count, second count — are the entire evidence base for your workshop comparison.

**Takeaway:** Score six fields as right, wrong, or missing against your verified header, keeping omission separate from invention, and record the error counts before and after correction.

---

## **25 Content**

**Precision and Recall, From Your Own Counts**

Your scorecard already contains two standard measures. They have formal names, and using them correctly will sharpen your comparison (De Cristofaro & Zilio, 2025).

**Precision** asks: of everything the AI claimed, how much was right? Divide the right answers by everything it supplied. Low precision means it makes things up.

**Recall** asks: of everything that should have been found, how much did it find? Divide the right answers by everything in your header. Low recall means it leaves things out.

Work an example. The AI fills five of your six fields and gets four right. Precision is four out of five. Recall is four out of six. Two different numbers describing two different failures, from one grid.

This is why reporting a single score hides what happened. A model with high precision and low recall is cautious and incomplete — say too little, all of it true. A model with high recall and low precision is thorough and unreliable — say everything, some of it invented. Those call for opposite responses: the first needs prompting to be bolder, the second needs stricter verification.

You may combine them into one figure, which is called F1, but the pair tells you more than the average.

**Takeaway:** Precision is how much of what the AI said was true and recall is how much of the truth it found, and the pair distinguishes a cautious model from an unreliable one.

---

## **26 Content**

**Sorting the Differences**

Put your validated header beside the AI's and go through the differences one at a time. `git diff` will line them up, using the tool from Lesson 1.1.

Each difference falls into one of four categories, and choosing the category *is* the analysis.

1. **Structural error.** The schema found it for you.
2. **Factual error.** A fabricated date, a hand that does not exist, a wrong shelfmark. Only you can find it.
3. **The AI was right and you were not.** It caught something you missed.
4. **Legitimate disagreement.** Both descriptions defensible. A broader date range is not an error because you chose a narrower one.

```
Discrepancy log — worked example:
  origDate     you "0550-0599"  | AI "0500-0600"      -> legitimate disagreement
  supportDesc  you "parchment"  | AI "parchment"      -> match
  handNote     you "h1, h2, h3" | AI "h1"             -> factual error: two hands missed
  decoNote     you none         | AI "marginal signs" -> AI was right; verify, then adopt
```

Category three deserves a word. It happens, it is not embarrassing, and recording it honestly is what makes this research rather than a defence of your own work. A comparison finding zero AI advantages reads as unobserved, not rigorous.

Keep the log as you go. Reconstructing it from memory afterwards does not work.

**Takeaway:** Every difference is a structural error, a factual error, a genuine AI catch, or a legitimate disagreement, and recording the third category honestly is what makes the audit credible.

---

## **27 Content**

**Recording the Machine's Part in the File**

If a model drafted part of your description, the edition must say so. This is not a disclaimer. It is provenance — which you already accept as an obligation for manuscripts, and which applies just as much to your own work.

The argument is simple. A future reader needs to know which claims came from an editor who examined the object and which from a system predicting plausible text. Those deserve different trust, and the difference is invisible in finished markup unless recorded.

TEI has the elements, and you met both on Tuesday.

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

Record the model version. "An AI wrote this" will mean little in ten years; a version and a date can be checked.

This also protects you. A documented AI draft that you audited is methodologically respectable. An undocumented one that a reader later detects is not.

**Takeaway:** Record AI contributions in `respStmt` and `revisionDesc` with model versions and dates, because algorithmic provenance is provenance.

---

## **28 Content**

**Friday's Lab, Step by Step**

Now run the experiment on your own witness.

1. **Look up your identifiers first.** Trismegistos, Pinakes, Diktyon. Do this before any prompting, so you hold verified values the model cannot influence.
2. **Gather your input.** Put your raw notes and catalogue description into a plain text file — the object as you found it, not your finished header.
3. **Prompt the model** using section 11. Save the prompt itself; you will quote it.
4. **Save the output untouched** as `witness_ai.xml`. Do not tidy it. The unedited version is your evidence.
5. **Validate and record the count** before fixing anything. This is section 13, and it is the step most often lost to enthusiasm.
6. **Run one correction round** as in section 14, and record the new count.
7. **Score the six fields** from section 24 against your validated header.
8. **Click every identifier** the model produced. This is where your subtle hallucinations are most likely to be, and it takes about a minute each.

Commit both files when you are done.

If time runs short, steps 1, 4, 5, and 8 are the ones that matter. An unfixed AI file, its first error count, and one identifier proven wrong is a complete finding.

**Takeaway:** Verify identifiers before prompting, record the untouched output and its first error count, then score six fields and follow every link the model produced.

---

## **29 Content**

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

Blackwell, C., & Smith, N. (2019). The CITE Architecture: A conceptual and practical overview. In M. Berti (Ed.), *Digital Classical Philology: Ancient Greek and Latin in the Digital Revolution* (pp. 73–94). De Gruyter Saur.

Clarysse, W. (2010). The Trismegistos database of ancient texts and manuscripts. *Literary and Linguistic Computing*, 25(3).

Cummings, J. (2018). The Text Encoding Initiative and the study of literature. In R. Siemens & S. Schreibman (Eds.), *A Companion to Digital Literary Studies* (pp. 451–476). Blackwell.

De Cristofaro, M., & Zilio, D. (2025). Automating XML-TEI encoding of unpublished correspondence: A comparative analysis of two LLM approaches. *AIUCD 2025 Proceedings: Diversity, Equity, and Inclusion: Challenges and Opportunities for Digital Humanities in the Age of Artificial Intelligence*.

Ignatowicz, J., Kutt, K., & Nalepa, G. J. (2025). Metadata Enrichment Model: Integrating neural networks and semantic knowledge graphs for cultural heritage applications. *arXiv preprint*. https://arxiv.org/abs/2505.23543

Koho, M., Burrows, T., Hyvönen, E., Ikkala, E., Page, K., Ransom, L., ... & Wijsman, H. (2021). Harmonizing and publishing heterogeneous premodern manuscript metadata as Linked Open Data. *Journal of the Association for Information Science and Technology*, 73(2), 240–257. https://doi.org/10.1002/asi.24499

Romanello, M., & Gautier, A. (2024). Automatic metadata extraction: Leveraging large language models in digital humanities. *Journal of Open Humanities Data*.

TEI Consortium. (2025). *TEI P5: Guidelines for Electronic Text Encoding and Interchange*. Version 4.8.0. https://tei-c.org/release/doc/tei-p5-doc/en/html/

Tiepmar, J., & Heyer, G. (2014). A new implementation for Canonical Text Services. In *Proceedings of the Workshop on Human-Computer Tractable Data for the Digital Humanities* (pp. 1–8).
