# Lesson 9.1 — Manual Entity Identification, Authority Record Research, and Canonical Citation

*RELS 398 / ENGL 398 · Topic 9: Named Entities · Meeting #23 (Tue Nov 3)*

***Step 1 of the three-step cycle: Manual ground truth.** Today you identify named entities by hand in your historical document, establish authority links to Wikidata, VIAF, and GeoNames, and encode a gold-standard TEI XML benchmark.*

---

## **01 Content**

**Names Beyond Strings: Why Editions Need Entity Markup**

Over the past eight weeks, you built a real digital edition from the ground up. You catalogued your witness in a `teiHeader`. You linked high-resolution images with `<facsimile>`. You transcribed every line as written. In Module 6, you normalized historical spelling with `<choice>`. In Module 7, you created stylesheets for online reading. Last week, in Module 8, you added parts of speech and dictionary lemmas to your words.

Now we take the next major step in digital textual editing: named entities. A computer sees text only as a sequence of letters and spaces. A search for the word *Paris* finds every instance of those five letters. But the computer does not know if *Paris* means the capital of France, a small town in Maine, or the mythological Trojan prince.

Named entity markup solves this problem. It identifies real-world people, geographic places, corporate organizations, and dates in your text. It links those mentions to global authority records. Today, you will establish this ground truth by hand for your own project witness.

**Vocabulary.** *Named Entity* — A real-world person, place, group, or date mentioned in a text. *Entity Disambiguation* — Distinguishing between different people or places that share the same name.

**Takeaway:** String searches find matching letters; entity markup reveals the actual people, places, groups, and dates behind those letters.

---

## **02 Content**

**The Four Core Classes: People, Places, Organizations, and Dates**

In digital humanities, entity recognition focuses on four main categories. Every historical document is shaped by these four classes of information.

The first class is **people** (`persName`). This includes authors, monarchs, scribes, soldiers, artists, and correspondents. The second class is **places** (`placeName`). This covers towns, rivers, provinces, roads, and natural features. The third class is **organizations** (`orgName`). This includes governments, parliaments, military regiments, churches, and committees. The fourth class is **dates** (`date`). This covers calendar days, months, years, and historical eras.

Separating these four classes requires human reading. Consider the word *Halifax* in Andromeda's 1752 Treaty. Does it mean the colonial town in Nova Scotia, the city in England, or Lord Halifax? The letters are identical. Only human context tells you that the treaty was signed in the coastal settlement of Halifax.

**Vocabulary.** *Person Entity* — An individual human being named in a text. *Place Entity* — A physical geographic location. *Organization Entity* — A group, council, or formal institution. *Date Entity* — A specific point or span in time.

**Takeaway:** The four core entity types in historical texts are people, places, organizations, and dates.

---

## **03 Content**

**TEI P5 Chapter 13: The Four Core Elements**

The Text Encoding Initiative gives us standard XML tags for names and dates in Chapter 13 of the Guidelines. These tags preserve your transcript while labeling what each name means.

To tag a person, wrap their name in `<persName>`. To tag a place, use `<placeName>`. For an organization, use `<orgName>`. For a date or time expression, use `<date>`.

Look at how these elements appear in practice:

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 0.5rem; text-align: left;">Entity Class</th>
      <th style="padding: 0.5rem; text-align: left;">TEI Tag</th>
      <th style="padding: 0.5rem; text-align: left;">Historical Example</th>
      <th style="padding: 0.5rem; text-align: left;">What It Marks</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Person</td>
      <td style="padding: 0.5rem;"><code>&lt;persName&gt;</code></td>
      <td style="padding: 0.5rem;">Major Jean Baptiste Cope</td>
      <td style="padding: 0.5rem;">A real human individual</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Place</td>
      <td style="padding: 0.5rem;"><code>&lt;placeName&gt;</code></td>
      <td style="padding: 0.5rem;">Chigabenakady</td>
      <td style="padding: 0.5rem;">A geographic site or territory</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Organization</td>
      <td style="padding: 0.5rem;"><code>&lt;orgName&gt;</code></td>
      <td style="padding: 0.5rem;">Assemblée nationale</td>
      <td style="padding: 0.5rem;">A formal group or assembly</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem;">Date</td>
      <td style="padding: 0.5rem;"><code>&lt;date&gt;</code></td>
      <td style="padding: 0.5rem;">22 Novembre 1752</td>
      <td style="padding: 0.5rem;">A calendar point in time</td>
    </tr>
  </tbody>
