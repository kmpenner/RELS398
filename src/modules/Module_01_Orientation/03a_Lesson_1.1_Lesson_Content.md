# Lesson 1.1 — The Digital Scholar's Workbench: Plain Text, Git, XML, and AI

*RELS 398 / ENGL 398 · Topic 1: Orientation · Meeting #1 (Wed Sep 2)*

*Orientation week — the three-step comparative cycle does not yet apply. This meeting establishes the foundational computational mindset, file formats, and software tools that you will use throughout the semester.*

---

## **01 Content**

**Moving from Word Processors to the Digital Workbench**

Welcome to the digital scriptorium. If you have written essays for university courses, you have almost certainly used software like Microsoft Word, Google Docs, or Apple Pages. These tools are designed around a simple, visual metaphor: a virtual sheet of 8.5 x 11-inch white paper upon which you arrange paragraphs, apply bold fonts, and adjust margins. For printing an essay or submitting a PDF, word processors are wonderful tools.

However, when our goal is to study historical documents computationally—to search across thousands of medieval manuscripts, to compare fifty variants of an ancient poem, or to publish an interactive digital edition on the web—traditional word processors fail us. Word processors are designed for *human eyes looking at printed pages*, not for *computer programs analyzing textual data*. 

In this course, we step behind the curtain of consumer software. You will learn to treat texts not merely as formatted documents, but as structured, living datasets. To do this, we replace the word processor with a **digital workbench**: a suite of transparent, open tools designed to give you total control over every character, word, and metadata tag in your scholarship.

**Vocabulary.** *Digital Humanities (DH)* — an interdisciplinary field that applies computational methods and tools to humanities research, teaching, and preservation. *Word Processor* — software designed for typing, formatting, and printing human-readable documents on simulated pages. *Data Transparency* — the degree to which a file format allows direct inspection and manipulation of its underlying raw data.

**Takeaway:** Traditional word processors are built for printing visual pages; digital scholarship requires a digital workbench where texts can be analyzed, searched, and transformed as computational data.

---

## **02 Content**

**What is Plain Text? (And Why .docx Hides Your Data)**

To understand why digital scholars work differently, consider what happens when you save a one-sentence document in Microsoft Word. If you type the word "Hello" and save it as `document.docx`, the resulting file on your hard drive is not five bytes of text. It is actually a zipped archive containing dozens of internal XML files, styling rules, font specifications, printing margins, and metadata tracking who created the file and when. 

If you try to open a `.docx` file in a simple programming script, the computer sees a scrambled wall of compressed binary code. The text you wrote is trapped inside proprietary formatting wrappers. If Microsoft Word were to disappear tomorrow, opening and reading those complex formatting structures would require specialized software.

**Plain text**, by contrast, is the universal lingua franca of computing. A plain text file (such as `.txt`, `.md`, or `.xml`) contains *only the exact characters you typed*—letters, numbers, spaces, and line breaks—with zero hidden binary formatting. A five-letter word in a plain text file takes up exactly five bytes of storage. Plain text created today will still be easily readable on any computer fifty or one hundred years from now. In computational philology, plain text is our bedrock of durability and transparency.

**Vocabulary.** *Plain Text* — unformatted text containing only raw character codes, universally readable across all operating systems without specialized software. *Binary File* — a file format encoded in machine-readable binary code that requires specific software to interpret. *Proprietary Format* — a file structure owned and controlled by a private company.

**Takeaway:** Plain text contains only the raw characters you type with no hidden styling codes, making it permanent, universally readable, and accessible to computer analysis.

---

## **03 Content**

**Meet Your Workbench: The Visual Studio Code (VS Code) Editor**

Because plain text contains no built-in styling, we do not edit it with a word processor. Instead, we use a specialized tool called a **code editor** or **text workbench**. In this course, our primary workbench is **Visual Studio Code** (commonly known as **VS Code**).

When you first open VS Code, it might look intimidating because it lacks the familiar toolbar of Microsoft Word (you will not find buttons to change text to Comic Sans or make margins 1.5 inches). Instead, VS Code provides tools built specifically for working with structured text and code:

- **Line Numbers:** Every line in your document is numbered along the left margin, allowing you to cite and locate specific passages instantly.
- **Syntax Highlighting:** When editing structured formats like XML or Python, VS Code automatically colors different components (tags in blue, text in white, attributes in orange), making structural errors jump out visually.
- **Integrated Terminal:** A built-in command prompt at the bottom of the screen where you can run scripts and version control commands without leaving your editor.
- **Extensibility:** Specialized plugins for historical languages (such as ancient Greek or Hebrew font support), XML schema validators, and Git tracking.

VS Code does not alter the underlying bytes of your files. What you see on screen is the literal reality of the data stored on your computer.

**Vocabulary.** *Code Editor* — a text editing program designed specifically for writing and editing plain text, markup, and computer programming languages. *Syntax Highlighting* — a feature that displays source code and markup in distinct colors and fonts according to their category. *Integrated Development Environment (IDE)* — a comprehensive software suite combining an editor, terminal, and debugging tools.

**Takeaway:** VS Code is our primary digital workbench, providing line numbers, syntax highlighting, and an integrated terminal to view and edit text files with complete precision.

---

## **04 Content**

**Files, Folders, and File Extensions (.txt, .md, .xml, .py)**

