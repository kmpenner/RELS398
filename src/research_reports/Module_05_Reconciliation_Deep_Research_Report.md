# Topic 05 (Topic_05_Reconciliation): Academic Deep Research Report

**Model:** 3.1 Pro (Deep Research)  
**Attachments:** 9 PDF(s)  
**Citations resolved:** 18

## Manuscript Transcription Reconciliation Methods

ContentsShare & Export
Create

# Reconciliation and Metrics in Digital Philology: Methods for Reconciling Manual, HTR, and AI-Generated Manuscript Transcriptions

## 1. Abstract and Executive Summary

The proliferation of mass digitization initiatives over the past two decades has fundamentally transformed the landscape of textual scholarship, yet it has simultaneously precipitated a profound epistemological crisis regarding textual reliability. As historical manuscripts and early printed books are translated into machine-readable formats through manual double-keying, Optical Character Recognition (OCR), and Handwritten Text Recognition (HTR), the resulting digital surrogates frequently harbor pervasive transcription noise. Establishing a definitive consensus text from these disparate and often conflicting data streams requires rigorous algorithmic reconciliation, sophisticated statistical benchmarking, and meticulously designed post-correction workflows. This comprehensive report investigates the precise methodologies and mathematical metrics that govern the evaluation, reconciliation, and subsequent post-correction of digital transcriptions in the context of advanced digital humanities and computational philology.

The core thesis advanced herein posits that systematic text reconciliation—achieved through double-keying error analysis, Character Error Rate (CER) and Word Error Rate (WER) benchmarking, and robust inter-annotator agreement statistical modeling—is absolutely essential for quantifying the efficacy of automated transcription pipelines. Without such empirical verification, the integration of Artificial Intelligence (AI) and Large Language Models (LLMs) into scholarly editing risks introducing unquantifiable systematic biases, historical anachronisms, and textual hallucinations into the scholarly record. By evaluating the mathematical foundations of the Levenshtein distance and the Wagner-Fischer algorithm, this analysis elucidates how raw string similarities are computed and utilized to identify typographical versus structural transcription errors. Furthermore, the synthesis explores the critical threshold at which transcription noise fatally degrades downstream Natural Language Processing (NLP) tasks, demonstrating the non-linear decay of algorithmic comprehension when confronted with historical textual artifacts.

Through exhaustive examinations of large-scale, real-world initiatives—including the Deutsches Textarchiv (DTA), the IMPACT project, the Bullinger Letters alignment project, and recent advancements in Pre-Editorial Normalization (PEN) for medieval manuscripts—this report demonstrates how targeted post-correction workflows bridge the usability gap between graphemic fidelity and normalized editorial expectations. Ultimately, the analysis translates these highly technical methodologies into pedagogical frameworks, equipping future digital philologists with the theoretical and practical competencies necessary to construct, audit, and mathematically verify digital scholarly editions.

## 2. Technical, Methodological, and Historical Foundations

### The Double-Keying Methodology

In the pursuit of establishing virtually error-free digital texts, particularly for historical documents characterized by complex layouts, obsolete typography (such as early modern Fraktur fonts), and highly irregular orthography, the double-keying methodology remains the gold standard of mass digitization. The process mandates that two independent human operators manually transcribe the identical source text. The resulting divergent textual outputs are subsequently compared via computational string-matching algorithms to identify discrepancies, which a senior editor or an automated reconciliation script then adjudicates to form a final consensus text[1].

The epistemological strength of double-keying derives from the statistical improbability of two independent operators committing the exact same typographical error at the precise same character position. Commercial data entry services employing this method routinely guarantee accuracy rates oscillating between 99.95% and 99.98%[1]. Furthermore, stringent institutional benchmarks, such as the German Research Foundation (DFG) Practical Guidelines on Digitization, stipulate an accuracy threshold of 99.997%, yielding a digitized corpus that is theoretically "virtually error-free"[2]. A profound methodological insight regarding double-keying is the frequent deployment of non-native speakers to perform the primary transcription. By deliberately severing the transcriber's semantic comprehension of the text from the visual recognition of its graphemes, the methodology effectively neutralizes the psychological phenomenon of auto-correction, wherein a native speaker might unconsciously modernize a historical spelling variant or mentally insert an omitted character[3].

Evaluating the ultimate correctness of double-keying necessitates a strict bipartite classification of errors: typographical and structural. Typographical errors occur at the character level, encompassing omissions, substitutions, and insertions of textual content. Conversely, structural errors manifest in the Extensible Markup Language (XML) or Text Encoding Initiative (TEI) markup layer, representing a failure to accurately capture the semantic or physical architecture of the document—for example, misidentifying a marginal note as a primary paragraph, or misapplying a speaker tag in a dramatic text[2]. The rigorous separation of these error classes is vital; typographical fidelity is rendered meaningless if the structural scaffolding of the XML renders the text computationally unreadable to parsing algorithms.

### Levenshtein Distance and the Wagner-Fischer Algorithm

The mathematical reconciliation of differing text streams—whether comparing two divergent manual transcriptions, or benchmarking an HTR output against an established ground truth—relies predominantly on edit distance metrics, most prominently the Levenshtein distance. Formulated by Soviet mathematician Vladimir Levenshtein in 1965, this metric mathematically quantifies the dissimilarity between two sequences by calculating the absolute minimum number of single-character editing operations required to transform the source string into the target string. The permissible operations are strictly restricted to insertions, deletions, and substitutions[4].

While the recursive mathematical definition of the Levenshtein distance is robust, its direct computational implementation is exponentially inefficient, exhibiting overlapping subproblems that drastically slow processing times for long textual sequences. This inefficiency was definitively resolved by the Wagner-Fischer algorithm (1974), which applies a bottom-up dynamic programming approach to compute the edit distance in O(mn) time and space complexity, where m and n denote the absolute lengths of the two strings being compared[4].

The Wagner-Fischer algorithm initializes a computational matrix D of dimensions (m+)×(n+). A foundational necessity of this matrix, which often confuses novice programmers, is the inclusion of the empty string (representing a prefix of length zero) as the base case for both the source and target strings[5]. This initialization step is mathematically imperative because it establishes the baseline cost of transforming any given string into an empty string (requiring i consecutive deletions) and transforming an empty string into any target string (requiring j consecutive insertions). The algorithm populates the matrix according to the following state transition logic, evaluating the optimal sub-path for every character:

D[i,j]=min⎩⎨⎧​D[i−,j]+D[i,j−]+D[i−,j−]+cost​(Deletion)(Insertion)(Substitution)​

In this formulation, the substitution cost equals if the characters s[i] and t[j] are identical; otherwise, the cost equals [5]. Upon traversing the entire sequence, the integer residing in the bottom-right cell of the matrix, D[m,n], represents the absolute Levenshtein distance. The underlying trend demonstrated by this dynamic programming approach is the spatial representation of textual mutation; by tracing the optimal path backward from D[m,n] to D[,], digital philologists can systematically extract the precise alignment of typographical errors, categorizing exactly where an HTR engine hallucinated a character, or where a human transcriber skipped a word during the double-keying process.

### Mathematical Definitions of CER and WER

The raw Levenshtein distance informs the two most critical benchmark metrics in digital document analysis: Character Error Rate (CER) and Word Error Rate (WER). These metrics normalize the raw edit distance against the total length of the ground truth text, providing a comparable percentage of transcription inaccuracy across texts of highly variable lengths[6].

The Character Error Rate is defined mathematically by the formula:

CER=NS+D+I​

Where S represents the total number of character substitutions, D represents character deletions, I represents character insertions, and N represents the total number of characters in the verified reference ground truth sequence[6]. Because insertions are added to the numerator without a corresponding increase in the denominator N, it is mathematically possible for the CER to exceed 100% in instances of severe algorithmic hallucination, wherein an HTR model generates vast strings of garbage text from a degraded manuscript image.

The Word Error Rate utilizes the identical mathematical formula, but shifts the unit of analysis from the individual character to the token (typically defined as whitespace-delimited words). WER is traditionally much higher than CER because a single incorrect character within a twenty-character word renders the entire word mathematically incorrect under the Wagner-Fischer evaluation[6]. A deep examination of the relationship between CER and WER reveals a fundamental dynamic in HTR evaluation: an automated model that produces a low CER but a disproportionately high WER is almost certainly suffering from systemic boundary detection failures, arbitrarily inserting whitespace and fracturing cohesive lexical units into nonsensical fragments.

### Inter-Annotator Agreement Metrics

While CER and WER evaluate the divergence between a transcription hypothesis and a verified ground truth, establishing that ground truth originally requires reconciling the subjective judgments of human annotators. When multiple philologists are tasked with tagging named entities, resolving complex paleographic abbreviations, or defining structural TEI boundaries, their conformity must be statistically validated to ensure that the dataset is not corrupted by idiosyncratic interpretation[7].

The simplest measurement of agreement—joint probability or percentage agreement—is structurally flawed because it completely fails to account for instances where annotators agree purely by random chance. To rectify this, researchers utilize chance-adjusted agreement metrics, prominently the Kappa family of statistics and Krippendorff's Alpha.

| Metric | Application Scope | Mathematical Foundation | Primary Limitations |
| --- | --- | --- | --- |
| **Cohen's Kappa** | Exactly 2 Raters, Categorical Data | κ=−Pe​Po​−Pe​​ | Cannot handle more than two raters. Susceptible to Kappa paradoxes in highly skewed datasets. |
| **Fleiss' Kappa** | > Raters, Categorical Data | Generalizes Cohen's formulation using marginal distributions of overall assignments. | Assumes raters are chosen at random from a larger population; less effective for fixed expert panels. |
| **Krippendorff's Alpha** | Any number of raters, handles missing data, mixed data types | α=−De​Do​​ (Observed disagreement over Expected disagreement) | Computationally complex, often requiring resampling methods like bootstrapping for variance evaluation. |

