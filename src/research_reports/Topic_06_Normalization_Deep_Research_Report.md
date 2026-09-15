# Topic 06 (Topic_06_Normalization): Academic Deep Research Report

**Model:** 3.1 Pro (Deep Research)  
**Attachments:** 6 PDF(s)  
**Citations resolved:** 30

## Historical Manuscript Orthographic Normalization

ContentsShare & Export
Create

# Orthographic Variation and Computational Normalization in Historical Manuscripts: A Methodological Evaluation of TEI Encoding, Deterministic Scripts, and AI Models

## 1. Abstract and Executive Summary

The digital turn in textual scholarship has fundamentally altered the epistemological frameworks through which historical manuscripts are transcribed, edited, and analyzed. Central to this paradigm shift is the challenge of orthographic variation. Historical texts—characterized by vast dialectal diversity, phonetic spellings, and idiosyncratic scribal practices—resist the standardized lexicons required by modern natural language processing (NLP) pipelines. Consequently, the computational processing of historical manuscripts necessitates robust normalization strategies. This report investigates the theoretical, methodological, and practical dimensions of orthographic normalization, with a specific focus on iotacism in Hellenistic and Byzantine Greek, and evaluates how these historical variants should be encoded within the Text Encoding Initiative (TEI) framework.

The core thesis advanced in this analysis posits that the editorial normalization of orthographic variants must carefully balance diplomatic fidelity (preserving the "text-as-document") against semantic searchability (enabling the "text-as-work"). To achieve this equilibrium, scholarly editions must deploy TEI's primary source markup mechanisms—specifically the `<choice>`, `<orig>`, `<reg>`, `<sic>`, and `<corr>` elements. Within this encoding environment, deterministic, rule-based transformations provide essential, verifiable baselines. These deterministic scripts act as foundational audit layers against which advanced statistical models, neural machine translation (NMT) systems, and modern Large Language Model (LLM) regularizers must be evaluated.

Recent advancements in deep learning, such as bi-directional Long Short-Term Memory (bi-LSTM) networks and retrieval-augmented generation (RAG) frameworks, demonstrate unprecedented capabilities in context-aware sequence transduction. However, empirical evaluations reveal that these neural architectures introduce significant risks of over-normalization, frequently collapsing vital morphological ambiguities in pursuit of generative fluency. By examining real-world applications across diverse digital humanities infrastructure projects—including the Duke Databank of Documentary Papyri (DDbDP), the Codex Sinaiticus project, and the Old Hungarian Lament of Mary—this analysis constructs a comprehensive pedagogical workflow for digital editors. The evidence indicates that orthographic anomalies are not mere noise to be cleaned; rather, they are carriers of crucial historical, phonological, and sociolinguistic data that must be preserved in the underlying markup and surfaced through sophisticated, multi-layered interfaces.

## 2. Technical, Methodological, and Historical Foundations

To accurately navigate the normalization of historical texts, one must first comprehend the linguistic phenomena that generate orthographic variation, followed by the ontological frameworks utilized to digitally encode them.

### Historical Phonology, Iotacism, and Phonetic Spellings

In historical linguistics, spelling variations frequently reflect profound diachronic shifts in the spoken language. A paramount example within the Greek manuscript tradition is iotacism (or itacism), a phonetic-phonological contact linguistic phenomenon where multiple vowel sounds and diphthongs gradually merged into the single close front unrounded vowel /i/[1].

During the Hellenistic and Roman periods, the Greek vowel system underwent a massive chain shift. Original sounds such as η (/ɛː/), ϵι (/eː/), υ (/y/), oι (/oi/), and υι (/yi/) systematically shifted toward the /i/ phoneme[1]. The relative infrequency of the ancient /iː/ and the overcrowding caused by the new long vowel /eː/ pulled /eː/ towards /iː/. This merger subsequently caused the original /ɛː/ to move toward the position abandoned by /eː/, eventually causing the diphthong /ai/ to monophthongize to /ɛː/[1].

Consequently, scribes writing in Koine Greek began to spell words phonetically. This was particularly prevalent in environments like Hellenistic Egypt, where Greek was often utilized as a second language and was heavily influenced by Egyptian-Coptic phonological transfer[1]. For example, the word τιμη (honor/price) might be written as τιμι, or δϵι (it is necessary) as δι[2].

| Original Classical Grapheme | Classical Phoneme (Approx. 800 BCE) | Hellenistic/Roman Phoneme | Common Scribal Substitutions in Papyri |
| --- | --- | --- | --- |
| ι (iota) | /i/ | /i/ | ϵι,η |
| ϵι (epsilon-iota) | /eː/ | /i/ | ι,η |
| η (eta) | /ɛː/ | /i/ (via /eː/) | ι,ϵι |
| oι (omicron-iota) | /oi/ | /y/ → /i/ | υ |
| υ (upsilon) | /y/ | /y/ → /i/ | oι,ι,η |
| αι (alpha-iota) | /ai/ | /ɛː/ | ϵ |

When encountering these forms in a manuscript, a digital editor faces an epistemological dilemma. Transcribing exactly what is on the page (diplomatic transcription) preserves vital evidence of the scribe's dialect, education level, and the chronological development of the language[3]. Conversely, failing to link these phonetic spellings to their standardized lemmas renders the text invisible to lexical search engines, corpus linguistics tools, and automated morphological parsers[4].

### TEI Chapter 11 Mechanisms: The Dual Ontology of Text

The Text Encoding Initiative (TEI) provides the prevailing international standard for the digital representation of texts. Chapter 11 of the TEI Guidelines details the representation of primary sources, outlining mechanisms to resolve the tension between the physical document and the abstract linguistic work[5]. The TEI architecture accommodates this dual ontology by allowing parallel, multi-layered encodings.

The primary mechanism for managing orthographic variation is the `<choice>` element. As the TEI Guidelines specify, `<choice>` groups a number of alternative encodings for the same point in a text, acknowledging that a full representation requires alternative encodings to be considered parallel rather than mutually exclusive[6]. Within the `<choice>` element, editors deploy specific element pairs depending on the precise nature of the textual variation:

The `<orig>` and `<reg>` (Original and Regularized) pair is utilized when a scribe employs a non-standard spelling that was common, phonetic, or acceptable in their specific historical context[7]. This includes phonetic spellings resulting from iotacism, or archaic dialectal forms. The `<orig>` element contains the diplomatic reading as it appears on the physical substrate, while the `<reg>` element contains the standardized or modernized equivalent[3].

In contrast, the `<sic>` and `<corr>` (Sic and Corrected) pair is reserved strictly for outright errors, blunders, or *lapsus calami*—instances where the scribe wrote something that was unambiguously incorrect even by the grammatical standards of their own time, and which requires editorial emendation to restore the textual archetype[8].

The distinction between `<orig>`/`<reg>` and `<sic>`/`<corr>` is intensely debated in modern textual scholarship. An idiosyncratic spelling might be interpreted as an outright error (`<sic>`) by one editor, or as evidence of an undocumented regional dialect (`<orig>`) by another. By enforcing the use of these distinct semantic tags, TEI XML allows downstream NLP algorithms to target the normalized layer for part-of-speech (POS) tagging and dependency parsing, while allowing historical linguists to query the original layer to study phenomena like vowel chain shifts[3].

Furthermore, Chapter 11 introduces elements such as `<sourceDoc>`, `<surface>`, and `<zone>`, which prioritize the spatial and physical features of the manuscript over its logical textual structure[8]. By combining `<surface>` coordinate mapping with `<choice>` orthographic normalization, the digital edition anchors the abstract linguistic regularization directly to the digitized physical facsimile, ensuring total scholarly transparency.

## 3. Comparative Methodological Evaluation

Transforming raw historical text into a dual-layer TEI XML format requires mapping historical variant spellings to standard contemporary forms. The methodology chosen to automate this complex text-to-text generation task dictates the accuracy, scalability, and scholarly integrity of the resulting corpus.

### Manual Philological Normalization

Historically, textual normalization was performed manually by philologists constructing a critical apparatus. While this approach guarantees high precision and deep contextual understanding, it is fundamentally unscalable for large corpora. Traditional printed critical editions often suppressed orthographic variation entirely, silently correcting forms to classical norms and thereby erasing vital socio-linguistic data[9]. The transition to digital editions mandates a shift from silent correction to explicit, machine-readable markup.

### Deterministic Rule-Based and Regex/Dictionary Scripts

To automate normalization without sacrificing transparency, early computational philology relied on substitution lists, dictionary lookups, and rule-based finite-state transducers (FST). Systems such as VARD 2 for English[10] and Norma for German[10] utilize hand-crafted or automatically derived context-aware replacement rules. In a rule-based system, historical variants are processed through character-replacement rules (e.g., historical `<v>` representing modern `<u>`, or ι mapping to ϵι)[11].

