## **16 Content**

**Fonts for Polytonic Greek**

A font maps code points to glyphs. If a font lacks a glyph for a code point, the
text is not wrong — it simply cannot be displayed, and you will see a replacement
box. Students routinely mistake this for data corruption and "fix" correct files.

Not every Unicode font covers the Greek Extended block, and coverage of rare
combinations is uneven even among fonts that advertise polytonic support. Choose
a font with documented coverage and use it consistently.

| Font | Coverage | Notes |
| --- | --- | --- |
| Gentium Plus | Full polytonic; extensive diacritics | Free; designed for linguistic and philological use |
| New Athena Unicode | Full polytonic, epigraphic and papyrological marks | Free; standard in classics |
| Brill | Full polytonic, extensive scholarly range | Free for academic use; excellent rendering |
| IFAO-Grec Unicode | Polytonic plus papyrological symbols | Free; strong for documentary texts |
| Noto Serif / Sans | Good polytonic coverage | Free; consistent cross-platform rendering |

Install at least two. When a character fails to render, the diagnostic step is to
view the file in a different font: if the second font shows the character, your
data is fine and the first font simply lacked the glyph. If every font shows a
box, the code point may genuinely be wrong — at which point you inspect code
points as in the previous section.

For your XML editor and terminal, set a polytonic-capable monospace or serif face
explicitly rather than accepting the default. A default font that silently fails
on rare combinations will cost you an afternoon in Week 6, when you are working
with exactly those combinations.

**Takeaway:** A missing glyph is a font problem, not a data
problem; diagnose by changing fonts before changing files.

---


## **17 Content**

**Keyboard Layouts and Input Methods**

You will type a good deal of polytonic Greek this term, and the input method you
choose determines both your speed and — critically — the normalization form of
what you produce.

| Method | Platform | Approach | Typical output form |
| --- | --- | --- | --- |
| Greek Polytonic layout | Windows, macOS, Linux | System layout with dead keys for diacritics | NFC on Windows; often NFD on macOS |
| Keyman (Galaxie / classical layouts) | Cross-platform | Installable layout with mnemonic input | Configurable; usually NFC |
| Unicode hex input | All | Type the code point directly | Exactly what you type |
| Copy from a digital corpus | All | Reuse existing text | Whatever the source used — verify |

The system polytonic layouts use *dead keys*: a key that produces no character
itself but modifies the next keystroke. Typing the smooth-breathing dead key
followed by alpha produces ἀ. Combinations chain, so breathing, accent, and iota
subscript can be entered in sequence. The layouts repay a few hours of practice
early in the term, and this weekend is the right time.

The last row of the table is the one to be careful about. Text copied from a
digital corpus, a PDF, or a website arrives in whatever form that source used,
which is frequently not NFC and occasionally not consistent within a single
document. Always normalize after pasting, and never assume that text which looks
right is encoded right.

Whatever method you adopt, verify its output once, deliberately: type a
multi-diacritic character such as ᾧ, dump its code points, and learn what your
own setup produces. Knowing your own tooling's default saves diagnosis later.

**Takeaway:** Verify what normalization form your own keyboard
produces, and always normalize text pasted from external sources.

---


## **18 Content**

**Oxygen XML Editor**

Oxygen is the standard professional environment for TEI work and is available to
you through the university. Its advantage over a general text editor is that it
understands the schema your document declares.

The features that matter for this course:

- **Schema-aware completion.** With the TEI or EpiDoc schema associated, Oxygen offers only elements valid at the cursor position, which prevents a large class of encoding errors as you type (TEI Consortium, 2026; EpiDoc Guidelines, 2026).
- **Continuous validation.** Errors are flagged as you work rather than at commit time, with the specific rule violated.
- **Author mode.** A visual editing view driven by a stylesheet, useful when the raw markup becomes dense enough to obscure the text.
- **XPath evaluation.** Query your own document interactively — indispensable from Week 8, when the apparatus makes documents large.
- **Built-in XSLT and transformation scenarios.** Preview output without a separate toolchain.

Two configuration steps to take before Week 2. First, associate the TEI P5
schema with your documents so validation is live from the outset. Second, set the
editor font to a polytonic-capable face from the previous section, and set the
file encoding explicitly to UTF-8.

Oxygen also has Git integration adequate for staging and committing. It is
perfectly acceptable to use it — with the caveat from Lesson 1.1 that graphical
Git tools do not expose hooks, trailers, or pickaxe searches, so you will need
the command line for those.

