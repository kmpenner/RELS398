# Session content spec vs. current lessons

**Given by Ken:** 2026-09-10.
**Purpose:** what each session should cover, verbatim, compared against what the lessons currently contain.

## The spec

> **1.1** The Scholarly edition pipeline tasks (catalog, photograph, transcribe (diplomatic), regularize (normalized), collate (if multiple exemplars), parse (lemma and MSD attribute of `w` element), markup named entities, translate, comment, present/publish) across the course pattern (Manual, Deterministic, AI).
>
> **1.2** FAIR principles, bash, text files, `.md` files, choosing a historical document, git
>
> **2.1** git, XML files, TEI, TEI header, writing a TEI header manually with bash `echo >` and `>>`
>
> **2.2** VS Code, Red Hat XML extension, schemas, DTDs, Relax NG, TEI validator extension for VS Code
>
> **2.3** AI accounts, AI extensions for VS Code: Antigravity/Claude Code/GitHub Copilot/Codex, AI assistance making TEI header element
>
> **3.1** The manual lesson: TEI spec for facsimile, surface, and zone; considerations and techniques when making digital images of historical documents (epigraphs, papyri, scrolls, manuscripts, codices, books, maps, illustrations, etc.); preparing students to photograph or scan a historical document; advanced imaging (multispectral, infrared, raking light, RTI).
>
> **3.2** The deterministic/algorithmic computer-assisted lesson: the IIIF standard; open source image editing software (GIMP, ImageMagick, libvips); operations (cropping, contrast, colour adjustment, masking, deskewing, sharpening); file storage formats (JPEG, GIF, PNG, TIFF, PDF, etc. — compression, colour spaces, bit depth, archival masters vs web derivatives).
>
> **3.3** The AI-assisted imaging lesson: how AI can make the activities in lesson 3.1 and 3.2 more efficient — adding bounding boxes for zones (layout analysis, segmenting text lines/regions), organizing & naming images (automated metadata extraction, sequence ordering), inserting and aligning facsimile elements with text.

## What the spec implies structurally

The tools form a deliberate **ladder**, and the current lessons have it out of order:

| Spec order | Tool introduced | Where it currently sits |
|---|---|---|
| 1.2 | bash, text files, git | **1.1** (s5 command line, s7–13 git, s2/s4 text and `.md`) |
| 2.1 | XML/TEI written **by hand in the shell** (`echo >`, `>>`) | 2.1 writes the header in **VS Code** (s28) |
| 2.2 | **VS Code** + extensions + schemas + DTD + RNG | VS Code is introduced in **1.1** (s3) |
| 2.3 | **AI accounts + AI extensions** | AI is introduced in **1.1** (s25–28) |

So the intended progression is **shell → editor → AI**, and the current lessons front-load the editor and the AI into 1.1. The 2.1 change is the clearest signal: the header is built with `echo >` and `>>` *before* VS Code appears in 2.2.

Also note **1.1's spec is the pipeline**, which currently lives in **1.2** (s10–19, "The Workflow: Eight Stages").

## Gap analysis

### 1.1 — spec: the pipeline × Manual/Deterministic/AI

**Current (30 sections, 7,621 words):** a toolkit tour — plain text, VS Code, command line, git, XML/TEI basics, Python, LLMs, Antigravity, the three-step method.

**Gap:** the pipeline is in 1.2, not here. 1.1 has tools instead of the domain. Ken's list is also **10 tasks** against 1.2's **8 stages** — his adds *markup named entities* and splits *parse (lemma and MSD on `<w>`)* out of "linguistic markup", and separates *comment* from *translate*:

| Ken's task | 1.2's stage |
|---|---|
| catalog | 1 Cataloguing the witnesses |
| photograph | 2 Digitization and IIIF |
| transcribe (diplomatic) | 3 Transcription |
| regularize (normalized) | 4 Reconciliation and normalization |
| collate (if multiple exemplars) | 5 Collation and textual criticism |
| **parse (lemma + MSD @ `w`)** | 6 Linguistic markup (combined) |
| **markup named entities** | — (absent) |
| translate | 7 Translation and annotation |
| **comment** | 7 (combined with translate) |
| present/publish | 8 Presentation and publication |

