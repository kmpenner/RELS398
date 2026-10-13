import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

shared_dir = Path(__file__).resolve().parents[3] / "shared" / "scripts"
sys.path.insert(0, str(shared_dir))
from question_bank import Q

src_mod = Path("src/modules/Module_15_Apparatus")
dist_mod = Path("dist/moodle/Module_15_Apparatus")
src_mod.mkdir(parents=True, exist_ok=True)
dist_mod.mkdir(parents=True, exist_ok=True)

# 1. Banner Image (1200x300)
def create_banner():
    w, h = 1200, 300
    img = Image.new("RGB", (w, h), color="#292524")  # dark walnut / stone
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, w-10, h-10], outline="#c29b38", width=2)
    draw.rectangle([16, 16, w-16, h-16], outline="#44403c", width=1)
    draw.rectangle([20, 20, 35, h-20], fill="#b91c1c")  # Venetian red accent
    
    try:
        font_course = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font_course = font_title = font_sub = ImageFont.load_default()
        
    draw.text((60, 45), "RELS 398 / ENGL 398  •  DIGITAL METHODS FOR HISTORICAL DOCUMENTS", fill="#c29b38", font=font_course)
    draw.text((60, 100), "Module 15: Digital Critical Apparatus", fill="#f8fafc", font=font_title)
    draw.text((60, 175), "Positive & Negative Apparatus  •  TEI Parallel Segmentation  •  Toolbox Validation", fill="#cbd5e1", font=font_sub)
    draw.line([60, 225, w-60, 225], fill="#c29b38", width=1)
    draw.text((60, 245), "StFX Department of Religious Studies  •  Computational Philology Pipeline", fill="#a8a29e", font=font_sub)
    
    for p in [dist_mod / "01_Banner.png", src_mod / "01_Banner.png"]:
        img.save(p, "PNG")
        print(f"Wrote banner: {p}")

create_banner()

# 2. Learning Objectives
obj_html = """<div class="card p-3 mb-3 border-info" style="border-left: 5px solid #b91c1c; background-color: #fef2f2; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #991b1b; margin-top: 0;">Module 15: Digital Critical Apparatus — Learning Objectives</h4>
    <p>By the end of this module, students will be able to:</p>
    <ul>
        <li><strong>Differentiate</strong> conceptually between a positive apparatus (which explicitly enumerates witnesses supporting the lemma) and a negative apparatus (which lists only dissenting witnesses).</li>
        <li><strong>Encode</strong> complex multi-witness textual variations using TEI P5 <code>&lt;app&gt;</code>, <code>&lt;lem&gt;</code>, and <code>&lt;rdg&gt;</code> elements with standard <code>@wit</code> pointers.</li>
        <li><strong>Transform</strong> automated CollateX alignment data into well-formed TEI parallel segmentation XML structures.</li>
        <li><strong>Validate and visualize</strong> critical editions using the TEI Critical Apparatus Toolbox and schema linters.</li>
        <li><strong>Detect and correct</strong> common AI apparatus hallucinations, including non-existent manuscript sigla and corrupted lemma boundary tags.</li>
    </ul>
</div>"""

# 3. Readings
reading_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #c29b38; background-color: #fcfcfd; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c29b38; margin-top: 0;">Assigned Readings & Foundational Scholarship</h4>
    <p>Please study the following resources on critical apparatus architecture and digital textual editing:</p>
    <ul>
        <li><strong>TEI Consortium.</strong> "Chapter 12: Critical Apparatus." <em>TEI P5: Guidelines for Electronic Text Interchange</em>, Version 4.8.0, 2024.</li>
        <li><strong>Burnard, Lou.</strong> <em>What is the Text Encoding Initiative? How to Add Intelligent Value to Your Digital Texts</em>. OpenEdition Press, 2014.</li>
        <li><strong>Burghart, Marjorie.</strong> "The TEI Critical Apparatus Toolbox: Empowering Textual Scholars through Automated Processing." <em>Journal of the Text Encoding Initiative</em>, Issue 10, 2016.</li>
    </ul>
