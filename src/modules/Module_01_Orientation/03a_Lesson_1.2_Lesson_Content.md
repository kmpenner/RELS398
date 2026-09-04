# Lesson 1.2 — Data That Lasts: FAIR Principles and the Scholarly Edition Workflow

*RELS 398 / ENGL 398 · Topic 1: Orientation · Meeting #2 (Fri Sep 4)*

*Orientation week — the three-step comparative cycle does not yet apply. This meeting sets the scholarly agenda for the whole term: what digital humanists are trying to produce, and why they produce it that way. By the end of today you will know the FAIR principles, the standard workflow of a scholarly digital edition, and the tools and accounts you will use — and you will have chosen the manuscript passage that every later assignment builds on.*

---

## **01 Content**

**Where We Stand After Lesson 1.1**

On Wednesday you met the digital workbench: plain text instead of proprietary document formats, VS Code as your editor, the command line as a precision instrument, Git as a time machine, XML as a way of labeling what text means, Python as an automation engine, and AI assistants that must always be checked against evidence. If any of those words still feel shaky, that is expected — every one of them returns in a specific week of this course, where it gets practiced for real.

Today we answer a different question. Not *what tools will we use*, but *what are we making, and why does it look like this?* The answer is a scholarly edition — a curated, documented, reusable representation of a historical document. And the reason digital humanists insist on plain text, Git, and XML is that those choices are what make an edition trustworthy, shareable, and durable. The technical habits of Lesson 1.1 exist to serve scholarly values you will meet today.

Those values have a name and a formal statement: the FAIR principles. They also have a concrete shape: the workflow that every scholarly edition of an ancient document follows, from cataloguing the manuscript to publishing the finished text. Both come straight from the research community you are joining this semester.

**Vocabulary.** *Scholarly edition* — a curated representation of a document that records evidence and editorial decisions so that others can examine and reuse them. *Research data* — the artifacts (texts, images, metadata, code) on which scholarly claims are based.

**Takeaway:** Lesson 1.1 gave you the tools; today gives you the purpose — producing scholarship that other people can find, check, and reuse.

---

## **02 Content**

**Why Ancient Documents Are Hard to Study**

Start with the object itself. A surviving ancient or medieval document is handwritten — there is no typeset original to consult. Each manuscript is unique: when scribes copied a text, every copy introduced small differences, so hundreds of "editions" of one work exist, none authoritative. Hands are difficult to read: abbreviations were standard, spelling was not fixed, and layout carries meaning that a plain transcription flattens. Manuscripts are also physically dispersed — the witnesses to a single ancient work may sit in libraries in five countries — and they are fragile, so direct access is rationed and expensive.

These difficulties explain almost every technique you will learn this semester. Because every copy differs, we learn collation and textual criticism (Modules 7–8). Because hands are hard to read, we learn transcription and HTR (Module 4). Because documents are dispersed, we learn to work from digital images (Module 3) and shared catalogs (Module 2). The field did not adopt digital methods out of fashion; it adopted them because the objects demand systematic comparison and sharing.

Keep this in mind as a reading strategy for the whole course: whenever a new tool appears, ask *which difficulty of the manuscript itself* is this tool answering? If you can answer that, you understand the method. If you cannot, you have probably memorized a button.

**Vocabulary.** *Witness* — one manuscript copy of a work, used as evidence for its text. *HTR* — handwritten text recognition, machine transcription of handwriting. *Dispersed corpus* — the surviving copies of a work, scattered across many libraries.

**Takeaway:** Ancient documents are handwritten, individually variable, dispersed, and fragile — and each digital method in this course exists to answer one of those difficulties.

---

## **03 Content**

**What Scholars Have Always Made: The Edition**

