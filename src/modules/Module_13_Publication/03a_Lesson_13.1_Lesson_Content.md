# Lesson 13.1 — Formulating Editorial Principles, Methodology, and the Edition Introduction

*RELS 398 / ENGL 398 · Topic 13: Publication · Meeting #34 (Tue Dec 1)*

***Studio and publication assembly week (no three-step cycle).** Today you formulate the complete Editorial Introduction and Principles in TEI `<editorialDecl>` for your capstone digital edition portfolio. You document the historical context, physical materiality, and provenance of your primary witness (Ace: 1791 French decree; Olyvia: 1967 Maud Lewis letter; Andromeda: 1752 Peace and Friendship Treaty), establish open access licensing, and organize your master repository.*

---

## **01 Content**

**Entering the Studio: The Capstone Digital Scholarly Edition**

Welcome to Week 13. Over the past twelve weeks, you have learned the core crafts of digital textual scholarship. You began in September with basic text files and the command line. You catalogued historical documents, transcribed handwritten ink, normalized archaic spelling, parsed grammar, aligned translations, and authored commentary.

This week is our **capstone publication studio**. There is no three-step cycle this week. Instead, every class meeting focuses on bringing your work together into a unified digital scholarly edition.

A digital edition is not just a folder of separate files. It is an integrated scholarly publication. Readers should be able to view high-resolution page images, read your careful transcription, inspect your historical notes, and check your editorial decisions.

This week, you will assemble your work into a publication-grade edition. Today, you will write the editorial introduction and formal editorial principles.

**Vocabulary.** *Digital Scholarly Edition (DSE)* — a digital publication of a historical text that provides critical paratexts, images, and tools beyond a printed book. *Capstone Studio* — a collaborative workshop where students integrate semester-long projects into finished publications.

**Takeaway:** Week 13 brings together all your semester projects into an integrated, publication-grade digital scholarly edition.

---

## **02 Content**

**The Anatomy of a Digital Edition Portfolio**

A complete digital edition unites several editorial layers created across the term:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px; text-align: left; width: 25%;">Editorial Layer</th>
      <th style="padding: 8px; text-align: left; width: 40%;">What It Provides</th>
      <th style="padding: 8px; text-align: left; width: 35%;">TEI XML Element</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>1. Catalogue Metadata</strong></td>
      <td style="padding: 8px;">Document title, repository, dates, and physical description</td>
      <td style="padding: 8px;"><code>&lt;teiHeader&gt;</code>, <code>&lt;msDesc&gt;</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>2. Facsimile Binding</strong></td>
      <td style="padding: 8px;">High-resolution archival images with coordinate zones</td>
      <td style="padding: 8px;"><code>&lt;facsimile&gt;</code>, <code>&lt;surface&gt;</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>3. Diplomatic Text</strong></td>
      <td style="padding: 8px;">Exact character-by-character transcription of ink on paper</td>
      <td style="padding: 8px;"><code>&lt;body&gt;</code>, <code>&lt;lb/&gt;</code>, <code>&lt;pb/&gt;</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>4. Regularized Text</strong></td>
      <td style="padding: 8px;">Standardized modern spelling for searchability</td>
      <td style="padding: 8px;"><code>&lt;choice&gt;</code>, <code>&lt;orig&gt;</code>, <code>&lt;reg&gt;</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>5. Linguistic Markup</strong></td>
      <td style="padding: 8px;">Dictionary lemmas and grammatical tags</td>
      <td style="padding: 8px;"><code>&lt;w lemma="" pos=""&gt;</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>6. Named Entities</strong></td>
      <td style="padding: 8px;">People, places, and organizations linked to authority records</td>
      <td style="padding: 8px;"><code>&lt;persName&gt;</code>, <code>&lt;placeName&gt;</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>7. Parallel Alignment</strong></td>
      <td style="padding: 8px;">Bilingual translation linked sentence by sentence</td>
      <td style="padding: 8px;"><code>&lt;linkGrp&gt;</code>, <code>&lt;link&gt;</code></td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>8. Scholarly Commentary</strong></td>
      <td style="padding: 8px;">Historical, linguistic, and intertextual notes in standoff markup</td>
      <td style="padding: 8px;"><code>&lt;standOff&gt;</code>, <code>&lt;note&gt;</code></td>
    </tr>
  </tbody>
