# Topic 07 (Topic_07_Collation): Academic Deep Research Report

**Model:** 3.1 Pro (Deep Research)  
**Attachments:** 3 PDF(s)  
**Citations resolved:** 18

## Automated Text Collation Research

ContentsShare & Export
Create

# Automating the Archive: Computational Collation, Variant Graph Models, and the Transformation of Textual Scholarship

## 1. Abstract & Executive Summary

Within the context of digital humanities and textual scholarship based in Antigonish, Nova Scotia, the integration of computational methodologies into undergraduate curricula requires a rigorous evaluation of the tools that are reshaping the discipline. At the heart of this methodological revolution is the automation of textual collation—the process of aligning multiple manuscript witnesses to identify textual variance. For centuries, this foundational philological task relied entirely upon the cognitive endurance of the human editor. Today, computational collation tools, most notably CollateX, have fundamentally transformed the landscape of textual criticism. By systematically aligning witnesses and generating reproducible variant tables and graphs, these algorithms allow scholars to process massive, hyper-contaminated textual traditions that were previously insurmountable.

The central inquiry of this report investigates how computational collation tools automate witness alignment and textual variant identification across manuscript traditions, and how this computational paradigm compares to traditional manual collation. The core thesis substantiated herein posits that automated collation algorithms transform textual criticism by enforcing explicit, reproducible workflows, effectively replacing the implicit, subjective normalization inherent in manual collation with the rigorous architectural framework of the Gothenburg Model. However, algorithmic alignment is not an infallible panacea. It must be continuously checked against traditional manual collation principles and adjudicated with a rigorous variant taxonomy. The inherently "literal" nature of computational string-matching algorithms often produces excessive "noise" when confronted with the extreme orthographic and morphological instability of historical languages. Therefore, algorithmic output must be mediated by expert philological judgment.

Drawing upon a synthesis of computational philology, bioinformatics, and manuscript studies, this report provides an exhaustive evaluation of the technical foundations of text alignment. This includes a deep analysis of the bioinformatic Needleman-Wunsch and Gotoh algorithms, which form the mathematical basis for sequence alignment, and the variant graph data models that underpin modern collation engines. Through comparative methodological evaluations and real-world digital edition case studies—including the *Editio Critica Maior* (ECM), the Charles Darwin Manuscripts, and the *Canterbury Tales Project*—the analysis demonstrates both the power and the epistemological limitations of digital recension. Finally, the report translates these scholarly insights into a pedagogical framework, offering a comprehensive Python tutorial for CollateX and a variant taxonomy classification guide specifically designed for the training of next-generation digital editors.

## 2. Technical, Methodological & Historical Foundations

To comprehend the mechanics of contemporary automated collation, it is necessary to trace the historical trajectory of textual comparison, the adoption of bioinformatic algorithms for string alignment, and the graph-based data models that structure complex textual variance.

### 2.1 Traditional Collation Methods and Early Automation

The endeavor to automate the collation process is nearly as old as modern computing itself. In the mid-twentieth century, scholars faced the daunting reality of comparing dozens, sometimes hundreds, of manuscript witnesses to construct a *stemma codicum* (a genealogical tree of manuscripts). Traditional manual procedures were staggeringly labor-intensive. For instance, John Manly and Edith Rickert’s monumental edition of Geoffrey Chaucer’s *Canterbury Tales* relied on a manual procedure involving thousands of physical index cards for each variant site[1]. The lemma from the base text was copied at the top of the card, followed by the variants across all witnesses and notations of missing lines or sections[1].

Early attempts at mechanical assistance included Charlton Hinman’s optical collation in the 1940s, which utilized retroprojectors to overlay printed pages to identify physical type variations[2]. By the 1960s, Dom Jacques Froger had conceptualized one of the first automated collation programs utilizing punched cards and mainframe computers, which required scholars to strip away punctuation and capitalization to accommodate hardware limitations[3]. This was followed by early software like Peter Robinson’s *Collate* and Wilhelm Ott’s *TUSTEP* in the 1980s and 1990s[3].

These early computational programs often relied on a "base text" or "pairwise" methodology, comparing witnesses one by one against a single master text[2]. While efficient for simple traditions, this approach carried inherent genealogical biases. The choice of the base text arbitrarily dictated the structure of the collation results and failed to accurately map the fluid, rhizomatic nature of manuscript transmission, where texts frequently merge, diverge, and overlap[2].

### 2.2 The Gothenburg Model

The modern architecture of automated collation was formalized in 2009 by the Interedition research project, a European initiative focused on the interoperability of tools for textual scholarship. The resulting framework is known as the "Gothenburg Model"[3]. The Gothenburg Model enforces a strict "separation of concerns" within the software architecture, breaking the collation process into five distinct, modular operations. This ensures that individual components can be upgraded or swapped without destabilizing the entire software ecosystem[3].

| Gothenburg Model Stage | Function and Mechanism |
| --- | --- |
| **Tokenization** | The division of a character sequence into minimal units (tokens), typically words. The algorithm identifies tokens based on spaces, punctuation, or specific markup tags[3]. |
| **Normalization** | The preparation of tokens for alignment by neutralizing non-significant variations (e.g., case folding, resolving scribal abbreviations, or neutralizing orthographic variance). Crucially, this does not alter the underlying archival transcription, but creates a secondary processing layer[3]. |
| **Alignment** | The algorithmic core where the engine establishes mathematical correspondences between tokens across multiple witnesses[3]. |
| **Analysis (Feedback)** | An optional interpretative stage where algorithms refine the initial alignment based on statistical or heuristic analyses, such as correcting misaligned near-matches based on semantic or phonetic proximity[3]. |
| **Output (Visualization)** | The rendering of the alignment into human-readable or machine-actionable formats, such as variant tables (CSV), Directed Acyclic Graphs (SVG/DOT), or TEI XML parallel segmentation[3]. |

### 2.3 Bioinformatic Alignment: Needleman-Wunsch and Gotoh Algorithms

The algorithmic breakthroughs that power modern text collation originated in bioinformatics, specifically in the global alignment of DNA and protein sequences. Because textual sequences (strings of words or characters) behave mathematically similarly to nucleotide sequences (strings of amino acids), computational philologists adapted these dynamic programming algorithms to identify textual homology.

#### The Needleman-Wunsch Algorithm

Developed in 1970 by Saul B. Needleman and Christian D. Wunsch, the Needleman-Wunsch algorithm is the foundational algorithm for optimal global alignment[4]. It guarantees the best possible alignment across the entire length of two sequences by dividing the large alignment problem into a series of smaller sub-problems using a dynamic programming matrix[5].

The algorithm requires a defined scoring system containing three parameters: a positive score for a "Match" (identical tokens), a negative penalty for a "Mismatch" (different tokens), and a negative penalty for an "Indel" (an insertion or deletion, where a token aligns with a gap)[5].

The algorithm constructs an O(mn) matrix, where m and n represent the lengths of the two textual sequences[5]. The matrix is populated iteratively using a recurrence relation. For sequences X and Y, the optimal score at any given cell Fi,j​ is calculated as the maximum of three possible preceding states: 

Fi,j​=max⎩⎨⎧​Fi−,j−​+S(Xi​,Yj​)Fi−,j​+dFi,j−​+d​(Match/Mismatch from diagonal)(Deletion from above)(Insertion from left)​

 where S is the substitution score and d is the gap penalty[6]. After the matrix is fully populated, a "traceback" step originates from the bottom-right cell (the end of the sequences) and follows the path of highest scores back to the top-left cell, thereby reconstructing the optimal alignment path[5].

#### The Gotoh Algorithm and Affine Gap Penalties

A critical limitation of the basic Needleman-Wunsch algorithm for textual scholarship is its linear gap penalty. A linear penalty treats a gap of ten words as ten independent, sequential omissions, penalizing the alignment equally for each word[6]. In manuscript transmission, however, a scribe is highly likely to skip an entire phrase or line at once—often due to *homoioteleuton*, a visual error where the scribe's eye skips from one similar word ending to another further down the page.

To model this biological and philological reality accurately, Osamu Gotoh (1982) introduced an optimized algorithm utilizing "affine gap penalties"[4]. The affine gap model applies a heavy penalty for *opening* a gap, but a much smaller penalty for *extending* an already open gap. The penalty W for a gap of length l is calculated as: 