On modern smartphones and tablets, operating systems hide the file system: apps save data into mysterious cloud silos, and users rarely see where a document physically lives. In digital scholarship, however, you must be the master of your file system. You need to know exactly which folder a document lives in and what kind of data it contains.

A file's identity is signaled by its **file extension**—the letters following the final period in its filename:

- `.txt` *(Plain Text):* Pure, unadorned text without any special formatting or tags.
- `.md` *(Markdown):* Lightweight plain text that uses simple punctuation symbols for formatting (e.g., `# Header`, `**bold**`, `*italics*`, `- list item`). We use Markdown for taking notes, writing documentation, and drafting lesson content.
- `.xml` *(Extensible Markup Language):* Plain text structured into hierarchical tags (e.g., `<title>Odyssey</title>`), which we use for digital editions and Moodle question banks.
- `.py` *(Python Script):* Plain text containing instructions written in the Python programming language that your computer can execute.

In this course, everything we build is stored in clean, well-organized folder trees where filenames are descriptive, lower-case or snake_case, and free of spaces (e.g., `lesson_01_notes.md` rather than `My Notes For Class (1) final.md`).

**Vocabulary.** *File Extension* — a suffix at the end of a computer file name indicating its format and encoding. *Markdown (.md)* — a lightweight markup language with plain-text formatting syntax designed to be converted to HTML. *Directory Tree* — the hierarchical organization of folders and subfolders on a computer storage device.

**Takeaway:** File extensions (.txt, .md, .xml, .py) tell the computer how to interpret plain text data, and maintaining organized directory structures is essential for digital scholarship.

---

## **05 Content**

**The Command Line: Talking Directly to Your Operating System**

For most computer users, interacting with software happens through a **Graphical User Interface (GUI)**: clicking icons with a mouse, dragging files into windows, and tapping buttons. While GUIs are friendly, they limit you to doing only what the software developer anticipated. If you need to rename 500 image files at once or search 50 XML documents for a Greek keyword, clicking 500 times by hand is exhausting.

The **Command Line Interface (CLI)**, also known as the **Terminal** or **Shell**, allows you to talk directly to your computer's operating system by typing short, precise text commands. Instead of clicking on a folder icon, you type `cd projects/RELS` to change directories; instead of right-clicking to see what files exist, you type `ls` (on Linux/Mac) or `dir` (on Windows) to list files.

The terminal is not a relic of 1970s computing; it is the most powerful, reproducible tool in the modern digital humanist's toolkit. When you run a task in the terminal, you can record the exact command in your research notes, allowing any other scholar in the world to re-run that exact command and get the identical result.

**Vocabulary.** *Command Line Interface (CLI)* — a text-based interface used to run programs, manage files, and interact with the operating system. *Graphical User Interface (GUI)* — a visual interface based on windows, icons, and menus. *Terminal / Shell* — the program that receives keyboard commands and passes them to the operating system.

**Takeaway:** The command line allows scholars to issue precise, scriptable, and reproducible text instructions directly to the computer, bypassing the limitations of point-and-click interfaces.

---

## **06 Content**

**Why Digital Humanities Projects Need Open, Transparent Tools**

Consider a tragedy common in academic history: a scholar spends ten years creating a digital catalogue of rare manuscripts using a proprietary commercial database software. Five years later, the software company goes out of business, the operating system updates, the software stops running, and the scholar's ten years of research are locked in an unreadable binary vault.

This phenomenon is known as **digital obsolescence** or **software rot**. To ensure that cultural heritage and historical scholarship endure for generations, the international Digital Humanities community adheres to a set of core principles:

1. **Open Standards:** Using non-proprietary, openly documented formats (like plain text, XML, and JSON) that belong to no single corporation.
2. **Open Source Software:** Using tools whose source code is publicly accessible, free to inspect, and maintainable by the academic community (such as VS Code, Git, and Python).
3. **Data Portability:** Ensuring that your research data can be moved effortlessly from one computer to another, from local drives to web servers, without loss of fidelity.

When you learn these open tools in RELS 398, you are not just learning software for a single semester; you are learning the durable foundation of open scholarly infrastructure.

**Vocabulary.** *Digital Obsolescence* — the situation where digital resources become inaccessible because the necessary hardware or software is no longer available. *Open Standard* — a publicly available specification with collaborative development that ensures interoperability. *Open Source* — software whose source code is released under a license allowing anyone to study, change, and distribute it.

**Takeaway:** Digital humanities relies on open standards and plain-text formats to prevent software obsolescence and guarantee that cultural research remains accessible for decades.

---

## **07 Content**

**The "Final_Final_v2" Trap: Why We Need Version Control**

Every student and writer has lived through the chaos of manual document versioning. You write an essay draft and save it as `Essay.docx`. Later, you make edits and save it as `Essay_v2.docx`. Your professor gives feedback, so you create `Essay_revised.docx`. The night before the deadline, you make late corrections and save `Essay_final.docx`, followed an hour later by `Essay_final_really_FINAL_v2.docx`.

This haphazard naming system creates serious scholarly problems:

- **Loss of Context:** Which file contains the paragraph you deleted yesterday? You have to open five files and compare them side by side.
- **Accidental Overwriting:** If you work on two different computers, you might accidentally copy an older file over a newer one, erasing days of research.
- **No Record of Rationale:** You see that a sentence was changed, but you have no memory of *why* you changed it—was it to fix a typo, or because a new source disproved your original argument?

