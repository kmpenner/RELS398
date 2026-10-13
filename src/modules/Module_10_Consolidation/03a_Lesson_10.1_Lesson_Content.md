# Lesson 10.1 — Collaborative Git Workflows for Digital Textual Scholarship

*RELS 398 / ENGL 398 · Topic 10: Consolidation · Meeting #26 (Tue Nov 10)*

*Consolidation week — Wednesday November 11 is closed for Remembrance Day. This
week is a two-step consolidation pause with no new philological method. Today you
move from solitary local version control to distributed multi-editor workflows:
remotes, forks, branching strategies, pull requests as apparatus, and issue tracking.*

---

## **01 Content**

**The Mid-Term Consolidation Milestone**

Over the past nine weeks, you built a rich digital edition from scratch. You started in Week 1 with terminal Git commands. In Weeks 2 and 3, you catalogued your document in a `<teiHeader>` and linked digital images. Weeks 4 through 6 guided you through diplomatic transcription, AI reconciliation, and regularizing spellings with `<choice>` tags. In Week 7, you created reading stylesheets using CSS. In Weeks 8 and 9, you added grammar tags and named entities.

Until now, you worked as a solitary editor in an isolated folder. You made files on your own laptop and tested them in private. But real scholarly editions are rarely solitary projects. Real editions require teams of historians, paleographers, and encoders to work together across institutions.

Week 10 is our consolidation milestone. The university is closed on Wednesday for Remembrance Day. Therefore, this week has two focused meetings. We introduce no new XML tags this week. Instead, we connect your isolated workspace to GitHub. You will learn to share editions, propose changes, and review work as a community.

**Vocabulary.** *Consolidation* — Pausing new tag authoring to synthesize, organize, and validate all accumulated edition layers. *Collaborative Edition* — A digital scholarly project produced and maintained by multiple editors working together.

**Takeaway:** Consolidation synthesizes nine discrete encoding layers into a shared, multi-editor digital scholarly edition on GitHub.

---

## **02 Content**

**From Solitary Editor to Distributed Textual Community**

In traditional print scholarship, an editor often worked alone in an archive. That solitary scholar transcribed manuscripts into private notebooks. They resolved textual puzzles in isolation. Eventually, they published a single book. When early computer projects began, editors often continued this solitary habit. They typed transcriptions into desktop word processors. They emailed files back and forth as attachments.

Exchanging files by email causes severe problems. Files quickly drift out of sync. Suppose Ace emails a corrected XML file to Olyvia. Meanwhile, Olyvia adds entity tags to her own copy. Which file is current? Merging those two files by hand is slow and painful. Crucial editorial decisions get buried in private email chains instead of staying with the text.

Distributed version control solves this dilemma. By hosting repositories on GitHub, all team members share one historical record. Every change is tracked. Every editorial choice is documented. Contributors receive full credit for their work. Moving to GitHub turns private files into an open, living resource.

**Vocabulary.** *Distributed Version Control* — A system where every editor holds a complete, independent copy of the project history while synchronizing through a shared network host. *Editorial Provenance* — The transparent, verifiable record of who changed a text, when they changed it, and why.

**Takeaway:** Distributed version control replaces chaotic email attachments with a transparent, communal record of all editorial interventions.

---

## **03 Content**

**The Directed Graph: How Git Tracks Repository History**

To collaborate smoothly, you must understand how Git stores history. Git does not save files as a loose collection of folders. Instead, Git models your repository as a graph of snapshots. Every time you run `git commit`, Git takes a complete snapshot of your project.

Each commit receives a unique forty-character fingerprint. We call this a SHA-1 hash. An example is `7a3f81b`. Git calculates this hash mathematically. It combines the exact file text, your commit message, the date, and the parent commit hash. Because each commit points backward to its parent, history forms an unbroken tree.

This graph structure guarantees scholarly integrity. Suppose someone modifies a single letter in Andromeda's 1752 Treaty in an old commit. That commit hash changes instantly. In turn, every subsequent commit hash breaks. Git makes secret alterations impossible. It provides a permanent audit trail for historical documents.

**Vocabulary.** *Commit Snapshot* — A permanent, frozen record of all tracked files in a repository at a specific moment. *SHA-1 Hash* — A unique cryptographic fingerprint that identifies a commit and verifies its contents have not been altered.

**Takeaway:** Git records project history as an immutable graph of commit snapshots, providing permanent citation stability and audit integrity.

---

## **04 Content**