**Needed:** move the pipeline to 1.1, restate it as 10 tasks, and frame each across the three modes. Drop or relocate the tool survey.

### 1.2 — spec: FAIR, bash, text files, `.md`, choosing a document, git

**Current:** FAIR (s5–9, good), the pipeline (s10–19, should move to 1.1), VS Code tools (s20–21), accounts (s22), platform FAIRness (s23–25), choosing the passage (s26–28, good), checklist (s29).

**Gap:** **bash and git are absent** — both live in 1.1. Text files and `.md` are also in 1.1 (s2, s4).

**Needed:** bring bash, text files, `.md` and git here; move the pipeline out to 1.1.

### 2.1 — spec: git, XML, TEI, header, **written with `echo >` and `>>`**

**Current:** strong on the header — XML tree (s5–6), `<teiHeader>` (s7–8), all four pillars, `<msIdentifier>`, `<msContents>`, `<physDesc>`, hands, layout, provenance (s9–25), template (s26), traps (s27).

**Gap:** **zero uses of `echo >` or `echo >>`.** The header is written in VS Code (s28) with `git commit` (s29). Under the spec, the shell is the tool here and VS Code arrives in 2.2.

**Needed:** rewrite s28 to build the header with `echo` and `>>` in the shell — including the pedagogical point that appending line by line is how you learn the structure, and that a mistyped redirect (`>` instead of `>>`) silently destroys the file.

### 2.2 — spec: VS Code, Red Hat XML, schemas, DTDs, Relax NG, TEI validator

**Current:** RELAX NG (s2, s4–5), validation in VS Code (s3, s24–25), Schematron (s6–7), ODD (s8–10), then authority control and citation (s11–28).

**Gap:**
- **DTDs are not taught** — one passing mention.
- **Red Hat XML appears only** in a note I inserted today, and it is framed as the *wrong* tool.
- **No TEI validator extension is named for installation.**

**Needed:** teach DTD vs XSD vs RELAX NG as the three schema languages; introduce VS Code properly *as new here*; and name the extensions to install.

### 2.3 — spec: AI accounts, AI extensions, AI making header elements

**Current (my rebuild today):** the audit method — find the information, record it, prompt, gate, compare, hallucination taxonomy, the comparison write-up. 30 sections, 8,211 words. Good material, and it is what the workshop grades.

**Gap:**
- **AI accounts: absent.** No section on creating them.
- **None of the four extensions is mentioned.** Zero occurrences of Antigravity, Claude Code, or Copilot. ("Codex" matches five times, all the manuscript sense of *codex*.)
- **"AI assistance making TEI header element"** is covered *methodologically* (prompt → output → audit) but not as a tooling task in the editor.

**Needed:** add the accounts step and the extension survey, and connect the audit to generating header elements inside VS Code rather than in a chat window. *(Closed in commits 3669c39 and dd391e1).*

### 3.1 — spec: Manual imaging, TEI facsimile/surface/zone, photography/scanning across media, advanced imaging

**Current:** "IIIF Foundations: The Image API, the Presentation API, and the Canvas". Has a front banner claiming "Infrastructure week — the three-step comparative cycle does not apply."

**Gap:**
- Does **not** teach the TEI `<facsimile>`, `<surface>`, and `<zone>` specifications.
- Does **not** prepare students for photographing or scanning physical historical documents (lighting, geometry, color checkers, scale bars, document supports, handling precautions).
- Covers historical media inadequately (epigraphs, papyri, scrolls, manuscripts, codices, books, maps, illustrations).
- Advanced imaging (multispectral, infrared, raking light, RTI) was misplaced into 3.2.

