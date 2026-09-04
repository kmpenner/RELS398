import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

shared_dir = Path(__file__).resolve().parents[3] / "shared" / "scripts"
sys.path.insert(0, str(shared_dir))
from question_bank import Q

src_mod = Path("src/modules/Module_05_Reconciliation")
dist_mod = Path("dist/moodle/Module_05_Reconciliation")
src_mod.mkdir(parents=True, exist_ok=True)
dist_mod.mkdir(parents=True, exist_ok=True)

# 1. Banner Image (1200x300)
def create_banner():
    w, h = 1200, 300
    img = Image.new("RGB", (w, h), color="#1c1917")  # warm stone / deep slate
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, w-10, h-10], outline="#c29b38", width=2)
    draw.rectangle([16, 16, w-16, h-16], outline="#44403c", width=1)
    draw.rectangle([20, 20, 35, h-20], fill="#d97706")  # warm amber / adjudication accent
    
    try:
        font_course = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font_course = font_title = font_sub = ImageFont.load_default()
        
    draw.text((60, 45), "RELS 398 / ENGL 398  •  DIGITAL METHODS FOR HISTORICAL DOCUMENTS", fill="#c29b38", font=font_course)
    draw.text((60, 100), "Module 05: Reconciliation & Double-Keying", fill="#f8fafc", font=font_title)
    draw.text((60, 175), "Independent Double-Keying  •  Inter-Annotator Agreement  •  Consensus Ground Truth", fill="#cbd5e1", font=font_sub)
    draw.line([60, 225, w-60, 225], fill="#c29b38", width=1)
    draw.text((60, 245), "StFX Department of Religious Studies  •  Computational Philology Pipeline", fill="#94a3b8", font=font_sub)
    
    for p in [dist_mod / "01_Banner.png", src_mod / "01_Banner.png"]:
        img.save(p, "PNG")
        print(f"Wrote banner: {p}")

create_banner()

# 2. Learning Objectives
obj_html = """<div class="card p-3 mb-3 border-info" style="border-left: 5px solid #d97706; background-color: #fdfaf8; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #92400e; margin-top: 0;">Module 05: Reconciliation & Double-Keying — Learning Objectives</h4>
    <p>By the end of this module, students will be able to:</p>
    <ul>
        <li><strong>Analyze</strong> the statistical reliability of independent double-keying and explain why post-editing proofreading suffers from cognitive confirmation bias.</li>
        <li><strong>Calculate and interpret</strong> Inter-Annotator Agreement (IAA) using percentage agreement and Cohen's Kappa coefficient across historical transcription samples.</li>
        <li><strong>Execute</strong> programmatic character-level and word-level diffing in VS Code using Git and terminal utilities (<code>diff</code>, <code>wdiff</code>) to locate textual discrepancies.</li>
        <li><strong>Adjudicate</strong> competing editorial readings against high-resolution facsimiles to establish an authoritative consensus ground truth.</li>
    </ul>
</div>"""

# 3. Readings
reading_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #c29b38; background-color: #fcfcfd; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c29b38; margin-top: 0;">Assigned Readings & Foundational Scholarship</h4>
    <p>Please study the following research papers on transcription quality, double-keying, and error classification:</p>
    <ul>
        <li><strong>Haaf, Susanne, Frank Wiegand, and Alexander Geyken.</strong> "Measuring the Correctness of Double-Keying: An Error-Classification for Evaluation of Text Digitisation." <em>Language Resources and Evaluation</em>, 49(4), 2015, pp. 759–789.</li>
        <li><strong>Griffitts, Troy.</strong> "Digital Editing of Biblical Texts." <em>Manuscript Cultures: Mapping Textual Landscapes</em>, § 4.5.2 (Reconciliation and Collation Baselines).</li>
    </ul>
</div>"""

# 4. Watch List
watch_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #d97706; background-color: #fdfaf8; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #92400e; margin-top: 0;">Curated Media & Technical Walkthroughs</h4>
    <p>Review these video demonstrations before completing your workshop assignment:</p>
    <ul>
        <li><strong>Double-Keying in Digital Humanities:</strong> Why two independent typists produce 99.98% accuracy while proofreading misses major errors (18 mins).</li>
        <li><strong>Three-Way Merge & Adjudication in VS Code:</strong> Resolving conflicting transcriptions using visual diff editors and Git merge tools (21 mins).</li>
        <li><strong>Quantifying Inter-Annotator Agreement:</strong> Calculating Cohen's Kappa for paleographical transcription in Python (16 mins).</li>
    </ul>
</div>"""

