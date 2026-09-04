import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

shared_dir = Path(__file__).resolve().parents[3] / "shared" / "scripts"
sys.path.insert(0, str(shared_dir))
from question_bank import Q

src_mod = Path("src/modules/Module_10_Consolidation")
dist_mod = Path("dist/moodle/Module_10_Consolidation")
src_mod.mkdir(parents=True, exist_ok=True)
dist_mod.mkdir(parents=True, exist_ok=True)

# 1. Banner Image (1200x300)
def create_banner():
    w, h = 1200, 300
    img = Image.new("RGB", (w, h), color="#172554")  # deep cobalt blue / slate
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, w-10, h-10], outline="#c29b38", width=2)
    draw.rectangle([16, 16, w-16, h-16], outline="#1e40af", width=1)
    draw.rectangle([20, 20, 35, h-20], fill="#ea580c")  # iron rust / warm orange accent
    
    try:
        font_course = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font_course = font_title = font_sub = ImageFont.load_default()
        
    draw.text((60, 45), "RELS 398 / ENGL 398  •  DIGITAL METHODS FOR HISTORICAL DOCUMENTS", fill="#c29b38", font=font_course)
    draw.text((60, 100), "Module 10: Editorial Consolidation & CI/CD", fill="#f8fafc", font=font_title)
    draw.text((60, 175), "Collaborative Git  •  Conflict Adjudication  •  Automated Schema CI Gates", fill="#cbd5e1", font=font_sub)
    draw.line([60, 225, w-60, 225], fill="#c29b38", width=1)
    draw.text((60, 245), "StFX Department of Religious Studies  •  Computational Philology Pipeline", fill="#93c5fd", font=font_sub)
    
    for p in [dist_mod / "01_Banner.png", src_mod / "01_Banner.png"]:
        img.save(p, "PNG")
        print(f"Wrote banner: {p}")

create_banner()

# 2. Learning Objectives
obj_html = """<div class="card p-3 mb-3 border-info" style="border-left: 5px solid #ea580c; background-color: #fff7ed; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #9a3412; margin-top: 0;">Module 10: Editorial Consolidation & CI/CD — Learning Objectives</h4>
    <p>By the end of this module, students will be able to:</p>
    <ul>
        <li><strong>Orchestrate</strong> distributed Git collaboration workflows, including repository forking, branch management, pull requests, and upstream synchronization.</li>
        <li><strong>Adjudicate and resolve</strong> merge conflicts inside complex TEI XML documents without introducing malformed markup or corrupting witness readings.</li>
        <li><strong>Execute</strong> comprehensive validation sweeps across multi-file edition corpora using <code>xmllint</code>, Relax NG, and Schematron.</li>
        <li><strong>Implement</strong> continuous integration (CI) pipelines using GitHub Actions to automate schema validation gates upon push.</li>
        <li><strong>Conduct</strong> scholarly peer code reviews, opening clear, actionable issue tickets and verifying reproducibility across editorial milestones.</li>
    </ul>
</div>"""

# 3. Readings
reading_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #c29b38; background-color: #fcfcfd; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c29b38; margin-top: 0;">Assigned Readings & Foundational Scholarship</h4>
    <p>Please review the following documentation and editorial standards for distributed digital collaboration:</p>
    <ul>
        <li><strong>Chacon, Scott and Ben Straub.</strong> <em>Pro Git</em>, 2nd Edition. Apress, 2014. Focus on Chapter 3 (Git Branching) and Chapter 6 (GitHub Workflows).</li>
        <li><strong>Driscoll, Matthew James and Elena Pierazzo.</strong> <em>Digital Scholarly Editing: Theories and Practices</em>. Open Book Publishers, 2016. Focus on collaborative quality assurance and project management.</li>
        <li><strong>TEI Consortium.</strong> "Validating TEI Documents." <em>TEI P5 Guidelines</em>, Version 4.8.0, 2024.</li>
    </ul>
