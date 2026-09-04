import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

shared_dir = Path(__file__).resolve().parents[3] / "shared" / "scripts"
sys.path.insert(0, str(shared_dir))
from question_bank import Q

src_mod = Path("src/modules/Module_06_Normalization")
dist_mod = Path("dist/moodle/Module_06_Normalization")
src_mod.mkdir(parents=True, exist_ok=True)
dist_mod.mkdir(parents=True, exist_ok=True)

# 1. Banner Image (1200x300)
def create_banner():
    w, h = 1200, 300
    img = Image.new("RGB", (w, h), color="#0f172a")  # deep lapis slate
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, w-10, h-10], outline="#c29b38", width=2)
    draw.rectangle([16, 16, w-16, h-16], outline="#334155", width=1)
    draw.rectangle([20, 20, 35, h-20], fill="#38bdf8")  # vibrant cyan/lapis accent
    
    try:
        font_course = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font_course = font_title = font_sub = ImageFont.load_default()
        
    draw.text((60, 45), "RELS 398 / ENGL 398  •  DIGITAL METHODS FOR HISTORICAL DOCUMENTS", fill="#c29b38", font=font_course)
    draw.text((60, 100), "Module 06: Orthographic Normalization", fill="#f8fafc", font=font_title)
    draw.text((60, 175), "Historical Variation  •  TEI orig/reg Markup  •  Deterministic & Neural Rules", fill="#94a3b8", font=font_sub)
    draw.line([60, 225, w-60, 225], fill="#c29b38", width=1)
    draw.text((60, 245), "StFX Department of Religious Studies  •  Computational Philology Pipeline", fill="#64748b", font=font_sub)
    
    for p in [dist_mod / "01_Banner.png", src_mod / "01_Banner.png"]:
        img.save(p, "PNG")
        print(f"Wrote banner: {p}")

create_banner()

# 2. Learning Objectives
obj_html = """<div class="card p-3 mb-3 border-info" style="border-left: 5px solid #0284c7; background-color: #f0f9ff; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #0369a1; margin-top: 0;">Module 06: Orthographic Normalization — Learning Objectives</h4>
    <p>By the end of this module, students will be able to:</p>
    <ul>
        <li><strong>Distinguish</strong> between meaningful textual variation and phonological or orthographic drift (such as Greek iotacism, vowel mergers, and early modern English spelling fluidity).</li>
        <li><strong>Encode</strong> diplomatic readings and normalized editorial regularizations using TEI <code>&lt;choice&gt;</code>, <code>&lt;orig&gt;</code>, and <code>&lt;reg&gt;</code> markup.</li>
        <li><strong>Construct and execute</strong> a deterministic Python script utilizing regular expressions (<code>re.sub</code>) to automate rule-based orthographic normalization.</li>
        <li><strong>Audit</strong> AI-generated normalization outputs against a manual ground truth to identify and mitigate the risks of "hypercorrection" and erasure of dialectal evidence.</li>
    </ul>
</div>"""

# 3. Readings
reading_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #c29b38; background-color: #fcfcfd; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c29b38; margin-top: 0;">Assigned Readings & Foundational Scholarship</h4>
    <p>Please study the following chapters and methodological frameworks on primary source representation and variant taxonomy:</p>
    <ul>
        <li><strong>TEI Consortium.</strong> "Chapter 11: Representation of Primary Sources." <em>TEI P5: Guidelines for Electronic Text Encoding and Interchange</em>, Version 4.8.0, 2024. Focus on § 11.3.1.2 (Alteration) and § 11.3.1.4 (Regularization).</li>
        <li><strong>Griffitts, Troy.</strong> "Digital Editing of Biblical Texts." <em>Manuscript Cultures: Mapping Textual Landscapes</em>, § 4.6.1 (Orthographic Regularization and Collation Baselines).</li>
        <li><strong>Sabel, Helena.</strong> "The Encoding of Variant Taxonomies in TEI: Distinguishing Error from Linguistic Diversity." <em>Journal of the Text Encoding Initiative</em>, Issue 12, 2019.</li>
    </ul>
