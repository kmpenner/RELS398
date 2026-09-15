# Lesson 1.1 — Local Git Version Control for Textual Scholarship

*RELS 398 / ENGL 398 · Topic 1: Orientation · Meeting #1 (Wed Sep 2)*

*Orientation week — the three-step comparative cycle does not yet apply. This
meeting establishes the version control discipline that every later week's
manual, deterministic, and AI-assisted work will be recorded in.*

---

## **01 Content**

**Why a Version Control System Belongs in a Philology Course**

You have enrolled in a course about historical documents, and the first thing
you will be asked to learn is a piece of software written for programmers. That
sequence deserves an explanation, because the justification is not that Git is a
useful job skill — though it is — but that Git is a formal model of the very
thing textual criticism has always studied.

Textual criticism exists because texts change as they are copied. A scribe
working from an exemplar introduces errors, corrections, and deliberate
alterations; a later scribe copies that copy, inheriting some changes and adding
others. The discipline's central problem is reconstructing the relationships
among those states from the surviving evidence. Git exists because software
changes as it is edited, and its central problem is recording the relationships
among those states exactly. The two disciplines converged on the same abstract
structure independently, and the convergence is not a coincidence: both are
concerned with tracking variant states of a document across a branching history
of transmission.

Huskey (2024) makes this argument directly, proposing that scholarly editors
treat the Git repository as a research journal rather than as file storage. The
claim is stronger than it sounds. A research journal is not a backup; it is an
argument in progress, in which each entry is dated, attributed, and justified. A
Git repository used properly has exactly those properties, and a Git repository
used carelessly has none of them. The difference lies entirely in the discipline
of the person committing.

**Vocabulary.** *Version control system (VCS)* — software that records the state
of a set of files at successive points in time, with the metadata needed to
identify, compare, and recover any of those states. *Exemplar* — the manuscript
a scribe copies from. *Witness* — any surviving manuscript that attests a text.

**Takeaway:** Git is on the syllabus because its data model
formalizes textual transmission, not because digital humanists are expected to
know developer tools.

---

## **02 Content**

**The Print Edition as a Lossy Record: Giarratano's *Bucolica***

The best case for version-controlled editing is a case where its absence
destroyed evidence. Huskey (2024) analyzes the editorial career of Caesar
Giarratano, who published five separate print editions of Calpurnius Siculus'
*Bucolica* between 1910 and 1951 — five editions of the same short pastoral
text, by the same editor, across forty-one years.

Across those editions Giarratano changed his method fundamentally. He moved from
a *positive* critical apparatus, which records all variant readings including
the one printed in the text, to a *negative* apparatus, which records only the
readings rejected. He abandoned his Greek-character manuscript sigla in favour of
Latin characters, silently renaming every witness in the edition. These are not
typographical adjustments; they are systemic changes to how the edition
represents evidence, and each implies a changed view of what an apparatus is for
(Huskey, 2024).

The rationale for those changes is gone. Print editions record outcomes, not
reasoning: the reader receives the finished apparatus with no account of why its
form changed between 1910 and 1951. A scholar today who wants to understand
Giarratano's development must physically obtain all five volumes and collate
them by hand — performing textual criticism on a modern critical edition, which
is precisely the labour the edition was supposed to spare them (Huskey, 2024).

Had Giarratano worked in a version-controlled repository, the change of sigla
would have been a single documented commit with a stated reason, and the shift
from positive to negative apparatus would have been a documented restructuring.
The evidence would still exist. This is the concrete stake of the discipline you
are about to learn: what is not committed with rationale is not recoverable.

**Takeaway:** Print editions preserve the editor's conclusions
and discard the editor's reasoning; a version-controlled edition preserves both.

---

## **03 Content**

**The Critical Apparatus and the Commit Log Are the Same Object**

Consider what a critical apparatus does. Against a base text, it records
alternative readings, each attributed to a witness, each located at a precise
point in the text. It is a structured record of deviation from a reference state.

Now consider what `git log` combined with `git diff` does. Against a base state,
it records alternative states, each attributed to an author, each located at a
precise point in the file. The structural correspondence is exact, and Huskey
(2024) argues it should be exploited pedagogically rather than treated as a
curiosity.

The correspondence extends through the whole vocabulary of the discipline, which
is why this course can teach both at once:

| Philological concept | Git equivalent | Shared epistemological function |
| --- | --- | --- |
| Exemplar or archetype | The `main` branch | The reference state from which variants deviate |
| Scribal copying | `git clone`, `git branch` | Duplicating a text so it can be altered independently |
| Variant reading or emendation | `git commit` | A dated, attributed alteration with stated rationale |
| Critical apparatus | `git diff`, `git log` | The aggregated record of deviation from the reference |
| Stemma codicum | The commit graph | The genealogy of states and their descent relations |
| Siglum | Commit hash | A short unique label identifying one witness or state |

There is one important asymmetry. The scribe did not intend to create an
apparatus; the apparatus is reconstructed after the fact by an editor working
from damaged and partial evidence. You, by contrast, are generating your own
transmission history deliberately and in full. You are in the unusual position of
being both the scribe and the editor of your own text — which means the quality
of your apparatus is entirely within your control, and entirely your
responsibility.

**Takeaway:** You will produce two editions this term: the TEI
edition of your passage, and the Git history that documents how you arrived at
it.

---

## **04 Content**

**Content-Addressable Storage: What Git Actually Stores**

Most people's mental model of version control is that it stores a list of
changes — a file, then a patch, then another patch. That model is wrong for Git,
and holding it will make Git's behaviour seem arbitrary. Git stores complete
snapshots, and it addresses them by their content.

A *content-addressable* store is one in which an object's name is derived from
its contents rather than assigned externally. Git computes a SHA-1 checksum over
each object's bytes, producing a forty-character hexadecimal identifier, and
that identifier *is* the object's name in the database (Chacon & Straub, 2014).
The consequence is that identical content necessarily has an identical name: if
two of your transcription files contain exactly the same text, Git stores that
content once and points at it twice, whatever the files are called and wherever
they sit in the directory tree.

