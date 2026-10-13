# Lesson 10.1 — Collaborative Git Workflows for Digital Textual Scholarship

*RELS 398 / ENGL 398 · Topic 10: Consolidation · Meeting #26 (Tue Nov 10)*

*Consolidation week — Wednesday November 11 is closed for Remembrance Day. This
week is a two-step consolidation pause with no new philological method. Today you
move from solitary local version control to distributed multi-editor workflows:
remotes, forks, branching strategies, pull requests as apparatus, and issue tracking.*

---

## **01 Content**

**The Mid-Term Consolidation Milestone**

Over the preceding nine weeks, you have constructed a multi-layered digital
scholarly edition from raw manuscript evidence. You began in Week 1 by
establishing a disciplined version-control habit and encoding Greek characters
under the strict Unicode standard. In Week 2 and Week 3, you catalogued your codex
within a structured `<teiHeader>` and mapped high-resolution digital facsimiles
through the International Image Interoperability Framework (IIIF). Weeks 4 through
9 executed the comparative philological cycle: transcribing primary witnesses by
hand and machine, reconciling double-keyed readings, normalizing historical
orthography, collating variant textual traditions, constructing a formal apparatus
criticus, and lemmatizing morphosyntax with grammatical metadata.

Each of these nine operations was performed as an isolated module within your
individual workspace. You worked primarily as a solitary editor, committing files
to a local Git repository and verifying that each discrete step satisfied its
immediate technical rubric. However, a digital scholarly edition is rarely the
product of an isolated scholar working in vacuum. Major critical editions—from the
*Nestle-Aland* Novum Testamentum Graece to large-scale digital archives—are
collective, cumulative undertakings requiring dozens of philologists, encoders,
and paleographers to harmonize their labor across years of research (Witt, 2018).

Week 10 pauses the introduction of new philological methods to address the
essential problem of collaborative synthesis. Wednesday is closed for Remembrance
Day, making this week a two-step consolidation pause by design. Today's meeting
transforms your isolated local repositories into networked nodes within a shared,
distributed editorial ecosystem. You will learn the mechanics of remote
repositories, forks, feature branching, pull requests, and issue tracking,
reframing software engineering workflows as rigorous instruments of collaborative
textual scholarship.

**Takeaway:** Consolidation is not an administrative pause but an
essential editorial synthesis where nine isolated methodological layers are
integrated into a collaborative, multi-editor digital critical edition.

---

## **02 Content**

**From Solitary Editor to Distributed Textual Community**

The traditional image of the textual critic is a solitary scholar seated in an
archive, manually collating physical codices and recording variant readings in
private notebooks. In nineteenth-century Lachmannian stemmatics, the editor acted
as a sovereign arbiter who single-handedly reconstructed the hypothetical
*archetype* or *Urtext* through solitary recension and emendation. When early
digital humanities projects emerged in the late twentieth century, they frequently
replicated this centralized, solitary model: individual researchers encoded
documents in siloed desktop applications, saving bespoke XML or SGML files onto
local hard drives or exchanging drafts via email attachments (Huskey, 2024).

This solitary paradigm introduced catastrophic vulnerabilities. Digital editions
constructed in desktop isolation suffered from extreme fragmentation, idiosyncratic
encoding habits, and rapid digital entropy. When a lead editor retired or grant
funding expired, the bespoke databases and unversioned files decayed, rendering
the scholarly output inaccessible to future researchers (Holmes & Turska, 2023).
Furthermore, exchanging unversioned documents via email produced conflicting
editorial files, overwritten transcriptions, and an untraceable provenance
history.

Distributed version control systems fundamentally dissolve this isolation. By
shifting from centralized desktop storage to distributed Git architectures,
textual scholarship becomes an open, communal enterprise (Witt, 2018). In a
distributed workflow, every participant holds a complete, self-contained record of
the entire editorial history. Multiple scholars can transcribe distinct folios,
debate thorny paleographical readings, and propose variant normalizations
simultaneously without risking data loss or stepping on each other's work. The
edition ceases to be a static, closed book produced by a solitary authority and
becomes a dynamic, living research corpus curated by a transparent community of
scholars (Almas & Beaulieu, 2013).

**Takeaway:** Modern digital textual scholarship replaces
solitary desktop curation with distributed, transparent collaboration, ensuring
data preservation, traceable provenance, and communal editorial adjudication.

---

## **03 Content**

**The Directed Acyclic Graph: The Abstract Topology of Git**

To collaborate effectively without corrupting scholarly data, editors must
understand the underlying mathematical structure that governs distributed version
control. In Lesson 1.1, you learned that Git does not track file differences as
disjointed delta patches; instead, it records a sequence of complete project
snapshots. Mathematically, these snapshots form a **Directed Acyclic Graph
(DAG)**, a network of nodes connected by directional edges that never loop back on
themselves (Huskey, 2024).

In Git's DAG, each node represents a commit—an immutable snapshot of the entire
repository at a specific point in time. Each commit node contains cryptographic
metadata: a 40-character SHA-1 (or newer SHA-256) hash representing the exact
content of the tree, the author's identity, a timestamp, a descriptive commit
message, and one or more parent pointers directed toward previous nodes. Because
each commit points backward to its parent, history moves forward along directed
branches that can diverge and later merge, but can never cycle backward into an
infinite loop.

| DAG Component | Mathematical Role | Philological Equivalent in Textual Editing |
|---|---|---|
| **Node (Commit)** | Immutable state snapshot identified by hash | A dated, attributed transcription or encoding milestone |
| **Directed Edge** | Pointer from child commit to parent commit | The genealogical lineage connecting an edited state to its exemplar |
| **Branch** | Named, movable pointer to a specific node | An independent editorial line or experimental hypothesis |
| **Merge Node** | Node possessing two or more parent pointers | The formal synthesis of two independent editorial streams |

This cryptographic DAG structure provides an extraordinary guarantee for
philologists: immutability. If a single character, punctuation mark, or XML tag in
a transcribed manuscript is altered, its resulting cryptographic hash changes
entirely, cascading across all subsequent nodes. Consequently, a Git repository
provides mathematically verifiable provenance for every reading in your edition,
guaranteeing that editorial interventions cannot be altered retroactively or
erased without detection (Himmelstein et al., 2019).

**Takeaway:** Git's Directed Acyclic Graph models textual
transmission as an immutable network of cryptographic nodes, ensuring permanent
provenance and citation stability for every editorial intervention.

---

## **04 Content**

**The Anatomy of Remotes: Local Clones and Remote Repositories**

Up to this point in the course, your Git operations have been strictly local. When
you executed `git commit`, Git recorded snapshot nodes entirely within the hidden
`.git` directory on your personal machine. In a collaborative project, however,
scholars must synchronize their local graphs with one or more **remote
repositories** hosted on network servers such as GitHub (Witt, 2018).

A remote repository is not a privileged, magical master server in the traditional
client-server database sense. In Git's distributed architecture, a remote is
simply another copy of the repository's Directed Acyclic Graph residing at a network
URL. The standard default name Git assigns to the primary remote from which a
repository was cloned is `origin`. In multi-editor projects, however, teams
typically establish an additional remote named `upstream`, which points to the
authoritative, canonical repository managed by the course instructor, principal
investigator, or editorial board (Faghihi et al., 2022).