When editing ancient manuscripts with multiple variant readings, this chaos is fatal. We need a system that tracks the complete evolution of a project cleanly, automatically, and permanently.

**Vocabulary.** *Version Control* — the management of changes to documents, computer programs, and other collections of information. *Rollback* — restoring a file or project to a previously saved state. *Diff* — a visual comparison showing the exact lines added, deleted, or modified between two versions of a document.

**Takeaway:** Saving multiple copies of files with names like "final_v2" causes confusion and lost work; version control solves this by tracking changes systematically within a single project history.

---

## **08 Content**

**What is Git? A Time Machine for Your Writing and Research**

**Git** is the world's standard version control system. Created in 2005 by Linus Torvalds, Git was built to coordinate work among thousands of software developers across the globe, but its core design makes it the ultimate tool for scholarly writers and digital editors.

Rather than making dozens of separate copies of your files, Git keeps all your files in a single folder called a **repository** (or "repo"). Whenever you reach a meaningful milestone in your work (e.g., you finished transcribing a folio, fixed five typos, or added a new bibliography entry), you ask Git to take a **snapshot** of the entire project. This snapshot is called a **commit**.

Think of Git as a video game checkpoint system or a historical time machine:

- Every commit records the exact state of all files at that precise second.
- Every commit records *who* made the change, *when* it was made, and a short message explaining *why*.
- You can travel back in time to inspect or restore any previous commit without losing any work created since.

**Vocabulary.** *Git* — a distributed version control system that tracks changes in files across time. *Repository (Repo)* — a directory containing your project files along with the complete, hidden history of all changes tracked by Git. *Commit* — a recorded snapshot of your project at a specific point in time, accompanied by a descriptive message.

**Takeaway:** Git acts as a project time machine, recording clean snapshots (commits) of your files with timestamps, author attribution, and explanations of why changes were made.

---

## **09 Content**

**Taking a Snapshot: The Three States (Edit -> Stage -> Commit)**

To understand how Git works in practice, you need to understand its **Three States**. Git does not automatically record every single keystroke you make (which would clutter your history with half-finished sentences). Instead, taking a snapshot is an intentional, three-step process:

1. **Working Directory (Editing):** This is your normal folder where you create, edit, and delete files using VS Code. When you save a file, the change exists on your hard drive, but Git has not recorded a formal snapshot yet.
2. **Staging Area (Preparing):** When you are ready to make a snapshot, you choose which specific files you want to include in the next commit using the command `git add <filename>`. Think of the staging area as a photographic studio: you arrange the exact files you want in the picture before snapping the camera.
3. **Repository (Committed Snapshot):** You execute `git commit -m "Your message"`. Git seals the snapshot permanently into the project's historical ledger.

This three-stage workflow gives you total control: you can edit four different files, but stage and commit only two of them if they represent a single, focused improvement.

**Vocabulary.** *Working Directory* — the local filesystem directory where you actively edit your project files. *Staging Area (Index)* — the intermediate holding zone where changes are gathered and formatted before being committed. *`git add`* — the command that moves changes from the working directory to the staging area. *`git commit`* — the command that permanently saves staged changes as a new historical snapshot.

**Takeaway:** Git's three-step workflow (Edit in Working Directory $\rightarrow$ Stage with `git add` $\rightarrow$ Commit with `git commit`) ensures that every snapshot is an intentional, curated record of progress.

---

## **10 Content**

**Writing Good Commit Messages: Leaving Breadcrumbs for Your Future Self**

When you create a commit, Git requires you to write a **commit message**. The commit message is the scholarly justification for why that snapshot exists.

A bad commit message tells the reader nothing:

- ❌ `"changes"`
- ❌ `"stuff"`
- ❌ `"fixed it"`
- ❌ `"asdfasdf"`

If you look back at your project six weeks later, those messages give you no clue which commit fixed an error in line 45 or why a paragraph was rephrased. 

A good commit message is concise, informative, and states the *reason* for the edit:

- ✅ `"Fix transcription error in Odyssey line 12: change alpha to omicron based on London papyrus"`
- ✅ `"Add bibliography entry for Romanello (2024) metadata extraction study"`
- ✅ `"Correct closing XML tags in Module 02 quiz questions"`

Writing clear commit messages is not a bureaucratic chore; it is the discipline of leaving breadcrumbs for your future self and your academic collaborators.

**Vocabulary.** *Commit Message* — the human-readable text explanation attached to every Git commit describing the purpose and rationale of the change. *Conventional Commits* — a standardized format for structuring commit message titles (e.g., `feat:`, `fix:`, `docs:`).

**Takeaway:** Good commit messages clearly explain the reason for an edit, turning your Git log into an intelligible, step-by-step history of your scholarly research.

---

## **11 Content**

**Checking Your Project History: Reading the Git Log**

Once you have made several commits, Git holds a complete, immutable ledger of your project's history. To inspect this history, you open your terminal and type the command:
```bash
git log
```

When you run `git log`, Git displays a list of your commits in reverse chronological order (newest on top). For each commit, you will see:

1. **Commit Hash (ID):** A unique identifier (e.g., `736dbb0...`) that names that exact snapshot.
2. **Author:** The name and email address of the scholar who made the change.
3. **Date and Time:** The exact timestamp when the snapshot was committed.
4. **Commit Message:** The explanation written by the author.