**Takeaway:** Oxygen's value is schema-aware validation as you
type, catching encoding errors before they enter the repository.

---


## **19 Content**

**VS Code as an XML and Git Environment**

VS Code is the alternative, and for many students the better one, because it
combines XML editing with the strongest available Git integration in a single
free tool.

| Extension | Provides | Needed from |
| --- | --- | --- |
| XML (Red Hat) | Schema validation, completion, formatting | Week 2 |
| Scholarly XML | TEI-aware completion and RelaxNG validation | Week 2 |
| GitLens | Inline blame, history, and authorship at each line | Week 4 |
| Git Graph | Visual DAG of the repository | Week 1 |
| Python | Running normalization and analysis scripts | Week 1 |

GitLens deserves specific mention for this course. It annotates each line of a
file with the commit that last changed it, the author, and the message —
transforming a static transcription into a document you can interrogate line by
line. Hovering over a reading in your edition shows when it entered and why,
provided you wrote a useful commit body. It renders the argument of Lesson 1.1
visible in the editor.

The practical advantage of consolidating on VS Code is that transcription,
validation, Python scripting, and version control happen in one window. The
practical disadvantage relative to Oxygen is a weaker Author mode and less mature
XSLT support. Many students in this course use both: Oxygen for heavy encoding
work, VS Code for scripting and Git.

Whichever you choose, configure it this weekend rather than in Week 2. Set the
font, set UTF-8, install the extensions, and verify that a deliberately invalid
XML file is flagged. Discovering that validation was never enabled is a poor way
to begin the cataloguing assignment.

**Takeaway:** VS Code with the XML and GitLens extensions puts
encoding, scripting, and version history in one window.

---


## **20 Content**

**Accounts to Create This Week**

Three accounts are required, and all three should exist before Week 2 because
each has an approval or setup delay that will otherwise cost you class time.

| Service | Purpose | Needed by | Setup note |
| --- | --- | --- | --- |
| GitHub | Remote hosting, submission, peer review | Week 2 | Use your StFX address; match your Git `user.email` |
| Transkribus | HTR model training and transcription | Week 4 | Free tier sufficient; model training needs credits |
| THREAD | Collaborative transcription environment | Week 4 | Account approval is not instantaneous |

For GitHub, the email address matters more than it appears. Commits are
associated with an author by email; if your local `user.email` does not match a
verified address on your GitHub account, your commits will appear as an
unrecognized author and will not be attributed to you in the interface. Set the
same address in both places.

Enable two-factor authentication on GitHub, which is required for account
security and affects how you authenticate from the command line: password
authentication over HTTPS is not available, so you will use either a personal
access token or an SSH key. Generate an SSH key this weekend and add it to your
account; the alternative is discovering the requirement mid-class when you first
try to push.

For Transkribus, note that the free tier covers a good deal of transcription but
that HTR *model training* consumes credits. Week 4 will use a shared course
allocation, but create the account now and familiarize yourself with the
interface.

**Takeaway:** Create all three accounts this week; GitHub's
email must match your Git configuration, and THREAD approval is not immediate.

---


## **21 Content**

**Case Study: Structure-Aware OCR of Greek Critical Editions**

A recent study illustrates why the encoding discipline in this lesson must
precede any use of automation, and it is worth examining in detail because you
will replicate a small version of it in Week 4.

Angleraud et al. (2026) address the digitization of printed Greek critical
editions — a genuinely hard problem because the printed page is *polycentric*.
A single page carries the primary text, a dense multi-layered apparatus at the
foot, marginal line numbers, and canonical reference milestones such as Stephanus
pagination embedded in the margins. Conventional OCR reads the page as a single
column of text and interleaves these registers into an unusable transcript.

The researchers fine-tuned vision-language models — Qwen3-VL and DeepSeek-OCR-2 —
on a synthetic corpus of 185,000 page images generated from TEI/XML sources with
controlled typographic variation. The models were trained to emit structured
output that explicitly separates the registers, marking milestones with `<ref>`
and marginalia with `<note>` rather than flattening them into the text
(Angleraud et al., 2026).

The results are worth reading carefully in both directions. The fine-tuned
Qwen3-VL-8B model achieved a median character error rate of 1.0% — excellent by
any standard, and better than most students achieve transcribing by hand. But the
same study documents "catastrophic page-level failures," in which the model's
output drifts entirely from the image and it generates fluent, grammatical,
entirely fabricated Greek. The models also struggled systematically with symbolic
ambiguity, particularly failing to distinguish alphabetic Greek numerals from
ordinary lexical tokens (Angleraud et al., 2026).

