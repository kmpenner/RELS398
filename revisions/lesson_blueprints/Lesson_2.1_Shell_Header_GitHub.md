# Blueprint: Lesson 2.1 — The TEI Header via Shell & GitHub Onboarding
## Course: RELS 398 / ENGL 398 · Meeting #3

> **Source Specification:** [`SESSION_CONTENT_SPEC.md`](file:///home/kmpenner/projects/RELS/398/SESSION_CONTENT_SPEC.md) §2.1  
> **Key Reform:** 
> 1. Students build their first XML document (`header.xml`) **by hand in the Unix shell** using `echo >` and `echo >>` to deeply internalize tag hierarchy, root elements, and redirection dangers.
> 2. Students connect their local Git repository to **remote GitHub**, establishing their student repository and pushing their first commit.

---

### Core Learning Objectives
1. Understand XML syntax fundamentals: elements, attributes, nesting trees, self-closing tags, and the single root element rule.
2. Construct the four pillars of the `<teiHeader>` (`<fileDesc>`, `<encodingDesc>`, `<profileDesc>`, `<revisionDesc>`).
3. Experience the visceral mechanics of stream redirection in the terminal (`>` overwrite vs. `>>` append).
4. Authenticate with GitHub via `gh` CLI / SSH keys, link local git to remote origin, and execute their first `git push`.

---

### 50-Minute Classroom Progression

#### 1. XML Anatomy & The TEI Header (12 mins)
* XML as an ordered tree hierarchy: root, parents, children, attributes.
* The four mandatory pillars of the TEI Header:
  * `<fileDesc>`: Title, edition, publication, and source description (`<msDesc>`).
  * `<encodingDesc>`: Editorial principles, taxonomy, project standards.
  * `<profileDesc>`: Creation date, languages (`xml:lang`).
  * `<revisionDesc>`: Change log with dates and editor responsibility (`@resp`).

#### 2. Building the Header with Bash Redirection (18 mins)
* The pedagogical reason to write XML in the shell before touching an editor: you learn exactly how characters form tags, and how a mistyped `>` instead of `>>` silently overwrites and destroys the file.
* Step-by-step shell construction:
  ```bash
  # Open root element (overwrite creates file)
  echo '<?xml version="1.0" encoding="UTF-8"?>' > header.xml
  echo '<TEI xmlns="http://www.tei-c.org/ns/1.0">' >> header.xml
  echo '  <teiHeader>' >> header.xml
  echo '    <fileDesc>' >> header.xml
  echo '      <titleStmt>' >> header.xml
  echo '        <title>Edition of My Primary Witness</title>' >> header.xml
  echo '        <author>Archival Scribe</author>' >> header.xml
  echo '        <editor>Student Name</editor>' >> header.xml
  echo '      </titleStmt>' >> header.xml
  echo '      <publicationStmt><p>Unpublished scholarly draft</p></publicationStmt>' >> header.xml
  echo '      <sourceDesc><p>Archival manuscript</p></sourceDesc>' >> header.xml
  echo '    </fileDesc>' >> header.xml
  echo '  </teiHeader>' >> header.xml
  echo '  <text><body><p>Text will be transcribed here.</p></body></text>' >> header.xml
  echo '</TEI>' >> header.xml
  ```
* Check well-formedness from shell: `cat header.xml`.

#### 3. GitHub Remote Onboarding (15 mins)
* Transition from local Git to remote GitHub:
  ```bash
  # Authenticate via GitHub CLI
  gh auth login
  
  # Connect local repo to assigned student repo on GitHub
  git remote add origin https://github.com/RELS398-2027/witness-[student].git
  git branch -M main
  git add header.xml
  git commit -m "feat: construct foundational TEI header via shell redirection"
  git push -u origin main
  ```
* Students open their repository in the web browser and view their pushed commit.

#### 4. Exit Ticket / Milestone (5 mins)
* Every student repository on GitHub displays a green commit containing `header.xml`.
