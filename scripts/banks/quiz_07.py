#!/usr/bin/env python3
"""Module 07: Publication I (Rendering) Phase F Assembly & Weekly Quiz Generator.

Generates:
1. 01_Banner.png (1200x300 branded banner)
2. 05_Reading_List.html
3. 06_Watch_List.html
4. 09_Quiz_Description.html
5. 09_Quiz.xml (10-question formative assessment quiz with rich diagnostic feedback)
"""
import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
src_mod = ROOT / "src/modules/Module_07_Rendering"
dist_mod = ROOT / "dist/moodle/Module_07_Rendering"
src_mod.mkdir(parents=True, exist_ok=True)
dist_mod.mkdir(parents=True, exist_ok=True)

# 1. Banner Image (1200x300)
def create_banner():
    w, h = 1200, 300
    img = Image.new("RGB", (w, h), color="#0c192c")  # deep indigo / slate
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, w-10, h-10], outline="#c29b38", width=2)
    draw.rectangle([16, 16, w-16, h-16], outline="#1e293b", width=1)
    draw.rectangle([20, 20, 35, h-20], fill="#f59e0b")  # warm amber/orange accent
    
    try:
        font_course = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font_course = font_title = font_sub = ImageFont.load_default()
        
    draw.text((60, 45), "RELS 398 / ENGL 398  •  DIGITAL METHODS FOR HISTORICAL DOCUMENTS", fill="#c29b38", font=font_course)
    draw.text((60, 100), "Module 07: Publication I (Rendering)", fill="#f8fafc", font=font_title)
    draw.text((60, 175), "Display Decisions  •  HTML & CSS Ground Truth  •  XSLT & CETEIcean  •  AI Audit", fill="#94a3b8", font=font_sub)
    draw.line([60, 225, w-60, 225], fill="#c29b38", width=1)
    draw.text((60, 245), "StFX Department of Religious Studies  •  Computational Philology Pipeline", fill="#64748b", font=font_sub)
    
    for p in [dist_mod / "01_Banner.png", src_mod / "01_Banner.png"]:
        img.save(p, "PNG")
        print(f"Wrote banner: {p}")

create_banner()

# 2. Readings
reading_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #c29b38; background-color: #fcfcfd; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c29b38; margin-top: 0;">Assigned Readings & Foundational Scholarship</h4>
    <p>Please study the following scholarship on digital edition rendering and separation of data from presentation:</p>
    <ul>
        <li><strong>Huskey, Samuel J.</strong> "Developing a New Integrated Editing Platform for Source Documents in Classics." <em>Digital Humanities Quarterly</em>, 2024. Focus on § 3 (Treating layout and visualization as a separate scholarly concern).</li>
        <li><strong>Pierazzo, Elena.</strong> "Digital Scholarly Editing in Practice: Making the Oxford University Voltaire." <em>Digital Scholarly Editing: Theories and Practices</em>, Open Book Publishers, 2016, pp. 47–70. (Generating diplomatic and reading views from one XML master).</li>
        <li><strong>TEI Consortium.</strong> "Chapter 11: Representation of Primary Sources." <em>TEI P5: Guidelines for Electronic Text Encoding and Interchange</em>, Version 4.8.0, 2024. § 11.3 (Display decisions, milestone tags, and parallel segmentation).</li>
    </ul>
</div>"""

# 3. Watch List
watch_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #0284c7; background-color: #f0f9ff; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #0369a1; margin-top: 0;">Curated Media & Technical Walkthroughs</h4>
    <p>Review these video demonstrations on stylesheet transformation and in-browser rendering:</p>
    <ul>
        <li><strong>From Angle Brackets to Living Pages:</strong> Decoupling scholarly evidence from web typography and responsive layout (16 mins).</li>
        <li><strong>XSLT 1.0 & CETEIcean in Practice:</strong> Transforming TEI elements into modern browser DOM trees using template matching and custom elements (21 mins).</li>
        <li><strong>Auditing AI-Generated Stylesheets:</strong> Spotting subtle whitespace collapses, first-child selector assumptions, and silent element drops with automated Python diffs (19 mins).</li>
    </ul>
</div>"""

# 4. Write HTML components
for mod_p in [dist_mod, src_mod]:
    (mod_p / "05_Reading_List.html").write_text(reading_html, encoding="utf-8")
    (mod_p / "06_Watch_List.html").write_text(watch_html, encoding="utf-8")
    (mod_p / "09_Quiz_Description.html").write_text("<p>Comprehensive weekly knowledge check covering display decisions, HTML/CSS ground truth, XSLT and CETEIcean transformation, and AI stylesheet auditing.</p>", encoding="utf-8")

print("Wrote HTML and Banner files.")