W(l)=gopen​+gext​×(l−)

 This mathematical distinction accurately reflects the mechanics of scribal error, computing the omission of a ten-word phrase as a single, extended cognitive event rather than ten isolated decisions[6].

### 2.4 Data Models: The Variant Graph

While pairwise alignment (comparing Witness A strictly to Witness B) relies on two-dimensional matrices, aligning dozens of witnesses simultaneously (progressive multiple sequence alignment) requires a more sophisticated data architecture. In 2009, Desmond Schmidt and Robert Colomb proposed the "Variant Graph" to model overlapping textual hierarchies and Multi-Version Documents (MVDs)[7].

The variant graph is a Directed Acyclic Graph (DAG)[8]. It consists of Nodes (vertices) representing specific textual readings or tokens, and Edges (arcs) representing the sequence relationships[9]. The edges are labeled with the witness identifiers (sigla) that transition from one node to the next.

Every variant graph begins with a single, empty "start" node and terminates in an analogous "end" node[10]. To read a specific witness, the system traverses the graph by following the edges bearing that witness's specific siglum[10]. Crucially, because the graph is *acyclic*, it strictly prohibits backward loops. The mathematical enforcement of acyclicity preserves the linear, temporal reading order of a text, ensuring that the computational model does not generate infinite loops when rendering the document[10].

### 2.5 The Architecture of CollateX

CollateX represents the state-of-the-art implementation of the variant graph model, developed under the auspices of the Interedition project[9]. Unlike earlier tools that relied on a fixed base text, CollateX utilizes "progressive multiple alignment"[2]. The software iteratively aligns pairs of witnesses, progressively merging the results into a unified, massive variant graph[2]. When a new witness is introduced to the collation, it is aligned against the accumulated variant graph itself, rather than against a single historical witness, thereby eliminating base-text bias[2].

CollateX is deployed primarily as a Python library, which allows computational philologists to integrate the engine directly into Jupyter Notebook environments[3]. The Python implementation allows scholars to intercept the Gothenburg pipeline dynamically. Editors can inject custom tokenization scripts, generate pre-tokenized JSON structures containing dual forms (normalized strings for algorithmic matching versus original diplomatic strings for final output), and export the resulting alignment into various formats including CSV, GraphViz DOT for visual rendering, and TEI XML for digital publication[10].

## 3. Comparative Methodological Evaluation

The introduction of computational collation tools forces a methodological reckoning within the discipline. By evaluating automated approaches against traditional manual collation, distinct epistemological differences emerge, particularly regarding cognitive load, the necessity of explicit normalization, the handling of punctuation, and the treatment of complex variance such as transpositions.

### 3.1 Manual Two-Column Collation vs. CollateX Alignment

Manual collation, typically executed via two-column ledgers or annotated margins, relies heavily on the scholar's implicit, internalized knowledge. A human editor processes orthographic variation instantly, effortlessly recognizing that *scripse* and *scrisse* represent the same lexical unit, and discards this insignificant spelling difference without formally recording the algorithmic logic behind the decision[3].

However, this manual method imposes an extreme cognitive load. In massive traditions—such as the medieval Spanish legal code *Siete Partidas*, comprising approximately 100 witnesses and over 11 million words—manual collation becomes practically insurmountable and highly susceptible to fatigue-induced errors[11]. The human brain cannot hold the exact permutations of 100 witnesses simultaneously.

Automated collation with CollateX eliminates physical fatigue and ensures absolute, mathematical reproducibility. Every decision is explicit. However, computers are inherently, recalcitrantly literal. If left unconfigured, the Needleman-Wunsch algorithm will flag a capital "R" versus a lowercase "r" as a substantive, sequence-breaking variation[11]. Consequently, automated collation forces the editor to make normalization rules explicit *before* alignment begins. It shifts the critical philological labor away from the physical act of reading and comparing, redirecting it toward the act of data modeling and algorithm configuration.

### 3.2 Managing "Noise": Orthography and Levenshtein Distance

Medieval vernacular texts present severe orthographic instability. Standardized spelling did not exist; the same word may be spelled a dozen different ways across a single manuscript, let alone across a continent. When aligning un-normalized medieval texts, deterministic algorithms fragment the alignment entirely, producing highly disjointed graphs saturated with non-genealogical "noise"[3].

There are two primary computational strategies deployed within CollateX to mitigate this noise:

1. **Pre-Alignment Normalization (Dual-Token JSON):** Scholars enrich the transcription data by assigning a normalized lemma to each token prior to collation. CollateX accepts JSON input where a token possesses both an `n` (normalized) value used strictly for the alignment algorithm, and a `t` (text) value used for the final output[3]. For example, the diplomatic tokens *sança* and *sença* are both assigned the `n` value *SENZA*. The algorithm aligns them perfectly as a match, but the final output preserves the archival spelling for the user[3].
2. **Heuristic Fuzzy Matching (`near_match`):** CollateX features a built-in `near_match` parameter that evaluates tokens based on their Levenshtein (edit) distance rather than strict binary equality[3]. If the edit distance (the number of insertions, deletions, or substitutions required to change one word into another) between *legemmo* and *leggemmo* is below a defined threshold, the algorithm calculates them as a match. While significantly less labor-intensive than manual lemmatization, fuzzy matching introduces statistical risk: it may align distinct, substantive words that coincidentally share characters (e.g., *casa* and *cosa*), potentially introducing false positives into the critical apparatus[2].

### 3.3 Handling Complex Variance: Transpositions, Omissions, and Additions

The variant graph elegantly handles additions and omissions through branching pathways and gap penalties. However, *transpositions*—where a sequence of text is moved from one location in the text to an entirely different location—pose a severe mathematical challenge to the model.

Because the variant graph must remain a Directed Acyclic Graph (DAG) to preserve the linear progression of the text, mapping a transposition by drawing a literal edge backward to an earlier section of text would create a forbidden cycle[10]. An algorithm attempting to traverse a cyclic graph would become trapped in an infinite loop.

To circumvent this mathematical limitation, CollateX identifies transposed passages through secondary heuristic passes that occur *after* the primary alignment. The engine superimposes these transpositions onto the graph as unlabelled, dashed lines[10]. These dashed edges effectively treat the transposition as an added metadata layer rather than a structural component of the DAG[10]. For the digital editor, this means transpositions must often be manually audited in the resulting output, as the core algorithm inherently treats the moved text as a deletion in one location and a separate insertion in another, rather than a single, genetic scribal event.

### 3.4 Punctuation Handling

The treatment of punctuation illustrates the philosophical divide between traditional and digital methods. In early mainframe collation (e.g., Froger in 1966), punctuation was aggressively stripped from the input data to conserve memory and reduce variance noise[3].

In modern digital editing utilizing the TEI (Text Encoding Initiative) guidelines, punctuation carries semantic and historical weight. Editors must decide whether to treat punctuation as attached to the preceding word token (e.g., `word,`), which causes the algorithm to view `word` and `word,` as a mismatch, or to tokenize punctuation as entirely independent nodes in the variant graph. Tokenizing punctuation separately increases the processing time and matrix size exponentially, but allows the algorithm to align the text perfectly while isolating the punctuation variance as a distinct scribal intervention.

### 3.5 Algorithmic Alignment vs. LLM Variant Identification

An emerging, highly experimental frontier in computational philology is the integration of Large Language Models (LLMs) to identify variants and reconstruct stemmata[12]. Traditional tools like CollateX rely on deterministic dynamic programming; they possess no semantic comprehension. They align the Old French words *grant* and *grans* based solely on character overlap or pre-coded normalization dictionaries[3].

LLMs, conversely, calculate semantic proximity through high-dimensional vector embeddings. Recent benchmarking studies demonstrate that integrating LLMs to simulate text transmission can improve the identification of substantive variants by recognizing synonyms and semantic equivalents without requiring explicit manual lemmatization[12]. However, the stochastic, generative nature of LLMs currently lacks the strict mathematical reproducibility, transparency, and deterministic rigor required to produce definitive critical apparatuses. Consequently, deterministic algorithms like Needleman-Wunsch and Gotoh remain the persistent gold standard for baseline scholarly collation.

## 4. Real-World Digital Edition Case Studies

