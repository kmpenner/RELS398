# Lesson 9.1 — Manual Morphological Parsing, Lemmatization, and Treebanking

*RELS 398 / ENGL 398 · Topic 9: Lemmatization · Meeting #23 (Tue Nov 3)*

***Step 1 of the three-step cycle: manual.** Today you parse, lemmatize, and construct syntactic dependency trees for a passage by hand using lexica and established treebank standards. That gold-standard annotation is the reference for Wednesday's rule-based taggers and Friday's AI evaluation.*

---

## **01 Content**

**What Lemmatization and Parsing Accomplish**

Linguistic annotation transforms a raw sequence of characters into an analytically structured text. In earlier modules of this course, you transcribed manuscript witnesses (Topic 4), reconciled conflicting readings (Topic 5), regularized orthographic divergence (Topic 6), and constructed a critical apparatus of textual variants (Topics 7 and 8). Throughout those stages, your computational unit remained the orthographic string—the literal characters inscribed on parchment or papyrus. While string matching allows editors to collate witnesses and record divergences, it leaves the grammatical engine of the language opaque to computational queries. A computer cannot inherently deduce that the Greek surface forms *ἔγνων*, *γιγνώσκει*, and *γνωσθήσεται* are all manifestations of the same underlying lexical entry, nor can it determine whether a given noun functions as the subject or object of an elided verb.

Lemmatization is the algorithmic or manual process of mapping an inflected surface token to its canonical dictionary headword, known as the lemma. Morphological parsing decomposes that surface token into its constituent grammatical categories—such as part of speech, person, number, tense, mood, voice, case, and gender. Syntactic dependency treebanking goes one step further by explicitly mapping the structural relationships of government and dependency between words in a sentence, establishing which head term controls each dependent phrase.

In a digital edition, these layers of annotation convert text into a rich knowledge graph. Instead of searching merely for strings of characters, an editor or researcher can query for all instances where a verb of perception governs an accusative participle, or locate all occurrences of third-declension feminine abstract nouns across a corpus. This linguistic transparency is essential for tracing syntactic evolution across dialects and historical periods.

Together, these operations bridge the divide between philological close reading and computational distant reading. When an edition is annotated with rigorous morphological and syntactic data, scholars can query grammatical constructions across millions of words, analyze stylistic shifts across centuries, and build accurate translation alignments. Today, you will establish the reference ground truth by performing these analytical operations entirely by hand using authoritative lexica and formal grammatical standards.

**The takeaway for this page:** Lemmatization and morphological parsing convert unstructured character sequences into semantically and grammatically queryable linguistic data.

---

## **02 Content**

**The Anatomy of an Inflected Word Form**

To parse a historical language by hand, an editor must understand the morphological anatomy of the word. Ancient Greek and Latin are synthetic, fusional languages: their words are composed of morphemes—minimal units of meaning or grammatical function—fused together into a single surface token. Unlike agglutinative languages where each morpheme corresponds to a single discrete grammatical feature (such as a separate affix for plural and a separate affix for dative case), fusional languages compress multiple grammatical categories into single, indivisible affixes.

A typical inflected word in Greek or Latin contains a lexical root, thematic vowels or derivational affixes that form a stem, and inflectional endings. In verbs, the word may also incorporate an augment or reduplication marking past time or completed aspect, tense-formative suffixes (such as the sigma of the Greek sigmatic aorist), mood morphemes, and primary or secondary personal endings. For instance, in the Classical Greek verb *ἐπαιδεύσαμεν* ("we educated"), the token decomposes into a temporal augment (*ἐ-*), the verbal stem (*παιδευ-*), the aorist tense-formative marker (*-σ-*), and the secondary first-person plural active ending (*-αμεν*).

In nominal and adjectival systems, the stem attaches directly to case-number-gender terminations. Because these terminations are fusional, a single morpheme like the Greek *-ων* simultaneously denotes genitive case and plural number across masculine, feminine, and neuter nouns. The philologist’s task during manual parsing is to isolate these constituent layers, stripping inflectional morphology to identify the base lexical stem while recording the full bundle of grammatical features encoded in the surface form.

**The takeaway for this page:** Fusional morphology bundles multiple grammatical categories into single affixes, requiring editors to systematically isolate stems, affixes, and inflectional terminations.

---

## **03 Content**

**The Concept of the Lemma and Lexicographical Conventions**

The lemma is an abstract lexicographical convention chosen to represent the entire inflectional paradigm of a lexeme. While speakers and scribes produce surface word forms in context, lexica organize vocabulary under standardized citation forms. The choice of citation form is not dictated by universal linguistic principles, but by historical lexicographical tradition specific to each linguistic community.

In Ancient Greek lexicography, such as the *Greek-English Lexicon* of Liddell, Scott, and Jones (LSJ), verbs are cited in the first-person singular present active indicative (e.g., *παιδεύω*, *ποιέω*, or *δίδωμι*). If a verb is deponent or lacks an active form in standard usage, it is cited in the middle/passive voice (e.g., *γίγνομαι*, *δέχομαι*). In Latin lexicography, such as Lewis and Short or the *Oxford Latin Dictionary*, verbs are similarly cited in the first-person singular present active indicative (e.g., *amo*, *rego*), traditionally accompanied by the second-person singular or present infinitive, perfect active indicative, and supine to identify the principal parts. In contrast, languages like Hebrew or Classical Syriac cite verbs under the third-person masculine singular perfect/past form (the uninflected root), while modern languages like German or French cite the infinitive.

| Linguistic Tradition | Canonical Verb Citation Form | Sample Surface Form | Canonical Dictionary Lemma |
|---|---|---|---|
| Ancient Greek (LSJ) | 1st person singular present active indicative | ἔγνωσαν | γιγνώσκω |
| Latin (Lewis & Short) | 1st person singular present active indicative | rexerunt | rego |
| Classical Hebrew (BDB) | 3rd person masculine singular perfect (root) | יִכְתְּבוּ | כָּתַב |
| Classical Syriac (Payne Smith) | 3rd person masculine singular perfect (root) | ܟܬܰܒܘ | ܟܬܰܒ |
| Modern English / French | Present active infinitive / Infinitif | wrote / écrivit | write / écrire |

When assigning a lemma during manual analysis, the editor must strictly adhere to the chosen authority's citation standard. Assigning the infinitive *παιδεύειν* or the stem *παιδευ-* as a Greek lemma violates the standard and breaks downstream computational collation against Perseus and PROIEL databases.

**The takeaway for this page:** A lemma is a standardized lexicographical citation form, and manual annotation must strictly follow the reference authority's canonical convention.

---

## **04 Content**

**Tokenization and Segmental Ambiguity**

Before a word can be assigned a lemma or parsed grammatically, the continuous textual stream of a manuscript must be divided into discrete linguistic tokens. In modern printed texts, white space and punctuation marks provide explicit boundary markers. In pre-modern historical manuscripts, however, scribes routinely wrote in *scriptio continua* (continuous script without word spaces) or utilized idiosyncratic punctuation systems that do not correspond to modern syntactic boundaries.

Tokenization is therefore an interpretive editorial act rather than a purely mechanical division. Even when editing a normalized text with standard spacing, Greek and Latin present complex segmental phenomena where a single orthographic unit contains multiple grammatical words, or where a single grammatical word spans multiple orthographic tokens. Consider the Latin enclitic conjunction *-que* ("and") attached to a noun: *senatusque* constitutes a single orthographic string, but linguistically it consists of two distinct tokens: the noun *senatus* (nominative singular masculine) and the coordinating conjunction *-que*. To parse the sentence correctly, the editor must split *senatusque* into two discrete tokens.

