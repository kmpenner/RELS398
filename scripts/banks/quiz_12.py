import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

shared_dir = Path(__file__).resolve().parents[3] / "shared" / "scripts"
sys.path.insert(0, str(shared_dir))
from question_bank import Q

src_mod = Path("src/modules/Module_12_Commentary")
dist_mod = Path("dist/moodle/Module_12_Commentary")
src_mod.mkdir(parents=True, exist_ok=True)
dist_mod.mkdir(parents=True, exist_ok=True)

# 1. Banner Image (1200x300)
def create_banner():
    w, h = 1200, 300
    img = Image.new("RGB", (w, h), color="#3c1e14")  # deep warm terracotta / dark earth
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, w-10, h-10], outline="#c29b38", width=2)
    draw.rectangle([16, 16, w-16, h-16], outline="#5c2e1f", width=1)
    draw.rectangle([20, 20, 35, h-20], fill="#0284c7")  # Aegean blue accent
    
    try:
        font_course = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font_course = font_title = font_sub = ImageFont.load_default()
        
    draw.text((60, 45), "RELS 398 / ENGL 398  •  DIGITAL METHODS FOR HISTORICAL DOCUMENTS", fill="#c29b38", font=font_course)
    draw.text((60, 100), "Module 12: Digital Scholarly Commentary", fill="#f8fafc", font=font_title)
    draw.text((60, 175), "Intertextuality  •  TEI Standoff Notes  •  W3C Web Annotation Standards", fill="#cbd5e1", font=font_sub)
    draw.line([60, 225, w-60, 225], fill="#c29b38", width=1)
    draw.text((60, 245), "StFX Department of Religious Studies  •  Computational Philology Pipeline", fill="#fdba74", font=font_sub)
    
    for p in [dist_mod / "01_Banner.png", src_mod / "01_Banner.png"]:
        img.save(p, "PNG")
        print(f"Wrote banner: {p}")

create_banner()

# 2. Learning Objectives
obj_html = """<div class="card p-3 mb-3 border-info" style="border-left: 5px solid #0284c7; background-color: #f0f9ff; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #0369a1; margin-top: 0;">Module 12: Digital Scholarly Commentary — Learning Objectives</h4>
    <p>By the end of this module, students will be able to:</p>
    <ul>
        <li><strong>Classify</strong> scholarly commentary into distinct epistemological categories: philological/linguistic, historical/contextual, and intertextual text-reuse.</li>
        <li><strong>Encode</strong> granular inline and stand-off commentary notes in TEI P5 using <code>&lt;note&gt;</code>, <code>&lt;anchor&gt;</code>, and <code>@target</code> pointer mechanisms.</li>
        <li><strong>Apply</strong> algorithmic text-reuse discovery frameworks (such as Tesserae n-gram frequency matching) to detect intertextual allusions across classical and historical corpora.</li>
        <li><strong>Model</strong> annotations using the W3C Web Annotation Data Model, specifying targets, bodies, motivations, and selectors in JSON-LD.</li>
        <li><strong>Audit and vet</strong> AI-generated commentary notes, catching fabricated citations, anachronistic interpretations, and unsupported claims.</li>
    </ul>
</div>"""

# 3. Readings
reading_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #c29b38; background-color: #fcfcfd; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c29b38; margin-top: 0;">Assigned Readings & Foundational Scholarship</h4>
    <p>Please study the following key literature on digital commentary, annotation standards, and text reuse:</p>
    <ul>
        <li><strong>TEI Consortium.</strong> "Chapter 17: Simple Analytic Mechanisms." <em>TEI P5 Guidelines</em>, Version 4.8.0, 2024. Focus on § 17.1 (Notes and Annotations).</li>
        <li><strong>W3C.</strong> <em>Web Annotation Data Model: W3C Recommendation</em>. World Wide Web Consortium, 2017.</li>
        <li><strong>Vander Meulen, David L.</strong> "The Digital Commentary: Past Practices and Future Directions." <em>Textual Cultures</em>, 12(2), 2019, pp. 45–72.</li>
    </ul>
