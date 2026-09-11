#!/usr/bin/env python3
"""Deploy Lesson 3.3 interactive quiz on RELS 398 (Section 3).
Purges old categories, imports new 60-question bank, recreates quiz, restores ordering and restrictions.
"""

import sys
from pathlib import Path

COURSE_DIR = Path("/home/kmpenner/projects/RELS/398")
sys.path.insert(0, str(COURSE_DIR.parent / "shared" / "scripts"))
from moodle_automation import MoodleDriver

COURSE_ID = 51185
SECTION = 3
CDP_URL = "http://127.0.0.1:9222"
DIST = COURSE_DIR / "dist" / "moodle" / "Module_03_IIIF_Imaging"

def linked_question_names(driver, cmid):
    driver.page.goto(
        f"{driver.base_url}/mod/quiz/edit.php?cmid={cmid}",
        wait_until="domcontentloaded",
    )
    driver.page.wait_for_timeout(2500)
    names = driver.page.evaluate(
        """() => Array.from(document.querySelectorAll(
               '.questionname, a[href*="question/question.php"]'
           )).map(e => e.textContent.trim()).filter(Boolean)"""
    )
    return sorted({n for n in names if len(n) < 120})

def main():
    title = "Lesson 3.3: Interactive Quiz"
    xml = DIST / "03_Interactive_Lesson_3.3.xml"

    print("=" * 72)
    print(f"{title}  <-  {xml.name}")

    if not xml.exists():
        sys.exit(f"Bank XML missing: {xml}")

    with MoodleDriver(course_id=COURSE_ID, cdp_url=CDP_URL) as driver:
        details = driver.get_section_cm_details(SECTION)
        by_title = {str(cm.get("name", "")).lower(): cm for cm in details}

        cm = by_title.get(title.lower())
        if not cm:
            sys.exit(f"No such quiz '{title}' live in Section 3")

        cmid = cm.get("id")
        attempts = driver.get_quiz_attempt_count(cmid)
        print(f"Live cmid={cmid}, attempts={attempts}")
        if attempts:
            sys.exit("Students have attempted this quiz; aborting.")

        # Find position of Lesson 3.3 Notes (PDF) to place the quiz right before it
        notes_cm = by_title.get("lesson 3.3 notes (pdf)")
        notes_cmid = notes_cm.get("id") if notes_cm else None
        print(f"Target preceding position: before notes cmid={notes_cmid}")

        # Resolve categories
        paths = driver.get_category_paths()
        target_tail = "03_Interactive_Lesson_3.3"
        stale_tail = "Lesson_3.3_Interactive"
        target = [(cid, p) for cid, p in paths.items() if p and p[-1] == target_tail]
        stale = [(cid, p) for cid, p in paths.items() if p and p[-1] == stale_tail]

        for cid, p in target:
            print(f"Category (XML-declared): {cid} {'/'.join(p)}")
        for cid, p in stale:
            print(f"Category (stale duplicate): {cid} {'/'.join(p)}")

        print(f"Deleting old quiz cmid={cmid} ...")
        driver.delete_activity(int(cmid))

        for cid, p in target + stale:
            print(f"Purging questions in {'/'.join(p)} (cat={cid})")
            driver.purge_question_category(cid, name="/".join(p))

        print(f"Importing {xml.name} ...")
        driver.import_question_xml(xml, label="Lesson 3.3 questions")

        # Re-resolve fresh category
        paths = driver.get_category_paths()
        fresh = [(cid, p) for cid, p in paths.items() if p and p[-1] == target_tail]
        if not fresh:
            sys.exit(f"Category '{target_tail}' not found after import")

        cat_id = fresh[0][0]
        print(f"Creating quiz against cat={cat_id} ...")
        new_cmid = driver.create_quiz(SECTION, title, cat_id)
        print(f"New quiz created: cmid={new_cmid}")

        if notes_cmid:
            print(f"Moving new quiz (cmid={new_cmid}) before Notes PDF (cmid={notes_cmid}) ...")
            driver.move_activity(new_cmid, target_section_num=SECTION, before_cmid=notes_cmid)

            print(f"Updating completion restriction on Notes PDF (cmid={notes_cmid}) to require Quiz cmid={new_cmid} ...")
            driver.add_completion_restriction(notes_cmid, "Lesson 3.3 Notes (PDF)", new_cmid)

        names = linked_question_names(driver, new_cmid)
        print(f"VERIFY cmid={new_cmid}: {len(names)} linked question labels")
        for n in names[:10]:
            print(f"    {n}")
        if len(names) > 10:
            print(f"    ... and {len(names) - 10} more questions")

    print("=" * 72)
    print("Lesson 3.3 quiz successfully deployed and verified!")

if __name__ == "__main__":
    main()
