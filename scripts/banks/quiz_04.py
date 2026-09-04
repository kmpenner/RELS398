import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

shared_dir = Path(__file__).resolve().parents[3] / "shared" / "scripts"
sys.path.insert(0, str(shared_dir))
from question_bank import Q

src_mod = Path("src/modules/Module_04_Transcription")
dist_mod = Path("dist/moodle/Module_04_Transcription")
src_mod.mkdir(parents=True, exist_ok=True)
dist_mod.mkdir(parents=True, exist_ok=True)

# 1. Banner Image (1200x300)
def create_banner():
    w, h = 1200, 300
    img = Image.new("RGB", (w, h), color="#1e293b")  # slate / dark charcoal
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, w-10, h-10], outline="#c29b38", width=2)
    draw.rectangle([16, 16, w-16, h-16], outline="#334155", width=1)
    draw.rectangle([20, 20, 35, h-20], fill="#0284c7")  # vibrant cyan / digital ink accent
    
    try:
        font_course = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font_course = font_title = font_sub = ImageFont.load_default()
        
    draw.text((60, 45), "RELS 398 / ENGL 398  •  DIGITAL METHODS FOR HISTORICAL DOCUMENTS", fill="#c29b38", font=font_course)
    draw.text((60, 100), "Module 04: Diplomatic Transcription & HTR", fill="#f8fafc", font=font_title)
    draw.text((60, 175), "Palaeographical Ground Truth  •  Transkribus PyLaia Models  •  CER & VLM Auditing", fill="#cbd5e1", font=font_sub)
    draw.line([60, 225, w-60, 225], fill="#c29b38", width=1)
    draw.text((60, 245), "StFX Department of Religious Studies  •  Computational Philology Pipeline", fill="#94a3b8", font=font_sub)
    
    for p in [dist_mod / "01_Banner.png", src_mod / "01_Banner.png"]:
        img.save(p, "PNG")
        print(f"Wrote banner: {p}")

create_banner()

# 2. Learning Objectives
obj_html = """<div class="card p-3 mb-3 border-info" style="border-left: 5px solid #002D62; background-color: #f8fafc; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #002D62; margin-top: 0;">Module 04: Transcription & Palaeography — Learning Objectives</h4>
    <p>By the end of this module, students will be able to:</p>
    <ul>
        <li><strong>Differentiate</strong> diplomatic (graphemically faithful) from normalized editorial transcription and apply standard editorial conventions to damaged surfaces.</li>
        <li><strong>Transcribe</strong> a full manuscript folio by hand in plain text to establish an authoritative ground-truth reference for downstream evaluation.</li>
        <li><strong>Configure and train</strong> Handwritten Text Recognition (HTR) baseline and character models using Transkribus, identifying bounding polygons, baselines, and line-order hierarchies.</li>
        <li><strong>Benchmark and audit</strong> Vision-Language Models (VLMs) and LLM-assisted transcription outputs against manual ground truth, quantifying Character Error Rate (CER) and diagnosing hallucination modes.</li>
    </ul>
</div>"""

# 3. Readings
reading_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #c29b38; background-color: #fcfcfd; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c29b38; margin-top: 0;">Assigned Readings & Foundational Scholarship</h4>
    <p>Please study the following research papers on paleography, HTR, and transcription evaluation:</p>
    <ul>
        <li><strong>AlKendi, Mohamed, et al.</strong> "Benchmarking Vision-Language Models for Handwritten Text Recognition in Historical Documents." <em>Digital Scholarship in the Humanities</em>, 2024.</li>
        <li><strong>Muehlberger, Guenter, et al.</strong> "Transforming Scholarly Editing with Transkribus: Automated Text Recognition for Historical Documents." <em>Journal of Documentation</em>, 75(5), 2019.</li>
    </ul>
