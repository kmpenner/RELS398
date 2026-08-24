# RELS 398 — schedule & syllabus revision, handoff

**Session date:** 2026-08-24 · **State:** changes written to disk, both PDFs compile, **nothing committed.**

---

## 1. What prompted this

Question was "we have a syllabus; could the schedule be improved?", then extended to:
are the 13 stages appropriate, and is it reasonable for each week to run three steps
across the three meeting days —

1. **Tue** manual, in a text editor
2. **Wed** deterministic, off-the-shelf specialist software
3. **Fri** AI-assisted (LLMs, Antigravity, Claude Code, Hermes)

Both questions were to be informed by a Scholar Labs best-practices search per
`shared/LESSON_PIPELINE.md` §B2.

---

## 2. Findings

### 2.1 The calendar layer was already correct

Every date in the old schedule checks out against `shared/term-dates-2026-27.md`:
all 36 meetings on the right weekdays, closures (Wed Sep 30, Wed Nov 11, Thu Dec 3)
correct, study break Oct 12–16, Fri Dec 4 Wednesday-timetable correct, and Mon Dec 7
correctly excluded (Tue/Wed/Fri course). **No date was changed in this revision.**
Class numbers #1–#36 are also unchanged.

### 2.2 Evaluation weights summed to 95, not 100 — FIXED

`\evaltotalrow{100}` printed a total the ten `\evalrow` entries never reached
(5+15+5+5+5+5+20+20+10+5 = 95). Inherited: present in `archive/RELS 398 Syllabus_2026-08-11.html`
too, so the LaTeX transition did not introduce it.

Separately the schedule promised a "Comprehensive Digital Edition Portfolio" in the
exam period that appeared nowhere in the evaluation table — students were being asked
for exam-period work worth zero.

**Fix applied (your decision):** added a `Comprehensive Digital Edition Portfolio` row
at 5%. All ten pre-existing rows untouched. Verified sum = 100.

### 2.3 The stages are right; the schedule had drifted from your own published model

The Scholar Labs sequencing search returned, as its top hits, **your own two 2026
chapters** in *Artificial Intelligence for Bible Translation…*:

- *The Scholarly Edition Workflow: Tradition Meets Technology* (Penner 2026)
- *Evaluating AI for the Digital Scholarly Edition* (Penner 2026)

Scholar's synthesis describes a seven-stage traditional process rendered as a ten-step
undergraduate sequence: **manuscript identification (catalogue) → transcription →
reconciliation → normalizing → … → presentation**, ending in a TEI-conformant file with
teiHeader catalogue info, diplomatic transcription, normalized text with variants,
lemmas and parsings, translation, and comments.

Two drifts from that model, both now corrected:

**(a) "Reconciliation" had been deleted.** Your archived Aug 11 schedule had it as
Week 5 — *"comparing manual and automated transcriptions, double-keying error rates,
consensus text building"*, reading Haaf et al. on double-keying correctness. The
current version replaced it with Normalization. Restored to Week 5.

**(b) TEI arrived too late.** Students were asked for a TEI Header in W2, TEI ch. 11
encoding in W5, and an apparatus in W6 — but "TEI XML Schema" was not taught until W7.
Two independent sources say structure comes first:

- **Bodard & Stoyanova 2016** (cited 33) *changed* the EpiDoc training sequence away
  from detailed markup first to **document structure first**, because it "proved
  clearer and more comprehensible to students."
- **Russell et al. 2023**: working through data models before encoding "helps students
  articulate assumptions about the text structure."

TEI/XML fundamentals and schema validation moved into **Week 2**, where the Header
assignment already needs them.

Two things the literature says were already right and were kept: Bodard & Stoyanova put
**lemmatizing and indexing last** (kept at W9), and **Pierazzo 2016** (cited 401) begins
with **choosing the object to edit** — which the schedule never scheduled. Week 1 now
carries an ungraded "choose your manuscript passage by Fri Sep 4" gate.

Other supporting hits: Dahlström & Doracic 2009 (cited 32, whole digitization chain);
Rehbein & Fritze 2012 (cited 43, "learning-by-project", each phase builds the next —
supports the cumulative single-edition model); Caers 2024 *Quaerendo*, "Teaching
handwritten text recognition: can new technologies save old skills?"; "Training eyes and
training hands in the digital research with manuscripts".

### 2.4 The three-step cycle is sound — but not for all 13 weeks