The philological payoff is immediate. Because the name is derived from the
content, the name cannot disagree with the content. If a byte changes, the hash
changes; if the hash is unchanged, no byte has changed. There is no way to alter
a stored transcription while leaving its identifier intact, which means the
identifier functions as a tamper-evident seal on the state of your edition at a
moment in time (Chacon & Straub, 2014).

This is why Git can make guarantees that a folder of files named
`transcription_v2_FINAL_revised.xml` cannot. Manual versioning schemes encode
your intentions in filenames, and filenames lie — they are assigned by a tired
student at midnight and are not checked against anything. Hashes are computed
from the data and cannot lie.

**Vocabulary.** *SHA-1* — a cryptographic hash function producing a 160-bit
(40 hex character) digest. *Checksum* — a value computed from data such that a
change in the data changes the value. *Content-addressable* — named by content
rather than by assigned label.

**Takeaway:** Git names every stored object by a hash of its
contents, so an object's identifier is a verifiable claim about its bytes.

---

## **05 Content**

**The Four Object Types: Blobs, Trees, Commits, and Tags**

The entire Git database is built from four object types. Understanding them is
not optional trivia; nearly every confusing Git behaviour you will encounter
this term becomes obvious once you know which object is involved.

A **blob** stores the raw contents of a file, and nothing else — no filename, no
path, no timestamp, no permissions. A blob of your transcription is just the
bytes of the transcription. A **tree** supplies exactly what the blob omits: it
is a directory listing, mapping names to the hashes of blobs and of other trees,
along with file mode information. A **commit** points to a single root tree —
that is, to a complete snapshot of the project — and adds the metadata that makes
the snapshot meaningful: author, committer, timestamp, message, and pointers to
its parent commit or commits. A **tag** is a named, optionally signed pointer to
a specific commit, used to mark states that matter permanently (Chacon & Straub,
2014).

| Object | Stores | Points to | Editorial analogue |
| --- | --- | --- | --- |
| Blob | Raw file contents | Nothing | The text of one witness, unlabelled |
| Tree | Names, modes, structure | Blobs and sub-trees | The physical arrangement of a codex |
| Commit | Author, date, message | One root tree, parent commits | A dated editorial intervention with rationale |
| Tag | A label, optionally signed | One commit | A published edition, cited by version |

The separation of blob from tree explains a behaviour that puzzles new users:
Git does not track file renames as such. When you rename a transcription file,
the blob is unchanged — the content did not change — and only the tree entry
differs. Git detects renames after the fact by noticing that a blob left one
path and arrived at another, rather than by recording a rename operation.

**Takeaway:** Blobs hold content, trees hold structure, commits
hold history and rationale, and tags mark states worth citing.

---

## **06 Content**

**The Directed Acyclic Graph**

Because every commit stores the hash of its parent, commits chain backwards
through time. That chain is not a simple line: a commit may have two parents (a
merge), and several commits may share one parent (a branch point). The resulting
structure is a **directed acyclic graph**, or DAG (Chacon & Straub, 2014).

Each word in the term does work. *Directed*: the parent relation has an
orientation — a commit knows its parents, but a parent does not know its
children, exactly as an exemplar does not know what was copied from it.
*Acyclic*: there are no loops, because a commit's hash incorporates its parents'
hashes, so a commit cannot be its own ancestor. *Graph*: the structure is a
network of nodes and edges, not a list.

The philological reader will recognize this shape immediately. A stemma codicum
is a directed acyclic graph over manuscripts: descent has an orientation, no
manuscript descends from itself, and the structure branches. The two fields
arrived at the same formalism because they are modelling the same phenomenon —
descent with modification through copying (Huskey, 2024).

There is one instructive place where the analogy breaks, and it is worth
noticing now. Stemmatic reconstruction is *inference under uncertainty*: the
editor infers relations among witnesses from shared errors, because the actual
history is unobserved and most intermediate copies are lost. Your Git DAG, by
contrast, is *observed* — it is not reconstructed but recorded, complete, with no
missing intermediaries. This term you will experience what a philologist almost
never has: a transmission history with no gaps in it.

**Vocabulary.** *DAG* — a set of nodes connected by directed edges containing no
cycles. *Stemma codicum* — the genealogical tree of a text's surviving witnesses.
*Merge commit* — a commit with more than one parent.

**Takeaway:** A repository's history is a directed acyclic
graph, the same formal structure as a stemma — but recorded rather than inferred.

---

## **07 Content**

**Cryptographic Integrity and the Cascading Hash**

The properties described so far combine into something stronger than either
alone. Because a commit's hash is computed over its content — which includes its
tree hash and its parent hashes — a change anywhere in the history propagates
outward to every commit that descends from it.

Follow the cascade concretely. You alter a single combining diacritic in a TEI
transcription. The file's bytes differ, so its blob hash differs. The tree
listing that blob now references a different hash, so the tree's own hash
differs. The commit pointing at that tree now references a different tree hash,
so the commit hash differs. Every subsequent commit references a changed parent
hash, so every one of them changes too (Chacon & Straub, 2014).

The security consequence is that silent tampering is not merely difficult but
structurally impossible. There is no way to reach into the middle of a
repository's history, alter a reading, and leave the surrounding history intact:
either the downstream hashes change and the alteration is visible, or they do not
change and the alteration did not happen. History can be *rewritten* — Git
provides tools for that — but a rewrite produces a visibly different graph. It
cannot be done invisibly.

For a scholarly edition this is the guarantee that matters. Huskey's (2024)
argument for reproducibility and explainability in editing depends on the audit
trail being trustworthy; an audit trail that could be quietly edited afterwards
would establish nothing. The cryptographic chain is what converts "here is my
work log" into "here is a verifiable claim about my work."

**Takeaway:** A change anywhere in history changes every hash
downstream of it, so a repository's history cannot be altered without leaving
evidence.

---

## **08 Content**

**Branching, and Why You Will Use It for Editorial Hypotheses**

