#!/usr/bin/env python3
"""Extract Gemini Deep Research responses *with* their citations.

Background
----------
The original downloader saved `last_response.inner_text()`. Gemini renders each
citation as a small inline chip (rendered text is just "PDF", "+ 1", "+ 3", or a
number) whose real content -- source title, publisher, URL -- only exists in the
DOM: partly as attributes on the chip, and partly in a hover card that Gemini
builds when you point at the chip. `inner_text()` throws all of that away, which
is why the saved reports read "...holistic well-being.  PDF  + 1" with no source
anywhere.

This module keeps the citations:

1. `tag_and_serialize()` runs in-page, walks the response DOM, emits Markdown,
   and replaces every citation chip with a `<<<GCITE:k>>>` placeholder while
   stamping the chip with `data-gcite="k"` so Python can find it again.
2. `resolve_hover_cards()` hovers (and, if that yields nothing, clicks) each chip
   whose metadata is still incomplete and scrapes the hover card.
3. `build_document()` renumbers the surviving sources, rewrites the placeholders
   as `[n]`, and appends an APA-style reference list.

Sources that point at one of the attached PDFs are matched back to
`readings_manifest.md`, which already carries authors / venue / year, so those
entries come out as real APA journal citations rather than bare filenames.

Selector fragility: Gemini's DOM changes often. Every selector list below is
deliberately broad, and `--dump-html` writes the raw response HTML next to the
report so a broken run can be diagnosed without re-running the research.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote

# --------------------------------------------------------------------------
# In-page serializer
# --------------------------------------------------------------------------

# Returns {"markdown": str, "chips": [{"k": int, "text": str, "url": str|None,
#          "title": str|None, "label": str|None, "site": str|None}], "html": str}
_SERIALIZE_JS = r"""
(rootSelectorList) => {
  // ---- locate the response container -------------------------------------
  let root = null;
  for (const sel of rootSelectorList) {
    const nodes = document.querySelectorAll(sel);
    if (nodes.length) { root = nodes[nodes.length - 1]; break; }
  }
  if (!root) return null;

  // Chip detection is deliberately two-tier. Gemini wraps each *cited sentence*
  // in a generic <span class="citation-71">...whole sentence...</span>, so
  // treating anything matching [class*="citation"] as a citation marker deletes
  // real prose from the report. Only the dedicated citation components are
  // chips outright; class-based matches must also look like a marker.
  const STRONG_SEL = [
    'source-footnote', 'sources-carousel-inline', 'source-inline-chip',
    'browse-item', '[data-citation-index]',
    'button[aria-label*="source detail" i]', 'button[aria-label*="citation" i]',
  ].join(',');

  const WEAK_SEL = [
    'sup', '.citation', '[class*="citation"]', '[class*="Citation"]',
    '[class*="source-inline"]', '[class*="attribution"]',
    'span[role="button"][aria-label*="source" i]',
  ].join(',');

  // "PDF", "+ 3", "2", "[4]" -- what a collapsed citation marker renders as.
  const CHIP_TEXT = /^(\s*(pdf|\+\s*\d+|\d+|\[\d+\])\s*)+$/i;

  const isChip = (el) => {
    if (!el.matches) return false;
    if (el.matches(STRONG_SEL)) return true;
    const t = (el.innerText || '').trim();
    if (el.matches(WEAK_SEL)) {
      // Empty <sup class="superscript"> placeholders count; sentence wrappers don't.
      return !t || (t.length <= 12 && CHIP_TEXT.test(t));
    }
    if (!t || t.length > 12 || !CHIP_TEXT.test(t)) return false;
    return ['SUP', 'SPAN', 'BUTTON', 'A'].includes(el.tagName);
  };

  const chips = [];
  let k = 0;

  const chipMeta = (el) => {
    const meta = { k: k, text: (el.innerText || '').trim() };
    const a = el.matches('a[href]') ? el : el.querySelector('a[href]');
    if (a) { meta.url = a.href; meta.title = (a.getAttribute('title') || a.innerText || '').trim() || null; }
    // Gemini keeps the source name on a *descendant* button, e.g.
    //   <sources-carousel-inline><source-inline-chip><button
    //      aria-label="View source details for citation from PDF: 08_Beyond_....pdf.
    //                  Press Enter to open sources dialog.">
    // so reading attributes off the chip element alone finds nothing. Scan the
    // chip and everything under it; this resolves attached-PDF citations with
    // no hovering at all.
    const labelled = [el, ...el.querySelectorAll('*')];
    const seenLabels = new Set();
    for (const node of labelled) {
      for (const attr of ['aria-label', 'title', 'data-title', 'data-tooltip', 'alt']) {
        const v = node.getAttribute && node.getAttribute(attr);
        if (v && v.trim() && !seenLabels.has(v.trim())) {
          seenLabels.add(v.trim());
          meta.label = (meta.label ? meta.label + ' | ' : '') + v.trim();
        }
      }
      for (const attr of ['data-url', 'data-source-url', 'data-href', 'href']) {
        const v = node.getAttribute && node.getAttribute(attr);
        if (v && !meta.url && /^https?:/i.test(v)) meta.url = v;
      }
    }
    // Deep Research marks each inline citation with
    //   <sup class="superscript" data-turn-source-index="7">
    // which is a 1-based index into the report's "Sources used in the report"
    // list. That mapping is authoritative and needs no hover interaction.
    const sup = el.matches('[data-turn-source-index]')
      ? el : el.querySelector('[data-turn-source-index]');
    if (sup) {
      const n = parseInt(sup.getAttribute('data-turn-source-index'), 10);
      if (!isNaN(n)) meta.turn_index = n;
    }
    const img = el.querySelector && el.querySelector('img[alt]');
    if (img) meta.site = (img.getAttribute('alt') || '').trim() || null;
    meta.html = el.outerHTML.slice(0, 4000);
    return meta;
  };

  // ---- DOM -> Markdown ----------------------------------------------------
  const BLOCK = new Set(['P','DIV','SECTION','ARTICLE','UL','OL','LI','TABLE','TR',
                         'BLOCKQUOTE','PRE','H1','H2','H3','H4','H5','H6','BR','HR']);

  const walk = (node, ctx) => {
    if (node.nodeType === Node.TEXT_NODE) return node.nodeValue.replace(/\s+/g, ' ');
    if (node.nodeType !== Node.ELEMENT_NODE) return '';
    const el = node;
    if (el.tagName === 'STYLE' || el.tagName === 'SCRIPT') return '';
    const style = window.getComputedStyle(el);
    if (style && (style.display === 'none' || style.visibility === 'hidden')) return '';

    if (isChip(el)) {
      el.setAttribute('data-gcite', String(k));
      chips.push(chipMeta(el));
      k += 1;
      return `<<<GCITE:${k - 1}>>>`;
    }

    const kids = () => Array.from(el.childNodes).map((c) => walk(c, ctx)).join('');

    switch (el.tagName) {
      case 'BR': return '\n';
      case 'HR': return '\n\n---\n\n';
      case 'H1': return `\n\n# ${kids().trim()}\n\n`;
      case 'H2': return `\n\n## ${kids().trim()}\n\n`;
      case 'H3': return `\n\n### ${kids().trim()}\n\n`;
      case 'H4': return `\n\n#### ${kids().trim()}\n\n`;
      case 'H5':
      case 'H6': return `\n\n##### ${kids().trim()}\n\n`;
      case 'STRONG':
      case 'B': { const t = kids().trim(); return t ? `**${t}**` : ''; }
      case 'EM':
      case 'I': { const t = kids().trim(); return t ? `*${t}*` : ''; }
      case 'CODE': {
        if (el.closest('pre')) return kids();
        const t = kids().trim();
        return t ? '`' + t + '`' : '';
      }
      case 'PRE': return `\n\n\`\`\`\n${el.innerText.replace(/\n+$/, '')}\n\`\`\`\n\n`;
      case 'BLOCKQUOTE':
        return '\n\n' + kids().trim().split('\n').map((l) => '> ' + l).join('\n') + '\n\n';
      case 'A': {
        const t = kids().trim();
        const href = el.getAttribute('href');
        if (!t) return '';
        return href && /^https?:/i.test(href) ? `[${t}](${href})` : t;
      }
      case 'LI': {
        const parent = el.parentElement;
        const ordered = parent && parent.tagName === 'OL';
        const idx = parent ? Array.from(parent.children).indexOf(el) + 1 : 1;
        const marker = ordered ? `${idx}. ` : '- ';
        const body = kids().trim().replace(/\n+/g, ' ');
        return body ? `${marker}${body}\n` : '';
      }
      case 'UL':
      case 'OL': {
        const items = kids().split('\n').map((l) => l.trim()).filter(Boolean);
        return `\n${items.join('\n')}\n`;
      }
      case 'TR': {
        const cells = Array.from(el.children).map((c) => walk(c, ctx).trim().replace(/\n+/g, ' '));
        return `| ${cells.join(' | ')} |\n`;
      }
      case 'TABLE': {
        const rows = kids().trim().split('\n').filter(Boolean);
        if (!rows.length) return '';
        const ncols = (rows[0].match(/\|/g) || []).length - 1;
        const sep = `|${' --- |'.repeat(Math.max(ncols, 1))}`;
        return `\n\n${rows[0]}\n${sep}\n${rows.slice(1).join('\n')}\n\n`;
      }
      default: {
        const body = kids();
        return BLOCK.has(el.tagName) ? `\n${body}\n` : body;
      }
    }
  };

  // The report's source list: one anchor per cited source, in index order.
  const srcNodes = Array.from(root.querySelectorAll(
    'a[data-test-id="browse-web-item-link"], browse-item a[href]'));
  const sources = srcNodes.map((a, i) => {
    const lines = (a.innerText || '').split('\n').map((s) => s.trim())
      .filter((s) => s && !/^opens in a new window$/i.test(s));
    return { i: i + 1, url: a.href, site: lines[0] || null, title: lines[1] || null };
  });

  let md = walk(root, {});
  md = md.replace(/[ \t]+\n/g, '\n').replace(/\n{3,}/g, '\n\n').trim();
  return { markdown: md, chips: chips, sources: sources, html: root.outerHTML };
}
"""

RESPONSE_ROOT_SELECTORS = [
    "extended-response-panel",
    "deep-research-immersive-panel",
    "immersive-editor",
    "model-response message-content",
    "message-content",
    ".model-response-text",
    ".response-container-content",
]

# Popup that Gemini opens when a citation chip is hovered/clicked.
HOVER_CARD_SELECTORS = [
    '[role="tooltip"]',
    ".cdk-overlay-pane",
    "source-preview",
    "[class*='hover-card']",
    "[class*='citation-card']",
    "[class*='source-card']",
    '[role="dialog"]',
]


# --------------------------------------------------------------------------
# Source model
# --------------------------------------------------------------------------

@dataclass
class Source:
    """One resolved citation target."""
    key: str                      # dedup key (normalized url, or pdf filename)
    url: str | None = None
    title: str | None = None
    site: str | None = None
    kind: str = "web"             # "web" | "pdf"
    raw: list[str] = field(default_factory=list)   # tooltip / label text, for debugging
    number: int = 0


def _clean_url(url: str | None) -> str | None:
    """Unwrap Google's redirector and drop tracking noise."""
    if not url:
        return None
    url = url.strip()
    if not re.match(r"^https?://", url, re.I):
        return None
    # Gemini appends scroll-to-text fragments (#:~:text=...) that are long,
    # ugly, and meaningless in a reference list.
    url = re.sub(r"#:~:text=.*$", "", url)
    p = urlparse(url)
    if "google.com" in p.netloc and p.path.startswith(("/url", "/search")):
        q = parse_qs(p.query)
        for param in ("url", "q", "imgurl"):
            if q.get(param):
                inner = unquote(q[param][0])
                if re.match(r"^https?://", inner, re.I):
                    return inner
    return url