</div>"""

# 4. Watch List
watch_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #0284c7; background-color: #f0f9ff; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #0369a1; margin-top: 0;">Curated Media & Technical Walkthroughs</h4>
    <p>Review these video demonstrations before completing your workshop assignment:</p>
    <ul>
        <li><strong>From Marginalia to Linked Annotations:</strong> Historical origins and modern digital commentary architecture (22 mins).</li>
        <li><strong>Encoding Standoff Commentary in TEI XML:</strong> Anchoring notes with <code>&lt;anchor&gt;</code> and <code>&lt;ptr&gt;</code> in VS Code (24 mins).</li>
        <li><strong>Detecting Intertextual Text Reuse with Tesserae:</strong> Algorithmic allusion matching across historical corpora (20 mins).</li>
    </ul>
</div>"""

# 5. Workshop
ws_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #0284c7; background-color: #f0f9ff; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #0369a1; margin-top: 0;">Workshop: Multi-Tiered Scholarly Commentary & Intertextual Linking</h4>
    <p><strong>Overview:</strong> In this workshop, you will author five scholarly commentary notes for your primary witness passage spanning three distinct categories (philological, historical, intertextual). You will encode them using stand-off TEI markup, connect them to Linked Open Data authorities, and compare your manual analysis against an automated text-reuse discovery query.</p>
    <p><strong>Deadlines:</strong> Comparison Post due Friday by 11:00 PM; Peer Reviews due Monday by 11:00 PM.</p>
</div>"""

ws_sub = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Submission Instructions</h4>
    <ol>
        <li>Draft five scholarly commentary notes on your passage: at least one philological (explaining grammar/idiom), one historical/cultural (explaining realia/context), and one intertextual (documenting an allusion or scripture citation).</li>
        <li>Encode the notes in TEI XML using stand-off <code>&lt;back&gt;&lt;div type="commentary"&gt;&lt;note target="#token-or-anchor" type="..."&gt;...&lt;/note&gt;&lt;/div&gt;&lt;/back&gt;</code>.</li>
        <li>Link at least two notes to external Linked Open Data authorities (e.g. Pleiades URI for places, VIAF for historical figures, or CTS URN for classical passages).</li>
        <li>Run an intertextual text-reuse check (via Tesserae or targeted corpus search) and evaluate whether automated n-gram matching detected your allusion.</li>
        <li>Submit your TEI XML file and a <strong>300–500 word reflection</strong> discussing the trade-offs between inline vs. stand-off commentary architecture.</li>
    </ol>
</div>"""

ws_assess = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Peer Assessment Rubric</h4>
    <ul>
        <li><strong>Commentary Categorization & Erudition (4 pts):</strong> The commentary notes exhibit genuine scholarly depth, clearly distinguishing between linguistic glosses, historical context, and verified literary allusions.</li>
        <li><strong>Stand-Off TEI & LOD Pointers (3 pts):</strong> The stand-off markup is valid, accurately anchored to text coordinates, and includes functional Linked Open Data URI attributes.</li>
        <li><strong>Text Reuse & Architecture Reflection (3 pts):</strong> The 300–500 word analysis insightfully critiques the limitations of purely statistical text-reuse algorithms and defends the selected TEI annotation model.</li>
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
    (mod_p / "09_Quiz_Description.html").write_text("<p>Comprehensive weekly knowledge check covering scholarly commentary taxonomy, TEI standoff notes, Tesserae intertextual discovery, and W3C Web Annotation standards.</p>", encoding="utf-8")

print("Wrote HTML and Banner files.")