That combination — excellent median accuracy with occasional total fabrication —
is the defining risk profile of machine transcription, and it is why this course
records provenance in commit trailers and measures error rates against your own
ground truth. A model wrong 1% of the time uniformly could be trusted and spot-
checked. A model that is 99% correct and occasionally invents a page cannot.

**Takeaway:** Machine transcription can achieve a 1.0% median
error rate while occasionally fabricating entire pages, which is why provenance
and ground truth are non-negotiable.

---


## **22 Content**

**What the OCR Case Study Implies for Your Workflow**

Draw out the consequences, because they shape how the rest of the term is
structured.

If failures were uniformly distributed, sampling would be a valid quality
control: check 10% of the output, estimate the error rate, and correct
proportionally. Catastrophic page-level failure defeats sampling entirely,
because the failures are concentrated and a sample may contain none of them while
the document contains several (Angleraud et al., 2026).

If failures were *visible*, they would be self-correcting: fluent output that is
obviously wrong gets caught. But a hallucinated page of Greek is grammatical and
plausible. It reads as competent Greek because the model is very good at
producing competent Greek — which is the source of the problem, not a mitigation
of it. The only detection method is comparison against the image.

| Failure profile | Effective control | Why |
| --- | --- | --- |
| Uniform low-rate errors | Sampling and spot-check | Sample is representative of the whole |
| Concentrated catastrophic failure | Full comparison against source | Sample may miss the affected region entirely |
| Fluent fabrication | Comparison against the image, not the text | Output is internally plausible and self-consistent |
| Symbolic ambiguity (numerals) | Targeted review of known-hard categories | Failure is systematic and therefore predictable |

Three practices follow, and each has a place later in the course. Every page of
machine output is checked against the facsimile, not sampled. Machine output is
committed separately from your corrections, so that the raw state remains
recoverable and the error rate remains measurable. And known-hard categories —
numerals, abbreviations, marginalia — receive targeted review rather than being
trusted at the general rate.

**Takeaway:** Concentrated, fluent failures defeat sampling, so
machine output must be compared page by page against the image.

---


## **23 Content**

**Machine Learning and Philological Judgement**

The OCR case study concerns transcription. A second body of work concerns
something more ambitious — machine assistance in *editorial* judgement — and it
frames a question this course returns to repeatedly.

Cowen-Breen et al. (2023) describe Logion, a BERT-based model trained on
premodern Greek, applied to the detection of scribal errors and the suggestion of
emendations. The model learns the statistical regularities of Greek as attested
in a large corpus, and can therefore identify passages that are anomalous with
respect to those regularities — which is, in a limited but real sense, what a
philologist does when a reading strikes them as wrong.

The limitation is precise and worth stating carefully. The model identifies
*statistical* anomaly, not *textual* error. A passage may be unusual because a
scribe erred, or because the author wrote something unusual — and authors of
literary interest are, notoriously, the ones who write unusual things. The model
cannot make that distinction, because the distinction requires knowing what the
author was doing, which is not in the training data (Cowen-Breen et al., 2023).

This maps directly onto the Friday step of every week from Week 4 onward. The
machine's proposal is evidence — genuinely useful evidence, of a kind that would
take a human a long time to assemble. It is not a conclusion. Your task on those
Fridays is to adjudicate the proposal against the manuscript and against your
knowledge of the text, and to record in the commit body why you accepted or
rejected it.

The pedagogical value of such tools may lie less in their proposals than in the
articulation they force. Explaining why a statistically anomalous reading is
nevertheless correct requires stating your reasoning explicitly — which is
exactly the reasoning that Giarratano's print editions failed to preserve.

**Takeaway:** Language models detect statistical anomaly, not
textual error, so their proposals are evidence for your judgement rather than
substitutes for it.

---


## **24 Content**

**Codicological Description and the Vocabulary of the Object**

Before selecting a passage, you need enough descriptive vocabulary to say what
you are looking at. Comparative Oriental Manuscript Studies provides the standard
framework for describing manuscripts as physical objects, and its terminology is
what Week 2's cataloguing assignment will require (Bausi et al., 2015).

