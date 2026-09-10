# RELS 398 — Session Handoff

**Date:** 2026-09-10 (evening)
**Repo:** `~/projects/RELS/398` (remote `https://github.com/kmpenner/RELS398.git`)
**Also touched this session:** `~/projects/RELS/shared` (2 commits), `~/projects/RELS/398/labs` (1 commit)
**Read first:** `LEDGER.md` — it is current as of this session and carries the settled decisions plus several traps.
**Supersedes** the 2026-09-09 handoff. That document's §0 (companion media) and §6 (next steps) are now largely done; read §3 below for what replaced them.

---

## 1. The short version

Everything needed for **Friday's Meeting #5 (Fri 11 Sep, 9:30–10:20, MULH 3032)** is live on Moodle and verified. The bigger job — rebuilding Lessons 2.2 and 2.3 away from their Greek-manuscript assumptions for a cohort of three students working on non-Greek documents — is done through the full build chain **except slide images**.

One thing is genuinely unfinished and needs a decision: **30 slide images per lesson are stale**, and the deployment is deliberately text-only to avoid shipping pictures that contradict the text.

---

## 2. What is deployed and verified live

Course 51185, Section 2. Verified against the rendered pages after deploy, not against script output.

| Item | cmid | State |
|---|---|---|
| Lesson 2.2 Notes (PDF) | 1431218 | rebuilt |
| Lesson 2.3 Notes (PDF) | 1431219 | rebuilt |
| Lesson 2.2: Interactive Quiz | 1431227 | rebuilt bank, 30 slots |
| Lesson 2.3: Interactive Quiz | 1431229 | rebuilt bank, 30 slots |
| Lesson 2.3: Infographic (label) | 1431247 | regenerated |
| Authority Control Guide (label) | 1431174 | live |

Notes PDFs are restricted until their quiz is complete. `moodle_manifest.json` is current.

**New cmids exist because labels, resources and quizzes are delete-and-recreate on this Moodle.** The old ones (1428514/1428515/1430835/1430839, and infographic 1431118) are dead and 404.

**A verification note worth keeping.** Checking the section by iterating `li.activity` undercounts it, because labels do not always render as `li.activity` — the 2.3 infographic appeared as a blank line and looked missing. Count `[id^="module-"]` instead, and to find a specific item's cmid walk up from its `<img>` to the ancestor whose id is `module-<cmid>`. `replace_activity` also returns `None` for label recreation while still creating the module, so never treat a `None` return as failure — confirm against the page.

### The quizzes *are* the interactive lessons

Confirmed by Ken, and recorded in the ledger as settled terminology. Each quiz holds 60 slots: 30 content pages plus 30 questions, one pair per section, in page order. There is no separate lesson-player activity, and do not go looking for one. When someone says "deploy the lesson", they mean the quiz.

---

## 3. What was rebuilt, and why

Ken: *"We need full content rebuild before Friday."*

The cohort is three students, none on a Greek literary manuscript:

- **Jay** — an Emily Dickinson manuscript
- **Olyvia** — an 18th-century French royal act
- **Andromeda** — the 1752 Peace and Friendship Treaty

Both lessons taught Greek sources as *the* authority tools and CTS URNs as *the* citation system. Neither applies to any of the three, and Module 2's workshop rubric — already rewritten this session — grades authority differently.

**Settled scope (Ken):** authority teaching belongs in **2.2**, where authority control is introduced. **2.3** covers only four objectives: find the information, record it in the header, generate it with an LLM, compare machine against manual. Both keep the 30-section house model. Trim the extraneous.

| | 2.2 | 2.3 |
|---|---|---|
| Content | 30 sections, 8,117 words | 30 sections, 8,211 words |
| Bank | 30/30 aligned | 30/30 aligned |
| Notes PDF | rebuilt | rebuilt |
| Interactive XML | rebuilt, text-only | rebuilt, text-only |
| Infographic | stale (see §4) | **regenerated** |
| Slide images | stale (see §4) | stale (see §4) |