</div>"""

# 4. Watch List
watch_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #0284c7; background-color: #f0f9ff; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #0369a1; margin-top: 0;">Curated Media & Technical Walkthroughs</h4>
    <p>Review these video demonstrations before completing your workshop assignment:</p>
    <ul>
        <li><strong>Phonetic Drift & Scribes:</strong> Understanding iotacism, vowel shifts, and historical orthography across handwritten codices (17 mins).</li>
        <li><strong>Automating Normalization with Python Regex:</strong> Writing safe <code>re.sub</code> patterns with word boundaries and capture groups in VS Code (22 mins).</li>
        <li><strong>The Peril of Hypercorrection:</strong> How commercial LLMs inadvertently erase scribal dialects and premodern regional idiolects (19 mins).</li>
    </ul>
</div>"""

# 5. Workshop
ws_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #0284c7; background-color: #f0f9ff; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #0369a1; margin-top: 0;">Workshop: Comparative Orthographic Normalization (Manual vs. Script vs. LLM)</h4>
    <p><strong>Overview:</strong> In this workshop, you will apply three successive normalization methods to a 20-line passage of your primary manuscript witness. You will compare manual TEI <code>&lt;choice&gt;&lt;orig&gt;...&lt;reg&gt;...&lt;/choice&gt;</code> encoding against a deterministic Python regex script and a prompt-engineered LLM normalization, documenting every disagreement and evaluating hypercorrection errors.</p>
    <p><strong>Deadlines:</strong> Comparison Post due Friday by 11:00 PM; Peer Reviews due Monday by 11:00 PM.</p>
</div>"""

ws_sub = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Submission Instructions</h4>
    <ol>
        <li>Select a 20-line excerpt from your consensus diplomatic transcription.</li>
        <li><strong>Step 1 (Manual):</strong> Hand-encode all orthographic variations using TEI <code>&lt;choice&gt;&lt;orig&gt;diplomatic&lt;/orig&gt;&lt;reg resp="#editor"&gt;normalized&lt;/reg&gt;&lt;/choice&gt;</code>, documenting your explicit regularization rules.</li>
        <li><strong>Step 2 (Script):</strong> Write a small Python script (<code>normalize.py</code>) using <code>re.sub()</code> rules that automatically applies your orthographic rules to the raw text.</li>
        <li><strong>Step 3 (AI):</strong> Pass the raw diplomatic text to an LLM (via VS Code or local CLI) with a system prompt instructing it to normalize orthography while preserving morphological syntax.</li>
        <li>Submit your TEI XML file, your Python script, and a <strong>300–500 word comparative reflection</strong> evaluating the false positive and hypercorrection rate of the automated passes against your manual baseline.</li>
    </ol>
</div>"""

ws_assess = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Peer Assessment Rubric</h4>
    <ul>
        <li><strong>TEI Choice Markup Validity (4 pts):</strong> The <code>&lt;choice&gt;</code> elements correctly enclose paired <code>&lt;orig&gt;</code> and <code>&lt;reg&gt;</code> children without syntax errors or broken tags.</li>
        <li><strong>Deterministic Rule Precision (3 pts):</strong> The Python script uses appropriate regex boundaries to avoid corrupting substrings inside unrelated words.</li>
        <li><strong>Comparative Critical Analysis (3 pts):</strong> The reflection articulates a clear philological rationale distinguishing legitimate dialectal variants from mechanical spelling slips, identifying specific instances of AI hypercorrection.</li>
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
    (mod_p / "09_Quiz_Description.html").write_text("<p>Comprehensive weekly knowledge check covering orthographic variation, TEI orig/reg encoding, regex normalization, and AI hypercorrection auditing.</p>", encoding="utf-8")

print("Wrote HTML and Banner files.")

