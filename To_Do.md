# RELS 398 Digital Methods — setup to-do

> **Blocked:** a stale `.git/index.lock` cannot be removed from the Cowork
> sandbox (deletion is gated and the permission prompt was declined). Only the
> first commit exists. Everything since — folder READMEs, the import plan, the
> `.gitignore` additions, the RELS 398 rename — is on disk and **uncommitted**.
> See §5. Nothing is lost; it just needs four lines in your own shell.
>
> **Also blocked:** the OneDrive import cannot run from here at all. There is no
> OneDrive mount in this sandbox — only Google Drive and `~/projects`. See §7.

Scaffolded in `~/projects/RELS/` (the authoritative repo tree) to match the
conventions of the existing course repos. Outstanding items below.

## 1. Course number — RELS 398 ✅ (one manual step left)

- [x] Folder renamed `Digital_Methods` → `398`, matching the bare-number
      convention (`103`, `117`, `216`, `222`, `225`, `331`).
- [x] `course.json` → `"code": "RELS 398"`.
- [x] `.gitignore` header comment → `RELS 398 (Digital Methods) .gitignore`.
      (Kept the parenthetical: unlike the other courses, the number alone doesn't
      say what this is. Drop it if you'd rather match exactly.)
- [x] `398.code-workspace` created, following 331's bare-number pattern rather
      than 117's `RELS117.code-workspace`.
- [x] **`rm DigitalMethods.code-workspace`** — removed.
- [x] GitHub remote → `https://github.com/kmpenner/RELS398.git` configured and tracking `main`.
- [ ] Optionally add `398` to the `REPOS=(...)` array in `shared/init-repos.sh`.
      Not required — nothing reads that array except the script itself, and
      `/sit`, `/stand`, and `drive-sync.sh` all discover repos by looking for
      `.git`.

## 1a. Term and year ✅

- [x] Set `term` (`"Fall 2026"`) and `year` (`2026`) in `course.json`.

## 1b. Moodle site ✅

Recorded as `"moodle_url"` in `course.json`:
`https://moodle.stfx.ca/course/view.php?id=49782`

## 2. Git remote ✅

- [x] GitHub remote created and configured (`origin -> https://github.com/kmpenner/RELS398.git`).

## 3. course.json ✅

- [x] `term` and `year` set.
- [x] Template versions confirmed (`syllabus_template_version: 2026-01-22`, `schedule_template_version: 2024-5-6`).

## 4. Workspace file

- [ ] 331 and 117 each add a second folder pointing at the OneDrive course
      folder (331: `C:/Users/kmpen/OneDrive - St. Francis Xavier
      University/RELS331`). Add the equivalent `Digital Methods` path to
      `398.code-workspace` once you know the local OneDrive path on this machine.

## 5. Repository Scaffold & History ✅

- [x] Folder READMEs, `.gitignore`, and initial commits landed cleanly.

## 6. Content & Syllabus/Schedule ✅

- [x] Authored canonical LaTeX syllabus (`RELS 398 Syllabus.tex`) and schedule (`RELS 398 Schedule.tex`).
- [x] Restructured schedule for 13-week three-step comparative cycle (Manual ground truth Tue -> Deterministic software Wed -> AI/LLM evaluation Fri), restored Reconciliation to Week 5, staggered due dates, and balanced evaluation weights to 100%.
- [x] Master Research Prompts (`03_Research/RESEARCH_PROMPTS.md`) updated with Stage 1 and Stage 2 prompts for all 13 topics.
- [ ] Layout migration to `shared/LESSON_PIPELINE.md` §A3 standard (`raw/`, `src/`, `dist/`, `config/`, `scripts/`, `private/`).

## 7. OneDrive import — CANNOT RUN FROM COWORK

Ken green-lit the import (copy, not move). It did not happen, and not because
of a decision still pending: **this sandbox has no OneDrive access.** The only
mounts are `RELS` (Google Drive), `projects--RELS`, `outputs`, and `uploads`.
There is no `~/OneDrive*`, no `/mnt/*OneDrive*`, nothing.

The browser tools can *read* the SharePoint folder — that's how it was
inventoried — but reading a file listing in a web UI is not a file transfer.
Downloading ~120 files across 14 nested folders by clicking through a web UI is
not a viable import path, and each download needs its own approval.

Three ways to actually do it, best first:

1. **rclone with a OneDrive remote** — fits the existing toolchain exactly;
   `drive-sync.sh` already uses rclone for the Google Drive channel.
   ```bash
   rclone config          # new remote, name it "onedrive", type: Microsoft OneDrive
   rclone copy onedrive:"Digital Methods" ~/projects/RELS/398/_onedrive_staging \
       --exclude "tei-pragmatic-glass-box/**" --progress
   ```
   Staging first, then filing per the plan, keeps a bad import out of the repo.
   `copy` (not `sync`, not `move`) leaves the OneDrive originals untouched.

2. **OneDrive desktop sync** — 331's workspace file already points at
   `C:/Users/kmpen/OneDrive - St. Francis Xavier University/RELS331`, so the
   client may already be syncing on the Windows machine. If so it's a plain
   `cp -r` from a local path, run in your own shell.

3. **Browser download of the whole folder as a .zip** — OneDrive's toolbar has a
   Download action on a folder selection. One approval instead of 120, but it
   lands in `~/Downloads` on your machine, not here.

Either way the **filing** step — applying the mapping in
`00_Syllabus_and_Admin/OneDrive_import_plan.md`, splitting out `private/`,
checking the syllabus HTML — can be done from here once the files are on disk.

- [ ] Get the files down by one of the above, then say so and the import
      proceeds per the plan.

## 8. OneDrive import — mapping and open checks

`OneDrive/Documents/Digital Methods` holds 14 folders. Full mapping is in
`00_Syllabus_and_Admin/OneDrive_import_plan.md`, updated with Ken's decisions
(Griffitts → Drive-only; `tei-pragmatic-glass-box` → its own repo; `Sus` → live
under `01_Course_Modules/`; superseded syllabus → `archive/`; copy, not move).
Nothing has been moved, copied, or downloaded. Open items:

- [x] ~~Which syllabus is authoritative~~ — "Digital Methods - Syllabus 2026"
      is canonical; the undated one is superseded.
- [ ] **HTML is the canonical format** for course documents; PDF/DOCX are
      derived. On import, check whether the 2026 syllabus HTML is clean authored
      markup or a Word export (`MsoNormal`, `mso-*`, `<o:p>`, a `_files/`
      sidecar). If it's an export, flag it — don't silently rewrite.
- [ ] **`Final Project grades.docx` is student data.** It must land in
      `private/`, which is git-ignored *and* excluded from the Drive mirror
      (`--exclude '**/private/**'` in `drive-sync.sh`) — not in
      `02_Assignments_and_Projects/`.
- [ ] **Screen the other 15 items in `Course Administration/` for student
      identifiers** during the import — participation logs, email lists, letters
      of accommodation, anything with a name or student number. Only the grades
      file announces itself in its filename. `drive-sync.sh` also excludes
      `**/Grades-*.csv`, `**/final_moodle_grades.json`, and
      `**/*assignsubmission*`, which is a good hint at what has turned up in
      other courses.

## Notes on conventions followed

- `.gitignore` follows the 331/103 style (the `.pptx`/`*.zip`/media exclusions
  mean the copied `Supplementary Templates` binaries are **not** tracked in git —
  they reach other machines via the Drive mirror, same as in the other courses).
- **No `.gitconfig-shared`.** Only 222 has one. `bootstrap-machine.sh` now does
  auth globally via `gh auth setup-git`, which covers every repo including this
  one, so the per-repo file is legacy. Commit identity (`user.name` /
  `user.email`) is set in this repo's local `.git/config`, since the sandbox has
  no global gitconfig.
- **`/sit` and `/stand` pick this folder up automatically** — both iterate
  `$RELS/*/` and take any folder containing `.git`. No registration needed.
  `/stand` will skip the push step until a remote exists (item 2 above).
- **`drive-sync.sh mirror` also picks it up automatically** — it syncs all of
  `~/projects/RELS`. On the next `/stand` it will create `gdrive:RELS/398` and
  retire the older Drive-side scaffold at `gdrive:RELS/Digital_Methods` into
  `gdrive:RELS-attic/<timestamp>`, since the local tree no longer has a folder
  by that name. Expect that in the mirror output; it's the rename propagating,
  not data loss.
- **Two-channel split, as the skills describe it:** git tracks what you author
  (`.md`, `.html`, `.xml`, `.py`, `.docx`, `.xlsx`); bulk media, decks, and
  downloaded readings are git-ignored and travel via the Drive mirror.
  `03_Research/` is the landing zone for `/sit`'s Deep Research / NotebookLM
  ingest, which *exports* Docs to Markdown rather than copying 0-byte stubs.
