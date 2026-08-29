import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import xml.etree.ElementTree as ET

shared_dir = Path(__file__).resolve().parent.parent.parent / "shared" / "scripts"
sys.path.insert(0, str(shared_dir))
from question_bank import Q

src_mod = Path("src/modules/Module_02_Cataloguing")
dist_mod = Path("dist/moodle/Module_02_Cataloguing")
src_mod.mkdir(parents=True, exist_ok=True)
dist_mod.mkdir(parents=True, exist_ok=True)

# 1. Banner Image (1200x300)
def create_banner():
    w, h = 1200, 300
    img = Image.new("RGB", (w, h), color="#2c221e")  # deep walnut / vellum tone
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, w-10, h-10], outline="#c29b38", width=2)
    draw.rectangle([16, 16, w-16, h-16], outline="#4a3b32", width=1)
    draw.rectangle([20, 20, 35, h-20], fill="#3d5a80")  # faded lapis accent
    
    try:
        font_course = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font_course = font_title = font_sub = ImageFont.load_default()
        
    draw.text((60, 45), "RELS 398 / ENGL 398  •  DIGITAL METHODS FOR HISTORICAL DOCUMENTS", fill="#c29b38", font=font_course)
    draw.text((60, 100), "Module 02: Cataloguing & Codicological Metadata", fill="#f8fafc", font=font_title)
    draw.text((60, 175), "Trismegistos & Pinakes Authority Files  •  TEI Header Architecture  •  Linked Data", fill="#cbd5e1", font=font_sub)
    draw.line([60, 225, w-60, 225], fill="#c29b38", width=1)
    draw.text((60, 245), "StFX Department of Religious Studies  •  Computational Philology Pipeline", fill="#94a3b8", font=font_sub)
    
    for p in [dist_mod / "01_Banner.png", src_mod / "01_Banner.png"]:
        img.save(p, "PNG")
        print(f"Wrote banner: {p}")

create_banner()

# 2. Learning Objectives
obj_html = """<div class="card p-3 mb-3 border-info" style="border-left: 5px solid #3d5a80; background-color: #f8fafc; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #3d5a80; margin-top: 0;">Module 02: Cataloguing & Metadata — Learning Objectives</h4>
    <p>By the end of this module, students will be able to:</p>
    <ul>
        <li><strong>Analyze</strong> the structural relationship between physical codicology (support, quires, watermarks, ruling) and digital metadata standards.</li>
        <li><strong>Query and integrate</strong> international manuscript authority files including Trismegistos (TM), Pinakes, and the Canonical Text Services (CTS) URN namespace.</li>
        <li><strong>Author and validate</strong> comprehensive TEI Header structures (<code>&lt;teiHeader&gt;</code>, <code>&lt;msDesc&gt;</code>, <code>&lt;physDesc&gt;</code>, <code>&lt;history&gt;</code>) compliant with the TEI P5 schema.</li>
        <li><strong>Evaluate</strong> the accuracy and hallucination risks of Large Language Models (LLMs) when generating structured archival metadata and implement deterministic validation audits.</li>
    </ul>
</div>"""

# 3. Readings
reading_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #c29b38; background-color: #fcfcfd; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c29b38; margin-top: 0;">Assigned Readings & Foundational Scholarship</h4>
    <p>Please study the following research papers on manuscript metadata and digital harmonization:</p>
    <ul>
        <li><strong>Hyvönen, Eero, et al.</strong> "Harmonizing and Publishing Heterogeneous Premodern Manuscript Metadata as Linked Open Data." <em>Semantic Web Journal</em>, 2023.</li>
        <li><strong>TEI Consortium.</strong> "Manuscript Description." In <em>TEI P5: Guidelines for Electronic Text Encoding and Interchange</em>, Chapter 10. TEI Consortium, 2024.</li>
        <li><strong>Romanello, Matteo, and Alban Gautier.</strong> "Automatic Metadata Extraction: Leveraging Large Language Models in Digital Humanities." <em>Journal of Open Humanities Data</em>, 2024.</li>
        <li><strong>Clarysse, Willy.</strong> "The Trismegistos Database of Ancient Texts and Manuscripts." <em>Literary and Linguistic Computing</em>, 2010.</li>
    </ul>
    <p class="text-muted" style="font-size: 0.9rem; color: #64748b;"><em>Assigned reading PDFs are available in the repository below.</em></p>