**Needed:** Rebuild 3.1 as the foundational manual lesson: TEI facsimile elements (`<facsimile>`, `<surface>`, `<zone>`), document photography and scanning field techniques across diverse physical media, and physical/optical recovery methods (multispectral, infrared, raking light, RTI).

### 3.2 — spec: Deterministic/algorithmic computer-assisted imaging, IIIF standard, open-source software, image operations, file storage formats

**Current:** "Raking Light, Multispectral Imaging, and Computational Palaeography".

**Gap:**
- The IIIF standard (Image API, Presentation API, Manifest, Canvas) was misplaced in 3.1 instead of 3.2.
- Missing coverage of open-source image editing software (GIMP, ImageMagick, libvips).
- Missing deterministic/algorithmic operations: cropping, contrast, colour adjustment / white balance, masking, deskewing, sharpening.
- Missing comprehensive file storage formats: JPEG, GIF, PNG, TIFF, PDF (compression lossy vs lossless, bit depth, colour spaces, archival master vs derivative web delivery).

**Needed:** Rebuild 3.2 as the deterministic computer-assisted lesson: bring the IIIF standard here, teach open-source tools (ImageMagick CLI, GIMP, libvips), programmatic image operations, and archival/web file storage formats.

### 3.3 — spec: AI-assisted imaging, automated bounding boxes, organizing/naming images, aligning facsimile with text

**Current:** "Building the Manifest and Binding It to TEI". Hand-crafts JSON-LD manifests and manual canvas binding.

**Gap:**
- Does **not** teach AI-assisted layout analysis or automated bounding boxes for `<zone>` elements.
- Does **not** teach AI-driven organization, naming pipelines, or sequence ordering for document images.
- Does **not** teach AI assistance in inserting and aligning `<facsimile>` elements with transcribed text.

**Needed:** Rebuild 3.3 as the AI-assisted imaging lesson: automated bounding boxes and layout analysis (detecting blocks, lines, marginalia), AI-assisted image organization and naming, and aligning `<facsimile>` elements to text.

## The extension question — verified

Ken's spec says "Red Hat XML extension" **and** "TEI validator extension for VS Code". Both are right, for different jobs:

| Extension | What it validates | Evidence |
|---|---|---|
| **Red Hat XML** (`redhat.vscode-xml`) | DTD, XSD — the general-purpose XML extension | See caveat below |
| **Scholarly XML** (`raffazizzi.sxml`) | **RELAX NG and Schematron** | Marketplace listing, verified 2026-09-10 |

**Scholarly XML** is almost certainly the "TEI validator extension" meant, and the listing settles why it is the right choice for students:

- *"a RELAX NG and Schematron validator and autocomplete with features typically needed by academic encoding projects"*
- *"Unlike most XML VSCode extensions, Scholarly XML **does not require Java**"* — it is built on a TypeScript RELAX NG implementation (a fork of Salve), which the publisher says *"makes Scholarly XML easy to install for use with students, in workshops, and in minimal computing projects"*
- Awarded the **Rahtz Prize for TEI Ingenuity (2024)**
- 19,453 installs, rated 5/5

**Caveat on Red Hat XML.** My note in 2.2 today says it "validates DTD and XSD" and that "only Scholarly XML checks RELAX NG". I could not re-verify whether recent `vscode-xml` releases have added RELAX NG support — the release page I fetched returned only navigation. **Verify before teaching it as fact**, because if Red Hat XML does handle RELAX NG, my note is wrong and would send students to install an extension they do not need.

## Recommendation

**For tomorrow (2.2 + 2.3):** the gaps are small enough to close tonight and large enough to matter — 2.2 is missing DTDs and the named extension, and 2.3 is missing the entire accounts-and-extensions step that the session is supposed to open with.

**For 1.1, 1.2 and 2.1:** these have been taught, so rewriting them now does not reach the students. They need a restructure — the pipeline moves 1.2 → 1.1, and bash/git/text/`.md` move 1.1 → 1.2, with 2.1's header written by `echo` — before the course runs again.
