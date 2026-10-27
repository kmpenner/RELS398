import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

shared_dir = Path(__file__).resolve().parents[3] / "shared" / "scripts"
sys.path.insert(0, str(shared_dir))
from question_bank import Q

src_mod = Path("src/modules/Module_11_Alignment")
dist_mod = Path("dist/moodle/Module_11_Alignment")
src_mod.mkdir(parents=True, exist_ok=True)
dist_mod.mkdir(parents=True, exist_ok=True)

# 1. Banner Image (1200x300)
def create_banner():
    w, h = 1200, 300
    img = Image.new("RGB", (w, h), color="#1e1b4b")  # deep lapis lazuli / indigo
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, w-10, h-10], outline="#c29b38", width=2)
    draw.rectangle([16, 16, w-16, h-16], outline="#3730a3", width=1)
    draw.rectangle([20, 20, 35, h-20], fill="#eab308")  # vibrant saffron / gold accent
    
    try:
        font_course = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font_course = font_title = font_sub = ImageFont.load_default()
        
    draw.text((60, 45), "RELS 398 / ENGL 398  •  DIGITAL METHODS FOR HISTORICAL DOCUMENTS", fill="#c29b38", font=font_course)
    draw.text((60, 100), "Module 11: Text Alignment & Interlinear Glossing", fill="#f8fafc", font=font_title)
    draw.text((60, 175), "Leipzig Glossing Rules  •  TEI linkGrp Standoff  •  Statistical Alignment Models", fill="#cbd5e1", font=font_sub)
    draw.line([60, 225, w-60, 225], fill="#c29b38", width=1)
    draw.text((60, 245), "StFX Department of Religious Studies  •  Computational Philology Pipeline", fill="#fde047", font=font_sub)
    
    for p in [dist_mod / "01_Banner.png", src_mod / "01_Banner.png"]:
        img.save(p, "PNG")
        print(f"Wrote banner: {p}")

create_banner()

# 2. Learning Objectives
obj_html = """<div class="card p-3 mb-3 border-info" style="border-left: 5px solid #eab308; background-color: #fefce8; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #854d0e; margin-top: 0;">Module 11: Text Alignment & Interlinear Glossing — Learning Objectives</h4>
    <p>By the end of this module, students will be able to:</p>
    <ul>
        <li><strong>Construct</strong> four-line Interlinear Glossed Text (IGT) adhering strictly to the international Leipzig Glossing Rules, distinguishing morpheme cuts (-) from fused grammatical categories (.).</li>
        <li><strong>Encode</strong> sentence-level parallel alignments in TEI P5 using stand-off <code>&lt;linkGrp&gt;</code> and <code>&lt;link&gt;</code> architecture in Visual Studio Code.</li>
        <li><strong>Analyze</strong> the operational principles of length-based sentence alignment (Gale-Church) using character count ratios and visual alignment matrices.</li>
        <li><strong>Utilize</strong> interactive digital humanities alignment platforms (Alpheios Alignment Editor, Ugarit) to produce verified parallel corpora without command-line friction.</li>
        <li><strong>Audit and evaluate</strong> AI-assisted translation alignments, identifying failure modes such as silent spelling modernization, Rule 2 hyphen confusion, and pronoun enclisis slips.</li>
    </ul>
</div>"""

# 3. Readings
reading_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #c29b38; background-color: #fcfcfd; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c29b38; margin-top: 0;">Assigned Readings & Foundational Scholarship</h4>
    <p>Please study the following key literature on text alignment, linguistic glossing, and parallel digital editions:</p>
    <ul>
        <li><strong>Bickel, Balthasar, Bernard Comrie, and Martin Haspelmath.</strong> "The Leipzig Glossing Rules: Conventions for Multilingual Interlinear Glosses." <em>Max Planck Institute for Evolutionary Anthropology & Department of Linguistics, University of Leipzig</em>, 2015.</li>
        <li><strong>TEI Consortium.</strong> "Chapter 16: Linking, Segmentation, and Alignment." <em>TEI P5 Guidelines</em>, Version 4.8.0, 2024. Focus on § 16.1.3 (Blocks of Correspondence: linkGrp).</li>
        <li><strong>Tiedemann, Jörg.</strong> "Parallel Data Extraction." <em>Bitext Alignment</em>, Morgan & Claypool Publishers, 2011.</li>
        <li><strong>Baumgardt, Sonja.</strong> "Digital Interlinear Editions: Challenges and Perspectives for Ancient and Medieval Texts." <em>Journal of Digital Humanities</em>, 2020.</li>
    </ul>