</div>"""

# 4. Watch List
watch_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #002D62; background-color: #f8fafc; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #002D62; margin-top: 0;">Curated Media & Technical Walkthroughs</h4>
    <p>Review these video demonstrations before completing your workshop assignment:</p>
    <ul>
        <li><strong>Palaeographical Decipherment Masterclass:</strong> Recognizing ligatures, abbreviations, and ductus across premodern and colonial hands (24 mins).</li>
        <li><strong>Transkribus Workflow from Scratch:</strong> Setting up collections, running automatic layout analysis, correcting baselines, and training custom PyLaia HTR models (28 mins).</li>
        <li><strong>Evaluating Machine Transcription:</strong> Calculating Character Error Rate (CER) and Word Error Rate (WER) using Levenshtein distance in Python and VS Code (19 mins).</li>
    </ul>
</div>"""

# 5. Workshop
ws_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #002D62; background-color: #fdfaf8; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #002D62; margin-top: 0;">Workshop: Ground-Truth Diplomatic Transcription & HTR Auditing</h4>
    <p><strong>Overview:</strong> In this workshop, you will produce a complete diplomatic transcription of your chosen full-page textual witness. You will run your folio through Transkribus HTR and an LLM/VLM transcription prompt, compare both machine outputs against your manual ground truth, and calculate your model's Character Error Rate (CER).</p>
    <p><strong>Deadlines:</strong> Comparison Post due Friday by 11:00 PM; Peer Reviews due Monday by 11:00 PM.</p>
</div>"""

ws_sub = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Submission Instructions</h4>
    <ol>
        <li>Open your chosen manuscript witness image in VS Code or your IIIF viewer alongside a plain text file (<code>ground_truth.txt</code>).</li>
        <li>Transcribe the entire page by hand line by line, preserving original orthography, abbreviations, and line breaks.</li>
        <li>Run the same page through Transkribus (automated baseline detection and transcription) and an LLM/VLM vision prompt.</li>
        <li>Compare the outputs against your human ground truth: calculate CER, record where the machine failed (e.g. damaged ink, ligatures, margin notes), and identify any hallucinations.</li>
        <li>Submit your transcription files and a <strong>300–500 word comparative reflection</strong> evaluating the limits of automated transcription on unique cultural artifacts.</li>
    </ol>
</div>"""

ws_assess = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Peer Assessment Rubric</h4>
    <ul>
        <li><strong>Diplomatic Precision & Ground Truth (4 pts):</strong> The human transcription faithfully captures all graphemic features, line breaks, and scribal idiosyncrasies of the witness.</li>
        <li><strong>HTR & VLM Error Analysis (3 pts):</strong> The submission rigorously documents machine errors, correctly distinguishing baseline misalignment, ligature confusion, and text hallucination.</li>
        <li><strong>Methodological Reflection (3 pts):</strong> The 300–500 word post articulates why automated transcription requires human ground truth as an indispensable epistemic anchor.</li>
    </ul>
</div>"""

quiz_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #002D62; background-color: #f8fafc; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #002D62; margin-top: 0;">Module 04 Knowledge Check Quiz</h4>
    <p>This formative quiz contains 10 multiple-choice questions covering diplomatic transcription, palaeographical ground truth, Transkribus HTR models, CER calculations, and LLM vision auditing.</p>
    <ul>
        <li><strong>Format:</strong> 10 Multiple Choice Questions with diagnostic feedback</li>
        <li><strong>Attempts:</strong> Unlimited (highest score counts)</li>
    </ul>
</div>"""

html_map = {
    "02_Learning_Objectives.html": obj_html,
    "05_Reading_List.html": reading_html,
    "06_Watch_List.html": watch_html,
    "08_Workshop_Description.html": ws_desc,
    "08a_Workshop_Submission_Instructions.html": ws_sub,
    "08b_Workshop_Assessment_Instructions.html": ws_assess,
    "09_Quiz_Description.html": quiz_desc,
}

for folder in [src_mod, dist_mod]:
    for fn, cont in html_map.items():
        (folder / fn).write_text(cont.strip() + "\n", encoding="utf-8")
        print(f"Wrote {folder / fn}")