</table>

When these layers link together seamlessly, your edition becomes an authoritative research tool.

**Takeaway:** A digital edition combines eight distinct editorial layers into a single structured master document.

---

## **03 Content**

**The Purpose of the Editorial Introduction**

Historical documents cannot explain their own origins. A raw transcription leaves readers with urgent questions:
<ul>
  <li>Where is the original manuscript kept today?</li>
  <li>Who created this document, and why?</li>
  <li>What condition is the paper or parchment in?</li>
  <li>What rules did the editor follow when expanding abbreviations or modernizing words?</li>
</ul>

The **Editorial Introduction** answers these questions. It is the scholar's preface. It sets up your authority as an editor. It gives readers the historical context they need to understand your primary witness.

Without an introduction, your edition is a puzzle. With an introduction, your edition becomes a trustworthy scholarly reference.

**Takeaway:** The editorial introduction sets up context, explains document history, and makes editorial decisions transparent to readers.

---

## **04 Content**

**The Twofold Introduction: Narrative Preface vs Machine Metadata**

In a standard printed book, the introduction is simply a written essay at the beginning. In a digital edition, the introduction exists in two complementary forms:
<ul>
  <li><strong>The Narrative Preface:</strong> A readable essay written for humans. It appears on the opening webpage or the first pages of a printed PDF. It explains historical background and summarizes key findings.</li>
  <li><strong>The Machine-Actionable Metadata:</strong> Structured XML tags stored inside the <code>&lt;teiHeader&gt;</code>. Software can read this data to index dates, creators, and editorial rules automatically.</li>
</ul>

Both forms are vital:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px; text-align: left; width: 30%;">Feature</th>
      <th style="padding: 8px; text-align: left; width: 35%;">Narrative Preface</th>
      <th style="padding: 8px; text-align: left; width: 35%;">TEI Header Metadata</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Audience</strong></td>
      <td style="padding: 8px;">Human students and researchers</td>
      <td style="padding: 8px;">Search engines and XML processors</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Format</strong></td>
      <td style="padding: 8px;">Markdown prose or HTML paragraphs</td>
      <td style="padding: 8px;">Standardized TEI XML elements</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Primary Location</strong></td>
      <td style="padding: 8px;"><code>README.md</code> and front matter</td>
      <td style="padding: 8px;"><code>&lt;teiHeader&gt;&lt;encodingDesc&gt;</code></td>
    </tr>
  </tbody>
</table>

Today you will author both the narrative prose and its structured TEI representation.

**Takeaway:** Digital editions provide a twofold introduction: narrative prose for human readers and structured XML metadata for machines.

---

## **05 Content**

**The Single-Witness Documentary Edition**

In older philology, scholars often worked with dozens of damaged copies of ancient Greek or Latin texts. They built family trees of manuscripts (called *stemmata*) to reconstruct a lost original.

Our course takes a different, modern path: the **single-witness documentary edition**.

Each student in our cohort is working with one unique archival document:
<ul>
  <li>Ace edits a specific 1791 Paris printing of a revolutionary decree.</li>
  <li>Olyvia edits a handwritten personal letter mailed by Maud Lewis in 1967.</li>
  <li>Andromeda edits the official 1752 treaty proclamation held in Halifax.</li>
</ul>

In documentary editing, our goal is not to fix or alter the past. Our goal is to represent our specific witness with absolute fidelity, documenting its physical ink, handwriting quirks, and social context.

**Vocabulary.** *Documentary Edition* — a scholarly edition focused on representing the exact text and physical features of a specific historical manuscript or print copy.

**Takeaway:** Our cohort creates single-witness documentary editions, prioritizing deep fidelity to individual historical artifacts over multi-witness collation.

---

## **06 Content**

**Introducing Ace's Witness: 1791 French Revolutionary Decree**

Let us examine how to write the introduction for Ace's document: the *Loi relative à la fabrication des assignats* (May 1791).