**Why it works:** the Tuesday manual pass produces the **ground truth** that Wednesday's
deterministic output and Friday's AI output are measured against. That is how HTR and
collation are actually evaluated (CER/WER against a gold standard), so the Friday
deliverable becomes a three-way comparison with error rates and a judgment, not just
"do the task." It also does real work for the AI policy: a student cannot pass off AI
output as their own when Tuesday already recorded what they produced by hand.

**Day mapping is right as-is:** Tue→Wed is ~26 h, Wed→Fri ~47 h. Manual and deterministic
*should* be tightly coupled; the longer gap correctly sits before the AI day, which needs
the most independent judgment.

**Where it does not fit — now declared in the rows rather than forced:**

| Week | Why it departs |
|---|---|
| 1 Orientation | Setup week — no method to run three ways |
| 3 IIIF Imaging | Infrastructure; no manual analogue |
| 10 Consolidation | Deliberately no new method |
| 13 Publication | Studio/assembly week |

**The short-week collision (the load-bearing finding).** Wed Sep 30 and Wed Nov 11 are
closures, so in Weeks 5 and 10 **the deterministic day is the one that disappears.** The
old schedule put Normalization in W5 (where the deterministic pass *is* the content) and
Translation Alignment — a 20% item — in W10. Both were bad choices.

**Fix applied (your decision):** W5 = Reconciliation, whose entire subject *is* the
manual-vs-automated comparison, so losing the middle day costs nothing. Interlinear
Glossing merged into Translation Alignment (W11), freeing **W10 as a consolidation and
peer-review week** — the schedule's only slack across ten deadlines.

### 2.5 Deadline rhythm: every assignment now lands one week after its topic

Previously all ten assignments were due on the Friday of the week their topic was
introduced — no practice interval anywhere in the term, and the two 20% items got the
same three-days-and-submit footprint as the 5% items. The first deadline was also the
remote-delivery day.

New mapping (dates unchanged; only due dates moved):

| Assignment | % | Was | Now |
|---|---|---|---|
| Cataloguing & Metadata | 5 | Fri Sep 25 | **Fri Sep 18** |
| Transcription (incl. reconciliation report) | 15 | Fri Oct 2 | Fri Oct 2 |
| Normalization | 5 | Fri Oct 9 | **Fri Oct 23** |
| Textual Variants & Collation | 5 | Fri Oct 23 | **Fri Oct 30** |
| Linguistic Markup | 5 | Fri Oct 30 | **Fri Nov 13** |
| Interlinear Glossing | 5 | Fri Nov 6 | **Fri Nov 27** |
| Translation Alignment | 20 | Fri Nov 13 | **Fri Nov 27** |
| Scholarly Commentary | 20 | Fri Nov 20 | **Fri Dec 4** |
| Edition Introduction | 10 | Fri Nov 27 | **exam period** |
| Print-Ready Publication | 5 | Fri Dec 4 | **exam period** |
| Digital Edition Portfolio | 5 | *(did not exist)* | **exam period** |

Mid-term grades (due Mon Oct 26) still have three assignments in by then.
Glossing + Alignment share Fri Nov 27 deliberately — word-level and sentence-level
alignment of the same passage, one submission.

---

## 3. Files changed (uncommitted)

| File | Change |
|---|---|
| `RELS 398 Schedule.tex` | Rewritten: topic sequence, three-step cycle per week, new due dates, short lesson titles |
| `RELS 398 Syllabus.tex` | Added Portfolio 5% row; weights now sum to 100 |
| `RELS 398 Schedule.pdf` | Recompiled (5 pp, xelatex exit 0) |
| `RELS 398 Syllabus.pdf` | Recompiled (3 pp, xelatex exit 0) |
| `03_Research/SCHOLAR_LABS_PAPERS.md` | **New** — rendered Scholar Labs catalogue (§B2 artifact) |
| `03_Research/scholar_labs/` | **New** — raw result JSON, query sets, and the runner scripts |
| `HANDOFF_schedule_revision.md` | This file |

Pre-edit backup of the schedule: `/tmp/.../scratchpad/Schedule.tex.bak` (ephemeral —
`git diff` against HEAD is the reliable record, since nothing is committed).

Suggested commit split:

```bash
cd ~/projects/RELS/398
git add "RELS 398 Syllabus.tex" "RELS 398 Syllabus.pdf"
git commit -m "Fix syllabus evaluation weights: add Digital Edition Portfolio row, total now sums to 100"

git add "RELS 398 Schedule.tex" "RELS 398 Schedule.pdf"
git commit -m "Restructure schedule: restore Reconciliation week, move TEI fundamentals to Week 2, add three-step weekly cycle, stagger due dates one week after topic"

git add 03_Research HANDOFF_schedule_revision.md
git commit -m "Add Scholar Labs pedagogy search results and schedule revision handoff"
```

