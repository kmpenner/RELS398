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
    <h4 style="color: #c2593f; margin-top: 0;">Workshop: Anchoring Your Page to Its Image</h4>
    <p><strong>Overview:</strong> Your TEI header describes your document. Nothing in your file yet points at a picture of it. In this workshop you attach the image: you establish which image you are entitled to use, measure it, write a TEI <code>&lt;facsimile&gt;</code> that maps regions of that image, and link those regions to your text.</p>
    <p>This is the Module 3 version of the three-step cycle. You will get your coordinates twice &mdash; once by eye and once from a tool that measures instead of guessing &mdash; and the difference between the two is part of what you submit.</p>
    <p><strong>A note on IIIF.</strong> Whether your holding institution publishes IIIF is outside your control and differs for each of your four documents. So the manifest task below is written as a choice: if your repository serves IIIF, examine what it actually gives you; if it does not, that is a finding about the state of your document's digitization, and you write it up as one. Neither path is worth more marks.</p>
    <p><strong>Deliverables:</strong> a validated TEI <code>&lt;facsimile&gt;</code> block, an image provenance record, your coordinate comparison, and a 300&ndash;500 word reflection. Post them for peer review.</p>
    <p><strong>Deadlines:</strong> the submission and assessment dates shown in this workshop's Moodle settings.</p>
</div>"""

ws_sub = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Submission Instructions</h4>
    <p style="font-size:0.93rem; color:#475569;">Work on the <strong>same one page</strong> you catalogued in Workshop 2. Everything below goes in your project repository and gets committed as you work.</p>
    <ol>
        <li><strong>Get the best image you are allowed to use, and say where it came from.</strong> In most cases this is the holding institution's digitized surrogate. Record, in a file called <code>IMAGE_PROVENANCE.md</code>:
            <ul>
                <li>the URL you downloaded it from, and the date;</li>
                <li>the file name, format, and file size;</li>
                <li>whether a higher-resolution version exists that you did not take, and why (paywall, login, reading-room only, no larger version offered);</li>
                <li>if you photographed or scanned the object yourself: the device, the lighting, whether a ruler or colour reference was in frame, and any handling constraint you worked under.</li>
            </ul>
        </li>
        <li><strong>Measure the image twice.</strong>
            <ul>
                <li><em>By eye:</em> open it in a viewer and write down the width and height you see reported.</li>
                <li><em>By tool:</em> run <code>file yourimage.jpg</code>, or <code>identify -format "%w x %h" yourimage.jpg</code> if you have ImageMagick, or <code>python3 labs/make_surface.py yourimage.jpg</code>.</li>
                <li><em>If your repository serves IIIF:</em> fetch the image service's <code>info.json</code> and record the <code>width</code> and <code>height</code> it reports for the master. Note whether that master is larger than your download. <strong>If it does not serve IIIF, record that you checked and where you looked</strong> &mdash; a verified absence is a result, and it earns the same credit.</li>
            </ul>
            Record all the numbers you got, including any that disagreed.
        </li>
        <li><strong>Write the TEI <code>&lt;facsimile&gt;</code>.</strong> In your <code>witness.xml</code>, between <code>&lt;/teiHeader&gt;</code> and <code>&lt;text&gt;</code>, add:
            <ul>
                <li>one <code>&lt;surface&gt;</code> with an <code>@xml:id</code> and the real <code>@ulx @uly @lrx @lry</code> of your image;</li>
                <li>a <code>&lt;graphic&gt;</code> pointing at the image (a relative path if the file is in your repository, the full URL if it is not);</li>
                <li><strong>at least three <code>&lt;zone&gt;</code> elements</strong> marking features that matter on <em>your</em> document &mdash; a heading, a signature, a seal, a stamp, a column, a correction, a printer's line, an area of damage. Give each a <code>@type</code> you can defend;</li>
                <li>at least one link from your text into the facsimile, using <code>@facs</code> on <code>&lt;pb&gt;</code>, <code>&lt;lb&gt;</code>, or <code>&lt;div&gt;</code>. The value starts with <code>#</code>.</li>
            </ul>
            Validate against <code>msdesc.rng</code> and drive the Problems panel to <strong>0 errors</strong>. Remember that the schema cannot check whether a <code>@facs</code> pointer aims at an id that exists &mdash; check that yourself.
        </li>
        <li><strong>Settle the rights question in one short section</strong> of <code>IMAGE_PROVENANCE.md</code>. The rights in the object and the licence on the digital image are separate. State the licence or terms of use, quote the credit line the institution requires, and answer one question: <em>are you permitted to produce a cropped or altered derivative of this image?</em> If you are not, say what that rules out and note that zones point at regions without creating a new file.</li>
        <li><strong>Choose one and do it:</strong>
            <ul>
                <li><em>If your document is served by IIIF:</em> open its manifest, and report what it contains &mdash; how many Canvases, what the labels are, what metadata fields the institution chose to publish, and one thing you would want that is missing.</li>
                <li><em>If it is not:</em> write the case for what a manifest of your page would need to contain, and describe concretely what is currently lost by its absence &mdash; what can a reader of your edition not do that a reader of a IIIF-served edition can?</li>
            </ul>
        </li>
        <li><strong>Write a 300&ndash;500 word reflection</strong> on this question: <em>where did your eye disagree with the tool, and which of you was wrong?</em> Report your coordinate numbers, say what caused each discrepancy, and then address the part no tool settles &mdash; how you decided which three regions deserved a zone, and what a reader can check because you drew them.</li>
        <li><strong>Submit:</strong> your <code>&lt;facsimile&gt;</code> block, your <code>IMAGE_PROVENANCE.md</code>, and the reflection. Commit your work as you go, not in one commit at the end.</li>
    </ol>
    <p style="margin-bottom:0;"><strong>Note on fit.</strong> The vocabulary of this module &mdash; folio, recto, opening, leaf &mdash; comes from bound manuscripts, and most of your documents are not bound manuscripts. Use the terms that honestly describe your object, and where you have to make a judgement call, write one sentence saying why. Those sentences are graded.</p>
</div>"""