| Term | Refers to | Why it matters for selection |
| --- | --- | --- |
| Folio | A leaf; recto is the front, verso the back | Passage locations are cited as f. 42r, f. 42v |
| Quire / gathering | A bundle of folded leaves forming a unit | Quire boundaries often coincide with damage or loss |
| Ruling | Lines guiding the script | Affects legibility and line segmentation for HTR |
| Hand | The writing of one scribe | A change of hand mid-passage complicates model training |
| Lacuna | A physical gap where text is lost | Requires editorial restoration; adds difficulty |
| Palimpsest | A reused leaf with erased underwriting | Requires multispectral imaging; usually too hard for this term |
| Marginalia | Notes added in the margins | Must be encoded distinctly from the main text |
| Colophon | A scribal note, often with date and place | Valuable metadata for the Week 2 TEI header |

Bausi et al. (2015) emphasize that codicological description is not preliminary
to textual work but part of it: the physical structure of the book carries
evidence about how the text was transmitted, and an edition that ignores the
object is missing data.

For your purposes this week, this vocabulary is the checklist you take to the
selection decision. You should be able to state, of the passage you choose, how
many folios it spans, whether it is written in one hand, whether it contains
lacunae or marginalia, and whether a colophon is present anywhere in the
manuscript.

**Takeaway:** You need codicological vocabulary to describe what
you have chosen, and the physical structure of the book is evidence, not context.

---


## **25 Content**

**Choosing Your Passage: The Criteria That Matter**

The selection due today governs the entire term. Every assignment from Week 2 to
Week 13 operates on this passage, and a poor choice cannot be corrected in
November. Weigh the following.

| Criterion | Target | Why |
| --- | --- | --- |
| Length | 20–40 lines | Enough for meaningful collation; small enough to encode fully |
| Legibility | Clear, consistent hand | HTR training in Week 4 requires readable baselines |
| Witnesses | At least 2, ideally 3 | Week 7 collation requires more than one witness |
| Image availability | Open-licensed, high resolution | Week 3 IIIF work requires images you may use |
| Textual interest | Known variants or cruxes | Weeks 8 and 12 need something to discuss |
| Prior editions | At least one available | Provides a comparison for your editorial decisions |
| Script | Not a difficult minuscule or palimpsest | Manageable within a thirteen-week term |

The witness requirement is the one students most often underestimate. A passage
surviving in a single manuscript makes Week 7's collation exercise impossible in
any real sense — you cannot align witnesses you do not have, and substituting
printed editions is a poor approximation of the exercise. Confirm that at least
two witnesses are digitized and accessible *before* committing to a passage.

Image licensing is the second common failure. Many manuscript images are online
but under restrictive terms; a IIIF manifest you cannot legally build or share
undermines Week 3 and the final publication in Week 13. Prefer institutions with
explicit open licensing — the Vatican Library, the British Library, the
Bibliothèque nationale, e-codices, and similar repositories that publish IIIF
endpoints openly.

Resist the temptation toward difficulty. A famously contested passage in a
notoriously difficult hand is a compelling choice in September and an
unfinishable one in November. Textual interest matters, but tractability matters
more, and a clean passage encoded completely is worth more than an ambitious one
abandoned in Week 9.

**Takeaway:** Confirm at least two accessible witnesses and open
image licensing before committing; those two constraints eliminate most
unworkable choices.

---


## **26 Content**

**Verifying Your Choice Before Committing to It**

Do not select from a catalogue description alone. Run the following checks, all
of which are quick and any of which can disqualify a passage.

- **Open the images.** Confirm the resolution is sufficient to read individual letters when zoomed, not merely to identify the page.
- **Locate the IIIF manifest.** Most major repositories expose a manifest URL; find it now, because Week 3 depends on it and its absence is a serious obstacle.
- **Check the licence explicitly.** Find the stated terms, not an assumption. Note the required attribution formula.
- **Identify the second witness.** Confirm it is digitized, accessible, and covers the same passage — not merely the same work.
- **Read ten lines.** Actually attempt to read them. A hand that looks clear at page scale can be much harder at line scale.
- **Find one prior edition.** Confirm a published text exists for comparison.
- **Check for a change of hand.** Scan the passage boundaries for a shift in script.

If a passage fails on witnesses or on licensing, discard it and choose again —
those two are not recoverable later. Failing on textual interest is survivable;
failing on legibility is survivable if the passage is short. Failing on image
resolution is not, because everything downstream depends on being able to read
the source.

Bring the results of these checks to Week 2. The cataloguing assignment, due
Friday September 18, will ask you to produce a TEI header describing this
manuscript, and much of what the header needs — repository, shelfmark, date,
material, extent, hand — is what you are gathering now (Bausi et al., 2015; TEI
Consortium, 2026).