</table>

These tags leave the ink on the page unchanged. They simply add a digital wrapper that explains what the name is.

**Vocabulary.** *TEI Chapter 13* — The section of the TEI Guidelines that governs names, dates, people, and places. *Element Wrapper* — An XML tag placed around historical words without changing their spelling.

**Takeaway:** TEI P5 provides four primary tags—persName, placeName, orgName, and date—to identify historical entities.

---

## **04 Content**

**Names with Internal Parts: Surnames, Forenames, and Titles**

Historical names often contain multiple parts. Scribes combine official titles, first names, family surnames, and nicknames in a single phrase.

TEI allows you to break down a name into smaller pieces inside the `<persName>` tag. You can tag a first name with `<forename>`. You can tag a family name with `<surname>`. You can mark an official office or military rank with `<roleName>`.

Look at the signature in the 1752 Treaty: *Major Jean Baptiste Cope*. In basic markup, you can tag the whole string as `<persName>`. In detailed markup, you can tag *Major* as `<roleName>`, *Jean Baptiste* as `<forename>`, and *Cope* as `<surname>`. This helps future scholars search for all military officers or sort people by family name without confusing titles with personal names.

**Vocabulary.** *Forename* — A given first or middle name. *Surname* — A family or clan name. *Role Name* — An official title, military rank, or social office.

**Takeaway:** Detailed tags like forename, surname, and roleName let you break historical names into clear grammatical parts.

---

## **05 Content**

**Places with Layers: Towns, Counties, and Countries**

Geographic locations also appear in layers. An address or travel record often moves from a specific building or town to a larger district, province, and nation.

TEI represents these spatial layers using child elements inside `<placeName>`. You can tag a village or city with `<settlement>`. You can tag a county or province with `<region>`. You can tag an entire sovereign realm with `<country>`.

When Maud Lewis writes from *Marshalltown, Digby County, Nova Scotia*, she names three geographic layers. Marshalltown is a `<settlement>`. Digby County is a `<region type="county">`. Nova Scotia is a `<region type="province">`. This keeps your digital map accurate and prevents software from mistaking a tiny village for a whole region.

**Vocabulary.** *Settlement* — A town, village, or city. *Region* — A county, state, province, or district. *Country* — A sovereign nation or land.

**Takeaway:** Nested place tags like settlement and region preserve the spatial layers of historical geography.

---

## **06 Content**

**Time on the Page: The Essential @when Attribute**

Dates in historical documents look very different from modern calendar entries. Scribes write dates in words, Latin phrases, or regnal years. A clerk might write *the twenty-second Day of November in the twenty-sixth Year of the Reign of King George*.

A search engine looking for the year 1752 will miss that phrase unless you help it. TEI solves this with the `@when` attribute on the `<date>` tag.

The text inside the tag keeps the scribe's exact words: `<date when="1752-11-22">the twenty-second Day of November</date>`. The `@when` attribute holds the standardized date in ISO 8601 format (`YYYY-MM-DD`). This lets computers sort, filter, and timeline historical events while keeping the original manuscript ink visible.

**Vocabulary.** *ISO 8601* — The international standard format for dates (YYYY-MM-DD). *The @when Attribute* — The TEI attribute that stores a normalized computer-readable date.

**Takeaway:** The when attribute normalizes historical dates into YYYY-MM-DD format while preserving original manuscript phrasing.

---

## **07 Content**

**When Capital Letters Lie: Scribes and Common Nouns**

In modern English, we capitalize proper names and lowercase common nouns. In eighteenth-century manuscripts, scribes did not follow this rule.

In the 1752 Treaty and the 1791 French decree, scribes capitalized common nouns for emphasis or elegance. Words like *Treaty*, *Governor*, *Assembly*, *Law*, and *Peace* often begin with capital letters. A computer might guess that every capitalized word is a proper name.

A human editor knows better. Capital letters alone do not make a word a named entity. You must ask whether the word refers to an individual person, a real geographic site, or a formal legal body. Human judgment separates scribe habits from true historical entities.

**Vocabulary.** *Proper Noun* — A specific name for a person, place, or thing. *Common Noun* — A general word for a class of items or ideas. *Capitalization Drift* — Scribe habits of capitalizing ordinary words for decoration or emphasis.

**Takeaway:** Historical scribes capitalized common nouns frequently; editors must look beyond capital letters to find real entities.

---

## **08 Content**

