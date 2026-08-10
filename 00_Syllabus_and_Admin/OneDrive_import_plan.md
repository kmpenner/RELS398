# OneDrive → repo import plan (proposal — nothing has been moved)

Source: `StFX OneDrive / Documents / Digital Methods` — 14 folders, no loose
top-level files. Read-only inventory only; nothing downloaded, moved, or
deleted. **Do not run this until Ken has signed off on the mapping.**

## Document-format convention (applies to everything below)

HTML is the **canonical, authored** form of course documents — it is
machine-editable, diffable in git, and readable by every downstream tool.
PDF and DOCX are **derived artifacts** generated from the HTML, never
separately maintained. When both exist for the same document, the HTML wins
and the others get regenerated rather than hand-edited.

This matches 117 and 222, which both carry `.html` alongside `.docx`/`.pdf`
for syllabus and schedule.

⚠️ **To verify on import:** if `Digital Methods - Syllabus 2026.html` turns out
to be a Word "Save as HTML" export (`<o:p>`, `class="MsoNormal"`, inline
`mso-*` styles, a `_files/` sidecar directory) rather than clean authored
markup, it is not usable as a source of truth. Flag it to Ken and decide
whether to clean it up — do **not** silently rewrite it.

## Mapping

| OneDrive folder | Items | Proposed destination | Notes |
|---|---|---|---|
| `weeks/` | 12 | `01_Course_Modules/` | week1–week12, each with lesson1/lesson2/lesson3 — already the 222/331 module-lesson shape. See below. |
| `Course Administration/` | 16 | `00_Syllabus_and_Admin/` | **Except the grades file** — see Decisions. |
| `Tools & APIs/` | 10 | `03_Research/Tools_and_APIs/` | Reference material on tooling. |
| `TEI & EpiDoc Guidelines/` | 19 | `03_Research/TEI_and_EpiDoc_Guidelines/` | Standards documentation. |
| `EpiDoc/` | 1 | `03_Research/TEI_and_EpiDoc_Guidelines/` | Single item; fold in rather than keeping a one-item folder. |
| `SunoikisisDC/` | 5 | `03_Research/SunoikisisDC/` | External curriculum Ken draws on. |
| `Griffitts Thesis & Software/` | 10 | `03_Research/Griffitts_Thesis_and_Software/` | **Drive-only (Ken).** Explicitly git-ignored; reaches other machines via the Drive mirror. See Decisions §3. |
| `Texts & Manuscripts/` | 11 | `01_Course_Modules/01_Source_Materials/` | Primary sources. That path is git-ignored by design — travels via the Drive mirror. |
| `Tutorials & Presentations/` | 10 | `04_Media_and_Transcripts/` | Decks (`.pptx`) are git-ignored; any transcripts/notes beside them are tracked. |
| `tei-pragmatic-glass-box/` | 13 | **not this repo** — `~/projects/RELS/tei-pragmatic-glass-box/` | **Its own repo (Ken), like `Syriac`.** See Decisions §4. |
| `Sus/` | 10 | `01_Course_Modules/` or `archive/` | The Susanna case study from the first offering (2 yrs ago). Live example vs. archived — see Decisions §5. |
| `mods.d/` | 1 | `03_Research/Tools_and_APIs/` | SWORD module config; one item each. |
| `modules/` | 1 | `03_Research/Tools_and_APIs/` | Same. |
| `.agents/` | 1 | repo root `.agents/` | 222 has a root `.agents/`; matches that convention. Inspect the single file first. |

### `weeks/` in detail

`week1`…`week12`, each containing `lesson1`, `lesson2`, `lesson3`. Two options:

1. **331 pattern** — `01_Course_Modules/Module_01_Topic_Name/` with the three
   lessons inside. Requires a topic name per week, read off the lesson content.
2. **Literal carry-over** — `01_Course_Modules/week01/lesson1/` etc., renamed
   later once topics are confirmed.