A branch in Git is startlingly cheap: it is a file containing a single commit
hash, plus a name. Creating one costs a few dozen bytes, which is why Git
encourages branching in situations where older version control systems made it a
significant undertaking (Chacon & Straub, 2014).

The editorial use is the interesting one. You will frequently face a decision
with no clearly correct answer: whether to treat a marginal addition as part of
the text or as apparatus, whether a damaged sequence is best restored one way or
another, whether to encode a correction with `<sic>`/`<corr>` or to leave it
diplomatic. The traditional response is to choose, proceed, and record the
rejected option in a footnote. The version-controlled response is to encode both
fully, on separate branches, and compare the finished results before deciding.

This changes what an editorial hypothesis costs. On paper, pursuing an
alternative encoding through an entire passage is expensive enough that editors
rarely do it, and so alternatives are usually rejected on the basis of a
prospective judgement rather than a completed trial. On a branch, the same
experiment costs almost nothing and can be abandoned without trace or merged
without penalty. You should expect to use this repeatedly from Week 6 onward,
when normalization decisions start to have consequences that only become visible
several steps later in the pipeline.

The Perseids Platform makes exactly this affordance central to its pedagogy:
students work on their own branches precisely so that they can attempt difficult
encoding without risking the shared text, and submit the result for editorial
review only once it is complete (Almas & Beaulieu, 2012).

**Takeaway:** Branches make editorial alternatives cheap enough
to test rather than merely to speculate about.

---

## **09 Content**

**Installing Git and Declaring Who You Are**

Before the first commit, Git needs to know how to attribute your work. This is
not a formality: authorship metadata is baked into every commit object and cannot
be changed later without rewriting history.

Configure your identity globally, once, on each machine you will work on:

```bash
git config --global user.name "Your Full Name"
git config --global user.email "yourid@stfx.ca"
```

Use the name you want to appear in the permanent record of your edition, in the
form you would use in a publication. Use your StFX address rather than a personal
one, since the repository will be reviewed as coursework. If you also work on a
personal laptop, configure it identically — commits made under two different
identities look like two different editors to anyone reading the log later, and
the resulting apparatus is misattributed.

Two further global settings will save you difficulty in Week 4 and after. Set
the default branch name explicitly, and set your editor to something you can
actually exit:

| Setting | Command | Why it matters here |
| --- | --- | --- |
| Default branch name | `git config --global init.defaultBranch main` | Keeps every student repository consistent for review |
| Commit editor | `git config --global core.editor "code --wait"` | Enables multi-line commit bodies without `vi` |
| Rebase on pull | `git config --global pull.rebase false` | Preserves merge commits as evidence of integration |

Verify the result with `git config --global --list` before continuing. Everything
in this course accumulates, and an identity error committed today propagates
through every assignment that follows.

**Takeaway:** Authorship metadata is permanent in the commit
object, so configure it correctly before the first commit rather than after.

---

## **10 Content**

**Initializing the Repository for Your Edition**

Each of you will maintain a single repository for the whole term, containing the
passage you select this week and every layer of encoding you subsequently build
on it. Create it now, in a location you will not lose:

```bash
mkdir rels398-edition
cd rels398-edition
git init
```

`git init` creates a `.git` directory. That hidden directory *is* the repository:
the object database, the references, the configuration, and the hooks all live
inside it. The visible files beside it are merely the currently checked-out
state — a view of one commit, which Git can regenerate at any time from the
objects it holds. Deleting `.git` deletes your entire history while leaving the
current files intact, which is a mistake that looks harmless right up until you
need an earlier state.

Establish the directory structure now rather than reorganizing later. The layout
below mirrors the distinction between source material, working files, and
outputs that the course assignments assume:

| Directory | Holds | Populated in |
| --- | --- | --- |
| `images/` | Facsimile images and IIIF manifest for your passage | Week 3 |
| `transcription/` | Diplomatic and normalized transcriptions | Weeks 4–6 |
| `collation/` | Witness files, CollateX input and output | Week 7 |
| `edition/` | The TEI file with apparatus, lemmatization, commentary | Weeks 8–12 |
| `logs/` | Error-rate reports, AI-usage notes, reconciliation records | Weeks 5 onward |

Add a `README.md` at the root stating which manuscript passage you have chosen
and why. That file is the first thing a reviewer reads, and by the end of term it
will be the front matter of your edition.

**Takeaway:** `.git` is the repository and the visible files are
just a checked-out view of it; structure the working tree once, at the start.

---

## **11 Content**

**The Three States: Working Directory, Staging Area, Repository**

Git's most distinctive feature, and the one that most reliably confuses
newcomers, is that a file exists in three places at once. Understanding the
three states is what makes atomic committing possible.

The **working directory** is what you see and edit: ordinary files on disk. The
**staging area** — also called the index — is a proposed next commit, holding the
exact content that will be recorded when you commit. The **repository** is the
object database in `.git`, holding every committed state permanently (Chacon &
Straub, 2014).

| State | Contents | Moved into it by | Reverted by |
| --- | --- | --- | --- |
| Working directory | Files as currently edited | Editing in Oxygen or VS Code | `git restore <file>` |
| Staging area | The proposed next commit | `git add <file>` | `git restore --staged <file>` |
| Repository | All permanently recorded states | `git commit` | `git revert <commit>` |

The staging area is what separates Git from a backup tool, and it exists
precisely so that *what you commit need not be everything you have changed*. In
a morning's work you may fix a typographic error in a transcription, adjust the
TEI header, and experiment with an encoding you are not yet sure about. Those are
three different scholarly acts. The staging area lets you record them as three
commits, in an order you choose, rather than as one undifferentiated lump.

Use `git status` constantly — it reports which files sit in which state, and it
suggests the command to move them. Experienced users run it more often than any
other command, not less.

**Takeaway:** The staging area exists so that a commit can
record one logical change rather than everything you happen to have edited.

---

## **12 Content**

**Your First Commit**

With the structure in place, record the initial state. The sequence is: inspect,
stage, inspect again, commit.

```bash
git status
git add README.md
git status
git commit -m "chore(repo): initialize edition repository with README"
```