By viewing this log, you can reconstruct the complete story of your edition. If you want to see a condensed, one-line summary of recent history, you can type `git log --oneline`, which displays a clean timeline of your project's milestones.

**Vocabulary.** *`git log`* — the command that lists the chronological history of commits in a repository. *Commit Hash / SHA* — a unique alphanumeric fingerprint that identifies a specific commit. *Provenance* — the chronological record of the ownership, custody, and modification history of a historical artifact or digital file.

**Takeaway:** Running `git log` displays the chronological timeline of your project, showing who changed what, when it occurred, and the rationale behind every milestone.

---

## **12 Content**

**Undoing Mistakes Safely Without Panic**

One of the greatest fears for students working with computers is making a catastrophic mistake: accidentally deleting three pages of text, overwriting a file with junk, or breaking formatting so badly that nothing works. In a normal word processor, pressing Ctrl+Z a few times might help, but if you close the program, those undo steps vanish forever.

In Git, **you never need to panic**. Because every commit is a permanent snapshot, you can easily discard experimental mistakes and restore your files to the exact state of your last commit with a single command:
```bash
git restore <filename>
```

If you made changes to a file that didn't work out, `git restore` wipes away the unstaged edits and reloads the pristine version from your last commit. If you want to see what changes you made before deciding to keep or discard them, you type `git diff`, which displays every added word in green and every deleted word in red. Git gives you total psychological freedom to experiment boldly, knowing a safety net is always in place.

**Vocabulary.** *`git restore`* — the command that discards uncommitted changes in your working directory and restores the file from the repository. *`git diff`* — the command that displays the line-by-line differences between your current working file and your last commit. *Safety Net* — the version control guarantee that committed work cannot be accidentally deleted or overwritten.

**Takeaway:** Git eliminates the fear of making mistakes by allowing you to inspect changes with `git diff` and instantly restore previous clean states with `git restore`.

---

## **13 Content**

**Cloud Sharing: What is GitHub vs. Local Git?**

A common point of confusion for beginners is the difference between **Git** and **GitHub**:

- **Git** is the *local software tool* running on your own laptop that creates snapshots, tracks history, and manages files on your hard drive. Git does not require an internet connection; you can commit changes while sitting on an airplane or in a cabin in the woods.
- **GitHub** is a *cloud-based hosting service* (owned by Microsoft) that stores copies of Git repositories on the internet. GitHub allows scholars across the world to share repositories, collaborate on digital editions, report issues, and publish web pages.

Think of Git as your local camera, and GitHub as an online photo album where you upload copies of your pictures to share with colleagues. When you want to send your local commits up to GitHub, you use the command `git push`. When you want to download updates that a collaborator pushed to GitHub down to your laptop, you use the command `git pull`.

**Vocabulary.** *GitHub* — a web-based hosting platform for Git repositories offering collaboration tools, code review, and project management. *`git push`* — the command that uploads local repository commits to a remote server like GitHub. *`git pull`* — the command that downloads and integrates remote changes into your local repository. *Remote Repository* — a version of your project hosted on the internet or network.

**Takeaway:** Git is the local program tracking changes on your computer; GitHub is the online platform where repositories are backed up, shared, and collaborated on globally.

---

## **14 Content**

**How Computers Read: Strings of Characters**

Before we explore how to mark up historical documents, we must pause and consider how a computer "thinks" about language. When a human reads the word *"Homer"*, our brain instantly retrieves rich semantic associations: ancient Greece, epic poetry, the Trojan War, blindness, and hexameter verse.

To a computer, however, the word *"Homer"* is merely a sequence (a **string**) of five abstract numerical character codes:

- `'H'` (Unicode value 72)
- `'o'` (Unicode value 111)
- `'m'` (Unicode value 109)
- `'e'` (Unicode value 101)
- `'r'` (Unicode value 114)

The computer possesses zero inherent understanding that "Homer" is an author, that the text is Greek literature, or that the sentence is a question. If we want a computer program to search for all personal names in an ancient text, or to distinguish a spoken dialogue from narrator commentary, we must provide explicit structural cues that the computer can parse.

**Vocabulary.** *String* — a sequence of characters (letters, numbers, punctuation, and spaces) treated as a fundamental data type in computer programming. *Character Encoding* — a system that pairs each character in a language with a specific numerical code (e.g., ASCII, Unicode). *Semantic Meaning* — the human understanding, context, and significance conveyed by words.

**Takeaway:** Computers process text as dumb strings of numerical character codes; to make historical texts computable, human scholars must add explicit structural and semantic markers.

---

## **15 Content**

**What is Markup? Putting Labels on Human Language**

The word **markup** comes from traditional print publishing. Before computers, an editor would take an author's handwritten manuscript and literally "mark it up" in the margins with blue pencil, writing instructions to the typesetter: *"Set this in 14pt italics," "Indent this paragraph,"* or *"Insert footnote here."*

In digital humanities, **digital markup** serves a similar purpose, but with a crucial difference: instead of only giving *visual formatting* instructions (like "make this bold"), digital markup gives *semantic and structural* meaning to the text.

Imagine you have this plain text sentence:
> Socrates spoke to Plato in Athens.

To mark this up digitally, we place descriptive labels around the words:
> `<person>Socrates</person> spoke to <person>Plato</person> in <place>Athens</place>.`