Key historical points to cover in the introduction:
<ul>
  <li><strong>Political Context:</strong> In 1791, the National Assembly was restructuring France. The monarchy was losing power, and King Louis XVI was forced to sanction assembly laws.</li>
  <li><strong>Economic Crisis:</strong> France faced massive public debt. The assembly issued paper money (*assignats*) backed by confiscated church lands.</li>
  <li><strong>The 5-Livre Problem:</strong> Early notes were only printed in huge amounts. Workers and soldiers could not buy food. This decree ordered the production of small 5-livre bills to fix coin shortages.</li>
  <li><strong>Physical Printing:</strong> Printed by the Imprimerie Royale in Paris, featuring official royal typography and legal seals.</li>
</ul>

The introduction explains why this small piece of paper represents a turning point in world history.

**Takeaway:** Ace's introduction frames the 1791 decree within the French Revolution's monetary collapse, paper assignats, and royal legal sanction.

---

## **07 Content**

**Introducing Olyvia's Witness: 1967 Maud Lewis Letter**

Next, let us consider Olyvia's document: Maud Lewis's February 1967 letter to Leonard Kinnear.

Key biographical and cultural points to include:
<ul>
  <li><strong>The Writer:</strong> Maud Lewis (1903–1970) lived in a tiny one-room house in Marshalltown near Digby, Nova Scotia. Despite severe arthritis, she painted cheerful scenes of maritime life.</li>
  <li><strong>The Correspondent:</strong> Leonard Kinnear was an amateur collector from Moncton, New Brunswick, who ordered paintings through the mail.</li>
  <li><strong>The 1960s Art Market:</strong> Following national CBC television broadcasts in 1965, tourists and collectors flooded her cottage. Maud continued selling paintings for just \$6.00 each.</li>
  <li><strong>Physical Characteristics:</strong> Handwritten in blue ink on folded letter paper, featuring phonetic folk spelling and intimate personal updates.</li>
</ul>

The introduction helps readers appreciate the quiet dignity of Nova Scotia's most beloved folk artist.

**Takeaway:** Olyvia's introduction highlights Maud Lewis's daily life, modest pricing, folk spelling, and personal correspondence with collector Leonard Kinnear.

---

## **08 Content**

**Introducing Andromeda's Witness: 1752 Peace and Friendship Treaty**

Now let us look at Andromeda's document: the 1752 Peace and Friendship Treaty concluded at Halifax.

Key diplomatic and legal context to include:
<ul>
  <li><strong>Signatories:</strong> Negotiated between Mi'kmaw Chief Jean-Baptiste Cope of Shubenacadie and Nova Scotia Governor Peregrine Hopson.</li>
  <li><strong>Diplomatic Purpose:</strong> Renewed peaceful trade and security following years of colonial conflict in Mi'kma'ki.</li>
  <li><strong>Key Provisions:</strong> Guaranteed hunting and fishing rights, promised gift exchanges, and set up a government trading post (truckhouse).</li>
  <li><strong>Archival Provenance:</strong> Preserved in the Nova Scotia Archives in Halifax (Record Group 1, volume 430, number 2).</li>
</ul>

The introduction grounds the treaty in 18th-century Maritime history, explaining its lasting importance for Indigenous rights.

**Takeaway:** Andromeda's introduction documents the 1752 treaty negotiations between Chief Cope and Governor Hopson, emphasizing ongoing Mi'kmaw resource rights.

---

## **09 Content**

**Describing the Physical Artifact in `<sourceDesc>` and `<msDesc>`**

In TEI XML, physical descriptions live inside the `<teiHeader>`. You record them using `<sourceDesc>` and `<msDesc>`:
<pre><code>&lt;sourceDesc&gt;
  &lt;msDesc&gt;
    &lt;msIdentifier&gt;
      &lt;country&gt;Canada&lt;/country&gt;
      &lt;region&gt;Nova Scotia&lt;/region&gt;
      &lt;settlement&gt;Halifax&lt;/settlement&gt;
      &lt;repository&gt;Nova Scotia Archives&lt;/repository&gt;
      &lt;idno&gt;RG 1 vol 430 no 2&lt;/idno&gt;
    &lt;/msIdentifier&gt;
    &lt;physDesc&gt;
      &lt;objectDesc form="single_sheet"&gt;
        &lt;supportDesc material="paper"&gt;
          &lt;extent&gt;4 pages (folded folio)&lt;/extent&gt;
        &lt;/supportDesc&gt;
      &lt;/objectDesc&gt;
    &lt;/physDesc&gt;
  &lt;/msDesc&gt;
