import sys
from pathlib import Path
import xml.etree.ElementTree as ET

shared_dir = Path(__file__).resolve().parent.parent.parent / "shared" / "scripts"
sys.path.insert(0, str(shared_dir))
from question_bank import Q

TOPIC = "Module_01_Orientation"
TITLE = "Module 01 Knowledge Check Quiz"

QUESTIONS = [
    Q("Git DAG and Textual Transmission",
      "How does Git's Directed Acyclic Graph (DAG) commit model structurally correspond to the transmission of ancient manuscript traditions?",
      correct=("Both model textual history as a branching sequence of discrete states descending from ancestral nodes with attributed modifications.",
               "Correct. The Git DAG models historical descent with modification, exactly mirroring stemmatological branching in manuscript transmission."),
      wrong=[("Both rely on a single central authoritative server that dictates the canonical reading to all subscribers.",
              "Incorrect. Git is inherently distributed and peer-to-peer, just like historical manuscript copying prior to print monopolies."),
             ("Both automatically erase previous textual states whenever a new correction is introduced.",
              "Incorrect. Git is strictly append-only and preserves the complete history of previous states."),
             ("Both require mechanical typecasting that standardizes every character into fixed physical blocks.",
              "Incorrect. This describes print typography, not graph-based textual transmission.")],
      note="Git's DAG formally mirrors stemmatology: directed branches of textual descent with cumulative, attributable modifications."),

    Q("Snapshots vs. Diff Deltas",
      "How does Git internally store the state of files across successive commits compared to older version control systems like RCS or CVS?",
      correct=("Git stores each commit as a complete snapshot of the project tree (with unchanged files referencing existing blob objects), rather than a delta list of line-by-line diffs.",
               "Correct. Git commits point to a complete root tree object, giving each commit an immutable, self-contained record of the entire repository state."),
      wrong=[("Git stores only the line-by-line textual differences (deltas) and computes full files on demand by replaying the history.",
              "Incorrect. Older VCS tools like CVS/SCCS used delta chains; Git uses root tree snapshots of blob objects."),
             ("Git compresses all files into a single flat binary database that cannot be inspected without internet connectivity.",
              "Incorrect. Git repositories are fully local and store objects in a content-addressable object store under .git/objects."),
             ("Git only tracks file metadata (timestamps and filenames) while leaving content history to external backup utilities.",
              "Incorrect. Git tracks the complete content of every tracked file via cryptographic hashing.")],
      note="Git stores commits as full repository tree snapshots rather than cumulative delta diffs, ensuring atomic integrity across edits."),

    Q("Cryptographic Hashes and Tamper-Evidence",
      "Why is Git's content-addressable object database (using SHA-1/SHA-256 hashes) vital for digital philology and critical editions?",
      correct=("Because any change to a single character, diacritic, or commit parent alters the resulting hash, guaranteeing an immutable, tamper-evident audit trail.",
               "Correct. The cryptographic hash function ensures that any modification to textual data or historical metadata produces a completely different object ID, preventing silent corruption."),
      wrong=[("Because cryptographic hashes automatically translate ancient Greek dialects into modern English.",
              "Incorrect. Hashes are mathematical checksums, not translation algorithms."),
             ("Because hashes encrypt the text so that only authorized journal editors can view the transcription.",
              "Incorrect. Git hashing is for content identification and integrity verification, not encryption or access restriction."),
             ("Because using hashes eliminates the need to record the scholar's name or email in the commit metadata.",
              "Incorrect. Commit objects explicitly record the author and committer metadata alongside the tree hash.")],
      note="Content-addressable hashing guarantees tamper-evident provenance for every transcribed character and editorial decision."),

    Q("The Three Trees of Git",
      "In standard Git architecture, which component represents the intermediate staging area where changes are prepared before being committed to repository history?",
      correct=("The Index (or Staging Area), which allows scholars to assemble granular, focused commits rather than dumping all working directory changes at once.",
               "Correct. The Index bridges the local working directory and the permanent repository history, enabling precise, modular commit curation."),
      wrong=[("The Working Tree, where untracked and uncommitted files are permanently sealed against modification.",
              "Incorrect. The Working Tree is the active directory on the filesystem where files are edited."),
             ("The Remote Origin, which stores backup files on GitHub or GitLab.",
              "Incorrect. Remote origin is a remote tracking repository, not the local intermediate staging area."),
             ("The Reflog, which permanently publishes student grades to the university registrar.",
              "Incorrect. The reflog is a local tracking log of HEAD pointer movements.")],
      note="The Git Index (Staging Area) allows editors to craft precise, atomic commits reflecting specific philological interventions."),

    Q("Branching and the HEAD Pointer",
      "When creating a new branch in Git (e.g., <code>git checkout -b witness-alpha</code>), what is physically created in the repository database?",
      correct=("A lightweight 41-byte pointer file holding the 40-character commit hash of the current HEAD, with no duplication of source files.",
               "Correct. Branches in Git are simple, lightweight reference pointers to commit objects, making branching instantaneous and cheap."),
      wrong=[("A complete duplicate copy of every file in the project folder stored in a hidden partition.",
              "Incorrect. Git does not duplicate project files when creating branches; branches are simply pointer references."),
             ("A new remote web server hosted in the cloud dedicated to that branch.",
              "Incorrect. Branch creation is entirely local and does not require cloud infrastructure."),
             ("A locked, read-only PDF export of the working directory.",
              "Incorrect. Branches are fully active, editable lines of development.")],
      note="Git branches are lightweight pointer files that point to specific commit hashes, allowing effortless multi-witness collation lines."),

    Q("Merge Conflicts as Philological Divergence",
      "Under what conditions does Git halt an automatic merge and signal a merge conflict when combining two witness branches?",
      correct=("When both branches have modified the exact same line(s) of a file differently since their common ancestor commit.",
               "Correct. When two divergent branches alter the same line range, Git cannot deterministically decide which reading to privilege and requires editorial intervention."),
      wrong=[("Whenever two branches contain files with Greek Unicode characters.",
              "Incorrect. Git handles UTF-8 encoded Greek without conflict as long as edits do not overlap on identical lines."),
             ("Whenever a branch has more than three commits in its log history.",
              "Incorrect. Git effortlessly merges long branch histories via recursive three-way merge algorithms."),
             ("Only when the remote server loses internet connectivity during the merge command.",
              "Incorrect. Merges are executed locally in the working directory.")],
      note="Merge conflicts occur when divergent branches modify identical lines, requiring the textual critic to resolve variant readings."),

    Q("Unicode Code Points and Hexadecimal Notation",
      "In the Unicode Standard, how is a specific character uniquely identified across computational architectures?",
      correct=("By a unique integer code point conventionally formatted in hexadecimal as <code>U+XXXX</code> (e.g., <code>U+03B1</code> for GREEK SMALL LETTER ALPHA).",
               "Correct. Unicode assigns an immutable abstract code point (U+XXXX) to every distinct grapheme across world scripts."),
      wrong=[("By its pixel coordinate in the Microsoft Windows font registry.",
              "Incorrect. Unicode defines abstract character numbers, independent of font glyphs or display pixels."),
             ("By the sequential order in which the character appears in the Homeric epics.",
              "Incorrect. Unicode code points follow architectural block allocations, not literary chronology."),
             ("By a proprietary ASCII escape sequence licensed by Adobe Systems.",
              "Incorrect. Unicode is an open, international encoding standard maintained by the Unicode Consortium.")],
      note="Unicode identifies characters via universal, abstract hexadecimal code points (e.g., U+03B1 for alpha)."),

    Q("NFC vs. NFD Normalization in Polytonic Greek",
      "What is the operational difference between Unicode Normalization Form C (NFC) and Normalization Form D (NFD)?",
      correct=("NFC uses precomposed characters where available (e.g., single code point U+1F00 for ἁ), whereas NFD decomposes characters into a base letter plus separate combining diacritical marks (e.g., U+03B1 + U+0314).",
               "Correct. NFC (Canonical Composition) combines base characters and accents into single precomposed codepoints; NFD (Canonical Decomposition) separates them into atomic building blocks."),
      wrong=[("NFC converts Greek text into Latin transliteration, whereas NFD converts Latin into Cyrillic.",
              "Incorrect. Normalization forms alter internal byte representation within the same script, not language translation."),
             ("NFC compresses text files into ZIP archives, whereas NFD expands them into uncompressed XML.",
              "Incorrect. Normalization has nothing to do with archive compression."),
             ("NFC is designed exclusively for Hebrew text, whereas NFD is designed exclusively for Latin script.",
              "Incorrect. Normalization forms apply universally across all Unicode-encoded writing systems.")],
      note="NFC favours precomposed characters (U+1F00) while NFD separates base letters from combining diacritics (U+03B1 + U+0314)."),

    Q("The Silent Danger of Un-Normalized Greek Text",
      "Why will a Python regex search for the Greek word <code>ἁμαρτία</code> silently fail if the search query is in NFC and the manuscript corpus is in NFD?",
      correct=("Because string comparison operates on underlying byte sequences; even though NFC and NFD render identically on screen (canonically equivalent), their code points and byte streams differ.",
               "Correct. Visual equivalence does not equal binary equality. A string search compares numerical byte values, so decomposed and precomposed forms fail exact matches unless normalized first."),
      wrong=[("Because Python does not support non-ASCII character strings in regular expressions.",
              "Incorrect. Python 3 strings are fully Unicode-compliant by default."),
             ("Because NFD text causes the operating system graphics card to crash during text rendering.",
              "Incorrect. Operating system font shaping engines render both forms correctly."),
             ("Because Greek vowels lose their semantic definition when combined with breathing marks.",
              "Incorrect. The semantic meaning is identical; the underlying numeric representation is what differs.")],
      note="Visual identity does not guarantee binary identity: NFC and NFD byte streams differ, causing silent search and collation failures."),

    Q("UTF-8 Variable-Length Encoding",
      "How are Polytonic Greek characters in the Greek and Coptic block (U+0370–U+03FF) and Greek Extended block (U+1F00–U+1FFF) encoded in UTF-8?",
      correct=("As multi-byte sequences (2 bytes for Basic Greek, 3 bytes for Greek Extended), where each byte begins with specific header bits defining the sequence length.",
               "Correct. UTF-8 is a variable-length encoding: standard ASCII uses 1 byte, Basic Greek uses 2 bytes, and Greek Extended precomposed characters use 3 bytes."),
      wrong=[("As fixed 4-byte integers stored in Big-Endian binary arrays with no compression.",
              "Incorrect. This describes UTF-32, not variable-length UTF-8."),
             ("As single 8-bit ASCII characters where accents are ignored.",
              "Incorrect. 8-bit ASCII cannot encode the vast inventory of polytonic Greek characters."),
             ("As proprietary binary blobs accessible only within Microsoft Word.",
              "Incorrect. UTF-8 is the universal open standard of the modern web and digital humanities.")],
      note="UTF-8 encodes Basic Greek in 2 bytes and Greek Extended polytonic characters in 3 bytes."),
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

if __name__ == "__main__":
    # Also write scripts/banks/quiz_01.py
    bank_file = Path("scripts/banks/quiz_01.py")
    bank_file.write_text(Path(__file__).read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Wrote bank file {bank_file}")

    xml_content = render_quiz(TOPIC, TITLE, QUESTIONS)
    ET.fromstring(xml_content) # validate XML

    for p in [Path("dist/moodle/Module_01_Orientation/09_Quiz.xml"), Path("src/modules/Module_01_Orientation/09_Quiz.xml")]:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(xml_content, encoding="utf-8")
        print(f"Wrote and validated {p}")