**Takeaway:** Verify images, manifest, licence, and second
witness before committing to a passage; the first four checks are the ones that
cannot be fixed later.

---


## **27 Content**

**Recording the Choice in the Repository**

The selection is ungraded but not informal. Record it in your repository, as your
first substantive commit, in a form that a reviewer can evaluate.

Your `README.md` should state:

- The work, author, and passage reference (book, chapter, line, or folio range).
- The primary manuscript: repository, shelfmark, date, and folio range.
- The second and any further witnesses, with the same identifying detail.
- The image source, IIIF manifest URL, and licence terms.
- At least one prior edition, cited.
- Two or three sentences on why you chose this passage.

The last item is the one that matters intellectually. Stating your reasons now
produces a record you can evaluate later — in Week 10's consolidation session you
will reread it and see whether the passage delivered what you expected, and in
Week 13's publication you will have the beginning of an editorial introduction
already written.

Commit it with a message that follows the conventions from Lesson 1.1:

```text
docs(readme): select MS Vat. gr. 1209 ff. 42r-43v as edition passage

Chosen for a clear tenth-century minuscule hand, two further digitized
witnesses (BnF gr. 2934, BL Add. 17210), and open IIIF access via the
Vatican Library. Passage covers 34 lines with two known variants
discussed in the Wachtel edition, giving material for the Week 8
apparatus.
```

Note what that body does: it states the choice, gives the reasons against the
selection criteria, and records the evidence that the criteria were met. Three
months from now it is the only surviving record of why you are working on this
text.

**Takeaway:** Record the passage and your reasons for choosing
it as a committed document; it becomes the seed of your editorial introduction.

---


## **28 Content**

**How the Encoding Foundation Carries Through the Term**

It is worth seeing where each element of this lesson reappears, because the
material can feel like unmotivated preliminaries until it becomes load-bearing.

| Established here | Becomes essential in | Consequence of neglect |
| --- | --- | --- |
| NFC normalization | Week 5 error rates | Error rate inflated by encoding mismatch, not transcription error |
| Pre-commit hook | Every week | Unnormalized text accumulates and must be fixed retroactively |
| Code point inspection | Weeks 5–7 | Encoding faults misdiagnosed as transcription or collation faults |
| Polytonic font | Weeks 4–6 | Correct data mistaken for corruption; correct files "repaired" |
| Diacritic vocabulary | Week 6 normalization | Cannot state what is being normalized or justify the decision |
| Adscript / subscript distinction | Week 6 | Silent normalization of an editorial convention |
| Codicological vocabulary | Week 2 TEI header | Header incomplete; cataloguing assignment weakened |
| Passage with 2+ witnesses | Week 7 collation | Collation exercise cannot be performed as designed |
| Open image licence | Weeks 3 and 13 | IIIF manifest unbuildable; edition unpublishable |

The pattern is that encoding problems do not present as encoding problems. They
present as inexplicable error rates, spurious collation variants, mysterious diff
noise, and files that look corrupted but are not. Every one of those symptoms
sends students hunting in the wrong place, and the hours lost are hours not spent
on the text.

This is why the course front-loads the infrastructure. Boschetti (2010) makes the
same argument about corpus preparation: normalization is prerequisite to
analysis, and analysis performed on unnormalized data yields results that are
wrong without appearing wrong.

**Takeaway:** Encoding faults present as inexplicable error
rates and phantom variants, which is why they must be eliminated before the
analysis that would otherwise be blamed.

---


## **29 Content**

**A Complete Setup Checklist**

Consolidate everything from both meetings of Week 1 into a verifiable list.
Complete it before Week 2 begins.

**Version control (Lesson 1.1).**

- `git config --global user.name` and `user.email` set, matching your GitHub account.
- `git config --global init.defaultBranch main` set.
- `git config --global diff.algorithm histogram` set.
- Repository created with the directory structure from Lesson 1.1.
- `.gitattributes` committed with `* text=auto eol=lf`.
- `.gitignore` committed, covering `.DS_Store`, editor backups, and `.vscode/`.

**Encoding (this lesson).**

- At least two polytonic fonts installed and verified on a multi-diacritic character.
- A polytonic input method installed, and its output normalization form verified.
- `tools/normalize_nfc.py` written and committed.
- `pre-commit` hook installed and tested on a deliberately decomposed file.

