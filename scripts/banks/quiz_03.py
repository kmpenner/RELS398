import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import xml.etree.ElementTree as ET

shared_dir = Path(__file__).resolve().parent.parent.parent / "shared" / "scripts"
sys.path.insert(0, str(shared_dir))
from question_bank import Q

src_mod = Path("src/modules/Module_03_IIIF_Imaging")
dist_mod = Path("dist/moodle/Module_03_IIIF_Imaging")
src_mod.mkdir(parents=True, exist_ok=True)
dist_mod.mkdir(parents=True, exist_ok=True)

# 1. Banner Image (1200x300)
def create_banner():
    w, h = 1200, 300
    img = Image.new("RGB", (w, h), color="#1e1b4b")  # deep spectral indigo
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, w-10, h-10], outline="#c29b38", width=2)
    draw.rectangle([16, 16, w-16, h-16], outline="#312e81", width=1)
    draw.rectangle([20, 20, 35, h-20], fill="#818cf8")  # violet/spectral accent
    
    try:
        font_course = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font_course = font_title = font_sub = ImageFont.load_default()
        
    draw.text((60, 45), "RELS 398 / ENGL 398  •  DIGITAL METHODS FOR HISTORICAL DOCUMENTS", fill="#c29b38", font=font_course)
    draw.text((60, 100), "Module 03: IIIF Imaging & Digital Facsimiles", fill="#f8fafc", font=font_title)
    draw.text((60, 175), "Image API & Presentation API  •  Mirador Deep Zoom  •  TEI Facsimile Linking", fill="#cbd5e1", font=font_sub)
    draw.line([60, 225, w-60, 225], fill="#c29b38", width=1)
    draw.text((60, 245), "StFX Department of Religious Studies  •  Computational Philology Pipeline", fill="#94a3b8", font=font_sub)
    
    for p in [dist_mod / "01_Banner.png", src_mod / "01_Banner.png"]:
        img.save(p, "PNG")
        print(f"Wrote banner: {p}")

create_banner()

# 2. Learning Objectives
obj_html = """<div class="card p-3 mb-3 border-info" style="border-left: 5px solid #818cf8; background-color: #f8fafc; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #312e81; margin-top: 0;">Module 03: IIIF Imaging & Facsimiles — Learning Objectives</h4>
    <p>By the end of this module, students will be able to:</p>
    <ul>
        <li><strong>Deconstruct</strong> the International Image Interoperability Framework (IIIF) Image API syntax (<code>{scheme}://{server}/{prefix}/{identifier}/{region}/{size}/{rotation}/{quality}.{format}</code>) for parametric image retrieval.</li>
        <li><strong>Construct and validate</strong> IIIF Presentation API 3.0 Manifests structuring complex manuscript sequences, Canvases, AnnotationPages, and Painting annotations.</li>
        <li><strong>Link</strong> digital image coordinates to structured transcription text using TEI <code>&lt;facsimile&gt;</code>, <code>&lt;surface&gt;</code>, and <code>&lt;zone&gt;</code> elements linked via <code>@facs</code> XML attributes.</li>
        <li><strong>Deploy</strong> client-side digital workspace viewers (Mirador and Universal Viewer) to conduct comparative multi-witness side-by-side paleographical collation.</li>
    </ul>
</div>"""

# 3. Readings
reading_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #c29b38; background-color: #fcfcfd; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c29b38; margin-top: 0;">Assigned Readings & Foundational Scholarship</h4>
    <p>Please review the following core technical specifications and scholarship on digital facsimiles:</p>
    <ul>
        <li><strong>IIIF Consortium.</strong> <em>IIIF Image API 3.0</em> and <em>IIIF Presentation API 3.0</em>. International Image Interoperability Framework, 2023. [Open Access]</li>
        <li><strong>Snydman, Michael, Robert Sanderson, and Tom Cramer.</strong> "The International Image Interoperability Framework (IIIF): A Community-Driven Solution for Digital High-Resolution Image Delivery." <em>Archiving Conference</em>, 2015.</li>
        <li><strong>TEI Consortium.</strong> "Representation of Primary Sources: Digital Facsimiles." In <em>TEI P5 Guidelines</em>, Chapter 11. TEI Consortium, 2024.</li>
        <li><strong>Cayless, Hugh, et al.</strong> "Multimodal Manuscript Representation Toward an Open Repository for Manuscript Research." <em>Digital Humanities Quarterly</em>, 2023.</li>
    </ul>
    <p class="text-muted" style="font-size: 0.9rem; color: #64748b;"><em>Assigned reading PDFs are accessible in the repository below.</em></p>