To contextualize these algorithms and methodologies, it is necessary to examine how large-scale digital editing projects implement automated collation to resolve the specific eccentricities of their respective manuscript traditions.

### 4.1 The Editio Critica Maior (ECM) and the Coherence-Based Genealogical Method

The Institut für Neutestamentliche Textforschung (INTF) in Münster utilizes automated collation at an unparalleled scale for the production of the *Editio Critica Maior* (ECM) of the Greek New Testament[13]. The New Testament represents a hyper-contaminated tradition. Scribes frequently consulted multiple exemplars simultaneously, weaving different textual lineages together into a single manuscript. Traditional Lachmannian stemmatics—which rely on identifying shared errors to build a clean family tree—fail entirely under conditions of heavy contamination.

To resolve this, the INTF developed the Coherence-Based Genealogical Method (CBGM), an approach heavily reliant on automated collation workflows and computational phylogenetic tools[13]. Using software libraries like `open-cbgm`, the ECM project parses massive TEI XML collation data (for example, analyzing 137 witnesses and 116 variation units for the Epistle of 3 John) to calculate pre-genealogical coherence between witnesses[13].

The collation data feeds directly into distance matrices, allowing advanced phylogenetic software, such as MrBayes, or clustering algorithms like Neighbor-Joining (NJ), to organize witnesses into local stemmata[13]. The CBGM navigates contamination by statistically evaluating the directionality of variants across the entire textual network, identifying manuscripts that serve as "potential ancestors" even when their texts are highly mixed[14].

### 4.2 The Canterbury Tales Project and Phylogenetic Trees

Peter Robinson's work on the *Canterbury Tales Project* marked the definitive transition from the manual index cards of Manly and Rickert to digital progressive multiple alignment[1]. The project applied evolutionary biology software to the collation data generated from dozens of Chaucerian manuscripts.

By treating textual variants as genetic mutations, the project utilized distance matrix methods and Maximum Parsimony algorithms to construct unrooted phylogenetic trees[15]. Maximum Parsimony attempts to find the genealogical tree that requires the minimum overall number of changes (mutations/scribal errors) to explain the observed textual data[15]. The automated collation output from tools like Collate provided the exact distance metrics required by the Neighbor-Joining algorithms to cluster the manuscripts into distinct families, proving that biological algorithms could accurately map human cultural transmission[15].

### 4.3 Genetic Editing: The Charles Darwin and Samuel Beckett Manuscripts

Automated collation is not strictly limited to medieval scribal transmission; it is equally vital for modern genetic editing, which traces the authorial development of a text. Projects dealing with the Charles Darwin Manuscripts (e.g., *The Origin of Species*) and the Beckett Digital Manuscript Project utilize CollateX to map authorial revisions across multiple drafts[16].

Unlike scribal copies, authorial drafts represent "layers" of revision within the same document[16]. By treating each revision campaign as a distinct "witness" and passing them through CollateX, editors can automatically compute the differences between intra-document layers[16]. The variant graph successfully models these overlapping hierarchies, allowing the digital interface to render heat-maps or "aligned barcodes" that visually highlight the exact passages Darwin or Beckett expanded, deleted, or transposed between editions[7].

### 4.4 Scaling to Millions of Words: The *Siete Partidas* and *Fuero Juzgo*

The *Siete Partidas* of Alfonso X the Wise represents one of the most imposing editing challenges in medieval Iberian scholarship. The tradition comprises approximately 100 witnesses containing over 11 million words, with complex conflations across both manuscript and early printed editions[11].

In the *7PartidasDigital* project, José Manuel Fradejas Rueda highlights the absolute necessity of programmatic workflows over manual labor. Initial attempts to manually collate the texts using Excel color-coding proved unsustainable. By implementing Python scripts that pipeline tokenized transcriptions directly into CollateX, the project fully automated the alignment[11]. Crucially, Fradejas Rueda utilized CollateX's `near_match` function to minimize orthographic noise (e.g., instructing the algorithm to ignore the difference between *rOmeros* and *romeros*). This enabled the scholarly team to focus exclusively on substantive morphosyntactic and lexical variants. The output was exported to CSV for manual adjudication, allowing the team to detect subtle linguistic retrogressions between the 1491 and 1555 printed editions that a manual reading would have entirely missed[11].

Similarly, in analyzing the Old Spanish *Fuero Juzgo*, Charles Mabille evaluated multiple tools—Juxta, CollateX, Stemmaweb, and TRAViz—to establish a *stemma codicum* for 42 witnesses[2]. Mabille found that while Juxta provided intuitive visual heat-maps, its reliance on a fixed base-text and its inability to handle pre-alignment normalization rendered it largely useless for discovering overarching genealogical relationships[2]. Stemmaweb’s phylogenetic Neighbor-Joining tree provided a broad, useful overview of witness distances, but failed to adequately process user annotations distinguishing orthographic from substantive variants[2]. Ultimately, CollateX's Python implementation proved to be the only viable engine. It allowed for JSON-based pre-alignment normalization and produced a CSV matrix that could be manually refined by the editor for rigorous *recensio*[2].

## 5. Pedagogical Takeaways & Synthesis for Digital Editors

For undergraduate curricula in digital humanities, computational philology must be taught not merely as a set of technical skills, but as an epistemological framework. Students must understand that algorithms do not replace editorial judgment; they restructure it. The following provides a pedagogical synthesis for executing automated collation via CollateX and establishing a rigorous variant taxonomy.

### 5.1 Step-by-Step CollateX Python Tutorial

To teach progressive multiple alignment, students should utilize Jupyter Notebooks. This environment allows them to integrate executable Python code directly with markdown documentation, facilitating a transparent, reproducible workflow[17].

**Step 1: Preparation and Tokenization (The JSON Structure)** CollateX readily accepts raw plain text, but for historical languages, students must be trained to construct JSON objects containing both the original diplomatic transcription (`t`) and the normalized lemma (`n`).

JSON

```
{
 "witnesses": [
 {
 "id": "Wit_A",
 "tokens": [
 {"t": "Grant", "n": "grant"},
 {"t": "fu", "n": "estre"},
 {"t": "la", "n": "le"},
 {"t": "ioie", "n": "joie"}
 ]
 },
 {
 "id": "Wit_B",
 "tokens": [
 {"t": "grans", "n": "grant"},
 {"t": "fu", "n": "estre"},
 {"t": "la", "n": "le"},
 {"t": "joie", "n": "joie"}
 ]
 }
 ]
}
```

**Step 2: Execution in Python** Using the CollateX Python library, the JSON payload is parsed and passed to the alignment engine. Students should experiment with the `near_match` parameter to observe how Levenshtein distance thresholds drastically alter the complexity of the alignment graph.

Python

```
from collatex import *
import json

# Load the normalized JSON data
with open('witnesses.json') as f:
 data = json.load(f)

# Initialize the Collation object and iterate through witnesses
collation = Collation()
for witness in data['witnesses']:
 collation.add_witness(witness)

# Execute the alignment algorithm
# Setting near_match=False forces reliance on the 'n' (normalized) JSON values
alignment = collate(collation, output='html', near_match=False)
```

**Step 3: Exporting to TEI Parallel Segmentation** A critical pedagogical outcome is understanding data interoperability. CollateX can export the variant graph directly into TEI XML using the parallel segmentation method. This standard output wraps variants in `<app>` (apparatus), `<rdg>` (reading), and `<lem>` (lemma) tags, rendering the data ready for publication or ingest into tools like the TEI Critical Apparatus Toolbox.

Python

```
tei_output = collate(collation, output='tei')
print(tei_output)
```

*Output:*

XML

```
<app>
 <rdg wit="#Wit_A">Grant</rdg>
 <rdg wit="#Wit_B">grans</rdg>
</app>
<app>
 <rdg wit="#Wit_A #Wit_B">fu la</rdg>
</app>
<app>
 <rdg wit="#Wit_A">ioie</rdg>
 <rdg wit="#Wit_B">joie</rdg>
</app>
```

### 5.2 Variant Taxonomy Classification Guide

Once the collation table or graph is generated, students must be trained to critically adjudicate the results. Algorithmic output is inherently agnostic; it contains all deviations, regardless of importance. The human editor must classify these deviations to determine their stemmatic relevance[2].