# 5. Workshop
ws_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #d97706; background-color: #fdfaf8; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #92400e; margin-top: 0;">Workshop: Pair Reconciliation & Consensus Ground Truth</h4>
    <p><strong>Overview:</strong> In this workshop, you will swap your blind diplomatic transcription with a peer. You will run an automated diff between both transcriptions, identify every point of divergence, return to the high-resolution IIIF facsimile to adjudicate each difference, and establish an agreed consensus ground truth.</p>
    <p><strong>Deadlines:</strong> Comparison Post due Friday by 11:00 PM; Peer Reviews due Monday by 11:00 PM.</p>
</div>"""

ws_sub = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Submission Instructions</h4>
    <ol>
        <li>Exchange your raw diplomatic transcription (<code>transcription_A.txt</code>) with your assigned workshop partner (<code>transcription_B.txt</code>).</li>
        <li>Perform a character-level and word-level diff between both files in VS Code or Terminal (<code>diff -u transcription_A.txt transcription_B.txt</code>).</li>
        <li>Generate a reconciliation report listing every discrepancy, citing line numbers and specific glyph differences.</li>
        <li>Examine the high-resolution facsimile together to adjudicate each discrepancy, deciding whether A is correct, B is correct, or a third reading is warranted.</li>
        <li>Submit your final <code>consensus_ground_truth.txt</code> file and a <strong>300–500 word reflection</strong> analyzing which categories of palaeographical features (e.g. abbreviations, ink erosion, ligatures) generated the highest discrepancy rates.</li>
    </ol>
</div>"""

ws_assess = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Peer Assessment Rubric</h4>
    <ul>
        <li><strong>Diff Completeness & Precision (4 pts):</strong> The submission identifies all discrepancies between the two independent transcriptions without omitting subtle punctuation or capitalization variations.</li>
        <li><strong>Adjudication Evidentiary Rigor (3 pts):</strong> Every editorial decision is justified with explicit visual evidence from the IIIF image rather than arbitrary compromise.</li>
        <li><strong>Methodological Reflection (3 pts):</strong> The 300–500 word analysis insightfully discusses how double-keying eliminates blind spots that single-editor proofreading fails to catch.</li>
    </ul>
