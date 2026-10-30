# RELS 398 slide audit: Lessons 8.3, 9.1, 9.2, 9.3 (2026-10-29)

Read-only. The src and dist decks are identical. Wikidata IDs were checked live today, and the spaCy code was run in `RELS/.venv` (spaCy 3.8.16, en_core_web_sm and fr_core_news_sm 3.8.0).

## Common to all four

- **Slide count:** 8.3 and 9.3 have 16 slides, because the Friday diff-and-merge slide (ledger 2026-10-23) was added. 9.1 and 9.2 have 15.
- **Speaker notes:** on every slide, 81–103 words each.
- **Meeting numbers, dates, times and room:** all correct.
- **Font sizes:** content text is 16–40pt. Each slide also has three chrome runs at 10/11/12pt (course header, clock, footer), so the 16pt floor holds for content only.
- **Pictures:** none. Every slide is text-only, and most have about 8 bullets plus a banner sentence, which is dense for projection.
- **Leftovers:** no Jay/Dickinson references and no Greek/CLTK content in these decks.

## 8.3, tomorrow (Fri Oct 30, #22)

1. **Slide 11, "Cohort Case Studies":** states results as already found, e.g. "SpaCy guessed NOUN; AI recovered 'décréter'" and "AI easily handled informal tone". Nobody has run Friday's AI step yet. Reword it as things to look for, or fill it in from the students' actual Wednesday output.
2. **Slide 11, French example:** "décréter" from an imperfect in "-oit" is a guess about Ace's text. Check that the form is actually in the decree.
3. **Slide 2:** prints two lines of "Technologic" lyrics. Cut them to the title and artist, which is all that copyright allows.
4. **Slide 3:** says "Measuring precision and recall", but slide 9 scores accuracy, not P/R. Pick one.
5. **Slide 10:** the taxonomy has 4 categories, which is fine. Everything else is accurate enough for tomorrow.

## 9.1 (Tue Nov 3, #23)

1. **Slide 10:** the Maud Lewis `ref` is **Q2302306, a sea urchin**. The correct ID is **Q1479154**.
2. **Slides 5 and 9:** Hopson is given as **Q7169421, which is Pero Kovačević, a Croatian politician**. The correct ID is **Q7167799** (Peregrine Hopson, British Army general). This is the lesson that teaches students to verify `@ref`, so both IDs must be fixed before Tuesday.
3. **Slide 5:** `bnf:cb12255570v` and `geonames:6324729` are unverified (GeoNames rate-limited me). Check them by hand.
4. **Slide 2:** the "Fogarty's Cove" lines quoted ("Watch the waves roll in…", "Names carved on the headstones…") don't look like Stan Rogers's lyrics, so they're probably invented. Remove them.
5. **Slide 12:** "Chigabenakady". The treaty spells it "Chibenaccadie" (Shubenacadie). Use the diplomatic spelling.
6. **Slide 13:** check the name "Leonard Kinnear" against Olyvia's letter, which reads only "Mr. Kinnear". If the forename isn't in the source, it's invented.

## 9.2 (Wed Nov 4, #24)

1. **Slide 12, EntityRuler demo:** the code doesn't work as shown.
   - spaCy splits `Jean-Baptiste` into three tokens, so the `{'TEXT':'Jean-Baptiste'}` pattern never matches.
   - Run on "Chief Sachem Jean-Baptiste Cope", the statistical NER returns the clipped span "Sachem Jean-Baptiste Cope". That is the very boundary error the slide claims the ruler fixes.
   - The treaty's real spelling is "Major Jean Baptiste Cope" (no hyphen), so neither pattern fires on Andromeda's text.
   - Fix: use phrase patterns built from the treaty's exact strings.
2. **Slide 8:** these labels are the English model's. **fr_core_news_sm uses PER/LOC/ORG/MISC**, so Ace will see no PERSON or GPE labels, and the mapping table breaks for the French decree.
3. **Slide 6:** "Guarantees 100% precision" and "0% recall" overstate the case. A gazetteer still produces false positives on homonyms and capitalized common nouns ("King", "Treaty", the trap 9.1 slide 8 teaches), and recall depends on how complete the list is. Slide 12 repeats "100% precision".
4. **Slide 5:** "B- opens, O closes" is wrong. A span ends at the next B- or O, and also at the end of the text.
5. **Slide 14:** "four-part taxonomy (OOV, boundary, type, ambiguity)" doesn't match 9.3 slide 10's four classes, which have hallucination where this one has ambiguity. Align them.

## 9.3 (Fri Nov 6, #25)

1. **Slide 5:** uses `Q98471203` as an example of a Q-number "that does not exist". **It exists** (Hui Qu, a researcher). **Slide 10's `Q9842109` also exists.** Replace both with IDs confirmed missing, or use the 9.1 slide 10 typo cases (real IDs that point to the wrong item), which teach the point better.
2. **Slide 10:** labels SpaCy output `B-PER`, but the English model gives `PERSON`. The "Everett: O (Missed)" row is filed under "Class 2: Boundary". A missed entity is a recall miss, not a boundary error.
3. **Slide 6:** says "temperature=0.0 for deterministic, repeatable outputs". Hosted LLMs aren't strictly deterministic even at 0. Say "more repeatable".
4. **Slide 1:** "VS Code Antigravity" mixes two different editors.
5. **Slide 16:** names Module 10 "Consolidation & Critical Apparatus". The ledger has "Editorial Consolidation & CI/CD".
6. **Slide 4:** pre-states that the LLM resolves Everett. Frame it as a hypothesis to test.

## The one deterministic tool for Week 9: spaCy `EntityRuler`, used as a gazetteer

- **Why this one:**
  - It's already in the lesson, the plan and the deck (Wednesday's slide title is "Automated NER and Gazetteer Lookup").
  - It's installed in the course venv, and it runs on both the English and the French texts.
  - Unlike spaCy's statistical `ner`, its output is a pure function of the pattern list, which is what "deterministic" means in the Tue/Wed/Fri cycle. A statistical model is still a learned guess, so it is a weak stand-in for the "rules" step.
- **How to run it:**
  - Each student builds the gazetteer (phrase patterns, each with an `id` holding the verified `@ref`) from their own `ENTITY_POLICIES.md` registry list.
  - Run it with `overwrite_ents=True`, and score it against Tuesday's file.
- **What's left for the reflection:**
  - Statistical NER becomes the comparison inside Wednesday, not the tool.
  - Precision then fails only on homonyms. Recall then fails only on names missing from the list, which shows what deterministic lookup can and cannot do.
- **The deck needs a fix first:** slide 12's patterns must be corrected (see 9.2 #1), or the live demo will fail in class.