# 6. Weekly Quiz Data Module
TOPIC = "Module_04_Transcription"
TITLE = "Module 04 Knowledge Check Quiz"

QUESTIONS = [
    Q("Diplomatic vs. Normalized Transcription",
      "What defines a diplomatic transcription in contrast to a normalized critical edition?",
      correct=("It faithfully records the exact graphemic characters, lineation, scribal errors, and physical abbreviations found on the surface without modernization.",
               "Correct. Diplomatic transcription prioritizes the physical carrier's exact graphemic reality over editorial modernization."),
      wrong=[("It modernizes spelling, punctuation, and capitalization to make the text immediately legible to modern readers.",
              "Incorrect. That describes a normalized or modernized edition."),
             ("It reconstructs lost archetype readings by collating multiple manuscript witnesses together.",
              "Incorrect. That describes stemmatic critical collation, not diplomatic transcription."),
             ("It translates historical idiomatic expressions into contemporary English equivalents.",
              "Incorrect. Transcription deals with the source text, not dynamic-equivalence translation.")],
      note="Diplomatic transcription models the physical manuscript witness as a material document."),

    Q("The Primacy of Ground Truth",
      "Why must manual diplomatic transcription precede automated HTR and LLM workflows in scientific philology?",
      correct=("Human diplomatic transcription provides the authoritative ground truth against which machine error rates and hallucinations are quantitatively evaluated.",
               "Correct. Without verified human ground truth, automated outputs cannot be scored or audited."),
      wrong=[("Transkribus and LLMs cannot parse digital images unless a human types the text first into the model prompt.",
              "Incorrect. Vision models can process raw pixels directly; human text is needed for evaluation, not initiation."),
             ("Unicode standards require human verification before digital font glyphs can render on web browsers.",
              "Incorrect. Font rendering engines parse character codepoints automatically."),
             ("International copyright law prohibits training computer vision models directly on raw manuscript photographs.",
              "Incorrect. Copyright law does not govern the technical sequencing of manual and automated editing.")],
      note="The manual baseline is the scientific control of computational editing."),

    Q("Baselines in HTR Models",
      "In the Transkribus HTR pipeline, what is the specific technical function of a 'baseline'?",
      correct=("A vector line upon which the characters of a line of text rest, guiding the neural network's sequential character recognition window.",
               "Correct. Baselines define the geometric orientation and trajectory along which character recognition models traverse text."),
      wrong=[("A bounding rectangle enclosing the entire manuscript page to crop out library margins and color charts.",
              "Incorrect. That is a page or Region of Interest (ROI) boundary, not a baseline."),
             ("The minimum acceptable Character Error Rate (CER) required before a model can be deployed in production.",
              "Incorrect. That is an accuracy threshold, not a baseline in layout analysis."),
             ("The baseline coordinates of the holding library's physical building in geographic coordinates.",
              "Incorrect. Baselines are image coordinate vectors.")],
      note="Transkribus trains character recognition on extracted baseline polygon strips."),

    Q("Character Error Rate (CER) Calculation",
      "How is Character Error Rate (CER) mathematically calculated when benchmarking machine transcription against human ground truth?",
      correct=("The sum of character substitutions, deletions, and insertions divided by the total number of characters in the ground truth.",
               "Correct. CER is normalized Levenshtein distance computed at the character level."),
      wrong=[("The total number of misspelled words divided by the total word count of the document.",
              "Incorrect. That is Word Error Rate (WER), not CER."),
             ("The percentage of pixels in the binary image that do not match the predicted font outline.",
              "Incorrect. Pixel mismatch measures visual binarization loss, not semantic character error."),
             ("The ratio of valid XML tags to total XML tags generated by the vision-language model.",
              "Incorrect. That measures syntactic schema validity, not transcription CER.")],
      note="CER = (Substitutions + Deletions + Insertions) / Total Reference Characters."),

    Q("Vision-Language Model Hallucination",
      "What is the primary architectural cause of 'hallucination' when using Vision-Language Models (such as GPT-4o or Claude 3.5 Sonnet) for manuscript transcription?",
      correct=("The model's autoregressive language prior overrules ambiguous visual evidence, generating syntactically plausible text that does not exist on the page.",
               "Correct. Strong linguistic priors cause the model to 'read' what it expects textually rather than what ink actually depicts."),
      wrong=[("The image resolution is automatically downsampled by the browser, destroying high-frequency line edges.",
              "Incorrect. Downsampling causes blur and unreadability, but not generative hallucination of absent text."),
             ("The model's internal memory runs out of tokens, causing it to loop the same sentence repeatedly.",
              "Incorrect. Token exhaustion causes truncated output, not fabricated readings."),
             ("The physical manuscript's ink chemical composition interferes with optical character recognition sensors.",
              "Incorrect. LLMs operate on digital pixels, not chemical sensors.")],
      note="Generative models hallucinate when language probability overpowers weak visual signals."),

    Q("TEI Diplomatic Abbreviation Markup",
      "In TEI XML diplomatic encoding, which pair of elements is used to capture both the original scribal abbreviation and its editorial expansion?",
      correct=("<choice> wrapping <abbr> and <expan>",
               "Correct. The <choice> container allows digital editions to toggle between diplomatic (<abbr>) and expanded (<expan>) views."),
      wrong=[("<subst> wrapping <add> and <del>",
              "Incorrect. <subst> encodes scribal substitutions (additions replacing deletions)."),
             ("<orig> wrapping <sic> and <corr>",
              "Incorrect. <choice> wraps <sic> and <corr>, or <orig> and <reg>."),
             ("<app> wrapping <rdg> and <lem>",
              "Incorrect. <app> is for critical apparatus variants across multiple witnesses.")],
      note="<choice><abbr>...</abbr><expan>...</expan></choice> is the standard TEI pattern."),

    Q("Overfitting in PyLaia HTR Training",
      "What is 'overfitting' in the context of training a custom Transkribus PyLaia HTR model?",
      correct=("The model achieves near 0% CER on the training pages by memorizing noise and specific ink blots, but fails to generalize to unseen folios in the same hand.",
               "Correct. Overfitting occurs when a neural network memorizes training idiosyncrasies at the expense of generalizability."),
      wrong=[("The model exceeds the 100-page training limit imposed by Transkribus cloud servers.",
              "Incorrect. That is an administrative quota, not statistical overfitting."),
             ("The neural network layers become too wide to fit into the GPU memory buffer during inference.",
              "Incorrect. That causes an Out-Of-Memory (OOM) error, not overfitting."),
             ("The model attempts to transcribe text in two different languages simultaneously within the same line.",
              "Incorrect. Polyglot training is a domain transfer task, not overfitting.")],
      note="Overfitted models show artificially low validation loss on training data but fail on validation sets."),

    Q("Show-Through and Bleed-Through Artifacts",
      "When an ancient or colonial manuscript has ink bleeding through from the reverse side (show-through), what risk does this pose to automated layout analysis?",
      correct=("The algorithm mistakenly detects the reverse-side ink traces as active text baselines on the current folio.",
               "Correct. Bleed-through ink often mimics dark strokes, triggering false baseline generation in layout analysis."),
      wrong=[("The image file format corrupts and cannot be read by IIIF image servers.",
              "Incorrect. Visual bleed-through does not corrupt image file headers or IIIF manifests."),
             ("The character recognition engine defaults to Latin script regardless of the language.",
              "Incorrect. Script priors are determined by language models, not ink bleed-through."),
             ("The XML validator flags the document as structurally ill-formed.",
              "Incorrect. Schema validation tests XML syntax, not image pixel artifacts.")],
      note="Bleed-through requires morphological filtering or manual baseline curation in Transkribus."),

    Q("Leiden Conventions for Lacunae",
      "Under the Leiden Conventions frequently used in documentary papyrology and epigraphy, what do square brackets `[ ... ]` indicate?",
      correct=("Text lost through physical damage to the carrier and restored by editorial conjecture.",
               "Correct. Square brackets signal a physical lacuna where text is missing and supplied by the editor."),
      wrong=[("Text deleted by the original scribe by strikethrough or expunction.",
              "Incorrect. Scribal deletions are marked with braces `{...}` in Leiden conventions."),
             ("Abbreviations expanded by the modern editor.",
              "Incorrect. Editorial expansions of abbreviations are marked with parentheses `(...)`."),
             ("Letters that are damaged and legible only through contextual guesswork.",
              "Incorrect. Uncertain letters are indicated with underdots in Leiden notation.")],
      note="In TEI, Leiden `[...]` maps to `<supplied reason=\"lost\">`."),

    Q("WER vs. CER Divergence",
      "Why is Word Error Rate (WER) typically significantly higher than Character Error Rate (CER) on historical manuscript corpora?",
      correct=("A single incorrect character in a word causes the entire word to be scored as an error in WER.",
               "Correct. Because words comprise multiple characters, a 5% CER easily translates to 20-30% WER."),
      wrong=[("Historical manuscripts do not separate words with spaces, making word counts impossible.",
              "Incorrect. While scriptio continua exists, WER algorithms tokenize by whitespace or dictionary boundaries."),
             ("WER measures only grammatical errors, whereas CER measures spelling errors.",
              "Incorrect. Both measure string edit distance, simply at different token granularities."),
             ("CER is weighted by token frequency, while WER treats all tokens identically.",
              "Incorrect. Standard CER and WER are both unweighted edit distances.")],
      note="One single character substitution flips a whole word from correct to incorrect in WER.")
]