**Why Text Strings Fail: Connecting Names to Real Things**

Text strings are slippery. A single historical figure can appear under half a dozen different names in the same archive.

In Revolutionary France, the king might be called *Louis XVI*, *Louis Seize*, *le Roi*, or *Citoyen Capet*. In British records, Governor Hopson might be called *Peregrine Thomas Hopson*, *Governor Hopson*, or *His Excellency*. A computer reading plain text sees four different people.

Authority control solves this problem. It links all those different names to a single, permanent record in an authority database. Instead of treating names as isolated text strings, authority control connects them to real historical entities.

**Vocabulary.** *Authority Control* — Linking different names and spelling variants to a single official record. *Identifier* — A unique code or web address that stands for one specific entity.

**Takeaway:** Authority control connects multiple name variants across documents to a single permanent identity.

---

## **09 Content**

**Three Global Registries: Wikidata, VIAF, and GeoNames**

Digital scholars rely on three main open authority registries to link their documents to the wider world.

First, **Wikidata** is an open knowledge database run by the Wikimedia Foundation. Every person, place, and event gets a unique Q-number. For example, Maud Lewis is `Q2302306`. King Louis XVI is `Q7732`.

Second, **VIAF** (the Virtual International Authority File) combines authority lists from national libraries across the world. It assigns a single number that clusters library records for an author or historical figure.

Third, **GeoNames** is the world's standard geographic database. It provides coordinates, administrative codes, and variant names for millions of places. For example, Halifax, Nova Scotia, is GeoNames `6324729`.

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 0.5rem; text-align: left;">Registry</th>
      <th style="padding: 0.5rem; text-align: left;">What It Covers</th>
      <th style="padding: 0.5rem; text-align: left;">Identifier Format</th>
      <th style="padding: 0.5rem; text-align: left;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Wikidata</td>
      <td style="padding: 0.5rem;">People, things, groups, events</td>
      <td style="padding: 0.5rem;"><code>Q[0-9]+</code></td>
      <td style="padding: 0.5rem;">Q2302306 (Maud Lewis)</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">VIAF</td>
      <td style="padding: 0.5rem;">Library authority files</td>
      <td style="padding: 0.5rem;"><code>viaf:[0-9]+</code></td>
      <td style="padding: 0.5rem;">viaf:84035444 (Louis XVI)</td>
    </tr>
    <tr>
      <td style="padding: 0.5rem;">GeoNames</td>
      <td style="padding: 0.5rem;">Geographic places and features</td>
      <td style="padding: 0.5rem;"><code>geonames:[0-9]+</code></td>
      <td style="padding: 0.5rem;">geonames:6324729 (Halifax)</td>
    </tr>
  </tbody>
</table>

**Vocabulary.** *Wikidata* — A free, multilingual knowledge graph of people, concepts, and places. *VIAF* — A global registry combining national library authority files. *GeoNames* — A global database of geographic names and coordinates.

**Takeaway:** Wikidata, VIAF, and GeoNames are the primary public databases used to identify people, libraries, and places.

---

## **10 Content**

**The TEI @ref Attribute: Building the Linked Data Bridge**

In TEI XML, you link an entity to an authority database using the `@ref` attribute. The `@ref` attribute holds the web address (URI) or identifier of the official record.

Look at how the attribute attaches to a name tag:
```xml
<persName ref="https://www.wikidata.org/wiki/Q2302306">Maud Lewis</persName>
```

The text between the opening and closing tags remains the exact manuscript wording. The `@ref` attribute builds the bridge to the global web of data.

When another scholar searches your edition, their software can follow the `@ref` link to learn Maud Lewis's birth year, artistic style, and museum holdings. You can also write shorter forms like `ref="wikidata:Q2302306"` if you define the prefix in your header.

**Vocabulary.** *The @ref Attribute* — The TEI attribute that points to an external authority record or local identifier. *Linked Data* — A method of publishing structured data so that digital documents can link to one another.

**Takeaway:** The TEI ref attribute embeds authority links into names, connecting local editions to global research networks.

---

## **11 Content**

**Local and Regional Registers: Canadian and Indigenous Databases**

Global databases like Wikidata and VIAF are immense, but they have major blind spots. They focus heavily on famous European rulers, published writers, and large cities. They often overlook regional Canadian artists, local historical figures, and Indigenous communities.

When you edit regional manuscripts, specialized databases provide far better information. For Canadian figures, the **Dictionary of Canadian Biography (DCB)** gives peer-reviewed historical profiles. The **Canadian Heritage Information Network (CHIN)** catalogues Canadian artists and museum collections.

