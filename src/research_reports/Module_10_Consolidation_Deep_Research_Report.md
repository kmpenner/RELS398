# Topic 10 (Topic_10_Consolidation): Academic Deep Research Report

**Model:** 3.1 Pro (Deep Research)  
**Attachments:** 6 PDF(s)  
**Citations resolved:** 32

## Digital Humanities Collaborative Workflows Report

ContentsShare & Export
Create

# Collaborative Workflows, XML Schema Validation, and Structured Peer Review in Digital Scholarly Editing

## Abstract and Executive Summary

The transition of textual scholarship from print-centric paradigms to digital scholarly editing fundamentally alters the infrastructure, ontology, and collaborative potential of the humanistic text. Historically, the creation of digital editions relied on solitary editors or highly centralized teams working within localized software environments. This approach often resulted in fragmented, idiosyncratic data architectures that succumbed rapidly to digital entropy, rendering editions obsolete as proprietary software environments degraded. However, the contemporary landscape of the digital humanities is increasingly defined by a synthesis of distributed version control, rigorous automated quality assurance, and community-driven peer review. This report investigates the intersection of GitHub collaborative workflows—encompassing forks, pull requests, and issue tracking—with robust XML and Schematron schema validation, examining how these integrated systems enhance data integrity, ensure sustainable publication, and elevate pedagogical efficacy in digital scholarly editing curricula.

The core thesis substantiated throughout this analysis posits that cumulative digital scholarly editions require structured mid-project consolidation, which is optimally achieved by combining distributed GitHub workflows with automated continuous integration (CI) pipelines. By embedding XML and Schematron validation engines into these pipelines, projects can ensure strict adherence to the Text Encoding Initiative (TEI) guidelines, automatically detect encoding inconsistencies, enforce complex business rules, and eliminate the catastrophic introduction of malformed data into canonical repositories. Simultaneously, this architecture transforms the editorial process into a transparent, reproducible, and highly collaborative pedagogical environment. Rather than treating validation and version control merely as post-production archiving steps, modern digital methods position them as active interfaces where students and scholars engage in iterative, structured scholarly critique. Through a detailed examination of the theoretical foundations of markup languages, the technical implementation of continuous integration, and real-world case studies—including the Scholastic Commentaries and Texts Archive (SCTA), the E-LAUTE multimodal edition, the FIHRIST manuscript catalogue, and the minimal computing principles of the Endings Project—this report provides a comprehensive blueprint for deploying robust, sustainable, and pedagogically sound digital editing workflows.

## Technical and Historical Foundations of Digital Editing

To fully grasp the efficacy of modern distributed workflows in digital scholarly editing, it is necessary to examine the historical, theoretical, and technical foundations that necessitate such complex infrastructures. This requires a deep exploration of textual ontology in the digital sphere, the evolution of version control, and the precise mathematical and logical mechanisms of XML validation.

### The OHCO Thesis and the Ontology of the Digital Text

The Text Encoding Initiative (TEI) has served as the definitive standard for the representation of texts in digital form for over three decades, providing a comprehensive vocabulary for marking up structural, semantic, and philological phenomena[1]. At its theoretical inception, the TEI was heavily influenced by a conceptual model of textuality known as the Ordered Hierarchy of Content Objects (OHCO)[2]. Formulated by Allen Renear, Steven DeRose, and David Durand in the early 1990s, the OHCO thesis postulates that a text is not merely a sequence of characters on a physical artifact, but a logical, hierarchical structure composed of nesting elements[3]. Under this framework, books contain chapters, chapters contain paragraphs, and paragraphs contain sentences and words[4]. This ontological assumption maps perfectly onto the hierarchical tree structure of Extensible Markup Language (XML), making TEI/XML an exceptionally powerful tool for descriptive markup[4].

Despite its utility, the OHCO model possesses significant theoretical and practical limitations when applied to the full complexity of historical artifacts[5]. Jerome McGann and others have critiqued the OHCO model, arguing that texts operate as "autopoietic systems" wherein ambiguity, fluid composition, and overlapping physical realities resist reduction into singular hierarchical trees[2]. Texts are rarely perfectly hierarchical; a medieval manuscript, for instance, exhibits overlapping hierarchies where the logical structure of a poem (stanzas and lines) often conflicts with the physical structure of the codex (quires, folios, and columns)[6]. If a stanza crosses a page boundary, the strict XML tree structure is violated because XML parsers require elements to nest cleanly without intersection[7].

To circumvent the limitations of the OHCO model, digital philologists developed sophisticated mechanisms. Stand-off markup, wherein structural annotations are stored separately from the primary text string and linked via XPath pointers, allows multiple competing hierarchies to coexist without violating XML syntax rules[4]. Empty milestone elements (such as `<pb/>` for page breaks) are utilized to mark physical boundaries within a logical stream without breaking the tree[7]. Furthermore, scholars have increasingly argued for a paradigm shift from a "text-as-document" approach—which focuses entirely on representing a single physical artifact—to a "text-as-network" paradigm, leveraging Linked Open Data (LOD) to represent the highly interconnected nature of historical corpora, treating texts as a series of data points and relationships rather than isolated hierarchies[8]. These advanced markup strategies exponentially increase the complexity of the encoded data, thereby necessitating rigorous, automated validation mechanisms to ensure structural integrity and prevent human error during the encoding process.

### The Evolution of Distributed Version Control

Historically, collaborative textual editing suffered from what scholars term the "fallacy of prescience," a scenario requiring editors to define rigid structures before fully understanding the text, which made simultaneous collaboration across a team highly precarious[6]. The adoption of Git—a distributed version control system originally designed for software engineering—has revolutionized collaborative digital humanities by solving this exact problem[9]. Unlike centralized systems that rely on a single server to dictate the current state of a project, Git provides every contributor with a complete, independent local copy of the repository, including its entire historical timeline[10].

In a distributed version control architecture, data provenance is maintained through cryptographic hashes, ensuring that every historical state of a text is permanently addressable and immutable[11]. This provides a profound advantage for scholarly editing by entirely eliminating the fear of irreversible data loss, thereby encouraging experimentation and allowing editors to track the exact genesis of every textual emendation[9]. Platforms like GitHub, GitLab, and Bitbucket extend this architecture by introducing the "fork-and-pull" model. A scholar or student can "fork" (copy) a master repository, make localized edits to the TEI XML files on a separate branch, and subsequently issue a "pull request" to merge their changes back into the authoritative corpus[9]. This architecture inherently decentralizes the editorial process, shifting the paradigm from solitary curation to asynchronous, massive, community-driven collaboration[12].

### Schema Validation: Grammar vs. Rule-Based Engines

Ensuring the integrity of highly complex TEI XML documents requires a multi-tiered validation approach. The foundational tier is syntax checking, which merely ensures the XML is well-formed (i.e., all tags are properly closed, and namespaces are declared)[13]. The second tier relies on grammar-based schema languages, such as Document Type Definitions (DTD), W3C XML Schema (XSD), or RELAX NG[13]. RELAX NG is the preferred grammar for TEI projects; it excels at enforcing structural constraints, dictating, for example, that a `<teiHeader>` must contain a `<fileDesc>`, and that a `<listWit>` must only contain `<witness>` elements[14].

However, grammar-based schemas are inherently limited; they cannot validate context-dependent "business rules" or complex co-occurrence constraints across a document tree[15]. To address this structural blindness, digital scholarly editions rely on Schematron, standardized globally as ISO/IEC 19757-3[15]. Schematron is a rule-based validation language that utilizes the XPath query language to make specific assertions about the presence, absence, or relationship of patterns within an XML tree[16]. While RELAX NG defines the geometric shape of the document, Schematron defines the conditional logic the document must satisfy[17].

| Validation Technology | Mechanism of Action | Scholarly Editing Application |
| --- | --- | --- |
| **Standard XML Parser** | Validates basic syntax (well-formedness). | Prevents broken tags or missing closing brackets from crashing the publication platform. |
| **RELAX NG / DTD** | Validates structural grammar and parent-child element relationships. | Ensures a `<teiHeader>` contains required metadata fields like `<titleStmt>` and `<publicationStmt>`. |
| **ISO Schematron** | Validates conditional logic, co-occurrence constraints, and relationships via XPath. | Asserts that an `@xml:id` is unique, or that if `@type="translation"`, the `@xml:lang` does not match the source text language. |
| **XPath 2.0 / 3.0** | Traverses the document tree to evaluate the context of specific nodes. | Locates all `<ref>` elements and ensures their `@target` attributes resolve to a valid identifier elsewhere in the repository. |

In advanced TEI workflows, Schematron rules are frequently embedded directly within ODD (One Document Does it all) customization files, ensuring that the project's documentation and its validation logic are generated from the exact same source[10]. Schematron logic is articulated using three primary elements: `<sch:rule>` to establish the context node, `<sch:assert>` to trigger a validation error if its XPath test evaluates to false, and `<sch:report>` to trigger a message if its test evaluates to true[17]. Processing these complex XPath assertions typically requires an XSLT engine, such as Saxon, which compiles the Schematron XML into an XSLT stylesheet that can be executed against the target document[18]. The output of this compilation is a Schematron Validation Report Language (SVRL) file, which provides a machine-readable list of every assertion that failed[18].

## Applied Implementation and Editorial Dimensions

Deploying distributed version control and automated validation in a digital humanities project fundamentally alters the day-to-day editorial workflow. Transitioning from isolated desktop software to a networked ecosystem requires meticulous management of forks, the design of structured peer-review protocols, specialized strategies for conflict resolution, and the calibration of automated linting environments.

### Pull Requests as the Modern Apparatus Criticus

In traditional digital editions, textual review often consisted of exchanging Word documents or isolated XML files via email, leading to severe versioning crises, lost data, and overwritten files. The GitHub fork-and-pull model formalizes and streamlines this process into a highly visible, asynchronous conversation[9]. The primary project repository acts as the authoritative "canon." Individual researchers, students, or crowdsourcing volunteers fork this repository to their personal accounts. Working on isolated feature branches, they encode the text using software like Oxygen XML Editor or lightweight browser-based tools[1].

Upon completing a distinct unit of work—such as transcribing a single manuscript folio or generating a prosopographical index—the contributor initiates a pull request (PR). The PR interface provides a precise, line-by-line visualization (a "diff") of every addition, deletion, and modification[9]. This diff visualization is paramount for philological review. Senior editors or peer reviewers can leave inline comments directly on specific XML tags, questioning an editorial emendation or correcting a transcription error[9]. The contributor can then push further commits to the same branch to address the feedback, updating the PR dynamically without needing to generate new files. This iterative loop transforms the PR from a mere administrative mechanism into a vibrant forum for scholarly debate, essentially serving as a dynamic, interactive apparatus criticus[9]. Furthermore, GitHub Issues act as the modern equivalent of scholarly marginalia, allowing teams to track encoding bugs, debate interpretation guidelines, and establish editorial consensus transparently[19].

### Automated Linting and Continuous Integration Pipelines

To alleviate the immense cognitive load on human reviewers, routine quality control must be delegated to automated linting via Continuous Integration (CI) pipelines. CI is a DevOps practice wherein code changes are automatically built and tested whenever they are committed to a shared repository[9]. In the context of digital scholarly editing, CI platforms like GitHub Actions or Travis CI act as tireless, automated editorial assistants[9].

When an editor submits a pull request containing modified TEI XML files, the CI pipeline is triggered automatically. The pipeline provisions a virtual container, installs required dependencies (such as Java, Jing, and Saxon), and runs the modified files against the project's RELAX NG and Schematron schemas[20]. Tools specifically designed for this workflow, such as the `xml-model-validator` or `dracor-validate-action`, parse `xml-model` processing instructions directly from the XML files, download the appropriate schemas, and execute the validations[20].

If the validation fails, the pull request is blocked from being merged, ensuring that malformed data cannot pollute the production repository[11]. Crucially, the CI runner intercepts these failures and translates the SVRL output into inline GitHub annotations[20]. Consequently, an encoder does not need to parse a cryptic terminal output on their local machine; instead, they see a highly contextualized error message directly alongside their code on GitHub, vastly accelerating the debugging and learning process[20]. A highly optimized CI pipeline in a DSE project typically executes several discrete stages before allowing a merge, including syntax checking, grammar validation, business logic enforcement, and a dry-run transformation to ensure the final HTML compiles correctly[11].

### Resolving Encoding Merge Conflicts in Tree Structures

A significant challenge in distributed textual editing is the resolution of merge conflicts, which occur when two contributors alter the exact same line of a TEI document simultaneously[1]. Because XML relies on an ordered, perfectly nesting hierarchy, improperly resolved merge conflicts can easily break the document's well-formedness by severing opening and closing tags, rendering the entire document unparsable[13].