Note the deliberate second `git status`. Staging is the step where mistakes
happen — a stray file, a forgotten file, an editor backup — and it is far easier
to correct the index before committing than to correct the history afterwards.
Read what Git tells you is staged, and confirm it is what you meant.

The `-m` flag supplies a single-line message. It is convenient and it is the
right tool for a genuinely trivial commit, but it will not serve you for most of
this term's work, because a one-line message cannot carry rationale. From Week 4
onward, run `git commit` with no `-m`, let your editor open, and write a subject
line followed by a blank line and a body explaining *why*.

A frequent early error deserves naming: `git add .` stages everything in the
directory, including files you did not intend to track — editor swap files,
operating system metadata, large image derivatives, and half-finished
experiments. Prefer naming files explicitly. Where a broad add is genuinely
convenient, protect yourself first with a `.gitignore` file listing the patterns
that should never be tracked, such as `.DS_Store`, `*~`, and `.vscode/`.

**Takeaway:** Stage deliberately and inspect the index before
committing; correcting the staging area is trivial, correcting history is not.

---

## **13 Content**

**Atomic Commits as Cognitive Discipline**

An **atomic commit** records exactly one logical change — one scholarly act,
complete in itself. The requirement sounds like tidiness. It is in fact the
central intellectual discipline of this course's version control practice, and
Huskey (2024) treats it as the precondition for a repository functioning as a
research journal at all.

Consider why. If a commit contains one change, its message can state what that
change was and why it was made, and the message is verifiable against the diff.
If a commit contains six unrelated changes, no honest message can describe it —
the author is forced into vagueness ("various corrections"), and the record
becomes unusable for exactly the purpose it was created to serve. Non-atomic
commits do not merely make history untidy; they make it uninformative.

Atomicity also determines whether history is *reversible*. Suppose you later
discover that your treatment of a particular abbreviation was wrong. If that
decision was applied in its own commit, you can revert precisely it, leaving
everything else untouched. If it was bundled with your header metadata and three
transcription corrections, reverting it means losing those too, and you will
instead redo the work by hand — which is to say the history provided no
protection at all.

The practical test is a sentence. Before committing, state what the commit does
in one clause without using "and". "Corrects the iotacism at line 14." "Adds the
TEI header." If you need "and", or if you find yourself reaching for a semicolon,
you are looking at two commits.

**Vocabulary.** *Atomic commit* — a commit recording a single logical change that
is complete and independently reversible. *Revert* — a new commit that undoes the
effect of an earlier one, without erasing it from history.

**Takeaway:** If you cannot describe a commit in one clause
without "and", it is more than one commit.

---

## **14 Content**

**What Non-Atomic Commits Look Like in Practice**

Recognizing the failure is easier than defining the rule. The table below
contrasts commits from a real editorial workflow — the left column shows patterns
that recur constantly in student repositories, the right shows the same work
recorded usably.

| Non-atomic commit | Why it fails | Atomic replacement |
| --- | --- | --- |
| `updates` | Describes nothing; diff must be read to learn anything | Separate commits, each naming its change |
| `fixed typos and added header` | Two unrelated acts; neither is separately reversible | `fix(transcription): correct itacism at 3.14`, then `feat(header): add teiHeader` |
| `end of day` | Groups by time rather than by meaning | One commit per decision made that day |
| `AI stuff` | Hides provenance of machine-generated content | `feat(transcription): add LLM draft` with an `AI-Generated: true` trailer |
| `asdfasdf` | Placeholder committed in haste and never revisited | Any message stating the actual change |

Two habits produce most non-atomic commits. The first is committing by clock
rather than by meaning — working for three hours and then committing whatever
has accumulated. The remedy is to commit when a change is *finished*, not when
you stop working. The second is treating commits as saves. Your editor already
saves your file; a commit is a claim that a piece of work is complete enough to
be recorded, and it should be reserved for that.

There is a legitimate exception worth knowing. Work-in-progress commits on a
private branch, made to preserve state before an experiment, are a normal and
useful practice. The expectation is that such commits are cleaned up — squashed
and given real messages — before the branch is merged. What must not happen is
work-in-progress commits reaching `main` and being left there as the permanent
record.

**Takeaway:** Commit when a change is complete, not when you
stop working for the day.

---

## **15 Content**

**The Conventional Commits Specification**

Ad-hoc commit messages degrade predictably. A log of "fixed typos," "more
edits," and "updated XML" carries no information that could not be obtained by
reading the diffs, which means the log has failed (Huskey, 2024). The remedy
adopted in this course is a formal message grammar: the Conventional Commits
specification.

The specification mandates a structured subject line (Conventional Commits,
n.d.):

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

The `type` is drawn from a fixed vocabulary and states the *kind* of change. The
optional `scope`, in parentheses, states *where* the change applies. The
description states what changed, in the imperative mood and lower case, without
a closing period. The body — separated by a blank line — carries the rationale,
and the footers carry structured metadata.

The value of a fixed grammar is that it makes the log machine-readable. A history
written this way can be filtered, counted, and summarized programmatically: every
apparatus correction, every normalization decision, every AI-assisted commit can
be extracted with a single command. A history written ad hoc can only be read
one line at a time by a human being, which in practice means it is not read at
all.

**Vocabulary.** *Type* — the fixed-vocabulary term classifying a commit.
*Scope* — an optional parenthesized noun naming the affected component. *Footer /
trailer* — structured `Key: value` metadata at the end of a commit message.

**Takeaway:** A fixed message grammar makes the commit log
queryable, which is what makes it usable as an apparatus.

---

## **16 Content**

**Mapping Commit Types to Editorial Acts**

Conventional Commits was written for software, and its vocabulary reflects that.
This course adopts the specification but binds each type to a specific class of
editorial intervention, so that the log describes philological work rather than
programming work (Huskey, 2024).