For Indigenous places and treaties, **Native Land Digital** maps ancestral territories and treaties. Relying only on colonial databases can erase Indigenous heritage. Always look for authority records that respect the local history of your document.

**Vocabulary.** *Regional Authority* — A specialized database focused on national or local historical figures. *Dictionary of Canadian Biography* — The premier scholarly biographical dictionary for Canadian history. *Native Land Digital* — An Indigenous-led platform mapping ancestral territories and languages.

**Takeaway:** Specialized regional databases provide essential authority records where global databases fall short.

---

## **12 Content**

**The Verified Absence Rule: When a Person Has No Record**

What happens when you research a person in your document and find no record in Wikidata, VIAF, or any national archive?

Many beginners panic and attach an unrelated person who shares the same name. Other beginners leave the name untagged. Both choices damage scholarship. Forcing a fake match introduces false data into the historical record.

In our course, you follow the **Verified Absence Rule**. If you search the relevant archives and prove that no record exists, that verified absence earns full credit. Document the registries you searched and state clearly that the person is unindexed. Proving that an archive overlooked an ordinary person is an important historical finding.

**Vocabulary.** *Verified Absence* — Documenting that an entity does not exist in standard authority databases after a thorough search. *False Match* — Forcing a name to link to an unrelated person who shares a similar spelling.

**Takeaway:** Proving and documenting that a person lacks an authority record earns full credit; never force-fit an incorrect link.

---

## **13 Content**

**Building Your Own Directory: <particDesc> in the Header**

When people in your document lack public records in Wikidata, where do you store their biographical information?

TEI solves this by letting you build your own biographical directory inside the `teiHeader`. The element is called `<particDesc>` (participation description). It lives inside the `<profileDesc>` section of the header.

Inside `<particDesc>`, you add a `<person>` element for each individual and give them an internal ID, like `xml:id="person-kinnear"`. You record their birth date, occupation, and role in your text. In your transcript, your tag points to this internal ID: `<persName ref="#person-kinnear">Mr. Kinnear</persName>`. This keeps your edition complete and self-contained.

**Vocabulary.** *particDesc* — The TEI header element that houses a local directory of people mentioned in a document. *Local ID* — An internal xml:id used to link mentions in the text to descriptions in the header.

**Takeaway:** The particDesc element in the header lets you create a local biographical directory for people without external records.

---

## **14 Content**

**Building Your Own Map: <settingDesc> in the Header**

Just as you create a local directory of people in `<particDesc>`, you can create a local gazetteer of places in `<settingDesc>`.

Historical letters and treaties often mention local creeks, family farms, or Indigenous trails that do not appear in GeoNames. Forcing a local path into a modern city record distorts geography.

Inside `<settingDesc>`, you add a `<place>` element with a unique `xml:id`, historical notes, and geographic coordinates if known. In your transcript, you point your place tag to your local record: `<placeName ref="#place-marshalltown">Marshalltown</placeName>`. This allows your edition to record local geography with complete historical integrity.

**Vocabulary.** *settingDesc* — The TEI header element that houses a local gazetteer of places. *Local Gazetteer* — A project-specific list of place names and geographic notes.

**Takeaway:** The settingDesc element in the header houses a local gazetteer for historical places missing from modern databases.

---

## **15 Content**

**Case Study 1: Political Entities in Ace's 1791 French Decree**

Let us look at the entities in Ace's 1791 French Revolutionary decree from the *Comité des décrets* (British Library Zweig MS 169). This document was produced during a dramatic political shift: the creation of a constitutional monarchy in France.