Deterministic scripts operate by generating "rule cores" from training data. For example, comparing the historical German variant *unnuts* to its modern equivalent *unnütz* generates transformation candidates based on edit distance algorithms[12]. These candidates are then pruned using algorithms like PRISM to select the most statistically useful rules[12].

Deterministic systems present several distinct advantages. Rule-based and distance-based metrics (such as the context-sensitive weighted Levenshtein distance) provide highly verifiable outputs[12]. They excel in extremely low-resource environments; research indicates that the Norma tool can achieve over 83% accuracy on English texts with as few as 100 tokens of training data[5]. Furthermore, rule-based scripts act as a transparent baseline. When an FST maps a truncated stem to a normalized form, the exact phonetic or graphemic rule applied is known, mathematically quantifiable, and can be logged in the TEI header.

However, deterministic scripts struggle with context-dependent ambiguity. If a historical spelling can map to multiple modern lemmas based on syntactic context (e.g., the historical English *ther* could represent the modern *their* or *there*), pure dictionary lookups and character-level regex fail to disambiguate, as they process tokens in isolation[12].

### Statistical and Neural Machine Translation (SMT / NMT)

To address contextual ambiguity, researchers framed historical text normalization as a machine translation task—specifically employing character-based statistical machine translation (CSMT) and subsequently character-based neural machine translation (CNMT)[12].

Deep bi-directional Long Short-Term Memory (bi-LSTM) encoder-decoder networks have been extensively evaluated on historical corpora. A bi-LSTM reads the input character sequence in both forward and reverse directions, allowing the model to learn from both the left and right contexts at each timestep[13]. By basing the model on individual characters as input, the vocabulary size remains small, reducing the model's complexity and the amount of data required to train it effectively[13].

NMT models consistently outperform rule-based baselines when sufficient training data is available. In extensive evaluations across diverse languages—including English, German, Hungarian, Icelandic, Spanish, Portuguese, Slovene, and Swedish—NMT models successfully learned complex, non-linear mappings between historical and modern orthographies without requiring hand-crafted lexicons[13]. For instance, on the Anselm corpus of Early New High German, bi-LSTM models achieved an average word accuracy of 80.55%, outperforming conditional random field (CRF) taggers[13].

Data sparsity in historical corpora can be further mitigated using multi-task learning (MTL). By training a sequence-to-sequence model simultaneously on a primary normalization task and an auxiliary task (such as grapheme-to-phoneme mapping or normalization of a related dialect), the shared encoder layers learn robust, language-independent representations[13]. However, empirical results demonstrate that MTL provides the most significant error reduction only when the target dataset is exceptionally small (sparse data scenarios of roughly 5,000 tokens). When abundant target data exists, MTL can sometimes degrade performance due to domain mismatch[14].

### Large Language Models (LLMs) and Generative AI

The advent of Transformer-based Large Language Models (LLMs) in 2024 and 2025 has introduced new paradigms for textual scholarship. LLMs excel at zero-shot and few-shot Named Entity Recognition (NER), POS tagging, and complex normalization without requiring extensive task-specific fine-tuning[15].

LLMs address the severe token-context limitation of older character-based models. By utilizing extensive self-attention mechanisms, an LLM can parse an entire paragraph, recognize the syntactic role of an ambiguous historical spelling, and normalize it correctly[15]. Advanced architectures leverage Retrieval-Augmented Generation (RAG) to ground the LLM's normalizations in external, domain-specific knowledge bases (such as historical lexicons, grammatica, or aligned translations), significantly reducing hallucination rates[16]. Furthermore, LLMs can be prompted to output structured TEI XML natively, generating the `<choice>`, `<orig>`, and `<reg>` tags in a single pass[15].

Despite their power, LLMs pose severe epistemological risks to digital scholarly editions. Generative models are inherently probabilistic; they prioritize fluency over diplomatic fidelity. Without strict architectural constraints, an LLM might "over-normalize" a text—altering valid dialectal syntax or replacing an archaic lexeme with a modern synonym, rather than merely modernizing the orthography[17]. Furthermore, LLMs struggle with the deterministic projection of character-level alignments required for strict TEI markup. Consequently, modern computational philology pipelines propose a hybrid approach: using constrained, rule-based FSTs for deterministic stem and affix normalization, and employing LLMs purely for contextual disambiguation and lacuna detection[18].

### Impact on Downstream NLP Tasks

A critical consideration in evaluating these systems is their utility for downstream tasks. Normalization is rarely an end in itself; it is a vital preprocessing step for POS tagging, morphological parsing, and corpus querying[19]. Research evaluating historical text normalization systems reveals a recurring paradox: while neural models generalize exceptionally well to unseen variant spellings, they do not always provide a clear statistical benefit over a naive memorization baseline for downstream POS tagging[20].

Normalizing text unequivocally yields better tagging accuracy than leaving it in its raw, noisy state[21]. However, aggressive sentence-level neural normalization can incur precision penalties if the model incorrectly splits, merges, or over-corrects tokens that should remain unchanged[22]. Therefore, the evaluation of an AI regularizer must involve auditing its outputs against a verifiable rule-based baseline to ensure that morphological ambiguity is preserved rather than collapsed by generative fluency.

| Normalization Methodology | Primary Mechanism | Strengths | Weaknesses |
| --- | --- | --- | --- |
| **Manual Philology** | Expert human analysis | Perfect contextual accuracy; highly diplomatic. | Unscalable; prone to silent correction in print formats. |
| **Rule-Based Scripts** | Regex, Levenshtein distance, substitution lists | Deterministic; verifiable; excellent in low-resource settings. | Fails to resolve syntactic ambiguity; processes tokens in isolation. |
| **NMT / bi-LSTM** | Character-based sequence-to-sequence translation | Handles non-linear variations well; learns without hand-crafted rules. | Requires training data; struggles with out-of-domain vocabulary. |
| **LLMs + RAG** | Attention mechanisms, retrieval-augmented prompts | Flawless contextual disambiguation; generates native TEI XML. | High risk of over-normalization and hallucination; computationally expensive. |

## 4. Real-World Digital Edition Case Studies

The abstract methodologies discussed above find concrete application in major digital humanities infrastructure projects. An examination of three distinct paradigms reveals how orthographic variation is negotiated, encoded, and analyzed in practice.

### Case Study 1: The Duke Databank of Documentary Papyri (DDbDP) and Papyri.info

Papyrology has long been at the vanguard of the digital humanities. The Papyrological Navigator (PN) at Papyri.info hosts tens of thousands of Greek and Latin documentary texts encoded in EpiDoc, a TEI XML customization designed specifically for epigraphic and papyrological documents[23].

The Greek documentary papyri are fraught with the aforementioned iotacism and phonetic spellings. In older print editions, editors either silently corrected these errors or relegated them to the apparatus criticus (e.g., noting "l. βιβλίδιον" for *lege* βιβλίδιον)[9]. In the EpiDoc schema utilized by the DDbDP, this variation is brought directly into the inline markup, ensuring the preservation of the original text[24].

Using the Leiden+ input syntax, papyrologists encode regularizations seamlessly. For instance, if a papyrus reads `φρόνδεισον` instead of the standard `φρόντισον`, it is entered by the scholar as `<:φρόντισον|reg|φρόνδεισον:>`[7]. The backend translates this into the standard TEI `<choice>` structure:

XML

```
<choice>
 <reg>φρόντισον</reg>
 <orig>φρόνδεισον</orig>
</choice>
```

Conversely, outright scribal mistakes are encoded using the Leiden+ syntax `<:τιμὴν|corr|τμμὴν:>`, which automatically generates a `<choice><corr>...<sic>...` block[7].

This massive repository of TEI-encoded variation has enabled downstream projects like *PapyGreek* and *Trismegistos Text Irregularities* to perform quantitative, algorithmic studies on language change in Greco-Roman Egypt[2]. Because the `<orig>` tags preserve the phonetic data while the `<reg>` tags map to classical lemmas, scholars can digitally isolate all instances where ϵι was substituted for ι preceding a specific consonant class, transforming what was once considered "scribal error" into a goldmine of sociolinguistic data[1].

### Case Study 2: Codex Sinaiticus and Transcription Accuracy

The Codex Sinaiticus, a fourth-century majuscule manuscript of the Greek Bible, highlights the profound intersection of paleography, orthography, and digital representation. The digital edition of the Codex utilizes TEI XML to map the text to high-resolution digital facsimiles, providing transcriptions that capture complex corrections and alterations made by multiple generations of scribes[25].

A central debate surrounding the transmission of Sinaiticus is the "dictation theory"—the hypothesis that portions of the manuscript were copied via dictation rather than visual copying, leading to a high prevalence of phonetic spelling errors[25]. The distinction between a scribe who misreads a visual exemplar and one who mishears a dictated word hinges entirely on orthographic analysis. Iotacism is rampant; the vowel mergers common in the fourth century dictate that dictation would inevitably result in homophonic substitutions[25].