</div>"""

# 4. Watch List
watch_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #ea580c; background-color: #fff7ed; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #9a3412; margin-top: 0;">Curated Media & Technical Walkthroughs</h4>
    <p>Review these video demonstrations before completing your workshop assignment:</p>
    <ul>
        <li><strong>Git Forking & Pull Request Workflows in Digital Humanities:</strong> Collaborative editing across distributed teams (22 mins).</li>
        <li><strong>Resolving TEI XML Merge Conflicts in VS Code:</strong> Navigating conflict markers and maintaining structural validity (24 mins).</li>
        <li><strong>Setting Up GitHub Actions for TEI Validation:</strong> Automating <code>xmllint</code> and Relax NG checks on every commit (19 mins).</li>
    </ul>
</div>"""

# 5. Workshop
ws_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #ea580c; background-color: #fff7ed; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #9a3412; margin-top: 0;">Workshop: Collaborative Pull Request, Merge Conflict Resolution & Validation Sweep</h4>
    <p><strong>Overview:</strong> In this consolidation workshop, you will collaborate with a partner to intentionally create, inspect, and resolve a Git merge conflict in a shared TEI XML file. You will then run an exhaustive validation sweep across all your semester edition files, ensuring 100% schema compliance before the final publishing modules.</p>
    <p><strong>Deadlines:</strong> Comparison Post due Friday by 11:00 PM; Peer Reviews due Monday by 11:00 PM.</p>
</div>"""

ws_sub = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Submission Instructions</h4>
    <ol>
        <li>Create a feature branch in your repository and invite your partner as a collaborator or work via fork/PR.</li>
        <li>Concurrently edit the same line of TEI XML in both branches to produce an intentional merge conflict.</li>
        <li>Open the conflicted file in VS Code, evaluate both conflicting readings against your facsimile evidence, combine them correctly into a single valid TEI block, and delete all conflict markers (<code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code>, <code>=======</code>, <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code>).</li>
        <li>Verify well-formedness with <code>xmllint --noout</code> and complete the merge commit.</li>
        <li>Run a complete validation sweep on all TEI XML files in your project directory against the official TEI All Relax NG schema, verifying zero validation errors.</li>
        <li>Submit your merged Git commit hash, terminal validation sweep log, and a <strong>300–500 word reflection</strong> on how continuous integration safeguards scholarly editions against accidental regression.</li>
    </ol>
</div>"""

ws_assess = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Peer Assessment Rubric</h4>
    <ul>
        <li><strong>Conflict Adjudication & XML Integrity (4 pts):</strong> The resolved XML file contains zero orphaned conflict markers and passes well-formedness and schema checks without data loss.</li>
        <li><strong>Validation Sweep Exhaustiveness (3 pts):</strong> The terminal log confirms that all accumulated edition files (metadata, transcription, collation, linguistic markup) were audited and passed with 0 errors.</li>
        <li><strong>Continuous Integration Reflection (3 pts):</strong> The 300–500 word analysis insightfully discusses how automated CI checks and disciplined Git branching protect complex digital editions from configuration drift.</li>
    </ul>
