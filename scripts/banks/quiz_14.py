import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

shared_dir = Path(__file__).resolve().parents[3] / "shared" / "scripts"
sys.path.insert(0, str(shared_dir))
from question_bank import Q

src_mod = Path("src/modules/Module_14_Collation")
dist_mod = Path("dist/moodle/Module_14_Collation")
src_mod.mkdir(parents=True, exist_ok=True)
dist_mod.mkdir(parents=True, exist_ok=True)

# 1. Banner Image (1200x300)
def create_banner():
    w, h = 1200, 300
    img = Image.new("RGB", (w, h), color="#1e1b4b")  # deep midnight indigo / navy
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, w-10, h-10], outline="#c29b38", width=2)
    draw.rectangle([16, 16, w-16, h-16], outline="#312e81", width=1)
    draw.rectangle([20, 20, 35, h-20], fill="#e11d48")  # vibrant crimson / variant accent
    
    try:
        font_course = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font_course = font_title = font_sub = ImageFont.load_default()
        
    draw.text((60, 45), "RELS 398 / ENGL 398  •  DIGITAL METHODS FOR HISTORICAL DOCUMENTS", fill="#c29b38", font=font_course)
    draw.text((60, 100), "Module 14: Automated Textual Collation", fill="#f8fafc", font=font_title)
    draw.text((60, 175), "Sequence Alignment  •  CollateX Engine  •  Variant Graphs & Stemmatology", fill="#cbd5e1", font=font_sub)
    draw.line([60, 225, w-60, 225], fill="#c29b38", width=1)
    draw.text((60, 245), "StFX Department of Religious Studies  •  Computational Philology Pipeline", fill="#94a3b8", font=font_sub)
    
    for p in [dist_mod / "01_Banner.png", src_mod / "01_Banner.png"]:
        img.save(p, "PNG")
        print(f"Wrote banner: {p}")

create_banner()

# 2. Learning Objectives
obj_html = """<div class="card p-3 mb-3 border-info" style="border-left: 5px solid #e11d48; background-color: #fff1f2; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #9f1239; margin-top: 0;">Module 14: Automated Textual Collation — Learning Objectives</h4>
    <p>By the end of this module, students will be able to:</p>
    <ul>
        <li><strong>Classify</strong> textual divergence into the four canonical variant categories: substitution, addition, omission, and transposition.</li>
        <li><strong>Execute</strong> a manual two-witness collation against a base text to establish baseline editorial competencies.</li>
        <li><strong>Configure and run</strong> the CollateX Python library using dynamic programming alignment algorithms (Gotoh) and customized tokenizers.</li>
        <li><strong>Interpret</strong> directed acyclic variant graphs and export alignment matrices into TEI XML parallel segmentation encoding.</li>
        <li><strong>Evaluate</strong> AI-assisted variant classification models to identify conjunctive errors without conflating stemmatic evidence with convergent scribal slips.</li>
    </ul>
</div>"""

# 3. Readings
reading_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #c29b38; background-color: #fcfcfd; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c29b38; margin-top: 0;">Assigned Readings & Foundational Scholarship</h4>
    <p>Please study the following key literature on collation theory, algorithmic alignment, and stemmatic criticism:</p>
    <ul>
        <li><strong>Haentjens Dekker, Ronald, Dirk van Hulle, Gregor Middell, Vincent Neyt, and Joris van Zundert.</strong> "Computer-Supported Collation of Modern Manuscripts: CollateX and the Beckett Digital Manuscript Project." <em>Digital Scholarship in the Humanities</em>, 30(3), 2015, pp. 452–470.</li>
        <li><strong>Griffitts, Troy.</strong> "Digital Editing of Biblical Texts." <em>Manuscript Cultures: Mapping Textual Landscapes</em>, § 4.6.2–3 (Collation Algorithms) and § 4.7 (Stemmatic Alignment).</li>
        <li><strong>Robinson, Peter.</strong> "Collation and Textual Criticism." <em>A Companion to Digital Literary Studies</em>, ed. R. Siemens and S. Schreibman, Blackwell, 2007.</li>
    </ul>