| Type | Editorial meaning | Example |
| --- | --- | --- |
| `feat` | New material: a witness, a division, a translation, an apparatus entry | `feat(collation): add witness N for lines 1-20` |
| `fix` | Correction of an error: a mistranscription, an invalid tag, a wrong siglum | `fix(apparatus): correct siglum from V to N at line 14` |
| `refactor` | Systemic change to encoding method, with no change to the reading | `refactor(epidoc): move inline app entries to external div` |
| `chore` | Maintenance: metadata, formatting, normalization passes | `chore(unicode): normalize Greek text to NFC` |
| `docs` | Editorial documentation: README, method notes, decision records | `docs(method): record normalization policy for iota subscript` |
| `test` | Validation work: schema checks, error-rate measurement scripts | `test(schema): add RelaxNG validation for edition.xml` |

The distinction between `fix` and `refactor` is the one that repays attention,
because it maps onto a genuine philological difference. A `fix` changes what the
edition *claims* — the reading was wrong and is now right. A `refactor` changes
how the edition *expresses* a claim that is unchanged — the same reading, encoded
differently. Giarratano's shift from positive to negative apparatus was a
refactor of enormous scope, and recording it as such would have marked it as a
methodological change rather than a textual one (Huskey, 2024).

Use `chore` sparingly. It is a genuine category for mechanical maintenance, but
it is also the path of least resistance, and a log in which most commits are
`chore` is a log whose author was not thinking about classification.

**Takeaway:** The type prefix classifies the *kind* of
editorial act, and `fix` versus `refactor` marks the difference between changing
a claim and changing its expression.

---

## **17 Content**

**The Commit Body: Recording Rationale, Not Description**

The subject line says what changed. The body says why — and the body is where
the scholarship lives. A diff already shows what changed, exhaustively and
without ambiguity; no prose description can improve on it. What the diff cannot
supply is the reasoning, and that is irrecoverable once forgotten.

Compare two records of the same edit:

```text
fix(transcription): correct reading at line 14
```

```text
fix(transcription): correct ἐγένετο to ἐγένοντο at line 14

The plural is required by the compound subject in line 13. Collation
against the facsimile at f. 42v confirms the manuscript reads -οντο;
the singular in my Tuesday transcription was an eye-skip to the
identical form in line 11. Cf. the same error corrected at 2.7.
```

The first is adequate bookkeeping. The second is a scholarly note: it states the
evidence, identifies the cause of the original error, and cross-references a
related decision. Six weeks from now, when you are writing the commentary layer
and need to explain this reading, the second commit has already written half of
it (Huskey, 2024).

The habit to build is to write the body as though for a reader who does not have
your current context — because in December, you will be that reader. State what
the manuscript shows, what you decided, and what evidence or principle decided
it. Where a decision was genuinely uncertain, say so and say what would resolve
it; a recorded uncertainty is far more useful to a later editor than a confident
silence.

**Takeaway:** The diff records what you changed; only the
commit body can record why, and only if you write it at the time.

---

## **18 Content**

**Reading History with `git log`**

A log is only valuable if it can be interrogated. `git log` in its bare form
prints commits in reverse chronological order with full metadata, which is
rarely the view you want. Its options turn it into a genuine research
instrument.

| Command | Returns | Editorial use |
| --- | --- | --- |
| `git log --oneline` | One line per commit | A rapid overview of the edition's development |
| `git log --oneline --graph` | The same, with the DAG drawn | Seeing where branches diverged and merged |
| `git log --follow <file>` | History of one file across renames | The full record of one transcription |
| `git log -S "ἐγένοντο"` | Commits that added or removed a string | Finding when a reading entered the text |
| `git log --grep="apparatus"` | Commits whose messages match a pattern | Retrieving all apparatus-related decisions |
| `git log --since="2026-10-01"` | Commits within a date range | Reconstructing a week's work for a report |

The `-S` option — the "pickaxe" — deserves particular attention, because it has
no analogue in ordinary file management and it answers a question philologists
ask constantly: *when did this reading enter the text, and who put it there?*
Given a form you are unsure about, `-S` returns exactly the commits that
introduced or removed it, and the commit body then supplies the rationale.

You will use these in Week 12, when the commentary layer requires you to justify
editorial decisions made two months earlier. Students who wrote informative
commit bodies retrieve their reasoning in seconds. Students who wrote "updates"
reconstruct it from memory, badly.

**Takeaway:** `git log` with `-S` and `--grep` turns the commit
history into a searchable record of editorial decisions.

---

## **19 Content**

**Reading Change with `git diff`**

Where `log` shows which commits exist, `diff` shows what they altered. It
operates between any two states Git knows about, which includes states you have
not committed.

| Invocation | Compares | Answers |
| --- | --- | --- |
| `git diff` | Working directory against index | What have I changed but not staged? |
| `git diff --staged` | Index against last commit | What exactly am I about to commit? |
| `git diff HEAD` | Working directory against last commit | What have I changed since the last commit? |
| `git diff abc123 def456` | Any two commits | What changed between these two states? |
| `git diff main..experiment` | Two branches | How does this editorial hypothesis differ? |

`git diff --staged` should become reflexive. It is the last check before a commit
becomes permanent, and it catches the two most common errors — staging a file you
did not intend to include, and failing to stage one you did.

For a scholarly edition, `git diff main..experiment` is the powerful case. It
renders the full difference between two complete editorial approaches as a
structured document — which is, precisely, an apparatus criticus generated
automatically from your own work. When in Week 6 you produce a hand-normalized
text and a script-normalized text, this command is how you will compare them.

**Takeaway:** `diff` compares any two states Git knows about,
including two competing editorial hypotheses on separate branches.

---

## **20 Content**

**Why the Default Diff Algorithm Fails on TEI XML**

Here the general-purpose tool meets the specialized material, and the fit is
poor. Git's default diff uses the Myers algorithm, designed for source code, in
which lines are typically long and distinctive. Its assumption is that matching
lines between two versions is a good proxy for corresponding content.

