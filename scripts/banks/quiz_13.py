import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

shared_dir = Path(__file__).resolve().parents[3] / "shared" / "scripts"
sys.path.insert(0, str(shared_dir))
from question_bank import Q

src_mod = Path("src/modules/Module_13_Publication")
dist_mod = Path("dist/moodle/Module_13_Publication")
src_mod.mkdir(parents=True, exist_ok=True)
dist_mod.mkdir(parents=True, exist_ok=True)

# 1. Banner Image (1200x300)
def create_banner():
    w, h = 1200, 300
    img = Image.new("RGB", (w, h), color="#1c1917")  # warm dark bronze / charcoal
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, w-10, h-10], outline="#c29b38", width=2)
    draw.rectangle([16, 16, w-16, h-16], outline="#44403c", width=1)
    draw.rectangle([20, 20, 35, h-20], fill="#f59e0b")  # radiant warm amber accent
    
    try:
        font_course = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font_course = font_title = font_sub = ImageFont.load_default()
        
    draw.text((60, 45), "RELS 398 / ENGL 398  •  DIGITAL METHODS FOR HISTORICAL DOCUMENTS", fill="#c29b38", font=font_course)
    draw.text((60, 100), "Module 13: Digital Edition Publication & Archiving", fill="#f8fafc", font=font_title)
    draw.text((60, 175), "TEI Processing Model  •  CSS Paged Media  •  FAIR Data & Zenodo Archiving", fill="#cbd5e1", font=font_sub)
    draw.line([60, 225, w-60, 225], fill="#c29b38", width=1)
    draw.text((60, 245), "StFX Department of Religious Studies  •  Computational Philology Pipeline", fill="#fde68a", font=font_sub)
    
    for p in [dist_mod / "01_Banner.png", src_mod / "01_Banner.png"]:
        img.save(p, "PNG")
        print(f"Wrote banner: {p}")

create_banner()

# 2. Learning Objectives
obj_html = """<div class="card p-3 mb-3 border-info" style="border-left: 5px solid #d97706; background-color: #fffbeb; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #b45309; margin-top: 0;">Module 13: Digital Edition Publication & Archiving — Learning Objectives</h4>
    <p>By the end of this module, students will be able to:</p>
    <ul>
        <li><strong>Formulate</strong> a comprehensive scholarly Editorial Declaration in TEI <code>&lt;editorialDecl&gt;</code>, detailing explicit policies for transcription, normalization, rendering, and named-entity markup.</li>
        <li><strong>Document and defend</strong> the textual transmission and documentary history of your primary witness within the scholarly introduction.</li>
        <li><strong>Author</strong> a TEI Processing Model ODD customization, mapping semantic markup to multi-target presentation behaviors (<code>&lt;model&gt;</code>, <code>@behaviour</code>, <code>@predicate</code>).</li>
        <li><strong>Compile</strong> multi-modal distribution packages (interactive web editions, responsive offline HTML players, and print-ready PDF/A volumes via CSS Paged Media) from a single canonical TEI XML master.</li>
        <li><strong>Implement</strong> multi-tiered open access licensing (Creative Commons and open source software licenses) and deposit archival edition portfolios according to FAIR data principles with persistent Zenodo DOIs.</li>
    </ul>
</div>"""

# 3. Readings
reading_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #c29b38; background-color: #fcfcfd; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c29b38; margin-top: 0;">Assigned Readings & Foundational Scholarship</h4>
    <p>Please study the following foundational works on digital edition architecture, transformation pipelines, and long-term preservation:</p>
    <ul>
        <li><strong>Sahle, Patrick.</strong> "What is a Digital Scholarly Edition?" In <em>Digital Scholarly Editing: Theories and Practices</em>, ed. M. J. Driscoll and E. Pierazzo, Open Book Publishers, 2016, pp. 19–39.</li>
        <li><strong>Pierazzo, Elena.</strong> <em>Digital Textual Scholarship: Theories, Methods and Common Practices</em>. Ashgate/Routledge, 2015. Focus on Chapter 4 (Modelling) and Chapter 5 (Publishing).</li>
        <li><strong>Turska, Magdalena, James Cummings, and Sebastian Rahtz.</strong> "Challenging the Myth of Presentation in 'Pure' TEI: The TEI Processing Model." <em>Journal of the Text Encoding Initiative</em>, Issue 10, 2016.</li>
    </ul>