| Taxonomy Tier | Description | Algorithmic Treatment | Stemmatic Value |
| --- | --- | --- | --- |
| **Orthographic / Graphematic** | Spelling variations (e.g., *sança* vs. *sença*, *ioie* vs. *joie*). | Creates massive noise in the matrix. Must be neutralized via pre-alignment `n` (lemma) targeting or `near_match` fuzzy logic[3]. | Generally polygenetic; highly limited value for establishing genetic relationships. |
| **Morphological** | Variations in word form (e.g., singular vs. plural, verb tense shifts). | Identifiable if pre-normalized by part-of-speech (POS) taggers prior to CollateX alignment[3]. | Moderate. May reveal regional scribal habits or systemic linguistic updates over time. |
| **Lexical Substitution** | Complete word replacements (e.g., *alcalde* vs. *juez*). | CollateX will flag these as distinct, divergent nodes in the variant graph[18]. | High. If shared across multiple witnesses, it strongly indicates a shared exemplar (a conjunctive error or innovation). |
| **Omissions / Homoioteleuton** | Missing blocks of text. | Represented as empty paths traversing the DAG. Computed mathematically using Gotoh affine gap penalties[4]. | Very High. Long, inexplicable omissions are powerful indicators of genetic descent. |
| **Transpositions** | Text moved to a completely different location in the document. | DAG models fundamentally reject backward cycles. CollateX identifies them post-alignment and superimposes them as dashed, unlabelled edges[10]. | High. Indicates deliberate scribal intervention, editorial restructuring, or the physical misarrangement of folios. |

By mastering this taxonomy, student editors learn that automated collation does not do the philological work for them. Rather, it provides a perfectly structured, mathematically sound dataset upon which rigorous textual criticism can be performed. The transition from manual reading to algorithmic alignment represents the maturation of digital humanities—moving beyond mere digitization into a highly analytical, computational science.

## 6. Comprehensive Academic & Technical References Synthesis

To fully grasp the trajectory of computational philology, scholars must engage with a diverse corpus of literature that bridges evolutionary biology, computer science, and traditional manuscript studies. This synthesis details the primary foundational texts and digital tools that inform modern collation workflows.

The algorithmic bedrock of sequence alignment rests upon Needleman and Wunsch’s (1970) seminal paper on dynamic programming[5], heavily refined by Gotoh’s (1982) introduction of affine gap penalties, which provided the mathematical flexibility required to model both biological mutations and human scribal omissions accurately[4]. The translation of these bioinformatic principles into a viable data architecture for textual scholarship was achieved by Schmidt and Colomb (2009), whose conceptualization of the variant graph as a Directed Acyclic Graph (DAG) resolved the longstanding issue of overlapping textual hierarchies[7].

The practical implementation of these algorithms is detailed extensively by Haentjens Dekker and Middell (2011), who articulate the architecture of CollateX and the formulation of the Gothenburg Model, establishing the modular paradigm (tokenization, normalization, alignment) that dominates contemporary workflows[9]. Subsequent research by Haentjens Dekker et al. (2015) demonstrates the application of these tools to modern genetic editing, specifically tracking authorial revisions in the Samuel Beckett Digital Manuscript Project[16].

For the integration of phylogenetic analysis into textual criticism, Howe et al. (2012) provide a critical defense of evolutionary methods, detailing how algorithms like Neighbor-Joining and Maximum Parsimony—utilized extensively in the *Canterbury Tales Project*—can accurately construct unrooted stemmata from collation distance matrices[15]. The scaling of these methods is exemplified by the Institut für Neutestamentliche Textforschung (INTF) and their development of the Coherence-Based Genealogical Method (CBGM) for the *Editio Critica Maior* (ECM), which relies on `open-cbgm` libraries to parse TEI XML data and resolve hyper-contamination[13].

Finally, the practical, linguistic challenges of applying these tools to medieval vernaculars are deeply explored by Fradejas Rueda (2022), who demonstrates the necessity of Python pipelining and fuzzy matching when processing the 11-million-word corpus of the *Siete Partidas*[11]. Similarly, Nury and Spadini (2020) and Mabille (2023) offer vital comparative evaluations, utilizing tools like PyCoviz to visualize variant graphs, proving that while algorithms can perfectly align character strings, the epistemological burden of defining and interpreting textual variance ultimately remains with the human scholar[2].