Understanding the movement of data between these environments requires tracking
four distinct storage zones on your computer and the network:

1. **Working Directory:** The physical files on your local drive that you directly
   edit in VS Code with XML extensions.

2. **Staging Area (Index):** The local preparation zone where you gather specific
   modified files (`git add`) prior to committing.

3. **Local Repository:** The hidden `.git` database on your machine storing your
   committed snapshot nodes and branch pointers.

4. **Remote Repository (`origin`/`upstream`):** The external repository hosted on
   GitHub that receives your pushed commits (`git push`) and supplies external
   updates (`git fetch`).

**Takeaway:** A Git remote is an external peer repository used to
synchronize Directed Acyclic Graphs across distributed editors, mediated through
local working trees, staging indexes, and remote tracking branches.

---

## **05 Content**

**Collaboration Models: Shared Write Access vs. Fork-and-Pull**

When organizing a multi-editor scholarly project, teams must choose how
contributors will submit their work. In software engineering and digital
humanities, two primary collaboration models exist: the **Shared Repository Model**
(direct write access) and the **Fork-and-Pull Model** (distributed sandboxes)
(Himmelstein et al., 2019).

In the Shared Repository Model, every team member is granted direct push
permissions to a single central repository. Contributors clone the repository,
create branches locally, and push those branches directly to the central remote.
While this model works well for small, tightly knit teams of senior software
engineers, it is hazardous in large digital scholarly editing projects. A single
accidental force-push (`git push --force`) or an improperly merged branch by an
inexperienced encoder can overwrite canonical TEI files, corrupt commit histories,
or break XML schema validation across the entire corpus (Almas & Beaulieu, 2013).

```
Shared Model:      [Contributor A] ---> ( Direct Push ) ---> [ Canonical Repo ]
                   [Contributor B] ---> ( Direct Push ) ---> [ Canonical Repo ]

Fork-and-Pull:     [Contributor A] ---> [ Fork A (Remote) ] ---> ( Pull Request ) ---> [ Canonical ]
                   [Contributor B] ---> [ Fork B (Remote) ] ---> ( Pull Request ) ---> [ Canonical ]
```

The **Fork-and-Pull Model** eliminates these hazards and is the universal standard
for open-source software, large-scale digital humanities initiatives, and
classroom environments (Faghihi et al., 2022). Under this model, contributors do not
possess write access to the canonical repository. Instead, each editor creates a
personal, server-side clone—a **fork**—under their own GitHub account. Contributors
push changes freely to their personal forks and then submit a formal **Pull
Request (PR)** asking the project maintainers to pull and merge the verified
changes into the canonical repository.

**Takeaway:** The fork-and-pull model isolates experimental
editorial work within personal sandboxes, protecting the canonical corpus from
accidental data corruption while enabling open, distributed collaboration.

---

## **06 Content**

**Forking a Scholarly Repository on GitHub**

Forking is not a native Git command-line operation; it is a platform-level feature
pioneered by GitHub and GitLab that orchestrates server-side repository
duplication while maintaining a permanent upstream lineage pointer (Himmelstein et
al., 2019). When you click the "Fork" button on an upstream repository, GitHub
instantly creates an identical copy of the repository's Directed Acyclic Graph
under your personal user account.

Your fork is a fully autonomous repository. You possess complete administrative and
write privileges over it. You can create experimental branches, modify TEI schema
rules, refactor directory layouts, and commit imperfect transcription drafts
without any danger of altering the upstream project. Yet, because GitHub tracks the
parentage of the fork, your repository remains permanently aware of the upstream
canonical source, enabling seamless bidirectional synchronization (Faghihi et
al., 2022).

In a digital humanities pedagogy context, forking provides students with an
ideal, low-anxiety sandbox. Beginners often suffer from computational apprehension,
fearing that a syntax error or a botched Git command will destroy their peers'
scholarly labor (Faghihi et al., 2022). Forking eliminates this anxiety entirely:
students experiment freely within their personal forks, safe in the knowledge that
no change can alter the canonical edition until it has been explicitly reviewed,
validated, and accepted through a structured pull request.

**Vocabulary.** *Fork* — a platform-level server-side clone of an upstream
repository hosted under a contributor's personal account. *Upstream* — the
authoritative, primary repository from which personal forks are derived.

**Takeaway:** Forking provides an autonomous personal sandbox
for experimental editorial labor while maintaining the genealogical linkage
necessary for upstream contribution.

---

## **07 Content**

**Branching Topologies in Textual Scholarship**

A common pitfall in novice version control is committing all work directly to the
default `main` (or `master`) branch. In a collaborative scholarly edition, this
practice quickly leads to chaos. If an editor commits an unverified transcription
draft, an experimental normalization script, and an incomplete apparatus
simultaneously to `main`, it becomes impossible to isolate and merge one verified
feature without dragging unvetted or broken files along with it.

To maintain editorial rigor, collaborative DH projects rely on structured
**branching topologies** (Weigl et al., 2024). A branch in Git is simply a lightweight,
movable pointer to a specific commit node in the DAG. Creating a branch costs
virtually zero disk space and takes milliseconds, yet it establishes an isolated
context where an editor can pursue a single, well-defined philological task.

| Branch Type | Topology Role | Content and Lifecycle |
|---|---|---|
| **Mainline (`main`)** | Production / Canonical | Contains only vetted, schema-validated, peer-reviewed edition layers. Never committed to directly. |
| **Feature Branch** | Editorial Topic / Folio | Dedicated to a single discrete task (e.g. `transcribe-folio-12r`). Deleted immediately upon merge. |
| **Fix Branch** | Targeted Correction | Created to repair a specific error, such as fixing an invalid XML tag or a misread Greek lemma. |
| **Release Branch** | Milestone Snapshot | Named tags or branches representing frozen publication states (e.g. `release-v1.0-diplomatic`). |

By dedicating each feature branch to a single philological unit—such as
transcribing a specific manuscript quire or encoding variant readings for a single
chapter—editors ensure that each contribution can be reviewed, debugged, and
merged independently of all other ongoing work (Witt, 2018).

**Takeaway:** Feature branches isolate discrete editorial tasks
into independent streams, ensuring the `main` branch remains clean, stable, and
continuously publishable.

---

## **08 Content**

**Branch Naming Conventions and Repository Hygiene**

Because a multi-editor project may contain dozens of active branches simultaneously,
teams must enforce strict, semantic **branch naming conventions**. Ambiguous names
like `my-edits`, `updates`, `test`, or `fixes` convey zero philological context and
force maintainers to guess what data the branch contains.

Disciplined digital editing projects establish standardized prefixes that
categorize the nature and scope of the editorial intervention (Weigl et al., 2024).
Common conventions include:

- `transcribe/<witness>-<folio>` (e.g. `transcribe/codex-b-fol-04r`)

- `norm/<chapter>-<section>` (e.g. `norm/romans-08-01-15`)

- `apparatus/<witness-group>` (e.g. `apparatus/byzantine-collation`)

- `lemma/<linguistic-layer>` (e.g. `lemma/pos-tagging-q1`)

- `fix/<issue-number>-<short-description>` (e.g. `fix/42-unclosed-choice-tag`)