&lt;/sourceDesc&gt;</code></pre>

This markup records where the physical object is stored and what it is made of, creating a permanent archival record.

**Takeaway:** Use msDesc inside sourceDesc to record the repository, shelfmark, physical support, and dimensions of your document.

---

## **10 Content**

**Documenting Materiality: Parchment, Paper, Seals, and Ink**

A digital edition should help readers imagine the physical object. In your introduction, describe its physical material:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px; text-align: left; width: 25%;">Material Feature</th>
      <th style="padding: 8px; text-align: left; width: 35%;">What to Look For</th>
      <th style="padding: 8px; text-align: left; width: 40%;">Cohort Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Support Medium</strong></td>
      <td style="padding: 8px;">Handmade rag paper vs machine paper</td>
      <td style="padding: 8px;">1791 French decree on laid rag paper with chain lines.</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Ink &amp; Medium</strong></td>
      <td style="padding: 8px;">Iron gall ink, printing ink, or ballpoint</td>
      <td style="padding: 8px;">Maud Lewis writing in blue commercial ballpoint ink.</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Seals &amp; Stamps</strong></td>
      <td style="padding: 8px;">Wax seals, ink revenue stamps, ribbons</td>
      <td style="padding: 8px;">Red wax signet seals on the 1752 treaty parchment.</td>
    </tr>
  </tbody>
</table>

Noticing these details bridges digital screens and historical reality.

**Takeaway:** Describing paper, ink, and wax seals connects digital readers to the physical craftsmanship of historical documents.

---

## **11 Content**

**Documenting Provenance and Archival Custody**

How did this piece of paper survive from the past into our hands today? That story is its **provenance**.

Documenting provenance prevents forgeries and explains why texts survived:
<ul>
  <li><strong>Institutional Custody:</strong> Treaties and decrees were kept in official colonial council chests or government record offices.</li>
  <li><strong>Private Custody:</strong> Personal letters were kept in desk drawers, passed down through families, and later sold at estate auctions.</li>
</ul>

In TEI XML, record this history inside `<history>` and `<provenance>`:
<pre><code>&lt;history&gt;
  &lt;provenance&gt;
    Purchased by Leonard Kinnear in 1967; preserved in the Kinnear family collection;
    sold at Heffel Fine Art Auction in 2022.
  &lt;/provenance&gt;
&lt;/history&gt;</code></pre>

Tracing custody shows that your document is authentic.

**Takeaway:** Provenance documents how a manuscript traveled from its historical creator to modern archives and collections.

---

## **12 Content**

**The TEI Editorial Declaration: `<editorialDecl>`**

The most important part of your technical introduction is the **Editorial Declaration** (`<editorialDecl>`).

The `<editorialDecl>` lives inside `<encodingDesc>`. It is the formal contract between you and your reader. It states your exact editorial policies:
<ul>
  <li>Did you silently fix spelling mistakes, or did you preserve them?</li>
  <li>Did you expand abbreviations?</li>
  <li>How did you divide sentences?</li>
  <li>What secondary dictionaries did you consult?</li>
</ul>

If an editor changes a historical text without explaining their rules, readers cannot trust the edition. The `<editorialDecl>` makes every rule explicit.

**Takeaway:** The editorialDecl element declares your explicit rules for transcription, correction, and normalization, ensuring scholarly trust.

---

## **13 Content**

**The `<correction>` Element: Handling Errors and Emendations**

Every historical document contains scribal slips, printer errors, or ink blots. The `<correction>` element explains how you handled them:
<pre><code>&lt;editorialDecl&gt;
  &lt;correction status="high" method="markup"&gt;
    &lt;p&gt;Apparent scribal slips are preserved in the text using &lt;orig&gt; tags.
    Editorial corrections are supplied in &lt;reg&gt; or &lt;corr&gt; without altering
    the diplomatic baseline.&lt;/p&gt;
  &lt;/correction&gt;