**2.2** keeps its schema/validation spine. §14 became a two-layer authority treatment (general layer: VIAF, Wikidata, LC, Getty, GeoNames; tradition-specific layer that does *not* transfer, with a per-project table). The five CTS-URN sections that had students mint URNs for Genesis 1:1–1:14 became citation teaching serving all three documents: ARK vs call number vs archival reference, reading a record, dating traps.

**2.3** was cut to the four objectives. Removed: the ethics digression, and four prompting/validation sections that duplicated the rewritten block. Merged: the six-field scorecard, precision/recall, and difference-sorting sections into one. Added seven sections where the objectives were thinnest — the dossier checklist, choosing the right element, converting counts into a defensible claim, and what the marker looks for.

Full detail in commit messages `5143aa1`, `24a58c0`, `6b68bc9`, and in `LEDGER.md` §5.

---

## 4. The one unfinished thing: slide images

**Every slide image in both lessons is stale.** The 30 files per lesson date from 2026-08-26 and carry rendered section headings, so the rewrite invalidated all of them. 2.2's image 20 is literally titled "CTS URN Anatomy" and now sits above text retitled "Three Citation Systems, Three Traditions".

**The deployment is text-only because of this.** Both interactive XMLs were compiled with `--no-images` (2.2 3.24 MB → 0.14 MB, 2.3 → 0.13 MB, all 61 question elements intact). Ken chose this over shipping mismatched art.

**Quota:** Ken mentioned ~15 slide images available. One infographic was spent this session, so the 15 remain unspent. Ken's instruction: **prioritise 2.3.** Decide whether to spend all 15 there (the rewritten block is roughly sections 6–13 and 22–29) or split with 2.2.

**Before spending any quota, fix the notebook sources** — see §5. The media and image scripts select sources *by filename* from the notebook, so a stale upload silently produces art for the superseded lesson.

**The 2.2 infographic is also stale** — it was regenerated 2026-09-09 for the previous 2.2 and has not been redone. It is currently live.

---

## 5. Traps — read before touching the media pipeline

### Stale notebook sources

The notebook holds `Lesson_2.2_part1/2.md` and `Lesson_2.3_part1/2.md`. `generate_lesson_images.py` refuses to run when the on-disk text differs from what was uploaded, warning the deck would illustrate superseded content. **That guard is correct and must not be bypassed with `--replace-source`** — on the images script that flag means "deliberately reuse the stale upload", the opposite of what is wanted.

The correct fix:

1. Generate the staging halves (`generate_lesson_images.py --topic 2 --lesson X --force`; it writes `.staging_LX.Y/` and stops).
2. Refresh each source with `notebook_ui.replace_source(page, md_path)`.
3. **Reconcile `03c_Lesson_X.Y_Images/.sources.json`** — it holds the SHA-256 of the text actually in the notebook. `replace_source` updates the notebook but not this file, so the guard keeps firing until you set it to the new digest.

Both 2.2 and 2.3 were refreshed this session, so the sources are current as of now.

### Sandbox blocks Chrome downloads

Chrome's default download target is `~/Downloads`, which the workspace sandbox mounts **read-only**. Any browser-download-based media script will report an empty file **even though generation succeeded**. This cost several attempts on the infographic.

Redirect the download into the workspace on the **same CDP session**:

```python
cdp = ctx.new_cdp_session(page)
cdp.send("Browser.setDownloadBehavior",
         {"behavior": "allow",
          "downloadPath": "/home/kmpenner/projects/RELS/398/scratch/chrome-downloads",
          "eventsEnabled": True})
```

It does not persist across separate `connect_over_cdp` calls. `notebook_ui._download_from_card`'s fallback searches only `~/Downloads` and `/tmp`, so it will not find the file — check the redirect directory directly. Recorded in `LEDGER.md`.

### Other traps carried forward