For five centuries the central product of textual scholarship has been the edition. An edition is not a photograph and not a paraphrase. It is an argument, made with evidence: the editor gathers the witnesses, compares their readings, decides which reading probably stood in the lost original (or deliberately preserves each witness's own text), and presents a reconstructed text together with an *apparatus* — the formal record of important variants and emendations.

Print editions achieve a great deal. A critical edition of a classical work, with its introduction describing the manuscripts and its apparatus recording variants, lets a reader who will never visit the Vatican Library know what the evidence is. This is worth dwelling on: scholarly publishing solved the dispersion problem, in its own medium, long before computers. Catalogs, printed facsimiles, and critical editions were the original knowledge infrastructure.

But print has a structural limit. An edition must *conclude*: the editor's decisions are baked into the printed text, while the evidence that justified them is compressed into a few cramped apparatus lines. If you disagree with the editor's choice — or want to ask a question the editor never thought of — the printed page cannot answer you. The evidence has been consumed in the act of publication.

**Vocabulary.** *Critical edition* — an edition that reconstructs a text by weighing variant readings across witnesses. *Apparatus criticus* — the formal footnoted record of variant readings in a critical edition. *Emendation* — a proposed correction to the transmitted text.

**Takeaway:** Print editions record the editor's conclusions, but the reasoning and evidence are compressed almost beyond recovery — the limitation digital editions exist to remove.

---

## **04 Content**

**What a Digital Edition Adds**

A digital edition treats the *evidence* — not just the conclusions — as the publication. Every witness transcription is stored. Every variant is marked up as structured data, not squeezed into a footnote. Every editorial decision can carry its justification inline. A reader can display the text of manuscript B instead of the editor's reconstruction, search across all witnesses, or count how often a particular scribe makes a particular kind of error. Gabler called this the digital scholarly edition: not a text with decoration, but a library of linked, machine-readable evidence that generates many possible readings.

This only works because of the Lesson 1.1 stack. The transcription is plain text, so any program can read it. It is marked up in XML using TEI vocabulary, so the tags mean the same thing in every project. It is version-controlled in Git, so every editorial change is dated, attributed, and reversible. A claim in a digital edition is *inspectable* in a way a printed claim cannot be: you can walk from the published reading back to the image of the manuscript.

Your instructor sketched this program in a keynote — "A Toolkit for Humanities Research and Editing Ancient Documents" (DHSI-East 2022) — which is the direct ancestor of this course's structure. Its proposal: standardize the workflow, connect existing open tools instead of reinventing them, and make every intermediate product reusable. That agenda is this syllabus.

**Vocabulary.** *Digital scholarly edition* — an edition published as structured, machine-readable data, preserving evidence alongside conclusions. *TEI* — the Text Encoding Initiative, the standard XML vocabulary for encoding texts. *Inspectability* — the ability of a reader to trace a published claim back to its evidence.

**Takeaway:** A digital edition publishes the evidence itself, so readers can re-derive, question, and reuse the editor's work — which is exactly what print cannot do.

---

## **05 Content**

**FAIR: The Principles That Govern Research Data**

In 2016 a consortium of research organizations published a short paper that became the reference point for data management across the sciences and humanities: Wilkinson et al., *The FAIR Guiding Principles for scientific data management and stewardship*. FAIR states what well-managed research data should be. The acronym stands for:

- **F**indable — others (and machines) can discover the data, through persistent identifiers and rich metadata.
- **A**ccessible — once found, the data can actually be retrieved, using open, well-defined protocols.
- **I**nteroperable — the data uses shared formats and vocabularies, so different tools and projects can combine it.
- **R**eusable — the data is documented and licensed clearly enough that a stranger can legitimately build on it.

Two points of emphasis. First, FAIR is about *data and metadata*, not about software or paper: a PDF of an edition is not FAIR because its contents are locked in presentation. Second, FAIR is deliberately not a rulebook but a matrix of principles — each project decides how to implement them. FAIR says a digital edition should be findable, accessible, interoperable, and reusable; TEI, Git, GitHub, IIIF, and open licenses are *how* this course implements it.

**Vocabulary.** *FAIR principles* — Findable, Accessible, Interoperable, Reusable: the guiding criteria for research data management (Wilkinson et al. 2016). *Metadata* — structured information about an object: who made it, what it is, where it lives. *Persistent identifier* — a stable web address (like a DOI) that keeps pointing at an object even if it moves.

**Takeaway:** FAIR = Findable, Accessible, Interoperable, Reusable — the checklist that turns a personal project into community infrastructure.

---

## **06 Content**

**FAIR Before the Internet**

FAIR sounds like a modern invention, but scholarly practice was converging on it for centuries — with paper. Findable: manuscripts were described in library catalogs and printed indexes, so a scholar could discover that Codex Marchalianus was in the Vatican, without traveling there first. Accessible: facsimile volumes and printed editions put the texts into libraries worldwide. Interoperable: Latin, and later modern languages, plus conventions like standard citations, meant a German edition could be used by an Italian scholar. Reusable: critical apparatus explicitly licensed *reuse* — the next editor built on the last one's variant reports rather than re-reading every manuscript.

The keynote slide titled "FAIR before the Internet" makes exactly this point: manuscript catalogs and print editions were the FAIR infrastructure of early modern scholarship. What the internet changed was scale and mechanism. A printed catalog can tell you a manuscript exists; an online catalog with images lets you *read it* from Antigonish. A printed apparatus lets you see a handful of variants; a digital corpus lets you *compute* over thousands.

So this course is not teaching something alien. It is teaching the same scholarly values, with tools that operate at a scale print never could — and with new failure modes (link rot, format obsolescence) that FAIR's emphasis on durable identifiers and open formats is designed to prevent.

**Vocabulary.** *Catalog* — a structured description of a library's holdings; the original "findable" layer. *Facsimile* — a full reproduction of a manuscript, photographic or printed. *Link rot* — the decay of web addresses over time, the failure mode persistent identifiers exist to prevent.

**Takeaway:** Catalogs, facsimiles, and print editions already pursued findability, accessibility, and reuse — the internet changed the scale, not the values.

---

## **07 Content**

**F and A: Making Manuscripts Findable and Accessible**

The first two FAIR letters concern getting hold of the material. *Findable* means a researcher can discover that an object exists and where it lives. For manuscripts this is the work of shared catalogs: Pinakes for Greek manuscripts, the LDAB for literary papyri, Papyri.info for documentary papyri, Trismegistos for dates and identifiers. Each catalog record is *metadata* — shelfmark, contents, date, provenance, bibliography — built so that both humans and machines can retrieve it. In Module 2 you will write metadata of exactly this kind for your own passage, as a TEI header.

*Accessible* means retrieval is actually possible under defined conditions. For manuscripts this changed everything in the last two decades: digitization programs and the IIIF framework (the International Image Interoperability Framework — the subject of Module 3) put high-resolution images online with standard web addresses, so a scholar can study and even *annotate* the images without traveling. Many libraries now publish IIIF image servers for open materials; the Bodleian, the Vatican, and vHMML all serve manuscript images this way.

Notice the division of labor: catalogs make things findable, image servers make them accessible, and neither requires the scholar to own anything. When you choose your manuscript passage on Friday, you will be relying on exactly this layer — a findable record with accessible images.

**Vocabulary.** *Pinakes / LDAB / Papyri.info* — shared catalogs of Greek manuscripts and papyri. *IIIF* — International Image Interoperability Framework; standard URLs for serving and working with high-resolution images. *Shelfmark* — a manuscript's library call number (e.g., "Vat. gr. 2121").

**Takeaway:** Shared catalogs make manuscripts findable and IIIF image servers make them accessible — the F and A of FAIR, and the raw material of your own project.

---

## **08 Content**

**I: Interoperability — Shared Formats and Vocabularies**

Interoperable means data from one project can be combined with data from another without custom translation. This is the letter that dictates most of this course's technical choices. If my transcription says a damaged word is `<damage>` and yours says `<lacuna>`, no software can combine our work; if both say the TEI's `<damage>`, every TEI-aware tool handles both. Interoperability is why you will learn XML and TEI rather than some bespoke format — TEI tags are the shared vocabulary of the field.

The same logic runs through every layer. Metadata uses shared vocabularies (Dublin Core terms, RDF triples with standard properties) so that catalog records can be merged across institutions — that is Week 2's Wednesday exercise, building RDF from your TEI header. Identifiers follow shared schemes: CTS URNs give every passage of ancient literature a permanent, canonical address, so a citation in my edition can point at the exact passage in yours. Images follow IIIF so any viewer can display any library's images.

Interoperability has a human face too: a format a stranger can understand counts as interoperable in the scholarly sense. This is why this course, and the THREAD project your instructor described in the keynote, favor boring, open, documented standards over clever proprietary ones. Clever locks out; boring composes.

**Vocabulary.** *Interoperability* — the ability of data and tools from different projects to work together. *RDF triple* — a subject–predicate–object statement in a shared machine-readable vocabulary. *CTS URN* — a permanent canonical identifier for a passage of ancient literature.

**Takeaway:** Interoperability means choosing shared vocabularies — TEI, Dublin Core, CTS URNs, IIIF — over private ones, so that projects compose instead of isolating.

---

## **09 Content**

**R: Reusability — Licensing, Documentation, Provenance**

The last letter is where digital scholarship most often fails, and where you have the most control. Reusable means: a stranger, finding your data and downloading it, can understand what it is, trust where it came from, and know what they are allowed to do with it. Three things deliver that.

*Documentation.* Your TEI header will contain not just the manuscript's metadata but yours: who transcribed, with what method, on what date, following which conventions. Huskey (2024) shows Git functioning as a research journal here — the commit history is the documentation of *how the work developed*, and your commit messages are its prose.

*Licensing.* Data without a license is legally unusable, because copyright defaults to "all rights reserved." This course follows the open-science norm: your edition work will carry an open license (such as Creative Commons Attribution), which converts "please ask" into "reuse freely, with credit."

*Provenance.* A reusable dataset records where each piece came from: which library's image, which HTR model's transcription, which human corrected it. You will practice this in Module 5, where the reconciliation report states the error rate of each source — machine and human — against your hand-made ground truth.

**Vocabulary.** *Open license* — a statement (e.g., CC BY) granting reuse rights in advance. *Provenance* — the documented origin and processing history of a piece of data. *Ground truth* — a manually verified reference product against which automated outputs are measured.

**Takeaway:** Reusability = documentation + open license + provenance; Git, TEI headers, and reconciliation reports are where each lives.

---

## **10 Content**

**The Workflow: Eight Stages of Editing an Ancient Text**

Now assemble the purpose and the principles into a procedure. The keynote's central diagram — borrowed and extended by THREAD and similar projects — lays out the standard workflow of a scholarly digital edition as a sequence of stages, each with dedicated open tools:

Cataloguing → Images → Transcription → Normalization/Reconciliation → Collation/Textual criticism → Linguistic markup → Translation & Annotation → Presentation.

This is not a checklist invented for a course; it is how the field organizes itself. Papyri.info, the Homer Multitext, Codex Sinaiticus Online, eScriptorium projects — all follow some version of this pipeline, because it mirrors the logic of the task: you must know what witnesses exist (cataloguing) before you can look at them (images), read them (transcription), clean and compare what you read (normalization, collation), analyze it (linguistic markup), interpret it (translation, annotation), and only then publish (presentation).

Two properties are worth naming. The stages *compose*: each stage's output is the next stage's input, in open formats — that is interoperability in action. And the stages are *checkpointed*: modern practice keeps each stage's product in version control, so the edition's history is inspectable end to end — that is reusability.

This course's thirteen modules are this workflow, spread over a semester, each practiced three ways (manual, deterministic, AI-assisted).

**Vocabulary.** *Pipeline* — a staged workflow where each stage consumes the previous stage's output. *eScriptorium* — an open platform for HTR transcription. *Homer Multitext / Codex Sinaiticus* — flagship digital editions illustrating the workflow at scale.

**Takeaway:** The scholarly edition workflow — cataloguing through presentation — structures this entire course, and each stage feeds the next through open formats.

---

## **11 Content**

**Stage 1: Cataloguing the Witnesses**

Everything begins with a question most students skip: *which copies of this text exist, and where are they?* Cataloguing means answering that with metadata: for each witness, an identifier, a library and shelfmark, a date, a description of contents, and a bibliography. Before an editor transcribes a single letter, this stage decides the *scope of the evidence* — and a mistake here (missing a witness, misdating one) propagates into every later stage.

The work is institutionalized in shared catalogs. Pinakes catalogs Greek manuscripts; the Leuven Database of Ancient Books (LDAB) covers literary papyri; Papyri.info integrates papyrological editions; Trismegistos assigns stable identifiers that other databases reuse. These catalogs are FAIR infrastructure in the strict sense: findable (searchable online), interoperable (shared identifiers like Trismegistos numbers that appear in other systems), reusable (openly consultable).

In Week 2 you will do a miniature of this: identify the manuscript your passage comes from, gather its metadata, and write it as a TEI header — the catalog record that will live inside your own edition files for the rest of the term. Your Tuesday-by-hand version becomes the ground truth against which you judge a validation run and an AI-enriched version. Cataloguing is not clerical preface work; it is the first scholarly act.

**Vocabulary.** *TEI header* — the metadata section of a TEI file, describing the source, the editing, and the responsible parties. *Trismegistos number* — a stable identifier shared across papyrological databases. *Scope of evidence* — the set of witnesses an edition takes into account.

**Takeaway:** Cataloguing fixes the identity and location of your evidence; Week 2 has you write your passage's catalog record as a TEI header.

---

## **12 Content**

**Stage 2: Getting the Images — Digitization and IIIF**

An editor used to work from microfilm or travel; today the first stop is a digital image. Libraries photograph manuscripts at very high resolution and serve the images through IIIF, which gives every image — and every *region* of every image — a standard web address. IIIF also lets scholars annotate and compare images across libraries in shared viewers, which is why Module 3 is devoted to it.

Image quality is not a luxury. Transcription, paleographic analysis (letterforms, abbreviations, corrections), and HTR training all consume images, and their quality bounds what the later stages can achieve. This is the pipeline's first lesson in *garbage in, garbage out*: an unreadable image produces an unverifiable transcription no matter how careful the scholar.

Two practices from this stage matter for your project. First, *record the image source*: your TEI header will point at the specific IIIF address of each page you use, which is provenance and findability in one act. Second, *respect the access conditions*: libraries publish images under specific agreements, and reusable scholarship cites them properly rather than hoarding copies. When you verify your chosen passage on Friday, checking that good images exist — and bookmarking their IIIF addresses — is part of the check.

**Vocabulary.** *IIIF image server* — a library service delivering manuscript images at standard URLs with zoom and region support. *Paleography* — the study of historical handwriting. *Digitization program* — a library's systematic campaign to photograph and publish its holdings.

**Takeaway:** Digitized images accessed through IIIF are the edition's sensory evidence — and citing their source is your first provenance practice.

---

## **13 Content**

**Stage 3: Transcription — From Pixels to Plain Text**

Transcription converts the image into plain text: the pivotal stage, because it is where the manuscript first becomes computable. The key distinction, which Week 4 takes up in depth, is *diplomatic* versus *normalized*. A diplomatic transcription records exactly what the scribe wrote — abbreviations expanded in brackets, line breaks preserved, errors left standing. A normalized transcription silently regularizes spelling and layout to modern conventions. Editors choose deliberately, and record the choice; this course will have you do both and feel the trade-off.

Machine help has transformed the stage. HTR systems such as Transkribus learn a specific hand from examples and then transcribe pages automatically; you will train a model on your own hand-typed ground truth in Week 4. But machine output always contains errors, so professionals work by *double-keying* (two independent transcriptions compared letter by letter) or by systematic correction against the image — the reconciliation work of Week 5, which measures error rates rather than trusting impressions.

This is where Lesson 1.1 becomes daily practice: the transcription is typed in VS Code as plain text (or exported from Transkribus into plain text), and every session is committed to Git with a message saying what was done. The transcription file is the single most cited artifact of the whole edition.

**Vocabulary.** *Diplomatic transcription* — a transcription preserving the source's exact spelling, layout, and errors. *Double-keying* — two independent transcriptions compared to catch errors. *Ground truth* — your hand-verified transcription, used to measure machine output.

**Takeaway:** Transcription turns image into computable plain text; HTR accelerates it but never removes the human duty of verification.

---

## **14 Content**

**Stage 4: Reconciliation and Normalization**

Raw transcriptions disagree — with the manuscript, with each other, and with themselves. *Reconciliation* is comparing independent transcriptions of the same page and building a consensus text, recording every disagreement and how it was resolved. Week 5 has you do this by hand (Haaf et al. explain the statistics of double-keying), and then measure character and word error rates for the HTR and AI passes against your manual ground truth. Error rates sound humble, but they are the difference between a dataset a scholar can trust and one she must re-check entirely.

*Normalization* is a different operation: deciding *how to represent* what the text says. Ancient texts vary wildly in spelling; manuscripts abbreviate; early printed editions normalized silently. Modern practice records both layers — the original form and the regularized form — explicitly, using markup that keeps the two apart (TEI's `orig` and `reg` elements, Week 6's subject). A normalization *rule set* is written down, so the next person can apply, audit, or dispute it.

Notice the FAIR logic humming under both: measured quality (reconciliation reports) and explicit, documented transformations (normalization rules) are what make the text *reusable* — a stranger knows exactly what was done to the raw evidence, and can undo it.

**Vocabulary.** *Consensus text* — the agreed text built from independent transcriptions. *Character/word error rate* — the measured proportion of wrong characters/words against ground truth. *Regularization* — representing variant spelling in a standard form, recorded separately from the original.

**Takeaway:** Reconciliation measures trustworthiness; documented normalization makes transformations explicit — together they keep the text honest and reversible.

---

## **15 Content**

**Stage 5: Collation and Textual Criticism**

When a work survives in multiple manuscripts, the witnesses' texts differ: scribes misread, skipped lines, "corrected" from memory, or deliberately revised. *Collation* is the systematic comparison of the witnesses' texts, variant by variant; its product is the *apparatus*. *Textual criticism* is the reasoning performed on that comparison — classifying the witnesses, detecting the scribes' error patterns, and where warranted, reconstructing the earliest recoverable text.

Digital tools changed this stage's economics. CollateX aligns multiple transcriptions computationally and outputs the variant positions as data; visualization tools (like the Versioning Machine) display variants side by side. A collation that took a summer by hand can be re-run in seconds whenever a transcription improves — because the transcriptions are plain text in a repository, the whole comparison is *repeatable*, and the apparatus becomes a living dataset instead of a frozen print product.

For your project, this stage explains *why* your passage choice matters: a passage with interesting variant transmission is one where collation has something to say. When you choose a passage on Friday, you are choosing the evidence for Weeks 7–8.

**Vocabulary.** *Collation* — systematic comparison of witness texts to identify variants. *Variant* — a place where witnesses differ. *Recension* — a reconstructable branch of a text's transmission history.

**Takeaway:** Collation compares witnesses and generates the apparatus as reusable data; your passage choice determines what this stage will have to work with.

---

## **16 Content**

**Stage 6: Linguistic Markup — Morphology, Lemmas, Syntax**

Once the text is stable, the linguistic analysis begins. *Morphological tagging* assigns each word its grammatical analysis — part of speech, person, number, tense. *Lemmatization* links each word form to its dictionary headword, so that all inflected forms of one word can be found together. Syntax tagging goes further and records phrase structure. With these layers added, questions that classical scholarship previously answered by memory and card catalogs become queries: find every future indicative after a conditional particle, across a whole corpus, in seconds.

Open tools do the first pass: CLTK (the Classical Language Toolkit) provides tokenizers, taggers, and lemmatizers for Greek and Latin; treebanks like Perseus' Ancient Greek Dependency Treebank provide hand-corrected exemplars. But — the recurring lesson — machine output is a draft. Tagging errors compound silently, so scholarly practice keeps the human in the loop, correcting and validating. Modules 9–11 of this course cover lemmatization, alignment, and consolidation, each with the manual-deterministic-AI cycle.

For FAIR, linguistic layers are interoperability cashed out: tagsets follow shared schemes (like Universal Dependencies), so a lemmatized corpus can be searched by the same tools regardless of who produced it.

**Vocabulary.** *Morphological tagging* — labeling each word's grammatical properties. *Lemma* — the dictionary headword form of an inflected word. *CLTK* — the Classical Language Toolkit, open-source NLP for ancient languages.

**Takeaway:** Linguistic markup turns a readable text into a queryable dataset — machine-tagged first, human-verified always, using shared tagsets.

---

## **17 Content**

**Stage 7: Translation and Annotation**

Translation in a digital edition is not an appendix; it is an alignment problem. Tools like the Alpheios Translation Alignment Editor let editors link each phrase of the translation to the phrase of the original it renders. The aligned translation then becomes data: a reader can click a Greek phrase to see the English; a researcher can study *how* a translator handled a construction across a whole work. Ugarit and similar platforms treat alignment quality itself as an object of study.

*Annotation* is the broader art of attaching interpretive notes to the text — identifying people and places, explaining allusions, marking quotations. Digital annotation platforms (Recogito for places, CATMA for interpretive tagging) make annotations shared and structured instead of locked in a commentator's head, and they distinguish clearly between the *text*, which is evidence, and the *annotations*, which are arguments about the evidence. That distinction is FAIR thinking applied to interpretation: the layers stay separable so future readers can accept, reject, or extend each independently.

Your edition will include a translation and commentary layer in the final modules (12–13), built by exactly this method — aligned, tagged, and kept distinct from the transcript of the manuscript itself.

**Vocabulary.** *Translation alignment* — explicit word- or phrase-level links between original and translation. *Annotation layer* — interpretive notes stored separately from the transcribed text. *Recogito / CATMA* — open annotation platforms.

**Takeaway:** Translations and notes become structured, separable layers — interpretation preserved as reusable data, never merged into the evidence.

---

## **18 Content**

**Stage 8: Presentation and Publication**

The final stage turns the data stack into something humans read: a web page, a print PDF, an API. The crucial principle is *separation of data from presentation* — the same TEI file can render as a reading website (via TEI Publisher or CETEIcean), a print-ready PDF, or a machine interface, without editing the file itself. Publications also export and archive: stable identifiers and institutional repositories (or GitHub, with archived releases) keep the edition addressable after the project website's funding ends.

This stage is where all five FAIR letters are audited. Is the edition findable — does it have a DOI or equivalent? Accessible — does it work without special software? Interoperable — can its data be exported in standard TEI? Reusable — is the license stated, the method documented, the code archived? A beautiful website that fails these is a poster, not an edition.

The Publication module (13) has you assemble your term's work into exactly this package. The syllabus's final deliverable — the Digital Edition Portfolio in the December exam period — is your presentation layer, built on thirteen weeks of data that were designed to survive presentation.

**Vocabulary.** *Separation of data and presentation* — storing content as data so multiple renderings are possible. *TEI Publisher* — an open platform for publishing TEI documents to the web. *DOI* — a persistent identifier for scholarly objects.

**Takeaway:** Presentation renders the data stack for humans — and a real edition passes the FAIR audit at the moment of publication.

---

## **19 Content**

**The Workflow Is Your Semester**

Look at the schedule with the workflow in mind and the course stops being a list of topics. Cataloguing (Module 2, Week 2). Images and IIIF (Module 3, Week 3). Transcription (Module 4, Week 4). Reconciliation (Module 5, Week 5). Normalization (Module 6, Week 6). Collation (Module 7, Week 7). Apparatus/textual criticism (Module 8, Week 8). Lemmatization (Module 9, Week 9). Consolidation, alignment (Modules 10–11, Weeks 10–11). Commentary (Module 12, Week 12). Publication (Module 13, Week 13).

Each module also runs the same *method* on its stage: Tuesday you do the stage by hand, Wednesday a deterministic script does it, Friday you compare an AI-assisted version against both — the three-step comparative cycle that begins in Week 2. The workflow gives the "what"; the cycle gives the "how," and it exists so that you personally experience what each tool adds and fails at.

This is why the FAIR principles and the workflow belong in Orientation, before any tool training. Every command you learn this term is serving a named stage and a named principle. When a tool frustrates you — and one will — you will be able to ask whether it failed *you*, or whether it is genuinely hard, by comparing notes against the workflow.

**Vocabulary.** *Three-step comparative cycle* — manual baseline, deterministic tool, AI-assisted pass, compared each week. *Orientation* — Weeks 1's setup of concepts, tools, and accounts before the cycle begins.

**Takeaway:** Modules 2–13 walk the standard edition workflow in order, each stage practiced manual → deterministic → AI-assisted.

---

## **20 Content**

**Tool: Editing and Validating XML in VS Code**

In this course, we use **Visual Studio Code (VS Code)** rather than proprietary commercial suites to edit all text and XML files. Installing an XML extension (such as the standard Red Hat XML extension or Scholarly XML) equips VS Code with professional-grade XML capabilities: real-time schema validation (against RELAX NG, W3C XML Schema, or DTDs), tag autocompletion, syntax checking, and inline error highlighting right as you type.

Why this matters: XML is strict. A mistyped tag or an element in the wrong place makes the file unusable to downstream parsers. Real-time validation in VS Code catches syntax defects immediately, as red squiggles and diagnostic warnings in your editor panel, before broken markup ever reaches your Git repository or publication pipeline.

In Week 2 you will hand-write a TEI header in a bare text editor on Tuesday, then enable schema validation in VS Code on Wednesday to audit it against the official TEI schema. The errors flagged in VS Code are the lesson: they show you exactly what a schema *is* — a formal, machine-readable contract of your project's editorial standards.

**Vocabulary.** *Schema validation* — checking an XML file against a formal specification of legal structure. *TEI schema* — the rulebook defining legal TEI elements and their arrangement. *XML extension* — an editor add-on that brings language server validation and autocomplete into VS Code.

**Takeaway:** VS Code with an XML extension validates your markup in real time — interoperability enforced at typing time, without requiring proprietary editors.

---

## **21 Content**

**Tool: VS Code as the Unified Scholarly Workbench**

Using VS Code for both plain text and XML keeps our toolkit unified and portable. Rather than dividing labor across multiple separate applications with proprietary licensing barriers, your entire digital scholarly workflow runs inside a single, free, cross-platform environment: editing plain text notes, authoring TEI XML editions, running Python scripts, querying AI assistants, and managing Git version control.

Three VS Code practices to establish now, in Orientation, before Module 2 begins. *One project, one repository*: keep all course files for your edition inside a single Git-tracked folder, so every file's history is recorded in one place. *Commit at checkpoints*: end each work session with a commit whose message says what stage you were working on ("Lesson 1.2: chose passage, recorded shelfmark") — Huskey (2024) calls this the research journal, and your future self will read it that way. *Plain text always*: no file in this course should ever need a proprietary program to open.

There is no shortage of tools in this field; the keynote counted dozens at every workflow stage. The course's deliberate choice is a *minimal* stable toolkit — VS Code, Git, GitHub, Transkribus, Zotero — so that your energy goes into the scholarship and the method, not into relearning interfaces every month.

**Vocabulary.** *Repository (repo)* — the Git-tracked folder containing a project and its complete history. *Minimal toolkit* — a deliberately small, stable set of tools mastered deeply. *Research journal* — using commit messages to record scholarly decisions as they happen.

**Takeaway:** VS Code unifies plain text, XML validation, Git, and Python into a single open workbench — eliminating tool fragmentation and software bloat.

---

## **22 Content**

**Accounts to Create This Week**

The workflow is operated through free online platforms, and every student needs accounts on four of them before Week 2. Create each with your StFX email, using a strong password and a password manager rather than reusing passwords.

*GitHub* (github.com) hosts Git repositories online: it is the backup, sharing, and collaboration layer over local Git. GitHub also gives education accounts extra private-repository features. *Transkribus* (transkribus.eu) is the HTR platform for Module 4: you will upload manuscript images, transcribe ground truth, and train a recognition model on your own hand. *Zotero* (zotero.org) manages bibliographic data and exports it in open formats — the FAIR way to handle your bibliography, integrated with Word and browsers. *THREAD / Perseids* — the THREAD project's documentation (github.com/THREAD-project) is the open toolkit this course draws on; an account lets you explore the integration sites used in later modules.

Two principles for choosing accounts, both from the FAIR discussion. Prefer platforms that *export* your data in open formats — platforms you can leave. And treat the account itself as part of your scholarly identity: the same username across GitHub and Zotero, attached to real work, becomes your provenance trail — the record that *you* produced *this* transcription on *this* date.

**Vocabulary.** *GitHub* — the online hosting service for Git repositories. *Transkribus* — the HTR training and transcription platform used in Module 4. *Zotero* — open-source reference management with open export formats.

**Takeaway:** Create GitHub, Transkribus, and Zotero accounts (plus THREAD documentation access) with your StFX email — each platform maps to a workflow stage you will use this term.

---

## **23 Content**

**Why the Platforms Themselves Must Be FAIR**

It is worth noticing that the platforms you just signed up for are themselves subject to the principles they serve. GitHub is useful to scholarship *because* your repository is exportable — the entire history, as plain files, clones to any machine. Zotero is useful *because* it exports open bibliographic formats instead of locking your library in a database. Transkribus is more guarded — trained models and processing time sit behind its accounts — which is precisely why this course also has you keep your ground truth and corrections in your own repository, in your own hands.

This is the practical skill the FAIR framework trains: reading a tool not just as a convenience but as a *data custody decision*. Where does my data live? In what format? Can I get it out, with its history intact? Who else can access it, under what terms? A tool that answers those questions well composes with the rest of the FAIR stack; a tool that answers badly becomes a lock on your own research.

You will meet this decision repeatedly: choosing an image host, a publication platform, an annotation service. The workflow stage changes; the questions do not. Ask them every time, and you will not wake up in April with a term's work trapped in a service you cannot export.

**Vocabulary.** *Data custody* — the question of where data lives and under whose control. *Export path* — the mechanism by which your data leaves a platform. *Vendor lock-in* — dependence on a service that does not let your data leave.

**Takeaway:** Evaluate every platform as a custody decision — open formats and real export paths are what keep your research yours.

---

## **24 Content**

**Case Study: Machine Recognition of Greek Editions**

To see the workflow's current frontier, consider a 2026 study by Angleraud, Karamolegkou, Sagot, and Clérice on structure-aware text recognition for ancient Greek critical editions. The problem: printed critical editions are dense two-dimensional objects — text interleaved with apparatus footnotes, corner brackets marking lemma citations, abbreviations everywhere — and standard OCR, which assumes plain flowing text, destroys exactly that structure. Their system trains a model to recognize not just the letters but the *layout roles*: which region is running text, which is apparatus, where a lemma begins.

Read it against this lesson and it is the whole workflow in miniature. It presupposes findable, accessible inputs (scanned editions). Its center is transcription, machine-accelerated but evaluated against human-checked ground truth — error rates again. Its output is structured data (the apparatus as data, not typography), which is interoperability: once the apparatus is data, it can be collated, searched, and republished. The paper is also FAIR practice in itself: it documents method and releases code so others can reuse the approach.

The frontier moves — this study is 2026, your course materials will age — but the *shape* of the work is stable: identify the structure, get the evidence into plain data, measure against ground truth, publish openly. That shape is what you are learning.

**Vocabulary.** *OCR / HTR* — optical/handwritten text recognition. *Structure-aware recognition* — models trained to recover layout roles, not just characters. *Apparatus as data* — variant information extracted into machine-usable form.

**Takeaway:** Current research automates the edition workflow stage by stage — but every advance is measured against human ground truth and published as open, structured data.

---

## **25 Content**

**Machine Learning and Philological Judgment**

A caution that the readings (Cowen-Breen et al. 2023) press directly: machine learning in philology is powerful *statistical pattern-matching*, not understanding. A language model that "reads" Greek has never seen a manuscript, cares nothing for scribal habits, and will produce fluent nonsense with the same confidence as truth. The studies that introduced ML into philology showed genuine gains — in OCR correction, in lemmatizing difficult forms — and equally showed that the gains evaporate without human evaluation.

The three-step cycle this course runs every week is the practical answer. Tuesday's manual work is your ground truth: slow, effortful, but * yours*, and authoritative for your passage. Wednesday's deterministic script does exactly what it is told — no intelligence, but perfect repeatability, which makes it auditable. Friday's AI pass is fast and occasionally brilliant, and worthless until compared. The comparison is the scholarship. A scholar who only runs the AI pass has not outsourced work; they have abandoned the evidence for a plausible imitation of it.

Hold this position through the semester: automation changes *where* your effort goes — from mechanical transcription toward judgment, verification, and design of checks — not *whether* judgment is required. The workflow stages that looked clerical (double-keying, error rates) turn out to be exactly where scholarship lives.

**Vocabulary.** *Statistical pattern matching* — predicting likely output from training data, without understanding. *Deterministic tool* — software that always produces the same output from the same input. *Evaluation* — measuring machine output against ground truth.

**Takeaway:** AI assists every stage but is only trustworthy when measured against your manual ground truth — the comparison is the scholarship.

---

## **26 Content**

**Choosing Your Passage: The Criteria**

By the end of today you will choose the manuscript passage that every assignment this term builds on — catalogued in Week 2, imaged in Week 3, transcribed in Week 4, and so on through publication in Week 13. Choose with the workflow in mind, because you are choosing the raw material for thirteen weeks of work.

The criteria: *Size* — an entire full page (one complete folio recto or verso, or a complete epigraphic surface) of the textual artifact: substantial enough to contain complete page layout, ruling lines, margins, and scribal features, providing the codicological context needed across the whole term. *Image quality* — a high-resolution, well-lit, publicly accessible image (minimum 300 DPI or zoomable via IIIF). *Manageable apparatus* — some abbreviations or corrections to make transcription interesting, but not a page of impenetrable cursive ligatures for your first semester. *Ancient language* — Greek or another historical language you are studying or willing to work with via computational tools; the linguistic modules need real morphology. *Sustained interest* — you will study this page dozens of times; pick a textual artifact you genuinely care about.

Good sources of candidates: the manuscripts cited in this week's readings; digitized codices available in online IIIF collections (e.g., Digita Vaticana, British Library, CSNTM, Gallica); or an artifact connected to research in your other courses. Nothing needs to be final today beyond the page selection itself — the ungraded deadline exists so that every later week starts from a fixed, authoritative physical object.

**Vocabulary.** *Full-page witness* — an entire surviving manuscript folio page or epigraphic surface chosen as the physical object for an edition. *Ligature* — two or more letters written joined in a single stroke. *IIIF collection* — a library's online gallery of IIIF-served manuscript images.

**Takeaway:** Choose one complete full page (folio recto or verso) with a high-resolution public image, manageable scribal difficulty, and a language you will enjoy working in.

---

## **27 Content**

**Verifying Your Choice Before Committing**

Before you commit (in both senses) to a passage, run five checks — ten minutes now saves a stranded project in October.

1. *Image exists and is legible.* Find the actual page image online. Zoom to 100%: can you read every line? If the library's viewer is the only access, confirm it allows study use.
2. *Identity is established.* Can you find the manuscript in a catalog (Pinakes, LDAB, Papyri.info, or the library's catalog)? You will need its shelfmark and basic description for Week 2's TEI header. If no catalog record exists, the passage is still possible but Week 2 becomes harder.
3. *Text is identifiable.* Do you know (or can you determine) what text the passage contains? A published edition or translation to compare against makes every later stage easier.
4. *The passage is self-contained.* It should start and end at natural boundaries — not stop mid-word at the image's edge.
5. *You can name its difficulty.* In one sentence, what will be hard here — the script, the abbreviations, the damage? Naming it now is the beginning of your documentation.

Record the results of all five checks; they become the first entries in your project's documentation.

**Vocabulary.** *Shelfmark verification* — confirming the manuscript's exact catalog identity. *Self-contained passage* — text with natural start and end points within the surviving image.

**Takeaway:** Five checks — image, identity, text, boundaries, difficulty — turn a candidate passage into a defensible project choice.

---

## **28 Content**

**Recording the Choice in the Repository**

Now the Lesson 1.1 machinery earns its keep. Your passage choice becomes a file — `README.md` in your course repository — containing: the manuscript's shelfmark and catalog identifier; the passage's location (folio and line numbers); the text it contains; the IIIF or web address of the image(s); and one sentence on the passage's expected difficulty. This small file is the seed of the TEI header you will write in Week 2 and the provenance record your whole project will stand on.

Then commit it. In VS Code: stage the file, write a commit message like "Choose full-page witness: Vat. gr. 2121 f. 213r (Gen 1:1–14)" — specific enough that December-you knows exactly what happened — and commit. Push if you have GitHub set up. You have just performed the workflow's first FAIR act: the choice is findable (in your repo), documented (the file), and timestamped with attribution (the commit). Huskey's "research journal" begins exactly here.

The deadline is Friday, September 4 — today. The choice is ungraded, but as the schedule says, every later assignment builds on it. If you are torn between two manuscript pages, commit the README for your primary choice and note the runner-up in the same file; you can note what would have changed, and the decision is at least recorded rather than drifting.

**Vocabulary.** *README* — the standard first file of a repository, explaining what the project is. *Commit message* — the Git record of what changed and why. *Seed metadata* — the small initial record that later, fuller documentation grows from.

**Takeaway:** Write the full-page witness's identity, location, image URL, and difficulty in a committed README.md — your project's first FAIR artifact is born today.

---

## **29 Content**

**Complete Setup Checklist**

By Sunday, every item on this list should be true. Check them off literally — this section is your checklist.

**Software (from Wednesday):** VS Code installed; Git installed and configured with your name and email (`git config --global user.name`, `user.email`); a course repository folder created and initialized with `git init`.

**Accounts:** GitHub (StFX email; education benefits requested); Transkribus basic account; Zotero account with browser connector; THREAD project documentation bookmarked.

**Passage:** chosen per the criteria in section 26; verified per the five checks in section 27; recorded in `README.md`; committed with a specific message; pushed to GitHub.

**Reading:** Finney, "Manuscript Markup" and Griffitts §3.4.1, plus TEI Guidelines vi.2, are the Week 1 readings — skim before Monday; Week 2's assignments assume them.

**In the lab:** confirm VS Code with an XML extension is installed and operational on your laptop or lab machine — Week 2's Wednesday validation pass relies on it, and it is better to discover configuration problems now than during class.

None of this is deep work; all of it is *unblocking* work. Every minute spent now is not spent during Module 4 wondering why Transkribus won't accept your upload.

**Vocabulary.** *Setup debt* — postponed configuration work that later blocks real work. *Onboarding* — the complete process of becoming operational on a project's tools.

**Takeaway:** Software, accounts, passage, commit, push, readings, lab access — the full checklist, cleared now, keeps Week 2 about scholarship instead of setup.

---

## **30 Content**

**Synthesis: Principles, Pipeline, and Your Project**

Two frameworks and one decision — that was today. The FAIR principles (Findable, Accessible, Interoperable, Reusable) are the *values*: what separates community infrastructure from a private folder. The eight-stage workflow — cataloguing, images, transcription, reconciliation and normalization, collation, linguistic markup, translation and annotation, presentation — is the *practice*: how the field actually edits ancient documents, and the exact path your modules 2–13 will follow. And your chosen passage is the *object*: the manuscript evidence that will travel through every stage, in your hands, for thirteen weeks.

The connection between the frameworks is the deep fact of this course. FAIR is not a compliance exercise attached to the workflow; it is what makes the workflow *cumulative* — each stage's output usable as the next stage's input, and each scholar's contribution reusable by the next scholar. Your README commit today and your published edition in December are the same act at two scales: evidence, documented, committed, dated, and open to the reader who comes after you.

**Due today, Friday September 4.** Your passage, chosen and verified, recorded in a committed `README.md`.

**Next week.** Module 2 begins the cycle: Tuesday, hand-write your passage's TEI header; Wednesday, validate it against the TEI schema in VS Code and build RDF triples from it; Friday, compare an AI-enriched version against your own. Bring your passage's catalog information.

**Takeaway:** FAIR supplies the values, the eight-stage workflow supplies the practice, and your passage gives them an object — the course is their meeting.

---

## References

Angleraud, N., Karamolegkou, A., Sagot, B., & Clérice, T. (2026).
*Structure-aware text recognition for ancient Greek critical editions* (arXiv:
2603.02803v3). Inria.

Boschetti, F. (2010). Analytical developments for the Homer Multitext:
Palaeography, orthography, morphology. In *Improving OCR accuracy for classical
critical editions*.

Cowen-Breen, C., Brooks, C., Graziosi, B., & Haubold, J. (2023). Machine
learning and the future of philology: A case study. *Transactions of the American
Philological Association, 153*(1), 253–284.

Gabler, H. W. (2010). Theorizing the digital scholarly edition. *Literature
Compass, 7*(2), 43–56.

Haaf, S., Gius, E., & Würbach, S. (2019). Measuring correctness of double-keying.
*Digital Humanities Quarterly*.

Huskey, S. J. (2024). Committing to reproducibility and explainability: Using
Git as a research journal. *International Journal of Digital Humanities, 6*,
9–21. https://doi.org/10.1007/s42803-023-00076-9

Penner, K. M. (2022, May 2). *A toolkit for humanities research and editing
ancient documents* [Keynote address]. DHSI-East, virtual.

Robinson, P. (2010). Current issues in making digital editions of medieval
texts — or, do electronic scholarly editions end? In M. Driscoll & E. S. Edward
(Eds.), *New directions in medieval manuscript studies*.

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange* (Version 4.12.0). https://tei-c.org/guidelines/p5/

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M.,
Baak, A., Blomberg, N., et al. (2016). The FAIR Guiding Principles for
scientific data management and stewardship. *Scientific Data, 3*, 160018.
https://doi.org/10.1038/sdata.2016.18