def _norm_key(url: str) -> str:
    p = urlparse(url)
    return f"{p.netloc.lower().removeprefix('www.')}{p.path.rstrip('/')}"


def _site_from_url(url: str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")


# "View source details for citation from PDF: <name>.pdf. Press Enter to open
# sources dialog." -> "<name>.pdf"
_ARIA_SOURCE_RE = re.compile(
    r"citation from\s*(?:PDF:)?\s*(?P<name>.+?)\.?\s*(?:Press Enter|$)", re.I | re.S)


def source_name_from_label(label: str) -> str | None:
    """Pull the cited source's name out of a chip's aria-label."""
    if not label:
        return None
    for part in label.split(" | "):
        m = _ARIA_SOURCE_RE.search(part)
        if m:
            name = m.group("name").strip().strip(".")
            if name:
                return name
    return None


def _squash(text: str) -> str:
    """Lowercase alphanumeric-only form, for tolerant title matching."""
    return re.sub(r"[^a-z0-9]+", "", (text or "").lower())


def _loose_match(a: str, b: str, n: int = 40) -> bool:
    """True if either string's first `n` squashed chars occur in the other.

    Chip labels and hover-card titles are frequently truncated ("Religion,
    spirituality & chronic illness: A scoping review" vs the manifest's full
    "...: A scoping review and implications for health care practitioners"),
    so a plain substring test in one direction misses the match."""
    sa, sb = _squash(a), _squash(b)
    if not sa or not sb:
        return False
    return sa[:n] in sb or sb[:n] in sa


# --------------------------------------------------------------------------
# readings_manifest.md -> APA metadata for the attached PDFs
# --------------------------------------------------------------------------

@dataclass
class Reading:
    index: int
    title: str
    authors: str | None
    venue: str | None
    year: str | None
    url: str | None
    local_file: str | None


_AUTHORS_VENUE_RE = re.compile(
    # "<title><AUTHORS> - <Venue>, <YEAR> - <publisher><trailing snippet...>"
    r"^(?P<authors>[^-]{3,200}?)\s+-\s+(?P<venue>[^-,]{2,120}?),\s*(?P<year>(19|20)\d{2})\s+-\s+",
)


def parse_readings_manifest(manifest: Path) -> list[Reading]:
    """Pull author/venue/year out of `readings_manifest.md`.

    The manifest's "Authors/Venue" line is a single scraped blob that runs the
    title, the Scholar byline and the result snippet together, e.g.
        "<Title>M Litalien, DO Atari, I Obasi - Journal of religion and health, 2022 - Springer<snippet>"
    so we strip the leading title (which we already have from the heading) and
    then match the "AUTHORS - Venue, YEAR - publisher" byline.
    """
    if not manifest.exists():
        return []
    out: list[Reading] = []
    blocks = manifest.read_text(encoding="utf-8").split("\n### ")
    for block in blocks[1:]:
        head, _, body = block.partition("\n")
        m = re.match(r"\s*(\d+)\.\s*(.+?)\s*(?:—|--).*$", head.strip())
        if m:
            idx, title = int(m.group(1)), m.group(2).strip()
        else:
            idx, title = len(out) + 1, head.strip()

        def field_of(name: str) -> str | None:
            fm = re.search(rf"^- \*\*{re.escape(name)}:\*\*\s*(.+)$", body, re.M)
            return fm.group(1).strip() if fm else None

        local = field_of("Local File")
        if local:
            local = local.strip("`")
        pub = field_of("Publisher Link")
        url = None
        if pub:
            lm = re.search(r"\((https?://[^)]+)\)", pub)
            url = lm.group(1) if lm else (pub if pub.startswith("http") else None)

        blob = field_of("Authors/Venue") or ""
        blob = blob.strip("* ")
        if blob.startswith(title):
            blob = blob[len(title):]
        am = _AUTHORS_VENUE_RE.match(blob)
        authors = venue = year = None
        if am:
            authors = am.group("authors").strip()
            venue = am.group("venue").strip()
            year = am.group("year")

        out.append(Reading(idx, title, authors, venue, year, url, local))
    return out


def _apa_authors(scholar_authors: str) -> str:
    """Turn a Scholar byline ("M Litalien, DO Atari, I Obasi…") into APA-ish
    "Litalien, M., Atari, D. O., & Obasi, I." Scholar only gives initials, so
    this is as close to APA as the available data allows."""
    raw = [a.strip() for a in scholar_authors.replace("…", "").split(",") if a.strip()]
    names = []
    for a in raw:
        parts = a.split()
        if len(parts) < 2:
            names.append(a)
            continue
        initials, surname = parts[:-1], parts[-1]
        inits = " ".join(f"{c}." for p in initials for c in p if c.isalpha())
        names.append(f"{surname}, {inits}")
    if not names:
        return ""
    if len(names) == 1:
        return names[0]
    if len(names) > 20:
        names = names[:19] + ["..."] + names[-1:]
    return ", ".join(names[:-1]) + ", & " + names[-1]


def apa_from_reading(r: Reading) -> str:
    date = f"({r.year})." if r.year else "(n.d.)."
    title = r.title.rstrip(".")
    bits = []
    if r.authors:
        bits += [_apa_authors(r.authors), date, f"{title}."]
    else:
        # Some manifest entries have no scraped byline at all. APA moves the
        # title into the author slot rather than opening with a bare "(n.d.)".
        bits += [f"*{title}*.", date]
    if r.venue:
        bits.append(f"*{r.venue}*.")
    if r.url:
        bits.append(r.url)
    return " ".join(b for b in bits if b)


def apa_from_source(s: Source, accessed: str | None = None) -> str:
    """APA 7 web-page form: Site. (n.d.). Title. URL

    Gemini's hover cards rarely expose an author or a publication date, so we
    fall back to the site as the group author and n.d. for the date rather than
    inventing metadata."""
    title = (s.title or "").strip().rstrip(".")
    site = (s.site or (_site_from_url(s.url) if s.url else "")).strip()
    # Page titles usually end with " - <Site>"; that repeats the group author.
    if site:
        parts = [x for x in site.split(".") if x]
        bare = parts[-2] if len(parts) >= 2 else site   # en.wikipedia.org -> wikipedia
        title = re.sub(rf"\s*[-|–—]\s*{re.escape(bare)}\s*$", "", title, flags=re.I)
    bits = []
    if site:
        # Group-author form: Site. (n.d.). Title. URL
        bits.append(f"{site}.")
        bits.append("(n.d.).")
        if title and title.lower() != site.lower():
            bits.append(f"*{title}*.")
    else:
        # No identifiable author/publisher -- APA puts the title first.
        bits.append(f"*{title}*." if title else "*[Untitled source]*.")
        bits.append("(n.d.).")
    if s.url:
        bits.append(s.url)
    line = " ".join(bits)
    if accessed and s.url:
        line += f" (accessed {accessed})"
    return line


# --------------------------------------------------------------------------
# Extraction driver
# --------------------------------------------------------------------------

# Chip-shaped UI affordances that are not citations. "Learn More" chips sit in
# Deep Research reports next to source lists and otherwise become bogus entries.
_JUNK_LABEL_RE = re.compile(
    r"^(learn more|show more|opens in a new window|more|sources?)$", re.I)


def _is_junk_chip(chip: dict) -> bool:
    parts = {(chip.get("label") or "").strip(), (chip.get("text") or "").strip(),
             (chip.get("card_text") or "").strip()}
    parts = {q for p in parts for q in p.split("|")}
    parts = {p.strip() for p in parts if p.strip()}
    return bool(parts) and all(_JUNK_LABEL_RE.match(p) for p in parts)


def _needs_hover(chip: dict) -> bool:
    """Should we open this chip's hover card?

    Hovering is the slow part of extraction (~2-4s per chip), so only do it for
    chips that can actually gain something:
      - a chip with a URL already in the DOM is done;
      - Gemini's empty <source-footnote><sup></sup></source-footnote> spacers
        carry nothing and never will;
      - an attached-PDF chip's aria-label already names the file, and its hover
        card just repeats that name -- no URL to gain.
    Everything else (web citations, whose URL lives only in the card) is hovered.
    """
    if _clean_url(chip.get("url")):
        return False
    if chip.get("turn_index"):
        return False   # resolvable from the report's source list
    if _is_junk_chip(chip):
        return False   # "Learn More" and friends are not citations
    label = (chip.get("label") or "").strip()
    text = (chip.get("text") or "").strip()
    if not label and not text:
        return False
    named = source_name_from_label(label)
    if named and named.lower().endswith(".pdf"):
        return False
    return True


def _card_metadata(page, timeout_ms: int = 1500) -> dict:
    """Read whatever hover card is currently open."""
    for sel in HOVER_CARD_SELECTORS:
        loc = page.locator(sel)
        try:
            n = loc.count()
        except Exception:
            continue
        for i in range(n):
            card = loc.nth(i)
            try:
                if not card.is_visible(timeout=timeout_ms):
                    continue
                text = (card.inner_text() or "").strip()
                if not text:
                    continue
                links = card.locator("a[href]")
                url = None
                for j in range(links.count()):
                    href = _clean_url(links.nth(j).get_attribute("href"))
                    if href:
                        url = href
                        break
                lines = [l.strip() for l in text.splitlines() if l.strip()]
                title = next((l for l in lines if len(l) > 12), lines[0] if lines else None)
                return {"url": url, "title": title, "text": text}
            except Exception:
                continue
    return {}


def extract_response(page, hover: bool = True, hover_limit: int = 400,
                     verbose: bool = True) -> dict | None:
    """Return {'markdown', 'chips', 'html'} for the last response on `page`,
    with each chip's metadata resolved as far as the DOM allows."""
    data = page.evaluate(_SERIALIZE_JS, RESPONSE_ROOT_SELECTORS)
    if not data:
        return None

    chips = data["chips"]
    if hover and chips:
        unresolved = [c for c in chips if _needs_hover(c)]
        if verbose:
            print(f"   Resolving {len(unresolved)} citation chip(s) via hover cards "
                  f"({len(chips) - len(unresolved)} of {len(chips)} need no hover: "
                  f"already linked, named by aria-label, or empty spacers)...")
        for c in unresolved[:hover_limit]:
            chip = page.locator(f'[data-gcite="{c["k"]}"]').first
            try:
                chip.scroll_into_view_if_needed(timeout=3000)
            except Exception:
                pass
            # The hover/click target is the inner button; the outer custom
            # element (sources-carousel-inline) isn't itself interactive.
            loc = chip
            try:
                inner = chip.locator("button, a, [role='button']").first
                if inner.count():
                    loc = inner
            except Exception:
                pass
            meta = {}
            for action in ("hover", "click"):
                try:
                    getattr(loc, action)(timeout=2000)
                    page.wait_for_timeout(450)
                    meta = _card_metadata(page)
                except Exception:
                    meta = {}
                if meta.get("url") or meta.get("title"):
                    break
            if meta:
                c["url"] = c.get("url") or meta.get("url")
                c["title"] = c.get("title") or meta.get("title")
                c["card_text"] = meta.get("text")
            try:
                page.keyboard.press("Escape")
                page.mouse.move(0, 0)
                page.wait_for_timeout(80)
            except Exception:
                pass
    return data


def _source_for_chip(chip: dict, readings: list[Reading],
                     source_list: dict[int, dict] | None = None) -> Source | None:
    # A Deep Research chip indexes into the report's own source list; that beats
    # anything a hover card or aria-label can tell us.
    ti = chip.get("turn_index")
    if ti and source_list and ti in source_list:
        entry = source_list[ti]
        url = _clean_url(entry.get("url"))
        if url:
            return Source(key=_norm_key(url), url=url,
                          title=entry.get("title") or None,
                          site=entry.get("site") or _site_from_url(url),
                          kind="pdf" if url.lower().endswith(".pdf") else "web")

    if _is_junk_chip(chip):
        return None

    url = _clean_url(chip.get("url"))
    blob = " | ".join(filter(None, [chip.get("label"), chip.get("title"),
                                    chip.get("card_text"), chip.get("site")]))
    named = source_name_from_label(chip.get("label") or "") or None

    # An attached-PDF chip ("PDF") carries no URL; match it to a manifest entry
    # by filename or title appearing in the chip's label / hover card.
    if not url:
        for r in readings:
            needles = [n for n in (r.local_file, r.title) if n]
            haystacks = [h for h in (named, blob) if h]
            if any(_loose_match(n, h) for n in needles for h in haystacks):
                # Key on the reading's identity, preferring its URL. Keying on
                # "pdf::<local_file or title>" split one paper across two keys
                # when different chips matched it by filename vs by title, so
                # the same source appeared twice in the reference list.
                key = _norm_key(r.url) if r.url else f"reading::{r.index}"
                return Source(key=key, url=r.url, title=r.title, site=r.venue,
                              kind="pdf", raw=[blob])
    if not url:
        label = named or blob.strip()
        if not label:
            return None
        return Source(key=f"raw::{label[:120]}", title=label.splitlines()[0][:200],
                      kind="pdf" if label.lower().endswith(".pdf") else "web", raw=[blob])
    return Source(key=_norm_key(url), url=url,
                  title=chip.get("title") or None,
                  site=chip.get("site") or _site_from_url(url),
                  kind="pdf" if url.lower().endswith(".pdf") else "web",
                  raw=[blob] if blob else [])


def build_document(data: dict, readings: list[Reading] | None = None,
                   uncited_readings: bool = True) -> tuple[str, list[Source]]:
    """Rewrite `<<<GCITE:k>>>` placeholders as `[n]` and append an APA list."""
    readings = readings or []
    md = data["markdown"]
    source_list = {s["i"]: s for s in data.get("sources") or [] if s.get("url")}
    by_key: dict[str, Source] = {}
    chip_to_num: dict[int, int] = {}

    unresolved = 0
    for chip in data["chips"]:
        src = _source_for_chip(chip, readings, source_list)
        if src is None:
            # Gemini emits an empty <source-footnote><sup></sup></source-footnote>
            # next to each real chip; those carry nothing and are decorative, so
            # only a chip that actually had content counts as a lost citation.
            if (chip.get("text") or "").strip() or (chip.get("label") or "").strip():
                unresolved += 1
            continue
        existing = by_key.get(src.key)
        if existing:
            if not existing.title and src.title:
                existing.title = src.title
            existing.raw.extend(src.raw)
        else:
            src.number = len(by_key) + 1
            by_key[src.key] = src
            existing = src
        chip_to_num[chip["k"]] = existing.number

    def sub(m: re.Match) -> str:
        k = int(m.group(1))
        n = chip_to_num.get(k)
        return f"[{n}]" if n else ""

    md = re.sub(r"<<<GCITE:(\d+)>>>", sub, md)
    md = re.sub(r"\[(\d+)\](\s*\[\1\])+", r"[\1]", md)      # collapse repeats
    md = re.sub(r"(\[\d+\])\s+(?=[.,;:])", r"\1", md)
    md = re.sub(r"[ \t]{2,}", " ", md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()

    sources = sorted(by_key.values(), key=lambda s: s.number)

    lines = ["", "## References (APA)", ""]
    if sources:
        matched_files = set()
        for s in sources:
            reading = None
            if readings:
                for r in readings:
                    if (s.url and r.url and _norm_key(s.url) == _norm_key(r.url)) or \
                       (s.key.startswith("pdf::") and r.local_file and r.local_file in s.key) or \
                       (s.title and _loose_match(s.title, r.title)):
                        reading = r
                        break
            if reading:
                matched_files.add(reading.local_file)
                lines.append(f"{s.number}. {apa_from_reading(reading)}")
            else:
                lines.append(f"{s.number}. {apa_from_source(s)}")
        if uncited_readings:
            extra = [r for r in readings if r.local_file and r.local_file not in matched_files]
            if extra:
                lines += ["", "### Attached sources not tied to a specific in-text citation", ""]
                for r in extra:
                    lines.append(f"- {apa_from_reading(r)}")
        if unresolved:
            lines += ["", f"_{unresolved} citation marker(s) carried no resolvable source in the "
                          f"DOM and were dropped; see the `*_citations.json` sidecar._"]
    else:
        lines.append("_No citation chips were found in the response DOM. "
                     "If the report visibly has citations, the chip selectors in "
                     "`gemini_citations.py` need updating -- inspect the saved "
                     "`*_response.html` sidecar._")

    return md + "\n" + "\n".join(lines) + "\n", sources


def save_debug(data: dict, base: Path) -> None:
    """Write the raw response HTML + chip dump next to the report."""
    base.with_name(base.stem + "_response.html").write_text(data.get("html", ""), encoding="utf-8")
    base.with_name(base.stem + "_citations.json").write_text(
        json.dumps(data.get("chips", []), indent=2, ensure_ascii=False), encoding="utf-8")


def extract_and_write(page, out_file: Path, *, title: str,
                      meta: dict[str, str] | None = None,
                      readings: list[Reading] | None = None,
                      hover: bool = True, debug_dump: bool = True,
                      fallback_text: str | None = None,
                      verbose: bool = True) -> dict:
    """Extract the response, build the APA document and write it.

    Every caller (single runner, batch runner, re-extract CLI) previously
    carried its own copy of this sequence, which is how they drifted -- e.g.
    the CLI wrote a header without the model/attachment provenance the runners
    recorded. Returns {"sources", "chips", "chars"}.
    """
    data = extract_response(page, hover=hover, verbose=verbose)
    if data is None:
        if fallback_text is None:
            raise RuntimeError(
                "Could not locate a response container. Update "
                "RESPONSE_ROOT_SELECTORS in gemini_citations.py.")
        if verbose:
            print("   ⚠️ No response container found; saving plain text without references.")
        body, sources, chips = fallback_text, [], []
    else:
        if debug_dump:
            save_debug(data, out_file)
        body, sources = build_document(data, readings or [])
        chips = data["chips"]

    lines = [f"# {title}", ""]
    for k, v in (meta or {}).items():
        lines.append(f"**{k}:** {v}  ")
    lines.append(f"**Citations resolved:** {len(sources)}")
    lines.append("")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text("\n".join(lines) + "\n" + body, encoding="utf-8")

    if verbose:
        print(f"   ✓ {len(sources)} source(s) from {len(chips)} chip(s) -> {out_file.name}")
    return {"sources": len(sources), "chips": len(chips), "chars": len(body)}