Ace's text contains powerful political bodies. The primary group is the `<orgName ref="wikidata:Q120563">l'Assemblée nationale</orgName>` (the National Assembly). The document also mentions the `<orgName>Comité des décrets</orgName>`, the legislative committee that verified and printed parliamentary decrees.

Personal names include the constitutional king, `<persName ref="wikidata:Q7732">Louis XVI</persName>`, and administrative signers like `<persName>Dejoly</persName>`. The place of issue is `<placeName ref="geonames:2988507">Paris</placeName>`. Identifying these entities requires understanding the French state in the summer of 1791.

**Vocabulary.** *National Assembly* — The revolutionary parliamentary body of France from 1789 to 1791. *Constitutional Monarchy* — A system where a monarch rules alongside an elected parliament under a constitution.

**Takeaway:** Ace's 1791 French decree features formal revolutionary assemblies, royal figures, and administrative signers in Paris.

---

## **16 Content**

**The National Assembly and the King: Royal and Legislative Bodies**

In August 1791, power in France was split between the elected National Assembly and King Louis XVI. Decrees had to be approved by the assembly and sanctioned by the king before they became law.

When encoding these organizations, editors must distinguish between legislative bodies and the crown. The National Assembly is tagged as `<orgName>`. The king can be tagged as an individual with `<persName>` or as an office with `<roleName>le Roi</roleName>`.

Notice how the words *Nation*, *Loi*, and *Roi* frequently appear together: "la Nation, la Loi, et le Roi." An automated program might confuse these capitalized words for personal names. A human editor tags *la Loi* as a concept, *la Nation* as the body politic, and *le Roi* as the monarch.

**Vocabulary.** *Royal Sanction* — The official royal approval required to turn an assembly decree into law. *Body Politic* — The collective political body of the people or state.

**Takeaway:** Editorial judgment distinguishes royal offices and legal concepts from ordinary personal names in French administrative texts.

---

## **17 Content**

**French Authority Files: Using BnF and IdRef for Revolutionary Names**

When researching French historical figures, French national databases offer richer evidence than general English websites.

Two French registries are essential. First, the **Bibliothèque nationale de France (BnF)** maintains authoritative catalogue records for every person, printer, and institution in French history. Second, **IdRef** is the French higher education authority registry, linking researchers, deputies, and historical manuscripts.

In Ace's document, legislative deputies and minor clerks who appear only as signatures can often be found in IdRef or the BnF catalogue. Linking to BnF or IdRef alongside Wikidata provides ironclad authority evidence for French digital editions.

**Vocabulary.** *BnF* — The National Library of France, maintaining standard French authority records. *IdRef* — The French academic authority registry used by universities and research libraries.

**Takeaway:** The BnF and IdRef registries provide authoritative documentation for French historical figures and institutions.

---

## **18 Content**

**Case Study 2: Personal Names in Olyvia's 1967 Maud Lewis Letter**

Olyvia is editing a 1967 handwritten letter by Nova Scotia folk artist Maud Lewis. This witness offers a total contrast to Ace's formal political decree. It is an intimate, twentieth-century personal letter about art and daily life.

Maud Lewis lived in a tiny painted house in Marshalltown, Nova Scotia. She suffered from severe arthritis and sold painted boards from her home. Her letter to art buyer Leonard Kinnear discusses painting prices, house visits, and her husband Everett.

The entities here are personal and local: `<persName ref="wikidata:Q2302306">Maud Lewis</persName>`, her husband `<persName ref="wikidata:Q96473843">Everett Lewis</persName>`, and correspondent `<persName>Mr. Kinnear</persName>`. The geographic references point to rural Nova Scotia. Understanding these names requires attention to mid-century folk art culture.

**Vocabulary.** *Folk Artist* — An artist without formal academic training whose work reflects local community culture. *Epistolary Witness* — A handwritten letter preserved as primary historical evidence.

**Takeaway:** Olyvia's Maud Lewis letter features intimate personal names and rural Maritime locations in mid-century Nova Scotia.

---

## **19 Content**

**First Names and Nicknames: Resolving 'Everett' in Letters**

In personal letters, writers rarely use full formal names. Maud Lewis does not write "my husband Everett Lewis." She simply writes "Everett."

How should an editor encode a bare first name like "Everett"? In your TEI transcript, you must never alter the text. The tag wraps only the single word: `<persName>Everett</persName>`.

To show who "Everett" is, you use the `@ref` attribute: `<persName ref="wikidata:Q96473843">Everett</persName>`. The link connects this casual first name to the full biography of Everett Lewis. This preserves the warm, informal tone of the letter while providing full digital clarity for researchers.

**Vocabulary.** *Bare Name* — A first name or nickname used without a surname or official title. *Biographical Resolution* — Linking a casual first name to its full canonical identity via an attribute.

**Takeaway:** The ref attribute allows casual first names and nicknames in letters to resolve to complete biographical records.

---

## **20 Content**

**Maritime Places: Marshalltown, Digby, and Nova Scotia**

The geography in Maud Lewis's letter anchors her art in the rural landscape of southwestern Nova Scotia.

She writes from *Marshalltown*, located near the town of *Digby* in *Digby County*. In GeoNames, Digby has its own entry (`geonames:5938959`), and Marshalltown has a separate entry (`geonames:6066228`).

When encoding these places, an editor captures their geographic relationship:
```xml
<placeName ref="geonames:6066228">Marshalltown</placeName>,
<placeName ref="geonames:5938959">Digby</placeName>
```
Local Maritime history is essential here. Without knowing Nova Scotia geography, an automated tool might confuse Digby with Digby Island in British Columbia.

**Vocabulary.** *Toponym* — The proper name of a place or geographic feature. *Geographic Disambiguation* — Distinguishing between different towns that share the same name in different regions.

**Takeaway:** Accurate Maritime place tagging links local Nova Scotia communities to precise gazetteer coordinates.

---

## **21 Content**

**Case Study 3: Sovereign Entities in Andromeda's 1752 Treaty**

Andromeda is editing the 1752 Peace and Friendship Treaty concluded in Halifax, Nova Scotia. This diplomatic proclamation is a foundational legal pact between the British Crown and the Mi'kmaq Nation.

This document contains high-stakes political and sovereign entities. It names the British monarch, King George II, and his colonial representative, Governor Peregrine Thomas Hopson. It names the Mi'kmaw leader, Major Jean-Baptiste Cope, described as the Chief Sachem of the Chignecto tribe.

The treaty also names nations and sovereign bodies: the `<orgName>Tribe of Mickmack Indians</orgName>` and the `<orgName>His Majesty's Council</orgName>`. Editing this document requires historical precision, legal understanding, and cultural respect.

