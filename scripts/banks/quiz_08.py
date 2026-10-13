import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

shared_dir = Path(__file__).resolve().parents[3] / "shared" / "scripts"
sys.path.insert(0, str(shared_dir))
from question_bank import Q

src_mod = Path("src/modules/Module_08_Lemmatization")
dist_mod = Path("dist/moodle/Module_08_Lemmatization")
src_mod.mkdir(parents=True, exist_ok=True)
dist_mod.mkdir(parents=True, exist_ok=True)

# 1. Banner Image (1200x300)
def create_banner():
    w, h = 1200, 300
    img = Image.new("RGB", (w, h), color="#14261c")  # deep olive green / slate
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, w-10, h-10], outline="#c29b38", width=2)
    draw.rectangle([16, 16, w-16, h-16], outline="#2d4a3e", width=1)
    draw.rectangle([20, 20, 35, h-20], fill="#84cc16")  # vibrant lime/olive accent
    
    try:
        font_course = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font_course = font_title = font_sub = ImageFont.load_default()
        
    draw.text((60, 45), "RELS 398 / ENGL 398  •  DIGITAL METHODS FOR HISTORICAL DOCUMENTS", fill="#c29b38", font=font_course)
    draw.text((60, 100), "Module 08: Morphological Analysis & Lemmatization", fill="#f8fafc", font=font_title)
    draw.text((60, 175), "Lexical Headwords  •  CLTK & Stanza Pipelines  •  Syntactic Dependency Trees", fill="#cbd5e1", font=font_sub)
    draw.line([60, 225, w-60, 225], fill="#c29b38", width=1)
    draw.text((60, 245), "StFX Department of Religious Studies  •  Computational Philology Pipeline", fill="#86efac", font=font_sub)
    
    for p in [dist_mod / "01_Banner.png", src_mod / "01_Banner.png"]:
        img.save(p, "PNG")
        print(f"Wrote banner: {p}")

create_banner()

# 2. Learning Objectives
obj_html = """<div class="card p-3 mb-3 border-info" style="border-left: 5px solid #65a30d; background-color: #f7fee7; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #3f6212; margin-top: 0;">Module 08: Morphological Analysis & Lemmatization — Learning Objectives</h4>
    <p>By the end of this module, students will be able to:</p>
    <ul>
        <li><strong>Distinguish</strong> clearly between inflected surface tokens, dictionary headwords (lemmas), and morphological feature bundles (case, number, gender, tense, voice, mood).</li>
        <li><strong>Encode</strong> linguistic annotations within TEI XML using <code>&lt;w&gt;</code> elements with <code>lemma=</code>, <code>pos=</code>, and <code>@ana</code> attributes.</li>
        <li><strong>Deploy</strong> specialized NLP pipelines (such as CLTK, TreeTagger, and Stanza) to automate part-of-speech tagging and lemmatization on historical texts.</li>
        <li><strong>Model</strong> grammatical syntax using Universal Dependencies (UD) dependency relations and treebank structures.</li>
        <li><strong>Audit and benchmark</strong> neural LLM morphological taggers against a curated manual ground truth, evaluating out-of-vocabulary handling and hallucinated lemmas.</li>
    </ul>
</div>"""

# 3. Readings
reading_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #c29b38; background-color: #fcfcfd; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c29b38; margin-top: 0;">Assigned Readings & Foundational Scholarship</h4>
    <p>Please study the following resources on computational linguistics for historical languages:</p>
    <ul>
        <li><strong>Johnson, Kyle P. et al.</strong> "The Classical Language Toolkit: An Open-Source Library for Text Analysis in Ancient and Medieval Languages." <em>Proceedings of the ACL 2021 System Demonstrations</em>, pp. 248–254.</li>
        <li><strong>TEI Consortium.</strong> "Chapter 17: Simple Analytic Mechanisms" and "Chapter 18: Feature Structures." <em>TEI P5 Guidelines</em>, Version 4.8.0, 2024.</li>
        <li><strong>Schmid, Helmut.</strong> "Probabilistic Part-of-Speech Tagging Using Decision Trees (TreeTagger)." <em>International Conference on New Methods in Language Processing</em>, Manchester, UK.</li>
    </ul>