In a collaborative environment, teaching contributors how to read Git conflict markers and manually reconcile overlapping markup is critical. Modern XML editors equipped with Git integrations provide visual merge tools that render the conflicting XML trees side-by-side, highlighting where the OHCO hierarchy is threatened[13]. Best practices in workflow design mitigate merge conflicts by modularizing the text. Rather than housing an entire manuscript in a single monolithic XML file, the text is divided into smaller files (e.g., one file per chapter, folio, or act) and synthesized virtually using the W3C XInclude (`<xi:include>`) standard[21]. This modularity drastically reduces the probability of simultaneous edits colliding on the same exact node, allowing multiple editors to work on the same larger work concurrently.

### Designing Structured Peer-Review Rubrics for TEI XML

While automated CI pipelines excel at catching structural and syntactic errors, they cannot evaluate scholarly judgment, historical accuracy, or interpretive nuance[22]. An automated pipeline can confirm that a `<persName>` tag is syntactically valid, but it cannot determine if the scholar identified the correct historical figure. Therefore, the CI pipeline must be complemented by structured human peer review. Within a pedagogical setting or a crowdsourced project, reviewers require explicit rubrics to evaluate the quality of a TEI XML submission effectively.

A robust TEI peer-review rubric bridges the technical and the humanistic. It prompts the reviewer to assess whether the encoder appropriately utilized semantic tags, whether editorial interventions (such as `<corr>` for corrections or `<supplied>` for illegible text) are adequately justified by the manuscript evidence, and whether the `<teiHeader>` accurately reflects the provenance of the transcription[1]. By embedding these rubrics directly into GitHub Pull Request Templates, projects mandate that reviewers systematically check these interpretive dimensions before approving a merge, ensuring a uniform standard of scholarly rigor across distributed teams.

## Real-World Digital Edition Case Studies

The theoretical frameworks and technical architectures discussed above are best understood through their application in large-scale, active digital scholarly editions. The following case studies illustrate how diverse projects leverage GitHub workflows, TEI/MEI encoding, Schematron validation, and Linked Open Data to achieve unique scholarly objectives.

### The Scholastic Commentaries and Texts Archive (SCTA)

The Scholastic Commentaries and Texts Archive (SCTA), directed by Jeffrey C. Witt, represents one of the most sophisticated implementations of the "text-as-network" paradigm in the digital humanities[8]. The SCTA curates a massive, highly interconnected corpus of medieval scholastic philosophy and theology, primarily focusing on commentaries on Peter Lombard's *Sentences*[8]. Because scholastic texts are inherently intertextual—relying on dense, cross-referential networks of quotations, refutations, and marginalia—treating them as isolated documents is analytically insufficient[23].

The SCTA utilizes a highly specialized subset of the TEI guidelines, known as the LombardPress Schema, to encode diplomatic and critical transcriptions[24]. To maintain data integrity across thousands of interconnected files, the SCTA relies entirely on distributed GitHub workflows and automated quality control. All data is maintained in publicly accessible Git repositories, ensuring transparent provenance[11]. When new transcriptions are submitted via pull requests, they are validated using continuous integration pipelines implemented with GitHub Actions. These pipelines run strict structural consistency checks, verify metadata integrity against the project's Expression Description File (EDF) schema, and ensure that textual links (`@target`) accurately resolve to other nodes within the broader SCTA Linked Open Data network[11].

By decoupling the storage of the XML data from the applications that consume and display it, and by enforcing immutable Git versioning, the SCTA ensures citation stability and reproducible scholarship[11]. The project demonstrates that when automated XML validation is merged with community-based peer review—sometimes performed in collaboration with entities like the Medieval Academy of America via the Library of Digital Latin Texts—a massive, distributed corpus can maintain impeccable scholarly standards without relying on a centralized publishing bottleneck[11].

### E-LAUTE: A Multimodal Digital Edition

The E-LAUTE project (Electronic Linked Annotated Unified Tablature Edition) presents a highly complex editing scenario, assembling a comprehensive multimodal digital edition of surviving German lute tablature (GLT) sources from the 15th and 16th centuries[25]. Unlike modern notation or simpler French and Italian tablatures, GLT relies on an unintuitive diagrammatic system mapping course-fret combinations to unique symbols, making the corpus largely unplayable and inaccessible for contemporary musicians[25].

To overcome this, E-LAUTE transcends traditional TEI boundaries by integrating the Music Encoding Initiative (MEI) schema alongside TEI-XML[25]. The project utilizes a bespoke web-based collaborative editor, `mei-friend`, which provides interactive graphical notation panels alongside the raw XML, relying heavily on the Verovio engraving library for dynamic rendering[26]. Crucially, `mei-friend` features native integration with Git cloud services, allowing distributed scholars, musicologists, and performers to edit documents collaboratively in a version-controlled environment[25].

The E-LAUTE workflow heavily leverages CI/CD automation. When editing is completed, a formal release is created in GitHub, triggering a CI pipeline that executes automated XML validation and cross-checks the encoded metadata against a central relational database (E-LAUTEdb) via Linked Data mapping[25]. Furthermore, the pipeline automatically generates derivative encodings, computationally converting GLT into more accessible formats to support performance practice[25]. The E-LAUTE workflow exemplifies how GitHub Actions and schema validation are not merely punitive checks, but generative tools that automatically synthesize and cross-reference multimodal data prior to publication on digital platforms.

### FIHRIST and DHClass-Hub: Collaborative and Pedagogical Environments

The deployment of distributed workflows is equally transformative in cataloging and explicitly pedagogical environments. The FIHRIST project, a union catalogue for manuscripts from the Islamicate world maintained by Oxford and Cambridge, highlights the necessity of iterative, collaborative learning when teaching the TEI manuscript description (`<msDesc>`) module[1]. Because no prior TEI examples existed for Islamic manuscripts at the project's inception, the team had to model the data and learn the encoding standards simultaneously[1]. Transitioning the project to GitHub revolutionized their workflow and training protocols[1]. By managing all files via the GitHub client and the Oxygen XML Editor, and resolving conflicts through pull requests, catalogers learned XML not through abstract theory, but through the transparent, communicative workflows of the Git repository[1].

Similarly, the DHClass-Hub project at Pitt-Greensburg demonstrates the pedagogical efficacy of GitHub in an undergraduate setting[19]. Instructors deployed a GitHub repository designed to familiarize students with version control through daily usage. The repository functioned as a "cooperative garage" where students shared code and utilized GitHub Issues to debug problems collaboratively[19]. The DHClass-Hub unexpectedly generated a flipped learning environment, where students initiated dialogues and effectively crowd-sourced peer review for their digital humanities assignments[19]. These cases prove that when the steep learning curve of TEI and Git is scaffolded by continuous integration and transparent review workflows, students transition from passive learners to active practitioners in the digital humanities ecosystem.

### CLEF and Manubot: Provenance and Open Collaboration

Extending beyond traditional XML editions, platforms like CLEF (Crowdsourcing Linked Entities via web Form) and Manubot utilize Git repositories to drive entirely new forms of scholarly collaboration. Manubot pioneered open collaborative writing by allowing dozens of geographically distributed scholars to co-author scientific papers in Markdown via GitHub, using Travis CI to automatically render the manuscript and resolve bibliographic citations[9].