```bash
# Good practice: semantic, scoped, contextual branch names
git checkout -b transcribe/ms-a-folio-14v
git checkout -b lemma/greek-participles-ch3
git checkout -b fix/issue-18-milestone-nesting

# Bad practice: vague, uninformative names
git checkout -b new-work
git checkout -b edits2
git checkout -b ken-branch
```

Maintaining **repository hygiene** also requires retiring branches once their
contributions have been merged into `main`. Stale, abandoned branches clutter the
repository topology, confuse collaborators, and increase the likelihood of
re-introducing obsolete readings. Once a pull request is merged, its associated
feature branch should be promptly deleted from both the local machine and the
remote fork.

**Takeaway:** Semantic branch naming conventions communicate
editorial intent instantly, while prompt deletion of merged branches preserves
repository clarity and historical hygiene.

---

## **09 Content**

**Configuring and Managing Remotes via the Command Line**

To participate in a collaborative fork-and-pull workflow, you must configure your
local Git installation to communicate with two distinct remote endpoints: your
personal GitHub fork (`origin`) and the shared canonical class repository
(`upstream`) (Faghihi et al., 2022).

When you initially clone your personal fork to your local workstation, Git
automatically registers that fork as the remote named `origin`. You can verify
this configuration by querying your existing remotes with the verbose flag:

```bash
git remote -v
# Output:
# origin  https://github.com/<your-username>/RELS398.git (fetch)
# origin  https://github.com/<your-username>/RELS398.git (push)
```

To establish a communication bridge with the canonical project repository, you must
manually add a second remote named `upstream` using the `git remote add` command:

```bash
# Add the canonical upstream class repository
git remote add upstream https://github.com/kmpenner/RELS398.git

# Verify that both remotes are now registered
git remote -v
# Output:
# origin    https://github.com/<your-username>/RELS398.git (fetch)
# origin    https://github.com/<your-username>/RELS398.git (push)
# upstream  https://github.com/kmpenner/RELS398.git (fetch)
# upstream  https://github.com/kmpenner/RELS398.git (push)
```

With both remotes configured, your local workstation becomes a bridge: you will
fetch updates from `upstream` to stay synchronized with your peers, while pushing
your personal editorial branches exclusively to `origin`.

**Takeaway:** Mapping both `origin` (personal fork) and `upstream`
(canonical repository) enables bidirectional synchronization between individual
editorial labor and the broader collaborative project.

---

## **10 Content**

**Synchronizing with Upstream: Fetch, Merge, and Rebase**

In a collaborative project, the canonical `upstream` repository is continually
moving forward as peers merge verified pull requests. If you allow your local
repository and personal fork to fall behind `upstream`, you will eventually attempt
to merge outdated XML files, triggering severe merge conflicts. Regular
synchronization is therefore an essential daily discipline (Huskey, 2024).

Synchronizing your repository involves two distinct operations: **fetching** and
**merging**. The command `git fetch upstream` downloads all new commits, branches,
and tags from the canonical repository into your local `.git` database without
modifying any of your working files. These updates land in remote tracking
branches, such as `upstream/main`.

```bash
# 1. Fetch all new commits from the canonical upstream repository
git fetch upstream

# 2. Switch to your local main branch
git checkout main

# 3. Fast-forward your local main branch to match upstream/main
git merge upstream/main

# 4. Push the synchronized main branch up to your personal GitHub fork
git push origin main
```

Philological projects must also consider the choice between `git merge` and `git
rebase`. When integrating upstream updates into an active feature branch, `git
merge` creates a visible merge commit that explicitly records the historical moment
of integration. Conversely, `git rebase` rewinds your local commits, replays them
on top of the latest upstream state, and produces a linear history (Huskey, 2024).
While rebasing yields clean, linear commit logs, merging preserves the true
chronological record of transmission. In textual scholarship, where data provenance
is paramount, explicit merge commits are widely preferred.

**Takeaway:** Regularly fetching and merging `upstream/main`
keeps your local environment synchronized with canonical project updates,
preventing drift and minimizing downstream merge collisions.

---

## **11 Content**

**The Pull Request as the Dynamic Apparatus Criticus**

In traditional print scholarship, the **apparatus criticus** sits at the foot of
the page, presenting a dense, highly abbreviated summary of variant readings and
editorial emendations. While indispensable, the print apparatus is fundamentally
static and post-facto: it records the final, frozen verdicts of the editor,
discarding the rich scholarly debates, rejected hypotheses, and paleographical
arguments that occurred during the edition's preparation (Huskey, 2024).

The GitHub **Pull Request (PR)** reimagines the apparatus criticus as a dynamic,
interactive, and permanent scholarly forum (Witt, 2019). When an editor submits a
pull request, they are not merely requesting that a technical file be copied into a
folder; they are formally presenting a scholarly hypothesis to the editorial board
for peer review.

> **Pull Request #14: Encode variant apparatus for Romans 8:28 in Codex B**
> *Author:* `@student_encoder` · *Reviewers:* `@senior_editor`, `@peer_reviewer`
>
> **Description:** This PR supplies the diplomatic transcription and variant
> apparatus for Romans 8:28, encoding the reading "πάντα συνεργεῖ ὁ θεός" found in
> P46 and Vaticanus against the majority Byzantine text.
>
> **Automated CI Status:** `Passed: RELAX NG & Schematron`
> **Inline Peer Review:** 4 comments debated; consensus reached on `<choice>`.

Within the PR interface, every line of proposed TEI XML is exposed to granular,
line-by-line scrutiny. Senior editors and peer reviewers can highlight specific XML
elements, query a doubtful letter reading, request corroborating IIIF facsimile
links, or debate whether an editorial intervention should be marked as `<corr>` or
`<reg>` (Witt, 2018). Once accepted, the entire PR conversation—including all
debated revisions and reviewer approvals—remains permanently archived and linked to
the merge commit, creating a fully transparent audit trail of editorial reasoning.

**Takeaway:** A pull request is a dynamic apparatus criticus,
transforming code review into an attributed, transparent forum for collaborative
philological debate and editorial adjudication.

---

## **12 Content**

**Anatomy of a Scholarly Pull Request**

Submitting an effective pull request requires both technical discipline and
philological rhetoric. A poorly constructed PR—featuring a vague title, no
explanatory context, and hundreds of unrelated edits sprawled across multiple
unconnected files—overwhelms reviewers and brings collaborative adjudication to a
halt (Himmelstein et al., 2019).

A model scholarly pull request adheres to the principle of **atomicity**. An
atomic PR addresses a single, tightly scoped editorial task: transcribing one
specific folio, adding morphological tags to a defined passage, or fixing a broken
schema pointer. By keeping the PR small and focused, the contributor makes it
straightforward for peers to review the diff line-by-line, verify schema
compliance, and provide prompt feedback.

Every scholarly PR should include four essential components:

1. **Descriptive Title:** A clear summary naming the manuscript, passage, and
   editorial operation (e.g., `Transcribe and encode apparatus for Folio 14v (Codex
   Alexandrinus)`).

2. **Philological Summary:** A prose paragraph explaining what text was encoded,
   what paleographical challenges were encountered, and what editorial principles
   were applied.

3. **Issue Linkage:** Explicit reference to related tracking issues using GitHub's
   automation keywords (e.g., `Closes #18`, `Resolves #24`).

4. **Self-Audit Verification:** Confirmation that the contributor has validated the
   XML locally, checked facsimile alignments, and verified that all tags conform to
   project schemas.