TEI XML violates that assumption comprehensively. Marked-up philological text is
densely nested and full of short, repetitive closing tags: `</w>`, `</rdg>`,
`</app>`, `</lem>`, each occurring hundreds of times and each identical to every
other instance. Presented with two versions, Myers finds enormous numbers of
equally valid alignments among these identical lines, and frequently selects one
that is minimal in edit distance but meaningless in structure — pairing the
closing tag of one apparatus entry with that of an entirely different one
(Angleraud et al., 2026).

The output is a diff that is technically correct and practically unreadable: a
scattering of additions and deletions spread across a region where one word
actually changed. A student reviewing such a diff cannot see what happened, and
so stops reviewing diffs. The audit trail is intact and useless — the failure
mode Huskey (2024) identifies as the real risk in version-controlled editing,
where the record exists but no one can read it.

This matters more than it may appear. Every verification practice in this course
— checking an HTR output against your ground truth, reviewing an AI-suggested
normalization, auditing a collation — depends on your ability to read a diff of
XML. If diffs are illegible, verification degrades into trust.

**Takeaway:** The default diff algorithm misaligns the
repetitive closing tags of TEI XML, producing accurate diffs that no one can
read.

---

## **21 Content**

**Patience and Histogram Diff**

The fix is to change algorithms, and Git ships with alternatives designed for
exactly this failure.

The **patience** algorithm inverts Myers' approach. Rather than seeking the
minimal edit script over all lines, it first discards every line that appears
more than once, computes the longest common subsequence over the *unique* lines
that remain, and only then fills in the gaps between those anchors. Because
`</app>` appears hundreds of times it is ignored as an anchor, while the distinct
line containing your actual reading is unique and anchors correctly. The result
aligns on meaningful content and keeps structural pairs together.

The **histogram** algorithm extends patience with a refinement to how it handles
lines of low occurrence, and is substantially faster on large files. For TEI work
it gives output of comparable quality to patience at better performance, and it
is the sensible default for this course.

Set it once, globally:

```bash
git config --global diff.algorithm histogram
```

Do this now, before your first transcription. The setting costs nothing, changes
no stored data — diff algorithms affect only how differences are *displayed*, not
what is recorded — and it is the difference between a reviewable edition and an
unreviewable one.

**Vocabulary.** *Longest common subsequence* — the longest sequence of elements
appearing in the same order in two sequences, not necessarily contiguously.
*Anchor* — a uniquely matching line used to align two versions before filling in
surrounding differences.

**Takeaway:** `diff.algorithm histogram` makes TEI diffs
legible by anchoring on unique lines instead of repetitive closing tags.

---

## **22 Content**

**Line Endings, `.gitattributes`, and Cross-Platform Collaboration**

A second infrastructural hazard is invisible until it destroys a week's diffs.
Operating systems disagree about how to end a line: Windows writes a carriage
return followed by a line feed (CRLF), while macOS and Linux write a bare line
feed (LF).

The consequence in a mixed-platform class is severe. A student edits one word of
a transcription on Windows and commits; their editor rewrites every line ending
in the file, and Git — which compares bytes — correctly reports that every line
changed. The one-word edit is now invisible inside a diff claiming the entire
document was rewritten. Nothing is corrupted, but the audit trail for that commit
is destroyed.

The remedy is a `.gitattributes` file at the repository root, which instructs Git
to normalize line endings on commit regardless of the committing platform:

```text
* text=auto eol=lf
*.xml text eol=lf
*.md text eol=lf
*.jpg binary
*.tif binary
```

Commit this file before anyone else touches the repository, so that normalization
applies from the beginning. The `binary` declarations matter too: they stop Git
from attempting line-ending conversion on facsimile images, which would corrupt
them outright.

`.gitattributes` also controls diff behaviour per file type, and you will extend
it in Week 8 when the apparatus layer makes XML-aware diffing worth configuring
specifically.

**Takeaway:** `* text=auto eol=lf` in `.gitattributes` prevents
platform line-ending differences from swamping your diffs.

---

## **23 Content**

**Pre-Commit Hooks: Automating Editorial Hygiene**

Some requirements are too easy to forget and too consequential to leave to
memory. Git's answer is the **hook**: a script that runs automatically at a
defined point in the Git workflow. A `pre-commit` hook runs immediately before a
commit is finalized, and if it exits with a non-zero status the commit is
aborted.

For a digital editing repository, two checks belong in that hook. The first is
Unicode normalization: a short script using Python's `unicodedata` library
rewrites all staged text into Normalization Form C before the commit proceeds
(Python Software Foundation, n.d.). The second is schema validation: the staged
XML is checked against the EpiDoc RelaxNG schema, so that a structurally invalid
file cannot enter the history at all (EpiDoc Guidelines, 2026; TEI Consortium,
2026).

Hooks live in `.git/hooks/` and must be executable. A minimal skeleton:

```bash
#!/bin/sh
# .git/hooks/pre-commit
python3 tools/normalize_nfc.py || exit 1
xmllint --noout --relaxng schema/tei-epidoc.rng edition/*.xml || exit 1
```

Note one consequence of where hooks live: `.git/hooks/` is *not* itself version
controlled, so hooks do not travel when a repository is cloned. Keep the scripts
in a tracked `tools/` directory and install them into `.git/hooks/` with a setup
script — otherwise your collaborators, and the instructor, will not have the
checks you rely on.

Why the second check matters will become clear in Week 8: a malformed XML file
breaks every downstream process in the pipeline, and the cost of catching it at
commit time is a few seconds, while the cost of discovering it three weeks later
is a re-encoding.

**Takeaway:** A pre-commit hook enforces normalization and
schema validity automatically, but hooks are not cloned — install them from a
tracked directory.

---

## **24 Content**

**Commit Trailers and the Documentation of AI Interventions**

This course will have you use machine assistance every Friday, and will require
you to measure it against your own work. That comparison depends on being able to
tell, unambiguously and later, which text a machine produced and which text you
produced. Memory will not supply this; the repository must.

Git's mechanism is the **trailer**: structured `Key: value` metadata on the final
lines of a commit message, which Git parses and can filter on (Conventional
Commits, n.d.). Every commit in this course that contains machine-generated or
machine-corrected content must carry trailers recording the fact.