**The Anatomy of Remotes: Local Clones and GitHub**

During the first nine weeks of class, your Git repository lived only on your laptop. Your commits were strictly local. If your computer crashed, your work was lost. A **remote** is a copy of your repository hosted on the web, usually on GitHub.

A remote repository stores the same commit graph and files as your local project. It acts as a shared central meeting point. In Git terminology, the default name for your primary remote repository is **origin**. When you connect your local repo to GitHub, you register this remote web address.

Working with a remote involves two main actions: pushing and fetching. Running `git push` uploads your local commits to GitHub so others can view them. Running `git fetch` downloads new commits from GitHub to your laptop. The remote simply mirrors your commit graph on the web.

**Vocabulary.** *Remote Repository* — A copy of your Git repository hosted on a network server such as GitHub. *Origin* — The standard default name Git assigns to your primary remote repository.

**Takeaway:** A remote repository on GitHub acts as an accessible central anchor for sharing commit snapshots across multiple computers.

---

## **05 Content**

**Collaboration Models: Shared Write Access vs. Fork-and-Pull**

Digital editions organize teamwork using two primary models: shared write access and the fork-and-pull model.

<table class="table table-bordered my-3">
<thead>
<tr>
<th>Collaboration Model</th>
<th>How It Works</th>
<th>Best Use Case</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Shared Write Access</strong></td>
<td>Every team member has direct push permission to the main repository. Anyone can commit directly to branches.</td>
<td>Small, tightly coordinated teams of two or three trusted co-authors.</td>
</tr>
<tr>
<td><strong>Fork-and-Pull</strong></td>
<td>Contributors make a personal copy (fork) on GitHub, push to their fork, and submit a Pull Request to the upstream project.</td>
<td>Public open-source projects, large editions, and classroom peer review.</td>
</tr>
</tbody>
</table>

In this course, we practice the fork-and-pull model. This model protects the authoritative edition from accidental errors. It guarantees that every proposed change is inspected, discussed, and validated before it enters the official text.

**Vocabulary.** *Shared Write Access* — Granting multiple users permission to push commits directly into a single repository. *Fork-and-Pull Model* — A workflow where contributors edit personal forks and request that maintainers pull their changes.

**Takeaway:** The fork-and-pull model protects the primary edition while inviting outside scholars and peers to propose improvements.

---

## **06 Content**

**Forking a Scholarly Repository on GitHub**

A **fork** is a personal copy of another user's repository on GitHub. It lives under your personal account. When you click the "Fork" button on GitHub, GitHub copies the whole repository. This copy includes all files, branches, and commit history.

Forking lets you experiment without risking the original project. For instance, Andromeda can fork the course repository to study Ace's French Revolutionary decree. In her fork, Andromeda can test alternative `<persName>` tags. She can try new CSS styles. Ace's original repository remains untouched.

Your fork stays connected to the original project across GitHub. The original repository is called the **upstream** repository. Once you finish an editorial improvement on your fork, you can send those commits back to upstream as a formal proposal.

**Vocabulary.** *Fork* — A server-side duplicate of a GitHub repository hosted under your own personal account. *Upstream* — The original parent repository from which a fork was created.

**Takeaway:** Forking creates a safe personal sandbox where you can freely modify an edition before contributing back to the parent project.

---

## **07 Content**

**Branching Strategies for Digital Scholarly Editions**

Working directly on your `main` branch can be dangerous. The `main` branch should always hold your stable, production-ready edition. If you start transcribing a messy new page directly on `main`, your repository is temporarily broken.

A **branch** is an independent line of development. It branches off from `main`. You can think of a branch as a lightweight moveable pointer. Creating a branch takes one second. On a branch, you can draft markup, test regularizations, or revise metadata safely.

When your work on the branch is complete and validated, you merge it into `main`. If an experiment fails, you simply delete the branch. Your main edition stays completely clean.

**Vocabulary.** *Main Branch* — The primary, stable line of development in a Git repository. *Feature Branch* — A temporary branch created to develop a specific addition, fix, or editorial layer in isolation.

**Takeaway:** Isolating editorial work on temporary feature branches keeps the primary main branch clean, stable, and always valid.

---

## **08 Content**

**Branch Naming Conventions and Repository Hygiene**

In collaborative projects, descriptive branch names prevent confusion. If three students name their branches `test`, `new`, and `my-branch`, nobody knows what each branch contains. Professional digital humanities teams establish clear branch naming conventions.