**Takeaway:** An effective pull request is atomic, tightly
scoped, and thoroughly documented, facilitating rapid, rigorous peer evaluation.

---

## **13 Content**

**Standardizing Editorial Contributions: `PULL_REQUEST_TEMPLATE.md`**

In large collaborative projects, maintainers cannot rely on contributors
remembering every required self-audit step from memory. To enforce consistent
editorial rigor, GitHub repositories utilize a standardized **Pull Request
Template** (`.github/PULL_REQUEST_TEMPLATE.md`) (Faghihi et al., 2022).

When a contributor opens a new pull request on GitHub, the platform automatically
populates the PR description box with the markdown structure defined in the
template file. This transforms the submission process into a structured,
self-guiding rubric that prompts the contributor to certify their work before
requesting human review.

```markdown
<!-- .github/PULL_REQUEST_TEMPLATE.md -->
### Editorial Summary
*Provide a concise summary of the manuscript witness, folio range, and TEI layers modified.*

### Related Issues
*Closes #*

### Contributor Self-Audit Checklist
- [ ] **Well-Formedness:** XML is well-formed and parses with zero syntax errors.
- [ ] **Schema Compliance:** Validated locally against the project RELAX NG schema (`jing`).
- [ ] **Business Rules:** Validated against project ISO Schematron rules (`saxon`).
- [ ] **Facsimile Alignment:** Every `<pb/>` and `<lb/>` accurately corresponds to the IIIF manifest.
- [ ] **Philological Precision:** All editorial interventions (`<corr>`, `<supplied>`, `<reg>`) are justified.
- [ ] **Provenance:** `<revisionDesc>` has been updated with author name, date, and change description.
```

By embedding these checklists directly into the repository infrastructure, projects
ensure that basic technical quality control occurs prior to peer review, freeing
human reviewers to concentrate on paleographical and interpretive matters (Witt,
2018).

**Takeaway:** Pull request templates standardize submission
protocols, embedding self-audit checklists directly into the collaborative
workflow to guarantee baseline data integrity.

---

## **14 Content**

**Visualizing Diffs in Hierarchical XML Documents**

The central visual interface of a pull request is the **diff** (difference) view,
which renders a side-by-side or unified comparison of the original text against the
proposed modifications. In standard software development, diffs compare flat lines
of code. In digital humanities, however, diffing hierarchical TEI XML documents
presents unique interpretive challenges (Huskey, 2024).

Standard Git diffs operate on a line-by-line basis. If an encoder alters a single
word inside a 100-word paragraph formatted as a single continuous line, standard
diff engines highlight the entire line as deleted and replaced, obscuring the exact
point of editorial emendation. To inspect granular textual changes, scholars use
specialized diff flags:

```bash
# Display word-level differences inline rather than whole-line replacements
git diff --word-diff

# Highlight word changes using color highlights without line duplication
git diff --word-diff=color

# Ignore cosmetic whitespace and indentation changes to focus on textual content
git diff --ignore-all-space
```

| Diff Display Mode | Mechanism | Scholarly Utility in TEI Editing |
|---|---|---|
| **Standard Line Diff** | Compares whole lines between commits | Ideal for tracking structural additions (new `<sp>`, `<p>`, `<lg>`) |
| **Word-Level Diff** | Compares token-by-token within lines | Pinpoints precise orthographic corrections or lemma adjustments |
| **Whitespace-Agnostic** | Ignores space and indentation changes | Distinguishes substantive textual edits from cosmetic XML re-indentation |

Understanding how diffs render hierarchical trees allows reviewers to quickly
verify whether an edit altered only the text string, modified semantic attribute
values (such as changing `@ana="#noun"` to `@ana="#verb"`), or reorganized the
underlying XML hierarchy (Huskey, 2024).

**Takeaway:** Mastering word-level and whitespace-aware diffs
allows reviewers to isolate substantive philological emendations from cosmetic XML
formatting changes.

---

## **15 Content**

**The Scholarly Code Review Interface**

GitHub's code review interface provides a comprehensive suite of tools for
conducting granular, asynchronous peer review on proposed TEI XML files. Rather than
writing general feedback in an external document, reviewers engage directly with the
underlying markup (Faghihi et al., 2022).

By hovering over any line number in the PR diff view, a reviewer can click the blue
`+` icon to open an inline comment box. Reviewers can highlight single lines or drag
across multi-line code spans to critique entire XML structures, such as an
apparatus entry (`<app>`) or a manuscript description block (`<msDesc>`).

```xml
<!-- Proposed markup in Pull Request #14 -->
<choice>
  <sic>καρδια</sic>
  <corr>καρδίᾳ</corr>
</choice>
```

> **Reviewer Comment from `@peer_reviewer`:**
> "Looking closely at the IIIF facsimile (canvas #12 at high zoom), there is a
> faint iota subscript visible beneath the alpha. This should be encoded as
> `<orig>καρδίᾳ</orig>` rather than a scribal error requiring editorial `<corr>`."
>
> **Suggested Replacement:** `<orig>καρδίᾳ</orig>`

Reviewers can utilize GitHub's **Suggested Changes** syntax (fenced code blocks
labeled `suggestion`). When a suggestion is inserted, GitHub renders a one-click
"Apply suggestion" button for the PR author, allowing them to accept and commit the
corrected markup directly from the web interface without touching their local
terminal (Himmelstein et al., 2019). When finishing a review, the evaluator can
select one of three formal dispositions: *Comment* (general feedback), *Approve*
(ready to merge), or *Request Changes* (blocking merge until critical defects are
resolved).

**Takeaway:** Inline review comments and direct markdown
suggestions turn the pull request diff into an active workspace for collaborative
paleographical correction and markup refinement.

---

## **16 Content**

**Iterating on an Open Pull Request**

A common misconception among beginner digital editors is that once a pull request is
opened, it is frozen in time, and any required corrections require closing the PR
and starting over from scratch. In reality, a pull request is a dynamic, live window
into the underlying feature branch (Faghihi et al., 2022).

When a reviewer requests changes on your PR—for instance, pointing out an unescaped
Greek accent or an invalid Schematron attribute—you do not open a new pull request.
Instead, you simply return to your local workstation, switch to the active feature
branch, make the necessary corrections in your text editor, and commit the fixes:

```bash
# 1. Ensure you are on the correct feature branch
git checkout transcribe/ms-a-folio-14v

# 2. Edit the TEI XML file to address reviewer feedback
# (e.g. fix the <orig> tag in VS Code)

# 3. Stage and commit the correction with a clear commit message
git add src/modules/Topic_04_Transcription/ms_a_folio_14v.xml
git commit -m "Address review feedback: replace sic/corr with orig based on IIIF zoom"

# 4. Push the commit to your personal fork
git push origin transcribe/ms-a-folio-14v
```

The moment you execute `git push`, GitHub automatically detects the new commit on
your remote branch and appends it to the open pull request thread. The diff view
updates dynamically, the automated validation pipelines re-run, and the reviewer is
notified that the requested modifications have been implemented. This iterative
feedback loop continues until the edition meets all scholarly standards and receives
formal approval (Weigl et al., 2024).

**Takeaway:** Pushing new commits to an active feature branch
automatically updates the open pull request, supporting a seamless, iterative
dialogue between contributor and reviewer.

