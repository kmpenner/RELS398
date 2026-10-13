import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

shared_dir = Path(__file__).resolve().parents[3] / "shared" / "scripts"
sys.path.insert(0, str(shared_dir))

src_mod = Path("src/modules/Module_09_Named_Entities")
dist_mod = Path("dist/moodle/Module_09_Named_Entities")
src_mod.mkdir(parents=True, exist_ok=True)
dist_mod.mkdir(parents=True, exist_ok=True)

# 1. Banner Image (1200x300)
def create_banner():
    w, h = 1200, 300
    img = Image.new("RGB", (w, h), color="#12281e")  # deep spruce green
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, w-10, h-10], outline="#c29b38", width=2)
    draw.rectangle([16, 16, w-16, h-16], outline="#234e3b", width=1)
    draw.rectangle([20, 20, 35, h-20], fill="#10b981")  # vibrant spruce / emerald accent
    
    try:
        font_course = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font_course = font_title = font_sub = ImageFont.load_default()
        
    draw.text((60, 45), "RELS 398 / ENGL 398  •  DIGITAL METHODS FOR HISTORICAL DOCUMENTS", fill="#c29b38", font=font_course)
    draw.text((60, 100), "Module 09: Named-Entity Markup & Authority Linking", fill="#f8fafc", font=font_title)
    draw.text((60, 175), "Manual TEI Annotation  •  SpaCy NER & Gazetteers  •  LLM Audit & Linking", fill="#cbd5e1", font=font_sub)
    draw.line([60, 225, w-60, 225], fill="#c29b38", width=1)
    draw.text((60, 245), "StFX Department of Religious Studies  •  Computational Philology Pipeline", fill="#6ee7b7", font=font_sub)
    
    for p in [dist_mod / "01_Banner.png", src_mod / "01_Banner.png"]:
        img.save(p, "PNG")
        print(f"Wrote banner: {p}")

create_banner()

# 2. Learning Objectives (ensure consistency across src and dist)
obj_html = """<div class="card p-3 mb-3 border-info" style="border-left: 5px solid #047857; background-color: #ecfdf5; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #065f46; margin-top: 0;">Module 09: Named-Entity Markup: Learning Objectives</h4>
    <p>By the end of this module, students will be able to:</p>
    <ul>
        <li><strong>Identify</strong> the people, places, organizations and dates in a historical document, and say when a name is ambiguous.</li>
        <li><strong>Encode</strong> them with <code>&lt;persName&gt;</code>, <code>&lt;placeName&gt;</code>, <code>&lt;orgName&gt;</code> and <code>&lt;date @when&gt;</code>, linking each to an authority record (Wikidata, VIAF, GeoNames) with <code>@ref</code>.</li>
        <li><strong>Run</strong> automated entity recognition and gazetteer lookup, and measure its precision and recall against your hand tagging.</li>
        <li><strong>Audit</strong> AI-assisted entity tagging and linking for invented identifiers and wrong matches, recording a verified absence where no authority record exists.</li>
    </ul>
</div>"""

# 3. Readings
reading_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #c29b38; background-color: #fcfcfd; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c29b38; margin-top: 0;">Assigned Readings & Foundational Scholarship</h4>
    <p>Please study the following foundational scholarship on historical named entity recognition and authority linking:</p>
    <ul>
        <li><strong>TEI Consortium.</strong> "Chapter 13: Names, Dates, People, and Places." <em>TEI P5: Guidelines for Electronic Text Encoding and Interchange</em>, Version 4.8.0, 2024.</li>
        <li><strong>Ehrmann, Maud, et al.</strong> "Named Entity Recognition and Classification in Historical Documents: A Survey." <em>ACM Computing Surveys</em> 56, no. 2 (2023): 1–47.</li>
        <li><strong>Flickinger, Dan, and Adam Przepiórkowski.</strong> "Authority Files, Disambiguation, and Linked Open Data in Digital Scholarly Editions." <em>Journal of the Text Encoding Initiative</em> 14 (2021): 112–134.</li>
    </ul>