</div>"""

# 4. Watch List
watch_html = """<div class="card p-3 mb-3" style="border-left: 5px solid #818cf8; background-color: #f8fafc; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #312e81; margin-top: 0;">Curated Media & Technical Walkthroughs</h4>
    <p>Watch these technical demonstrations prior to completing your workshop:</p>
    <ul>
        <li><strong>Deconstructing the IIIF Image URL:</strong> Dynamic manipulation of region bounding boxes, percentage scaling, and rotation parameters via terminal curl requests (15 mins).</li>
        <li><strong>Authoring a IIIF 3.0 Presentation Manifest:</strong> Building a JSON-LD manifest from scratch with Canvases, dimensions, and image services (20 mins).</li>
        <li><strong>Connecting Mirador to TEI Facsimile Markup:</strong> Using SVG surface zones to link transcription lines directly to high-resolution parchment pixels (18 mins).</li>
    </ul>
</div>"""

# 5. Workshop
ws_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #c2593f; background-color: #fdfaf8; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #c2593f; margin-top: 0;">Workshop: IIIF Manifest Assembly & Canvas Coordinate Mapping</h4>
    <p><strong>Overview:</strong> In this workshop, you will build a compliant IIIF Presentation 3.0 JSON-LD Manifest for a two-page manuscript opening, construct a corresponding TEI <code>&lt;facsimile&gt;</code> element mapping line zones to pixel bounding boxes, and load both into a local Mirador viewer instance.</p>
    <p><strong>Deadlines:</strong> Comparison Post due Friday by 11:00 PM; Peer Reviews due Monday by 11:00 PM.</p>
</div>"""

ws_sub = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Submission Instructions</h4>
    <ol>
        <li>Construct a valid IIIF 3.0 JSON-LD manifest (<code>manifest.json</code>) defining two Canvases for recto and verso of your assigned manuscript leaf.</li>
        <li>Extract image coordinates for three distinct textual lines (using pixel coordinates <code>x,y,w,h</code>).</li>
        <li>Write a TEI <code>&lt;facsimile&gt;</code> block containing <code>&lt;surface&gt;</code> and <code>&lt;zone&gt;</code> elements linked to your TEI <code>&lt;text&gt;</code> lines using <code>@facs</code>.</li>
        <li>Verify your manifest in the online IIIF Manifest Validator and load it into Mirador.</li>
        <li>Submit your JSON manifest, TEI snippet, and a <strong>300–500 word reflection</strong> on how IIIF decouples image hosting from scholarly annotation architectures.</li>
    </ol>
</div>"""

ws_assess = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Peer Assessment Rubric</h4>
    <ul>
        <li><strong>IIIF Manifest Validity (4 pts):</strong> The JSON-LD manifest strictly conforms to the IIIF Presentation 3.0 API schema with valid Canvases and Painting annotations.</li>
        <li><strong>TEI Facsimile Precision (3 pts):</strong> The <code>&lt;zone&gt;</code> coordinates accurately map bounding boxes to transcription lines without coordinate mismatch.</li>
        <li><strong>Critical Reflection (3 pts):</strong> The reflection clearly analyzes how the separation of Canvas coordinate space from pixel resolution enables perpetual interoperability.</li>
    </ul>
</div>"""