```text
feat(transcription): add HTR output for ff. 42r-43v

Transkribus model trained on 8 pages of my own diplomatic transcription
(Week 4 Tuesday ground truth). Uncorrected model output; corrections
follow in a separate commit so that raw CER can be measured against
this state.

AI-Generated: true
Model: Transkribus / Text Titan I
Human-Verified: false
Ground-Truth-Commit: a3f9c21
```

The `Human-Verified: false` trailer is the one students most often omit and most
need. It marks text that has entered the repository but has *not* yet been
checked — the single most dangerous state for an edition, because unverified
machine output is indistinguishable on screen from verified transcription. A
later commit flips it to `true` once you have checked the passage against the
facsimile.

The requirement is not bureaucratic. Angleraud et al. (2026) document
vision-language models achieving a median character error rate of 1.0% on Greek
critical editions while simultaneously producing "catastrophic page-level
failures" — fluent, entirely fabricated Greek text with no relation to the image.
Output that good on average and that bad occasionally is precisely the kind that
must be labelled, because spot-checking will not find the failures.

**Takeaway:** Every commit containing machine-generated text
carries trailers recording the model, and whether a human has verified it.

---

## **25 Content**

**Auditing Provenance Programmatically**

Trailers earn their keep when the history is queried rather than read. Because
the metadata is structured, the whole repository can be interrogated for the
provenance of its contents (Huskey, 2024).

| Question | Command |
| --- | --- |
| Which commits introduced machine-generated text? | `git log --grep="AI-Generated: true"` |
| What remains unverified by a human? | `git log --grep="Human-Verified: false"` |
| Which models were used across the term? | `git log --pretty=format:"%(trailers:key=Model)"` |
| How much of the edition is machine-assisted? | `git rev-list --all --grep="AI-Generated: true" --count` |
| What did a given model contribute? | `git log --grep="Model: Transkribus"` |

The second query is the one to run habitually. It produces a live list of
everything in your edition that a machine wrote and you have not yet checked —
a work queue that maintains itself, and, at the end of term, a statement of
exactly how much of your edition rests on unverified automation.

This capability is the concrete form of the reproducibility argument. A reader of
your finished edition can ask what came from where and receive an answer derived
from the record rather than from your recollection. Cowen-Breen et al. (2023),
describing machine learning applied to premodern Greek, emphasize that the value
of such tools in scholarship depends on the scholar's ability to state precisely
where the machine's judgement enters — which is exactly what these trailers make
possible.

**Takeaway:** Structured trailers let you query your own
edition for what a machine wrote and what you have verified.

---

## **26 Content**

**Tags and Semantic Versioning for Published States**

Some states of an edition matter permanently: the version submitted for an
assignment, the version reviewed by a peer, the version published at term's end.
Commit hashes identify these perfectly but cite terribly — `a3f9c21` is not a
reference a reader can use. A **tag** attaches a durable name to a commit.

```bash
git tag -a v1.0.0 -m "Cataloguing and metadata assignment as submitted, Sep 18"
```

The `-a` flag creates an *annotated* tag, which is a full object in the database
carrying its own author, date, and message. Lightweight tags — created without
`-a` — are bare pointers with no metadata, and are not appropriate for anything
you intend to cite.

The Library of Digital Latin Texts applies semantic versioning to editions, and
this course follows the same scheme (Huskey, 2024):

| Component | Increments when | Editorial meaning |
| --- | --- | --- |
| Major (`2.0.0`) | Method or markup changes systemically | A different editorial approach to the same text |
| Minor (`1.1.0`) | Material is added without restructuring | New witnesses, apparatus entries, or commentary |
| Patch (`1.0.1`) | Localized errors are corrected | Typographic and encoding fixes only |

The payoff is citability with recoverable difference. A reviewer given `v1.0.0`
and `v2.0.0` can run `git diff v1.0.0..v2.0.0` and see the complete evolution of
your editorial thought between two published states — the precise capacity that
Giarratano's five print editions destroyed (Huskey, 2024).

**Takeaway:** Annotated tags with semantic versions give an
edition citable states whose differences remain machine-recoverable.

---

## **27 Content**

**Case Study: The Library of Digital Latin Texts**

The LDLT, operating under the Digital Latin Library, is the fullest realization
of the argument this lesson has been making, and it is worth examining as a model
for what your own repository is a small instance of.

The project's foundational commitment is the separation of the edition's *data*
from its *presentation*. A traditional critical edition fuses the two
irretrievably: the apparatus is a set of typographic conventions at the foot of a
page, and extracting the underlying scholarly claims from that layout is a manual
task. The LDLT instead maintains editions as TEI XML in Git repositories, from
which any number of presentations — print, web, machine-readable API — can be
generated. The edition is a database; the book is one view of it (Huskey, 2024).

This decoupling makes version control not merely useful but necessary. When the
edition is a printed artifact, "the edition" is unambiguous — it is the object on
the shelf. When the edition is a repository, identity must be established
explicitly, which is what the annotated tag and the semantic version supply.
The LDLT requires its editors to use both, so that any state of any edition can
be cited and retrieved exactly (Huskey, 2024).

The editorial workflow is correspondingly formalized. Editors work in branches;
changes arrive by pull request; review happens on the diff, with reviewers
commenting on specific lines of the proposed change. Peer review of an edition
thus operates on the *change* rather than on the finished object — reviewers see
not only what the editor concluded but what the editor altered and why. This is
the workflow you will practise in the Week 5 reconciliation exercise and in every
peer review thereafter.

**Takeaway:** The LDLT treats an edition as a versioned
database with citable releases, making peer review operate on changes rather than
on finished objects.

---

## **28 Content**

**Case Study: The Perseids Platform and Undergraduate Editing**

Perseids, developed at Tufts University in association with the Perseus Project,
demonstrates that the workflow in this lesson is achievable by undergraduates —
which is the relevant question for you this week (Almas & Beaulieu, 2012).

