#!/usr/bin/env python3
"""Render Scholar Labs result JSON to readable markdown, recovering cards whose
raw_text arrived without newlines (parse_block then dumps everything into
authors_venue_year)."""
import json, re, sys
from pathlib import Path

TAIL = re.compile(r"(Save\s*Cite|Related articles|Cited by \d+|All \d+ versions|Looking for more results).*$", re.S)
KP = re.compile(r"([A-Z][A-Za-z /&'-]{2,45}):\s")

def split_card(r):
    blob = r.get("authors_venue_year") or ""
    title = r["title"]
    if blob.startswith(title):
        blob = blob[len(title):]
    blob = TAIL.sub("", blob).strip()
    m = re.match(r"(.{0,160}?\b(?:19|20)\d{2}\b\s*-\s*[\w.]+\.\w+)(.*)$", blob, re.S)
    cite, rest = (m.group(1).strip(), m.group(2).strip()) if m else ("", blob)
    parts = KP.split(rest)
    summary = parts[0].strip()
    kps = [(parts[i].strip(), parts[i+1].strip()) for i in range(1, len(parts)-1, 2)]
    if not kps and r.get("key_points"):
        kps = [(k["label"], k["text"]) for k in r["key_points"]]
    if not summary and r.get("summary"):
        summary = r["summary"]
    return cite, summary, kps

out = ["# RELS 398 — Scholar Labs evidence on course structure\n"]
for f in sorted(Path(sys.argv[1]).glob("q*.json")):
    d = json.loads(f.read_text())
    out.append(f"## {d['id']}. {d['title']}\n")
    out.append(f"**Query:** *{d['query']}*\n")
    if not d["results"]:
        out.append("_Scholar Labs returned no cards for this query._\n\n---\n"); continue
    for i, r in enumerate(d["results"], 1):
        cite, summary, kps = split_card(r)
        pdf = f" · [PDF]({r['pdf_link']})" if r.get("pdf_link") else ""
        cb = f" · cited by {r['cited_by']}" if r.get("cited_by") is not None else ""
        out.append(f"**{i}. [{r['title']}]({r['title_link']})**{pdf}{cb}  ")
        if cite: out.append(f"*{cite}*  ")
        if summary: out.append(f"\n> {summary}\n")
        for lab, txt in kps: out.append(f"- **{lab}:** {txt}")
        out.append("")
    out.append("---\n")
Path(sys.argv[2]).write_text("\n".join(out), encoding="utf-8")
print(f"wrote {sys.argv[2]}")