In the digital edition, capturing these substitutions without silently standardizing them is critical for rigorous stemmatic analysis. By utilizing TEI's `<choice>` mechanisms, the digital transcription allows scholars to filter the text dynamically. A user can read the normalized text for theological study, or toggle to the diplomatic transcription to study the lector's accent, the scribe's phonetic idiosyncrasies, and the exact sequence of corrections utilizing the `<del>`, `<add>`, and `<handShift>` elements[26]. The strict separation of the document from the normalized work allows scholars to quantify the orthographic shifts over time.

### Case Study 3: The Old Hungarian Lament of Mary

The processing of early vernacular manuscripts presents unique morphological challenges that test the limits of automated normalization. An analysis of the *Old Hungarian Lament of Mary* (encoded in the Leuven Codex) demonstrates how computational normalization interacts with poetic and semantic structures[18].

In the text, the scribe wrote the word *szegekkel* (with nails) as `ſcegegkel`. A meticulous morphological analysis reveals this is not merely a random misspelling. It reflects a truncated stem where the final vowel dropped out, combined with an archaic graphical variant of the instrumental suffix *-val/-vel* undergoing place assimilation, and a historical phonological change (ηk>g)[18].

If an AI model or a naive stemmer processes `ſcegegkel` without historical context, it might falsely detect plurality (due to the "k") or fail to recognize the root *szeg* (nail). This has profound semantic implications. The Hungarian poem parallels a Latin sequence detailing the Passion of Christ. Where the original Latin variants read either *spinas* (thorns) or *clavos* (nails), the Hungarian translation relies on the root *szeg*. If the normalization pipeline fails and the word is lost or mistranslated by an automated system, the theological emphasis of the text shifts dramatically from the physical brutality of the crucifixion to the mockery of the crown of thorns[18].

To solve this, modern computational pipelines employ a highly orchestrated hybrid approach. A neural sequence converter (Transformer-based HTR) reads the manuscript, a rule-based FST reconstructs the stem and suffix assimilation deterministically, and a noisy channel model (Edit Distance combined with a Trigram Language Model) ranks the candidates[18]. The final output is encoded in highly granular TEI XML that separates the graphemic, phonological, and morphological layers, ensuring that the machine-readable text maintains perfect diplomatic fidelity. Furthermore, alignment-based lacuna detection tools (e.g., UGARIT, CollateX, or LF Aligner) map the Latin *clavos* against the Hungarian text, automatically flagging any structural omissions[18].

## 5. Pedagogical Takeaways & Synthesis for Digital Editors

As the theoretical debate in digital editing shifts from the "text-as-document" paradigm to the "text-as-network" paradigm[27], the curriculum for training undergraduate and graduate digital editors must adapt accordingly. Instructors must convey that computational methods do not render critical editing obsolete; rather, they demand a more rigorous, explicitly formalized editorial logic[28].

### Establishing an Orthographic Decision Log

The cornerstone of a digital textual editing curriculum must be the establishment of a standardized orthographic decision log. Because historical spelling is highly fluid, encoders must document exactly where the boundary lies between a valid linguistic variant (`<orig>`) and an outright error (`<sic>`)[24].

Editors should be taught to implement the following systematic workflow:

1. **Diplomatic Transcription First:** Utilize optical or handwritten text recognition (OCR/HTR) to capture the text exactly as it appears on the physical surface[18].
2. **Algorithmic Candidate Generation:** Run the diplomatic text through a deterministic, rule-based script (e.g., weighted Levenshtein distance or a context-aware regex dictionary) to generate normalization candidates. This creates a verifiable baseline[11].
3. **AI-Assisted Contextual Disambiguation:** Deploy sequence-to-sequence neural models or RAG-enabled LLMs to rank the generated candidates based on sentence-level context[16].
4. **Human-in-the-Loop (HITL) Auditing:** The scholar must manually review cases where the AI model's confidence scoring is low, or where the rule-based baseline conflicts severely with the neural output[29].
5. **TEI XML Projection:** The finalized pairings are injected into the XML tree using the `<choice>` element, ensuring that no historical data is overwritten and that both the document and the work are preserved.

### Guarding Against AI Over-Normalization

A critical pedagogical takeaway is the danger of algorithmic "black boxes." When an LLM is tasked with normalizing a text, it tends to project modern grammatical sensibilities onto historical syntax[17]. Students must be trained to treat neural and LLM regularizers with deep skepticism.

By utilizing TEI's primary source markup where deterministic rule-based transformations provide verifiable baselines, editors create a transparent audit trail. If a neural model converts an archaic regionalism into a modern standard word, the rule-based baseline (which only performs character-level substitution) will flag a massive morphological deviation. This immediately alerts the editor that the AI has crossed the line from orthographic regularization to semantic alteration.

Furthermore, students must understand the structure of the TEI header and metadata declarations. Any automated normalization pipeline applied to a corpus must be extensively documented within the `<encodingDesc>` and `<editorialDecl>` elements of the TEI Header[30]. Future researchers must know precisely whether a specific `<reg>` tag was generated by a human philologist, a deterministic FST, or a neural network, as this provenance dictates the reliability of the data for downstream corpus linguistics.

## 6. Theoretical Synthesis and Technical Integration

The methodological frameworks and technological paradigms explored throughout this report are substantiated by a robust continuum of scholarly literature spanning computational linguistics, papyrology, and digital humanities. The evolution from manual transcription to AI-driven normalization requires a deep synthesis of these overlapping disciplines.

In the domain of historical phonology and papyrology, the foundational analyses provided by Gignac in *A Grammar of the Greek Papyri of the Roman and Byzantine Periods* (1976) continue to anchor our understanding of phenomena such as iotacism and Egyptian-Coptic phonological transfer. This phonetic baseline allows modern digital corpora—such as those maintained by the Duke Databank of Documentary Papyri (DDbDP) and analyzed via Trismegistos—to systematically classify linguistic variation rather than dismissing it as error. The contemporary synthesis of these vowel shifts, notably observed in Dahlgren’s analyses of coarticulation and language contact in Egyptian Greek, relies entirely on the precise XML markup of these ancient texts.

The architectural principles of digital scholarly editions have been subject to intense theoretical debate. The epistemological shift brought about by digital editing has been thoroughly dissected by scholars such as Peter Robinson and Matthew J. Driscoll. In their pivotal volume, *Digital Scholarly Editing: Theories and Practices* (Open Book Publishers, 2016; DOI: 10.11647/OBP.0095), the tension between the "text-as-document" and the "text-as-work" is laid bare. Robinson warns against the reduction of scholarly editing to mere documentary transcription, advocating instead for multi-witness critical editions that leverage digital tools to enhance, rather than replace, traditional philological judgment.

On the computational front, the empirical foundation for automating historical text normalization is extensively mapped by Marcel Bollmann. Bollmann’s comprehensive 2019 study, *A Large-Scale Comparison of Historical Text Normalization Systems* (arXiv:1904.02036), rigorously evaluates rule-based systems, statistical machine translation (SMT), and neural machine translation (NMT) across eight languages. The subsequent exploration of deep bi-directional LSTMs and multi-task learning (MTL) demonstrates that while deep learning captures long-range contextual dependencies, its efficacy is heavily dependent on training data volume. Crucially, MTL proves most beneficial in sparse data scenarios, providing a vital tool for low-resource languages.

The downstream impact of these normalization techniques is critically assessed in the 2018 evaluation by Alexander Robertson and Sharon Goldwater (ACL Anthology: N18-2113). Their findings highlight a crucial limitation: while NMT models achieve high accuracy on unseen historical variants, they do not consistently yield statistically significant improvements in downstream POS tagging compared to naive memorization baselines. This reality underscores the absolute necessity of human-in-the-loop auditing and task-specific fine-tuning.

Finally, the integration of Large Language Models (LLMs) into the digital humanities workflow represents the current methodological frontier. Recent 2024 and 2025 papers on Retrieval-Augmented Generation (RAG) and zero-shot Named Entity Recognition demonstrate that LLMs can process unstructured historical text and project valid TEI XML markup directly. However, the scholarly consensus strongly cautions against the unconstrained use of generative AI. Without strict architectural guardrails—such as those provided by the TEI `<choice>`, `<orig>`, and `<reg>` paradigms—LLMs risk over-normalizing texts, thereby erasing the very morphological and dialectal ambiguities that digital editions seek to preserve.

Ultimately, the synthesis of these linguistic, theoretical, and computational disciplines confirms that the future of digital textual scholarship relies not on replacing the philologist with an algorithm, but on utilizing deterministic scripts and probabilistic AI to enrich the explicit, standard-compliant markup of historical documents.

