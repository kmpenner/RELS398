# Blueprint: Lesson 1.2 — FAIR Principles, The Unix Shell, Git, & GitHub
## Course: RELS 398 / ENGL 398 · Meeting #2

> **Source Specification:** [`SESSION_CONTENT_SPEC.md`](file:///home/kmpenner/projects/RELS/398/SESSION_CONTENT_SPEC.md) §1.2 + Early GitHub Directive  
> **Key Reform:** Introduces **plain text**, **the Unix shell (bash)**, **local Git version control**, and **remote GitHub repositories** in Week 1 (relocating the core GitHub onboarding from old Lesson 10.1). Every student leaves Week 1 with an active GitHub repository ready for all course submissions.

---

### Core Learning Objectives
1. Understand the **FAIR Data Principles** (Findable, Accessible, Interoperable, Reusable) as the gold standard of digital scholarship.
2. Navigate the filesystem, inspect files, and manipulate directories strictly using the Unix command-line interface (`bash`).
3. Distinguish between proprietary binary document containers (`.docx`) and durable, human-readable plain text (`.txt`, `.md`).
4. Initialize or clone a Git repository, record atomic commits, push to **remote GitHub**, and understand how all course assignments are submitted via GitHub commits and Pull Requests.

---

### 50-Minute Classroom Progression

#### 1. FAIR Data Principles & Plain Text (10 mins)
* Why Word documents (`.docx`) are proprietary zip archives that trap historical evidence.
* Plain text and UTF-8 encoding as the foundation of digital preservation across centuries.
* Markdown (`.md`) as structured plain text.

#### 2. Terminal Fundamentals in Bash (12 mins)
* Directory navigation: `pwd`, `ls -la`, `cd`.
* File creation and inspection: `touch`, `cat`, `head`, `mkdir`.
* Safe handling: why spaces in filenames cause computational breakage; hyphen and underscore naming standards (`witness_transcription.md`).

#### 3. Local Git & Remote GitHub Onboarding (23 mins)
* Why "save as `file_v2_final_FINAL.docx`" and Moodle file dropboxes fail scholarly rigor.
* The four states of Git + GitHub: **Working Directory**, **Staging Area** (`git add`), **Local Repository** (`git commit`), and **Remote Origin on GitHub** (`git push` / `git pull`).
* Hands-on lab (using the 1760–1761 Halifax Treaty demo repo and student GitHub Classroom repos):
  ```bash
  # Authenticate with GitHub CLI
  gh auth login

  # Clone student repository from GitHub Classroom (or init and link remote)
  gh repo clone RELS398-2027/edition-studentname
  cd edition-studentname

  # Create initial witness documentation in Markdown
  echo "# Primary Witness: 1760-1761 Halifax Peace and Friendship Treaty" > README.md
  git add README.md
  git commit -m "chore: initialize project repository with witness README"
  git push origin main
  ```
* Inspecting the pushed commit on `github.com` in the browser.

#### 4. Exit Ticket / Milestone (5 mins)
* Each student has a live **GitHub repository** with their first pushed commit (`README.md` documenting their chosen witness and passage), verified online.