</div>"""

# 4. Watch List
watch_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #b91c1c; background-color: #fef2f2; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #991b1b; margin-top: 0;">Curated Media & Technical Walkthroughs</h4>
    <p>Review these video demonstrations before completing your workshop assignment:</p>
    <ul>
        <li><strong>The Architecture of the Critical Apparatus:</strong> From traditional print footnotes to dynamic digital apparatuses (20 mins).</li>
        <li><strong>Building TEI Parallel Segmentation:</strong> Hand-authoring <code>&lt;app&gt;</code>, <code>&lt;lem&gt;</code>, and <code>&lt;rdg&gt;</code> in VS Code (25 mins).</li>
        <li><strong>Testing with the TEI Critical Apparatus Toolbox:</strong> Visualizing witness variation and verifying sigla consistency (18 mins).</li>
    </ul>
</div>"""

# 5. Workshop
ws_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #b91c1c; background-color: #fef2f2; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #991b1b; margin-top: 0;">Workshop: Hand-Authoring and Generating a TEI Critical Apparatus</h4>
    <p><strong>Overview:</strong> In this workshop, you will encode a 25-line critical edition of your primary witness collated against two additional witnesses. You will author positive apparatus entries by hand, verify that every witness sigil resolves to a <code>&lt;listWit&gt;</code> entry in your TEI header, and visualize your edition in the TEI Critical Apparatus Toolbox.</p>
    <p><strong>Deadlines:</strong> Comparison Post due Friday by 11:00 PM; Peer Reviews due Monday by 11:00 PM.</p>
</div>"""

ws_sub = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Submission Instructions</h4>
    <ol>
        <li>Construct a TEI XML document containing your base text wrapped in <code>&lt;body&gt;</code>, with all collated variants encoded inside <code>&lt;app&gt;</code> elements.</li>
        <li>Ensure your <code>&lt;teiHeader&gt;</code> contains a populated <code>&lt;sourceDesc&gt;&lt;listWit&gt;</code> explicitly declaring each witness ID (e.g. <code>xml:id="witA"</code>).</li>
        <li>Encode at least 5 variant locations using a positive apparatus format (declaring both <code>&lt;lem wit="..."&gt;</code> and <code>&lt;rdg wit="..."&gt;</code>).</li>
        <li>Run your file through the TEI Critical Apparatus Toolbox or an XML validator in VS Code.</li>
        <li>Submit your completed TEI XML file and a <strong>300–500 word critical reflection</strong> explaining why digital parallel segmentation solves the space-saving ambiguities inherent in traditional print apparatus criticus.</li>
    </ol>
</div>"""