Good branch names use lowercase letters, numbers, and hyphens. They typically begin with a prefix describing the category of work, followed by a slash and a concise summary:

<table class="table table-bordered my-3">
<thead>
<tr>
<th>Branch Prefix</th>
<th>Purpose</th>
<th>Example Branch Name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>feature/</code></td>
<td>Adding a substantial new encoding layer or document section</td>
<td><code>feature/french-named-entities</code></td>
</tr>
<tr>
<td><code>fix/</code></td>
<td>Correcting a transcription mistake or schema error</td>
<td><code>fix/maud-lewis-date-when</code></td>
</tr>
<tr>
<td><code>docs/</code></td>
<td>Updating project documentation or README files</td>
<td><code>docs/treaty-citation-guide</code></td>
</tr>
</tbody>
</table>

Notice how clear these names are. When Olyvia sees `fix/maud-lewis-date-when`, she knows immediately that the branch fixes an attribute error on a `<date>` element without opening a single file.

**Vocabulary.** *Branch Prefix* — A standard category label (such as `feature/` or `fix/`) placed at the start of a branch name. *Repository Hygiene* — Habits of organization, clear naming, and regular cleanups that keep a codebase readable.

**Takeaway:** Meaningful branch names with standard prefixes communicate the exact scope of an editorial task to collaborators.

---

## **09 Content**

**Configuring and Managing Remotes via the Command Line**

To manage remotes in VS Code, use the `git remote` command. When you clone your fork from GitHub to your laptop, Git automatically creates one remote. It names this remote `origin`, pointing to your personal fork.

You can check your remotes by typing:

```bash
git remote -v
```

This command prints the name and URL for both fetch and push operations. To keep your fork in sync with the course project, add a second remote. By convention, name this second remote **upstream**:

```bash
git remote add upstream https://github.com/stfx-rels/rels-398-editions.git
```

Now your local repository knows about two locations. It knows `origin` (your personal fork with write permission). It also knows `upstream` (the shared class repository with read permission).

**Vocabulary.** *git remote -v* — The command that prints all configured remote names alongside their network URLs. *Remote Tracking Branch* — A local read-only reference that tracks the state of a branch on a remote server.

**Takeaway:** Configuring both origin and upstream remotes allows your local repository to push personal work and pull shared updates.

---

## **10 Content**

**Synchronizing with Upstream: Fetch, Merge, and Fast-Forward**

As weeks pass, classmates and instructors add files to the upstream project. Your personal fork does not update automatically. You must fetch and merge those upstream changes yourself.

The safest workflow has two clear steps: `git fetch` and `git merge`. First, fetch the latest commits from upstream:

```bash
git fetch upstream
```

This command downloads new commits and updates `upstream/main`. Crucially, `git fetch` never touches your working files. It never edits your active branches. It simply downloads the data so you can check it.

Next, switch to your local `main` branch, and merge the upstream commits:

```bash
git checkout main
git merge upstream/main
```

If you made no local commits on `main`, Git does a **fast-forward** merge. It simply advances your `main` pointer forward. Your local files are now fully up to date.

**Vocabulary.** *git fetch* — Downloading commits and branches from a remote without altering your local working directory. *Fast-Forward Merge* — Advancing a branch pointer directly forward along a linear line of history when no diverging commits exist.

**Takeaway:** Fetching from upstream and merging into your local main branch keeps your workspace synchronized with project updates.

---

## **11 Content**

**The Pull Request as the Dynamic Apparatus Criticus**

In print editions, the **apparatus criticus** sits at the page foot. It records variant readings, proposed emendations, and editor notes. The apparatus lets readers evaluate why an editor picked one reading over another.

In digital editing on GitHub, the **Pull Request (PR)** acts as a living apparatus criticus. When you open a pull request, you are not just submitting code. You are proposing a scholarly hypothesis. You say: "Here is my proposed transcription. Here is the historical evidence for it. Here is how it improves our edition."

A pull request creates an open discussion forum attached to your commit diff. Collaborators can debate paleographical readings, challenge regularizations, and test markup before accepting it into the master text.

**Vocabulary.** *Pull Request (PR)* — A formal proposal on GitHub to merge commits from one branch into another, accompanied by discussion and review. *Scholarly Apparatus* — The critical commentary and recorded variants accompanying an edition's primary text.

**Takeaway:** A GitHub Pull Request acts as a living apparatus criticus where editors debate textual readings before adopting them.

---

## **12 Content**