Now, a simple computer script can scan 10,000 pages of text and extract a list of every `<person>` mentioned and every `<place>` visited, without getting confused by ordinary words.

**Vocabulary.** *Markup* — text added to the content of a document to provide structural, formatting, or semantic metadata. *Semantic Markup* — markup that describes the meaning and conceptual nature of text content rather than its visual appearance. *Presentational Markup* — markup that describes only visual styling (e.g., bold, color, font size).

**Takeaway:** Digital markup embeds explicit labels within text, allowing computers to search, categorize, and analyze semantic entities like people, places, and dates across large textual corpora.

---

## **16 Content**

**The Anatomy of XML: Elements, Tags, Content, and Attributes**

The global standard for writing structured markup in the humanities is **XML** (which stands for **Extensible Markup Language**). XML is not a programming language; it is a markup format with strict, elegant grammatical rules.

Let us examine the anatomy of a standard XML building block:
```xml
<placeName type="city" ref="https://pleiades.stoa.org/places/579885">Athens</placeName>
```

This snippet consists of four fundamental parts:

1. **Opening Tag (`<placeName>`):** Starts with `<` and ends with `>`, announcing that a specific element begins here.
2. **Element Name (`placeName`):** The identifier that names what kind of information this is.
3. **Attributes (`type="city"` and `ref="..."`):** Key-value pairs inside the opening tag that provide extra metadata. Attributes always use an equals sign and wrap their values in quotation marks (`name="value"`).
4. **Content (`Athens`):** The actual text lying between the opening and closing tags.
5. **Closing Tag (`</placeName>`): Starts with `</` and ends with `>`, signaling that this element is finished.

Together, the opening tag, attributes, content, and closing tag form a single **XML Element**.

**Vocabulary.** *XML (Extensible Markup Language)* — a text format designed for storing and transporting structured data with customizable tags. *XML Element* — a logical unit of XML comprising an opening tag, content, and closing tag. *XML Attribute* — a name-value pair inside an opening tag providing supplementary metadata about the element.

**Takeaway:** An XML element consists of an opening tag with optional attributes, text content, and a matching closing tag (`<tag attribute="value">content</tag>`).

---

## **17 Content**

**Golden Rules of XML: Closing Tags and Clean Nesting**

Unlike human readers, who can easily overlook missing punctuation or deduce meaning from messy handwriting, XML parser software is strictly unforgiving. For an XML document to be valid, it must be **well-formed**, meaning it obeys two golden rules:

**Rule 1: Every opening tag must have an exact closing tag.**

- ❌ Broken: `<title>The Iliad` (missing `</title>`)
- ✅ Valid: `<title>The Iliad</title>`

**Rule 2: Elements must be cleanly nested, never overlapping.**
Elements must close in the reverse order that they opened, like Russian nesting dolls:

- ❌ Broken: `<sentence><person>Achilles</sentence></person>` (overlapping tags)
- ✅ Valid: `<sentence><person>Achilles</person></sentence>` (clean nesting)

If an element has no text content (such as a line break), it can be written as a self-closing tag: `<lb/>` or `<pb n="12r"/>` (page break for folio 12 recto). If an XML file violates even a single rule, the computer refuses to process it and reports a syntax error. This strictness is intentional: it guarantees that data is never ambiguous.

**Vocabulary.** *Well-Formed XML* — XML code that strictly adheres to the syntactic grammar rules of the XML specification (all tags closed, properly nested, attributes quoted). *Self-Closing Tag* — an empty XML element that closes itself without separate closing tags (e.g., `<lb/>`). *XML Parser* — software that reads and checks XML documents to ensure they are well-formed before processing.

**Takeaway:** Well-formed XML requires that every tag is explicitly closed and that elements nest cleanly without overlapping boundaries.

---

## **18 Content**

**What is TEI? The Global Standard for Historical Manuscripts**

Because XML is "extensible," anyone can invent whatever tag names they want. You could invent `<coolManuscript>` and someone else could invent `<oldBook>`. But if every university and archive uses random tags, nobody can share data.

In 1987, an international consortium of literature professors, manuscript curators, and computer scientists founded the **Text Encoding Initiative (TEI)**. The TEI created an exhaustive, scholarly dictionary of XML tags specifically designed for historical texts, manuscripts, and literary works.

Today, the **TEI P5 Guidelines** are the universal standard for digital scholarly editions worldwide (used by Oxford, the British Library, the Vatican Library, Perseus, and Harvard). When you learn TEI in this course, you are learning the exact encoding framework used by professional digital editors across the globe.

**Vocabulary.** *Text Encoding Initiative (TEI)* — an international organization and standard for encoding humanities texts in XML. *TEI P5* — the current fifth version of the official TEI Guidelines and tagset. *Digital Scholarly Edition* — a critical edition of a historical text produced and published using digital computational standards.

**Takeaway:** The TEI (Text Encoding Initiative) is the international standard vocabulary of XML tags used by libraries, universities, and scholars to encode historical texts and manuscripts.

---

## **19 Content**

**A Simple TEI Example: Marking People, Places, and Deleted Words**

To see how intuitive TEI XML is, look at how a medieval manuscript sentence is encoded when a scribe made a mistake and crossed out a word:

```xml
<p>
  In the year <date when="1245">1245</date>, 
  <persName ref="#scribe_john">John</persName> visited 
  <placeName ref="#antioch">Antioch</placeName> and wrote 
  <del rend="strikethrough">twenty</del>
  <add place="above">thirty</add> pages.
</p>
```

Look at what this simple TEI snippet accomplishes:

- `<persName>` and `<placeName>` identify the historical human beings and geographical locations.
- `<date when="1245">` allows a computer timeline to index this event, even if the text wrote "the twelfth year of the king's reign."
- `<del>` (deletion) records that the word "twenty" was crossed out on the physical parchment.
- `<add>` (addition) records that the word "thirty" was written above the line by the corrector.

A web browser reading this TEI file can display the clean text to general readers, or render a specialized view for palaeographers showing the strikethrough and insertion in exact visual positions.

**Vocabulary.** *`<persName>` / `<placeName>`* — TEI elements that encode proper names of persons and places. *`<del>` / `<add>`* — TEI elements that record physical scribal deletions and text additions in a manuscript. *Palaeography* — the study of ancient and medieval handwriting and scripts.

**Takeaway:** TEI markup allows scholars to simultaneously capture historical meaning, physical manuscript alterations (scribal corrections and additions), and metadata in a single, transparent XML file.

---

## **20 Content**

**Why Well-Formed Markup Protects Cultural Heritage**

Why do scholars invest hundreds of hours encoding ancient manuscripts in TEI XML rather than simply typing them into a blog or uploading a PDF?

The answer is **long-term preservation and multi-purpose reusability**. When a historical text is encoded in clean, valid TEI XML:

1. **It Never Goes Out of Date:** XML is stored in plain text. It will be just as readable in 2126 as it is today.
2. **It Can Be Transformed into Any Format:** From a single TEI XML master file, automated scripts can instantly generate a printed book PDF, an interactive website, a mobile app version, or an audio screen-reader transcript without re-typing a single word.
3. **It Connects to Global Knowledge Graphs:** Linking places to online historical gazetteers (like Pleiades) connects your local edition to a global map of the ancient world.

By learning to create well-formed markup, you are learning how to preserve endangered cultural heritage in a format that outlives any single software application or hardware platform.

**Vocabulary.** *Data Longevity* — the ability of digital information to remain readable and usable over long time horizons. *Transformation Pipeline* — an automated series of computational steps that converts master data (e.g., TEI XML) into multiple output formats (HTML, PDF, EPUB). *Gazetteer* — a geographical dictionary or database linking historical place names to geographic coordinates.

**Takeaway:** Well-formed TEI markup protects cultural heritage by preserving historical evidence in a durable, software-independent format that can be automatically transformed into websites, books, and research databases.

---

## **21 Content**

**What is Python and Why Do Humanists Use It?**

As your digital collection of historical texts grows from one page to thousands of pages, doing everything by hand becomes impossible. If you need to count how many times each character speaks in a 500-page drama, or verify that every date in 200 XML files is formatted correctly, you need automation.

This is where **Python** enters our digital scriptorium. Python is one of the world's most popular programming languages, celebrated for its clear, readable syntax that looks very close to plain English. 

In this course, you are **not** expected to be a computer science major or a professional software engineer. We use Python as a **scholarly research assistant**—writing short, focused scripts to handle tedious, repetitive tasks:

- Scanning folders to find specific words or phrases.
- Converting spreadsheets of manuscript metadata into valid XML records.
- Calculating word frequencies and vocabulary overlap across ancient authors.
- Automating the compilation of course interactive lessons and quizzes.

**Vocabulary.** *Python* — a high-level, interpreted programming language known for its readability and widespread use in data science, artificial intelligence, and digital humanities. *Script* — a small program written in a language like Python to automate a specific sequence of tasks. *Interpreted Language* — a programming language where code is executed directly by an interpreter line-by-line without prior machine compilation.

**Takeaway:** Python is a readable, beginner-friendly programming language that digital humanists use to automate tedious tasks, process text collections, and transform research data.

---

## **22 Content**

**Running Your First Python Script in the Terminal**

Writing and running a Python script is remarkably straightforward. Because a Python script is simply a plain text file saved with the `.py` extension, you can create it directly inside VS Code.

Consider a simple script saved as `hello_humanities.py`:
```python
student_name = "Alex"
course = "RELS 398: Digital Methods"
print(f"Welcome to {course}, {student_name}!")
```

To run this script, you open the integrated terminal in VS Code and type:
```bash
python3 hello_humanities.py
```

The computer invokes the Python interpreter, executes the instructions line-by-line, and prints the output directly onto your screen:
`Welcome to RELS 398: Digital Methods, Alex!`

In our weekly workshops, you will run pre-built Python scripts provided in the repository, learning how each command connects to the files on your hard drive.

**Vocabulary.** *`python3`* — the terminal command used to invoke the Python 3 interpreter and execute a Python script file. *Variable* — a named storage location in a computer program that holds data (e.g., `student_name = "Alex"`). *`print()`* — a fundamental Python function that outputs text to the terminal screen.

**Takeaway:** Python scripts are plain text files (.py) executed through the terminal using the command `python3 <script_name>`, executing your instructions line-by-line.

---

## **23 Content**

**Automating Repetitive Tasks: Counting Words and Searching Texts**

