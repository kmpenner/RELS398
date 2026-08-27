# RELS 398 — Lesson Pipeline Handoff

**Date:** 2026-08-25
**Repo:** `~/projects/RELS/398` (remote `https://github.com/kmpenner/RELS398.git`)
**HEAD at handoff:** `d4192ad`
**Read first:** `~/projects/RELS/shared/LESSON_PIPELINE.md` — the single end-to-end
procedure. Its §0 ground rules are not negotiable per-course. This document does
not replace it; it records where 398 sits inside it.

---

## 1. Where the work stands

| Stage | Progress | Blocker |
|---|---|---|
| Content markdown | **16 / 16 written** | — |
| Question banks | **2 / 16** | none; just authoring |
| PDF notes | **1 / 16** | none; needs banks first per build order |
| Images | 0 / 16 | **`.gemini_notebook` does not exist** |
| Interactive XML | 0 / 16 | hard-gated on images (correctly) |
| HTML player | 0 / 16 | follows XML |

`python3 scripts/status.py` prints the live board. Trust it over this table.

**Lint is clean:** all 16 lessons pass `lint_lesson_content.py` with 0 issues.
Keep it that way — it is the gate, not a checklist (§0.5).

---

## 2. The lesson model for this course

398 is **one lesson per class meeting**, not per topic. The schedule has 36
numbered meetings; `LESSON_MAP` in `scripts/topic_map.py` records all 36 and
cross-checks exactly against `src/syllabus/RELS 398 Schedule.tex`. If you change
one, change the other.

Most weeks run the **three-step comparative cycle**, and the lessons are built
around it:

- **Tue — manual.** Establishes the reference by hand.
- **Wed — deterministic.** A specialized/rule-based tool, measured against it.
- **Fri — AI-assisted.** A general model, measured against the same reference.

Weeks 1, 3, 5, 10, 13 depart from the pattern and say so in the schedule. Week 5
is two-step (Wed Sep 30 closed for Truth and Reconciliation); Week 10 is two-step
(Wed Nov 11 Remembrance Day).

**Written so far (16):**

| Topic | Lessons | Cycle |
|---|---|---|
| 01 Orientation | 1.1 Git, 1.2 Unicode Greek | no cycle |
| 03 IIIF Imaging | 3.1 APIs, 3.2 imaging, 3.3 manifest→TEI | no cycle |
| 04 Transcription | 4.1 manual, 4.2 Transkribus HTR, 4.3 LLM | full |
| 05 Reconciliation | 5.1 double-keying, 5.2 CER/WER | two-step |
| 06 Normalization | 6.1 manual, 6.2 rule script, 6.3 AI | full |
| 07 Collation | 7.1 manual, 7.2 CollateX, 7.3 AI | full |

**Writable now but not yet written (9):** Topics 02, 08, 09 — research reports
landed and are substantial.

**Not writable (18):** Topics 10–13 have no Deep Research reports yet.

---

## 3. Authoring conventions actually used

These are decisions already made across 16 lessons. Follow them or the corpus
becomes inconsistent.

**Structure.** Exactly 30 sections, `## **01 Content**` … `## **30 Content**`,
each with a bold thematic sub-header, 2–4 developed paragraphs, and a closing
`**Takeaway:** …` line. Close the file with `## References`.

**Front matter.** Each lesson opens with a title line, then an italic line giving
course, topic, meeting number and date, then an italic note naming which step of
the cycle it is and what it produces. Copy the shape from any existing lesson.

**Citations.** Cite *only* sources in that topic's Deep Research report and its
readings manifest. Never invent a citation. Where a concept is not tied to a
report source, explain it thoroughly with no citation attached — this is used
heavily and is fine. Every in-text citation must have a `## References` entry;
I check with a script (see §6).

**Length.** Lessons run ~8,500–9,500 words. That is roughly double the 222
exemplar and is deliberate for a 300-level course. Do not pad to match, but do
not write 4,000-word lessons either — the corpus should be even.

**Tables, not ASCII art.** Sequences become numbered tables with a `Step` column;
hierarchies become tables under a bold caption. The linter fails on box-drawing
characters. `.lesson-lint-allow` does not exist for this course and should not
need to — no lesson has a genuinely spatial figure.

**Two linter traps I hit:**