Sources used in the report
[researchgate.net

Iotacism in Egyptian Greek: Greek-internal development and transfer effect from Egyptian-Coptic - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/398588837_Iotacism_in_Egyptian_Greek_Greek-internal_development_and_transfer_effect_from_Egyptian-Coptic)[brill.com

Chapter 4 Egyptian Greek: A Contact Variety in - Brill

 Opens in a new window](https://brill.com/display/book/9789004508828/BP000005.xml)[helda.helsinki.fi

Phonological Variation in Greek Papyri : Two Case Studies Using PapyGreek Search - Helda - University of Helsinki

 Opens in a new window](https://helda.helsinki.fi/bitstreams/2cd4ede8-bec7-438d-bf4b-6c2ecfc5f81f/download)[archive.org

A grammar of the Greek papyri of the Roman and Byzantine periods : Gignac, Francis T : Free Download, Borrow, and Streaming - Internet Archive

 Opens in a new window](https://archive.org/details/grammarofgreekpa0002gign)[helda.helsinki.fi

Preprocessing Greek Papyri for Linguistic Annotation - HELDA - University of Helsinki

 Opens in a new window](https://helda.helsinki.fi/bitstreams/bc90b56d-c78a-4504-994c-493a4290bf37/download)[grbs.library.duke.edu

Linguistic Variation in Greek Papyri:

 Opens in a new window](https://grbs.library.duke.edu/index.php/grbs/article/download/15245/6561/17149)[researchgate.net

Linguistic Variation in Greek Papyri: Towards a New Tool for Quantitative Study

 Opens in a new window](https://www.researchgate.net/publication/296707789_Linguistic_Variation_in_Greek_Papyri_Towards_a_New_Tool_for_Quantitative_Study)[tei-c.org

11 Representation of Primary Sources - The TEI Guidelines

 Opens in a new window](https://www.tei-c.org/Vault/P5/3.0.0/doc/tei-p5-doc/en/html/PH.html)[sfu.ca

11 Representation of Primary Sources - The TEI Guidelines

 Opens in a new window](https://www.sfu.ca/~takeda/tei-guidelines/issue_2382_eventName/html/PH.html)[tei-c.org

TEI element choice (choice) - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-choice.html)[academia.edu

(PDF) Digital Papyrology I: Methods, Tools and Trends - Academia.edu

 Opens in a new window](https://www.academia.edu/35878624/Digital_Papyrology_I_Methods_Tools_and_Trends)[scholarlypublications.universiteitleiden.nl

Encoding Linguistic Variation in Greek Documentary Papyri: the past, present and future of editorial regularization - Scholarly Publications Leiden University

 Opens in a new window](https://scholarlypublications.universiteitleiden.nl/access/item%3A3567176/download)[researchgate.net

Towards a Theory of Digital Editions | Request PDF - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/334793266_Towards_a_Theory_of_Digital_Editions)

01_Resolving_High-Vowel_Ambiguity_(⟨_ï⟩⟨_i⟩⟨_ı⟩)_in_OCR-Derived_Old_Turkic_Editions.pdf

03_The_identification_of_spelling_variants_in_English_and_German_historical_texts_M.pdf

02_A_large-scale_comparison_of_historical_text_normalization_systems.pdf

06_Computational_approaches_and_the_epistemology_of_scholarly_editing.pdf

07_Improving_historical_spelling_normalization_with_bi-directional_LSTMs_and_multi-.pdf

04_Natural_language_processing_for_historical_texts.pdf

