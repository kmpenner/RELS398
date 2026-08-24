#!/usr/bin/env python3
"""RELS 398: Google Scholar Labs Search Runner

Executes Stage 1 queries against Google Scholar Labs via Chrome CDP (port 9222),
parses synthesized paper cards, saves per-topic JSON, and compiles the master
markdown catalogue in src/SCHOLAR_LABS_PAPERS.md.
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

HOME_URL = "https://scholar.google.com/scholar_labs/search?hl=en"
CDP_URL = "http://127.0.0.1:9222"

EXTRACT_JS = """
() => {
  const container = document.querySelector('main') || document.body;
  const headings = Array.from(container.querySelectorAll('h3'));
  const out = [];
  headings.forEach((h, idx) => {
    const next = headings[idx + 1];
    const range = document.createRange();
    range.setStartBefore(h);
    if (next) range.setEndBefore(next);
    else range.setEndAfter(container.lastElementChild || container);
    const frag = range.cloneContents();
    const wrapper = document.createElement('div');
    wrapper.appendChild(frag);
    const titleLink = h.querySelector('a');
    const links = Array.from(wrapper.querySelectorAll('a')).map(a => ({
      text: (a.textContent || '').trim(),
      href: a.href,
    }));
    out.push({
      title_raw: (h.innerText || '').trim(),
      title_link: titleLink ? titleLink.href : null,
      raw_text: wrapper.innerText || '',
      links,
    });
  });
  return out;
}
"""

LABEL_LINE = re.compile(r"^([A-Z][^:]{2,60}):\s+(.*)$")
CITED_BY = re.compile(r"^Cited by (\d+)$")


def parse_block(block):
    title = re.sub(r"^(\[(PDF|BOOK|HTML|CITATION)\]\s*)+", "", block["title_raw"], flags=re.I).strip()
    lines = [l.strip() for l in block["raw_text"].split("\n") if l.strip()]

    meta = None
    summary = None
    key_points = []
    for line in lines:
        if line in ("Save", "Cite", "More", "Fewer") or (line.startswith("[") and line.endswith("]")):
            continue
        if meta is None and (" - " in line and re.search(r"\b(19|20)\d{2}\b", line)):
            meta = line
            continue
        if line == "Save":
            break
        m = LABEL_LINE.match(line)
        if m:
            key_points.append({"label": m.group(1).strip(), "text": m.group(2).strip()})
        elif summary is None and meta is not None:
            summary = line

    cited_by = None
    cited_by_link = None
    pdf_link = None

    for link in block["links"]:
        t = link["text"]
        if "[PDF]" in t or link["href"].lower().endswith(".pdf"):
            pdf_link = link["href"]
        m = CITED_BY.match(t)
        if m:
            cited_by = int(m.group(1))
            cited_by_link = link["href"]

    return {
        "title": title,
        "title_link": block["title_link"],
        "pdf_link": pdf_link,
        "authors_venue_year": meta,
        "summary": summary,
        "key_points": key_points,
        "cited_by": cited_by,
        "cited_by_link": cited_by_link,
    }


def render_markdown(catalogue_path: Path, out_dir: Path, query_items: list[dict]):
    md = [
        "# RELS 398 / ENGL 398: Google Scholar Labs Curated Papers & Research Evidence\n",
        "This master catalogue records the peer-reviewed papers, AI syntheses, and PDF links discovered via Google Scholar Labs for all 13 weekly topics in **RELS 398.10 / ENGL 398.10 (ST: Digital Methods for Historical Documents)**.\n",
        "---\n"
    ]
    for item in query_items:
        qid = item["id"]
        json_file = out_dir / f"q{qid}.json"
        if not json_file.exists():
            continue
        data = json.loads(json_file.read_text(encoding="utf-8"))
        results = data.get("results", [])
        md.append(f"## Topic {qid}: {data['title']}\n")
        md.append(f"**Scholar Labs Inquiry:** *\"{data['query']}\"*\n")
        md.append(f"**Discovered Literature ({len(results)} items):**\n")
        for i, r in enumerate(results, 1):
            pdf_badge = f" [[PDF Direct Link]({r['pdf_link']})]" if r.get("pdf_link") else ""
            cb = f" · *Cited by {r['cited_by']}*" if r.get("cited_by") is not None else ""
            md.append(f"### {i}. [{r['title']}]({r['title_link']}){pdf_badge}{cb}")
            if r.get("authors_venue_year"):
                md.append(f"*{r['authors_venue_year']}*")
            if r.get("summary"):
                md.append(f"\n> {r['summary']}\n")
            if r.get("key_points"):
                for kp in r["key_points"]:
                    md.append(f"- **{kp['label']}:** {kp['text']}")
            md.append("")
        md.append("---\n")
    catalogue_path.write_text("\n".join(md), encoding="utf-8")
    print(f"Updated master catalogue at {catalogue_path}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--queries", default="raw/scholar_labs_results/queries_course.json")
    ap.add_argument("--out-dir", default="raw/scholar_labs_results")
    ap.add_argument("--md", default="src/SCHOLAR_LABS_PAPERS.md")
    ap.add_argument("--cdp", default=CDP_URL)
    ap.add_argument("--topics", help="Comma-separated IDs to run, e.g. '01,02,03'")
    args = ap.parse_args()

    course_root = Path(__file__).resolve().parent.parent
    queries_file = course_root / args.queries
    out_dir = course_root / args.out_dir
    md_file = course_root / args.md
    out_dir.mkdir(parents=True, exist_ok=True)

    items = json.loads(queries_file.read_text(encoding="utf-8"))
    if args.topics:
        selected_ids = {t.strip().zfill(2) for t in args.topics.split(",")}
        items_to_run = [it for it in items if it["id"].zfill(2) in selected_ids]
    else:
        items_to_run = items

    print(f"Connecting to Chrome over CDP at {args.cdp}...")
    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp(args.cdp)
        except Exception as e:
            sys.exit(f"Error connecting to CDP at {args.cdp}: {e}\nEnsure Chrome is running with --remote-debugging-port=9222")

        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.new_page()

        for it in items_to_run:
            qid = it["id"]
            title = it["title"]
            query = it["query"]
            print(f"\n[Topic {qid}] {title}")
            print(f"         Query: {query[:95]}...")

            try:
                page.goto(HOME_URL, timeout=30000)
                page.wait_for_timeout(1500)
                box = page.locator("textarea, input[type='text']").first
                box.click()
                box.type(query, delay=15)
                page.wait_for_timeout(500)
                page.keyboard.press("Enter")

                print("         Waiting for Scholar Labs results...", end="", flush=True)
                prev_count = 0
                stable_cycles = 0
                for _ in range(25):  # up to 50s
                    page.wait_for_timeout(2000)
                    headings = page.locator("h3").count()
                    body_text = page.locator("body").inner_text()
                    if headings > 0 and headings == prev_count:
                        stable_cycles += 1
                        if stable_cycles >= 2:  # count stable for 4s
                            break
                    elif headings > 0:
                        prev_count = headings
                        stable_cycles = 0
                    if "Found" in body_text and "relevant" in body_text:
                        break
                    if "Scholar Labs is currently not designed" in body_text:
                        print(" (Query not supported by Labs)")
                        break
                    print(".", end="", flush=True)

                page.wait_for_timeout(1500)
                raw_blocks = page.evaluate(EXTRACT_JS)
                results = [parse_block(b) for b in raw_blocks]
                print(f" -> Found {len(results)} cards.")

                data = {
                    "id": qid,
                    "topic": it.get("topic", f"Topic_{qid}"),
                    "title": title,
                    "query": query,
                    "results_count": len(results),
                    "results": results
                }
                out_file = out_dir / f"q{qid}.json"
                out_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
                print(f"         Saved {out_file.name}")

            except Exception as ex:
                print(f"\n         !! Error on Topic {qid}: {ex}")

            time.sleep(3.5)

        page.close()

    render_markdown(md_file, out_dir, items)
    print("\nAll queried topics processed successfully.")


if __name__ == "__main__":
    main()