ws_assess = """<div class="card p-3 mb-3" style="padding: 1.25rem;">
    <h4 style="margin-top: 0;">Peer Assessment Rubric (10 pts)</h4>
    <p style="font-size:0.92rem; color:#475569; margin-top:0;">Peer review is blind and constructive: for each criterion, say what earns credit and name one specific improvement. "Looks good" earns nothing.</p>
    <ul>
        <li><strong>Facsimile Validity &amp; Fit (4 pts):</strong> The block validates, and the coordinates are coherent &mdash; each zone lies inside its surface, and the four attributes are corners rather than width and height. Every <code>@facs</code> points at an <code>xml:id</code> that exists; check this by eye, because the schema does not. The three zones mark features that genuinely exist on <em>this</em> object, with defensible <code>@type</code> values. A zone invented to fill a quota, or a <code>@type</code> borrowed from codicology that does not apply, scores zero on that zone.</li>
        <li><strong>Image Provenance &amp; Measurement (3 pts):</strong> The source URL, date, format, and dimensions are recorded, and the measurements are reported with any disagreement between them rather than silently reconciled. The IIIF check is answered either way, with evidence of where the student looked. Credit the honesty of the record: "the only public image is 900 px wide and too small to read the marginal note" is a stronger submission than a tidy one that hides the limitation.</li>
        <li><strong>Rights &amp; Reflection (3 pts):</strong> Object rights and image licence are treated as separate questions, the terms are quoted rather than paraphrased from memory, and the derivative question is answered directly. The reflection reports real numbers, diagnoses the cause of each discrepancy, and says how the zone choices were made. A reflection that only praises the tool's accuracy has missed the point: the tool cannot choose the zones.</li>
    </ul>
    <p style="margin-bottom:0; font-size:0.92rem; color:#475569;"><strong>Marking guide:</strong> 9&ndash;10 exceptional; 7&ndash;8 solid and defensible; 5&ndash;6 complete but uncritical (typically: a valid block, real numbers, but no account of judgement); below 5 means a criterion is unaddressed or the markup does not validate.</p>
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