[researchgate.net

Annotating, projecting, and interpreting named entities in digital scholarly editions with LLMs

 Opens in a new window](https://www.researchgate.net/publication/400164750_Annotating_projecting_and_interpreting_named_entities_in_digital_scholarly_editions_with_LLMs)[irep.mbzuai.ac.ae

Retrieval-augmented generation for natural language processing: a survey - MBZUAI iRep

 Opens in a new window](https://irep.mbzuai.ac.ae/bitstreams/2fa1aff9-660b-4393-9174-6b1cf88e41a9/download)[arxiv.org

A Survey on Knowledge-Oriented Retrieval-Augmented Generation - arXiv

 Opens in a new window](https://arxiv.org/html/2503.10677v2)[socialsciencechronicle.com

Narrative Minds and Material Ecologies: Reconfiguring Classical Hermeneutics through Polycentric Classics and Digital Humanities

 Opens in a new window](https://socialsciencechronicle.com/wp-content/uploads/2025-005.pdf)[cambridge.org

How to tag non-standard language: Normalisation versus domain adaptation for Slovene historical and user-generated texts

 Opens in a new window](https://www.cambridge.org/core/journals/natural-language-engineering/article/how-to-tag-nonstandard-language-normalisation-versus-domain-adaptation-for-slovene-historical-and-usergenerated-texts/5C6BE72AE2FD6A7BB78B3F01741C64DF)[semanticscholar.org

Evaluating Historical Text Normalization Systems: How Well Do They Generalize?

 Opens in a new window](https://www.semanticscholar.org/paper/Evaluating-Historical-Text-Normalization-Systems%3A-Robertson-Goldwater/ca008695bc1163d36270ca20c466930f7d86854b)[aclanthology.org

Evaluating Historical Text Normalization Systems: How Well Do They Generalize? - ACL Anthology

 Opens in a new window](https://aclanthology.org/N18-2113.pdf)[journals.openedition.org

POS Tagging and Lemmatization of Historical Varieties of Languages. The Challenge of Old Italian - OpenEdition Journals

 Opens in a new window](https://journals.openedition.org/ijcol/1325)[emergentmind.com

Lexical Normalization in NLP - Emergent Mind

 Opens in a new window](https://www.emergentmind.com/topics/lexical-normalization)[brill.com

Armenian Philology in the Modern Era - Brill

 Opens in a new window](https://brill.com/display/book/9789004270961/9789004270961_webready_content_text.pdf)[dokumen.pub

Armenian Philology in the Modern Era : From Manuscript to Digital Text [1 ed.] 9789004270961, 9789004259942 - DOKUMEN.PUB

 Opens in a new window](https://dokumen.pub/armenian-philology-in-the-modern-era-from-manuscript-to-digital-text-1nbsped-9789004270961-9789004259942.html)[en.wikipedia.org

Text Encoding Initiative - Wikipedia

 Opens in a new window](https://en.wikipedia.org/wiki/Text_Encoding_Initiative)[scribd.com

The Freer Biblical Manuscripts | PDF | Gospels | Ancient Christian Texts - Scribd

 Opens in a new window](https://www.scribd.com/document/336107160/The-Freer-Biblical-Manuscripts)[aai.uni-hamburg.de

Comparative Oriental Manuscript Studies Newsletter No. 5

 Opens in a new window](https://www.aai.uni-hamburg.de/en/comst/pdf/comst-newsletter-5-2013.pdf)[scribd.com

The Freer Biblical Manuscripst. Fresh Studies of An American Treasure Trove PDF - Scribd

 Opens in a new window](https://www.scribd.com/document/460501121/The-Freer-Biblical-Manuscripst-Fresh-Studies-of-an-American-Treasure-Trove-pdf)[brill.com

THE HISTORICAL DEVELOPMENT - Brill

 Opens in a new window](https://brill.com/downloadpdf/book/9789047409700/Bej.9789004151574.i-241_003.xml)[epapers.bham.ac.uk

IGNTP Guidelines for Transcribing Greek Manuscripts using the IGNTP implementation of the Online Transcription Editor

 Opens in a new window](https://epapers.bham.ac.uk/2161/1/Transcription_Editor_Guidelines_1-2.pdf)[msdesc.github.io

TEI P5 Customization and Encoding Guidelines for Manuscript Description - GitHub Pages

 Opens in a new window](https://msdesc.github.io/consolidated-tei-schema/msdesc.html)[kups.ub.uni-koeln.de

Digital Scholarly Editions as Interfaces

 Opens in a new window](https://kups.ub.uni-koeln.de/9118/1/10_witt.pdf)[lirias.kuleuven.be

Andrews - Philology and Critical Edition in the Digital Age-postedit - Lirias

 Opens in a new window](https://lirias.kuleuven.be/retrieve/6e417bf2-dc80-41c3-80fa-4636903962a2)[confident-ai.com

Introduction to Human-in-the-Loop | Confident AI Docs

 Opens in a new window](https://www.confident-ai.com/docs/human-in-the-loop/introduction)[teibyexample.org

Tutorials | Module 2: The TEI Header - TEI by Example

 Opens in a new window](https://teibyexample.org/exist/tutorials/TBED02v00.htm)[guidelines.tei-c.de

TEI: Guidelines for Electronic Text Encoding and Interchange

 Opens in a new window](https://guidelines.tei-c.de/en/html/)
Sources read but not used in the report
[sfu.ca

3 Elements Available in All TEI Documents - The TEI Guidelines - Simon Fraser University

 Opens in a new window](https://www.sfu.ca/~takeda/tei-guidelines/issue_2382_eventName/html/CO.html)[web.uvic.ca

10 Manuscript Description - TEI P5: — Guidelines for Electronic Text Encoding and Interchange

 Opens in a new window](http://web.uvic.ca/lancenrd/martin/guidelines/tei_MS.html)[tei-c.org

Example: - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/Vault/P5//1.7.0/doc/tei-p5-doc/en/html/examples-choice.html)[tei-c.org

Example: - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/examples-choice.html)[tei.org

TEI Manual of Organization & Operation | Tax Executives Institute, Inc.

 Opens in a new window](https://www.tei.org/tei-manual-organization-operation)[backoffice.biblio.ugent.be

10th International colloquium on ancient greek linguistics madrid 2022 - Biblio - Universiteit Gent

 Opens in a new window](https://backoffice.biblio.ugent.be/download/8747590/8747591)[dokumen.pub

Eastern Crossroads: Essays on Medieval Christian Legacy 9781463212827 - dokumen.pub

 Opens in a new window](https://dokumen.pub/eastern-crossroads-essays-on-medieval-christian-legacy-9781463212827-z-7931262.html)[edizioni.libreriauniversitaria.it

storie e linguaggistorie - Edizioni libreriauniversitaria.it

 Opens in a new window](https://edizioni.libreriauniversitaria.it/wp-content/uploads/2024/06/sel_2019-1.pdf)[papyri.info

Text Leiden+ Documentation - Papyri.info

 Opens in a new window](https://papyri.info/docs/leiden_plus)[brillpublishers.gitlab.io

Epidoc · GitBook - GitLab

 Opens in a new window](https://brillpublishers.gitlab.io/documentation-tei-xml/epidoc.html)[papirologia.unipr.it

Nicola Reggiani (Ed.) - DIGITAL PAPYROLOGY II - Papirologia Unipr

 Opens in a new window](http://www.papirologia.unipr.it/ERC/files/reggiani-dp2.pdf)[arxiv.org

From Parliamentary Rhetoric to Enacted Law: An NLP Pipeline for Semantic Auditing of the Greek Legislative Process - arXiv

 Opens in a new window](https://arxiv.org/pdf/2606.00030)[aclanthology.org

Fifteenth Language Resources and Evaluation Conference - ACL Anthology

 Opens in a new window](https://aclanthology.org/events/lrec-2026/)[sighum.wordpress.com

Proceedings of the 10th Joint SIGHUM Workshop on Computational Linguistics for Cultural Heritage, Social Sciences, Humanities an

 Opens in a new window](https://sighum.wordpress.com/wp-content/uploads/2026/03/proceedings.pdf)[anil.recoil.org

AI-assisted Living Evidence Databases for Conservation Science

 Opens in a new window](https://anil.recoil.org/papers/2025-evidence-tap.pdf)[arxiv.org

[1804.02545] Evaluating historical text normalization systems: How well do they generalize?

 Opens in a new window](https://arxiv.org/abs/1804.02545)[homepages.inf.ed.ac.uk

Evaluating historical text normalization systems: How well do they generalize? - Informatics Homepages Server

 Opens in a new window](https://homepages.inf.ed.ac.uk/sgwater/papers/naacl18-textnorm.pdf)[arxiv.org

[1707.05116] To Normalize, or Not to Normalize: The Impact of Normalization on Part-of-Speech Tagging - arXiv

 Opens in a new window](https://arxiv.org/abs/1707.05116)[aclanthology.org

Learning from Within? Comparing PoS Tagging Approaches for Historical Text - ACL Anthology

 Opens in a new window](https://aclanthology.org/L16-1684.pdf)[tei-c.org

11 Manuscript Description - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html)[tei-c.org

11 Representation of Primary Sources - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/Vault/P5//3.5.0/doc/tei-p5-doc/en/html/PH.html)[tei-c.org

3 Elements Available in All TEI Documents - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/Vault/P5/4.1.0/doc/tei-p5-doc/en/html/CO.html)[tei-c.org

23 Documentation Elements - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/release/doc/tei-p5-doc/en/html/TD.html)[livingstoneonline.org

Livingstone Online TEI P5 Encoding Guidelines

 Opens in a new window](https://livingstoneonline.org/resources/livingstone-online-tei-p5-encoding-guidelines)[sfu.ca

TEI element choice (choice)

 Opens in a new window](https://www.sfu.ca/~takeda/tei-guidelines/issue_2382_eventName/html/ref-choice.html)[tei-c.org

3 Elements Available in All TEI Documents - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html)[journals.uchicago.edu

Digital Corpora and Scholarly Editions of Latin Texts: Features and Requirements of Textual Criticism | Speculum: Vol 92, No S1

 Opens in a new window](https://www.journals.uchicago.edu/doi/full/10.1086/693823)[books.openedition.org

12. The Battle We Forgot to Fight: Should We Make a Case for Digital Editions?

 Opens in a new window](https://books.openedition.org/obp/3423?lang=en)[tei-c.org

Electronic Textual Editing: Editors' introduction [ Lou Burnard (Oxford University & Text Encoding Initiative)

 Opens in a new window](https://tei-c.org/Vault/ETE/Preview/intro.html)[scholarlyediting.org

Digital Documentary Editions and the Others - Scholarly Editing

 Opens in a new window](https://www.scholarlyediting.org/2014/essays/essay.pierazzo.html)[paolomonella.it

Why are there no comprehensively digital scholarly editions of classical texts? - Paolo Monella

 Opens in a new window](https://www.paolomonella.it/lincei/files/why/why_paper.pdf)[journals.openedition.org

The Archival Impulse and the Editorial Impulse - OpenEdition Journals

 Opens in a new window](https://journals.openedition.org/variants/570?lang=fr)[scispace.com

12. The Battle We Forgot to Fight: Should We Make a Case for

 Opens in a new window](https://scispace.com/pdf/12-the-battle-we-forgot-to-fight-should-we-make-a-case-for-3wxfclkjaq.pdf)[academia.edu

(PDF) Epigraphic Treebanks: Some Considerations from a Work in

 Opens in a new window](https://www.academia.edu/97594648/Epigraphic_Treebanks_Some_Considerations_from_a_Work_in_Progress)
Thoughts

Framing Editorial Trade-offs and TEI Protocols

I am examining how digital editorial workflows balance diplomatic accuracy against search accessibility when handling historical spelling variations like iotacism. To establish a firm baseline, I am reviewing TEI Chapter 11 guidelines for primary source encoding, focusing on how elements like original readings, regularized forms, and editorial corrections interact within structural choice frameworks.

Comparing Normalization Paradigms and Case Studies

I am comparing deterministic rule-based systems against neural language models to evaluate how each handles morphological ambiguity and prevents over-normalization. To see these approaches in practice, I am investigating digital manuscript initiatives including the Duke Databank of Documentary Papyri, Papyri.info, and the Codex Sinaiticus digital project to see how Leiden+ syntax and TEI representations record phonetic mergers in Hellenistic and Byzantine Greek.

Targeted Information Gathering

I will perform targeted searches to gather specific documentation on TEI XML markup practices for papyrologic texts, historical phonological background on Greek iotacism, and recent empirical research comparing finite-state transducers and large language models for historical text regularization.

[sfu.ca

11 Representation of Primary Sources - The TEI Guidelines](https://www.sfu.ca/~takeda/tei-guidelines/issue_2382_eventName/html/PH.html)[tei-c.org

11 Representation of Primary Sources - The TEI Guidelines](https://www.tei-c.org/Vault/P5/3.0.0/doc/tei-p5-doc/en/html/PH.html)[sfu.ca

3 Elements Available in All TEI Documents - The TEI Guidelines - Simon Fraser University](https://www.sfu.ca/~takeda/tei-guidelines/issue_2382_eventName/html/CO.html)[livingstoneonline.org

Livingstone Online TEI P5 Encoding Guidelines](https://livingstoneonline.org/resources/livingstone-online-tei-p5-encoding-guidelines)[web.uvic.ca

10 Manuscript Description - TEI P5: — Guidelines for Electronic Text Encoding and Interchange](http://web.uvic.ca/lancenrd/martin/guidelines/tei_MS.html)[teibyexample.org

Tutorials | Module 2: The TEI Header - TEI by Example](https://teibyexample.org/exist/tutorials/TBED02v00.htm)[tei-c.org

Example: - Text Encoding Initiative](https://tei-c.org/Vault/P5//1.7.0/doc/tei-p5-doc/en/html/examples-choice.html)[tei-c.org

Example: - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/examples-choice.html)[tei.org

TEI Manual of Organization & Operation | Tax Executives Institute, Inc.](https://www.tei.org/tei-manual-organization-operation)[papyri.info

Text Leiden+ Documentation - Papyri.info](https://papyri.info/docs/leiden_plus)

Investigating Text Encoding Standards for Historical Manuscripts

I am analyzing the specific guidelines and XML structures used in primary source encoding, particularly focusing on how textual variants are structured within the choice element. I examined the distinction between preserving original manuscript readings and applying regularized standard forms or editorial corrections, ensuring clear criteria for distinguishing dialectal orthography from clear scribal errors.

Examining Digital Humanities Workflows for Papyri and Codices

I am exploring real-world implementations of normalization protocols in major digital editions, such as papyrological databases using Leiden syntax mapped to EpiDoc XML and ancient codex digitization projects. This involves evaluating how phonetic shifts like iotacism are represented in diplomatic versus regularized transcriptions to balance linguistic fidelity with digital searchability.

Synthesizing Hybrid Normalization and Auditing Protocols

I am structuring an integrated workflow that combines deterministic finite-state transducers with neural and language-model-driven approaches. Next, I will synthesize these methodologies into a unified editorial framework, detailing decision protocols, automated verification pipelines, and structured encoding standards to prevent artificial hallucinations while maximizing transcription accuracy across historical corpora.

[brill.com

Armenian Philology in the Modern Era - Brill](https://brill.com/display/book/9789004270961/9789004270961_webready_content_text.pdf)[helda.helsinki.fi

Phonological Variation in Greek Papyri : Two Case Studies Using PapyGreek Search - Helda - University of Helsinki](https://helda.helsinki.fi/bitstreams/2cd4ede8-bec7-438d-bf4b-6c2ecfc5f81f/download)[dokumen.pub

Armenian Philology in the Modern Era : From Manuscript to Digital Text [1 ed.] 9789004270961, 9789004259942 - DOKUMEN.PUB](https://dokumen.pub/armenian-philology-in-the-modern-era-from-manuscript-to-digital-text-1nbsped-9789004270961-9789004259942.html)[academia.edu

(PDF) Digital Papyrology I: Methods, Tools and Trends - Academia.edu](https://www.academia.edu/35878624/Digital_Papyrology_I_Methods_Tools_and_Trends)[grbs.library.duke.edu

Linguistic Variation in Greek Papyri:](https://grbs.library.duke.edu/index.php/grbs/article/download/15245/6561/17149)[backoffice.biblio.ugent.be

10th International colloquium on ancient greek linguistics madrid 2022 - Biblio - Universiteit Gent](https://backoffice.biblio.ugent.be/download/8747590/8747591)[scribd.com

The Freer Biblical Manuscripts | PDF | Gospels | Ancient Christian Texts - Scribd](https://www.scribd.com/document/336107160/The-Freer-Biblical-Manuscripts)[brill.com

THE HISTORICAL DEVELOPMENT - Brill](https://brill.com/downloadpdf/book/9789047409700/Bej.9789004151574.i-241_003.xml)[aai.uni-hamburg.de

Comparative Oriental Manuscript Studies Newsletter No. 5](https://www.aai.uni-hamburg.de/en/comst/pdf/comst-newsletter-5-2013.pdf)[papirologia.unipr.it

Nicola Reggiani (Ed.) - DIGITAL PAPYROLOGY II - Papirologia Unipr](http://www.papirologia.unipr.it/ERC/files/reggiani-dp2.pdf)[scribd.com

The Freer Biblical Manuscripst. Fresh Studies of An American Treasure Trove PDF - Scribd](https://www.scribd.com/document/460501121/The-Freer-Biblical-Manuscripst-Fresh-Studies-of-an-American-Treasure-Trove-pdf)[dokumen.pub

Eastern Crossroads: Essays on Medieval Christian Legacy 9781463212827 - dokumen.pub](https://dokumen.pub/eastern-crossroads-essays-on-medieval-christian-legacy-9781463212827-z-7931262.html)[edizioni.libreriauniversitaria.it

storie e linguaggistorie - Edizioni libreriauniversitaria.it](https://edizioni.libreriauniversitaria.it/wp-content/uploads/2024/06/sel_2019-1.pdf)

Examining Digital Papyrology and XML Schemas

I am analyzing how digital papyrology projects such as Papyri.info and PapyGreek leverage EpiDoc XML standards to handle phonetic and morphological deviations. My investigation reveals that embedded regularizations within the primary text allow researchers to conduct quantitative linguistic analyses on phonological contact without sacrificing the underlying diplomatic transcription.

Distinguishing Editorial Corrections from Ancient Scribes

I am resolving structural nuances between modern editorial regularizations and historical scribal corrections. While phonetic shifts like iotacism require paired original and regularized elements to retain manuscript authenticity, ancient physical alterations on the artifact itself are encoded using dedicated scribal correction structures to prevent conflating modern standardization with original scribe activity.

Retrieving Technical Encoding Examples

I will execute targeted searches to retrieve exact XML syntax examples for structural choice markup in papyrological sources, examine specific transcription practices used in major biblical manuscript initiatives, and review recent empirical comparisons on artificial intelligence accuracy and hallucination risks during automated historical text normalization.

[papyri.info

Text Leiden+ Documentation - Papyri.info](https://papyri.info/docs/leiden_plus)[researchgate.net

Linguistic Variation in Greek Papyri: Towards a New Tool for Quantitative Study](https://www.researchgate.net/publication/296707789_Linguistic_Variation_in_Greek_Papyri_Towards_a_New_Tool_for_Quantitative_Study)[helda.helsinki.fi

Preprocessing Greek Papyri for Linguistic Annotation - HELDA - University of Helsinki](https://helda.helsinki.fi/bitstreams/bc90b56d-c78a-4504-994c-493a4290bf37/download)[en.wikipedia.org

Text Encoding Initiative - Wikipedia](https://en.wikipedia.org/wiki/Text_Encoding_Initiative)[brillpublishers.gitlab.io

Epidoc · GitBook - GitLab](https://brillpublishers.gitlab.io/documentation-tei-xml/epidoc.html)[grbs.library.duke.edu

Linguistic Variation in Greek Papyri:](https://grbs.library.duke.edu/index.php/grbs/article/download/15245/6561/17149)[scholarlypublications.universiteitleiden.nl

Encoding Linguistic Variation in Greek Documentary Papyri: the past, present and future of editorial regularization - Scholarly Publications Leiden University](https://scholarlypublications.universiteitleiden.nl/access/item%3A3567176/download)[papirologia.unipr.it

Nicola Reggiani (Ed.) - DIGITAL PAPYROLOGY II - Papirologia Unipr](http://www.papirologia.unipr.it/ERC/files/reggiani-dp2.pdf)[epapers.bham.ac.uk

IGNTP Guidelines for Transcribing Greek Manuscripts using the IGNTP implementation of the Online Transcription Editor](https://epapers.bham.ac.uk/2161/1/Transcription_Editor_Guidelines_1-2.pdf)

Mapping EpiDoc Implementations and Linguistic Datasets

I am reviewing how specialized digital papyrology platforms adapt standard encoding guidelines to manage ancient nonstandard orthography. My examination reveals how databases like the Duke Databank and initiative platforms convert Leiden syntax into structured markup, using designated tag pairings within choice elements to distinguish phonetic variation from modern editorial corrections.

Resolving Papyrological and Computational Frameworks

I am addressing the methodological challenge of separating historical phonological shifts, such as iotacism, from pure scribal mistakes in ancient papyri. By evaluating specialized tools like Sematia and the Trismegistos Text Irregularities database, I am clarifying how dual-layer architectures capture both raw manuscript forms for historical linguistics and standardized forms for lemmatization and syntactic treebanking.

Expanding Empirical Research on Neural Regularization

I am initiating targeted queries to deepen the empirical foundation across language-model-driven text normalization, automated markup generation, and pedagogical digital humanities frameworks. I will search for recent studies on fine-tuning neural architectures, auditing hallucination risks, and establishing structured encoding decision logs for historical text editing.

[irep.mbzuai.ac.ae

Retrieval-augmented generation for natural language processing: a survey - MBZUAI iRep](https://irep.mbzuai.ac.ae/bitstreams/2fa1aff9-660b-4393-9174-6b1cf88e41a9/download)[arxiv.org

From Parliamentary Rhetoric to Enacted Law: An NLP Pipeline for Semantic Auditing of the Greek Legislative Process - arXiv](https://arxiv.org/pdf/2606.00030)[arxiv.org

A Survey on Knowledge-Oriented Retrieval-Augmented Generation - arXiv](https://arxiv.org/html/2503.10677v2)[researchgate.net

Annotating, projecting, and interpreting named entities in digital scholarly editions with LLMs](https://www.researchgate.net/publication/400164750_Annotating_projecting_and_interpreting_named_entities_in_digital_scholarly_editions_with_LLMs)[aclanthology.org

Fifteenth Language Resources and Evaluation Conference - ACL Anthology](https://aclanthology.org/events/lrec-2026/)[sighum.wordpress.com

Proceedings of the 10th Joint SIGHUM Workshop on Computational Linguistics for Cultural Heritage, Social Sciences, Humanities an](https://sighum.wordpress.com/wp-content/uploads/2026/03/proceedings.pdf)[socialsciencechronicle.com

Narrative Minds and Material Ecologies: Reconfiguring Classical Hermeneutics through Polycentric Classics and Digital Humanities](https://socialsciencechronicle.com/wp-content/uploads/2025-005.pdf)[anil.recoil.org

AI-assisted Living Evidence Databases for Conservation Science](https://anil.recoil.org/papers/2025-evidence-tap.pdf)[researchgate.net

Iotacism in Egyptian Greek: Greek-internal development and transfer effect from Egyptian-Coptic - ResearchGate](https://www.researchgate.net/publication/398588837_Iotacism_in_Egyptian_Greek_Greek-internal_development_and_transfer_effect_from_Egyptian-Coptic)[brill.com

Chapter 4 Egyptian Greek: A Contact Variety in - Brill](https://brill.com/display/book/9789004508828/BP000005.xml)[arxiv.org

[1804.02545] Evaluating historical text normalization systems: How well do they generalize?](https://arxiv.org/abs/1804.02545)[aclanthology.org

Evaluating Historical Text Normalization Systems: How Well Do They Generalize? - ACL Anthology](https://aclanthology.org/N18-2113.pdf)[homepages.inf.ed.ac.uk

Evaluating historical text normalization systems: How well do they generalize? - Informatics Homepages Server](https://homepages.inf.ed.ac.uk/sgwater/papers/naacl18-textnorm.pdf)[semanticscholar.org

Evaluating Historical Text Normalization Systems: How Well Do They Generalize?](https://www.semanticscholar.org/paper/Evaluating-Historical-Text-Normalization-Systems%3A-Robertson-Goldwater/ca008695bc1163d36270ca20c466930f7d86854b)[journals.openedition.org

POS Tagging and Lemmatization of Historical Varieties of Languages. The Challenge of Old Italian - OpenEdition Journals](https://journals.openedition.org/ijcol/1325)[arxiv.org

[1707.05116] To Normalize, or Not to Normalize: The Impact of Normalization on Part-of-Speech Tagging - arXiv](https://arxiv.org/abs/1707.05116)[emergentmind.com

Lexical Normalization in NLP - Emergent Mind](https://www.emergentmind.com/topics/lexical-normalization)[aclanthology.org

Learning from Within? Comparing PoS Tagging Approaches for Historical Text - ACL Anthology](https://aclanthology.org/L16-1684.pdf)[cambridge.org

How to tag non-standard language: Normalisation versus domain adaptation for Slovene historical and user-generated texts](https://www.cambridge.org/core/journals/natural-language-engineering/article/how-to-tag-nonstandard-language-normalisation-versus-domain-adaptation-for-slovene-historical-and-usergenerated-texts/5C6BE72AE2FD6A7BB78B3F01741C64DF)[confident-ai.com

Introduction to Human-in-the-Loop | Confident AI Docs](https://www.confident-ai.com/docs/human-in-the-loop/introduction)

Uncovering Neural and Contact Linguistic Models

I am observing how recent neural models and retrieval-augmented frameworks process historical Greek orthography, particularly where language contact between Greek and Egyptian-Coptic drives systematic phonetic variations. The literature shows that large language models require domain-specific fine-tuning or constrained retrieval interfaces to maintain structured TEI markup standards and prevent semantic hallucination when analyzing non-standard manuscript spellings.

Resolving Automation and Structural Encoding Gaps

I am addressing the tension between fully automated machine-learning pipelines and human-in-the-loop scholarly validation when annotating historical texts. By examining multi-stage retrieval setups and digital scholarly editions, I am determining how to balance diplomatic preservation with machine readability, ensuring that automated normalizations do not obscure genuine historical phonology or historical scribal corrections.

Investigating Downstream Tasks and Verification Workflows

I am planning targeted searches to evaluate the downstream impacts of historical text normalization on part-of-speech tagging, parsing accuracy, and named entity recognition. Additionally, I will investigate human-in-the-loop verification architectures, confidence scoring mechanisms, and pedagogical strategies for integrating XML markup and computational philology into digital humanities curricula.

Downstream Impacts of Historical Text Normalization

I am analyzing empirical findings on how automatic spelling normalization affects downstream natural language processing tasks like part-of-speech tagging and parsing. My synthesis indicates that while normalizing historical spelling generally improves tagging accuracy over raw non-canonical text, standard neural architectures do not consistently outperform simpler baseline memory models on seen vocabulary, highlighting the importance of evaluating unseen tokens separately.

Balancing Normalization and Domain Adaptation

I am evaluating the trade-offs between applying explicit text normalization pipelines versus training downstream models directly via domain adaptation on raw historical variants. While pre-processing normalization reduces out-of-vocabulary tokens for standard tools, sentence-level and context-aware approaches provide more resilient improvements for complex downstream annotations without over-correcting valid manuscript forms.

Executing Final Scholarly Searches

I will execute a final targeted search to confirm specific technical details regarding official encoding guidelines for manuscript variations and historical Greek phonological shifts before synthesizing these findings into the comprehensive editorial framework.

[tei-c.org

11 Manuscript Description - The TEI Guidelines - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html)[tei-c.org

11 Representation of Primary Sources - The TEI Guidelines - Text Encoding Initiative](https://tei-c.org/Vault/P5//3.5.0/doc/tei-p5-doc/en/html/PH.html)[guidelines.tei-c.de

TEI: Guidelines for Electronic Text Encoding and Interchange](https://guidelines.tei-c.de/en/html/)[tei-c.org

3 Elements Available in All TEI Documents - The TEI Guidelines - Text Encoding Initiative](https://tei-c.org/Vault/P5/4.1.0/doc/tei-p5-doc/en/html/CO.html)[tei-c.org

TEI element choice (choice) - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-choice.html)[tei-c.org

23 Documentation Elements - The TEI Guidelines - Text Encoding Initiative](https://tei-c.org/release/doc/tei-p5-doc/en/html/TD.html)[livingstoneonline.org

Livingstone Online TEI P5 Encoding Guidelines](https://livingstoneonline.org/resources/livingstone-online-tei-p5-encoding-guidelines)[sfu.ca

TEI element choice (choice)](https://www.sfu.ca/~takeda/tei-guidelines/issue_2382_eventName/html/ref-choice.html)[msdesc.github.io

TEI P5 Customization and Encoding Guidelines for Manuscript Description - GitHub Pages](https://msdesc.github.io/consolidated-tei-schema/msdesc.html)[tei-c.org

3 Elements Available in All TEI Documents - The TEI Guidelines - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html)[archive.org

A grammar of the Greek papyri of the Roman and Byzantine periods : Gignac, Francis T : Free Download, Borrow, and Streaming - Internet Archive](https://archive.org/details/grammarofgreekpa0002gign)

Uncovering Theoretical Debates in Digital Philology

I am exploring foundational theoretical debates surrounding digital scholarly editions, particularly focusing on the tension between diplomatic transcription and normalized representations. Recent scholarly discourse highlights contrasting views on whether aggressive text regularization risks over-simplifying manuscript variance or whether structured XML markup successfully bridges the gap between diplomatic authenticity and computational accessibility.

Resolving Downstream Parsing and Normalization Trade-Offs

I am evaluating how text normalization directly impacts downstream natural language processing tasks such as dependency parsing, part-of-speech tagging, and lemmatization for non-standard historical languages. Synthesizing these insights helps resolve trade-offs between processing raw manuscript forms and normalized readings, showing that dual-layer representation preserves dialectal phonology while improving automated syntactic annotation accuracy.

Conducting Deep Exploration on AI Post-Correction and Criticisms

I will execute targeted searches to investigate transformer-based optical character recognition post-correction for historical manuscripts, examine scholarly criticisms regarding TEI over-normalization, and gather empirical data on how normalization affects dependency treebanking accuracy across ancient languages.

[journals.uchicago.edu

Digital Corpora and Scholarly Editions of Latin Texts: Features and Requirements of Textual Criticism | Speculum: Vol 92, No S1](https://www.journals.uchicago.edu/doi/full/10.1086/693823)[researchgate.net

Towards a Theory of Digital Editions | Request PDF - ResearchGate](https://www.researchgate.net/publication/334793266_Towards_a_Theory_of_Digital_Editions)[books.openedition.org

12. The Battle We Forgot to Fight: Should We Make a Case for Digital Editions?](https://books.openedition.org/obp/3423?lang=en)[tei-c.org

Electronic Textual Editing: Editors' introduction [ Lou Burnard (Oxford University & Text Encoding Initiative)](https://tei-c.org/Vault/ETE/Preview/intro.html)[kups.ub.uni-koeln.de

Digital Scholarly Editions as Interfaces](https://kups.ub.uni-koeln.de/9118/1/10_witt.pdf)[scholarlyediting.org

Digital Documentary Editions and the Others - Scholarly Editing](https://www.scholarlyediting.org/2014/essays/essay.pierazzo.html)[paolomonella.it

Why are there no comprehensively digital scholarly editions of classical texts? - Paolo Monella](https://www.paolomonella.it/lincei/files/why/why_paper.pdf)[journals.openedition.org

The Archival Impulse and the Editorial Impulse - OpenEdition Journals](https://journals.openedition.org/variants/570?lang=fr)[lirias.kuleuven.be

Andrews - Philology and Critical Edition in the Digital Age-postedit - Lirias](https://lirias.kuleuven.be/retrieve/6e417bf2-dc80-41c3-80fa-4636903962a2)[scispace.com

12. The Battle We Forgot to Fight: Should We Make a Case for](https://scispace.com/pdf/12-the-battle-we-forgot-to-fight-should-we-make-a-case-for-3wxfclkjaq.pdf)[academia.edu

(PDF) Epigraphic Treebanks: Some Considerations from a Work in](https://www.academia.edu/97594648/Epigraphic_Treebanks_Some_Considerations_from_a_Work_in_Progress)

Uncovering Theoretical Debates in Digital Scholarly Editing

I am examining the ongoing theoretical debate between document-centric and work-centric digital editions. Recent scholarship highlights how early digital practices often privileged diplomatic transcriptions of individual documents over multi-witness critical editions, prompting calls to reconnect digital encoding with traditional textual criticism and prevent digital editions from becoming mere digital representations of printed books.

Resolving Tooling Dependency and Data-Interface Decoupling

I am clarifying how customized TEI markup practices create dependencies on specialized software and prevent long-term sustainability across digital projects. Re-evaluating these workflows demonstrates the need to decouple underlying encoded textual data from frontend user interfaces, enabling reusable API-driven displays while maintaining rigorous scholarly standards across both diplomatic and critical perspectives.

Concluding the Research Phase

Having completed extensive exploration across theoretical frameworks, text encoding schemas, neural normalization pipelines, and downstream annotation impact, I am finalizing the research process and transitioning to synthesizing the full academic report.

The initial research has returned a lot of information. I'm sorting through it and organizing it. This will make sure the whole thing flows well and hits all the key points you asked for.

This is it! I’m bringing it all together. Jotting down my final thoughts, polishing everything up, and making sure I give you my very best work.

## References (APA)

1. researchgate.net. (n.d.). *Iotacism in Egyptian Greek: Greek-internal development and transfer effect from Egyptian-Coptic*. https://www.researchgate.net/publication/398588837_Iotacism_in_Egyptian_Greek_Greek-internal_development_and_transfer_effect_from_Egyptian-Coptic
2. helda.helsinki.fi. (n.d.). *Phonological Variation in Greek Papyri : Two Case Studies Using PapyGreek Search - Helda - University of Helsinki*. https://helda.helsinki.fi/bitstreams/2cd4ede8-bec7-438d-bf4b-6c2ecfc5f81f/download
3. helda.helsinki.fi. (n.d.). *Preprocessing Greek Papyri for Linguistic Annotation - HELDA - University of Helsinki*. https://helda.helsinki.fi/bitstreams/bc90b56d-c78a-4504-994c-493a4290bf37/download
4. grbs.library.duke.edu. (n.d.). *Linguistic Variation in Greek Papyri:*. https://grbs.library.duke.edu/index.php/grbs/article/download/15245/6561/17149
5. tei-c.org. (n.d.). *11 Representation of Primary Sources - The TEI Guidelines*. https://www.tei-c.org/Vault/P5/3.0.0/doc/tei-p5-doc/en/html/PH.html
6. tei-c.org. (n.d.). *TEI element choice (choice) - Text Encoding Initiative*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-choice.html
7. academia.edu. (n.d.). *(PDF) Digital Papyrology I: Methods, Tools and Trends - Academia.edu*. https://www.academia.edu/35878624/Digital_Papyrology_I_Methods_Tools_and_Trends
8. sfu.ca. (n.d.). *11 Representation of Primary Sources - The TEI Guidelines*. https://www.sfu.ca/~takeda/tei-guidelines/issue_2382_eventName/html/PH.html
9. scholarlypublications.universiteitleiden.nl. (n.d.). *Encoding Linguistic Variation in Greek Documentary Papyri: the past, present and future of editorial regularization - Scholarly Publications Leiden University*. https://scholarlypublications.universiteitleiden.nl/access/item%3A3567176/download
10. researchgate.net. (n.d.). *Annotating, projecting, and interpreting named entities in digital scholarly editions with LLMs*. https://www.researchgate.net/publication/400164750_Annotating_projecting_and_interpreting_named_entities_in_digital_scholarly_editions_with_LLMs
11. arxiv.org. (n.d.). *A Survey on Knowledge-Oriented Retrieval-Augmented Generation*. https://arxiv.org/html/2503.10677v2
12. irep.mbzuai.ac.ae. (n.d.). *Retrieval-augmented generation for natural language processing: a survey - MBZUAI iRep*. https://irep.mbzuai.ac.ae/bitstreams/2fa1aff9-660b-4393-9174-6b1cf88e41a9/download
13. socialsciencechronicle.com. (n.d.). *Narrative Minds and Material Ecologies: Reconfiguring Classical Hermeneutics through Polycentric Classics and Digital Humanities*. https://socialsciencechronicle.com/wp-content/uploads/2025-005.pdf
14. cambridge.org. (n.d.). *How to tag non-standard language: Normalisation versus domain adaptation for Slovene historical and user-generated texts*. https://www.cambridge.org/core/journals/natural-language-engineering/article/how-to-tag-nonstandard-language-normalisation-versus-domain-adaptation-for-slovene-historical-and-usergenerated-texts/5C6BE72AE2FD6A7BB78B3F01741C64DF
15. aclanthology.org. (n.d.). *Evaluating Historical Text Normalization Systems: How Well Do They Generalize? - ACL Anthology*. https://aclanthology.org/N18-2113.pdf
16. journals.openedition.org. (n.d.). *POS Tagging and Lemmatization of Historical Varieties of Languages. The Challenge of Old Italian - OpenEdition Journals*. https://journals.openedition.org/ijcol/1325
17. brill.com. (n.d.). *Armenian Philology in the Modern Era*. https://brill.com/display/book/9789004270961/9789004270961_webready_content_text.pdf
18. semanticscholar.org. (n.d.). *Evaluating Historical Text Normalization Systems: How Well Do They Generalize?*. https://www.semanticscholar.org/paper/Evaluating-Historical-Text-Normalization-Systems%3A-Robertson-Goldwater/ca008695bc1163d36270ca20c466930f7d86854b
19. dokumen.pub. (n.d.). *Armenian Philology in the Modern Era : From Manuscript to Digital Text [1 ed.] 9789004270961, 9789004259942 - DOKUMEN.PUB*. https://dokumen.pub/armenian-philology-in-the-modern-era-from-manuscript-to-digital-text-1nbsped-9789004270961-9789004259942.html
20. en.wikipedia.org. (n.d.). *Text Encoding Initiative*. https://en.wikipedia.org/wiki/Text_Encoding_Initiative
21. scribd.com. (n.d.). *The Freer Biblical Manuscripts | PDF | Gospels | Ancient Christian Texts*. https://www.scribd.com/document/336107160/The-Freer-Biblical-Manuscripts
22. scribd.com. (n.d.). *The Freer Biblical Manuscripst. Fresh Studies of An American Treasure Trove PDF*. https://www.scribd.com/document/460501121/The-Freer-Biblical-Manuscripst-Fresh-Studies-of-an-American-Treasure-Trove-pdf
23. brill.com. (n.d.). *THE HISTORICAL DEVELOPMENT*. https://brill.com/downloadpdf/book/9789047409700/Bej.9789004151574.i-241_003.xml
24. researchgate.net. (n.d.). *Linguistic Variation in Greek Papyri: Towards a New Tool for Quantitative Study*. https://www.researchgate.net/publication/296707789_Linguistic_Variation_in_Greek_Papyri_Towards_a_New_Tool_for_Quantitative_Study
25. kups.ub.uni-koeln.de. (n.d.). *Digital Scholarly Editions as Interfaces*. https://kups.ub.uni-koeln.de/9118/1/10_witt.pdf
26. guidelines.tei-c.de. (n.d.). *TEI: Guidelines for Electronic Text Encoding and Interchange*. https://guidelines.tei-c.de/en/html/
27. web.uvic.ca. (n.d.). *10 Manuscript Description - TEI P5: — Guidelines for Electronic Text Encoding and Interchange*. http://web.uvic.ca/lancenrd/martin/guidelines/tei_MS.html
28. tei-c.org. (n.d.). *Example: - Text Encoding Initiative*. https://tei-c.org/Vault/P5//1.7.0/doc/tei-p5-doc/en/html/examples-choice.html
29. tei-c.org. (n.d.). *Example: - Text Encoding Initiative*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/examples-choice.html
30. tei.org. (n.d.). *TEI Manual of Organization & Operation | Tax Executives Institute, Inc*. https://www.tei.org/tei-manual-organization-operation

_44 citation marker(s) carried no resolvable source in the DOM and were dropped; see the `*_citations.json` sidecar._
