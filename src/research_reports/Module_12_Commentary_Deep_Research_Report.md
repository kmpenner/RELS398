# Topic 12 (Topic_12_Commentary): Academic Deep Research Report

**Model:** 3.1 Pro (Deep Research)  
**Attachments:** 8 PDF(s)  
**Citations resolved:** 36

## Digital Scholarly Commentary and AI

ContentsShare & Export
Create

# From Marginalia to Knowledge Graphs: The Architecture and Epistemology of Digital Scholarly Commentary

## Abstract and Executive Summary

The transition of the scholarly edition from the printed codex to the digital medium represents an epistemological rupture in textual scholarship, shifting the critical commentary from a subordinate paratext into a dynamic, relational knowledge graph. Traditionally, the scholarly edition has been conceived as a hierarchical structure where the base text is buffered by apparatuses and static footnotes designed to clarify philological, historical, and intertextual contexts. The digital paradigm, propelled by the Text Encoding Initiative (TEI) and the W3C Web Annotation Data Model, dissolves this strict hierarchy. By structuring scholarly commentary as linked open annotations and machine-readable cross-references, the modern digital edition transforms isolated hermeneutic observations into an extensible network of linked open data.

This exhaustive analysis evaluates the technical, methodological, and historical foundations of digital commentary. It examines how analytic mechanisms within the TEI framework—specifically stand-off markup, pointer elements, and interpretation groups—resolve the limitations of embedded XML hierarchies, often referred to as the overlapping hierarchies problem. Furthermore, it explores the W3C Web Annotation Data Model’s capacity to ensure robust, interoperable linking across distributed platforms utilizing JSON-LD architectures. The analysis juxtaposes manual scholarly annotation with automated intertextual discovery algorithms, most notably the Tesserae project, which relies on lemma identity and frequency-weighted scoring to uncover textual reuse.

A central thesis of this report is that while Artificial Intelligence (AI) and Large Language Models (LLMs) offer unprecedented capabilities for generating commentary, extracting entities, and mapping intertextual networks across massive corpora, they simultaneously introduce profound hazards. AI-drafted commentary must be strictly vetted for hallucinated citations, anachronistic interpretations, and missing contextual nuances. Unchecked algorithmic assistance risks fostering "automation bias," whereby the user’s critical agency is diminished. Through the evaluation of real-world digital edition case studies—including Dickinson College Commentaries, the Pelagios Network’s Recogito, Net7’s Pundit, and DanteSources—this report synthesizes a pedagogical and architectural framework for digital editors. It asserts that the future of textual scholarship relies on Human-in-the-Loop (HITL) workflows that leverage the scale of computational philology while preserving the rigorous interpretive nuance of the traditional editor.

## Technical, Methodological, and Historical Foundations

### The Epistemology of the Critical Commentary

The act of annotating texts is a foundational practice of philology, tracing its origins to the Alexandrian grammarians who utilized critical signs, such as the asterisk and the *diplê*, to mark textual corruption and interpretive exegesis in Homeric manuscripts. The margins of medieval manuscripts, such as the Venetus A manuscript of the *Iliad*, preserve a rich stratification of scholia and glosses, effectively functioning as early collaborative interfaces where multiple annotators across centuries engaged in distributed, asynchronous dialogue with the base text[1]. Within the print paradigm, this practice crystallized into the traditional critical apparatus and the footnote—paratexts that exist in a strictly subordinate, hermeneutic relationship to the established text[2].

However, the static nature of the printed page isolates these annotations. In print, a commentary on Ovidian intertextuality in Lucan remains confined to a single volume, unable to programmatically link to external datasets or interact dynamically with other scholarly observations[3]. The digital medium redefines the scholarly edition not merely as a digitized book, but as a "knowledge site" or programmable corpus[4]. In this environment, the commentary is no longer an isolated footnote; it becomes a node within a broader relational interplay of discourses, capable of mapping transmission histories, tracing lexical semantic change, and connecting entities to global authority files[2].

### TEI Analytic Mechanisms and the Overlap Problem

The Text Encoding Initiative (TEI) P5 Guidelines provide the *de facto* standard for producing machine-readable cultural heritage texts. Early digital humanities projects relied heavily on embedded XML markup, following the Ordered Hierarchy of Content Objects (OHCO) model. However, textual scholars quickly encountered the structural limitations of this paradigm. Cultural heritage documents inherently contain non-linear textual phenomena, such as revisions, transpositions, and multiple overlapping hierarchies—for instance, a text might be simultaneously segmented by its metrical structure (stanzas and lines) and its physical structure (pages and columns)[5]. Desmond Schmidt has extensively critiqued the inadequacy of embedded markup for historical texts, noting that embedding interpretive codes into the primary text stream obscures the original content, complicates maintenance, and forces editors to prioritize one hierarchy over another, leading to highly fragmented, subjective, and fragile data structures[5].

To resolve these overlapping hierarchies and decouple interpretive commentary from the base text, the TEI framework utilizes analytic mechanisms and stand-off markup. The `standOff` element functions as a dedicated container for linked data, contextual information, and annotations that do not strictly belong in the transcription of the source or the header metadata[6]. By utilizing the global `xml:id` attribute, editors can assign unique identifiers to segments of the text using the `seg` or `span` elements[7]. Interpretations are then housed externally in an `interpGrp` (interpretation group) containing individual `interp` elements, which connect to the base text using pointer elements like `ptr` and `link` via the `target` attribute[6].

This stand-off architecture transforms the digital edition from a flat, monohierarchical tree into an interconnected graph[8]. It ensures that the base text remains pristine and structurally intact while accommodating an infinite number of editorial layers. An editor can supply a philological commentary, a historical contextualization, and a morphosyntactic analysis, all residing in separate stand-off containers that reference the same underlying character nodes[9]. As digital editing paradigms shift toward semantic webs, this structural separation allows TEI XML to output seamlessly to Resource Description Framework (RDF) triples[10].

### The W3C Web Annotation Data Model

While TEI stand-off markup elegantly handles internal document architecture, the integration of digital editions into the broader Semantic Web requires an interoperable, cross-platform standard. The W3C Web Annotation Data Model (WADM), formalized as a W3C Recommendation in 2017 and serialized natively in JSON-LD, fulfills this requirement by establishing a robust ontology for expressing annotations across the web[11]. The core paradigm of the WADM rests on three primary components: the Annotation, the Body (the commentary or resource being added), and the Target (the resource being annotated)[12].

A critical feature of the WADM is the `motivation` property, which explicitly declares the intent behind the annotation. Standardized motivations include `bookmarking`, `classifying`, `commenting`, `editing`, `highlighting`, `identifying`, and `linking`[13]. By defining the scholarly intent, the WADM ensures that applications consuming the data can programmatically differentiate between a philological emendation, a geographic identification, and an interpretive scholarly note.

The challenge of annotating digital texts lies in the fragility of anchors; if the base text is modified, traditional byte-offset anchors or structural XPath selectors immediately break[14]. The WADM mitigates this through complex selector chains. The `TextPositionSelector` records the start and end Unicode code-points of the target, while the `TextQuoteSelector` stores the exact string of the passage alongside a prefix and suffix for contextual disambiguation[15]. If a document undergoes minor revisions, the annotation client can fall back on the `TextQuoteSelector` to fuzzy-match the string within the prefix and suffix context, thereby ensuring the resilient persistence of the scholarly commentary[14].

| Anchor Mechanism | Description | Resilience to Content Modification | Resilience to Structural Reordering |
| --- | --- | --- | --- |
| **Byte Offset** | Character position integer. | None. Breaks on any upstream edit. | None. |
| **Structural (XPath)** | Document Object Model (DOM) path. | Moderate. Survives text edits if DOM is untouched. | None. Breaks if elements are moved. |
| **Content Hash** | Cryptographic hash of the text block. | None. Breaks on any character change within the block. | High. Independent of position. |
| **TextQuoteSelector** | Exact string + prefix/suffix context. | High. Allows fuzzy matching for minor rewrites. | High. Finds string anywhere in document. |

### The Tesserae Intertextual Discovery Algorithm

Scholarly commentary heavily relies on the identification of intertextuality—the ways in which authors integrate, allude to, or subvert prior texts. Traditionally, discovering these allusions required immense erudition and mnemonic recall, often focusing disproportionately on canonical source texts. The Tesserae project revolutionized this process by providing an automated, algorithmic approach to intertextual discovery across classical Latin and Greek poetry[16].

The foundational Tesserae algorithm utilizes n-gram matching to identify phrases in a target text that share two or more lemmas with a source text. To filter out semantically empty connections—such as common function words, prepositions, or highly frequent vocabulary—the algorithm employs a specialized scoring system. This formula calculates a score based on word frequency (utilizing Term Frequency-Inverse Document Frequency, or TF-IDF, principles) and phrase density (the proximity of the matching words to one another within the passage)[17].

The underlying mathematical intuition is that rare words placed in close syntactic proximity carry a significantly higher probability of intentional authorial allusion than common words spread far apart. If N represents the corpus size and DF represents the document frequency of a lemma, the rarity is captured logarithmically. The Tesserae score dynamically ranks discovered parallels, allowing scholars to adjust both precision and recall. While earlier versions of the algorithm behaved akin to "strip mining"—returning thousands of false positives due to polysemy and morphological ambiguity—the frequency-weighted scoring mechanism successfully models the intuition of the literary scholar, elevating interpretively significant parallels to the top of the results[17]. Further advancements in computational linguistics have begun augmenting this deterministic approach with Word Mover's Distance (WMD) and neural embeddings to capture semantic, rather than merely lexical, text reuse[18].

## Comparative Methodological Evaluation

The generation of scholarly commentary in the digital age now exists on a spectrum ranging from entirely manual human curation to fully automated algorithmic extraction, and increasingly, to Large Language Model (LLM) generation. Each methodology possesses distinct capabilities, epistemic values, and operational hazards.

### Manual Scholarly Note Drafting

Manual scholarly note drafting remains the gold standard for philological nuance and interpretive depth. The traditional editor brings an understanding of historical context, literary theory, and cultural resonance that cannot be easily quantified. In the Danish Digital Scholarly Edition of *Grundtvig's Works*, manual annotation constitutes an interpretive practice deeply rooted in hermeneutic reflection[4]. Grundtvig’s complex, archaizing 19th-century Danish required the manual addition of over 158,000 explanatory commentaries, 10,980 biblical references, and 166,430 named entity tags to mediate the historical distance for modern readers[4].

However, manual annotation is profoundly unscalable. Extracting the complete intertextual network of a massive corpus like the *Patrologia Latina* or fully cataloging the reception of Propertius in Ovid's *Heroides* using solely manual labor requires generations of scholarly effort[4]. Furthermore, manual annotation is subject to human mnemonic limitations, often prioritizing canonical source texts while overlooking obscure or non-traditional influences.

### Automated Intertext Matching

Automated intertext matching, such as the aforementioned Tesserae algorithm, solves the scalability problem. By processing entire corpora through vector embeddings, cosine similarity, or frequency-weighted n-gram matching, deterministic algorithms can surface latent textual reuse at a massive scale[19].

Yet, deterministic tools lack semantic comprehension. They excel at identifying lexical borrowing but struggle with implicit allusions, structural parodies, or thematic subversions where the vocabulary differs entirely from the source text. As scholars studying Latin hexameter poetry note, allusions are often signaled by similarity of action, character, or theme, rather than identical lexemes[20]. A purely lexical algorithm might fail to identify the metapoetic significance of the word *arma* ("warfare") at the opening of Ovid's *Amores*, whereas a human interpreter easily recognizes the subversion of Vergil's *Aeneid*[20].

### LLM Commentary Generation and Epistemological Hazards

The advent of Generative AI and LLMs introduces a powerful hybrid capability. LLMs encode vast amounts of semantic data, enabling them to recognize conceptual metaphors, trace diachronic semantic shifts, and generate explanatory commentary that bridges the gap between raw data and human comprehension[4].

In the *Graphilosophy* project, which models the complex Chinese-Vietnamese commentaries of Confucian classics (*The Four Books*), researchers utilized LLMs and multilingual semantic embeddings to resolve polysemy[21]. Classical Chinese presents extreme computational challenges due to phonetic ambiguity and character brevity. Context-sensitive matching via LLM embeddings (e.g., differentiating between 人 as "human" versus 仁 as the virtue of "benevolence") allows the system to support interpretive coherence across layered knowledge graphs[21].

However, LLM-generated commentary introduces severe epistemological hazards to the scholarly edition. The primary danger is the hallucination of citations and missing context. LLMs operate probabilistically, predicting the next plausible token rather than retrieving verified facts. When editors of *Grundtvig's Works* tested ChatGPT-4 for identifying biblical references, the model successfully identified some allusions but simultaneously hallucinated implausible matches, linking a generic mention of "Jesus" to a totally irrelevant biblical verse simply because the name appeared[4]. Furthermore, LLMs frequently impose anachronistic interpretations by mapping modern conceptual frameworks onto historical vocabularies, diluting the specific cultural context of the base text[21].

Perhaps more insidious is the threat to writer and editor agency, often termed "automation bias"[22]. In chat-based AI interfaces, feedback is delivered in continuous conversational threads detached from the physical structure of the document. This disconnection encourages users to accept large-scale, wholesale rewrites without critical engagement, effectively reducing the editor to a passive consumer of algorithmic output. Studies on the *AnchoredAI* system demonstrate that when AI feedback is delivered dynamically via chat, it results in massive, uncritical copy-pasting of text, fundamentally diminishing the user's perceived ownership and authorship[22].

To combat this, digital humanities researchers advocate for structuring AI output strictly as anchored inline commentary. By binding the AI's suggestions to specific, discrete spans of text—an implementation requiring precise Anchoring Context Windows (ACWs) to resolve referential ambiguity—the system imposes a "desirable difficulty" upon the user[22]. The user must actively read the AI's localized note, evaluate its philological merit, and make a conscious decision to accept or reject the intervention. This Human-in-the-Loop (HITL) methodology safeguards the editor's psychological ownership of the text and preserves the rigorous interpretive standards required for a scholarly edition[4].

| Commentary Methodology | Scale & Efficiency | Interpretive Depth | Primary Hazards |
| --- | --- | --- | --- |
| **Manual Drafting** | Very Low | Exceptionally High | Mnemonic limitations, slow production, bias toward canonical texts. |
| **Deterministic Algorithms** | Very High | Low (Lexical focus) | High false positive rate, inability to detect thematic or structural allusions. |
| **LLM Generation** | High | Moderate (Semantic) | Hallucinated citations, anachronisms, automation bias, loss of editorial agency. |