</div>"""

# 4. Watch List
watch_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #047857; background-color: #ecfdf5; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #065f46; margin-top: 0;">Curated Media & Technical Walkthroughs</h4>
    <p>Review these video demonstrations before completing your weekly laboratory assignments:</p>
    <ul>
        <li><strong>Encoding Named Entities in TEI XML:</strong> Practical tagging of <code>&lt;persName&gt;</code>, <code>&lt;placeName&gt;</code>, and <code>&lt;date&gt;</code> elements (19 mins).</li>
        <li><strong>Building Automated NER Pipelines with SpaCy:</strong> Statistical sequence tagging, custom EntityRuler components, and gazetteers (25 mins).</li>
        <li><strong>Authority Control and Wikidata Entity Linking:</strong> Querying APIs, disambiguating historical names, and documenting verified absences (22 mins).</li>
    </ul>
</div>"""

# 5. Workshop / Assignment Description & Instructions
ws_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #047857; background-color: #ecfdf5; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #065f46; margin-top: 0;">Assignment: Module 9 (Named-Entity Markup)</h4>
    <p><strong>Overview:</strong> In this capstone portfolio assignment, you will identify, annotate, and link 20 entities from your primary manuscript witness across three distinct tiers: (1) manual TEI markup with authority linking; (2) deterministic NLP tagging with SpaCy and gazetteers; and (3) prompt-engineered AI parsing in VS Code Antigravity. You will measure precision, recall, and F1 scores, compile a three-way discrepancy matrix, and author a 300–500 word critical methodological reflection in <code>ENTITY_AUDIT.md</code>.</p>
    <p><strong>Deadline:</strong> due Friday, November 6, by 11:00 PM.</p>
</div>"""

ws_sub = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Submission Instructions</h4>
    <ol>
        <li>Select a 20-entity excerpt from your primary manuscript witness.</li>
        <li><strong>Tier 1 (Manual Ground Truth):</strong> Compile your editorial policies in <code>ENTITY_POLICIES.md</code>, research authority records (Wikidata, VIAF, GeoNames, DCB), and hand-author <code>ground_truth_entities_manual.xml</code>.</li>
        <li><strong>Tier 2 (Automated NER Pipeline):</strong> Run a SpaCy tagging script, export predictions to <code>ner_baseline.xml</code>, evaluate precision/recall/F1 against your manual baseline, and compile <code>NER_BENCHMARK.md</code>.</li>
        <li><strong>Tier 3 (AI Pipeline & Linking):</strong> Run <code>ai_entity_parser.py</code> with system constraints in VS Code Antigravity, validate schema and token alignment, and test authority links against live registries.</li>
        <li><strong>Three-Way Comparative Audit:</strong> Compile the discrepancy matrix and author your 300–500 word reflection in <code>ENTITY_AUDIT.md</code> classifying errors into our course error taxonomy.</li>
        <li>Verify all repository files pass schema validation, and submit your portfolio on Moodle before 11:00 PM on Friday, November 6.</li>
    </ol>
</div>"""

ws_assess = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Evaluation Rubric</h4>
    <ul>
        <li><strong>Manual Ground Truth Precision (4 pts):</strong> The 20-entity manual parse reflects exemplary philological rigor, with verified authority links, documented verified absences, and an explicit <code>ENTITY_POLICIES.md</code> document.</li>
        <li><strong>TEI XML Markup Validity (3 pts):</strong> The XML conforms strictly to TEI P5 guidelines, maintains valid <code>@when</code> ISO dates and <code>@ref</code> URIs, and preserves unbroken token alignment across all versions.</li>
        <li><strong>Comparative Error Analysis (3 pts):</strong> The 300–500 word reflection insightfully diagnoses computational failure modes (OOV orthography, boundary slips, type confusion, hallucinations) with accurate mathematical metrics (P/R/F1).</li>
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
    (mod_p / "09_Quiz_Description.html").write_text("<p>Comprehensive weekly knowledge check covering named entity recognition, TEI Chapter 13 encoding, authority registries (Wikidata, VIAF, GeoNames), statistical sequence tagging, and comparative AI audits.</p>", encoding="utf-8")

print("Wrote HTML and Banner files.")