To see the real power of Python in textual scholarship, imagine you are given a 100,000-word Latin or Greek text and asked to find every line containing the word for "king" (*basileus* or *rex*). Searching manually with your eyes would take hours and you might easily miss occurrences due to fatigue.

In Python, this task requires only five lines of code:
```python
with open("ancient_text.txt", "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        if "king" in line.lower():
            print(f"Line {line_num}: {line.strip()}")
```

In less than one-tenth of a second, Python scans all 100,000 words, checks every sentence, and prints every matching line alongside its exact line number. This is not about replacing human scholarly reading; it is about freeing the human scholar from mechanical drudgery so you can focus your intellect on deep interpretation, critical analysis, and historical context.

**Vocabulary.** *Iteration (Loop)* — a computational process where a sequence of instructions is repeated for each item in a collection (e.g., for every line in a file). *Computational Reading (Distant Reading)* — an approach in literary and historical studies that analyzes large text corpora computationally rather than through traditional close reading alone.

**Takeaway:** Python automates mechanical textual tasks (like concordance searches and frequency counts) in milliseconds, liberating scholars to focus on critical interpretation.

---

## **24 Content**

**Python as the Glue Connecting Texts, Images, and Web Pages**

In a modern digital edition project, you work with many different kinds of media simultaneously:

- High-resolution photographs of manuscript pages from library servers (IIIF).
- Structured TEI XML transcription files.
- Metadata spreadsheets tracking scribes, dates, and watermark dimensions.
- Web browser user interfaces (HTML/CSS) displaying the finished edition.

Python is the **universal glue** that binds all these pieces together. A Python script can download manuscript images from an Oxford server via an API, match each image to the corresponding TEI XML page break tag (`<pb/>`), extract vocabulary definitions, and compile everything into a seamless interactive web page or Moodle quiz. Throughout this course, our shared Python scripts handle this pipeline smoothly behind the scenes.

**Vocabulary.** *Glue Code* — software code that does not implement core algorithms itself, but instead connects disparate software components, formats, and services together. *Pipeline* — a set of automated data processing elements connected in series, where the output of one element is the input of the next.

**Takeaway:** Python acts as the connective glue in digital scholarship, linking raw manuscript images, XML markup, metadata databases, and interactive web interfaces into a unified workflow.

---

## **25 Content**

**What is a Large Language Model (Claude)?**

In recent years, artificial intelligence has undergone a revolutionary shift with the development of **Large Language Models (LLMs)**, such as Anthropic's **Claude** and OpenAI's GPT models.

An LLM is not a conscious mind, nor is it a magical all-knowing oracle. At a technical level, an LLM is a massive statistical neural network trained on hundreds of billions of words from books, academic articles, websites, and source code. By analyzing these vast patterns of human language, the model learns the complex grammatical, syntactic, and conceptual relationships between words.

When you give an LLM a prompt (e.g., *"Translate this ancient Greek sentence into English and explain the grammatical case of each noun"*), the model uses statistical probability to generate a coherent, contextually appropriate response. Because LLMs have ingested vast multilingual and coding corpora, they are remarkably fluent at analyzing historical languages and writing computational code.

**Vocabulary.** *Large Language Model (LLM)* — an artificial intelligence algorithm trained on massive text datasets that uses deep learning to understand, generate, and process natural human language. *Prompt* — the natural-language input, question, or instruction given to an AI model to guide its response. *Neural Network* — a computational model inspired by the human brain's interconnected neurons, used in machine learning to recognize patterns in data.

**Takeaway:** Large Language Models like Claude are powerful statistical AI systems trained on vast textual datasets, capable of understanding prompts and generating fluent natural language and code.

---

## **26 Content**

**How AI Can Assist: Transcribing, Summarizing, and Formatting**

For digital humanists, LLMs represent an astonishingly versatile research partner. When used properly, an AI assistant like Claude can accelerate scholarship in several major areas:

1. **Preliminary Transcription & Decipherment:** Helping decipher damaged or difficult manuscript readings by proposing plausible grammatical reconstructions based on context.
2. **Metadata Extraction:** Reading an unstructured 19th-century Latin catalogue entry and automatically restructuring the dates, authors, and shelfmarks into a tidy table or JSON format.
3. **Drafting Markup:** Converting plain text into draft TEI XML with proper tags and attributes in seconds, saving hours of manual bracket typing.
4. **Code Explanation:** Explaining what a confusing Python script does line-by-line in plain English, helping you debug errors.

AI does not replace the scholar's expertise; it acts as a tireless research assistant that handles tedious structural conversions at lightning speed.

**Vocabulary.** *AI-Assisted Philology* — the practice of using artificial intelligence models to assist with transcription, translation, grammatical parsing, and markup in textual scholarship. *Data Restructuring* — converting unstructured text (like a narrative book description) into standardized, structured data (like XML or JSON).

**Takeaway:** AI models can assist scholars by generating draft transcriptions, restructuring messy bibliographic notes into clean XML, and explaining complex computer code.

---

## **27 Content**

**The Critical Rule: AI Hallucinations and Why the Human Stays in Charge**

Despite their impressive fluency, LLMs have a critical, dangerous flaw: **hallucination**. Because an LLM generates text based on statistical plausibility rather than an internal concept of ground-truth fact, it can confidently invent false information that *looks* completely convincing:

- An LLM might invent a non-existent Greek manuscript shelfmark at the British Library.
- It might cite a fake academic paper written by real professors.
- It might translate a Latin verb with absolute grammatical confidence, but completely invert the historical meaning.