**Environment.**

- Oxygen or VS Code installed, with TEI schema validation confirmed working.
- Editor font set to a polytonic face; encoding set to UTF-8.
- Python 3 available on the command line.

**Accounts.**

- GitHub account with verified StFX email, 2FA enabled, SSH key added.
- Transkribus account created.
- THREAD account requested.

**Passage.**

- Passage selected against the criteria in section 25.
- All seven verification checks in section 26 completed.
- `README.md` committed recording the choice and the reasons.

Test the hook rather than assuming it works: create a file containing decomposed
Greek, stage it, commit, and confirm the committed content is NFC. An untested
hook is not a control.

**Takeaway:** Complete and verify the checklist before Week 2;
test the pre-commit hook rather than assuming it functions.

---


## **30 Content**

**Synthesis: Infrastructure as Editorial Method**

The two meetings of this week have covered version control and character
encoding, which look like technical preliminaries to the real work of the course.
They are not preliminaries. They are the conditions that make the real work
possible, and the argument connecting them is worth stating explicitly.

An edition makes claims: this manuscript reads thus, this variant is to be
preferred, this reading is corrupt. A *scholarly* edition additionally makes those
claims inspectable — a reader can see what the evidence was and how the editor
reasoned from it. Huskey (2024) frames this as reproducibility and explainability,
and identifies version control as the mechanism that delivers both for a digital
edition.

Character encoding is the same argument one level down. Before a claim about a
reading can be inspected, the reading must be represented unambiguously. Text
that is sometimes NFC and sometimes NFD does not make one claim; it makes a claim
that varies by platform and by tool. Normalization is what makes the object of the
claim stable enough to be argued about (Unicode Consortium, 2025).

Both, finally, are about the same thing: making your work *checkable*. The commit
history lets a reader check your reasoning. Consistent encoding lets a machine
check your text. The three-step cycle that begins in Week 2 — manual, then
deterministic, then AI-assisted — is an extended exercise in checking, and it
depends entirely on the two foundations laid this week.

**Due today, Friday September 4.** Your manuscript passage, selected against the
criteria in section 25, verified by the checks in section 26, and recorded in a
committed `README.md`. The selection is ungraded. Every graded assignment for the
next twelve weeks builds on it.

**Next week.** Topic 2 begins the three-step cycle: Tuesday you hand-write a TEI
header in a plain text editor, Wednesday you validate it against the schema in
Oxygen and build RDF triples, and Friday you compare AI-generated metadata against
the header you wrote yourself.

**Takeaway:** Version control makes your reasoning checkable and
normalization makes your text checkable; the whole course is an exercise in
checking, and this week built its preconditions.

---

## References

Angleraud, N., Karamolegkou, A., Sagot, B., & Clérice, T. (2026).
*Structure-aware text recognition for ancient Greek critical editions* (arXiv:
2603.02803v3). Inria.

Bausi, A., Borbone, P. G., Briquel-Chatonnet, F., Buzi, P., Gippert, J., Macé,
C., Maniaci, M., Melis, Z., Parodi, L. E., Witakowski, W., & Sokolinski, E.
(Eds.). (2015). *Comparative Oriental manuscript studies: An introduction*.
COMSt.

Boschetti, F. (2010). Analytical developments for the Homer Multitext:
Palaeography, orthography, morphology. In *Improving OCR accuracy for classical
critical editions*.

Chacon, S., & Straub, B. (2014). *Pro Git* (2nd ed.). Apress.
https://git-scm.com/book/en/v2

Cowen-Breen, C., Brooks, C., Graziosi, B., & Haubold, J. (2023). Machine
learning and the future of philology: A case study. *Transactions of the American
Philological Association, 153*(1), 253–284.

EpiDoc Guidelines. (2026). *Critical apparatus*.
https://epidoc.stoa.org/gl/latest/supp-apparatus.html

Huskey, S. J. (2024). Committing to reproducibility and explainability: Using
Git as a research journal. *International Journal of Digital Humanities, 6*,
9–21. https://doi.org/10.1007/s42803-023-00076-9

Python Software Foundation. (n.d.). *unicodedata — Unicode database*. Python 3.12
documentation. https://docs.python.org/3/library/unicodedata.html

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and
interchange* (Version 4.12.0). https://tei-c.org/guidelines/p5/

Unicode Consortium. (2025). *Unicode Standard Annex #15: Unicode normalization
forms* (Revision 57). https://www.unicode.org/reports/tr15/