- **`--no-images` was broken** in both lesson compilers and is now fixed (`shared` f8ed8fa). In `compile_interactive_lesson.py` it only suppressed the safety check and then embedded images anyway; `generate_interactive_html_lesson.py` had no flag at all. If a text-only build ever ships illustrated again, suspect a regression here.
- **Parallel Moodle question categories.** Module 2 had *both* `course/03_Interactive_Lesson_2.2|2.3` (originals) and `Module_02_Cataloguing/Lesson_2.2|2.3_Interactive` (freshly imported). `create_quiz` resolves the `03_Interactive_Lesson_X` name first, so a new quiz can silently link to the *old* questions. This happened — the first deploy served pre-rebuild questions and reported success. Purge **both** sets before importing. **After any quiz deploy, read the linked question names off the live quiz**; do not trust the script output.
- **A quiz holding questions blocks the hard-delete of those questions.** Delete the quiz, then purge, then import, then create. `populate_moodle_topic.py` is fixed (`shared` a3584b3) but direct driver calls must respect the order.
- **Deleting a quiz orphans anything restricted on it.** Notes PDF restrictions must be re-pointed at the new cmid.
- **`generate_lesson_media.py` exits 0 without doing anything when outputs exist.** Use `--force`.
- **Verify the signal, not the proxy.** Three separate times this session an operation reported success while the live state disagreed, and once a verification read a stale page and reported a failure that had not happened. Check rendered pages, byte hashes, and live cmids.

---

## 6. Loose ends outside the immediate work

1. **`labs/` is a nested git repo with no remote.** It holds `witness.xml`, the seeded demo file and `msdesc.rng`. Committed but **unbacked-up**. Decide: give it a remote, gitignore it from 398, or move it out of the tree.
2. **`.staging_L3.3/Lesson_3.3_part1.md` is still tracked** from earlier work. `.staging_*/` is now gitignored so it will not recur, but this one is already in history — remove it when convenient.
3. **`lesson_2_1.py` question names do not match its markdown section titles.** 1.1, 2.2 and 2.3 now follow the strict one-to-one convention; 2.1 uses loose thematic names.
4. **The 2.2 question bank was stale before this session** — 25 of 30 titles mismatched, dating from `220b5e7`, which rewrote the lesson and never rebuilt its bank. Worth a sweep of the other 32 banks for the same pattern.
5. **Remaining novice rewrites:** 16 lessons from the 2026-08-26 bulk-authored cohort (Modules 08–13).
6. **Course is still hidden from students**; Modules 4–13 are empty shells.

---

## 7. Student project findings that may affect teaching

Researched this session; full reports in `private/student_projects/` (gitignored — it names students).

- **Jay cannot do "a letter".** Houghton's Dickinson *letters* are restricted to the Harvard network; only the poetry manuscripts are open access. Verified four times on Houghton's own collection page. Recommended substitute: `MS Am 1118.3 [338]`, a wrapping-paper draft. **He may already have started on a letter — worth telling him.**
- **Andromeda's object is the 1752 treaty.** Ken confirmed the "1753" was his misremembering; the research independently found no 1753 treaty exists.
- **Fabricated authority identifiers return HTTP 200.** Verified for VIAF. A student link-checking will certify a hallucination. Now in the Authority Control card.

---

## 8. Working agreements (unchanged)

- Lint before every commit: `python3 ../shared/scripts/lint_lesson_content.py --course-dir .` — currently **1 issue**, the pre-existing dangling citation in 13.1.
- Commit per repo, per topic; substantive messages; lint status noted.
- Never fork shared scripts into `398/scripts/` — thin `runpy` wrappers only.
- `/sit` is read-only on remotes; `/stand` is the only push.
- `private/` holds student PII; gitignored; nothing moves out of it.
- Question banks: one question per section in page order, diagnostic feedback on every distractor, `note=` restates that section's takeaway. **Rebuild the bank in the same commit as any content change** — that is the failure mode from `220b5e7`.
- Slide images are titled with rendered section headings, so **any lesson rewrite invalidates its images.**

---

## 9. If you only do one thing

**Regenerate the 2.3 slide images.** Fifteen are affordable and Ken asked for 2.3 to be prioritised. Fix the notebook sources first (§5), then run `generate_lesson_images.py --topic 2 --lesson 2.3 --force`. Recompile the interactive lesson *with* images afterwards, and redeploy the quiz.

The second priority is the 2.2 infographic, which is live and stale.