---

## **17 Content**

**Merge Conflicts in Hierarchical Tree Structures**

When multiple editors work simultaneously on the same text corpus, their
contributions will inevitably collide, resulting in a **merge conflict**. A merge
conflict occurs when Git cannot automatically reconcile differences between two
branches because both branches have modified the exact same lines of a file since
their common ancestor commit (Huskey, 2024).

In programming languages like Python or C, merge conflicts are often localized and
straightforward: two developers may have edited different functions or adjusted
variable names on the same line. In digital scholarly editing, however, merge
conflicts in TEI XML documents pose severe structural hazards because XML documents
are governed by the strict nesting rules of the **Ordered Hierarchy of Content
Objects (OHCO)** model (Renear et al., 1996).

```xml
<!-- Contributor A Branch: Added semantic name tagging -->
<p>In the beginning was the <persName ref="#logos">Word</persName>...</p>

<!-- Contributor B Branch: Added morphological apparatus -->
<p>In the beginning was the <app><rdg wit="#A">Word</rdg><rdg wit="#B">Reason</rdg></app>...</p>
```

If Git's raw text-matching algorithm attempts to interleave these two edits
naively, it will produce malformed XML containing overlapping elements, unclosed
tags, or mismatched attribute namespaces (Renear et al., 1996; McGann, 2014). An
improperly resolved XML merge conflict instantly destroys the document's
well-formedness, crashing parsers, breaking publication pipelines, and halting
continuous integration builds. Resolving XML conflicts therefore demands deep
philological understanding alongside rigorous structural awareness.

**Takeaway:** Merge conflicts in TEI XML documents threaten the
validity of hierarchical tree structures and cannot be resolved mechanically
without careful philological and syntactic adjudication.

---

## **18 Content**

**Anatomy of a Git Conflict in TEI XML**

When a merge conflict occurs, Git halts the merge process, leaves your working
directory in an uncommitted conflict state, and injects visible **conflict
markers** directly into the affected files (Huskey, 2024). Understanding how to
read these markers is an essential technical skill for every digital editor.

A Git conflict block is divided into three distinct zones separated by seven-character
delimiters:

```xml
<<<<<<< HEAD
<w lemma="λόγος" ana="#noun_masc_nom_sg">λόγος</w>
<app>
  <rdg wit="#CodexA">ἦν πρὸς τὸν θεόν</rdg>
</app>
=======
<w lemma="λόγος" ana="#noun_masc_nom_sg">λόγος</w>
<app>
  <rdg wit="#CodexA #CodexB">ἦν πρὸς τὸν θεόν</rdg>
  <rdg wit="#CodexC">ἦν μετὰ τοῦ θεοῦ</rdg>
</app>
>>>>>>> upstream/main
```

1. `<<<<<<< HEAD`: Marks the start of the conflict block and contains the lines
   currently present on your local checkout branch (your version).

2. `=======`: The central dividing line separating the two competing editorial
   hypotheses.

3. `>>>>>>> upstream/main` (or branch name): Marks the end of the conflict block and
   contains the incoming lines from the branch being merged (the conflicting
   version).

Everything between `<<<<<<<` and `=======` represents your local reading, while
everything between `=======` and `>>>>>>>` represents the incoming remote reading.
To resolve the conflict, you must manually edit the text to synthesize the correct
combined reading and completely delete all seven-character marker lines before
saving (Huskey, 2024).

**Takeaway:** Git conflict markers explicitly delimit competing
editorial readings, providing the raw evidence needed to synthesize a valid,
consensus XML tree.

---

## **19 Content**

**Modular Architecture and Conflict Mitigation**

While Git provides robust tools for resolving merge conflicts, the most effective
editorial strategy is to design a repository architecture that prevents conflicts
from occurring in the first place. In monolithic digital editions—where an entire
multi-volume work or manuscript codex is stored inside a single massive XML file
spanning thousands of lines—merge conflicts become a constant, crippling
bottleneck (TEI Consortium, 2026).

To eliminate this vulnerability, mature digital humanities projects implement a
**modular document architecture** (Witt, 2018). Instead of maintaining one gigantic
XML file, the text is decomposed into small, logical units: one XML file per folio,
per poem, or per chapter. These modular child files are then dynamically synthesized
into a complete composite document using the W3C **XInclude (`<xi:include>`)**
standard (TEI Consortium, 2026).

```xml
<!-- Master Composite File: text_corpus_master.xml -->
<TEI xmlns="http://www.tei-c.org/ns/1.0" xmlns:xi="http://www.w3.org/2001/XInclude">
  <teiHeader>
    <xi:include href="header/master_teiHeader.xml"/>
  </teiHeader>
  <text>
    <body>
      <div type="folio" n="12r">
        <xi:include href="transcriptions/folio_12r.xml"/>
      </div>
      <div type="folio" n="12v">
        <xi:include href="transcriptions/folio_12v.xml"/>
      </div>
    </body>
  </text>
</TEI>
```

Under this modular architecture, Editor A can transcribe `folio_12r.xml` on one
branch while Editor B lemmatizes `folio_12v.xml` on another. Because the two editors
are modifying completely separate physical files on disk, Git merges both feature
branches automatically with zero merge collisions (Witt, 2018).

**Takeaway:** Modularizing large texts into discrete, folio-level
files assembled via W3C XInclude drastically reduces merge collisions and allows
distributed teams to edit concurrently.

---

## **20 Content**

**Step-by-Step Manual Conflict Resolution**

When a merge conflict does occur in your TEI files, resolving it requires a
disciplined, four-step protocol. Attempting to resolve conflicts haphazardly in a
state of panic often introduces malformed XML or accidentally deletes valid
transcriptions (Huskey, 2024).

| Step | Terminal Operation | Action and Verification |
|---|---|---|
| **1. Identify Conflicted Files** | `git status` | Look under "Unmerged paths" to see which exact `.xml` files contain collision markers. |
| **2. Inspect and Adjudicate** | Open file in VS Code | Locate each `<<<<<<< HEAD` block. Evaluate both readings against the IIIF facsimile, combine valid markup, and delete all conflict markers. |
| **3. Validate Well-Formedness** | `xmllint --noout <file>` | Verify that your manual edits did not unbalance tags or break basic XML syntax rules. |
| **4. Stage and Conclude Merge** | `git add <file>`<br>`git commit` | Staging the file informs Git that the conflict has been resolved. Committing completes the merge node. |

Let us trace this protocol in the terminal. When you attempt a merge that
conflicts, Git reports:

```bash
$ git merge upstream/main
Auto-merging src/modules/Topic_04_Transcription/ms_a_folio_14v.xml
CONFLICT (content): Merge conflict in src/modules/Topic_04_Transcription/ms_a_folio_14v.xml
Automatic merge failed; fix conflicts and then commit the result.

# Step 1: Confirm the conflicted file
$ git status
Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   src/modules/Topic_04_Transcription/ms_a_folio_14v.xml

# Step 2: Open ms_a_folio_14v.xml, reconcile tags, remove <<<<<<<, =======, >>>>>>>
# Step 3: Validate syntax immediately
$ xmllint --noout src/modules/Topic_04_Transcription/ms_a_folio_14v.xml

# Step 4: Stage and commit the resolution
$ git add src/modules/Topic_04_Transcription/ms_a_folio_14v.xml
$ git commit -m "Reconcile merge conflict in Folio 14v: combine lemma tags with variant apparatus"
```

