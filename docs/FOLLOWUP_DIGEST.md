# Follow-up digest: Shiloh, the gate, canes, Jerusalem, tents, and the history of the blind

Written 3 October 2026, after Brian's second round of questions. It goes with `data/reference/followup_candidates.json`, which is built by `src/build_followup_candidates.py` (that script refuses to write a quote it cannot find in the shelf) and checked by `tests/test_followup_candidates.py`.

Counts: 68 items across 7 keys (`eli-duties` 10, `ahijah-duties` 9, `gate-life` 10, `canes-and-staffs` 10, `jerusalem-layout` 10, `tent-life` 10, `history-of-the-blind` 9). Every item has a plain statement of what the shelf says, a citation, one or more verbatim quotes with file and character offset (line endings as LF), a confidence of `high` or `medium`, and a `caution`. The test checks that each quote is in its file at its offset. It does not check that the paragraph is a fair reading of the quote, and nothing here has been seen by Brian or by a second reader. Read the cautions before using an item. Nothing in the JSON comes from outside the shelf.

How to find an item: this digest cites them as `key[n]` (n counts from 0, in the order of the JSON). Wikipedia quotes are raw wikitext, so links and templates show (for example `{{convert|15|m|ft}}` means 15 metres); the text field of each item says what the numbers are.

## What was added to the shelf for this pass

Seven requests (the log now holds 42 in all; the cap is 60), one per second, with the standard User-Agent. archive.org was already in the host list in `tests/test_shelf.py`, so that test file was not changed; sacred-texts.com was not needed.

- James Wilson, *Biography of the Blind* (4th edition, Birmingham, 1838), from the Internet Archive scan (`biographyofblind00wilsuoft`). Public domain by date. Wilson was blind from infancy (his title page says so), which makes this the only first-person blind voice on the shelf, from 1838.
- W. H. Levy, *Blindness and the Blind: or, A Treatise on the Science of Typhlology* (London, 1872), from the Internet Archive (`blindnessblindor00levyiala`). Public domain by date. Chosen with Wilson as the brief preferred; Pierre Villey's *The World of the Blind* (US 1930) was not taken because publication in 1930 makes its status for the shelf less clear than a plain pre-1930 date, and Howe's reports were not looked for.
- 31 Wikipedia articles (CC BY-SA 4.0, revision ids in `SOURCE.md`): White cane, Walking stick, Staff of office, Tyropoeon Valley, Kohen, Hebrew Bible judges, Prophets in Judaism, Visual impairment, Didymus the Blind, Blind musicians, Eli (biblical figure), Ahijah the Shilonite, Trachoma, Tent, Bedouin, Nomadic pastoralism, Guide dog, Tiresias, Homer, Jerusalem, Louis Braille, Valentin Haüy, Temple Mount, Western Wall, Siege of Jerusalem (70 CE), Robinson's Arch, Stepped street (Jerusalem), Huldah Gates, Book of Tobit, Antonia Fortress, Sheep Gate. Three further API response files (`wikipedia_batch3.json` to `batch5.json`) are listed too.
- Not found as Wikipedia titles: 'Education of the blind', 'History of blindness', 'Judge (biblical)', 'Herodian Jerusalem', 'Jerusalem in the Second Temple period', 'Pilgrim Road (Jerusalem)', 'Stoa of Herod', 'Disability in the ancient world', 'Quinze-Vingts Hospital'. 'Stepped Street (Jerusalem)' only worked in the lower case form 'Stepped street (Jerusalem)'. 'Wilson's Arch' redirected to an unrelated article on a Utah rock arch (it is in the JSON response only; it was not kept as a text file).
- Not obtained: Villey, Howe, the Mishnah and Talmud (no public-domain copy was on the allowed hosts in 2-3 requests), the Jewish Encyclopedia, Easton's or Smith's entries for 'Staff', 'Rod', 'Nomad' and 'Ophthalmia' (they have none; the ISBE has 'Staff', 'Rod' and 'Disease' and those were used). The 'Walking stick' and 'Staff of office' Wikipedia articles were read and have nothing on the Bible or the ancient world, so no item uses them.
- All the new shelf files are in the index (`data/reference/shelf_index.csv`, now 4,897 rows). The index has no real locators for Wilson and Levy because they have no chapter markers the indexer reads; their labels say so.

## Brian's questions and where the answers are

1. Shiloh (priest and judge Eli; prophet Ahijah): `eli-duties`, `ahijah-duties`.
2. The walled town and its gate: `gate-life`.
3. First-century Jerusalem, canes and staffs: `canes-and-staffs`, `jerusalem-layout`.
4. Life in tents: `tent-life`.
5. History of the blind beyond the Bible: `history-of-the-blind` (plus the guide and staff material in `canes-and-staffs`).