- A column headed exactly `Element`, `Detail`, or `Column N` trips `generic-header`. Use `TEI element`, `Validation item`, etc.
- An escaped pipe `\|` inside a code span still counts as a cell separator and trips `bad-table`. Rewrite the command to avoid the pipe (e.g. `git rev-list --count` instead of `git log | wc -l`).

**Cross-lesson references.** Lessons refer back precisely — "Lesson 3.3 section
04". These are load-bearing for the course's argument; if you renumber sections,
fix the references. `renumber_lessons.py` handles file/id renames but will not
catch prose section references.

---

## 4. Commands that work (with the gotchas)

Run everything from `~/projects/RELS/398`. All scripts here are `runpy` shims to
`shared/scripts/` — **never fork one into this repo** (§0.1).

```bash
# Lint — the gate. Run before every commit.
python3 scripts/lint_lesson_content.py --course-dir .

# Question banks. Lesson id is a STRING.
python3 scripts/question_bank.py 1.1
python3 scripts/question_bank.py --all

# PDF notes. NOTE: --topic is an INT (topic number), --lesson is a STRING.
python3 scripts/compile_lesson_notes_pdf.py \
  --topic 1 --lesson 1.1 \
  --title "Local Git Version Control for Textual Scholarship" \
  --course-code "RELS 398" \
  --course-title "Digital Methods for Historical Documents"

# Status board
python3 scripts/status.py
```

The `--topic` int / `--lesson` string split is consistent with §0.2 but is not
guessable and cost me two failed invocations.

**Verified toolchain on this machine:** typst 0.11.1 at `~/.local/bin/typst`,
pandoc 3.1.11.1, Chrome CDP live on `:9222`.

---

## 5. Immediate next task: question banks

**14 remaining**, 30 questions each = 420 questions. This is the bulk of the work
and it needs no new research — it is authored from content that already exists.

Data modules live in `scripts/banks/lesson_<major>_<minor>.py` (dots are illegal
in module names, so `7.3` → `lesson_7_3.py`). The builder generates and validates
the XML, so hand-written XML is unreachable — which is the point.

Read `scripts/banks/lesson_1_1.py` as the model. The contract:

```python
from question_bank import Q
TOPIC = "Topic_01_Orientation"          # must match the src/modules/ folder name
TITLE = "Local Git Version Control for Textual Scholarship"
QUESTIONS = [
    Q("Thematic name matching the section",
      "Question stem; inline HTML allowed, use &lt;orig&gt; for literal tags.",
      correct=("The right answer.", "Correct. Why it is right."),
      wrong=[("A wrong answer.", "Incorrect. Why specifically it is wrong."),
             ("...", "..."), ("...", "...")],
      note="Restates the section's takeaway."),
    # ... 29 more, one per content section, in page order
]
```

Non-negotiables I applied throughout:

- **One question per content section, in page order.** Q7 tests section 07.
- **Every distractor gets its own diagnostic feedback** explaining why *that* answer is wrong. A bank without this is not done — it is the pedagogy.
- **`note=` restates the section takeaway**, becoming `<generalfeedback>`.
- **Four options**, exactly one correct.
- **Avoid `&` in the `name` field.** The builder escapes it, but names sit outside CDATA and a bare `&` there is the classic fatal `ParseError`.
- Distractors should be *plausible and diagnostic* — common misconceptions the lesson explicitly corrects, not filler.

Output lands at `src/modules/<TOPIC>/03b_Lesson_<id>_Questions.xml`.

---

## 6. Verification worth running

The linter does not check citations. This catches a cited work with no
References entry (it reports possessives like "Huskey's (2024)" as false
positives — check before acting):

```bash
python3 - <<'PY'
import re, pathlib
for f in sorted(pathlib.Path("src/modules").glob("*/03a_Lesson_*_Content.md")):
    t = f.read_text(encoding="utf-8"); refs = t.split("## References")[-1]
    for m in re.finditer(r"\(([A-Z][A-Za-zé]+)(?: et al\.| & [A-Z][A-Za-zé]+)?, (\d{4}|n\.d\.)", t):
        if m.group(1) not in refs:
            print(f"{f.name}: {m.group(1)} ({m.group(2)}) cited, not in References")
PY
```

After building a bank, confirm structure rather than trusting the exit code:

```bash
python3 -c "
import xml.etree.ElementTree as ET
r=ET.parse('src/modules/Topic_01_Orientation/03b_Lesson_1.1_Questions.xml').getroot()
qs=[q for q in r.findall('question') if q.get('type')=='multichoice']
print(len(qs),'questions')
print('all 4-option, one correct:', all(len(q.findall('answer'))==4 and
      [a.get('fraction') for a in q.findall('answer')].count('100')==1 for q in qs))
"
```

After a PDF, confirm it rendered rather than merely exited 0:

```bash
pdftotext dist/moodle/Topic_01_Orientation/04_Lesson_1.1_Notes.pdf - \
  | grep -cF '**Takeaway:**'      # expect 30
```

---

## 7. The images blocker

**This is the one piece of infrastructure that does not exist.** Everything
downstream — interactive XML, HTML player — is gated behind it, correctly:
`compile_interactive_lesson.py` exits non-zero when the image folder is empty,
and `--no-images` must never be added to a batch loop to make it pass (§0.3).

What is needed: a Gemini Notebook for the course. The id is passed once and then
remembered:

```bash
python3 scripts/generate_lesson_images.py --topic 1 --lesson 1.1 \
  --notebook "<notebook id or URL>" --cdp http://127.0.0.1:9222
# writes .gemini_notebook; later runs omit --notebook
```

**Ask Ken for the notebook** — do not create one unilaterally. Chrome is already
running with CDP on `:9222` and is signed in, so the moment the id exists this
stage is unblocked.

Note from prior sessions: the Notebook slide-deck UI has a **real 15-slide cap**,
so 30 sections means two decks per lesson — this is Phase D1's split-into-halves,
not a workaround. Images land as
`src/modules/<TOPIC>/03c_Lesson_<id>_Images/01.jpg … 30.jpg`, one per section.

Also note `generate_lesson_images.py` takes `--style`, reused from a `.style` file
if omitted. 398 has no `.style` yet; a style clause should be chosen once and kept
consistent across all 16 lessons or the decks will not look like one course.

---

## 8. Research status

Reports live in `src/research_reports/`, one per topic, generated via Gemini Deep
Research through Chrome/CDP by Antigravity (working in parallel — expect new
reports to appear as untracked files; check `git status` before assuming a topic
is missing).

| Topic | Words | Citations | State |
|---|---|---|---|
| 01 Orientation | 9,622 | 114 | used |
| 02 Cataloguing | 7,764 | 170 | **re-run; now usable** |
| 03 IIIF Imaging | 8,828 | 112 | used |
| 04 Transcription | 16,148 | 291 | used |
| 05 Reconciliation | 8,975 | 112 | used |
| 06 Normalization | 7,875 | 109 | used |
| 07 Collation | 7,703 | 136 | used |
| 08 Apparatus | 6,949 | 112 | ready, unwritten |
| 09 Lemmatization | 7,548 | 136 | ready, unwritten |
| 10–13 | — | — | not yet generated |

**Topic 02 history worth knowing:** its first report was 619 words — properly
cited but far too thin to source 30 sections × 3 lessons without heavy uncited
padding. It was held back and re-run, and is now in line with the others. Apply
the same judgement: a report under ~5,000 words is a re-run candidate, not a
writing input. §B4's `audit_reports.py` exists for exactly this check.

---

## 9. Suggested order

1. **Finish question banks for the 16 written lessons.** Mechanical from existing content, unblocks PDFs for all 16, no external dependency.
2. **Batch the PDFs** once banks exist.
3. **Get the notebook id from Ken**, then images, then interactive XML.
4. **Write Topics 02, 08, 09** (9 lessons) — research is ready and fresh.
5. **Topics 10–13** as their research lands.

Steps 1 and 4 are independent and either order works. Step 3 needs a human.

---

## 10. Working agreements

- **Commit per topic**, not per lesson — messages have been substantive, naming what each lesson covers and confirming lint passed.
- **Lint before every commit.** Note that `lint … | tail` masks the exit code; check `$?` explicitly or don't pipe.
- **Never `--no-images`** in a batch loop.
- **Never fork a shared script** into `398/scripts/`.
- `/sit` and `/stand` are the session boundary; `/sit` is read-only on remotes, `/stand` is the only thing that pushes. I pushed directly this session at Ken's request — follow his lead rather than assuming.
- `private/` is gitignored and holds student PII. Never move anything into a tracked directory.