</div>"""

# 4. Watch List
watch_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #eab308; background-color: #fefce8; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #854d0e; margin-top: 0;">Curated Media & Technical Walkthroughs</h4>
    <p>Review these video demonstrations before completing your workshop assignment:</p>
    <ul>
        <li><strong>The Leipzig Glossing Rules in Practice:</strong> How to build rigorous 4-line interlinear linguistic glosses (21 mins).</li>
        <li><strong>Encoding Bilingual Alignments in TEI XML:</strong> Practical stand-off markup using <code>&lt;linkGrp&gt;</code> in VS Code (24 mins).</li>
        <li><strong>Algorithmic Text Alignment with Gale-Church:</strong> Length-based sentence alignment and interactive web editors (20 mins).</li>
    </ul>
</div>"""

# 5. Workshop / Assignment
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
    (mod_p / "09_Quiz_Description.html").write_text("<p>Comprehensive weekly knowledge check covering Leipzig Glossing Rules, TEI stand-off alignment, Gale-Church sentence alignment, and AI bilingual parsing.</p>", encoding="utf-8")

print("Wrote HTML and Banner files.")

# 7. Build Weekly Quiz (10 Questions)
questions = [
    ("01 Question: Architecture of Four-Line Leipzig Glossing",
      "In linguistic and philological scholarship, what are the four standard tiers of an Interlinear Glossed Text (IGT) adhering to the Leipzig Glossing Rules?",
      [
          ("Tier 1: Original source text; Tier 2: Morphological segmentation; Tier 3: Morpheme-by-morpheme grammatical gloss; Tier 4: Free idiomatic translation.", 100, "Correct. The Leipzig standard establishes these four vertical tiers to represent text from raw surface form down to morphemic analysis and free translation."),
          ("Tier 1: Latin; Tier 2: French; Tier 3: German; Tier 4: English.", 0, "Incorrect. The tiers represent linguistic analytical layers of a single text, not four arbitrary European languages."),
          ("Tier 1: Shelfmark; Tier 2: Scribe; Tier 3: Date; Tier 4: Provenance.", 0, "Incorrect. These are codicological cataloguing metadata fields, not interlinear glossing tiers."),
          ("Tier 1: Author; Tier 2: Publisher; Tier 3: ISBN; Tier 4: Price.", 0, "Incorrect. These are bibliographic publication metadata fields.")
      ]),
    ("02 Question: Leipzig Punctuation Conventions",
      "According to Rule 2 of the Leipzig Glossing Rules, what is the crucial distinction between a hyphen (`-`) and a period (`.`) in the grammatical gloss line?",
      [
          ("A hyphen indicates a distinct morpheme boundary clearly segmented in the text above, while a period connects multiple grammatical meanings expressed by a single indivisible morpheme (portmanteau).", 100, "Correct. Hyphens align with physical morpheme cuts, whereas periods separate multiple category labels (e.g. '1SG.PST') that correspond to a single fused segment."),
          ("A hyphen indicates an error by the scribe, while a period indicates a word that should be deleted.", 0, "Incorrect. Both marks are analytical tools for linguistic glossing, not scribal defect indicators."),
          ("A hyphen is used only for nouns, while a period is used only for verbs.", 0, "Incorrect. Leipzig punctuation applies universally across all grammatical parts of speech."),
          ("Hyphens are forbidden in digital editions because XML parsers cannot process them.", 0, "Incorrect. XML handles standard ASCII hyphens without issue.")
      ]),
    ("03 Question: TEI Stand-Off Linkage Architecture",
      "How does TEI P5 represent alignment between source and target text segments without physically mingling their XML trees?",
      [
          ("Using stand-off annotation with `<linkGrp>` containing `<link target=\"#srcID #tgtID\"/>` elements that pair IDs defined in separate `<text>` bodies.", 100, "Correct. Stand-off markup keeps each language's text hierarchy clean and autonomous, linking them via ID reference pairs inside <linkGrp>."),
          ("By pasting the English translation directly into the `<author>` tag of the `<teiHeader>`.", 0, "Incorrect. <author> records the author of the work, not parallel translations."),
          ("By converting both documents into a single unformatted plain text file with no XML tags.", 0, "Incorrect. Unformatted text destroys structural alignment and XML validity."),
          ("By writing both languages alternately, word by word, inside a single `<p>` tag.", 0, "Incorrect. Interleaving words inside a single paragraph corrupts the syntax and parsing of both languages.")
      ]),
    ("04 Question: Operational Heuristic of Gale-Church Alignment",
      "On what foundational heuristic does the classical Gale-Church sentence alignment algorithm operate?",
      [
          ("Sentence length correlation: across translated texts, corresponding sentences tend to have closely correlated lengths measured in character counts.", 100, "Correct. Gale and Church proved that sentence length correlation alone enables robust, language-independent dynamic programming alignment without needing bilingual lexicons."),
          ("Alphabetical sorting: all sentences are sorted alphabetically from A to Z before pairing.", 0, "Incorrect. Sorting alphabetically destroys narrative order and textual alignment."),
          ("Rhyme scheme: sentences are aligned based on whether their final syllables rhyme in both languages.", 0, "Incorrect. The algorithm evaluates character count probabilities, not poetic rhyme."),
          ("Parchment moisture: sentences are aligned based on the relative humidity of the manuscript room.", 0, "Incorrect. Physical conservation parameters have no bearing on computational text alignment.")
      ]),
    ("05 Question: Statistical Word Alignment with fast_align",
      "How do statistical word alignment tools like IBM Models and `fast_align` calculate word-level correspondences in parallel corpora?",
      [
          ("They use Expectation-Maximization (EM) algorithms and log-linear models to find the probability that a word in the source sentence generates a specific word in the target sentence across large corpora.", 100, "Correct. Statistical aligners optimize lexical translation probabilities and positional distortion parameters using EM over sentence-aligned bitexts."),
          ("They assign words randomly until the user stops the script.", 0, "Incorrect. Statistical alignment is a principled mathematical optimization process."),
          ("They look up every word in Google Translate via an active internet browser connection.", 0, "Incorrect. fast_align is a standalone mathematical model that trains directly on the input corpus."),
          ("They require the user to manually type every single pairing before running.", 0, "Incorrect. The purpose of statistical alignment is to automate lexical pairing across massive text collections.")
      ]),
    ("06 Question: The Non-Isomorphic Alignment Dilemma",
      "Why is word-for-word (1-to-1) alignment often impossible when translating ancient or highly inflected languages into modern English?",
      [
          ("Typological asymmetry (non-isomorphism): a single synthetic inflected word often corresponds to a multi-word analytic phrase in English (1-to-many), or an idiomatic phrase collapses into one word (many-to-1).", 100, "Correct. Languages differ in morphological synthesis; synthetic and polysynthetic words express concepts that analytic languages require auxiliary verbs and prepositions to convey."),
          ("Because English grammar forbids sentences from having more than four words.", 0, "Incorrect. English sentences can have arbitrary grammatical length."),
          ("Because ancient manuscripts never contained verbs.", 0, "Incorrect. Historical languages contain rich, complex verbal systems."),
          ("Because digital text editors automatically delete translation words that exceed eight letters.", 0, "Incorrect. Software imposes no such restriction.")
      ]),
    ("07 Question: Role of Ugarit and Alpheios in Historical Alignment",
      "What capability do specialized platforms like Ugarit and the Alpheios Alignment Editor offer for scholarly historical editing?",
      [
          ("They provide web-based interactive interfaces for creating, editing, and visualizing fine-grained word-level and phrase-level alignments between historical texts and translations.", 100, "Correct. Ugarit and Alpheios specialize in classical and historical language alignment, supporting token-level linking, multi-word units, and TEI/JSON export."),
          ("They automatically forge ancient manuscript provenance documents to increase sale value.", 0, "Incorrect. Digital humanities platforms promote academic integrity, not document forgery."),
          ("They are physical microfilm cameras used in library basements.", 0, "Incorrect. They are digital software web applications."),
          ("They encrypt text files to make them permanently unreadable by the public.", 0, "Incorrect. They produce open-access, readable parallel text representations.")
      ]),
    ("08 Question: AI Failure Modes in Interlinear Glossing",
      "When using an LLM to generate Leipzig glosses for an unfamiliar historical language, what is a frequent critical error?",
      [
          ("Morphological confabulation: inventing non-existent grammatical prefixes or suffixes and projecting modern English semantic categories onto ancient synthetic stems.", 100, "Correct. Without deep grounding in historical grammar, LLMs frequently hallucinate morpheme boundaries and invent grammatical category labels that do not exist in the language."),
          ("Formatting text using the UTF-8 character encoding.", 0, "Incorrect. UTF-8 is the global standard for digital text, not an error."),
          ("Responding in less than five seconds.", 0, "Incorrect. Rapid computation is a technical feature, not a philological defect."),
          ("Saving the output as an HTML or XML file.", 0, "Incorrect. Producing structured markup is standard practice.")
      ]),
    ("09 Question: Translating Cultural Realia in Parallel Editions",
      "How should an editor handle 'cultural realia' (untranslatable culture-specific terms, e.g. weights, legal ranks, ancient religious ceremonies) in a Leipzig glossed edition?",
      [
          ("Retain the transliterated term in the segmentation line and provide a specialized grammatical/cultural label in the gloss, supplemented by commentary notes rather than misleading generic modern equivalents.", 100, "Correct. Precise philological glossing avoids anachronistic modern substitutions by preserving the technical cultural term and explaining its specific semantic domain."),
          ("Replace every unfamiliar cultural term with a modern brand name.", 0, "Incorrect. Anachronistic commercial substitutions destroy historical scholarship."),
          ("Delete the word completely from the edition and pretend it was never written.", 0, "Incorrect. Editorial suppression of difficult terms violates scholarly integrity."),
          ("Declare that the ancient scribe was illiterate and rewrite the entire chapter.", 0, "Incorrect. Scholarly editing respects the historical witness.")
      ]),
    ("10 Question: Significance of Parallel Corpora for Digital Philology",
      "Why is rigorously aligned parallel text invaluable for computational humanities research?",
      [
          ("It provides structured training data for historical machine translation, enables cross-lingual semantic search, and powers interactive reading environments that scaffold novice language learning.", 100, "Correct. Aligned parallel corpora are the bedrock of multilingual NLP, computational lexicography, and accessible digital pedagogy for historical languages."),
          ("It allows universities to discard all historical paper manuscripts in recycling bins.", 0, "Incorrect. Digital representations complement, rather than replace, the physical preservation of cultural heritage."),
          ("It proves that all languages throughout human history originated from Python code.", 0, "Incorrect. Human natural languages evolved biologically and culturally millennia before computer programming languages."),
          ("It makes all historical texts exactly identical in length and vocabulary.", 0, "Incorrect. Parallel alignment preserves the distinctive linguistic properties of each language.")
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

print("Module 11 Phase F Assembly successfully completed!")