**Anatomy of a Scholarly Pull Request**

An effective pull request must be clear and helpful. Submitting a PR with no description or a title like "updates" forces reviewers to guess what you did.

A professional scholarly pull request contains four key parts:

1. **A Clear Title:** State the exact editorial action (such as `Add named entities for French National Assembly deputies`).
2. **Context and Rationale:** Explain why you made the change. Did you fix a transcription typo? Did you normalize an archaic spelling?
3. **Evidence and Citations:** Cite the manuscript folio image or authority record (like VIAF or Wikidata) supporting your choice.
4. **Validation Proof:** State that your TEI XML file passed `xmllint` and schema checks with zero errors.

When Ace submits a PR for his 1791 decree, he attaches an image crop. He explains why he linked *M. de Bouillé* to VIAF ID `61536214`. Reviewing that PR becomes quick, educational, and reliable.

**Vocabulary.** *Pull Request Description* — The markdown body of a PR explaining the rationale, scope, and evidence for proposed changes. *Imperative Title* — A concise title phrased as a command describing what the change achieves.

**Takeaway:** A thorough PR description pairs proposed markup changes with historical evidence, rationale, and schema validation proof.

---

## **13 Content**

**Standardizing Editorial Contributions: `PULL_REQUEST_TEMPLATE.md`**

To help contributors provide proper evidence, repositories use pull request templates. When you add a file named `PULL_REQUEST_TEMPLATE.md` to `.github/`, GitHub displays that template whenever someone opens a new PR.

A template provides a helpful checklist for digital philology:

```markdown
## Summary of Changes
- What document or encoding layer does this PR modify?

## Codicological and Paleographical Evidence
- [ ] Facsimile image verified against primary witness
- [ ] Authority IDs verified against VIAF or Wikidata

## Schema and Validation Checklist
- [ ] Well-formed XML verified (`xmllint --noout`)
- [ ] Relax NG schema passes with 0 errors
```

This checklist prevents rushed submissions. It reminds Olyvia to check her Maud Lewis date attributes. It prompts Andromeda to verify her treaty placenames before opening the PR.

**Vocabulary.** *PULL_REQUEST_TEMPLATE.md* — A standardized markdown form automatically displayed by GitHub when creating a pull request. *Pre-Flight Checklist* — A set of verification steps an author completes before requesting scholarly review.

**Takeaway:** Standardized PR templates ensure that every submitted edition update includes required evidence and validation checks.

---

## **14 Content**

**Visualizing Diffs in Hierarchical XML Documents**

The heart of any pull request review is the **diff**. GitHub compares your branch with the target branch line by line. It shows additions in green with a plus sign (`+`). It shows deletions in red with a minus sign (`-`).

Reading XML diffs requires attention to nesting. A change on line 42 can affect an opening tag on line 10. When viewing a diff on GitHub, you can pick between two view modes:

<table class="table table-bordered my-3">
<thead>
<tr>
<th>Diff View Mode</th>
<th>Description</th>
<th>Best Use Case</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Unified Diff</strong></td>
<td>Shows deletions and additions inline in a single continuous column.</td>
<td>Quick checks on mobile screens or small one-line typo fixes.</td>
</tr>
<tr>
<td><strong>Split Diff</strong></td>
<td>Displays the original file on the left and the modified file on the right side by side.</td>
<td>Reviewing structural XML changes, closing tags, and nested elements.</td>
</tr>
</tbody>
</table>

Split diff mode makes missing tags obvious. If an editor deleted an opening `<p>` tag thirty lines earlier, the split view reveals the structural shift right away.

**Vocabulary.** *Diff* — A visual representation of differences between two versions of a file, highlighting additions and deletions. *Split Diff* — A side-by-side view comparing original and modified text in parallel columns.

**Takeaway:** Using split diff view helps reviewers spot subtle structural changes and mismatched tags in hierarchical XML.

---

## **15 Content**

**The Scholarly Code Review Interface**

GitHub provides clean tools for peer review. Hover your cursor over any line number in a pull request diff. A blue plus icon appears. Clicking that icon opens an inline comment box on that exact line.

This inline interface enables focused dialogue. Instead of sending a vague message saying "your date looks wrong," a reviewer clicks directly on `<date when="1752-11-22">` and writes:

> "The proclamation heading says *November 22*, but the articles were signed on November 24. Should we encode two separate date elements?"