</div>"""

# 4. Watch List
watch_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #65a30d; background-color: #f7fee7; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #3f6212; margin-top: 0;">Curated Media & Technical Walkthroughs</h4>
    <p>Review these video demonstrations before completing your workshop assignment:</p>
    <ul>
        <li><strong>Morphological Disambiguation in Ancient Languages:</strong> Why inflected languages demand contextual parsing (21 mins).</li>
        <li><strong>Running CLTK & Stanza in Python:</strong> Tokenization, POS tagging, and lemmatizing Greek, Latin, and historical corpora (26 mins).</li>
        <li><strong>Visualizing Dependency Treebanks:</strong> Understanding syntactic heads, dependents, and Universal Dependencies (19 mins).</li>
    </ul>
</div>"""

# 5. Workshop
ws_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #65a30d; background-color: #f7fee7; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #3f6212; margin-top: 0;">Workshop: Comparative Morphological Parsing & Lemmatization</h4>
    <p><strong>Overview:</strong> In this workshop, you will parse a 20-word excerpt of your primary manuscript witness across three distinct tiers: (1) manual philological parse using a scholarly lexicon; (2) deterministic NLP tagging with CLTK or TreeTagger; and (3) zero-shot LLM parsing. You will compare accuracy, document edge cases, and build a TEI linguistic XML fragment.</p>
    <p><strong>Deadlines:</strong> Comparison Post due Friday by 11:00 PM; Peer Reviews due Monday by 11:00 PM.</p>
</div>"""

ws_sub = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Submission Instructions</h4>
    <ol>
        <li>Select 20 consecutive words from your primary manuscript witness.</li>
        <li><strong>Tier 1 (Manual):</strong> For each word, look up its canonical dictionary lemma and provide a full morphological breakdown (part of speech, gender/number/case or tense/voice/mood) in a Markdown table.</li>
        <li><strong>Tier 2 (NLP Engine):</strong> Run the excerpt through a computational tagging script (using Python CLTK, Stanza, or TreeTagger) and record the predicted lemmas and POS tags.</li>
        <li><strong>Tier 3 (LLM):</strong> Query an LLM with a structured system prompt requesting JSON or TEI <code>&lt;w&gt;</code> tags with <code>lemma</code> and <code>pos</code> attributes.</li>
        <li>Encode the excerpt in TEI XML using <code>&lt;w lemma="..." pos="..."&gt;token&lt;/w&gt;</code> elements based on your verified ground truth.</li>
        <li>Submit your TEI file, your Python/prompt script, and a <strong>300–500 word reflection</strong> analyzing which morphological categories caused the highest failure rate in the automated pipelines.</li>
    </ol>
</div>"""

ws_assess = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Peer Assessment Rubric</h4>
    <ul>
        <li><strong>Manual Ground Truth Precision (4 pts):</strong> The 20-word manual parse accurately identifies dictionary lemmas and correct inflectional morphology without grammatical errors.</li>
        <li><strong>TEI Linguistic Markup Validity (3 pts):</strong> The XML cleanly wraps tokens in <code>&lt;w&gt;</code> tags with valid <code>lemma</code> and <code>pos</code> attributes conforming to TEI P5 guidelines.</li>
        <li><strong>Comparative Error Analysis (3 pts):</strong> The 300–500 word analysis insightfully discusses why automated engines struggle with homographs, dialectal forms, or rare irregular conjugations.</li>
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
    (mod_p / "09_Quiz_Description.html").write_text("<p>Comprehensive weekly knowledge check covering morphological analysis, dictionary lemmatization, TEI linguistic encoding, CLTK pipelines, and dependency treebanking.</p>", encoding="utf-8")

print("Wrote HTML and Banner files.")