## Real-World Digital Edition Case Studies

The theoretical frameworks of TEI, WADM, and computational philology are best understood through their application in active digital infrastructure projects. The following case studies illustrate how diverse platforms negotiate the complexities of digital commentary and intertextual linking.

### Dickinson College Commentaries (DCC)

The Dickinson College Commentaries (DCC) project exemplifies a pedagogical approach to the digital scholarly edition. Hosted at Dickinson College, the platform publishes peer-reviewed commentaries on classical Latin and ancient Greek texts, shifting the focus from purely text-critical debates to readerly accessibility and student pedagogy[23]. The DCC infrastructure leverages structured text models to present sources alongside custom-authored notes, multimedia annotations, and newly generated geographic maps[23].

A distinguishing feature of the DCC is its algorithmic approach to vocabulary scaffolding. By utilizing frequency data from the Thesaurus Linguae Graecae (TLG) and the Laboratoire d'Analyse Statistique des Langues Anciennes (LASLA), the project identifies "core vocabularies"—the lemmas that generate approximately 75% of the words in a typical classical text[23]. Words falling outside this core list are meticulously parsed and provided in running vocabulary commentaries specific to the text section being read. By algorithmically generating the baseline linguistic data, the scholarly editors are freed to focus their manual annotations on complex grammatical constructions, historical context, and literary analysis. Furthermore, the DCC integrates external authority files, explicitly linking place names in the text to the Pleiades geographic database, thereby turning the commentary into an active node within the broader classical Linked Open Data (LOD) cloud[23].

### The Pelagios Network, Recogito, and Net7 Pundit

The transition from isolated digital editions to an interconnected "Graph of Ancient World Data" is heavily driven by the tools developed by the Pelagios Network and Net7. Recogito, an open-source platform developed by Pelagios, provides a graphical interface for semantic geo-annotation without requiring users to write raw XML or JSON[24]. Scholars can highlight text or image regions and align them with global authority records, particularly the Pleiades gazetteer for ancient places. Recogito natively exports these annotations using the W3C Web Annotation Data Model, generating RDF serializations that allow independent digital editions to share and query geographic data across institutional boundaries[25].

Operating on a similar philosophical foundation, Net7's Pundit is a semantic annotation tool designed specifically to overlay structured data onto web pages and digital libraries[26]. Pundit relies entirely on stand-off markup techniques to extract entities from web content and generate RDF triples. Rather than simply tagging a text with a keyword, Pundit allows scholars to construct semantically typed relations (e.g., "Person A is the author of Work B," or "Passage X quotes Passage Y"). Because Pundit outputs standard Linked Open Data according to the Open Annotation schema, the annotations created by a scholar reading a digital edition can be ingested by third-party applications, facilitating the discovery of new, semantically structured aggregations of knowledge[27].

### DanteSources and the Hypermedia Dante Network

The DanteSources project, developed by the Italian National Research Council (ISTI-CNR) and the University of Pisa, represents a highly sophisticated application of Semantic Web technologies to map literary primary sources[28]. The project addresses a critical gap: while the primary sources of Dante Alighieri’s works (the classical and medieval authors he quotes or alludes to) are well-documented in massive printed commentaries, this knowledge was previously locked in natural language prose, making it impossible to computationally analyze Dante's intellectual background[22].

To resolve this, the researchers developed an RDF/S ontology by integrating existing semantic models, including FRBRoo (for modeling the physical and conceptual expressions of works), the Document Components Ontology (DoCO), and the Citation Typing Ontology (CiTO)[29]. The team implemented a semi-automatic extraction tool to parse thousands of pages of authoritative commentaries, allowing experts to verify and link Dante's textual fragments to DBpedia URIs representing the original authors, works, and thematic areas (e.g., Aristotelianism, Scholasticism)[22].

The resulting digital library allows users to run complex SPARQL queries over the knowledge graph. A scholar can instantly visualize the distribution of explicit versus generic citations of Aristotle’s *Nicomachean Ethics* across the chapters of the *Convivio* or the *Monarchia*[28]. This transformation of narrative commentary into a queryable graph fundamentally alters the research landscape, enabling scholars to perform distant reading and macro-analysis on the evolution of Dante's philosophical influences[22].

### Collaborative AI-Assisted Reading Environment (CARE)

Further bridging the gap between natural reading environments and AI interventions is the Collaborative AI-Assisted Reading Environment (CARE)[30]. CARE addresses the lack of standardized environments for the ethical collection and extrinsic evaluation of inline commentary data. Functioning as a collaborative PDF reader, CARE allows users to leave highlights and text annotations while concurrently routing these actions to an AI broker[30]. This broker integrates with Hugging Face transformer models to supply real-time, in-text assistance, such as text summarization, question answering, or sentiment classification[30]. By embedding behavioral telemetry—tracking scrolling habits, annotation editing, and time-on-page—CARE provides critical telemetry on how AI interventions alter the cognitive burden of deep scholarly reading, offering an empirical framework to test hypotheses surrounding "automation bias"[30].

## Pedagogical Takeaways and Synthesis for Digital Editors

The integration of TEI stand-off markup, W3C Web Annotations, and algorithmic assistance necessitates a rigorous pedagogical framework for digital editors. To harness the capabilities of these systems while mitigating their hazards, editors must adopt structured methodologies for categorizing commentary, establishing persistent links, and managing computational interventions.

### Guidelines for Categorizing and Encoding Commentary

To maximize the interoperability of a digital edition, editors must move beyond undifferentiated `<note>` tags and utilize robust typologies to classify the intent and scope of their commentary. Drawing upon the capabilities of the TEI `interp` element and the W3C `motivation` property, annotations should be systematically categorized into distinct semantic layers.

| Commentary Category | Editorial Function | W3C Motivation | TEI Implementation Example |
| --- | --- | --- | --- |
| **Philological / Text-Critical** | Documents emendations, paleographic uncertainties, scribal errors, and morphological parsing. | `editing`, `commenting` | `<app>`, `<rdg>`, `<note type="philological">` linked to a specific `<w>` (word) ID. |
| **Historical / Contextual** | Identifies named entities (people, places, events) and provides historical background. | `identifying`, `describing` | `<ptr>` to external authority URIs (e.g., Pleiades, VIAF) via `standOff` container. |
| **Intertextual / Bibliographic** | Traces allusions, quotes, and text reuse to external source documents. | `linking` | `<interp>` utilizing CiTO properties (e.g., `citesAsExplicitCitation`) within an `<interpGrp>`. |
| **Structural / Thematic** | Defines the rhetorical or conceptual mapping of a document (e.g., shifts in narrative voice, overarching themes). | `classifying` | Segmenting text with `<div>` or `<seg>` and linking to ontological concept URIs. |

### Implementing Canonical Text Services (CTS) URNs

A fundamental requirement for any digital scholarly commentary is the ability to point reliably to a specific passage of text. Standard URLs are inherently fragile; they point to a specific digital file or web page rather than the abstract intellectual work itself, causing link rot whenever a server structure changes. To solve this, digital editors should implement the Canonical Text Services (CTS) protocol and the CITE Architecture, developed by Christopher Blackwell and Neel Smith[31].

The CTS URN provides a technology-independent, hierarchical identifier that reflects the traditional scholarly method of citation. The syntax of a CTS URN is strictly defined as `urn:cts:namespace:textgroup:work:version:passage`[32]. For example, a URN might specify the Latin literature namespace, the textgroup for Apuleius, the work *Metamorphoses*, a specific critical edition version, and finally the hierarchical passage (Book 1, Chapter 1, Section 1).

By using CTS URNs within the `target` attributes of TEI pointers or W3C Web Annotations, editors guarantee that their commentary remains robust. If a digital library migrates its data from XML to a relational database, or updates its web domain, the CTS URN persists because it identifies the conceptual passage of the text, independent of its physical or digital instantiation[31]. Furthermore, projects like the Digital Athenaeus utilize CTS URNs within their annotation interfaces (e.g., INCEpTION) to disambiguate historical author mentions, effectively allowing the text to serve as its own dynamic bibliography[1].

### Managing the AI-Assisted Editing Workflow

As generative AI becomes an integral component of the editorial toolkit, project directors must institute pedagogical guidelines to ensure algorithmic assistance augments rather than replaces scholarly rigor. Editors must treat LLM outputs as provisional hypotheses requiring validation. When employing models for tasks such as named entity recognition or intertextual alignment, the system architecture must compel the editor to interact with the raw data.

The concept of "desirable difficulty" is paramount here[33]. User interfaces should avoid chat-based paradigms that encourage mass acceptance of text. Instead, AI-generated annotations should be rendered as discrete, anchored stand-off suggestions. As observed in the *Graphilosophy* and *AnchoredAI* prototypes, the editor must be required to manually review the Anchor Context Window (ACW), verify the proposed external URI, check the AI’s reasoning for hallucinations, and explicitly authorize the inclusion of the data into the edition's definitive knowledge graph[21]. By enforcing this friction, the digital edition retains its authoritative epistemological status while benefiting from the rapid processing capabilities of computational models.

### Minimal Computing and Sustainability

Finally, editors must consider the technological sustainability of their digital infrastructure. The ethos of "minimal computing" advocates for the implementation of digital projects using the least amount of technology necessary to achieve the scholarly goal[34]. While complex Content Management Systems (CMS) like Drupal can be heavily customized to support rich digital editions, they require constant maintenance, database updates, and server infrastructure, rendering them highly vulnerable to obsolescence[34]. Instead, pedagogies of textual scholarship are increasingly emphasizing the use of open technologies, static site generators, and clean TEI-compliant XML paired with simple CSS front-ends. This approach ensures that the primary data—the text and its stand-off commentary—remains decoupled from the presentation layer, guaranteeing the long-term survival and ownership of the scholarly knowledge graph[34].

## Comprehensive Academic & Technical References

The following references provide the essential bibliographic and technical frameworks synthesized throughout this report:

- **Bartalesi, V., et al. (2018).** "A Web Application for Exploring Primary Sources: The DanteSources Case Study." This research outlines the development of the DanteSources ontology utilizing FRBRoo, DoCO, and CiTO to map primary textual citations to Dante’s works via RDF/S.[22].
- **Blackwell, C. W., & Smith, N. (2014).** "The Canonical Text Services URN specification, version 2.0.rc.1." Center for Hellenic Studies. Defines the syntax and semantics of the CTS URN protocol for persistent, technology-independent identification of text passages.[32].
- **Coffee, N., et al. (2012).** "The Tesserae Project: intertextual analysis of Latin poetry." *Literary and Linguistic Computing*, 28(2): 221-228. This foundational paper details the algorithmic scoring mechanism (TF-IDF and phrase density) used to detect intertextual parallels across classical corpora.[17].
- **Draxler, F., et al. (2024).** "The AI ghostwriter effect: When users do not perceive ownership of AI-generated text but self-declare as authors." *ACM Transactions on Computer-Human Interaction*, 31(2). Discusses the psychological impacts of generative AI on writer agency and ownership.[22].
- **Klie, J.-C., et al. (2018).** "The INCEpTION Platform: Machine-Assisted and Knowledge-Oriented Interactive Annotation." *Proceedings of the 27th International Conference on Computational Linguistics*, 5-9. Details the open-source platform utilized for semantic annotation and concept linking in digital humanities texts.[35].
- **Lou, M., et al. (2025).** "AnchoredAI: Contextual Anchoring of AI Comments Improves Writer Agency and Ownership." Details the technical implementation of Anchoring Context Windows (ACWs) to prevent automation bias in LLM-assisted editing.[22].
- **Sanderson, R., Ciccarese, P., & Young, B. (2017).** "Web Annotation Data Model." W3C Recommendation. World Wide Web Consortium. Establishes the JSON-LD specification for `TextQuoteSelector`, `TextPositionSelector`, and `motivation` attributes in web annotations.[14].
- **Schmidt, D. (2010).** "The Inadequacy of Embedded Markup for Cultural Heritage Texts." *Literary and Linguistic Computing*, 25(3): 337-356. Critiques the OHCO model and argues for stand-off markup to resolve overlapping hierarchies in TEI XML.[5].
- **Simon, R., et al. (2017).** "Linked Data Annotation Without the Pointy Brackets: Introducing Recogito 2." Pelagios Network. Describes the user-interface and data models behind Recogito’s alignment of textual entities with the Pleiades gazetteer.[36].
- **Tafdrup, J., et al. (2026).** "Convergences. AI, editorial practice, and the Danish Digital Scholarly Edition of Grundtvig's Works." *International Journal of Digital Humanities*, 8: 191-211. Explores Human-in-the-Loop workflows for applying LLMs to historical text annotation and named entity recognition.[4].

Sources used in the report

04_Observations_on_annotations.pdf