GitHub also includes an "Insert a suggestion" button. Reviewers can write the exact replacement XML they recommend. The author can accept the suggestion with one click. GitHub creates a commit that applies the fix instantly.

**Vocabulary.** *Inline Comment* — A review note attached to a specific line number within a pull request diff. *Suggested Change* — A proposed code replacement submitted by a reviewer that the author can accept with one click.

**Takeaway:** Inline review comments allow scholars to conduct precise, line-by-line debates directly on the digital text.

---

## **16 Content**

**Iterating on an Open Pull Request**

Opening a pull request does not freeze your files. A pull request is a discussion, not a final exam. When reviewers suggest improvements, you do not close the PR or start over.

To update your pull request, return to your branch in VS Code. Make the requested edits, commit them, and push them to your fork:

```bash
git checkout feature/treaty-entities
# edit witness.xml to address reviewer suggestions
git add witness.xml
git commit -m "Clarify ratification date and add VIAF reference"
git push origin feature/treaty-entities
```

As soon as your push reaches GitHub, the pull request updates automatically. Your new commit appears in the PR thread. The diff updates immediately. When all comments are resolved and validation passes, the maintainer merges your work into `main`.

**Vocabulary.** *Pull Request Iteration* — Pushing new commits to an active feature branch to address peer feedback before merging. *PR Lifecycle* — The progression of a proposal from draft creation through review, iteration, approval, and merge.

**Takeaway:** Pushing new commits to your active branch automatically updates the open pull request, making peer review an iterative cycle.

---

## **17 Content**

**Understanding Merge Conflicts in Hierarchical XML**

Collaboration is straightforward when editors work on separate files. But what happens when two editors edit the same lines at the same time? Git stops and reports a **merge conflict**.

Git is designed to be safe. Suppose Ace edits line 45 to read `<persName ref="#bouille">Bouillé</persName>`. Meanwhile, Olyvia edits line 45 to read `<persName role="general">Bouillé</persName>`. Git cannot know which interpretation is correct. Rather than guessing and erasing someone's work, Git pauses. It asks a human editor to choose.

Merge conflicts are not software bugs. They are normal events in collaborative work. They simply mean two scholars proposed different readings for the same phrase, requiring thoughtful adjudication.

**Vocabulary.** *Merge Conflict* — A state where Git cannot automatically combine two branches because both changed the same lines in conflicting ways. *Editorial Adjudication* — The human decision-making process required to evaluate conflicting textual interpretations.

**Takeaway:** Merge conflicts occur when two branches alter the same lines concurrently; Git safely pauses to let human editors decide.

---

## **18 Content**

**Anatomy of a Git Conflict Marker**

When a merge conflict happens, Git writes special text markers directly into the file. These markers show both competing versions.

Here is a conflict marker in TEI XML:

```xml
<<<<<<< HEAD
<date when="1967-02-13">Feb 13</date>
=======
<date when="1967-02-15" cert="medium">Feb 15?</date>
>>>>>>> feature/date-audit
```

The markers divide the text into three sections:

- `<<<<<<< HEAD`: Marks the start of the conflict. It contains text from your current local branch.
- `=======`: The divider separating your version from the incoming version.
- `>>>>>>> feature/date-audit`: Marks the end of the conflict and names the incoming branch.

While these markers remain, your XML is invalid. You must open the file, select the right reading, and erase all three marker lines.

**Vocabulary.** *Conflict Marker* — Special delimiter strings (`<<<<<<<`, `=======`, `>>>>>>>`) inserted by Git to highlight competing text versions. *HEAD (Conflict Context)* — The commit representing your currently active local branch during a merge.

**Takeaway:** Git conflict markers isolate competing readings between HEAD and the incoming branch, requiring manual editing to resolve.

---

## **19 Content**

**Modular Architecture and Conflict Mitigation**

The best way to handle merge conflicts is to prevent them. In large digital editions, teams design a **modular architecture** to minimize simultaneous edits on the same file.

If an entire edition sits in one large 5,000-line `edition.xml` file, conflicts happen constantly. Every time someone touches metadata or changes a tag, they collide with a classmate.

Teams reduce conflicts through smart file separation:

1. **Splitting Layers:** Store metadata in `teiHeader.xml`, diplomatic text in `transcription.xml`, and entity lists in `taxonomy.xml`.
2. **Page-by-Page Files:** Store each folio in its own file, such as `folio_01r.xml`.
3. **Task Assignment:** Use GitHub Issues to claim specific folios before editing so two people never transcribe the same page simultaneously.