# 7. Build Weekly Quiz (10 Questions)
questions = [
    ("01 Question: Lemma vs Inflected Surface Token",
      "What is the precise definition of a 'lemma' in computational linguistics and lexicography?",
      [
          ("The canonical, uninflected base form (headword) under which a set of inflected words is conventionally grouped in a dictionary.", 100, "Correct. A lemma is the chosen dictionary citation form (e.g., 'write' for 'writes', 'wrote', 'written')."),
          ("The physical ink composition used by a medieval scriptorium.", 0, "Incorrect. Lemma is a linguistic and lexicographical concept, not a chemical writing fluid."),
          ("A software bug that causes a computer program to loop endlessly.", 0, "Incorrect. An endless loop is a software defect, not a lemma."),
          ("The physical dimension of a parchment leaf measured in millimeters.", 0, "Incorrect. Leaf dimension is a codicological measurement, not a linguistic lemma.")
      ]),
    ("02 Question: Morphological Feature Bundles",
      "Which set of linguistic categories constitutes the morphological feature bundle for a fully inflected finite verb in historical inflected languages?",
      [
          ("Person, number, tense, voice, and mood.", 100, "Correct. Finite verbs are parsed according to person (1st/2nd/3rd), number (singular/plural/dual), tense, voice, and mood."),
          ("Shelfmark, binding, watermark, and collation formula.", 0, "Incorrect. These are codicological book-structure terms."),
          ("Brightness, contrast, saturation, and gamma curve.", 0, "Incorrect. These are digital imaging raster attributes."),
          ("Font family, font size, line height, and letter spacing.", 0, "Incorrect. These are typographic and CSS formatting properties.")
      ]),
    ("03 Question: TEI Encoding of Linguistic Words",
      "How does TEI P5 recommend encoding an individual word token with its associated lemma and part-of-speech tag?",
      [
          ("<w lemma=\"regere\" pos=\"verb\">rexit</w>", 100, "Correct. The <w> element encloses the inflected surface token with attributes providing the dictionary lemma and part-of-speech category."),
          ("<choice><orig>regere</orig><reg>rexit</reg></choice>", 0, "Incorrect. <choice><orig><reg> is used for orthographic regularization, not grammatical lemmatization."),
          ("<teiHeader type=\"verb\" n=\"rexit\"/>", 0, "Incorrect. teiHeader is the document metadata container, not an inline word element."),
          ("<abbr expan=\"rexit\">regere</abbr>", 0, "Incorrect. <abbr> and <expan> are for scribal abbreviation expansion, not inflectional parsing.")
      ]),
    ("04 Question: Homography and Morphological Disambiguation",
      "Why is automated morphological parsing inherently challenging in inflected historical languages?",
      [
          ("Because identical surface word forms (homographs) can represent multiple distinct lemmas or grammatical analyses, requiring syntactic and semantic context to disambiguate.", 100, "Correct. Inflected languages exhibit widespread syncretism and homography, where a single spelling may represent several different cases, genders, or entirely different words."),
          ("Because historical manuscripts were written in secret cyphers designed to prevent reading.", 0, "Incorrect. Premodern literary and archival manuscripts were intended to be read by literate communities."),
          ("Because computers are fundamentally incapable of processing text written before the year 1900.", 0, "Incorrect. Computers process textual data of any era provided character encodings are defined."),
          ("Because ancient languages had no rules of grammar or syntax.", 0, "Incorrect. Classical and historical languages possessed highly rigorous, formalized grammatical systems.")
      ]),
    ("05 Question: Role of the Classical Language Toolkit (CLTK)",
      "What primary function does the Classical Language Toolkit (CLTK) Python library serve in digital humanities research?",
      [
          ("It provides specialized Natural Language Processing (NLP) tools, tokenizers, lemmatizers, and language models tailored specifically for ancient and medieval languages.", 100, "Correct. CLTK is an open-source library providing NLP pipelines for Greek, Latin, Old English, Sanskrit, and dozens of historical languages."),
          ("It is a hardware device that physically flattens ancient parchment scrolls.", 0, "Incorrect. CLTK is a software library, not a physical conservation machine."),
          ("It automatically converts historical documents into 3D video games.", 0, "Incorrect. CLTK focuses on computational linguistic text analysis."),
          ("It replaces university registrars by automatically grading student tuition payments.", 0, "Incorrect. CLTK has no administrative registrar functionality.")
      ]),
    ("06 Question: Out-of-Vocabulary (OOV) Dilemma",
      "What occurs when a rule-based or dictionary-lookup lemmatizer encounters an 'Out-of-Vocabulary' (OOV) word in a historical text?",
      [
          ("It fails to assign a lemma, either returning an unknown token flag or defaulting to the surface string, because the form does not exist in its static lexicon.", 100, "Correct. Static lexicon lookups cannot parse novel spelling variants, dialectal forms, or rare compound words not previously catalogued in the dictionary."),
          ("It immediately deletes the entire computer operating system.", 0, "Incorrect. Software graceful degradation returns null or unknown flags, not system deletion."),
          ("It contacts the author of the manuscript via email for clarification.", 0, "Incorrect. Authors of historical manuscripts are deceased."),
          ("It converts all adjacent words into capital letters.", 0, "Incorrect. OOV handling does not alter casing of surrounding tokens.")
      ]),
    ("07 Question: Syntactic Dependency Treebanking",
      "In a Universal Dependencies (UD) syntactic treebank, what do nodes and directed edges represent?",
      [
          ("Nodes represent individual words (tokens), and directed edges represent grammatical dependency relations pointing from a syntactic head to its dependent modifier.", 100, "Correct. Dependency grammar structures sentences as rooted trees where words connect via labeled grammatical relations (e.g. subject, object, modifier) directed from heads to dependents."),
          ("Nodes represent library buildings, and edges represent delivery truck routes.", 0, "Incorrect. That describes a physical logistical network, not a syntactic treebank."),
          ("Nodes represent punctuation marks, and edges represent paper thickness.", 0, "Incorrect. Dependency trees model the grammatical architecture of human language."),
          ("Nodes represent computer memory addresses, and edges represent electric current.", 0, "Incorrect. That describes computer hardware architecture, not linguistic syntax.")
      ]),
    ("08 Question: AI Hallucinations in Morphological Parsing",
      "What is a common failure mode when asking a general-purpose commercial LLM to lemmatize historical Greek or Latin poetry?",
      [
          ("Hallucinating modern language roots, inventing non-existent dictionary headwords, or confabulating grammatical genders to fit modern linguistic intuitions.", 100, "Correct. Without domain-specific grounding, general LLMs frequently project modern vocabulary or invent plausible-sounding but fictitious classical lemmas."),
          ("Outputting responses entirely in binary Morse code.", 0, "Incorrect. LLMs respond in natural language or requested structured formats."),
          ("Crashing the web browser due to excessive file size.", 0, "Incorrect. Text parsing outputs are small text objects that do not crash browsers."),
          ("Refusing to parse words that have more than six letters.", 0, "Incorrect. Models have no arbitrary character length restrictions on words.")
      ]),
    ("09 Question: Computational Value of Lemmatization",
      "Why is high-quality lemmatization indispensable for large-scale corpus analysis and digital text indexing?",
      [
          ("It collapses all inflected surface variants into a single conceptual index, enabling researchers to search and model vocabulary regardless of grammatical endings.", 100, "Correct. Lemmatization enables accurate frequency analysis, concordances, topic modeling, and stylometric search across inflected languages."),
          ("It prevents readers from copying text out of a PDF document.", 0, "Incorrect. Lemmatization is an analytical enhancement, not digital rights management (DRM)."),
          ("It reduces the physical weight of printed books in libraries.", 0, "Incorrect. Digital data processing does not alter the physical mass of paper codices."),
          ("It automatically translates the entire text into modern emoji pictograms.", 0, "Incorrect. Lemmatization preserves scholarly linguistic rigor.")
      ]),
    ("10 Question: Human-in-the-Loop Verification of Linguistic Data",
      "In a digital scholarly critical edition, why must automated linguistic annotations undergo human expert review?",
      [
          ("Because grammatical interpretation often reflects subtle theological, philosophical, or literary arguments that probabilistic algorithms cannot adjudicate authoritatively.", 100, "Correct. High-level syntactic and morphological decisions often define the core interpretive contribution of a scholarly edition, requiring expert human adjudication."),
          ("Because university regulations forbid the use of any software written after 1995.", 0, "Incorrect. Universities actively support modern technological research."),
          ("Because automated taggers always produce 0% accuracy on every language.", 0, "Incorrect. Modern taggers often achieve 85-95% accuracy, but the remaining errors are critical philological cruxes."),
          ("Because XML files become unreadable by web browsers if created by a computer script.", 0, "Incorrect. Browsers parse XML regardless of whether it was typed by hand or generated by a script.")
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

print("Module 08 Phase F Assembly successfully completed!")
