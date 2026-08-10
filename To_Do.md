# Digital Methods — setup to-do

Scaffolded in `~/projects/RELS/` (the authoritative repo tree) to match the
conventions of the existing course repos. Outstanding items below.

## 1. Course number (blocks several renames)

The folder is `Digital_Methods` as a **placeholder**. Every other course repo is
named by its bare number (`103`, `117`, `216`, `222`, `225`, `331`). Once the
number is assigned, rename and update, in this order:

- [ ] `git mv`-free rename: `mv ~/projects/RELS/Digital_Methods ~/projects/RELS/NNN`
- [ ] `course.json` → `"code": "RELS NNN"` (currently the literal string `RELS NNN`)
- [ ] `.gitignore` header comment, line 2 → `RELS NNN .gitignore`
      (drop the `(Digital Methods)` parenthetical to match the others)
- [ ] `DigitalMethods.code-workspace` → `NNN.code-workspace`
      (117 uses `RELS117.code-workspace`, 331 uses `331.code-workspace`; the bare
      number is the newer pattern — follow 331)
- [ ] GitHub remote → `https://github.com/kmpenner/RELSNNN.git`.
      If the remote was already created under a placeholder name, rename the repo
      on GitHub, then `git remote set-url origin <new URL>`.
- [ ] If the course gets a folder in `shared/init-repos.sh`, add `NNN` to the
      `REPOS=(...)` array so future re-runs pick it up (it is not there now).

## 2. Git remote — not yet created

- [ ] The local repo is initialized (`main`, one commit) but has **no remote**.
      Ken asked to be consulted first. Other repos use
      `https://github.com/kmpenner/RELS<NNN>.git`, private. Create with:
      `gh repo create RELSNNN --private --source=. --remote=origin --push`
      (Note: `init-repos.sh` would name it `RELS-NNN` with a hyphen, which does
      **not** match the existing remotes — only `RELS-shared` uses a hyphen.)

## 3. course.json

- [ ] Fill in `term` (currently `"TBD"`) and confirm `year` (currently `2027`).
- [ ] Confirm the two template versions are still current.

## 4. Workspace file

- [ ] 331 and 117 add a second folder pointing at the OneDrive course folder.
      Once the StFX OneDrive `Digital Methods` folder is settled, add it to
      `DigitalMethods.code-workspace` the same way.

## 5. Content

- [ ] Templates are copied into `Supplementary Templates/` from `shared/`.
      Build the real syllabus and schedule into `00_Syllabus_and_Admin/`.
- [ ] Add module folders under `01_Course_Modules/`, following either the 331
      pattern (`Module_01_Topic_Name`) or the 222 pattern
      (`Module 1 - Topic Name`, containing `01_Source_Materials`,
      `02_Drafts_and_Outlines`, `03_Moodle_Assets`).
- [ ] Remove the `.gitkeep` files from the numbered folders as real content lands.

## Notes on conventions followed

- `.gitignore` follows the 331/103 style (the `.pptx`/`*.zip`/media exclusions
  mean the copied `Supplementary Templates` binaries are **not** tracked in git —
  they reach other machines via the Drive mirror, same as in the other courses).
- No `.gitconfig-shared` was added: only 222 has one; 103, 216, 225, 331, and 117
  do not. Add it later if the shared-config approach is rolled out everywhere.
- `/sit` and `/stand` pick up any folder under `~/projects/RELS` with a `.git`,
  so no change is needed there — but `/stand` will only push once a remote exists.