**Takeaway:** Resolving an XML merge conflict requires
synthesizing competing readings, deleting all conflict markers, verifying XML
well-formedness, and concluding the merge with a descriptive commit.

---

## **21 Content**

**GitHub Issues as Scholarly Marginalia**

In traditional codicology, **marginalia**—notes, glosses, and queries penned in the
margins of a manuscript—reveal how generations of readers, scribes, and scholars
interacted with the text. In distributed digital editing, **GitHub Issues** serve
as the modern digital equivalent of scholarly marginalia (Faghihi et al., 2022).

Too often, newcomers view the "Issues" tab of a repository strictly as a place for
reporting broken software bugs. In a digital humanities project, however, issues
function as an open, searchable research notebook. Scholars use issues to document
paleographical ambiguities, record undecipherable scribal hands, debate variant
grammatical parsings, and track outstanding editorial tasks across the corpus
(Faghihi et al., 2022).

> **Issue #28: Ambiguous ligature on Folio 16r, line 12 (Codex B)**
> *Labels:* `paleography`, `needs-second-opinion`
>
> **Description:** In transcribing line 12, the third word appears to be an
> abbreviated form of "πνεῦμα", but the supralinear stroke resembles a circumflex
> over an omicron-upsilon ligature.
>
> **Facsimile Reference:** IIIF Manifest Canvas #16 (Region: 450,820,300,120)
>
> **Question:** Should we encode this as `<abbr>πν̅α</abbr>` with an editorial
> `<expan>` or record it as an unresolvable `<unclear>` reading?

Because issues support rich markdown, image embeds, IIIF deep links, and `@mentions`,
collaborators can convene around a specific manuscript puzzle, debate alternative
solutions, and establish a documented consensus before any code is committed
(Faghihi et al., 2022).

**Takeaway:** GitHub Issues function as open, collaborative
scholarly marginalia, providing a structured space to debate paleographical
puzzles and record editorial decisions.

---

## **22 Content**

**Authoring Issue Templates for Digital Editions**

Just as pull requests benefit from standardized templates, issue tracking in a
collaborative edition must be structured to ensure contributors provide adequate
scholarly context. Without structured templates, issue reports often arrive as vague
complaints like "the Greek text in chapter 3 looks wrong," providing zero folio
numbers, image links, or proposed corrections.

Digital scholarly projects deploy **GitHub Issue Templates** (stored in
`.github/ISSUE_TEMPLATE/`) to guide contributors through specific reporting
protocols (Faghihi et al., 2022). By defining YAML or Markdown forms, repositories
can present specialized issue categories:

1. **Paleographical Query:** For ambiguous letterforms, unreadable ligatures, or
   physical damage requiring second opinions.

2. **Linguistic / Lemma Dispute:** For debating morphological parsings, dictionary
   headwords, or semantic part-of-speech tags.

3. **Encoding / Schema Defect:** For reporting invalid TEI nesting, broken
   attribute pointers, or Schematron rule failures.

```yaml
# .github/ISSUE_TEMPLATE/paleographical_query.yml
name: Paleographical Query
description: Submit an ambiguous manuscript reading or unreadable scribal hand for peer consultation.
labels: ["paleography", "needs-second-opinion"]
body:
  - type: input
    id: witness_folio
    attributes:
      label: Witness & Folio Reference
      description: E.g., Codex Vaticanus Graecus 1209, Folio 142r, Line 8.
    validations:
      required: true
  - type: input
    id: iiif_link
    attributes:
      label: IIIF Manifest URL / Canvas Coordinates
      description: Direct URL to the high-resolution image canvas.
    validations:
      required: true
  - type: textarea
    id: problem_description
    attributes:
      label: Transcription Puzzle & Proposed Readings
      description: Describe the letterforms and list competing transcription hypotheses.
    validations:
      required: true
```

**Takeaway:** Structured issue templates ensure that
collaborative textual queries include necessary manuscript citations, IIIF
coordinates, and transcription hypotheses.

---

## **23 Content**

**Project Management: Labels, Milestones, and Kanban Boards**

Coordinating the transcription, reconciliation, normalization, and lemmatization
of dozens of manuscript folios across a team of student editors requires robust
project management infrastructure. GitHub provides three integrated mechanisms for
organizing editorial labor: **Labels**, **Milestones**, and **GitHub Projects
(Kanban Boards)** (Weigl et al., 2024).

**Labels** are color-coded tags that categorize issues and pull requests by topic,
methodological layer, and urgency. A well-organized TEI repository establishes a
controlled vocabulary of labels:

- *Layer:* `layer:diplomatic`, `layer:normalization`, `layer:apparatus`, `layer:morphosyntax`

- *Status:* `status:in-progress`, `status:needs-review`, `status:blocked`

- *Discipline:* `paleography`, `codicology`, `tei-schema`, `iiif`

**Milestones** group related issues and pull requests toward a shared academic
deadline or edition release target (e.g. `Milestone 1: Complete Diplomatic Layer (Nov
20)` or `Milestone 2: Critical Edition Release v1.0 (Dec 15)`). Milestones track
progress dynamically, displaying a percentage completion bar as associated issues
and PRs are closed.

**GitHub Projects** synthesizes these elements into an interactive **Kanban Board**.
Each manuscript folio moves through visual columns across its editorial lifecycle:

```
+----------------+----------------+----------------+----------------+
|    Backlog     |  In Progress   | In Peer Review |  Merged/Done   |
+----------------+----------------+----------------+----------------+
| Folio 18r (MS) | Folio 16v (MS) | Folio 15r (MS) | Folio 14r (MS) |
| Folio 18v (MS) | Folio 17r (MS) | Folio 15v (MS) | Folio 14v (MS) |
+----------------+----------------+----------------+----------------+
```

**Takeaway:** Labels, milestones, and Kanban project boards
transform sprawling editorial tasks into a transparent, visual project management
pipeline.

---

## **24 Content**

**Case Study: The Scholastic Commentaries and Texts Archive (SCTA)**

To see distributed version control operating at the cutting edge of digital
humanities, we turn to the **Scholastic Commentaries and Texts Archive (SCTA)**,
directed by Jeffrey C. Witt (Witt, 2018). The SCTA curates a massive, highly
interconnected corpus of medieval scholastic philosophy and theology, focusing
primarily on commentaries on Peter Lombard's *Sentences*—a foundational four-book
theological textbook that generated thousands of commentaries across four
centuries (Witt, 2018; Witt, 2019).

Scholastic texts are inherently intertextual: every commentary consists of a dense
web of quotations, refutations, and cross-references pointing to other scholastic
authors, Aristotle, and the Bible. Historically, editing this corpus was
paralyzed by institutional centralization: individual universities published
isolated print volumes over decades, resulting in fragmented, incompatible
editions that obscured the living intellectual network of the Middle Ages (Witt,
2018).

| Architectural Tier | Component Name | Editorial and Publication Function |
|---|---|---|
| **Data Layer** | Distributed Git Repositories | Independent scholars author TEI XML transcriptions in personal forks. |
| **Index Layer** | SCTA Central SPARQL Index | Aggregates and links expression descriptions and semantic cross-references. |
| **Interface Layer** | LombardPress Web Viewer | Dynamically queries the index to render interactive transcriptions and facsimiles. |
| **Output Layer** | Print & Export Engines | Generates camera-ready PDF critical apparatuses and exposes Linked Open Data APIs. |