Similar phenomena abound in Ancient Greek with proclitics and enclitics (e.g., *εἴ_γε*, *οὐ_πώποτε*), crasis (the contraction of two words across a boundary, such as *κἀγώ* from *καὶ ἐγώ*), and elision (where a final vowel is dropped before an initial vowel, as in *δ' ἄλλος* for *δὲ ἄλλος*). Prodelision or aphaeresis (where an initial vowel is absorbed by a preceding long vowel or diphthong, such as *ὦ 'γάθ'* for *ὦ ἀγαθέ*) presents an identical challenge. If an editor fails to segment crasis or split enclitics during manual preparation, the resulting composite string cannot be mapped to any valid dictionary lemma.

**The takeaway for this page:** Tokenization is an interpretive philological decision that requires isolating enclitics, crasis, and contracted forms into discrete grammatical units.

---

## **05 Content**

**Morphological Ambiguity and Paradigmatic Syncretism**

The central challenge in manual morphological parsing is morphological ambiguity. In an inflected language, a single surface form frequently corresponds to multiple theoretical analyses across different grammatical categories, a phenomenon known as paradigmatic syncretism. Without sentence-level context, the surface form is indeterminate.

Consider the Latin form *profundum*. In isolation, *profundum* can be parsed as:

- An accusative singular masculine form of the adjective *profundus* ("deep").
- A nominative singular neuter form of the adjective *profundus*.
- An accusative singular neuter form of the adjective *profundus*.
- A nominative singular neuter substantive noun (*profundum*, "the depth/abyss").
- An accusative singular neuter substantive noun (*profundum*).

Similarly, the Greek form *λόγου* is unambiguously the genitive singular of *λόγος*, but the form *λόγοι* could theoretically be nominative plural or vocative plural. Forms like *ταύτῃ* can be a dative singular feminine demonstrative pronoun ("to this woman"), an instrumental/manner adverb ("in this way"), or a locative adverb ("here").

To resolve these ambiguities during manual analysis, the philologist must examine the syntactic environment: the case government of the governing verb, prepositions, agreement with neighboring nouns or adjectives, and discourse context. Manual parsing establishes the gold-standard benchmark precisely because a trained human scholar can resolve homophony by synthesizing syntactic, semantic, and pragmatic clues that automated algorithms frequently miss.

**The takeaway for this page:** Paradigmatic syncretism creates pervasive surface ambiguity that can only be resolved through systematic analysis of syntactic context and semantic government.

---

## **06 Content**

**Verbal Complexity: Stems, Aspect, and Principal Parts**

The verbal system of Ancient Greek represents one of the most intricate inflectional systems in Indo-European linguistics, presenting significant hurdles for rule-based and computational parsing. Unlike modern English, which builds verb forms primarily through analytic periphrasis (e.g., "I will have seen"), Ancient Greek utilizes a synthetic system of six distinct principal parts, each exhibiting its own aspectual stem.

These aspectual stems are not derived from one another by simple concatenation of suffixes. Instead, they frequently involve deep phonological alterations, including ablaut (vowel gradation between zero-grade, e-grade, and o-grade), infixation, suffixation, reduplication, and suppletion (where entirely different historical roots combine into a single paradigm). For example, the verb *ὁράω* ("to see") constructs its principal parts from three completely distinct roots:

- Present active stem: *ὁρα-* (*ὁράω*)
- Future middle stem: *ὀπ-* (*ὄψομαι*)
- Aorist active stem: *ἰδ-* (*εἶδον*)
- Perfect active stem: *ὀπωπ-* (*ὄπωπα*)
- Perfect middle/passive stem: *ἑωρα-* (*ἑώραμαι*)
- Aorist passive stem: *ὀφθ-* (*ὤφθην*)

When an editor encounters the surface token *δόντι* in a text, simple suffix stripping cannot trace the word back to its dictionary lemma *δίδωμι* ("to give"). The editor must recognize *δόντι* as the masculine/neuter dative singular of the second aorist active participle (root *δο-*). Manual parsing requires the scholar to trace surface aspectual stems back to their parent lexeme through systematic knowledge of historical phonology and principal parts.

**The takeaway for this page:** Ancient verbal systems rely on distinct aspectual stems and suppletive roots, requiring philological identification of principal parts rather than naive affix stripping.

---

## **07 Content**

**Nominal and Adjectival Inflection: Agreement and Case Government**

Nominal systems in historical Indo-European languages convey syntactic relations through nominal declension. In Ancient Greek and Latin, nouns, pronouns, adjectives, and articles inflect for three grammatical dimensions: case (nominative, genitive, dative, accusative, vocative, and in Latin, ablative), number (singular, plural, and in Greek, dual), and grammatical gender (masculine, feminine, neuter).

Manual parsing of nominals requires identifying the declension class (first/a-stem, second/o-stem, third/consonantal stem) and verifying grammatical agreement. In Classical Greek, an attributive adjective or definite article must agree with its governing noun in gender, number, and case, even if the noun and adjective belong to completely different declension classes and carry entirely different surface endings. For example, in the phrase *τῇ καλῇ πόλει* ("to the beautiful city"), the article *τῇ* and adjective *καλῇ* belong to the first declension, while the noun *πόλει* belongs to the third declension; nevertheless, all three agree in feminine gender, singular number, and dative case.

Furthermore, manual parsing requires identifying how cases are governed by surrounding syntactic heads. A genitive case may represent possession, partitive relation, source, value, or the object of a specific verb of remembering or ruling; an accusative may represent a direct object, extent of space/time, or an adverbial accusative of respect; a dative may represent an indirect object, instrument, agent, reference, or location. Recording the morphological features of a noun is thus the foundation for determining its syntactic dependency role in the sentence.

**The takeaway for this page:** Nominal parsing involves identifying declension classes, verifying gender-number-case agreement across phrases, and establishing syntactic case government.

---

## **08 Content**

**Closed-Class Categories: Particles, Conjunctions, and Prepositions**

While nouns and verbs constitute open lexical classes that constantly admit new words, closed-class functional words—particles, conjunctions, prepositions, and adverbs—form the syntactic connective tissue of historical prose and poetry. In Ancient Greek in particular, particles (*μέν*, *δέ*, *γάρ*, *οὖν*, *ἄν*, *δή*, *τοί*, *καίτοι*) play a vital role in organizing discourse, marking narrative transitions, indicating evidentiality, and modulating modal nuance.

Closed-class words are predominantly indeclinable: they do not take inflectional endings for case, person, or tense. However, manual parsing of closed-class items is far from trivial. Many functional words are polysemous and homophonous with forms from other word classes. For example, the Greek token *ὡς* can function as an adverb of manner ("as", "how"), a coordinating or subordinating conjunction ("that", "in order that", "since"), a preposition governing the accusative case ("to", used only with persons), or an accentual variant with numerals ("approximately"). Modal particles like *ἄν* or epic *κε(ν)* fundamentally alter the mood semantics of associated optatives and subjunctives, turning potential assertions into counterfactual or deliberative structures.

Similarly, prepositions (*ἐπί*, *παρά*, *πρός*, *διά*, *κατά*) govern multiple distinct cases, shifting their semantic meaning fundamentally depending on whether the governed noun is in the genitive, dative, or accusative. When parsing a preposition like *παρά*, the editor must record its part of speech (adposition) and document the case of its complement (*παρὰ τοῦ βασιλέως* = "from the king" [genitive/source]; *παρὰ τῷ βασιλεῖ* = "beside the king" [dative/location]; *παρὰ τὸν βασιλέα* = "to the presence of the king" / "contrary to the king" [accusative/motion or opposition]).

**The takeaway for this page:** Closed-class particles and prepositions must be categorized by their specific syntactic function and case government rather than treated as static lexical glosses.

---

## **09 Content**

**The Universal Dependencies (UD) Taxonomy and UPOS Tagset**

To ensure that linguistic annotations are computationally interoperable across different languages and software pipelines, the international computational linguistics community established the Universal Dependencies (UD) framework (de Marneffe et al., 2021). UD provides a standardized, cross-linguistically consistent taxonomy for grammatical description, encompassing part-of-speech tagging, morphological features, and syntactic dependency trees.

The foundational layer of UD annotation is the Universal Part-of-Speech (UPOS) tagset, which defines exactly 17 coarse-grained categories applicable to any human language. Every token in a text must receive exactly one of these 17 tags:

| Universal Tag | Category Label | Grammatical Definition and Historical Examples |
|---|---|---|
| `NOUN` | Noun | Common substantives (*λόγος*, *homo*, *urbs*, *βιβλίον*) |
| `PROPN` | Proper Noun | Names of people, deities, places (*Σωκράτης*, *Roma*, *Ἀθῆναι*) |
| `VERB` | Verb | Main lexical verbs (*γράφω*, *scribo*, *δίδωμι*, *amavit*) |
| `AUX` | Auxiliary Verb | Copulas and tense/aspect auxiliaries (*εἰμί*, *sum*, *esse*) |
| `ADJ` | Adjective | Modifiers specifying nominal attributes (*καλός*, *magnus*) |
| `ADV` | Adverb | Modifiers of verbs, adjectives, or clauses (*εὖ*, *bene*, *ταχέως*) |
| `PRON` | Pronoun | Personal, demonstrative, relative pronouns (*ἐγώ*, *hic*, *qui*, *ὅς*) |
| `DET` | Determiner | Articles and pronominal determiners (*ὁ*, *ἡ*, *τό*, *ille*) |
| `ADP` | Adposition | Prepositions and postpositions (*ἐν*, *in*, *πρός*, *ad*) |
| `CCONJ` | Coordinating Conjunction | Coordinators (*καί*, *et*, *sed*, *ἀλλά*, *que*) |
| `SCONJ` | Subordinating Conjunction | Subordinators (*ὅτι*, *ut*, *si*, *ἐπεί*, *quoniam*) |
| `NUM` | Numeral | Cardinal numbers (*εἷς*, *tres*, *πέντε*, *centum*) |
| `PART` | Particle | Grammatical and modal particles (*γάρ*, *μέν*, *δέ*, *ἄν*, *non*) |
| `INTJ` | Interjection | Exclamations and emotional cries (*ὦ*, *heu*, *vae*) |
| `PUNCT` | Punctuation | Punctuation marks (periods, commas, semicolons, middot) |
| `SYM` | Symbol | Mathematical and scribal symbols, currency marks, cruces |
| `X` | Other / Unanalyzable | Foreign words, corruptions, unparseable fragments |

When annotating by hand, assigning the correct UPOS tag requires distinguishing functional categories that historical grammars often conflated. For instance, the Greek definite article *ὁ, ἡ, τό* is tagged as `DET` (determiner), while demonstrative pronouns like *οὗτος* used independently are tagged as `PRON`.

**The takeaway for this page:** The Universal Dependencies UPOS tagset provides 17 standardized, cross-linguistic categories that establish the foundational part-of-speech classification for every token.

---

## **10 Content**

**Language-Specific Part-of-Speech Tags (XPOS) and Positional Tagsets**

While the 17 UPOS tags provide cross-linguistic consistency, they are too coarse to capture the detailed inflectional distinctions necessary for historical philology. Universal Dependencies therefore accommodates Language-Specific Part-of-Speech (XPOS) tags. In classical computational linguistics, the dominant XPOS standard is the 9-position positional tagset developed for the Perseus Digital Library and the Ancient Greek and Latin Dependency Treebank (AGLDT) (Celano, 2014; Crane, 1991).

In the Perseus 9-position XPOS scheme, every token is assigned a fixed-length string of exactly nine characters, where each position corresponds to a specific morphological dimension. If a dimension is not applicable to that word class, it is filled with a hyphen (`-`):

- Position 1: Part of Speech (`n`=noun, `v`=verb, `a`=adjective, `d`=adverb, `l`=article, `p`=pronoun, `c`=conjunction, `r`=preposition, `m`=numeral, `e`=interjection, `u`=punctuation, `g`=particle)
- Position 2: Person (`1`=1st, `2`=2nd, `3`=3rd)
- Position 3: Number (`s`=singular, `p`=plural, `d`=dual)
- Position 4: Tense (`p`=present, `i`=imperfect, `r`=perfect, `l`=pluperfect, `t`=future perfect, `f`=future, `a`=aorist)
- Position 5: Mood (`i`=indicative, `s`=subjunctive, `o`=optative, `n`=infinitive, `m`=imperative, `p`=participle)
- Position 6: Voice (`a`=active, `m`=middle, `p`=passive, `e`=middle/passive)
- Position 7: Gender (`m`=masculine, `f`=feminine, `n`=neuter)
- Position 8: Case (`n`=nominative, `g`=genitive, `d`=dative, `a`=accusative, `v`=vocative, `b`=ablative)
- Position 9: Degree (`c`=comparative, `s`=superlative)

For example, consider the Latin verb form *rexit* ("he ruled"). Its Perseus XPOS tag is `v3sria---`:

- Position 1: `v` (verb)
- Position 2: `3` (3rd person)
- Position 3: `s` (singular)
- Position 4: `r` (perfect tense)
- Position 5: `i` (indicative mood)
- Position 6: `a` (active voice)
- Positions 7–9: `---` (gender, case, and degree not applicable to finite verbs)

Now consider the Greek noun form *πόλεσιν* ("to the cities"): its XPOS tag is `n-p---fd-` (`n` = noun, `p` = plural, `f` = feminine, `d` = dative). Positional XPOS strings provide an exceptionally compact, deterministic representation of complete inflectional bundles.

**The takeaway for this page:** Positional XPOS tagsets use a 9-character code to record the complete inflectional profile of a historical word form in a standardized, machine-readable syntax.

---

## **11 Content**

**Morphosyntactic Features (FEATS) in Universal Dependencies**

In addition to UPOS and XPOS, the Universal Dependencies standard defines the `FEATS` column, which stores morphological properties as explicit, human-readable key-value pairs separated by vertical bars (de Marneffe et al., 2021). This format eliminates the opacity of positional character codes and aligns with modern semantic web and Linked Open Data standards.

Standard UD morphological features for Greek and Latin include:

- `Person`: `1`, `2`, `3`
- `Number`: `Sing`, `Plur`, `Dual`
- `Tense`: `Pres`, `Past` (or `Imp`, `Aor`, `Pqp`, `Fut`)
- `Aspect`: `Perf`, `Imp`, `Prosp`
- `Mood`: `Ind`, `Sub`, `Opt`, `Imp`, `Prp`
- `Voice`: `Act`, `Mid`, `Pass`
- `VerbForm`: `Fin`, `Inf`, `Part`, `Gerd`, `Gdv`
- `Gender`: `Masc`, `Fem`, `Neut`
- `Case`: `Nom`, `Gen`, `Dat`, `Acc`, `Voc`, `Abl`
- `Degree`: `Cmp`, `Sup`, `Pos`

For the Latin verb *haesit* ("he clung"), the FEATS string is structured as:  
`Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin|Voice=Act`.  
For the noun *faucibus* ("in the jaws"), the FEATS string is:  
`Case=Abl|Gender=Fem|Number=Plur`.

When constructing manual annotations, features must be ordered alphabetically by feature name, without spaces around the equal signs or pipes. Empty or inapplicable features are omitted entirely rather than marked with hyphens. The combination of UPOS, XPOS, and FEATS ensures that every token carries both a broad syntactic category and a fully detailed inflectional description.

**The takeaway for this page:** The Universal Dependencies FEATS standard encodes morphological properties as sorted, pipe-delimited key-value pairs for transparent data exchange.

---

## **12 Content**

**Principles of Dependency Grammar for Historical Languages**

Beyond parsing individual words, syntactic annotation models the relationships that bind words into sentences. In modern computational linguistics, two competing paradigms exist: constituency grammar (phrase-structure grammar) and dependency grammar.

Constituency grammar, popularized by Chomskyan linguistics, organizes sentences into nested hierarchical phrases (Noun Phrases, Verb Phrases, Prepositional Phrases). While well-suited for configurational languages like English where word order is rigid and grammatical relations depend on phrase positioning, constituency grammar breaks down when applied to ancient Greek and Latin. Classical languages possess free or pragmatically determined word order, characterized by discontinuous constituents, tmesis, and hyperbaton (the separation of syntactically linked words across long clauses).

Dependency grammar, originating in the work of Lucien Tesnière and formalized in Universal Dependencies, models syntactic structure as direct binary relations between words. Every dependency link connects a **head** (the governing word) to a **dependent** (the subordinate word), labeled with a specific grammatical relation (**DEPREL**).

In a dependency tree for the Latin sentence *regem cives amant* ("The citizens love the king"):

- The finite verb *amant* serves as the root head of the clause (`root`).
- The noun *cives* depends directly on *amant* with the relation `nsubj` (nominal subject).
- The noun *regem* depends directly on *amant* with the relation `obj` (direct object).

Notice that this structure remains identical regardless of whether the sentence is written *regem cives amant*, *cives amant regem*, or *amant cives regem*. Dependency trees are invariant under word-order permutation, making them the optimal framework for ancient corpora.

**The takeaway for this page:** Dependency grammar models direct head-dependent relations between words, providing a robust syntax model for the flexible word order and hyperbaton of ancient languages.

---

## **13 Content**

**Syntactic Dependency Relations (DEPREL) in Universal Dependencies**

Universal Dependencies defines a standardized set of Universal Dependency Relations (`DEPREL`) that describe the functional link between a head and its dependent (de Marneffe et al., 2021). When constructing a dependency tree by hand, the editor must assign one of these relations to every non-root token in the sentence:

| Relation Tag | Syntactic Role | Description and Grammatical Context |
|---|---|---|
| `root` | Sentence Root | The root node of the sentence (usually the main finite verb) |
| `nsubj` | Nominal Subject | The nominal subject of an active or stative predicate |
| `obj` | Direct Object | The core nominal direct object (accusative complement) |
| `iobj` | Indirect Object | The core nominal indirect object (dative complement) |
| `csubj` | Clausal Subject | A subordinate clause functioning as the subject |
| `ccomp` | Clausal Complement | A dependent clause functioning as a core clausal argument |
| `xcomp` | Open Clausal Complement | A non-finite complement lacking an independent subject (e.g. infinitive) |
| `obl` | Oblique Nominal | A non-core nominal dependent, adverbial noun, or prepositional phrase |
| `advmod` | Adverbial Modifier | An adverb modifying a verb, adjective, or clause |
| `amod` | Adjectival Modifier | An adjective modifying a noun |
| `nmod` | Nominal Modifier | A noun modifying another noun (e.g. adnominal genitive) |
| `det` | Determiner | A determiner or article modifying a noun |
| `case` | Case Marker | A preposition or case particle governing a nominal |
| `conj` | Conjunct | The second and subsequent conjuncts in a coordinate structure |
| `cc` | Coordinating Conjunction | The coordinating conjunction linking conjuncts |
| `mark` | Marker | A subordinating conjunction introducing a clause |
| `punct` | Punctuation | Punctuation attached to its governing clause head |

In manual treebanking, identifying the correct head is essential. In UD, content words are privileged as heads: in a prepositional phrase like *ἐν τῇ πόλει* ("in the city"), the noun *πόλει* is the head of the phrase, while the preposition *ἐν* attaches to *πόλει* with the relation `case`, and the article *τῇ* attaches to *πόλει* with `det`.

**The takeaway for this page:** Universal Dependencies DEPREL tags specify the exact grammatical relation connecting each dependent word to its governing semantic head.

---

## **14 Content**

**The Ancient Greek and Latin Dependency Treebank (AGLDT) Standard**

The earliest and most extensive gold-standard dependency corpus for classical antiquity is the Ancient Greek and Latin Dependency Treebank (AGLDT), developed under the auspices of the Perseus Digital Library and the Tufts Center for Hellenic Studies (Celano, 2014; Crane, 1991). The AGLDT established the foundational protocols for annotating Greek authors (Homer, Hesiod, Aeschylus, Sophocles, Euripides, Thucydides, Lysias, Plato) and Latin authors (Cicero, Caesar, Virgil, Horace, Ovid, Jerome).

The AGLDT was built using the Prague Dependency Treebank annotation schema, which was subsequently mapped onto Universal Dependencies. In the AGLDT Prague-style system, syntactic tags carry specific prefixes and function codes (e.g., `PRED` for predicate, `SBJ` for subject, `OBJ` for object, `ADV` for adverbial, `ATR` for attribute, `PNOM` for predicate nominal, `COORD` for coordination head, and `AuxP` for preposition).

Consider the phrase *in monte alto* ("on the high mountain"):

- In the legacy AGLDT model: The preposition *in* acts as the head (`AuxP`), governing the noun *monte* (`ADV`), which in turn governs the adjective *alto* (`ATR`).
- In the Universal Dependencies model: The noun *monte* acts as the content head (`obl`), governing both the preposition *in* (`case`) and the adjective *alto* (`amod`).

The key structural difference between legacy AGLDT and modern UD lies in the treatment of function words. In the legacy AGLDT, prepositions and auxiliary verbs were treated as heads governing content words. In modern UD, content words (nouns, lexical verbs) are consistently treated as heads, while function words (prepositions, auxiliaries, conjunctions) attach as dependents. When consulting classical treebank data, the editor must recognize which standard governs the file.

**The takeaway for this page:** The AGLDT standard provided the historical foundation for classical treebanking, which has now been harmonized into the content-head architecture of Universal Dependencies.

---

## **15 Content**

**The PROIEL Treebank Architecture and Biblical Corpora**

The Pragmatic Resources in Old Indo-European Languages (PROIEL) project, initiated at the University of Oslo, expanded treebanking methodology into early Indo-European translations, focusing on the Greek New Testament, the Latin Vulgate, the Gothic Bible, and Classical Armenian (Haug & Jøhndal, 2008). PROIEL introduced sophisticated theoretical advances to historical treebanking, particularly in the domain of information structure, discourse referentiality, and secondary predication.

PROIEL documents not only syntactic dependency trees but also anaphoric links, information packaging (given vs. new information, topic and focus), and non-projective syntactic structures. In PROIEL, secondary predicates (such as predicative participles in Greek genitive absolutes or Latin ablative absolutes) are explicitly represented with dual dependency indices, capturing both their matrix syntactic attachment and their semantic argument government (Haug & Jøhndal, 2008).

The PROIEL Greek and Latin treebanks have been fully converted into Universal Dependencies format (`grc_proiel` and `la_proiel`), providing over 200,000 syntactically annotated tokens. Because the PROIEL corpus was annotated and verified entirely by expert philologists, it serves as the definitive reference dataset used to train neural parsing models like Stanza and UDPipe. When evaluating automated tools on biblical or Koine Greek, your manual benchmark will be compared directly against PROIEL standards.

**The takeaway for this page:** The PROIEL treebank provides an expertly annotated, gold-standard reference for biblical and historical corpora, pioneering the integration of syntax, pragmatics, and secondary predication.

---

## **16 Content**

**Manual Annotation Protocols and Scholarly Lexica**

Conducting a rigorous manual parse requires establishing an unambiguous annotation protocol before processing a single line of text. The editor must select and document the scholarly authorities used for lexical identification, morphological disambiguation, and syntax modeling.

For Ancient Greek, the standard lexical authority is the Liddell-Scott-Jones *Greek-English Lexicon* (LSJ), supplemented by the *Diccionario Griego-Español* (DGE) for specialized vocabulary and Lampe’s *Patristic Greek Lexicon* for late antique and early Christian texts. For Latin, the primary authorities are Lewis and Short’s *Latin Dictionary*, the *Thesaurus Linguae Latinae* (ThLL), and the *Oxford Latin Dictionary* (OLD).

During manual parsing, the editor must follow a four-step verification protocol for every token:

1. **Surface Identification:** Record the exact surface string, noting diacritics, breathing marks, and capitalization.
2. **Lexical Lookup:** Query the reference lexicon to locate the canonical headword, verifying that the proposed lemma matches the dialect and genre of the author.
3. **Morphological Decomposition:** Deconstruct the word into its principal part, stem, tense/aspect marker, and inflectional termination, assigning the complete bundle of UPOS, XPOS, and FEATS features.
4. **Syntactic Attachment:** Determine the governing head token within the sentence and assign the appropriate DEPREL relation based on Universal Dependencies guidelines.

Documenting edge cases and controversial interpretations in an editorial log ensures that manual ground truth remains internally consistent and reproducible.

**The takeaway for this page:** A standardized four-step manual protocol backed by authoritative lexica guarantees that gold-standard annotations remain methodologically sound and consistent.

---

## **17 Content**

**TEI P5 Chapter 18: Simple Analytic Mechanisms for Linguistic Annotation**

Once a text has been parsed and lemmatized by hand, the resulting linguistic analysis must be encoded in a durable, interoperable data format. The international standard for encoding digital scholarly editions is the Text Encoding Initiative (TEI) P5 Guidelines (TEI Consortium, 2026). Chapter 18, titled "Simple Analytic Mechanisms," provides the formal XML schema for representing linguistic segmentation and morphosyntactic analysis.

Historically, complex linguistic markup in TEI relied on ISO-standard Feature Structures (`<fs>`, `<f>`, `<vAlt>`) encoded in separate standoff documents. While feature structures offer unlimited expressive power for representing overlapping syntactic trees and deep phonetic hierarchies, they introduce massive XML verbosity and syntactic complexity that makes standard text processing cumbersome (TEI Consortium, 2026).

Chapter 18 defines an inline, lightweight mechanism that attaches analytical metadata directly to the text stream. By wrapping linguistic tokens in dedicated segmentation elements—primarily `<w>` for words, `<pc>` for punctuation, and `<s>` for sentences—editors can embed lemmas, parts of speech, and morphological descriptions directly within the text of their digital edition without separating analysis from the diplomatic reading.

**The takeaway for this page:** TEI P5 Chapter 18 defines lightweight inline XML mechanisms that embed morphological analysis directly into the text stream of a digital edition.

---

## **18 Content**

**The `att.linguistic` Attribute Class in TEI XML**

The core of TEI inline linguistic annotation is the `att.linguistic` attribute class (TEI Consortium, 2026). When the Simple Analytic Mechanisms module is enabled in a TEI schema, the `att.linguistic` class equips the `<w>` (word) and `<pc>` (punctuation) elements with a standardized suite of analytical attributes:

- `@lemma`: Contains the canonical dictionary headword associated with the surface token.
- `@lemmaRef`: A URI linking the lemma directly to an external lexicographical authority, such as an entry in the Perseus Hopper, Logeion, or an online LSJ/Lewis & Short database.
- `@pos`: Records the primary grammatical category or Part of Speech (typically populated with the Universal Dependencies UPOS tag).
- `@msd`: Stores the Morphosyntactic Description, populated either with a positional XPOS string (e.g., `v3siia---`) or a structured Universal Dependencies FEATS string (e.g., `Case=Nom|Gender=Masc|Number=Sing`).
- `@join`: Specifies whether a token is orthographically joined to neighboring tokens (useful for enclitics, proclitics, and hyphenated compounds).

```xml
<!-- Example of lightweight TEI inline linguistic annotation -->
<w xml:id="w1" 
   lemma="λόγος" 
   lemmaRef="https://logeion.uchicago.edu/λόγος"
   pos="NOUN" 
   msd="Case=Nom|Gender=Masc|Number=Sing">λόγος</w>
```

By encoding linguistic metadata inside `att.linguistic` attributes, the textual scholar maintains complete separation between the surface reading (the element text content) and the linguistic analysis (the XML attributes), allowing automated scripts to query grammatical features while rendering tools display clean text to human readers.

**The takeaway for this page:** The TEI `att.linguistic` attribute class provides standardized `@lemma`, `@pos`, and `@msd` attributes to store morphological analyses directly on `<w>` elements.

---

## **19 Content**

**Segmenting Sentences, Words, and Punctuation in TEI XML**

Encoding an entire text using TEI Chapter 18 requires full structural tokenization. The document hierarchy begins with the sentence or clause element `<s>`, inside which every word is enclosed in `<w>` and every punctuation character is enclosed in `<pc>` (TEI Consortium, 2026).

The `<pc>` element handles punctuation tokens and includes specialized attributes from the `att.lexicographic` class:

- `@force`: Indicates the strength of the syntactic boundary (`strong` for periods and question marks; `weak` for commas and colons; `inter` for intermediate breaks).
- `@unit`: Identifies the type of punctuation mark (`sentence`, `clause`, `word`, `quotation`).

Consider the encoding of a complete Latin sentence (*Veritas vincit.*):

```xml
<s xml:id="s1" n="1">
  <w xml:id="s1_w1" 
     lemma="veritas" 
     pos="NOUN" 
     msd="Case=Nom|Gender=Fem|Number=Sing">Veritas</w>
  <w xml:id="s1_w2" 
     lemma="vinco" 
     pos="VERB" 
     msd="Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act">vincit</w>
  <pc xml:id="s1_pc1" force="strong" unit="sentence">.</pc>
</s>
```

Every word and punctuation mark receives a globally unique `@xml:id`. This identifier serves as the indispensable anchor for all subsequent computational layers, including syntactic dependency linking, translation alignment (Topic 11), and scholarly commentary (Topic 12).

**The takeaway for this page:** Full TEI linguistic encoding wraps sentences in `<s>`, words in `<w>`, and punctuation in `<pc>`, assigning unique `@xml:id` anchors to every token.

---

## **20 Content**

**Step-by-Step Manual Parsing Walkthrough: Classical Greek Prose**

To master the manual annotation workflow, let us examine a complete step-by-step parse of a classical Greek prose sentence from Plato (*Apology* 17a):  
*Ὅτι μὲν ὑμεῖς, ὦ ἄνδρες Ἀθηναῖοι, πεπόνθατε ὑπὸ τῶν ἐμῶν λόγων, οὐκ οἶδα.*  
("What effect my words have had upon you, men of Athens, I do not know.")

Let us trace the manual analysis of each token:

1. `Ὅτι`: Lemma *ὅτι*, UPOS `SCONJ`, XPOS `c--------`, FEATS `_`, Head: `πεπόνθατε`, DEPREL `mark`. (Subordinating conjunction introducing the clausal complement).
2. `μὲν`: Lemma *μέν*, UPOS `PART`, XPOS `g--------`, FEATS `_`, Head: `πεπόνθατε`, DEPREL `advmod`. (Discourse particle marking the concessive protasis).
3. `ὑμεῖς`: Lemma *σύ*, UPOS `PRON`, XPOS `p-p---mn-`, FEATS `Case=Nom|Gender=Masc|Number=Plur|Person=2|PronType=Prs`, Head: `πεπόνθατε`, DEPREL `nsubj`. (Second-person plural subject pronoun).
4. `ὦ`: Lemma *ὦ*, UPOS `INTJ`, XPOS `e--------`, FEATS `_`, Head: `ἄνδρες`, DEPREL `discourse`. (Vocative interjection).
5. `ἄνδρες`: Lemma *ἀνήρ*, UPOS `NOUN`, XPOS `n-p---mv-`, FEATS `Case=Voc|Gender=Masc|Number=Plur`, Head: `πεπόνθατε`, DEPREL `vocative`. (Vocative noun of address).
6. `Ἀθηναῖοι`: Lemma *Ἀθηναῖος*, UPOS `ADJ`, XPOS `a-p---mv-`, FEATS `Case=Voc|Gender=Masc|Number=Plur`, Head: `ἄνδρες`, DEPREL `amod`. (Attributive proper adjective modifying *ἄνδρες*).
7. `πεπόνθατε`: Lemma *πάσχω*, UPOS `VERB`, XPOS `v2pria---`, FEATS `Aspect=Perf|Mood=Ind|Number=Plur|Person=2|Tense=Past|VerbForm=Fin|Voice=Act`, Head: `οἶδα`, DEPREL `ccomp`. (Second-person plural perfect active indicative verb of *πάσχω*; head of the complement clause).
8. `ὑπὸ`: Lemma *ὑπό*, UPOS `ADP`, XPOS `r--------`, FEATS `_`, Head: `λόγων`, DEPREL `case`. (Preposition governing genitive of agent).
9. `τῶν`: Lemma *ὁ*, UPOS `DET`, XPOS `l-p---mg-`, FEATS `Case=Gen|Definite=Def|Gender=Masc|Number=Plur|PronType=Art`, Head: `λόγων`, DEPREL `det`. (Definite article in agreement with *λόγων*).
10. `ἐμῶν`: Lemma *ἐμός*, UPOS `ADJ`, XPOS `a-p---mg-`, FEATS `Case=Gen|Gender=Masc|Number=Plur|Poss=Yes`, Head: `λόγων`, DEPREL `amod`. (Possessive adjective in agreement with *λόγων*).
11. `λόγων`: Lemma *λόγος*, UPOS `NOUN`, XPOS `n-p---mg-`, FEATS `Case=Gen|Gender=Masc|Number=Plur`, Head: `πεπόνθατε`, DEPREL `obl`. (Genitive plural noun of agent dependent on *πεπόνθατε*).
12. `οὐκ`: Lemma *οὐ*, UPOS `PART`, XPOS `d--------`, FEATS `Polarity=Neg`, Head: `οἶδα`, DEPREL `advmod`. (Negative adverbial particle).
13. `οἶδα`: Lemma *οἶδα*, UPOS `VERB`, XPOS `v1sria---`, FEATS `Aspect=Perf|Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin|Voice=Act`, Head: `0` (Root), DEPREL `root`. (First-person singular perfect active indicative verb with present meaning; matrix predicate of the sentence).

This rigorous decomposition leaves no word unaccounted for, providing a complete structural blueprint of the Greek sentence.

**The takeaway for this page:** Manual parsing systematically resolves every token's lemma, morphosyntactic feature bundle, and syntactic dependency attachment within the sentence hierarchy.

---

## **21 Content**

**Step-by-Step Manual Parsing Walkthrough: Poetic Hyperbaton and Dialect**

Manual parsing becomes even more critical when confronting ancient poetry, where meter dictates word placement, creating hyperbaton, dialectal archaisms, and uncontracted forms. Consider the opening line of Homer's *Iliad* (1.1):  
*Μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος*  
("Sing, goddess, the wrath of Achilles, Peleus' son.")

In this epic line, the direct object *Μῆνιν* stands in the emphatic initial position, separated from its governing verb *ἄειδε* and genitive modifiers by the vocative *θεὰ*:

- Predicate Root: *ἄειδε* (verb)
- Direct Object: *Μῆνιν* (noun, dependent on *ἄειδε*)
- Direct Address: *θεὰ* (noun, dependent on *ἄειδε*)
- Adnominal Modifier: *Ἀχιλῆος* (proper noun, dependent on *Μῆνιν*)
- Patronymic Modifier: *Πηληϊάδεω* (proper noun, dependent on *Ἀχιλῆος*)

Philological analysis reveals several epic dialect features that automated taggers frequently mishandle:

- *Μῆνιν*: Lemma *μῆνις*, UPOS `NOUN`, XPOS `n-s---fa-`, FEATS `Case=Acc|Gender=Fem|Number=Sing`. Direct object of *ἄειδε*.
- *ἄειδε*: Lemma *ἀείδω* (Homeric uncontracted form of Attic *ᾄδω*), UPOS `VERB`, XPOS `v2spma---`, FEATS `Aspect=Imp|Mood=Imp|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin|Voice=Act`. Root predicate.
- *θεὰ*: Lemma *θεά*, UPOS `NOUN`, XPOS `n-s---fv-`, FEATS `Case=Voc|Gender=Fem|Number=Sing`. Direct address.
- *Πηληϊάδεω*: Lemma *Πηληϊάδης*, UPOS `PROPN`, XPOS `n-s---mg-`, FEATS `Case=Gen|Gender=Masc|Number=Sing`. Epic Ionic genitive singular ending in *-εω* with synizesis, modifying *Ἀχιλῆος*.
- *Ἀχιλῆος*: Lemma *Ἀχιλλεύς*, UPOS `PROPN`, XPOS `n-s---mg-`, FEATS `Case=Gen|Gender=Masc|Number=Sing`. Epic genitive singular with single lambda and uncontracted *-ηος*, modifying *Μῆνιν*.

If an editor relies on a standard Classical Attic dictionary lookup, *Πηληϊάδεω* and *Ἀχιλῆος* fail to match standard paradigms. The human philologist recognizes the epic dialectal markers and supplies the proper lemma and case assignment.

**The takeaway for this page:** Poetic hyperbaton and dialectal morphology require human philological expertise to resolve non-projective word order and non-standard inflectional endings.

---

## **22 Content**

**Encoding Standoff Syntactic Dependencies in TEI XML**

While Chapter 18’s `att.linguistic` attributes provide inline storage for lemmas and morphological features, representing full syntactic dependency graphs within TEI XML requires linking tokens across the document tree. Because XML is strictly hierarchical (a single tree of nested elements), it cannot natively represent intersecting or cross-branching dependency relations without auxiliary linking structures (TEI Consortium, 2026).

TEI P5 provides the `<linkGrp>` (link group) and `<link>` elements within the Simple Analytic Mechanisms module to encode standoff syntax graphs:

```xml
<s xml:id="s1">
  <w xml:id="s1_w1" lemma="μῆνις" pos="NOUN" msd="Case=Acc|Gender=Fem|Number=Sing">Μῆνιν</w>
  <w xml:id="s1_w2" lemma="ἀείδω" pos="VERB" msd="Mood=Imp|Number=Sing|Person=2">ἄειδε</w>
  <w xml:id="s1_w3" lemma="θεά" pos="NOUN" msd="Case=Voc|Gender=Fem|Number=Sing">θεά</w>
</s>

<linkGrp type="dependency-syntax" corresp="#s1">
  <link type="root" targets="#s1 #s1_w2"/>
  <link type="obj" targets="#s1_w2 #s1_w1"/>
  <link type="vocative" targets="#s1_w2 #s1_w3"/>
</linkGrp>
```

In this standoff architecture, the `<linkGrp>` element points to the governing sentence (`@corresp="#s1"`). Each `<link>` element specifies the syntactic relation (`@type="obj"`) and records the source and target tokens in the `@targets` attribute (`targets="#s1_w2 #s1_w1"`, indicating that `#s1_w2` is the head and `#s1_w1` is the dependent). Standoff linking cleanly decouples syntax trees from text serialization, allowing an edition to store multiple competing syntactic analyses of the same line.

**The takeaway for this page:** TEI `<linkGrp>` and `<link>` elements represent syntactic dependency graphs by linking head and dependent token IDs without disrupting text hierarchy.

---

## **23 Content**

**The CoNLL-U Format: The Global Exchange Standard for Syntax Trees**

While TEI XML is the premier format for archival digital editions, the computational linguistics community exchanges dependency treebanks using the plain-text **CoNLL-U** format. A CoNLL-U file represents each sentence as a series of tab-delimited lines, preceded by comment lines (`# sent_id`, `# text`), followed by a blank line marking the sentence boundary.

Every token in a CoNLL-U file occupies exactly one line containing ten mandatory fields:

| Field Position | Field Identifier | Description and Historical Annotation Example |
|---|---|---|
| Position 1 | `ID` | Word index in sentence, integer starting at 1 (`1`, `2`, `3`) |
| Position 2 | `FORM` | Word form or punctuation symbol as it appears in text (`Μῆνιν`) |
| Position 3 | `LEMMA` | Lemma or stem of the word form (`μῆνις`) |
| Position 4 | `UPOS` | Universal part-of-speech tag (`NOUN`) |
| Position 5 | `XPOS` | Language-specific part-of-speech tag (`n-s---fa-`) |
| Position 6 | `FEATS` | List of morphological features (`Case=Acc, Gender=Fem, Number=Sing`) |
| Position 7 | `HEAD` | Head of the current word: ID of parent word or 0 for root (`2`) |
| Position 8 | `DEPREL` | Universal dependency relation to the HEAD (`obj`) |
| Position 9 | `DEPS` | Enhanced dependency graph (secondary links, or `_`) |
| Position 10 | `MISC` | Miscellaneous annotations, e.g. `SpaceAfter=No` or XML IDs |

```
# sent_id = iliad_1.1
# text = Μῆνιν ἄειδε θεά
1	Μῆνιν	μῆνις	NOUN	n-s---fa-	Case=Acc|Gender=Fem|Number=Sing	2	obj	_	_
2	ἄειδε	ἀείδω	VERB	v2spma---	Mood=Imp|Number=Sing|Person=2	0	root	_	_
3	θεά	θεά	NOUN	n-s---fv-	Case=Voc|Gender=Fem|Number=Sing	2	vocative	_	SpaceAfter=No
4	.	.	PUNCT	u--------	_	2	punct	_	_
```

Because all modern NLP parsers (Stanza, UDPipe, Trankit, spaCy) ingest and output CoNLL-U, your manual ground truth will be authored in or converted to CoNLL-U to enable automated scoring against machine taggers.

**The takeaway for this page:** CoNLL-U is the 10-column tab-delimited standard used to exchange and evaluate morphological and syntactic treebanks across all modern NLP software.

---

## **24 Content**

**Inter-Annotator Agreement in Morphosyntactic Annotation**

When building a gold-standard reference dataset, a single scholar’s intuition is insufficient to guarantee objectivity. Philologists frequently disagree on ambiguous syntactic attachments, the boundary between adjectival and substantival usage, or the categorization of polysemous particles. To establish an authoritative benchmark, multiple annotators must parse the same text independently, after which their agreement is measured mathematically.

Inter-annotator agreement (IAA) is evaluated using statistical metrics that correct for chance agreement:

- **Cohen's Kappa ($\kappa$):** Measures agreement between two annotators on categorical classifications (such as UPOS or case assignment).
- **Fleiss' Kappa:** Extends Cohen's Kappa to three or more annotators.
- **Krippendorff's Alpha ($\alpha$):** A robust metric that handles missing data and multiple annotators across categorical, ordinal, or interval data.

$$\kappa = \frac{P_o - P_e}{1 - P_e}$$

In this formula, $P_o$ is the observed proportional agreement among annotators, and $P_e$ is the hypothetical probability of chance agreement. In morphological tagging of Greek and Latin, expert human annotators typically achieve $\kappa \ge 0.95$ on coarse UPOS tagging, $\kappa \approx 0.90$ on full morphosyntactic feature bundles, and $\kappa \approx 0.85$ on syntactic dependency heads. Disagreements are brought to an adjudication session where scholars debate the philological evidence and establish an agreed consensus gold standard.

**The takeaway for this page:** Inter-annotator agreement metrics quantify consensus among human annotators, establishing a statistically validated gold standard for machine evaluation.

---

## **25 Content**

**Edge Cases in Manual Annotation: Clitics, Crasis, and Tmesis**

During manual parsing, several historical linguistic phenomena test the limits of rigid tokenization and dependency modeling:

1. **Clitics and Accent Shifts:** In Ancient Greek, enclitics (*τε*, *γε*, *τις*, *ἐστι*) lean phonologically on the preceding word, frequently causing the host word to receive an additional acute accent on its final syllable (e.g., *ἄνθρωπός τις*). The editor must ensure that the accent on *ἄνθρωπός* is normalized to *ἄνθρωπος* for lemma lookup, while parsing *τις* as an independent indefinite pronoun.
2. **Crasis:** When two words merge across a boundary (*τοὔνομα* from *τὸ ὄνομα*; *κἀμοί* from *καὶ ἐμοί*), the editor must split the token into two distinct CoNLL-U entries (multi-word token lines `1-2`, followed by sub-tokens `1` and `2`), assigning the lemma *ὁ* to the article component and *ὄνομα* to the noun.
3. **Tmesis:** In early Greek epic and archaic Latin, prefix preverbs are separated from their verbs by intervening words (e.g., *κατὰ δάκρυ χέουσα* for *καταχέουσα δάκρυ*). In Universal Dependencies, the detached preposition *κατά* is tagged as `ADP` or `ADV` and linked to the verb *χέουσα* with the relation `compound:prt` (compound particle), preserving the semantic unity of the verb without violating word boundaries.

Properly documenting these edge cases in your manual parsing notes prevents systematic scoring penalties when testing automated taggers on Wednesday and Friday.

**The takeaway for this page:** Clitics, crasis, and tmesis require multi-word token segmentation and compound relation tagging to preserve morphological and syntactic integrity.

---

## **26 Content**

**Edge Cases in Manual Annotation: Ellipsis and Null Heads**

Pre-modern authors frequently omit words that can be readily inferred from context, creating syntactic structures with elided verbs, omitted copulas, or null subject heads. Representing these null structures in dependency trees requires clear theoretical guidelines.

In Classical Greek and Latin, the copula (*εἰμί*, *sum*) is routinely omitted in nominal sentences (*Omnia praeclara rara* = "All excellent things [are] rare"). In Universal Dependencies:

- The predicate adjective (*rara*) is promoted to the status of clause **head** (`root`).
- The subject (*Omnia*) attaches to the predicate adjective as `nsubj`.
- The modifying adjective (*praeclara*) attaches to *Omnia* as `amod`.

In cases of **gapping** (where a lexical verb is expressed in the first coordinate clause but elided in subsequent coordinate clauses, e.g., *Caesar vicit Gallos, Pompeius Hispanos*), Universal Dependencies utilizes the `orphan` relation. The subject *Pompeius* attaches to the matrix verb *vicit* as a conjunct clause (`conj`), while the object *Hispanos* attaches to *Pompeius* with the relation `orphan`. Understanding these formal conventions allows human editors to construct valid dependency trees even when key syntactic elements are physically absent from the manuscript.

**The takeaway for this page:** Universal Dependencies handles ellipsis and copula omission by promoting predicate words to clause heads and utilizing the `orphan` relation for gapped arguments.

---

## **27 Content**

**Creating the Ground-Truth Benchmark Dataset**

To prepare for the comparative cycle of Topic 9, you will construct an uncorrupted, representative ground-truth benchmark dataset. The quality of any computational evaluation depends strictly on the representative breadth of its reference test set.

Your benchmark dataset should comprise approximately 200–300 words of continuous text, selected from the corpus you are editing for your term portfolio. The passage must be chosen to include a balanced distribution of linguistic phenomena:

- Standard regular nouns and verbs across major declensions and conjugations.
- At least three closed-class particles, prepositions, or subordinating conjunctions.
- At least one instance of morphological ambiguity (e.g., case syncretism or homophonous verbal forms).
- At least one complex syntactic structure (e.g., hyperbaton, a participial clause, or a coordinated compound sentence).

Once selected, you will parse every token by hand, recording the surface form, canonical lemma, UPOS tag, Perseus 9-position XPOS tag, UD FEATS string, governing HEAD index, and DEPREL relation. This manual parse will be locked as the definitive ground-truth against which automated systems will be evaluated.

**The takeaway for this page:** A representative ground-truth dataset spanning regular paradigms, ambiguous forms, and complex syntax is the necessary benchmark for evaluating automated NLP pipelines.

---

## **28 Content**

**Documenting the Editorial Annotation Schema**

No benchmark dataset is complete without an explicit annotation schema manual. An annotation manual documents the editorial decisions, dictionary editions, and taxonomy interpretations applied during manual parsing, ensuring that another scholar could replicate the dataset with identical results.

Your editorial schema document must record:

1. **Lexical Authority:** The exact dictionary version and URL resolver used for lemma selection (e.g., LSJ 1940 via Perseus/Logeion; Lewis & Short 1879).
2. **Tokenization Rules:** How punctuation, enclitics, elisions, and crasis were segmented into tokens.
3. **Taxonomic Disambiguation:** How ambiguous parts of speech were categorized (e.g., whether participles were tagged as `VERB` with `VerbForm=Part` or as `ADJ`; whether proper names were tagged as `NOUN` or `PROPN`).
4. **Dependency Conventions:** How coordinate conjunctions, vocatives, and prepositional phrases were attached to head nodes.

Version-controlling this schema document alongside your CoNLL-U and TEI XML files in your Git repository guarantees scientific transparency and replicability.

**The takeaway for this page:** A comprehensive annotation manual documents lexical authorities and disambiguation rules, ensuring transparency and reproducibility for the gold-standard dataset.

---

## **29 Content**

**Preparing Ground-Truth Data for Automated Testing**

To enable automated scoring on Wednesday and Friday, your manual parse must be exported into standardized machine-readable files. You will prepare two synchronized representations of your gold standard:

1. **`gold_standard.conllu`:** A strictly formatted 10-column CoNLL-U file containing every token, lemma, UPOS, XPOS, FEATS, HEAD, and DEPREL relation.
2. **`gold_standard_tei.xml`:** A valid TEI P5 Chapter 18 XML document wrapping the passage in `<s>`, `<w>`, and `<pc>` elements with full `att.linguistic` attributes (`@lemma`, `@pos`, `@msd`, `@xml:id`).

You can verify the syntactic validity of your CoNLL-U file using the official Universal Dependencies validation script:

```bash
python3 shared/scripts/validate_conllu.py --lang grc gold_standard.conllu
```

Once validated, these gold files will serve as the exact evaluation keys for calculating precision, recall, macro-F1 scores, and Unlabeled/Labeled Attachment Scores (UAS/LAS) across deterministic and AI-assisted pipelines.

**The takeaway for this page:** Exporting manual annotations to validated CoNLL-U and TEI XML files creates the machine-readable evaluation keys required for automated benchmarking.

---

## **30 Content**

**Synthesis: The Philologist as the Ground Truth**

Today’s manual exercise establishes the foundational methodology of computational philology: computational algorithms do not create linguistic truth; they attempt to approximate the analytical judgments of human philologists. Without an expertly curated, manually verified ground truth, it is impossible to determine whether an automated tagger is operating at 95% accuracy or failing systematically on historical dialect forms.

By parsing, lemmatizing, and treebanking a passage by hand, you have mastered the anatomical structure of ancient inflected languages and learned the international standards (Universal Dependencies, Perseus XPOS, TEI P5 Chapter 18) that govern digital editions.

On Wednesday (Lesson 9.2), you will pass this identical text through deterministic and rule-based NLP engines—including Morpheus, TreeTagger, and the Classical Language Toolkit (CLTK)—to measure how well rule cascades and Markov models reproduce your manual parsing decisions. On Friday (Lesson 9.3), you will evaluate large language models and neural transformers against this same ground truth, investigating precision, recall, and morphological hallucination.

**The takeaway for this page:** Human philological expertise creates the gold-standard reference against which all deterministic, statistical, and neural models must be measured.

---

## References

Celano, G. G. A. (2014). *The Ancient Greek and Latin Dependency Treebank*. Perseus Digital Library.

Crane, G. (1991). Generating and parsing Classical Greek. *Literary and Linguistic Computing*, 6(4), 243–245.

de Marneffe, M.-C., Manning, C. D., Nivre, J., & Zeman, D. (2021). Universal Dependencies. *Computational Linguistics*, 47(2), 255–308.

Haug, D. T. T., & Jøhndal, M. (2008). Creating a parallel treebank of the Old Indo-European Bible translations (PROIEL). In *Proceedings of the Second Workshop on Language Technology for Cultural Heritage Data (LaTeCH 2008)*, 27–34.

TEI Consortium. (2026). *TEI P5: Guidelines for electronic text encoding and interchange*. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/