# 7. Build Weekly Quiz (10 Questions)
questions = [
    ("01 Question: Core Named Entity Classes",
      "Which four primary entity classes form the core foundation of computational information extraction and TEI Chapter 13 encoding?",
      [
          ("Persons, Places, Organizations, and Dates.", 100, "Correct. Computational entity recognition and TEI Chapter 13 standardize on people (<persName>), places (<placeName>), institutions (<orgName>), and calendar times (<date>)."),
          ("Nouns, Verbs, Adjectives, and Adverbs.", 0, "Incorrect. These are grammatical parts of speech, not named entity semantic categories."),
          ("Parchment, Paper, Papyrus, and Vellum.", 0, "Incorrect. These are historical writing materials and codicological substrates."),
          ("Margins, Headers, Footers, and Columns.", 0, "Incorrect. These are typographic and structural page layout elements.")
      ]),
    ("02 Question: TEI Chapter 13 Tagging Syntax",
      "Which TEI P5 XML element correctly tags the name of an official governmental institution or legislative body?",
      [
          ("<orgName>Comité des décrets</orgName>", 100, "Correct. TEI P5 Chapter 13 designates <orgName> specifically for institutions, corporate bodies, and governmental organizations."),
          ("<institution name=\"Comité des décrets\"/>", 0, "Incorrect. <institution> is not an inline named entity element in TEI P5."),
          ("<gov committee=\"yes\">Comité des décrets</gov>", 0, "Incorrect. <gov> is not a valid TEI element."),
          ("<placeName>Comité des décrets</placeName>", 0, "Incorrect. <placeName> is reserved for geographic locations, not institutional bodies.")
      ]),
    ("03 Question: ISO 8601 Temporal Normalization",
      "Why must historical calendar dates be enriched with the @when attribute in TEI XML?",
      [
          ("To record a normalized, computer-readable date in ISO 8601 format (YYYY-MM-DD) while preserving historical scribal wording in the text node.", 100, "Correct. The @when attribute bridges historical phrasing (e.g. 'the twenty-second Day of November') to standard machine-readable ISO dates (1752-11-22)."),
          ("To automatically delete the original scribal text from the electronic edition.", 0, "Incorrect. TEI preserves the historical surface reading intact within the element."),
          ("To tell the web browser to trigger an alarm clock on that calendar date.", 0, "Incorrect. @when is an analytical scholarly attribute, not an alarm timer."),
          ("To translate historical dates from English into modern Latin.", 0, "Incorrect. ISO 8601 uses universal numerical notation, not Latin prose.")
      ]),
    ("04 Question: Canonical Authority Registries",
      "What is the primary function of the @ref attribute on a named entity tag?",
      [
          ("To link the entity directly to a canonical URI in an external authority registry (such as Wikidata, VIAF, or GeoNames) or a local project identifier.", 100, "Correct. The @ref attribute establishes Linked Open Data connections to authoritative external registries or local prosopography."),
          ("To assign a font size to the printed word on paper.", 0, "Incorrect. Font sizes are handled by CSS stylesheets, not @ref attributes."),
          ("To count the total number of letters in the author's surname.", 0, "Incorrect. Character counting is not the purpose of entity linking."),
          ("To indicate that the entity is a fictional character in a novel.", 0, "Incorrect. @ref identifies real historical authority records regardless of genre.")
      ]),
    ("05 Question: The Verified Absence Standard",
      "What protocol must an editor follow under our course rules when a historical person does not appear in Wikidata or VIAF?",
      [
          ("Document a Verified Absence by logging the searched repositories and dates, and mint a local project identifier (e.g. #person-001).", 100, "Correct. When exhaustive searches confirm no external record exists, editors document the absence and create a local project identifier rather than inventing a link."),
          ("Invent a synthetic 8-digit Wikidata Q-identifier and pretend it exists.", 0, "Incorrect. Inventing synthetic external IDs corrupts linked data integrity."),
          ("Delete the individual entirely from the transcribed historical text.", 0, "Incorrect. Scholarly editions never alter primary texts to satisfy database limitations."),
          ("Abort the editing project immediately and delete the repository.", 0, "Incorrect. Documenting verified absences locally is standard scholarly practice.")
      ]),
    ("06 Question: Statistical Sequence Tagging Mechanics",
      "How do modern NLP libraries like SpaCy identify entity spans in unannotated running text?",
      [
          ("Using statistical sequence models trained on large annotated corpora to evaluate token transition probabilities and contextual embeddings.", 100, "Correct. Statistical NER models predict entity tags based on probabilistic contextual patterns learned from training data."),
          ("By matching words against an alphabetical list of human names printed in 1850.", 0, "Incorrect. Static lists describe gazetteers; statistical models use contextual machine learning weights."),
          ("By checking whether each word contains an even or odd number of letters.", 0, "Incorrect. Letter counts have no bearing on semantic entity recognition."),
          ("By connecting directly to the human author via telepathic sensors.", 0, "Incorrect. Machine learning algorithms process digital textual data mathematically.")
      ]),
    ("07 Question: Out-of-Vocabulary Historical Orthography",
      "Why do off-the-shelf modern NLP models frequently fail when applied to eighteenth-century archival manuscripts?",
      [
          ("Because modern models are trained on contemporary news and web text, making them fragile when encountering historical spelling, archaic punctuation, and early modern capitalization habits.", 100, "Correct. Out-of-Vocabulary (OOV) mismatches occur when the orthographic patterns of archival witnesses diverge sharply from contemporary training data."),
          ("Because eighteenth-century manuscripts are written in computer assembly code.", 0, "Incorrect. Archival documents are written in human natural languages."),
          ("Because modern computers are legally prohibited from parsing texts written before 1900.", 0, "Incorrect. Software operates freely across all historical time periods."),
          ("Because early modern printers did not use the Roman alphabet.", 0, "Incorrect. Early modern English and French used the Roman alphabet.")
      ]),
    ("08 Question: Error Metrics: Precision and Recall",
      "In named entity benchmarking, what does the Precision metric measure?",
      [
          ("The percentage of entities predicted by the automated model that were actually correct according to the human ground truth.", 100, "Correct. Precision = True Positives / (True Positives + False Negatives), measuring the accuracy of the model's positive claims."),
          ("The percentage of all real ground-truth entities that the model managed to find.", 0, "Incorrect. That is the definition of Recall, not Precision."),
          ("The clock execution time required to process one manuscript page.", 0, "Incorrect. Processing time measures throughput, not mathematical accuracy."),
          ("The number of words in the student's final analytical reflection.", 0, "Incorrect. Word count is an assignment parameter, not an algorithmic evaluation metric.")
      ]),
    ("09 Question: Generative AI Hallucination in Entity Linking",
      "What critical risk must scholars audit when using generative Large Language Models to link entities to external databases?",
      [
          ("The hallucination of plausible-sounding but completely fictitious Wikidata Q-identifiers or nonexistent authority URLs.", 100, "Correct. Generative models prioritize fluent continuation and will generate syntactically convincing but fabricated identifiers if ungrounded."),
          ("The physical corruption of the computer hard drive memory sectors.", 0, "Incorrect. Model inference does not physically damage disk sectors."),
          ("The automated translation of all text into binary Morse code.", 0, "Incorrect. LLMs output requested natural language or structured formats."),
          ("The immediate deletion of the user's internet browser history.", 0, "Incorrect. LLM inference does not manipulate local browser history files.")
      ]),
    ("10 Question: The Human-in-the-Loop Methodology",
      "Why does computational textual scholarship reject 'pure automation' in favor of a 'human-in-the-loop' paradigm?",
      [
          ("Because automated tools accelerate draft generation, but trained human scholars must audit, adjudicate ambiguous cruxes, and maintain ethical accountability for the edition.", 100, "Correct. Computational models lack historical understanding and accountability; human scholarly adjudication remains essential for authoritative critical editions."),
          ("Because universities have banned all digital computers from humanities departments.", 0, "Incorrect. Universities actively champion digital humanities methodologies."),
          ("Because automated models achieve 0% accuracy on every document genre.", 0, "Incorrect. Modern models achieve valuable accuracy, but their remaining errors represent critical historical cruxes."),
          ("Because web browsers cannot display XML created by computer programs.", 0, "Incorrect. Browsers parse XML regardless of how it was produced.")
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

print("Module 09 Phase F Assembly successfully completed!")