Cohen's Kappa evaluates the agreement of exactly two raters. The value Po​ denotes the relative observed agreement among the raters, while Pe​ computes the hypothetical probability of chance agreement based on the marginal distributions of the raters' distinct categorizations[8]. A value of 1 indicates perfect alignment, while 0 indicates no agreement beyond what would be expected by random chance. However, Cohen's Kappa suffers from paradoxes regarding prevalence and bias; in manuscript corpora where a specific phenomenon is exceedingly rare (e.g., a highly specific scribal abbreviation), high observed agreement can paradoxically result in a low Kappa score because the highly skewed marginal distributions inflate the mathematical expectation of chance agreement[9].

For large-scale transcription efforts involving crowd-sourced labor or multiple scholarly annotators, Fleiss' Kappa extends the chance-adjusted metric to accommodate more than two raters[10]. Yet, the most robust metric for digital humanities and textual editing remains Krippendorff's Alpha. Unlike the Kappa statistics, which calculate observed versus expected agreement, Krippendorff's Alpha calculates observed versus expected *disagreement*[7]. Furthermore, it seamlessly handles missing data—a frequent occurrence in illegible historical manuscripts where one annotator may simply skip a damaged word that another attempts to transcribe—and supports various distance metrics across nominal, ordinal, and continuous data structures[7].

## 3. Comparative Methodological Evaluation

### Reconciling Human Disagreement vs. Scoring HTR and LLM Output

The reconciliation of human-generated double-keying output operates on fundamentally different epistemological premises than the scoring of automated HTR or Large Language Model (LLM) outputs. When two human transcribers disagree, the error topology is heavily weighted toward cognitive substitutions (e.g., misreading a long 's' for an 'f' due to paleographic similarities) or simple mechanical transposition errors resulting from keyboard layout (e.g., typing "teh" instead of "the"). In these scenarios, the consensus text is established through targeted manual arbitration, often relying on the aforementioned inter-annotator agreement metrics to identify which specific transcriber is consistently deviating from the physical paleographic reality of the document.

Conversely, the error typology generated by sequence-to-sequence neural networks, Convolutional Neural Networks (CNNs), and LLMs interacting with manuscript images introduces distinct, systemic algorithmic artifacts. Automated HTR models frequently struggle with macro-structural preservation, exhibiting extremely high insertion and deletion rates at the physical boundaries of text lines. A persistent anomaly in historical text recognition is the handling of line-end hyphenation; predictive models frequently fail to reconstruct the fractured lexical unit, treating the hyphenated fragment at the end of one line and the beginning of the next as distinct, unrelated tokens, thereby artificially inflating the Word Error Rate and destroying the semantic coherence of the sentence[11].

Furthermore, AI-generated transcriptions are highly susceptible to out-of-vocabulary (OOV) failures. If a historical manuscript contains a unique geographical toponym or an idiosyncratic spelling variant not comprehensively represented in the HTR model's training data, the predictive algorithm will often substitute the anomalous word with a visually similar but linguistically incorrect word that possesses a higher probability distribution within the model's lexicon[1]. This phenomenon highlights a critical distinction: whereas human transcribers transcribe what they see (even if it makes no immediate semantic sense), AI models transcribe what they statistically expect to see, introducing pervasive anachronisms into the text.

### The Impact of Transcription Noise on Downstream NLP

The imperative to aggressively drive down CER and WER through rigorous post-correction is not merely an exercise in typographical pedantry; transcription noise exerts a devastating and highly non-linear impact on downstream computational analysis. A comprehensive extrinsic assessment of OCR quality impact conducted by van Strien et al. (2020) definitively demonstrated that the ingestion of noisy historical texts irrevocably harms standard Natural Language Processing (NLP) tools, which are overwhelmingly trained on pristine, modern digital corpora[12].

The degradation of these tools follows disparate trajectories based on the specific nature of the computational task. Part-of-Speech (POS) tagging exhibits a relatively linear decay; the tagger's accuracy degrades in direct proportion to the error rate of the OCR output, crossing a threshold of significant uselessness at approximately 5% CER[13]. The degradation occurs primarily because morphological suffixes, which POS taggers heavily rely upon to determine syntactic categories (e.g., identifying a verb by an "-ed" suffix), are the elements most frequently corrupted by character-level substitutions during the OCR process.

The impact on Named Entity Recognition (NER), however, represents a catastrophic failure cascade. The primary function of NER is to extract proper nouns—such as individuals, geographical locations, and organizations—from the surrounding prose[13]. Named entities inherently exhibit low textual redundancy; if the name "Robespierre" is misspelled as "Kobespierre" due to a degraded capital letter on the manuscript, the entire entity is permanently lost to the search index. Empirical evidence from van Strien's evaluations indicates that NER F-scores drop precipitously from an acceptable 90% down to a mathematically useless 60% when the WER of the text increases from 1% to just 7%, or when the CER increases from 8% to 20%[12]. The underlying cause is that named entities frequently overlap with the precise out-of-vocabulary terms that automated recognition models struggle to process. Consequently, without human-in-the-loop post-correction or specialized algorithmic reconciliation, the extraction of historical actors and geographic networks from noisy digitizations is statistically invalid[12].

### Pre-Editorial Normalization and LLM Output Scoring

To bridge the usability gap between raw, noisy HTR output and the pristine texts required by downstream NLP, contemporary digital philology has introduced the paradigm of Pre-Editorial Normalization (PEN). Explored extensively by Clérice et al. (2026) in the context of medieval Latin and Old French manuscripts, the PEN task is explicitly designed to algorithmically normalize graphemic ATR (Automatic Text Recognition) output according to standardized editorial conventions before the text is subjected to final human curation[11].

Historically, textual scholarship has existed on a spectrum between the strictly graphetic (recording every minute visual variation, retaining unexpanded abbreviations, and mirroring the exact physical layout) and the heavily normalized (expanding all abbreviations, modernizing capitalization, and standardizing punctuation)[11]. Graphemic models, trained on highly specialized datasets like CATMuS or CoMMA, preserve historical variations and demonstrate high generalizability across disparate manuscript hands, but yield output that fundamentally breaks modern NLP tools[11].

The implementation of LLMs, specifically byte-level sequence-to-sequence transformers like ByT5, addresses this gap by ingesting the graphemic HTR output and generating a pre-edited consensus text. The LLM is instructed via complex few-shot prompting to resolve scribal abbreviations contextually (e.g., expanding a nasal macron into an 'm' or an 'n' depending on the ensuing consonant), normalize the ramist letters ('u' versus 'v', 'i' versus 'j') based strictly on vocalic or consonantal usage, and rectify standard HTR confusions (e.g., distinguishing a minim sequence parsed as 'rn' versus 'm')[11].

However, evaluating LLM output requires intense scholarly vigilance against the phenomenon of algorithmic over-normalization and hallucination. When LLMs process historical texts characterized by fluid orthography, they frequently collapse historically significant dialectical variants into a singular standard form, thereby permanently erasing critical linguistic evidence[11]. Furthermore, LLMs may hallucinate entire strings of content when encountering severe HTR noise, seamlessly generating grammatically coherent but entirely fabricated prose to bridge the illegible gap. Therefore, the reconciliation of LLM-generated transcriptions mandates strict boundaries: abbreviations corresponding to proper names lacking contextual clarity must remain unexpanded, and continuous spans of severe noise must be flagged for human review rather than algorithmically overwritten[11]. Utilizing these constraints, Clérice et al. demonstrated that a tightly controlled ByT5 normalization model achieved a robust 6.7% CER on medieval manuscripts, substantially accelerating the subsequent human editorial workflow without sacrificing paleographic integrity[11].

## 4. Real-World Digital Edition Case Studies

### Case Study 1: The Deutsches Textarchiv (DTA)

The Deutsches Textarchiv (DTA), hosted by the Berlin-Brandenburg Academy of Sciences and Humanities (BBAW), serves as a paramount case study in the deployment of mass double-keying for the creation of an unimpeachable historical reference corpus. Digitizing printed works in the New High German Language dating from 1600 to 1900, the DTA elected to bypass OCR entirely for its foundational texts. This decision acknowledged the severe limitations of optical recognition on early modern Fraktur fonts, irregular inking, and highly variable historic spelling patterns[3]. By January 2016, the archive comprised 2,331 texts representing approximately 1.1 billion characters[14].

To establish its consensus texts, the DTA outsourced the primary transcription to non-native speakers executing a strict double-keying protocol[3]. The vendors guaranteed a minimum character accuracy of 99.9%. Following the initial algorithmic reconciliation of the dual data streams, the DTA applied extensive linguistic analysis and rule-based heuristics to normalize historic spellings to modern lemmas, enabling advanced phonetic and lemma-based search capabilities across the corpus[3].

Crucially, the DTA's methodological approach highlights the absolute necessity of distinguishing the typographical layer from the semantic markup layer. All transcriptions were mapped to the DTA "Base Format" (DTABf), a highly customized, strict subset of the TEI P5 guidelines designed to enforce standardized structural markup across massive and heterogeneous text collections[3]. Haaf, Wiegand, and Geyken demonstrated in their statistical analyses that while the typographical error rate of the double-keying process was vanishingly small, structural errors—such as the incorrect demarcation of a marginal note, or the misapplication of a speaker tag in a drama—required sophisticated XML validation schemas (e.g., Schematron) and continuous community-driven quality control platforms to resolve[2]. The eventual evolution of the DTABf to the DTABf-M (Manuscripts) further necessitated the expansion of the TEI subset to accommodate the unique physical architectures of handwritten documents, proving that transcription accuracy is inseparable from structural encoding accuracy[15].

### Case Study 2: The IMPACT Project and the Australian Newspaper Digitisation Program (ANDP)