**Vocabulary.** *Peace and Friendship Treaty* — An 18th-century treaty between the British Crown and Indigenous nations in the Maritimes establishing peace and trade without ceding land. *Sovereign Entity* — A self-governing political nation or royal authority.

**Takeaway:** Andromeda's 1752 Treaty contains sovereign diplomatic entities, British officials, and Mi'kmaw national leadership.

---

## **22 Content**

**Mi'kmaw Leadership: Chief Sachem Jean-Baptiste Cope**

The central Indigenous figure in the 1752 Treaty is Major Jean-Baptiste Cope (c. 1698–c. 1760). Cope was a prominent Mi'kmaw leader from Shubenacadie who negotiated with British authorities in Halifax.

In the treaty text, his name appears with colonial titles: *Major Jean Baptiste Cope, Chief Sachem*. The title *Major* was an honorary distinction given by French authorities, while *Sachem* is an Indigenous leadership title.

In TEI, you can encode his name with granular precision or as a complete phrase:
```xml
<persName ref="dcb:cope_jean_baptiste">
  <roleName>Major</roleName>
  <forename>Jean Baptiste</forename>
  <surname>Cope</surname>
</persName>
```
His scholarly biography is published in the *Dictionary of Canadian Biography*, providing an authoritative citation link.

**Vocabulary.** *Sachem* — A traditional title for a chief or sovereign leader in eastern Indigenous nations. *Honorary Rank* — A military title granted as a diplomatic courtesy rather than an active command.

**Takeaway:** Major Jean-Baptiste Cope's title combines Mi'kmaw and European leadership roles, linking to the Dictionary of Canadian Biography.

---

## **23 Content**

**Colonial Government: Governor Peregrine Thomas Hopson**

The primary British official in the 1752 Treaty is Peregrine Thomas Hopson (1696–1759). Hopson served as Governor of Nova Scotia from 1752 to 1755, following Governor Edward Cornwallis.

Hopson pursued a deliberate policy of diplomatic reconciliation with the Mi'kmaq. His treaty guaranteed hunting and fishing rights and established a framework for regulated commerce.

In your markup, Hopson is encoded with his authority link:
```xml
<persName ref="wikidata:Q7167817">Peregrine Thomas Hopson</persName>
```
Hopson also appears in the *Dictionary of Canadian Biography*. Linking his name connects the treaty to eighteenth-century British colonial administration records.

**Vocabulary.** *Colonial Governor* — The appointed royal official representing the British Crown in a colony. *Diplomatic Reconciliation* — A formal policy aimed at resolving military conflict through legal treaties.

**Takeaway:** Governor Peregrine Thomas Hopson represented the British Crown in the 1752 negotiations, linking to colonial administrative records.

---

## **24 Content**

**Historical Toponyms: Chigabenakady and Colonial Renaming**

When editing colonial treaties, you encounter historical place names that colonial officials later altered or Anglicized.