Witt solved this problem by decoupling data curation from presentation. All SCTA
transcriptions are authored in TEI XML conformant to the LombardPress schema and
stored in public GitHub repositories (Witt, 2018). Independent scholars across the
world transcribe distinct questions and distinctions in their own Git forks,
submitting pull requests to central corpus repositories. When merged, automated
pipelines validate the TEI data and index its Linked Open Data relationships.
Applications like the LombardPress web viewer consume this data via open APIs,
ensuring that the underlying textual data remains permanent, version-controlled,
and citeable regardless of future software changes (Witt, 2019).

**Takeaway:** The SCTA proves that distributed Git repositories
and community pull requests can curate massive, interconnected medieval corpora
without centralized publishing bottlenecks.

---

## **25 Content**

**Case Study: Perseids and Classics Collaborative Editing**

Another pioneering implementation of collaborative version control in classical
philology is the **Perseids Project**, developed by Bridget Almas and Marie-Claire
Beaulieu at Tufts University in partnership with the Perseus Digital Library (Almas &
Beaulieu, 2013).

Perseids was created to solve a fundamental pedagogical and scholarly challenge:
how to enable undergraduate and graduate students to produce vetted,
publication-grade digital critical editions of Greek and Latin source documents
without overwhelming instructors with manual grading and file management (Almas &
Beaulieu, 2013). The platform integrates specialized web-based editing tools—such
as the Son of Suda On-Line (SOSOL) transcription tool, morphological taggers, and
syntax treebank editors—directly on top of Git version control.

In the Perseids workflow, students transcribe manuscript witnesses, annotate Greek
dialects, and construct dependency treebanks. Under the hood, Perseids commits every
student action to a Git repository. When a student completes a task, Perseids
generates a pull request assigned to an editorial board of instructors and senior
scholars. The board reviews the student's Greek parsing and TEI markup through a
structured review rubric, providing feedback and approving merges (Almas & Beaulieu,
2013). Perseids established that distributed version control provides the exact
scaffolding required to transform classroom exercises into authentic contributions
to digital classical scholarship.

**Takeaway:** The Perseids Project demonstrates that
version-controlled pull request workflows allow students to produce vetted,
publication-grade classical editions within a structured pedagogical framework.

---

## **26 Content**

**Case Study: Manubot and Open Collaborative Writing**

While TEI XML remains the dominant standard for historical texts, the principles of
distributed version control have revolutionized collaborative scholarly writing
more broadly. A leading exemplar is **Manubot**, an open-source publishing
platform developed by Daniel Himmelstein and colleagues for collaborative scientific
and humanistic authoring (Himmelstein et al., 2019).

Manubot was created to overcome the severe limitations of traditional word
processors and closed authoring platforms. When dozens of geographically
distributed scholars co-author a major study, Google Docs and Microsoft Word
inevitably suffer from version collisions, unversioned copy-pasting, broken citation
indexes, and an inability to track granular authorship attribution. Manubot shifts
the entire writing process to GitHub: scholars write chapters in plain text
Markdown, store files in a Git repository, and manage all co-author contributions
through pull requests and issue tracking (Himmelstein et al., 2019).

| Pipeline Stage | Processing Mechanism | Scholarly Function in Manubot |
|---|---|---|
| **1. Co-Authoring** | Distributed Pull Requests | Co-authors write chapters in Markdown and submit atomic pull requests. |
| **2. Continuous Integration** | GitHub Actions / CI Runners | Triggers automated build containers on every pull request push. |
| **3. Citation Resolution** | Persistent Identifier Lookup | Queries CrossRef, DataCite, and PubMed to fetch and format metadata from DOIs. |
| **4. Multiformat Rendering** | Pandoc & Template Engines | Compiles validated manuscript source into HTML, PDF, and JATS XML formats. |

Crucially, Manubot integrates automated Continuous Integration pipelines. When a
co-author submits a pull request, CI runners automatically resolve bibliographic
citations from persistent identifiers (such as DOIs, ISBNs, and PubMed IDs),
validate document syntax, and compile the entire manuscript into publication-grade
HTML and PDF formats (Himmelstein et al., 2019). Manubot proves that combining Git
collaboration with automated pipeline processing creates a frictionless, highly
reproducible scholarly authoring environment.

**Takeaway:** Manubot shows how Git version control and
automated continuous integration can transform multi-author scholarly writing into
a transparent, reproducible, and version-tracked collaboration.

---

## **27 Content**

**Case Study: Multimodal Collaborative Editing in E-LAUTE**

Collaborative digital editing is not restricted to standard textual prose; it extends
equally to complex multimodal historical sources combining text, tabular notation,
and audio. A remarkable recent exemplar is the **E-LAUTE Project** (Electronic Linked
Annotated Unified Tablature Edition), directed by David Weigl and colleagues (Weigl
et al., 2024).

E-LAUTE is assembling a comprehensive multimodal critical edition of sixteenth-century
German Lute Tablature (GLT). German lute tablature represents an exceptionally
difficult historical encoding challenge: unlike modern musical stave notation or
standard Italian tablature, GLT utilizes an intricate, non-intuitive grid of
letters, numbers, and bespoke symbols representing specific course-fret
combinations on the instrument's neck (Weigl et al., 2024). Transcribing and
validating this repertoire requires simultaneous coordination among musicologists,
philologists, and performing lute players.

To manage this complex collaborative workflow, E-LAUTE bridges the **Text Encoding
Initiative (TEI)** with the **Music Encoding Initiative (MEI)** in a distributed Git
ecosystem. Contributors use a specialized web-based notation editor named
`mei-friend`, which integrates directly with Git cloud repositories. Musicologists
transcribe tablature symbols, philologists encode historical song texts in TEI XML,
and performers annotate performance practice. When editorial teams complete an
edition release, GitHub Actions pipelines automatically validate the hybrid TEI/MEI
schemas, verify metadata against linked databases, and synthesize interactive web
renderings (Weigl et al., 2024).

**Takeaway:** E-LAUTE demonstrates that distributed Git workflows
successfully coordinate complex multimodal editions combining TEI text, MEI musical
notation, and performance data across multidisciplinary teams.

---

## **28 Content**

**Scholarly Attribution, Provenance, and `<revisionDesc>`**

A fundamental ethical and academic requirement in any scholarly edition is
**attribution**: every participant who transcribes a folio, normalizes a word, or
corrects a reading must receive formal, transparent credit for their intellectual
labor. In traditional print scholarship, student research assistants and junior
encoders are frequently relegated to a generic acknowledgement footnote, obscuring
who performed which specific editorial emendations (Daquino et al., 2023).

Distributed version control provides an automated, fine-grained record of
authorship through Git commit metadata. Every commit cryptographically binds the
author's name, email, and timestamp to the exact characters modified. However,
because an edition's canonical output must remain independent of external software
platforms, digital editions must bridge Git's commit history directly into the
internal TEI header metadata (TEI Consortium, 2026).