</div>"""

# 4. Watch List
watch_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #3d5a80; background-color: #f8fafc; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #3d5a80; margin-top: 0;">Curated Media & Technical Walkthroughs</h4>
    <p>Review these video demonstrations before completing your workshop assignment:</p>
    <ul>
        <li><strong>Navigating Trismegistos and Pinakes:</strong> Resolving conflicting shelfmarks and cross-referencing TM numbers across international repositories (16 mins).</li>
        <li><strong>TEI <code>msDesc</code> Encoding Masterclass:</strong> Live encoding of a complex composite codex with multiple quires, hands, and decoration tiers in Oxygen XML (22 mins).</li>
        <li><strong>Auditing AI Metadata Pipelines:</strong> Constructing Python RelaxNG and Schematron validators to catch hallucinations in LLM-generated TEI headers (18 mins).</li>
    </ul>
</div>"""

# 5. Workshop
ws_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #c2593f; background-color: #fdfaf8; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c2593f; margin-top: 0;">Workshop: Codicological TEI Header & Authority Reconciliation</h4>
    <p><strong>Overview:</strong> In this workshop, you will catalogue an assigned un-digitized Greek manuscript witness. You will query Trismegistos and Pinakes to identify authority records, construct a complete, validated TEI <code>&lt;msDesc&gt;</code> block, and audit an LLM-generated metadata record for hallucinated codicological data.</p>
    <p><strong>Deadlines:</strong> Comparison Post due Friday by 11:00 PM; Peer Reviews due Monday by 11:00 PM.</p>
</div>"""

ws_sub = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Submission Instructions</h4>
    <ol>
        <li>Select your assigned manuscript shelfmark from the course inventory.</li>
        <li>Lookup and verify authority IDs in Trismegistos (TM), Pinakes, and Diktyon.</li>
        <li>Write a valid TEI XML snippet containing <code>&lt;teiHeader&gt;</code> with full <code>&lt;msIdentifier&gt;</code>, <code>&lt;msContents&gt;</code>, and <code>&lt;physDesc&gt;</code> (including support, foliation, layout, and scribal hands).</li>
        <li>Prompt an LLM (e.g. Claude or GPT-4) to extract the same metadata from a raw library catalogue entry, and identify at least two subtle hallucinations or schema violations.</li>
        <li>Submit your validated TEI snippet and a <strong>300–500 word comparison</strong> detailing how structured schemas enforce scholarly rigor against probabilistic AI errors.</li>
    </ol>
</div>"""

ws_assess = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Peer Assessment Rubric</h4>
    <ul>
        <li><strong>TEI XML Validity & Schema Compliance (4 pts):</strong> The <code>msDesc</code> snippet is well-formed XML, validates against the TEI P5 schema, and properly nests codicological elements.</li>
        <li><strong>Authority Control & Accuracy (3 pts):</strong> The submission correctly cross-references standard authority records (TM, Pinakes) and uses accurate CTS URN syntax.</li>
        <li><strong>Critical AI Audit (3 pts):</strong> The comparative reflection precisely diagnoses model hallucinations and explains the methodological necessity of deterministic validation.</li>
    </ul>