# 5. Build Weekly Quiz (10 Questions)
questions = [
    ("01 Question: Content vs Presentation Separation",
      "Why do scholarly digital editions strictly separate encoded textual content from presentation stylesheets?",
      [
          ("Keeping the look in display rules means editors can update, redesign, or reformat presentation without touching or risking the primary textual evidence.", 100, "Correct. Separating content from presentation ensures that evidence remains fixed and reproducible while display stylesheets can evolve independently."),
          ("Web browsers refuse to parse XML files that contain any visual styling instructions.", 0, "Incorrect. Browsers can apply styling via CSS or XSLT, but mixing display directives with semantic encoding violates digital humanities standards."),
          ("TEI schemas automatically delete any XML file that specifies font sizes or margin widths.", 0, "Incorrect. Schemas validate element containment and attribute constraints; they do not delete files."),
          ("Print publishers require all digital files to be monochrome before peer review.", 0, "Incorrect. Digital editions support multi-modal publication across color web screens and print formats.")
      ]),
    ("02 Question: One File Many Views",
      "How does a single normalized TEI XML document support both a diplomatic view and a modernized reading view?",
      [
          ("The stylesheet selectively activates different child elements within TEI &lt;choice&gt; containers (displaying &lt;orig&gt; for diplomatic views and &lt;reg&gt; for reading views).", 100, "Correct. The &lt;choice&gt; container encapsulates alternative layers, allowing stylesheets to toggle between verbatim witness evidence and normalized reading text."),
          ("The editor must maintain two separate XML files in different Git repositories.", 0, "Incorrect. Maintaining duplicate files causes version drift; a single TEI file holds both layers simultaneously."),
          ("A machine learning model rewrites the text dynamically on the fly each time a student visits the page.", 0, "Incorrect. Scholarly editions rely on deterministic, editorially verified markup rather than live non-deterministic AI regeneration."),
          ("Diplomatic views require specialized hardware monitors that cannot display modern fonts.", 0, "Incorrect. Both views are rendered in standard web browsers using standard CSS and web typography.")
      ]),
    ("03 Question: Milestone Line Breaks and Word Boundaries",
      "Why must stylesheet rules for milestone line breaks (&lt;lb/&gt;) be carefully audited for whitespace handling?",
      [
          ("A naive line-break rule that outputs a line break without a trailing or leading space will glue the last word of a line to the first word of the next line, unless &lt;lb break=\"no\"/&gt; is specified.", 100, "Correct. Milestone line breaks replace physical line breaks; omitting spaces on standard breaks merges adjacent words into unreadable strings."),
          ("Browsers automatically crash when encountering self-closing XML milestone elements.", 0, "Incorrect. Modern XML parsers and custom element processors handle self-closing tags without issue."),
          ("Line break elements permanently delete all vowels from preceding words during transformation.", 0, "Incorrect. Line breaks mark physical layout transitions; they do not alter lexical tokens."),
          ("HTML does not support line breaks in paragraphs.", 0, "Incorrect. HTML supports &lt;br&gt; and CSS block line-breaking.")
      ]),
    ("04 Question: Browser Treatment of Custom TEI Elements",
      "When a modern browser renders custom elements generated by CETEIcean (e.g., &lt;tei-p&gt; or &lt;tei-div&gt;), what is its default layout behavior before custom CSS is applied?",
      [
          ("Browsers treat unknown custom elements as inline elements (display: inline), requiring explicit CSS rules (display: block) to establish structural paragraph blocks.", 100, "Correct. The HTML specification treats unregistered custom elements as inline by default; CSS must explicitly declare structural blocks."),
          ("Browsers immediately hide all custom elements with display: none.", 0, "Incorrect. Browsers render unknown elements inline rather than hiding them."),
          ("Browsers automatically format &lt;tei-p&gt; with standard 16px paragraph margins and line breaks.", 0, "Incorrect. HTML user-agent stylesheets only style native HTML elements (like &lt;p&gt;), not custom custom elements."),
          ("Browsers throw a fatal security exception and halt JavaScript execution.", 0, "Incorrect. Custom elements are fully valid in HTML5 and DOM specifications.")
      ]),
    ("05 Question: XSLT Template Transformation Engine",
      "In an XSLT stylesheet, what is the primary function of the &lt;xsl:apply-templates/&gt; instruction inside a matched template?",
      [
          ("It instructs the transformation processor to recursively process the child nodes of the current element using the stylesheet's matching rules.", 100, "Correct. &lt;xsl:apply-templates/&gt; drives recursive descent through the XML tree, applying the appropriate template rules to child elements."),
          ("It compiles the XML file into an executable binary program.", 0, "Incorrect. XSLT is a declarative tree-transformation language, not a binary compiler."),
          ("It sends an automated email notification to the repository administrator.", 0, "Incorrect. XSLT templates process XML node hierarchies."),
          ("It permanently overwrites the input XML source file with raw HTML.", 0, "Incorrect. XSLT takes an input tree and produces an output tree, leaving the source file untouched.")
      ]),
    ("06 Question: CETEIcean In-Browser Architecture",
      "How does the CETEIcean JavaScript library render TEI documents without requiring server-side XSLT transformation?",
      [
          ("It loads TEI XML directly into the browser DOM, prefixing elements with 'tei-' to create valid HTML5 custom elements that are styled directly with standard CSS.", 100, "Correct. CETEIcean imports TEI XML into the browser DOM as custom elements, allowing direct CSS styling and client-side behavioral attachment."),
          ("It converts all XML text into raster PNG screenshots before display.", 0, "Incorrect. CETEIcean produces live, accessible, searchable DOM text elements."),
          ("It runs a full headless Ubuntu Linux virtual machine inside the web browser.", 0, "Incorrect. CETEIcean is a lightweight JavaScript library that manipulates DOM elements directly."),
          ("It translates the TEI file into Markdown and parses it with Python.", 0, "Incorrect. CETEIcean operates entirely in browser-side JavaScript without Python runtime dependencies.")
      ]),
    ("07 Question: Local HTTP Server Requirement for CETEIcean",
      "Why must a local CETEIcean HTML file be opened through a web server (such as Python's http.server) rather than by double-clicking the file (file:///)?",
      [
          ("Browser security models block JavaScript fetch() requests to local file:/// URLs under the Same-Origin Policy (CORS), preventing the script from reading the XML file.", 100, "Correct. Browser security restrictions block client-side fetch requests to local file system paths, requiring an HTTP server origin."),
          ("Custom CSS files can only be downloaded from remote cloud servers.", 0, "Incorrect. CSS can be served locally; the restriction specifically applies to JavaScript fetch() on file:/// URLs."),
          ("Python http.server is required to compile XML into C++ before the browser can understand it.", 0, "Incorrect. Browsers parse XML natively; the server simply fulfills HTTP GET requests."),
          ("Local files are encrypted by the operating system until an HTTP handshake occurs.", 0, "Incorrect. Local file permissions are governed by the OS, but browser security sandbox rules enforce CORS restrictions on fetch.")
      ]),
    ("08 Question: First-Child Assumptions in AI-Generated Stylesheets",
      "What common architectural error do AI models frequently introduce when asked to write XSLT rules for TEI &lt;choice&gt; containers?",
      [
          ("Selecting child elements by position (e.g. *[1]) rather than by element name (e.g. tei:reg), causing silent failures whenever markup order or child types vary.", 100, "Correct. Assuming that the regularized reading is always the first child creates brittle rules that break whenever &lt;orig&gt; or comments precede &lt;reg&gt;."),
          ("Assuming that &lt;choice&gt; can only contain audio recordings.", 0, "Incorrect. AI models recognize &lt;choice&gt; as textual, but frequently assume a rigid child sequence."),
          ("Replacing all &lt;choice&gt; tags with SQL database table queries.", 0, "Incorrect. The issue is XPath selector specificity, not database injection."),
          ("Refusing to generate XSLT because TEI is considered deprecated.", 0, "Incorrect. AI models readily generate XSLT, but often rely on fragile positional selectors.")
      ]),
    ("09 Question: Whitespace Normalization Traps in Mixed Content",
      "Why is applying the XSLT normalize-space() function indiscriminately across an entire document hazardous in scholarly editions?",
      [
          ("In mixed content (text interleaved with inline tags), normalize-space() strips leading and trailing spaces around inline elements, gluing adjacent words together.", 100, "Correct. normalize-space() removes boundary whitespace; when applied to inline elements like &lt;persName&gt; or &lt;hi&gt;, it fuses them with surrounding prose."),
          ("normalize-space() permanently converts all uppercase letters to lowercase.", 0, "Incorrect. normalize-space() only collapses whitespace; it does not alter letter case."),
          ("The function causes XML parsers to run out of memory on files larger than 10 lines.", 0, "Incorrect. normalize-space() is a lightweight string processing function."),
          ("It converts all spaces into hexadecimal numbers.", 0, "Incorrect. It strips leading/trailing spaces and collapses internal whitespace to single spaces.")
      ]),
    ("10 Question: The Four-Part Stylesheet Audit Framework",
      "In Lesson 7.3's human-in-the-loop audit framework, which sequence of verification steps ensures that an AI-generated stylesheet satisfies scholarly fidelity?",
      [
          ("1) Execution check (does it run); 2) Template inspection; 3) Word-by-word diff against manual ground truth (compare.py); 4) Element count audit (count.py).", 100, "Correct. The four-part framework verifies basic execution, inspects template logic, catches silent text omissions or corruptions via text diff, and verifies element counts."),
          ("1) Prompting the model twice; 2) Accepting the second output without checking.", 0, "Incorrect. Unchecked AI output violates basic digital humanities reproducibility and rigor."),
          ("1) Running a spell-check in Microsoft Word; 2) Uploading directly to Moodle.", 0, "Incorrect. Spell checks do not evaluate XML structural mapping or stylesheet fidelity."),
          ("1) Converting the stylesheet to PDF; 2) Printing on paper; 3) Shredding the original.", 0, "Incorrect. Digital scholarship requires rigorous algorithmic and textual auditing.")
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

print("Module 07 Phase F Assembly successfully completed!")