</div>"""

quiz_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #d97706; background-color: #fdfaf8; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #92400e; margin-top: 0;">Module 05 Knowledge Check Quiz</h4>
    <p>This formative quiz contains 10 multiple-choice questions covering independent double-keying theory, Inter-Annotator Agreement (Cohen's Kappa), diff analysis, and reconciliation workflows.</p>
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
TOPIC = "Module_05_Reconciliation"
TITLE = "Module 05 Knowledge Check Quiz"

QUESTIONS = [
    Q("Statistical Independence in Double-Keying",
      "Why does independent double-keying achieve an accuracy rate near 99.98% while single-pass transcription with proofreading rarely exceeds 95%?",
      correct=("Independent typists make uncorrelated random errors, meaning the probability of both making the exact same error at the exact same position is the product of their individual error rates (e.g. 0.01 × 0.01 = 0.0001).",
               "Correct. Independence ensures errors do not correlate, making identical simultaneous mistakes statistically improbable."),
      wrong=[("Proofreaders are legally prohibited from modifying raw digital transcription files.",
              "Incorrect. Proofreading workflows allow editing; the failure is cognitive, not legal."),
             ("Two transcribers automatically cancel out camera optical distortion in the source image.",
              "Incorrect. Optical distortion affects image quality, not the statistical model of human typing error."),
             ("Double-keying forces both transcribers to write in valid TEI XML syntax from the first keystroke.",
              "Incorrect. Double-keying is a transcription methodology, independent of XML serialization.")],
      note="If Transcriber A has a 1% error rate and Transcriber B has a 1% error rate, the probability of an undetected shared error is 0.01%."),

    Q("Cognitive Confirmation Bias in Proofreading",
      "In digital humanities text digitization, why does 'proofreading' against an existing transcription systematically miss up to 50% of errors?",
      correct=("Human readers naturally perform top-down lexical completion, reading what they expect the sentence to say rather than what the characters literally depict.",
               "Correct. Cognitive science shows the human brain automatically 'smooths over' typos and omissions when reading pre-existing text."),
      wrong=[("Monitors emit high-frequency screen flicker that degrades short-term ocular memory.",
              "Incorrect. The limitation is cognitive expectation, not hardware display flicker."),
             ("Proofreaders are trained exclusively in modern grammar and cannot recognize historical scripts.",
              "Incorrect. Even expert palaeographers suffer from confirmation bias when proofreading pre-existing transcripts."),
             ("Operating systems cache previous keystrokes, causing proofreading tools to reload old errors.",
              "Incorrect. Confirmation bias is a psychological phenomenon, not an OS cache behavior.")],
      note="Proofreading against a draft creates cognitive anchoring, blinding the reader to subtle errors."),

    Q("Inter-Annotator Agreement (Cohen's Kappa)",
      "Why is Cohen's Kappa coefficient preferred over simple percent agreement when measuring Inter-Annotator Agreement (IAA) between two transcribers?",
      correct=("Cohen's Kappa statistically accounts for the agreement that would be expected to occur by random chance alone.",
               "Correct. In texts where 98% of characters match easily, percent agreement overstates reliability; Kappa isolates true consensus above chance."),
      wrong=[("Cohen's Kappa automatically corrects misspelled words using an internal Latin dictionary.",
              "Incorrect. Kappa is a purely mathematical agreement statistic, not a spell-checker."),
             ("Simple percent agreement requires at least five independent transcribers to calculate.",
              "Incorrect. Percent agreement can be computed with two transcribers; its defect is ignoring chance agreement."),
             ("Cohen's Kappa is the only metric supported by the TEI Consortium guidelines.",
              "Incorrect. TEI guidelines do not mandate specific statistical agreement formulas.")],
      note="Cohen's Kappa = (Observed Agreement - Chance Agreement) / (1 - Chance Agreement)."),

    Q("Character-Level vs. Word-Level Diffing",
      "When comparing two independent diplomatic transcriptions in VS Code or Terminal, why is character-level diffing (`diff` or `wdiff`) essential over standard line-level diffing?",
      correct=("Standard line diffs flag an entire 40-character line as divergent even if only a single accent, dot, or ligature differs, obscuring the exact location of disagreement.",
               "Correct. Line diffs provide too coarse a granularity for palaeographical reconciliation; character diffs pinpoint the exact glyph in question."),
      wrong=[("Line-level diffing consumes exponential RAM and crashes local editors on files over 10 KB.",
              "Incorrect. Line diffing is computationally lightweight, but pedagogically and philologically too coarse."),
             ("Character-level diffing is required by Git version control before commits can be staged.",
              "Incorrect. Git operates natively on line diffs; character diffing is chosen for editorial precision."),
             ("Standard line diffs automatically convert all Unicode characters to ASCII.",
              "Incorrect. Diff utilities preserve Unicode encodings.")],
      note="Character-level inspection isolates the exact disputed grapheme without visual clutter."),

    Q("The Adjudication Step",
      "In the double-keying workflow, what is the specific role of the 'Adjudicator'?",
      correct=("A designated third editor who inspects the high-resolution facsimile exclusively at points of disagreement to make the authoritative decision and produce the consensus ground truth.",
               "Correct. The adjudicator does not re-transcribe the entire text, but focuses their expertise on resolving genuine discrepancies."),
      wrong=[("An AI algorithm that automatically chooses whichever transcription was submitted first.",
              "Incorrect. Adjudication is an expert scholarly judgment rooted in material evidence."),
             ("A peer student who evaluates the grammar of the modern English translation.",
              "Incorrect. Adjudication operates on the source transcription, not dynamic translation."),
             ("A legal representative who assigns Creative Commons licenses to the digital edition.",
              "Incorrect. Licensing is distinct from philological adjudication.")],
      note="Adjudication leverages expert attention efficiently by targeting only divergent points."),

    Q("Handling Genuine Palaeographical Ambiguity",
      "What should editors do during reconciliation when a letter is physically damaged such that both transcribers proposed plausible, mutually incompatible readings?",
      correct=("Encode the ambiguity using TEI `<choice>` wrapping `<orig>` or `<app>` with multiple `<rdg>` elements, preserving the uncertainty rather than forcing a false consensus.",
               "Correct. Scholarly digital editions document genuine physical ambiguity rather than concealing it behind forced certainty."),
      wrong=[("Delete the disputed character entirely and remove it from the line count.",
              "Incorrect. Deleting text destroys material lineation and distorts downstream metrics."),
             ("Toss a coin to pick one reading and mark it as verified ground truth.",
              "Incorrect. Random choice violates scholarly integrity."),
             ("Discard the manuscript witness and choose an undamaged printed edition.",
              "Incorrect. Historical philology studies surviving material artifacts as they are.")],
      note="TEI markup allows digital editions to preserve scholarly debate and material ambiguity explicitly."),

    Q("LLM Post-Editing vs. Independent Keying",
      "Why does having a human 'post-edit' an LLM-generated transcription often reproduce the same systemic failures as single-pass proofreading?",
      correct=("The human editor becomes cognitively anchored to the LLM's plausible hallucinations, accepting fabricated words that fit the syntax but do not exist in the ink.",
               "Correct. LLMs generate fluent text, creating strong anchoring that deceives human checkers into confirming phantom readings."),
      wrong=[("LLMs introduce hidden invisible Unicode characters that lock the editor's keyboard.",
              "Incorrect. The failure is human cognitive anchoring, not software keyboard locks."),
             ("Post-editing requires running specialized neural networks on local GPUs.",
              "Incorrect. Post-editing is done in standard text editors."),
             ("Academic copyright law invalidates editions that involve human-AI collaboration.",
              "Incorrect. Intellectual property law does not prohibit AI-assisted scholarly editing.")],
      note="Independent human transcription remains the only immune baseline against generative hallucination."),

    Q("Systematic vs. Random Errors in Double-Keying",
      "When evaluating reconciliation discrepancies, what distinguishes a 'systematic error' from a 'random error'?",
      correct=("Systematic errors stem from conceptual misunderstandings of scribal conventions (e.g. consistently misidentifying long-s as 'f'), while random errors are accidental keystroke slips.",
               "Correct. Systematic errors require paleographical re-education, whereas random errors are naturally filtered out by double-keying."),
      wrong=[("Systematic errors occur only in printed books, while random errors occur only in manuscripts.",
              "Incorrect. Both error classes occur across all material formats."),
             ("Random errors can be predicted using Cohen's Kappa, but systematic errors cannot.",
              "Incorrect. Kappa measures overall agreement, not error taxonomy."),
             ("Systematic errors always produce invalid XML syntax, while random errors produce valid XML.",
              "Incorrect. Error class describes editorial causation, not XML schema validity.")],
      note="Identifying systematic errors is how transcribers refine their palaeographical decipherment skills."),

    Q("Truth and Reconciliation in Textual Scholarship",
      "Why is the methodology of textual reconciliation pedagogically and ethically significant when transcribing historical documents?",
      correct=("It establishes historical truth through rigorous, accountable evidence-testing, confronting discrepancies openly rather than enforcing an unverified singular narrative.",
               "Correct. Reconciliation in scholarship is an exercise in intellectual humility, evidence-based consensus, and transparent accountability."),
      wrong=[("It guarantees that no two scholars will ever disagree on historical interpretation.",
              "Incorrect. Scholarship always involves debate; reconciliation provides transparent evidence for that debate."),
             ("It allows editors to alter historical records to conform to modern sensibilities.",
              "Incorrect. Philological reconciliation respects historical reality and material evidence."),
             ("It eliminates all human involvement from archival publishing.",
              "Incorrect. Reconciliation is fundamentally a human, deliberative process.")],
      note="Reconciliation proves that truth is established through rigorous comparative adjudication."),

    Q("Downstream Impact on Computational Philology",
      "How does a peer-reconciled consensus ground truth impact downstream machine learning tasks (such as training Transkribus HTR or fine-tuning LLMs)?",
      correct=("It prevents models from learning human typographical noise as ground truth, significantly lowering model perplexity and Character Error Rates.",
               "Correct. Training algorithms on noisy ground truth bakes human errors into the neural network; reconciled data yields clean, robust models."),
      wrong=[("It allows neural networks to bypass GPU computation and train instantly on CPU.",
              "Incorrect. Data quality improves model accuracy, but does not eliminate hardware requirements."),
             ("It automatically triples the size of the training image dataset.",
              "Incorrect. Reconciliation cleans text labels; it does not generate synthetic images."),
             ("It removes the need to validate XML schemas with Schematron.",
              "Incorrect. Clean transcription text does not substitute for structural schema validation.")],
      note="Garbage in, garbage out: machine learning models can only be as accurate as their training ground truth.")
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