</div>"""

quiz_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #3d5a80; background-color: #f8fafc; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #3d5a80; margin-top: 0;">Module 02 Knowledge Check Quiz</h4>
    <p>This formative quiz contains 10 multiple-choice questions covering manuscript metadata, Trismegistos, Pinakes, CTS URNs, TEI <code>&lt;msDesc&gt;</code> encoding, and AI metadata auditing.</p>
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
TOPIC = "Module_02_Cataloguing"
TITLE = "Module 02 Knowledge Check Quiz"

QUESTIONS = [
    Q("Authority Files vs. Local Shelfmarks",
      "Why are global authority identifiers (such as Trismegistos numbers or Pinakes records) essential in digital manuscript cataloguing rather than relying solely on local library shelfmarks?",
      correct=("Because local shelfmarks can change during institutional reorganizations or vary in spelling across languages, whereas authority URIs provide persistent, unambiguous identifiers across international databases.",
               "Correct. Authority files disambiguate manuscripts whose library names, cities, or catalogue call numbers vary across centuries and publications."),
      wrong=[("Because local shelfmarks are copyright-protected by holding libraries and cannot be published online.",
              "Incorrect. Shelfmarks are historical catalogue numbers and are not copyright-restricted."),
             ("Because Trismegistos stores the full high-resolution photographic scans of every manuscript.",
              "Incorrect. Trismegistos is a metadata authority database, not an image repository."),
             ("Because authority identifiers automatically translate Greek manuscripts into English.",
              "Incorrect. Authority records track cataloguing identifiers and textual metadata, not linguistic translation.")],
      note="Global authority IDs (e.g. Trismegistos, Pinakes) provide persistent, language-independent identification across dispersed collections."),

    Q("Canonical Text Services (CTS) URN Syntax",
      "In the Canonical Text Services (CTS) URN architecture, what structural hierarchy is encoded in the identifier <code>urn:cts:greekLit:tlg0012.tlg001.perseus-grc1:1.1</code>?",
      correct=("Namespace, textgroup (Homer), work (Iliad), version/edition, and specific passage citation (Book 1, Line 1).",
               "Correct. CTS URNs express a strict conceptual hierarchy moving from author/textgroup down to specific passage citations."),
      wrong=[("The physical GPS coordinates of the library where the manuscript is housed.",
              "Incorrect. CTS URNs cite abstract textual works and passages, not physical buildings."),
             ("The IP address and TCP port number of the Moodle web server.",
              "Incorrect. CTS URNs are uniform resource names for philological citation, not network addresses."),
             ("The date and timestamp of the most recent Git commit.",
              "Incorrect. CTS URNs follow Homer Multitext citation ontology, independent of version control timestamps.")],
      note="CTS URNs encode a rigorous conceptual hierarchy: namespace -> textgroup -> work -> edition -> passage citation."),

    Q("TEI Header Architecture",
      "Under the Text Encoding Initiative (TEI P5) guidelines, which element is the mandatory container for all codicological, palaeographical, and administrative metadata describing a manuscript witness?",
      correct=("<code>&lt;msDesc&gt;</code> (Manuscript Description) within the <code>&lt;sourceDesc&gt;</code> of the <code>&lt;teiHeader&gt;</code>.",
               "Correct. The <msDesc> element holds the structured codicological hierarchy, including identification, contents, physical description, and history."),
      wrong=[("<code>&lt;body&gt;</code> inside <code>&lt;text&gt;</code>.",
              "Incorrect. The <body> element contains the primary transcription text, not the codicological metadata."),
             ("<code>&lt;encodingDesc&gt;</code> inside <code>&lt;profileDesc&gt;</code>.",
              "Incorrect. <encodingDesc> documents the editorial and transcription principles applied during encoding."),
             ("<code>&lt;revisionDesc&gt;</code> inside <code>&lt;front&gt;</code>.",
              "Incorrect. <revisionDesc> documents the change log of the XML file itself.")],
      note="<msDesc> within <sourceDesc> is the canonical TEI container for structured manuscript cataloguing and codicological data."),

    Q("Physical Description Hierarchy in TEI",
      "Which TEI element specifically structures information about the material support, quire collation, foliation, and page layout of a codex?",
      correct=("<code>&lt;physDesc&gt;</code> (Physical Description), containing children such as <code>&lt;objectDesc&gt;</code>, <code>&lt;supportDesc&gt;</code>, and <code>&lt;layoutDesc&gt;</code>.",
               "Correct. <physDesc> is the specialized sub-tree in <msDesc> dedicated to material aspects of the manuscript artifact."),
      wrong=[("<code>&lt;msContents&gt;</code>, which lists the modern scholars who purchased the manuscript.",
              "Incorrect. <msContents> lists the intellectual works, titles, and rubrics contained within the manuscript."),
             ("<code>&lt;history&gt;</code>, which records the grammar rules of ancient Greek.",
              "Incorrect. <history> records provenance, acquisition, and former owners."),
             ("<code>&lt;additional&gt;</code>, which stores student quiz grades.",
              "Incorrect. <additional> holds administrative notes and surrogate image details.")],
      note="<physDesc> houses the physical architecture of the codex: support, collation, dimensions, script, and binding."),

    Q("Quire Collation Formulae",
      "In classical codicology, what does the collation formula <code>1–5⁸, 6⁶ (fol. 46)</code> indicate about the physical construction of a manuscript?",
      correct=("The codex consists of five quires of 8 leaves (quaterniones) followed by one quire of 6 leaves (ternio), totaling 46 leaves.",
               "Correct. Standard collation notation records quire indices with superscript leaf counts and total foliation."),
      wrong=[("The manuscript was written by five different scribes over six centuries.",
              "Incorrect. The numbers represent quires (gatherings) and leaves, not scribal personnel."),
             ("The text has five chapters of 8 verses each and six footnotes.",
              "Incorrect. Collation formulae describe the physical gatherings of parchment/paper, not text divisions."),
             ("The codex was sold five times for eight gold florins.",
              "Incorrect. Collation formulae are structural binding formulas.")],
      note="Collation formulae represent the quire structure (gatherings) and leaf counts that constitute the codicological body."),

    Q("Dublin Core vs. TEI msDesc",
      "Why is standard Dublin Core (DC) metadata insufficient on its own for critical manuscript scholarship?",
      correct=("Dublin Core uses flat, 15-property key-value pairs designed for modern bibliographies, whereas TEI msDesc models deeply nested, composite codicological realities like multiple scribal hands, palimpsests, and quire repairs.",
               "Correct. Dublin Core is too flat and generic to capture the intricate multi-tiered physical and historical nuances of premodern manuscripts."),
      wrong=[("Dublin Core is an obsolete proprietary format that cannot be viewed on modern computers.",
              "Incorrect. Dublin Core is an active, universal metadata standard (ISO 15836), but it lacks domain depth for codicology."),
             ("Dublin Core is illegal under European open-access copyright legislation.",
              "Incorrect. Dublin Core is completely open and public-domain."),
             ("Dublin Core does not permit dates earlier than 1900 CE.",
              "Incorrect. Dublin Core allows historical dates, but lacks structural fields for material codicology.")],
      note="TEI msDesc provides the hierarchical depth required for physical codicology that flat standards like Dublin Core cannot represent."),

    Q("Linked Open Data and URIs",
      "How does expressing manuscript metadata as RDF triples (Subject–Predicate–Object) with dereferenceable URIs improve scholarly discovery?",
      correct=("It allows disparate library catalogues across the world to be queried as a single decentralized graph database, automatically connecting manuscripts with linked bibliographies, gazetteers, and prosopographies.",
               "Correct. RDF linked data enables automated federated SPARQL queries across international institutional silos."),
      wrong=[("It encrypts library records to prevent unauthorized public access.",
              "Incorrect. Linked Open Data is designed for open, frictionless interoperability."),
             ("It converts all ancient manuscripts into modern MP3 audiobooks.",
              "Incorrect. RDF is a knowledge graph data model, not an audio conversion format."),
             ("It replaces all human librarians with automated cataloguing bots.",
              "Incorrect. Linked data assists scholars and librarians by interconnecting semantic metadata.")],
      note="RDF triples and linked data URIs connect isolated manuscript records into a global, queryable scholarly knowledge graph."),

    Q("LLM Hallucinations in Codicological Extraction",
      "When using Large Language Models (LLMs) to automatically convert unstructured 19th-century Latin catalogue descriptions into TEI XML, what is a common hallucination risk?",
      correct=("The LLM may fabricate plausible-sounding folio counts, invent watermarks, or confabulate shelfmarks that appear syntactically valid but do not exist in the source document.",
               "Correct. Probabilistic language models optimize for plausible fluent text and can invent specific historical numbers or codicological details."),
      wrong=[("The LLM will refuse to process any text written in Latin or Greek.",
              "Incorrect. Modern LLMs handle Latin and ancient Greek fluently."),
             ("The LLM will alter the physical parchment in the library vault.",
              "Incorrect. Software models interact only with digital representations, not physical artifacts."),
             ("The LLM will automatically delete the Git repository if an error is encountered.",
              "Incorrect. LLM inference does not execute destructive repository commands unless piped into unmonitored scripts.")],
      note="LLMs can hallucinate plausible-sounding codicological details; automated schema validation and manual verification are mandatory."),

    Q("Deterministic Validation with Schematron",
      "Why is ISO Schematron used alongside RelaxNG or XML Schema in professional TEI metadata pipelines?",
      correct=("Schematron can validate complex co-occurrence constraints and business logic (e.g. asserting that if a manuscript is marked 'fragment', foliation must be under 5 leaves) that grammar-based schemas cannot express.",
               "Correct. Schematron uses XPath expressions to test rule-based contextual dependencies and logical constraints across XML documents."),
      wrong=[("Schematron is the only tool that can translate Greek into Latin.",
              "Incorrect. Schematron is a structural and semantic XML validation language."),
             ("Schematron is required to compile Python scripts into executable machine code.",
              "Incorrect. Schematron is an XML validation standard, not a Python compiler."),
             ("Schematron automatically writes student research papers.",
              "Incorrect. Schematron is an automated validation engine.")],
      note="Schematron enforces contextual business rules and philological constraints that structural schemas cannot express."),

    Q("The Role of Controlled Vocabularies",
      "Why should TEI metadata attributes (such as <code>@script</code>, <code>@material</code>, or <code>@ruling</code>) use values drawn from controlled vocabularies (e.g. Getty AAT or CERL thesauri)?",
      correct=("Controlled vocabularies eliminate synonymous variations (e.g. 'parchment' vs. 'vellum' vs. 'pergamentum'), enabling precise computational filtering and cross-corpus aggregation.",
               "Correct. Standardized ontologies ensure that identical concepts are indexed consistently regardless of local linguistic preference."),
      wrong=[("Because using uncontrolled strings results in immediate criminal copyright prosecution.",
              "Incorrect. Controlled vocabularies are a scholarly best practice for interoperability, not a criminal matter."),
             ("Because controlled vocabularies reduce the size of the XML file by 95%.",
              "Incorrect. Vocabulary control improves semantic consistency, not file compression."),
             ("Because controlled vocabularies make text unreadable to humans.",
              "Incorrect. Controlled terms use clear natural language concepts mapped to persistent URIs.")],
      note="Controlled vocabularies guarantee semantic consistency across independent cataloguing projects and search engines."),
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

# Write quiz bank
bank_file = Path("scripts/banks/quiz_02.py")
bank_file.write_text(Path(__file__).read_text(encoding="utf-8"), encoding="utf-8")
print(f"Wrote bank file {bank_file}")

xml_content = render_quiz(TOPIC, TITLE, QUESTIONS)
ET.fromstring(xml_content)

for p in [dist_mod / "09_Quiz.xml", src_mod / "09_Quiz.xml"]:
    p.write_text(xml_content, encoding="utf-8")
    print(f"Wrote and validated {p}")