Recommend (1), deriving topic names from the lesson files during import, since
`week4` tells you nothing six months from now. Zero-pad to `Module_01` so they
sort correctly (the OneDrive listing already shows `week1, week10, week11,
week12, week2, …`).

## Decisions

1. ✅ **Canonical syllabus** — "Digital Methods - Syllabus 2026". The older
   undated one is superseded and goes to `00_Syllabus_and_Admin/archive/`
   (Ken confirmed `archive/` is fine). Note that `archive/` is git-ignored, so
   it survives in the Drive mirror only — that is the intended behaviour here.

2. ⏳ **`Final Project grades.docx` → `private/`.** Student data. `private/` is
   git-ignored *and* excluded from the Drive mirror
   (`--exclude '**/private/**'` in `drive-sync.sh`), so it stays on the machine.
   It must not go into `02_Assignments_and_Projects/`. Still worth confirming
   whether anything else in `Course Administration/` is student-identifying —
   16 items, and only the one is obvious from its filename.

3. ✅ **`Griffitts Thesis & Software/` — Drive-only, not git.** Imported to
   `03_Research/Griffitts_Thesis_and_Software/` and excluded by an explicit
   `.gitignore` line (added ahead of the import, so it can never be
   accidentally committed). The generic `*/sources/` pattern would not have
   covered this path — git's `*` doesn't cross `/`, so a two-segment pattern
   only matches two-segment paths. The explicit line is deliberate.

4. ✅ **`tei-pragmatic-glass-box/` — its own repo**, like `Syriac`. It does
   **not** get imported into this scaffold. Separate job:
   - clone/copy to `~/projects/RELS/tei-pragmatic-glass-box/`
   - `git init -b main`, private remote (Ken's approval needed, same as this repo)
   - `/sit`, `/stand` and the Drive mirror pick it up automatically once it has
     a `.git` — it sits beside the course folders, not inside one
   - if it already has git history in OneDrive, adopt it rather than re-initing
     (`init-repos.sh` has an adoption path for exactly this, used for 117/Syriac)

5. ⏳ **`Sus/` — the Susanna case study from the first offering, two years ago.**
   Now that we know what it is, placement depends on one thing: is it still a
   live teaching example or a historical record?
   - **Live example** → `01_Course_Modules/` beside the `weeks/` modules, or
     `02_Assignments_and_Projects/` if it was the model for the final project.
     Tracked in git, editable, reusable.
   - **Archived** → `archive/`, which is git-ignored and Drive-only.

   Recommend **live** unless the course is being substantially rebuilt: a worked
   example of a real TEI/EpiDoc encoding on an actual apocryphal text is the
   hardest kind of teaching material to reproduce, and the cost of keeping it in
   git is ~10 files. Archiving is easy later; recovering it from a Drive attic
   is not.

6. ⏳ **Copy or move?** Recommend **copy**, leaving OneDrive untouched until the
   import is verified and committed. The OneDrive folder can then become the
   derived-artifact drop for students, or be retired. **Ken is being asked now —
   do not begin the transfer until he confirms.**

## Status

Nothing has been transferred. Awaiting the copy-vs-move answer (§6), plus §2
and §5. The only change made in anticipation is the `.gitignore` line for
Griffitts — safe in either direction, since ignoring a path that never arrives
costs nothing.

## Once approved

Import order: `Course Administration/` first (establishes the canonical HTML
syllabus and schedule, which the `make_pdf.py` pipeline then consumes), then
`weeks/`, then the research folders. Commit in batches so a bad import is one
`git revert` away, not a tangle.

First check on arrival: whether `Digital Methods - Syllabus 2026.html` is clean
authored markup or a Word export. `shared/pdf-pipeline/make_pdf.py` expects
pandoc-style output with `data-custom-style` spans (`Course_Number`,
`Course_Name`, `Course_Date`) and falls back to `course.json` when they're
absent — a Word export will have neither, plus `MsoNormal` cruft. Flag it;
don't rewrite it.