&lt;/editorialDecl&gt;</code></pre>

Attributes explain your approach:
<ul>
  <li><code>status="high"</code> means you checked corrections carefully against the image.</li>
  <li><code>method="markup"</code> means you used TEI tags (like <code>&lt;choice&gt;</code>) rather than silently rewriting words.</li>
</ul>

This transparency protects historical evidence.

**Takeaway:** The correction element explains how scribal slips and typographical errors were identified, preserved, or corrected.

---

## **14 Content**

**The `<normalization>` Element: Articulating Regularization Rules**

In Module 6, you studied normalization. You learned how to regularize historical spelling variations using `<choice>`, `<orig>`, and `<reg>`.

Inside `<normalization>`, summarize the rules from your `NORMALIZATION.md` ledger:
<pre><code>&lt;normalization method="markup"&gt;
  &lt;p&gt;Historical spelling forms are retained in &lt;orig&gt; and regularized
  to modern orthography in &lt;reg&gt;. In the 1791 French decree, eighteenth-century
  imperfect verb endings in -oit are regularized to modern -ait.&lt;/p&gt;
&lt;/normalization&gt;</code></pre>

Stating these rules clearly helps readers understand your search features.

**Takeaway:** The normalization element documents regularized spelling patterns, such as updating eighteenth-century verb endings.

---

## **15 Content**

**The `<quotation>` and `<hyphenation>` Elements**

Punctuation and line breaks present special editorial problems in historical texts:
<ul>
  <li><strong>Quotation Marks:</strong> 18th-century scribes often used margin marks or indentation instead of modern quotation marks.</li>
  <li><strong>End-of-Line Hyphens:</strong> When a word splits across two lines, did you keep the hyphen or join the word?</li>
</ul>

Explain your policy using standard TEI elements:
<pre><code>&lt;quotation marks="none"&gt;
  &lt;p&gt;Direct speech is not enclosed in modern quotation marks unless present
  in the primary ink.&lt;/p&gt;
&lt;/quotation&gt;
&lt;hyphenation eol="all"&gt;
  &lt;p&gt;End-of-line hyphens are preserved as written on the page using milestone
  &lt;lb break="no"/&gt; elements.&lt;/p&gt;
&lt;/hyphenation&gt;</code></pre>

These declarations ensure your text can be searched and displayed accurately.

**Takeaway:** Declare quotation and hyphenation rules so readers understand how line breaks and spoken dialogue are handled.

---

## **16 Content**

**The `<interpretation>` Element: Defining Annotation Scope**

In Module 12, you wrote commentary notes. In your editorial declaration, use `<interpretation>` to define the scope of your notes:
<pre><code>&lt;interpretation&gt;
  &lt;p&gt;Scholarly commentary notes are organized into three distinct categories:
  philological (explaining archaic words), historical (documenting institutions
  and events), and intertextual (tracing legal text reuse). All notes are stored
  in stand-off markup within &lt;standOff&gt;.&lt;/p&gt;
&lt;/interpretation&gt;</code></pre>

This tells readers what kinds of notes to expect and where they are stored in the XML document.

**Takeaway:** The interpretation element explains the categories, purpose, and standoff architecture of your commentary notes.

---

## **17 Content**

**Stating Linguistic Policies: Lemmas, Glosses, and Dictionaries**

In Module 8 and Module 11, you parsed grammar and aligned translations. In your introduction, document the reference dictionaries you consulted:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px; text-align: left; width: 30%;">Document</th>
      <th style="padding: 8px; text-align: left; width: 35%;">Linguistic Focus</th>
      <th style="padding: 8px; text-align: left; width: 35%;">Authoritative Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>1791 French Decree</strong></td>
      <td style="padding: 8px;">Revolutionary legal French</td>
      <td style="padding: 8px;"><em>Dictionnaire de l'Académie française</em> (5th ed., 1798).</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>1752 Peace Treaty</strong></td>
      <td style="padding: 8px;">Colonial British treaty English</td>
      <td style="padding: 8px;">Oxford English Dictionary historical quotations.</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>1967 Maud Lewis Letter</strong></td>
      <td style="padding: 8px;">Maritime folk phonetic dialect</td>
      <td style="padding: 8px;">Dictionary of Canadianisms on Historical Principles.</td>
    </tr>
  </tbody>