# 7. Build Weekly Quiz (10 Questions)
questions = [
    ("01 Question: Taxonomy of Scholarly Commentary",
      "Which three primary categories constitute the foundation of a comprehensive scholarly commentary on a historical text?",
      [
          ("Philological (linguistic/grammatical), historical/cultural (realia/context), and intertextual (citations/allusions/text reuse).", 100, "Correct. Standard critical commentaries address linguistic difficulty, historical realia, and intertextual relationships with other literary works."),
          ("Financial, legal, marketing, and advertising.", 0, "Incorrect. These are corporate commercial business categories, not humanities scholarly commentary domains."),
          ("HTML, CSS, JavaScript, and PHP.", 0, "Incorrect. These are web development programming languages."),
          ("Hardcover, paperback, audiobook, and ebook.", 0, "Incorrect. These are commercial book publishing formats.")
      ]),
    ("02 Question: Inline vs Stand-Off Commentary Architecture",
      "Why do modern digital critical editions strongly prefer 'stand-off' commentary notes over 'inline' `<note>` elements?",
      [
          ("Stand-off notes reside outside the primary narrative body (e.g. in `<back>`), preventing editorial prose from interrupting the syntactic flow of the source text and facilitating multiple overlapping commentary layers.", 100, "Correct. Stand-off markup maintains clean separation between source text and editorial interpretation, allowing multiple scholars to annotate the same coordinates without tag overlapping collisions."),
          ("Because inline notes are illegal under Canadian intellectual property laws.", 0, "Incorrect. Markup architecture is an engineering and philological decision, not a legal statute."),
          ("Because web browsers refuse to display any webpage containing inline notes.", 0, "Incorrect. Browsers can render any valid HTML/XML structure."),
          ("Because stand-off notes automatically delete the source text to save server bandwidth.", 0, "Incorrect. Stand-off notes point to the source text via URI targets; they never delete it.")
      ]),
    ("03 Question: Anchoring Non-Hierarchical Text Spans",
      "In TEI P5, how can an editor attach a commentary note to an arbitrary sequence of words that crosses paragraph or line boundaries without violating XML nesting?",
      [
          ("By placing empty `<anchor xml:id=\"...\">` milestone elements at the start and end of the passage and referencing both IDs in the note's `@target` attribute.", 100, "Correct. Empty anchor milestones provide precise coordinate points in the text tree without creating illegal overlapping XML hierarchies."),
          ("By deleting the closing `</p>` tags so that elements can overlap freely.", 0, "Incorrect. Deleting closing tags produces malformed XML that immediately crashes parsers."),
          ("By converting the whole paragraph into an uncompressed JPEG picture.", 0, "Incorrect. Converting text to raster images destroys machine readability and searchability."),
          ("By renaming all tags `<div1>`, `<div2>`, and `<div3>`.", 0, "Incorrect. Arbitrary tag renaming does not resolve structural overlapping.")
      ]),
    ("04 Question: Operational Principles of Tesserae",
      "How does the Tesserae intertextual discovery tool identify literary text reuse across classical texts?",
      [
          ("It uses frequency-weighted n-gram matching, calculating scores based on the rarity of shared words and their proximity within sentences.", 100, "Correct. Tesserae finds intertextual allusions by scoring pairs of shared words inversely proportional to their overall corpus frequencies and positional distance."),
          ("It reads the author's personal diary to find written confessions of plagiarism.", 0, "Incorrect. Tesserae is an automated computational text analysis tool operating on digital corpora."),
          ("It translates both texts into binary Morse code and compares the audio frequencies.", 0, "Incorrect. Tesserae evaluates lexical frequency vectors, not acoustic sound waves."),
          ("It checks whether both authors purchased books from the same bookstore.", 0, "Incorrect. Ancient authors lived centuries before modern commercial book chains.")
      ]),
    ("05 Question: W3C Web Annotation Data Model",
      "In the W3C Web Annotation Data Model (JSON-LD), what are the two essential components linked together by an `Annotation` object?",
      [
          ("The `body` (the commentary content, translation, or tag) and the `target` (the specific digital resource or text fragment being annotated).", 100, "Correct. W3C Web Annotation formally links a Target (what is being annotated) to a Body (the commentary or analytical content) via a declared Motivation."),
          ("The `username` and the `password`.", 0, "Incorrect. These are authentication credentials, not W3C annotation components."),
          ("The `printer` and the `paper`.", 0, "Incorrect. These are physical printing hardware elements."),
          ("The `input` and the `output`.", 0, "Incorrect. These are general software engineering concepts.")
      ]),
    ("06 Question: W3C TextQuoteSelector",
      "How does a W3C `TextQuoteSelector` anchor an annotation to a specific phrase in a web document even if the underlying HTML shifts slightly?",
      [
          ("By recording an `exact` matching string along with a `prefix` context and a `suffix` context to locate the unique occurrence robustly.", 100, "Correct. A TextQuoteSelector uses exact text plus surrounding prefix and suffix context, ensuring stable anchoring even across dynamic DOM updates."),
          ("By calculating the physical weight of the reader's laptop computer.", 0, "Incorrect. Hardware weight is completely irrelevant to digital text selectors."),
          ("By permanently locking the webpage so that nobody can ever edit it again.", 0, "Incorrect. TextQuoteSelectors are designed specifically to handle documents that undergo minor edits."),
          ("By converting all surrounding words into secret passwords.", 0, "Incorrect. Selectors operate on transparent plaintext context strings.")
      ]),
    ("07 Question: Linking Notes to Linked Open Data Authorities",
      "Why is enriching commentary notes with Linked Open Data URIs (such as Pleiades for places and VIAF for people) methodologically valuable?",
      [
          ("It disambiguates entities unambiguously and links the edition to the global semantic web, enabling automated cross-project querying and interactive spatial mapping.", 100, "Correct. Resolvable authority URIs eliminate naming ambiguities (e.g. distinguishing Antioch in Syria from Antioch in Pisidia) and integrate the text with global knowledge graphs."),
          ("Because it increases the purchase price of the digital edition on commercial ebook stores.", 0, "Incorrect. Linked Open Data promotes open scholarship, not commercial price gouging."),
          ("Because university servers crash if an XML file contains fewer than ten web links.", 0, "Incorrect. Servers do not require external links to function."),
          ("Because it allows the user to play 3D computer games inside the footnote.", 0, "Incorrect. Linked Data facilitates rigorous scholarly research, not video gaming.")
      ]),
    ("08 Question: AI Hallucinations in Historical Commentary",
      "When using generative AI to assist in drafting historical commentary notes, what is a frequent, treacherous hallucination hazard?",
      [
          ("Fabricating scholarly citations (inventing non-existent books, authors, or journal page numbers) and projecting anachronistic modern theological or social concepts onto premodern sources.", 100, "Correct. LLMs frequently generate completely fabricated but highly convincing bibliographies and project anachronistic concepts back into antiquity."),
          ("Translating the text into completely flawless ancient Sumerian cuneiform.", 0, "Incorrect. Models typically fail at low-resource ancient scripts rather than producing flawless translations."),
          ("Refusing to write any sentence that contains the letter 'e'.", 0, "Incorrect. Models have no constraint against standard letters unless explicitly prompted."),
          ("Deleting all comments made by the instructor on Moodle.", 0, "Incorrect. Generating text in a chat prompt cannot interact with or delete remote Moodle forum posts.")
      ]),
    ("09 Question: Distinguishing Literary Allusion from Coincidental Overlap",
      "Why must algorithmic text-reuse matches (e.g. from Tesserae) be verified by a human scholar before being published as an intertextual commentary note?",
      [
          ("Because statistical algorithms frequently flag coincidental collocations of common grammatical words or stock idioms that lack any intentional literary or historical allusion.", 100, "Correct. Algorithms detect string similarities; only human philologists can evaluate whether shared vocabulary reflects genuine intertextual dialogue, formulaic convention, or random chance."),
          ("Because computers are legally prohibited from publishing literary criticism.", 0, "Incorrect. Computational analysis is widely published in academic venues."),
          ("Because all ancient authors wrote completely unique sentences that never shared a single word.", 0, "Incorrect. Historical texts share vast lexical conventions and literary allusions."),
          ("Because digital editions are only allowed to have one commentary note per chapter.", 0, "Incorrect. Digital editions impose no arbitrary limits on commentary density.")
      ]),
    ("10 Question: Quality Assurance for TEI Commentary Markup",
      "What is the critical validation requirement for stand-off commentary notes before compiling a digital edition?",
      [
          ("Verifying that every `@target` URI correctly resolves to an existing `xml:id` in the text body, and that all cited authorities resolve to valid HTTP URIs.", 100, "Correct. Dangling pointers and dead links undermine the reliability of a digital edition; every anchor target must resolve cleanly during validation."),
          ("Ensuring that every note is written in iambic pentameter verse.", 0, "Incorrect. Scholarly commentary is written in analytical academic prose."),
          ("Confirming that every single word in the text has at least three footnotes.", 0, "Incorrect. Commentary should be judicious, focused on genuine cruxes, rather than cluttering clear text."),
          ("Deleting all original manuscript text so only the commentary remains.", 0, "Incorrect. A critical commentary accompanies and elucidates the primary source, rather than erasing it.")
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

print("Module 12 Phase F Assembly successfully completed!")