</div>"""

# 4. Watch List
watch_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #d97706; background-color: #fffbeb; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #b45309; margin-top: 0;">Curated Media & Technical Walkthroughs</h4>
    <p>Review these video demonstrations before completing your workshop assignment:</p>
    <ul>
        <li><strong>The Final Milestone: Publishing the Digital Edition:</strong> Multi-modal transformation from TEI to Web, Print, and Mobile (24 mins).</li>
        <li><strong>The TEI Processing Model in Action:</strong> Writing declarative <code>&lt;model&gt;</code> rules and CSS Paged Media pipelines (25 mins).</li>
        <li><strong>FAIR Data, Persistent DOIs, and Zenodo Archiving:</strong> Ensuring your scholarly edition survives the next century (19 mins).</li>
    </ul>
</div>"""

# 5. Workshop
ws_desc = (src_mod / "08_Workshop_Description.html").read_text(encoding="utf-8")  # src HTML is the source of truth; edit it, not this file

ws_sub = (src_mod / "08a_Workshop_Submission_Instructions.html").read_text(encoding="utf-8")  # src HTML is the source of truth; edit it, not this file

ws_assess = (src_mod / "08b_Workshop_Assessment_Instructions.html").read_text(encoding="utf-8")  # src HTML is the source of truth; edit it, not this file

# 6. Write HTML components
for mod_p in [dist_mod, src_mod]:
    (mod_p / "02_Learning_Objectives.html").write_text(obj_html, encoding="utf-8")
    (mod_p / "05_Reading_List.html").write_text(reading_html, encoding="utf-8")
    (mod_p / "06_Watch_List.html").write_text(watch_html, encoding="utf-8")
    (mod_p / "08_Workshop_Description.html").write_text(ws_desc, encoding="utf-8")
    (mod_p / "08a_Workshop_Submission_Instructions.html").write_text(ws_sub, encoding="utf-8")
    (mod_p / "08b_Workshop_Assessment_Instructions.html").write_text(ws_assess, encoding="utf-8")
    (mod_p / "09_Quiz_Description.html").write_text("<p>Comprehensive weekly knowledge check covering digital edition publication, TEI Processing Model ODD, CSS Paged Media, FAIR archiving, and multi-tiered open licensing.</p>", encoding="utf-8")

print("Wrote HTML and Banner files.")