---

## 4. Open items — NOT done

1. **Lesson column is too narrow — unfixed.** `stfx_schedule.sty:49` sets it to
   `p{0.78in}`, sized for a lesson number, not a title. LaTeX hyphenates rather than
   overflows, so only a trivial `Overfull \hbox` warning fires and the damage is invisible
   in the log. The old PDF rendered `4. Tran-/scription/Platforms:/Tran-/skribus &/THREAD`.
   **Mitigated, not fixed:** lesson titles are now one or two words (`4. Transcription`,
   `5. Reconciliation`) with detail moved to the Activities column. The real fix is a
   column rebalance — `Lesson` is starved at 0.78in while `Activities` has 4.02in — but
   `stfx_schedule.sty` is **byte-identical to `shared/pdf-pipeline/`**, so widening it
   touches all twelve courses. Not changed unilaterally.
2. **`Copyright © 2027` on a Fall 2026 document.** Hardcoded at
   `stfx_schedule.sty:65,67`. May be deliberate (academic year 2026–27). Shared — affects
   every course. Needs a decision.
3. **`03_Research/RESEARCH_PROMPTS.md` does not reflect the three-step cycle.** It mentions
   AI once in 433 lines, and its topic list is the *old* sequence (still has "TEI XML Schema
   & Linguistic Markup" at Topic 7, no Reconciliation topic). Both the topic list and the
   Stage 1/Stage 2 prompts need re-templating against the revised schedule, or Phase B
   research will not support the course as now designed.
4. **398 uses the retired layout.** `00_Syllabus_and_Admin/`…`04_Media_and_Transcripts/`
   rather than the mandatory `raw/ src/ dist/ config/ scripts/ private/` of
   LESSON_PIPELINE §A3. There is also no `scripts/` shim, so no Phase B or C–E tooling runs
   from this repo. `shared/scripts/migrate_222_layout.py` may be the starting point.
5. **`To_Do.md` is stale.** §1a claims `term` is TBD; `course.json` has had `"Fall 2026"`
   since commit `d9ea2ca`. Other items (git remote, OneDrive import) may also be resolved.
6. **The syllabus prose was not updated to match.** §2.5 moved every due date and the
   Course Overview still does not state that the ten assignments are cumulative stages of a
   single edition — which is the whole rationale for the structure, and what Rehbein &
   Fritze's "learning-by-project" finding supports. Recommend adding one paragraph.

---

## 5. Scholar Labs run — read this before re-running

**Only 2 of 10 queries returned results.** q01 (sequencing) and q03 (HTR pedagogy) each
returned 10 cards. All eight later queries returned **0 cards**, across two batches and
both abstract and domain-anchored phrasings.

My first hypothesis — that Labs refuses abstract "how effective is X" questions — is
**not supported**: q07 was tightly domain-anchored ("ground truth transcription, character
error rates, double-keying") and still returned 0. The result-page DOM carried
`"Scholar Labs is currently not designed for queries like this"` **and** `"You're on the
waitlist"`. The simpler explanation is a **per-session or daily Labs quota exhausted after
the first two queries**, which matches LESSON_PIPELINE §D3's account-level quota pattern.

Consequence: **the evidence base here is two queries deep, not ten.** The sequencing
conclusions (§2.3) rest on solid, well-cited hits. The claims about the three-step cycle
(§2.4) rest on q03 plus first-principles reasoning — the cumulative-assessment and
cognitive-load/spacing questions returned nothing and **were not substantiated.** Re-run
these on a fresh day before treating §2.4 as evidence-backed:

```
scholar_labs/queries2.json   # 04b, 02b, 07, 05b — all still unanswered
```

**Tooling note.** Phase B scripts remain 117-only and hardcoded (LESSON_PIPELINE §7 gap 1):
`117/scripts/run_scholar_search.py` has a literal question and Windows paths;
`batch_scholar_search.py` parses 117's lesson-card HTML. I wrote a generic runner —
`03_Research/scholar_labs/scholar_search.py --queries Q.json --out-dir D --md M.md` —
which is the obvious candidate to promote to `shared/scripts/` with `--course-dir`,
closing that gap. It needs Chrome on `--remote-debugging-port=9222`, signed in.

Two known rough edges in it: the `[PDF]` badge is captured **off by one** (Scholar renders
it after the card, so it attaches to the previous result — `title_link` is correct,
`pdf_link` is not trustworthy); and when a card's `raw_text` arrives without newlines,
`parse_block` dumps everything into `authors_venue_year`. `render.py` recovers that case,
but the JSON is raw.