## 1. Shiloh: what Eli and Ahijah did

### Coverage

`eli-duties` is the better covered. The shelf has four dictionary entries that agree on Eli's offices (Easton, Smith's, ISBE, and the Smith's 'Priest' duties list), a long run of Matthew Henry on 1 Samuel 1 to 4 and Leviticus 13, the ISBE on the judge's work, and short Wikipedia summaries. `ahijah-duties` has less: the two verses (1 Kings 14:4-6) as printed in Henry, one sentence in the ISBE that calls him 'the blind old prophet', Henry on the passage, and general accounts of the prophet's office (Easton, Smith's). Nothing on the shelf describes a day in Ahijah's life or says who looked after him.

### Eli: the offices

Eli is high priest at Shiloh and also judge (`eli-duties[0]`, `[1]`). Easton says he 'judged Israel for forty years'; the ISBE says it was the first time the two offices were combined in one person (that is one writer's claim and the other works do not repeat it). Easton, in its entry on judges, says the judgeship came to him 'ex officio'.

### Eli: the things a priest did, from the sources

Smith's 'Priest' entry (`eli-duties[2]`): keep the altar fire burning day and night; feed the golden lamp with oil; offer the morning and evening sacrifices at the door of the tabernacle; teach the statutes; act as a court of appeal in difficult cases (Deuteronomy 17:8-13). Smith's does not say which of these Eli did himself. Henry adds that 'the judge' in Deuteronomy 17:9 is the priest (`eli-duties[4]`) and that Eli 'sat to receive addresses and give direction' by a post of the temple (`eli-duties[3]`). The ISBE on the judge's work (`eli-duties[8]`): the court was open, each party presented his own view, and the only evidence was what the witnesses said.

Henry on 1 Samuel 3 (`eli-duties[6]`) pictures Samuel as having waited on Eli to his bed, and Eli, who did not hear the voice himself, giving Samuel the words to answer. Henry on 1 Samuel 4 (`eli-duties[7]`) has Eli 'old, and blind, and heavy', placing himself by the wayside to wait for news; the verses have him hear the noise of the crying, ask what it meant, and be told by a messenger who had first told the city. Easton (`eli-duties[0]`) puts the seat 'outside the gate of the sanctuary by the wayside'.

### Which duties sight carried (an analysis of the sources, not a finding)

This section is written to help Brian think through each task. It is my sorting of the evidence, not something the sources say, and the conclusions are his.

Duties that the sources tie to looking:

- The skin-disease inspections of Leviticus 13: the priest 'shall look on' the sore, again at seven days, and 'pronounce' (`eli-duties[5]`). Henry reports a Jewish rule that a priest who was disabled from the sanctuary by a blemish could still judge the disease 'provided the blemish were not in his eye', and that the priest could take a common person to assist him in the search, 'but the priest only must pronounce the judgment'. That is the only place on the shelf where the work of assisting eyes is described. Its source and date are not given ('All the Jews say').
- Reading a person who is praying without sound: Eli 'marked her mouth' (Hannah) and misjudged her (`eli-duties[3]`).
- Watching for news: Eli sat by the road and gate (`eli-duties[7]`).
- Easton's gloss of Eli's eyes as 'stiffened' (`eli-duties[0]`). Henry also says the Jewish tradition had a 'sagan' or deputy who viewed sacrifices for blemish (see the Henry note on Leviticus 22, on sacrifices without blemish, offset 3063215 in `matthew_henry_vol1_genesis_to_deuteronomy.txt`; not in the JSON, and Henry gives it only as what 'the Jews say').

Duties that, in the sources, run on speech, hearing, memory or presence:

- Teaching the statutes, blessing, giving direction to those who come (Smith's; Henry).
- Hearing a case: the parties speak and the witnesses give evidence (ISBE 'Judge').
- Instructing Samuel in how to answer the voice (Henry).
- Offering the sacrifices and tending the fire and lamp (Smith's; whether this is hand-and-memory work or needed seeing is not discussed).

Where a helper appears in the text: Samuel waits on Eli (1 Samuel 3, in Henry's picture); the 'common person' of the Jewish rule above; the priests' servant with the flesh-hook in 1 Samuel 2:13-14 (a description of the sons' abuse, not Eli's duty, and not in the JSON).

Questions that the shelf cannot answer and that Brian may want to answer for himself: How would you recognise a particular worshipper? How would you know the lamp was out or the altar fire low? How would you tell who spoke in a crowded gate? Which of these would you give to an assistant, and which would you keep for yourself? The sources offer one model (assistance in the search, judgment kept by the priest); they do not offer a second.

What the shelf does not say: whether a blind priest could serve at the altar (the law of Leviticus 21:18 and the ISBE and Henry on it are in `law_and_life_candidates.json`, key `law-priest`; Eli is not said to have been removed for his eyes); whether Eli's dimness of sight began before or after he became judge; and what the 'temple' at Shiloh looked like inside (the ISBE says the sanctuary there is called a 'temple' with doorpost and doors, 'a more durable structure than the old tent'; its scan is too garbled to quote).

### Ahijah: what the prophet did

The ISBE, in 'Shiloh', calls him 'the blind old prophet' and, in 'Ahijah', says the narrative gives the impression of 'a very old man' (`ahijah-duties[0]`). The verses (1 Kings 14:4-6, as printed in Henry; `ahijah-duties[1]`): 'Ahijah could not see; for his eyes were set by reason of his age', and when he 'heard the sound of her feet, as she came in at the door' he called Jeroboam's wife by name and asked why she pretended. The text also says the Lord had told him she was coming (Henry stresses that, `ahijah-duties[3]`).

What he did as a prophet, from the sources: delivered a message to Jeroboam on the road by an acted sign, tearing a new garment into twelve pieces (1 Kings 11:29-31; Henry, `ahijah-duties[4]`); received a visitor with a gift, which prophets 'accepted, and yet were no hirelings' (Henry, `[3]`); delivered a judgment on the king's house; and, according to 2 Chronicles as summarised by Wikipedia, wrote a book on Solomon's reign (`[8]`). Easton: the great task of a prophet was 'to correct moral and religious abuses'; foretelling was 'only an incidental part' (`[6]`). Prophets spoke at gates and in public places (Easton, Henry, `[7]`).

Henry's comment that such visions 'need not bodily eyes, but are rather favoured by the want of them' (`[2]`) is a devotional opinion; it can sound like romanticising blindness and is offered only as how one commentator read the verse.

Which of the prophet's tasks would blindness have changed? The two he is shown doing in old age, receiving a visitor and speaking a message, are hearing-and-speaking tasks. The earlier sign with the torn garment is a seeing-and-touching task (he is not described as blind then). The writing of a book, if he wrote it, would have needed an amanuensis; the shelf does not say. As with Eli, this is a sorting of the evidence and not a finding.

## 2. The walled town and its gate

### Coverage

Good. Smith's, Easton's, the ISBE and Edersheim give the structure; Henry gives specific scenes (Ruth 4, 2 Samuel 18, 2 Kings 7, 1 Samuel 4, Amos 5). Henry's comment on Deuteronomy 21 and 22 prints the verses (elders and the gate) but adds nothing about the gate itself. The Wikipedia 'City gate' article was already on the shelf and is general.

### The picture, activity by activity

The approach (`gate-life[0]`, `[3]`): Edersheim describes a low wall and a ditch, then the wall proper and 'a massive gate, often covered with iron, and secured by strong bars and bolts', with a watch-tower above. The ISBE adds pivoting doors, a bar fitting into clamps in the post, a defending tower, sometimes an inner gate. Smith's says the gate had chambers over it.

The gatekeeper and the watchman (`gate-life[6]`): Easton's 'porter' is a gate-keeper (and the Levites' temple porters were 4,000 in number under David). In 2 Samuel 18:24-27 David sits 'between the two gates'; the watchman on the roof sees and announces runners and 'called unto the porter'; he recognised the first runner by his running. The ISBE (entry 'Watchman', not an item) says sentinels stood on the walls and also 'watchmen that go about the city', pointing to some kind of municipal police.

The elders and the court (`gate-life[7]`, `[4]`): Easton says 'judges of the gate' were a recognised phrase, that courts of justice were frequently held at the gates, and that elders 'appear as governors... local magistrates, administering justice'. Henry on Ruth 4: Boaz goes up to the gate, perhaps as 'father of the city' who 'sat chief'; he gathers ten elders (a 'town-hall over the gate'); the matter is stated and a sandal is passed to confirm the sale. Smith's lists public deliberation, justice, and audience for kings among the gate's uses.

Who sat where (`gate-life[5]`, `[4]`): Job 29:7-8 (in the passage where Job calls himself 'eyes to the blind'): he 'prepared my seat in the street'; young men saw him and hid, the aged 'arose, and stood up'. Henry's Ruth reading has Boaz sitting 'chief'. Edersheim says 'within the gate' was the sheltered place where the elders sat. The kings of Israel and Judah sat 'in their robes and chairs of state, in the gate of Samaria' to hear Micaiah (Henry on 1 Kings 22, in `ahijah-duties[7]`).

Trade and news (`gate-life[1]`, `[8]`): Edersheim's squares behind the gate: country people hawking, foreign merchants and pedlars, and the idle and busy crowd 'chattering, chaffing, good-humoured'; streets named after trades; workmen sitting outside their shops 'and exchanging greetings or banter'. Smith's and Easton: markets at the gate; Henry on 2 Kings 7 explains Elisha's promise as the market being held at the gate again. News: 'the noise of the crying' reaches Eli (1 Samuel 4), and runners are seen and named from the gate roof (2 Samuel 18).

Punishment and injustice (`gate-life[7]`, `[9]`): Easton, 'criminals were punished without the gates'. Henry on Amos 5:10-12: 'they turn aside the poor in the gate, in the courts of justice, from their right'.

Closing at night (`gate-life[2]`, `[3]`): Smith's, the gates were 'carefully guarded, and closed at nightfall'. The shelf gives no account of the hour, who closed it, or what a latecomer did.

### What remains unknown for the gate

The hours; tolls or tax at the gate in the time of the judges (Edersheim's tax-gatherer belongs to the Roman period); the number of guards; how noisy it was (the shelf has crowd descriptions but no measure); whether the gate area was paved; whether beggars (and blind beggars) sat there in Israelite times (the law-and-life candidates have the later evidence). Edersheim's town is a composite of rabbinic and biblical sources, from different centuries, and Brian should not take it as a description of any one town.

## 3. Canes, staffs and guides

### Coverage

Thin for the Bible and the ancient world, and honest about it. There is no verse on the shelf in which a blind person carries a staff. There is no source on the shelf that says what blind people in first-century Jerusalem used. What exists is a ring of indirect evidence, set out below.

### What the shelf does show

- **Guides by the hand in the Bible** (`canes-and-staffs[8]`): Samson 'said unto the lad that held him by the hand, Suffer me that I may feel the pillars' (Judges 16:26); of Elymas, 'he went about seeking some to lead him by the hand' (Acts 13:11); Saul was led by the hand into Damascus (Acts 9, in Henry); Jesus 'took the blind man by the hand, and led him out of the town' (Mark 8:23). Note that Samson's lad (a boy, 'the lad') is the nearest thing to a described blind-person's guide.
- **Staffs in Scripture** (`canes-and-staffs[7]`): ordinary equipment for travel and for old age: Jacob, 'with my staff I passed over this Jordan'; the Passover eaten with 'your staff in your hand'; Zechariah 8:4, old men in Jerusalem's streets 'with his staff in his hand for very age'. The ISBE says Hebrew has several words for 'rod' and 'staff' (the shepherd's rod and staff of Psalm 23).
- **A rule about staffs at the Temple** (`canes-and-staffs[5]`): Edersheim, citing the rabbis, says one must not enter the Temple carrying a staff, nor with shoes, nor with dust on the feet, nor with scrip or purse, and that Jesus's instruction to the Twelve corresponds to it. This is the single most useful finding for Brian's question and it is a rule for everyone: the shelf says nothing about a blind person's exemption, so none is claimed. How a blind pilgrim reached the court is unanswered.
- **Support on the Sabbath** (`canes-and-staffs[6]`): Edersheim from the Mishnah: it 'was also allowed to go about on crutches, or with a wooden leg'. Canes for the blind are not mentioned; whether a blind person's staff counted as dress or as a burden is not answered. Edersheim also says a staff might have 'a secret receptacle' at the top to hold valuables or water.
- **Greek tradition** (`canes-and-staffs[0]`): in the myth of Tiresias (via Pseudo-Apollodorus, 'Bibliotheca', as Wikipedia reports) Athena gives him a cornel-wood staff 'wherewith he walked like those who see'. It is a myth, and Greek, but it is the earliest explicit staff-for-a-blind-person on the shelf, and Levy reads it as showing that the ancients noticed blind people walking alone with a stick.
- **A dog** (`history-of-the-blind[5]`, `[6]`): the Herculaneum wall painting (buried in 79 CE) shows 'a blind-man being guided by his dog', as Wikipedia's 'Guide dog' reports with a reservation that more evidence would be needed. Tobit's dog travels with Tobias, but Tobit is at home.
- **Later accounts of how a staff is used** (`canes-and-staffs[2]`, `[3]`, `[4]`): Levy (1872) on technique (the stick 'waved alternately from right to left to correspond with the movements of the feet', steps 'gauged with the stick'), and James Wilson (1838), blind from infancy, on his own habits: he drifts to the hand that holds the staff on unfamiliar roads, found the edge of a well with it, and used it to find stepping stones. These are not evidence about the first century, but they describe what a staff does, which Brian can compare with his own long cane.
- **The white cane** (`canes-and-staffs[9]`): the modern white cane dates from 1921 (Biggs), 1930 (Peoria), 1931 (France), 1944 (Hoover's technique). Wikipedia says 'blind people have used canes as mobility tools for centuries' and cites a page on the history of orientation and mobility as a profession; it gives no date or place.
- **The law** (cross-reference): Leviticus 19:14 and Deuteronomy 27:18 (a stumbling-block before the blind; making the blind wander out of the way) assume that blind people travelled and could be misled. The candidates for those verses are in `law_and_life_candidates.json`.

### The frank answer to 'did they use canes?'

The shelf does not show either way for first-century Jerusalem. Guides by the hand are in the text. Staffs are ordinary equipment in the text and the Temple rule (for everyone) restricts them. A blind person's staff is in Greek myth. The 19th-century sources show it as a normal tool then. A reader may reasonably think a staff was one tool among others (a guide, a wall, a companion's arm, memory of a route), but that is an inference, and it is Brian's to make.

## 4. First-century Jerusalem: the layout

### Coverage

Good for the shape and the dimensions; patchy on the dates; nothing on how blind people got about (see `history-of-the-blind` and `canes-and-staffs`). Josephus, Edersheim and the dictionaries give the old picture; Wikipedia's recent articles on the stepped street, Robinson's Arch and the Pool of Siloam give the excavated picture.

### The picture, with the numbers the sources give

- **Two hills and a valley** (`jerusalem-layout[0]`, Josephus *Wars* V.4.1): the upper city on a higher hill, the lower city on 'Acra', and a valley between them 'at which valley the corresponding rows of houses on both hills end'. The Valley of the Cheesemongers 'extended as far as Siloam'. The Hasmoneans filled up part of the second valley and lowered Acra so the Temple would be higher.
- **The Tyropoeon** (`jerusalem-layout[3]`): Easton, a ravine now filled with rubbish and once 'spanned by bridges, the most noted of which was Zion Bridge'; the western wall of the Temple platform rose 'from the bottom of this valley to the height of 84 feet'.
- **A road across it** (`jerusalem-layout[1]`, Josephus *Antiquities* XV.11.5): on the west side of the Temple, four gates: one led 'to a passage over the intermediate valley' (the king's palace), two to the suburbs, one to 'the other city, where the road descended down into the valley by a great number of steps, and thence up again by the ascent'. The south cloister stood over a valley so deep that a person looking down 'would be giddy'.
- **The stepped street** (`jerusalem-layout[4]`, Wikipedia): from Jerusalem's southern gates and the Pool of Siloam up to the Temple Mount's south-west corner; 8 metres wide; 600 metres long; paved 'in the pattern of two steps followed by a long landing, followed by two more steps and another landing'. Dated by coins to 30-31 CE at the earliest ('built at the earliest during the 30s CE'). A drain runs under it.
- **The way up from Siloam** (`jerusalem-layout[5]`, Wikipedia): the pool is the lowest place in the historic city (about 625 m above sea level); the ascent to the Temple Mount is 115 m in about 634 m (about 18 per cent, my arithmetic; roughly a rise of 1 in 5.5). The pool found in the recent excavations was about 225 feet wide with steps on at least three sides, in 'three sets of five steps' with platforms. An older excavation found a stairway of 34 rock-hewn steps to the west of the (later) pool, tapering in width from 27 to 22 feet. The smaller Byzantine pool, which dictionaries (Easton gives 53 by 18 by 19 feet) described as the New Testament pool, 'was wrongly thought' to be it until the Second Temple pool was found.
- **Robinson's Arch** (`jerusalem-layout[6]`, Wikipedia): 'a monumental staircase carried by an unusually wide stone arch' at the south-west corner; 15 m span, 15.2 m wide, about 17 m above the street below, the stair more than 35 m long; it 'carried traffic up from ancient Jerusalem's Lower Market area and over the Tyropoeon street to the Royal Stoa'; the width 'approximates that of a modern four-lane highway'. The article reports that it may not have been finished until some 20 years after Herod's death.
- **Streets and stairs** (`jerusalem-layout[7]`, ISBE 1915): 'houses terraced on steep slopes with stairways for streets' ('as it does today', i.e. 1915, so inferred for earlier times); a 'great main street running down the Tyropoeon' with a rock-cut drain beneath it; the approach to the Virgin's Spring is down two flights of 10 and 14 steps.
- **The sound and feel of the business quarter** (`jerusalem-layout[8]`, Edersheim): 'the same narrow streets' in the business quarters; craftsmen at work outside their shops (the shoemaker 'hammering his sandals', the tailor 'plying his needle', carpenters, workers in iron and brass); the Lower City as 'the business-quarter with its markets, bazaars, and streets of trades and guilds'; the Upper City of palaces; about 300 acres in all.
- **The Temple Mount and its approaches** (`jerusalem-layout[9]`, Wikipedia; `[2]`, Josephus *Wars* V.5): a platform measuring 488 m (west), 470 m (east), 315 m (north) and 280 m (south); the Huldah Gates on the south reached the esplanade 'by means of underground vaulted ramps'. Josephus: a stone partition three cubits high with warning inscriptions; the second court reached 'by fourteen steps from the first court' (he says thirteen a few lines later); further flights of five steps to the gates; fifteen steps to the great eastern gate; twelve steps to the holy house; the outer cloisters thirty cubits broad.

### Cautions that matter for this picture

- The stepped street is dated to the 30s CE at the earliest. The man born blind of John 9 was sent to Siloam; whether this street existed then is uncertain. The pool Brian will see on a modern map may be the smaller later one.
- Josephus's numbers (cubits, steps) come in Whiston's 1737 translation, with an internal inconsistency on the number of steps (fourteen and thirteen). The shelf does not define his cubit.
- Wikipedia's articles on the stepped street and Pool of Siloam are partly about modern excavation politics and archaeological disputes; they are not repeated here.
- None of these sources describes how blind people crossed this ground, how the steps were marked, or what the pavement felt like underfoot.

## 5. Life in tents

### Coverage

Describes the tent and the camp well (the ISBE 'Tent', Easton, Wikipedia 'Bedouin'). Says very little about people with disabilities in a camp, and nothing on a blind person's day in one. Eye disease and dust are covered by general sources and by Levy.

### The picture

- **The tent** (`tent-life[0]`, `[1]`, ISBE vol 5): black goats'-hair cloth sewed into one piece; poles 'at intervals'; ropes of goats' hair or hemp fastened to hard-wood pins driven into the ground; a mallet for the pegs 'part of the regular camp equipment'; the door a corner of matting turned back; in summer the walls mostly removed; floors of mats and rugs; food in bags and skins; copper cooking vessels and a coffee set; the women pitch the tents; a sheikh has several tents (one for guests, others for the women and servants and for the animals).
- **Inside** (`tent-life[2]`, Wikipedia 'Bedouin'): black goat-hair tents 'divided by cloth curtains into rug-floor areas for males, family and cooking'; travel 'in groups of fifty to a hundred' (a 20th-century Arabian account); the Bedouin ethos of hospitality.
- **Scale** (`tent-life[3]`, Easton): the patriarchs were 'dwellers in tents'; all Israel dwelt in tents in the wilderness; the camp 'about 3 square miles' (Easton's own estimate from Numbers 2).
- **Heat** (`tent-life[4]`, Henry on Genesis 18:1): Abraham 'sat in the tent-door, in the heat of the day', to give hospitality to travellers.
- **Eye disease** (`tent-life[5]`, `[6]`, `[8]`): the ISBE says the diseases of the Bible 'are those that still prevail' and lists 'ophthalmia and skin diseases' among the commonest; Smith's says flies are 'the great instrument of spreading the well-known ophthalmia' in Egypt; Wikipedia 'Trachoma' (modern medicine) says it spreads 'through clothing or flies', with crowding and poor water increasing the spread, and that repeated infection causes the blinding form. Levy (1872) names sandy country, sun and weather, and a particular fly in Arabia, and gives his own estimate of the blind of Arabia as one in 400, from travellers' remarks, not a count.
- **Dust and sand** (`tent-life[7]`): Easton, 'storms of sand and dust sometimes overtake Eastern travellers'; Smith's on the sandstorm and the Khamaseen wind. Neither entry mentions eyes.
- **A story** (`tent-life[9]`): a blind guide who led merchants across desert by smell, from Leo Africanus via Casaubon (1656) via Levy. It is a traveller's tale at third hand and is flagged as such.

### What remains unknown for the camp

How a blind person was cared for in a camp; whether the work of a camp (pegs, guy-ropes, poles, moving camp every few weeks) was shared out or withheld; where the person slept or sat; what a person who could not follow the herds did all day. These are the things Brian's question asks, and nothing on the shelf answers them. Isaac in Genesis 27 is the one blind person on the shelf who lives in a patriarchal household, the kind of life the tent entries describe; there he receives his sons, speaks, touches and smells. The relevant items are in `law_and_life_candidates.json` under `life-camp`.

## 6. The history of life as a blind person, beyond the Bible

### Coverage

The shelf now has two public-domain books about blind people written in the 19th century (Wilson, Levy), several Wikipedia articles, and the ISBE's 'Blindness' and 'Begging' entries (already used in the law-and-life candidates). That is a thin, mostly European and mostly 19th-century base. It has almost nothing for the ancient world beyond Greek myth, the Herculaneum painting, Didymus and the Homer tradition. The modern works below would do more.

### What is in the JSON

- Wilson (`history-of-the-blind[0]`, `[1]`): a blind man's 1838 collection of lives of 'distinguished' blind people, with a purpose of 'rescuing my fellow sufferers from the neglect and obscurity'. It includes Homer, Didymus of Alexandria, and Metcalf the road builder.
- Didymus the Blind (`[2]`): a teacher in Alexandria, died 398, blind from the age of four (Wikipedia) or five (Wilson, on Jerome's report), 'excelled in scholarship because of his incredible memory'.
- Levy on institutions (`[3]`): the Quinze-Vingts founded by Louis IX in 1260 for 300 blind persons; blind men begging with the cry 'Sainte terre'.
- Haüy (`[4]`): the first school for the blind, Paris, 1785; Braille entered it in 1819.
- Guides and companions in antiquity (`[5]`, `[6]`): Oedipus 'led and supported by his daughter Antigone'; the Herculaneum wall painting; Tobit's household. Not evidence of how most blind people lived.
- Levy on whole societies (`[7]`): his sketches of Persia and France in the 1870s; second-hand and generalising.
- The image of the blind musician (`[8]`): the Homer tradition 'whose basis in truth is uncertain'; blind musicians' contributions.

### What this adds to Brian's picture

The most useful general point the shelf supports is that expectations of blind people differed from place to place even in the 1870s (Levy's Persia and France), so the first century probably was not uniform either. That is an inference. The other is Wilson's own existence as evidence: a blind man who researched, compiled and published in 1820 and 1838, who also tells (`canes-and-staffs[3]`, `[4]`) how he moved about with a staff.

## What remains unknown (a frank list)

- Whether any blind person in the Bible or in first-century Judea is shown with a cane or staff. None is on the shelf.
- Whether the Temple rule against carrying a staff applied to a blind person, and how a blind pilgrim went up. The shelf has the rule, not the exception.
- How Eli and Ahijah managed their duties in old age; who helped them; whether they had assistants who read or spoke for them. The shelf only has the verses, and Henry's pictures of them.
- How blind people were treated in a nomadic camp, and what they did all day.
- The ancient gate's routine, hours, guard rota and noise.
- Whether the stepped street existed when the man born blind went to Siloam, and which pool he used.
- How accurate Josephus's step counts and cubits are, and what the Temple approaches felt like underfoot.
- Anything on blind people in Egypt, Mesopotamia and Greece beyond myth and the few lives above. The shelf's coverage of non-biblical antiquity is nearly empty.
- Anything on blind women, blind children or blind labourers: Wilson and the dictionaries are mostly about men of note or beggars.
- The modern research literature on disability in the ancient world, which would answer several of these questions (the books below).

## Language flagged, not reproduced

- Henry says Eli's dim eyes were 'an affliction which came justly upon him' for his sons' faults (1 Samuel 3). This links blindness to sin; it is not quoted (the same flag is in `LAW_AND_LIFE_DIGEST.md`).
- Henry's remark that Ahijah's visions are 'favoured by the want of' bodily eyes (`ahijah-duties[2]`) is quoted with a caution; it can read as romanticising.
- Henry on Leviticus 13 calls lepers 'stigmatized by the justice of God'; not quoted.
- Levy (1872) has passages with patronising language about the blind and about particular nations, and a long section on blinding as a punishment with graphic detail; none is quoted. His comment on 'shallow philanthropists' who would keep the blind from walking alone is dismissive in tone and is not reproduced, though the point it makes (that blind people should be able to walk alone) is paraphrased.
- Wilson (1838) writes with admiration for 'distinguished' blind people and in a providential frame ('an all-directing Providence'); the quotations used are his practical accounts, kept in his own voice.
- Edersheim's description of the gate crowd includes colourful and prejudiced words about a Pharisee, an Essene and a publican; only the neutral sentences are used.
- The Valentin Haüy item records that blind people were mocked at a street festival; the quotation is there to explain the school's founding.
- Wikipedia's 'Tiresias', 'Book of Tobit' and 'Guide dog' articles have material about blinding as divine punishment; only the staff, the dog and the dependence on others are used.

## Modern works Brian could consult

From my general knowledge, not from the shelf and not checked against any library catalogue: titles, authors and years may be slightly wrong, and I have not read most of them. Treat every line as unverified until Brian or a librarian has confirmed it.

Disability and blindness in the Bible and the ancient world:
- Saul M. Olyan, *Disability in the Hebrew Bible: Interpreting Mental and Physical Differences* (2008). Covers Leviticus 21 and the status of blind and lame people.
- Hector Avalos, Sarah J. Melcher and Jeremy Schipper (eds.), *This Abled Body: Rethinking Disabilities in Biblical Studies* (2007).
- Candida R. Moss and Jeremy Schipper (eds.), *Disability Studies and Biblical Literature* (2011).
- Jeremy Schipper, *Disability Studies and the Hebrew Bible: Figuring Mephibosheth in the David Story* (2006).
- Martha L. Rose, *The Staff of Oedipus: Transforming Disability in Ancient Greece* (2003). Relevant to the staff.
- Robert Garland, *The Eye of the Beholder: Deformity and Disability in the Graeco-Roman World* (1995).
- Christian Laes (ed.), *Disability in Antiquity* (2017), and Laes's *Disabilities and the Disabled in the Roman World* (2018).
- Moshe Barasch, *Blindness: The History of a Mental Image in Western Thought* (2001).
- Edward Wheatley, *Stumbling Blocks Before the Blind: Medieval Constructions of a Disability* (2010).
- Zina Weygand, *The Blind in French Society from the Middle Ages to the Century of Louis Braille* (English translation 2009).
- Frances A. Koestler, *The Unseen Minority: A Social History of Blindness in the United States* (1976). The cane and orientation-and-mobility history cited by the Wikipedia white cane article draws on it.

Daily life, the gate, the town and the tent:
- Philip J. King and Lawrence E. Stager, *Life in Biblical Israel* (2001).
- Oded Borowski, *Daily Life in Biblical Times* (2003).
- Roland de Vaux, *Ancient Israel: Its Life and Institutions* (English translation 1961).
- Ze'ev Herzog, *Archaeology of the City: Urban Planning in Ancient Israel and Its Social Implications* (1997).
- Kenneth E. Bailey, *Poet and Peasant* and *Through Peasant Eyes* (1976, 1980), on Middle Eastern village and household culture behind the parables.

Jerusalem:
- Joachim Jeremias, *Jerusalem in the Time of Jesus* (English translation 1969).
- Leen Ritmeyer, *The Quest: Revealing the Temple Mount in Jerusalem* (2006).
- Dan Bahat, *The Illustrated Atlas of Jerusalem* (1990, English edition 1996).
- Ronny Reich, *Excavating the City of David: Where Jerusalem's History Began* (2011), by the excavator of the stepped street and the Siloam pool.
- Jerome Murphy-O'Connor, *The Holy Land: An Oxford Archaeological Guide* (the Wikipedia article on the Huldah Gates cites it).

Samuel, Kings, priesthood and prophecy:
- P. Kyle McCarter, *I Samuel* (Anchor Bible, 1980).
- Ralph W. Klein, *1 Samuel* (Word Biblical Commentary, 1983).
- Robert Alter, *The David Story* (1999), translation with notes on 1 and 2 Samuel.
- Jacob Milgrom, *Leviticus 1-16* (1991) and *Leviticus 17-22* (2000), Anchor Bible; on the skin-disease inspections and the blemish rules.
- Joseph Blenkinsopp, *A History of Prophecy in Israel* (1983); Lester L. Grabbe, *Priests, Prophets, Diviners, Sages* (1995).

First-person accounts by blind authors (any period after the 1960s):
- Jacques Lusseyran, *And There Was Light* (English translation 1963), a memoir.
- John M. Hull, *Touching the Rock: An Experience of Blindness* (1990).
- Georgina Kleege, *Sight Unseen* (1999).
- Rod Michalko, *The Mystery of the Eye and the Shadow of Blindness* (1998).

## Method and checks

- Each item's quotes were written from the shelf and located by `src/build_followup_candidates.py`, which stops if a quote is not found. Where a source breaks a word across a line (OCR text) the quote keeps the break ('fast- ened' appears in the scan; the quotes avoid splitting a word where possible).
- `tests/test_followup_candidates.py` checks structure, that all seven keys are present with 4 to 10 items, that each quote is in its file within 2,000 characters of its offset and starts at the offset, that Wikipedia items name their revision date and licence, that the new shelf files are in `SOURCE.md` and the index, and that this digest carries its required sections.
- The old Wikipedia files and the shelf index were not changed except for the entries listed above; `src/build_shelf_index.py` was re-run after adding the new works to `WORKS`.