</div>"""

# 4. Watch List
watch_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #e11d48; background-color: #fff1f2; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #9f1239; margin-top: 0;">Curated Media & Technical Walkthroughs</h4>
    <p>Review these video demonstrations before completing your workshop assignment:</p>
    <ul>
        <li><strong>The Foundations of Collation:</strong> How textual critics compare witnesses to uncover stemmatic descent (19 mins).</li>
        <li><strong>Automated Collation in Python with CollateX:</strong> Tokenization, alignment parameters, and generating SVG variant graphs (24 mins).</li>
        <li><strong>Handling Transpositions and Complex Variants:</strong> Why word-order shifts challenge linear alignment algorithms (18 mins).</li>
    </ul>
</div>"""

# 5. Workshop
ws_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #e11d48; background-color: #fff1f2; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #9f1239; margin-top: 0;">Workshop: Automated Collation and Alignment with CollateX</h4>
    <p><strong>Overview:</strong> In this workshop, you will collate your primary witness transcription against a peer's witness and an authoritative base text using both manual visual inspection and the programmatic CollateX engine in Python. You will inspect the resulting variant graph, adjudicate discrepancies, and export an aligned TEI apparatus block.</p>
    <p><strong>Deadlines:</strong> Comparison Post due Friday by 11:00 PM; Peer Reviews due Monday by 11:00 PM.</p>
</div>"""

ws_sub = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Submission Instructions</h4>
    <ol>
        <li>Prepare plain text files for three witnesses: Witness A (your adopted manuscript passage), Witness B (your partner's manuscript passage), and Base (an authoritative reference or critical edition text).</li>
        <li><strong>Manual Collation:</strong> Create a table in Markdown manually recording all differences between Witness A and the Base text.</li>
        <li><strong>CollateX Script:</strong> Run a Python script using <code>collatex</code> to collate all three witnesses, outputting an alignment table and an SVG/HTML variant graph.</li>
        <li>Inspect the CollateX output: identify any alignment missteps (e.g. transpositions treated as deletion+addition).</li>
        <li>Submit your Python script, CollateX output, and a <strong>300–500 word analysis</strong> explaining how the variant graph structure reveals scribal habits and potential shared errors between the witnesses.</li>
    </ol>
</div>"""

ws_assess = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Peer Assessment Rubric</h4>
    <ul>
        <li><strong>CollateX Pipeline Execution (4 pts):</strong> The submission successfully runs CollateX, producing an accurate alignment table across all three input witnesses without tokenization crashes.</li>
        <li><strong>Alignment Evaluation & Diagnostics (3 pts):</strong> The author astutely diagnoses how the algorithm resolved complex spots (such as transpositions or lacunae) and notes any needed editorial overrides.</li>
        <li><strong>Stemmatic Reflection (3 pts):</strong> The 300–500 word report demonstrates a mature understanding of variant taxonomy, clearly separating substantive genealogical errors from trivial orthographic noise.</li>
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
    (mod_p / "09_Quiz_Description.html").write_text("<p>Comprehensive weekly knowledge check covering collation algorithms, CollateX configuration, variant graph topology, and stemmatic variant taxonomy.</p>", encoding="utf-8")

print("Wrote HTML and Banner files.")

