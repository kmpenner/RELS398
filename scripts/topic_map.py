#!/usr/bin/env python3
"""RELS 398: Topic number -> literature folder, report destination, and Stage 2 prompt extractor."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TOPIC_MAP = {
    1: "Topic_01_Orientation",
    2: "Topic_02_Cataloguing",
    3: "Topic_03_IIIF_Imaging",
    4: "Topic_04_Transcription",
    5: "Topic_05_Reconciliation",
    6: "Topic_06_Normalization",
    7: "Topic_07_Collation",
    8: "Topic_08_Apparatus",
    9: "Topic_09_Lemmatization",
    10: "Topic_10_Consolidation",
    11: "Topic_11_Alignment",
    12: "Topic_12_Commentary",
    13: "Topic_13_Publication",
}


def lit_dir(topic_num: int) -> Path:
    folder = TOPIC_MAP.get(topic_num, f"Topic_{topic_num:02d}")
    return ROOT / "raw/readings" / folder


def report_path(topic_num: int) -> Path:
    folder = TOPIC_MAP.get(topic_num, f"Topic_{topic_num:02d}")
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