</div>"""

# 6. Write HTML components
for mod_p in [dist_mod, src_mod]:
    (mod_p / "02_Learning_Objectives.html").write_text(obj_html, encoding="utf-8")
    (mod_p / "05_Reading_List.html").write_text(reading_html, encoding="utf-8")
    (mod_p / "06_Watch_List.html").write_text(watch_html, encoding="utf-8")
    (mod_p / "08_Workshop_Description.html").write_text(ws_desc, encoding="utf-8")
    (mod_p / "08a_Workshop_Submission_Instructions.html").write_text(ws_sub, encoding="utf-8")
    (mod_p / "08b_Workshop_Assessment_Instructions.html").write_text(ws_assess, encoding="utf-8")
    (mod_p / "09_Quiz_Description.html").write_text("<p>Comprehensive weekly knowledge check covering collaborative Git branching, conflict adjudication, TEI schema validation sweeps, and continuous integration pipelines.</p>", encoding="utf-8")

print("Wrote HTML and Banner files.")

# 7. Build Weekly Quiz (10 Questions)
questions = [
    ("01 Question: Architecture of Distributed Git Repositories",
      "In a distributed Git workflow, what is the key functional distinction between `origin` and `upstream` remotes?",
      [
          ("`origin` refers to your personal fork of the repository on GitHub where you push work, while `upstream` points to the authoritative central project repository from which you fetch updates.", 100, "Correct. In fork-and-pull workflows, `origin` is your personal remote fork, and `upstream` is the central project repository."),
          ("`origin` is stored on your local hard drive, whereas `upstream` is stored in the computer's CPU cache.", 0, "Incorrect. Both `origin` and `upstream` are network remotes hosted on GitHub or another server."),
          ("`origin` only accepts text files, whereas `upstream` only accepts digital image files.", 0, "Incorrect. Git remotes track all file formats committed to the repository."),
          ("`origin` is deleted automatically whenever a pull request is merged.", 0, "Incorrect. Remote repository pointers persist indefinitely until manually deleted.")
      ]),
    ("02 Question: Anatomy of a Git Merge Conflict",
      "When Git encounters conflicting edits in a file during a merge, what does the text between `<<<<<<< HEAD` and `=======` represent?",
      [
          ("The local changes present on the currently checked-out branch before the merge was attempted.", 100, "Correct. `<<<<<<< HEAD` marks the start of the current branch's code, while `=======` separates it from the incoming changes up to `>>>>>>>`."),
          ("The remote changes made by another developer on GitHub.", 0, "Incorrect. Incoming changes appear between `=======` and `>>>>>>>`."),
          ("A fatal virus warning generated by the Linux kernel.", 0, "Incorrect. Conflict markers are standard Git notification delimiters."),
          ("An encrypted cryptographic hash representing the author's password.", 0, "Incorrect. Conflict markers contain human-readable plaintext from the conflicted branches.")
      ]),
    ("03 Question: Adjudicating Conflicts in TEI XML",
      "Why is simply choosing 'Accept Current' or 'Accept Incoming' in a merge conflict tool dangerous in TEI XML documents?",
      [
          ("Because both branches may contain valid, complementary editorial markup (e.g. one editor added a gloss while the other corrected an apparatus pointer) that must be merged rather than discarded.", 100, "Correct. Editorial conflicts in digital scholarship frequently require synthesising contributions from both branches rather than arbitrarily discarding one editor's scholarly work."),
          ("Because clicking either button triggers an immediate irreversible format of the user's hard drive.", 0, "Incorrect. Git never damages physical hardware."),
          ("Because XML schemas automatically crash if both versions are not identical.", 0, "Incorrect. Schemas evaluate validity of the resolved result, not previous versions."),
          ("Because GitHub bans user accounts that resolve conflicts in under five minutes.", 0, "Incorrect. GitHub imposes no time restrictions on conflict resolution.")
      ]),
    ("04 Question: Post-Conflict XML Well-Formedness Verification",
      "What command-line operation should an editor immediately execute after editing a conflicted TEI file to verify basic syntax before staging?",
      [
          ("`xmllint --noout <filename>.xml`", 100, "Correct. `xmllint --noout` quickly verifies that manual resolution did not leave unclosed tags, unbalanced brackets, or orphan conflict markers."),
          ("`rm -rf .git`", 0, "Incorrect. That disastrously deletes the entire Git repository history!"),
          ("`git push --force origin main`", 0, "Incorrect. Force-pushing unverified or broken files corrupts the shared repository."),
          ("`ping google.com`", 0, "Incorrect. Testing network connectivity does not validate XML file syntax.")
      ]),
    ("05 Question: Purpose of Continuous Integration (CI)",
      "What primary protection does a Continuous Integration (CI) pipeline (such as GitHub Actions) provide for a collaborative scholarly edition?",
      [
          ("It automatically runs schema validation and test suites on every pushed commit and pull request, preventing invalid XML or broken code from ever being merged into `main`.", 100, "Correct. CI acts as an automated quality gate, ensuring that all contributed files strictly conform to project schemas before merging."),
          ("It prints the edition on physical paper and mails it to the university library.", 0, "Incorrect. CI is an automated cloud-based software build and testing system."),
          ("It generates artificial student grades to reduce instructor marking workloads.", 0, "Incorrect. CI tests code and document validity, not academic student grading."),
          ("It renames all files with random numbers to improve cybersecurity.", 0, "Incorrect. CI maintains established file naming conventions.")
      ]),
    ("06 Question: ISO Schematron vs Grammar Schemas",
      "Why do mature TEI projects pair Relax NG grammars with ISO Schematron rules in their validation sweeps?",
      [
          ("Relax NG enforces structural grammar and element hierarchies, while Schematron enforces cross-element constraints and business rules (e.g., verifying that every `@wit` points to a declared `<witness>`).", 100, "Correct. Grammar schemas define valid parent-child structures, whereas Schematron uses XPath to validate relational constraints across distinct parts of the document."),
          ("Schematron is used solely to compress XML files into ZIP archives.", 0, "Incorrect. Schematron is a rule-based validation language, not a compression algorithm."),
          ("Relax NG only works on Windows, while Schematron only works on Mac.", 0, "Incorrect. Both validation standards are cross-platform and open-source."),
          ("Because university accreditation requires using at least two different software licenses.", 0, "Incorrect. Both tools are open standards used for complementary technical verification.")
      ]),
    ("07 Question: Etiquette and Rigor in Pull Request Reviews",
      "Which practice exemplifies rigorous scholarly peer review within a GitHub Pull Request?",
      [
          ("Reviewing line-by-line diffs against the primary witness facsimile, testing validation locally, and providing constructive commentary explaining why specific markup choices need revision.", 100, "Correct. Scholarly peer review combines evidentiary verification against primary sources with polite, actionable critique of code and markup."),
          ("Approving all pull requests immediately without reading the changed files.", 0, "Incorrect. Rubber-stamping PRs defeats the quality-control purpose of peer review."),
          ("Posting abusive comments criticizing the other student's personal handwriting.", 0, "Incorrect. Professional academic collaboration requires respectful, constructive discourse."),
          ("Deleting the pull request branch without providing any feedback.", 0, "Incorrect. Unilateral deletion without explanation disrupts collaborative teamwork.")
      ]),
    ("08 Question: Value of Atomic Commits",
      "Why is making small, 'atomic' commits with informative commit messages superior to committing an entire month of changes at once?",
      [
          ("Atomic commits isolate discrete logical changes, making it straightforward to review diffs, identify when regressions occurred, or revert specific defects without losing other work.", 100, "Correct. Atomic commits preserve a transparent, auditable history where individual changes can be tested, tracked, or reverted cleanly."),
          ("Because Git charges a financial fee for every commit that exceeds 100 lines of text.", 0, "Incorrect. Git is free and open-source software with no per-commit fees."),
          ("Because computers run out of RAM if a commit contains more than two files.", 0, "Incorrect. Git handles commits with thousands of files easily, but large commits hinder human review."),
          ("Because GitHub automatically rejects any commit message longer than five words.", 0, "Incorrect. GitHub supports multi-line, detailed commit descriptions.")
      ]),
    ("09 Question: Resolving Configuration Drift",
      "If a TEI file passes validation in a student's local desktop editor but fails in the GitHub Actions CI runner, what is the most likely cause?",
      [
          ("Configuration drift: the local editor is validating against a different or outdated schema version compared to the pinned canonical schema running in CI.", 100, "Correct. Local IDEs often cache older schemas or use default configurations; CI provides the authoritative, reproducible baseline environment."),
          ("GitHub's servers do not have access to electricity on weekends.", 0, "Incorrect. GitHub operates 24/7 cloud data centers."),
          ("The XML language changes its grammar rules every 24 hours at midnight.", 0, "Incorrect. XML and TEI standards remain stable across years."),
          ("The student used a Mac, and GitHub Actions only supports smartphones.", 0, "Incorrect. GitHub Actions runs on enterprise Linux, Windows, and macOS virtual machines.")
      ]),
    ("10 Question: Purpose of the Editorial Consolidation Milestone",
      "Why is a dedicated consolidation milestone strategically valuable before transitioning to final publication and web rendering?",
      [
          ("It ensures that all previous editorial layers (cataloguing, transcription, collation, and linguistic parsing) are synchronized, validated, and free of syntax defects before building downstream publication pipelines.", 100, "Correct. Consolidation stabilizes the textual corpus, ensuring that downstream transformation and publication pipelines operate on clean, standardized, bug-free data."),
          ("It allows students to permanently delete their manuscript witnesses and stop working.", 0, "Incorrect. The consolidation phase prepares materials for final publication, not abandonment."),
          ("It serves as a mandatory vacation during which all computer screens must be turned off.", 0, "Incorrect. It is an active laboratory consolidation and validation period."),
          ("It changes the course syllabus to eliminate all remaining deadlines.", 0, "Incorrect. Course schedules and publication deadlines remain in full effect.")
      ])
]

root = ET.Element("quiz")
for q_data in questions:
    name, text, answers = q_data
    q_el = ET.SubElement(root, "question", type="multichoice")
    name_el = ET.SubElement(q_el, "name")
    ET.SubElement(name_el, "text").text = name
    qtext_el = ET.SubElement(q_el, "questiontext", format="html")
    ET.SubElement(qtext_el, "text").text = f"<![CDATA[<p>{text}</p>]]>"
    ET.SubElement(q_el, "generalfeedback", format="html")
    ET.SubElement(q_el, "defaultgrade").text = "1.0000000"
    ET.SubElement(q_el, "penalty").text = "0.3333333"
    ET.SubElement(q_el, "hidden").text = "0"
    ET.SubElement(q_el, "idnumber").text = ""
    ET.SubElement(q_el, "single").text = "true"
    ET.SubElement(q_el, "shuffleanswers").text = "true"
    ET.SubElement(q_el, "answernumbering").text = "abc"
    ET.SubElement(q_el, "showstandardinstruction").text = "0"
    ET.SubElement(q_el, "correctfeedback", format="html").append(ET.Element("text"))
    q_el.find("correctfeedback/text").text = "<![CDATA[<p>Your answer is correct.</p>]]>"
    ET.SubElement(q_el, "partiallycorrectfeedback", format="html").append(ET.Element("text"))
    q_el.find("partiallycorrectfeedback/text").text = "<![CDATA[<p>Your answer is partially correct.</p>]]>"
    ET.SubElement(q_el, "incorrectfeedback", format="html").append(ET.Element("text"))
    q_el.find("incorrectfeedback/text").text = "<![CDATA[<p>Your answer is incorrect.</p>]]>"

    for ans_text, frac, fb in answers:
        ans_el = ET.SubElement(q_el, "answer", fraction=str(frac), format="html")
        ET.SubElement(ans_el, "text").text = f"<![CDATA[<p>{ans_text}</p>]]>"
        fb_el = ET.SubElement(ans_el, "feedback", format="html")
        ET.SubElement(fb_el, "text").text = f"<![CDATA[<p>{fb}</p>]]>"

raw_xml = ET.tostring(root, encoding="utf-8").decode("utf-8")
clean_xml = raw_xml.replace("&lt;![CDATA[", "<![CDATA[").replace("]]&gt;", "]]>")
header = '<?xml version="1.0" encoding="UTF-8"?>\n'
final_xml = header + clean_xml

for mod_p in [dist_mod, src_mod]:
    (mod_p / "09_Quiz.xml").write_text(final_xml, encoding="utf-8")
    print(f"Wrote quiz: {mod_p / '09_Quiz.xml'}")

print("Module 10 Phase F Assembly successfully completed!")