# 7. Build Weekly Quiz (10 Questions)
questions = [
    ("01 Question: Four Canonical Classes of Textual Variation",
      "Which four fundamental categories encompass all textual divergences identified during manuscript collation?",
      [
          ("Substitution, addition, omission, and transposition.", 100, "Correct. Textual criticism classifies all textual variance into substitutions (replacements), additions (insertions), omissions (deletions), and transpositions (word-order inversions)."),
          ("Compression, encryption, decryption, and decompression.", 0, "Incorrect. These are computer science data transmission terms, not philological variant categories."),
          ("Paleography, codicology, epigraphy, and papyrology.", 0, "Incorrect. These are auxiliary historical disciplines, not textual variant classes."),
          ("Parchment, papyrus, paper, and vellum.", 0, "Incorrect. These are physical manuscript writing materials.")
      ]),
    ("02 Question: Role of the Base Text in Collation",
      "Why is a 'base text' (or *textus collatus*) conventionally chosen when conducting textual collation?",
      [
          ("It provides a constant reference point against which all witness divergences and coordinates can be systematically recorded and indexed.", 100, "Correct. A base text serves as a stable coordinate system and comparison standard, even if the editor does not believe it represents the original text."),
          ("Because the base text is legally required to be the oldest manuscript surviving in the world.", 0, "Incorrect. Base texts are chosen for editorial convenience or accessibility, not necessarily age."),
          ("To ensure that no other manuscripts are allowed to disagree with it.", 0, "Incorrect. The entire point of collation is to discover and record where witnesses disagree with the base text."),
          ("Because computer algorithms cannot function without declaring one manuscript as divine truth.", 0, "Incorrect. Algorithmic collation is neutral; the base text merely anchors string alignment.")
      ]),
    ("03 Question: Needleman-Wunsch and Gotoh Algorithms",
      "How do biological sequence alignment algorithms like Needleman-Wunsch and Gotoh apply to automated textual collation?",
      [
          ("They use dynamic programming matrix calculation to find the optimal global alignment of character or token sequences while penalizing gaps and mismatches.", 100, "Correct. Needleman-Wunsch and Gotoh compute optimal alignments between textual strings by minimizing cost functions for insertions, deletions, and substitutions."),
          ("They automatically reconstruct the exact handwriting speed of the ancient scribe.", 0, "Incorrect. Alignment algorithms evaluate string distances, not scribal physical biomechanics."),
          ("They convert Greek and Latin words into DNA nucleotide base pairs (A, C, G, T) to test biological tissue origin.", 0, "Incorrect. Although originally developed for bioinformatics, textual critics apply the mathematical logic of the algorithms to linguistic tokens."),
          ("They force all sentences in different languages to have the identical number of words.", 0, "Incorrect. Alignment algorithms allow gaps (insertions/deletions) to accommodate differing sentence lengths.")
      ]),
    ("04 Question: Tokenization in CollateX",
      "Why is the choice of tokenization method critical when feeding witness transcriptions into the CollateX engine?",
      [
          ("Word-level tokenization aligns substantive lexical units, whereas character-level tokenization aligns individual letters and can obscure word-boundary shifts.", 100, "Correct. Tokenization determines the atomic unit of comparison: word-level matches semantic units, while character-level catches intra-word spelling variations."),
          ("CollateX cannot process text unless every single word is exactly five letters long.", 0, "Incorrect. CollateX handles arbitrary token lengths seamlessly."),
          ("Tokenization is only required if the input files are saved as binary executable files.", 0, "Incorrect. Tokenization is the essential first step of parsing plain text into a sequence of linguistic symbols."),
          ("Character-level tokenization deletes all vowels automatically from the source text.", 0, "Incorrect. Character tokenization preserves all characters while breaking them into discrete sequence elements.")
      ]),
    ("05 Question: Topology of a Variant Graph",
      "In CollateX, how is a textual tradition visually and topologically represented?",
      [
          ("As a Directed Acyclic Graph (DAG) where nodes represent tokens and edges represent the sequential paths taken by different manuscript witnesses.", 100, "Correct. A variant graph models textual variation as a DAG: shared readings converge on single nodes, while variant readings branch into parallel paths before rejoining."),
          ("As a concentric circular pie chart showing the weight of parchment.", 0, "Incorrect. Variant graphs are topological network graphs, not pie charts."),
          ("As a 3D polygonal terrain map indicating elevation changes.", 0, "Incorrect. CollateX outputs directed graphs and tables, not topographical maps."),
          ("As an unlinked scatterplot where words are placed randomly across a coordinate grid.", 0, "Incorrect. Nodes in a variant graph are strictly connected by directional sequence edges representing witness readings.")
      ]),
    ("06 Question: TEI Parallel Segmentation Encoding",
      "Which TEI element structure correctly represents a point of textual variation among multiple manuscript witnesses in a parallel segmentation apparatus?",
      [
          ("<app><lem wit=\"#witA\">reading_A</lem><rdg wit=\"#witB\">reading_B</rdg></app>", 100, "Correct. In TEI parallel segmentation, <app> encloses the variant location, with <lem> holding the base/preferred lemma and <rdg> holding variant witness readings."),
          ("<choice><sic>reading_A</sic><corr>reading_B</corr></choice>", 0, "Incorrect. <sic> and <corr> represent scribal errors and editorial corrections in a single witness, not collation variants across multiple witnesses."),
          ("<subst><del>reading_A</del><add>reading_B</add></subst>", 0, "Incorrect. <subst> represents physical alterations on a single manuscript folio."),
          ("<milestone unit=\"variant\"/>reading_A//reading_B", 0, "Incorrect. Milestones are empty boundary markers, not container elements for critical apparatus data.")
      ]),
    ("07 Question: Transposition Challenge in Linear Alignment",
      "Why do standard dynamic programming collation algorithms struggle when two witnesses exhibit a word-order transposition (e.g. 'Christ Jesus' vs 'Jesus Christ')?",
      [
          ("Because linear alignment algorithms assume monotonic sequence progression and typically interpret a transposition as an omission in one place coupled with an addition elsewhere.", 100, "Correct. Dynamic programming optimizes monotonic sequence alignment; recognizing that a displaced word is the same lexical item moved across another requires non-linear transposition detection heuristics."),
          ("Because XML schemas forbid the rearrangement of words under any circumstances.", 0, "Incorrect. XML schemas validate markup structure, not textual word order."),
          ("Because the algorithm automatically deletes both words to resolve the paradox.", 0, "Incorrect. CollateX does not delete data; it represents it as an alignment gap or parallel branch."),
          ("Because transpositions only exist in modern printed novels, never in handwritten manuscripts.", 0, "Incorrect. Transposition (metathesis) is one of the most common scribal phenomena in manuscript traditions.")
      ]),
    ("08 Question: Stemmatic Value of Conjunctive Errors",
      "In classical Lachmannian stemmatology, what is a 'conjunctive error' (*error coniunctivus*) and why is it essential?",
      [
          ("A shared distinctive error that is so improbable to have occurred independently by coincidence that it proves the witnesses sharing it descend from a common ancestor.", 100, "Correct. Conjunctive errors establish genealogical kinship between witnesses because two independent scribes would not spontaneously commit the identical idiosyncratic mistake."),
          ("A spelling error in a conjunction such as 'and' or 'but'.", 0, "Incorrect. Conjunctive errors refer to genealogical connection (*coniungere*), not parts of speech."),
          ("A syntax error caused by connecting an external hard drive during collation.", 0, "Incorrect. Conjunctive error is a fundamental philological concept in textual stemmatics."),
          ("An error that occurs when two lines of text physically overlap on a palimpsest.", 0, "Incorrect. That is a codicological/optical phenomenon, not a genealogical conjunctive error.")
      ]),
    ("09 Question: Semantic vs Orthographic Variation in AI Auditing",
      "When using an LLM to categorize variant readings extracted by CollateX, what critical boundary must the prompt instruct the model to observe?",
      [
          ("The model must strictly separate orthographic/phonetic variants from substantive semantic variants that affect syntax, lexicon, or theological/historical interpretation.", 100, "Correct. LLMs must be explicitly constrained to distinguish superficial phonetic noise from substantive readings that carry stemmatic and semantic weight."),
          ("The model must rewrite all variants in modern French.", 0, "Incorrect. Historical collation must preserve the original languages of the witnesses."),
          ("The model must assume that the witness with the best handwriting is automatically the author's original.", 0, "Incorrect. Calligraphic elegance does not correlate with textual authenticity."),
          ("The model must discard any variant that contains more than two syllables.", 0, "Incorrect. Syllable count is irrelevant to variant validity.")
      ]),
    ("10 Question: Human-in-the-Loop Editorial Adjudication",
      "Why can automated tools like CollateX never fully replace the human scholarly editor in establishing a critical text?",
      [
          ("Because software can align strings and calculate mathematical edit distances, but only human scholars can evaluate paleographical plausibility, scribal psychology, dialectal nuance, and historical context.", 100, "Correct. Computational collation automates the mechanical identification of divergence; the critical evaluation of causes and the establishment of the text remains an interpretive scholarly act."),
          ("Because computer processors cannot store non-English alphabets in their internal memory.", 0, "Incorrect. Unicode enables modern computers to handle virtually all historical scripts."),
          ("Because publishing houses refuse to print books unless every single word was typed without software assistance.", 0, "Incorrect. Academic publishers actively embrace digital scholarly methods."),
          ("Because collation algorithms always crash if more than three manuscripts are compared at once.", 0, "Incorrect. CollateX routinely collates dozens of manuscript witnesses simultaneously.")
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

print("Module 14 Phase F Assembly successfully completed!")
