/* RELS 398 / ENGL 398 — Static TEI + IIIF Edition Viewer
 * Zero-build client-side renderer for GitHub Pages and offline HTML packages.
 */
(function () {
  "use strict";

  const TEI_NS = "http://www.tei-c.org/ns/1.0";
  const XML_NS = "http://www.w3.org/XML/1998/namespace";

  const state = {
    docs: { source: null, translation: null, alignment: null, commentary: null },
    baseUrl: new URL("./", window.location.href).href,
    imageSrc: null,
    imageType: "image", // "image" | "iiif-info"
    zones: [],          // { id, ulx, uly, lrx, lry }
    surfaceBox: { width: 1000, height: 1300 },
    links: new Map(),   // id -> Set<id>
    spansById: new Map(),
    zonesById: new Map(),
    notes: [],          // { index, id, targets, type, resp, html, rawText }
    qaChecks: [],       // { id, label, status, summary, details }
    frontHtml: "",
    backHtml: "",
    defaultLang: "en",
    viewMode: "diplomatic",
    osdViewer: null,
    svgZoom: 1,
    svgPanX: 0,
    svgPanY: 0,
    dragging: false,
    dragStart: null,
    activeNoteFilter: "all",
  };

  const els = {
    app: document.getElementById("app"),
    docTitle: document.getElementById("docTitle"),
    docSubtitle: document.getElementById("docSubtitle"),
    workspace: document.getElementById("workspace"),
    sourceBody: document.getElementById("sourceBody"),
    interlinearBody: document.getElementById("interlinearBody"),
    transBody: document.getElementById("transBody"),
    facsBody: document.getElementById("facsBody"),
    osdStage: document.getElementById("osdStage"),
    svgStage: document.getElementById("svgStage"),
    svgTransform: document.getElementById("svgTransform"),
    facsImg: document.getElementById("facsImg"),
    zoneOverlay: document.getElementById("zoneOverlay"),
    facsEmpty: document.getElementById("facsEmpty"),
    inspectorBar: document.getElementById("inspectorBar"),
    statusText: document.getElementById("statusText"),
    statusWarn: document.getElementById("statusWarn"),
    loaderDrawer: document.getElementById("loaderDrawer"),
    sideDrawer: document.getElementById("sideDrawer"),
    drawerTitle: document.getElementById("drawerTitle"),
    drawerBody: document.getElementById("drawerBody"),
    printFront: document.getElementById("printFront"),
    printAppendix: document.getElementById("printAppendix"),
    wordPopover: document.getElementById("wordPopover"),
    btnDiplomatic: document.getElementById("btnDiplomatic"),
    btnRegularized: document.getElementById("btnRegularized"),
    btnInterlinear: document.getElementById("btnInterlinear"),
    btnToggleTrans: document.getElementById("btnToggleTrans"),
    btnAbout: document.getElementById("btnAbout"),
    btnQA: document.getElementById("btnQA"),
    btnNotes: document.getElementById("btnNotes"),
    btnFiles: document.getElementById("btnFiles"),
    btnPrint: document.getElementById("btnPrint"),
  };

  function xid(el) {
    if (!el || !el.getAttribute) return "";
    return el.getAttributeNS(XML_NS, "id") || el.getAttribute("xml:id") || el.getAttribute("id") || "";
  }

  function cleanRefs(attr) {
    return (attr || "")
      .trim()
      .split(/\s+/)
      .filter(Boolean)
      .map((s) => s.replace(/^.*#/, ""));
  }

  function escHtml(str) {
    return (str || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function parseConfig() {
    let cfg = {};
    const tag = document.getElementById("edition-config");
    if (tag && tag.textContent.trim()) {
      try { cfg = JSON.parse(tag.textContent); } catch (_) {}
    }
    const qs = new URLSearchParams(window.location.search);
    if (qs.has("source")) delete cfg.edition;
    if (qs.has("edition")) delete cfg.source;
    for (const k of ["edition", "source", "translation", "alignment", "commentary", "image", "iiif", "view"]) {
      if (qs.has(k)) cfg[k] = qs.get(k);
    }
    return cfg;
  }

  function parseXml(text, label) {
    const doc = new DOMParser().parseFromString(text, "application/xml");
    const err = doc.getElementsByTagName("parsererror")[0];
    if (err) throw new Error(`${label}: invalid XML — ${err.textContent.trim()}`);
    return doc;
  }

  async function loadTextUrl(url) {
    const resp = await fetch(url);
    if (!resp.ok) throw new Error(`HTTP ${resp.status} for ${url}`);
    return await resp.text();
  }

  function setViewMode(mode) {
    state.viewMode = mode === "regularized" || mode === "interlinear" ? mode : "diplomatic";
    els.app.setAttribute("data-view", state.viewMode);
    els.btnDiplomatic.setAttribute("aria-pressed", String(state.viewMode === "diplomatic"));
    els.btnRegularized.setAttribute("aria-pressed", String(state.viewMode === "regularized"));
    if (els.btnInterlinear) els.btnInterlinear.setAttribute("aria-pressed", String(state.viewMode === "interlinear"));
    if (els.interlinearBody) els.interlinearBody.hidden = state.viewMode !== "interlinear";
  }

  function addDomRef(map, id, node) {
    if (!id) return;
    if (!map.has(id)) map.set(id, []);
    map.get(id).push(node);
  }

  function cloneTeiSubtree(node, options = {}) {
    if (node.nodeType === Node.TEXT_NODE) {
      return document.createTextNode(node.nodeValue.replace(/\s+/g, " "));
    }
    if (node.nodeType !== Node.ELEMENT_NODE) return null;

    const name = node.localName.toLowerCase();
    // Elements stored separately from main prose flow
    if (name === "teiheader" || name === "facsimile" || name === "standoff" || name === "linkgrp" || name === "front" || name === "back") {
      return null;
    }
    if (options.skipTranslation && isTranslationNode(node)) {
      return null;
    }

    const el = document.createElement("tei-" + name);
    for (const attr of node.attributes) {
      if (attr.name === "xml:id" || attr.localName === "id") {
        el.dataset.xmlid = attr.value;
      } else if (attr.name === "xml:lang" || attr.localName === "lang") {
        el.setAttribute("lang", attr.value);
      } else {
        el.setAttribute(attr.name, attr.value);
      }
    }

    const id = xid(node);
    if (id) {
      el.dataset.xmlid = id;
      addDomRef(state.spansById, id, el);
    }
    if (node.hasAttribute("facs")) {
      el.dataset.facs = cleanRefs(node.getAttribute("facs")).join(" ");
    }

    if (name === "figure") {
      const fd = node.getElementsByTagNameNS(TEI_NS, "figDesc")[0] || node.querySelector("figDesc");
      el.textContent = fd ? `[Mark: ${fd.textContent.trim()}]` : "[Figure / Mark]";
      return el;
    }

    if (name === "pb") {
      const n = node.getAttribute("n");
      el.textContent = n ? `f. ${n}` : "pb";
      return el;
    }

    for (const child of node.childNodes) {
      const rendered = cloneTeiSubtree(child, options);
      if (rendered) el.appendChild(rendered);
    }

    if (name === "choice") {
      const hasOrig = !!el.querySelector("tei-orig, tei-abbr, tei-sic");
      const hasReg = !!el.querySelector("tei-reg, tei-expan, tei-corr");
      if (!hasOrig || !hasReg) el.classList.add("no-alt");
    }

    return el;
  }

  function isTranslationNode(el) {
    if (!el || el.nodeType !== Node.ELEMENT_NODE) return false;
    const ln = el.localName.toLowerCase();
    if (ln !== "div" && ln !== "text") return false;
    const t = (el.getAttribute("type") || "").toLowerCase();
    const st = (el.getAttribute("subtype") || "").toLowerCase();
    return t === "translation" || st === "translation";
  }

  function extractHeaderInfo(doc) {
    if (!doc) return {};
    const textOf = (tag) => {
      const found = doc.getElementsByTagNameNS(TEI_NS, tag)[0] || doc.getElementsByTagName(tag)[0];
      return found ? found.textContent.replace(/\s+/g, " ").trim() : "";
    };
    const allOf = (tag) =>
      Array.from(doc.getElementsByTagNameNS(TEI_NS, tag)).concat(Array.from(doc.getElementsByTagName(tag)));

    const title = textOf("title") || "Digital Scholarly Edition";
    const institution = textOf("institution");
    const shelfmark = textOf("idno");
    const origDate = textOf("origDate");
    const origPlace = textOf("origPlace");
    const support = textOf("support");
    const licenceEl = allOf("licence")[0];
    const licenceText = licenceEl ? licenceEl.textContent.replace(/\s+/g, " ").trim() : "";
    const licenceHref = licenceEl ? licenceEl.getAttribute("target") || "" : "";

    const resps = Array.from(doc.getElementsByTagNameNS(TEI_NS, "respStmt")).map((r) => {
      const resp = r.getElementsByTagNameNS(TEI_NS, "resp")[0]?.textContent?.replace(/\s+/g, " ").trim() || "";
      const nm = (r.getElementsByTagNameNS(TEI_NS, "name")[0] || r.getElementsByTagNameNS(TEI_NS, "persName")[0])
        ?.textContent?.replace(/\s+/g, " ").trim() || "";
      return resp && nm ? `${resp}: ${nm}` : r.textContent.replace(/\s+/g, " ").trim();
    });
    const edDecl = doc.getElementsByTagNameNS(TEI_NS, "editorialDecl")[0] || doc.getElementsByTagNameNS(TEI_NS, "projectDesc")[0];
    const edDeclParas = edDecl
      ? Array.from(edDecl.getElementsByTagNameNS(TEI_NS, "p")).map((p) => p.textContent.replace(/\s+/g, " ").trim())
      : [];

    const altIds = allOf("altIdentifier").map((a) => ({
      type: a.getAttribute("type") || "",
      val: a.textContent.replace(/\s+/g, " ").trim(),
    }));
    const iiifHint = (altIds.find((x) => x.type.toLowerCase() === "iiif") || {}).val || "";
    const textLangEl = allOf("textLang")[0];
    const mainLang = (textLangEl && (textLangEl.getAttribute("mainLang") || textLangEl.getAttribute("xml:lang"))) || "en";

    return { title, institution, shelfmark, origDate, origPlace, support, licenceText, licenceHref, resps, edDeclParas, iiifHint, mainLang };
  }

  function extractFrontAndBack(doc) {
    state.frontHtml = "";
    state.backHtml = "";
    if (!doc) return;
    const renderRichBlock = (node) => {
      if (node.nodeType === Node.TEXT_NODE) return escHtml(node.nodeValue.replace(/\s+/g, " "));
      if (node.nodeType !== Node.ELEMENT_NODE) return "";
      const name = node.localName.toLowerCase();
      const childrenHtml = Array.from(node.childNodes).map(renderRichBlock).join("");
      if (name === "head") return `<h5>${childrenHtml}</h5>`;
      if (name === "p") return `<p>${childrenHtml}</p>`;
      if (name === "listbibl") return `<ul class="bibl-list">${childrenHtml}</ul>`;
      if (name === "bibl") return `<li>${childrenHtml}</li>`;
      if (name === "title") return `<em>${childrenHtml}</em>`;
      if (name === "mentioned" || name === "q") return `<q class="note-quote">${childrenHtml}</q>`;
      if (name === "ref") {
        const href = expandCurie(node.getAttribute("target") || "");
        return href ? `<a href="${escHtml(href)}" target="_blank" rel="noopener">${childrenHtml || escHtml(href)}</a>` : childrenHtml;
      }
      if (name === "div") return `<div class="meta-subsection">${childrenHtml}</div>`;
      return childrenHtml;
    };
    const front = Array.from(doc.getElementsByTagNameNS(TEI_NS, "front")).concat(Array.from(doc.getElementsByTagName("front")))
      .find((el) => !el.closest("teiHeader"));
    if (front) state.frontHtml = Array.from(front.childNodes).map(renderRichBlock).join("").trim();

    const back = Array.from(doc.getElementsByTagNameNS(TEI_NS, "back")).concat(Array.from(doc.getElementsByTagName("back")))
      .find((el) => !el.closest("teiHeader"));
    if (back) state.backHtml = Array.from(back.childNodes).map(renderRichBlock).join("").trim();

    if (els.printFront) {
      els.printFront.innerHTML = state.frontHtml ? `<h3>Editorial Introduction</h3>${state.frontHtml}` : "";
    }
  }

  function collectFacsimile(doc) {
    state.zones = [];
    if (!doc) return { graphicUrl: null };
    const surf = doc.getElementsByTagNameNS(TEI_NS, "surface")[0] || doc.getElementsByTagName("surface")[0];
    if (!surf) return { graphicUrl: null };

    const lrx = parseFloat(surf.getAttribute("lrx")) || 1000;
    const lry = parseFloat(surf.getAttribute("lry")) || 1300;
    const ulx = parseFloat(surf.getAttribute("ulx")) || 0;
    const uly = parseFloat(surf.getAttribute("uly")) || 0;
    state.surfaceBox = { width: Math.max(1, lrx - ulx), height: Math.max(1, lry - uly) };

    const gfx = surf.getElementsByTagNameNS(TEI_NS, "graphic")[0] || surf.getElementsByTagName("graphic")[0];
    const graphicUrl = gfx ? gfx.getAttribute("url") : null;

    const zones = Array.from(surf.getElementsByTagNameNS(TEI_NS, "zone")).concat(
      Array.from(surf.getElementsByTagName("zone"))
    );
    const seen = new Set();
    for (const z of zones) {
      const id = xid(z);
      if (!id || seen.has(id)) continue;
      seen.add(id);
      const zulx = parseFloat(z.getAttribute("ulx"));
      const zuly = parseFloat(z.getAttribute("uly"));
      const zlrx = parseFloat(z.getAttribute("lrx"));
      const zlry = parseFloat(z.getAttribute("lry"));
      if ([zulx, zuly, zlrx, zlry].every((v) => !Number.isNaN(v))) {
        state.zones.push({ id, ulx: zulx, uly: zuly, lrx: zlrx, lry: zlry });
      }
    }
    return { graphicUrl };
  }

  function resolveRelativeUrl(u) {
    if (!u) return null;
    if (/^(https?:|blob:|data:)/i.test(u)) return u;
    try { return new URL(u, state.baseUrl).href; } catch (_) { return u; }
  }

  async function resolveIiifSource(url) {
    if (!url) return null;
    if (/info\.json(\?.*)?$/i.test(url)) {
      return { type: "iiif-info", tileSource: url, fallbackImg: url.replace(/info\.json.*$/, "full/max/0/default.jpg") };
    }
    try {
      const resp = await fetch(url);
      if (!resp.ok) return { type: "image", tileSource: url, fallbackImg: url };
      const data = await resp.json();
      // IIIF Presentation v3
      if (Array.isArray(data.items) && data.items[0]) {
        const body = data.items[0]?.items?.[0]?.items?.[0]?.body;
        const svc = Array.isArray(body?.service) ? body.service[0] : body?.service;
        const svcId = svc?.id || svc?.["@id"];
        const imgId = body?.id || (svcId ? `${svcId.replace(/\/$/, "")}/full/max/0/default.jpg` : null);
        if (svcId) return { type: "iiif-info", tileSource: `${svcId.replace(/\/$/, "")}/info.json`, fallbackImg: imgId };
        if (imgId) return { type: "image", tileSource: imgId, fallbackImg: imgId };
      }
      // IIIF Presentation v2
      if (Array.isArray(data.sequences) && data.sequences[0]) {
        const res = data.sequences[0]?.canvases?.[0]?.images?.[0]?.resource;
        const svcId = res?.service?.["@id"] || res?.service?.id;
        const imgId = res?.["@id"] || res?.id;
        if (svcId) return { type: "iiif-info", tileSource: `${svcId.replace(/\/$/, "")}/info.json`, fallbackImg: imgId };
        if (imgId) return { type: "image", tileSource: imgId, fallbackImg: imgId };
      }
    } catch (_) {}
    return { type: "image", tileSource: url, fallbackImg: url };
  }

  function renderSvgZoneBoxes() {
    const svg = els.zoneOverlay;
    svg.innerHTML = "";
    state.zonesById.clear();
    const { width, height } = state.surfaceBox;
    svg.setAttribute("viewBox", `0 0 ${width} ${height}`);

    for (const z of state.zones) {
      const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
      rect.setAttribute("x", String(z.ulx));
      rect.setAttribute("y", String(z.uly));
      rect.setAttribute("width", String(Math.max(1, z.lrx - z.ulx)));
      rect.setAttribute("height", String(Math.max(1, z.lry - z.uly)));
      rect.setAttribute("class", "zone-rect");
      rect.dataset.zoneId = z.id;
      const title = document.createElementNS("http://www.w3.org/2000/svg", "title");
      title.textContent = z.id;
      rect.appendChild(title);
      rect.addEventListener("click", (e) => {
        e.stopPropagation();
        highlightZoneAndText(z.id);
      });
      svg.appendChild(rect);
      state.zonesById.set(z.id, rect);
    }
  }

  function applySvgTransform() {
    els.svgTransform.style.transform = `translate(${state.svgPanX}px, ${state.svgPanY}px) scale(${state.svgZoom})`;
  }

  function resetImageViewport() {
    if (state.osdViewer) {
      state.osdViewer.viewport.goHome();
      return;
    }
    state.svgZoom = 1;
    state.svgPanX = 0;
    state.svgPanY = 0;
    applySvgTransform();
  }

  function zoomImageBy(factor) {
    if (state.osdViewer) {
      state.osdViewer.viewport.zoomBy(factor);
      state.osdViewer.viewport.applyConstraints();
      return;
    }
    state.svgZoom = Math.min(6, Math.max(0.6, state.svgZoom * factor));
    applySvgTransform();
  }

  function focusZone(zoneId) {
    const z = state.zones.find((item) => item.id === zoneId);
    if (!z) return;
    if (state.osdViewer && window.OpenSeadragon) {
      const { width, height } = state.surfaceBox;
      const pad = 0.05;
      const rect = new window.OpenSeadragon.Rect(
        Math.max(0, z.ulx / width - pad),
        Math.max(0, z.uly / height - pad),
        Math.min(1, (z.lrx - z.ulx) / width + 2 * pad),
        Math.min(1, (z.lry - z.uly) / height + 2 * pad)
      );
      state.osdViewer.viewport.fitBounds(rect);
    }
  }

  async function renderFacsimile(imgConfig) {
    if (state.osdViewer) {
      state.osdViewer.destroy();
      state.osdViewer = null;
    }
    els.osdStage.hidden = true;
    els.svgStage.hidden = true;
    els.facsEmpty.hidden = false;

    const rawUrl = imgConfig || state.imageSrc;
    if (!rawUrl) return;

    const resolved = await resolveIiifSource(rawUrl);
    if (!resolved) return;

    // Prefer OpenSeadragon only for IIIF tileSources when CDN loaded cleanly; use SVG stage for local/SVG or fallback
    const canUseOsd = typeof window.OpenSeadragon === "function" && resolved.type === "iiif-info";
    if (canUseOsd) {
      els.facsEmpty.hidden = true;
      els.osdStage.hidden = false;
      state.osdViewer = window.OpenSeadragon({
        id: "osdStage",
        prefixUrl: "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/images/",
        tileSources: resolved.tileSource,
        showNavigationControl: false,
      });
      state.osdViewer.addHandler("open", () => {
        const { width, height } = state.surfaceBox;
        state.zonesById.clear();
        for (const z of state.zones) {
          const box = document.createElement("div");
          box.className = "osd-zone";
          box.title = z.id;
          box.addEventListener("click", (e) => {
            e.stopPropagation();
            highlightZoneAndText(z.id);
          });
          state.osdViewer.addOverlay({
            element: box,
            location: new window.OpenSeadragon.Rect(z.ulx / width, z.uly / height, (z.lrx - z.ulx) / width, (z.lry - z.uly) / height),
          });
          state.zonesById.set(z.id, box);
        }
      });
      return;
    }

    const imgUrl = resolved.fallbackImg || resolved.tileSource;
    els.facsEmpty.hidden = true;
    els.svgStage.hidden = false;
    els.facsImg.onload = () => {
      if (state.surfaceBox.width === 1000 && els.facsImg.naturalWidth > 0 && !state.zones.length) {
        state.surfaceBox = { width: els.facsImg.naturalWidth, height: els.facsImg.naturalHeight };
      }
      renderSvgZoneBoxes();
    };
    els.facsImg.src = imgUrl;
    renderSvgZoneBoxes();
    resetImageViewport();
  }

  function renderPanesContent() {
    els.sourceBody.innerHTML = "";
    els.transBody.innerHTML = "";
    state.spansById.clear();

    const sDoc = state.docs.source;
    if (!sDoc) {
      els.sourceBody.innerHTML = "<p>No TEI edition loaded yet. Open <strong>Files</strong> above to load a TEI XML document.</p>";
      return;
    }

    const rootContainer =
      sDoc.getElementsByTagNameNS(TEI_NS, "group")[0] ||
      sDoc.getElementsByTagNameNS(TEI_NS, "body")[0] ||
      sDoc.getElementsByTagName("body")[0] ||
      sDoc.documentElement;

    const allCandidates = Array.from(sDoc.getElementsByTagName("*"));
    const embeddedTransDiv = allCandidates.find((el) => isTranslationNode(el)) || null;

    for (const child of rootContainer.childNodes) {
      const rendered = cloneTeiSubtree(child, { skipTranslation: true });
      if (rendered) els.sourceBody.appendChild(rendered);
    }

    if (state.docs.translation) {
      const tBody =
        state.docs.translation.getElementsByTagNameNS(TEI_NS, "body")[0] ||
        state.docs.translation.getElementsByTagName("body")[0] ||
        state.docs.translation.documentElement;
      const rendered = cloneTeiSubtree(tBody);
      if (rendered) els.transBody.appendChild(rendered);
      els.workspace.classList.remove("two-pane");
    } else if (embeddedTransDiv) {
      const rendered = cloneTeiSubtree(embeddedTransDiv);
      if (rendered) els.transBody.appendChild(rendered);
      els.workspace.classList.remove("two-pane");
    } else {
      els.transBody.innerHTML =
        '<p class="facs-empty" style="color:#64748b;">No translation layer present yet. Add a <code>&lt;div type="translation"&gt;</code> or load a translation TEI XML file to populate this pane.</p>';
      els.workspace.classList.add("two-pane");
    }
    els.btnToggleTrans.textContent = els.workspace.classList.contains("two-pane") ? "Show Translation Pane" : "Hide Translation Pane";
  }

  function collectLinks() {
    state.links = new Map();
    const linkPairs = [];
    const addLink = (a, b) => {
      if (a === b) return;
      if (!state.links.has(a)) state.links.set(a, new Set());
      state.links.get(a).add(b);
    };

    const allDocs = Object.values(state.docs).filter(Boolean);
    for (const doc of allDocs) {
      const linkEls = Array.from(doc.getElementsByTagNameNS(TEI_NS, "link")).concat(Array.from(doc.getElementsByTagName("link")));
      const seenLinks = new Set(linkEls);
      for (const l of seenLinks) {
        const targets = cleanRefs(l.getAttribute("target"));
        if (targets.length > 1) {
          linkPairs.push(targets);
          for (const a of targets) for (const b of targets) addLink(a, b);
        }
      }
      for (const el of doc.querySelectorAll("[corresp]")) {
        const id = xid(el);
        const targets = cleanRefs(el.getAttribute("corresp"));
        if (id && targets.length) {
          for (const t of targets) {
            addLink(id, t);
            addLink(t, id);
          }
        }
      }
    }
  }

  function noteHtmlFromElement(noteEl) {
    let out = "";
    for (const child of noteEl.childNodes) {
      if (child.nodeType === Node.TEXT_NODE) {
        out += escHtml(child.nodeValue.replace(/\s+/g, " "));
      } else if (child.nodeType === Node.ELEMENT_NODE) {
        const name = child.localName.toLowerCase();
        const ref = child.getAttribute("ref") || child.getAttribute("target") || "";
        const inner = noteHtmlFromElement(child);
        if (name === "mentioned" || name === "title") {
          out += `<em>${inner}</em>`;
        } else if (name === "quote" || name === "q") {
          out += `<q class="note-quote">${inner}</q>`;
        } else if (name === "bibl") {
          out += `<span class="note-bibl">Source: ${inner}</span>`;
        } else if (ref) {
          const href = expandCurie(ref);
          out += href ? `<a href="${escHtml(href)}" target="_blank" rel="noopener">${inner || escHtml(href)}</a>` : inner;
        } else {
          out += inner;
        }
      }
    }
    return out;
  }

  function expandCurie(ref) {
    if (!ref) return "";
    if (/^https?:/i.test(ref)) return ref;
    if (ref.startsWith("wikidata:")) return "https://www.wikidata.org/wiki/" + ref.slice(9);
    if (ref.startsWith("geonames:")) return "https://www.geonames.org/" + ref.slice(9);
    return "";
  }

  function collectNotes() {
    state.notes = [];
    document.querySelectorAll(".note-pin").forEach((p) => p.remove());

    const seenEl = new Set();
    const rawNotes = [];
    for (const doc of [state.docs.source, state.docs.commentary]) {
      if (!doc) continue;
      const noteNodes = Array.from(doc.getElementsByTagNameNS(TEI_NS, "note")).concat(Array.from(doc.getElementsByTagName("note")));
      for (const n of noteNodes) {
        if (seenEl.has(n)) continue;
        seenEl.add(n);
        if (n.closest("teiHeader") || !n.hasAttribute("target")) continue;
        rawNotes.push(n);
      }
    }

    let idx = 1;
    const unresolved = [];
    for (const n of rawNotes) {
      const targets = cleanRefs(n.getAttribute("target"));
      const noteObj = {
        index: idx++,
        id: xid(n) || `note_${idx}`,
        targets,
        type: (n.getAttribute("type") || "editorial").toLowerCase(),
        resp: n.getAttribute("resp") || "",
        html: noteHtmlFromElement(n).trim(),
        rawText: n.textContent.replace(/\s+/g, " ").trim(),
        resolved: false,
      };

      for (const t of targets) {
        const domMatches = state.spansById.get(t);
        if (domMatches && domMatches.length) {
          noteObj.resolved = true;
          const pin = document.createElement("button");
          pin.type = "button";
          pin.className = "note-pin";
          pin.textContent = `[${noteObj.index}]`;
          pin.title = `${noteObj.type} note (${noteObj.index})`;
          pin.dataset.noteIdx = String(noteObj.index);
          pin.addEventListener("click", (e) => {
            e.stopPropagation();
            openNotesDrawer(noteObj.index);
          });
          domMatches[0].insertAdjacentElement("afterend", pin);
          break;
        }
      }
      if (!noteObj.resolved) unresolved.push(...targets);
      state.notes.push(noteObj);
    }

    renderPrintAppendix();
    return unresolved;
  }

  function renderPrintAppendix() {
    const h = extractHeaderInfo(state.docs.source);
    let html = `<h3>Editorial Apparatus &amp; Commentary Notes</h3>`;
    if (h.edDeclParas?.length) {
      html += `<p><strong>Editorial Declaration:</strong> ${escHtml(h.edDeclParas.join(" "))}</p>`;
    }
    if (state.notes.length) {
      html += "<ol>";
      for (const n of state.notes) {
        html += `<li><strong>[${escHtml(n.type.toUpperCase())}]</strong> ${n.html} <em>(${escHtml(n.resp || "editor")})</em></li>`;
      }
      html += "</ol>";
    }
    if (state.backHtml) {
      html += `<h4>Bibliography &amp; Sources</h4>${state.backHtml}`;
    }
    els.printAppendix.innerHTML = html;
  }

  function clearHighlights() {
    for (const cls of ["w-sel", "w-linked", "seg-sel", "seg-linked", "s-sel", "s-linked", "facs-target-active"]) {
      document.querySelectorAll("." + cls).forEach((el) => el.classList.remove(cls));
    }
    state.zonesById.forEach((el) => el.classList.remove("zone-active"));
  }

  function extractReadingText(node, mode) {
    if (!node) return "";
    if (node.nodeType === Node.TEXT_NODE) return node.nodeValue.replace(/\s+/g, " ");
    if (node.nodeType !== Node.ELEMENT_NODE) return "";
    const ln = node.localName.toLowerCase().replace(/^tei-/, "");
    if (mode === "regularized") {
      if (ln === "orig" || ln === "abbr" || ln === "sic" || ln === "del") return "";
      if (ln === "lb") return node.getAttribute("break") === "no" ? "" : " ";
    } else {
      if (ln === "reg" || ln === "expan" || ln === "corr") return "";
      if (ln === "lb") return " ";
    }
    if (ln === "figure" || ln === "pb" || ln === "note") return "";
    return Array.from(node.childNodes).map((c) => extractReadingText(c, mode)).join("");
  }

  function dictionaryLinksForWord(queryWord, rawLang) {
    const lang = (rawLang || "en").toLowerCase().split(/[-_]/)[0];
    const clean = (queryWord || "").replace(/^[\s.,;:!?'"«»()\[\]]+|[\s.,;:!?'"«»()\[\]]+$/g, "");
    if (!clean) return [];
    const enc = encodeURIComponent(clean.toLowerCase());
    if (lang === "fr") {
      return [
        { label: "TLFi (CNRTL)", url: `https://www.cnrtl.fr/definition/${enc}` },
        { label: "Acad. francaise", url: `https://www.dictionnaire-academie.fr/search?term=${enc}` },
        { label: "Wiktionary FR", url: `https://fr.wiktionary.org/wiki/${enc}` },
      ];
    }
    if (lang === "grc" || lang === "la") {
      return [
        { label: "Logeion", url: `https://logeion.uchicago.edu/${enc}` },
        { label: "Wiktionary", url: `https://en.wiktionary.org/wiki/${enc}` },
      ];
    }
    return [
      { label: "Wiktionary", url: `https://en.wiktionary.org/wiki/${enc}` },
      { label: "OED Search", url: `https://www.oed.com/search/dictionary/?scope=Entries&q=${enc}` },
      { label: "Merriam-Webster", url: `https://www.merriam-webster.com/dictionary/${enc}` },
    ];
  }

  function hideWordPopover() {
    if (els.wordPopover) els.wordPopover.hidden = true;
  }

  function showWordPopover(wEl, anchorEl) {
    if (!els.wordPopover || !wEl) return;
    const origForm = extractReadingText(wEl, "diplomatic").replace(/\s+/g, " ").trim();
    const regForm = extractReadingText(wEl, "regularized").replace(/\s+/g, " ").trim() || origForm;
    const lemma = wEl.getAttribute("lemma") || regForm;
    const pos = wEl.getAttribute("pos") || "";
    const msd = wEl.getAttribute("msd") || "";
    const resp = wEl.getAttribute("resp") || "";
    const lang = wEl.closest("[lang]")?.getAttribute("lang") || state.defaultLang || "en";

    const entEl = wEl.closest("tei-persname, tei-placename, tei-orgname, tei-date");
    const authorityRef = entEl ? entEl.getAttribute("ref") || "" : "";
    const authorityHref = expandCurie(authorityRef);

    const wid = wEl.dataset.xmlid;
    const linkedWords = [];
    if (wid && state.links.has(wid)) {
      for (const tid of state.links.get(wid)) {
        for (const tEl of state.spansById.get(tid) || []) {
          linkedWords.push(tEl.textContent.replace(/\s+/g, " ").trim());
        }
      }
    }

    const dictLinks = dictionaryLinksForWord(lemma || regForm, lang);

    els.wordPopover.innerHTML = `
      <div class="wpop-head">
        <div>
          <span class="wpop-word">${escHtml(regForm || origForm)}</span>
          ${pos ? `<span class="wpop-pos">${escHtml(pos)}</span>` : ""}
        </div>
        <button type="button" class="wpop-close" id="btnCloseWpop" aria-label="Close word popover">&times;</button>
      </div>
      <div class="wpop-body">
        ${origForm !== regForm ? `<div class="wpop-row"><strong>Diplomatic:</strong> ${escHtml(origForm)} &rarr; <strong>Regularized:</strong> ${escHtml(regForm)}</div>` : ""}
        <div class="wpop-row"><strong>Lemma:</strong> <code>${escHtml(lemma)}</code> (${escHtml(lang)})${msd ? ` &middot; <strong>MSD:</strong> ${escHtml(msd)}` : ""}</div>
        ${resp ? `<div class="wpop-row"><strong>Resp:</strong> ${escHtml(resp)}</div>` : ""}
        ${authorityRef ? `<div class="wpop-row"><strong>Authority:</strong> ${authorityHref ? `<a href="${escHtml(authorityHref)}" target="_blank" rel="noopener">${escHtml(authorityRef)}</a>` : escHtml(authorityRef)}</div>` : ""}
        ${linkedWords.length ? `<div class="wpop-row"><strong>Aligned gloss:</strong> ${escHtml(linkedWords.join(" "))}</div>` : ""}
        ${dictLinks.length ? `<div class="wpop-links">${dictLinks.map((d) => `<a href="${escHtml(d.url)}" target="_blank" rel="noopener">${escHtml(d.label)}</a>`).join("")}</div>` : ""}
      </div>
    `;

    els.wordPopover.hidden = false;
    const rect = (anchorEl || wEl).getBoundingClientRect();
    const popWidth = Math.min(320, window.innerWidth - 24);
    const left = Math.min(window.innerWidth - popWidth - 12, Math.max(12, rect.left));
    const spaceBelow = window.innerHeight - rect.bottom;
    const top = spaceBelow > 190 ? rect.bottom + 6 : Math.max(12, rect.top - 185);
    els.wordPopover.style.left = `${left}px`;
    els.wordPopover.style.top = `${top}px`;

    const closeBtn = document.getElementById("btnCloseWpop");
    if (closeBtn) closeBtn.addEventListener("click", hideWordPopover);
  }

  function renderInterlinear() {
    if (!els.interlinearBody) return;
    els.interlinearBody.innerHTML = "";
    const sentences = Array.from(els.sourceBody.querySelectorAll("tei-s"));
    const blocks = sentences.length ? sentences : Array.from(els.sourceBody.querySelectorAll("tei-p, tei-head"));
    if (!blocks.length) {
      els.interlinearBody.innerHTML = "<p>Load a TEI edition with &lt;w&gt; or &lt;s&gt; elements to inspect the interlinear view.</p>";
      return;
    }

    for (const blk of blocks) {
      const sId = blk.dataset.xmlid || "";
      const wrap = document.createElement("div");
      wrap.className = "il-sentence";
      if (sId) wrap.dataset.xmlid = sId;

      const label = document.createElement("div");
      label.className = "il-head";
      label.textContent = sId ? `Sentence ${sId}` : "Block";
      wrap.appendChild(label);

      const grid = document.createElement("div");
      grid.className = "interlinear-grid";
      const words = Array.from(blk.querySelectorAll("tei-w"));
      if (words.length) {
        for (const w of words) {
          const wid = w.dataset.xmlid || "";
          const orig = extractReadingText(w, "diplomatic").replace(/\s+/g, " ").trim();
          const reg = extractReadingText(w, "regularized").replace(/\s+/g, " ").trim() || orig;
          const lemma = w.getAttribute("lemma") || "";
          const pos = w.getAttribute("pos") || "";

          const card = document.createElement("button");
          card.type = "button";
          card.className = "iw";
          if (wid) card.dataset.xmlid = wid;
          card.innerHTML = `
            <span class="iw-reg">${escHtml(reg)}</span>
            ${orig && orig !== reg ? `<span class="iw-orig">${escHtml(orig)}</span>` : ""}
            <span class="iw-morph">${escHtml([lemma, pos].filter(Boolean).join(" · ") || "—")}</span>
          `;
          card.addEventListener("click", (e) => {
            e.stopPropagation();
            handleTextClick(w, card);
            card.classList.add("w-sel");
          });
          grid.appendChild(card);
        }
      } else {
        const plain = document.createElement("span");
        plain.textContent = blk.textContent.replace(/\s+/g, " ").trim();
        grid.appendChild(plain);
      }
      wrap.appendChild(grid);

      if (sId && state.links.has(sId)) {
        const glossParts = [];
        for (const tid of state.links.get(sId)) {
          for (const tEl of state.spansById.get(tid) || []) {
            if (tEl.closest("#transBody")) {
              glossParts.push(extractReadingText(tEl, "regularized").replace(/\s+/g, " ").trim());
            }
          }
        }
        if (glossParts.length) {
          const gloss = document.createElement("div");
          gloss.className = "il-gloss";
          gloss.innerHTML = `<strong>Translation</strong> ${escHtml(glossParts.join(" "))}`;
          wrap.appendChild(gloss);
        }
      }

      els.interlinearBody.appendChild(wrap);
    }
  }

  function runQaChecks() {
    const allDocs = Object.values(state.docs).filter(Boolean);
    const idCounts = new Map();
    const allIds = new Set();
    const respStmts = [];
    const danglingPointers = [];
    const unresolvedResp = [];

    for (const doc of allDocs) {
      for (const el of doc.getElementsByTagName("*")) {
        const id = xid(el);
        if (id) {
          allIds.add(id);
          idCounts.set(id, (idCounts.get(id) || 0) + 1);
        }
        if (el.localName.toLowerCase() === "respstmt") {
          const txt = el.textContent.replace(/\s+/g, " ").trim();
          if (txt) respStmts.push(txt);
        }
      }
    }

    const dupIds = [...idCounts.entries()].filter(([, c]) => c > 1).map(([id]) => id);

    for (const doc of allDocs) {
      for (const el of doc.getElementsByTagName("*")) {
        for (const attrName of ["target", "corresp", "facs"]) {
          const val = el.getAttribute(attrName);
          if (!val) continue;
          for (const tok of val.trim().split(/\s+/)) {
            if (tok.startsWith("#")) {
              const refId = tok.slice(1);
              if (refId && !allIds.has(refId)) {
                danglingPointers.push(`${el.localName}@${attrName}=#${refId}`);
              }
            }
          }
        }
        const resp = el.getAttribute("resp");
        if (resp) {
          for (const tok of resp.trim().split(/\s+/)) {
            if (tok.startsWith("#") && !allIds.has(tok.slice(1))) {
              unresolvedResp.push(`${el.localName}@resp=${tok}`);
            }
          }
        }
      }
    }

    const srcSentences = Array.from(els.sourceBody.querySelectorAll("tei-s")).filter((s) => s.dataset.xmlid);
    const unlinkedSentences = srcSentences.filter((s) => !state.links.has(s.dataset.xmlid)).map((s) => s.dataset.xmlid);
    const hasTranslation = Boolean(state.docs.translation) || els.transBody.querySelectorAll("tei-s, tei-p").length > 0;

    // Commentary discipline checks: com_target, com_lemma (<quote>/<q>), unsourced_com (<bibl>/<ref>)
    const comErrors = [];
    const comWarnings = [];
    const rawNoteEls = [];
    for (const doc of [state.docs.source, state.docs.commentary]) {
      if (!doc) continue;
      for (const n of Array.from(doc.getElementsByTagNameNS(TEI_NS, "note")).concat(Array.from(doc.getElementsByTagName("note")))) {
        if (n.closest("teiHeader") || !n.hasAttribute("target")) continue;
        if (!rawNoteEls.includes(n)) rawNoteEls.push(n);
      }
    }
    for (const n of rawNoteEls) {
      const nid = xid(n) || "(note)";
      const refs = cleanRefs(n.getAttribute("target"));
      const resolvedAny = refs.some((r) => state.spansById.has(r));
      if (!resolvedAny) comErrors.push(`${nid}: unresolved target ${n.getAttribute("target")}`);
      const hasQuote = Array.from(n.getElementsByTagName("*")).some((c) => ["quote", "q"].includes(c.localName.toLowerCase()));
      if (!hasQuote) comWarnings.push(`${nid}: com_lemma — add <quote> citing target reading`);
      const hasSource = Array.from(n.getElementsByTagName("*")).some((c) => ["bibl", "ref"].includes(c.localName.toLowerCase()));
      if (!hasSource) comWarnings.push(`${nid}: unsourced_com — add <bibl> or <ref> authority source`);
    }

    const checks = [
      {
        id: "dup_ids",
        label: "Duplicate xml:id check",
        status: dupIds.length ? "error" : "ok",
        summary: dupIds.length ? `${dupIds.length} duplicate xml:id(s) found.` : `All ${allIds.size} xml:id attributes are unique.`,
        details: dupIds,
      },
      {
        id: "dangling",
        label: "Pointer integrity (#target, #corresp, #facs)",
        status: danglingPointers.length ? "error" : "ok",
        summary: danglingPointers.length
          ? `${danglingPointers.length} dangling # reference(s) found.`
          : "All internal #target, #corresp, and #facs pointers resolve.",
        details: [...new Set(danglingPointers)],
      },
      {
        id: "align_coverage",
        label: "Translation alignment coverage",
        status: !hasTranslation ? "ok" : unlinkedSentences.length ? "warn" : "ok",
        summary: !hasTranslation
          ? "No translation layer loaded yet (coverage check deferred)."
          : srcSentences.length
          ? `${srcSentences.length - unlinkedSentences.length}/${srcSentences.length} source <s> elements linked.`
          : "No tokenized <s> elements present in source pane.",
        details: unlinkedSentences.map((id) => `Unlinked source sentence: #${id}`),
      },
      {
        id: "com_checks",
        label: "Commentary discipline (target, <quote>, <bibl>/<ref>)",
        status: comErrors.length ? "error" : rawNoteEls.length === 0 || comWarnings.length ? "warn" : "ok",
        summary: rawNoteEls.length === 0
          ? "No <note target=\"#...\"> commentary notes encoded yet."
          : comErrors.length || comWarnings.length
          ? `${rawNoteEls.length} note(s): ${comErrors.length} broken target, ${comWarnings.length} missing <quote>/<bibl>.`
          : `All ${rawNoteEls.length} notes include valid targets, <quote> lemmas, and <bibl>/<ref> sources.`,
        details: [...comErrors, ...comWarnings],
      },
      {
        id: "model_credit",
        label: "Responsibility & AI credit (<respStmt>, @resp)",
        status: !respStmts.length || unresolvedResp.length ? "warn" : "ok",
        summary: !respStmts.length
          ? "Add a <respStmt> in <teiHeader> crediting human/AI responsibilities."
          : unresolvedResp.length
          ? `${unresolvedResp.length} @resp pointer(s) lack a matching xml:id in <respStmt>.`
          : `${respStmts.length} <respStmt> entry/entries documented; all @resp pointers resolve.`,
        details: [...new Set(unresolvedResp)],
      },
    ];

    state.qaChecks = checks;
    const errCount = checks.filter((c) => c.status === "error").length;
    const warnCount = checks.filter((c) => c.status === "warn").length;
    if (els.btnQA) {
      els.btnQA.classList.remove("qa-ok", "qa-warn", "qa-err");
      if (errCount) {
        els.btnQA.textContent = `QA (${errCount} err${warnCount ? `, ${warnCount} warn` : ""})`;
        els.btnQA.classList.add("qa-err");
      } else if (warnCount) {
        els.btnQA.textContent = `QA (${warnCount} warn)`;
        els.btnQA.classList.add("qa-warn");
      } else {
        els.btnQA.textContent = "QA (0)";
        els.btnQA.classList.add("qa-ok");
      }
    }
    return checks;
  }

  function openQaDrawer() {
    const checks = state.qaChecks.length ? state.qaChecks : runQaChecks();
    const errs = checks.filter((c) => c.status === "error").length;
    const warns = checks.filter((c) => c.status === "warn").length;
    const overall = errs ? "error" : warns ? "warn" : "ok";
    const headline = errs
      ? `${errs} error check(s) and ${warns} warning check(s) require attention before publication.`
      : warns
      ? `0 errors, ${warns} warning check(s) recommended before publication.`
      : "0 errors, 0 warnings — edition passed all structural and scholarly checks.";

    els.drawerTitle.textContent = "Edition QA Diagnostics";
    els.drawerBody.innerHTML = `
      <div class="qa-summary ${overall}">${escHtml(headline)}</div>
      ${checks
        .map(
          (c) => `
        <div class="qa-item qa-${c.status}">
          <div class="qa-item-head">
            <span>${escHtml(c.label)}</span>
            <span class="tag">${c.status.toUpperCase()}</span>
          </div>
          <div class="qa-item-detail">${escHtml(c.summary)}</div>
          ${c.details.length ? `<ul>${c.details.slice(0, 12).map((d) => `<li><code>${escHtml(d)}</code></li>`).join("")}</ul>` : ""}
        </div>`
        )
        .join("")}
    `;
    els.sideDrawer.hidden = false;
  }

  function highlightZoneAndText(zoneId) {
    clearHighlights();
    hideWordPopover();
    const zEl = state.zonesById.get(zoneId);
    if (zEl) zEl.classList.add("zone-active");
    focusZone(zoneId);

    const linkedEls = Array.from(document.querySelectorAll(`[data-facs~="${CSS.escape(zoneId)}"]`)).filter(
      (el) => el.localName !== "tei-pb"
    );
    linkedEls.forEach((el, i) => {
      el.classList.add("facs-target-active");
      if (i === 0) el.scrollIntoView({ block: "center", behavior: "smooth" });
    });
    els.inspectorBar.textContent = `Facsimile zone ${zoneId}: ${linkedEls.length} linked text element(s).`;
  }

  function handleTextClick(target, popAnchor = null) {
    clearHighlights();
    const infoParts = [];

    // 1. Check morphology & entity attributes
    const wEl = target.closest("tei-w");
    if (wEl && (wEl.hasAttribute("lemma") || wEl.hasAttribute("pos") || wEl.hasAttribute("msd"))) {
      const wordText = wEl.textContent.replace(/\s+/g, " ").trim();
      const lemma = wEl.getAttribute("lemma") || "—";
      const pos = wEl.getAttribute("pos") || "—";
      const msd = wEl.getAttribute("msd") || "";
      infoParts.push(`Word "${wordText}" · lemma: ${lemma} · UPOS: ${pos}${msd ? " · " + msd : ""}`);
    }

    const entEl = target.closest("tei-persname, tei-placename, tei-orgname");
    if (entEl && entEl.hasAttribute("ref")) {
      infoParts.push(`Authority: ${entEl.getAttribute("ref")}`);
    }

    // 2. Highlight aligned s / seg / w chains
    const levels = [];
    for (const cls of ["tei-w", "tei-seg", "tei-s"]) {
      const m = target.closest(cls);
      if (m && m.dataset.xmlid) levels.push(m);
    }

    let firstScrollTarget = null;
    for (const el of levels) {
      const id = el.dataset.xmlid;
      const role = el.localName.slice(4); // w | seg | s
      el.classList.add(`${role}-sel`);
      const counterparts = state.links.get(id);
      if (counterparts && counterparts.size) {
        const labels = [];
        for (const tid of counterparts) {
          const domList = state.spansById.get(tid) || [];
          for (const tEl of domList) {
            tEl.classList.add(`${role}-linked`);
            if (!firstScrollTarget && tEl.closest(".pane") !== el.closest(".pane")) {
              firstScrollTarget = tEl;
            }
            labels.push(tid);
          }
        }
        infoParts.push(`${role.toUpperCase()} ${id} -> ${[...new Set(labels)].join(", ")}`);
      }
    }
    if (firstScrollTarget) firstScrollTarget.scrollIntoView({ block: "center", behavior: "smooth" });

    // 3. Highlight matching @facs zone
    const facsEl = target.closest("[data-facs]");
    if (facsEl) {
      const zids = cleanRefs(facsEl.dataset.facs);
      for (const zid of zids) {
        const zRect = state.zonesById.get(zid);
        if (zRect) {
          zRect.classList.add("zone-active");
          focusZone(zid);
        }
      }
    }

    if (wEl && (wEl.closest("#sourceBody") || wEl.hasAttribute("lemma") || wEl.hasAttribute("pos"))) {
      showWordPopover(wEl, popAnchor || wEl);
    } else {
      hideWordPopover();
    }

    if (infoParts.length) {
      els.inspectorBar.textContent = infoParts.join("  |  ");
    }
  }

  function openAboutDrawer() {
    const h = extractHeaderInfo(state.docs.source);
    els.drawerTitle.textContent = "About this Digital Edition";
    els.drawerBody.innerHTML = `
      <div class="meta-section">
        <h4>Title &amp; Creators</h4>
        <p><strong>${escHtml(h.title || "Untitled Edition")}</strong></p>
        ${h.resps?.length ? `<ul>${h.resps.map((r) => `<li>${escHtml(r)}</li>`).join("")}</ul>` : ""}
      </div>
      ${state.frontHtml ? `<div class="meta-section"><h4>Editorial Introduction (&lt;front&gt;)</h4>${state.frontHtml}</div>` : ""}
      <div class="meta-section">
        <h4>Source Witness</h4>
        <p><strong>Repository:</strong> ${escHtml(h.institution || "—")}</p>
        <p><strong>Shelfmark / Call No.:</strong> ${escHtml(h.shelfmark || "—")}</p>
        <p><strong>Origin:</strong> ${escHtml([h.origDate, h.origPlace].filter(Boolean).join(", ") || "—")}</p>
        ${h.support ? `<p><strong>Material:</strong> ${escHtml(h.support)}</p>` : ""}
      </div>
      <div class="meta-section">
        <h4>Editorial Declaration (&lt;editorialDecl&gt;)</h4>
        ${h.edDeclParas?.length ? h.edDeclParas.map((p) => `<p>${escHtml(p)}</p>`).join("") : "<p>No &lt;editorialDecl&gt; encoded yet.</p>"}
      </div>
      ${state.backHtml ? `<div class="meta-section"><h4>Bibliography &amp; Sources (&lt;back&gt;)</h4>${state.backHtml}</div>` : ""}
      <div class="meta-section">
        <h4>Rights &amp; Licence</h4>
        <p>${escHtml(h.licenceText || "No <licence> specified.")}</p>
        ${h.licenceHref ? `<p><a href="${escHtml(h.licenceHref)}" target="_blank" rel="noopener">${escHtml(h.licenceHref)}</a></p>` : ""}
      </div>
    `;
    els.sideDrawer.hidden = false;
  }

  function openNotesDrawer(focusIdx = null) {
    els.drawerTitle.textContent = `Scholarly Commentary (${state.notes.length})`;
    const types = ["all", ...new Set(state.notes.map((n) => n.type))];
    const filtered = state.activeNoteFilter === "all" ? state.notes : state.notes.filter((n) => n.type === state.activeNoteFilter);

    const filterButtons = types
      .map((t) => `<button type="button" class="btn-outline" data-filter="${escHtml(t)}" aria-pressed="${state.activeNoteFilter === t}">${escHtml(t)}</button>`)
      .join("");

    const cards = filtered.length
      ? filtered
          .map(
            (n) => `
          <article class="note-card ${focusIdx === n.index ? "active" : ""}" id="drawer-note-${n.index}">
            <div class="note-meta">
              <span class="tag tag-${escHtml(n.type)}">${escHtml(n.type)}</span>
              <span>Note [${n.index}]</span>
              <span>Target: ${escHtml(n.targets.join(" "))}</span>
              ${n.resp ? `<span>Resp: ${escHtml(n.resp)}</span>` : ""}
            </div>
            <div>${n.html}</div>
          </article>`
          )
          .join("")
      : "<p>No stand-off <code>&lt;note target=\"#...\"&gt;</code> commentary notes encoded yet.</p>";

    els.drawerBody.innerHTML = `<div class="note-filters">${filterButtons}</div>${cards}`;
    els.drawerBody.querySelectorAll("[data-filter]").forEach((btn) => {
      btn.addEventListener("click", () => {
        state.activeNoteFilter = btn.dataset.filter;
        openNotesDrawer(focusIdx);
      });
    });

    els.sideDrawer.hidden = false;
    if (focusIdx) {
      const targetCard = document.getElementById(`drawer-note-${focusIdx}`);
      if (targetCard) targetCard.scrollIntoView({ block: "center", behavior: "smooth" });
    }
  }

  function rebuildEdition() {
    const h = extractHeaderInfo(state.docs.source);
    state.defaultLang = h.mainLang || "en";
    extractFrontAndBack(state.docs.source);
    renderPanesContent();
    collectLinks();
    renderInterlinear();
    const missingNoteTargets = collectNotes();
    runQaChecks();
    hideWordPopover();

    els.docTitle.textContent = h.title || "Digital Scholarly Edition";
    els.docSubtitle.textContent = [h.institution, h.shelfmark, h.origDate].filter(Boolean).join(" · ") || "Static TEI + IIIF Edition";

    // Diagnostics & unresolved # check
    const missingLinks = [...state.links.keys()].filter((id) => !state.spansById.has(id));
    const unresolved = [...new Set([...missingLinks, ...missingNoteTargets])];
    const facs = collectFacsimile(state.docs.source);
    const chosenImg = state.imageSrc || resolveRelativeUrl(facs.graphicUrl) || h.iiifHint;
    renderFacsimile(chosenImg);

    const wCount = els.sourceBody.querySelectorAll("tei-w").length;
    const sCount = els.sourceBody.querySelectorAll("tei-s").length;
    els.statusText.textContent = `XML valid · ${sCount} source sentences · ${wCount} tokens · ${state.notes.length} notes · ${state.zones.length} image zones`;
    els.statusWarn.textContent = unresolved.length ? `Unresolved #targets (${unresolved.length}): ${unresolved.slice(0, 8).join(", ")}` : "";
  }

  async function initFromConfig() {
    const cfg = parseConfig();
    if (cfg.view) setViewMode(cfg.view);

    const mainUrl = cfg.edition || cfg.source;
    if (!mainUrl) {
      els.loaderDrawer.hidden = false;
      return;
    }
    try {
      state.baseUrl = new URL(mainUrl, window.location.href).href;
      state.docs.source = parseXml(await loadTextUrl(state.baseUrl), mainUrl);
      if (cfg.translation) state.docs.translation = parseXml(await loadTextUrl(cfg.translation), cfg.translation);
      if (cfg.alignment) state.docs.alignment = parseXml(await loadTextUrl(cfg.alignment), cfg.alignment);
      if (cfg.commentary) state.docs.commentary = parseXml(await loadTextUrl(cfg.commentary), cfg.commentary);
      if (cfg.iiif) state.imageSrc = cfg.iiif;
      else if (cfg.image) state.imageSrc = resolveRelativeUrl(cfg.image);
      rebuildEdition();
    } catch (err) {
      els.loaderDrawer.hidden = false;
      els.statusWarn.textContent = `Auto-load note: ${err.message}. Use the Local File Loader above if opening offline.`;
    }
  }

  function wireEvents() {
    els.btnDiplomatic.addEventListener("click", () => setViewMode("diplomatic"));
    els.btnRegularized.addEventListener("click", () => setViewMode("regularized"));
    if (els.btnInterlinear) els.btnInterlinear.addEventListener("click", () => setViewMode("interlinear"));

    document.getElementById("chkEntities").addEventListener("change", (e) => {
      els.app.classList.toggle("show-entities", e.target.checked);
    });
    document.getElementById("chkNotes").addEventListener("change", (e) => {
      els.app.classList.toggle("show-notes", e.target.checked);
    });
    document.getElementById("chkIds").addEventListener("change", (e) => {
      els.app.classList.toggle("show-ids", e.target.checked);
    });

    els.btnToggleTrans.addEventListener("click", () => {
      const two = els.workspace.classList.toggle("two-pane");
      els.btnToggleTrans.textContent = two ? "Show Translation Pane" : "Hide Translation Pane";
    });
    els.btnAbout.addEventListener("click", openAboutDrawer);
    if (els.btnQA) els.btnQA.addEventListener("click", openQaDrawer);
    els.btnNotes.addEventListener("click", () => openNotesDrawer(null));
    els.btnFiles.addEventListener("click", () => { els.loaderDrawer.hidden = !els.loaderDrawer.hidden; });
    els.btnPrint.addEventListener("click", () => window.print());
    document.getElementById("btnCloseDrawer").addEventListener("click", () => { els.sideDrawer.hidden = true; });

    document.getElementById("btnZoomIn").addEventListener("click", () => zoomImageBy(1.25));
    document.getElementById("btnZoomOut").addEventListener("click", () => zoomImageBy(0.8));
    document.getElementById("btnZoomReset").addEventListener("click", resetImageViewport);

    // Pan & wheel zoom on built-in SVG stage
    els.svgStage.addEventListener("wheel", (e) => {
      e.preventDefault();
      zoomImageBy(e.deltaY < 0 ? 1.15 : 0.87);
    }, { passive: false });
    els.svgStage.addEventListener("pointerdown", (e) => {
      if (e.target.closest(".zone-rect")) return;
      state.dragging = true;
      state.dragStart = { x: e.clientX - state.svgPanX, y: e.clientY - state.svgPanY };
    });
    window.addEventListener("pointermove", (e) => {
      if (!state.dragging) return;
      state.svgPanX = e.clientX - state.dragStart.x;
      state.svgPanY = e.clientY - state.dragStart.y;
      applySvgTransform();
    });
    window.addEventListener("pointerup", () => { state.dragging = false; });

    // Delegate click on source and translation prose
    [els.sourceBody, els.transBody].forEach((pane) => {
      pane.addEventListener("click", (e) => {
        if (e.target.closest(".note-pin")) return;
        handleTextClick(e.target);
      });
    });

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") {
        hideWordPopover();
        if (!els.sideDrawer.hidden) els.sideDrawer.hidden = true;
      }
    });

    document.addEventListener("click", (e) => {
      if (!els.wordPopover || els.wordPopover.hidden) return;
      if (e.target.closest("#wordPopover") || e.target.closest("tei-w") || e.target.closest(".iw")) return;
      hideWordPopover();
    });

    // Local file inputs
    const bindFileXml = (inputId, key) => {
      const inp = document.getElementById(inputId);
      if (!inp) return;
      inp.addEventListener("change", async () => {
        const f = inp.files[0];
        if (!f) return;
        try {
          state.docs[key] = parseXml(await f.text(), f.name);
          els.statusWarn.textContent = "";
          rebuildEdition();
        } catch (err) {
          els.statusWarn.textContent = err.message;
        }
      });
    };
    bindFileXml("fileSource", "source");
    bindFileXml("fileTranslation", "translation");
    bindFileXml("fileAlignment", "alignment");
    bindFileXml("fileCommentary", "commentary");

    const fileImg = document.getElementById("fileImage");
    if (fileImg) {
      fileImg.addEventListener("change", () => {
        const f = fileImg.files[0];
        if (!f) return;
        state.imageSrc = URL.createObjectURL(f);
        renderFacsimile(state.imageSrc);
      });
    }

    const iiifInput = document.getElementById("inputIiifUrl");
    const btnIiif = document.getElementById("btnLoadIiif");
    if (btnIiif && iiifInput) {
      btnIiif.addEventListener("click", () => {
        const u = iiifInput.value.trim();
        if (!u) return;
        state.imageSrc = u;
        renderFacsimile(u);
      });
    }
  }

  wireEvents();
  initFromConfig();
})();