CLEF adapts this distributed, CI-driven model for Linked Open Data (LOD) crowdsourcing in the cultural heritage sector[27]. Developed to support projects like ARTchives (surveying art historians' archival collections) and musoW (cataloging musical resources), CLEF binds changes in Linked Data to commits in GitHub, utilizing the PROV ontology to track exact provenance[27]. By maintaining data in a Git repository rather than solely in a database, CLEF ensures that every modification is peer-reviewed, easily revertible, and permanently archived. Furthermore, by linking GitHub releases directly to Zenodo, these projects ensure long-term preservation and assign DOIs to datasets, satisfying the FAIR (Findable, Accessible, Interoperable, Reusable) data principles[27].

## Pedagogical Takeaways and the Minimal Computing Paradigm

Integrating GitHub, CI/CD pipelines, and XML schema validation into a digital editing curriculum requires careful pedagogical design. Educators must actively mitigate student anxiety, provide structured evaluation metrics, and instill principles of digital longevity to ensure that student labor yields sustainable, rather than ephemeral, scholarly products.

### Mitigating Student Anxiety and the Learning Curve

The digital humanities suffer from an inherently steep learning curve, particularly regarding the command line, XML namespaces, and the conceptual abstractness of version control[28]. Students lacking a computer science background often experience profound "technophobia" when confronted with Git conflict markers or Schematron XPath validation errors[28].

To mitigate this, pedagogical best practices dictate a constructivist approach rooted in real-world application[29]. Rather than teaching TEI in a vacuum, students should be integrated into active, community-driven projects where their encoding contributes to a tangible, published outcome[1]. Utilizing intuitive interfaces, such as GitHub Desktop or visual XML editors, abstracts away the intimidating command-line syntax while preserving the underlying distributed workflow[30]. Furthermore, CI/CD pipelines serve as an objective, non-judgmental automated tutor. When a student commits malformed XML, the pipeline provides immediate, specific feedback without requiring instructor intervention, fostering a "growth mindset" where failure is viewed as an iterative step in the debugging process rather than an academic penalty[19].

### Digital Longevity and the Endings Project Principles

A critical pedagogical imperative in modern DSE is teaching students the value of digital longevity. The digital humanities are plagued by "digital entropy" and "link rot," wherein complex, database-driven projects decay rapidly when grant funding expires, security patches fail, or server infrastructure is decommissioned[31]. Teaching students to rely on monolithic, proprietary platforms or heavy server-side applications inadvertently sets their scholarship up for rapid obsolescence[31].

The Endings Project, spearheaded by the University of Victoria, provides a vital pedagogical and architectural framework for combating this entropy[32]. The Endings principles advocate for "minimal computing," demanding that projects utilize open standards (like TEI XML), maintain strict version control, and eliminate dependencies on server-side processing architectures like PHP or MySQL databases[31].

By employing static site generators (e.g., Jekyll, Hugo) or lightweight JavaScript transformers (e.g., CETEIcean, Verovio) hosted on free infrastructure like GitHub Pages, editions achieve graceful degradation and long-term stability[26]. Instructing students in minimal computing workflows ensures that their portfolios remain accessible for decades, decoupling the quality of their scholarship from the financial resources of their host institutions, and promoting global equity in digital humanities production[26].

| Infrastructure Approach | Characteristics | Longevity Vulnerabilities | Endings Project / Minimal Computing Alternative |
| --- | --- | --- | --- |
| **Monolithic CMS** | Relies on server-side databases (MySQL), PHP, and dynamic rendering. | Highly vulnerable to security flaws, software deprecation, and server defunding. | Generate static HTML directly from TEI-XML; host on standard web servers. |
| **Proprietary Software** | Custom-built visualization tools dependent on specific operating systems or paid licenses. | Becomes unusable when the vendor alters the API, goes bankrupt, or drops support. | Utilize open-source, browser-native rendering libraries (CETEIcean, MathJax, Verovio). |
| **Centralized Storage** | Master files reside on a single university server or local hard drive. | Susceptible to catastrophic hardware failure or institutional administrative changes. | Utilize distributed Git repositories; archive formal releases to Zenodo for persistent DOIs. |

### Audit Checklist and GitHub Peer-Review Rubric for Intermediate TEI

To facilitate the translation of traditional humanistic peer review into a GitHub Pull Request workflow, instructors and project managers should utilize a structured rubric. The following rubric provides a framework for evaluating intermediate TEI XML editions prior to merging into a production repository:

| Evaluation Domain | Technical and Philological Assessment Criteria | Action Required if Deficient |
| --- | --- | --- |
| **1. Pipeline Validation** | Does the PR pass all automated CI checks? (Syntax, Jing RELAX NG, Saxon Schematron). Are there any outstanding GitHub annotations? | **Block Merge.** Contributor must review CI logs and resolve XML syntax or schema violations. |
| **2. Structural Integrity** | Does the OHCO mapping reflect the physical document? Are `<pb/>`, `<cb/>`, and `<lb/>` milestones placed correctly without violating logical nesting? | **Request Changes.** Reviewer provides inline suggestions on GitHub highlighting incorrect nesting. |
| **3. Philological Accuracy** | Are editorial interventions properly tagged? Are `<choice>`, `<orig>`, `<reg>`, `<sic>`, and `<corr>` used in accordance with project guidelines? Does the transcription accurately reflect the facsimile? | **Request Changes.** Reviewer cites manuscript evidence in PR comments to justify alternative transcriptions. |
| **4. Semantic Precision** | Are entities appropriately identified? Are `<persName>`, `<placeName>`, and `<date>` tags utilized? Do `@ref` or `@key` attributes point to valid authority files or LOD URIs? | **Request Changes.** Reviewer identifies missed semantic tagging opportunities or invalid URIs. |
| **5. Metadata Provenance** | Is the `<teiHeader>` complete? Does the `<revisionDesc>` log the student's contribution? Are source dimensions, hands, and repository details accurately captured in the `<sourceDesc>`? | **Request Changes.** Contributor must update provenance trails to ensure academic attribution. |
| **6. Minimal Computing** | Does the XML render correctly via the project's static site generator or CETEIcean implementation? Are there any hardcoded display attributes (e.g., bypassing CSS)? | **Request Changes.** Remove hardcoded styles to ensure separation of data and presentation. |

## Conclusion

The convergence of distributed version control, rigorous XML schema validation, and structured peer review represents a profound maturation of the digital humanities. As demonstrated by the historical trajectory from the theoretical limitations of the OHCO model to the dynamic, networked corpora of the Scholastic Commentaries and Texts Archive, digital scholarly editing has transcended the static representation of isolated texts. The adoption of GitHub collaborative workflows—characterized by the fork, the atomic commit, and the pull request—democratizes the editorial process, distributing the immense labor of transcription and semantic markup across global communities of scholars and students.

Crucially, the sustainability of this decentralized model is contingent upon automated continuous integration. By embedding RELAX NG and ISO/IEC 19757-3 Schematron engines directly into CI/CD pipelines, projects can enforce intricate business logic and structural integrity without overwhelming human reviewers. This automation allows humanistic peer review to focus on philological accuracy and interpretive nuance, facilitated by structured rubrics and inline code-review mechanisms.

Furthermore, integrating these workflows into undergraduate and graduate curricula yields profound pedagogical benefits. By exposing students to real-world data environments, mitigating technophobia through automated feedback, and emphasizing the minimal computing principles of the Endings Project, educators equip the next generation of scholars with the tools necessary to build robust, sustainable digital archives. Ultimately, the synthesis of Git-based collaboration and automated XML validation ensures that digital scholarly editions are not ephemeral technological experiments, but rigorous, durable, and continuously evolving instruments of humanistic inquiry.

Sources used in the report

04_Teaching_the_Text_Encoding_Initiative_Context,_Community_and_Collaboration.pdf

[tei-c.org

v. A Gentle Introduction to XML - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/release/doc/tei-p5-doc/en/html/SG.html)[harvest.usask.ca

Digital Textuality, Autopoietic Editing, and the Courten MS A Project Paper Submitted to the College of Graduate Studies and Res - HARVEST

 Opens in a new window](https://harvest.usask.ca/bitstreams/e3768511-7aee-47cc-8209-310de59ca695/download)[balisage.net

Balisage Paper: Hierarchies within range space

 Opens in a new window](https://www.balisage.net/Proceedings/vol13/html/Piez01/BalisageVol13-Piez01.html)[blogs.library.duke.edu

Graphs, Trees, and Streams: The TEI Data Model - Duke Collaboratory for Classics Computing (DC3)

 Opens in a new window](https://blogs.library.duke.edu/dcthree/2013/08/26/graphs-trees-and-streams-the-tei-data-model/)[companions.digitalhumanities.org

The Text Encoding Initiative and the Study of Literature - Blackwell Companions to Digital Humanities

 Opens in a new window](https://companions.digitalhumanities.org/DLS/?chapter=content/9781405148641_chapter_25.html)[nl.ijs.si

1. A Gentle Introduction to XML

 Opens in a new window](https://nl.ijs.si/et/talks/esslli02/reader/gentleintro.pdf)[journals.openedition.org

Why TEI Stand-off Markup Authoring Needs Simplification - OpenEdition Journals

 Opens in a new window](https://journals.openedition.org/jtei/1838)[digitalstudies.org

Chapter 5Digital editing as autopoietic process - Digital Studies / Le champ numérique

 Opens in a new window](https://www.digitalstudies.org/article/id/7285/)[chwp.artsci.utoronto.ca

Liu and Smith, “ A Relational Database Model for Text Encoding” - CH Working Papers

 Opens in a new window](https://chwp.artsci.utoronto.ca/CHC2007/Liu_Smith/Liu_Smith.htm)[balisage.net

Balisage Paper: Why TEI stand-off annotation doesn't quite work

 Opens in a new window](https://www.balisage.net/Proceedings/vol5/html/Banski01/BalisageVol5-Banski01.html)[ids-pub.bsz-bw.de

Proceedings of Extreme Markup Languages®

 Opens in a new window](https://ids-pub.bsz-bw.de/files/4537/Witt_Multiple_hierarchies_new_aspects_of_an_old_solution_2004.pdf)[kups.ub.uni-koeln.de

Digital Scholarly Editions as Interfaces

 Opens in a new window](https://kups.ub.uni-koeln.de/9085/1/SIDE_12_digital_scholarly_editions_as_interfaces.pdf)[access.archive-ouverte.unige.ch

Re-conceiving the Christian scholastic corpus with the scholastic commentaries and texts archive - Archive ouverte UNIGE

 Opens in a new window](https://access.archive-ouverte.unige.ch/access/metadata/07719c93-ba9f-4b86-bb0a-b01902c09b33/download)

01_Forking_anatomy_How_MorphoDepot_applies_the_open‐source_development_model_to_3D_.pdf

[github.com

curateteaching/digitalpedagogy: Digital Pedagogy in the Humanities: Concepts, Models, and Experiments - GitHub

 Opens in a new window](https://github.com/curateteaching/digitalpedagogy)[tei-c.org

Using the TEI GitHub Repository

 Opens in a new window](https://tei-c.org/guidelines/p5/using-the-tei-github-repository/)[pcreview.co.uk

(OT) Microsoft being sued AGAIN! - PC Review

 Opens in a new window](https://www.pcreview.co.uk/threads/ot-microsoft-being-sued-again.1966285/)[community.scta.info

SCTA Data Management Policies and Practices

 Opens in a new window](https://community.scta.info/policy/data-management)

02_Open_collaborative_writing_with_Manubot.pdf

[slideshare.net

Validating XML and JSON Documents Using Oxygen Scripting | PDF - Slideshare

 Opens in a new window](https://www.slideshare.net/slideshow/validating-xml-and-json-documents-using-oxygen-scripting/258712883)[tei-c.org

23 Documentation Elements - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://www.tei-c.org/release/doc/tei-p5-doc/fr/html/TD.html)[community.scta.info

LombardPress Diplomatic Transcription Guidelines - SCTA Community

 Opens in a new window](https://community.scta.info/pages/lombardpress-schema-diplomatic.html)[driscoll.dk

TEI XML customisation for manuscript description

 Opens in a new window](http://driscoll.dk/fasnl/FASNL_msDesc_v1_2016.html)[en.wikipedia.org

Schematron - Wikipedia

 Opens in a new window](https://en.wikipedia.org/wiki/Schematron)[docs.rs

schematron 0.4.0 - Docs.rs

 Opens in a new window](https://docs.rs/crate/schematron/latest)[tags.hypotheses.org

Bag of tags | Formats and standards for humanities information

 Opens in a new window](https://tags.hypotheses.org/)[github.com

schema/svrl.sch at main - GitHub

 Opens in a new window](https://github.com/Schematron/schema/blob/main/svrl.sch)[metadata101.org

Schematron - Metadata 101

 Opens in a new window](https://metadata101.org/schematron/)[balisage.net

Balisage Paper: Schematron as XSLT Interface, and Advanced Validation Models

 Opens in a new window](https://www.balisage.net/Proceedings/vol30/html/Kalvesmaki01/BalisageVol30-Kalvesmaki01.html)[libcal.library.ubc.ca

TEI 2026: Low-cost, low-infrastructure, low-threshold strategies for authoring and publishing TEI (and friends) - UBC Library - University of British Columbia

 Opens in a new window](https://libcal.library.ubc.ca/event/4043887)[semanticscholar.org

A GitHub Garage for a Digital Humanities Course - Semantic Scholar

 Opens in a new window](https://www.semanticscholar.org/paper/046ddb24c0f0edbd6bda8d1bfd0340e5a9400415)[github.com

Stylesheets/ChangeLog at dev · TEIC/Stylesheets - GitHub

 Opens in a new window](https://github.com/TEIC/Stylesheets/blob/dev/ChangeLog)[github.com

adunning/xml-model-validator - GitHub

 Opens in a new window](https://github.com/adunning/xml-model-validator)[github.com

dracor-org/dracor-validate-action: GitHub action for validating TEI files

 Opens in a new window](https://github.com/dracor-org/dracor-validate-action)[tei-c.org

23 Documentation Elements - The TEI Guidelines - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/release/doc/tei-p5-doc/en/html/TD.html)[wwp.neu.edu

Customizing TEI to Check Pointers - Women Writers Project - Northeastern University

 Opens in a new window](https://www.wwp.neu.edu/research/publications/documentation/other/checking_pointers_in_ODD.html)[pmc.ncbi.nlm.nih.gov

Digital humanities in the era of digital reproducibility: towards a fairest and post-computational framework - PMC

 Opens in a new window](https://pmc.ncbi.nlm.nih.gov/articles/PMC11111558/)[cuny.manifoldapp.org

Punk Rock Pedagogies: DIY, Minimal, No-Code/Low-Code, Resource Constrained, Learning Frameworks for the (Digital) Humanities | Manifold @CUNY

 Opens in a new window](https://cuny.manifoldapp.org/read/punk-rock-pedagogies-diy-minimal-no-code-low-code-resource-constrained-learning-frameworks-for-the-digital-humanities-36e69847-b193-4914-899b-f996d2c782fb)[livingstoneonline.org

Livingstone Online TEI P5 Encoding Guidelines

 Opens in a new window](https://livingstoneonline.org/resources/livingstone-online-tei-p5-encoding-guidelines)[kups.ub.uni-koeln.de

Digital Scholarly Editions as Interfaces

 Opens in a new window](https://kups.ub.uni-koeln.de/9118/1/10_witt.pdf)[journals.openedition.org

Finding Relatedness: pathways for detecting textual relatedness in the medieval scholastic corpus - OpenEdition Journals

 Opens in a new window](https://journals.openedition.org/methodos/10987)[dokumen.pub

Past and Future: Medieval Studies Today (Textes Et Etudes Du Moyen Age, 98) (English, French and Spanish Edition) 9782503594705, 2503594700 - DOKUMEN.PUB

 Opens in a new window](https://dokumen.pub/past-and-future-medieval-studies-today-textes-et-etudes-du-moyen-age-98-english-french-and-spanish-edition-9782503594705-2503594700.html)[lombardpress.org

Lombard Press Schema 1.0.0 - Diplomatic Transcription Guidelines

 Opens in a new window](https://lombardpress.org/schema/docs/diplomatic/)[spear-prosop.org

Encoding Manual and TEI Customization for SPEAR: Syriaca Persons, Events, and Relations

 Opens in a new window](https://spear-prosop.org/documentation/Schema/SPEAR.html)[researchgate.net

Decoupling Quality Control and Publication: The Digital Latin Library

 Opens in a new window](https://www.researchgate.net/publication/402936927_Decoupling_Quality_Control_and_Publication_The_Digital_Latin_Library_and_the_Traveling_Imprimatur)[github.com

Petri Gracilis Commentarius in Libros Sententiarum, Liber 1, Lectiones 1–20 - GitHub

 Opens in a new window](https://github.com/Library-of-Digital-Latin-Texts/MAA-gracilis-1-1-20)

06_Collaborative_workflows_for_encoding,_validating,_and_publishing_a_multimodal_di.pdf

[fabian-moss.de

Minimal Publishing of Multimodal Sources: Integrating MEI, TEI, and More | Fabian C. Moss

 Opens in a new window](https://fabian-moss.de/talk/minimal-publishing-of-multimodal-sources-integrating-mei-tei-and-more/)

03_Developing_a_new_integrated_editing_platform_for_source_documents_in_classics.pdf

05_Clef._a_linked_open_data_native_system_for_crowdsourcing.pdf

[ceur-ws.org

Teaching Computational Methods to Humanities Students - CEUR-WS.org

 Opens in a new window](https://ceur-ws.org/Vol-2364/44_paper.pdf)[aubreemarshall.com

DH Teaching Statement - Aubree Marshall

 Opens in a new window](https://www.aubreemarshall.com/dh-teaching-statement.html)[researchgate.net

(PDF) An Investigation Into the Perceived Effectiveness of GitHub Repositories to Teach Programming - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/386074958_An_Investigation_Into_the_Perceived_Effectiveness_of_GitHub_Repositories_to_Teach_Programming)[researchgate.net

(PDF) Teaching Computational Methods to Humanities Students - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/384778860_Teaching_Computational_Methods_to_Humanities_Students)[aacademica.org

Against infrastructure: global approaches to digital scholarly editing - Acta Académica

 Opens in a new window](https://www.aacademica.org/gimena.delrio.riande/224.pdf)[adamdjbrett.com

Digital Humanities Part 5: Preserving Digital Humanities Projects | Adam DJ Brett

 Opens in a new window](https://www.adamdjbrett.com/blog/dh-part-5-preserving-digital-humanities-projects/)[dh-tech.adho.org

Embracing Endings: Principles for Digital Longevity and Their Importance for Research Software Engineers | DHTech

 Opens in a new window](https://dh-tech.adho.org/blog/2023/08/07/endings-principles/)[adamdjbrett.com

Digital Humanities Part 6: Preservation through Minimal Computing and GO::DH

 Opens in a new window](https://www.adamdjbrett.com/blog/dh-part-6-minimal-computing-and-go-dh/)[researchgate.net

Making Marx More Readable: A Minimal Computing Approach to a Community-Driven Edition of Capital Vol. 1 - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/410806010_Making_Marx_More_Readable_A_Minimal_Computing_Approach_to_a_Community-Driven_Edition_of_Capital_Vol_1)
Sources read but not used in the report
[wwp.northeastern.edu

Proceedings - Women Writers Project

 Opens in a new window](https://www.wwp.northeastern.edu/outreach/seminars/uvic_advanced_2015/venue/bauman_freedom_to_constrain.pdf)[tei-c.org

TEI Technical Council virtual “F2F”, 2020-05-01 / 05-03 - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/activities/council/meetings/tei-technical-council-virtual-f2f-2020-05-01-05-03-05-05-05-12/)[dse-communities.nplp.pl

Program - DSE Communities

 Opens in a new window](https://dse-communities.nplp.pl/programme)[researchgate.net

The International Image Interoperability Framework (IIIF): raising awareness of the user benefits for scholarly editions - ResearchGate

 Opens in a new window](https://www.researchgate.net/profile/Julien-Raemy/publication/322538093_The_International_Image_Interoperability_Framework_IIIF_raising_awareness_of_the_user_benefits_for_scholarly_editions/links/5aa7e785458515b024faec14/The-International-Image-Interoperability-Framework-IIIF-raising-awareness-of-the-user-benefits-for-scholarly-editions.pdf)[cuny.manifoldapp.org

Teaching DH on a Shoestring: Minimalist Digital Humanities Pedagogy - Manifold @CUNY

 Opens in a new window](https://cuny.manifoldapp.org/read/teaching-dh-on-a-shoestring-minimalist-digital-humanities-pedagogy)[arxiv.org

KBSET – Knowledge-Based Support for Scholarly Editing and Text Processingwith Declarative LaTeX Markupand a Core Written in SWI-Prolog - arXiv

 Opens in a new window](https://arxiv.org/html/2002.10329v1)[teibyexample.org

Examples | Module 8: Customising TEI, ODD, Roma - TEI by Example

 Opens in a new window](https://teibyexample.org/exist/examples/TBED08v00.htm?target=jTEI)[research.it.ox.ac.uk

The Livingstone Online TEI P5 Encoding Guidelines

 Opens in a new window](http://research.it.ox.ac.uk/LEAP/leap.html)[dev.tbe.kantl.be

Module 8: Customising TEI, ODD, Roma - TEI by Example

 Opens in a new window](https://dev.tbe.kantl.be/examples/TBED08v00.htm)[clarin-eric.github.io

The structure and encoding of PressMint corpora - GitHub Pages

 Opens in a new window](https://clarin-eric.github.io/PressMint/)[korpling.german.hu-berlin.de

TEI LAUDATIO Customization Metadata Concept 'Corpus' - Humboldt-Universität zu Berlin

 Opens in a new window](https://korpling.german.hu-berlin.de/schemata/laudatio/doc/S6/corpus/)[journals.openedition.org

A TEI Customization for Writing TEI Customizations - OpenEdition Journals

 Opens in a new window](https://journals.openedition.org/jtei/2573)[wwp.northeastern.edu

Northeastern University Women Writers Project Textbase Encoding Language

 Opens in a new window](https://wwp.northeastern.edu/wwo/source/schema/wwp-store.html)[utppublishing.com

The Global Medieval Sourcebook: Creating a Sustainable Digital Anthology of Medieval Texts and Translations | Seminar - University of Toronto Press

 Opens in a new window](https://utppublishing.com/doi/abs/10.3138/seminar.57.3.1)[brill.com

Chapter 5 Philology: Standards for Digital Editing in - Brill

 Opens in a new window](https://brill.com/display/book/9789004400351/BP000014.xml?language=en)[journals.uchicago.edu

Digital Corpora and Scholarly Editions of Latin Texts: Features and Requirements of Textual Criticism | Speculum: Vol 92, No S1 - The University of Chicago Press: Journals

 Opens in a new window](https://www.journals.uchicago.edu/doi/10.1086/693823)[researchgate.net

(PDF) 6 Editions - ResearchGate

 Opens in a new window](https://www.researchgate.net/publication/380100585_6_Editions)[stfx.ca

English Department - St. Francis Xavier University

 Opens in a new window](https://www.stfx.ca/department/english)[stfx.ca

English Department - Courses | St. Francis Xavier University

 Opens in a new window](https://www.stfx.ca/programs-courses/courses/481)[stfx.ca

Who We Are | St. Francis Xavier University

 Opens in a new window](https://www.stfx.ca/research/research-institutes-centres-networks/digital-humanities/who-we-are)[stfx.ca

Digital Humanities | St. Francis Xavier University

 Opens in a new window](https://www.stfx.ca/research/research-institutes-centres-networks/digital-humanities)[stfx.ca

Faculty Publications – English | St. Francis Xavier University

 Opens in a new window](https://www.stfx.ca/department/english/faculty-publications)[stfx.ca

DHSI-East: Digital Archives & Databases | St. Francis Xavier University

 Opens in a new window](https://www.stfx.ca/research/research-institutes-centres-networks/digital-humanities-centre/dhsi-east/past-events-0)[stfx.ca

DHSI-East | St. Francis Xavier University

 Opens in a new window](https://www.stfx.ca/research/digital-humanities/dhsi-east)[stfx.ca

StFX English Department celebrates five new books | St. Francis Xavier University

 Opens in a new window](https://www.stfx.ca/news/English-Department-book-launch)[gist.github.com

ipfs-view-npm-registry.md - GitHub Gist

 Opens in a new window](https://gist.github.com/dignifiedquire/575965768b301f58506e)[github.com

FYP_similartags/RerunKeming/allTags_test.txt at master - GitHub

 Opens in a new window](https://github.com/lint0011/FYP_similartags/blob/master/RerunKeming/allTags_test.txt)[sourceforge.net

Page 5 | Best Open Source Mac Data Formats Software 2026

 Opens in a new window](https://sourceforge.net/directory/data-formats/mac/?page=5)[ftp3.us.freebsd.org

FreeBSD Ports Collection Index

 Opens in a new window](http://ftp3.us.freebsd.org/pub/FreeBSD-CVS/www/data/es/ports/master-index.html)[vb-net.com

FreeBSD Ports Collection Index - VB.NET

 Opens in a new window](https://www.vb-net.com/Freebsd/FreeBSDPortsCollectionIndex.htm)[scribd.com

Skills | PDF - Scribd

 Opens in a new window](https://www.scribd.com/document/819588329/Skills)[hcmc.uvic.ca

A brief history of BBTI - Humanities Computing and Media Centre (HCMC)

 Opens in a new window](https://hcmc.uvic.ca/project/bbti/about.html)[tei-c.org

News - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/news/)[cambridge.org

Digital Scholarly Editing in Practice - Cambridge University Press & Assessment

 Opens in a new window](https://www.cambridge.org/core/elements/digital-scholarly-editing-in-practice/033E79028A8F05B3537450D993A121C3)[cdr.lib.unc.edu

FirstReport16Oct22 - Carolina Digital Repository

 Opens in a new window](https://cdr.lib.unc.edu/downloads/js956x788)[tei-c.org

TEI-C Elections 2023 - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/news/2023/08/06/tei-c-elections-2023/)[teibyexample.org

Module 8: Customising TEI, ODD, Roma - TEI by Example

 Opens in a new window](https://teibyexample.org/exist/examples/TBED08v00.htm)[e-ditiones.github.io

Encoding guidelines for the teiHeader of manuscripts - E-Ditiones

 Opens in a new window](https://e-ditiones.github.io/ODD/ODD-header_MS.html)[tei-c.org

jTEI input customizationRon Van den Branden ron.vandenbranden@kantl.be, Martin Holmes mholmes@uvic.ca. - Text Encoding Initiative

 Opens in a new window](https://tei-c.org/release/doc/tei-p5-exemplars/html/tei_jtei.doc.html)[dvpp.uvic.ca

1. The Digital Victorian Periodical Poetry Schema and Guidelines for Encoding

 Opens in a new window](https://dvpp.uvic.ca/dvpp.html)[academiccommons.columbia.edu

Doing· Digital Humanities - Columbia Academic Commons

 Opens in a new window](https://academiccommons.columbia.edu/doi/10.7916/D8T445R9/download)[books.openedition.org

11. Highly Available Dissertations: Open Sourcing Humanities Scholarship - OpenEdition Books

 Opens in a new window](https://books.openedition.org/obp/21175?lang=en)[shawnaross.github.io

Using Digital Humanities in the Classroom Companion - GitHub Pages

 Opens in a new window](https://shawnaross.github.io/teachdh/)[dhdebates.gc.cuny.edu

2. Reprogramming the Invisible Discipline: An Emancipatory Approach to Digital Technology through Higher Education | People, Practice, Power

 Opens in a new window](https://dhdebates.gc.cuny.edu/read/people-practice-power/section/2e2b8286-3210-432b-a753-81f2d2cddca6)[dhq-static.digitalhumanities.org

No Boutique or Fashionable Technologies: Project Development, Mentorship, and Sustainability - DHQ Static

 Opens in a new window](https://dhq-static.digitalhumanities.org/pdf/000660.pdf)[scholarlyediting.org

On Automating Editions | Volume 41 | Scholarly Editing Journal

 Opens in a new window](https://scholarlyediting.org/issues/41/on-automating-editions/)[mapoflondon.uvic.ca

MoEML: Mission Statement - The Map of Early Modern London

 Opens in a new window](https://mapoflondon.uvic.ca/mission_statement.htm)[lemdo.uvic.ca

MoEML Mayoral Shows: MoMS Editorial Guidelines - Linked Early Modern Drama Online

 Opens in a new window](https://lemdo.uvic.ca/moms/edGuide.html)[ospolicyobservatory.uvic.ca

Draft Report: Research Data Management Support in the Humanities: Challenges and Recommendations | Open Scholarship Policy Observatory

 Opens in a new window](https://ospolicyobservatory.uvic.ca/draft-report-rdm/)[w3.org

Service Modeling Language, Version 1.1 - W3C

 Opens in a new window](https://www.w3.org/TR/2007/WD-sml-20070926/)[github.com

maa-hedon-d3c6-reviewed-repo/readme.md at master · Library-of

 Opens in a new window](https://github.com/Library-of-Digital-Latin-Texts/maa-hedon-d3c6-reviewed-repo/blob/master/readme.md)[zfdg.de

›A digital edition is not visible‹ - some thoughts on the nature and persistence of digital editions

 Opens in a new window](https://zfdg.de/2020_005)[chwp.arts.ubc.ca

Liu and Smith, “ A Relational Database Model for Text Encoding”

 Opens in a new window](https://chwp.arts.ubc.ca/CHC2007/Liu_Smith/Liu_Smith.htm)[dhi.ac.uk

The Quest for the “Hundred Year” Digital Scholarly Edition

 Opens in a new window](https://www.dhi.ac.uk/books/digital-editing-and-publishing/rosselli-del-turco/)[endings.uvic.ca

Principles | Principes - The Endings Project - UVic

 Opens in a new window](https://endings.uvic.ca/principles.html)[bostondh.org

2025 Symposium - Boston DH

 Opens in a new window](https://bostondh.org/symposium-2025/)
Thoughts

Mapping Core Theoretical Frameworks

I am initiating a comprehensive investigation into how distributed version control systems, automated XML schema validation, and structured peer review intersect to enhance textual data integrity and student outcomes in digital scholarly editing. By analyzing the provided research literature on collaborative platforms like Perseids, E-LAUTE, and CLEF, I am evaluating how automated continuous integration pipelines enforce encoding standards and streamline scholarly critique.

Identifying Domain-Specific Knowledge Gaps

To build an exhaustive academic synthesis, I need deeper insights into specific real-world case studies and pedagogical frameworks. Specifically, I am targeting details around the Scholastic Commentaries and Texts Archive validation architecture, custom Schematron integration via automated continuous integration workflows, and specific undergraduate digital humanities rubric designs.

Executing Targeted Knowledge Retrieval

I am launching structured queries to gather targeted literature on TEI quality assurance pipelines using GitHub Actions, Schematron validation engines, and SCTA distributed workflows. Additionally, I am exploring undergraduate digital humanities curricula to ensure the practical pedagogical recommendations and audit rubrics reflect real-world classroom practices.

[community.scta.info

SCTA Data Management Policies and Practices](https://community.scta.info/policy/data-management)[dokumen.pub

Past and Future: Medieval Studies Today (Textes Et Etudes Du Moyen Age, 98) (English, French and Spanish Edition) 9782503594705, 2503594700 - DOKUMEN.PUB](https://dokumen.pub/past-and-future-medieval-studies-today-textes-et-etudes-du-moyen-age-98-english-french-and-spanish-edition-9782503594705-2503594700.html)[researchgate.net

The International Image Interoperability Framework (IIIF): raising awareness of the user benefits for scholarly editions - ResearchGate](https://www.researchgate.net/profile/Julien-Raemy/publication/322538093_The_International_Image_Interoperability_Framework_IIIF_raising_awareness_of_the_user_benefits_for_scholarly_editions/links/5aa7e785458515b024faec14/The-International-Image-Interoperability-Framework-IIIF-raising-awareness-of-the-user-benefits-for-scholarly-editions.pdf)[kups.ub.uni-koeln.de

Digital Scholarly Editions as Interfaces](https://kups.ub.uni-koeln.de/9085/1/SIDE_12_digital_scholarly_editions_as_interfaces.pdf)[tei-c.org

Using the TEI GitHub Repository](https://tei-c.org/guidelines/p5/using-the-tei-github-repository/)

Synthesizing Core Infrastructures

I am synthesizing findings from key platforms like the Scholastic Commentaries and Texts Archive (SCTA), Perseids, and Manubot to detail how version control and continuous integration automate scholarly text validation. Exploring how Git-based workflows transform XML documents into linked digital networks highlights the transition from static digital editions to dynamic, machine-actionable scholarly data.

Mapping Pedagogical and Technical Frameworks

I am framing technical validation—such as ISO Schematron rule assertions and automated schema checks via continuous integration pipelines—alongside open peer-review rubrics. This addresses the challenge of resolving structural XML merge conflicts within line-oriented version control systems, establishing clear criteria for both computational rigor and undergraduate digital humanities training.

Formulating Targeted Domain Inquiries

I will search for specialized literature on ISO Schematron implementation patterns in scholarly markup, technical analyses of XML-aware diffing tools in version-controlled workflows, and documented case studies evaluating GitHub pull-request workflows in humanities teaching environments.

[github.com

Stylesheets/ChangeLog at dev · TEIC/Stylesheets - GitHub](https://github.com/TEIC/Stylesheets/blob/dev/ChangeLog)[wwp.northeastern.edu

Proceedings - Women Writers Project](https://www.wwp.northeastern.edu/outreach/seminars/uvic_advanced_2015/venue/bauman_freedom_to_constrain.pdf)[tei-c.org

TEI Technical Council virtual “F2F”, 2020-05-01 / 05-03 - Text Encoding Initiative](https://tei-c.org/activities/council/meetings/tei-technical-council-virtual-f2f-2020-05-01-05-03-05-05-05-12/)[lombardpress.org

Lombard Press Schema 1.0.0 - Diplomatic Transcription Guidelines](https://lombardpress.org/schema/docs/diplomatic/)[dse-communities.nplp.pl

Program - DSE Communities](https://dse-communities.nplp.pl/programme)[kups.ub.uni-koeln.de

Digital Scholarly Editions as Interfaces](https://kups.ub.uni-koeln.de/9085/1/SIDE_12_digital_scholarly_editions_as_interfaces.pdf)[dokumen.pub

Past and Future: Medieval Studies Today (Textes Et Etudes Du Moyen Age, 98) (English, French and Spanish Edition) 9782503594705, 2503594700 - DOKUMEN.PUB](https://dokumen.pub/past-and-future-medieval-studies-today-textes-et-etudes-du-moyen-age-98-english-french-and-spanish-edition-9782503594705-2503594700.html)[researchgate.net

The International Image Interoperability Framework (IIIF): raising awareness of the user benefits for scholarly editions - ResearchGate](https://www.researchgate.net/profile/Julien-Raemy/publication/322538093_The_International_Image_Interoperability_Framework_IIIF_raising_awareness_of_the_user_benefits_for_scholarly_editions/links/5aa7e785458515b024faec14/The-International-Image-Interoperability-Framework-IIIF-raising-awareness-of-the-user-benefits-for-scholarly-editions.pdf)[shawnaross.github.io

Using Digital Humanities in the Classroom Companion - GitHub Pages](https://shawnaross.github.io/teachdh/)[cuny.manifoldapp.org

Teaching DH on a Shoestring: Minimalist Digital Humanities Pedagogy - Manifold @CUNY](https://cuny.manifoldapp.org/read/teaching-dh-on-a-shoestring-minimalist-digital-humanities-pedagogy)[github.com

curateteaching/digitalpedagogy: Digital Pedagogy in the Humanities: Concepts, Models, and Experiments - GitHub](https://github.com/curateteaching/digitalpedagogy)[researchgate.net

(PDF) An Investigation Into the Perceived Effectiveness of GitHub Repositories to Teach Programming - ResearchGate](https://www.researchgate.net/publication/386074958_An_Investigation_Into_the_Perceived_Effectiveness_of_GitHub_Repositories_to_Teach_Programming)[semanticscholar.org

A GitHub Garage for a Digital Humanities Course - Semantic Scholar](https://www.semanticscholar.org/paper/046ddb24c0f0edbd6bda8d1bfd0340e5a9400415)

Synthesizing Validation Architectures and Projects

I am analyzing the specific technical implementations of constraint-based validation rules within modular TEI guidelines, focusing on Schematron pattern matching and custom schema compilation. Examining real-world deployments such as the LombardPress transcription ecosystem and the Scholastic Commentaries and Texts Archive reveals how distributed text services, linked data specifications, and manuscript annotation frameworks maintain strict structural uniformities across dispersed editorial teams.

Examining Collaborative Workflows and Pedagogy

I am exploring how collaborative platform environments serve as collaborative spaces for undergraduate digital humanities education. Dedicated classroom repositories operate as open peer-review hubs, turning technical troubleshooting into shared learning moments and promoting long-term, well-documented project maintainability.

Investigating Deep Theoretical and Automation Mechanics

I am planning targeted searches into the underlying data models of text encoding, contrasting strict hierarchical content structures with overlap solutions like stand-off annotation. Concurrently, I am preparing to investigate precise automated deployment scripts—incorporating command-line XML processors within continuous integration environments—to complete a thorough technical and pedagogical synthesis.

[blogs.library.duke.edu

Graphs, Trees, and Streams: The TEI Data Model - Duke Collaboratory for Classics Computing (DC3)](https://blogs.library.duke.edu/dcthree/2013/08/26/graphs-trees-and-streams-the-tei-data-model/)[tei-c.org

v. A Gentle Introduction to XML - The TEI Guidelines - Text Encoding Initiative](https://tei-c.org/release/doc/tei-p5-doc/en/html/SG.html)[journals.openedition.org

Why TEI Stand-off Markup Authoring Needs Simplification - OpenEdition Journals](https://journals.openedition.org/jtei/1838)[arxiv.org

KBSET – Knowledge-Based Support for Scholarly Editing and Text Processingwith Declarative LaTeX Markupand a Core Written in SWI-Prolog - arXiv](https://arxiv.org/html/2002.10329v1)[balisage.net

Balisage Paper: Hierarchies within range space](https://www.balisage.net/Proceedings/vol13/html/Piez01/BalisageVol13-Piez01.html)[companions.digitalhumanities.org

The Text Encoding Initiative and the Study of Literature - Blackwell Companions to Digital Humanities](https://companions.digitalhumanities.org/DLS/?chapter=content/9781405148641_chapter_25.html)[zfdg.de

›A digital edition is not visible‹ - some thoughts on the nature and persistence of digital editions](https://zfdg.de/2020_005)[harvest.usask.ca

Digital Textuality, Autopoietic Editing, and the Courten MS A Project Paper Submitted to the College of Graduate Studies and Res - HARVEST](https://harvest.usask.ca/bitstreams/e3768511-7aee-47cc-8209-310de59ca695/download)[digitalstudies.org

Chapter 5Digital editing as autopoietic process - Digital Studies / Le champ numérique](https://www.digitalstudies.org/article/id/7285/)[chwp.artsci.utoronto.ca

Liu and Smith, “ A Relational Database Model for Text Encoding” - CH Working Papers](https://chwp.artsci.utoronto.ca/CHC2007/Liu_Smith/Liu_Smith.htm)[teibyexample.org

Examples | Module 8: Customising TEI, ODD, Roma - TEI by Example](https://teibyexample.org/exist/examples/TBED08v00.htm?target=jTEI)[driscoll.dk

TEI XML customisation for manuscript description](http://driscoll.dk/fasnl/FASNL_msDesc_v1_2016.html)[tei-c.org

23 Documentation Elements - The TEI Guidelines - Text Encoding Initiative](https://tei-c.org/release/doc/tei-p5-doc/en/html/TD.html)[livingstoneonline.org

Livingstone Online TEI P5 Encoding Guidelines](https://livingstoneonline.org/resources/livingstone-online-tei-p5-encoding-guidelines)[research.it.ox.ac.uk

The Livingstone Online TEI P5 Encoding Guidelines](http://research.it.ox.ac.uk/LEAP/leap.html)[wwp.neu.edu

Customizing TEI to Check Pointers - Women Writers Project - Northeastern University](https://www.wwp.neu.edu/research/publications/documentation/other/checking_pointers_in_ODD.html)[spear-prosop.org

Encoding Manual and TEI Customization for SPEAR: Syriaca Persons, Events, and Relations](https://spear-prosop.org/documentation/Schema/SPEAR.html)[e-ditiones.github.io

Encoding guidelines for the teiHeader of manuscripts - E-Ditiones](https://e-ditiones.github.io/ODD/ODD-header_MS.html)[dev.tbe.kantl.be

Module 8: Customising TEI, ODD, Roma - TEI by Example](https://dev.tbe.kantl.be/examples/TBED08v00.htm)[wwp.northeastern.edu

Northeastern University Women Writers Project Textbase Encoding Language](https://wwp.northeastern.edu/wwo/source/schema/wwp-store.html)

Deconstructing Textual Data Models

I am examining foundational theoretical debates surrounding digital textuality, particularly focusing on the Ordered Hierarchy of Content Objects (OHCO) model and its limitations when encoding overlapping hierarchies or non-linear manuscript structures. By contrasting strict single-tree XML structures with hybrid graph models and autopoietic editing approaches, I am establishing how modern digital editions account for complex textual realities beyond rigid document trees.

Resolving Schema and Workflow Bottlenecks

I am evaluating practical solutions for enforcing domain-specific semantic constraints that standard RELAX NG schemas cannot address alone. Integrating ISO Schematron rules allows for context-sensitive validation, while automated continuous integration workflows streamline schema checking during source control contributions, resolving structural ambiguities early in the editorial pipeline.

Refining Implementation Details

I will perform targeted searches to gather concrete syntax examples for Schematron rules and continuous integration workflow definitions. Additionally, I will examine specific institutional digital humanities curricula to ensure the resulting framework provides actionable guidelines for both technical configuration and undergraduate research pedagogy.

Analyzing Advanced Schematron Pointer Validation

I am examining how business rules and context-dependent constraints, such as verifying cross-references and pointer targets between elements like identifiers and target attributes, are defined using ISO Schematron assertions inside TEI custom ODD files. Insights from specialized projects demonstrate how automated tests enforce structural integrity across complex manuscript descriptions and document headers.

Mapping Quality Assurance Workflows

I am clarifying how continuous integration tasks utilize command-line XML processors and validators like Jing or Saxon to execute automated schema validation upon push or pull-request events. This bridges the gap between manual editorial oversight and automated continuous deployment, ensuring that encoded digital texts meet strict structural guidelines prior to publication.

Investigating Continuous Integration Pipelines

I will conduct targeted searches into the specific automation configurations of central TEI repository pipelines, advanced Schematron context rules using local variables, and formal peer-review rubric designs that bridge software code reviews with scholarly digital editing feedback.

[tags.hypotheses.org

Bag of tags | Formats and standards for humanities information](https://tags.hypotheses.org/)[tei-c.org

jTEI input customizationRon Van den Branden ron.vandenbranden@kantl.be, Martin Holmes mholmes@uvic.ca. - Text Encoding Initiative](https://tei-c.org/release/doc/tei-p5-exemplars/html/tei_jtei.doc.html)[clarin-eric.github.io

The structure and encoding of PressMint corpora - GitHub Pages](https://clarin-eric.github.io/PressMint/)[wwp.neu.edu

Customizing TEI to Check Pointers - Women Writers Project - Northeastern University](https://www.wwp.neu.edu/research/publications/documentation/other/checking_pointers_in_ODD.html)[tei-c.org

23 Documentation Elements - The TEI Guidelines - Text Encoding Initiative](https://www.tei-c.org/release/doc/tei-p5-doc/fr/html/TD.html)[korpling.german.hu-berlin.de

TEI LAUDATIO Customization Metadata Concept 'Corpus' - Humboldt-Universität zu Berlin](https://korpling.german.hu-berlin.de/schemata/laudatio/doc/S6/corpus/)[journals.openedition.org

A TEI Customization for Writing TEI Customizations - OpenEdition Journals](https://journals.openedition.org/jtei/2573)[spear-prosop.org

Encoding Manual and TEI Customization for SPEAR: Syriaca Persons, Events, and Relations](https://spear-prosop.org/documentation/Schema/SPEAR.html)[e-ditiones.github.io

Encoding guidelines for the teiHeader of manuscripts - E-Ditiones](https://e-ditiones.github.io/ODD/ODD-header_MS.html)[wwp.northeastern.edu

Northeastern University Women Writers Project Textbase Encoding Language](https://wwp.northeastern.edu/wwo/source/schema/wwp-store.html)

Mapping Validation Engine Mechanics

I am examining how ISO Schematron rules interact with RELAX NG grammars to validate complex structural and semantic patterns across TEI headers and bibliographies. Analyzing explicit XPath assertions reveals how embedded constraint checks systematically catch non-fatal semantic warnings and complex relational constraints, such as cross-referencing valid target identifiers, which standard structural schemas cannot enforce on their own.

Addressing Structural and Technical Gaps

I am bridging the gap between broad pedagogical peer-review principles and precise automated continuous integration configurations. By evaluating specific command-line XML processing tools and workflow orchestration files, I am establishing how automated linting scripts reduce manual editorial overhead and provide instant diagnostic feedback for contributors submitting pull requests.

Gathering Academic Citations and Case Studies

I am planning targeted inquiries to secure precise academic literature citations, digital object identifiers, and institutional case studies related to continuous integration setups in digital scholarly editions. This will allow me to finalize a comprehensive theoretical, practical, and pedagogical framework complete with evaluation rubrics and audit checklists.

[utppublishing.com

The Global Medieval Sourcebook: Creating a Sustainable Digital Anthology of Medieval Texts and Translations | Seminar - University of Toronto Press](https://utppublishing.com/doi/abs/10.3138/seminar.57.3.1)[github.com

Petri Gracilis Commentarius in Libros Sententiarum, Liber 1, Lectiones 1–20 - GitHub](https://github.com/Library-of-Digital-Latin-Texts/MAA-gracilis-1-1-20)[access.archive-ouverte.unige.ch

Re-conceiving the Christian scholastic corpus with the scholastic commentaries and texts archive - Archive ouverte UNIGE](https://access.archive-ouverte.unige.ch/access/metadata/07719c93-ba9f-4b86-bb0a-b01902c09b33/download)[brill.com

Chapter 5 Philology: Standards for Digital Editing in - Brill](https://brill.com/display/book/9789004400351/BP000014.xml?language=en)[journals.uchicago.edu

Digital Corpora and Scholarly Editions of Latin Texts: Features and Requirements of Textual Criticism | Speculum: Vol 92, No S1 - The University of Chicago Press: Journals](https://www.journals.uchicago.edu/doi/10.1086/693823)[kups.ub.uni-koeln.de

Digital Scholarly Editions as Interfaces](https://kups.ub.uni-koeln.de/9118/1/10_witt.pdf)[journals.openedition.org

Finding Relatedness: pathways for detecting textual relatedness in the medieval scholastic corpus - OpenEdition Journals](https://journals.openedition.org/methodos/10987)[researchgate.net

(PDF) 6 Editions - ResearchGate](https://www.researchgate.net/publication/380100585_6_Editions)[community.scta.info

LombardPress Diplomatic Transcription Guidelines - SCTA Community](https://community.scta.info/pages/lombardpress-schema-diplomatic.html)[github.com

adunning/xml-model-validator - GitHub](https://github.com/adunning/xml-model-validator)[stfx.ca

English Department - St. Francis Xavier University](https://www.stfx.ca/department/english)[stfx.ca

English Department - Courses | St. Francis Xavier University](https://www.stfx.ca/programs-courses/courses/481)[stfx.ca

Who We Are | St. Francis Xavier University](https://www.stfx.ca/research/research-institutes-centres-networks/digital-humanities/who-we-are)[stfx.ca

Digital Humanities | St. Francis Xavier University](https://www.stfx.ca/research/research-institutes-centres-networks/digital-humanities)[stfx.ca

Faculty Publications – English | St. Francis Xavier University](https://www.stfx.ca/department/english/faculty-publications)[stfx.ca

DHSI-East: Digital Archives & Databases | St. Francis Xavier University](https://www.stfx.ca/research/research-institutes-centres-networks/digital-humanities-centre/dhsi-east/past-events-0)[stfx.ca

DHSI-East | St. Francis Xavier University](https://www.stfx.ca/research/digital-humanities/dhsi-east)[stfx.ca

StFX English Department celebrates five new books | St. Francis Xavier University](https://www.stfx.ca/news/English-Department-book-launch)

Verifying Infrastructure Configurations

I am reviewing the technical specifications for continuous integration workflows, ensuring that rule-based Schematron verification and standard RELAX NG validation are executed efficiently using command-line processors. Analyzing how automated checks process pull requests reveals how continuous integration prevents malformed XML or broken cross-references from entering main project branches.

Consolidating Case Study Architecture

I am evaluating distributed data models across major digital scholarly initiatives, such as the Scholastic Commentaries and Texts Archive and the Perseids platform. Tracing how these projects employ centralized schema definitions alongside decentralized Git repositories demonstrates how digital editions maintain strict structural uniformity while enabling multi-institutional collaboration.

Finalizing Pipeline Syntax and Guidance

I am conducting final technical checks to verify precise syntax for automated continuous integration action files, ensuring accurate execution steps for schema parsing and linter deployment. Following this, I will synthesize these findings into a comprehensive framework covering technical architectures, practical merge conflict resolutions, and structured pedagogical rubrics.

Integrating Automated XML Validation Pipelines

I am examining specialized automation setups designed for XML validation, such as using specialized action workflows that combine RELAX NG parsers with XSLT engines to validate complex processing instructions. Incorporating specialized CLI tools into source control platforms allows editorial teams to run inline diagnostic checks, emit step summaries, and flag structural schema mismatches automatically during repository contributions.

Synthesizing Institutional Digital Humanities Initiatives

I am reviewing institutional frameworks and regional training hubs focused on digital humanities scholarship, such as those promoting sustainable digital archives, databases, and micro-editions. Examining projects that integrate linked open data principles and long-term digital preservation standards helps establish best practices for training researchers in durable textual editing.

Exploring Theoretical and Pedagogical Frameworks

I am planning targeted searches to further examine theoretical perspectives on document modeling, contrasting single-tree representations with non-linear or graph-based markup approaches. Additionally, I will investigate the cognitive mechanics of error-driven learning in classroom editing workflows to refine peer-review rubrics and undergraduate training guidelines.

[gist.github.com

ipfs-view-npm-registry.md - GitHub Gist](https://gist.github.com/dignifiedquire/575965768b301f58506e)[github.com

FYP_similartags/RerunKeming/allTags_test.txt at master - GitHub](https://github.com/lint0011/FYP_similartags/blob/master/RerunKeming/allTags_test.txt)[slideshare.net

Validating XML and JSON Documents Using Oxygen Scripting | PDF - Slideshare](https://www.slideshare.net/slideshow/validating-xml-and-json-documents-using-oxygen-scripting/258712883)[github.com

dracor-org/dracor-validate-action: GitHub action for validating TEI files](https://github.com/dracor-org/dracor-validate-action)[sourceforge.net

Page 5 | Best Open Source Mac Data Formats Software 2026](https://sourceforge.net/directory/data-formats/mac/?page=5)[pcreview.co.uk

(OT) Microsoft being sued AGAIN! - PC Review](https://www.pcreview.co.uk/threads/ot-microsoft-being-sued-again.1966285/)[ftp3.us.freebsd.org

FreeBSD Ports Collection Index](http://ftp3.us.freebsd.org/pub/FreeBSD-CVS/www/data/es/ports/master-index.html)[vb-net.com

FreeBSD Ports Collection Index - VB.NET](https://www.vb-net.com/Freebsd/FreeBSDPortsCollectionIndex.htm)[scribd.com

Skills | PDF - Scribd](https://www.scribd.com/document/819588329/Skills)

Integrating Project Preservation Principles

I am incorporating core principles from long-term digital preservation projects, such as the Endings Project, to evaluate how static file generation and minimal-dependency architectures interface with version-controlled markup. Aligning these static site methodologies with continuous integration workflows ensures that scholarly digital editions remain accessible, archival-grade, and resilient to infrastructure decay over time.

Examining Specialized Publishing Frameworks

I am investigating domain-specific peer-review and validation ecosystems, including the Digital Latin Library's submission pipeline and TEI customization guidelines. Exploring how specialized editorial boards leverage automated schema checks alongside formal peer-review registries highlights how decentralized contributions transition into authoritative, peer-reviewed digital editions.

Refining Sustainable Editorial Infrastructure

I am initiating targeted queries into the specific governance models, citation systems, and automated validation scripts utilized by established scholarly digital publishing initiatives. This will finalize a comprehensive framework spanning technical continuous integration setups, long-term archival stability, and structured pedagogical rubrics.

[dh-tech.adho.org

Embracing Endings: Principles for Digital Longevity and Their Importance for Research Software Engineers | DHTech](https://dh-tech.adho.org/blog/2023/08/07/endings-principles/)[hcmc.uvic.ca

A brief history of BBTI - Humanities Computing and Media Centre (HCMC)](https://hcmc.uvic.ca/project/bbti/about.html)[libcal.library.ubc.ca

TEI 2026: Low-cost, low-infrastructure, low-threshold strategies for authoring and publishing TEI (and friends) - UBC Library - University of British Columbia](https://libcal.library.ubc.ca/event/4043887)[mapoflondon.uvic.ca

MoEML: Mission Statement - The Map of Early Modern London](https://mapoflondon.uvic.ca/mission_statement.htm)[aacademica.org

Against infrastructure: global approaches to digital scholarly editing - Acta Académica](https://www.aacademica.org/gimena.delrio.riande/224.pdf)[fabian-moss.de

Minimal Publishing of Multimodal Sources: Integrating MEI, TEI, and More | Fabian C. Moss](https://fabian-moss.de/talk/minimal-publishing-of-multimodal-sources-integrating-mei-tei-and-more/)[adamdjbrett.com

Digital Humanities Part 5: Preserving Digital Humanities Projects | Adam DJ Brett](https://www.adamdjbrett.com/blog/dh-part-5-preserving-digital-humanities-projects/)[dhi.ac.uk

The Quest for the “Hundred Year” Digital Scholarly Edition](https://www.dhi.ac.uk/books/digital-editing-and-publishing/rosselli-del-turco/)[cambridge.org

Digital Scholarly Editing in Practice - Cambridge University Press & Assessment](https://www.cambridge.org/core/elements/digital-scholarly-editing-in-practice/033E79028A8F05B3537450D993A121C3)[tei-c.org

News - Text Encoding Initiative](https://tei-c.org/news/)[researchgate.net

Decoupling Quality Control and Publication: The Digital Latin Library](https://www.researchgate.net/publication/402936927_Decoupling_Quality_Control_and_Publication_The_Digital_Latin_Library_and_the_Traveling_Imprimatur)

Evaluating Digital Longevity and Minimal Computing

I am analyzing the Endings Project principles and minimal computing paradigms to address the long-term sustainability of digital scholarly editions. Shifting from complex server-side environments toward static site architectures built on plain HTML, CSS, and client-side rendering frameworks mitigates software entropy, ensuring project availability well beyond typical funding lifecycles.

Resolving Infrastructure and Maintenance Vulnerabilities

I am exploring strategies to decouple quality control from web hosting dependencies by combining static site generators with versioned data repositories and archivers like Zenodo. This resolves major vulnerabilities inherent in dynamic database-backed platforms, creating predictable archival releases that maintain academic integrity without ongoing server maintenance budgets.

Investigating Pedagogical and Systemic Downstream Effects

I am initiating targeted inquiries into the broader systemic and pedagogical consequences of introducing continuous integration and minimal computing into humanities curricula. I will analyze the trade-offs between complex markup standards and simplified publishing workflows, as well as the learning curve friction experienced by students engaging with version control and automated quality assurance.

[ospolicyobservatory.uvic.ca

Draft Report: Research Data Management Support in the Humanities: Challenges and Recommendations | Open Scholarship Policy Observatory](https://ospolicyobservatory.uvic.ca/draft-report-rdm/)[cambridge.org

Digital Scholarly Editing in Practice - Cambridge University Press & Assessment](https://www.cambridge.org/core/elements/digital-scholarly-editing-in-practice/033E79028A8F05B3537450D993A121C3)[aacademica.org

Against infrastructure: global approaches to digital scholarly editing - Acta Académica](https://www.aacademica.org/gimena.delrio.riande/224.pdf)[cdr.lib.unc.edu

FirstReport16Oct22 - Carolina Digital Repository](https://cdr.lib.unc.edu/downloads/js956x788)[researchgate.net

Making Marx More Readable: A Minimal Computing Approach to a Community-Driven Edition of Capital Vol. 1 - ResearchGate](https://www.researchgate.net/publication/410806010_Making_Marx_More_Readable_A_Minimal_Computing_Approach_to_a_Community-Driven_Edition_of_Capital_Vol_1)[tei-c.org

TEI-C Elections 2023 - Text Encoding Initiative](https://tei-c.org/news/2023/08/06/tei-c-elections-2023/)[dhi.ac.uk

The Quest for the “Hundred Year” Digital Scholarly Edition](https://www.dhi.ac.uk/books/digital-editing-and-publishing/rosselli-del-turco/)[adamdjbrett.com

Digital Humanities Part 6: Preservation through Minimal Computing and GO::DH](https://www.adamdjbrett.com/blog/dh-part-6-minimal-computing-and-go-dh/)[adamdjbrett.com

Digital Humanities Part 5: Preserving Digital Humanities Projects | Adam DJ Brett](https://www.adamdjbrett.com/blog/dh-part-5-preserving-digital-humanities-projects/)

Evaluating Static Edition Longevity Models

I am analyzing long-term digital preservation strategies by examining minimal computing initiatives like the Endings Project alongside lightweight publishing frameworks. Synthesizing these approaches demonstrates how decoupling raw XML content and static HTML/CSS views from dynamic server infrastructure prevents software obsolescence, ensuring that scholarly editions survive institutional shifts and server deprecations.

Resolving Infrastructure Decay vs Scholarly Authority Gaps

I am addressing the critical vulnerability of project degradation where complex content management stacks rot over time, undermining scholarly citations and accessibility. By contrasting heavy, database-backed web applications with static, version-controlled reading editions, I am establishing how minimal-dependency architectures safeguard textual evidence without sacrificing computational rigour or collaborative annotation capabilities.

Investigating Domain-Specific Quality Assurance Workflows

I will perform targeted searches to examine automated quality assurance workflows used within major text encoding consortium repositories, advanced Schematron assertions for cross-referencing document metadata, and formal rubrics that align continuous integration feedback with undergraduate peer review.

Evaluating Pedagogy and Version Control Learning Curves

I am analyzing the cognitive load and technical hurdles students face when learning version control, schema validation, and collaborative markup in undergraduate digital humanities courses. Synthesizing pedagogical strategies helps balance the rigor of strict XML encoding standards with intuitive, error-driven learning environments that support novice researchers without overwhelming them.

Resolving Static Longevity and Dynamic Validation Trade-Offs

I am addressing the friction between complex automated quality assurance pipelines and long-term static preservation. By harmonizing rigorous continuous integration testing during the active editorial phase with zero-dependency static releases for archiving, I am bridging the gap between dynamic computational editing and multi-decade project longevity.

Targeting Deep Quality Assurance Case Studies

I am initiating focused searches into specialized continuous integration workflows, static edition longevity standards, and undergraduate digital humanities rubrics. This deep exploration will finalize a comprehensive blueprint covering continuous validation setups, long-term archival resilience, and structured peer-review pedagogy.

[teibyexample.org

Module 8: Customising TEI, ODD, Roma - TEI by Example](https://teibyexample.org/exist/examples/TBED08v00.htm)[wwp.neu.edu

Customizing TEI to Check Pointers - Women Writers Project - Northeastern University](https://www.wwp.neu.edu/research/publications/documentation/other/checking_pointers_in_ODD.html)[driscoll.dk

TEI XML customisation for manuscript description](http://driscoll.dk/fasnl/FASNL_msDesc_v1_2016.html)[livingstoneonline.org

Livingstone Online TEI P5 Encoding Guidelines](https://livingstoneonline.org/resources/livingstone-online-tei-p5-encoding-guidelines)[tei-c.org

23 Documentation Elements - The TEI Guidelines - Text Encoding Initiative](https://tei-c.org/release/doc/tei-p5-doc/en/html/TD.html)[e-ditiones.github.io

Encoding guidelines for the teiHeader of manuscripts - E-Ditiones](https://e-ditiones.github.io/ODD/ODD-header_MS.html)[tei-c.org

jTEI input customizationRon Van den Branden ron.vandenbranden@kantl.be, Martin Holmes mholmes@uvic.ca. - Text Encoding Initiative](https://tei-c.org/release/doc/tei-p5-exemplars/html/tei_jtei.doc.html)[spear-prosop.org

Encoding Manual and TEI Customization for SPEAR: Syriaca Persons, Events, and Relations](https://spear-prosop.org/documentation/Schema/SPEAR.html)[dvpp.uvic.ca

1. The Digital Victorian Periodical Poetry Schema and Guidelines for Encoding](https://dvpp.uvic.ca/dvpp.html)

Synthesizing Domain Constraints and Rule Engines

I am analyzing advanced Schematron implementation patterns that enforce contextual business logic across metadata headers and structural references in text encoding. Examining explicit XPath test assertions reveals how custom schema layers validate fine-grained constraints—such as ensuring pointer targets resolve to valid identifiers or mandating mandatory descriptive elements—which standard grammar schemas cannot validate in isolation.

Resolving Technical Barriers and Pedagogical Friction

I am examining key institutional barriers and controversies surrounding continuous integration and custom schema design in digital humanities education. By evaluating the complexity of authoring custom validation rules alongside student learning curves within open version control platforms, I am balancing the operational overhead of running automated XML validation scripts against the educational benefits of instant diagnostic compiler feedback.

Investigating Critical Controversies and Consensus

I will perform targeted searches to analyze documented critiques and dissenting opinions regarding the complexity of customization languages in text encoding systems, performance bottlenecks in large automated validation test suites, and potential student anxiety stemming from public code review processes in open repositories.

[researchgate.net

(PDF) Teaching Computational Methods to Humanities Students - ResearchGate](https://www.researchgate.net/publication/384778860_Teaching_Computational_Methods_to_Humanities_Students)[ceur-ws.org

Teaching Computational Methods to Humanities Students - CEUR-WS.org](https://ceur-ws.org/Vol-2364/44_paper.pdf)[academiccommons.columbia.edu

Doing· Digital Humanities - Columbia Academic Commons](https://academiccommons.columbia.edu/doi/10.7916/D8T445R9/download)[books.openedition.org

11. Highly Available Dissertations: Open Sourcing Humanities Scholarship - OpenEdition Books](https://books.openedition.org/obp/21175?lang=en)[pmc.ncbi.nlm.nih.gov

Digital humanities in the era of digital reproducibility: towards a fairest and post-computational framework - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11111558/)[shawnaross.github.io

Using Digital Humanities in the Classroom Companion - GitHub Pages](https://shawnaross.github.io/teachdh/)[cuny.manifoldapp.org

Punk Rock Pedagogies: DIY, Minimal, No-Code/Low-Code, Resource Constrained, Learning Frameworks for the (Digital) Humanities | Manifold @CUNY](https://cuny.manifoldapp.org/read/punk-rock-pedagogies-diy-minimal-no-code-low-code-resource-constrained-learning-frameworks-for-the-digital-humanities-36e69847-b193-4914-899b-f996d2c782fb)[dhdebates.gc.cuny.edu

2. Reprogramming the Invisible Discipline: An Emancipatory Approach to Digital Technology through Higher Education | People, Practice, Power](https://dhdebates.gc.cuny.edu/read/people-practice-power/section/2e2b8286-3210-432b-a753-81f2d2cddca6)[aubreemarshall.com

DH Teaching Statement - Aubree Marshall](https://www.aubreemarshall.com/dh-teaching-statement.html)

Synthesizing Pedagogical Frameworks and Student Cognitive Load

I am examining pedagogical strategies within digital humanities classrooms to address student anxiety and steep learning curves associated with command-line tools, Git version control, and strict XML schema validation. Evaluating approaches like minimal-computing frameworks, low-code/no-code onboarding, and peer-assisted workflows reveals how breaking down computational tasks into step-by-step diagnostic exercises fosters confidence, demystifies automated error logs, and transforms technical troubleshooting into collaborative learning opportunities.

Resolving Technical Gatekeeping vs. Methodological Rigor

I am exploring how to balance the institutional scarcity of specialized technical infrastructure with the demand for computational rigor in textual editing. By contrasting resource-heavy server deployments with low-barrier, process-oriented methods—such as static site generators and accessible continuous integration pipelines—I am establishing how non-specialist students can meaningfully engage with version-controlled editing without being deterred by complex software gatekeeping.

Formulating Final Structural Synthesis

I am preparing a final search turn to gather explicit continuous integration configuration patterns, static site longevity standards, and structured peer-review rubric templates. This step will complete a unified blueprint connecting continuous XML quality assurance, durable minimal-computing archiving, and inclusive undergraduate digital methods instruction.

Evaluating Validation Performance and Specialized Platform Architecture

I am analyzing the technical performance profiles and diagnostic outputs of rule-based validation engines, contrasting local interactive development environments with headless continuous integration execution. By examining platform architectures such as Perseids and SCTA, I am determining how specific constraint validation rules govern domain-specific text services, linked data resolution, and manuscript commentary models without incurring excessive computational overhead.

Resolving Diagnostic Clarity and Validation Bottlenecks

I am addressing the gap between raw, command-line validation outputs and student-friendly error reporting in collaborative repositories. Evaluating how custom validation scripts process Schematron assertions allows me to resolve bottlenecks where complex error messages obscure actionable structural fixes, ensuring automated feedback remains constructive for undergraduate editors.

Exploring Specialized Technical Nuances

I am launching targeted searches to explore specific performance nuances of constraint validation engines, long-term static site preservation principles within text encoding projects, and specialized schema validation rules used in medieval commentary frameworks.

[adamdjbrett.com

Digital Humanities Part 6: Preservation through Minimal Computing and GO::DH](https://www.adamdjbrett.com/blog/dh-part-6-minimal-computing-and-go-dh/)[dhq-static.digitalhumanities.org

No Boutique or Fashionable Technologies: Project Development, Mentorship, and Sustainability - DHQ Static](https://dhq-static.digitalhumanities.org/pdf/000660.pdf)[dhi.ac.uk

The Quest for the “Hundred Year” Digital Scholarly Edition](https://www.dhi.ac.uk/books/digital-editing-and-publishing/rosselli-del-turco/)[scholarlyediting.org

On Automating Editions | Volume 41 | Scholarly Editing Journal](https://scholarlyediting.org/issues/41/on-automating-editions/)[aacademica.org

Against infrastructure: global approaches to digital scholarly editing - Acta Académica](https://www.aacademica.org/gimena.delrio.riande/224.pdf)[adamdjbrett.com

Digital Humanities Part 5: Preserving Digital Humanities Projects | Adam DJ Brett](https://www.adamdjbrett.com/blog/dh-part-5-preserving-digital-humanities-projects/)[mapoflondon.uvic.ca

MoEML: Mission Statement - The Map of Early Modern London](https://mapoflondon.uvic.ca/mission_statement.htm)[lemdo.uvic.ca

MoEML Mayoral Shows: MoMS Editorial Guidelines - Linked Early Modern Drama Online](https://lemdo.uvic.ca/moms/edGuide.html)[ospolicyobservatory.uvic.ca

Draft Report: Research Data Management Support in the Humanities: Challenges and Recommendations | Open Scholarship Policy Observatory](https://ospolicyobservatory.uvic.ca/draft-report-rdm/)

Synthesizing Preservation Principles and Static Architecture

I am analyzing how digital humanities projects operationalize long-term digital preservation through minimal computing principles and static site generation architectures. Examining findings from the Endings Project at the University of Victoria demonstrates that abandoning server-side software, relational databases, and dynamic content management stacks in favor of pre-rendered HTML, CSS, and client-side rendering engines protects digital scholarly editions from software rot, link decay, and infrastructure abandonment.

Resolving Technical Obsolescence versus Editorial Richness

I am addressing the fundamental tension between the need for sophisticated, highly expressive textual encoding standards and the mandate for long-term technical sustainability. Synthesizing workflows that use custom schema transformation scripts to output static alpha editions reveals how projects retain rich underlying XML markup for scholarship while delivering lightweight, platform-agnostic, and archival-grade web interfaces that survive well past active funding cycles.

Investigating Formal Standardization and Pedagogical Scaffolding

I am planning targeted searches to examine exact formal specification rules across XML standards, schema validation specs, and peer-review rubrics. This will allow me to finalize a comprehensive blueprint linking automated validation architectures, static digital longevity guidelines, and structured undergraduate research rubrics.

[balisage.net

Balisage Paper: Schematron as XSLT Interface, and Advanced Validation Models](https://www.balisage.net/Proceedings/vol30/html/Kalvesmaki01/BalisageVol30-Kalvesmaki01.html)[en.wikipedia.org

Schematron - Wikipedia](https://en.wikipedia.org/wiki/Schematron)[github.com

schema/svrl.sch at main - GitHub](https://github.com/Schematron/schema/blob/main/svrl.sch)[metadata101.org

Schematron - Metadata 101](https://metadata101.org/schematron/)[w3.org

Service Modeling Language, Version 1.1 - W3C](https://www.w3.org/TR/2007/WD-sml-20070926/)[docs.rs

schematron 0.4.0 - Docs.rs](https://docs.rs/crate/schematron/latest)[github.com

maa-hedon-d3c6-reviewed-repo/readme.md at master · Library-of](https://github.com/Library-of-Digital-Latin-Texts/maa-hedon-d3c6-reviewed-repo/blob/master/readme.md)[researchgate.net

Decoupling Quality Control and Publication: The Digital Latin Library](https://www.researchgate.net/publication/402936927_Decoupling_Quality_Control_and_Publication_The_Digital_Latin_Library_and_the_Traveling_Imprimatur)

Synthesizing Validation Engine Expressiveness

I am evaluating the technical capabilities and performance characteristics of ISO Schematron implementations across different query binding languages, specifically examining how XPath 3.0 and XSLT 3.0 enable advanced business rules like cross-document validation and external resource checks. Analyzing lightweight, native runtime engines alongside transform-based architectures illustrates how rule-based constraint checking can be executed efficiently in headless continuous integration environments without requiring heavy, full-stack dependencies.

Resolving Peer-Review Decoupling and Static Longevity

I am analyzing how digital publishing initiatives, such as the Library of Digital Latin Texts, decouple quality control from web platform hosting by establishing independent peer-review registries and version-controlled repositories. Harmonizing these decentralized review models with static site preservation principles resolves the tension between rigorous academic peer review and long-term digital longevity, ensuring critical editions remain permanently citeable without ongoing dynamic server maintenance.

Diving into Deep Empirical and Regional Case Studies

I am launching targeted searches to explore empirical studies on digital humanities pedagogy, focusing on student learning curves and anxiety related to version control and public pull-request reviews. Additionally, I am investigating theoretical critiques surrounding overlapping hierarchy models in text markup, regional digital humanities lab frameworks, and long-term static site principles to finalize a multi-layered synthesis.

[balisage.net

Balisage Paper: Why TEI stand-off annotation doesn't quite work](https://www.balisage.net/Proceedings/vol5/html/Banski01/BalisageVol5-Banski01.html)[companions.digitalhumanities.org

The Text Encoding Initiative and the Study of Literature - Blackwell Companions to Digital Humanities](https://companions.digitalhumanities.org/DLS/?chapter=content/9781405148641_chapter_25.html)[blogs.library.duke.edu

Graphs, Trees, and Streams: The TEI Data Model - Duke Collaboratory for Classics Computing (DC3)](https://blogs.library.duke.edu/dcthree/2013/08/26/graphs-trees-and-streams-the-tei-data-model/)[ids-pub.bsz-bw.de

Proceedings of Extreme Markup Languages®](https://ids-pub.bsz-bw.de/files/4537/Witt_Multiple_hierarchies_new_aspects_of_an_old_solution_2004.pdf)[tei-c.org

v. A Gentle Introduction to XML - The TEI Guidelines - Text Encoding Initiative](https://tei-c.org/release/doc/tei-p5-doc/en/html/SG.html)[journals.openedition.org

Why TEI Stand-off Markup Authoring Needs Simplification - OpenEdition Journals](https://journals.openedition.org/jtei/1838)[zfdg.de

›A digital edition is not visible‹ - some thoughts on the nature and persistence of digital editions](https://zfdg.de/2020_005)[digitalstudies.org

Chapter 5Digital editing as autopoietic process - Digital Studies / Le champ numérique](https://www.digitalstudies.org/article/id/7285/)[nl.ijs.si

1. A Gentle Introduction to XML](https://nl.ijs.si/et/talks/esslli02/reader/gentleintro.pdf)[chwp.arts.ubc.ca

Liu and Smith, “ A Relational Database Model for Text Encoding”](https://chwp.arts.ubc.ca/CHC2007/Liu_Smith/Liu_Smith.htm)[dhi.ac.uk

The Quest for the “Hundred Year” Digital Scholarly Edition](https://www.dhi.ac.uk/books/digital-editing-and-publishing/rosselli-del-turco/)[endings.uvic.ca

Principles | Principes - The Endings Project - UVic](https://endings.uvic.ca/principles.html)[bostondh.org

2025 Symposium - Boston DH](https://bostondh.org/symposium-2025/)

Synthesizing Document Theories and Standoff Architectures

I am examining foundational debates in digital textuality, particularly evaluating the strengths and limitations of the Ordered Hierarchy of Content Objects model when encoding complex manuscript features. Synthesizing insights on overlapping markup structures, standoff annotation layers, and autopoietic editorial models reveals how modern digital editions accommodate multidimensional textual realities while maintaining structural coherence across primary and secondary document hierarchies.

Harmonizing Static Preservation with Dynamic Validation

I am resolving the core friction between dynamic continuous integration testing environments and multi-decade digital longevity. By combining rigorous, rule-based continuous validation during the active editorial phase with zero-dependency static site releases following minimal computing principles, I am establishing a complete lifecycle model that preserves rich scholarly annotations without risking dynamic software obsolescence.

Finalizing the Comprehensive Editorial Framework

Having reached full evaluative analytical saturation across theoretical data models, continuous validation pipelines, project case studies, and pedagogical rubrics, I am completing the research phase. I am now transitioning to compiling the final comprehensive report detailing continuous integration architectures, static preservation standards, and structured undergraduate peer-review rubrics.

The initial research has returned a lot of information. I'm sorting through it and organizing it. This will make sure the whole thing flows well and hits all the key points you asked for.

This is it! I’m bringing it all together. Jotting down my final thoughts, polishing everything up, and making sure I give you my very best work.

## References (APA)

1. tei-c.org. (n.d.). *v. A Gentle Introduction to XML - The TEI Guidelines - Text Encoding Initiative*. https://tei-c.org/release/doc/tei-p5-doc/en/html/SG.html
2. balisage.net. (n.d.). *Balisage Paper: Hierarchies within range space*. https://www.balisage.net/Proceedings/vol13/html/Piez01/BalisageVol13-Piez01.html
3. blogs.library.duke.edu. (n.d.). *Graphs, Trees, and Streams: The TEI Data Model - Duke Collaboratory for Classics Computing (DC3)*. https://blogs.library.duke.edu/dcthree/2013/08/26/graphs-trees-and-streams-the-tei-data-model/
4. companions.digitalhumanities.org. (n.d.). *The Text Encoding Initiative and the Study of Literature - Blackwell Companions to Digital Humanities*. https://companions.digitalhumanities.org/DLS/?chapter=content/9781405148641_chapter_25.html
5. digitalstudies.org. (n.d.). *Chapter 5Digital editing as autopoietic process - Digital Studies / Le champ numérique*. https://www.digitalstudies.org/article/id/7285/
6. balisage.net. (n.d.). *Balisage Paper: Why TEI stand-off annotation doesn't quite work*. https://www.balisage.net/Proceedings/vol5/html/Banski01/BalisageVol5-Banski01.html
7. harvest.usask.ca. (n.d.). *Digital Textuality, Autopoietic Editing, and the Courten MS A Project Paper Submitted to the College of Graduate Studies and Res - HARVEST*. https://harvest.usask.ca/bitstreams/e3768511-7aee-47cc-8209-310de59ca695/download
8. access.archive-ouverte.unige.ch. (n.d.). *Re-conceiving the Christian scholastic corpus with the scholastic commentaries and texts archive - Archive ouverte UNIGE*. https://access.archive-ouverte.unige.ch/access/metadata/07719c93-ba9f-4b86-bb0a-b01902c09b33/download
9. tei-c.org. (n.d.). *Using the TEI GitHub Repository*. https://tei-c.org/guidelines/p5/using-the-tei-github-repository/
10. community.scta.info. (n.d.). *SCTA Data Management Policies and Practices*. https://community.scta.info/policy/data-management
11. tei-c.org. (n.d.). *23 Documentation Elements - The TEI Guidelines - Text Encoding Initiative*. https://www.tei-c.org/release/doc/tei-p5-doc/fr/html/TD.html
12. community.scta.info. (n.d.). *LombardPress Diplomatic Transcription Guidelines - SCTA Community*. https://community.scta.info/pages/lombardpress-schema-diplomatic.html
13. driscoll.dk. (n.d.). *TEI XML customisation for manuscript description*. http://driscoll.dk/fasnl/FASNL_msDesc_v1_2016.html
14. docs.rs. (n.d.). *schematron 0.4.0 - Docs.rs*. https://docs.rs/crate/schematron/latest
15. github.com. (n.d.). *schema/svrl.sch at main*. https://github.com/Schematron/schema/blob/main/svrl.sch
16. balisage.net. (n.d.). *Balisage Paper: Schematron as XSLT Interface, and Advanced Validation Models*. https://www.balisage.net/Proceedings/vol30/html/Kalvesmaki01/BalisageVol30-Kalvesmaki01.html
17. metadata101.org. (n.d.). *Schematron - Metadata 101*. https://metadata101.org/schematron/
18. libcal.library.ubc.ca. (n.d.). *TEI 2026: Low-cost, low-infrastructure, low-threshold strategies for authoring and publishing TEI (and friends) - UBC Library - University of British Columbia*. https://libcal.library.ubc.ca/event/4043887
19. github.com. (n.d.). *dracor-org/dracor-validate-action: GitHub action for validating TEI files*. https://github.com/dracor-org/dracor-validate-action
20. wwp.neu.edu. (n.d.). *Customizing TEI to Check Pointers - Women Writers Project - Northeastern University*. https://www.wwp.neu.edu/research/publications/documentation/other/checking_pointers_in_ODD.html
21. cuny.manifoldapp.org. (n.d.). *Punk Rock Pedagogies: DIY, Minimal, No-Code/Low-Code, Resource Constrained, Learning Frameworks for the (Digital) Humanities | Manifold @CUNY*. https://cuny.manifoldapp.org/read/punk-rock-pedagogies-diy-minimal-no-code-low-code-resource-constrained-learning-frameworks-for-the-digital-humanities-36e69847-b193-4914-899b-f996d2c782fb
22. kups.ub.uni-koeln.de. (n.d.). *Digital Scholarly Editions as Interfaces*. https://kups.ub.uni-koeln.de/9118/1/10_witt.pdf
23. github.com. (n.d.). *curateteaching/digitalpedagogy: Digital Pedagogy in the Humanities: Concepts, Models, and Experiments*. https://github.com/curateteaching/digitalpedagogy
24. researchgate.net. (n.d.). *Decoupling Quality Control and Publication: The Digital Latin Library*. https://www.researchgate.net/publication/402936927_Decoupling_Quality_Control_and_Publication_The_Digital_Latin_Library_and_the_Traveling_Imprimatur
25. researchgate.net. (n.d.). *(PDF) An Investigation Into the Perceived Effectiveness of GitHub Repositories to Teach Programming*. https://www.researchgate.net/publication/386074958_An_Investigation_Into_the_Perceived_Effectiveness_of_GitHub_Repositories_to_Teach_Programming
26. github.com. (n.d.). *adunning/xml-model-validator*. https://github.com/adunning/xml-model-validator
27. adamdjbrett.com. (n.d.). *Digital Humanities Part 5: Preserving Digital Humanities Projects | Adam DJ Brett*. https://www.adamdjbrett.com/blog/dh-part-5-preserving-digital-humanities-projects/
28. dh-tech.adho.org. (n.d.). *Embracing Endings: Principles for Digital Longevity and Their Importance for Research Software Engineers | DHTech*. https://dh-tech.adho.org/blog/2023/08/07/endings-principles/
29. researchgate.net. (n.d.). *Making Marx More Readable: A Minimal Computing Approach to a Community-Driven Edition of Capital Vol. 1*. https://www.researchgate.net/publication/410806010_Making_Marx_More_Readable_A_Minimal_Computing_Approach_to_a_Community-Driven_Edition_of_Capital_Vol_1
30. adamdjbrett.com. (n.d.). *Digital Humanities Part 6: Preservation through Minimal Computing and GO::DH*. https://www.adamdjbrett.com/blog/dh-part-6-minimal-computing-and-go-dh/
31. tei-c.org. (n.d.). *TEI Technical Council virtual “F2F”, 2020-05-01 / 05-03 - Text Encoding Initiative*. https://tei-c.org/activities/council/meetings/tei-technical-council-virtual-f2f-2020-05-01-05-03-05-05-05-12/
32. researchgate.net. (n.d.). *The International Image Interoperability Framework (IIIF): raising awareness of the user benefits for scholarly editions*. https://www.researchgate.net/profile/Julien-Raemy/publication/322538093_The_International_Image_Interoperability_Framework_IIIF_raising_awareness_of_the_user_benefits_for_scholarly_editions/links/5aa7e785458515b024faec14/The-International-Image-Interoperability-Framework-IIIF-raising-awareness-of-the-user-benefits-for-scholarly-editions.pdf

_32 citation marker(s) carried no resolvable source in the DOM and were dropped; see the `*_citations.json` sidecar._