**Vocabulary.** *Modular Architecture* — Organizing an edition into separate, self-contained files to reduce editing friction and collision. *Conflict Mitigation* — Proactive project design and communication strategies that minimize overlapping edits.

**Takeaway:** Dividing an edition into modular files and assigning clear editorial roles drastically reduces concurrent merge conflicts.

---

## **20 Content**

**Step-by-Step Conflict Resolution in VS Code**

Modern code editors make resolving conflicts simple. When you open a conflicted file in Visual Studio Code, the editor displays clickable action buttons above the conflict:

- **Accept Current Change:** Keeps your current branch version (`HEAD`) and deletes the incoming version.
- **Accept Incoming Change:** Overwrites your version with the incoming branch version.
- **Accept Both Changes:** Keeps both versions stacked together.
- **Compare Changes:** Opens a side-by-side diff to examine differences.

In scholarly editing, clicking "Accept Current" or "Accept Incoming" is often too blunt. Often, the ideal solution is a synthesis. Perhaps Ace added a necessary `@ref` attribute, while Olyvia added a valuable `@role` attribute.

The best editorial choice is to combine both contributions by hand: `<persName ref="#bouille" role="general">Bouillé</persName>`. After synthesizing the markup, delete any leftover marker lines.

**Vocabulary.** *Accept Current Change* — A VS Code shortcut that retains the local HEAD version and discards the incoming change. *Editorial Synthesis* — Combining valuable elements from both competing branches into a unified, superior reading.

**Takeaway:** Resolving scholarly conflicts often requires hand-synthesizing complementary markup from both branches rather than picking one.

---

## **21 Content**

**The Non-Negotiable Step: Verifying XML Well-Formedness**

After editing a merge conflict, never commit immediately. Editors often leave behind stray marker characters, duplicate tags, or broken brackets.

A single remaining marker like `<<<<<<<` makes your entire document fatally invalid. An XML parser will crash when reading it. Therefore, checking well-formedness immediately after resolving a conflict is mandatory:

```bash
xmllint --noout witness.xml
```

If `xmllint` returns complete silence with an exit code of 0, your file is clean. If it reports an error (such as `syntax error, unexpected '<'`), a broken tag or conflict marker survived. Fix the error in VS Code and run `xmllint` again until it passes cleanly.

**Vocabulary.** *xmllint --noout* — A terminal utility that parses an XML document to verify syntactic well-formedness without printing the file body. *Syntax Gate* — A mandatory validation check that must pass before any file can be staged or committed.

**Takeaway:** Always run xmllint --noout immediately after editing a conflict to ensure no stray markers or broken tags survive.

---

## **22 Content**

**Completing the Conflict Merge Commit**

When your resolved file passes `xmllint` and schema validation, you can finish the merge. Concluding a merge requires staging the file and recording a dedicated commit.

Run these three commands in your terminal:

```bash
git add witness.xml
git status
git commit -m "Merge branch 'feature/date-audit': synthesize date attributes"
```

Running `git status` verifies that the file moved from "Unmerged paths" to "Changes to be committed." Running `git commit` creates a **merge commit**. Unlike ordinary commits with one parent, a merge commit has two parents. It unites two diverged lines of history into one.

Your repository is now clean, unconflicted, and ready for further work.

**Vocabulary.** *Merge Commit* — A commit with two parent commits that records the successful integration of two diverged branches. *Staging a Resolution* — Using `git add` to tell Git that a conflicted file has been successfully edited and verified.

**Takeaway:** Staging resolved files with git add and committing creates a two-parent merge commit that reunites diverged branches.

---

## **23 Content**

**GitHub Issues as Scholarly Marginalia and Task Tracking**

Collaboration involves more than submitting files. Scholars need a space to discuss puzzles, question tricky handwriting, and plan upcoming tasks. On GitHub, this conversation happens in **Issues**.

An Issue is a dedicated discussion thread inside a repository. Think of Issues as public scholarly marginalia. Instead of scribbling a private note about an uncertain word in Maud Lewis's letter on a napkin, Olyvia opens a GitHub Issue titled: `Paleographical query: illegible verb on folio 1 verso line 14`.

In the Issue description, Olyvia attaches an image crop. She pastes her draft transcription. She tags Ace and Andromeda using `@username`. Her classmates receive alerts, inspect the script, and reply with readings. When the team agrees, the issue is closed, leaving a permanent public record.