The digitisation of historical newspapers presents uniquely hostile conditions for automated transcription. Degrading paper quality, complex multi-column layouts, inter-article boundary failures, and highly variable typography render traditional OCR algorithms highly inaccurate. During the initial phases of the Australian Newspaper Digitisation Program (ANDP), raw OCR accuracy on historical newspapers ranged radically from 71% to 98%, falling well below the operational threshold necessary for reliable full-text searching[16].

While the DTA solved accuracy deficits through comprehensive manual double-keying, the massive scale of newspaper archives rendered this approach financially prohibitive. The IMPACT project estimated the cost of manual keying at approximately 1 EUR per page, meaning a single large archival volume could easily consume upwards of 1,000 EUR in transcription costs alone[13]. To achieve a functional consensus text while mitigating costs, the ANDP pioneered a targeted hybrid methodology. Contractors were utilized to manually correct only the critical structural and metadata elements of the newspaper—specifically the article titles, subtitles, and the first four lines of text—guaranteeing a 99.5% accuracy rate for these high-value fields[16].

For the vast expanse of the remaining body text, the program instituted a revolutionary crowd-sourced post-correction model through the Trove platform. By exposing the raw, noisy OCR output to the public alongside the scanned image, volunteers manually reconciled the text line-by-line[15]. Complementing this human effort, institutions frequently deploy Recognizer Output Voting for Error Reduction (ROVER) techniques. ROVER aligns the hypotheses of multiple differing OCR engines operating on the same image, utilizing majority voting algorithms and dynamic programming to select the most probable correct character at any given position, thereby organically driving down the WER prior to human intervention[17]. The profound structural insight derived from the ANDP and IMPACT project is that a consensus text in digital philology does not necessarily need to be achieved prior to publication; rather, the digital edition can function as a dynamic, living document that asymptotically approaches perfection through continuous, decentralized human post-correction[15].

### Case Study 3: Connectionist Temporal Classification (CTC) Alignment in the Bullinger Letters

The Bullinger dataset, a vast collection of 3,622 16th-century letters written in Latin and premodern German by the Swiss reformer Heinrich Bullinger, presented a unique reconciliation challenge. While expert historians had produced highly accurate transcriptions of the letters, these transcriptions existed as continuous paragraphs devoid of spatial layout information, rendering them useless for training layout-aware HTR systems[18]. When automated systems like Transkribus were used to align these transcriptions with the physical line images, it introduced systematic hyphenation errors, fracturing words that spanned across line breaks.

To resolve this, Peer, Scius-Bertrand, and Fischer (2025) introduced a self-training methodology utilizing a Connectionist Temporal Classification (CTC) alignment algorithm. The algorithm ingested the expert-provided, layout-free transcription and the character posterior probabilities generated by HTR models (including PyLaia, HTRFlor, and Retsinas models)[18]. Utilizing dynamic programming, the CTC algorithm found the optimal sequence to insert line breaks into the continuous transcription, perfectly matching the visual layout of the scanned pages.

The implementation revealed a fascinating paradox: the alignment accuracy was frequently higher when utilizing a *weakly trained* HTR model rather than a highly optimized one, as the weaker model had not yet overfit to the faulty, hyphen-broken training data[18]. By iteratively filtering the alignments based on a confidence threshold (γ​, measuring the confidence of the first and last six characters of a line) and retraining the models, the researchers successfully improved the CER of the PyLaia model by 1.1 percentage points. This case study demonstrates that establishing a consensus text is not merely about correcting characters, but about perfectly reconciling the semantic transcription with the physical, geospatial coordinates of the manuscript page[18].

### Case Study 4: Multimodal LLM Extraction from Herbarium Specimens

The reconciliation of historical scientific data presents challenges that extend beyond prose. In the digitisation of botanical herbarium specimens, the "text" consists of highly unstructured, multi-modal elements: the physical pressed plant, scale bars, color charts, and degraded, handwritten taxonomic labels[6]. Standard OCR engines fail completely when attempting to parse the erratic spatial distribution of these labels.

To establish a verified digital record from the UoS_Data_Rescue dataset, researchers implemented a sophisticated multi-stage AI pipeline[6]. First, an object detection model isolated the physical label from the plant matter. Second, a transformer-based OCR model (TrOCR) generated a raw transcription of the handwritten text. Recognizing the extreme vulnerability of TrOCR to out-of-vocabulary taxonomic names and archaic abbreviations, the researchers introduced the ByT5 byte-level sequence-to-sequence model as an automated post-correction layer[6].

Because ByT5 operates at the byte level rather than relying on pre-defined token vocabularies, it successfully reconstructed highly complex, misspelled, and archaic Latin binomials that standard LLMs would have hallucinogenically "corrected" into common modern words[6]. The reconciliation of these labels into a consensus database record required the AI to actively integrate the visual features of the leaf morphology with the transcribed text, relying on contrastive learning models to ensure that the transcribed species name logically matched the visual data of the specimen[6].

## 5. Pedagogical Takeaways and Synthesis for Digital Editors

Integrating these complex, multi-layered reconciliation methodologies into an undergraduate digital methods or textual editing curriculum requires transitioning abstract mathematical theories into actionable, programmatic competencies. The modern digital editor must be trained not merely as a passive transcriber, but as an auditor of automated systems, fully capable of deploying statistical tools to quantify error, detect systemic AI bias, and establish ground truth.

### A Practical Guide to Calculating CER/WER in Python

To genuinely comprehend the mechanics of CER and WER, students must look beyond black-box libraries and understand the programmatic logic of the Wagner-Fischer algorithm. In a Python-based curriculum, this dynamic programming approach can be mapped conceptually.

The process begins by defining a function that accepts a reference string (the ground truth) and a hypothesis string (the HTR output). The script must initialize a two-dimensional array (matrix) where the number of rows equals the length of the reference string plus one, and the number of columns equals the length of the hypothesis string plus one. The critical pedagogical lesson here is the extra row and column: they represent the base case of the empty string.

The initialization phase populates the first row and first column with incrementally increasing integers. This represents the accumulating mathematical cost of purely deleting characters from the reference string to eventually reach the empty string, or purely inserting characters to build the hypothesis string from nothing.

The core of the algorithm utilizes nested iterations (e.g., iterating through rows, and within that, iterating through columns) to evaluate the cost of transition for every single character pair. A conditional check determines the substitution cost: if the current character in the reference matches the current character in the hypothesis, the substitution cost is 0; if they conflict, the cost is 1. The current cell in the matrix is then assigned the absolute minimum value among three calculated paths:

1. The cell directly above + 1 (representing a Deletion)
2. The cell directly to the left + 1 (representing an Insertion)
3. The cell diagonally up-and-left + the calculated substitution cost (representing a Substitution or a Match).

The terminal value located at the bottom-right corner of the matrix holds the minimum edit distance. To calculate the Character Error Rate, the student simply divides this integer by the total length of the reference string. To adapt this exact logic for the Word Error Rate, the student must first tokenize the reference and hypothesis strings by whitespace into arrays of words, and execute the exact same Wagner-Fischer matrix logic on the word arrays rather than the character arrays. By manually constructing this matrix, students visualize precisely how HTR pipelines trace and misinterpret errors, gaining the ability to write custom scripts capable of penalizing specific types of historical errors to better reflect paleographic realities.

### Writing an Audit Reconciliation Report

When establishing a consensus text from mixed manual and AI modalities, the digital editor must author a formal reconciliation audit report. This document ensures epistemological transparency, recording exactly how the text moved from the raw manuscript image to the final encoded XML file. An effective audit report must contain the following structural components:

1. **Ground Truth Sampling and IAA Validation:** The report must clearly define the specific subset of the corpus subjected to manual double-keying to serve as the ground truth. It must document the Inter-Annotator Agreement utilizing Krippendorff’s Alpha or Fleiss' Kappa to mathematically prove that the initial human transcribers achieved high consensus. This verifies the reliability of the ground truth data against which the AI will be benchmarked.
2. **Error Rate Benchmarking:** The report must transparently declare the CER and WER for all automated outputs. Crucially, the editor must identify the divergence between the two metrics. If the CER is 4% but the WER is an anomalous 25%, the audit must explicitly identify systemic tokenization or boundary detection failures within the HTR engine.
3. **Error Typology and Systematic Bias Identification:** The audit should classify the most frequent substitutions. Does the model systemically confuse the long 's' with 'f'? Does it hallucinate modern punctuation where none exists? Identifying these biases dictates the strict parameters required for the subsequent Pre-Editorial Normalization phase.
4. **Structural vs. Typographical Divergence:** If the text is encoded in TEI, the report must differentiate between characters misread by the OCR/HTR and XML structural errors. A missing closing tag represents a structural failure that compromises the entire document object model, taking absolute precedence over a minor typographical substitution.
5. **LLM Parameterization and Constraints:** If an LLM is utilized for post-correction, the exact few-shot prompt provided to the model must be appended to the audit report. The report must demonstrate that the LLM was explicitly instructed to preserve historically significant orthography and must include a statistical evaluation of the LLM's false-positive rate regarding unprompted, anachronistic normalizations.

## 6. Comprehensive Academic & Technical References

The theoretical and practical frameworks synthesized within this report are deeply rooted in the evolving literature of computational linguistics, digital humanities, and manuscript studies. The following references constitute the primary literature upon which this analysis is founded:

| Authors | Title and Context | Bibliographic Reference Data |
| --- | --- | --- |
| **Bawden, R., Clérice, T., Glaise, A., Pinche, A., & Smith, D.** | *Pre-Editorial Normalization for Automatically Transcribed Medieval Manuscripts in Old French and Latin.* Discusses the application of ByT5 models for PEN, the CoMMA and CATMuS datasets, and the risks of LLM hallucination in historical text normalization. | arXiv preprint, cs.CL. 2026. [URL: https://arxiv.org/abs/2602.13905][11] |
| **Haaf, S., Wiegand, F., & Geyken, A.** | *Measuring the Correctness of Double-Keying: Error Classification and Quality Control in a Large Corpus of TEI-Annotated Historical Text.* Foundational text on the Deutsches Textarchiv (DTA), establishing the 99.997% DFG accuracy benchmark, and distinguishing between typographical and TEI/XML structural errors. | *Journal of the Text Encoding Initiative*, Issue 4, 2013. DOI: 10.4000/jtei.739. [Download PDF](https://journals.openedition.org/jtei/pdf/739) [1] |
| **Peer, M., Scius-Bertrand, A., & Fischer, A.** | *CTC Transcription Alignment of the Bullinger Letters: Automatic Improvement of Annotation Quality.* Introduces the CTC token passing alignment algorithm to resolve line-break hyphenation errors and explores self-training protocols for PyLaia and HTRFlor models. | *ICCV Workshop Proceedings*, IEEE, 2025. [URL: https://github.com/andreas-fischer-unifr/nntp][18] |
| **Singh, L. G., & Middleton, S. E.** | *Tabular context-aware optical character recognition and tabular data reconstruction for historical records.* Examines the UoS_Data_Rescue dataset, integrating TrOCR with ByT5 byte-level models to resolve complex, long-tail historical taxonomic records. | *International Journal on Document Analysis and Recognition (IJDAR)*, Vol. 28, 2025. DOI: 10.1007/s10032-025-00543-9. [Download PDF](https://libkey.io/libraries/3054/articles/675615675/full-text-file?utm_source=nomad) [6] |
| **van Strien, D., Beelen, K., Ardanuy, M., Hosseini, K., McGillivray, B., & Colavizza, G.** | *Assessing the Impact of OCR Quality on Downstream NLP Tasks.* Conducts extrinsic assessments demonstrating the linear degradation of POS tagging and the catastrophic failure of NER resulting from historical transcription noise. | *Proceedings of the 12th International Conference on Agents and Artificial Intelligence*, INSTICC, 2020. DOI: 10.5220/0009169004840496.[13] |

(Note: The foundational algorithms of Levenshtein (1965), Wagner-Fischer (1974), Cohen's Kappa (1960), Fleiss' Kappa (1971), and Krippendorff's Alpha are referenced theoretically throughout the text via their standard algorithmic and statistical derivations as documented in computational literature[4]).

Sources used in the report
[researchgate.net

AVERAGE CHARACTER ACCURACY FOR ALL 17 DOCUMENTS - ResearchGate

 Opens in a new window](https://www.researchgate.net/figure/AVERAGE-CHARACTER-ACCURACY-FOR-ALL-17-DOCUMENTS_tbl1_221253904)[journals.openedition.org

Measuring the Correctness of Double-Keying: Error Classification and Quality Control in a Large Corpus of TEI-Annotated Historical Text - OpenEdition Journals

 Opens in a new window](https://journals.openedition.org/jtei/739)[journals.openedition.org

Measuring the Correctness of Double-Keying: Error Classification

 Opens in a new window](https://journals.openedition.org/jtei/pdf/739)[computerphilologie.digital-humanities.de

TEI und Textkorpora: Fehlerklassifikation und Qualitätskontrolle vor, während und nach der Texterfassung im Deutschen Textarchiv - Forum Computerphilologie

 Opens in a new window](http://computerphilologie.digital-humanities.de/jg09/geykenetal.pdf)[tei-c.org

Deutsches Textarchiv (The German Text Archive)

 Opens in a new window](https://tei-c.org/activities/projects/deutsches-textarchiv-the-german-text-archive/)[eadh.org

Deutsches Textarchiv | EADH - The European Association for Digital Humanities

 Opens in a new window](https://eadh.org/projects/deutsches-textarchiv)[researchgate.net

Measuring the Correctness of Double-Keying: Error Classification and Quality Control in a Large Corpus of TEI-Annotated Historical Text - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/272430304_Measuring_the_Correctness_of_Double-Keying_Error_Classification_and_Quality_Control_in_a_Large_Corpus_of_TEI-Annotated_Historical_Text)[baeldung.com

Levenshtein Distance Computation | Baeldung on Computer Science

 Opens in a new window](https://www.baeldung.com/cs/levenshtein-distance-computation)[en.wikipedia.org

Levenshtein distance - Wikipedia

 Opens in a new window](https://en.wikipedia.org/wiki/Levenshtein_distance)[en.wikipedia.org

Wagner–Fischer algorithm - Wikipedia

 Opens in a new window](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm)[cs.stackexchange.com

Wagner Fischer Algorithm and the Empty String - Computer Science Stack Exchange

 Opens in a new window](https://cs.stackexchange.com/questions/24005/wagner-fischer-algorithm-and-the-empty-string)[crispinagar.github.io

Levenshtein distance: the similarity of two strings - Crispin Agar

 Opens in a new window](https://crispinagar.github.io/blogs/levenshtein-distance.html)

07_A_review_of_artificial_intelligence_in_herbarium_specimen_image_analysis.pdf

[arxiv.org

Pre-Editorial Normalization for Automatically Transcribed Medieval Manuscripts in Old French and Latin - arXiv

 Opens in a new window](https://arxiv.org/html/2602.13905v1)

02_A_methodological_framework_for_the_use_of_AI_tools_in_automated_workflows_for_ge.pdf

[dokumen.pub

ARGUMENT MINING 9781786303035, 1786303035 - DOKUMEN.PUB

 Opens in a new window](https://dokumen.pub/argument-mining-9781786303035-1786303035.html)[ceur-ws.org

Semi-automatic pipeline for constructing HTR corpora from Ukrainian-language historical documents⋆ - CEUR-WS.org

 Opens in a new window](https://ceur-ws.org/Vol-4159/paper12.pdf)[en.wikipedia.org

Inter-rater reliability - Wikipedia

 Opens in a new window](https://en.wikipedia.org/wiki/Inter-rater_reliability)[pmc.ncbi.nlm.nih.gov

A Tutorial on Sample Size Calculation for Inter-rater and Intra-rater Agreement Studies - PMC

 Opens in a new window](https://pmc.ncbi.nlm.nih.gov/articles/PMC12935580/)[scale.com

Unraveling the Mysteries of Inter-Rater Reliability - Scale AI

 Opens in a new window](https://scale.com/blog/irr)[researchgate.net

(PDF) A Simple Guide to Inter-rater, Intra-rater and Test-retest Reliability for Animal Behaviour Studies - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/356782137_A_Simple_Guide_to_Inter-rater_Intra-rater_and_Test-retest_Reliability_for_Animal_Behaviour_Studies)[frontiersin.org

Evaluation of inter- and intra-rater reliability of video analysis in ski and snowboard cross

 Opens in a new window](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1746697/full)[researchgate.net

(PDF) On Krippendorff's Alpha Coefficient - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/267823285_On_Krippendorff's_Alpha_Coefficient)

04_Tabular_context-aware_optical_character_recognition_and_tabular_data_reconstruct.pdf

05_Pre-Editorial_Normalization_for_Automatically_Transcribed_Medieval_Manuscripts_i.pdf

[adammo12.github.io

124 Survey of Post-OCR Processing Approaches - GitHub Pages

 Opens in a new window](https://adammo12.github.io/adamjatowt/cs21.pdf)[researchgate.net

Assessing the Impact of OCR Quality on Downstream NLP Tasks - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/339848517_Assessing_the_Impact_of_OCR_Quality_on_Downstream_NLP_Tasks)[semanticscholar.org

Assessing the Impact of OCR Quality on Downstream NLP Tasks - Semantic Scholar

 Opens in a new window](https://www.semanticscholar.org/paper/Assessing-the-Impact-of-OCR-Quality-on-Downstream-Strien-Beelen/14531664a554eb4bb8fe8965e83ca149fa047407)[researchgate.net

Handwritten Text Recognition for Documentary Medieval Manuscripts - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/376769268_Handwritten_Text_Recognition_for_Documentary_Medieval_Manuscripts)[journals.openedition.org

Enabling the Encoding of Manuscripts within the DTABf: Extension and Modularization of the Format - OpenEdition Journals

 Opens in a new window](https://journals.openedition.org/jtei/pdf/1650)[journals.openedition.org

The DTA “Base Format”: A TEI Subset for the Compilation of a Large Reference Corpus of Printed Text from Multiple Sources - OpenEdition Journals

 Opens in a new window](https://journals.openedition.org/jtei/1114)[eprints.rclis.org

How Good Can It Get? Analysing and Improving OCR Accuracy in Large Scale Historic Newspaper Digitisation Programs.

 Opens in a new window](http://eprints.rclis.org/12908/1/ANDP__How_Good_Can_it_Get.pdf)[acoustics.asn.au

Speech recognition in noise by using word graph combinations

 Opens in a new window](https://www.acoustics.asn.au/conference_proceedings/ICA2010/cdrom-ICA2010/papers/p341.pdf)[ijournalse.org

Morpheme-Aware Interpolated N-gram Language Modeling for Low-Resource Speech Recognition - Emerging Science Journal

 Opens in a new window](https://ijournalse.org/index.php/ESJ/article/download/4006/1098/14302)

09_Ctc_transcription_alignment_of_the_bullinger_letters_Automatic_improvement_of_an.pdf

06_Reframing_Historical_Text_Extraction_A_Cross-Pathway_Validation_of_OCR,_LLM-Assi.pdf

Sources read but not used in the report
[semanticscholar.org

[PDF] Measuring the Correctness of Double-Keying: Error

 Opens in a new window](https://www.semanticscholar.org/paper/663090873b350b85856b60af211116a67f9dd2a9)[aclanthology.org

Proceedings of the Thirteenth Language Resources and Evaluation Conference - ACL Anthology

 Opens in a new window](https://aclanthology.org/volumes/2022.lrec-1/)[researchgate.net

TextBite: A Historical Czech Document Dataset for Logical Page Segmentation | Request PDF - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/397909329_TextBite_A_Historical_Czech_Document_Dataset_for_Logical_Page_Segmentation)[iris.unitn.it

Developing Language Resources:A Lexical-Diversity-Centric Approach - IRIS

 Opens in a new window](https://iris.unitn.it/retrieve/handle/11572/450650/992219/Thesis_final%20version.pdf)[mdpi.com

Cascade or Direct Speech Translation? A Case Study - MDPI

 Opens in a new window](https://www.mdpi.com/2076-3417/12/3/1097)[aiplusinfo.com

Best Text Annotation Datasets and Tools for Computer Vision - Artificial Intelligence +

 Opens in a new window](https://www.aiplusinfo.com/blog/best-text-annotation-datasets-and-tools-for-computer-vision-to-watch-out-for-in-2022/)[aclanthology.org

Proceedings of the 1st Workshop on NLP for Science (NLP4Science) - ACL Anthology

 Opens in a new window](https://aclanthology.org/2024.nlp4science-1.pdf)[maxqda.com

Intercoder Agreement - MAXQDA

 Opens in a new window](https://www.maxqda.com/help/coding/problem-intercoder-agreement-qualitative-research)[researchgate.net

Interpretation of cohen's kappa | Download Scientific Diagram - ResearchGate

 Opens in a new window](https://www.researchgate.net/figure/Interpretation-of-cohens-kappa_tbl2_364352370)[mathoverflow.net

Proof of dynamic programming calculation of Levenshtein distance - MathOverflow

 Opens in a new window](https://mathoverflow.net/questions/471115/proof-of-dynamic-programming-calculation-of-levenshtein-distance)[rosettacode.org

Levenshtein distance - Rosetta Code

 Opens in a new window](https://rosettacode.org/wiki/Levenshtein_distance)[stackoverflow.com

What's the difference between Levenshtein distance and the Wagner-Fischer algorithm

 Opens in a new window](https://stackoverflow.com/questions/35908166/whats-the-difference-between-levenshtein-distance-and-the-wagner-fischer-algori)[arxiv.org

Leuvenshtein: Efficient FHE-based Edit Distance Computation with Single Bootstrap per Cell - arXiv

 Opens in a new window](https://arxiv.org/pdf/2508.14568)[emergentmind.com

Fleiss' Kappa (κ): A Reliability Metric - Emergent Mind

 Opens in a new window](https://www.emergentmind.com/topics/fleiss-kappa)[researchgate.net

Constructing a Canonicalized Corpus of Historical German by Text

 Opens in a new window](https://www.researchgate.net/publication/257935633_Constructing_a_Canonicalized_Corpus_of_Historical_German_by_Text_Alignment)[researchgate.net

(PDF) Digitizing the Icelandic-Danish Blöndal Dictionary - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/352658012_Digitizing_the_Icelandic-Danish_Blondal_Dictionary)[innovatiana.com

Inter-Annotator Agreement: a key metric in Labeling - Innovatiana

 Opens in a new window](https://www.innovatiana.com/en/post/inter-annotator-agreement)[arxiv.org

 Opens in a new window](https://arxiv.org/html/2506.07707v1)[academia.edu

Read Online: (PDF) Literary Translation in Periodicals - Academia.edu

 Opens in a new window](https://www.academia.edu/90818851/Literary_Translation_in_Periodicals)[kups.ub.uni-koeln.de

Digital Scholarly Editions as Interfaces

 Opens in a new window](https://kups.ub.uni-koeln.de/9085/1/SIDE_12_digital_scholarly_editions_as_interfaces.pdf)[kclpure.kcl.ac.uk

Assessing the Impact of OCR Quality on Downstream NLP Tasks - King's College London

 Opens in a new window](https://kclpure.kcl.ac.uk/portal/en/publications/assessing-the-impact-of-ocr-quality-on-downstream-nlp-tasks/)[repository.cam.ac.uk

Assessing the Impact of OCR Quality on Downstream NLP Tasks - Apollo Repository

 Opens in a new window](https://www.repository.cam.ac.uk/items/ed38e0dc-410a-4431-bbef-f96ff1c0c3db)[emerald.com

Optical character recognition quality affects subjective user perception of historical newspaper clippings | Journal of Documentation - Emerald Insight

 Opens in a new window](https://www.emerald.com/jd/article/79/7/137/194961/Optical-character-recognition-quality-affects)[research.lyrasis.org

Toolkit to assess OCR'ed historical text in the era of big data - LYRASIS Research

 Opens in a new window](https://research.lyrasis.org/bitstreams/1fa5fcfc-0bba-4618-9278-c029710cc0cd/download)[scholar.google.com

‪Kaspar Beelen‬ - ‪Google Scholar‬

 Opens in a new window](https://scholar.google.com/citations?user=PY-yHdwAAAAJ&hl=en)[researchgate.net

Alexander GEYKEN | Berlin-Brandenburg Academy of Sciences and Humanities, Berlin | BBAW | Zentrum Sprache | Research profile - ResearchGate

 Opens in a new window](https://www.researchgate.net/profile/Alexander-Geyken)[computer.org

Towards Understanding the Characteristics of Code Generation Errors Made by Large Language Models - IEEE Computer Society

 Opens in a new window](https://www.computer.org/csdl/proceedings-article/icse/2025/056900a717/251mH51B1AY)[mpi.nl

1.9.2. Editing multiple files and analysis of multiple files

 Opens in a new window](https://www.mpi.nl/corpus/html/elan/ch01s09s02.html)[stackoverflow.com

Multi Label Annotator agreement with Cohen Kappa - Stack Overflow

 Opens in a new window](https://stackoverflow.com/questions/52272901/multi-label-annotator-agreement-with-cohen-kappa)[en.wikipedia.org

Intraclass correlation - Wikipedia

 Opens in a new window](https://en.wikipedia.org/wiki/Intraclass_correlation)[pmc.ncbi.nlm.nih.gov

Prompting large language models and evaluating inter- and intra-rater agreement for cancer progression assessment from radiology reports - PMC

 Opens in a new window](https://pmc.ncbi.nlm.nih.gov/articles/PMC12993880/)[clarin-d.net

Publications - CLARIN-D

 Opens in a new window](https://clarin-d.net/en/about/publications.html)[clarin.bbaw.de

Publikationen - Das CLARIN-Servicezentrum des Zentrums Sprache an der BBAW

 Opens in a new window](https://clarin.bbaw.de/publications)[catalyzex.com

Thibault Clérice - CatalyzeX

 Opens in a new window](https://www.catalyzex.com/author/Thibault%20Cl%C3%A9rice)[aclanthology.org

Rachel Bawden - ACL Anthology

 Opens in a new window](https://aclanthology.org/people/rachel-bawden/)[arxiv.org

[2602.13905] Pre-Editorial Normalization for Automatically Transcribed Medieval Manuscripts in Old French and Latin - arXiv

 Opens in a new window](https://arxiv.org/abs/2602.13905)[aclanthology.org

Proceedings of the Fourth Workshop on Language Technologies for Historical and Ancient Languages (LT4HALA 2026) @ LREC 2026 - ACL Anthology

 Opens in a new window](https://aclanthology.org/volumes/2026.lt4hala-1/)[researchgate.net

(PDF) Pre-Editorial Normalization for Automatically Transcribed

 Opens in a new window](https://www.researchgate.net/publication/400855711_Pre-Editorial_Normalization_for_Automatically_Transcribed_Medieval_Manuscripts_in_Old_French_and_Latin)[almanach.inria.fr

Publications - ALMAnaCH, Inria

 Opens in a new window](https://almanach.inria.fr/publications-en.html)[chatpaper.com

Pre-Editorial Normalization for Automatically ... - ChatPaper

 Opens in a new window](https://chatpaper.com/zh-CN/paper/238130)[sfb1102.uni-saarland.de

Workshop “Making effective use of metadata of historical ... - SFB 1102

 Opens in a new window](https://sfb1102.uni-saarland.de/sfbunisb/uploads/2021/08/MakingEffectiveUse_Abstracts-Workshop-2017.pdf)[journal.dhbenelux.org

Examining a Multi Layered Approach for Classification of OCR ...

 Opens in a new window](https://journal.dhbenelux.org/journal/issues/004/article-3-Cuper.html)
Thoughts

Mapping Core Literature and Concepts

I am reviewing the foundational research and provided literature on text reconciliation, double-keying, and post-recognition correction workflows. My focus is on synthesizing key frameworks across multimodal metadata extraction, pre-editorial normalization, tabular OCR reconstruction, and LLM-assisted handwritten text recognition (HTR) post-correction.

Identifying Methodological Gaps

To build an exhaustive curriculum guide, I am isolating specific technical details that require deeper verification, such as formal mathematical definitions for Character Error Rate (CER), Word Error Rate (WER), and Cohen's Kappa for inter-annotator agreement, alongside historical benchmarking metrics like the Deutsches Textarchiv (DTA) double-keying standards.

Targeting Targeted Case Studies

I am preparing targeted queries to examine specific historical digital humanities initiatives, including the DTA quality assurance guidelines and the IMPACT project protocols. This will help ground the theoretical metrics in practical, real-world editorial workflows.

[eadh.org

Deutsches Textarchiv | EADH - The European Association for Digital Humanities](https://eadh.org/projects/deutsches-textarchiv)[journals.openedition.org

Measuring the Correctness of Double-Keying: Error Classification and Quality Control in a Large Corpus of TEI-Annotated Historical Text - OpenEdition Journals](https://journals.openedition.org/jtei/739)[journals.openedition.org

Measuring the Correctness of Double-Keying: Error Classification](https://journals.openedition.org/jtei/pdf/739)[researchgate.net

Measuring the Correctness of Double-Keying: Error Classification and Quality Control in a Large Corpus of TEI-Annotated Historical Text - ResearchGate](https://www.researchgate.net/publication/272430304_Measuring_the_Correctness_of_Double-Keying_Error_Classification_and_Quality_Control_in_a_Large_Corpus_of_TEI-Annotated_Historical_Text)[tei-c.org

Deutsches Textarchiv (The German Text Archive)](https://tei-c.org/activities/projects/deutsches-textarchiv-the-german-text-archive/)[journals.openedition.org

Enabling the Encoding of Manuscripts within the DTABf: Extension and Modularization of the Format - OpenEdition Journals](https://journals.openedition.org/jtei/pdf/1650)[semanticscholar.org

[PDF] Measuring the Correctness of Double-Keying: Error](https://www.semanticscholar.org/paper/663090873b350b85856b60af211116a67f9dd2a9)[researchgate.net

AVERAGE CHARACTER ACCURACY FOR ALL 17 DOCUMENTS - ResearchGate](https://www.researchgate.net/figure/AVERAGE-CHARACTER-ACCURACY-FOR-ALL-17-DOCUMENTS_tbl1_221253904)[sfb1102.uni-saarland.de

Workshop “Making effective use of metadata of historical texts and corpora” 7-8 September 2017 List of talks and abstracts - SFB 1102](https://sfb1102.uni-saarland.de/sfbunisb/uploads/2021/08/MakingEffectiveUse_Abstracts-Workshop-2017.pdf)[adammo12.github.io

124 Survey of Post-OCR Processing Approaches - GitHub Pages](https://adammo12.github.io/adamjatowt/cs21.pdf)[eprints.rclis.org

How Good Can It Get? Analysing and Improving OCR Accuracy in Large Scale Historic Newspaper Digitisation Programs.](http://eprints.rclis.org/12908/1/ANDP__How_Good_Can_it_Get.pdf)

Historical Digitization Standards Evaluated

Analyzing vendor benchmarks and double-keying workflows reveals that manual double-transcription achieves character accuracy rates between 99.9% and 99.997%. Reviewing quality control frameworks from initiatives like the German Text Archive demonstrates how structural TEI markup and typographical validation are systematically separated to maintain text integrity across large-scale historical collections.

Cost and Error Metrics Synthesized

Comparing manual double-keying against semi-automated HTR and OCR pipelines highlights clear trade-offs between financial cost and transcription accuracy. Evaluating metrics such as Character Error Rate, Word Error Rate, and inter-annotator agreement coefficients like Cohen's Kappa provides a mathematical basis for measuring transcription fidelity and model hallucination risks.

Targeted Methodological Inquiries

Planning additional searches to gather detailed historical formulas and implementation nuances for statistical agreement metrics in manuscript transcription. This will complete the theoretical foundation for comparing human and machine transcription alignments before finalizing the programmatic evaluation tools.

[dokumen.pub

ARGUMENT MINING 9781786303035, 1786303035 - DOKUMEN.PUB](https://dokumen.pub/argument-mining-9781786303035-1786303035.html)[aclanthology.org

Proceedings of the Thirteenth Language Resources and Evaluation Conference - ACL Anthology](https://aclanthology.org/volumes/2022.lrec-1/)[researchgate.net

TextBite: A Historical Czech Document Dataset for Logical Page Segmentation | Request PDF - ResearchGate](https://www.researchgate.net/publication/397909329_TextBite_A_Historical_Czech_Document_Dataset_for_Logical_Page_Segmentation)[ceur-ws.org

Semi-automatic pipeline for constructing HTR corpora from Ukrainian-language historical documents⋆ - CEUR-WS.org](https://ceur-ws.org/Vol-4159/paper12.pdf)[iris.unitn.it

Developing Language Resources:A Lexical-Diversity-Centric Approach - IRIS](https://iris.unitn.it/retrieve/handle/11572/450650/992219/Thesis_final%20version.pdf)[mdpi.com

Cascade or Direct Speech Translation? A Case Study - MDPI](https://www.mdpi.com/2076-3417/12/3/1097)[aiplusinfo.com

Best Text Annotation Datasets and Tools for Computer Vision - Artificial Intelligence +](https://www.aiplusinfo.com/blog/best-text-annotation-datasets-and-tools-for-computer-vision-to-watch-out-for-in-2022/)[aclanthology.org

Proceedings of the 1st Workshop on NLP for Science (NLP4Science) - ACL Anthology](https://aclanthology.org/2024.nlp4science-1.pdf)[pmc.ncbi.nlm.nih.gov

A Tutorial on Sample Size Calculation for Inter-rater and Intra-rater Agreement Studies - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12935580/)[maxqda.com

Intercoder Agreement - MAXQDA](https://www.maxqda.com/help/coding/problem-intercoder-agreement-qualitative-research)[en.wikipedia.org

Inter-rater reliability - Wikipedia](https://en.wikipedia.org/wiki/Inter-rater_reliability)[researchgate.net

Interpretation of cohen's kappa | Download Scientific Diagram - ResearchGate](https://www.researchgate.net/figure/Interpretation-of-cohens-kappa_tbl2_364352370)[arxiv.org

Interaction Analysis by Humans and AI: A Comparative Perspective - arXiv](https://arxiv.org/html/2506.07707v1)

Synthesizing Domain Findings

I am consolidating insights from historical digitization frameworks and recent multimodal research. I observed how vendor accuracy guarantees, pre-editorial normalization models, and post-processing pipelines handle transcription challenges like historical orthography and tabular data layout, highlighting the significant impact that minor character error rates have on downstream natural language processing tasks.

Resolving Evaluation Trade-offs

I am analyzing structural contradictions between automated metric improvements and text integrity. Specifically, I noticed how large language model post-correction can significantly lower word error rates while leaving character error rates unchanged, and how weakly trained line-alignment models can surprisingly outperform overfitted ones when navigating faulty line breaks.

Refining Mathematical Formulations

I am planning targeted searches to verify the exact mathematical recurrence relations and metrics used across alignment algorithms. This includes retrieving formal definitions for dynamic programming matrix alignments, standard error rates, and inter-annotator agreement statistics to ensure complete technical precision in the curriculum.

[baeldung.com

Levenshtein Distance Computation | Baeldung on Computer Science](https://www.baeldung.com/cs/levenshtein-distance-computation)[mathoverflow.net

Proof of dynamic programming calculation of Levenshtein distance - MathOverflow](https://mathoverflow.net/questions/471115/proof-of-dynamic-programming-calculation-of-levenshtein-distance)[cs.stackexchange.com

Wagner Fischer Algorithm and the Empty String - Computer Science Stack Exchange](https://cs.stackexchange.com/questions/24005/wagner-fischer-algorithm-and-the-empty-string)[en.wikipedia.org

Levenshtein distance - Wikipedia](https://en.wikipedia.org/wiki/Levenshtein_distance)[rosettacode.org

Levenshtein distance - Rosetta Code](https://rosettacode.org/wiki/Levenshtein_distance)[crispinagar.github.io

Levenshtein distance: the similarity of two strings - Crispin Agar](https://crispinagar.github.io/blogs/levenshtein-distance.html)[stackoverflow.com

What's the difference between Levenshtein distance and the Wagner-Fischer algorithm](https://stackoverflow.com/questions/35908166/whats-the-difference-between-levenshtein-distance-and-the-wagner-fischer-algori)[en.wikipedia.org

Wagner–Fischer algorithm - Wikipedia](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm)[arxiv.org

Leuvenshtein: Efficient FHE-based Edit Distance Computation with Single Bootstrap per Cell - arXiv](https://arxiv.org/pdf/2508.14568)[emergentmind.com

Fleiss' Kappa (κ): A Reliability Metric - Emergent Mind](https://www.emergentmind.com/topics/fleiss-kappa)

Empirical Double-Keying Failure Modes

Investigating empirical discrepancies between vendor accuracy claims and historical transcription benchmarks reveals distinct failure categories. Differentiating structural markup errors from pure typographical typos provides deeper insight into how double-keying verification systems process XML elements versus standard body text.

Downstream Impacts on NLP Models

Analyzing how pre-editorial normalization influences subsequent computational pipelines shows that uncorrected transcription artifacts propagate non-linearly into downstream tasks. Evaluating these downstream effects illustrates the direct sensitivity of named entity recognition, part-of-speech tagging, and stylometric analysis to initial character-level errors.

Agreement Metrics for Sequential Alignment

Extending traditional inter-annotator agreement metrics like Fleiss' Kappa and Krippendorff's Alpha from discrete categorical labels to continuous string alignments presents unique mathematical challenges. Examining character-by-character tokenization frameworks clarifies how positional displacement impacts statistical reliability calculations across multi-rater transcription datasets.

Deepening Empirical and Mathematical Inquiries

Initiating directed queries to capture specific quantitative studies on double-keying error distributions and mathematical adaptations of reliability coefficients for sequence alignment. This will refine the formal specifications for comparing human double-keying against automated transcription post-correction.

[journals.openedition.org

Measuring the Correctness of Double-Keying: Error Classification](https://journals.openedition.org/jtei/pdf/739)[researchgate.net

Constructing a Canonicalized Corpus of Historical German by Text](https://www.researchgate.net/publication/257935633_Constructing_a_Canonicalized_Corpus_of_Historical_German_by_Text_Alignment)[researchgate.net

Measuring the Correctness of Double-Keying: Error Classification and Quality Control in a Large Corpus of TEI-Annotated Historical Text - ResearchGate](https://www.researchgate.net/publication/272430304_Measuring_the_Correctness_of_Double-Keying_Error_Classification_and_Quality_Control_in_a_Large_Corpus_of_TEI-Annotated_Historical_Text)[academia.edu

Read Online: (PDF) Literary Translation in Periodicals - Academia.edu](https://www.academia.edu/90818851/Literary_Translation_in_Periodicals)[journals.openedition.org

Measuring the Correctness of Double-Keying: Error Classification and Quality Control in a Large Corpus of TEI-Annotated Historical Text - OpenEdition Journals](https://journals.openedition.org/jtei/739)[researchgate.net

AVERAGE CHARACTER ACCURACY FOR ALL 17 DOCUMENTS - ResearchGate](https://www.researchgate.net/figure/AVERAGE-CHARACTER-ACCURACY-FOR-ALL-17-DOCUMENTS_tbl1_221253904)[researchgate.net

(PDF) Digitizing the Icelandic-Danish Blöndal Dictionary - ResearchGate](https://www.researchgate.net/publication/352658012_Digitizing_the_Icelandic-Danish_Blondal_Dictionary)[researchgate.net

(PDF) On Krippendorff's Alpha Coefficient - ResearchGate](https://www.researchgate.net/publication/267823285_On_Krippendorff's_Alpha_Coefficient)[innovatiana.com

Inter-Annotator Agreement: a key metric in Labeling - Innovatiana](https://www.innovatiana.com/en/post/inter-annotator-agreement)

Empirical Transcription Benchmarks Identified

Analyzing large-scale digitization data from the German Text Archive verifies that double-keying achieves accuracy rates near 99.7% at the word level, successfully validating commercial quality claims. Furthermore, reviewing retro-digitization workflows for specialized historical dictionaries demonstrates that most post-OCR errors concentrate within specific structural regions like bold and italicized entry fields, requiring targeted semi-automatic annotation workbenches rather than uniform post-processing.

Agreement Metric Formulations Resolved

Evaluating inter-annotator agreement metrics indicates that calculating Krippendorff's alpha for text transcription can be simplified using agreement tables and distance-based weightings rather than traditional coincidence matrices. This formulation resolves computational complexities associated with resampling while effectively accounting for partial alignment agreements and missing data across human and machine annotators.

Deepening Document Analysis

I am initiating direct source document reviews across primary digitisation reports, survey papers on post-OCR processing, and statistical studies. This deep exploration will extract fine-grained empirical findings regarding manual correction costs, downstream natural language processing impacts, and hybrid human-AI annotation frameworks.

[adammo12.github.io

124 Survey of Post-OCR Processing Approaches - GitHub Pages](https://adammo12.github.io/adamjatowt/cs21.pdf)[arxiv.org](https://arxiv.org/html/2506.07707v1)[eprints.rclis.org

How Good Can It Get? Analysing and Improving ... - E-LIS repository](http://eprints.rclis.org/12908/1/ANDP__How_Good_Can_it_Get.pdf)[pmc.ncbi.nlm.nih.gov

A Tutorial on Sample Size Calculation for Inter-rater and Intra-rater ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC12935580/)[journals.openedition.org

Measuring the Correctness of Double-Keying: Error Classification ...](https://journals.openedition.org/jtei/739)[ceur-ws.org

Semi-automatic pipeline for constructing HTR ... - CEUR-WS.org](https://ceur-ws.org/Vol-4159/paper12.pdf)

Downstream Degradation Thresholds Clarified

Analyzing recent findings on downstream language processing tasks demonstrates that optical character errors impact models non-linearly. Named entity recognition experiences a steep decline in performance once character error rates exceed eight percent, while part-of-speech tagging exhibits a linear error progression starting at a five percent threshold across multi-lingual corpora.

Crowdsourcing and Hybrid Correction Trade-Offs

Evaluating historic newspaper digitisation programs resolves the cost-accuracy contradiction between commercial double-keying and raw machine outputs. Strategic manual correction focused exclusively on titles and initial paragraph lines ensures basic discoverability, while open public crowdsourcing offers a scalable mechanism to remediate full-text body errors over long horizons without prohibitive contractor expenses.

Investigating Consensus Alignment Algorithms

Initiating focused inquiries into multi-engine text reconciliation techniques, including sequence alignment via weighted finite-state transducers, Levenshtein distance alignments, and majority voting models like recognizer output voting for error reduction. These investigations will also examine empirical quality standards from national digitisation guidelines and philological impacts on lemmatization and stylometry.

[journals.openedition.org

Measuring the Correctness of Double-Keying: Error Classification](https://journals.openedition.org/jtei/pdf/739)[computerphilologie.digital-humanities.de

TEI und Textkorpora: Fehlerklassifikation und Qualitätskontrolle vor, während und nach der Texterfassung im Deutschen Textarchiv - Forum Computerphilologie](http://computerphilologie.digital-humanities.de/jg09/geykenetal.pdf)[acoustics.asn.au

Speech recognition in noise by using word graph combinations](https://www.acoustics.asn.au/conference_proceedings/ICA2010/cdrom-ICA2010/papers/p341.pdf)[academia.edu

Read Online: (PDF) Literary Translation in Periodicals - Academia.edu](https://www.academia.edu/90818851/Literary_Translation_in_Periodicals)[kups.ub.uni-koeln.de

Digital Scholarly Editions as Interfaces](https://kups.ub.uni-koeln.de/9085/1/SIDE_12_digital_scholarly_editions_as_interfaces.pdf)[kclpure.kcl.ac.uk

Assessing the Impact of OCR Quality on Downstream NLP Tasks - King's College London](https://kclpure.kcl.ac.uk/portal/en/publications/assessing-the-impact-of-ocr-quality-on-downstream-nlp-tasks/)[semanticscholar.org

Assessing the Impact of OCR Quality on Downstream NLP Tasks - Semantic Scholar](https://www.semanticscholar.org/paper/Assessing-the-Impact-of-OCR-Quality-on-Downstream-Strien-Beelen/14531664a554eb4bb8fe8965e83ca149fa047407)[journal.dhbenelux.org

Examining a Multi Layered Approach for Classification of OCR Quality without Ground Truth](https://journal.dhbenelux.org/journal/issues/004/article-3-Cuper.html)[researchgate.net

Assessing the Impact of OCR Quality on Downstream NLP Tasks - ResearchGate](https://www.researchgate.net/publication/339848517_Assessing_the_Impact_of_OCR_Quality_on_Downstream_NLP_Tasks)[repository.cam.ac.uk

Assessing the Impact of OCR Quality on Downstream NLP Tasks - Apollo Repository](https://www.repository.cam.ac.uk/items/ed38e0dc-410a-4431-bbef-f96ff1c0c3db)[emerald.com

Optical character recognition quality affects subjective user perception of historical newspaper clippings | Journal of Documentation - Emerald Insight](https://www.emerald.com/jd/article/79/7/137/194961/Optical-character-recognition-quality-affects)[research.lyrasis.org

Toolkit to assess OCR'ed historical text in the era of big data - LYRASIS Research](https://research.lyrasis.org/bitstreams/1fa5fcfc-0bba-4618-9278-c029710cc0cd/download)[scholar.google.com

‪Kaspar Beelen‬ - ‪Google Scholar‬](https://scholar.google.com/citations?user=PY-yHdwAAAAJ&hl=en)[researchgate.net

(PDF) Pre-Editorial Normalization for Automatically Transcribed](https://www.researchgate.net/publication/400855711_Pre-Editorial_Normalization_for_Automatically_Transcribed_Medieval_Manuscripts_in_Old_French_and_Latin)[almanach.inria.fr

Publications - ALMAnaCH, Inria](https://almanach.inria.fr/publications-en.html)

Consensus Mechanisms and Normalization Insights

Analyzing multi-engine recognition combination techniques reveals how voting algorithms and confusion networks reconcile outputs from distinct recognition models by preserving hypothesis timing and alignment state graphs. Furthermore, reviewing pre-editorial normalization paradigms highlights how specialized sequence-to-sequence transformer architectures effectively bridge the gap between graphetic manuscript variants and normalized graphemic representations without sacrificing textual fidelity.

Downstream Sensitivities and Error Distributions

Evaluating downstream natural language processing performance on historical digitized texts demonstrates that token-level dictionary lookup rates correlate strongly with string similarity metrics, offering a reliable quality proxy when ground-truth transcripts are absent. However, character-level transcription errors impact downstream tasks unevenly, with sentence segmentation and named entity recognition proving particularly vulnerable to minor OCR degradation compared to document-level topic modeling.

Executing Targeted Algorithmic Verification

I am conducting a focused batch of queries to verify specific mathematical formulations of inter-annotator agreement metrics applied to continuous character strings, alongside detailed classification matrices for typographical versus structural TEI encoding errors. This targeted retrieval will ensure complete formal precision for the multi-engine text consensus and alignment frameworks.

[researchgate.net

Alexander GEYKEN | Berlin-Brandenburg Academy of Sciences and Humanities, Berlin | BBAW | Zentrum Sprache | Research profile - ResearchGate](https://www.researchgate.net/profile/Alexander-Geyken)[journals.openedition.org

The DTA “Base Format”: A TEI Subset for the Compilation of a Large Reference Corpus of Printed Text from Multiple Sources - OpenEdition Journals](https://journals.openedition.org/jtei/1114)[computer.org

Towards Understanding the Characteristics of Code Generation Errors Made by Large Language Models - IEEE Computer Society](https://www.computer.org/csdl/proceedings-article/icse/2025/056900a717/251mH51B1AY)[scale.com

Unraveling the Mysteries of Inter-Rater Reliability - Scale AI](https://scale.com/blog/irr)[mpi.nl

1.9.2. Editing multiple files and analysis of multiple files](https://www.mpi.nl/corpus/html/elan/ch01s09s02.html)[stackoverflow.com

Multi Label Annotator agreement with Cohen Kappa - Stack Overflow](https://stackoverflow.com/questions/52272901/multi-label-annotator-agreement-with-cohen-kappa)[researchgate.net

(PDF) A Simple Guide to Inter-rater, Intra-rater and Test-retest Reliability for Animal Behaviour Studies - ResearchGate](https://www.researchgate.net/publication/356782137_A_Simple_Guide_to_Inter-rater_Intra-rater_and_Test-retest_Reliability_for_Animal_Behaviour_Studies)[en.wikipedia.org

Intraclass correlation - Wikipedia](https://en.wikipedia.org/wiki/Intraclass_correlation)[pmc.ncbi.nlm.nih.gov

Prompting large language models and evaluating inter- and intra-rater agreement for cancer progression assessment from radiology reports - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12993880/)[frontiersin.org

Evaluation of inter- and intra-rater reliability of video analysis in ski and snowboard cross](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1746697/full)[ijournalse.org

Morpheme-Aware Interpolated N-gram Language Modeling for Low-Resource Speech Recognition - Emerging Science Journal](https://ijournalse.org/index.php/ESJ/article/download/4006/1098/14302)

Historical Transcription Standards and Multi-Rater Metrics

Reviewing historical text encoding standards from major German digital archive projects confirms how TEI tag sets and strict controlled vocabularies maintain consistency across multi-source historical corpora. Evaluating statistical agreement measures shows how multi-rater variants like Fleiss' Kappa build upon traditional two-rater models by assuming uniform rating propensities across annotators to handle non-binary agreement distributions.

Resolving Multi-Engine Consensus Challenges

Analyzing multi-model text reconciliation frameworks reveals how speech and text recognition pipelines combine hypotheses from separate recognizers through word-level alignment and voting algorithms to lower word error rates, bridging the gap between raw optical recognition outputs and finalized normalized transcriptions.

Targeted Primary Source Examination

Executing targeted document reviews across digitisation workshop reports and specialized humanities journals to examine double-keying error classification schemes, dictionary-assisted optical character quality metrics, and pre-editorial graphemic normalization models for downstream processing.

[journals.openedition.org

The DTA “Base Format”: A TEI Subset for the Compilation of a Large Reference Corpus of Printed Text from Multiple Sources - OpenEdition Journals](https://journals.openedition.org/jtei/1114)[clarin-d.net

Publications - CLARIN-D](https://clarin-d.net/en/about/publications.html)[clarin.bbaw.de

Publikationen - Das CLARIN-Servicezentrum des Zentrums Sprache an der BBAW](https://clarin.bbaw.de/publications)[catalyzex.com

Thibault Clérice - CatalyzeX](https://www.catalyzex.com/author/Thibault%20Cl%C3%A9rice)[aclanthology.org

Rachel Bawden - ACL Anthology](https://aclanthology.org/people/rachel-bawden/)[arxiv.org

Pre-Editorial Normalization for Automatically Transcribed Medieval Manuscripts in Old French and Latin - arXiv](https://arxiv.org/html/2602.13905v1)[arxiv.org

[2602.13905] Pre-Editorial Normalization for Automatically Transcribed Medieval Manuscripts in Old French and Latin - arXiv](https://arxiv.org/abs/2602.13905)[aclanthology.org

Proceedings of the Fourth Workshop on Language Technologies for Historical and Ancient Languages (LT4HALA 2026) @ LREC 2026 - ACL Anthology](https://aclanthology.org/volumes/2026.lt4hala-1/)[researchgate.net

Handwritten Text Recognition for Documentary Medieval Manuscripts - ResearchGate](https://www.researchgate.net/publication/376769268_Handwritten_Text_Recognition_for_Documentary_Medieval_Manuscripts)[researchgate.net

(PDF) Pre-Editorial Normalization for Automatically Transcribed](https://www.researchgate.net/publication/400855711_Pre-Editorial_Normalization_for_Automatically_Transcribed_Medieval_Manuscripts_in_Old_French_and_Latin)[almanach.inria.fr

Publications - ALMAnaCH, Inria](https://almanach.inria.fr/publications-en.html)[chatpaper.com

Pre-Editorial Normalization for Automatically ... - ChatPaper](https://chatpaper.com/zh-CN/paper/238130)[sfb1102.uni-saarland.de

Workshop “Making effective use of metadata of historical ... - SFB 1102](https://sfb1102.uni-saarland.de/sfbunisb/uploads/2021/08/MakingEffectiveUse_Abstracts-Workshop-2017.pdf)[journal.dhbenelux.org

Examining a Multi Layered Approach for Classification of OCR ...](https://journal.dhbenelux.org/journal/issues/004/article-3-Cuper.html)

Synthesis of Evaluation Frameworks

I am consolidating findings across error metrics, sequence alignment algorithms, and human-AI reconciliation workflows into a unified framework. Analyzing recent developments in pre-editorial normalization and byte-level sequence models reveals how intermediate diplomatic layers can effectively bridge raw historical transcriptions with modern computational pipelines while preserving textual nuance.

Model Trade-Offs and Hallucinations Resolved

Evaluating large language model post-correction performance addresses the tension between overall word accuracy and structural preservation. Findings demonstrate that generative post-processing can significantly improve word error rates without degrading character-level precision, though models remain prone to domain-specific spelling biases and over-normalization if unconstrained by explicit schema validation.

Finalizing Editorial Guidelines

I am preparing the final synthesis, synthesizing practical python implementations for Levenshtein dynamic programming alignment alongside auditing standards for digital editions. The final output will provide a comprehensive pedagogical guide for scholarly editors comparing human double-keying, multi-engine consensus, and language model post-processing.

The initial research has returned a lot of information. I'm sorting through it and organizing it. This will make sure the whole thing flows well and hits all the key points you asked for.

This is it! I’m bringing it all together. Jotting down my final thoughts, polishing everything up, and making sure I give you my very best work.

## References (APA)

1. researchgate.net. (n.d.). *AVERAGE CHARACTER ACCURACY FOR ALL 17 DOCUMENTS*. https://www.researchgate.net/figure/AVERAGE-CHARACTER-ACCURACY-FOR-ALL-17-DOCUMENTS_tbl1_221253904
2. journals.openedition.org. (n.d.). *Measuring the Correctness of Double-Keying: Error Classification and Quality Control in a Large Corpus of TEI-Annotated Historical Text - OpenEdition Journals*. https://journals.openedition.org/jtei/739
3. tei-c.org. (n.d.). *Deutsches Textarchiv (The German Text Archive)*. https://tei-c.org/activities/projects/deutsches-textarchiv-the-german-text-archive/
4. baeldung.com. (n.d.). *Levenshtein Distance Computation | Baeldung on Computer Science*. https://www.baeldung.com/cs/levenshtein-distance-computation
5. en.wikipedia.org. (n.d.). *Levenshtein distance*. https://en.wikipedia.org/wiki/Levenshtein_distance
6. arxiv.org. (n.d.). *Pre-Editorial Normalization for Automatically Transcribed Medieval Manuscripts in Old French and Latin*. https://arxiv.org/html/2602.13905v1
7. en.wikipedia.org. (n.d.). *Inter-rater reliability*. https://en.wikipedia.org/wiki/Inter-rater_reliability
8. researchgate.net. (n.d.). *(PDF) A Simple Guide to Inter-rater, Intra-rater and Test-retest Reliability for Animal Behaviour Studies*. https://www.researchgate.net/publication/356782137_A_Simple_Guide_to_Inter-rater_Intra-rater_and_Test-retest_Reliability_for_Animal_Behaviour_Studies
9. frontiersin.org. (n.d.). *Evaluation of inter- and intra-rater reliability of video analysis in ski and snowboard cross*. https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1746697/full
10. pmc.ncbi.nlm.nih.gov. (n.d.). *A Tutorial on Sample Size Calculation for Inter-rater and Intra-rater Agreement Studies - PMC*. https://pmc.ncbi.nlm.nih.gov/articles/PMC12935580/
11. dokumen.pub. (n.d.). *ARGUMENT MINING 9781786303035, 1786303035 - DOKUMEN.PUB*. https://dokumen.pub/argument-mining-9781786303035-1786303035.html
12. ceur-ws.org. (n.d.). *Semi-automatic pipeline for constructing HTR corpora from Ukrainian-language historical documents⋆ - CEUR-WS.org*. https://ceur-ws.org/Vol-4159/paper12.pdf
13. journals.openedition.org. (n.d.). *Enabling the Encoding of Manuscripts within the DTABf: Extension and Modularization of the Format - OpenEdition Journals*. https://journals.openedition.org/jtei/pdf/1650
14. eadh.org. (n.d.). *Deutsches Textarchiv | EADH - The European Association for Digital Humanities*. https://eadh.org/projects/deutsches-textarchiv
15. researchgate.net. (n.d.). *Measuring the Correctness of Double-Keying: Error Classification and Quality Control in a Large Corpus of TEI-Annotated Historical Text*. https://www.researchgate.net/publication/272430304_Measuring_the_Correctness_of_Double-Keying_Error_Classification_and_Quality_Control_in_a_Large_Corpus_of_TEI-Annotated_Historical_Text
16. aclanthology.org. (n.d.). *Proceedings of the Thirteenth Language Resources and Evaluation Conference - ACL Anthology*. https://aclanthology.org/volumes/2022.lrec-1/
17. researchgate.net. (n.d.). *TextBite: A Historical Czech Document Dataset for Logical Page Segmentation | Request PDF*. https://www.researchgate.net/publication/397909329_TextBite_A_Historical_Czech_Document_Dataset_for_Logical_Page_Segmentation
18. mdpi.com. (n.d.). *Cascade or Direct Speech Translation? A Case Study*. https://www.mdpi.com/2076-3417/12/3/1097

_52 citation marker(s) carried no resolvable source in the DOM and were dropped; see the `*_citations.json` sidecar._