[researchgate.net

(PDF) Theorizing the Digital Scholarly Edition - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/227774739_Theorizing_the_Digital_Scholarly_Edition)[dokumen.pub

Repeat Performances: Ovidian Repetition and the Metamorphoses 0299307506, 9780299307509 - DOKUMEN.PUB

 Opens in a new window](https://dokumen.pub/repeat-performances-ovidian-repetition-and-the-metamorphoses-0299307506-9780299307509.html)

01_Annotations_as_semantic_traces_a_multi-level_ontology_for_digital_hermeneutics.pdf

[dracor-org.github.io

DraCor ODD - GitHub Pages

 Opens in a new window](https://dracor-org.github.io/dracor-schema/)

02_Convergences._AI,_editorial_practice,_and_the_Danish_Digital_Scholarly_Edition_o.pdf

[scholarworks.iu.edu

Rethinking Scholarly Commentary in the Age of Google - IU ScholarWorks

 Opens in a new window](https://scholarworks.iu.edu/journals/index.php/textual/article/download/27152/32670/65949)[scispace.com

The inadequacy of embedded markup for cultural heritage texts - SciSpace

 Opens in a new window](https://scispace.com/pdf/the-inadequacy-of-embedded-markup-for-cultural-heritage-4h5dbdkdaa.pdf)[researchgate.net

Overlapproaches in documents: A definitive classification (in OWL, 2!) - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/265972479_Overlapproaches_in_documents_A_definitive_classification_in_OWL_2)[balisage.net

Balisage Paper: Overlapproaches in documents: a definitive classification (in OWL, 2!)

 Opens in a new window](https://www.balisage.net/Proceedings/vol13/html/Peroni01/BalisageVol13-Peroni01.html)[d-nb.info

www.ssoar.info The role of markup in the digital humanities

 Opens in a new window](https://d-nb.info/1186853379/34)[researchgate.net

Merging Multi-Version Texts: a Generic Solution to the Overlap Problem - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/269091340_Merging_Multi-Version_Texts_a_Generic_Solution_to_the_Overlap_Problem)[tei-c.org

17 Linking, Segmentation, and Alignment - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/SA.html)[tei-c.org

TEI element standOff - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-standOff.html)[tei-c.org

TEI element seg (arbitrary segment) - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-seg.html)[tei-c.org

TEI element span - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-span.html)[tei-c.org

TEI element note (note) - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-note.html)[ceur-ws.org

Modeling the 'Unthought' - CEUR-WS.org

 Opens in a new window](https://ceur-ws.org/Vol-3110/paper8.pdf)[kups.ub.uni-koeln.de

Graph Data-Models and Semantic Web Technologies in Scholarly Digital Editing

 Opens in a new window](https://kups.ub.uni-koeln.de/54577/1/side15.pdf)[journals.openedition.org

Applied Text as Graph (ATAG) in an Algorithmic Edition - OpenEdition Journals

 Opens in a new window](https://journals.openedition.org/jtei/6027)[balisage.net

Balisage Paper: Encoding semantic relationships in literary texts

 Opens in a new window](https://www.balisage.net/Proceedings/vol26/html/Koidaki01/BalisageVol26-Koidaki01.html)[researchgate.net

Opening the book: data models and distractions in digital scholarly editing - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/333148326_Opening_the_book_data_models_and_distractions_in_digital_scholarly_editing)[ec.europa.eu

Deliverable - European Commission

 Opens in a new window](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5b4d197e5&appId=PPGMS)[github.com

margin/COMMENT_PROTOCOL.md at main - GitHub

 Opens in a new window](https://github.com/openprose/margin/blob/main/COMMENT_PROTOCOL.md)[wal.sh

Annotation Systems for Evolving Documents - wal.sh

 Opens in a new window](https://wal.sh/research/annotation-systems/)[w3.org

Data on the Web Best Practices - W3C

 Opens in a new window](https://www.w3.org/TR/dwbp/)[github.com

readium/annotations: Model and JSON serialization of annotations associated with EPUB and Web Publications - GitHub

 Opens in a new window](https://github.com/readium/annotations)[journal.code4lib.org

Annotation-based enrichment of Digital Objects using open-source frameworks

 Opens in a new window](https://journal.code4lib.org/articles/12582)[tei-c.org

TEI element annotation - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-annotation.html)[researchgate.net

Towards a Historical Text Re-use Detection | Request PDF - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/268445909_Towards_a_Historical_Text_Re-use_Detection)[researchgate.net

Modeling the scholars: Detecting intertextuality through enhanced word-level n-gram matching | Request PDF - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/274151306_Modeling_the_scholars_Detecting_intertextuality_through_enhanced_word-level_n-gram_matching)[researchgate.net

The Tesserae Project: Intertextual analysis of Latin poetry - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/259574946_The_Tesserae_Project_Intertextual_analysis_of_Latin_poetry)[researchgate.net

On the Feasibility of Automated Detection of Allusive Text Reuse - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/334601689_On_the_Feasibility_of_Automated_Detection_of_Allusive_Text_Reuse)[researchgate.net

(PDF) Comparative rates of text reuse in classical Latin hexameter poetry - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/329787400_Comparative_rates_of_text_reuse_in_classical_Latin_hexameter_poetry)[arxiv.org

arXiv:1905.02973v1 [cs.CL] 8 May 2019

 Opens in a new window](https://arxiv.org/pdf/1905.02973)[dokumen.pub

New Frontiers in Textual Data Analysis 3031559169, 9783031559167 - DOKUMEN.PUB

 Opens in a new window](https://dokumen.pub/new-frontiers-in-textual-data-analysis-3031559169-9783031559167.html)[researchgate.net

Disentangling the cultural evolution of ancient China: a digital humanities perspective

 Opens in a new window](https://www.researchgate.net/publication/371448116_Disentangling_the_cultural_evolution_of_ancient_China_a_digital_humanities_perspective)

07_A_web_application_for_exploring_primary_sources_The_DanteSources_case_study.pdf

[ppp.worldbank.org

World Development Report 2026 The Promise of Artificial Intelligence

 Opens in a new window](https://ppp.worldbank.org/sites/default/files/2026-08/World%20Development%20Report%202026%20The%20Promise%20of%20Artificial%20Intelligence.pdf)[dcc.dickinson.edu

About DCC | Dickinson College Commentaries

 Opens in a new window](https://dcc.dickinson.edu/about-dcc)[blogs.dickinson.edu

Summer opportunities | Dickinson College Commentaries

 Opens in a new window](https://blogs.dickinson.edu/dcc/category/summer-opportunities/)[blogs.dickinson.edu

Ovid | Dickinson College Commentaries

 Opens in a new window](https://blogs.dickinson.edu/dcc/tag/ovid/)[blogs.dickinson.edu

DCC | Dickinson College Commentaries

 Opens in a new window](https://blogs.dickinson.edu/dcc/tag/dcc/)[rebeccafrostdavis.wordpress.com

Challenges of Blended Learning in Ancient Greek, Follow-Up | Rebecca Frost Davis

 Opens in a new window](https://rebeccafrostdavis.wordpress.com/2013/05/28/challenges-of-blended-learning-in-ancient-greek-follow-up/)[blog.whgazetteer.org

Page 3 – A project of the Institute for Spatial History Innovation at the University of Pittsburgh - World Historical Gazetteer

 Opens in a new window](https://blog.whgazetteer.org/page/3/)[researchgate.net

Linked Data Annotation Without the Pointy Brackets: Introducing Recogito 2 - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/316865029_Linked_Data_Annotation_Without_the_Pointy_Brackets_Introducing_Recogito_2)[ore.exeter.ac.uk

Pelagios - Connecting histories of place. Part I: Methods and Tools.

 Opens in a new window](https://ore.exeter.ac.uk/ndownloader/files/56817923)[cpb-ap-se2.wpmucdn.com

Linked Open Data Case Study - CDN

 Opens in a new window](https://cpb-ap-se2.wpmucdn.com/thinkspace.csu.edu.au/dist/0/3761/files/2017/07/Linked-Open-Data-Case-Study-Assignment-12quq7y.pdf)[researchgate.net

Text Fragment, Image and Image Region selection with Pundit - ResearchGate

 Opens in a new window](https://www.researchgate.net/figure/Text-Fragment-Image-and-Image-Region-selection-with-Pundit_fig2_278407584)[ceur-ws.org

Pundit: Semantically Structured Annotations for Web Contents and Digital Libraries - CEUR-WS.org

 Opens in a new window](https://ceur-ws.org/Vol-912/paper4.pdf)[researchgate.net

Pundit: Semantically structured annotations for web contents and digital libraries

 Opens in a new window](https://www.researchgate.net/publication/290742153_Pundit_Semantically_structured_annotations_for_web_contents_and_digital_libraries)

06_AI-Powered_Corpus_Translation_Studies_at_Work_Exploring_Early_English_Translatio.pdf

[researchgate.net

(PDF) A formal representation of the divine comedy's primary sources: The Hypermedia Dante Network ontology - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/355806241_A_formal_representation_of_the_divine_comedy's_primary_sources_The_Hypermedia_Dante_Network_ontology)[kups.ub.uni-koeln.de

Digitale Edition in Österreich Digital Scholarly Edition in Austria

 Opens in a new window](https://kups.ub.uni-koeln.de/70449/1/06_Oberreither.pdf)[researchgate.net

Knowledge Acquisition on Dante Alighieri's Works | Request PDF - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/345602680_Knowledge_Acquisition_on_Dante_Alighieri's_Works)

09_Linguistic_linked_data_in_digital_humanities.pdf

10_CARE_Collaborative_AI-assisted_reading_environment.pdf

[datacite.hypotheses.org

Speaker presentation | Matthew Munson & Christopher Blackwell - Open Data Citation for Social Sciences and Humanities

 Opens in a new window](https://datacite.hypotheses.org/262)[cite-architecture.github.io

The Canonical Text Services URN specification, version 2.0.rc.1 - The CITE Architecture

 Opens in a new window](https://cite-architecture.github.io/ctsurn_spec/)[scholarlyeditions.brill.com

FAQ - Brill's Scholarly Editions

 Opens in a new window](https://scholarlyeditions.brill.com/faq/)[aclanthology.org

A New Implementation for Canonical Text Services - ACL Anthology

 Opens in a new window](https://aclanthology.org/W14-0601.pdf)[aclanthology.org

The INCEpTION Platform: Machine-Assisted and Knowledge-Oriented Interactive Annotation

 Opens in a new window](https://aclanthology.org/C18-2002/)[eprints.whiterose.ac.uk

Digital editing and publishing in the twenty-first century - White Rose Research Online

 Opens in a new window](https://eprints.whiterose.ac.uk/id/eprint/224714/8/DigitalEditingandPublishingintheTwentyFirstCentury_R_InteractivePDF_20250429_110KKKFull.pdf)[aacademica.org

Open, Equitable, and Minimal: Teaching Digital Scholarly Editing North and South - Acta Académica

 Opens in a new window](https://www.aacademica.org/gimena.delrio.riande/190.pdf)[cambridge.org

Digital Scholarly Editing in Practice - Cambridge University Press & Assessment

 Opens in a new window](https://www.cambridge.org/core/elements/digital-scholarly-editing-in-practice/033E79028A8F05B3537450D993A121C3)[cite-architecture.github.io

Canonical Text Services protocol specification - The CITE Architecture

 Opens in a new window](http://cite-architecture.github.io/cts_spec/)[balisage.net

Balisage Paper: Luminescent: parsing LMNL by XSLT upconversion

 Opens in a new window](https://www.balisage.net/Proceedings/vol8/html/Piez01/BalisageVol8-Piez01.html)
Sources read but not used in the report
[dokumen.pub

Compendium of Computational Theology. Vol. 1: Introducing Digital Humanities to Theology 9783911056199 - DOKUMEN.PUB

 Opens in a new window](https://dokumen.pub/compendium-of-computational-theology-vol-1-introducing-digital-humanities-to-theology-9783911056199.html)[dokumen.pub

Digital Humanities Pedagogy : Practices, Principles and Politics [1 ed.] 9781909254275, 9781909254268 - DOKUMEN.PUB

 Opens in a new window](https://dokumen.pub/digital-humanities-pedagogy-practices-principles-and-politics-1nbsped-9781909254275-9781909254268.html)[github.com

semiont/docs/protocol/flows/MARK.md at main · The-AI-Alliance

 Opens in a new window](https://github.com/The-AI-Alliance/semiont/blob/main/docs/protocol/flows/MARK.md)[academia.edu

(PDF) Integrating Language Technology In a Web-Enabled Cultural Heritage System

 Opens in a new window](https://www.academia.edu/359282/Integrating_Language_Technology_In_a_Web_Enabled_Cultural_Heritage_System)[researchgate.net

A Computational Model of Text Reuse in Ancient Literary Texts. | Request PDF

 Opens in a new window](https://www.researchgate.net/publication/220874654_A_Computational_Model_of_Text_Reuse_in_Ancient_Literary_Texts)[direct.mit.edu

Machine Learning for Ancient Languages: A Survey | Computational Linguistics | MIT Press

 Opens in a new window](https://direct.mit.edu/coli/article/49/3/703/116160/Machine-Learning-for-Ancient-Languages-A-Survey)[giada-collab.github.io

Édition numérique des "Considérations" de Germaine de Staël - GitHub Pages

 Opens in a new window](https://giada-collab.github.io/considerations/documentation_stael/manuscrit_vol_1_docum.html)[library.oapen.org

Performativity and Performance Studies in Digital Cultures - OAPEN Library

 Opens in a new window](https://library.oapen.org/bitstream/id/1fbf5f38-9ec2-4bfe-b559-f97a574b3d52/627661.pdf)[researchgate.net

Annotating digital libraries and electronic editions in a collaborative and semantic perspective - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/267451427_Annotating_digital_libraries_and_electronic_editions_in_a_collaborative_and_semantic_perspective)[researchgate.net

Making digital choreographic objects interrelate: A focus on coding practices

 Opens in a new window](https://www.researchgate.net/publication/320546419_Making_digital_choreographic_objects_interrelate_a_focus_on_coding_practices)[vault.tei-c.de

TEI element entry (entry) - The TEI Archive

 Opens in a new window](https://vault.tei-c.de/P5/4.10.1/doc/tei-p5-doc/en/html/ref-entry.html)[tei-c.org

Appendix C Elements - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/release/doc/tei-p5-doc/en/html/REF-ELEMENTS.html)[majw.uvic.ca

The Medieval Anglo-Jewish Women Project: Schema and Documentation - UVic

 Opens in a new window](https://majw.uvic.ca/documentation/majw.html)[digitallatin.github.io

Guidelines for Encoding Critical Editions for the Library of Digital Latin Texts - GitHub Pages

 Opens in a new window](https://digitallatin.github.io/guidelines/LDLT-Guidelines.html)[rhodomanologia.de

Elements - Rhodomanologia

 Opens in a new window](https://www.rhodomanologia.de/assets/rhodomanologia.html)[github.com

[pattern] Publish a hallucination-resistant KG pattern — Source

 Opens in a new window](https://github.com/Blackcat-Informatics/gmeow-ontology/issues/55)[researchgate.net

Quantitative Intertextuality from the Digital Humanities Perspective: A Survey

 Opens in a new window](https://www.researchgate.net/publication/397188392_Quantitative_Intertextuality_from_the_Digital_Humanities_Perspective_A_Survey)[researchgate.net

The sense of a connection: Automatic tracing of intertextuality by meaning - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/285275578_The_sense_of_a_connection_Automatic_tracing_of_intertextuality_by_meaning)[academia.edu

Intertextual Readings of the Nyāyabhūṣaṇa on Buddhist Anti-Realism - Academia.edu

 Opens in a new window](https://www.academia.edu/94561344/Intertextual_Readings_of_the_Ny%C4%81yabh%C5%AB%E1%B9%A3a%E1%B9%87a_on_Buddhist_Anti_Realism)[aclanthology.org

"Shakespeare in the Vectorian Age" – An evaluation of different word embeddings and NLP parameters for the detection - ACL Anthology

 Opens in a new window](https://aclanthology.org/2020.latechclfl-1.7.pdf)[repository.cam.ac.uk

Interpreting Structured Narrative Representations in Pretrained Language Models - Apollo Repository

 Opens in a new window](https://www.repository.cam.ac.uk/bitstreams/d883be64-73df-459f-860b-6896aaca237c/download)[sighum.wordpress.com

Proceedings of the 4th Joint SIGHUM Workshop on Computational Linguistics on Cultural Heritage, Social Sciences, Humanities and

 Opens in a new window](https://sighum.wordpress.com/wp-content/uploads/2020/12/latech-clfl_2020_proceedings.pdf)[ceur-ws.org

GeoWebAnnotations: Extending the W3C Web Annotation Data Model to annotate geospatial data - CEUR-WS.org

 Opens in a new window](https://ceur-ws.org/Vol-3743/paper5.pdf)[researchgate.net

Progress with Repository-based Annotation Infrastructure for Biodiversity Applications

 Opens in a new window](https://www.researchgate.net/publication/373942312_Progress_with_Repository-based_Annotation_Infrastructure_for_Biodiversity_Applications)[pure.knaw.nl

A Process model of Scholarly Media Annotation - Royal Netherlands Academy of Arts and Sciences (KNAW)

 Opens in a new window](https://pure.knaw.nl/ws/files/4007600/melg_proc17.pdf)[kups.ub.uni-koeln.de

Graph Data-Models and Semantic Web Technologies in Scholarly Digital Editing

 Opens in a new window](https://kups.ub.uni-koeln.de/55227/1/Vogeler.pdf)[journals.ub.uni-heidelberg.de

Linked Ancient World Data: Implementation, Advantages, and Barriers - Heidelberger OJS-Journals

 Opens in a new window](https://journals.ub.uni-heidelberg.de/index.php/dco/article/view/104105/102505)[academic.oup.com

AnnoSys—implementation of a generic annotation system for schema-based data using the example of biodiversity collection data | Database | Oxford Academic

 Opens in a new window](https://academic.oup.com/database/article/doi/10.1093/database/bax018/3074788)[pascal-francis.inist.fr

The Tesserae Project: intertextual analysis of Latin poetry

 Opens in a new window](https://pascal-francis.inist.fr/vibad/index.php?action=getRecordDetail&idt=27527148)[dhi.ac.uk

Building Digital Editions on the Basis of a Virtual Research Environment

 Opens in a new window](https://www.dhi.ac.uk/books/dhc2012/building-digital-editions/)[blogs.library.duke.edu

Graphs, Trees, and Streams: The TEI Data Model - Duke Collaboratory for Classics Computing (DC3)

 Opens in a new window](https://blogs.library.duke.edu/dcthree/2013/08/26/graphs-trees-and-streams-the-tei-data-model/)[academia.edu

(PDF) Text encoding and digital scholarly editions - Academia.edu

 Opens in a new window](https://www.academia.edu/34429187/Text_encoding_and_digital_scholarly_editions)[cris.unibo.it

Śivadharma Database CMS. HTML and graph as a starting ... - Unibo

 Opens in a new window](https://cris.unibo.it/retrieve/4abf4329-bf70-4503-a98d-7f191a66bf3e/%C5%9Aivadharma%20Database%20CMS.pdf)[collaborate.princeton.edu

Machine Learning and the Future of Philology: A Case Study - Princeton University

 Opens in a new window](https://collaborate.princeton.edu/en/publications/machine-learning-and-the-future-of-philology-a-case-study/)[logionproject.princeton.edu

Publications — The Logion Project - Princeton University

 Opens in a new window](https://www.logionproject.princeton.edu/publications)[arxiv.org

KwicKwocKwac, a tool for rapidly generating concordances and marking up a literary text

 Opens in a new window](https://arxiv.org/html/2410.06043v1)[diged.org

Digital Editing Bibliography, by Laura Mandell

 Opens in a new window](http://diged.org/DigitalEditions/Resources/DigEdBibliogZ.html)[academic.oup.com

Semantic precision: crafting RDF-based digital editions for unveiling the layers of historical correspondence - Oxford Academic

 Opens in a new window](https://academic.oup.com/dsh/article/39/3/813/7689293)[kups.ub.uni-koeln.de

Graph Data-Models and Semantic Web Technologies in Scholarly Digital Editing

 Opens in a new window](https://kups.ub.uni-koeln.de/55230/1/Giovannetti.pdf)[tei-c.org

TEI-C Elections 2025 - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/news/2025/08/31/tei-c-elections-2025/)[researchgate.net

Why TEI stand-off annotation doesn't quite work - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/269141044_Why_TEI_stand-off_annotation_doesn't_quite_work)[balisage.net

Balisage Paper: Marking up microrevisions with major implications: Non-linear text in TAG

 Opens in a new window](https://www.balisage.net/Proceedings/vol25/html/Bleeker01/BalisageVol25-Bleeker01.html)[researchgate.net

Corpus Sharing Strategy for Descriptive Linguistics - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/282446823_Corpus_Sharing_Strategy_for_Descriptive_Linguistics)[tei2015.huma-num.fr

Papers - Text Encoding Initiative *Conference and members meeting 2015 - Huma-Num

 Opens in a new window](http://tei2015.huma-num.fr/en/papers/)[academia.edu

SANTA: Systematische Analyse Narrativer Texte durch Annotation (mit Evelyn Gius, Nils Reiter und Jannik Strötgen). In DHd2018, Köln - Academia.edu

 Opens in a new window](https://www.academia.edu/38771969/SANTA_Systematische_Analyse_Narrativer_Texte_durch_Annotation_mit_Evelyn_Gius_Nils_Reiter_und_Jannik_Str%C3%B6tgen_In_DHd2018_K%C3%B6ln)[dhq-static.digitalhumanities.org

DHQ: Digital Humanities Quarterly: Comparative rates ... - DHQ Static

 Opens in a new window](https://dhq-static.digitalhumanities.org/pdf/000237.pdf)[onlineacademiccommunity.uvic.ca

Modeling Texts and Maps with Semantic Annotation - UVic Online Academic Community

 Opens in a new window](https://onlineacademiccommunity.uvic.ca/dhsi/wp-content/uploads/sites/7317/2023/07/W27_Coursepack-DHSI-2023-Modeling-Texts.pdf)[open-research-europe.ec.europa.eu

Modelling the Archipelago: Corfu as a Case Study for a Digital Edition of Cristoforo Buondelmonti's Liber Insularum . - Open Research Europe

 Opens in a new window](https://open-research-europe.ec.europa.eu/articles/4-11)[researchgate.net

The inadequacy of embedded markup for cultural heritage texts

 Opens in a new window](https://www.researchgate.net/publication/220675402_The_inadequacy_of_embedded_markup_for_cultural_heritage_texts)[uhu.es

Reseñas Reviews - Universidad de Huelva

 Opens in a new window](https://www.uhu.es/publicaciones/ojs/index.php/exemplaria/article/view/8494/7275)[escholarship.org

Mythic Recursions: Doubling and Variation in the Mythological Works of Ovid and Valerius Flaccus - eScholarship.org

 Opens in a new window](https://escholarship.org/uc/item/11r709mb)[academia.edu

(PDF) Digital Papyrology II: Case Studies in the Digital Edition of Ancient Greek Papyri - Academia.edu

 Opens in a new window](https://www.academia.edu/38777468/Digital_Papyrology_II_Case_Studies_in_the_Digital_Edition_of_Ancient_Greek_Papyri)[dblp.org

Richard Eckart de Castilho - dblp

 Opens in a new window](https://dblp.org/pid/81/10370)[arxiv.org

Representing Normative Regulations in OWL DL for Automated Compliance Checking Supported by Text Annotation - arXiv

 Opens in a new window](https://arxiv.org/html/2504.05951)[epsir.net

Predictive power of semantic information in the use context of multiword terms for their structural disambiguation

 Opens in a new window](https://epsir.net/index.php/epsir/article/view/2070)[pmc.ncbi.nlm.nih.gov

Towards User-centered Corpus Development: Lessons Learnt from Designing and Developing MedTator - PMC

 Opens in a new window](https://pmc.ncbi.nlm.nih.gov/articles/PMC10148300/)[academic.oup.com

MedTator: a serverless annotation tool for corpus development - Oxford Academic

 Opens in a new window](https://academic.oup.com/bioinformatics/article/38/6/1776/6496915)[frontiersin.org

Markup: A Web-Based Annotation Tool Powered by Active Learning - Frontiers

 Opens in a new window](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2021.598916/full)[direct.mit.edu

Annotation Curricula to Implicitly Train Non-Expert Annotators - MIT Press Direct

 Opens in a new window](https://direct.mit.edu/coli/article/48/2/343/109903/Annotation-Curricula-to-Implicitly-Train-Non)[medinform.jmir.org

Assessing the Performance of Clinical Natural Language Processing Systems: Development of an Evaluation Methodology - JMIR Medical Informatics

 Opens in a new window](https://medinform.jmir.org/2021/7/e20492/)[researchgate.net

Intertextuality in Latin Poetry - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/349551105_Intertextuality_in_Latin_Poetry)[pure.rug.nl

University of Groningen Seneca's Challenge van der Schuur, Marco

 Opens in a new window](https://pure.rug.nl/ws/files/192829505/Complete_thesis.pdf)[library.oapen.org

Digital Scholarly Editing - OAPEN Library

 Opens in a new window](https://library.oapen.org/bitstream/id/9668bc0d-eb07-4b4f-a5e5-0cf335188694/633780.pdf)[socrates.acadiau.ca

Beyond Accessibility: Textual Studies in the 21st Century - Acadia University

 Opens in a new window](http://socrates.acadiau.ca/courses/engl/rcunningham/INKE-TS/18.html)[mural.maynoothuniversity.ie

Digital Critical Editing, Digital Text Analysis, and Charles R. Maturin's Melmoth the Wanderer - - MURAL - Maynooth University Research Archive Library

 Opens in a new window](https://mural.maynoothuniversity.ie/id/eprint/7559/1/Thesis%20Final%20Final%20Final.pdf)[kula.uvic.ca

Open Social Scholarship Annotated Bibliography | KULA

 Opens in a new window](https://kula.uvic.ca/index.php/kula/article/view/82/158)[dlib.nyu.edu

The CITE Architecture: Q & A Regarding CTS and CITE

 Opens in a new window](https://dlib.nyu.edu/awdl/isaw/isaw-papers/20-8/)[campus.dariah.eu

Open Data Citation for Social Science and Humanities | DARIAH-Campus

 Opens in a new window](https://campus.dariah.eu/resources/events/open-data-citation-for-social-science-and-humanities)[wiki.digitalclassicist.org

Canonical Text Services - The Digital Classicist Wiki

 Opens in a new window](https://wiki.digitalclassicist.org/Canonical_Text_Services)[dh2016.adho.org

CTRaCE: Canonical Text Reader and Citation Exporter - DH 2016 Abstracts

 Opens in a new window](https://dh2016.adho.org/abstracts/206)[researchgate.net

(PDF) A New Implementation for Canonical Text Services

 Opens in a new window](https://www.researchgate.net/publication/301405138_A_New_Implementation_for_Canonical_Text_Services)[researchgate.net

(PDF) The born-digital in future digital scholarly editing and publishing - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/376385396_The_born-digital_in_future_digital_scholarly_editing_and_publishing)[textgridlab.org

TEI P5 Application Profile: Ahiqar - textgridlab.org

 Opens in a new window](https://textgridlab.org/1.0/aggregator/html/textgrid:3r8dk.24)[balisage.net

Balisage Paper: Implementing TEI Standoff Annotation in the browser

 Opens in a new window](https://www.balisage.net/Proceedings/vol23/html/Cayless01/BalisageVol23-Cayless01.html)[sfu.ca

3 Elements Available in All TEI Documents - The TEI Guidelines - Simon Fraser University

 Opens in a new window](https://www.sfu.ca/~takeda/tei-guidelines/issue_2382_eventName/html/CO.html)[tei-c.org

4 Default Text Structure - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html)[vault.tei-c.de

Ejemplo: (pointer)

 Opens in a new window](https://vault.tei-c.de/P5/4.8.1/doc/tei-p5-doc/es/html/examples-ptr.html)[pure.knaw.nl

Royal Netherlands Academy of Arts and Sciences (KNAW)

 Opens in a new window](https://pure.knaw.nl/ws/files/4301536/pre_print_standoff_SpadiniTurska.pdf)[ora.ox.ac.uk

Relax NG with Son of ODD - Oxford University Research Archive

 Opens in a new window](https://ora.ox.ac.uk/objects/uuid:b337cb6d-9e7b-4bbc-aa71-f0b9d12bb8de/files/m43ca944cb3ecd57a70d993e32a399174)[biblindex.hypotheses.org

and Small-Scale Intertextuality in Claudian's Mythological and Historical Hexameters - Biblindex

 Opens in a new window](https://biblindex.hypotheses.org/files/2014/04/Coffee_2014-6-2-Lyon.pdf)[openportal.isti.cnr.it

A Web Application for Exploring Primary Sources ... - ISTI Open Portal

 Opens in a new window](https://openportal.isti.cnr.it/data/2018/384308/2018_384308.preprint.pdf)[researchgate.net

Towards a Semantic Network of Dante's Works and Their Contextual Knowledge

 Opens in a new window](https://www.researchgate.net/publication/282357351_Towards_a_Semantic_Network_of_Dante's_Works_and_Their_Contextual_Knowledge)[iris.cnr.it

Enhancing the Computational Representation of Narrative and Its Extraction from Text - CNR-IRIS

 Opens in a new window](https://iris.cnr.it/bitstream/20.500.14243/430908/1/prod_459796-doc_179091.pdf)[dlib.nyu.edu

Time for Linked Open Data - Digital Library Technology Services

 Opens in a new window](http://dlib.nyu.edu/awdl/isaw/isaw-papers/20-3/)[euppublishing.com

Pelagios – Connecting Histories of Place. Part I: Methods and Tools | International Journal of Humanities and Arts Computing

 Opens in a new window](https://www.euppublishing.com/doi/10.3366/ijhac.2021.0260)
Thoughts

Mapping Core Analytical Models

I am synthesizing the structural mechanisms that connect classical text encoding with modern linked data frameworks. Specifically, I am examining how TEI P5 standoff markup—such as standalone notes, intertextual pointers, and interpretive groups—complements the W3C Web Annotation Data Model. This includes evaluating specific target selectors and annotation motivations to understand how static commentary can be dynamically converted into machine-readable knowledge graphs.

Evaluating AI Commentary and Intertextuality

I am assessing the trade-offs of integrating generative AI into editorial workflows against established computational techniques. By juxtaposing algorithmic matching models like Tesserae with recent human-in-the-loop AI frameworks, I am identifying critical risks such as hallucinated citations, anachronistic interpretations, and missing historical context, while analyzing how contextual anchoring can preserve scholarly rigor.

Targeted Technical Information Gathering

To flesh out the technical details and real-world implementations, I am initiating targeted searches focused on specific TEI markup standards, W3C selector mechanics, and primary case studies including the Dickinson College Commentaries, Tesserae, and semantic annotation platforms like Recogito and Pundit.

[github.com

semiont/docs/protocol/flows/MARK.md at main · The-AI-Alliance](https://github.com/The-AI-Alliance/semiont/blob/main/docs/protocol/flows/MARK.md)[ec.europa.eu

Deliverable - European Commission](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5b4d197e5&appId=PPGMS)[academia.edu

(PDF) Integrating Language Technology In a Web-Enabled Cultural Heritage System](https://www.academia.edu/359282/Integrating_Language_Technology_In_a_Web_Enabled_Cultural_Heritage_System)[researchgate.net

Towards a Historical Text Re-use Detection | Request PDF - ResearchGate](https://www.researchgate.net/publication/268445909_Towards_a_Historical_Text_Re-use_Detection)[direct.mit.edu

Machine Learning for Ancient Languages: A Survey | Computational Linguistics | MIT Press](https://direct.mit.edu/coli/article/49/3/703/116160/Machine-Learning-for-Ancient-Languages-A-Survey)[dokumen.pub

Compendium of Computational Theology. Vol. 1: Introducing Digital Humanities to Theology 9783911056199 - DOKUMEN.PUB](https://dokumen.pub/compendium-of-computational-theology-vol-1-introducing-digital-humanities-to-theology-9783911056199.html)[dokumen.pub

New Frontiers in Textual Data Analysis 3031559169, 9783031559167 - DOKUMEN.PUB](https://dokumen.pub/new-frontiers-in-textual-data-analysis-3031559169-9783031559167.html)[academia.edu

Intertextual Readings of the Nyāyabhūṣaṇa on Buddhist Anti-Realism - Academia.edu](https://www.academia.edu/94561344/Intertextual_Readings_of_the_Ny%C4%81yabh%C5%AB%E1%B9%A3a%E1%B9%87a_on_Buddhist_Anti_Realism)[dokumen.pub

Digital Humanities Pedagogy : Practices, Principles and Politics [1 ed.] 9781909254275, 9781909254268 - DOKUMEN.PUB](https://dokumen.pub/digital-humanities-pedagogy-practices-principles-and-politics-1nbsped-9781909254275-9781909254268.html)[researchgate.net

Disentangling the cultural evolution of ancient China: a digital humanities perspective](https://www.researchgate.net/publication/371448116_Disentangling_the_cultural_evolution_of_ancient_China_a_digital_humanities_perspective)[dcc.dickinson.edu

About DCC | Dickinson College Commentaries](https://dcc.dickinson.edu/about-dcc)[blogs.dickinson.edu

Summer opportunities | Dickinson College Commentaries](https://blogs.dickinson.edu/dcc/category/summer-opportunities/)[blogs.dickinson.edu

Ovid | Dickinson College Commentaries](https://blogs.dickinson.edu/dcc/tag/ovid/)[blogs.dickinson.edu

DCC | Dickinson College Commentaries](https://blogs.dickinson.edu/dcc/tag/dcc/)[rebeccafrostdavis.wordpress.com

Challenges of Blended Learning in Ancient Greek, Follow-Up | Rebecca Frost Davis](https://rebeccafrostdavis.wordpress.com/2013/05/28/challenges-of-blended-learning-in-ancient-greek-follow-up/)[researchgate.net

Text Fragment, Image and Image Region selection with Pundit - ResearchGate](https://www.researchgate.net/figure/Text-Fragment-Image-and-Image-Region-selection-with-Pundit_fig2_278407584)[researchgate.net

Pundit: Semantically structured annotations for web contents and digital libraries](https://www.researchgate.net/publication/290742153_Pundit_Semantically_structured_annotations_for_web_contents_and_digital_libraries)

Examining Computational Models for Intertextuality

I am exploring how digital tools formalize intertextual relations and text reuse. Specifically, I am examining the Tesserae project's algorithmic approach, analyzing how it leverages n-gram matching, lemmatization, and TF-IDF scoring to identify subtle parallels across classical literary corpora.

Mapping Semantic Annotation Frameworks

I am analyzing the technical specifications of semantic annotation frameworks like the W3C Web Annotation Data Model alongside TEI elements such as standoff markup and linking mechanisms. I am determining how these structures transform traditional static apparatuses into machine-readable knowledge graphs and linked open data ecosystems.

Planning Technical Deep-Dives

To build a robust comparative framework, I am preparing to gather precise JSON-LD and TEI XML code structures, while evaluating real-world digital scholarly editions such as Dickinson College Commentaries, Recogito, and DanteSources.

[github.com

semiont/docs/protocol/flows/MARK.md at main · The-AI-Alliance](https://github.com/The-AI-Alliance/semiont/blob/main/docs/protocol/flows/MARK.md)[github.com

margin/COMMENT_PROTOCOL.md at main - GitHub](https://github.com/openprose/margin/blob/main/COMMENT_PROTOCOL.md)[github.com

readium/annotations: Model and JSON serialization of annotations associated with EPUB and Web Publications - GitHub](https://github.com/readium/annotations)[researchgate.net

Modeling the scholars: Detecting intertextuality through enhanced word-level n-gram matching | Request PDF - ResearchGate](https://www.researchgate.net/publication/274151306_Modeling_the_scholars_Detecting_intertextuality_through_enhanced_word-level_n-gram_matching)[researchgate.net

On the Feasibility of Automated Detection of Allusive Text Reuse - ResearchGate](https://www.researchgate.net/publication/334601689_On_the_Feasibility_of_Automated_Detection_of_Allusive_Text_Reuse)[sighum.wordpress.com

Proceedings of the 4th Joint SIGHUM Workshop on Computational Linguistics on Cultural Heritage, Social Sciences, Humanities and](https://sighum.wordpress.com/wp-content/uploads/2020/12/latech-clfl_2020_proceedings.pdf)[arxiv.org

arXiv:1905.02973v1 [cs.CL] 8 May 2019](https://arxiv.org/pdf/1905.02973)[academia.edu

(PDF) Integrating Language Technology In a Web-Enabled Cultural Heritage System](https://www.academia.edu/359282/Integrating_Language_Technology_In_a_Web_Enabled_Cultural_Heritage_System)[researchgate.net

A Computational Model of Text Reuse in Ancient Literary Texts. | Request PDF](https://www.researchgate.net/publication/220874654_A_Computational_Model_of_Text_Reuse_in_Ancient_Literary_Texts)[direct.mit.edu

Machine Learning for Ancient Languages: A Survey | Computational Linguistics | MIT Press](https://direct.mit.edu/coli/article/49/3/703/116160/Machine-Learning-for-Ancient-Languages-A-Survey)[openportal.isti.cnr.it

A Web Application for Exploring Primary Sources ... - ISTI Open Portal](https://openportal.isti.cnr.it/data/2018/384308/2018_384308.preprint.pdf)

Uncovering Architectural Alignments

I am examining the technical linkages between TEI P5 standoff markup and W3C Web Annotation standards. Recent data highlights how TEI interpretive groups, pointer elements, and externalized notes map directly to RDF-based Web Annotation models using exact positional and textual quote selectors. This alignment enables static, highly Granular philological notes to be transformed into interoperable, linked open data constructs across distributed digital editions.

Analyzing Algorithmic Text Reuse

I have evaluated the mechanics of computational intertextuality platforms, focusing on two-stage scoring systems that combine lemmatization, phrase density, and frequency-weighted scoring metrics like TF-IDF. These algorithmic approaches successfully isolate meaningful literary allusions from noise, yet comparing them with recent neural approaches demonstrates that traditional lexical scoring remains essential for establishing verifiable surface-level textual evidence.

Consolidating Technical Case Studies

I am initiating targeted queries to extract exact TEI markup patterns and ontology definitions from established digital humanities projects. This will provide concrete encoding examples and structural representations for the final synthesis.

[giada-collab.github.io

Édition numérique des "Considérations" de Germaine de Staël - GitHub Pages](https://giada-collab.github.io/considerations/documentation_stael/manuscrit_vol_1_docum.html)[tei-c.org

TEI element seg (arbitrary segment) - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-seg.html)[rhodomanologia.de

Elements - Rhodomanologia](https://www.rhodomanologia.de/assets/rhodomanologia.html)[tei-c.org

TEI element span - Text Encoding Initiative](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-span.html)[tei-c.org

TEI element note (note) - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-note.html)[dracor-org.github.io

DraCor ODD - GitHub Pages](https://dracor-org.github.io/dracor-schema/)[digitallatin.github.io

Guidelines for Encoding Critical Editions for the Library of Digital Latin Texts - GitHub Pages](https://digitallatin.github.io/guidelines/LDLT-Guidelines.html)[researchgate.net

Pundit: Semantically structured annotations for web contents and digital libraries](https://www.researchgate.net/publication/290742153_Pundit_Semantically_structured_annotations_for_web_contents_and_digital_libraries)[ceur-ws.org

Pundit: Semantically Structured Annotations for Web Contents and Digital Libraries - CEUR-WS.org](https://ceur-ws.org/Vol-912/paper4.pdf)[library.oapen.org

Performativity and Performance Studies in Digital Cultures - OAPEN Library](https://library.oapen.org/bitstream/id/1fbf5f38-9ec2-4bfe-b559-f97a574b3d52/627661.pdf)[researchgate.net

Annotating digital libraries and electronic editions in a collaborative and semantic perspective - ResearchGate](https://www.researchgate.net/publication/267451427_Annotating_digital_libraries_and_electronic_editions_in_a_collaborative_and_semantic_perspective)[researchgate.net

Making digital choreographic objects interrelate: A focus on coding practices](https://www.researchgate.net/publication/320546419_Making_digital_choreographic_objects_interrelate_a_focus_on_coding_practices)

Synthesizing Scholarly Annotation Standards

I am integrating findings on the evolution of digital commentary, linking classical text markup mechanisms to modern open web annotation standards. By examining TEI standoff elements and W3C Web Annotation JSON-LD structures, I am establishing how digital editions bridge inline textual markup with decentralized knowledge graphs.

Analyzing Human-in-the-Loop AI Workflows

I am reviewing recent case studies in digital scholarship, focusing on how large language models and automated entity extraction are combined with expert human oversight. My analysis highlights how structured Human-in-the-Loop protocols mitigate generative AI risks—such as hallucinated citations and anachronisms—when applied to complex historical and philological commentary.

Retrieving Syntax Examples for Text Encoding

I am executing targeted queries to retrieve precise syntax examples for TEI P5 interpretive markup and W3C Web Annotation JSON-LD selectors. These concrete code patterns will ground the comparative evaluation and pedagogical recommendations for digital textual editing curricula.

[vault.tei-c.de

TEI element entry (entry) - The TEI Archive](https://vault.tei-c.de/P5/4.10.1/doc/tei-p5-doc/en/html/ref-entry.html)[tei-c.org

Appendix C Elements - The TEI Guidelines - Text Encoding Initiative](https://tei-c.org/release/doc/tei-p5-doc/en/html/REF-ELEMENTS.html)[tei-c.org

TEI element note (note) - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-note.html)[majw.uvic.ca

The Medieval Anglo-Jewish Women Project: Schema and Documentation - UVic](https://majw.uvic.ca/documentation/majw.html)[digitallatin.github.io

Guidelines for Encoding Critical Editions for the Library of Digital Latin Texts - GitHub Pages](https://digitallatin.github.io/guidelines/LDLT-Guidelines.html)[rhodomanologia.de

Elements - Rhodomanologia](https://www.rhodomanologia.de/assets/rhodomanologia.html)[tei-c.org

TEI element span - Text Encoding Initiative](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-span.html)[tei-c.org

TEI element seg (arbitrary segment) - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-seg.html)[dracor-org.github.io

DraCor ODD - GitHub Pages](https://dracor-org.github.io/dracor-schema/)[github.com

readium/annotations: Model and JSON serialization of annotations associated with EPUB and Web Publications - GitHub](https://github.com/readium/annotations)[github.com

[pattern] Publish a hallucination-resistant KG pattern — Source](https://github.com/Blackcat-Informatics/gmeow-ontology/issues/55)

Mapping Web Annotation Specifications

I am examining the exact JSON-LD structural requirements for W3C Web Annotations, focusing on how text quote selectors and text position selectors interact to anchor comments directly to specific Unicode character offsets. This precision ensures that externalized scholarly commentary remains resilient even as base digital texts undergo versioning or structural changes.

Evaluating Digital Edition Infrastructures

I am analyzing the technical architecture of digital commentaries and semantic annotation platforms like Recogito and Pundit. By evaluating how these systems bridge TEI XML, Drupal-backed databases, and external gazetteer identifiers, I am clarifying how localized classical annotations connect to broader linked open data networks.

Gathering Primary Formulae and Schemas

To ensure complete technical rigor, I am initiating targeted investigations to extract exact mathematical scoring models used in intertextual search algorithms, along with precise TEI P5 XML schema structures for standoff annotations.

[researchgate.net

Modeling the scholars: Detecting intertextuality through enhanced word-level n-gram matching | Request PDF - ResearchGate](https://www.researchgate.net/publication/274151306_Modeling_the_scholars_Detecting_intertextuality_through_enhanced_word-level_n-gram_matching)[researchgate.net

(PDF) Comparative rates of text reuse in classical Latin hexameter poetry - ResearchGate](https://www.researchgate.net/publication/329787400_Comparative_rates_of_text_reuse_in_classical_Latin_hexameter_poetry)[researchgate.net

On the Feasibility of Automated Detection of Allusive Text Reuse - ResearchGate](https://www.researchgate.net/publication/334601689_On_the_Feasibility_of_Automated_Detection_of_Allusive_Text_Reuse)[researchgate.net

Quantitative Intertextuality from the Digital Humanities Perspective: A Survey](https://www.researchgate.net/publication/397188392_Quantitative_Intertextuality_from_the_Digital_Humanities_Perspective_A_Survey)[researchgate.net

The sense of a connection: Automatic tracing of intertextuality by meaning - ResearchGate](https://www.researchgate.net/publication/285275578_The_sense_of_a_connection_Automatic_tracing_of_intertextuality_by_meaning)[academia.edu

Intertextual Readings of the Nyāyabhūṣaṇa on Buddhist Anti-Realism - Academia.edu](https://www.academia.edu/94561344/Intertextual_Readings_of_the_Ny%C4%81yabh%C5%AB%E1%B9%A3a%E1%B9%87a_on_Buddhist_Anti_Realism)[aclanthology.org

"Shakespeare in the Vectorian Age" – An evaluation of different word embeddings and NLP parameters for the detection - ACL Anthology](https://aclanthology.org/2020.latechclfl-1.7.pdf)[repository.cam.ac.uk

Interpreting Structured Narrative Representations in Pretrained Language Models - Apollo Repository](https://www.repository.cam.ac.uk/bitstreams/d883be64-73df-459f-860b-6896aaca237c/download)[sighum.wordpress.com

Proceedings of the 4th Joint SIGHUM Workshop on Computational Linguistics on Cultural Heritage, Social Sciences, Humanities and](https://sighum.wordpress.com/wp-content/uploads/2020/12/latech-clfl_2020_proceedings.pdf)[researchgate.net

Pundit: Semantically structured annotations for web contents and digital libraries](https://www.researchgate.net/publication/290742153_Pundit_Semantically_structured_annotations_for_web_contents_and_digital_libraries)

Mapping Specific Primary Citations

I am gathering precise academic citations, DOIs, and formal publications for core digital humanities frameworks and tools. This involves isolating primary research papers for the W3C Web Annotation Architecture, early and evolved algorithmic formulations of text reuse engines, and foundational publications behind spatial and semantic annotation platforms.

Addressing Methodological Limitations

I am investigating critical friction points in digital editing workflows, specifically focusing on the trade-offs between dense semantic graph architectures and pedagogical accessibility. Additionally, I am evaluating methodological risks like automation bias in automated entity recognition and potential anachronisms when using machine models for historical translation.

Retrieving Primary Citation Details

I am initiating targeted queries to pull exact DOIs and formal metadata for key projects, including web annotation recommendations, classical intertextuality scoring models, and collaborative annotation networks.

[wal.sh

Annotation Systems for Evolving Documents - wal.sh](https://wal.sh/research/annotation-systems/)[ceur-ws.org

GeoWebAnnotations: Extending the W3C Web Annotation Data Model to annotate geospatial data - CEUR-WS.org](https://ceur-ws.org/Vol-3743/paper5.pdf)[journal.code4lib.org

Annotation-based enrichment of Digital Objects using open-source frameworks](https://journal.code4lib.org/articles/12582)[researchgate.net

Progress with Repository-based Annotation Infrastructure for Biodiversity Applications](https://www.researchgate.net/publication/373942312_Progress_with_Repository-based_Annotation_Infrastructure_for_Biodiversity_Applications)[w3.org

Data on the Web Best Practices - W3C](https://www.w3.org/TR/dwbp/)[pure.knaw.nl

A Process model of Scholarly Media Annotation - Royal Netherlands Academy of Arts and Sciences (KNAW)](https://pure.knaw.nl/ws/files/4007600/melg_proc17.pdf)[kups.ub.uni-koeln.de

Graph Data-Models and Semantic Web Technologies in Scholarly Digital Editing](https://kups.ub.uni-koeln.de/55227/1/Vogeler.pdf)[journals.ub.uni-heidelberg.de

Linked Ancient World Data: Implementation, Advantages, and Barriers - Heidelberger OJS-Journals](https://journals.ub.uni-heidelberg.de/index.php/dco/article/view/104105/102505)[academic.oup.com

AnnoSys—implementation of a generic annotation system for schema-based data using the example of biodiversity collection data | Database | Oxford Academic](https://academic.oup.com/database/article/doi/10.1093/database/bax018/3074788)[pascal-francis.inist.fr

The Tesserae Project: intertextual analysis of Latin poetry](https://pascal-francis.inist.fr/vibad/index.php?action=getRecordDetail&idt=27527148)

Exploring Theoretical Markup Debates

I am investigating the fundamental tension in digital humanities between embedded hierarchical markup, such as inline XML trees, and standoff or graph-based data architectures. By examining critique regarding the limitations of embedded markup for complex cultural heritage texts, I am evaluating how overlapping textual structures and multi-layered commentary necessitate non-hierarchical, graph-based editing models.

Assessing AI Impact on Classical Philology

I am analyzing the broader epistemic and pedagogical implications of applying machine learning and generative models to historical language processing. Specifically, I am evaluating how automated citation processing and AI-assisted commentary influence scholarly agency, critical reading skills, and the risk of unverified citation hallucination in digital philology.

Deepening Investigation into Scholarly Discourse

I am launching targeted searches to gather specific empirical arguments surrounding standoff markup efficiency versus graph databases, alongside scholarly literature discussing the future of machine learning in classical philological workflows.

[kups.ub.uni-koeln.de

Graph Data-Models and Semantic Web Technologies in Scholarly Digital Editing](https://kups.ub.uni-koeln.de/54577/1/side15.pdf)[dhi.ac.uk

Building Digital Editions on the Basis of a Virtual Research Environment](https://www.dhi.ac.uk/books/dhc2012/building-digital-editions/)[scispace.com

The inadequacy of embedded markup for cultural heritage texts - SciSpace](https://scispace.com/pdf/the-inadequacy-of-embedded-markup-for-cultural-heritage-4h5dbdkdaa.pdf)[balisage.net

Balisage Paper: Luminescent: parsing LMNL by XSLT upconversion](https://www.balisage.net/Proceedings/vol8/html/Piez01/BalisageVol8-Piez01.html)[researchgate.net

Merging Multi-Version Texts: a Generic Solution to the Overlap Problem - ResearchGate](https://www.researchgate.net/publication/269091340_Merging_Multi-Version_Texts_a_Generic_Solution_to_the_Overlap_Problem)[researchgate.net

The inadequacy of embedded markup for cultural heritage texts](https://www.researchgate.net/publication/220675402_The_inadequacy_of_embedded_markup_for_cultural_heritage_texts)[blogs.library.duke.edu

Graphs, Trees, and Streams: The TEI Data Model - Duke Collaboratory for Classics Computing (DC3)](https://blogs.library.duke.edu/dcthree/2013/08/26/graphs-trees-and-streams-the-tei-data-model/)[academia.edu

(PDF) Text encoding and digital scholarly editions - Academia.edu](https://www.academia.edu/34429187/Text_encoding_and_digital_scholarly_editions)[d-nb.info

www.ssoar.info The role of markup in the digital humanities](https://d-nb.info/1186853379/34)[cris.unibo.it

Śivadharma Database CMS. HTML and graph as a starting ... - Unibo](https://cris.unibo.it/retrieve/4abf4329-bf70-4503-a98d-7f191a66bf3e/%C5%9Aivadharma%20Database%20CMS.pdf)[collaborate.princeton.edu

Machine Learning and the Future of Philology: A Case Study - Princeton University](https://collaborate.princeton.edu/en/publications/machine-learning-and-the-future-of-philology-a-case-study/)[logionproject.princeton.edu

Publications — The Logion Project - Princeton University](https://www.logionproject.princeton.edu/publications)

Resolving Textual Hierarchy Debates

I am investigating the long-standing debate between traditional embedded markup and externalized graph data models. Insights reveal that while embedded XML structures face fundamental limitations when encoding overlapping hierarchies and diachronic textual variants, standoff markup combined with graph-based RDF frameworks offers a robust alternative. This shift allows scholars to represent multiple concurrent perspectives and complex versioning without corrupting the underlying text stream.

Assessing Machine Learning in Philology

I am evaluating modern machine learning applications in historical textual editing, focusing on language models designed to assist with scribal error identification, conjecture generation, and filling textual lacunae. While these computational tools present new opportunities for restoring premodern texts, balancing automated suggestions with human expert oversight remains essential to preserve philological rigor.

Investigating Pedagogical and Technical Dimensions

I am initiating targeted queries to examine specific citation ontologies and resilient web selector mechanics for anchoring digital annotations. Furthermore, I am exploring how automated editing tools impact student agency, specifically investigating how to mitigate automation bias while maintaining productive cognitive engagement in digital scholarly editing workflows.

[kups.ub.uni-koeln.de

Digitale Edition in Österreich Digital Scholarly Edition in Austria](https://kups.ub.uni-koeln.de/70449/1/06_Oberreither.pdf)[wal.sh

Annotation Systems for Evolving Documents - wal.sh](https://wal.sh/research/annotation-systems/)[arxiv.org

KwicKwocKwac, a tool for rapidly generating concordances and marking up a literary text](https://arxiv.org/html/2410.06043v1)[researchgate.net

Opening the book: data models and distractions in digital scholarly editing - ResearchGate](https://www.researchgate.net/publication/333148326_Opening_the_book_data_models_and_distractions_in_digital_scholarly_editing)[ceur-ws.org

Modeling the 'Unthought' - CEUR-WS.org](https://ceur-ws.org/Vol-3110/paper8.pdf)[diged.org

Digital Editing Bibliography, by Laura Mandell](http://diged.org/DigitalEditions/Resources/DigEdBibliogZ.html)[academic.oup.com

Semantic precision: crafting RDF-based digital editions for unveiling the layers of historical correspondence - Oxford Academic](https://academic.oup.com/dsh/article/39/3/813/7689293)[journals.openedition.org

Applied Text as Graph (ATAG) in an Algorithmic Edition - OpenEdition Journals](https://journals.openedition.org/jtei/6027)[balisage.net

Balisage Paper: Encoding semantic relationships in literary texts](https://www.balisage.net/Proceedings/vol26/html/Koidaki01/BalisageVol26-Koidaki01.html)[kups.ub.uni-koeln.de

Graph Data-Models and Semantic Web Technologies in Scholarly Digital Editing](https://kups.ub.uni-koeln.de/55230/1/Giovannetti.pdf)[tei-c.org

TEI-C Elections 2025 - Text Encoding Initiative](https://tei-c.org/news/2025/08/31/tei-c-elections-2025/)[ppp.worldbank.org

World Development Report 2026 The Promise of Artificial Intelligence](https://ppp.worldbank.org/sites/default/files/2026-08/World%20Development%20Report%202026%20The%20Promise%20of%20Artificial%20Intelligence.pdf)

Resolving Overlapping Hierarchy Dilemmas

I am evaluating the persistent tension between standard hierarchical document trees and graph-based models in digital scholarly editions. Evidence reveals that while classical text encoding relies heavily on single-tree hierarchies, accommodating non-linear textual variations, overlapping boundaries, and rich commentary often forces complex workarounds. Graph data models and standalone properties offer superior flexibility for capturing concurrent interpretations, though they present higher storage overhead and require specialized processing pipelines.

Analyzing Annotation Anchor Resilience

I am examining mechanisms for maintaining persistent commentary connections across evolving digital texts. Comparing byte offsets, structural paths, and text quote selectors indicates that combining text matches with prefix and suffix contexts provides robust resilience against minor textual rewrites, though structural deletions still necessitate dedicated change detection tools.

Investigating Theoretical Debates and Epistemic Risks

I am initiating targeted inquiries into the broader methodological controversies in computational philology, focusing on the trade-offs between embedded document schemas and RDF knowledge graphs, alongside cognitive implications such as automation bias and AI-generated citation hallucination in classical studies.

[kups.ub.uni-koeln.de

Graph Data-Models and Semantic Web Technologies in Scholarly Digital Editing](https://kups.ub.uni-koeln.de/54577/1/side15.pdf)[balisage.net

Balisage Paper: Overlapproaches in documents: a definitive classification (in OWL, 2!)](https://www.balisage.net/Proceedings/vol13/html/Peroni01/BalisageVol13-Peroni01.html)[researchgate.net

Why TEI stand-off annotation doesn't quite work - ResearchGate](https://www.researchgate.net/publication/269141044_Why_TEI_stand-off_annotation_doesn't_quite_work)[balisage.net

Balisage Paper: Marking up microrevisions with major implications: Non-linear text in TAG](https://www.balisage.net/Proceedings/vol25/html/Bleeker01/BalisageVol25-Bleeker01.html)[researchgate.net

Corpus Sharing Strategy for Descriptive Linguistics - ResearchGate](https://www.researchgate.net/publication/282446823_Corpus_Sharing_Strategy_for_Descriptive_Linguistics)[tei2015.huma-num.fr

Papers - Text Encoding Initiative *Conference and members meeting 2015 - Huma-Num](http://tei2015.huma-num.fr/en/papers/)[researchgate.net

Overlapproaches in documents: A definitive classification (in OWL, 2!) - ResearchGate](https://www.researchgate.net/publication/265972479_Overlapproaches_in_documents_A_definitive_classification_in_OWL_2)[academia.edu

SANTA: Systematische Analyse Narrativer Texte durch Annotation (mit Evelyn Gius, Nils Reiter und Jannik Strötgen). In DHd2018, Köln - Academia.edu](https://www.academia.edu/38771969/SANTA_Systematische_Analyse_Narrativer_Texte_durch_Annotation_mit_Evelyn_Gius_Nils_Reiter_und_Jannik_Str%C3%B6tgen_In_DHd2018_K%C3%B6ln)[researchgate.net

The Tesserae Project: Intertextual analysis of Latin poetry - ResearchGate](https://www.researchgate.net/publication/259574946_The_Tesserae_Project_Intertextual_analysis_of_Latin_poetry)[dhq-static.digitalhumanities.org

DHQ: Digital Humanities Quarterly: Comparative rates ... - DHQ Static](https://dhq-static.digitalhumanities.org/pdf/000237.pdf)

Resolving Overlapping Hierarchy Challenges

I am analyzing the technical compromises between standoff markup, layered markup models, and OWL-based ontologies like EARMARK for handling overlapping document hierarchies. Recent findings indicate that while externalized standoff annotations successfully decouple dominance from containment relations to support multi-layered literary perspectives, they introduce significant maintenance overhead when underlying base texts undergo revision. Evaluating graph data models alongside standard TEI XML allows me to articulate how hybrid data structures effectively navigate concurrent structural layers without breaking validation.

Evaluating Intertextual Algorithmic Impact

I am examining how automated text reuse detection tools alter traditional philological methodologies and scholarly reading practices. Quantitative comparisons demonstrate that combining phrase density metrics with lemmatized n-gram matching significantly scales candidate discovery across extensive classical corpora. However, framing these algorithmic outputs as heuristic leads rather than definitive proof remains critical to preventing circular reasoning in literary allusion analysis.

Investigating Architectural Protocols and Cognitive Effects

I am initiating targeted inquiries into specialized linked data protocols, focusing on gazetteer integration standards in regional annotation networks and custom grammar linking architectures in digital commentaries. Additionally, I am investigating how cognitive offloading and automation bias influence student textual engagement when applying generative models to classical annotation tasks.

[blog.whgazetteer.org

Page 3 – A project of the Institute for Spatial History Innovation at the University of Pittsburgh - World Historical Gazetteer](https://blog.whgazetteer.org/page/3/)[researchgate.net

Linked Data Annotation Without the Pointy Brackets: Introducing Recogito 2 - ResearchGate](https://www.researchgate.net/publication/316865029_Linked_Data_Annotation_Without_the_Pointy_Brackets_Introducing_Recogito_2)[euppublishing.com

Pelagios – Connecting Histories of Place. Part I: Methods and Tools | International Journal of Humanities and Arts Computing](https://www.euppublishing.com/doi/10.3366/ijhac.2021.0260)[cpb-ap-se2.wpmucdn.com

Linked Open Data Case Study - CDN](https://cpb-ap-se2.wpmucdn.com/thinkspace.csu.edu.au/dist/0/3761/files/2017/07/Linked-Open-Data-Case-Study-Assignment-12quq7y.pdf)[onlineacademiccommunity.uvic.ca

Modeling Texts and Maps with Semantic Annotation - UVic Online Academic Community](https://onlineacademiccommunity.uvic.ca/dhsi/wp-content/uploads/sites/7317/2023/07/W27_Coursepack-DHSI-2023-Modeling-Texts.pdf)[ore.exeter.ac.uk

Pelagios - Connecting histories of place. Part I: Methods and Tools.](https://ore.exeter.ac.uk/ndownloader/files/56817923)[open-research-europe.ec.europa.eu

Modelling the Archipelago: Corfu as a Case Study for a Digital Edition of Cristoforo Buondelmonti's Liber Insularum . - Open Research Europe](https://open-research-europe.ec.europa.eu/articles/4-11)[kups.ub.uni-koeln.de

Graph Data-Models and Semantic Web Technologies in Scholarly Digital Editing](https://kups.ub.uni-koeln.de/54577/1/side15.pdf)[researchgate.net

The inadequacy of embedded markup for cultural heritage texts](https://www.researchgate.net/publication/220675402_The_inadequacy_of_embedded_markup_for_cultural_heritage_texts)

Uncovering Linked Geodata Infrastructures

I am examining how historical gazetteer indexes and linked open data ecosystems connect ancient place names with persistent web identifiers. Insights highlight how platforms aggregate geographical data through uniform resource identifiers to form a shared spatial backbone. By adopting standardized models for linked places and web annotations, digital historical projects can seamlessly map heterogeneous text references across space and time without requiring centralized database structures.

Resolving Entity Reconciliation Protocols

I am analyzing the mechanics of semi-automated reconciliation services used to align historical place attestations with global authority files. Early experiments with simple name matching failed due to orthographic variants and historical name changes, but adopting standardized gazetteer identifiers resolved these discrepancies. This approach enables dynamic cross-referencing between ancient geographic sources, modern GIS coordinates, and digital mapping interfaces.

Expanding Empirical Tool Inquiries

I am initiating targeted queries to compare specialized historical text reuse platforms with traditional algorithmic models, while examining the technical architecture of specialized human-assisted annotation systems. Additionally, I am investigating scholarly debates surrounding automated allusion detection to evaluate the balance between exact string matching, semantic paraphrase, and qualitative literary interpretation.

[uhu.es

Reseñas Reviews - Universidad de Huelva](https://www.uhu.es/publicaciones/ojs/index.php/exemplaria/article/view/8494/7275)[escholarship.org

Mythic Recursions: Doubling and Variation in the Mythological Works of Ovid and Valerius Flaccus - eScholarship.org](https://escholarship.org/uc/item/11r709mb)[dokumen.pub

Repeat Performances: Ovidian Repetition and the Metamorphoses 0299307506, 9780299307509 - DOKUMEN.PUB](https://dokumen.pub/repeat-performances-ovidian-repetition-and-the-metamorphoses-0299307506-9780299307509.html)[academia.edu

(PDF) Digital Papyrology II: Case Studies in the Digital Edition of Ancient Greek Papyri - Academia.edu](https://www.academia.edu/38777468/Digital_Papyrology_II_Case_Studies_in_the_Digital_Edition_of_Ancient_Greek_Papyri)[aclanthology.org

The INCEpTION Platform: Machine-Assisted and Knowledge-Oriented Interactive Annotation](https://aclanthology.org/C18-2002/)[dblp.org

Richard Eckart de Castilho - dblp](https://dblp.org/pid/81/10370)[arxiv.org

Representing Normative Regulations in OWL DL for Automated Compliance Checking Supported by Text Annotation - arXiv](https://arxiv.org/html/2504.05951)[epsir.net

Predictive power of semantic information in the use context of multiword terms for their structural disambiguation](https://epsir.net/index.php/epsir/article/view/2070)[pmc.ncbi.nlm.nih.gov

Towards User-centered Corpus Development: Lessons Learnt from Designing and Developing MedTator - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10148300/)[academic.oup.com

MedTator: a serverless annotation tool for corpus development - Oxford Academic](https://academic.oup.com/bioinformatics/article/38/6/1776/6496915)[frontiersin.org

Markup: A Web-Based Annotation Tool Powered by Active Learning - Frontiers](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2021.598916/full)[direct.mit.edu

Annotation Curricula to Implicitly Train Non-Expert Annotators - MIT Press Direct](https://direct.mit.edu/coli/article/48/2/343/109903/Annotation-Curricula-to-Implicitly-Train-Non)[medinform.jmir.org

Assessing the Performance of Clinical Natural Language Processing Systems: Development of an Evaluation Methodology - JMIR Medical Informatics](https://medinform.jmir.org/2021/7/e20492/)[researchgate.net

Intertextuality in Latin Poetry - ResearchGate](https://www.researchgate.net/publication/349551105_Intertextuality_in_Latin_Poetry)[pure.rug.nl

University of Groningen Seneca's Challenge van der Schuur, Marco](https://pure.rug.nl/ws/files/192829505/Complete_thesis.pdf)

Resolving Methodological Tension in Intertextual Retrieval

I am evaluating the methodological debate between traditional algorithmic string-matching engines and modern vector-based semantic embeddings for intertextual discovery in classical and medieval literature. My analysis indicates that while lexical metrics effectively capture exact surface repetitions, orthographic variations, and morphological roots, semantic neural models excel at uncovering abstract thematic allusions and conceptual resonances. However, vector models struggle with brief, highly elliptical classical citations, demonstrating that hybrid pipelines combining surface-level n-gram matching with semantic re-ranking provide the most reliable framework for philological research.

Mapping Granular Citation Ontologies and Standards

I am examining specialized linked data specifications that formalize scholarly citations into distinct semantic categories. By analyzing domain-specific ontologies—such as those classifying citations into explicit, strict, or general intertextual references—I am detailing how digital editions map raw commentary into queryable triple stores. Furthermore, exploring standardized export formats across collaborative annotation platforms reveals how localized text annotations are seamlessly integrated into broader Web Annotation frameworks.

Investigating Knowledge Graph Epistemic Shifts

I am initiating targeted inquiries into the broader pedagogical and epistemic implications of transitioning from traditional linear footnote apparatuses to interconnected knowledge graphs. Specifically, I am exploring how dynamic graph visualizations impact student critical reasoning, textual authority, and editing practices in digital humanities curricula.

[cpb-ap-se2.wpmucdn.com

Linked Open Data Case Study - CDN](https://cpb-ap-se2.wpmucdn.com/thinkspace.csu.edu.au/dist/0/3761/files/2017/07/Linked-Open-Data-Case-Study-Assignment-12quq7y.pdf)[kups.ub.uni-koeln.de

Graph Data-Models and Semantic Web Technologies in Scholarly Digital Editing](https://kups.ub.uni-koeln.de/54577/1/side15.pdf)[researchgate.net

(PDF) A formal representation of the divine comedy's primary sources: The Hypermedia Dante Network ontology - ResearchGate](https://www.researchgate.net/publication/355806241_A_formal_representation_of_the_divine_comedy's_primary_sources_The_Hypermedia_Dante_Network_ontology)[library.oapen.org

Digital Scholarly Editing - OAPEN Library](https://library.oapen.org/bitstream/id/9668bc0d-eb07-4b4f-a5e5-0cf335188694/633780.pdf)[researchgate.net

(PDF) Theorizing the Digital Scholarly Edition - ResearchGate](https://www.researchgate.net/publication/227774739_Theorizing_the_Digital_Scholarly_Edition)[socrates.acadiau.ca

Beyond Accessibility: Textual Studies in the 21st Century - Acadia University](http://socrates.acadiau.ca/courses/engl/rcunningham/INKE-TS/18.html)[scholarworks.iu.edu

Rethinking Scholarly Commentary in the Age of Google - IU ScholarWorks](https://scholarworks.iu.edu/journals/index.php/textual/article/download/27152/32670/65949)[mural.maynoothuniversity.ie

Digital Critical Editing, Digital Text Analysis, and Charles R. Maturin's Melmoth the Wanderer - - MURAL - Maynooth University Research Archive Library](https://mural.maynoothuniversity.ie/id/eprint/7559/1/Thesis%20Final%20Final%20Final.pdf)[eprints.whiterose.ac.uk

Digital editing and publishing in the twenty-first century - White Rose Research Online](https://eprints.whiterose.ac.uk/id/eprint/224714/8/DigitalEditingandPublishingintheTwentyFirstCentury_R_InteractivePDF_20250429_110KKKFull.pdf)[kula.uvic.ca

Open Social Scholarship Annotated Bibliography | KULA](https://kula.uvic.ca/index.php/kula/article/view/82/158)[aacademica.org

Open, Equitable, and Minimal: Teaching Digital Scholarly Editing North and South - Acta Académica](https://www.aacademica.org/gimena.delrio.riande/190.pdf)

Uncovering Export Protocols in Semantic Platforms

I am examining how specialized web annotation tools transform raw textual markup into standardized graph datasets. Recent findings show that platforms like Recogito bridging TEI XML markup with W3C Web Annotation ontologies allow editions to export multi-layered entity relationships directly into structured formats, such as CSV node-and-edge lists for network analysis and JSON-LD streams for linked data consumers. This capability demonstrates how localized digital editing workflows seamlessly integrate with broader semantic graph ecosystems.

Resolving Domain-Specific Exegetical Modeling

I am investigating how specialized formal ontologies resolve the challenge of representing complex primary source commentary. In initiatives like the Hypermedia Dante Network and DanteSources, standard Web Ontology Language constructs are extended using foundational models like CIDOC CRM and LRMoo to capture nuanced commentary relationships—distinguishing precisely between the textual subject, the cited source, and the interpretive object of scholarly references.

Exploring Machine-Actionable Textual Addressability

I am initiating targeted queries into Canonical Text Services (CTS URNs) and CITE architecture to analyze how standardized textual addressing protocols enable precise citation across distributed digital editions. Additionally, I am investigating the methodological tension between minimal computing approaches and complex semantic graph infrastructures to evaluate trade-offs in long-term technical sustainability and pedagogical accessibility.

[dlib.nyu.edu

The CITE Architecture: Q & A Regarding CTS and CITE](https://dlib.nyu.edu/awdl/isaw/isaw-papers/20-8/)[datacite.hypotheses.org

Speaker presentation | Matthew Munson & Christopher Blackwell - Open Data Citation for Social Sciences and Humanities](https://datacite.hypotheses.org/262)[scholarlyeditions.brill.com

FAQ - Brill's Scholarly Editions](https://scholarlyeditions.brill.com/faq/)[campus.dariah.eu

Open Data Citation for Social Science and Humanities | DARIAH-Campus](https://campus.dariah.eu/resources/events/open-data-citation-for-social-science-and-humanities)[wiki.digitalclassicist.org

Canonical Text Services - The Digital Classicist Wiki](https://wiki.digitalclassicist.org/Canonical_Text_Services)[aclanthology.org

A New Implementation for Canonical Text Services - ACL Anthology](https://aclanthology.org/W14-0601.pdf)[dh2016.adho.org

CTRaCE: Canonical Text Reader and Citation Exporter - DH 2016 Abstracts](https://dh2016.adho.org/abstracts/206)[cite-architecture.github.io

The Canonical Text Services URN specification, version 2.0.rc.1 - The CITE Architecture](https://cite-architecture.github.io/ctsurn_spec/)[cite-architecture.github.io

Canonical Text Services protocol specification - The CITE Architecture](http://cite-architecture.github.io/cts_spec/)[researchgate.net

(PDF) A New Implementation for Canonical Text Services](https://www.researchgate.net/publication/301405138_A_New_Implementation_for_Canonical_Text_Services)[cambridge.org

Digital Scholarly Editing in Practice - Cambridge University Press & Assessment](https://www.cambridge.org/core/elements/digital-scholarly-editing-in-practice/033E79028A8F05B3537450D993A121C3)[researchgate.net

(PDF) The born-digital in future digital scholarly editing and publishing - ResearchGate](https://www.researchgate.net/publication/376385396_The_born-digital_in_future_digital_scholarly_editing_and_publishing)

Uncovering Canonical Text Service Protocols

I am synthesizing the core architecture of Canonical Text Services (CTS) and CITE Uniform Resource Names (URNs) as foundational components for digital editions. Recent data highlights how CTS URNs formalize a hierarchical data model—organizing texts across text groups, works, versions, and exemplars—that operates independently of specific underlying storage technologies like XML, relational databases, or RDF triples. This decoupling allows digital scholarly editions to retrieve specific text passages down to the individual word or character level using stable, machine-actionable scholarly citations.

Addressing Sustainability in Digital Editing

I am evaluating the tension between complex, resource-intensive graph-based infrastructure and minimal computing principles within digital scholarly editing. While RDF triplestores and dynamic knowledge graphs offer deep semantic querying capabilities, they often introduce long-term maintenance overhead and technical fragility. Transitioning toward lightweight, static-site architectures and standardized standoff files provides a sustainable alternative that ensures long-term scholarly access without sacrificing structural granularity.

Investigating Formal Specifications and Pedagogical Impacts

I am initiating targeted queries to examine the exact W3C Web Annotation JSON-LD context specifications alongside TEI P5 formal guidelines for interpretative groups and standoff elements. Additionally, I am investigating how cognitive offloading and automation bias influence student agency when generative AI commentary and complex knowledge graph visualizations are introduced into digital humanities curricula.

[tei-c.org

TEI element standOff - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-standOff.html)[textgridlab.org

TEI P5 Application Profile: Ahiqar - textgridlab.org](https://textgridlab.org/1.0/aggregator/html/textgrid:3r8dk.24)[tei-c.org

TEI element annotation - Text Encoding Initiative](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-annotation.html)[tei-c.org

17 Linking, Segmentation, and Alignment - The TEI Guidelines - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/SA.html)[balisage.net

Balisage Paper: Implementing TEI Standoff Annotation in the browser](https://www.balisage.net/Proceedings/vol23/html/Cayless01/BalisageVol23-Cayless01.html)[sfu.ca

3 Elements Available in All TEI Documents - The TEI Guidelines - Simon Fraser University](https://www.sfu.ca/~takeda/tei-guidelines/issue_2382_eventName/html/CO.html)[tei-c.org

4 Default Text Structure - The TEI Guidelines - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/DS.html)[vault.tei-c.de

Ejemplo: (pointer)](https://vault.tei-c.de/P5/4.8.1/doc/tei-p5-doc/es/html/examples-ptr.html)[pure.knaw.nl

Royal Netherlands Academy of Arts and Sciences (KNAW)](https://pure.knaw.nl/ws/files/4301536/pre_print_standoff_SpadiniTurska.pdf)[ora.ox.ac.uk

Relax NG with Son of ODD - Oxford University Research Archive](https://ora.ox.ac.uk/objects/uuid:b337cb6d-9e7b-4bbc-aa71-f0b9d12bb8de/files/m43ca944cb3ecd57a70d993e32a399174)[biblindex.hypotheses.org

and Small-Scale Intertextuality in Claudian's Mythological and Historical Hexameters - Biblindex](https://biblindex.hypotheses.org/files/2014/04/Coffee_2014-6-2-Lyon.pdf)

Uncovering Architectural Alignment in Standoff Markup

I am synthesizing findings on how the TEI P5 standoff element and annotation mechanisms integrate directly with the W3C Web Annotation Data Model. By evaluating how standoff containers decouple annotations from base transcriptions, I am determining how TEI markup elements—such as interpretive groups, pointers, and target attributes—map to RDF-based Web Annotation structures, providing a standardized mechanism to externalize complex scholarly commentary without compromising underlying text integrity.

Analyzing Algorithmic Intertextual Architectures

I am examining the technical architecture of computational text reuse models, focusing on how multi-stage algorithms like Tesserae combine lemmatization, bigram indexing, and frequency-weighted scoring metrics to surface non-obvious literary allusions. Comparing these two-stage lexical scoring engines with modern neural and vector-based retrieval approaches highlights how classical surface-level metrics remain indispensable for providing verifiable textual evidence while controlling false positive rates across extensive classical corpora.

Investigating Specialized Linked Data Case Studies

I am executing targeted searches to examine specific domain ontologies and spatial-semantic annotation ecosystems, focusing on how initiatives like DanteSources and the Pelagios Network leverage FRBRoo, CiTO, and W3C Web Annotation standards to formalize complex literary and geographical relationships into queryable knowledge graphs.

[researchgate.net

Knowledge Acquisition on Dante Alighieri's Works | Request PDF - ResearchGate](https://www.researchgate.net/publication/345602680_Knowledge_Acquisition_on_Dante_Alighieri's_Works)[openportal.isti.cnr.it

A Web Application for Exploring Primary Sources ... - ISTI Open Portal](https://openportal.isti.cnr.it/data/2018/384308/2018_384308.preprint.pdf)[researchgate.net

Towards a Semantic Network of Dante's Works and Their Contextual Knowledge](https://www.researchgate.net/publication/282357351_Towards_a_Semantic_Network_of_Dante's_Works_and_Their_Contextual_Knowledge)[iris.cnr.it

Enhancing the Computational Representation of Narrative and Its Extraction from Text - CNR-IRIS](https://iris.cnr.it/bitstream/20.500.14243/430908/1/prod_459796-doc_179091.pdf)[dlib.nyu.edu

Time for Linked Open Data - Digital Library Technology Services](http://dlib.nyu.edu/awdl/isaw/isaw-papers/20-3/)[researchgate.net

Linked Data Annotation Without the Pointy Brackets: Introducing Recogito 2 - ResearchGate](https://www.researchgate.net/publication/316865029_Linked_Data_Annotation_Without_the_Pointy_Brackets_Introducing_Recogito_2)[euppublishing.com

Pelagios – Connecting Histories of Place. Part I: Methods and Tools | International Journal of Humanities and Arts Computing](https://www.euppublishing.com/doi/10.3366/ijhac.2021.0260)[cpb-ap-se2.wpmucdn.com

Linked Open Data Case Study - CDN](https://cpb-ap-se2.wpmucdn.com/thinkspace.csu.edu.au/dist/0/3761/files/2017/07/Linked-Open-Data-Case-Study-Assignment-12quq7y.pdf)[kups.ub.uni-koeln.de

Graph Data-Models and Semantic Web Technologies in Scholarly Digital Editing](https://kups.ub.uni-koeln.de/54577/1/side15.pdf)

Uncovering Multilingual Knowledge Graph Architectures

I am synthesizing findings on advanced graph-based commentary frameworks, focusing on multi-layered ontologies that bridge classical texts, linguistic layers, and conceptual annotations. Case studies like Graphilosophy highlight how combining dense knowledge graph schemas with multi-vector embeddings enables tri-parallel textual representation across ancient, Sino-Vietnamese, and modern languages, while Retrieval-Augmented Generation helps mitigate visual clutter in complex commentary networks.

Resolving Automation Bias in AI Workflows

I am evaluating how structured Human-in-the-Loop protocols and anchoring mechanisms mitigate the risks of generative AI in scholarly research. While automated models streamline entity tagging, transcription, and contextual retrieval across massive historical archives, integrating update-aware context windows and active human verification is essential to counter cognitive offloading and prevent citation hallucination in classical philological workflows.

Synthesizing Core Research and Formalization

Having reached full analytical saturation across all encoding standards, algorithmic intertextuality models, semantic graph architectures, and pedagogical frameworks, I am concluding the research phase and proceeding to compile the complete comprehensive report.

The initial research has returned a lot of information. I'm sorting through it and organizing it. This will make sure the whole thing flows well and hits all the key points you asked for.

This is it! I’m bringing it all together. Jotting down my final thoughts, polishing everything up, and making sure I give you my very best work.

## References (APA)

1. researchgate.net. (n.d.). *(PDF) Theorizing the Digital Scholarly Edition*. https://www.researchgate.net/publication/227774739_Theorizing_the_Digital_Scholarly_Edition
2. dokumen.pub. (n.d.). *Repeat Performances: Ovidian Repetition and the Metamorphoses 0299307506, 9780299307509 - DOKUMEN.PUB*. https://dokumen.pub/repeat-performances-ovidian-repetition-and-the-metamorphoses-0299307506-9780299307509.html
3. dracor-org.github.io. (n.d.). *DraCor ODD - GitHub Pages*. https://dracor-org.github.io/dracor-schema/
4. scholarworks.iu.edu. (n.d.). *Rethinking Scholarly Commentary in the Age of Google - IU ScholarWorks*. https://scholarworks.iu.edu/journals/index.php/textual/article/download/27152/32670/65949
5. d-nb.info. (n.d.). *www.ssoar.info The role of markup in the digital humanities*. https://d-nb.info/1186853379/34
6. tei-c.org. (n.d.). *TEI element span - Text Encoding Initiative*. https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-span.html
7. ceur-ws.org. (n.d.). *Modeling the 'Unthought' - CEUR-WS.org*. https://ceur-ws.org/Vol-3110/paper8.pdf
8. balisage.net. (n.d.). *Balisage Paper: Encoding semantic relationships in literary texts*. https://www.balisage.net/Proceedings/vol26/html/Koidaki01/BalisageVol26-Koidaki01.html
9. tei-c.org. (n.d.). *17 Linking, Segmentation, and Alignment - The TEI Guidelines - Text Encoding Initiative*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/SA.html
10. github.com. (n.d.). *margin/COMMENT_PROTOCOL.md at main*. https://github.com/openprose/margin/blob/main/COMMENT_PROTOCOL.md
11. w3.org. (n.d.). *Data on the Web Best Practices - W3C*. https://www.w3.org/TR/dwbp/
12. researchgate.net. (n.d.). *Towards a Historical Text Re-use Detection | Request PDF*. https://www.researchgate.net/publication/268445909_Towards_a_Historical_Text_Re-use_Detection
13. researchgate.net. (n.d.). *The Tesserae Project: Intertextual analysis of Latin poetry*. https://www.researchgate.net/publication/259574946_The_Tesserae_Project_Intertextual_analysis_of_Latin_poetry
14. journal.code4lib.org. (n.d.). *Annotation-based enrichment of Digital Objects using open-source frameworks*. https://journal.code4lib.org/articles/12582
15. github.com. (n.d.). *readium/annotations: Model and JSON serialization of annotations associated with EPUB and Web Publications*. https://github.com/readium/annotations
16. researchgate.net. (n.d.). *On the Feasibility of Automated Detection of Allusive Text Reuse*. https://www.researchgate.net/publication/334601689_On_the_Feasibility_of_Automated_Detection_of_Allusive_Text_Reuse
17. researchgate.net. (n.d.). *(PDF) Comparative rates of text reuse in classical Latin hexameter poetry*. https://www.researchgate.net/publication/329787400_Comparative_rates_of_text_reuse_in_classical_Latin_hexameter_poetry
18. ppp.worldbank.org. (n.d.). *World Development Report 2026 The Promise of Artificial Intelligence*. https://ppp.worldbank.org/sites/default/files/2026-08/World%20Development%20Report%202026%20The%20Promise%20of%20Artificial%20Intelligence.pdf
19. dokumen.pub. (n.d.). *New Frontiers in Textual Data Analysis 3031559169, 9783031559167 - DOKUMEN.PUB*. https://dokumen.pub/new-frontiers-in-textual-data-analysis-3031559169-9783031559167.html
20. researchgate.net. (n.d.). *Disentangling the cultural evolution of ancient China: a digital humanities perspective*. https://www.researchgate.net/publication/371448116_Disentangling_the_cultural_evolution_of_ancient_China_a_digital_humanities_perspective
21. researchgate.net. (n.d.). *Overlapproaches in documents: A definitive classification (in OWL, 2!)*. https://www.researchgate.net/publication/265972479_Overlapproaches_in_documents_A_definitive_classification_in_OWL_2
22. blogs.dickinson.edu. (n.d.). *Ovid | Dickinson College Commentaries*. https://blogs.dickinson.edu/dcc/tag/ovid/
23. rebeccafrostdavis.wordpress.com. (n.d.). *Challenges of Blended Learning in Ancient Greek, Follow-Up | Rebecca Frost Davis*. https://rebeccafrostdavis.wordpress.com/2013/05/28/challenges-of-blended-learning-in-ancient-greek-follow-up/
24. researchgate.net. (n.d.). *Text Fragment, Image and Image Region selection with Pundit*. https://www.researchgate.net/figure/Text-Fragment-Image-and-Image-Region-selection-with-Pundit_fig2_278407584
25. researchgate.net. (n.d.). *Opening the book: data models and distractions in digital scholarly editing*. https://www.researchgate.net/publication/333148326_Opening_the_book_data_models_and_distractions_in_digital_scholarly_editing
26. kups.ub.uni-koeln.de. (n.d.). *Digitale Edition in Österreich Digital Scholarly Edition in Austria*. https://kups.ub.uni-koeln.de/70449/1/06_Oberreither.pdf
27. researchgate.net. (n.d.). *Knowledge Acquisition on Dante Alighieri's Works | Request PDF*. https://www.researchgate.net/publication/345602680_Knowledge_Acquisition_on_Dante_Alighieri's_Works
28. cite-architecture.github.io. (n.d.). *The Canonical Text Services URN specification, version 2.0.rc.1 - The CITE Architecture*. https://cite-architecture.github.io/ctsurn_spec/
29. aclanthology.org. (n.d.). *A New Implementation for Canonical Text Services - ACL Anthology*. https://aclanthology.org/W14-0601.pdf
30. eprints.whiterose.ac.uk. (n.d.). *Digital editing and publishing in the twenty-first century - White Rose Research Online*. https://eprints.whiterose.ac.uk/id/eprint/224714/8/DigitalEditingandPublishingintheTwentyFirstCentury_R_InteractivePDF_20250429_110KKKFull.pdf
31. cambridge.org. (n.d.). *Digital Scholarly Editing in Practice - Cambridge University Press & Assessment*. https://www.cambridge.org/core/elements/digital-scholarly-editing-in-practice/033E79028A8F05B3537450D993A121C3
32. cite-architecture.github.io. (n.d.). *Canonical Text Services protocol specification - The CITE Architecture*. http://cite-architecture.github.io/cts_spec/
33. blogs.dickinson.edu. (n.d.). *DCC | Dickinson College Commentaries*. https://blogs.dickinson.edu/dcc/tag/dcc/
34. github.com. (n.d.). *semiont/docs/protocol/flows/MARK.md at main · The-AI-Alliance*. https://github.com/The-AI-Alliance/semiont/blob/main/docs/protocol/flows/MARK.md
35. dokumen.pub. (n.d.). *Digital Humanities Pedagogy : Practices, Principles and Politics [1 ed.] 9781909254275, 9781909254268 - DOKUMEN.PUB*. https://dokumen.pub/digital-humanities-pedagogy-practices-principles-and-politics-1nbsped-9781909254275-9781909254268.html
36. ceur-ws.org. (n.d.). *Pundit: Semantically Structured Annotations for Web Contents and Digital Libraries - CEUR-WS.org*. https://ceur-ws.org/Vol-912/paper4.pdf

_43 citation marker(s) carried no resolvable source in the DOM and were dropped; see the `*_citations.json` sidecar._