The treaty refers to Cope's home territory as *Chigabenakady*. This is the historical English spelling of the Mi'kmaw name *Sipekne'katik*, which translates to "where the wild groundnuts grow." Today, the town is commonly spelled *Shubenacadie*.

If you link *Chigabenakady* only to the modern Canadian census town in GeoNames, you obscure its Indigenous geography. A responsible digital edition notes the ancestral territory of *Sipekne'katik* in the header or commentary:
```xml
<placeName ref="geonames:6147610">Chigabenakady</placeName>
```
Scholarly markup acknowledges original Indigenous place names rather than treating colonial spellings as the only truth.

**Vocabulary.** *Sipekne'katik* — The traditional Mi'kmaw district name meaning "place of wild groundnuts." *Anglicization* — Changing a foreign or Indigenous name to fit English spelling and pronunciation habits.

**Takeaway:** Historical treaty markup records original Indigenous place names like Chigabenakady alongside modern gazetteer coordinates.

---

## **25 Content**

**Regnal Years and Calendars: The King's Reign in Dates**

In eighteenth-century British law, dates were measured by the monarch's reign as well as the calendar year. A monarch's regnal year begins on the day they ascend the throne.

The 1752 Treaty dates its preamble "in the Twenty Sixth Year of the Reign of our Sovereign Lord George the Second." George II became king on June 11, 1727. Therefore, November 1752 fell in his twenty-sixth regnal year.

When you encode this legal date, wrap the entire phrase and calculate the true calendar date:
```xml
<date when="1752-11-22">the Twenty Sixth Year of the Reign of our Sovereign Lord George the Second</date>
```
The `@when` attribute stores the exact day in ISO 8601 format, ensuring your digital timeline remains accurate.

**Vocabulary.** *Regnal Year* — A year counted from the official accession date of a reigning monarch. *Accession* — The formal date when a monarch inherits the crown and begins their reign.

**Takeaway:** Legal regnal dates must be calculated and normalized into standard YYYY-MM-DD dates in the when attribute.

---

## **26 Content**

**Writing Your Editorial Policy: ENTITY_POLICIES.md**

Before you annotate entities in your text, you must record your editorial rules in a project policy file. You will create `ENTITY_POLICIES.md` in the root of your repository.

Your policy document must answer four concrete questions:

1. **Which authority registries govern your project?** (e.g., Wikidata and VIAF for people; GeoNames and Native Land Digital for places).
2. **What is your granularity policy?** Do you tag compound names like "Governor Hopson" as a single `<persName>`, or do you split them into `<roleName>` and `<surname>`?
3. **How do you normalize partial dates?** If a letter says "Feb 1967," do you write `when="1967-02"`?
4. **What is your verified absence procedure?** Which databases must you check before declaring a person unindexed?

Writing these rules down guarantees consistency across your entire manuscript.

**Vocabulary.** *Editorial Policy* — A written set of rules that defines how an editor makes markup and tagging decisions. *Granularity Policy* — The decision on how deeply to break names into sub-elements.

**Takeaway:** The ENTITY_POLICIES.md file records your project rules for registries, tagging depth, and date normalization.

---

## **27 Content**

**The 20-Entity Ground Truth Table**

To create your benchmark for this week's experiments, you will extract twenty entity mentions from your manuscript witness.

You will organize these twenty entities into a four-column table in your notes or policy file:

1. **Surface Mention:** The exact text as written on the historical page.
2. **Entity Class:** Person, Place, Organization, or Date.
3. **Canonical Name:** The standardized dictionary or biographical name.
4. **Authority Link:** The URI or ID from Wikidata, GeoNames, or your local header.

<table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 0.5rem; text-align: left;">Surface Mention</th>
      <th style="padding: 0.5rem; text-align: left;">Entity Class</th>
      <th style="padding: 0.5rem; text-align: left;">Canonical Name</th>
      <th style="padding: 0.5rem; text-align: left;">Authority Link (@ref)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Major Jean Baptiste Cope</td>
      <td style="padding: 0.5rem;">Person</td>
      <td style="padding: 0.5rem;">Jean-Baptiste Cope</td>
      <td style="padding: 0.5rem;"><code>dcb:cope_jean_baptiste</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">Halifax</td>
      <td style="padding: 0.5rem;">Place</td>
      <td style="padding: 0.5rem;">Halifax, Nova Scotia</td>
      <td style="padding: 0.5rem;"><code>geonames:6324729</code></td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 0.5rem;">l'Assemblée nationale</td>
      <td style="padding: 0.5rem;">Organization</td>
      <td style="padding: 0.5rem;">Assemblée nationale</td>
      <td style="padding: 0.5rem;"><code>wikidata:Q120563</code></td>
    </tr>
    <tr>
      <td style="padding: 0.5rem;">22 Novembre 1752</td>
      <td style="padding: 0.5rem;">Date</td>
      <td style="padding: 0.5rem;">1752-11-22</td>
      <td style="padding: 0.5rem;"><code>ISO-8601</code></td>
    </tr>
  </tbody>