ws_assess = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Peer Assessment Rubric</h4>
    <ul>
        <li><strong>Apparatus XML Well-Formedness & Validity (4 pts):</strong> The <code>&lt;app&gt;</code>, <code>&lt;lem&gt;</code>, and <code>&lt;rdg&gt;</code> elements are syntactically well-formed, correctly nested, and validate against the TEI schema.</li>
        <li><strong>Sigla Resolution & Header Integrity (3 pts):</strong> Every <code>@wit</code> pointer (e.g. <code>#witA</code>) exactly matches an <code>xml:id</code> declared in the <code>&lt;listWit&gt;</code> container.</li>
        <li><strong>Critical Editorial Rationale (3 pts):</strong> The reflection articulates a sophisticated understanding of positive vs. negative apparatus conventions and the epistemic benefits of digital text representation.</li>
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
    (mod_p / "09_Quiz_Description.html").write_text("<p>Comprehensive weekly knowledge check covering positive and negative apparatus conventions, TEI parallel segmentation, witness pointer integrity, and automated validation.</p>", encoding="utf-8")

print("Wrote HTML and Banner files.")

# 7. Build Weekly Quiz (10 Questions)
questions = [
    ("01 Question: Positive vs Negative Apparatus Structure",
      "What distinguishes a 'positive apparatus' from a 'negative apparatus' in classical textual criticism?",
      [
          ("A positive apparatus explicitly cites the witnesses that support the lemma as well as the variant readings, whereas a negative apparatus lists only the dissenting witnesses, assuming all others support the lemma.", 100, "Correct. A positive apparatus explicitly enumerates witnesses for the lemma, providing total clarity at the expense of typographical space, whereas a negative apparatus only lists variants."),
          ("A positive apparatus only records pleasant or inspiring passages, whereas a negative apparatus records tragic events.", 0, "Incorrect. The terms refer to explicit versus implicit witness citation, not emotional or literary tone."),
          ("A positive apparatus is used exclusively for printed books, whereas a negative apparatus is used for digital websites.", 0, "Incorrect. Both conventions originated in print textual editing and are modeled in digital TEI editions."),
          ("A positive apparatus requires approval from an ecclesiastical council, whereas a negative apparatus is secular.", 0, "Incorrect. The distinction is purely structural and philological.")
      ]),
    ("02 Question: TEI Apparatus Element Hierarchy",
      "In the TEI parallel segmentation method, what is the required structural hierarchy for encoding a textual variant?",
      [
          ("The <app> element contains a single optional <lem> (lemma) followed by one or more <rdg> (reading) elements.", 100, "Correct. In TEI P5, <app> groups the variation point, enclosing <lem> for the preferred reading and <rdg> for each witness variation."),
          ("The <lem> element encloses several child <app> elements, each containing a <choice>.", 0, "Incorrect. <app> is the parent container, not <lem>."),
          ("<rdg> encloses <lem>, which in turn encloses <sourceDesc>.", 0, "Incorrect. <sourceDesc> belongs in the teiHeader, and <rdg> cannot enclose <lem>."),
          ("All variants must be written inside an HTML <footnote> tag without XML elements.", 0, "Incorrect. TEI uses structured semantic tags (<app>, <lem>, <rdg>) rather than presentation footnotes.")
      ]),
    ("03 Question: Witness Sigla Pointer Integrity",
      "In a TEI critical edition, how should the `@wit` attribute on a `<rdg>` element reference a specific manuscript witness?",
      [
          ("With a URI hash pointer (e.g. `wit=\"#ms-A\"`) corresponding to an `xml:id=\"ms-A\"` declared on a `<witness>` element in the header's `<listWit>`.", 100, "Correct. In TEI, @wit uses IDREF URI syntax (prefixed with `#`) resolving directly to a unique xml:id defined in <listWit>."),
          ("With a free-text sentence describing the library shelf in plain prose.", 0, "Incorrect. Structured attributes require formal ID pointers for automated processing."),
          ("By writing the full binary file path to the witness on the editor's local Mac hard drive.", 0, "Incorrect. Pointers must be portable relative URIs, not machine-specific local paths."),
          ("By omitting the attribute entirely and letting the web browser guess the manuscript.", 0, "Incorrect. Omitting @wit makes the apparatus anonymous and untraceable.")
      ]),
    ("04 Question: Three TEI Apparatus Attachment Methods",
      "Which of the following represents the three recognized TEI methods for linking a critical apparatus to a text?",
      [
          ("Parallel segmentation, location-referenced method, and double-endpoint attachment.", 100, "Correct. TEI P5 Chapter 12 officially defines these three methods for apparatus encoding."),
          ("Git commit, Git push, and Git pull.", 0, "Incorrect. These are version control operations, not TEI apparatus encoding methods."),
          ("Bitmap, vector, and JPEG compression.", 0, "Incorrect. These are digital image formats."),
          ("HTML, CSS, and JavaScript.", 0, "Incorrect. These are web development technologies.")
      ]),
    ("05 Question: Purpose of the TEI Critical Apparatus Toolbox",
      "What is the primary function of the TEI Critical Apparatus Toolbox developed by Marjorie Burghart?",
      [
          ("It processes TEI XML files containing critical apparatus markup to visualize witness comparisons, generate apparatus statistics, and check sigla consistency.", 100, "Correct. The Toolbox provides specialized online tools to display parallel segmentation, inspect variant distribution, and validate witness lists."),
          ("It automatically translates ancient Greek poetry into modern Canadian English.", 0, "Incorrect. The Toolbox analyzes markup structure and variant distribution, not machine translation."),
          ("It scans physical manuscripts using a computer webcam.", 0, "Incorrect. It is a web-based analytical tool for processing encoded TEI XML documents."),
          ("It acts as an antivirus firewall for Moodle servers.", 0, "Incorrect. It is an editorial digital humanities tool, not network security software.")
      ]),
    ("06 Question: Transforming CollateX Data into TEI Apparatus",
      "When transforming a CollateX alignment matrix into a TEI `<app>` entry, how is a cell where a witness lacks text represented?",
      [
          ("As an empty `<rdg wit=\"#witX\"/>` element or an `<rdg wit=\"#witX\"><gap reason=\"omitted\"/></rdg>` element representing an omission.", 100, "Correct. An alignment gap in CollateX indicates that the witness omits the token, encoded in TEI as an empty <rdg> or explicit omission marker."),
          ("By deleting the witness entirely from the `<teiHeader>`.", 0, "Incorrect. Witnesses that omit a phrase remain part of the edition and must be accounted for."),
          ("By substituting text from an entirely different poem.", 0, "Incorrect. Splicing unrelated text violates textual scholarship."),
          ("By halting the transformation script and throwing a fatal error.", 0, "Incorrect. Omissions are standard variant phenomena handled routinely by alignment scripts.")
      ]),
    ("07 Question: Complex Variants with Corrections in Witnesses",
      "How can a TEI apparatus entry represent that a variant reading in Witness B was added by a second scribal hand (`#hand2`) after an earlier reading was erased?",
      [
          ("<rdg wit=\"#witB\"><subst><del>original_text</del><add hand=\"#hand2\">corrected_text</add></subst></rdg>", 100, "Correct. TEI modularity allows primary-source alteration elements (<subst>, <del>, <add>) to be nested directly inside apparatus <rdg> containers."),
          ("<app><error>correction_occurred</error></app>", 0, "Incorrect. <error> is not a valid TEI apparatus element."),
          ("By writing a footnote in Microsoft Word and pasting a screenshot into the XML file.", 0, "Incorrect. TEI editions use semantic XML markup, not raster screenshot images."),
          ("By creating two completely separate TEI documents and never linking them.", 0, "Incorrect. Apparatus markup explicitly unifies variant readings in a single comparative structure.")
      ]),
    ("08 Question: AI Hallucinations in Critical Apparatus Drafting",
      "When an LLM is asked to draft a TEI critical apparatus from collated tables, what is a frequent hallucination defect?",
      [
          ("Inventing non-existent manuscript sigla (phantom witnesses) or silently dropping dissenting witnesses from the `<rdg>` list.", 100, "Correct. Generative models struggle with rigid accounting across tables, often dropping rare witnesses or fabricating plausible-looking sigla not in the source."),
          ("Formatting the XML using valid hexadecimal color codes.", 0, "Incorrect. Color formatting is not a typical apparatus hallucination."),
          ("Refusing to output anything unless paid in cryptocurrency.", 0, "Incorrect. LLMs do not solicit cryptocurrency in code generation prompts."),
          ("Encrypting the witness names using RSA-2048 encryption.", 0, "Incorrect. Models produce text, not cryptographic ciphertexts, unless explicitly asked.")
      ]),
    ("09 Question: Advantages of Digital Parallel Segmentation over Print",
      "Why is the digital parallel segmentation method considered methodologically superior to traditional printed apparatus footnotes?",
      [
          ("It embeds variants directly at their exact point of occurrence in the text hierarchy, eliminating ambiguous footnote reference numbers and arbitrary print space constraints.", 100, "Correct. Parallel segmentation keeps the text and variants tightly coupled in machine-actionable XML, enabling dynamic multi-view rendering without print space compromises."),
          ("Because digital editions are completely free of all copyright restrictions worldwide.", 0, "Incorrect. Digital editions are subject to licensing and copyright laws like any scholarly publication."),
          ("Because digital files can never be deleted from a computer once written.", 0, "Incorrect. Digital files require active preservation and backups."),
          ("Because printed books are no longer permitted in university libraries.", 0, "Incorrect. Print books remain vital scholarly resources.")
      ]),
    ("10 Question: Quality Assurance Checklist for Apparatus XML",
      "Before finalizing a digital critical apparatus for publication, what verification step is essential?",
      [
          ("Validating the XML against the TEI schema and verifying that 100% of the `@wit` pointers resolve to declared witnesses in `<listWit>`.", 100, "Correct. Schema validation guarantees syntactic well-formedness, while pointer integrity auditing ensures no dangling or invalid witness references exist."),
          ("Confirming that every manuscript in the world agrees with the editor's personal interpretation.", 0, "Incorrect. Witnesses naturally disagree; the goal is accurate documentation, not forced unanimity."),
          ("Deleting the `<teiHeader>` to reduce file download size for mobile users.", 0, "Incorrect. The teiHeader contains vital metadata and witness declarations that cannot be removed."),
          ("Replacing all polytonic Greek characters with Latin transliterations.", 0, "Incorrect. Scholarly digital editions preserve authentic original scripts using Unicode.")
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

print("Module 15 Phase F Assembly successfully completed!")