</table>

Naming your reference sources proves that your linguistic tags reflect sound scholarship.

**Takeaway:** Citing authoritative historical dictionaries in your introduction validates your linguistic lemmas and grammatical glosses.

---

## **18 Content**

**Stating Named Entity and Authority Control Policies**

In Module 9, you tagged historical people, places, and organizations. Your introduction should explain your authority control policy:
<ul>
  <li>Which authority registries did you consult (Wikidata, VIAF, Canadian Biography)?</li>
  <li>How did you handle people who do not appear in official databases?</li>
  <li>How did you handle historical places whose names have changed?</li>
</ul>

Explain that unlisted historical people (like local Digby neighbors) are described through careful archive notes, while prominent figures link to persistent Wikidata QIDs.

**Takeaway:** Document your authority control strategy, explaining how historical entities are linked to Wikidata, VIAF, or local archive records.

---

## **19 Content**

**Stating Commentary Policies: Documenting AI Assistance and HITL Vetting**

In Module 12, you used AI assistants to draft commentary notes under strict Human-in-the-Loop (HITL) supervision.

Your introduction must state this computational method openly:
<p style="background-color: #f8fafc; border-left: 4px solid #64748b; padding: 12px; margin: 12px 0;">
<em>"Initial commentary drafts were generated using large language models. All factual claims, treaty clauses, and historical citations were audited against primary archival witnesses by the human editor. Fabricated references were rejected. Final editorial authority rests exclusively with the human editor, recorded via @resp attributes."</em>
</p>

Honest disclosure is the gold standard of modern digital scholarship.

**Takeaway:** The introduction must explicitly disclose AI assistance, describing the verification protocols used to ensure historical accuracy.

---

## **20 Content**

**The Editorial Method Statement: Ethical Transparency**

Putting all these policies together produces your **Editorial Method Statement**.

This statement appears as a prominent section in your introduction. It explains:
<ol>
  <li>The scope of the project and why this document was chosen.</li>
  <li>The principles governing transcription and character representation.</li>
  <li>The criteria used to annotate people, places, and legal terms.</li>
  <li>The tools used for digital encoding and verification.</li>
</ol>

Writing this statement gives you an opportunity to reflect on your journey as a digital humanist.

**Takeaway:** The Editorial Method Statement synthesizes your transcription, normalization, annotation, and verification principles into a clear public manifesto.

---

## **21 Content**

**Licensing and Copyright in `<publicationStmt>`**

Who owns your digital edition? Can other scholars reuse your XML code?

You must answer these questions inside `<publicationStmt>`:
<pre><code>&lt;publicationStmt&gt;
  &lt;publisher&gt;St. Francis Xavier University&lt;/publisher&gt;
  &lt;pubPlace&gt;Antigonish, Nova Scotia&lt;/pubPlace&gt;
  &lt;date when="2026-12"&gt;December 2026&lt;/date&gt;
  &lt;availability status="free"&gt;
    &lt;licence target="https://creativecommons.org/licenses/by/4.0/"&gt;
      Distributed under a Creative Commons Attribution 4.0 International License (CC BY 4.0).
    &lt;/licence&gt;
  &lt;/availability&gt;
&lt;/publicationStmt&gt;</code></pre>

Without a license, your work exists in legal limbo. With a Creative Commons license, scholars around the world can study and build upon your research.

**Takeaway:** Declare publisher, publication date, and open access licensing in publicationStmt to make your edition legally reusable.

---

## **22 Content**

**Choosing an Open Access License: Creative Commons (CC BY / CC0)**