</table>

Every entry must be checked by eye against historical sources. This table represents your ground truth.

**Vocabulary.** *Ground Truth Table* — A verified reference list of entities used to evaluate automated software predictions. *Canonical Name* — The official, standardized spelling of an entity's name.

**Takeaway:** A 20-entity table establishes the manual benchmark against which computational NER tools will be tested.

---

## **28 Content**

**Hand-Authoring ground_truth_entities_manual.xml**

Once your twenty entities are verified in your table, you will encode them into a TEI XML document named `ground_truth_entities_manual.xml`.

This file contains the continuous diplomatic transcription of your excerpt, with each entity wrapped in its appropriate tag. Every tag must include a unique `xml:id` and an authoritative `@ref` attribute.

Examine this clean model fragment:
```xml
<p>
  At <placeName xml:id="ent-01" ref="geonames:6324729">Halifax</placeName>,
  concluded with <persName xml:id="ent-02" ref="dcb:cope_jean_baptiste">Major 
  Jean Baptiste Cope</persName>, Chief Sachem of 
  <placeName xml:id="ent-03" ref="geonames:6147610">Chigabenakady</placeName>,
  this <date xml:id="ent-04" when="1752-11-22">22d Day of November 1752</date>.
</p>
```

Notice that commas and periods stay outside the tags. Keeping clean boundaries makes automated comparisons work smoothly on Wednesday.

**Vocabulary.** *Diplomatic Wrapper* — Wrapping tags around words without altering surface spelling or punctuation. *Tag Boundary* — The precise starting and ending points of an XML element in a sentence.

**Takeaway:** The manual XML file encodes your twenty verified entities in clean TEI markup with IDs and authority links.

---

## **29 Content**

**Validating Your Entity Markup in VS Code**

Before your manual ground truth can serve as an authoritative benchmark, it must pass schema validation in Visual Studio Code.

In Module 2, you set up the Red Hat XML and Scholarly XML extensions to validate files against RELAX NG schemas. Your `ground_truth_entities_manual.xml` file must validate to zero errors.

Watch out for three common mistakes:

1. **Misspelled Attributes:** Writing `href=` or `link=` instead of the TEI standard `ref=`.
2. **Invalid Dates:** Writing `when="Nov 22 1752"` instead of the required `when="1752-11-22"`.
3. **Overlapping Tags:** Putting an entity tag across paragraph or line boundaries incorrectly.

Open the Problems panel in VS Code (`Ctrl+Shift+M`) to confirm that your file shows zero errors.

**Vocabulary.** *Schema Validation* — Checking that an XML file follows all the structural rules of a schema. *Problems Panel* — The VS Code view that displays syntax and schema errors.

**Takeaway:** Schema validation confirms that your entity markup conforms strictly to TEI P5 guidelines with zero errors.

---

## **30 Content**

**The Stage Gate: Committing Your Manual Entity Baseline**

You have reached the finish line for Step 1 of Module 9. Today, you established a rigorous manual baseline for historical named entities.

You documented your editorial rules in `ENTITY_POLICIES.md`. You researched twenty historical people, places, organizations, and dates in your project witness. You linked them to Wikidata, GeoNames, or your local header. You encoded them in schema-valid TEI XML.

Before leaving class today, stage and commit your deliverables to your git repository:
```bash
git add ENTITY_POLICIES.md ground_truth_entities_manual.xml
git commit -m "Week 9 Step 1: establish manual named entity ground truth and authority links"
```

On Wednesday, in Lesson 9.2, you will run an automated natural language processing tool over this same passage to measure how well computers identify historical entities.

**Vocabulary.** *Stage Gate* — A required project milestone that must be completed and committed before moving forward. *Git Baseline* — A committed set of files used as the foundation for future testing.

**Takeaway:** Committing your entity policy and manual XML completes Step 1 and sets up Wednesday's automated NER tests.

---
