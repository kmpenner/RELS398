#!/usr/bin/env python3
"""Generic Google Scholar Labs runner: reads a queries JSON, writes per-query JSON + a markdown catalogue.

Parsing logic lifted verbatim from 117/scripts/batch_scholar_search.py; the only
change is that the query list and output dir are arguments rather than the RELS 117
lesson-card HTML.
"""
import argparse, json, re, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

HOME_URL = "https://scholar.google.com/scholar_labs/search?hl=en"

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
      text: (a.textContent || '').trim(), href: a.href,
    }));
    out.push({title_raw: (h.innerText||'').trim(), title_link: titleLink?titleLink.href:null,
             raw_text: wrapper.innerText||'', links});
  });
  return out;
}
"""
LABEL_LINE = re.compile(r"^([A-Z][^:]{2,60}):\s+(.*)$")
CITED_BY = re.compile(r"^Cited by (\d+)$")

def parse_block(block):
    title = re.sub(r"^(\[(PDF|BOOK|HTML|CITATION)\]\s*)+", "", block["title_raw"], flags=re.I).strip()
    lines = [l.strip() for l in block["raw_text"].split("\n") if l.strip()]
    meta = summary = None; key_points = []
    for line in lines:
        if line in ("Save","Cite","More","Fewer") or (line.startswith("[") and line.endswith("]")):
            continue
        if meta is None and (" - " in line and re.search(r"\b(19|20)\d{2}\b", line)):
            meta = line; continue
        if line == "Save": break
        m = LABEL_LINE.match(line)
        if m: key_points.append({"label": m.group(1).strip(), "text": m.group(2).strip()})
        elif summary is None and meta is not None: summary = line
    cited_by = cited_by_link = pdf_link = None
    for link in block["links"]:
        if "[PDF]" in link["text"]: pdf_link = link["href"]
        m = CITED_BY.match(link["text"])
        if m: cited_by = int(m.group(1)); cited_by_link = link["href"]
    return {"title": title, "title_link": block["title_link"], "pdf_link": pdf_link,
            "authors_venue_year": meta, "summary": summary, "key_points": key_points,
            "cited_by": cited_by, "cited_by_link": cited_by_link}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--queries", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--md", required=True)
    ap.add_argument("--heading", default="Google Scholar Labs results")
    ap.add_argument("--cdp", default="http://127.0.0.1:9222")
    a = ap.parse_args()

    items = json.loads(Path(a.queries).read_text())
    out_dir = Path(a.out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    md = [f"# {a.heading}\n"]

    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp(a.cdp)
        except Exception as e:
            print(f"CDP connect failed: {e}\nRun Chrome with --remote-debugging-port=9222"); sys.exit(1)
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.new_page()
        for it in items:
            print(f"[{it['id']}] {it['title']}\n      {it['query'][:90]}...", flush=True)
            try:
                page.goto(HOME_URL, timeout=30000)
                box = page.get_by_placeholder("Ask Scholar")
                if not box.is_visible(timeout=5000):
                    box = page.locator("textarea, input[type='text']").first
                box.click(); box.fill(it["query"]); page.keyboard.press("Enter")
                try:
                    page.wait_for_selector("text=/Found \\d+ relevant results?/", timeout=90000)
                except Exception:
                    print("      (count header timed out; extracting current DOM)")
                page.wait_for_timeout(2000)
                results = [parse_block(b) for b in page.evaluate(EXTRACT_JS)]
                print(f"      -> {len(results)} cards", flush=True)
                (out_dir / f"q{it['id']}.json").write_text(json.dumps(
                    {**it, "results_count": len(results), "results": results}, indent=2))
                md.append(f"## {it['id']}. {it['title']}\n")
                md.append(f"**Inquiry:** *\"{it['query']}\"*\n")
                md.append(f"**{len(results)} results**\n")
                for i, r in enumerate(results, 1):
                    pdf = f" [[PDF]({r['pdf_link']})]" if r.get("pdf_link") else ""
                    md.append(f"### {i}. [{r['title']}]({r['title_link']}){pdf}")
                    if r.get("authors_venue_year"): md.append(f"*{r['authors_venue_year']}*")
                    if r.get("summary"): md.append(f"\n> {r['summary']}\n")
                    for kp in r.get("key_points", []): md.append(f"- **{kp['label']}:** {kp['text']}")
                    if r.get("cited_by") is not None: md.append(f"- *Cited by {r['cited_by']}*")
                    md.append("")
                md.append("---\n")
            except Exception as ex:
                print(f"      !! {ex}")
                md.append(f"## {it['id']}. {it['title']}\n\nError: {ex}\n\n---\n")
            time.sleep(3.5)
        page.close()
    Path(a.md).write_text("\n".join(md), encoding="utf-8")
    print(f"\nCatalogue -> {a.md}")

if __name__ == "__main__":
    main()