In digital humanities, we practice **multi-tiered licensing**:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px; text-align: left; width: 25%;">Project Asset</th>
      <th style="padding: 8px; text-align: left; width: 35%;">Recommended License</th>
      <th style="padding: 8px; text-align: left; width: 40%;">What It Allows</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Editorial Text &amp; Notes</strong></td>
      <td style="padding: 8px;"><strong>CC BY 4.0</strong> (Attribution)</td>
      <td style="padding: 8px;">Free sharing and adaptation, provided you receive author credit.</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Metadata &amp; XML Schemas</strong></td>
      <td style="padding: 8px;"><strong>CC0 1.0</strong> (Public Domain)</td>
      <td style="padding: 8px;">Unrestricted global sharing for library discovery catalogs.</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Python / Shell Scripts</strong></td>
      <td style="padding: 8px;"><strong>MIT License</strong></td>
      <td style="padding: 8px;">Free software reuse and modification by other programmers.</td>
    </tr>
  </tbody>
</table>

Applying the right license to each layer ensures maximum accessibility and fair scholarly credit.

**Takeaway:** Use CC BY for editorial prose, CC0 for catalogue metadata, and MIT for scripts to enable open scholarship.

---

## **23 Content**

**Organizing the Capstone Project Repository in VS Code**

Before assembling your master files, organize your project workspace into a clean folder structure:
<pre><code>my_edition_portfolio/
├── README.md               # Public introduction and project overview
├── LICENSE.md              # Open access licensing terms
├── index.html              # Interactive web edition player
├── edition.pdf             # Formatted print-ready PDF volume
└── xml/
    ├── edition_master.xml  # Complete canonical TEI XML document
    └── schema/             # TEI Relax NG schema file</code></pre>

A tidy project folder makes compiling and testing smooth. It also allows external scholars to explore your code easily on GitHub.

**Takeaway:** Organize your project into clear folders for XML sources, web players, PDF deliverables, and license documentation.

---

## **24 Content**

**Master File Structure: Combining Header, Text, and Standoff**

Your final `edition_master.xml` file brings all your semester work into one elegant document:
<pre><code>&lt;TEI xmlns="http://www.tei-c.org/ns/1.0"&gt;
  &lt;teiHeader&gt;
    &lt;fileDesc&gt; ... &lt;/fileDesc&gt;
    &lt;encodingDesc&gt;
      &lt;editorialDecl&gt; ... &lt;/editorialDecl&gt;
    &lt;/encodingDesc&gt;
  &lt;/teiHeader&gt;
  &lt;facsimile&gt; ... &lt;/facsimile&gt;
  &lt;text&gt;
    &lt;body&gt; ... &lt;/body&gt;
  &lt;/text&gt;
  &lt;standOff&gt;
    &lt;interpGrp type="commentary"&gt; ... &lt;/interpGrp&gt;
  &lt;/standOff&gt;
&lt;/TEI&gt;</code></pre>

Every element has its proper place. The `<teiHeader>` describes the edition, `<text>` holds the primary words, and `<standOff>` holds your research commentary.

**Takeaway:** The canonical TEI master document combines teiHeader, facsimile, text body, and standOff commentary in a single XML file.

---

## **25 Content**

**Validating the Master TEI File Against Schema**

Before publishing any digital edition, you must test its syntax. A broken XML tag can crash web players or break PDF layout pipelines.