**Vocabulary.** *GitHub Issue* — A trackable discussion thread in a repository used for reporting bugs, proposing tasks, or debating scholarly questions. *Scholarly Marginalia* — Scholarly notes, queries, and annotations recorded alongside a primary text.

**Takeaway:** GitHub Issues serve as public, searchable discussion forums for tracking editorial tasks and resolving paleographical queries.

---

## **24 Content**

**Authoring Issue Templates for Digital Editions**

Just as pull request templates help file submissions, **issue templates** ensure structured discussions. Without templates, users open vague tickets like "broken text" without naming the file or folio.

You create issue templates by saving markdown files in `.github/ISSUE_TEMPLATE/`. For example, you can create a template for paleographical questions:

```markdown
---
name: Paleographical Query
about: Report an illegible hand, abbreviation, or damaged text
title: "[PALEOGRAPHY]: "
labels: transcription, needs-review
---

### Document and Location
- Document: [Ace 1791 / Maud Lewis / 1752 Treaty]
- Folio and Line Number:

### Image Evidence
Attach a high-resolution screenshot of the manuscript region.

### Proposed Readings
1. Reading A:
2. Reading B:
```

When someone clicks "New Issue" on GitHub, this template guides them. It ensures essential coordinates and evidence are included from the start.

**Vocabulary.** *Issue Template* — A pre-formatted form that guides users in submitting complete, well-documented issue tickets. *Issue Labels* — Coloured tags applied to issues to categorize their domain, priority, or status.

**Takeaway:** Issue templates prompt contributors to provide exact document coordinates, image crops, and competing readings up front.

---

## **25 Content**

**Project Management: Labels, Milestones, and Kanban Boards**

As a digital edition grows to dozens of files and hundreds of lines, managing workflow becomes essential. GitHub provides three lightweight project management tools built into every repository:

<table class="table table-bordered my-3">
<thead>
<tr>
<th>Project Tool</th>
<th>Function in Digital Editions</th>
<th>Concrete Course Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Labels</strong></td>
<td>Color-coded tags that categorize tickets by topic, status, or difficulty.</td>
<td><code>paleography</code>, <code>tei-header</code>, <code>needs-review</code>, <code>good-first-issue</code></td>
</tr>
<tr>
<td><strong>Milestones</strong></td>
<td>Target containers that group issues and PRs under a specific deadline.</td>
<td><code>Milestone: Week 10 Consolidation (Due Nov 13)</code></td>
</tr>
<tr>
<td><strong>Project Boards</strong></td>
<td>Visual Kanban boards with columns (To Do, In Progress, Done) to track task progress.</td>
<td>Moving "Tag French deputies in 1791 decree" from In Progress to Done.</td>
</tr>
</tbody>
</table>

Using these tools gives the entire editorial team a clear visual overview of progress. It ensures no historical witness is forgotten.

**Vocabulary.** *Milestone* — A project management target on GitHub that tracks progress toward a specific calendar deadline. *Kanban Board* — A visual workflow management board using columns to display task status from backlog to completion.

**Takeaway:** Labels, milestones, and project boards organize complex editorial labor into clear, trackable collaborative milestones.

---

## **26 Content**

**Case Study: The Scholastic Commentaries and Texts Archive (SCTA)**

To see these collaboration principles operating at scale, look at the **Scholastic Commentaries and Texts Archive (SCTA)**, directed by Jeffrey Witt. The SCTA is an open digital library preserving hundreds of medieval philosophical works written between 1200 and 1500.

Rather than forcing scholars worldwide into a single database, the SCTA decentralizes editing. Every medieval text lives in its own Git repository on GitHub. Researchers transcribe Latin manuscripts in TEI XML on personal forks and submit updates through pull requests.

Automated scripts regularly harvest these distributed repositories. They validate TEI markup and connect them into a global Linked Data graph. Witt's design proves that distributed Git workflows can unite international researchers around complex historical texts.

**Vocabulary.** *Scholastic Commentaries and Texts Archive (SCTA)* — A major distributed digital humanities project using Git and TEI to edit medieval manuscripts. *Decentralized Editing* — Allowing independent scholars to maintain separate edition repositories that aggregate into a shared network.

**Takeaway:** The SCTA demonstrates how international teams use GitHub repositories and pull requests to edit medieval texts collaboratively.

---

## **27 Content**

**Case Study: Perseids and Classics Collaborative Editing**

Another prominent example of collaborative digital philology is the **Perseids Project** at Tufts University. Perseids provides an online environment where students and professional Classicists collaborate on ancient Greek and Latin texts, papyri, and inscriptions.