# 7. Build Weekly Quiz (10 Questions)
questions = [
    ("01 Question: Sahle's Definition of a Digital Scholarly Edition",
      "According to Patrick Sahle's foundational definition, what essential criterion distinguishes a true Digital Scholarly Edition (DSE) from a digitized print book?",
      [
          ("A DSE is guided by a digital paradigm: it cannot be rendered in physical print without a significant loss of content, dynamic functionality, or analytical interconnectivity.", 100, "Correct. Sahle defines a DSE not by its digital medium of distribution (like a simple PDF), but by its adherence to a digital rationale that cannot be transposed to paper without catastrophic information loss."),
          ("A DSE is any book that is sold on Amazon Kindle.", 0, "Incorrect. Commercial ebooks are digitized print models, not scholarly critical editions."),
          ("A DSE is a text typed entirely by an artificial intelligence model without human oversight.", 0, "Incorrect. Scholarly digital editing demands expert human editorial rigor."),
          ("A DSE must contain animated dancing cartoon characters on every page.", 0, "Incorrect. Scholarly digital editions are rigorous academic research tools.")
      ]),
    ("02 Question: Single-Witness Documentary Fidelity",
      "In single-witness documentary editing, how does an editor treat historical spelling quirks, physical cancellations, and scribal additions?",
      [
          ("The editor records them diplomatically with physical fidelity, provides normalized views through markup, and explains their significance in standoff commentary rather than inventing composite readings.", 100, "Correct. Documentary editing respects the unique historical artifact, recording authentic material strokes rather than smoothing text into an idealized modern composite."),
          ("The editor silently deletes all strange spellings and rewrites the text in modern slang.", 0, "Incorrect. Documentary editing preserves historical voices rather than erasing them."),
          ("The editor burns the original manuscript in an incinerator if it contains spelling errors.", 0, "Incorrect. Historical artifacts are conserved and preserved with scholarly care."),
          ("The editor forces the text to match a modern printed textbook.", 0, "Incorrect. The edition reflects the surviving primary witness, not an anachronistic reprint.")
      ]),
    ("03 Question: Function of TEI editorialDecl",
      "Within a TEI header, what is the specific role of the `<editorialDecl>` element in `<encodingDesc>`?",
      [
          ("It provides an explicit, machine-readable declaration of all editorial principles applied, including policies on transcription, regularization, normalization, quotation, and apparatus selection.", 100, "Correct. The <editorialDecl> makes editorial practices fully transparent, documenting whether abbreviations were expanded, how spelling was regularized, and how variants were adjudicated."),
          ("It records the banking account details where donations should be sent.", 0, "Incorrect. That belongs in financial records, not scholarly TEI metadata."),
          ("It lists the names of all students who failed the course midterm.", 0, "Incorrect. Academic grades are private educational records (PII) and never appear in public TEI headers."),
          ("It sets the computer monitor brightness to maximum.", 0, "Incorrect. Display hardware settings are not controlled by XML document metadata.")
      ]),
    ("04 Question: Architecture of the TEI Processing Model",
      "How does the TEI Processing Model (encoded within an ODD customization) separate scholarly semantic markup from presentation styling?",
      [
          ("It expresses transformation rules declaratively using `<model>` elements with `@behaviour` (e.g. `paragraph`, `heading`, `note`) and `@predicate` XPath conditions, leaving media-specific CSS/XSLT generation to the publishing engine.", 100, "Correct. The Processing Model provides an abstract, declarative layer inside the ODD, defining how elements behave without hard-coding specific HTML tags or print formatting."),
          ("It forces all web browsers to use the comic sans font.", 0, "Incorrect. The Processing Model allows customizable, professional typographic styling."),
          ("It converts all XML tags into raw binary numbers (0s and 1s).", 0, "Incorrect. Processing model rules compile into human-readable HTML, XQuery, or XSLT."),
          ("It automatically deletes all images from the final edition.", 0, "Incorrect. The Processing Model supports complex multimodal graphic rendering behaviors.")
      ]),
    ("05 Question: CSS Paged Media for Print-Ready PDF Generation",
      "How does the CSS Paged Media standard (implemented by tools like WeasyPrint or paged.js) generate professional print-ready PDFs directly from HTML/XML?",
      [
          ("It extends standard CSS with page-specific rules (`@page`, `@top-left`, `@bottom-right`), margins, running headers, footnotes, and page break controls to produce publication-grade layout.", 100, "Correct. CSS Paged Media bridges web technologies and high-end print publishing, enabling automated generation of book-quality PDFs from web markup."),
          ("It takes a digital photo of the computer screen and prints it.", 0, "Incorrect. Paged Media generates vector typography and structured PDF streams, not raster screenshots."),
          ("It requires hand-carving wooden printing blocks for every letter in the alphabet.", 0, "Incorrect. That describes 15th-century moveable type, not modern CSS Paged Media."),
          ("It limits every document to a maximum length of exactly one page.", 0, "Incorrect. CSS Paged Media effortlessly formats multi-volume book publications.")
      ]),
    ("06 Question: Multi-Tiered Open Access Licensing Architecture",
      "Why do modern digital critical editions adopt a 'multi-tiered' licensing structure rather than a single monolithic license?",
      [
          ("Because different components require different permissions: editorial commentary is published under CC BY 4.0, structured metadata under CC0 (public domain) for maximum linked-data interoperability, and custom software scripts under open-source licenses (MIT/GPL).", 100, "Correct. Distinct intellectual products (interpretive prose, factual data triples, executable code) require dedicated licensing legal frameworks to balance scholarly attribution with open reusability."),
          ("To confuse readers so that they accidentally pay a secret subscription fee.", 0, "Incorrect. Multi-tiered licensing promotes open science and transparent reuse rights."),
          ("Because Canadian copyright law mandates having at least seven different licenses per book.", 0, "Incorrect. Multi-tiered licensing is an international digital humanities best practice, not a statutory mandate."),
          ("To prevent anyone from ever reading the edition outside the university library.", 0, "Incorrect. Open licenses guarantee unrestricted global reading access.")
      ]),
    ("07 Question: FAIR Data Principles in Digital Philology",
      "What do the FAIR data principles require of a published digital critical edition?",
      [
          ("That the edition and its underlying data be Findable (persistent DOI), Accessible (open protocols), Interoperable (standard TEI XML/RDF), and Reusable (clear open licensing and detailed documentation).", 100, "Correct. FAIR principles ensure that digital scholarly research remains discoverable and reusable by future generations and automated computational agents."),
          ("Fast, Affordable, Interesting, and Relatable.", 0, "Incorrect. FAIR stands for Findable, Accessible, Interoperable, and Reusable in research data management."),
          ("Federal, Academic, Institutional, and Regional.", 0, "Incorrect. That is not the definition of the FAIR acronym."),
          ("Free, Anonymous, Illegal, and Redacted.", 0, "Incorrect. Academic editions are open, attributed, and fully transparent.")
      ]),
    ("08 Question: Persistent Archiving with Zenodo DOIs",
      "Why is depositing a release archive on Zenodo considered superior to simply hosting files on a personal website or GitHub repository alone?",
      [
          ("Zenodo assigns a persistent Digital Object Identifier (DOI) and guarantees long-term archival preservation backed by CERN's infrastructure, ensuring links never break when URLs change.", 100, "Correct. Personal websites succumb to link rot and GitHub repositories can be deleted; Zenodo guarantees multi-decade persistent archival preservation and permanent citable DOIs."),
          ("Because Zenodo automatically translates the entire edition into thirty languages.", 0, "Incorrect. Zenodo is an archival repository, not a translation engine."),
          ("Because hosting files on Zenodo is legally required before submitting student coursework.", 0, "Incorrect. Zenodo is a repository for open research dissemination."),
          ("Because GitHub charges $1000 per month for every repository that stays online for more than a year.", 0, "Incorrect. GitHub public repositories are completely free of charge.")
      ]),
    ("09 Question: The 12-Gate Quality Assurance Checklist",
      "What is the operational function of an explicit multi-gate quality assurance checklist prior to publishing a digital critical edition?",
      [
          ("It provides an uncompromising deterministic verification gate (schema validation, pointer integrity, font embedding, license declaration) that halts release if any structural defect is detected.", 100, "Correct. Formal QA gates guarantee that digital publications meet high standards of syntactic validity, visual presentation, and long-term reproducibility."),
          ("It serves as a polite suggestion that editors can ignore whenever they are in a hurry.", 0, "Incorrect. Quality gates are strict prerequisites for release."),
          ("It randomly deletes 10% of the files to test the resilience of the backup system.", 0, "Incorrect. QA verification audits and validates data without destructive sabotage."),
          ("It prevents students from graduating until they pass an oral examination in Latin.", 0, "Incorrect. The checklist validates digital edition files, not student degree conferral.")
      ]),
    ("10 Question: Enduring Scholarly Legacy of Digital Editions",
      "What represents the ultimate scholarly achievement of authoring a standardized, TEI-conformant digital critical edition?",
      [
          ("Creating an authoritative, verifiable, and computationally actionable edition that preserves endangered cultural heritage and empowers future generations of scholars, students, and algorithms to explore historical texts.", 100, "Correct. Digital scholarly editions unite rigorous traditional philology with modern computational interoperability, establishing permanent intellectual monuments for humanity's shared textual heritage."),
          ("Writing a single viral social media post that disappears after 24 hours.", 0, "Incorrect. Digital critical editions are durable scholarly contributions designed for multi-decade longevity."),
          ("Getting a computer program to run without knowing what the text means.", 0, "Incorrect. Digital humanities balances technical computation with deep philological understanding."),
          ("Replacing all human historians with fully autonomous automated algorithms.", 0, "Incorrect. Digital methods augment and empower humanistic inquiry rather than replacing human scholars.")
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

print("Module 13 Phase F Assembly successfully completed!")