def render_quiz(topic, title, questions):
    out = [
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
        "<quiz>",
        "  <!-- Category Definition -->",
        "  <question type=\"category\">",
        "    <category>",
        f"      <text>$course$/{topic}/Weekly Quiz</text>",
        "    </category>",
        "    <info format=\"html\">",
        f"      <text><![CDATA[<p>Formative Knowledge Check Quiz for {topic}: {title}.</p>]]></text>",
        "    </info>",
        "  </question>",
        "",
    ]
    for n, q in enumerate(questions, start=1):
        out += [
            f"  <!-- {n:02d} Question -->",
            "  <question type=\"multichoice\">",
            "    <name>",
            f"      <text>{n:02d} Question: {q.name}</text>",
            "    </name>",
            "    <questiontext format=\"html\">",
            f"      <text><![CDATA[<p>{q.stem}</p>]]></text>",
            "    </questiontext>",
            "    <generalfeedback format=\"html\">",
            f"      <text><![CDATA[<p>{q.note}</p>]]></text>",
            "    </generalfeedback>",
            "    <defaultgrade>1.0000000</defaultgrade>",
            "    <penalty>0.3333333</penalty>",
            "    <hidden>0</hidden>",
            "    <single>true</single>",
            "    <shuffleanswers>true</shuffleanswers>",
            "    <answernumbering>abc</answernumbering>",
        ]
        for fraction, text, feedback in q.options():
            out += [
                f"    <answer fraction=\"{fraction}\" format=\"html\">",
                f"      <text><![CDATA[<p>{text}</p>]]></text>",
                "      <feedback format=\"html\">",
                f"        <text><![CDATA[<p>{feedback}</p>]]></text>",
                "      </feedback>",
                "    </answer>",
            ]
        out += ["  </question>", ""]
    out += ["</quiz>", ""]
    return "\n".join(out)

xml_content = render_quiz(TOPIC, TITLE, QUESTIONS)
ET.fromstring(xml_content)

for p in [dist_mod / "09_Quiz.xml", src_mod / "09_Quiz.xml"]:
    p.write_text(xml_content, encoding="utf-8")
    print(f"Wrote and validated {p}")