Sources used in the report
[boris-portal.unibe.ch

From giant despair to a new heaven: The early years of automatic collation - BORIS Portal

 Opens in a new window](https://boris-portal.unibe.ch/server/api/core/bitstreams/ccc28b82-7096-4f49-a355-d37fa1428ec3/content)

05_Risorse_e_sfide_per_la_collazione_automatica_di_testi_medievali.pdf

04_Automated_collation_and_digital_editions_From_theory_to_practice.pdf

[journals.openedition.org

Visualizing Collation Results - OpenEdition Journals

 Opens in a new window](https://journals.openedition.org/variants/950?lang=fr)[pure.knaw.nl

Royal Netherlands Academy of Arts and Sciences (KNAW)

 Opens in a new window](https://pure.knaw.nl/ws/files/799786159/Computer_supported_collation_with_CollateX_haentjens_dekker_middell.pdf)[researchgate.net

Intra-language Text Alignment Using iAligner - Proceedings, 7th International Conference of Digital Archives and Digital Humanities: December 1-3, 2016 National Taiwan University - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/326490273_Intra-language_Text_Alignment_Using_iAligner_-_Proceedings_7th_International_Conference_of_Digital_Archives_and_Digital_Humanities_December_1-3_2016_National_Taiwan_University)[researchgate.net

Computer-supported collation of modern manuscripts: CollateX and the Beckett Digital Manuscript Project | Request PDF - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/270752678_Computer-supported_collation_of_modern_manuscripts_CollateX_and_the_Beckett_Digital_Manuscript_Project)[kclpure.kcl.ac.uk

This electronic thesis or dissertation has been downloaded from the King's Research Portal at https://kclpure.kcl.ac.uk/portal

 Opens in a new window](https://kclpure.kcl.ac.uk/ws/files/105283803/2018_Nury_Elisa_1337422_ethesis.pdf)[dokumen.pub

Genetics Vol 1 & 2 First Edition - DOKUMEN.PUB

 Opens in a new window](https://dokumen.pub/genetics-vol-1-2-first-edition.html)[en.wikipedia.org

Needleman–Wunsch algorithm - Wikipedia

 Opens in a new window](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm)[open.oregonstate.education

Chapter 3: Sequence Alignments – Applied Bioinformatics - Open Educational Resources

 Opens in a new window](https://open.oregonstate.education/appliedbioinformatics/chapter/chapter-3/)[pmc.ncbi.nlm.nih.gov

Developments in Algorithms for Sequence Alignment: A Review - PMC

 Opens in a new window](https://pmc.ncbi.nlm.nih.gov/articles/PMC9024764/)[ebi.ac.uk

Computational Analysis of Protein Function within Complete Genomes Anton James Enright - EMBL-EBI

 Opens in a new window](https://www.ebi.ac.uk/sites/ebi.ac.uk/files/shared/documents/phdtheses/antonenrightthesis.pdf)[bio.libretexts.org

2.5: The Needleman-Wunsch Algorithm - Biology LibreTexts

 Opens in a new window](https://bio.libretexts.org/Bookshelves/Computational_Biology/Book%3A_Computational_Biology_-_Genomes_Networks_and_Evolution_(Kellis_et_al.)/02%3A_Sequence_Alignment_and_Dynamic_Programming/2.05%3A_The_Needleman-Wunsch_Algorithm)[dokumen.pub

Bioinformatics and Molecular Evolution 1405106832, 9781405106832, 1444311182, 9781444311181 - DOKUMEN.PUB

 Opens in a new window](https://dokumen.pub/bioinformatics-and-molecular-evolution-1405106832-9781405106832-1444311182-9781444311181.html)[computer.org

A Survey of Text Alignment Visualization - IEEE Computer Society

 Opens in a new window](https://www.computer.org/csdl/journal/tg/2021/02/09220137/1nRLN0fSuiI)[balisage.net

Balisage Paper: Merging Multi-Version Texts: a General Solution to the Overlap Problem

 Opens in a new window](https://www.balisage.net/Proceedings/vol3/html/Schmidt01/BalisageVol3-Schmidt01.html)[academic.oup.com

Graph schema validation at last? Work towards a StemmaREST ontology with Neo4J, RDF-STAR, and SHACL | Digital Scholarship in the Humanities | Oxford Academic

 Opens in a new window](https://academic.oup.com/dsh/article/41/Supplement_1/i3/8213722)[pure.knaw.nl

Computer-supported collation of modern manuscripts: CollateX and the Beckett Digital Manuscript Project - Royal Netherlands Academy of Arts and Sciences (KNAW)

 Opens in a new window](https://pure.knaw.nl/ws/files/797964/BDMP_Collatex_LLC_article_2013_05_24_submitted_20130529.pdf)[researchgate.net

(PDF) TRAViz: A visualization for Variant Graphs - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/282156951_TRAViz_A_visualization_for_Variant_Graphs)[github.com

Materials/session7/Session07b_Normalization.ipynb at master

 Opens in a new window](https://github.com/automaticCollationLausanne2020/Materials/blob/master/session7/Session07b_Normalization.ipynb)

07_3.3_Transcription_and_collation.pdf

[researchgate.net

Towards generating a stemma of complicated manuscript traditions: Petrus Alfonsi's Dialogus | Request PDF - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/280810610_Towards_generating_a_stemma_of_complicated_manuscript_traditions_Petrus_Alfonsi's_Dialogus)[github.com

jjmccollum/open-cbgm: Fast, compact, open-source, TEI-compliant C++ implementation of the Coherence-Based Genealogical Method - GitHub

 Opens in a new window](https://github.com/jjmccollum/open-cbgm)[brill.com

Three Direct Copies and Other Closely Related Manuscripts of the Pauline Epistles in - Brill

 Opens in a new window](https://brill.com/view/journals/nt/65/3/article-p381_6.xml)[researchgate.net

Responding to Criticisms of Phylogenetic Methods in Stemmatology - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/254962929_Responding_to_Criticisms_of_Phylogenetic_Methods_in_Stemmatology)[dspace.est.edu.br

MÉTODO GENEALÓGICO BASEADO NA COERÊNCIA: POTENCIALIDADES E FRAGILIDADES - Faculdades EST

 Opens in a new window](http://dspace.est.edu.br:8080/jspui/bitstream/BR-SlFE/1113/1/casagrande_w_td242.pdf)[dokumen.pub

The Journal of the European Society for Textual Scholarship [1 ed.] 9789401209021, 9789042036321 - DOKUMEN.PUB

 Opens in a new window](https://dokumen.pub/the-journal-of-the-european-society-for-textual-scholarship-1nbsped-9789401209021-9789042036321.html)[collatex.obdurodon.org

Computer-supported collation with CollateX

 Opens in a new window](https://collatex.obdurodon.org/)[academic.oup.com

From print to digital: A web edition of Giacomo Leopardi's Idilli - Oxford Academic

 Opens in a new window](https://academic.oup.com/dsh/article/36/Supplement_1/i23/5828480)[ride.i-d-e.de

Juxta Web Service, LERA, and Variance Viewer. Web based collation tools for TEI - RIDE

 Opens in a new window](https://ride.i-d-e.de/issues/issue-11/web-based-collation-tools/)[journals.openedition.org

Medieval Glosses as a Test Subject for the Building of Tools for Digital Critical Editions

 Opens in a new window](https://journals.openedition.org/jtei/3544)[kups.ub.uni-koeln.de

Digital Scholarly Editions as Interfaces

 Opens in a new window](https://kups.ub.uni-koeln.de/9085/1/SIDE_12_digital_scholarly_editions_as_interfaces.pdf)
Sources read but not used in the report
[researchgate.net

(PDF) From graveyard to graph: Visualisation of textual collation in a digital paradigm

 Opens in a new window](https://www.researchgate.net/publication/333883455_From_graveyard_to_graph_Visualisation_of_textual_collation_in_a_digital_paradigm)[scribd.com

Visual Text Analysis in Digital Humanities | PDF - Scribd

 Opens in a new window](https://www.scribd.com/document/556427015/Visual-text-analysis-in-digital-humanities)[dh-abstracts.library.virginia.edu

An Interactive Interface for Text Variant Graph Models - The Index of Digital Humanities Conferences

 Opens in a new window](https://dh-abstracts.library.virginia.edu/works/1707)[inria.hal.science

Neural Approaches to Historical Word Reconstruction - HAL-Inria

 Opens in a new window](https://inria.hal.science/tel-04505549v1/file/thesis.pdf)[researchgate.net

Multi-GPU Approach for Large-Scale Multiple Sequence Alignment - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/354488296_Multi-GPU_Approach_for_Large-Scale_Multiple_Sequence_Alignment)[arxiv.org

string2string Studio: An Interactive, In-Browser Platform for String-to-String Algorithms - arXiv

 Opens in a new window](https://arxiv.org/pdf/2608.03984)[researchgate.net

Performance dependency on number of threads and query length for global... - ResearchGate

 Opens in a new window](https://www.researchgate.net/figure/Performance-dependency-on-number-of-threads-and-query-length-for-global-alignments-The_fig2_293808254)[dokumen.pub

Understanding Bioinformatics [1 ed.] 0-8153-4024-9, 978-0-8153-4024-9 - DOKUMEN.PUB

 Opens in a new window](https://dokumen.pub/understanding-bioinformatics-1nbsped-0-8153-4024-9-978-0-8153-4024-9.html)[researchgate.net

(PDF) Developments in Algorithms for Sequence Alignment: A Review - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/359771650_Developments_in_Algorithms_for_Sequence_Alignment_A_Review)[imada.sdu.dk

Improving the Layout for Text Variant Graphs - IMADA

 Opens in a new window](https://imada.sdu.dk/~stjaenicke/data/papers/Improving_the_Layout_for_Text_Variant_Graphs.pdf)[kups.ub.uni-koeln.de

Graph Data-Models and Semantic Web Technologies in Scholarly Digital Editing

 Opens in a new window](https://kups.ub.uni-koeln.de/54577/1/side15.pdf)[cst.dk

TwinTalks at DHN 2018 – Understanding Collaboration in Digital Humanities

 Opens in a new window](https://cst.dk/DHN2019Pro/TwinTalksWorkshopProceedings.pdf)[wiki.tei-c.org

Critical Apparatus Workgroup - TEIWiki - Text Encoding Initiative

 Opens in a new window](https://wiki.tei-c.org/index.php/Critical_Apparatus_Workgroup)[academia.edu

A digital critical edition model for Priscian: glosses, graeca, quotations - Academia.edu

 Opens in a new window](https://www.academia.edu/39836638/A_digital_critical_edition_model_for_Priscian_glosses_graeca_quotations)[raw.githubusercontent.com

Juxta Web Service, LERA, and Variance Viewer. Web ... - GitHub

 Opens in a new window](https://raw.githubusercontent.com/i-d-e/ride/master/issues/issue11/collationtools/collationtools.pdf)[youtube.com

Understanding Sequence Alignment Algorithms: with Needleman-Wunsch - YouTube

 Opens in a new window](https://www.youtube.com/watch?v=b6xBvl0yPAY)[grokipedia.com

Recension - Grokipedia

 Opens in a new window](https://grokipedia.com/page/Recension)[researchgate.net

3: Liniamentis in the collation results. | Download Scientific Diagram

 Opens in a new window](https://www.researchgate.net/figure/Liniamentis-in-the-collation-results_fig2_334395640)[researchgate.net

Elisa NURY | Research scientist | University of Geneva, Genève | UNIGE | Department of Antiquity - ResearchGate

 Opens in a new window](https://www.researchgate.net/profile/Elisa-Nury)
Thoughts

Reviewing Core Collation Frameworks

I am synthesizing the core principles of automated textual collation and alignment, specifically examining the Gothenburg Model's multi-stage pipeline—tokenization, normalization, alignment, feedback, and visualization. Through assessing historical textual scholarly workflows, I am comparing manual spreadsheet-based comparisons against deterministic variant graph models used in computational philology tools like CollateX and Juxta.

Evaluating Algorithmic vs. Generative Alignment

I am analyzing dynamic programming algorithms, specifically Needleman-Wunsch and Gotoh alignment, to evaluate how exact match scoring and affine gap penalties handle complex textual mutations such as transpositions, substitutions, and omissions. I am also identifying critical gaps regarding how generative LLMs compare against these deterministic graph-based models in terms of hallucination risks, reproducibility, and handling raw manuscript variations.

Investigating Case Studies and Tooling

I am planning targeted searches across historical digital humanities projects—including the New Testament Editio Critica Maior, the Canterbury Tales Project, the Fuero Juzgo, and 7Partidas Digital—to examine real-world implementations of the Coherence-Based Genealogical Method and automated collation. Next, I will gather technical specifics on the CollateX Python API and recent scholarly evaluations comparing LLMs with deterministic variant graphs.

[academic.oup.com

Graph schema validation at last? Work towards a StemmaREST ontology with Neo4J, RDF-STAR, and SHACL | Digital Scholarship in the Humanities | Oxford Academic](https://academic.oup.com/dsh/article/41/Supplement_1/i3/8213722)[researchgate.net

(PDF) From graveyard to graph: Visualisation of textual collation in a digital paradigm](https://www.researchgate.net/publication/333883455_From_graveyard_to_graph_Visualisation_of_textual_collation_in_a_digital_paradigm)[scribd.com

Visual Text Analysis in Digital Humanities | PDF - Scribd](https://www.scribd.com/document/556427015/Visual-text-analysis-in-digital-humanities)[pure.knaw.nl

Royal Netherlands Academy of Arts and Sciences (KNAW)](https://pure.knaw.nl/ws/files/799786159/Computer_supported_collation_with_CollateX_haentjens_dekker_middell.pdf)[kclpure.kcl.ac.uk

This electronic thesis or dissertation has been downloaded from the King's Research Portal at https://kclpure.kcl.ac.uk/portal](https://kclpure.kcl.ac.uk/ws/files/105283803/2018_Nury_Elisa_1337422_ethesis.pdf)[dh-abstracts.library.virginia.edu

An Interactive Interface for Text Variant Graph Models - The Index of Digital Humanities Conferences](https://dh-abstracts.library.virginia.edu/works/1707)[researchgate.net

Computer-supported collation of modern manuscripts: CollateX and the Beckett Digital Manuscript Project | Request PDF - ResearchGate](https://www.researchgate.net/publication/270752678_Computer-supported_collation_of_modern_manuscripts_CollateX_and_the_Beckett_Digital_Manuscript_Project)[collatex.obdurodon.org

Computer-supported collation with CollateX](https://collatex.obdurodon.org/)[pure.knaw.nl

Computer-supported collation of modern manuscripts: CollateX and the Beckett Digital Manuscript Project - Royal Netherlands Academy of Arts and Sciences (KNAW)](https://pure.knaw.nl/ws/files/797964/BDMP_Collatex_LLC_article_2013_05_24_submitted_20130529.pdf)

Mapping Algorithmic and Structural Frameworks

I am examining the mathematical and structural mechanics underlying modern textual collation systems. My focus is on detailing how dynamic programming techniques—specifically pairwise sequence alignment and affine gap penalty adjustments—are adapted from bioinformatics to align textual versions. Simultaneously, I am evaluating directed acyclic graph structures to formalize how multi-witness variants, start and end anchor nodes, and complex transpositions are modeled within specialized alignment engines.

Evaluating Collation Paradigms and Failure Modes

I am synthesizing comparative analyses across manual workflows, deterministic graph-based alignment, and emerging large language model approaches. I am particularly interested in categorizing how each method handles specific textual phenomena such as homoioteleuton lacunae, word transpositions, and orthographic noise. Through this comparison, I am examining the operational boundaries of generative models, focusing on non-deterministic behavior, positioning errors across extensive manuscript traditions, and high compute overhead versus the deterministic guarantees of mathematical graph models.

Investigating Large-Scale Scholarly Implementations

I am gathering fine-grained details on prominent digital humanities projects to demonstrate real-world collation architectures. This includes investigating the genealogical coherence methods applied to the Greek New Testament, the multi-edition variant tracking in historical scientific texts, and the workflow pipelines that integrate automated handwritten text recognition with part-of-speech lemmatization for medieval vernacular traditions.

Targeting Deep-Dive Technical Searches

I am planning targeted searches to gather exact mathematical formulations for alignment scoring matrices, precise algorithmic steps for genealogical coherence calculations, and specific implementation patterns for scripted collation pipelines. These searches will ensure the technical and code-level components of the research are fully articulated.

[dokumen.pub

Bioinformatics and Molecular Evolution 1405106832, 9781405106832, 1444311182, 9781444311181 - DOKUMEN.PUB](https://dokumen.pub/bioinformatics-and-molecular-evolution-1405106832-9781405106832-1444311182-9781444311181.html)[pmc.ncbi.nlm.nih.gov

Developments in Algorithms for Sequence Alignment: A Review - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9024764/)[inria.hal.science

Neural Approaches to Historical Word Reconstruction - HAL-Inria](https://inria.hal.science/tel-04505549v1/file/thesis.pdf)[researchgate.net

Multi-GPU Approach for Large-Scale Multiple Sequence Alignment - ResearchGate](https://www.researchgate.net/publication/354488296_Multi-GPU_Approach_for_Large-Scale_Multiple_Sequence_Alignment)[arxiv.org

string2string Studio: An Interactive, In-Browser Platform for String-to-String Algorithms - arXiv](https://arxiv.org/pdf/2608.03984)[researchgate.net

Performance dependency on number of threads and query length for global... - ResearchGate](https://www.researchgate.net/figure/Performance-dependency-on-number-of-threads-and-query-length-for-global-alignments-The_fig2_293808254)[dokumen.pub

Understanding Bioinformatics [1 ed.] 0-8153-4024-9, 978-0-8153-4024-9 - DOKUMEN.PUB](https://dokumen.pub/understanding-bioinformatics-1nbsped-0-8153-4024-9-978-0-8153-4024-9.html)[researchgate.net

(PDF) Developments in Algorithms for Sequence Alignment: A Review - ResearchGate](https://www.researchgate.net/publication/359771650_Developments_in_Algorithms_for_Sequence_Alignment_A_Review)[ebi.ac.uk

Computational Analysis of Protein Function within Complete Genomes Anton James Enright - EMBL-EBI](https://www.ebi.ac.uk/sites/ebi.ac.uk/files/shared/documents/phdtheses/antonenrightthesis.pdf)[dokumen.pub

Genetics Vol 1 & 2 First Edition - DOKUMEN.PUB](https://dokumen.pub/genetics-vol-1-2-first-edition.html)[github.com

jjmccollum/open-cbgm: Fast, compact, open-source, TEI-compliant C++ implementation of the Coherence-Based Genealogical Method - GitHub](https://github.com/jjmccollum/open-cbgm)[dspace.est.edu.br

MÉTODO GENEALÓGICO BASEADO NA COERÊNCIA: POTENCIALIDADES E FRAGILIDADES - Faculdades EST](http://dspace.est.edu.br:8080/jspui/bitstream/BR-SlFE/1113/1/casagrande_w_td242.pdf)[brill.com

Three Direct Copies and Other Closely Related Manuscripts of the Pauline Epistles in - Brill](https://brill.com/view/journals/nt/65/3/article-p381_6.xml)[dokumen.pub

The Journal of the European Society for Textual Scholarship [1 ed.] 9789401209021, 9789042036321 - DOKUMEN.PUB](https://dokumen.pub/the-journal-of-the-european-society-for-textual-scholarship-1nbsped-9789401209021-9789042036321.html)

Mapping Graph Topologies and Affine Penalties

I am formalizing the mathematical mechanics of string alignment algorithms, contrasting linear gap scoring with Gotoh's affine gap penalty recurrences to model structural text insertions and deletions. Simultaneously, I am evaluating variant graph data models—focusing on vertex token representations, directed witness sigla edges, and topological ranking constraints—to determine how non-sequential transposition links disrupt standard directed acyclic graph structures during multi-text collation.

Contrasting Deterministic Graphs with Probabilistic LLMs

I am resolving key methodology tradeoffs between deterministic graph algorithms and generative large language models. While LLMs offer contextual semantic awareness, they struggle with high inference costs, token alignment drift across large manuscript traditions, and non-deterministic hallucinations. In contrast, graph-based collation models adhere strictly to reproducible pipeline architectures like the Gothenburg model, ensuring auditable witness attribution across hundreds of complex historical text sources.

Integrating Historical Case Studies and Execution Pipelines

I am preparing to detail real-world implementations, such as the Editio Critica Maior's Coherence-Based Genealogical Method and the Canterbury Tales Project, alongside legal codices like the Fuero Juzgo and 7Partidas Digital. Moving forward, I will finalize a step-by-step technical tutorial covering API-level collation and normalization routines, construct an undergraduate variant taxonomy guide, and gather final technical specifications on graph-matching algorithms.

[kclpure.kcl.ac.uk

This electronic thesis or dissertation has been downloaded from the King's Research Portal at https://kclpure.kcl.ac.uk/portal](https://kclpure.kcl.ac.uk/ws/files/105283803/2018_Nury_Elisa_1337422_ethesis.pdf)[researchgate.net

(PDF) TRAViz: A visualization for Variant Graphs - ResearchGate](https://www.researchgate.net/publication/282156951_TRAViz_A_visualization_for_Variant_Graphs)[balisage.net

Balisage Paper: Merging Multi-Version Texts: a General Solution to the Overlap Problem](https://www.balisage.net/Proceedings/vol3/html/Schmidt01/BalisageVol3-Schmidt01.html)[imada.sdu.dk

Improving the Layout for Text Variant Graphs - IMADA](https://imada.sdu.dk/~stjaenicke/data/papers/Improving_the_Layout_for_Text_Variant_Graphs.pdf)[pure.knaw.nl

Computer-supported collation of modern manuscripts: CollateX and the Beckett Digital Manuscript Project - Royal Netherlands Academy of Arts and Sciences (KNAW)](https://pure.knaw.nl/ws/files/797964/BDMP_Collatex_LLC_article_2013_05_24_submitted_20130529.pdf)[computer.org

A Survey of Text Alignment Visualization - IEEE Computer Society](https://www.computer.org/csdl/journal/tg/2021/02/09220137/1nRLN0fSuiI)[boris-portal.unibe.ch

From giant despair to a new heaven: The early years of automatic collation - BORIS Portal](https://boris-portal.unibe.ch/server/api/core/bitstreams/ccc28b82-7096-4f49-a355-d37fa1428ec3/content)[kups.ub.uni-koeln.de

Graph Data-Models and Semantic Web Technologies in Scholarly Digital Editing](https://kups.ub.uni-koeln.de/54577/1/side15.pdf)[academic.oup.com

From print to digital: A web edition of Giacomo Leopardi's Idilli - Oxford Academic](https://academic.oup.com/dsh/article/36/Supplement_1/i23/5828480)[researchgate.net

Intra-language Text Alignment Using iAligner - Proceedings, 7th International Conference of Digital Archives and Digital Humanities: December 1-3, 2016 National Taiwan University - ResearchGate](https://www.researchgate.net/publication/326490273_Intra-language_Text_Alignment_Using_iAligner_-_Proceedings_7th_International_Conference_of_Digital_Archives_and_Digital_Humanities_December_1-3_2016_National_Taiwan_University)[researchgate.net

Computer-supported collation of modern manuscripts: CollateX and the Beckett Digital Manuscript Project | Request PDF - ResearchGate](https://www.researchgate.net/publication/270752678_Computer-supported_collation_of_modern_manuscripts_CollateX_and_the_Beckett_Digital_Manuscript_Project)

Historical Roots of Variant Graphs

I am examining the historical development of graph data structures in scholarly editing, discovering that variant graphs trace back to early biblical textual criticism models from 1964 before being formalised into modern directed acyclic graph frameworks. I am analyzing how this model abstracts multi-version document variations—such as insertions, omissions, and overlapping hierarchies—into explicit start and end anchor nodes, edge-weight mappings for witness sigla, and topological rank calculations that permit flexible side-by-side comparative views.

Visualization and Layout Innovations

I am evaluating visualization rules designed to reduce cognitive load and visual clutter in large-scale collation layouts. My focus is on how contemporary tools address edge-crossing and vertex-labeling challenges by removing backward edges, utilizing color-coded edge bundling, and applying varying vertex font sizes to clearly communicate variant frequencies without disrupting reading order across complex manuscript families.

Targeting Dynamic Programming Recurrences

I am planning targeted searches to gather exact dynamic programming recurrences for affine gap penalty matrices and specific TEI XML parallel segmentation encoding patterns. These steps will ensure the mathematical formulations and practical implementation tutorials for scripted alignment pipelines are fully articulated.

[kups.ub.uni-koeln.de

Digital Scholarly Editions as Interfaces](https://kups.ub.uni-koeln.de/9085/1/SIDE_12_digital_scholarly_editions_as_interfaces.pdf)[kups.ub.uni-koeln.de

Graph Data-Models and Semantic Web Technologies in Scholarly Digital Editing](https://kups.ub.uni-koeln.de/54577/1/side15.pdf)[kclpure.kcl.ac.uk

This electronic thesis or dissertation has been downloaded from the King's Research Portal at https://kclpure.kcl.ac.uk/portal](https://kclpure.kcl.ac.uk/ws/files/105283803/2018_Nury_Elisa_1337422_ethesis.pdf)[cst.dk

TwinTalks at DHN 2018 – Understanding Collaboration in Digital Humanities](https://cst.dk/DHN2019Pro/TwinTalksWorkshopProceedings.pdf)[ride.i-d-e.de

Juxta Web Service, LERA, and Variance Viewer. Web based collation tools for TEI - RIDE](https://ride.i-d-e.de/issues/issue-11/web-based-collation-tools/)[wiki.tei-c.org

Critical Apparatus Workgroup - TEIWiki - Text Encoding Initiative](https://wiki.tei-c.org/index.php/Critical_Apparatus_Workgroup)[journals.openedition.org

Medieval Glosses as a Test Subject for the Building of Tools for Digital Critical Editions](https://journals.openedition.org/jtei/3544)[academia.edu

A digital critical edition model for Priscian: glosses, graeca, quotations - Academia.edu](https://www.academia.edu/39836638/A_digital_critical_edition_model_for_Priscian_glosses_graeca_quotations)[raw.githubusercontent.com

Juxta Web Service, LERA, and Variance Viewer. Web ... - GitHub](https://raw.githubusercontent.com/i-d-e/ride/master/issues/issue11/collationtools/collationtools.pdf)[en.wikipedia.org

Needleman–Wunsch algorithm - Wikipedia](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm)[open.oregonstate.education

Chapter 3: Sequence Alignments – Applied Bioinformatics - Open Educational Resources](https://open.oregonstate.education/appliedbioinformatics/chapter/chapter-3/)[bio.libretexts.org

2.5: The Needleman-Wunsch Algorithm - Biology LibreTexts](https://bio.libretexts.org/Bookshelves/Computational_Biology/Book%3A_Computational_Biology_-_Genomes_Networks_and_Evolution_(Kellis_et_al.)/02%3A_Sequence_Alignment_and_Dynamic_Programming/2.05%3A_The_Needleman-Wunsch_Algorithm)[youtube.com

Understanding Sequence Alignment Algorithms: with Needleman-Wunsch - YouTube](https://www.youtube.com/watch?v=b6xBvl0yPAY)

Examining Encoding Standards and Matrix Recursion

I am analyzing TEI XML parallel segmentation schemas, focusing on how apparatus elements like reading and lemma tags model inline textual variants without requiring external standoff markup. Simultaneously, I am working through the exact matrix recursion steps and traceback logic of the Needleman-Wunsch dynamic programming algorithm to formalize how global pairwise alignments compute optimal paths across scoring matrices.

Addressing Structural Constraints in Apparatus Markup

I am resolving structural limitations inherent in XML-based textual apparatuses, particularly conflicts where phrase-level variant containers struggle to encapsulate larger structural units like full paragraphs. I am also investigating how automated collation exports bridge the gap between graph-based internal alignments and standard TEI XML markup formats while preserving complex manuscript readings.

Refining Algorithmic Fuzzy Matching Parameters

I am planning targeted searches to gather specific implementation details on fuzzy matching algorithms, such as near-match Levenshtein distance rules within automated collation tools. This will help clarify how token-level edit distances handle orthographic variation during the initial alignment phase.

[github.com

Materials/session7/Session07b_Normalization.ipynb at master](https://github.com/automaticCollationLausanne2020/Materials/blob/master/session7/Session07b_Normalization.ipynb)

Resolving Near-Matching Implementations in Text Alignment

I am investigating the exact algorithmic mechanisms behind fuzzy alignment and near-matching in automated collation engines. My analysis focuses on how fuzzy matching uses Levenshtein distance metrics to detect minor orthographic, spelling, and scribal variations, allowing the engine to bridge minor character discrepancies without introducing artificial gaps or incorrect transpositions into the alignment graph.

Synthesizing Philological Workflows and Case Studies

I am consolidating the operational synthesis across various historical manuscript projects, including the 7Partidas Digital initiative and the Fuero Juzgo codices. By evaluating these against large-scale digital initiatives, I am mapping out how handwritten text recognition, lemmatization tools, and automated alignment pipelines integrate into standardized XML encoding formats for critical editions.

Formulating Advanced Phylogenetic and Visualization Queries

I am planning targeted searches into specialized phylogenetic tree algorithms used in stemmatology, specifically neighbor-joining methods implemented in text analysis tools, alongside specialized notebook environments designed for interactive variant graph visualization. These queries will provide deep technical clarity on how genealogical relationships between manuscript witnesses are computationally inferred.

[researchgate.net

Responding to Criticisms of Phylogenetic Methods in Stemmatology - ResearchGate](https://www.researchgate.net/publication/254962929_Responding_to_Criticisms_of_Phylogenetic_Methods_in_Stemmatology)[researchgate.net

Towards generating a stemma of complicated manuscript traditions: Petrus Alfonsi's Dialogus | Request PDF - ResearchGate](https://www.researchgate.net/publication/280810610_Towards_generating_a_stemma_of_complicated_manuscript_traditions_Petrus_Alfonsi's_Dialogus)[grokipedia.com

Recension - Grokipedia](https://grokipedia.com/page/Recension)[journals.openedition.org

Visualizing Collation Results - OpenEdition Journals](https://journals.openedition.org/variants/950?lang=fr)[researchgate.net

3: Liniamentis in the collation results. | Download Scientific Diagram](https://www.researchgate.net/figure/Liniamentis-in-the-collation-results_fig2_334395640)[kclpure.kcl.ac.uk

This electronic thesis or dissertation has been downloaded from the King's Research Portal at https://kclpure.kcl.ac.uk/portal](https://kclpure.kcl.ac.uk/ws/files/105283803/2018_Nury_Elisa_1337422_ethesis.pdf)[researchgate.net

Elisa NURY | Research scientist | University of Geneva, Genève | UNIGE | Department of Antiquity - ResearchGate](https://www.researchgate.net/profile/Elisa-Nury)

Synthesis of Stemmatic Algorithms and Collation Tools

I am synthesizing findings on computational stemmatics and collation software, specifically examining how neighbor-joining algorithms and distance metrics compute manuscript phylogenetic trees from variant matrices. I am also evaluating custom visualization tools and interactive notebook interfaces that assist editors in identifying shared manuscript errors and manually refining token alignments for complex classical traditions.

Resolving Methodological Saturation and Scope

I have resolved all primary information gaps regarding dynamic programming recurrences, variant graph topologies, historical project workflows, and LLM limitations in digital ecdotics. The research has reached comprehensive analytical saturation across technical, historical, and pedagogical dimensions.

Finalizing Research Phase and Transitioning to Report Construction

I am concluding the planning and information-gathering phase of the research. I am now transitioning to compiling and structuring the final comprehensive technical report, synthesizing all algorithmic formulations, case studies, variant taxonomy guides, and pipeline implementation tutorials.

The initial research has returned a lot of information. I'm sorting through it and organizing it. This will make sure the whole thing flows well and hits all the key points you asked for.

This is it! I’m bringing it all together. Jotting down my final thoughts, polishing everything up, and making sure I give you my very best work.

## References (APA)

1. boris-portal.unibe.ch. (n.d.). *From giant despair to a new heaven: The early years of automatic collation - BORIS Portal*. https://boris-portal.unibe.ch/server/api/core/bitstreams/ccc28b82-7096-4f49-a355-d37fa1428ec3/content
2. journals.openedition.org. (n.d.). *Visualizing Collation Results - OpenEdition Journals*. https://journals.openedition.org/variants/950?lang=fr
3. pure.knaw.nl. (n.d.). *Royal Netherlands Academy of Arts and Sciences (KNAW)*. https://pure.knaw.nl/ws/files/799786159/Computer_supported_collation_with_CollateX_haentjens_dekker_middell.pdf
4. open.oregonstate.education. (n.d.). *Chapter 3: Sequence Alignments – Applied Bioinformatics - Open Educational Resources*. https://open.oregonstate.education/appliedbioinformatics/chapter/chapter-3/
5. pmc.ncbi.nlm.nih.gov. (n.d.). *Developments in Algorithms for Sequence Alignment: A Review - PMC*. https://pmc.ncbi.nlm.nih.gov/articles/PMC9024764/
6. ebi.ac.uk. (n.d.). *Computational Analysis of Protein Function within Complete Genomes Anton James Enright - EMBL-EBI*. https://www.ebi.ac.uk/sites/ebi.ac.uk/files/shared/documents/phdtheses/antonenrightthesis.pdf
7. academic.oup.com. (n.d.). *Graph schema validation at last? Work towards a StemmaREST ontology with Neo4J, RDF-STAR, and SHACL | Digital Scholarship in the Humanities | Oxford Academic*. https://academic.oup.com/dsh/article/41/Supplement_1/i3/8213722
8. pure.knaw.nl. (n.d.). *Computer-supported collation of modern manuscripts: CollateX and the Beckett Digital Manuscript Project - Royal Netherlands Academy of Arts and Sciences (KNAW)*. https://pure.knaw.nl/ws/files/797964/BDMP_Collatex_LLC_article_2013_05_24_submitted_20130529.pdf
9. researchgate.net. (n.d.). *Computer-supported collation of modern manuscripts: CollateX and the Beckett Digital Manuscript Project | Request PDF*. https://www.researchgate.net/publication/270752678_Computer-supported_collation_of_modern_manuscripts_CollateX_and_the_Beckett_Digital_Manuscript_Project
10. en.wikipedia.org. (n.d.). *Needleman–Wunsch algorithm*. https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
11. brill.com. (n.d.). *Three Direct Copies and Other Closely Related Manuscripts of the Pauline Epistles in*. https://brill.com/view/journals/nt/65/3/article-p381_6.xml
12. researchgate.net. (n.d.). *Responding to Criticisms of Phylogenetic Methods in Stemmatology*. https://www.researchgate.net/publication/254962929_Responding_to_Criticisms_of_Phylogenetic_Methods_in_Stemmatology
13. dspace.est.edu.br. (n.d.). *MÉTODO GENEALÓGICO BASEADO NA COERÊNCIA: POTENCIALIDADES E FRAGILIDADES - Faculdades EST*. http://dspace.est.edu.br:8080/jspui/bitstream/BR-SlFE/1113/1/casagrande_w_td242.pdf
14. academic.oup.com. (n.d.). *From print to digital: A web edition of Giacomo Leopardi's Idilli - Oxford Academic*. https://academic.oup.com/dsh/article/36/Supplement_1/i23/5828480
15. collatex.obdurodon.org. (n.d.). *Computer-supported collation with CollateX*. https://collatex.obdurodon.org/
16. dokumen.pub. (n.d.). *Genetics Vol 1 & 2 First Edition - DOKUMEN.PUB*. https://dokumen.pub/genetics-vol-1-2-first-edition.html
17. researchgate.net. (n.d.). *Intra-language Text Alignment Using iAligner - Proceedings, 7th International Conference of Digital Archives and Digital Humanities: December 1-3, 2016 National Taiwan University*. https://www.researchgate.net/publication/326490273_Intra-language_Text_Alignment_Using_iAligner_-_Proceedings_7th_International_Conference_of_Digital_Archives_and_Digital_Humanities_December_1-3_2016_National_Taiwan_University
18. researchgate.net. (n.d.). *(PDF) TRAViz: A visualization for Variant Graphs*. https://www.researchgate.net/publication/282156951_TRAViz_A_visualization_for_Variant_Graphs

_50 citation marker(s) carried no resolvable source in the DOM and were dropped; see the `*_citations.json` sidecar._
