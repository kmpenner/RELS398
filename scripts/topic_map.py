#!/usr/bin/env python3
"""RELS 398: Topic number -> literature folder, report destination, and Stage 2 prompt extractor."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TOPIC_MAP = {
    1: "Module_01_Orientation",
    2: "Module_02_Cataloguing",
    3: "Module_03_IIIF_Imaging",
    4: "Module_04_Transcription",
    5: "Module_05_Reconciliation",
    6: "Module_06_Normalization",
    7: "Module_07_Collation",
    8: "Module_08_Apparatus",
    9: "Module_09_Lemmatization",
    10: "Module_10_Consolidation",
    11: "Module_11_Alignment",
    12: "Module_12_Commentary",
    13: "Module_13_Publication",
}
MODULE_MAP = TOPIC_MAP


# Lessons are one per class meeting, following the three-step comparative cycle
# (Tue manual / Wed deterministic / Fri AI-assisted). Weeks 1, 3, 5, 10 and 13
# depart from that pattern and say so in the schedule, so their lesson counts
# differ. Derived from src/syllabus/RELS 398 Schedule.tex -- keep in sync with it.
LESSON_MAP = {
    1:  ["1.1", "1.2"],                 # orientation week; no cycle
    2:  ["2.1", "2.2", "2.3"],
    3:  ["3.1", "3.2", "3.3"],          # infrastructure week; no cycle
    4:  ["4.1", "4.2", "4.3"],
    5:  ["5.1", "5.2"],                 # Wed Sep 30 closed; two-step by design
    6:  ["6.1", "6.2", "6.3"],
    7:  ["7.1", "7.2", "7.3"],
    8:  ["8.1", "8.2", "8.3"],
    9:  ["9.1", "9.2", "9.3"],
    10: ["10.1", "10.2"],               # Wed Nov 11 closed; consolidation
    11: ["11.1", "11.2", "11.3"],
    12: ["12.1", "12.2", "12.3"],
    13: ["13.1", "13.2", "13.3"],       # studio weeks; no cycle
}


def lessons(topic_num: int) -> list[str]:
    """Lesson ids for a topic, in meeting order."""
    return LESSON_MAP.get(topic_num, [])


def content_path(topic_num: int, lesson_id: str) -> Path:
    folder = TOPIC_MAP.get(topic_num, f"Module_{topic_num:02d}")
    return (ROOT / "src/modules" / folder /
            f"03a_Lesson_{lesson_id}_Lesson_Content.md")


def lit_dir(topic_num: int) -> Path:
    folder = TOPIC_MAP.get(topic_num, f"Module_{topic_num:02d}")
    return ROOT / "raw/readings" / folder


def report_path(topic_num: int) -> Path:
    folder = TOPIC_MAP.get(topic_num, f"Module_{topic_num:02d}")
    return ROOT / "src/research_reports" / f"{folder}_Deep_Research_Report.md"


def extract_prompt_for_topic(topic_num: int, prompts_file: Path = None) -> str:
    if prompts_file is None:
        prompts_file = ROOT / "src/RESEARCH_PROMPTS.md"
    content = prompts_file.read_text(encoding="utf-8")
    blocks = content.split("## Topic ")
    for b in blocks[1:]:
        header = b.split("\n")[0]
        try:
            num = int(header.split(":")[0].strip())
        except Exception:
            continue
        if num == topic_num:
            if "### Stage 2: Gemini Deep Research Prompt" in b:
                stage2 = b.split("### Stage 2: Gemini Deep Research Prompt")[1]
                parts = stage2.split("```text")
                if len(parts) > 1:
                    return parts[1].split("```")[0].strip()
    return ""


if __name__ == "__main__":
    print("Testing prompt extraction for all 13 topics:")
    for t in range(1, 14):
        p = extract_prompt_for_topic(t)
        folder = lit_dir(t)
        pdfs = list(folder.glob("*.pdf")) if folder.exists() else []
        print(f"Topic {t:02d} ({TOPIC_MAP[t]}): prompt length {len(p)} chars | {len(pdfs)} PDFs in {folder.name}")
