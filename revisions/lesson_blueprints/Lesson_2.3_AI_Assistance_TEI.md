# Blueprint: Lesson 2.3 — AI Assistance in TEI Header Authoring
## Course: RELS 398 / ENGL 398 · Meeting #5

> **Source Specification:** [`SESSION_CONTENT_SPEC.md`](file:///home/kmpenner/projects/RELS/398/SESSION_CONTENT_SPEC.md) §2.3  
> **Key Reform:** Introducing Generative AI models and VS Code extensions only *after* students understand plain text, Git, XML syntax, and schema validation. Teaches structured prompt engineering, negative constraints, and the Three-Way Comparative Audit.

---

### Core Learning Objectives
1. Configure AI coding assistants in VS Code (Google Antigravity, Claude Code, GitHub Copilot).
2. Author structured prompts for TEI XML generation using explicit system personas, TEI P5 guidelines, and negative constraints against hallucinations.
3. Use AI to draft complex `<msDesc>` subsections (`<physDesc>`, `<handDesc>`, `<supportDesc>`) from raw archival catalogue prose.
4. Execute the course's foundational Three-Step Audit: diffing AI-generated XML against manual authority records (VIAF, LCNAF, British Library / Archives nationales records), identifying errors, and merging validated elements into the final edition header.

---

### 50-Minute Classroom Progression

#### 1. The Role of Generative AI in Digital Humanities (10 mins)
* AI as an accelerator, not an authority.
* Why an unguided LLM invents nonexistent TEI elements (e.g., `<inkColor>`, `<manuscriptDimensions>`) unless strictly constrained by schemas.
* The rule of negative constraints: explicitly forbidding modernization, hallucinated shelfmarks, or unverified author names.

#### 2. Structured Prompt Engineering for TEI `<msDesc>` (15 mins)
* Feeding the AI a raw archival catalogue description and prompting for valid TEI P5 `<msDesc>`:
  ```text
  SYSTEM PROMPT:
  You are an expert Digital Humanities XML encoder. You output strictly valid TEI P5 XML conforming to the msdesc.rng schema.
  
  TASK:
  Convert the following archival description into a valid TEI <physDesc> block.
  
  NEGATIVE CONSTRAINTS:
  - Do not use markdown backticks; output raw XML only.
  - Do not invent elements not in TEI P5 (e.g., do not invent <quires> or <bindingDesc> if unmentioned).
  - Use exact NCName values for @xml:id (no spaces).
  - Every attribute value must be strictly valid under RELAX NG.
  
  CATALOGUE TEXT:
  [Insert British Library / Archives nationales description]
  ```

#### 3. In-Editor AI Execution & Side-by-Side Diff (15 mins)
* Running the prompt in VS Code (Antigravity / Copilot / Claude Code) and saving output to `header_ai.xml`.
* Using VS Code's side-by-side diff:
  ```bash
  code --diff header.xml header_ai.xml
  ```
* Auditing the differences:
  * Did the AI hallucinate dimensions?
  * Did it invent an authority file URI?
  * Did it format dates using ISO 8601 (`@when="1791-10-31"`) or natural language?

#### 4. The Synthesized Merge & Push (10 mins)
* Merge the best AI elements (e.g., detailed `<handNote>` descriptions) into `header.xml`.
* Validate locally and push to GitHub:
  ```bash
  xmllint --noout --relaxng schemas/msdesc.rng header.xml
  git add header.xml header_ai.xml
  git commit -m "Step 3 (ai): synthesize ai-assisted msDesc elements and verify schema compliance"
  git push origin main
  ```
* Verify GitHub Actions turns green.

#### 5. Exit Ticket / Milestone
* Module 2 assignment milestone: pushed repository containing validated `header.xml`, raw `header_ai.xml`, and the audit reflection in `README.md`.