In scholarship, an unverified hallucination is fatal. That is why the golden rule of this course is: **The AI proposes, but the human scholar disposes.** 

You must never blindly accept AI output as authoritative truth. Every AI-generated transcription, translation, and XML tag must be audited and verified against the primary historical evidence by a human editor.

**Vocabulary.** *Hallucination (AI)* — a confident response generated by an AI model that contains false, fabricated, or inaccurate information not grounded in its source data. *Human-in-the-Loop (HITL)* — a workflow design where automated or AI processes require human review, judgment, and approval at critical decision points.

**Takeaway:** AI models frequently hallucinate plausible-sounding falsehoods; human scholars must always audit and verify every AI-generated claim against primary evidence.

---

## **28 Content**

**What is Antigravity? An Agentic Workspace for Pair-Programming**

In traditional computing, you use software in isolation: you type code in one window, copy it into a chatbot web browser in another window, and paste the answer back. This back-and-forth copying is slow and disconnects the AI from your actual project environment.

In this course, we work in an advanced environment called **Antigravity** (built on Google's advanced agentic developer architecture). Antigravity is an **agentic pair-programming workspace**. 

In Antigravity:

- The AI agent can see your project files directly (reading the exact XML, Python, and Markdown files on your disk).
- You collaborate with the AI through natural-language conversation, asking it to inspect files, run automated verification linters, and propose edits.
- The AI creates structured implementation plans and highlights changes for your review before executing them.

Antigravity models the future of digital humanities collaboration: a seamless partnership where the human scholar directs the research questions and evaluates the historical evidence, while the AI agent assists with technical execution and automated consistency checks.

**Vocabulary.** *AI Agent* — an artificial intelligence system that can perceive its computational environment, use tools (like reading files and running terminal commands), and take autonomous actions to achieve a specified goal. *Pair Programming* — a collaborative software development technique where two developers (or a human and an AI agent) work together on the same codebase simultaneously.

**Takeaway:** Antigravity is an agentic pair-programming workspace where human scholars and AI agents collaborate directly within the project filesystem to build, test, and audit digital editions.

---

## **29 Content**

**The Three-Step Method of This Course: Manual -> Automated -> AI-Assisted**

To prepare you for the intellectual journey of this semester, RELS 398 is structured around a rigorous, comparative methodology called the **Three-Step Comparative Cycle**. Almost every module in this course walks through three distinct phases:

1. **Tuesday (Manual Foundations):** We work by hand, establishing the ground truth of scholarship. You will read raw manuscript images, transcribe letters with your own eyes, and experience the physical challenges that scribes and traditional editors faced.
2. **Wednesday (Deterministic & Rule-Based Tools):** We apply classical computational methods—running Python scripts, compiling TEI XML, executing CollateX algorithms, and testing against strict schemas. These tools follow rigid, predictable mathematical rules.
3. **Friday (AI-Assisted & Large Language Models):** We deploy generative AI models (like Claude) to perform the same task. We measure the AI's speed, evaluate its accuracy, audit its hallucinations, and calculate error rates (CER and WER) against our Tuesday manual ground truth.

By comparing all three methods every week, you will discover exactly where human judgment is irreplaceable, where rule-based algorithms excel, and where AI provides genuine scholarly leverage.

**Vocabulary.** *Ground Truth* — the empirically verified, authoritative baseline data against which automated and AI models are measured. *Deterministic Algorithm* — an algorithm that given the same input will always produce the exact same output every time. *Comparative Methodology* — a research strategy that systematically compares different techniques (manual, algorithmic, AI) on the same dataset to evaluate their strengths and weaknesses.

**Takeaway:** RELS 398 follows a Three-Step Comparative Cycle (Tuesday Manual $\rightarrow$ Wednesday Deterministic $\rightarrow$ Friday AI-Assisted) to teach you how traditional philology, rule-based algorithms, and modern AI intersect.

---

## **30 Content**

**Synthesis: Building Your Toolkit for the Semester Ahead**

Look back at what you have explored in this opening lesson. You have moved from the passive consumer mindset of word processors to the active, empowered stance of a digital humanist.

You now understand the complete anatomy of our digital scriptorium:

- **Plain Text and VS Code:** The durable, transparent foundation where all our data lives.
- **Git and Version Control:** The project time machine that protects your work and records your scholarly reasoning.
- **XML and the TEI:** The international language of structured manuscript markup that preserves cultural heritage.
- **Python:** The versatile script engine that automates repetitive textual tasks.
- **Claude and Antigravity:** The AI assistants and agentic workspace that augment your analytical reach while keeping you firmly in the editorial driver's seat.

You do not need to memorize every command or XML tag today. Each tool will be practiced step-by-step in the weeks ahead. You are now equipped with the conceptual roadmap for the digital methods of the 21st century. Welcome to the scriptorium—let us begin building!

**Vocabulary.** *Computational Philology* — the application of computational methods, software tools, and data structures to the historical study of language, texts, and manuscripts. *Digital Scriptorium* — a modern digital workspace for transcribing, editing, and publishing historical documents using computational tools.

**Takeaway:** Digital scholarship unites plain text, Git version control, TEI XML markup, Python automation, and AI pair-programming into a powerful, transparent workspace for preserving and studying historical documents.