```xml
<teiHeader>
  <fileDesc>
    <titleStmt>
      <title>Digital Critical Edition of Codex B (03)</title>
      <editor role="primaryEditor">Dr. Ken M. Penner</editor>
      <respStmt>
        <resp>Transcription and Apparatus Encoding</resp>
        <persName ref="https://orcid.org/0000-0002-1825-0097">Jane Doe</persName>
      </respStmt>
    </titleStmt>
    <!-- ... publicationStmt and sourceDesc ... -->
  </fileDesc>
  <revisionDesc status="draft">
    <change when="2026-11-10" who="#JD" status="reviewed">
      Transcribed Folio 14v and reconciled double-keyed readings against IIIF facsimile.
    </change>
    <change when="2026-11-03" who="#KP" status="approved">
      Approved Pull Request #14: merged lemmatization layer into canonical main branch.
    </change>
  </revisionDesc>
</teiHeader>
```

In the `<teiHeader>`, the `<respStmt>` and `<revisionDesc>` elements formalize
contributor provenance. Each major editorial milestone merged via pull request must
be accompanied by a corresponding `<change>` entry recording the editor's ORCID
identifier, the date, and the precise nature of the editorial intervention (TEI
Consortium, 2026; Daquino et al., 2023).

**Takeaway:** Digital editions must synchronize Git commit
provenance with internal TEI `<revisionDesc>` metadata to ensure rigorous,
permanent academic attribution.

---

## **29 Content**

**Synthesizing the Nine Layers in the Consolidated Repository**

Today's consolidation exercise culminates in organizing all nine methodological
layers constructed across Weeks 1 through 9 into a single, unified, and standardized
repository layout. When working in isolation, it is easy for file paths to drift,
temporary scratch scripts to accumulate, and directory names to become inconsistent.
Consolidation establishes structural harmony across the entire course corpus.

Every student repository must reflect a clean, standardized folder hierarchy where
each methodological component resides in its designated home:

| Directory Path | Methodological Topic | Managed Edition Assets |
|---|---|---|
| `.github/` | Topic 10 (Consolidation) | Issue templates, PR templates, and GitHub Actions CI/CD workflows. |
| `data/facsimiles/` | Topic 3 (IIIF Imaging) | IIIF manifest URLs, canvas coordinates, and high-resolution crops. |
| `data/transcriptions/` | Topics 4-6 (Transcription/Reconciliation) | Diplomatic transcriptions, consensus texts, and normalized TEI XML files. |
| `data/apparatus/` | Topics 7-8 (Collation/Apparatus) | Collation matrices, variant alignment trees, and critical apparatus entries. |
| `data/morphology/` | Topic 8 (Lemmatization) | Morphologically tagged tokens, Greek POS annotations, and lexical keys. |
| `schemas/` | Topic 10 (Validation) | Canonical RELAX NG and ISO Schematron constraint files. |
| `src/modules/` | Topics 1-13 | Course markdown lessons, reading notes, and research syntheses. |

Take time today to audit your working tree: move misplaced transcription files into
their designated directories, remove abandoned scratch files, verify that all file
names conform to the project naming standard (`03a_Lesson_XX_Content.md`), and
execute a clean commit to your local `main` branch (Weigl et al., 2024).

**Takeaway:** A consolidated scholarly repository organizes all
accumulated methodological layers into a clean, standardized directory structure,
laying the physical foundation for automated validation and collaborative peer
review.

---

## **30 Content**

**Looking Ahead to Friday: Preparing for Automated CI and Peer Review**

Today you transformed your relationship with version control, moving from a solitary
local Git habit to a networked, collaborative fork-and-pull ecosystem. You mapped
remote endpoints, established feature branching disciplines, explored pull
requests as a dynamic apparatus criticus, and investigated issue tracking as
collaborative scholarly marginalia.

Before Friday's class, ensure that your repository is fully prepared by completing
the following checklist:

1. **Verify Remotes:** Run `git remote -v` to confirm that `origin` points to your
   personal fork and `upstream` points to the canonical course repository.

2. **Synchronize Main:** Execute `git fetch upstream` and merge `upstream/main` into
   your local `main` branch, pushing the clean state to your fork.

3. **Push Active Branches:** Ensure that your current feature branches (including
   your Topic 8 lemmatization and linguistic markup work) are pushed to `origin`.

4. **Complete Assignment 3:** Finalize your **Linguistic Markup Assignment**, which
   is formally due this Friday, November 13.

On Friday in Lesson 10.2, we will build directly upon today's collaborative
infrastructure. You will implement automated **GitHub Actions CI/CD workflows** to
execute automated XML schema validation sweeps across every TEI layer produced to
date, and you will conduct structured, in-class **peer reviews** of your classmates'
editions using formal philological rubrics.

**Takeaway:** Today's version-control foundation prepares your
repository for Friday's automated schema validation sweeps, CI/CD pipelines, and
collaborative peer reviews.

---

## References

Almas, B., & Beaulieu, M.-C. (2013). Developing a new integrated editing platform
for source documents in classics. In *Digital Humanities 2013 Conference
Abstracts*. University of Nebraska–Lincoln.

Daquino, M., Wigham, M., Daga, E., Giagnolini, L., & Tomasi, F. (2023). CLEF: A
Linked Open Data native system for crowdsourcing. *ACM Journal on Computing and
Cultural Heritage*, 16(3), 1–17. https://doi.org/10.1145/3594721

Faghihi, Y., Holford, M., & Jones, H. (2022). Teaching the Text Encoding Initiative:
Context, Community and Collaboration. *Journal of Open Humanities Data*, 8(15),
1–14. https://doi.org/10.5334/johd.72

Himmelstein, D. S., Rubinetti, V., Slochower, D. R., Hu, D., Malladi, V. S., Greene,
C. S., & Gitter, A. (2019). Open collaborative writing with Manubot. *PLOS
Computational Biology*, 15(6), e1007128. https://doi.org/10.1371/journal.pcbi.1007128

Holmes, M., & Turska, M. (2023). Embracing Endings: Principles for digital
longevity and their importance for research software engineers. *DHTech Blog*.
https://dh-tech.adho.org/blog/2023/08/07/endings-principles/

Huskey, S. J. (2024). Decoupling quality control and publication: The Digital Latin
Library and the traveling imprimatur. In *Digital Scholarly Editing in Practice*.
Cambridge University Press.

McGann, J. (2014). *A New Republic of Letters: Memory and Scholarship in the Age of
Digital Reproduction*. Harvard University Press.

Renear, A., Mylonas, E., & Durand, D. (1996). Refining our notion of what text
really is: The problem of overlapping hierarchies. In *Research in Humanities
Computing* (Vol. 4). Oxford University Press.

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/

Weigl, D. M., Janjuš, O., Rosmer, S., de Valk, R., & Lewis, D. (2024). Collaborative
workflows for encoding, validating, and publishing a multimodal digital edition. In
*Proceedings of the 11th International Conference on Digital Libraries for
Musicology* (DLfM '24), pp. 78–86. https://doi.org/10.1145/3748336.3748349

Witt, J. C. (2018). Re-conceiving the Christian scholastic corpus with the
Scholastic Commentaries and Texts Archive. In *Past and Future: Medieval Studies
Today*, pp. 103–128. Brepols.

Witt, J. C. (2019). Digital scholarly editions as interfaces. In *Digital Scholarly
Editions as Interfaces*, pp. 191–214. BoD.
