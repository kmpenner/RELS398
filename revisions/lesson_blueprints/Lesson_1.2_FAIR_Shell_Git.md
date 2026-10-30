# Blueprint: Lesson 1.2 — FAIR Principles, The Unix Shell, & Local Git
## Course: RELS 398 / ENGL 398 · Meeting #2

> **Source Specification:** [`SESSION_CONTENT_SPEC.md`](file:///home/kmpenner/projects/RELS/398/SESSION_CONTENT_SPEC.md) §1.2  
> **Key Reform:** Introduces **plain text**, **the Unix shell (bash)**, and **local Git version control** as foundational prerequisites. Strips out premature GUI editors and cloud AI models.

---

### Core Learning Objectives
1. Understand the **FAIR Data Principles** (Findable, Accessible, Interoperable, Reusable) as the gold standard of digital scholarship.
2. Navigate the filesystem, inspect files, and manipulate directories strictly using the Unix command-line interface (`bash`).
3. Distinguish between proprietary binary document containers (`.docx`) and durable, human-readable plain text (`.txt`, `.md`).
4. Initialize a local Git repository, track changes, and record atomic commit messages.

---

### 50-Minute Classroom Progression

#### 1. FAIR Data Principles & Plain Text (10 mins)
* Why Word documents (`.docx`) are proprietary zip archives that trap historical evidence.
* Plain text and UTF-8 encoding as the foundation of digital preservation across centuries.
* Markdown (`.md`) as structured plain text.

#### 2. Terminal Fundamentals in Bash (15 mins)
* Directory navigation: `pwd`, `ls -la`, `cd`.
* File creation and inspection: `touch`, `cat`, `head`, `mkdir`.
* Safe handling: why spaces in filenames cause computational breakage; hyphen and underscore naming standards (`witness_transcription.md`).

#### 3. Local Git Version Control (20 mins)
* Why "save as `file_v2_final_FINAL.docx`" fails scholarly rigor.
* The three states of Git: **Working Directory**, **Staging Area** (`git add`), and **Repository Commit** (`git commit`).
* Hands-on lab:
  ```bash
  mkdir my_witness && cd my_witness
  git init
  echo "# Primary Witness: 1752 Treaty" > README.md
  git add README.md
  git commit -m "chore: initialize project repository with README"
  git log
  ```

#### 4. Exit Ticket / Milestone (5 mins)
* Each student has a verified local Git repository containing `README.md` documenting their chosen witness and passage.