In VS Code, run your validation sweep:
<ol>
  <li><strong>Check Well-Formedness:</strong> Confirm all opening tags have matching closing tags.</li>
  <li><strong>Verify XML Identifiers:</strong> Confirm that every <code>xml:id</code> is unique and that every <code>@target</code> pointer begins with a hash mark (<code>#</code>).</li>
  <li><strong>Validate Against Schema:</strong> Check your file against the official TEI Relax NG schema in VS Code.</li>
</ol>

A green checkmark in VS Code confirms that your document complies with international digital humanities standards.

**Takeaway:** Run schema validation in VS Code to ensure well-formed tags, unique identifiers, and valid pointer references.

---

## **26 Content**

**Writing a Project README.md for External Scholars**

When visitors view your GitHub repository, the first file they see is `README.md`.

Your `README.md` acts as your project's digital front door:
<ul>
  <li><strong>Project Title:</strong> State the document title and your name.</li>
  <li><strong>Project Summary:</strong> Two paragraphs explaining what the document is and why it matters.</li>
  <li><strong>Quick Start:</strong> Instructions on how to view the interactive web edition or download the PDF.</li>
  <li><strong>Editorial Summary:</strong> A concise summary of your transcription and commentary policies.</li>
  <li><strong>Citation:</strong> How other scholars should cite your digital edition in their research.</li>
</ul>

A clear README invites the world to explore your scholarship.

**Takeaway:** The project README.md welcomes visitors, summarizes document history, provides quick viewing links, and provides citation formats.

---

## **27 Content**

**Peer Reviewing the Editorial Introduction**

Scholarly publishing relies on **peer review**. Before submitting your capstone edition, exchange introductions with a classmate.

When reviewing a classmate's introduction, ask:
<ul>
  <li>Does the introduction clearly explain who wrote the document and where it is kept?</li>
  <li>Are the physical dimensions and materials described accurately?</li>
  <li>Does the editorial declaration clearly explain how spelling variations were handled?</li>
  <li>Is the prose clear, engaging, and free of modern clichés?</li>
</ul>

Constructive peer feedback helps you catch missing details before final evaluation.

**Takeaway:** Peer review helps editors identify missing archival details and clarify editorial principles before final publication.

---

## **28 Content**

**Common Flaws in Student Editorial Introductions**

When reviewing your introduction, watch out for these frequent beginner mistakes:
<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 8px; text-align: left; width: 30%;">Common Flaw</th>
      <th style="padding: 8px; text-align: left; width: 70%;">Editorial Correction</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Missing Shelfmark</strong></td>
      <td style="padding: 8px;">Always state the exact archival repository name and call number.</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Vague Normalization Rules</strong></td>
      <td style="padding: 8px;">Do not just say "spelling was modernized"; give specific examples of updated verb endings or letters.</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 8px;"><strong>Unattributed AI Drafts</strong></td>
      <td style="padding: 8px;">Always disclose AI drafting tools and describe human verification steps.</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Broken XML Targets</strong></td>
      <td style="padding: 8px;">Check that every <code>@target</code> points to a real <code>xml:id</code> anchor in your text.</td>
    </tr>
  </tbody>
</table>

Eliminating these flaws ensures your edition achieves professional quality.

**Takeaway:** Avoid common beginner errors by providing specific shelfmarks, concrete normalization examples, and verified XML pointers.

---

## **29 Content**

**Checklists for Editorial Completeness**

Before moving to visual styling in tomorrow's lesson, verify your editorial completeness:
<ul>
  <li>[ ] Is the historical narrative preface written and saved in <code>README.md</code>?</li>
  <li>[ ] Is the <code>&lt;msDesc&gt;</code> complete with repository, support, and physical dimensions?</li>
  <li>[ ] Does the <code>&lt;editorialDecl&gt;</code> contain explicit <code>&lt;correction&gt;</code> and <code>&lt;normalization&gt;</code> tags?</li>
  <li>[ ] Are reference dictionaries and authority files explicitly named?</li>
  <li>[ ] Is the open access license declared in <code>&lt;publicationStmt&gt;</code> and <code>LICENSE.md</code>?</li>
  <li>[ ] Does the entire XML document validate with zero errors in VS Code?</li>
</ul>

Checking off each item prepares your text for presentation styling.

**Takeaway:** Use an editorial checklist to confirm that all historical, material, and policy declarations are complete and valid.

---

## **30 Content**

**Synthesis: Preparing for Presentation Styling in Lesson 13.2**

Congratulations! Today you established the intellectual foundation of your capstone edition:
<ol>
  <li>You contextualized your primary witness within its unique historical, political, and material setting.</li>
  <li>You formulated clear editorial principles in a machine-actionable TEI <code>&lt;editorialDecl&gt;</code>.</li>
  <li>You selected open access licenses to make your research accessible and reusable.</li>
</ol>

Tomorrow, in **Lesson 13.2**, we will shift from editorial principles to visual presentation. You will explore the **TEI Processing Model**, learning how to map semantic XML elements to beautiful web layouts and typography using CSS stylesheets.

Open VS Code, review your editorial declaration, and get ready to bring your edition to life on screen!

**Takeaway:** Having formulated editorial principles in Lesson 13.1, you are ready to style your edition for the web in Lesson 13.2.