# 7. Build Weekly Quiz (10 Questions)
questions = [
    ("01 Question: Phonological Drift vs Substantive Variant",
      "What is the essential philological difference between an orthographic variant and a substantive textual variant?",
      [
          ("Orthographic variants represent superficial phonetic or spelling differences that do not alter lexical identity or grammatical meaning, whereas substantive variants involve different words, omissions, additions, or major grammatical shifts.", 100, "Correct. Orthographic variation reflects phonetic spelling or scribal habit without altering the semantic or lexical identity of the text."),
          ("Orthographic variants only occur in printed editions, whereas substantive variants are restricted to handwritten manuscripts.", 0, "Incorrect. Orthographic variation is ubiquitous across handwritten manuscript traditions."),
          ("Orthographic variants must always be corrected silently without recording the manuscript's original spelling.", 0, "Incorrect. Scholarly digital editions preserve the manuscript witness in <orig> or diplomatic layers."),
          ("Substantive variants are caused exclusively by physical damage to the parchment, whereas orthographic variants are caused by ink bleeding.", 0, "Incorrect. Substantive variants involve intentional or accidental linguistic changes by scribes, not merely physical parchment lacunae.")
      ]),
    ("02 Question: TEI Choice Container Mechanism",
      "In TEI P5 XML, how should an editor encode a manuscript word that exhibits historical spelling variation alongside a modern normalized form?",
      [
          ("<choice><orig>diplomatic_form</orig><reg>normalized_form</reg></choice>", 100, "Correct. The <choice> element groups alternative encodings, with <orig> preserving the diplomatic manuscript witness and <reg> providing the regularized editorial form."),
          ("<subst><del>diplomatic_form</del><add>normalized_form</add></subst>", 0, "Incorrect. <subst> with <del> and <add> is reserved for physical scribal alterations on the manuscript page itself, not editorial regularization."),
          ("<abbr>diplomatic_form<expan>normalized_form</expan></abbr>", 0, "Incorrect. <abbr> and <expan> are used specifically for expanding scribal abbreviations, not for general orthographic regularization."),
          ("<choice><sic>diplomatic_form</sic><corr>normalized_form</corr></choice>", 0, "Incorrect. <sic> and <corr> indicate an overt scribal error, whereas orthographic variation is a recognized historical spelling rather than an error.")
      ]),
    ("03 Question: Historical Phenomenon of Iotacism",
      "What historical linguistic phenomenon is termed 'iotacism' in premodern and Hellenistic/Byzantine Greek manuscripts?",
      [
          ("The phonological convergence of several distinct vowels and diphthongs (such as ι, η, υ, ει, οι, υι) to the single vowel sound /i/, causing scribes to spell words phonetically.", 100, "Correct. Iotacism describes the phonetic merger of multiple front vowels and diphthongs into /i/, leading to widespread scribal interchange in spelling."),
          ("The scribal practice of dropping the initial letter iota at the beginning of poetic verses.", 0, "Incorrect. Iotacism refers to vowel pronunciation convergence, not the omission of verse-initial letters."),
          ("The systematic insertion of iota subscripts beneath capital uncial letters in ninth-century book hands.", 0, "Incorrect. That relates to adscript/subscript history, not the phonetic phenomenon of iotacism."),
          ("A machine learning classification error where a vision model mistakes the letter iota for a vertical stroke delimiter.", 0, "Incorrect. Iotacism is a well-known historical phonological development in the Greek language.")
      ]),
    ("04 Question: Early Modern English Orthographic Fluidity",
      "Which of the following describes a standard orthographic convention in early modern English handwritten documents?",
      [
          ("Positional interchange of 'u' and 'v' (where 'v' often appeared initially and 'u' medially) and 'i' and 'j', regardless of vowel or consonant status.", 100, "Correct. In pre-17th-century English writing, 'v' was standard initially (e.g. 'vnder') and 'u' medially (e.g. 'haue')."),
          ("Strict adherence to 18th-century Samuel Johnson dictionary spellings across all personal letters.", 0, "Incorrect. Standardized dictionary orthography was not established until centuries later."),
          ("Mandatory hyphenation between every syllable in legal petitions.", 0, "Incorrect. Premodern legal scribes did not systematically hyphenate syllables."),
          ("The universal omission of all terminal silent '-e' letters in 16th-century court hands.", 0, "Incorrect. Terminal '-e' was exceptionally common and fluid in early modern orthography.")
      ]),
    ("05 Question: Pitfalls of Global Regex Normalization",
      "Why is executing a naive global string replacement like `s/vn/un/g` in a normalization script hazardous in historical texts?",
      [
          ("Without word-boundary delimiters (`\\b`), it will corrupt unrelated words containing that character sequence in both source and target contexts.", 100, "Correct. Regex replacement without word boundaries (`\\b`) will unintentionally modify substrings inside larger words."),
          ("Python's `re` module cannot process text encodings other than 7-bit ASCII.", 0, "Incorrect. Python 3's `re` module natively supports full Unicode strings."),
          ("XML parsers treat regular expressions as dangerous security exploits and refuse to open the document.", 0, "Incorrect. XML parsers process static text content and do not evaluate external regex scripts."),
          ("Global regex substitution permanently deletes the git commit history of the repository.", 0, "Incorrect. Regex scripts only alter the working directory files until committed.")
      ]),
    ("06 Question: AI Hypercorrection and Dialectal Erasure",
      "What is the danger of using an unconstrained commercial LLM to 'clean up the spelling' of a premodern manuscript transcription?",
      [
          ("The model tends to 'hypercorrect' authentic regional dialectal features and historical phonological spellings, erasing crucial linguistic and provenance evidence.", 100, "Correct. LLMs trained on modern standardized text tend to aggressively modernize idiosyncratic scribal spellings, destroying historical dialect data."),
          ("The LLM will automatically convert the text into binary machine code.", 0, "Incorrect. LLMs output natural language text, not machine code."),
          ("The LLM will delete all vowels from the document due to tokenization compression.", 0, "Incorrect. Tokenization preserves standard characters and words."),
          ("The model will notify copyright authorities that the historical text is unauthorized.", 0, "Incorrect. Historical manuscript texts are public domain and do not trigger copyright notifications.")
      ]),
    ("07 Question: Preserving Manuscript Transparency",
      "Why do scholarly digital editions prioritize storing both diplomatic and regularized forms rather than replacing the text outright?",
      [
          ("To ensure verifiable reproducibility, allowing readers and computational tools to toggle between the physical artifact's actual writing and a normalized reading view.", 100, "Correct. Digital editions maintain epistemological integrity by keeping the exact manuscript witness alongside interpretive editorial normalizations."),
          ("Because TEI schemas throw a fatal error whenever an XML document contains fewer than two distinct spellings per sentence.", 0, "Incorrect. TEI schemas enforce structural hierarchy and attributes, not an arbitrary word count rule."),
          ("To double the file size in order to meet grant funding storage quotas.", 0, "Incorrect. Academic editions prioritize scholarly rigor and verifiability, not artificial file inflation."),
          ("Because web browsers cannot render historical alphabets unless accompanied by modern translations.", 0, "Incorrect. Web browsers render historical Unicode characters perfectly well with proper font support.")
      ]),
    ("08 Question: Normalization as a Collation Baseline",
      "What vital role does orthographic normalization play prior to automated computer-assisted collation across multiple witnesses?",
      [
          ("It prevents trivial spelling variations from generating thousands of false-positive variant readings, allowing collators to focus on substantive textual divergences.", 100, "Correct. Normalization creates a clean linguistic baseline so automated collation algorithms highlight substantive variants rather than orthographic noise."),
          ("It reorders the manuscript witnesses according to their physical parchment thickness.", 0, "Incorrect. Collation compares textual sequences, not physical leaf thickness."),
          ("It eliminates the need for human editors to ever consult the original manuscripts.", 0, "Incorrect. High-resolution facsimiles and physical codices must always be consulted to verify substantive cruxes."),
          ("It forces all historical manuscripts into exact chronological order based on vowel counts.", 0, "Incorrect. Normalization aligns spelling, not chronological dating.")
      ]),
    ("09 Question: Safe Regex Pattern Architecture",
      "Which Python regular expression pattern correctly identifies the archaic initial 'v' representing a vowel (e.g. 'vnder', 'vnto') at the start of a word while preserving trailing letters?",
      [
          (r"\b[vV]([a-z]+)\b", 100, "Correct. The pattern uses word boundaries `\\b` and captures subsequent letters in group 1, allowing safe replacement with `u\\1` or `U\\1`."),
          (r".*v.*", 0, "Incorrect. `.*v.*` matches any line containing the letter 'v' anywhere in the line."),
          (r"[vV]", 0, "Incorrect. A bare character set without word boundaries matches every 'v' inside any word (e.g. 'every', 'have')."),
          (r"^v$", 0, "Incorrect. `^v$` only matches a line containing a single isolated letter 'v'.")
      ]),
    ("10 Question: Quality Auditing of Normalization Passes",
      "In the three-step comparative cycle (manual -> deterministic -> AI-assisted), how does an editor verify the reliability of an automated normalization pipeline?",
      [
          ("By calculating precision, recall, and error rate of the automated passes against the hand-encoded manual ground-truth sample.", 100, "Correct. Quantitative evaluation against a curated manual ground truth reveals both missed normalizations (false negatives) and over-regularizations (false positives)."),
          ("By assuming that if the script completes without an exception, 100% of the words were normalized correctly.", 0, "Incorrect. A script can run to completion while corrupting data or missing edge cases."),
          ("By relying solely on the LLM's self-generated claim that its output is perfectly accurate.", 0, "Incorrect. Generative AI models cannot objectively audit their own hallucination rates."),
          ("By discarding all original files and keeping only the final AI output.", 0, "Incorrect. That violates basic digital scholarship and data preservation principles.")
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

print("Module 06 Phase F Assembly successfully completed!")