quiz_desc = """<div class="card p-3 mb-3" style="border-left: 5px solid #818cf8; background-color: #f8fafc; border-radius: 6px; padding: 1.25rem;">
    <h4 style="color: #312e81; margin-top: 0;">Module 03 Knowledge Check Quiz</h4>
    <p>This formative quiz contains 10 multiple-choice questions testing IIIF Image API syntax, Presentation API 3.0 JSON-LD structures, Canvas coordinate spaces, deep zoom image pyramids, and TEI facsimile integration.</p>
    <ul>
        <li><strong>Format:</strong> 10 Multiple Choice Questions with diagnostic explanations</li>
        <li><strong>Attempts:</strong> Unlimited (highest grade counts)</li>
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
TOPIC = "Module_03_IIIF_Imaging"
TITLE = "Module 03 Knowledge Check Quiz"

QUESTIONS = [
    Q("IIIF Image API URL Structure",
      "In the standard IIIF Image API 3.0 specification, what does the URL path <code>.../120,300,800,600/max/0/default.jpg</code> specify?",
      correct=("Extract a rectangular region starting at pixel coordinate (120, 300) with width 800 and height 600, render it at full available resolution with no rotation, in default colour profile as a JPEG.",
               "Correct. The standard IIIF Image API parameter order is {region}/{size}/{rotation}/{quality}.{format}."),
      wrong=[("Download 120 images of size 300x800 at 0% quality.",
              "Incorrect. The numbers represent the region bounding box (x, y, w, h)."),
             ("Scale the whole image to 120x300 pixels and rotate it 600 degrees.",
              "Incorrect. Region precedes size, and rotation is 0 degrees."),
             ("Authenticate user ID 120 with password hash 300 on port 800.",
              "Incorrect. These are purely spatial and rendering image parameters.")],
      note="IIIF Image API syntax follows: {scheme}://{server}/{prefix}/{identifier}/{region}/{size}/{rotation}/{quality}.{format}."),

    Q("The Abstract Canvas Concept",
      "Why does the IIIF Presentation API define an abstract, virtual 'Canvas' rather than linking directly to image pixel dimensions?",
      correct=("A Canvas represents an abstract coordinate space that can host multiple layered images (e.g. multispectral bands, X-ray, RTI), vector annotations, and transcription overlays on a single shared surface.",
               "Correct. The Canvas is an abstract continuous coordinate space onto which multiple visual and textual resources are painted."),
      wrong=[("Because computer monitors are physically unable to display JPEG images directly.",
              "Incorrect. Standard image files display easily, but cannot layer multi-modal representations without an abstract canvas."),
             ("Because the IIIF Consortium prohibits the use of digital photography in scholarly archives.",
              "Incorrect. IIIF was designed specifically to optimize high-resolution digital photography delivery."),
             ("Because storing canvas coordinates eliminates the need for web browsers.",
              "Incorrect. IIIF canvases are interpreted by web client viewers like Mirador.")],
      note="The Canvas is an abstract coordinate space that decouples physical pixel dimensions from scholarly annotations and layered imaging."),

    Q("Tiled Deep Zoom (Image Pyramids)",
      "How do IIIF image servers (such as Cantaloupe or Loris) deliver smooth deep zooming for 500-megapixel manuscript scans over standard internet connections?",
      correct=("By generating hierarchical multi-resolution image pyramids and serving only the specific 256x256 pixel tiles visible in the user's current viewport at the requested zoom level.",
               "Correct. Tiled deep zoom avoids downloading massive multi-gigabyte files by serving small pre-rendered tiles on demand."),
      wrong=[("By compressing the entire 500MB manuscript scan into a single low-resolution GIF animation.",
              "Incorrect. Pyramidal tiling preserves full 100% resolution at deep zoom levels while streaming only visible tiles."),
             ("By transmitting raw uncompressed TIFF files over high-speed satellite relays.",
              "Incorrect. Raw TIFF downloads would overwhelm client bandwidth; tiled streaming solves bandwidth bottlenecks."),
             ("By requiring students to purchase specialized GPU server hardware.",
              "Incorrect. Standard web browsers easily render tiled deep zoom interfaces.")],
      note="Pyramidal image tiling allows instant deep zooming by delivering only the visible tiles for the client viewport."),

    Q("Painting Annotations in Presentation 3.0",
      "In IIIF Presentation API 3.0, what is the semantic role of an <code>Annotation</code> with <code>motivation: \"painting\"</code>?",
      correct=("It instructs the viewer to render the associated media resource (e.g. high-resolution image or video) as the primary visual content of the Canvas.",
               "Correct. In Presentation 3.0, images are 'painted' onto the Canvas via W3C Web Annotations with motivation='painting'."),
      wrong=[("It flags the manuscript image as an illegal graffiti vandalism.",
              "Incorrect. 'Painting' is the technical W3C term for displaying media on a canvas."),
             ("It applies artistic oil painting filters to modern photographs.",
              "Incorrect. No artistic alteration is applied; it is the standard media presentation directive."),
             ("It calculates student tuition fees for visual arts courses.",
              "Incorrect. Motivation attributes define presentation behavior in the JSON-LD schema.")],
      note="In IIIF 3.0, images are attached to Canvases via W3C Annotation objects with motivation='painting'."),

    Q("TEI Facsimile and surface/zone Elements",
      "How does the TEI <code>&lt;facsimile&gt;</code> element establish line-level correspondence with a high-resolution manuscript image?",
      correct=("A <code>&lt;surface&gt;</code> defines the page coordinates, child <code>&lt;zone&gt;</code> elements define bounding boxes for specific lines, and <code>&lt;lb facs=\"#zone_id\"/&gt;</code> links transcription lines to those zones.",
               "Correct. TEI facsimile markup uses @facs XML ID pointers to link specific textual elements (<p>, <l>, <lb>) to spatial <zone> coordinates."),
      wrong=[("By embedding binary image data directly into the middle of Greek words.",
              "Incorrect. TEI separates facsimile geometry from textual transcription, linking them cleanly via ID references."),
             ("By replacing the TEI header with an Adobe PDF wrapper.",
              "Incorrect. TEI maintains its own native <facsimile> architectural module."),
             ("By requiring scribes to write in HTML rather than ancient Greek.",
              "Incorrect. TEI models historical text structures independently of rendering formats.")],
      note="TEI <facsimile> uses <surface> and <zone> elements with @facs pointers to map text directly to image regions."),

    Q("Mirador Comparison Workspaces",
      "What core scholarly advantage does the Mirador digital viewer offer over traditional institutional library web viewers?",
      correct=("Mirador is an open, multi-window workspace that allows scholars to pull IIIF manifests from different libraries worldwide into side-by-side comparative panels with synchronized zoom and pan.",
               "Correct. Mirador breaks institutional silos by allowing manifests from Oxford, the Vatican, and the BNF to be collated in a single browser window."),
      wrong=[("Mirador automatically rewrites Greek manuscripts into modern French poetry.",
              "Incorrect. Mirador is a visual viewer and annotation environment, not a translation tool."),
             ("Mirador prevents students from taking notes during lecture.",
              "Incorrect. Mirador supports deep textual annotation and workspace configuration."),
             ("Mirador requires a proprietary annual license fee paid to Microsoft.",
              "Incorrect. Mirador is free, open-source software developed by the global IIIF community.")],
      note="Mirador enables side-by-side, synchronized multi-witness collation across disparate international repositories."),

    Q("Multispectral Imaging (MSI) in IIIF",
      "How can a palimpsest (a scraped and rewritten manuscript) be represented effectively within a single IIIF Canvas?",
      correct=("By attaching multiple image services (visible light, ultraviolet fluorescence, infrared, and false-color processed bands) as layered choices on the same Canvas, allowing users to cross-fade between spectral layers.",
               "Correct. IIIF canvases support multiple image layers, enabling seamless opacity blending between visible text and recovered undertext."),
      wrong=[("By physically cutting the parchment into thin slices.",
              "Incorrect. MSI is non-destructive optical imaging."),
             ("By deleting the undertext and keeping only the modern upper script.",
              "Incorrect. The primary goal of palimpsest imaging is recovering erased historical undertexts."),
             ("By converting the image into a single-channel audio waveform.",
              "Incorrect. Multispectral data consists of multi-wavelength visual photographic datasets.")],
      note="Layered IIIF Canvases allow real-time cross-fading and opacity adjustment across multispectral image bands."),

    Q("IIIF info.json Handshake",
      "What is the function of the <code>info.json</code> document requested by client viewers from a IIIF Image API server?",
      correct=("It delivers technical metadata about the image (maximum width and height, supported scale factors, tile dimensions, available color profiles, and service compliance level).",
               "Correct. The info.json handshake provides the client viewer with the exact geometry and capabilities of the image server before tile streaming begins."),
      wrong=[("It reveals the private home address of the manuscript curator.",
              "Incorrect. info.json contains image technical specifications, not personnel PII."),
             ("It contains the final exam questions for the academic course.",
              "Incorrect. It is a technical image descriptor document."),
             ("It compiles the Python server code into WebAssembly.",
              "Incorrect. info.json is a static JSON descriptor response.")],
      note="The info.json response informs the viewer of the image's dimensions, tile sizes, scale factors, and supported features."),

    Q("Decoupling Data from Presentation",
      "Why is the architectural separation of IIIF image hosting from scholarly annotation servers beneficial for long-term digital sustainability?",
      correct=("Libraries can maintain and upgrade their multi-terabyte image storage without breaking third-party scholarly annotations, which reference persistent URI coordinates rather than local server implementations.",
               "Correct. Decoupling image delivery from annotation storage ensures that research data remains durable and interoperable across software migrations."),
      wrong=[("Because image files become permanently unreadable after two years.",
              "Incorrect. Standard image formats remain readable, but coupled monolithic platforms suffer software rot."),
             ("Because digital humanities projects are prohibited from using web servers.",
              "Incorrect. Open web architectures depend on distributed microservices and standardized APIs."),
             ("Because decoupling automatically deletes all copyright notices.",
              "Incorrect. Rights and attribution are explicitly preserved in IIIF manifests.")],
      note="Decoupled IIIF architectures ensure that scholarly annotations remain valid even when repository hosting backends evolve."),

    Q("JSON-LD and Shared Ontologies",
      "Why does IIIF Presentation API 3.0 use JSON-LD (JavaScript Object Notation for Linked Data) with standard <code>@context</code> definitions?",
      correct=("JSON-LD combines developer-friendly JSON syntax with RDF semantics, enabling machines to understand that terms like 'Canvas', 'Annotation', and 'Manifest' map to formal Linked Data ontologies.",
               "Correct. The @context URI maps standard JSON keys to unambiguous semantic web URIs, bridging web development and knowledge graphs."),
      wrong=[("Because JSON-LD is the only programming language understood by the Linux operating system kernel.",
              "Incorrect. JSON-LD is a data serialization format, not an operating system language."),
             ("Because standard JSON is illegal in academic publications.",
              "Incorrect. JSON-LD extends JSON with semantic context mappings."),
             ("Because JSON-LD encrypts database records to prevent search engine indexing.",
              "Incorrect. Linked Data explicitly maximizes machine discoverability and indexing.")],
      note="JSON-LD bridges clean JSON data interchange with formal RDF Linked Data ontologies via @context."),
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
bank_file = Path("scripts/banks/quiz_03.py")
bank_file.write_text(Path(__file__).read_text(encoding="utf-8"), encoding="utf-8")
print(f"Wrote bank file {bank_file}")

xml_content = render_quiz(TOPIC, TITLE, QUESTIONS)
ET.fromstring(xml_content)

for p in [dist_mod / "09_Quiz.xml", src_mod / "09_Quiz.xml"]:
    p.write_text(xml_content, encoding="utf-8")
    print(f"Wrote and validated {p}")