The platform was built to address a specific bottleneck: an enormous stock of
inscriptions and manuscripts that had never been transcribed or translated, and
a supply of students capable of the work but not of the infrastructure it
required. Perseids' response was to keep the scholarly rigour and absorb the
infrastructural burden. Underneath, it runs SoSOL, a papyrological editing
platform built directly on a Git repository, so that every student intervention
is a commit in a real version-controlled history (Almas & Beaulieu, 2012).

Two architectural choices are worth noting for your own work. First, texts are
addressed with CTS URNs — canonical identifiers that resolve to specific
hierarchical locations in a work, so that `urn:cts:greekLit:tlg0012.tlg001.
perseus-grc1:1.1` identifies a precise textual node independently of any file or
page. Second, transcriptions are linked to high-resolution facsimiles through an
open annotation model, so that each editorial claim is anchored to the image
evidence supporting it (Almas & Beaulieu, 2012). You will build both of these
relations for your own passage: CTS-style identifiers in Week 2, image
anchoring in Week 3.

The pedagogical result is the one this course is designed around. Because student
work arrives as reviewable commits on branches, the instructor can assess the
*process* — how a transcription developed, what was tried and abandoned, where
judgement was exercised — rather than only the final artifact. Your commit
history is part of what is being evaluated, and it is evidence of thinking that a
finished file cannot supply.

**Takeaway:** Perseids shows undergraduates producing genuine
version-controlled editions, with the commit history itself serving as evidence
of scholarly process.

---

## **29 Content**

**Interfaces, Accessibility, and Where Effort Should Go**

A caution against a misplaced emphasis. This lesson has used command-line
examples throughout, because commands are unambiguous to write down. It does not
follow that you must work at the command line.

The command line imposes real costs: syntax memorization, unforgiving error
messages, and a cognitive load that competes directly with the philological
thinking that is the actual point of the course. Huskey (2024) is explicit that
students should be permitted and encouraged to use graphical interfaces and
editor integrations for routine staging and committing, on the principle that
mental effort should be spent on textual problems rather than on tool syntax.

| Interface | Best suited to | Limitation |
| --- | --- | --- |
| Command line | Precise operations, scripting, hooks, unusual cases | Steep syntax burden; unhelpful errors |
| VS Code Git integration | Staging, committing, diff review during editing | Obscures what commands are actually run |
| Oxygen XML Git support | Committing without leaving the XML editor | Limited to common operations |
| GitHub Desktop | Visual staging and history browsing | Little support for hooks or advanced work |

The distinction to hold is between *understanding* and *typing*. You are
responsible for understanding the object model, the DAG, atomicity, and what a
commit records — that is conceptual knowledge, and it is examinable. Whether you
produce a commit by typing `git commit` or by clicking a button in VS Code is a
matter of preference, and the resulting commit is byte-identical either way.

Use the interface that leaves you the most attention for the manuscript. Reach
for the command line when you need something a graphical tool does not expose —
which will happen, particularly with hooks, trailers, and `-S` searches.

**Takeaway:** Understand the model conceptually; use whichever
interface leaves you the most attention for the philology.

---

## **30 Content**

**Synthesis: The Repository as Research Journal**

Everything in this lesson serves one claim, which Huskey (2024) states as the
thesis of version-controlled editing: a scholarly edition should be
reproducible and explainable, and the repository is the instrument that makes it
so.

*Reproducible* means that any state of the edition can be recovered exactly. The
content-addressable object store and the cascading hash chain provide this
absolutely — any commit can be checked out and will be byte-identical to the
state recorded. *Explainable* means that any decision can be traced to its
rationale. Nothing in Git provides this automatically; it is supplied entirely by
atomic commits, informative bodies, and honest trailers. The first property is
architectural, the second is a discipline, and only the second can be neglected —
which is exactly why it is what this course assesses.

The practices to carry into Week 2 and beyond:

- Commit atomically — one editorial act per commit, describable without "and".
- Type every commit with a Conventional Commits prefix that classifies the act.
- Write bodies that record evidence and reasoning, for the reader you will be in December.
- Trail every machine-assisted commit with its model and verification status.
- Tag every submitted state with an annotated semantic version.
- Configure `diff.algorithm histogram` and `.gitattributes` before the first transcription.

**Due this week.** Choose your manuscript passage by **Friday, September 4**. The
selection is ungraded, but every assignment from Week 2 to Week 13 builds on it,
so choose a passage with legible script, at least two available witnesses, and a
manageable length — twenty to forty lines. Record the choice and your reasons in
your repository's `README.md`, and commit it.

**Takeaway:** Reproducibility is guaranteed by Git's
architecture; explainability is guaranteed only by your commit discipline, which
is why the commit discipline is what is assessed.

---

## References

Almas, B., & Beaulieu, M.-C. (2012). Developing a new integrated editing
platform for source documents in classics. *Tufts University & Perseus Project*.

Angleraud, N., Karamolegkou, A., Sagot, B., & Clérice, T. (2026).
*Structure-aware text recognition for ancient Greek critical editions* (arXiv:
2603.02803v3). Inria.

Chacon, S., & Straub, B. (2014). *Pro Git* (2nd ed.). Apress.
https://git-scm.com/book/en/v2

Conventional Commits. (n.d.). *Conventional Commits specification v1.0.0*.
Retrieved from https://www.conventionalcommits.org/

Cowen-Breen, C., Brooks, C., Graziosi, B., & Haubold, J. (2023). Machine
learning and the future of philology: A case study. *Transactions of the American
Philological Association, 153*(1), 253–284.

EpiDoc Guidelines. (2026). *Critical apparatus*.
https://epidoc.stoa.org/gl/latest/supp-apparatus.html

Huskey, S. J. (2024). Committing to reproducibility and explainability: Using
Git as a research journal. *International Journal of Digital Humanities, 6*,
9–21. https://doi.org/10.1007/s42803-023-00076-9

Python Software Foundation. (n.d.). *unicodedata — Unicode database*. Python 3.12
documentation. https://docs.python.org/3/library/unicodedata.html

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange* (Version 4.12.0). https://tei-c.org/guidelines/p5/