Perseids incorporates version control directly into its teaching. When students annotate treebanks, transcribe inscriptions, or encode variants, their work is backed by Git commits. Scholars review student contributions through a board modeled on GitHub pull requests.

This workflow turns student assignments into real scholarly contributions. A student who transcribes an inscription does not merely receive a grade. Their verified work merges into the permanent scholarly edition with full credit.

**Vocabulary.** *Perseids Project* — A collaborative digital platform for editing ancient Greek and Latin texts using distributed version control. *Pedagogical Philology* — Integrating student classroom encoding directly into permanent, peer-reviewed scholarly digital editions.

**Takeaway:** The Perseids Project proves that student editors can contribute directly to published digital editions through disciplined version control.

---

## **28 Content**

**Case Study: Multimodal Collaborative Editing in E-LAUTE**

Collaborative version control extends beyond literary texts into diverse historical media. The **E-LAUTE** project is an international collaboration between scholars in Germany and Switzerland editing sixteenth-century lute music books.

Lute tablatures combine musical notes, German and French lyrics, woodcut illustrations, and printer metadata. To edit these works, the team coordinates musicologists, computer scientists, and bibliographers across institutions.

The E-LAUTE team maintains their digital editions on GitHub. They use feature branches for transcriptions, automated checks for musical validity, and GitHub Releases to publish versioned editions. Their work shows that distributed Git workflows successfully coordinate interdisciplinary teams editing varied historical media.

**Vocabulary.** *E-LAUTE* — An international collaborative digital edition project encoding Renaissance lute tablatures and song lyrics. *Multimodal Edition* — A scholarly digital project that integrates text, musical notation, and visual book art into a unified edition.

**Takeaway:** E-LAUTE illustrates how international interdisciplinary teams coordinate complex, multimodal digital editions using Git and GitHub.

---

## **29 Content**

**Scholarly Attribution, Provenance, and `<revisionDesc>`**

While GitHub tracks commit hashes and usernames on the web, a TEI XML document must remain self-contained offline. In TEI P5, this internal provenance lives inside the `<revisionDesc>` element in the `<teiHeader>`.

Every major editorial milestone, pull request merge, or conflict resolution should be recorded in a `<change>` element:

```xml
<revisionDesc>
  <change when="2026-11-10" who="#editor" status="consolidated">
    Consolidated Modules 1 through 9 layers; resolved merge conflict 
    in date attributes via PR #4; verified zero schema errors.
  </change>
</revisionDesc>
```

Notice how the TEI metadata directly references the collaborative workflow. The `@who` attribute points to the editor definition in `titleStmt`. The `@when` attribute records the date. The description records the specific pull request. By mirroring Git milestones inside the TEI header, your edition guarantees permanent, self-documenting provenance.

**Vocabulary.** *revisionDesc* — The TEI Header element that records the chronological revision history of a digital edition. *change* — A single entry inside revisionDesc detailing an editorial intervention, timestamp, and responsible editor.

**Takeaway:** Mirroring GitHub pull request merges and milestones inside the TEI revisionDesc element preserves self-contained scholarly provenance.

---

## **30 Content**

**Looking Ahead to Friday: Preparing for Automated CI and Peer Review**

Today, you connected solitary desktop editing to distributed community collaboration. You learned about remotes, forking, feature branching, pull request apparatus, and conflict resolution in VS Code.

Before our next meeting on Friday, make sure your repository is fully prepared:

1. Confirm your local `witness.xml` contains all nine completed layers (metadata, facsimiles, transcription, reconciliation, regularization, reading stylesheets, lemmatization, and named entities).
2. Verify that your file passes `xmllint --noout witness.xml` with zero syntax errors.
3. Push your latest commits to your `main` branch on GitHub.

On Friday, in Meeting #27, we conclude our consolidation milestone. We will build an automated Continuous Integration (CI) pipeline using **GitHub Actions**. You will write an automated workflow that runs `xmllint` and the Relax NG schema every time you push. We will also exchange repositories for in-class peer review.

**Vocabulary.** *Continuous Integration (CI)* — Automatically testing and validating code every time a developer pushes changes to a shared repository. *Peer Review Exchange* — An in-class exercise where students evaluate a classmate's edition against a structured rubric.

**Takeaway:** Preparing your repository today sets the stage for Friday's automated GitHub Actions validation and collaborative peer review.

---
